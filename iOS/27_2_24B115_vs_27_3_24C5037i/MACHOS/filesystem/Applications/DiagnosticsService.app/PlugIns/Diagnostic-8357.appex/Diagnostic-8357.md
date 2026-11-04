## Diagnostic-8357

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8357.appex/Diagnostic-8357`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-1374.42.1.0.0
-  __TEXT.__text: 0xa448
-  __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_stubs: 0x3c0
+1374.60.20.0.0
+  __TEXT.__text: 0x9840
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_stubs: 0x3a0
   __TEXT.__objc_methlist: 0x1c4
-  __TEXT.__const: 0x2d4
+  __TEXT.__const: 0x218
   __TEXT.__objc_classname: 0x5f
-  __TEXT.__objc_methname: 0x506
+  __TEXT.__objc_methname: 0x4f6
   __TEXT.__objc_methtype: 0x121
-  __TEXT.__constg_swiftt: 0xd0
-  __TEXT.__swift5_typeref: 0x2b3
-  __TEXT.__swift5_reflstr: 0xc6
-  __TEXT.__swift5_fieldmd: 0xec
+  __TEXT.__constg_swiftt: 0x88
+  __TEXT.__swift5_typeref: 0x283
+  __TEXT.__swift5_reflstr: 0x96
+  __TEXT.__swift5_fieldmd: 0x90
   __TEXT.__cstring: 0x83
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_capture: 0x10c
-  __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift_as_entry: 0x20
-  __TEXT.__swift_as_ret: 0x14
-  __TEXT.__swift_as_cont: 0x20
-  __TEXT.__unwind_info: 0x328
-  __TEXT.__eh_frame: 0x308
-  __DATA_CONST.__const: 0x518
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__swift5_capture: 0xbc
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift_as_cont: 0x3c
+  __TEXT.__unwind_info: 0x2e0
+  __TEXT.__eh_frame: 0x248
+  __DATA_CONST.__const: 0x368
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x480
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__auth_ptr: 0x98
+  __DATA_CONST.__auth_got: 0x468
+  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__auth_ptr: 0x58
   __DATA.__objc_const: 0x298
-  __DATA.__objc_selrefs: 0x1d0
+  __DATA.__objc_selrefs: 0x1c8
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x2c8
+  __DATA.__data: 0x2c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 190
-  Symbols:   119
-  CStrings:  96
+  Functions: 165
+  Symbols:   121
+  CStrings:  95
 
Symbols:
+ _swift_asyncLet_begin
+ _swift_asyncLet_finish
+ _swift_asyncLet_get
- _objc_retain_x27
CStrings:
- "isCancelled"
```
