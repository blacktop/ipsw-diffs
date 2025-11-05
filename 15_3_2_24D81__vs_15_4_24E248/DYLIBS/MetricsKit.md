## MetricsKit

> `/System/Library/PrivateFrameworks/MetricsKit.framework/Versions/A/MetricsKit`

```diff

 2.8.5.0.0
-  __TEXT.__text: 0x2f4f0
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x364c
+  __TEXT.__text: 0x2f424
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_methlist: 0x3cfc
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x2659
+  __TEXT.__cstring: 0x2657
   __TEXT.__gcc_except_tab: 0xba0
   __TEXT.__oslogstring: 0xa44
-  __TEXT.__unwind_info: 0xdb8
+  __TEXT.__unwind_info: 0xdc0
   __TEXT.__objc_classname: 0x982
   __TEXT.__objc_methname: 0x768a
   __TEXT.__objc_methtype: 0xd43

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f30
+  __DATA_CONST.__objc_selrefs: 0x2040
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1e8
-  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__auth_got: 0x2c0
   __AUTH_CONST.__const: 0x1040
   __AUTH_CONST.__cfstring: 0x3080
-  __AUTH_CONST.__objc_const: 0xbf60
+  __AUTH_CONST.__objc_const: 0xb340
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH.__objc_data: 0x1db0
   __DATA.__objc_ivar: 0x2ec

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
-  UUID: 076A2B12-3947-34A6-A757-F5F124507A36
-  Functions: 1243
-  Symbols:   3772
-  CStrings:  2626
+  UUID: F03254ED-9A6B-382A-92CE-D01C07FB3CEF
+  Functions: 1251
+  Symbols:   3779
+  CStrings:  2625
 
Symbols:
+ +[MTEventRecorderAMSMetricsDelegate amsMetricsObjectCache].cold.1
+ +[MTPromise _globalPromiseStorageAccessQueue].cold.1
+ +[MTPromise _globalPromiseStorage].cold.1
+ +[MTTreatment treatmentWithConfigData:].cold.1
+ +[MTTreatmentProfile treatmentProfileWithConfigData:].cold.1
+ -[MTEnvironmentDeviceDelegate osVersion].cold.1
+ MTMetricsKitOSLog.cold.1
+ __52-[MTMediaActivityEventHandler didCreateMetricsData:]_block_invoke.cold.1
- _strcmp
Functions:
~ ___40-[MTPeriodicQueue setFlushTimeInterval:]_block_invoke : 44 -> 48
~ ___40-[MTPeriodicQueue setFlushTimerEnabled:]_block_invoke : 48 -> 52
~ -[MTPeriodicQueue __beginFlushTimer] : 304 -> 300
~ -[MTEventRecorderAMSMetricsDelegate initWithContainerId:amsBag:] : 712 -> 708
~ +[MTEventRecorderAMSMetricsDelegate amsMetricsObjectCache] : 84 -> 68
~ -[MTEventRecorderAMSMetricsDelegate periodicQueueForTopic:] : 540 -> 536
~ ___59-[MTEventRecorderAMSMetricsDelegate periodicQueueForTopic:]_block_invoke : 108 -> 104
~ -[MTEventRecorderAMSMetricsDelegate _beginTransaction] : 236 -> 240
~ -[MTEventRecorderAMSMetricsDelegate recordEvent:toTopic:] : 636 -> 632
~ -[MTJSContextEventFilter jsContext] : 516 -> 512
~ _MTMetricsKitOSLog : 84 -> 68
~ -[MTConfig setDelegate:] : 200 -> 196
~ -[MTConfig eventDataTimeout] : 276 -> 272
~ ___28-[MTConfig eventDataTimeout]_block_invoke : 252 -> 248
~ -[MTEventRecorder setDelegate:] : 200 -> 196
~ -[MTHLSVideoPlaylist indexOfLastRollItemWithStartBeforePosition:] : 308 -> 296
~ -[MTEnvironmentDeviceDelegate osVersion] : 84 -> 68
~ ___48+[MTReflectUtil removeNullValuesFromDictionary:]_block_invoke : 116 -> 112
~ -[MTEnvironment setDelegate:] : 200 -> 196
~ -[MTSystem queue] : 352 -> 348
~ -[MTTreatmentAction performAction:atKeyIndex:context:] : 1036 -> 1056
~ -[MTPageEventHandler didCreateMetricsData:] : 212 -> 208
~ -[MTPromise catchWithBlock:] : 328 -> 324
~ -[MTPromise thenWithBlock:] : 328 -> 324
~ -[MTPromise finishWithResult:error:] : 956 -> 952
~ -[MTPromise boolCompletionHandlerAdapter] : 232 -> 228
~ -[MTPromise completionHandlerAdapter] : 232 -> 228
~ -[MTPromise errorOnlyCompletionHandlerAdapter] : 232 -> 228
~ -[MTPromise nilValueCompletionHandlerAdapter] : 232 -> 228
~ +[MTPromise _configureAllPromise:withResults:promises:currentPromiseIndex:] : 528 -> 524
~ ___75+[MTPromise _configureAllPromise:withResults:promises:currentPromiseIndex:]_block_invoke : 176 -> 172
~ +[MTPromise _configureAnyPromise:withPromises:currentPromiseIndex:] : 476 -> 472
~ +[MTPromise _globalPromiseStorage] : 84 -> 68
~ +[MTPromise _globalPromiseStorageAccessQueue] : 84 -> 68
~ -[MTInterprocessChangeNotifier notify] : 60 -> 56
~ ___52-[MTMediaActivityEventHandler didCreateMetricsData:]_block_invoke : 492 -> 476
~ -[MTPromiseWithTimeout initWithTimeout:queue:timeoutBlock:] : 496 -> 492
~ -[MTSampling isSampledInWithEventType:sessionSamplingPercentage:sessionDurationMs:] : 812 -> 808
~ _MTConfigurationError : 408 -> 412
~ -[MTEventDataProvider knownFieldMethodsForKnownFields:] : 600 -> 564
~ -[MTEventDataProvider processMetricsData:performanceData:] : 916 -> 912
~ -[NSDictionary(Utilities) mt_deepCopy] : 684 -> 612
~ ___37-[MTConstraintTreatmentFilter apply:]_block_invoke : 348 -> 344
~ +[MTTreatment treatmentWithConfigData:] : 304 -> 288
~ -[NSObject(Utilities) mt_nullableValueForKeyPathArray:index:] : 1104 -> 1100
~ ___50-[MTMetricsDataPredicate evaluateWithMetricsData:]_block_invoke : 476 -> 472
~ -[MTCallerSuppliedFields mergedFields] : 412 -> 408
~ +[MTTreatmentProfile treatmentProfileWithConfigData:] : 304 -> 288
~ ___40-[MTTreatmentProfile performTreatments:]_block_invoke : 120 -> 112
~ -[MTMetricsData toDictionary] : 616 -> 600

```
