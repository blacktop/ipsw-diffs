## MicroLocationUtilities

> `/System/Library/PrivateFrameworks/MicroLocationUtilities.framework/MicroLocationUtilities`

```diff

-62.0.3.0.0
-  __TEXT.__text: 0x70d0
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0xc60
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x3a6
-  __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__oslogstring: 0x201
-  __TEXT.__unwind_info: 0x338
-  __TEXT.__objc_classname: 0x1ae
-  __TEXT.__objc_methname: 0x156a
-  __TEXT.__objc_methtype: 0x97b
-  __TEXT.__objc_stubs: 0x1440
-  __DATA_CONST.__got: 0xe0
+106.0.2.0.0
+  __TEXT.__text: 0x7690
+  __TEXT.__objc_methlist: 0xd80
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x3d3
+  __TEXT.__gcc_except_tab: 0xc8
+  __TEXT.__oslogstring: 0x1e5
+  __TEXT.__unwind_info: 0x340
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x5b8
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x758
+  __DATA_CONST.__objc_selrefs: 0x7e0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x2e0
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x300
-  __AUTH_CONST.__objc_const: 0x15f0
-  __AUTH.__objc_data: 0x230
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__got: 0x118
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x320
+  __AUTH_CONST.__objc_const: 0x1820
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x5c
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_data: 0x460
+  __DATA.__bss: 0x60
+  __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C939C2BB-645B-3174-B0AB-4E886AB49025
-  Functions: 255
-  Symbols:   1101
-  CStrings:  474
+  UUID: 56109878-10BE-3285-AAE4-6C848C4C9448
+  Functions: 283
+  Symbols:   1206
+  CStrings:  81
 
Symbols:
+ +[ULRotationMatrixUtils leftBudYawFromQuaternion:]
+ +[ULRotationMatrixUtils quaternionFromColumnMajorMatrix:]
+ +[ULRotationMatrixUtils quaternionFromTransform:]
+ +[ULRotationMatrixUtils quaternionFromYaw:]
+ +[ULRotationMatrixUtils rightBudYawFromQuaternion:]
+ +[ULRotationMatrixUtils rot2quat:quaternion:]
+ +[ULRotationMatrixUtils rotationMatrixFromQuaternion:]
+ +[ULRotationMatrixUtils yawFromQuaternion:]
+ +[ULTimerFactory _instance]
+ +[ULTimerFactory _instance].cold.1
+ +[ULTimerFactory timerOnPrimaryQueueWithInterval:repeats:block:]
+ +[ULTimerFactory(queueSetter) setPrimaryQueue:]
+ -[ULTimer .cxx_destruct]
+ -[ULTimer dealloc]
+ -[ULTimer init]
+ -[ULTimer invalidate]
+ -[ULTimer setTimerSource:]
+ -[ULTimer timerSource]
+ -[ULTimer(init) initWithInterval:repeats:queue:block:]
+ -[ULTimer(testing) isTimerSourceNil]
+ -[ULTimerFactory .cxx_destruct]
+ -[ULTimerFactory primaryQueue]
+ -[ULTimerFactory setPrimaryQueue:]
+ GCC_except_table6
+ _NSInternalInconsistencyException
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_ULRotationMatrixUtils
+ _OBJC_CLASS_$_ULTimer
+ _OBJC_CLASS_$_ULTimerFactory
+ _OBJC_IVAR_$_ULTimer._timerSource
+ _OBJC_IVAR_$_ULTimerFactory._primaryQueue
+ _OBJC_METACLASS_$_ULRotationMatrixUtils
+ _OBJC_METACLASS_$_ULTimer
+ _OBJC_METACLASS_$_ULTimerFactory
+ _ULLeftBudYawFromQuaternion
+ _ULQuaternionFromTransform
+ _ULQuaternionFromYaw
+ _ULRightBudYawFromQuaternion
+ _ULRotationNotAvailable
+ _ULYawFromQuaternion
+ _ULYawNotAvailable
+ __OBJC_$_CLASS_METHODS_ULRotationMatrixUtils
+ __OBJC_$_CLASS_METHODS_ULTimerFactory(queueSetter)
+ __OBJC_$_INSTANCE_METHODS_ULTimer(init|testing)
+ __OBJC_$_INSTANCE_METHODS_ULTimerFactory
+ __OBJC_$_INSTANCE_VARIABLES_ULTimer
+ __OBJC_$_INSTANCE_VARIABLES_ULTimerFactory
+ __OBJC_$_PROP_LIST_ULFuture.167
+ __OBJC_$_PROP_LIST_ULPromise.182
+ __OBJC_$_PROP_LIST_ULTimer
+ __OBJC_$_PROP_LIST_ULTimerFactory
+ __OBJC_CLASS_RO_$_ULRotationMatrixUtils
+ __OBJC_CLASS_RO_$_ULTimer
+ __OBJC_CLASS_RO_$_ULTimerFactory
+ __OBJC_METACLASS_RO_$_ULRotationMatrixUtils
+ __OBJC_METACLASS_RO_$_ULTimer
+ __OBJC_METACLASS_RO_$_ULTimerFactory
+ ___27+[ULTimerFactory _instance]_block_invoke
+ ___47-[ULEventMonitor removeObserver:fromEventName:]_block_invoke.25
+ ___54-[ULTimer(init) initWithInterval:repeats:queue:block:]_block_invoke
+ ___69-[ULDarwinNotificationHelper addObserverForNotificationName:handler:]_block_invoke.29
+ ___block_descriptor_49_e8_32bs40w_e5_v8?0ls32l8w40l8
+ ___block_literal_global.64
+ ___sincosf_stret
+ __dispatch_main_q
+ __dispatch_source_type_timer
+ __instance.instance
+ __instance.onceToken
+ _atan2f
+ _dispatch_activate
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_time
+ _objc_claimAutoreleasedReturnValue
+ _objc_exception_throw
+ _objc_msgSend$_instance
+ _objc_msgSend$exceptionWithName:reason:userInfo:
+ _objc_msgSend$initWithInterval:repeats:queue:block:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isRunningInXCTestEnvironment
+ _objc_msgSend$leftBudYawFromQuaternion:
+ _objc_msgSend$primaryQueue
+ _objc_msgSend$quaternionFromTransform:
+ _objc_msgSend$quaternionFromYaw:
+ _objc_msgSend$rightBudYawFromQuaternion:
+ _objc_msgSend$rot2quat:quaternion:
+ _objc_msgSend$setPrimaryQueue:
+ _objc_msgSend$setTimerSource:
+ _objc_msgSend$timerSource
+ _objc_msgSend$yawFromQuaternion:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x8
- -[ULDarwinNotificationHelper stateForNotificationName:]
- __OBJC_$_PROP_LIST_ULFuture.168
- __OBJC_$_PROP_LIST_ULPromise.183
- ___47-[ULEventMonitor removeObserver:fromEventName:]_block_invoke.26
- ___55-[ULDarwinNotificationHelper stateForNotificationName:]_block_invoke
- ___55-[ULDarwinNotificationHelper stateForNotificationName:]_block_invoke.cold.1
- ___69-[ULDarwinNotificationHelper addObserverForNotificationName:handler:]_block_invoke.30
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_literal_global.65
- _notify_get_state
- _objc_msgSend$removeObserverForNotificationName:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
CStrings:
+ "%@ cannot be initialized directly"
- "#"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<ULFuture>\"24@0:8@?<@\"<ULFuture>\"@?@\"NSError\">16"
- "@\"<ULFuture>\"24@0:8@?<@\"<ULFuture>\"@?@>16"
- "@\"<ULFuture>\"24@0:8@?<@@?@>16"
- "@\"<ULFuture>\"32@0:8@\"<ULScheduler>\"16@?<@\"<ULFuture>\"@?@\"NSError\">24"
- "@\"<ULFuture>\"32@0:8@\"<ULScheduler>\"16@?<@\"<ULFuture>\"@?@>24"
- "@\"<ULFuture>\"32@0:8@\"<ULScheduler>\"16@?<@@?@>24"
- "@\"NSConditionLock\""
- "@\"NSError\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"ULFuture\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8^{__CFString=}16"
- "@24@0:8d16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@\"NSDate\"16^@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@32@0:8d16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@?24@32"
- "@48@0:8{?=[8I]}16"
- "@?"
- "@?16@0:8"
- "@?<v@?@\"NSError\">16@0:8"
- "@?<v@?@@\"NSError\">16@0:8"
- "@?<v@?B@\"NSError\">16@0:8"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSError\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B32@0:8@16@\"NSError\"24"
- "B32@0:8@16@24"
- "Could not get state for: %@"
- "MicroLocationUtilities"
- "NSCopying"
- "NSObject"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q24@0:8q16"
- "T#,&,N,V_class"
- "T#,R"
- "T@\"<ULScheduler>\",R"
- "T@\"NSMutableDictionary\",&,N,V_keyToValueMap"
- "T@\"NSMutableDictionary\",&,N,V_observersMap"
- "T@\"NSMutableDictionary\",&,N,V_registrations"
- "T@\"NSMutableDictionary\",&,N,V_valueToKeyMap"
- "T@\"NSNumber\",&,N,V_registrationToken"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",&,N,V_notificationName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"ULFuture\",R,V_future"
- "T@,R,N"
- "T@,R,N,V_first"
- "T@,R,N,V_second"
- "T@,W,N,V_object"
- "T@?,C,N,V_handler"
- "T@?,R"
- "TB,R,GisCancelled"
- "TB,R,GisFinished"
- "TQ,R"
- "Tr^v,N,V_observer"
- "ULBidirectionalDictionary"
- "ULCancelable"
- "ULDarwinNotificationHelper"
- "ULDarwinNotificationRecord"
- "ULEvent"
- "ULEventMonitor"
- "ULFeatureFlags"
- "ULFuture"
- "ULImmediateScheduler"
- "ULMemoryLoadHelper"
- "ULNumericUtilities"
- "ULObjectCacheNSString"
- "ULObserverRecord"
- "ULPair"
- "ULPlatform"
- "ULPromise"
- "ULPromisePrivate"
- "ULQueueScheduler"
- "ULSameSpaceUtilities"
- "ULScheduler"
- "ULTapToRadar"
- "ULUserNotification"
- "ULWeakProxy"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_addCompletionBlock:"
- "_always:withBlock:scheduler:"
- "_class"
- "_classificationFromULTapToRadarClassification:"
- "_completionBlocks"
- "_error"
- "_finishWithFuture:"
- "_first"
- "_flushCompletionBlocks"
- "_future"
- "_handleDarwinNotificationCallback:"
- "_handler"
- "_join:ignoreFailures:"
- "_keyToValueMap"
- "_mobileGestaltAnswerForQuestion:"
- "_notificationName"
- "_nts_isFinished"
- "_object"
- "_observer"
- "_observersMap"
- "_pid"
- "_postNotificationWithAlertLevel:alertOptions:handler:"
- "_presentWithAlertLevel:title:message:defaultButton:cancelButton:otherButton:handler:"
- "_queue"
- "_recover:withBlock:scheduler:"
- "_registrationToken"
- "_registrations"
- "_reproducibilityFromULTapToRadarReproducibility:"
- "_responseButtonFromOptionFlags:"
- "_result"
- "_rusage"
- "_second"
- "_signingIdentityForAuditToken:"
- "_stateLock"
- "_then:withBlock:scheduler:"
- "_userNotificationAlertLevelFlagsFromAlertLevel:"
- "_valueToKeyMap"
- "absoluteVerticalDistanceBetweenPredictionCoordinates:andLabelCoordinates:"
- "addFailureBlock:"
- "addObject:"
- "addObserver:eventName:handler:"
- "addObserverForNotificationName:handler:"
- "addSuccessBlock:"
- "allKeys"
- "allValues"
- "always:"
- "appendFormat:"
- "appendString:"
- "array"
- "arrayByAddingObject:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "auditToken"
- "autorelease"
- "boolErrorCompletionHandlerAdapter"
- "boolValue"
- "buildVersion"
- "cancel"
- "cancelled"
- "chain:"
- "class"
- "code"
- "combine:"
- "completionHandlerAdapter"
- "condition"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "cosineSimilarityBetweenPredictionProbabilities:andLabelProbabilities:"
- "cosineSimilarityBetweenPredictionProbabilities:withPreCalculatedMagnitude:andLabelProbabilities:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDraft:forProcessNamed:withDisplayReason:completionHandler:"
- "createRadarWithComponentName:componentVersion:componentID:classification:reproducibility:title:description:extensionIDs:processName:displayReason:isUserInitiated:completionHandler:"
- "d16@0:8"
- "d24@0:8@16"
- "d32@0:8@16@24"
- "d40@0:8@16d24@32"
- "d48@0:81632"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "description"
- "deviceClass"
- "dictionary"
- "didCancel"
- "dispatchQueueSchedulerWithQueue:"
- "distantFuture"
- "distantPast"
- "domain"
- "dotProduct:vectorB:"
- "doubleValue"
- "enumerateObjectsUsingBlock:"
- "errorOnlyCompletionHandlerAdapter"
- "errorWithDomain:code:userInfo:"
- "eventName"
- "featureFlagsDescription"
- "finishWithError:"
- "finishWithFuture:"
- "finishWithResult:"
- "finishWithResult:error:"
- "finished"
- "first"
- "firstObject"
- "formatBytes:"
- "forwardInvocation:"
- "forwardingTargetForSelector:"
- "future"
- "futureWithBlock:"
- "futureWithError:"
- "futureWithResult:"
- "getNumberOfObserversForEventName:"
- "globalAsyncScheduler"
- "handler"
- "hasBooleanEntitlement:"
- "hash"
- "horizontalDistanceSquaredBetweenPredictionCoordinates:andLabelCoordinates:"
- "i"
- "immediateScheduler"
- "init"
- "initWithCondition:"
- "initWithFirst:second:"
- "initWithFormat:"
- "initWithName:version:identifier:"
- "initWithNotificationName:registrationToken:handler:"
- "initWithObject:"
- "initWithQueue:"
- "instanceMethodSignatureForSelector:"
- "intValue"
- "integerValue"
- "isCancelled"
- "isEqual:"
- "isFinished"
- "isInternalInstall"
- "isIpad"
- "isIphone"
- "isIpod"
- "isKindOfClass:"
- "isMac"
- "isMacBook"
- "isMemberOfClass:"
- "isProxy"
- "isRunningInXCTestEnvironment"
- "join:"
- "keyForObject:"
- "keyToValueMap"
- "latestEventAfterAddingObserverForEventName:"
- "load"
- "lock"
- "lockWhenCondition:beforeDate:"
- "magnitudeOfVector:"
- "map:"
- "measure"
- "member:"
- "methodSignatureForSelector:"
- "mutableCopy"
- "name"
- "notificationName"
- "null"
- "nullFuture"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "object"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observer"
- "observersMap"
- "onScheduler:addFailureBlock:"
- "onScheduler:addSuccessBlock:"
- "onScheduler:always:"
- "onScheduler:futureWithBlock:"
- "onScheduler:map:"
- "onScheduler:recover:"
- "onScheduler:then:"
- "pairWithFirst:second:"
- "peakLoad"
- "performAsyncBlock:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performSyncBlock:"
- "pil"
- "platformInfo"
- "postEvent:"
- "presentWithAlertLevel:title:message:defaultButton:cancelButton:otherButton:handler:"
- "promise"
- "q24@0:8Q16"
- "q24@0:8q16"
- "queue"
- "r^v"
- "r^v16@0:8"
- "recover:"
- "registrationToken"
- "registrations"
- "release"
- "removeAllObjects"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObserver:"
- "removeObserver:fromEventName:"
- "removeObserverForNotificationName:"
- "reset"
- "respondsToSelector:"
- "result"
- "result:"
- "resultBeforeDate:error:"
- "resultIfAvailable"
- "resultIfAvailable:"
- "resultWithTimeout:error:"
- "retain"
- "retainCount"
- "second"
- "self"
- "sequence:"
- "setClass:"
- "setClassification:"
- "setComponent:"
- "setDiagnosticExtensionIDs:"
- "setHandler:"
- "setIsUserInitiated:"
- "setKeyToValueMap:"
- "setName:"
- "setNotificationName:"
- "setObject:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObserver:"
- "setObserversMap:"
- "setProblemDescription:"
- "setQueue:"
- "setRegistrationToken:"
- "setRegistrations:"
- "setReproducibility:"
- "setTitle:"
- "setValueToKeyMap:"
- "shared"
- "signingIdentity"
- "signingIdentityForSelf"
- "startMonitoring:"
- "stateForNotificationName:"
- "stopMonitoring:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "sumOfVector:"
- "superclass"
- "supportsExclave"
- "then:"
- "tryCancel"
- "ul_allWhere:"
- "ul_cachedInstanceForNSString:"
- "ul_containsObjectPassingTest:"
- "ul_firstWhere:"
- "unlock"
- "unlockWithCondition:"
- "v108@0:8@16@24@32q40q48@56@64@72@80@88B96@?100"
- "v16@0:8"
- "v24@0:8#16"
- "v24@0:8@\"<ULFuture>\"16"
- "v24@0:8@\"ULFuture\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@>16"
- "v24@0:8r^v16"
- "v32@0:8@\"<ULScheduler>\"16@?<v@?>24"
- "v32@0:8@\"<ULScheduler>\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"<ULScheduler>\"16@?<v@?@>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8r^v16@24"
- "v40@0:8@16@?24@32"
- "v40@0:8q16@24@?32"
- "v40@0:8r^v16@24@?32"
- "v72@0:8q16@24@32@40@48@56@?64"
- "valueForEntitlement:"
- "valueToKeyMap"
- "weakObjectsHashTable"
- "zone"
- "{rusage_info_v4=\"ri_uuid\"[16C]\"ri_user_time\"Q\"ri_system_time\"Q\"ri_pkg_idle_wkups\"Q\"ri_interrupt_wkups\"Q\"ri_pageins\"Q\"ri_wired_size\"Q\"ri_resident_size\"Q\"ri_phys_footprint\"Q\"ri_proc_start_abstime\"Q\"ri_proc_exit_abstime\"Q\"ri_child_user_time\"Q\"ri_child_system_time\"Q\"ri_child_pkg_idle_wkups\"Q\"ri_child_interrupt_wkups\"Q\"ri_child_pageins\"Q\"ri_child_elapsed_abstime\"Q\"ri_diskio_bytesread\"Q\"ri_diskio_byteswritten\"Q\"ri_cpu_time_qos_default\"Q\"ri_cpu_time_qos_maintenance\"Q\"ri_cpu_time_qos_background\"Q\"ri_cpu_time_qos_utility\"Q\"ri_cpu_time_qos_legacy\"Q\"ri_cpu_time_qos_user_initiated\"Q\"ri_cpu_time_qos_user_interactive\"Q\"ri_billed_system_time\"Q\"ri_serviced_system_time\"Q\"ri_logical_writes\"Q\"ri_lifetime_max_phys_footprint\"Q\"ri_instructions\"Q\"ri_cycles\"Q\"ri_billed_energy\"Q\"ri_serviced_energy\"Q\"ri_interval_max_phys_footprint\"Q\"ri_runnable_time\"Q}"

```
