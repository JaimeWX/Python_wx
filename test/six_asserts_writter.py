import json

asserts = {}
asserts['assertEqual(a,b)'] = '核实a==b'
asserts['assertNotEqual(a,b)'] = '核实a!=b'
asserts['assertTrue(x)'] = '核实x为True'
asserts['assertFalse(x)'] = '核实x为False'
asserts['assertIn(item,list)'] = '核实item在list中'
asserts['assertNotIn(item,list)'] = '核实item不在list中'

fileName = 'sixAsserts'
with open(fileName,'w', encoding="utf8") as f_obj:
    json.dump(asserts,f_obj, ensure_ascii=False)