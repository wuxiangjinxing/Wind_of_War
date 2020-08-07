from module_troops import *
from module_items import  *
from module_factions import  *
from ID_factions import  *
from process_common import  *
import re


keep_old_faction=0


def list2string(lst):
  out_str="["
  for item in lst:
    out_str=out_str+item+","
  out_str=re.sub(",\Z","]",out_str)
  return out_str



def set_item_faction():
  r_tuple=[]
  for k_item in xrange(len(items)):    
    faction_list=[]
    for i_troop in xrange(len(troops)):
      for i_item in troops[i_troop][7]:    
        if i_item==k_item:
          if troops[i_troop][6]<=fac_kingdoms_end and troops[i_troop][6]>=fac_kingdom_1:
            if troops[i_troop][3] & tf_hero == 0:
              if items[k_item][3] & itp_merchandise == itp_merchandise:
                faction_list.append(troops[i_troop][6])
    faction_set=set(faction_list)
    faction_list=list(faction_set)
    if len(faction_set)>0:    
      faction_strings=[]
      for i_fac in faction_list:
        faction_strings.append("fac_"+factions[i_fac][0])
      r_tuple.append([items[k_item][0], faction_strings,k_item]) 
  return r_tuple


def parse_faction():
  item_tuple=set_item_faction()  
  parsed=[]
  file = open("./module_items.py","r")    
  content=file.read()      
  file.close()
    
  for i_item_tuple in item_tuple:
    print i_item_tuple[0],i_item_tuple[1] 	

    if len(items[i_item_tuple[2]])==10 and keep_old_faction==0:
      content=re.sub('(\["'+i_item_tuple[0]+'".*?)\[fac_.*?\]',r"\1"+list2string(i_item_tuple[1]),content,re.S)
    elif len(items[i_item_tuple[2]])<10:
      repstr=", "+list2string(i_item_tuple[1])
      if len(items[i_item_tuple[2]])<9:      
        repstr=", []"+repstr
      i=content.find('["'+i_item_tuple[0]+'"')
      
      i=i+len('\["'+i_item_tuple[0]+'"')	
	
      match=0;

      while (match<=0):
        if(content[i]==']'):
          match=match+1
	if(content[i]=='['):
          match=match-1
	i=i+1	      
      content=content[:i-1]+repstr+content[i-1:]
	
   
    
  file = open("./module_items_factionize.py","w")    
  file.write(content)      
  file.close()  
  

  
  

parse_faction()
  
