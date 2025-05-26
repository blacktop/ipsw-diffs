## coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-1394.62.1.0.0
-  __TEXT.__text: 0x227dc
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0x2240
-  __TEXT.__objc_methlist: 0xb84
-  __TEXT.__const: 0xf84
-  __TEXT.__objc_methname: 0x2c2c
-  __TEXT.__cstring: 0x1ee2
-  __TEXT.__objc_classname: 0x3d1
-  __TEXT.__objc_methtype: 0x139f
-  __TEXT.__oslogstring: 0x12e8
-  __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__unwind_info: 0x948
-  __DATA_CONST.__auth_got: 0x678
-  __DATA_CONST.__got: 0x98
+1394.82.1.0.0
+  __TEXT.__text: 0x25bac
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_stubs: 0x2c00
+  __TEXT.__objc_methlist: 0xe34
+  __TEXT.__const: 0xfa4
+  __TEXT.__objc_methname: 0x3bba
+  __TEXT.__cstring: 0x2138
+  __TEXT.__objc_classname: 0x50f
+  __TEXT.__objc_methtype: 0x1a70
+  __TEXT.__oslogstring: 0x1389
+  __TEXT.__gcc_except_tab: 0x234
+  __TEXT.__dlopen_cstrs: 0x9b
+  __TEXT.__unwind_info: 0xa58
+  __DATA_CONST.__auth_got: 0x6c8
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1ea8
-  __DATA_CONST.__cfstring: 0xb20
-  __DATA_CONST.__objc_classlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__const: 0x2128
+  __DATA_CONST.__cfstring: 0xbe0
+  __DATA_CONST.__objc_classlist: 0xe8
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x4900
-  __DATA.__objc_selrefs: 0xa68
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x1b8
-  __DATA.__objc_superrefs: 0x80
-  __DATA.__objc_ivar: 0xe4
-  __DATA.__objc_data: 0x730
-  __DATA.__data: 0xfe8
-  __DATA.__bss: 0x148
+  __DATA.__objc_const: 0x6678
+  __DATA.__objc_selrefs: 0xd50
+  __DATA.__objc_protorefs: 0x40
+  __DATA.__objc_classrefs: 0x2b8
+  __DATA.__objc_superrefs: 0x90
+  __DATA.__objc_ivar: 0x134
+  __DATA.__objc_data: 0x910
+  __DATA.__data: 0x12e8
+  __DATA.__bss: 0x168
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 758
-  Symbols:   279
-  CStrings:  1102
+  Functions: 834
+  Symbols:   317
+  CStrings:  1321
 
Symbols:
+ _CFStringCompare
+ _LACDTBiometryWatchdogGlobalFallbackTime
+ _LACDTORatchetStateDurationInfinite
+ _LACDarwinNotificationSystemLanguageDidChange
+ _LACLogDTOStorage
+ _MKBDeviceUnlockedSinceBoot
+ _OBJC_CLASS_$_LAACMBiometricAttemptNotifier
+ _OBJC_CLASS_$_LAACMHelper
+ _OBJC_CLASS_$_LAAnalyticsDTO
+ _OBJC_CLASS_$_LACDTOBiometryWatchdog
+ _OBJC_CLASS_$_LACDTOBiometryWatchdogPack
+ _OBJC_CLASS_$_LACDTODarwinNotificationsController
+ _OBJC_CLASS_$_LACDTOEnvironmentProviderFactory
+ _OBJC_CLASS_$_LACDTOEventBus
+ _OBJC_CLASS_$_LACDTOFeatureController
+ _OBJC_CLASS_$_LACDTOKVStoreValue
+ _OBJC_CLASS_$_LACDTOLocationMonitor
+ _OBJC_CLASS_$_LACDTOLocationProviderCRAdapter
+ _OBJC_CLASS_$_LACDTOLocationProviderKVSAdapter
+ _OBJC_CLASS_$_LACDTOLostModeController
+ _OBJC_CLASS_$_LACDTOLostModeProviderAKAdapter
+ _OBJC_CLASS_$_LACDTOLostModeProviderKVSAdapter
+ _OBJC_CLASS_$_LACDTOPendingPolicyEvaluationController
+ _OBJC_CLASS_$_LACDTOPolicyEvaluationController
+ _OBJC_CLASS_$_LACDTORatchetState
+ _OBJC_CLASS_$_LACDTORatchetStateMonitor
+ _OBJC_CLASS_$_LACDTORatchetStateWithWatchdogs
+ _OBJC_CLASS_$_LACDTOServiceXPCHost
+ _OBJC_CLASS_$_LACMobileGestalt
+ _OBJC_CLASS_$_LACPersistentStoreFactory
+ _OBJC_CLASS_$_LAPasscodeHelper
+ _OBJC_CLASS_$_LAServiceAdapter
+ __os_feature_enabled_impl
+ __sl_dlopen
+ _abort_report_np
+ _dispatch_assert_queue$V2
+ _geteuid
+ _objc_getClass
CStrings:
+ "\x0f\x01"
+ "%@:%@"
+ "%s"
+ "<UNKNOWN>"
+ "@\"<LACDTODeviceInfoProvider>\""
+ "@\"<LACDTOEnvironmentProviding>\""
+ "@\"<LACDTOEnvironmentProviding>\"16@0:8"
+ "@\"<LACDTOFeatureControlling>\"16@0:8"
+ "@\"<LACDTOKVStore>\""
+ "@\"<LACDTOLocationProvider>\"8@?0"
+ "@\"<LACDTOLostModeProvider>\"8@?0"
+ "@\"<LACDTOPendingPolicyEvaluationController>\"16@0:8"
+ "@\"<LACDTOPolicyEvaluationController>\"16@0:8"
+ "@\"<LACDTORatchetStateProvider>\"16@0:8"
+ "@\"<LACDTOService>\""
+ "@\"<LACDTOServiceXPC>\"16@0:8"
+ "@\"<LACPersistentStore>\""
+ "@\"<LASecureStorageService>\""
+ "@\"LAAnalyticsDTO\""
+ "@\"LACDTODarwinNotificationsController\""
+ "@\"LACDTODarwinNotificationsController\"8@?0"
+ "@\"LACDTOEventBus\""
+ "@\"LACDTOFeatureController\""
+ "@\"LACDTOFeatureController\"8@?0"
+ "@\"LACDTOLocationMonitor\""
+ "@\"LACDTOLocationMonitor\"8@?0"
+ "@\"LACDTOLostModeController\""
+ "@\"LACDTOLostModeController\"8@?0"
+ "@\"LACDTOPendingPolicyEvaluationController\""
+ "@\"LACDTOPendingPolicyEvaluationController\"8@?0"
+ "@\"LACDTOPolicyEvaluationController\""
+ "@\"LACDTORatchetStateMonitor\""
+ "@\"LACDTORatchetStateMonitor\"8@?0"
+ "@\"LACDTOServiceXPCHost\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSString\"32@0:8@\"<LACXPCClientInfo>\"16@\"NSString\"24"
+ "@24@0:8^{?=iQ{?=[16C]}BQIBQQQ}16"
+ "@24@0:8q16"
+ "@32@0:8r^{?=QQQQQ}16r^{?=iQ{?=[16C]}BQIBQQQ}24"
+ "AKAccountManager"
+ "AuthKit"
+ "AuthorizedLocation"
+ "B48@0:8@16q24@32@?40"
+ "CLLocationManager"
+ "CoreRoutine"
+ "DTO"
+ "DTODeviceInfoProvider"
+ "DTOKVStore"
+ "DTOPolicyEvaluationIdentifierFactory"
+ "DTORatchetHandler"
+ "DTORatchetStateParser"
+ "DTOService"
+ "Finished KVS query: { key: %d, result: %@, error: %@ }"
+ "Finished KVS update: { key: %d, result: %@, error: %@ }"
+ "LACDTODeviceInfoProvider"
+ "LACDTOKVStore"
+ "LACDTOPolicyEvaluationIdentifierFactory"
+ "LACDTORatchetHandler"
+ "LACDTORatchetStateProvider"
+ "LACDTOService"
+ "LACDTOServiceXPC"
+ "LACDarwinNotificationCenterObserver"
+ "Should kill daemon because of localization change"
+ "T@\"<LACDTOEnvironmentProviding>\",R,N"
+ "T@\"<LACDTOEnvironmentProviding>\",R,N,V_environmentProvider"
+ "T@\"<LACDTOFeatureControlling>\",R,N"
+ "T@\"<LACDTOFeatureControlling>\",R,N,V_featureController"
+ "T@\"<LACDTOPendingPolicyEvaluationController>\",R,N"
+ "T@\"<LACDTOPendingPolicyEvaluationController>\",R,N,V_pendingEvaluationsController"
+ "T@\"<LACDTOPolicyEvaluationController>\",R,N"
+ "T@\"<LACDTOPolicyEvaluationController>\",R,N,V_policyController"
+ "T@\"<LACDTORatchetStateProvider>\",R,N"
+ "T@\"<LACDTORatchetStateProvider>\",R,N,V_ratchetStateProvider"
+ "T@\"<LACDTOService>\",R,N,V_dto"
+ "T@\"<LACDTOServiceXPC>\",R,N"
+ "T@\"<LACDTOServiceXPC>\",R,N,V_xpcController"
+ "UUID"
+ "UUIDString"
+ "Unable to find class %s"
+ "Unexpected value type for KVS key: %d"
+ "_analytics"
+ "_biometryWatchdogDTOFromConfig:status:"
+ "_biometryWatchdogGlobalFromConfig:status:"
+ "_callerIDForClient:"
+ "_checkDTOEntitlementsWithOriginator:policy:options:failureHandler:"
+ "_configFromRatchetState:"
+ "_darwinNotificationsController"
+ "_deviceInfo"
+ "_dto"
+ "_durationFromRatchetStatus:config:"
+ "_environmentProvider"
+ "_eventBus"
+ "_featureController"
+ "_kvStore"
+ "_locationProvider"
+ "_lostMode"
+ "_pendingEvaluationsController"
+ "_persistentStore"
+ "_policyController"
+ "_ratchetStateFromACMRatchetState:"
+ "_ratchetStateProvider"
+ "_ratchetStatusWithCompletion:"
+ "_ratchetUUIDFromACMRatchetState:"
+ "_registerObserverForLocalizationChanges"
+ "_resetDurationFromRatchetStatus:config:"
+ "_resetRatchetWithCompletion:"
+ "_scaleDuration:"
+ "_secureStorage"
+ "_setValue:forKey:contextUUID:connection:completion:"
+ "_startDTO"
+ "_statusFromRatchetState:"
+ "_storage"
+ "_storageForKey:"
+ "_storageKeyForKVSKey:"
+ "_uncheckedStorage"
+ "_workQueue"
+ "_xpcController"
+ "addEventHandler:"
+ "callerIdWithPid:auditToken:"
+ "cancelPendingEvaluationWithRatchetIdentifier:reason:completion:"
+ "checkCanEnableFeatureWithCompletion:"
+ "checkIsFeatureAvailableWithCompletion:"
+ "checkIsFeatureEnabledWithCompletion:"
+ "checkIsFeatureSupportedWithCompletion:"
+ "com.apple.private.LocalAuthentication.DTO"
+ "d24@0:8d16"
+ "d32@0:8^{?=iQ{?=[16C]}BQIBQQQ}16^{?=QQQQQ}24"
+ "data"
+ "disableFeatureWithContext:completion:"
+ "dto"
+ "dtoAnalytics"
+ "enableFeatureWithCompletion:"
+ "entitlementsForPolicy:options:"
+ "environment"
+ "environmentProvider"
+ "environmentProviderWithLocationProvider:featureController:ratchetStateProvider:lostModeController:"
+ "evaluatePolicy:options:client:evaluationBlock:reply:"
+ "evaluationIdentifierForClient:ratchetIdentifier:"
+ "evaluationResult:error:"
+ "featureController"
+ "handlesPolicy:options:"
+ "hasBeenUnlockedSinceBoot"
+ "hasBiometricEnrollmentsForCurrentUser"
+ "hasHSA2Account"
+ "hasLocationServicesEnabled"
+ "hasPasscodeSetForCurrentUser"
+ "initForStatusMonitoringWithEnvironment:workQueue:"
+ "initWithBiometryWatchdogGlobal:biometryWatchdogDTO:"
+ "initWithData:"
+ "initWithEnvironment:evaluationIdentifierFactory:device:"
+ "initWithExportedInterface:exportedObject:queue:"
+ "initWithFeatureController:ratchetStateProvider:pendingEvaluationController:"
+ "initWithIntegerValue:"
+ "initWithIsRunning:time:minThreshold:maxThreshold:"
+ "initWithKVStore:"
+ "initWithKVStore:device:workQueue:"
+ "initWithLocationProvider:store:workQueue:"
+ "initWithLostModeProvider:store:workQueue:"
+ "initWithNotificationCenter:"
+ "initWithRatchetState:watchdogs:"
+ "initWithRatchetStateProvider:ratchetHandler:evaluationIdentifierFactory:persistentStore:workQueue:"
+ "initWithRatchetStateProvider:workQueue:"
+ "initWithRawValue:duration:resetDuration:uuid:"
+ "initWithUUIDBytes:"
+ "initWithWorkQueue:"
+ "initWithWorkQueue:deviceInfo:"
+ "initWithWorkQueue:notificationCenter:"
+ "isEnrolled:error:"
+ "isIdiomPhone"
+ "isPasscodeSetForUser:error:"
+ "isPhone"
+ "kLAServiceTypeRatchet"
+ "locationServicesEnabled"
+ "makePersistentStoreWithUserDefaults:"
+ "notificationCenter:didReceiveNotification:"
+ "pendingPolicyEvaluationController"
+ "policyController"
+ "primaryAuthKitAccount"
+ "q24@0:8^{?=iQ{?=[16C]}BQIBQQQ}16"
+ "q24@0:8q16"
+ "ratchetStateFromState:"
+ "ratchetStateProvider"
+ "ratchetStateWithCompletion:"
+ "ratchetStateWithWatchdogsCompletion:"
+ "ratchetStatusWithConfig:"
+ "resetRatchet:"
+ "resetRatchetWithCompletion:"
+ "securityLevelForAccount:"
+ "serialNumber"
+ "setDtoEnvironment:"
+ "setDtoRequestIdentifier:"
+ "setEventBus:"
+ "setValue:forKey:completion:"
+ "setValue:forKey:connection:completion:"
+ "setValue:forKey:contextUUID:completion:"
+ "setValue:forKey:contextUUID:connection:completion:"
+ "softlink:r:path:/System/Library/Frameworks/CoreLocation.framework/CoreLocation"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit"
+ "startController"
+ "v24@0:8@?<v@?@\"LACDTORatchetState\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"LACDTORatchetStateWithWatchdogs\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v32@0:8@\"<LACDarwinNotificationCenter>\"16^{__CFString=}24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
+ "v32@0:8q16@?<v@?@\"LACDTOKVStoreValue\"@\"NSError\">24"
+ "v40@0:8@\"LACDTOKVStoreValue\"16q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8q16@\"NSXPCConnection\"24@?<v@?@\"LACDTOKVStoreValue\"@\"NSError\">32"
+ "v40@?0q8@\"NSDictionary\"16@\"<LACDTOPolicyEvaluationRequest>\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v48@0:8@\"LACDTOKVStoreValue\"16q24@\"NSUUID\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"LACDTOKVStoreValue\"16q24@\"NSXPCConnection\"32@?<v@?@\"NSError\">40"
+ "v56@0:8@\"LACDTOKVStoreValue\"16q24@\"NSUUID\"32@\"NSXPCConnection\"40@?<v@?@\"NSError\">48"
+ "valueForKey:completion:"
+ "valueForKey:connection:completion:"
+ "watchdogPackFromState:"
+ "xpcController"
+ "{?=QQQQQ}24@0:8@16"
+ "{?=iQ{?=[16C]}BQIBQQQ}24@0:8@16"

```
