## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-985.0.0.0.0
-  __TEXT.__text: 0xcdbc0
+990.0.0.0.0
+  __TEXT.__text: 0xcdc58
   __TEXT.__auth_stubs: 0x1740
   __TEXT.__objc_stubs: 0xd0e0
   __TEXT.__objc_methlist: 0x5044
   __TEXT.__const: 0x288
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__gcc_except_tab: 0x3854
-  __TEXT.__oslogstring: 0x116e4
-  __TEXT.__cstring: 0xdf54
+  __TEXT.__gcc_except_tab: 0x3888
+  __TEXT.__oslogstring: 0x116a5
+  __TEXT.__cstring: 0xdf7a
   __TEXT.__objc_methname: 0x102bb
   __TEXT.__objc_classname: 0xc2e
   __TEXT.__objc_methtype: 0x2a60

   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0x108
-  __DATA_CONST.__objc_intobj: 0x6d8
+  __DATA_CONST.__objc_intobj: 0x6f0
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0xbb0
   __DATA_CONST.__got: 0x840

   - /usr/lib/libobjc.A.dylib
   Functions: 2254
   Symbols:   618
-  CStrings:  6306
+  CStrings:  6305
 
Functions:
~ sub_100010060 : 3288 -> 3224
~ sub_100047c80 -> sub_100047c40 : 612 -> 604
~ sub_10005306c -> sub_100053024 : 1860 -> 1916
~ sub_1000b587c -> sub_1000b586c : 5960 -> 6128
CStrings:
+ "Ignoring proxy match dictionary, not applicable for seed"
+ "Seed"
+ "https://mask-api.icloud.com/v6_2/fetchConfigFile"
- "Ignoring proxy match dictionary, not applicable for internal"
- "Ignoring proxy match dictionary, not applicable for public"
- "Internal"
- "Public"
```
