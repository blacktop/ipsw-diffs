## IPConfiguration

> `/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-557.60.2.0.0
-  __TEXT.__text: 0x5c530
+557.60.4.0.0
+  __TEXT.__text: 0x5c69c
   __TEXT.__auth_stubs: 0x10d0
   __TEXT.__const: 0x318
-  __TEXT.__oslogstring: 0x623e
-  __TEXT.__cstring: 0x425e
+  __TEXT.__oslogstring: 0x6261
+  __TEXT.__cstring: 0x427b
   __TEXT.__unwind_info: 0xf30
   __DATA_CONST.__const: 0x1db0
   __DATA_CONST.__cfstring: 0x2b40

   - /usr/lib/libbsm.0.dylib
   Functions: 1030
   Symbols:   494
-  CStrings:  1744
+  CStrings:  1746
 
Functions:
~ sub_1714 : 2832 -> 2888
~ sub_2bf48 -> sub_2bf80 : 948 -> 936
~ sub_2e260 -> sub_2e28c : 24 -> 344
CStrings:
+ "%s(%s): router IP/hwaddr not valid"
+ "service_router_set_all_valid"
```
