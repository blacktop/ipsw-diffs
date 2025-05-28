## com.apple.mlhost.QuartzWorker

> `/System/Library/ExtensionKit/Extensions/com.apple.mlhost.QuartzWorker.appex/com.apple.mlhost.QuartzWorker`

```diff

-1.0.3.0.0
-  __TEXT.__text: 0x4078
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__const: 0x3d2
-  __TEXT.__cstring: 0x112
+1.1.2.0.0
+  __TEXT.__text: 0x5ab8
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__const: 0x3e2
+  __TEXT.__cstring: 0x1a1
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x12f
+  __TEXT.__swift5_typeref: 0x16b
   __TEXT.__constg_swiftt: 0x90
-  __TEXT.__swift5_reflstr: 0x5d
-  __TEXT.__swift5_fieldmd: 0x94
+  __TEXT.__swift5_reflstr: 0x45
+  __TEXT.__swift5_fieldmd: 0x7c
   __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_capture: 0x14
+  __TEXT.__objc_methname: 0x11
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x1bc
-  __TEXT.__eh_frame: 0x258
-  __DATA_CONST.__auth_got: 0x2f8
-  __DATA_CONST.__got: 0x98
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__eh_frame: 0x288
+  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x388
+  __DATA_CONST.__const: 0x468
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x1c0
+  __DATA.__objc_selrefs: 0x8
+  __DATA.__objc_classrefs: 0x10
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x7d0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/TabularData.framework/TabularData
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
+  - /System/Library/PrivateFrameworks/LighthouseQuartz.framework/LighthouseQuartz
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreML.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVision.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 123
-  Symbols:   58
-  CStrings:  10
+  - /usr/lib/swift/libswiftsimd.dylib
+  Functions: 143
+  Symbols:   92
+  CStrings:  14
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ __Block_copy
+ __Block_release
+ __NSConcreteStackBlock
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreML
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftVision
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_stdlib_bridgeErrorToNSError
+ _bzero
+ _objc_autoreleaseReturnValue
+ _objc_msgSend
+ _objc_opt_self
+ _objc_release
+ _objc_release_x8
+ _objc_retain_x10
+ _objc_retain_x23
+ _swift_deallocObject
+ _swift_dynamicCast
+ _swift_errorRetain
+ _swift_getObjCClassMetadata
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Config doesn't have shouldRun set, exiting early"
+ "Got an error from runAnalysisCommand: %@"
+ "Setting up for analysis"
+ "Starting analysis command"
+ "com.apple.LighthouseHealth.DailySummary"
+ "initWithInteger:"
- "Task interruped while sleeping."
- "TaskId: %s, TaskName: %s: currentDuration: %f"
- "durationThreshold"

```
