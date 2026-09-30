## diagnosticspushd

> `/usr/libexec/diagnosticspushd`

```diff

-11.0.0.0.0
-  __TEXT.__text: 0x8978
-  __TEXT.__auth_stubs: 0x8b0
+14.0.0.0.0
+  __TEXT.__text: 0x8edc
+  __TEXT.__auth_stubs: 0x900
   __TEXT.__objc_stubs: 0x60
   __TEXT.__objc_methlist: 0xa0
   __TEXT.__const: 0x7f6
-  __TEXT.__oslogstring: 0x24f
-  __TEXT.__cstring: 0x5d6
-  __TEXT.__objc_methname: 0x4aa
+  __TEXT.__oslogstring: 0x28f
+  __TEXT.__cstring: 0x694
+  __TEXT.__objc_methname: 0x543
   __TEXT.__constg_swiftt: 0x24c
-  __TEXT.__swift5_typeref: 0x1fd
+  __TEXT.__swift5_typeref: 0x1fe
   __TEXT.__swift5_reflstr: 0xfa
   __TEXT.__swift5_fieldmd: 0x1ec
   __TEXT.__swift5_capture: 0x48

   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0x342
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x348
+  __TEXT.__unwind_info: 0x350
   __TEXT.__eh_frame: 0x240
-  __DATA_CONST.__auth_got: 0x460
-  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__auth_got: 0x488
+  __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x148
-  __DATA_CONST.__const: 0x6e8
+  __DATA_CONST.__const: 0x6f0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA.__objc_const: 0x710
-  __DATA.__objc_selrefs: 0xc8
+  __DATA.__objc_selrefs: 0x100
   __DATA.__objc_data: 0x178
   __DATA.__data: 0x488
   __DATA.__common: 0x80
   __DATA.__bss: 0xe80
+  - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 256
-  Symbols:   240
-  CStrings:  153
+  Functions: 258
+  Symbols:   251
+  CStrings:  167
 
Symbols:
+ _$s13TapToRadarKit0abC7ServiceC11createDraft_11processName13displayReason10completionySo0cG0C_SSSgAJys5Error_pSgcSgtF
+ _$s13TapToRadarKit0abC7ServiceC6sharedACvgZ
+ _$s13TapToRadarKit0abC7ServiceCMa
+ _$s13TapToRadarKit0abC7ServiceCMn
+ _$s13TapToRadarKit0abC7ServiceCMo
+ _$s13TapToRadarKit0abC7ServiceCN
+ _$sSS6appendyySSF
+ _$ss11_StringGutsV4growyySiF
+ _OBJC_CLASS_$_RadarComponent
+ _OBJC_CLASS_$_RadarDraft
+ __swift_FORCE_LOAD_$_swiftOSLog
CStrings:
+ " was unexpectedly expired."
+ "Background task "
+ "Failed to create TTR draft: %!@(MISSING)"
+ "Push Notification"
+ "Successfully created TTR draft"
+ "[TTR] diagnosticspushd post-install task expired"
+ "initWithName:version:identifier:"
+ "setClassification:"
+ "setComponent:"
+ "setProblemDescription:"
+ "setReproducibility:"
+ "setShouldCapturePerformanceTrace:"
+ "setTitle:"
+ "setup took too long"

```
