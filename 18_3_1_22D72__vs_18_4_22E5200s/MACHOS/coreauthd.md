## coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x23e98
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_stubs: 0x3380
-  __TEXT.__objc_methlist: 0xfa0
-  __TEXT.__const: 0x160
-  __TEXT.__objc_methname: 0x4438
-  __TEXT.__cstring: 0x260a
-  __TEXT.__objc_classname: 0x6a2
-  __TEXT.__objc_methtype: 0x1f44
-  __TEXT.__oslogstring: 0x15f6
-  __TEXT.__gcc_except_tab: 0x244
-  __TEXT.__unwind_info: 0x810
-  __DATA_CONST.__auth_got: 0x3c8
-  __DATA_CONST.__got: 0x3f0
+1656.100.213.0.1
+  __TEXT.__text: 0x22664
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__objc_stubs: 0x3200
+  __TEXT.__objc_methlist: 0x1934
+  __TEXT.__const: 0x140
+  __TEXT.__objc_methname: 0x41f8
+  __TEXT.__cstring: 0x259c
+  __TEXT.__objc_classname: 0x6a5
+  __TEXT.__objc_methtype: 0x1eab
+  __TEXT.__gcc_except_tab: 0x210
+  __TEXT.__oslogstring: 0x14d1
+  __TEXT.__unwind_info: 0x7b0
+  __DATA_CONST.__auth_got: 0x3c0
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xb70
-  __DATA_CONST.__cfstring: 0xac0
-  __DATA_CONST.__objc_classlist: 0xf8
-  __DATA_CONST.__objc_protolist: 0x178
+  __DATA_CONST.__const: 0xa90
+  __DATA_CONST.__cfstring: 0xae0
+  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x81b0
-  __DATA.__objc_selrefs: 0xf68
-  __DATA.__objc_ivar: 0x178
-  __DATA.__objc_data: 0x9b0
-  __DATA.__data: 0x11a2
-  __DATA.__bss: 0x120
+  __DATA_CONST.__objc_intobj: 0xc0
+  __DATA.__objc_const: 0x72d8
+  __DATA.__objc_selrefs: 0x1010
+  __DATA.__objc_ivar: 0x164
+  __DATA.__objc_data: 0x960
+  __DATA.__data: 0x1202
+  __DATA.__bss: 0x110
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 685
-  Symbols:   259
-  CStrings:  1442
+  Functions: 767
+  Symbols:   257
+  CStrings:  1387
 
Symbols:
+ _LACErrorCodeRequestFailed
+ _OBJC_CLASS_$_LACAnalyticsData
+ _OBJC_CLASS_$_LACAnalyticsProcessor
+ _OBJC_CLASS_$_LACAnalyticsSession
+ _OBJC_CLASS_$_LACConcurrentEvaluationController
+ _OBJC_CLASS_$_LACDTORatchetSEPInterface
+ _OBJC_CLASS_$_LACDTORatchetSEPStateParser
- _LACDTBiometryWatchdogGlobalFallbackTime
- _LACDTORatchetStateDurationInfinite
- _LACErrorCodeInternal
- _OBJC_CLASS_$_LACDTOBiometryWatchdog
- _OBJC_CLASS_$_LACDTOBiometryWatchdogPack
- _OBJC_CLASS_$_LACDTOFeatureEnablementModeCoder
- _OBJC_CLASS_$_LACDTOGracePeriodState
- _OBJC_CLASS_$_LACDTORatchetState
- _OBJC_CLASS_$_LACProcessingConfiguration
CStrings:
+ "\x03#"
+ "@\"<LACConcurrentEvaluationManaging>\""
+ "@\"<LACContextCallbackXPC>\""
+ "@\"<LACContextCallbackXPC>\"16@0:8"
+ "@\"<LACDTORatchetSEPInterface>\""
+ "@\"<LACRemoteUIHost>\""
+ "@\"LACAnalyticsSession\""
+ "@\"LACDTORatchetStateComposite\"8@?0"
+ "@\"NSXPCListener\"24@0:8@\"NSString\"16"
+ "B24@0:8@\"NSUUID\"16"
+ "ConcurrentEvaluationService"
+ "Finished KVS deletion: { key: %d, result: %@, error: %@ }"
+ "LACConcurrentEvaluationService"
+ "LACContextExternalizationObserving"
+ "LACContextExternalizing"
+ "LACOriginatorProt"
+ "LACRemoteUIHost"
+ "No active analytics session."
+ "No analytics session to finish."
+ "T@\"<LACContextCallbackXPC>\",R,N"
+ "T@\"<LACContextCallbackXPC>\",R,N,V_callback"
+ "T@\"<LACEvaluationRequestProcessor>\",R,N"
+ "_analyticsSession"
+ "_manager"
+ "_removeValueForKey:contextUUID:connection:storage:completion:"
+ "_replyQueue"
+ "_sep"
+ "_vendedListeners"
+ "analyticsAction:dismissing:reply:"
+ "analyticsData"
+ "analyticsMechanism:result:reply:"
+ "analyticsMechanism:starting:reply:"
+ "analyticsSessionStarting:dialogID:bundleID:reply:"
+ "anonymousListenerWithIdentifier:"
+ "authenticationAction:dismissing:"
+ "authenticationResult:event:"
+ "authenticationStartedForEvent:"
+ "checkHasPendingUIRequestsWithCompletion:"
+ "connectRemoteUI:requestID:reply:"
+ "connectionToViewServiceInvalidatedForIdentifier:reply:"
+ "fetchConfigurationAndStatus:"
+ "finish"
+ "handleRequest:completion:"
+ "initWithContextProvider:sep:"
+ "initWithDialogID:bundleID:"
+ "initWithManager:replyQueue:"
+ "makeRootProcessorWithSubprocessors:"
+ "restartRequestsForContextID:"
+ "setAnalyticsData:"
+ "setDirty:"
+ "setSession:"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSError\">32"
+ "v40@0:8q16@\"<LACOriginatorProt>\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8q16@\"<LACOriginatorProt>\"24@?<v@?@@\"NSError\">32"
+ "v40@0:8q16@\"<LACOriginatorProt>\"24@?<v@?B@\"NSError\">32"
+ "v44@0:8B16@\"NSString\"20@\"NSString\"28@?<v@?B@\"NSError\">36"
+ "v44@0:8B16@20@28@?36"
+ "v44@0:8B16q20@\"<LACOriginatorProt>\"28@?<v@?B@\"NSError\">36"
+ "v48@0:8@\"EvaluationRequest\"16@\"<LAUIDelegate>\"24@\"<LACOriginatorProt>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
+ "v48@0:8@16q24@\"<LACOriginatorProt>\"32@?<v@?B@\"NSError\">40"
+ "v56@0:8@\"NSData\"16q24@\"NSDictionary\"32@\"<LACOriginatorProt>\"40@?<v@?B@\"NSError\">48"
+ "v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
+ "weakToStrongObjectsMapTable"
- "\x02\x11\x11"
- "\x02#"
- "%s %d, %d on %@"
- "-[CoachingFeedbackFilter dispatchNowOrWhenFeedbackDurationAchieved:finish:block:]"
- "@\"<LACDTOKVStoreReader>\""
- "@\"<LAContextCallbackXPC>\""
- "@\"<LAContextCallbackXPC>\"16@0:8"
- "@\"<LARemoteUIHost>\""
- "@\"LACDTOGracePeriodState\"8@?0"
- "@\"MechanismBase<LARemoteUI>\""
- "@\"NSNumber\""
- "@\"NSSet\""
- "@\"NSXPCListener\"16@0:8"
- "@24@0:8^{?=iQ{?=[16C]}BQIBQQQQ}16"
- "@32@0:8r^{?=QQQQQQ}16r^{?=iQ{?=[16C]}BQIBQQQQ}24"
- "@48@0:8@16@24d32d40"
- "CoachingFeedbackFilter"
- "DTORatchetStateParser"
- "LAContextExternalizationObserverProt"
- "LAContextExternalizationProt"
- "LAOriginatorProt"
- "LARemoteUIHost"
- "No result for request rid: %i"
- "T@\"<LAContextCallbackXPC>\",R,N"
- "T@\"<LAContextCallbackXPC>\",R,N,V_callback"
- "T@\"MechanismBase<LARemoteUI>\",W,N,V_delegate"
- "T@\"NSSet\",R,N,V_feedbackSet"
- "TB,R,N,GisFinished,V_finished"
- "Td,R,N,V_feedbackDuration"
- "Td,R,N,V_iconDuration"
- "_biometryWatchdogDTOFromConfig:status:"
- "_biometryWatchdogGlobalFromConfig:status:"
- "_configFromRatchetState:"
- "_delegate"
- "_dispatchPendingBlocks"
- "_doneWaiting"
- "_durationFromRatchetStatus:config:"
- "_feedbackDuration"
- "_feedbackSet"
- "_finished"
- "_gracePeriodStateFromConfig:status:"
- "_iconDuration"
- "_kvstore"
- "_lastFeedback"
- "_lastSentFeedback"
- "_pendingBlocks"
- "_ratchetStateFromACMRatchetState:"
- "_ratchetUUIDFromACMRatchetState:"
- "_resetDurationFromRatchetStatus:config:"
- "_scaleDuration:"
- "_sendFeedback:"
- "_statusFromRatchetState:"
- "_timeoutForFeedback:"
- "_waiting"
- "bytes"
- "checkClearForIdleExitWithCompletion:"
- "connectRemoteUI:reply:"
- "connectionToViewServiceInvalidated:"
- "d"
- "d16@0:8"
- "d24@0:8d16"
- "d24@0:8q16"
- "d32@0:8^{?=iQ{?=[16C]}BQIBQQQQ}16^{?=QQQQQQ}24"
- "decode:"
- "defaultConfiguration"
- "delegate"
- "dispatchNowOrWhenFeedbackDurationAchieved:finish:block:"
- "dispatched directly"
- "done waiting, found pending feedback: %d"
- "done waiting, no pending feedback"
- "featureFlagDimpleKeyGracePeriodEnabled"
- "feedbackDuration"
- "feedbackSet"
- "finished"
- "iconDuration"
- "ignoring feedback (already finished)"
- "ignoring repeating feedback"
- "initWithBiometryWatchdogGlobal:biometryWatchdogDTO:"
- "initWithContextProvider:kvstore:"
- "initWithDelegate:feedbackSet:feedbackDuration:iconDuration:"
- "initWithIsRunning:time:minThreshold:maxThreshold:"
- "initWithRawValue:duration:resetDuration:uuid:"
- "initWithTime:maxThreshold:"
- "initWithUUIDBytes:"
- "intValue"
- "isEqualToNumber:"
- "isFinished"
- "makeProcessorWithSubprocessors:"
- "mechanismEvent:value:reply:"
- "noResponseEventWithParams:"
- "nullInstance"
- "pending block[%d]"
- "pending feedback: %d"
- "q24@0:8^{?=iQ{?=[16C]}BQIBQQQQ}16"
- "ratchetStatusWithConfig:"
- "rawValue"
- "scheduleFeedback:"
- "scheduling feedback: %d"
- "scheduling pending block[%d]"
- "sending feedback: %d, will wait %.2f sec"
- "v24@0:8@?<v@?@\"NSDate\"@\"NSError\">16"
- "v24@0:8q16"
- "v24@?0@\"LACDTOKVStoreValue\"8@\"NSError\"16"
- "v32@0:8@\"<LARemoteUI>\"16@?<v@?@\"<LAUIMechanism>\"@\"<LABackoffCounter>\"@\"NSError\">24"
- "v32@0:8B16B20@?24"
- "v40@0:8q16@\"<LAOriginatorProt>\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8q16@\"<LAOriginatorProt>\"24@?<v@?@@\"NSError\">32"
- "v40@0:8q16@\"<LAOriginatorProt>\"24@?<v@?B@\"NSError\">32"
- "v44@0:8B16q20@\"<LAOriginatorProt>\"28@?<v@?B@\"NSError\">36"
- "v48@0:8@\"EvaluationRequest\"16@\"<LAUIDelegate>\"24@\"<LAOriginatorProt>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSData\"16@\"<LAContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
- "v48@0:8@16q24@\"<LAOriginatorProt>\"32@?<v@?B@\"NSError\">40"
- "v56@0:8@\"NSData\"16q24@\"NSDictionary\"32@\"<LAOriginatorProt>\"40@?<v@?B@\"NSError\">48"
- "v64@0:8@\"NSUUID\"16@\"<LAContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
- "won't dispatch, already finished"
- "{?=QQQQQQ}24@0:8@16"
- "{?=iQ{?=[16C]}BQIBQQQQ}24@0:8@16"
- "\x81"

```
