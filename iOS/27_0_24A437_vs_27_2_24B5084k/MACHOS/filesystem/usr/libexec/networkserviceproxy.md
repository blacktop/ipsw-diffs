## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__auth_got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-985.0.0.0.0
-  __TEXT.__text: 0xc04c8
+990.0.0.0.0
+  __TEXT.__text: 0xc0544
   __TEXT.__auth_stubs: 0x18e0
   __TEXT.__objc_stubs: 0xd260
   __TEXT.__objc_methlist: 0x5044
   __TEXT.__const: 0x2a0
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x3858
-  __TEXT.__oslogstring: 0x117ab
-  __TEXT.__cstring: 0xdf35
+  __TEXT.__gcc_except_tab: 0x388c
+  __TEXT.__oslogstring: 0x1176c
+  __TEXT.__cstring: 0xdf5b
   __TEXT.__objc_methname: 0x1043c
   __TEXT.__objc_classname: 0xc2e
   __TEXT.__objc_methtype: 0x2a77

   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0x108
-  __DATA_CONST.__objc_intobj: 0x6d8
+  __DATA_CONST.__objc_intobj: 0x6f0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0xc80
   __DATA_CONST.__got: 0x848

   - /usr/lib/libobjc.A.dylib
   Functions: 2162
   Symbols:   645
-  CStrings:  6328
+  CStrings:  6327
 
Functions:
~ sub_1000174f0 : 3104 -> 3028
~ sub_10004a9b0 -> sub_10004a964 : 568 -> 560
~ sub_1000543b0 -> sub_10005435c : 1736 -> 1788
~ sub_1000abdd8 -> sub_1000abdb8 : 5668 -> 5824
CStrings:
+ "Ignoring proxy match dictionary, not applicable for seed"
+ "Seed"
+ "https://mask-api.icloud.com/v6_2/fetchConfigFile"
- "Ignoring proxy match dictionary, not applicable for internal"
- "Ignoring proxy match dictionary, not applicable for public"
- "Internal"
- "Public"
```
