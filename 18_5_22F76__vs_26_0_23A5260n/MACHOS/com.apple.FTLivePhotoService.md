## com.apple.FTLivePhotoService

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/XPCServices/com.apple.FTLivePhotoService.xpc/com.apple.FTLivePhotoService`

```diff

-1525.600.42.0.0
-  __TEXT.__text: 0x3b0c8
-  __TEXT.__auth_stubs: 0x1260
+1562.100.3.2.4
+  __TEXT.__text: 0x360e8
+  __TEXT.__auth_stubs: 0x1220
   __TEXT.__objc_stubs: 0x1560
-  __TEXT.__objc_methlist: 0x130c
+  __TEXT.__objc_methlist: 0x1344
   __TEXT.__cstring: 0x1e23
-  __TEXT.__const: 0x10b0
+  __TEXT.__const: 0x11d0
   __TEXT.__objc_classname: 0x198
-  __TEXT.__objc_methname: 0x2dcc
-  __TEXT.__objc_methtype: 0x158d
+  __TEXT.__objc_methname: 0x2ea4
+  __TEXT.__objc_methtype: 0x1669
   __TEXT.__oslogstring: 0x31d1
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__swift5_typeref: 0xc9a
+  __TEXT.__swift5_typeref: 0xc9c
   __TEXT.__swift5_fieldmd: 0x8dc
   __TEXT.__constg_swiftt: 0x10b0
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift5_capture: 0x40c
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x5c
-  __TEXT.__unwind_info: 0xe38
-  __TEXT.__eh_frame: 0x1418
-  __DATA_CONST.__auth_got: 0x940
+  __TEXT.__unwind_info: 0xe28
+  __TEXT.__eh_frame: 0x12e8
+  __DATA_CONST.__auth_got: 0x920
   __DATA_CONST.__got: 0x380
-  __DATA_CONST.__auth_ptr: 0x308
-  __DATA_CONST.__const: 0x1cd8
+  __DATA_CONST.__auth_ptr: 0x260
+  __DATA_CONST.__const: 0x1ce8
   __DATA_CONST.__cfstring: 0x2c0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2860
-  __DATA.__objc_selrefs: 0xb80
+  __DATA.__objc_const: 0x2888
+  __DATA.__objc_selrefs: 0xba8
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x13f0
-  __DATA.__data: 0x1478
+  __DATA.__data: 0x1348
   __DATA.__bss: 0xe50
   __DATA.__common: 0xe8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: A44236A2-0689-3AA2-A378-85C0B9810D0C
-  Functions: 1356
-  Symbols:   324
-  CStrings:  1097
+  UUID: D6B4F900-CA5E-3C1A-95E2-9A5E77079C24
+  Functions: 1310
+  Symbols:   316
+  CStrings:  1106
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _swift_bridgeObjectRelease_n
- _swift_release_n
- _swift_retain_n
- _swift_unknownObjectRelease_n
- _swift_unknownObjectRetain_n
CStrings:
+ "captionsClient:didChangeSourceLocale:"
+ "captionsClient:didConfigureCaptionsWithError:"
+ "captionsClient:didProduceLanguageHypothesis:"
+ "captionsClient:didStopLanguageDetectorWithError:"
+ "service:account:incomingBatchMessage:"
+ "v32@0:8@\"AVCCaptionsClient\"16@\"AVCCaptionsLanguageDetectorResults\"24"
+ "v32@0:8@\"AVCCaptionsClient\"16@\"NSError\"24"
+ "v32@0:8@\"AVCCaptionsClient\"16@\"NSLocale\"24"
+ "v40@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSIncomingBatchMessage\"32"

```
