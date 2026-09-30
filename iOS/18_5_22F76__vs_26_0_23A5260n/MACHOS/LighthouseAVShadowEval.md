## LighthouseAVShadowEval

> `/System/Library/ExtensionKit/Extensions/LighthouseAVShadowEval.appex/LighthouseAVShadowEval`

```diff

-26.0.0.0.0
-  __TEXT.__text: 0x47e8
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__const: 0x416
-  __TEXT.__cstring: 0x12e
-  __TEXT.__swift5_typeref: 0x10d
-  __TEXT.__swift5_reflstr: 0x12d
+29.0.0.0.0
+  __TEXT.__text: 0x5c54
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__const: 0x466
+  __TEXT.__cstring: 0x232
+  __TEXT.__swift5_typeref: 0x177
+  __TEXT.__swift5_reflstr: 0x162
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x84
-  __TEXT.__swift5_fieldmd: 0xc4
-  __TEXT.__oslogstring: 0x156
-  __TEXT.__objc_methname: 0x3f
+  __TEXT.__swift5_fieldmd: 0xe8
+  __TEXT.__oslogstring: 0x1cf
+  __TEXT.__objc_methname: 0x73
+  __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_proto: 0x38
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x10
-  __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x190
-  __TEXT.__eh_frame: 0x208
-  __DATA_CONST.__auth_got: 0x330
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA_CONST.__const: 0x368
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__eh_frame: 0x2c8
+  __DATA_CONST.__auth_got: 0x400
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__auth_ptr: 0x1c8
+  __DATA_CONST.__const: 0x438
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x18
-  __DATA.__data: 0xc0
+  __DATA.__objc_selrefs: 0x30
+  __DATA.__data: 0xe0
   __DATA.__bss: 0x740
   __DATA.__common: 0x18
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/LighthouseAV.framework/LighthouseAV
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

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
-  UUID: 5CAA4F07-658D-329C-A930-8C4F0E015D84
-  Functions: 102
-  Symbols:   86
-  CStrings:  18
+  UUID: E6EC6085-FBBD-3B0C-A66E-BA61FB5F5F97
+  Functions: 122
+  Symbols:   100
+  CStrings:  33
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSUserDefaults
+ __Block_copy
+ __Block_release
+ __NSConcreteStackBlock
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_autoreleaseReturnValue
+ _objc_release_x24
+ _objc_release_x27
+ _objc_retain_x19
+ _objc_retain_x23
+ _swift_arrayDestroy
+ _swift_bridgeObjectRetain_n
+ _swift_deallocObject
+ _swift_dynamicCast
+ _swift_getObjCClassMetadata
+ _swift_initStackObject
+ _swift_setDeallocating
+ _swift_unknownObjectRelease
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x8
- _swift_bridgeObjectRelease_n
- _swift_release_n
- _swift_retain_n
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Failed to compile model at %s"
+ "Failed to initialize model from compiled URL %s"
+ "Got non-date type object for last run date: %s"
+ "Metrics: %s"
+ "Submitting %s."
+ "com.apple.LighthouseAdaptiveVolume.UserMetric"
+ "lastPVShadowEvalRunDate:"
+ "modelConfiguration"
+ "runOnWholeHistory"
+ "setObject:forKey:"
+ "standardUserDefaults"
+ "trialDeploymentId"
+ "trialExperimentId"
+ "trialTreatmentId"
+ "valueForKey:"
- "Failed to initialize model from path %s"

```
