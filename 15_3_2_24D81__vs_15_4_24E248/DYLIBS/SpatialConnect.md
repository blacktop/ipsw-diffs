## SpatialConnect

> `/System/Library/PrivateFrameworks/SpatialConnect.framework/Versions/A/SpatialConnect`

```diff

 1.60.26.0.0
-  __TEXT.__text: 0x1114c
-  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__text: 0x10f48
+  __TEXT.__auth_stubs: 0xcb0
   __TEXT.__objc_methlist: 0x5d4
-  __TEXT.__const: 0x974
-  __TEXT.__cstring: 0xe0a
+  __TEXT.__const: 0x994
+  __TEXT.__cstring: 0xd5a
   __TEXT.__oslogstring: 0xe0b
-  __TEXT.__gcc_except_tab: 0x5e0
+  __TEXT.__gcc_except_tab: 0x5dc
   __TEXT.__swift5_typeref: 0x275
   __TEXT.__swift5_capture: 0x8c
   __TEXT.__constg_swiftt: 0x4d4

   __TEXT.__swift5_fieldmd: 0x318
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_proto: 0x70
+  __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_protos: 0x10
   __TEXT.__unwind_info: 0x5a8

   __TEXT.__objc_methtype: 0xc42
   __TEXT.__objc_stubs: 0x11c0
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x4f8
+  __DATA_CONST.__const: 0x500
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x578
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH_CONST.__const: 0xa08
   __AUTH_CONST.__cfstring: 0x460
   __AUTH_CONST.__objc_const: 0x1280

   __DATA.__objc_ivar: 0xb0
   __DATA.__data: 0xd0
   __DATA.__common: 0x1
-  __DATA.__bss: 0xce0
+  __DATA.__bss: 0xd60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: BCEDDED8-2FBB-35BE-A558-F58B9F5FF306
-  Functions: 531
-  Symbols:   1282
-  CStrings:  582
+  UUID: F066C711-CE65-3017-9FA4-4C13A4352B01
+  Functions: 539
+  Symbols:   1292
+  CStrings:  579
 
Symbols:
+ -[MipGenPolyphase initWithLibrary:].cold.1
+ -[Unwarp initForRenderingWithLibrary:destinationPixelFormat:warpMode:].cold.1
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_SpatialConnect
+ sc_log_foveation_service.cold.1
+ sc_log_invalidatable.cold.1
+ sc_log_server.cold.1
+ sc_log_statistics.cold.1
+ sc_log_warper.cold.1
+ sc_timebase_info.cold.1
CStrings:
- "Swift/UnsafePointer.swift"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"

```
