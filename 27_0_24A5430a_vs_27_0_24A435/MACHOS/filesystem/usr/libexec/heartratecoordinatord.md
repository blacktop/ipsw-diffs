## heartratecoordinatord

> `/usr/libexec/heartratecoordinatord`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 42.0.0.0.0
-  __TEXT.__text: 0x27c68
+  __TEXT.__text: 0x27d14
   __TEXT.__auth_stubs: 0x7d0
   __TEXT.__objc_stubs: 0x4180
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1abc
   __TEXT.__const: 0x375
   __TEXT.__oslogstring: 0x3bab
-  __TEXT.__cstring: 0x22cd
-  __TEXT.__gcc_except_tab: 0x44d8
+  __TEXT.__cstring: 0x231b
+  __TEXT.__gcc_except_tab: 0x44e4
   __TEXT.__objc_methname: 0x52de
   __TEXT.__objc_classname: 0x3a8
   __TEXT.__objc_methtype: 0x1c0f

   - /usr/lib/libobjc.A.dylib
   Functions: 939
   Symbols:   210
-  CStrings:  1632
+  CStrings:  1638
 
Functions:
~ sub_10000461c : 1944 -> 1996
~ sub_100004db4 -> sub_100004de8 : 184 -> 220
~ sub_100004e6c -> sub_100004ec4 : 2688 -> 2772
CStrings:
+ "Device1,8240"
+ "Device1,8242"
+ "Device1,8245"
+ "Device1,8246"
+ "Device1,8247"
+ "Device1,8248"
```
