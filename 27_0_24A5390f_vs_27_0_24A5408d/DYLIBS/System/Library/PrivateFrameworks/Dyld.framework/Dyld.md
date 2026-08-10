## Dyld

> `/System/Library/PrivateFrameworks/Dyld.framework/Dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-27060.1.0.0.0
-  __TEXT.__text: 0x51ad8
+27062.0.0.0.0
+  __TEXT.__text: 0x51de4
   __TEXT.__objc_methlist: 0x6ac
-  __TEXT.__const: 0x3408
-  __TEXT.__swift5_typeref: 0xd3b
-  __TEXT.__swift5_fieldmd: 0x1258
-  __TEXT.__constg_swiftt: 0xf70
+  __TEXT.__const: 0x34b8
+  __TEXT.__swift5_typeref: 0xd57
+  __TEXT.__swift5_fieldmd: 0x12bc
+  __TEXT.__constg_swiftt: 0xf8c
   __TEXT.__cstring: 0x13d7
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_mpenum: 0x70
-  __TEXT.__swift5_reflstr: 0xe26
-  __TEXT.__swift5_assocty: 0x640
+  __TEXT.__swift5_reflstr: 0xec6
+  __TEXT.__swift5_assocty: 0x658
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift5_proto: 0x1dc
-  __TEXT.__swift5_types: 0x12c
+  __TEXT.__swift5_proto: 0x1e8
+  __TEXT.__swift5_types: 0x130
   __TEXT.__swift5_types2: 0x2c
   __TEXT.__swift5_capture: 0x90
   __TEXT.__gcc_except_tab: 0xa18
-  __TEXT.__unwind_info: 0x11e8
+  __TEXT.__unwind_info: 0x11f8
   __TEXT.__eh_frame: 0x1470
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__got: 0x240
-  __AUTH_CONST.__const: 0x2050
+  __AUTH_CONST.__const: 0x20e0
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x1b70
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0xb68
   __AUTH.__objc_data: 0x640
   __AUTH.__data: 0x1670
-  __DATA.__data: 0xb78
+  __DATA.__data: 0xb80
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x3300
+  __DATA.__bss: 0x3480
   __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1448
-  Symbols:   1115
+  Functions: 1459
+  Symbols:   1118
   CStrings:  152
 
Symbols:
+ _associated conformance 4Dyld10AtlasErrorO13DiscriminatorOSHAASQ
+ _symbolic _____ 4Dyld10AtlasErrorO13DiscriminatorO
+ _symbolic ___________t s5Int32V 4Dyld10AtlasErrorO13DiscriminatorO
```
