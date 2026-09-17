## backgroundassets.user

> `/usr/libexec/backgroundassets.user`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-279.0.5.0.0
-  __TEXT.__text: 0x5cbec
+279.40.6.0.0
+  __TEXT.__text: 0x5cd48
   __TEXT.__auth_stubs: 0x1670
   __TEXT.__objc_stubs: 0x75a0
-  __TEXT.__objc_methlist: 0x34e4
+  __TEXT.__objc_methlist: 0x34ec
   __TEXT.__const: 0x1ae8
   __TEXT.__objc_classname: 0x84e
   __TEXT.__objc_methtype: 0x1952
   __TEXT.__oslogstring: 0x6cc4
   __TEXT.__cstring: 0x4110
-  __TEXT.__objc_methname: 0x9ab8
+  __TEXT.__objc_methname: 0x9ae8
   __TEXT.__gcc_except_tab: 0x14c8
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0x428

   __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__auth_ptr: 0x360
   __DATA.__objc_const: 0x59d0
-  __DATA.__objc_selrefs: 0x2120
+  __DATA.__objc_selrefs: 0x2128
   __DATA.__objc_ivar: 0x3b0
   __DATA.__objc_data: 0x1210
   __DATA.__data: 0x12e8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1988
+  Functions: 1989
   Symbols:   656
-  CStrings:  2582
+  CStrings:  2583
 
Functions:
~ sub_100016a80 : 436 -> 348
+ sub_100016bdc
CStrings:
+ "_pauseBackgroundDownloads"
+ "pauseAllBackgroundDownloads"
- "_pauseDownloads"
```
