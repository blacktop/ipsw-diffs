## biomed

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/Support/biomed`

```diff

-200.6.0.0.0
-  __TEXT.__text: 0x720
-  __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_stubs: 0x1a0
-  __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0xa3
+209.12.1.0.0
+  __TEXT.__text: 0x14e0
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_stubs: 0x260
+  __TEXT.__objc_methlist: 0x80
+  __TEXT.__const: 0xd6
+  __TEXT.__cstring: 0xa1
   __TEXT.__oslogstring: 0xf1
-  __TEXT.__objc_methname: 0x13a
-  __TEXT.__constg_swiftt: 0x38
-  __TEXT.__swift5_typeref: 0x14
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x60
-  __DATA_CONST.__objc_classlist: 0x8
+  __TEXT.__swift5_typeref: 0x7a
+  __TEXT.__swift5_capture: 0x64
+  __TEXT.__objc_methtype: 0x9b
+  __TEXT.__objc_methname: 0x23e
+  __TEXT.__objc_classname: 0x63
+  __TEXT.__constg_swiftt: 0x7c
+  __TEXT.__swift5_fieldmd: 0x20
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0xe0
+  __TEXT.__eh_frame: 0x48
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x218
+  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x48
-  __DATA.__objc_selrefs: 0x78
-  __DATA.__objc_data: 0xb0
-  __DATA.__data: 0x30
+  __DATA.__objc_const: 0xc0
+  __DATA.__objc_selrefs: 0xb0
+  __DATA.__objc_data: 0x170
+  __DATA.__data: 0xc8
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeDSL.framework/BiomeDSL
   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7F0E4E82-40BE-3217-BA85-F3B1335654AE
-  Functions: 11
-  Symbols:   63
-  CStrings:  30
+  UUID: CA95948B-DE6D-3786-8A39-1184477250AD
+  Functions: 57
+  Symbols:   99
+  CStrings:  47
 
Symbols:
+ _$s10Foundation22_convertNSErrorToErrorys0E0_pSo0C0CSgF
+ _$s10ObjectiveC8ObjCBoolVMn
+ _$s2os0A4_log_3dso0B0__ySo0a1_B7_type_ta_SVSo03OS_a1_B0Cs12StaticStringVs7CVarArg_pdtF
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSSN
+ _$sSSs7CVarArg10FoundationMc
+ _$sSo13os_log_type_ta0A0E5faultABvgZ
+ _$sSo13os_log_type_ta0A0E7defaultABvgZ
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss5ErrorP10FoundationE20localizedDescriptionSSvg
+ _$ss7CVarArgMp
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ __Block_copy
+ __Block_release
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
+ _objc_release
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x23
+ _swift_allocObject
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocObject
+ _swift_errorRelease
+ _swift_getErrorValue
+ _swift_getTypeByMangledNameInContext2
+ _swift_release
+ _swift_retain
+ _swift_willThrow
- _objc_claimAutoreleasedReturnValue
CStrings:
+ "B8@?0"
+ "BMBackgroundTaskScheduler"
+ "BMBackgroundTaskSchedulerProtocol"
+ "Deferred task %@"
+ "Error deferring task %@: %@"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "registerNoDeferralTaskWithIdentifier:asyncWorkHandler:"
+ "registerTaskWithIdentifier:workHandler:"
+ "registerXPCActivitiesWithTaskScheduler:"
+ "setExpirationHandler:"
+ "setTaskCompleted"
+ "setTaskExpiredWithRetryAfter:error:"
+ "sharedScheduler"
+ "v16@?0@\"BGSystemTask\"8"
+ "v32@0:8@\"NSString\"16@?<v@?@?<B@?>>24"
+ "v32@0:8@\"NSString\"16@?<v@?@?<v@?>>24"
+ "v32@0:8@16@?24"
- "registerXPCActivities"

```
