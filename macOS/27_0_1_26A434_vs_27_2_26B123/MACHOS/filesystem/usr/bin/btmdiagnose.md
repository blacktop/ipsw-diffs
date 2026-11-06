## btmdiagnose

> `/usr/bin/btmdiagnose`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-371.0.0.0.0
-  __TEXT.__text: 0x25104
+371.1.4.0.0
+  __TEXT.__text: 0x25174
   __TEXT.__auth_stubs: 0xa20
   __TEXT.__objc_stubs: 0x3620
   __TEXT.__objc_methlist: 0x171c
   __TEXT.__const: 0x122
   __TEXT.__gcc_except_tab: 0x418
-  __TEXT.__objc_methname: 0x4235
-  __TEXT.__cstring: 0x17b3
+  __TEXT.__objc_methname: 0x4234
+  __TEXT.__cstring: 0x17d3
   __TEXT.__oslogstring: 0x1db6
   __TEXT.__objc_classname: 0x176
   __TEXT.__objc_methtype: 0xfb1

   __TEXT.__unwind_info: 0x980
   __TEXT.__eh_frame: 0x260
   __DATA_CONST.__const: 0x800
-  __DATA_CONST.__cfstring: 0x1b40
+  __DATA_CONST.__cfstring: 0x1b80
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50

   - /usr/lib/swift/libswiftos.dylib
   Functions: 679
   Symbols:   269
-  CStrings:  1309
+  CStrings:  1311
 
Functions:
~ sub_10000457c : 9608 -> 9600
~ sub_10000af6c -> sub_10000af64 : 144 -> 172
~ sub_1000114cc -> sub_1000114e0 : 436 -> 472
~ sub_10001d000 -> sub_10001d038 : 1648 -> 1684
~ sub_100021700 -> sub_10002175c : 4256 -> 4260
~ sub_1000227a0 -> sub_100022800 : 120 -> 124
~ sub_100022b70 -> sub_100022bd4 : 264 -> 276
CStrings:
+ "domainForBackgroundUser:"
+ "system xpcservice"
+ "user xpcservice"
- "domainForRoleAccountUser:"
```
