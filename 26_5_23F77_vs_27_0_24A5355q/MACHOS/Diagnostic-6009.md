## Diagnostic-6009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6009.appex/Diagnostic-6009`

```diff

-283.0.0.0.0
-  __TEXT.__text: 0x1ec38
-  __TEXT.__auth_stubs: 0x1280
+335.0.0.0.0
+  __TEXT.__text: 0x1f900
+  __TEXT.__auth_stubs: 0x1470
   __TEXT.__objc_stubs: 0x520
   __TEXT.__objc_methlist: 0x2e4
-  __TEXT.__const: 0x15f8
-  __TEXT.__constg_swiftt: 0xb5c
-  __TEXT.__swift5_typeref: 0x2ba3
-  __TEXT.__cstring: 0x904
-  __TEXT.__swift5_reflstr: 0x767
+  __TEXT.__const: 0x15c8
+  __TEXT.__constg_swiftt: 0xb68
+  __TEXT.__swift5_typeref: 0x2b71
+  __TEXT.__cstring: 0x874
+  __TEXT.__swift5_reflstr: 0x779
   __TEXT.__swift5_fieldmd: 0x598
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x34
   __TEXT.__swift5_types: 0x3c
   __TEXT.__objc_classname: 0x1b6
   __TEXT.__objc_methname: 0xcee
-  __TEXT.__swift5_capture: 0x4a4
+  __TEXT.__swift5_capture: 0x514
+  __TEXT.__oslogstring: 0x85
   __TEXT.__objc_methtype: 0x280
   __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift_as_cont: 0x58
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6e0
-  __TEXT.__eh_frame: 0x714
-  __DATA_CONST.__auth_got: 0x948
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__auth_ptr: 0x4b8
-  __DATA_CONST.__const: 0x14a8
+  __TEXT.__unwind_info: 0x738
+  __TEXT.__eh_frame: 0x6f4
+  __DATA_CONST.__const: 0x1550
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__auth_got: 0xa40
+  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__auth_ptr: 0x4c0
   __DATA.__objc_const: 0xb28
   __DATA.__objc_selrefs: 0x2a0
   __DATA.__objc_data: 0x878
-  __DATA.__data: 0xf30
+  __DATA.__data: 0xfb0
   __DATA.__bss: 0x8b8
   __DATA.__common: 0x40
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D8EB8B3A-19CC-39EF-8ED9-37F35A096FF4
-  Functions: 663
-  Symbols:   162
+  UUID: 2F480C06-280E-30FF-818F-638BCE892246
+  Functions: 688
+  Symbols:   193
   CStrings:  246
 
Symbols:
+ __os_log_impl
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ _objc_release_x12
+ _objc_retain_x2
+ _objc_retain_x28
+ _os_log_type_enabled
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_release_n
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _swift_slowAlloc
+ _swift_slowDealloc
- __swift_FORCE_LOAD_$_swiftCoreMedia
- _objc_retain_x25
- _objc_retain_x3
CStrings:
+ "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
- "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."

```
