## Diagnostic-6009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6009.appex/Diagnostic-6009`

```diff

-202.1.0.0.0
-  __TEXT.__text: 0x1e7b4
-  __TEXT.__auth_stubs: 0x1210
+207.0.0.0.0
+  __TEXT.__text: 0x1e114
+  __TEXT.__auth_stubs: 0x11b0
   __TEXT.__objc_methlist: 0x2e4
-  __TEXT.__const: 0x11b8
-  __TEXT.__cstring: 0xce2
+  __TEXT.__const: 0x11a8
+  __TEXT.__cstring: 0xd72
   __TEXT.__objc_methname: 0x736
   __TEXT.__constg_swiftt: 0xa94
-  __TEXT.__swift5_typeref: 0x36e1
+  __TEXT.__swift5_typeref: 0x36d3
   __TEXT.__swift5_reflstr: 0x709
   __TEXT.__swift5_fieldmd: 0x540
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_capture: 0x470
   __TEXT.__swift5_proto: 0x34
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__oslogstring: 0x85
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__objc_classname: 0x37
   __TEXT.__objc_methtype: 0x19d
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6d0
+  __TEXT.__unwind_info: 0x6b8
   __TEXT.__eh_frame: 0x5e0
-  __DATA_CONST.__auth_got: 0x908
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__auth_ptr: 0x4f0
-  __DATA_CONST.__const: 0x1490
+  __DATA_CONST.__auth_got: 0x8d8
+  __DATA_CONST.__got: 0x3d0
+  __DATA_CONST.__auth_ptr: 0x4e8
+  __DATA_CONST.__const: 0x1448
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8622BA6E-D0AA-34CF-ADE6-A330F4DD368B
-  Functions: 669
-  Symbols:   157
+  UUID: C4E5BC5A-3DB8-374F-8F2C-5C1BE72C32D3
+  Functions: 662
+  Symbols:   149
   CStrings:  230
 
Symbols:
- __os_log_impl
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _os_log_type_enabled
- _swift_slowAlloc
- _swift_slowDealloc
CStrings:
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."

```
