## coreduetd

> `/usr/libexec/coreduetd`

```diff

-1892.22.0.0.0
-  __TEXT.__text: 0x2123c
+1917.0.1.0.0
+  __TEXT.__text: 0x216e4
   __TEXT.__auth_stubs: 0x990
-  __TEXT.__objc_stubs: 0x4f80
-  __TEXT.__objc_methlist: 0x19a8
+  __TEXT.__objc_stubs: 0x5080
+  __TEXT.__objc_methlist: 0x1998
   __TEXT.__objc_classname: 0x1ba
-  __TEXT.__objc_methname: 0x6075
-  __TEXT.__objc_methtype: 0x1bbb
-  __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x1abe
-  __TEXT.__oslogstring: 0x3520
-  __TEXT.__gcc_except_tab: 0x5c0
-  __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x790
+  __TEXT.__objc_methname: 0x619e
+  __TEXT.__objc_methtype: 0x1bc2
+  __TEXT.__const: 0xe0
+  __TEXT.__cstring: 0x1b52
+  __TEXT.__oslogstring: 0x34eb
+  __TEXT.__gcc_except_tab: 0x620
+  __TEXT.__dlopen_cstrs: 0x116
+  __TEXT.__unwind_info: 0x7b8
   __DATA_CONST.__auth_got: 0x4d8
-  __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0xe48
-  __DATA_CONST.__cfstring: 0x1640
+  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__const: 0xea0
+  __DATA_CONST.__cfstring: 0x1660
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x368
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2490
-  __DATA.__objc_selrefs: 0x16f8
-  __DATA.__objc_ivar: 0x198
+  __DATA.__objc_const: 0x24c0
+  __DATA.__objc_selrefs: 0x1748
+  __DATA.__objc_ivar: 0x19c
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x300
-  __DATA.__bss: 0x108
+  __DATA.__bss: 0x120
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 17856215-4AB6-3E35-942F-3EC6C88E6E9D
-  Functions: 646
-  Symbols:   312
-  CStrings:  1903
+  UUID: 22FD2D33-217C-35AF-BA74-6789246F3CC6
+  Functions: 654
+  Symbols:   314
+  CStrings:  1924
 
Symbols:
+ _OBJC_CLASS_$__PSBackgroundProcessingTask
+ _OBJC_CLASS_$__PSContactHandleFeatureProvider
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetDaemon/CoreDuetDaemon/Knowledge/CDKnowledgeDaemon.m:613"
+ "@\"_PSContactHandleFeatureProvider\""
+ "BGRepeatingSystemTaskRequest"
+ "BGSystemTaskScheduler"
+ "Failed to submit %@ task with error: %@"
+ "Interaction features for contact handles %{public}@"
+ "T@\"_PSContactHandleFeatureProvider\",R,N,V_contactHandleFeatureProvider"
+ "Task registration for %@ %s"
+ "_contactHandleFeatureProvider"
+ "_interactionFeaturesForHandle:"
+ "com.apple.proactive.psbackgroundprocessingtask"
+ "contactHandleFeatureProvider"
+ "failed"
+ "handleRepeatingTask:"
+ "initWithIdentifier:"
+ "interactionFeaturesForHandle:reply:"
+ "psBackgroundProcessingChannel"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "registerPSBackgroundProcessingTask"
+ "service:account:incomingBatchMessage:"
+ "setMinDurationBetweenInstances:"
+ "setRequiresExternalPower:"
+ "sharedScheduler"
+ "softlink:o:path:/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks"
+ "submitTaskRequest:error:"
+ "successful"
+ "taskRequestForIdentifier:"
+ "v16@?0@\"BGRepeatingSystemTask\"8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\">24"
+ "v40@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSIncomingBatchMessage\"32"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetDaemon/CoreDuetDaemon/Knowledge/CDKnowledgeDaemon.m:605"
- "Could not Validate CoreML model as device is class C locked"
- "Fetching ephemeral features for Share Sheet for client: %{public}@"
- "Validating CoreML model for client %{public}@"
- "computeEphemeralFeaturesWithPredictionContext:"
- "computeShareSheetEphemeralFeaturesWithPredictionContext:reply:"
- "v32@0:8@\"_PSPredictionContext\"16@?<v@?@\"NSDictionary\">24"
- "v40@0:8@\"NSDictionary\"16@\"_PSPredictionContext\"24@?<v@?@\"_PSPredictionContext\">32"
- "validateCoreMLModelWithRawInput:predictionContext:"
- "validateCoreMLScoringModelWithRawInput:predictionContext:reply:"

```
