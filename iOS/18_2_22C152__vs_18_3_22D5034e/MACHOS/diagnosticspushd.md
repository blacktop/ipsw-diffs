## diagnosticspushd

> `/usr/libexec/diagnosticspushd`

```diff

-16.0.0.0.0
-  __TEXT.__text: 0x11ad0
-  __TEXT.__auth_stubs: 0xca0
+18.0.0.0.0
+  __TEXT.__text: 0x11660
+  __TEXT.__auth_stubs: 0xc70
   __TEXT.__objc_stubs: 0x60
   __TEXT.__objc_methlist: 0xa0
   __TEXT.__const: 0x10c0
-  __TEXT.__oslogstring: 0x4bd
-  __TEXT.__cstring: 0x788
-  __TEXT.__objc_methname: 0x5e2
+  __TEXT.__oslogstring: 0x47d
+  __TEXT.__cstring: 0x6c8
+  __TEXT.__objc_methname: 0x549
   __TEXT.__constg_swiftt: 0x364
   __TEXT.__swift5_typeref: 0x333
   __TEXT.__swift5_reflstr: 0x19b

   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0x342
   __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__unwind_info: 0x5c8
+  __TEXT.__unwind_info: 0x5c0
   __TEXT.__eh_frame: 0x698
-  __DATA_CONST.__auth_got: 0x658
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__auth_ptr: 0x1c0
-  __DATA_CONST.__const: 0xea8
+  __DATA_CONST.__auth_got: 0x640
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__auth_ptr: 0x190
+  __DATA_CONST.__const: 0xea0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA.__objc_const: 0x7a0
-  __DATA.__objc_selrefs: 0x138
+  __DATA.__objc_selrefs: 0x100
   __DATA.__objc_data: 0x178
   __DATA.__data: 0x700
   __DATA.__common: 0xa0
   __DATA.__bss: 0x1e00
-  - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 496
-  Symbols:   331
-  CStrings:  205
+  Functions: 492
+  Symbols:   322
+  CStrings:  191
 
Symbols:
- _$s13TapToRadarKit0abC7ServiceC11createDraft_11processName13displayReason10completionySo0cG0C_SSSgAJys5Error_pSgcSgtF
- _$s13TapToRadarKit0abC7ServiceC6sharedACvgZ
- _$s13TapToRadarKit0abC7ServiceCMa
- _$s13TapToRadarKit0abC7ServiceCMn
- _$s13TapToRadarKit0abC7ServiceCMo
- _$s13TapToRadarKit0abC7ServiceCN
- _OBJC_CLASS_$_RadarComponent
- _OBJC_CLASS_$_RadarDraft
- __swift_FORCE_LOAD_$_swiftOSLog
CStrings:
- " was unexpectedly expired."
- "Background task "
- "Failed to create TTR draft: %@"
- "Push Notification"
- "Successfully created TTR draft"
- "[TTR] diagnosticspushd post-install task expired"
- "initWithName:version:identifier:"
- "setClassification:"
- "setComponent:"
- "setProblemDescription:"
- "setReproducibility:"
- "setShouldCapturePerformanceTrace:"
- "setTitle:"
- "setup took too long"

```
