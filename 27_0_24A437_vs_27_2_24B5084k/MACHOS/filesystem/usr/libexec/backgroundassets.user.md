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
-  __TEXT.__text: 0x59140
+279.40.6.0.0
+  __TEXT.__text: 0x59298
   __TEXT.__auth_stubs: 0x1970
   __TEXT.__objc_stubs: 0x7860
-  __TEXT.__objc_methlist: 0x352c
+  __TEXT.__objc_methlist: 0x3534
   __TEXT.__const: 0x1ae8
   __TEXT.__objc_classname: 0x84e
   __TEXT.__objc_methtype: 0x19b2
   __TEXT.__oslogstring: 0x6f94
   __TEXT.__cstring: 0x4230
-  __TEXT.__objc_methname: 0x9cae
+  __TEXT.__objc_methname: 0x9cde
   __TEXT.__gcc_except_tab: 0x14fc
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0x428

   __DATA_CONST.__got: 0x5c8
   __DATA_CONST.__auth_ptr: 0x360
   __DATA.__objc_const: 0x5a30
-  __DATA.__objc_selrefs: 0x21b8
+  __DATA.__objc_selrefs: 0x21c0
   __DATA.__objc_ivar: 0x3b8
   __DATA.__objc_data: 0x1210
   __DATA.__data: 0x12e8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1948
+  Functions: 1949
   Symbols:   704
-  CStrings:  2619
+  CStrings:  2620
 
Functions:
~ sub_100015144 : 424 -> 344
+ sub_10001529c
CStrings:
+ "_pauseBackgroundDownloads"
+ "pauseAllBackgroundDownloads"
- "_pauseDownloads"
```
