## coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x41420
-  __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_stubs: 0x4400
-  __TEXT.__objc_methlist: 0x16bc
-  __TEXT.__const: 0x1008
-  __TEXT.__objc_methname: 0x5494
-  __TEXT.__oslogstring: 0x2622
-  __TEXT.__cstring: 0x419b
-  __TEXT.__objc_classname: 0x8c5
-  __TEXT.__objc_methtype: 0x2500
-  __TEXT.__gcc_except_tab: 0x5ac
+1656.100.223.0.0
+  __TEXT.__text: 0x3fcf4
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_stubs: 0x43e0
+  __TEXT.__objc_methlist: 0x2234
+  __TEXT.__const: 0x1030
+  __TEXT.__objc_methname: 0x5567
+  __TEXT.__oslogstring: 0x265c
+  __TEXT.__cstring: 0x4197
+  __TEXT.__objc_classname: 0x8e6
+  __TEXT.__objc_methtype: 0x2505
+  __TEXT.__gcc_except_tab: 0x578
   __TEXT.__dlopen_cstrs: 0x269
-  __TEXT.__unwind_info: 0xe10
-  __DATA_CONST.__auth_got: 0x5e0
+  __TEXT.__unwind_info: 0xe20
+  __DATA_CONST.__auth_got: 0x5d8
   __DATA_CONST.__got: 0x460
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x2b48
-  __DATA_CONST.__cfstring: 0x1a60
+  __DATA_CONST.__const: 0x2ab8
+  __DATA_CONST.__cfstring: 0x1a80
   __DATA_CONST.__objc_classlist: 0x168
-  __DATA_CONST.__objc_protolist: 0x1c0
+  __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_intobj: 0x390
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x99b0
-  __DATA.__objc_selrefs: 0x1420
-  __DATA.__objc_ivar: 0x228
+  __DATA.__objc_const: 0x8be8
+  __DATA.__objc_selrefs: 0x1500
+  __DATA.__objc_ivar: 0x23c
   __DATA.__objc_data: 0xe10
-  __DATA.__data: 0x1b70
+  __DATA.__data: 0x1be0
   __DATA.__bss: 0x268
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1FDEA96-FB8C-3A27-BB43-3EF374C55194
-  Functions: 1205
-  Symbols:   342
-  CStrings:  2339
+  UUID: 4F67089B-5A49-334C-8775-48EF9A590673
+  Functions: 1437
+  Symbols:   341
+  CStrings:  2349
 
Symbols:
+ _LACErrorCodeRequestFailed
+ _OBJC_CLASS_$_LACAnalyticsData
+ _OBJC_CLASS_$_LACAnalyticsProcessor
+ _OBJC_CLASS_$_LACAnalyticsSession
+ _OBJC_CLASS_$_LACConcurrentEvaluationController
+ _OBJC_CLASS_$_LACConcurrentEvaluationManager
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
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "@\"<LACConcurrentEvaluationManaging>\""
+ "@\"<LACConcurrentEvaluationService>\""
+ "@\"<LACContextCallbackXPC>\""
+ "@\"<LACContextCallbackXPC>\"16@0:8"
+ "@\"<LACDTORatchetSEPInterface>\""
+ "@\"<LACRemoteContextOwnership>\""
+ "@\"<LACRemoteUIHost>\""
+ "@\"LACAnalyticsSession\""
+ "@\"LACDTORatchetStateComposite\"8@?0"
+ "@\"NSXPCListener\"24@0:8@\"NSString\"16"
+ "B24@0:8@\"NSUUID\"16"
+ "ConcurrentEvaluationService"
+ "Finished KVS deletion: { key: %d, result: %@, error: %@ }"
+ "LACConcurrentEvaluationService"
+ "LACContextCallbackXPC"
+ "LACContextExternalizationObserving"
+ "LACContextExternalizing"
+ "LACOriginatorProt"
+ "LACRemoteUIHost"
+ "No active analytics session."
+ "No analytics session to finish."
+ "T@\"<LACConcurrentEvaluationService>\",R,N,V_concurrentEvaluations"
+ "T@\"<LACContextCallbackXPC>\",R,N"
+ "T@\"<LACContextCallbackXPC>\",R,N,V_callback"
+ "T@\"<LACEvaluationRequestProcessor>\",R,N"
+ "T@\"<LACRemoteContextOwnership>\",R,N,V_remoteContextRegistration"
+ "_analyticsSession"
+ "_concurrentEvaluations"
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
+ "concurrentEvaluations"
+ "connectRemoteUI:requestID:reply:"
+ "connectionToViewServiceInvalidatedForIdentifier:reply:"
+ "featureFlagConcurrentEvaluationsEnabled"
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
+ "v24@0:8@?<v@?@\"<LACAgentProxyXPC>\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v24@?0@\"<LACRemoteContextOwnership>\"8@\"NSError\"16"
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
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "@\"<LACDTOKVStoreReader>\""
- "@\"<LAContextCallbackXPC>\""
- "@\"<LAContextCallbackXPC>\"16@0:8"
- "@\"<LARemoteContextOwnership>\""
- "@\"<LARemoteUIHost>\""
- "@\"LACDTOGracePeriodState\"8@?0"
- "@\"NSXPCListener\"16@0:8"
- "@24@0:8^{?=iQ{?=[16C]}BQIBQQQQ}16"
- "@32@0:8r^{?=QQQQQQ}16r^{?=iQ{?=[16C]}BQIBQQQQ}24"
- "DTORatchetStateParser"
- "LAContextCallbackXPC"
- "LAContextExternalizationObserverProt"
- "LAContextExternalizationProt"
- "LAOriginatorProt"
- "LARemoteUIHost"
- "No result for request rid: %i"
- "T@\"<LAContextCallbackXPC>\",R,N"
- "T@\"<LAContextCallbackXPC>\",R,N,V_callback"
- "T@\"<LARemoteContextOwnership>\",R,N,V_remoteContextRegistration"
- "_biometryWatchdogDTOFromConfig:status:"
- "_biometryWatchdogGlobalFromConfig:status:"
- "_configFromRatchetState:"
- "_durationFromRatchetStatus:config:"
- "_gracePeriodStateFromConfig:status:"
- "_kvstore"
- "_ratchetStateFromACMRatchetState:"
- "_ratchetUUIDFromACMRatchetState:"
- "_resetDurationFromRatchetStatus:config:"
- "_scaleDuration:"
- "_statusFromRatchetState:"
- "checkClearForIdleExitWithCompletion:"
- "connectRemoteUI:reply:"
- "connectionToViewServiceInvalidated:"
- "d24@0:8d16"
- "d32@0:8^{?=iQ{?=[16C]}BQIBQQQQ}16^{?=QQQQQQ}24"
- "decode:"
- "defaultConfiguration"
- "featureFlagDimpleKeyGracePeriodEnabled"
- "initWithBiometryWatchdogGlobal:biometryWatchdogDTO:"
- "initWithContextProvider:kvstore:"
- "initWithIsRunning:time:minThreshold:maxThreshold:"
- "initWithRawValue:duration:resetDuration:uuid:"
- "initWithTime:maxThreshold:"
- "initWithUUIDBytes:"
- "makeProcessorWithSubprocessors:"
- "nullInstance"
- "q24@0:8^{?=iQ{?=[16C]}BQIBQQQQ}16"
- "ratchetStatusWithConfig:"
- "rawValue"
- "v24@0:8@?<v@?@\"<LAAgentProxyXPC>\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDate\"@\"NSError\">16"
- "v24@?0@\"<LARemoteContextOwnership>\"8@\"NSError\"16"
- "v24@?0@\"LACDTOKVStoreValue\"8@\"NSError\"16"
- "v32@0:8@\"<LARemoteUI>\"16@?<v@?@\"<LAUIMechanism>\"@\"<LABackoffCounter>\"@\"NSError\">24"
- "v40@0:8q16@\"<LAOriginatorProt>\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8q16@\"<LAOriginatorProt>\"24@?<v@?@@\"NSError\">32"
- "v40@0:8q16@\"<LAOriginatorProt>\"24@?<v@?B@\"NSError\">32"
- "v44@0:8B16q20@\"<LAOriginatorProt>\"28@?<v@?B@\"NSError\">36"
- "v48@0:8@\"EvaluationRequest\"16@\"<LAUIDelegate>\"24@\"<LAOriginatorProt>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSData\"16@\"<LAContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
- "v48@0:8@16q24@\"<LAOriginatorProt>\"32@?<v@?B@\"NSError\">40"
- "v56@0:8@\"NSData\"16q24@\"NSDictionary\"32@\"<LAOriginatorProt>\"40@?<v@?B@\"NSError\">48"
- "v64@0:8@\"NSUUID\"16@\"<LAContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
- "{?=QQQQQQ}24@0:8@16"
- "{?=iQ{?=[16C]}BQIBQQQQ}24@0:8@16"

```
