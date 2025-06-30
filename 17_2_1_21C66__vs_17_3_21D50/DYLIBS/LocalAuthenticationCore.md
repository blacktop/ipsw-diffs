## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-1394.62.1.0.0
-  __TEXT.__text: 0x39f0
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x46c
-  __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x3c2
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__oslogstring: 0x39
-  __TEXT.__constg_swiftt: 0x88
-  __TEXT.__swift5_typeref: 0x62
-  __TEXT.__swift5_fieldmd: 0x20
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x1fc
-  __TEXT.__objc_classname: 0x10f
-  __TEXT.__objc_methname: 0xe6e
-  __TEXT.__objc_methtype: 0x46b
-  __TEXT.__objc_stubs: 0x880
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x170
-  __DATA_CONST.__objc_classlist: 0x70
-  __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x28
+1394.82.1.0.0
+  __TEXT.__text: 0x28d80
+  __TEXT.__auth_stubs: 0xe70
+  __TEXT.__objc_methlist: 0x1780
+  __TEXT.__const: 0x758
+  __TEXT.__cstring: 0x1cd3
+  __TEXT.__gcc_except_tab: 0x4a0
+  __TEXT.__oslogstring: 0xd27
+  __TEXT.__dlopen_cstrs: 0xa0
+  __TEXT.__swift5_typeref: 0x4a4
+  __TEXT.__swift5_fieldmd: 0x17c
+  __TEXT.__constg_swiftt: 0x314
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_reflstr: 0x147
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift5_proto: 0x28
+  __TEXT.__swift5_types: 0x24
+  __TEXT.__swift5_capture: 0x350
+  __TEXT.__unwind_info: 0x1cb0
+  __TEXT.__eh_frame: 0xd98
+  __TEXT.__objc_classname: 0x6e6
+  __TEXT.__objc_methname: 0x38e4
+  __TEXT.__objc_methtype: 0x1198
+  __TEXT.__objc_stubs: 0x2840
+  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__const: 0xe20
+  __DATA_CONST.__objc_classlist: 0x198
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x15c8
-  __DATA_CONST.__objc_selrefs: 0x3f0
-  __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x3f0
-  __AUTH_CONST.__const: 0x130
-  __AUTH_CONST.__auth_got: 0x370
-  __AUTH.__objc_data: 0x470
-  __AUTH.__data: 0xc0
-  __DATA.__objc_classrefs: 0xb0
-  __DATA.__objc_superrefs: 0x38
-  __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x1f8
-  __DATA.__bss: 0x50
+  __DATA_CONST.__objc_const: 0xa178
+  __DATA_CONST.__objc_selrefs: 0xd70
+  __DATA_CONST.__objc_arraydata: 0x38
+  __AUTH_CONST.__cfstring: 0xc00
+  __AUTH_CONST.__objc_const: 0xfb8
+  __AUTH_CONST.__const: 0xe48
+  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__auth_got: 0x748
+  __AUTH.__objc_data: 0x12f0
+  __AUTH.__data: 0x170
+  __DATA.__objc_protorefs: 0x88
+  __DATA.__objc_classrefs: 0x1c0
+  __DATA.__objc_superrefs: 0x110
+  __DATA.__objc_ivar: 0x1cc
+  __DATA.__objc_data: 0x98
+  __DATA.__data: 0xfe8
+  __DATA.__bss: 0x650
+  __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E4F1EFB7-B61C-3618-8D7D-2240F17F5FE5
-  Functions: 127
-  Symbols:   704
-  CStrings:  314
+  UUID: CACFD424-5F78-388A-A601-FC80F22AF892
+  Functions: 1148
+  Symbols:   4212
+  CStrings:  1260
 
Symbols:
+ +[LACDTOEnvironmentProviderFactory environmentProviderWithLocationProvider:featureController:ratchetStateProvider:lostModeController:]
+ +[LACDTOLocationState defaultLocationState]
+ +[LACDTOLostModeState defaultLostModeState]
+ +[LACDTORatchetNotificationCoolOff categoryIdentifier]
+ +[LACDTORatchetState supportsSecureCoding]
+ +[LACDTOSignpostEvent environmentUpdateDidFinish]
+ +[LACDTOSignpostEvent environmentUpdateWillStart]
+ +[LACDTOSignpostEvent locationStatusQueryDidFinish]
+ +[LACDTOSignpostEvent locationStatusQueryWillStart]
+ +[LACDTOSignpostEvent lostModeQueryDidFinish]
+ +[LACDTOSignpostEvent lostModeQueryWillStart]
+ +[LACError errorWithCode:subcode:]
+ +[LACError errorWithCode:subcode:debugDescription:]
+ +[LACPersistentStoreFactory makePersistentStoreWithUserDefaults:]
+ -[LACDTOBiometryWatchdog description]
+ -[LACDTOBiometryWatchdog initWithIsRunning:time:minThreshold:maxThreshold:]
+ -[LACDTOBiometryWatchdog isBarking]
+ -[LACDTOBiometryWatchdog isEqual:]
+ -[LACDTOBiometryWatchdog isRunning]
+ -[LACDTOBiometryWatchdog maxThreshold]
+ -[LACDTOBiometryWatchdog minThreshold]
+ -[LACDTOBiometryWatchdog time]
+ -[LACDTOBiometryWatchdogPack .cxx_destruct]
+ -[LACDTOBiometryWatchdogPack biometryWatchdogDTO]
+ -[LACDTOBiometryWatchdogPack biometryWatchdogGlobal]
+ -[LACDTOBiometryWatchdogPack description]
+ -[LACDTOBiometryWatchdogPack initWithBiometryWatchdogGlobal:biometryWatchdogDTO:]
+ -[LACDTOBiometryWatchdogPack isBarking]
+ -[LACDTOBiometryWatchdogPack isEqual:]
+ -[LACDTODarwinNotificationsController .cxx_destruct]
+ -[LACDTODarwinNotificationsController handleEvent:sender:]
+ -[LACDTODarwinNotificationsController initWithNotificationCenter:]
+ -[LACDTOEvent .cxx_destruct]
+ -[LACDTOEvent description]
+ -[LACDTOEvent initWithRawValue:]
+ -[LACDTOEvent initWithRawValue:optionalValue:]
+ -[LACDTOEvent initWithRawValue:value:]
+ -[LACDTOEvent isEqual:]
+ -[LACDTOEvent rawValue]
+ -[LACDTOEvent value]
+ -[LACDTOEventBus .cxx_destruct]
+ -[LACDTOEventBus addEventHandler:]
+ -[LACDTOEventBus dispatchEvent:sender:]
+ -[LACDTOEventBus dispatchEvent:sender:].cold.1
+ -[LACDTOEventBus init]
+ -[LACDTOEventBus removeEventHandler:]
+ -[LACDTOFeatureController .cxx_destruct]
+ -[LACDTOFeatureController _featureFlagKey]
+ -[LACDTOFeatureController _fetchDeviceHintsCurrentConnection:completion:]
+ -[LACDTOFeatureController _setFeatureEnabled:context:connection:completion:]
+ -[LACDTOFeatureController _setValue:forKey:contextUUID:connection:completion:]
+ -[LACDTOFeatureController checkCanEnableFeatureWithCompletion:]
+ -[LACDTOFeatureController checkIsFeatureAvailableWithCompletion:]
+ -[LACDTOFeatureController checkIsFeatureEnabledWithCompletion:]
+ -[LACDTOFeatureController checkIsFeatureSupportedWithCompletion:]
+ -[LACDTOFeatureController disableFeatureWithContext:completion:]
+ -[LACDTOFeatureController enableFeatureWithCompletion:]
+ -[LACDTOFeatureController eventBus]
+ -[LACDTOFeatureController fetchStateWithCompletion:]
+ -[LACDTOFeatureController initWithKVStore:device:workQueue:]
+ -[LACDTOFeatureController setEventBus:]
+ -[LACDTOKVStoreValue .cxx_destruct]
+ -[LACDTOKVStoreValue boolValue]
+ -[LACDTOKVStoreValue data]
+ -[LACDTOKVStoreValue initWithBoolValue:]
+ -[LACDTOKVStoreValue initWithData:]
+ -[LACDTOKVStoreValue initWithIntegerValue:]
+ -[LACDTOKVStoreValue integerValue]
+ -[LACDTOKVStoreValue isEqual:]
+ -[LACDTOLocationMonitor .cxx_destruct]
+ -[LACDTOLocationMonitor _locationStateFromBackgroundTaskResult:]
+ -[LACDTOLocationMonitor _runLocationStateBackgroundTask:completion:]
+ -[LACDTOLocationMonitor _startMonitoringWithReason:]
+ -[LACDTOLocationMonitor _startMonitoringWithReason:].cold.1
+ -[LACDTOLocationMonitor _stopMonitoringWithReason:]
+ -[LACDTOLocationMonitor checkIsInFamiliarLocationWithCompletion:]
+ -[LACDTOLocationMonitor description]
+ -[LACDTOLocationMonitor eventBus]
+ -[LACDTOLocationMonitor initWithLocationProvider:store:workQueue:]
+ -[LACDTOLocationMonitor locationStateBackgroundTask]
+ -[LACDTOLocationMonitor locationState]
+ -[LACDTOLocationMonitor pendingEvaluationController:updatedPendingEvaluation:]
+ -[LACDTOLocationMonitor pendingEvaluationControllerDidStartTrackingPendingEvaluations:]
+ -[LACDTOLocationMonitor pendingEvaluationControllerDidStopTrackingPendingEvaluations:]
+ -[LACDTOLocationMonitor setEventBus:]
+ -[LACDTOLocationMonitor setLocationState:]
+ -[LACDTOLocationMonitor setLocationStateBackgroundTask:]
+ -[LACDTOLocationMonitor setWorkQueue:]
+ -[LACDTOLocationMonitor workQueue]
+ -[LACDTOLocationProviderCRAdapter .cxx_destruct]
+ -[LACDTOLocationProviderCRAdapter checkIsInFamiliarLocationWithCompletion:]
+ -[LACDTOLocationProviderCRAdapter checkIsInFamiliarLocationWithCompletion:].cold.1
+ -[LACDTOLocationProviderCRAdapter description]
+ -[LACDTOLocationProviderCRAdapter initWithWorkQueue:]
+ -[LACDTOLocationProviderKVSAdapter .cxx_destruct]
+ -[LACDTOLocationProviderKVSAdapter checkIsInFamiliarLocationWithCompletion:]
+ -[LACDTOLocationProviderKVSAdapter description]
+ -[LACDTOLocationProviderKVSAdapter initWithKVStore:]
+ -[LACDTOLocationState .cxx_destruct]
+ -[LACDTOLocationState confirmed]
+ -[LACDTOLocationState createdAt]
+ -[LACDTOLocationState description]
+ -[LACDTOLocationState initWithIsInFamiliarLocation:confirmed:]
+ -[LACDTOLocationState initWithIsInFamiliarLocation:confirmed:createdAt:]
+ -[LACDTOLocationState isEqual:]
+ -[LACDTOLocationState isInFamiliarLocation]
+ -[LACDTOLocationState isValid:]
+ -[LACDTOLostModeController .cxx_destruct]
+ -[LACDTOLostModeController _lostModeStateFromBackgroundTaskResult:]
+ -[LACDTOLostModeController _runLostModeBackgroundTaskWithStrategy:completion:]
+ -[LACDTOLostModeController _runLostModeBackgroundTaskWithTimeout:completion:]
+ -[LACDTOLostModeController _storeLostModeState:completion:]
+ -[LACDTOLostModeController description]
+ -[LACDTOLostModeController fetchLostMode:completion:]
+ -[LACDTOLostModeController initWithLostModeProvider:store:workQueue:]
+ -[LACDTOLostModeController lostModeBackgroundTask]
+ -[LACDTOLostModeController setLostModeBackgroundTask:]
+ -[LACDTOLostModeProviderAKAdapter .cxx_destruct]
+ -[LACDTOLostModeProviderAKAdapter _lostModeStateWithCompletion:]
+ -[LACDTOLostModeProviderAKAdapter description]
+ -[LACDTOLostModeProviderAKAdapter initWithWorkQueue:deviceInfo:]
+ -[LACDTOLostModeProviderAKAdapter lostModeStateWithCompletion:]
+ -[LACDTOLostModeProviderKVSAdapter .cxx_destruct]
+ -[LACDTOLostModeProviderKVSAdapter description]
+ -[LACDTOLostModeProviderKVSAdapter initWithKVStore:]
+ -[LACDTOLostModeProviderKVSAdapter lostModeStateWithCompletion:]
+ -[LACDTOLostModeState .cxx_destruct]
+ -[LACDTOLostModeState confirmed]
+ -[LACDTOLostModeState createdAt]
+ -[LACDTOLostModeState description]
+ -[LACDTOLostModeState initWithIsInLostMode:]
+ -[LACDTOLostModeState initWithIsInLostMode:confirmed:]
+ -[LACDTOLostModeState initWithIsInLostMode:confirmed:createdAt:]
+ -[LACDTOLostModeState isEqual:]
+ -[LACDTOLostModeState isInLostMode]
+ -[LACDTOLostModeState isValid:]
+ -[LACDTOMutableEnvironment .cxx_destruct]
+ -[LACDTOMutableEnvironment allowsAuthenticationFallbacks]
+ -[LACDTOMutableEnvironment biometryWatchdogPack]
+ -[LACDTOMutableEnvironment description]
+ -[LACDTOMutableEnvironment featureState]
+ -[LACDTOMutableEnvironment hasExpiredBiometry]
+ -[LACDTOMutableEnvironment inFamiliarLocation]
+ -[LACDTOMutableEnvironment isDTOEnabled]
+ -[LACDTOMutableEnvironment isEqual:]
+ -[LACDTOMutableEnvironment ratchetState]
+ -[LACDTOMutableEnvironment setBiometryWatchdogPack:]
+ -[LACDTOMutableEnvironment setFeatureState:]
+ -[LACDTOMutableEnvironment setInFamiliarLocation:]
+ -[LACDTOMutableEnvironment setRatchetState:]
+ -[LACDTOMutableFeatureState description]
+ -[LACDTOMutableFeatureState isAvailable]
+ -[LACDTOMutableFeatureState isEnabled]
+ -[LACDTOMutableFeatureState isEqual:]
+ -[LACDTOMutableFeatureState isSupported]
+ -[LACDTOMutableFeatureState setIsAvailable:]
+ -[LACDTOMutableFeatureState setIsEnabled:]
+ -[LACDTOMutableFeatureState setIsSupported:]
+ -[LACDTOMutableLostModeFetchRequest .cxx_destruct]
+ -[LACDTOMutableLostModeFetchRequest biometryWatchdogPack]
+ -[LACDTOMutableLostModeFetchRequest description]
+ -[LACDTOMutableLostModeFetchRequest isDTOEnabled]
+ -[LACDTOMutableLostModeFetchRequest isEqual:]
+ -[LACDTOMutableLostModeFetchRequest options]
+ -[LACDTOMutableLostModeFetchRequest policy]
+ -[LACDTOMutableLostModeFetchRequest ratchetState]
+ -[LACDTOMutableLostModeFetchRequest setBiometryWatchdogPack:]
+ -[LACDTOMutableLostModeFetchRequest setIsDTOEnabled:]
+ -[LACDTOMutableLostModeFetchRequest setOptions:]
+ -[LACDTOMutableLostModeFetchRequest setPolicy:]
+ -[LACDTOMutableLostModeFetchRequest setRatchetState:]
+ -[LACDTOMutablePolicyEvaluationRequest .cxx_destruct]
+ -[LACDTOMutablePolicyEvaluationRequest description]
+ -[LACDTOMutablePolicyEvaluationRequest environment]
+ -[LACDTOMutablePolicyEvaluationRequest hash]
+ -[LACDTOMutablePolicyEvaluationRequest identifier]
+ -[LACDTOMutablePolicyEvaluationRequest initWithIdentifier:]
+ -[LACDTOMutablePolicyEvaluationRequest isEqual:]
+ -[LACDTOMutablePolicyEvaluationRequest isInteractiveRatchetEvaluation]
+ -[LACDTOMutablePolicyEvaluationRequest options]
+ -[LACDTOMutablePolicyEvaluationRequest policy]
+ -[LACDTOMutablePolicyEvaluationRequest setEnvironment:]
+ -[LACDTOMutablePolicyEvaluationRequest setIdentifier:]
+ -[LACDTOMutablePolicyEvaluationRequest setOptions:]
+ -[LACDTOMutablePolicyEvaluationRequest setPolicy:]
+ -[LACDTOMutablePolicyEvaluationResult .cxx_destruct]
+ -[LACDTOMutablePolicyEvaluationResult description]
+ -[LACDTOMutablePolicyEvaluationResult error]
+ -[LACDTOMutablePolicyEvaluationResult identifier]
+ -[LACDTOMutablePolicyEvaluationResult initWithIdentifier:]
+ -[LACDTOMutablePolicyEvaluationResult isEqual:]
+ -[LACDTOMutablePolicyEvaluationResult isSuccess]
+ -[LACDTOMutablePolicyEvaluationResult result]
+ -[LACDTOMutablePolicyEvaluationResult setError:]
+ -[LACDTOMutablePolicyEvaluationResult setIdentifier:]
+ -[LACDTOMutablePolicyEvaluationResult setResult:]
+ -[LACDTONotificationManager _ratchetCoolOffNotificationManager]
+ -[LACDTONotificationManager cancelPreviousSecurityDelayFinishedNotificationForPendingEvaluation:completion:]
+ -[LACDTONotificationManager scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:maxAge:completion:]
+ -[LACDTOPendingPolicyEvaluationController .cxx_destruct]
+ -[LACDTOPendingPolicyEvaluationController _addPendingEvaluationRecord:currentState:]
+ -[LACDTOPendingPolicyEvaluationController _addPendingEvaluationRecordForRequest:currentState:]
+ -[LACDTOPendingPolicyEvaluationController _canFinishPendingEvaluationsForRatchetState:]
+ -[LACDTOPendingPolicyEvaluationController _cancelPreviousNotificationForPendingEvaluationRecord:]
+ -[LACDTOPendingPolicyEvaluationController _checkIsRatchetStateIn:completion:]
+ -[LACDTOPendingPolicyEvaluationController _checkShouldAddPendingEvaluationRecordForRequest:completion:]
+ -[LACDTOPendingPolicyEvaluationController _checkShouldKeepPendingEvaluationRecordForResult:completion:]
+ -[LACDTOPendingPolicyEvaluationController _coolOffStartedTimestampForIdentifier:currentState:]
+ -[LACDTOPendingPolicyEvaluationController _forEachObserver:]
+ -[LACDTOPendingPolicyEvaluationController _handleRatchetStateChanged:]
+ -[LACDTOPendingPolicyEvaluationController _handleSwitchToCoolOffState:]
+ -[LACDTOPendingPolicyEvaluationController _handleSwitchToFinalState:]
+ -[LACDTOPendingPolicyEvaluationController _hasPendingEvaluationRecordForRequest:]
+ -[LACDTOPendingPolicyEvaluationController _loadPendingEvaluations]
+ -[LACDTOPendingPolicyEvaluationController _prunePendingEvaluationsWithUUID:]
+ -[LACDTOPendingPolicyEvaluationController _removePendingEvaluationRecordWithIdentifier:completion:]
+ -[LACDTOPendingPolicyEvaluationController _resetRatchetWithCompletion:]
+ -[LACDTOPendingPolicyEvaluationController _scheduleNotificationForPendingEvaluationRecord:after:maxAge:]
+ -[LACDTOPendingPolicyEvaluationController _shouldPrunePendingEvaluation:uuid:]
+ -[LACDTOPendingPolicyEvaluationController _updatePendingEvaluationsWithBlock:]
+ -[LACDTOPendingPolicyEvaluationController _updatePendingEvaluationsWithUpdateBlock:observerFilter:]
+ -[LACDTOPendingPolicyEvaluationController addObserver:]
+ -[LACDTOPendingPolicyEvaluationController cancelPendingEvaluationForClient:ratchetIdentifier:reason:completion:]
+ -[LACDTOPendingPolicyEvaluationController handleEvent:sender:]
+ -[LACDTOPendingPolicyEvaluationController initWithRatchetStateProvider:ratchetHandler:evaluationIdentifierFactory:persistentStore:workQueue:]
+ -[LACDTOPendingPolicyEvaluationController notificationManager]
+ -[LACDTOPendingPolicyEvaluationController policyController:didFinishPolicyEvaluation:result:]
+ -[LACDTOPendingPolicyEvaluationController policyController:willStartPolicyEvaluation:]
+ -[LACDTOPendingPolicyEvaluationController removeObserver:]
+ -[LACDTOPendingPolicyEvaluationController setNotificationManager:]
+ -[LACDTOPendingPolicyEvaluationController startController]
+ -[LACDTOPolicyEvaluationController .cxx_destruct]
+ -[LACDTOPolicyEvaluationController _checkDeviceHasBeenUnlockedSinceBoot]
+ -[LACDTOPolicyEvaluationController _errorCodesToFilterForOptions:]
+ -[LACDTOPolicyEvaluationController _evaluatePolicy:options:client:environment:evaluationBlock:reply:]
+ -[LACDTOPolicyEvaluationController _forEachObserver:]
+ -[LACDTOPolicyEvaluationController _mapResult:error:filterCodes:completion:]
+ -[LACDTOPolicyEvaluationController _noAuthenticationOnFallbackEvaluationBlockWithBlock:]
+ -[LACDTOPolicyEvaluationController _notifyObserversAboutEvaluation:]
+ -[LACDTOPolicyEvaluationController _notifyObserversAboutEvaluation:].cold.1
+ -[LACDTOPolicyEvaluationController _notifyObserversAboutEvaluation:result:]
+ -[LACDTOPolicyEvaluationController _notifyObserversAboutEvaluation:result:].cold.1
+ -[LACDTOPolicyEvaluationController _verifyHasRequiredOptions:forPolicy:error:]
+ -[LACDTOPolicyEvaluationController addObserver:]
+ -[LACDTOPolicyEvaluationController entitlementsForPolicy:options:]
+ -[LACDTOPolicyEvaluationController evaluatePolicy:options:client:evaluationBlock:reply:]
+ -[LACDTOPolicyEvaluationController handlesPolicy:options:]
+ -[LACDTOPolicyEvaluationController initWithEnvironment:evaluationIdentifierFactory:device:]
+ -[LACDTOPolicyEvaluationController initWithEnvironment:evaluationIdentifierFactory:device:].cold.1
+ -[LACDTOPolicyEvaluationController removeObserver:]
+ -[LACDTORatchetNotificationCoolOff .cxx_destruct]
+ -[LACDTORatchetNotificationCoolOff body]
+ -[LACDTORatchetNotificationCoolOff defaultActionURL]
+ -[LACDTORatchetNotificationCoolOff identifier]
+ -[LACDTORatchetNotificationCoolOff initWithIdentifier:body:deeplinkURL:]
+ -[LACDTORatchetNotificationCoolOff isTimeSensitive]
+ -[LACDTORatchetNotificationCoolOff maxAge]
+ -[LACDTORatchetNotificationCoolOff setBody:]
+ -[LACDTORatchetNotificationCoolOff setDefaultActionURL:]
+ -[LACDTORatchetNotificationCoolOff setIdentifier:]
+ -[LACDTORatchetNotificationCoolOff setIsTimeSensitive:]
+ -[LACDTORatchetNotificationCoolOff setMaxAge:]
+ -[LACDTORatchetNotificationCoolOff setSystemIconName:]
+ -[LACDTORatchetNotificationCoolOff setTitle:]
+ -[LACDTORatchetNotificationCoolOff systemIconName]
+ -[LACDTORatchetNotificationCoolOff title]
+ -[LACDTORatchetState .cxx_destruct]
+ -[LACDTORatchetState description]
+ -[LACDTORatchetState duration]
+ -[LACDTORatchetState effectiveDuration]
+ -[LACDTORatchetState encodeWithCoder:]
+ -[LACDTORatchetState initWithCoder:]
+ -[LACDTORatchetState initWithRawValue:duration:resetDuration:uuid:]
+ -[LACDTORatchetState isEqual:]
+ -[LACDTORatchetState rawValue]
+ -[LACDTORatchetState resetDuration]
+ -[LACDTORatchetState uuid]
+ -[LACDTORatchetStateMonitor .cxx_destruct]
+ -[LACDTORatchetStateMonitor _scheduleNextStatusCheck]
+ -[LACDTORatchetStateMonitor eventBus]
+ -[LACDTORatchetStateMonitor handleEvent:sender:]
+ -[LACDTORatchetStateMonitor initWithRatchetStateProvider:workQueue:]
+ -[LACDTORatchetStateMonitor policyController:didFinishPolicyEvaluation:result:]
+ -[LACDTORatchetStateMonitor policyController:willStartPolicyEvaluation:]
+ -[LACDTORatchetStateMonitor ratchetStateWithCompletion:]
+ -[LACDTORatchetStateMonitor ratchetStateWithWatchdogsCompletion:]
+ -[LACDTORatchetStateMonitor ratchetState]
+ -[LACDTORatchetStateMonitor setEventBus:]
+ -[LACDTORatchetStateMonitor setRatchetState:]
+ -[LACDTORatchetStateWithWatchdogs .cxx_destruct]
+ -[LACDTORatchetStateWithWatchdogs description]
+ -[LACDTORatchetStateWithWatchdogs initWithRatchetState:watchdogs:]
+ -[LACDTORatchetStateWithWatchdogs isEqual:]
+ -[LACDTORatchetStateWithWatchdogs ratchetState]
+ -[LACDTORatchetStateWithWatchdogs watchdogs]
+ -[LACDTOServiceXPCClient .cxx_destruct]
+ -[LACDTOServiceXPCClient _connectionWithErrorHandler:]
+ -[LACDTOServiceXPCClient _handleConnectionClose]
+ -[LACDTOServiceXPCClient _handleConnectionClose].cold.1
+ -[LACDTOServiceXPCClient _remoteObjectProxyWithErrorHandler:]
+ -[LACDTOServiceXPCClient _synchronousRemoteObjectProxyWithErrorHandler:]
+ -[LACDTOServiceXPCClient cancelPendingEvaluationWithRatchetIdentifier:reason:completion:]
+ -[LACDTOServiceXPCClient checkCanEnableFeatureWithCompletion:]
+ -[LACDTOServiceXPCClient checkIsFeatureAvailableWithCompletion:]
+ -[LACDTOServiceXPCClient checkIsFeatureEnabledWithCompletion:]
+ -[LACDTOServiceXPCClient checkIsFeatureSupportedWithCompletion:]
+ -[LACDTOServiceXPCClient dealloc]
+ -[LACDTOServiceXPCClient disableFeatureWithContext:completion:]
+ -[LACDTOServiceXPCClient enableFeatureWithCompletion:]
+ -[LACDTOServiceXPCClient initWithEndpointProvider:]
+ -[LACDTOServiceXPCClient isFeatureAvailable]
+ -[LACDTOServiceXPCClient isFeatureEnabled]
+ -[LACDTOServiceXPCClient isFeatureSupported]
+ -[LACDTOServiceXPCClient ratchetStateWithCompletion:]
+ -[LACDTOServiceXPCClient ratchetState]
+ -[LACDTOServiceXPCHost .cxx_destruct]
+ -[LACDTOServiceXPCHost cancelPendingEvaluationWithRatchetIdentifier:reason:completion:]
+ -[LACDTOServiceXPCHost checkCanEnableFeatureWithCompletion:]
+ -[LACDTOServiceXPCHost checkIsFeatureAvailableWithCompletion:]
+ -[LACDTOServiceXPCHost checkIsFeatureEnabledWithCompletion:]
+ -[LACDTOServiceXPCHost checkIsFeatureSupportedWithCompletion:]
+ -[LACDTOServiceXPCHost disableFeatureWithContext:completion:]
+ -[LACDTOServiceXPCHost enableFeatureWithCompletion:]
+ -[LACDTOServiceXPCHost initWithFeatureController:ratchetStateProvider:pendingEvaluationController:]
+ -[LACDTOServiceXPCHost ratchetStateWithCompletion:]
+ -[LACDTOSignpostEvent .cxx_destruct]
+ -[LACDTOSignpostEvent _sendWithMessage:]
+ -[LACDTOSignpostEvent initWithSendBlock:]
+ -[LACDTOSignpostEvent sendWithMessage:]
+ -[LACDTOSignpostEvent send]
+ -[LACDarwinNotificationCenter _synchronizedObservers:]
+ -[LACDarwinNotificationCenter _synchronizedSubscriptions:]
+ -[LACRatchetFlowManager .cxx_destruct]
+ -[LACRatchetFlowManager initWithPresenter:uiManager:]
+ -[LACRatchetFlowManager presenter]
+ -[LACRatchetFlowManager uiManager]
+ GCC_except_table1
+ GCC_except_table10
+ GCC_except_table11
+ GCC_except_table12
+ GCC_except_table13
+ GCC_except_table14
+ GCC_except_table15
+ GCC_except_table17
+ GCC_except_table18
+ GCC_except_table19
+ GCC_except_table20
+ GCC_except_table24
+ GCC_except_table28
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table4
+ GCC_except_table40
+ GCC_except_table45
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table5
+ GCC_except_table7
+ GCC_except_table8
+ GCC_except_table9
+ _$s10Foundation11JSONDecoderC6decode_4fromxxm_AA4DataVtKSeRzlFTj
+ _$s10Foundation11JSONDecoderCACycfc
+ _$s10Foundation11JSONDecoderCMa
+ _$s10Foundation11JSONEncoderC6encodeyAA4DataVxKSERzlFTj
+ _$s10Foundation11JSONEncoderCACycfc
+ _$s10Foundation11JSONEncoderCMa
+ _$s10Foundation17NSLocalizedString_9tableName6bundle5value7commentS2S_SSSgSo8NSBundleCS2StF
+ _$s10Foundation3URLVACSEAAWL
+ _$s10Foundation3URLVACSQAAWL
+ _$s10Foundation3URLVACSeAAWL
+ _$s10Foundation3URLVSEAAMc
+ _$s10Foundation3URLVSQAAMc
+ _$s10Foundation3URLVSeAAMc
+ _$s10Foundation3URLVSgML
+ _$s10Foundation3URLVSgMaTm
+ _$s10Foundation3URLVSgWOcTm
+ _$s10Foundation3URLVSgWOdTm
+ _$s10Foundation3URLVSgWOfTm
+ _$s10Foundation3URLVSgWOhTm
+ _$s10Foundation3URLVSg_ADtMD
+ _$s10Foundation4DataV15_RepresentationOWOe
+ _$s10Foundation4DataV19_bridgeToObjectiveCSo6NSDataCyF
+ _$s10Foundation4DataV36_unconditionallyBridgeFromObjectiveCyACSo6NSDataCSgFZ
+ _$s10Foundation4DataVMn
+ _$s10Foundation4DataVSgMD
+ _$s10Foundation4DataVSgWOb
+ _$s10Foundation4DataVSgWOe
+ _$s10Foundation4DateV18addingTimeIntervalyACSdF
+ _$s10Foundation4DateV19_bridgeToObjectiveCSo6NSDateCyF
+ _$s10Foundation4DateV1loiySbAC_ACtFZ
+ _$s10Foundation4DateV36_unconditionallyBridgeFromObjectiveCyACSo6NSDateCSgFZ
+ _$s10Foundation4DateV3nowACvgZ
+ _$s10Foundation4DateV5lower_AC5uppertMD
+ _$s10Foundation4DateVACSEAAWL
+ _$s10Foundation4DateVACSLAAWL
+ _$s10Foundation4DateVACSLAAWlTm
+ _$s10Foundation4DateVACSQAAWL
+ _$s10Foundation4DateVACSeAAWL
+ _$s10Foundation4DateVMa
+ _$s10Foundation4DateVMn
+ _$s10Foundation4DateVSEAAMc
+ _$s10Foundation4DateVSLAAMc
+ _$s10Foundation4DateVSQAAMc
+ _$s10Foundation4DateVSeAAMc
+ _$s10Foundation4DateVSgMD
+ _$s10Foundation4DateVSgML
+ _$s10Foundation4DateVSgWOb
+ _$s10Foundation4DateVSg_ADtMD
+ _$s23LocalAuthenticationCore19LACLocalizedStringsC15localizedString33_06C5009961CF12380B02F6187ECF7956LL3key5value11tableSuffixS2S_S2StFZTf4ndnd_n
+ _$s23LocalAuthenticationCore19LACLocalizedStringsC18securityDelayEndedSSvgZ
+ _$s23LocalAuthenticationCore19LACLocalizedStringsC18securityDelayEndedSSvgZTj
+ _$s23LocalAuthenticationCore19LACLocalizedStringsC18securityDelayEndedSSvgZTo
+ _$s23LocalAuthenticationCore19LACLocalizedStringsC18securityDelayEndedSSvgZToTm
+ _$s23LocalAuthenticationCore19LACLocalizedStringsC18securityDelayEndedSSvgZTq
+ _$s23LocalAuthenticationCore19LACLocalizedStringsC20continueWithSettingsSSvgZ
+ _$s23LocalAuthenticationCore19LACLocalizedStringsC20continueWithSettingsSSvgZTj
+ _$s23LocalAuthenticationCore19LACLocalizedStringsC20continueWithSettingsSSvgZTo
+ _$s23LocalAuthenticationCore19LACLocalizedStringsC20continueWithSettingsSSvgZTq
+ _$s23LocalAuthenticationCore19LACLocalizedStringsCMu
+ _$s23LocalAuthenticationCore19LACLocalizedStringsCfETo
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC012ratchetStateE033_E856350D1C5EB666EF0471B129C641C4LLSo013LACDTORatchetgE0_pvpWvd
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC08locationE017featureController012ratchetStateE008lostModeH0ACSo014LACDTOLocationE0_p_So24LACDTOFeatureControlling_pSo013LACDTORatchetjE0_pSo010LACDTOLostL12FetchService_ptcfC
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC08locationE017featureController012ratchetStateE008lostModeH0ACSo014LACDTOLocationE0_p_So24LACDTOFeatureControlling_pSo013LACDTORatchetjE0_pSo010LACDTOLostL12FetchService_ptcfCTj
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC08locationE017featureController012ratchetStateE008lostModeH0ACSo014LACDTOLocationE0_p_So24LACDTOFeatureControlling_pSo013LACDTORatchetjE0_pSo010LACDTOLostL12FetchService_ptcfCTq
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC08locationE017featureController012ratchetStateE008lostModeH0ACSo014LACDTOLocationE0_p_So24LACDTOFeatureControlling_pSo013LACDTORatchetjE0_pSo010LACDTOLostL12FetchService_ptcfc
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC08locationE017featureController012ratchetStateE008lostModeH0ACSo014LACDTOLocationE0_p_So24LACDTOFeatureControlling_pSo013LACDTORatchetjE0_pSo010LACDTOLostL12FetchService_ptcfcTo
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC08locationE033_E856350D1C5EB666EF0471B129C641C4LLSo014LACDTOLocationE0_pvpWvd
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC16fetchEnvironment6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctF
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC16fetchEnvironment6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFTj
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC16fetchEnvironment6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFTo
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC16fetchEnvironment6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFTq
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC16fetchEnvironment6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFyAL_ANtcfU_
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC16fetchEnvironment6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFyAL_ANtcfU_TA
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC17featureController33_E856350D1C5EB666EF0471B129C641C4LLSo24LACDTOFeatureControlling_pvpWvd
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC18lostModeController33_E856350D1C5EB666EF0471B129C641C4LLSo010LACDTOLostG12FetchService_pvpWvd
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC23performFetchEnvironment33_E856350D1C5EB666EF0471B129C641C4LL6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFySo18LACDTOFeatureState_pcfU_
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC23performFetchEnvironment33_E856350D1C5EB666EF0471B129C641C4LL6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFySo18LACDTOFeatureState_pcfU_TA
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC23performFetchEnvironment33_E856350D1C5EB666EF0471B129C641C4LL6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFySo18LACDTOFeatureState_pcfU_ySo013LACDTORatchetX13WithWatchdogsCSg_AOtcfU_
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC23performFetchEnvironment33_E856350D1C5EB666EF0471B129C641C4LL6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFySo18LACDTOFeatureState_pcfU_ySo013LACDTORatchetX13WithWatchdogsCSg_AOtcfU_TA
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC23performFetchEnvironment33_E856350D1C5EB666EF0471B129C641C4LL6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFySo18LACDTOFeatureState_pcfU_ySo013LACDTORatchetX13WithWatchdogsCSg_AOtcfU_ySo014LACDTOLostModeX0CcfU_
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC23performFetchEnvironment33_E856350D1C5EB666EF0471B129C641C4LL6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFySo18LACDTOFeatureState_pcfU_ySo013LACDTORatchetX13WithWatchdogsCSg_AOtcfU_ySo014LACDTOLostModeX0CcfU_TA
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC23performFetchEnvironment33_E856350D1C5EB666EF0471B129C641C4LL6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFySo18LACDTOFeatureState_pcfU_ySo013LACDTORatchetX13WithWatchdogsCSg_AOtcfU_ySo014LACDTOLostModeX0CcfU_TATm
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC23performFetchEnvironment33_E856350D1C5EB666EF0471B129C641C4LL6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFySo18LACDTOFeatureState_pcfU_ySo013LACDTORatchetX13WithWatchdogsCSg_AOtcfU_ySo014LACDTOLostModeX0CcfU_ySo014LACDTOLocationX0CcfU_
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC23performFetchEnvironment33_E856350D1C5EB666EF0471B129C641C4LL6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFySo18LACDTOFeatureState_pcfU_ySo013LACDTORatchetX13WithWatchdogsCSg_AOtcfU_ySo014LACDTOLostModeX0CcfU_ySo014LACDTOLocationX0CcfU_TA
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC23performFetchEnvironment33_E856350D1C5EB666EF0471B129C641C4LL6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFySo18LACDTOFeatureState_pcfU_ySo013LACDTORatchetX13WithWatchdogsCSg_AOtcfU_ySo014LACDTOLostModeX0CcfU_ySo014LACDTOLocationX0CcfU_yAS_AOtcfU_
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderC23performFetchEnvironment33_E856350D1C5EB666EF0471B129C641C4LL6policy7options10completionySi_SDys11AnyHashableVypGySo0D0_pSg_s5Error_pSgtctFySo18LACDTOFeatureState_pcfU_ySo013LACDTORatchetX13WithWatchdogsCSg_AOtcfU_ySo014LACDTOLostModeX0CcfU_ySo014LACDTOLocationX0CcfU_yAS_AOtcfU_TA
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderCACycfC
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderCACycfc
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderCACycfcTo
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderCMF
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderCMa
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderCMf
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderCMn
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderCMo
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderCMu
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderCN
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderCfD
+ _$s23LocalAuthenticationCore25LACDTOEnvironmentProviderCfETo
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC04userE033_854280EF363A87DD6F4551230F28E0D3LLSo06NSUserE0CvpWvd
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC04userE0ACSo06NSUserE0C_tcfC
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC04userE0ACSo06NSUserE0C_tcfCTj
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC04userE0ACSo06NSUserE0C_tcfCTq
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC04userE0ACSo06NSUserE0C_tcfc
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC04userE0ACSo06NSUserE0C_tcfcTo
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKF
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFTY0_
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFTj
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFTjTQ0_
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFTjTu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFTo
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFTq
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFTu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFyyYacfU_To
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFyyYacfU_ToTA
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFyyYacfU_ToTATQ0_
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFyyYacfU_ToTATu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFyyYacfU_ToTY0_
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC12removeObject6forKeyySS_tYaKFyyYacfU_ToTu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC15unownedExecutorScevg
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC15unownedExecutorScevpMV
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKF
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFTY0_
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFTj
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFTjTQ0_
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFTjTu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFTo
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFTq
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFTu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFyyYacfU_To
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFyyYacfU_ToTA
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFyyYacfU_ToTATQ0_
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFyyYacfU_ToTATu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFyyYacfU_ToTY0_
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC4data6forKey10Foundation4DataVSgSS_tYaKFyyYacfU_ToTu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKF
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFTY0_
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFTj
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFTjTQ0_
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFTjTu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFTo
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFTq
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFTu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFyyYacfU_To
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFyyYacfU_ToTA
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFyyYacfU_ToTATQ0_
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFyyYacfU_ToTATu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFyyYacfU_ToTY0_
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC7setData_6forKeyy10Foundation0I0V_SStYaKFyyYacfU_ToTu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCACycfC
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCACycfc
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCACycfcTo
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCMF
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCMa
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCMf
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCMn
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCMo
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCMu
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCN
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCScAAAMc
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCScAAAMcMK
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCScAAAScA15unownedExecutorScevgTW
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCfD
+ _$s23LocalAuthenticationCore30LACUserDefaultsPersistentStoreCfd
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC010addPendingF0yyAA013LACDTOMutableieF0CF
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC010addPendingF0yyAA013LACDTOMutableieF0CFTj
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC010addPendingF0yyAA013LACDTOMutableieF0CFTo
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC010addPendingF0yyAA013LACDTOMutableieF0CFTq
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC010persistentG09workQueueACSo013LACPersistentG0_p_So17OS_dispatch_queueCtcfC
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC010persistentG09workQueueACSo013LACPersistentG0_p_So17OS_dispatch_queueCtcfCTj
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC010persistentG09workQueueACSo013LACPersistentG0_p_So17OS_dispatch_queueCtcfCTq
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC010persistentG09workQueueACSo013LACPersistentG0_p_So17OS_dispatch_queueCtcfc
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC010persistentG09workQueueACSo013LACPersistentG0_p_So17OS_dispatch_queueCtcfcTo
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC013removePendingF04withySS_tF
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC013removePendingF04withySS_tFTj
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC013removePendingF04withySS_tFTo
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC013removePendingF04withySS_tFTq
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC07pendingF014withIdentifierAA020LACDTOMutablePendingeF0CSgSS_tF
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC07pendingF014withIdentifierAA020LACDTOMutablePendingeF0CSgSS_tFTj
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC07pendingF014withIdentifierAA020LACDTOMutablePendingeF0CSgSS_tFTo
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC07pendingF014withIdentifierAA020LACDTOMutablePendingeF0CSgSS_tFTq
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC18pendingEvaluationsSayAA020LACDTOMutablePendingeF0CGvg
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC18pendingEvaluationsSayAA020LACDTOMutablePendingeF0CGvgTj
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC18pendingEvaluationsSayAA020LACDTOMutablePendingeF0CGvgTo
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC18pendingEvaluationsSayAA020LACDTOMutablePendingeF0CGvgTq
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC18pendingEvaluationsSayAA020LACDTOMutablePendingeF0CGvpMV
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC18persistEvaluationsyyF
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC18persistEvaluationsyyFTj
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC18persistEvaluationsyyFTo
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC18persistEvaluationsyyFTq
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC22pendingEvaluationsDict33_2F3A14333F740D7E8D468D748269021ELLSDySSAA020LACDTOMutablePendingeF0CGvM
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC22pendingEvaluationsDict33_2F3A14333F740D7E8D468D748269021ELLSDySSAA020LACDTOMutablePendingeF0CGvM.resume.0
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC22pendingEvaluationsDict33_2F3A14333F740D7E8D468D748269021ELLSDySSAA020LACDTOMutablePendingeF0CGvpWvd
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tF
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFTj
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFTo
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFTq
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYaYbcfU_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYaYbcfU_TA
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYaYbcfU_TATQ0_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYaYbcfU_TATu
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYaYbcfU_TQ1_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYaYbcfU_TY0_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYaYbcfU_TY2_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYaYbcfU_TY3_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYaYbcfU_Tu
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYaYbcfU_yyYbcfU0_TA
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC24loadPersistedEvaluations10completionyySayAA020LACDTOMutablePendingeF0CGSg_s5Error_pSgtc_tFyyYaYbcfU_yyYbcfU_TA
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKF
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFTQ1_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFTY0_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFTY2_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFTY3_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFTj
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFTjTQ0_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFTjTu
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFTo
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFTq
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFTu
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFyyYacfU_To
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFyyYacfU_ToTA
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFyyYacfU_ToTATQ0_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFyyYacfU_ToTATu
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFyyYacfU_ToTQ0_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC4loadSayAA020LACDTOMutablePendingeF0CGyYaKFyyYacfU_ToTu
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC5store33_2F3A14333F740D7E8D468D748269021ELLSo013LACPersistentG0_pvpWvd
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyF
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYaYbcfU_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYaYbcfU_TA
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYaYbcfU_TA.47
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYaYbcfU_TA.47TQ0_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYaYbcfU_TA.47Tu
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYaYbcfU_TATQ0_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYaYbcfU_TATu
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYaYbcfU_TQ1_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYaYbcfU_TY0_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYaYbcfU_TY2_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYaYbcfU_TY3_
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC7persist33_2F3A14333F740D7E8D468D748269021ELLyyFyyYaYbcfU_Tu
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC8storeKeySSvau
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC8storeKeySSvgZ
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC8storeKeySSvgZTo
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC8storeKeySSvpZ
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC9workQueue33_2F3A14333F740D7E8D468D748269021ELLSo17OS_dispatch_queueCvpWvd
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreCACycfC
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreCACycfc
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreCACycfcTo
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreCMF
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreCMa
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreCMf
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreCMn
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreCMo
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreCMu
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreCN
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreCfD
+ _$s23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreCfETo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLO11stringValueAFSgSS_tcfCTf4nd_n
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOAFSQAAWL
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOAFSQAAWl
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOAFs0H3KeyAAWL
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOAFs0H3KeyAAWl
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOAFs23CustomStringConvertibleAAWL
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOAFs23CustomStringConvertibleAAWl
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOAFs28CustomDebugStringConvertibleAAWL
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOAFs28CustomDebugStringConvertibleAAWl
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOMF
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOMXX
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOMa
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOMf
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOMn
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOSHAAMc
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOSHAAMcMK
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOSHAASH13_rawHashValue4seedS2i_tFTW
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOSHAASH4hash4intoys6HasherVz_tFTW
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOSHAASH9hashValueSivgTW
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOSHAASQWb
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOSQAAMc
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOSQAAMcMK
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOSQAASQ2eeoiySbx_xtFZTW
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOWV
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs0H3KeyAAMc
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs0H3KeyAAMcMK
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs0H3KeyAAs23CustomStringConvertiblePWb
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs0H3KeyAAs28CustomDebugStringConvertiblePWb
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs0H3KeyAAsAGP11stringValueSSvgTW
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs0H3KeyAAsAGP11stringValuexSgSS_tcfCTW
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs0H3KeyAAsAGP8intValueSiSgvgTW
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs0H3KeyAAsAGP8intValuexSgSi_tcfCTW
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs23CustomStringConvertibleAAMc
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs23CustomStringConvertibleAAMcMK
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs23CustomStringConvertibleAAsAGP11descriptionSSvgTW
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs28CustomDebugStringConvertibleAAMc
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs28CustomDebugStringConvertibleAAMcMK
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs28CustomDebugStringConvertibleAAsAGP16debugDescriptionSSvgTW
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOwet
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOwst
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOwug
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOwui
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOwup
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10identifierACSS_tcfC
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10identifierACSS_tcfCTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10identifierACSS_tcfCTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10identifierACSS_tcfc
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10identifierACSS_tcfcTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10identifierSSvg
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10identifierSSvgTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10identifierSSvpMV
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10identifierSSvpWvd
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvM
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvM.resume.0
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvMTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvMTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvg
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvgTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvgTm
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvgTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvgTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvpACTk
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvpMV
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvpWvd
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvs
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvsTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvsTm
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvsTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11callbackURL10Foundation0I0VSgvsTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11descriptionSSvg
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11descriptionSSvgTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvM
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvM.resume.0
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvMTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvMTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvg
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvgTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvgTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvgTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvpMV
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvpWvd
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvs
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvsTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvsTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC11ratchetUUIDSSSgvsTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvM
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvM.resume.0
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvMTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvMTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvg
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvgTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvgTm
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvgTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvgToTm
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvgTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvpMV
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvpWvd
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvs
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvsTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvsTm
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvsTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvsToTm
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14callbackReasonSSSgvsTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvM
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvM.resume.0
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvMTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvMTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvg
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvgTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvgTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvgTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvpACTk
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvpMV
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvpWvd
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvs
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvsTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvsTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC14coolOffStarted10Foundation4DateVSgvsTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23isNotificationScheduled3forSb10Foundation4DateV_tF
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23isNotificationScheduled3forSb10Foundation4DateV_tFTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23isNotificationScheduled3forSb10Foundation4DateV_tFTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23isNotificationScheduled3forSb10Foundation4DateV_tFTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvM
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvM.resume.0
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvMTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvMTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvg
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvgTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvgTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvgToTm
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvgTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvpACTk
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvpMV
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvpWvd
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvs
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvsTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvsTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvsToTm
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC23notificationScheduledAt10Foundation4DateVSgvsTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC30hasNotifiedUserAboutCompletionSbvg
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC30hasNotifiedUserAboutCompletionSbvgTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC30hasNotifiedUserAboutCompletionSbvgTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC30hasNotifiedUserAboutCompletionSbvgTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC30hasNotifiedUserAboutCompletionSbvpMV
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC4fromACs7Decoder_p_tKcfC
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC4fromACs7Decoder_p_tKcfCTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC4fromACs7Decoder_p_tKcfCTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC4fromACs7Decoder_p_tKcfc
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC6encode2toys7Encoder_p_tKF
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC6encode2toys7Encoder_p_tKFTj
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC6encode2toys7Encoder_p_tKFTq
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC7isEqualySbypSgF
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC7isEqualySbypSgFTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCACSEAAWL
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCACSeAAWL
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCACSeAAWlTm
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCACycfC
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCACycfc
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCACycfcTo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCMF
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCMU
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCMa
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCMf
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCMl
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCMn
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCMo
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCMr
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCMu
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCN
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCSEAAMc
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCSEAAMcMK
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCSEAASE6encode2toys7Encoder_p_tKFTW
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCSeAAMc
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCSeAAMcMK
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCSeAASe4fromxs7Decoder_p_tKcfCTW
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCfD
+ _$s23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCfETo
+ _$s23LocalAuthenticationCore38LACDTOPendingPolicyEvaluationStoreType_pMF
+ _$s2os0A11LogInternal_3log4typeyAA12OSLogMessageV_So03OS_a1_D0CSo0a1_d1_E2_tatFyySpys5UInt8VGz_SpySo8NSObjectCSgGSgzSpyypGSgztcXEfU_
+ _$s2os14OSLogArgumentsV6appendyySSycFySpys5UInt8VGz_SpySo8NSObjectCSgGSgzSpyypGSgztcfU_
+ _$s2os14OSLogArgumentsV6appendyySo8NSObjectCSgycFySpys5UInt8VGz_SpyAGGSgzSpyypGSgztcfU_
+ _$s2os14OSLogArgumentsV6appendyys5UInt8VFySpyAFGz_SpySo8NSObjectCSgGSgzSpyypGSgztcfU_
+ _$s2os18OSLogInterpolationV06appendC0_5align7privacyySSyXA_AA0B15StringAlignmentVAA0B7PrivacyVtFSSycfu_
+ _$s2os6LoggerV23LocalAuthenticationCoreE13dtoEvaluationACvgZ
+ _$s2os6LoggerV23LocalAuthenticationCoreE14dtoEnvironmentACvgZ
+ _$s2os6LoggerV23LocalAuthenticationCoreE14dtoEnvironmentACvgZTm
+ _$s2os6LoggerV23LocalAuthenticationCoreE5dtoUIACvgZ
+ _$s2os6LoggerV23LocalAuthenticationCoreE5testsACvgZ
+ _$s2os9serialize_2atys5UInt8V_SpyAEGztF
+ _$s8Dispatch0A13WorkItemFlagsVACs10SetAlgebraAAWL
+ _$s8Dispatch0A13WorkItemFlagsVMa
+ _$s8Dispatch0A13WorkItemFlagsVMn
+ _$s8Dispatch0A13WorkItemFlagsVs10SetAlgebraAAMc
+ _$s8Dispatch0A3QoSV11unspecifiedACvgZ
+ _$s8Dispatch0A3QoSVMa
+ _$s8RawValueSYTl
+ _$sBi64_WV
+ _$sIeg_SgWOe
+ _$sIeghH_ytIeghHr_TR
+ _$sIeghH_ytIeghHr_TRTA
+ _$sIeghH_ytIeghHr_TRTA.22
+ _$sIeghH_ytIeghHr_TRTA.22TQ0_
+ _$sIeghH_ytIeghHr_TRTA.22Tu
+ _$sIeghH_ytIeghHr_TRTA.36
+ _$sIeghH_ytIeghHr_TRTA.36TQ0_
+ _$sIeghH_ytIeghHr_TRTA.36Tu
+ _$sIeghH_ytIeghHr_TRTATQ0_
+ _$sIeghH_ytIeghHr_TRTATu
+ _$sIeghH_ytIeghHr_TRTQ0_
+ _$sIeghH_ytIeghHr_TRTu
+ _$sIegh_IeyBh_TR
+ _$sIeyB_Ieg_TRTA
+ _$sSD10FoundationE19_bridgeToObjectiveCSo12NSDictionaryCyF
+ _$sSD10FoundationE36_unconditionallyBridgeFromObjectiveCySDyxq_GSo12NSDictionaryCSgFZ
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSS_23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCTg5Tf4nd_n
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCs11AnyHashableV_ypTg5Tf4nd_n
+ _$sSD8IteratorV8_VariantOyxq___GSHRzr0_lWOe
+ _$sSD8_VariantV11removeValue6forKeyq_Sgx_tFSS_23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCTg5
+ _$sSDsSQR_rlE2eeoiySbSDyxq_G_ABtFZSS_23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCTg5Tf4nnd_n
+ _$sSE6encode2toys7Encoder_p_tKFTq
+ _$sSEMp
+ _$sSH13_rawHashValue4seedS2i_tFTq
+ _$sSH4hash4intoys6HasherVz_tFTq
+ _$sSH9hashValueSivgTq
+ _$sSHMp
+ _$sSHSQTb
+ _$sSKsSS7ElementRtzrlE6joined9separatorS2S_tF
+ _$sSL2geoiySbx_xtFZTj
+ _$sSL2leoiySbx_xtFZTj
+ _$sSNy10Foundation4DateVGMD
+ _$sSQ2eeoiySbx_xtFZTj
+ _$sSQ2eeoiySbx_xtFZTq
+ _$sSQMp
+ _$sSS4hash4intoys6HasherVz_tF
+ _$sSS6appendyySSF
+ _$sSSSgMD
+ _$sSTsE21_copySequenceContents12initializing8IteratorQz_SitSry7ElementQzG_tFSD6ValuesVySS23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC_G_Tg5
+ _$sSY8rawValue03RawB0QzvgTq
+ _$sSY8rawValuexSg03RawB0Qz_tcfCTq
+ _$sSYMp
+ _$sSay23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCGMD
+ _$sSay23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCGSayxGSEsSERzlWL
+ _$sSay23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCGSayxGSesSeRzlWL
+ _$sSay23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCGSayxGSesSeRzlWlTm
+ _$sSay8Dispatch0A13WorkItemFlagsVGMD
+ _$sSay8Dispatch0A13WorkItemFlagsVGSayxGSTsWL
+ _$sSay8Dispatch0A13WorkItemFlagsVGSayxGSTsWl
+ _$sSaySSGMD
+ _$sSaySSGSayxGSKsWL
+ _$sSaySSGSayxGSKsWl
+ _$sSayxGSEsSERzlMc
+ _$sSayxGSKsMc
+ _$sSayxGSTsMc
+ _$sSayxGSesSeRzlMc
+ _$sScA15unownedExecutorScevgTq
+ _$sScAMp
+ _$sScP8rawValues5UInt8Vvg
+ _$sScPMa
+ _$sScPSgMD
+ _$sScPSgWOh
+ _$sSe4fromxs7Decoder_p_tKcfCTq
+ _$sSeMp
+ _$sSo13os_log_type_ta0A0E5errorABvgZ
+ _$sSo13os_log_type_ta0A0E7defaultABvgZ
+ _$sSo17LACDTOEnvironment_pSgSo7NSErrorCSgIeyByy_ABs5Error_pSgIeggg_TR
+ _$sSo17LACDTOEnvironment_pSgSo7NSErrorCSgIeyByy_ABs5Error_pSgIeggg_TRTA
+ _$sSo17LACRatchetUIStateVMB
+ _$sSo17LACRatchetUIStateVML
+ _$sSo17LACRatchetUIStateVMa
+ _$sSo17LACRatchetUIStateVMf
+ _$sSo17LACRatchetUIStateVMn
+ _$sSo17OS_dispatch_queueC8DispatchE5async5group3qos5flags7executeySo0a1_b1_F0CSg_AC0D3QoSVAC0D13WorkItemFlagsVyyXBtF
+ _$sSo18LACDTOFeatureState_pIegg_SoAA_pIeyBy_TR
+ _$sSo18LACPersistentStoreP23LocalAuthenticationCoreE3set6object3foryqd___SStYaKSERd__lF
+ _$sSo18LACPersistentStoreP23LocalAuthenticationCoreE3set6object3foryqd___SStYaKSERd__lFTQ1_
+ _$sSo18LACPersistentStoreP23LocalAuthenticationCoreE3set6object3foryqd___SStYaKSERd__lFTY0_
+ _$sSo18LACPersistentStoreP23LocalAuthenticationCoreE3set6object3foryqd___SStYaKSERd__lFTY2_
+ _$sSo18LACPersistentStoreP23LocalAuthenticationCoreE3set6object3foryqd___SStYaKSERd__lFTY3_
+ _$sSo18LACPersistentStoreP23LocalAuthenticationCoreE3set6object3foryqd___SStYaKSERd__lFTu
+ _$sSo18LACPersistentStoreP23LocalAuthenticationCoreE6object6forKeyqd__SgSS_tYaKSeRd__lF
+ _$sSo18LACPersistentStoreP23LocalAuthenticationCoreE6object6forKeyqd__SgSS_tYaKSeRd__lFTQ1_
+ _$sSo18LACPersistentStoreP23LocalAuthenticationCoreE6object6forKeyqd__SgSS_tYaKSeRd__lFTY0_
+ _$sSo18LACPersistentStoreP23LocalAuthenticationCoreE6object6forKeyqd__SgSS_tYaKSeRd__lFTY2_
+ _$sSo18LACPersistentStoreP23LocalAuthenticationCoreE6object6forKeyqd__SgSS_tYaKSeRd__lFTY3_
+ _$sSo18LACPersistentStoreP23LocalAuthenticationCoreE6object6forKeyqd__SgSS_tYaKSeRd__lFTu
+ _$sSo19LACDTOLocationStateCIegg_ABIeyBy_TR
+ _$sSo19LACDTOLocationStateCIegg_ABIeyBy_TRTm
+ _$sSo19LACDTOLostModeStateCIegg_ABIeyBy_TR
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5style10completionySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVys5Error_pSgcSgtF
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5style10completionySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVys5Error_pSgcSgtFyyYaYbcfU_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5style10completionySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVys5Error_pSgcSgtFyyYaYbcfU_TA
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5style10completionySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVys5Error_pSgcSgtFyyYaYbcfU_TATQ0_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5style10completionySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVys5Error_pSgcSgtFyyYaYbcfU_TATu
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5style10completionySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVys5Error_pSgcSgtFyyYaYbcfU_TQ1_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5style10completionySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVys5Error_pSgcSgtFyyYaYbcfU_TY0_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5style10completionySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVys5Error_pSgcSgtFyyYaYbcfU_TY2_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5style10completionySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVys5Error_pSgcSgtFyyYaYbcfU_TY3_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5style10completionySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVys5Error_pSgcSgtFyyYaYbcfU_Tu
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKF
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTQ11_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTQ1_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTQ3_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTQ5_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTQ7_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTQ9_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY0_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY10_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY12_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY13_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY14_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY15_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY16_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY17_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY18_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY2_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY4_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY6_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTY8_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE10transition33_25C38F3ED33D4353071787DC1A61A852LL2to4with5styleySo0A7UIStateV_SDys11AnyHashableVypGSo26LACAuthUIPresentationStyleVtYaKFTu
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE16showCoolOffSheet7options22presentationCompletion05sheetM0ySDys11AnyHashableVypG_ys5Error_pSgcSgyycSgtF
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE16showCoolOffSheet7options22presentationCompletion05sheetM0ySDys11AnyHashableVypG_ys5Error_pSgcSgyycSgtFTo
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss10completionyys5Error_pSgcSg_tF
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss10completionyys5Error_pSgcSg_tFTo
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss10completionyys5Error_pSgcSg_tFyyYaYbcfU_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss10completionyys5Error_pSgcSg_tFyyYaYbcfU_TA
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss10completionyys5Error_pSgcSg_tFyyYaYbcfU_TATQ0_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss10completionyys5Error_pSgcSg_tFyyYaYbcfU_TATu
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss10completionyys5Error_pSgcSg_tFyyYaYbcfU_TQ1_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss10completionyys5Error_pSgcSg_tFyyYaYbcfU_TY0_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss10completionyys5Error_pSgcSg_tFyyYaYbcfU_TY2_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss10completionyys5Error_pSgcSg_tFyyYaYbcfU_TY3_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss10completionyys5Error_pSgcSg_tFyyYaYbcfU_Tu
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss33_25C38F3ED33D4353071787DC1A61A852LLyyYaKF
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss33_25C38F3ED33D4353071787DC1A61A852LLyyYaKFTQ1_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss33_25C38F3ED33D4353071787DC1A61A852LLyyYaKFTQ3_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss33_25C38F3ED33D4353071787DC1A61A852LLyyYaKFTY0_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss33_25C38F3ED33D4353071787DC1A61A852LLyyYaKFTY2_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss33_25C38F3ED33D4353071787DC1A61A852LLyyYaKFTY4_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss33_25C38F3ED33D4353071787DC1A61A852LLyyYaKFTY5_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss33_25C38F3ED33D4353071787DC1A61A852LLyyYaKFTY6_
+ _$sSo21LACRatchetFlowManagerC23LocalAuthenticationCoreE7dismiss33_25C38F3ED33D4353071787DC1A61A852LLyyYaKFTu
+ _$sSo24LACDTOMutableEnvironmentC23LocalAuthenticationCoreE13locationState07featureG007ratchetG0ABSo014LACDTOLocationG0C_So013LACDTOFeatureG0_pSo013LACDTORatchetG13WithWatchdogsCtc33_E856350D1C5EB666EF0471B129C641C4LlfC
+ _$sSo24LACDTOMutableEnvironmentCML
+ _$sSo26LACAuthUIPresentationStyleVMB
+ _$sSo26LACAuthUIPresentationStyleVML
+ _$sSo26LACAuthUIPresentationStyleVMa
+ _$sSo26LACAuthUIPresentationStyleVMaTm
+ _$sSo26LACAuthUIPresentationStyleVMf
+ _$sSo26LACAuthUIPresentationStyleVMn
+ _$sSo26LACAuthUIPresentationStyleVSQSCMc
+ _$sSo26LACAuthUIPresentationStyleVSQSCMcMK
+ _$sSo26LACAuthUIPresentationStyleVSQSCSQ2eeoiySbx_xtFZTW
+ _$sSo26LACAuthUIPresentationStyleVSYSCMA
+ _$sSo26LACAuthUIPresentationStyleVSYSCMc
+ _$sSo26LACAuthUIPresentationStyleVSYSCMcMK
+ _$sSo26LACAuthUIPresentationStyleVSYSCSY8rawValue03RawE0QzvgTW
+ _$sSo26LACAuthUIPresentationStyleVSYSCSY8rawValuexSg03RawE0Qz_tcfCTW
+ _$sSo29LACDTOPendingPolicyEvaluation_pMD
+ _$sSo31LACDTORatchetStateWithWatchdogsCSgs5Error_pSgIeggg_ACSo7NSErrorCSgIeyByy_TR
+ _$sSo33LACDTOMutableLostModeFetchRequestC23LocalAuthenticationCoreE6policy7options12featureState07ratchetL0ABSi_SDys11AnyHashableVypGSo013LACDTOFeatureL0_pSo013LACDTORatchetL13WithWatchdogsCtc33_E856350D1C5EB666EF0471B129C641C4LlfC
+ _$sSo33LACDTOMutableLostModeFetchRequestCML
+ _$sSo33LACDTOMutableLostModeFetchRequestCMaTm
+ _$sSo6NSDataCSgSo7NSErrorCSgIeyByy_10Foundation4DataVSgSo18LACPersistentStoreRzSeRd__r__lTz_
+ _$sSo7NSArrayCSgSo7NSErrorCSgIeyByy_Say23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCGSgs5Error_pSgIeggg_TR
+ _$sSo7NSArrayCSgSo7NSErrorCSgIeyByy_Say23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCGSgs5Error_pSgIeggg_TRTA
+ _$sSo7NSErrorCSgIeyBy_s5Error_pSgIegg_TRTA.18
+ _$sSo7NSErrorCSgIeyBy_ytSo18LACPersistentStoreRzSERd__r__lTz_
+ _$sSo7NSErrorCSgIeyBy_ytTz_
+ _$sSo8NSBundleC23LocalAuthenticationCoreE7current33_06C5009961CF12380B02F6187ECF7956LLABvpZ
+ _$sSo8NSBundleC23LocalAuthenticationCoreE7current33_06C5009961CF12380B02F6187ECF7956LL_WZ
+ _$sSo8NSBundleC23LocalAuthenticationCoreE7current33_06C5009961CF12380B02F6187ECF7956LL_Wz
+ _$sSo8NSObjectC10ObjectiveCE2eeoiySbAB_ABtFZ
+ _$sSoMXM
+ _$sSq16debugDescriptionSSvg
+ _$sSqMa
+ _$ss018_bridgeAnyObjectToB0yypyXlSgF
+ _$ss10SetAlgebraPyxqd__ncSTRd__7ElementQyd__ACRtzlufCTj
+ _$ss10_HashTableV12previousHole6beforeAB6BucketVAF_tF
+ _$ss11AnyHashableV13_rawHashValue4seedS2i_tF
+ _$ss11AnyHashableV2eeoiySbAB_ABtFZ
+ _$ss11AnyHashableVMn
+ _$ss11AnyHashableVN
+ _$ss11AnyHashableVSHsWP
+ _$ss11AnyHashableVWOc
+ _$ss11AnyHashableVWOh
+ _$ss11AnyHashableV_yptMD
+ _$ss11AnyHashableV_yptWOc
+ _$ss11_StringGutsV4growyySiF
+ _$ss17_NativeDictionaryV20_copyOrMoveAndResize8capacity12moveElementsySi_SbtFSS_23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCTg5
+ _$ss17_NativeDictionaryV4copyyyFSS_23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCTg5
+ _$ss17_NativeDictionaryV7_delete2atys10_HashTableV6BucketV_tFSS_23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCTg5
+ _$ss17_NativeDictionaryV8setValue_6forKey8isUniqueyq_n_xSbtFSS_23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCTg5
+ _$ss18_DictionaryStorageC4copy8originalAByxq_Gs05__RawaB0C_tFZ
+ _$ss18_DictionaryStorageC6resize8original8capacity4moveAByxq_Gs05__RawaB0C_SiSbtFZ
+ _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
+ _$ss18_DictionaryStorageCMn
+ _$ss18_DictionaryStorageCySS23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationCGMD
+ _$ss18_DictionaryStorageCys11AnyHashableVypGMD
+ _$ss22KeyedDecodingContainerV15decodeIfPresent_6forKeySSSgSSm_xtKF
+ _$ss22KeyedDecodingContainerV15decodeIfPresent_6forKeyqd__Sgqd__m_xtKSeRd__lF
+ _$ss22KeyedDecodingContainerV6decode_6forKeyS2Sm_xtKF
+ _$ss22KeyedDecodingContainerVMn
+ _$ss22KeyedDecodingContainerVy23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOGMD
+ _$ss22KeyedEncodingContainerV15encodeIfPresent_6forKeyySSSg_xtKF
+ _$ss22KeyedEncodingContainerV15encodeIfPresent_6forKeyyqd__Sg_xtKSERd__lF
+ _$ss22KeyedEncodingContainerV6encode_6forKeyySS_xtKF
+ _$ss22KeyedEncodingContainerVMn
+ _$ss22KeyedEncodingContainerVy23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOGMD
+ _$ss22__RawDictionaryStorageC4find_9hashValues10_HashTableV6BucketV6bucket_Sb5foundtx_SitSHRzlFSS_Tg5
+ _$ss22__RawDictionaryStorageC4find_9hashValues10_HashTableV6BucketV6bucket_Sb5foundtx_SitSHRzlFs11AnyHashableV_Tg5
+ _$ss22__RawDictionaryStorageC4findys10_HashTableV6BucketV6bucket_Sb5foundtxSHRzlFSS_Tg5
+ _$ss22__RawDictionaryStorageC4findys10_HashTableV6BucketV6bucket_Sb5foundtxSHRzlFs11AnyHashableV_Tg5
+ _$ss23CustomStringConvertibleMp
+ _$ss23CustomStringConvertibleP11descriptionSSvgTq
+ _$ss23_ContiguousArrayStorageCySSGMD
+ _$ss23_ContiguousArrayStorageCyyXlGMD
+ _$ss27_stringCompareWithSmolCheck__9expectingSbs11_StringGutsV_ADs01_G16ComparisonResultOtF
+ _$ss28CustomDebugStringConvertibleMp
+ _$ss28CustomDebugStringConvertibleP16debugDescriptionSSvgTq
+ _$ss32_copyCollectionToContiguousArrayys0dE0Vy7ElementQzGxSlRzlFSD6ValuesVySS23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC_G_Tg5
+ _$ss53KEY_TYPE_OF_DICTIONARY_VIOLATES_HASHABLE_REQUIREMENTSys5NeverOypXpF
+ _$ss5ErrorMp
+ _$ss5ErrorWS
+ _$ss5Error_pMD
+ _$ss5Error_pSgIegg_SgWOy
+ _$ss6HasherV5_seedABSi_tcfC
+ _$ss6HasherV8_combineyySuF
+ _$ss6HasherV9_finalizeSiyF
+ _$ss7DecoderP9container7keyedBys22KeyedDecodingContainerVyqd__Gqd__m_tKs9CodingKeyRd__lFTj
+ _$ss7EncoderP9container7keyedBys22KeyedEncodingContainerVyqd__Gqd__m_ts9CodingKeyRd__lFTj
+ _$ss9CodingKeyMp
+ _$ss9CodingKeyP11stringValueSSvgTq
+ _$ss9CodingKeyP11stringValuexSgSS_tcfCTq
+ _$ss9CodingKeyP8intValueSiSgvgTq
+ _$ss9CodingKeyP8intValuexSgSi_tcfCTq
+ _$ss9CodingKeyPs23CustomStringConvertibleTb
+ _$ss9CodingKeyPs28CustomDebugStringConvertibleTb
+ _$ss9CodingKeyPsE11descriptionSSvg
+ _$ss9CodingKeyPsE16debugDescriptionSSvg
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.18
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.18TQ0_
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.18Tu
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.31
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.31TQ0_
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.31Tu
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.52
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.52TQ0_
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TA.52Tu
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TATQ0_
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TATu
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5TQ0_
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tg5Tu
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.27
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.27TQ0_
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.27Tu
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.41
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.41TQ0_
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.41Tu
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TATQ0_
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TATu
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TQ0_
+ _$sxIeghHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5Tu
+ _$sypSgMD
+ _$sypWOb
+ _$sytN
+ _AuthKitLibrary
+ _AuthKitLibraryCore.frameworkLibrary
+ _CoreRoutineLibraryCore.frameworkLibrary
+ _LACDTBiometryWatchdogGlobalFallbackTime
+ _LACDTOEnableFeatureResultKeyBiometricLivenessFlag
+ _LACDTOEnableFeatureResultKeyHSA2AccountEnabled
+ _LACDTOEnableFeatureResultKeyLocationServicesEnabled
+ _LACDTOLocationStateMaxValidity
+ _LACDTOLostModeFetchStrategyFromRequest
+ _LACDTOLostModeStateMaxAgeSeconds
+ _LACDTORatchetStateDurationInfinite
+ _LACDTORatchetStateMaxValidity
+ _LACDarwinNotificationRatchetStateDidChange
+ _LACDarwinNotificationSystemLanguageDidChange
+ _LACEntitlementDTO
+ _LACEntitlementDTOFallbackToNoAuth
+ _LACEntitlementDTOShortExpiration
+ _LACErrorCodeRequestFailed
+ _LACErrorCodeUserCustomRatchetCancel
+ _LACErrorSubcodeBeforeFirstUnlock
+ _LACLogDTO
+ _LACLogDTO.__logObj
+ _LACLogDTO.onceToken
+ _LACLogDTOClient
+ _LACLogDTOClient.__logObj
+ _LACLogDTOClient.onceToken
+ _LACLogDTOEnvironment
+ _LACLogDTOEnvironment.__logObj
+ _LACLogDTOEnvironment.onceToken
+ _LACLogDTOEvaluation
+ _LACLogDTOEvaluation.__logObj
+ _LACLogDTOEvaluation.onceToken
+ _LACLogDTOEvent
+ _LACLogDTOEvent.__logObj
+ _LACLogDTOEvent.onceToken
+ _LACLogDTOFeature
+ _LACLogDTOFeature.__logObj
+ _LACLogDTOFeature.onceToken
+ _LACLogDTOLocation
+ _LACLogDTOLocation.__logObj
+ _LACLogDTOLocation.onceToken
+ _LACLogDTOLostMode
+ _LACLogDTOLostMode.__logObj
+ _LACLogDTOLostMode.onceToken
+ _LACLogDTONotifications
+ _LACLogDTONotifications.__logObj
+ _LACLogDTONotifications.onceToken
+ _LACLogDTOState
+ _LACLogDTOState.__logObj
+ _LACLogDTOState.onceToken
+ _LACLogDTOStorage
+ _LACLogDTOStorage.__logObj
+ _LACLogDTOStorage.onceToken
+ _LACLogDTOTimers
+ _LACLogDTOTimers.__logObj
+ _LACLogDTOTimers.onceToken
+ _LACLogDTOUI
+ _LACLogDTOUI.__logObj
+ _LACLogDTOUI.onceToken
+ _LACLogSubsystem
+ _LACPolicyIsLocationBasedPolicy
+ _LACPolicyLocationBasedDeviceOwnerAuthentication
+ _LACPolicyLocationBasedDeviceOwnerAuthenticationWithBiometricRatchet
+ _LACPolicyOptionAuthenticationCallbackReason
+ _LACPolicyOptionAuthenticationCallbackURL
+ _LACPolicyOptionAuthenticationIdentifier
+ _LACPolicyOptionBeginRatchetLocalizedText
+ _LACPolicyOptionBeginRatchetLocalizedTitle
+ _LACPolicyOptionBeginRatchetShowsLocationWarning
+ _LACPolicyOptionCountdownLocalizedText
+ _LACPolicyOptionDTO
+ _LACPolicyOptionFallbackToNoAuthentication
+ _LACPolicyOptionUseDTOStrings
+ _LACPolicyOptionUseShortExpirationTimer
+ _NSGlobalDomain
+ _NSStringFromClass
+ _NSStringFromLACDTOLostModeFetchStrategy
+ _NSStringFromLACDTORatchetStateRawValue
+ _NSStringFromLADTOEventRawValue
+ _NSStringFromSelector
+ _OBJC_CLASS_$_LACDTOBiometryWatchdog
+ _OBJC_CLASS_$_LACDTOBiometryWatchdogPack
+ _OBJC_CLASS_$_LACDTODarwinNotificationsController
+ _OBJC_CLASS_$_LACDTOEnvironmentProviderFactory
+ _OBJC_CLASS_$_LACDTOEvent
+ _OBJC_CLASS_$_LACDTOEventBus
+ _OBJC_CLASS_$_LACDTOFeatureController
+ _OBJC_CLASS_$_LACDTOKVStoreValue
+ _OBJC_CLASS_$_LACDTOLocationMonitor
+ _OBJC_CLASS_$_LACDTOLocationProviderCRAdapter
+ _OBJC_CLASS_$_LACDTOLocationProviderKVSAdapter
+ _OBJC_CLASS_$_LACDTOLocationState
+ _OBJC_CLASS_$_LACDTOLostModeController
+ _OBJC_CLASS_$_LACDTOLostModeProviderAKAdapter
+ _OBJC_CLASS_$_LACDTOLostModeProviderKVSAdapter
+ _OBJC_CLASS_$_LACDTOLostModeState
+ _OBJC_CLASS_$_LACDTOMutableEnvironment
+ _OBJC_CLASS_$_LACDTOMutableFeatureState
+ _OBJC_CLASS_$_LACDTOMutableLostModeFetchRequest
+ _OBJC_CLASS_$_LACDTOMutablePolicyEvaluationRequest
+ _OBJC_CLASS_$_LACDTOMutablePolicyEvaluationResult
+ _OBJC_CLASS_$_LACDTONotificationManager
+ _OBJC_CLASS_$_LACDTOPendingPolicyEvaluationController
+ _OBJC_CLASS_$_LACDTOPolicyEvaluationController
+ _OBJC_CLASS_$_LACDTORatchetNotificationCoolOff
+ _OBJC_CLASS_$_LACDTORatchetState
+ _OBJC_CLASS_$_LACDTORatchetStateMonitor
+ _OBJC_CLASS_$_LACDTORatchetStateWithWatchdogs
+ _OBJC_CLASS_$_LACDTOServiceXPCClient
+ _OBJC_CLASS_$_LACDTOServiceXPCHost
+ _OBJC_CLASS_$_LACDTOSignpostEvent
+ _OBJC_CLASS_$_LACPersistentStoreFactory
+ _OBJC_CLASS_$_LACRatchetFlowManager
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_SwiftNativeNSObject
+ _OBJC_CLASS_$__TtC23LocalAuthenticationCore25LACDTOEnvironmentProvider
+ _OBJC_CLASS_$__TtC23LocalAuthenticationCore30LACUserDefaultsPersistentStore
+ _OBJC_CLASS_$__TtC23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStore
+ _OBJC_CLASS_$__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation
+ _OBJC_IVAR_$_LACDTOBiometryWatchdog._isRunning
+ _OBJC_IVAR_$_LACDTOBiometryWatchdog._maxThreshold
+ _OBJC_IVAR_$_LACDTOBiometryWatchdog._minThreshold
+ _OBJC_IVAR_$_LACDTOBiometryWatchdog._time
+ _OBJC_IVAR_$_LACDTOBiometryWatchdogPack._biometryWatchdogDTO
+ _OBJC_IVAR_$_LACDTOBiometryWatchdogPack._biometryWatchdogGlobal
+ _OBJC_IVAR_$_LACDTODarwinNotificationsController._notificationCenter
+ _OBJC_IVAR_$_LACDTOEvent._rawValue
+ _OBJC_IVAR_$_LACDTOEvent._value
+ _OBJC_IVAR_$_LACDTOEventBus._eventHandlers
+ _OBJC_IVAR_$_LACDTOFeatureController._device
+ _OBJC_IVAR_$_LACDTOFeatureController._kvStore
+ _OBJC_IVAR_$_LACDTOFeatureController._workQueue
+ _OBJC_IVAR_$_LACDTOFeatureController.eventBus
+ _OBJC_IVAR_$_LACDTOKVStoreValue._data
+ _OBJC_IVAR_$_LACDTOLocationMonitor._locationProvider
+ _OBJC_IVAR_$_LACDTOLocationMonitor._locationState
+ _OBJC_IVAR_$_LACDTOLocationMonitor._locationStateBackgroundTask
+ _OBJC_IVAR_$_LACDTOLocationMonitor._store
+ _OBJC_IVAR_$_LACDTOLocationMonitor._timer
+ _OBJC_IVAR_$_LACDTOLocationMonitor._workQueue
+ _OBJC_IVAR_$_LACDTOLocationMonitor.eventBus
+ _OBJC_IVAR_$_LACDTOLocationProviderCRAdapter._locationState
+ _OBJC_IVAR_$_LACDTOLocationProviderCRAdapter._manager
+ _OBJC_IVAR_$_LACDTOLocationProviderCRAdapter._workQueue
+ _OBJC_IVAR_$_LACDTOLocationProviderKVSAdapter._kvStore
+ _OBJC_IVAR_$_LACDTOLocationState._confirmed
+ _OBJC_IVAR_$_LACDTOLocationState._createdAt
+ _OBJC_IVAR_$_LACDTOLocationState._isInFamiliarLocation
+ _OBJC_IVAR_$_LACDTOLostModeController._lostModeBackgroundTask
+ _OBJC_IVAR_$_LACDTOLostModeController._lostModeProvider
+ _OBJC_IVAR_$_LACDTOLostModeController._store
+ _OBJC_IVAR_$_LACDTOLostModeController._workQueue
+ _OBJC_IVAR_$_LACDTOLostModeProviderAKAdapter._deviceInfo
+ _OBJC_IVAR_$_LACDTOLostModeProviderAKAdapter._lostModeState
+ _OBJC_IVAR_$_LACDTOLostModeProviderAKAdapter._workQueue
+ _OBJC_IVAR_$_LACDTOLostModeProviderKVSAdapter._kvStore
+ _OBJC_IVAR_$_LACDTOLostModeState._confirmed
+ _OBJC_IVAR_$_LACDTOLostModeState._createdAt
+ _OBJC_IVAR_$_LACDTOLostModeState._isInLostMode
+ _OBJC_IVAR_$_LACDTOMutableEnvironment._biometryWatchdogPack
+ _OBJC_IVAR_$_LACDTOMutableEnvironment._featureState
+ _OBJC_IVAR_$_LACDTOMutableEnvironment._inFamiliarLocation
+ _OBJC_IVAR_$_LACDTOMutableEnvironment._ratchetState
+ _OBJC_IVAR_$_LACDTOMutableFeatureState._isAvailable
+ _OBJC_IVAR_$_LACDTOMutableFeatureState._isEnabled
+ _OBJC_IVAR_$_LACDTOMutableFeatureState._isSupported
+ _OBJC_IVAR_$_LACDTOMutableLostModeFetchRequest._biometryWatchdogPack
+ _OBJC_IVAR_$_LACDTOMutableLostModeFetchRequest._isDTOEnabled
+ _OBJC_IVAR_$_LACDTOMutableLostModeFetchRequest._options
+ _OBJC_IVAR_$_LACDTOMutableLostModeFetchRequest._policy
+ _OBJC_IVAR_$_LACDTOMutableLostModeFetchRequest._ratchetState
+ _OBJC_IVAR_$_LACDTOMutablePolicyEvaluationRequest._environment
+ _OBJC_IVAR_$_LACDTOMutablePolicyEvaluationRequest._identifier
+ _OBJC_IVAR_$_LACDTOMutablePolicyEvaluationRequest._options
+ _OBJC_IVAR_$_LACDTOMutablePolicyEvaluationRequest._policy
+ _OBJC_IVAR_$_LACDTOMutablePolicyEvaluationResult._error
+ _OBJC_IVAR_$_LACDTOMutablePolicyEvaluationResult._identifier
+ _OBJC_IVAR_$_LACDTOMutablePolicyEvaluationResult._result
+ _OBJC_IVAR_$_LACDTOPendingPolicyEvaluationController._evaluationIdentifierFactory
+ _OBJC_IVAR_$_LACDTOPendingPolicyEvaluationController._evaluationStore
+ _OBJC_IVAR_$_LACDTOPendingPolicyEvaluationController._notificationManager
+ _OBJC_IVAR_$_LACDTOPendingPolicyEvaluationController._observers
+ _OBJC_IVAR_$_LACDTOPendingPolicyEvaluationController._ratchetHandler
+ _OBJC_IVAR_$_LACDTOPendingPolicyEvaluationController._ratchetStateProvider
+ _OBJC_IVAR_$_LACDTOPendingPolicyEvaluationController._workQueue
+ _OBJC_IVAR_$_LACDTOPolicyEvaluationController._device
+ _OBJC_IVAR_$_LACDTOPolicyEvaluationController._environment
+ _OBJC_IVAR_$_LACDTOPolicyEvaluationController._evaluationIdentifierFactory
+ _OBJC_IVAR_$_LACDTOPolicyEvaluationController._observers
+ _OBJC_IVAR_$_LACDTORatchetNotificationCoolOff.body
+ _OBJC_IVAR_$_LACDTORatchetNotificationCoolOff.defaultActionURL
+ _OBJC_IVAR_$_LACDTORatchetNotificationCoolOff.identifier
+ _OBJC_IVAR_$_LACDTORatchetNotificationCoolOff.isTimeSensitive
+ _OBJC_IVAR_$_LACDTORatchetNotificationCoolOff.maxAge
+ _OBJC_IVAR_$_LACDTORatchetNotificationCoolOff.systemIconName
+ _OBJC_IVAR_$_LACDTORatchetNotificationCoolOff.title
+ _OBJC_IVAR_$_LACDTORatchetState._duration
+ _OBJC_IVAR_$_LACDTORatchetState._rawValue
+ _OBJC_IVAR_$_LACDTORatchetState._resetDuration
+ _OBJC_IVAR_$_LACDTORatchetState._uuid
+ _OBJC_IVAR_$_LACDTORatchetStateMonitor._ratchetState
+ _OBJC_IVAR_$_LACDTORatchetStateMonitor._ratchetStateProvider
+ _OBJC_IVAR_$_LACDTORatchetStateMonitor._timer
+ _OBJC_IVAR_$_LACDTORatchetStateMonitor._workQueue
+ _OBJC_IVAR_$_LACDTORatchetStateMonitor.eventBus
+ _OBJC_IVAR_$_LACDTORatchetStateWithWatchdogs._ratchetState
+ _OBJC_IVAR_$_LACDTORatchetStateWithWatchdogs._watchdogs
+ _OBJC_IVAR_$_LACDTOServiceXPCClient._connection
+ _OBJC_IVAR_$_LACDTOServiceXPCClient._connectionLock
+ _OBJC_IVAR_$_LACDTOServiceXPCClient._endpointProvider
+ _OBJC_IVAR_$_LACDTOServiceXPCHost._featureController
+ _OBJC_IVAR_$_LACDTOServiceXPCHost._pendingEvaluationController
+ _OBJC_IVAR_$_LACDTOServiceXPCHost._ratchetStateProvider
+ _OBJC_IVAR_$_LACDTOSignpostEvent._sendBlock
+ _OBJC_IVAR_$_LACDarwinNotificationCenter._observersLock
+ _OBJC_IVAR_$_LACDarwinNotificationCenter._subscriptionsLock
+ _OBJC_IVAR_$_LACRatchetFlowManager._presenter
+ _OBJC_IVAR_$_LACRatchetFlowManager._uiManager
+ _OBJC_METACLASS_$_LACDTOBiometryWatchdog
+ _OBJC_METACLASS_$_LACDTOBiometryWatchdogPack
+ _OBJC_METACLASS_$_LACDTODarwinNotificationsController
+ _OBJC_METACLASS_$_LACDTOEnvironmentProviderFactory
+ _OBJC_METACLASS_$_LACDTOEvent
+ _OBJC_METACLASS_$_LACDTOEventBus
+ _OBJC_METACLASS_$_LACDTOFeatureController
+ _OBJC_METACLASS_$_LACDTOKVStoreValue
+ _OBJC_METACLASS_$_LACDTOLocationMonitor
+ _OBJC_METACLASS_$_LACDTOLocationProviderCRAdapter
+ _OBJC_METACLASS_$_LACDTOLocationProviderKVSAdapter
+ _OBJC_METACLASS_$_LACDTOLocationState
+ _OBJC_METACLASS_$_LACDTOLostModeController
+ _OBJC_METACLASS_$_LACDTOLostModeProviderAKAdapter
+ _OBJC_METACLASS_$_LACDTOLostModeProviderKVSAdapter
+ _OBJC_METACLASS_$_LACDTOLostModeState
+ _OBJC_METACLASS_$_LACDTOMutableEnvironment
+ _OBJC_METACLASS_$_LACDTOMutableFeatureState
+ _OBJC_METACLASS_$_LACDTOMutableLostModeFetchRequest
+ _OBJC_METACLASS_$_LACDTOMutablePolicyEvaluationRequest
+ _OBJC_METACLASS_$_LACDTOMutablePolicyEvaluationResult
+ _OBJC_METACLASS_$_LACDTONotificationManager
+ _OBJC_METACLASS_$_LACDTOPendingPolicyEvaluationController
+ _OBJC_METACLASS_$_LACDTOPolicyEvaluationController
+ _OBJC_METACLASS_$_LACDTORatchetNotificationCoolOff
+ _OBJC_METACLASS_$_LACDTORatchetState
+ _OBJC_METACLASS_$_LACDTORatchetStateMonitor
+ _OBJC_METACLASS_$_LACDTORatchetStateWithWatchdogs
+ _OBJC_METACLASS_$_LACDTOServiceXPCClient
+ _OBJC_METACLASS_$_LACDTOServiceXPCHost
+ _OBJC_METACLASS_$_LACDTOSignpostEvent
+ _OBJC_METACLASS_$_LACPersistentStoreFactory
+ _OBJC_METACLASS_$_LACRatchetFlowManager
+ _OBJC_METACLASS_$_SwiftNativeNSObject
+ _OBJC_METACLASS_$__TtC23LocalAuthenticationCore25LACDTOEnvironmentProvider
+ _OBJC_METACLASS_$__TtC23LocalAuthenticationCore30LACUserDefaultsPersistentStore
+ _OBJC_METACLASS_$__TtC23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStore
+ _OBJC_METACLASS_$__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __Block_object_dispose
+ __CATEGORY__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation_$_LocalAuthenticationCore
+ __CLASS_PROPERTIES__TtC23LocalAuthenticationCore19LACLocalizedStrings
+ __CLASS_PROPERTIES__TtC23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStore
+ __DATA__TtC23LocalAuthenticationCore25LACDTOEnvironmentProvider
+ __DATA__TtC23LocalAuthenticationCore30LACUserDefaultsPersistentStore
+ __DATA__TtC23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStore
+ __DATA__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation
+ __IVARS__TtC23LocalAuthenticationCore25LACDTOEnvironmentProvider
+ __IVARS__TtC23LocalAuthenticationCore30LACUserDefaultsPersistentStore
+ __IVARS__TtC23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStore
+ __IVARS__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation
+ __METACLASS_DATA__TtC23LocalAuthenticationCore25LACDTOEnvironmentProvider
+ __METACLASS_DATA__TtC23LocalAuthenticationCore30LACUserDefaultsPersistentStore
+ __METACLASS_DATA__TtC23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStore
+ __METACLASS_DATA__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation
+ __OBJC_$_CLASS_METHODS_LACDTOEnvironmentProviderFactory
+ __OBJC_$_CLASS_METHODS_LACDTOLocationState
+ __OBJC_$_CLASS_METHODS_LACDTOLostModeState
+ __OBJC_$_CLASS_METHODS_LACDTORatchetNotificationCoolOff
+ __OBJC_$_CLASS_METHODS_LACDTORatchetState
+ __OBJC_$_CLASS_METHODS_LACDTOSignpostEvent
+ __OBJC_$_CLASS_METHODS_LACPersistentStoreFactory
+ __OBJC_$_CLASS_METHODS__TtC23LocalAuthenticationCore19LACLocalizedStrings
+ __OBJC_$_CLASS_METHODS__TtC23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStore
+ __OBJC_$_CLASS_PROP_LIST_LACDTORatchetState
+ __OBJC_$_CLASS_PROP_LIST_LACDTOSignpostEvent
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_LACDTOBiometryWatchdog
+ __OBJC_$_INSTANCE_METHODS_LACDTOBiometryWatchdogPack
+ __OBJC_$_INSTANCE_METHODS_LACDTODarwinNotificationsController
+ __OBJC_$_INSTANCE_METHODS_LACDTOEvent
+ __OBJC_$_INSTANCE_METHODS_LACDTOEventBus
+ __OBJC_$_INSTANCE_METHODS_LACDTOFeatureController
+ __OBJC_$_INSTANCE_METHODS_LACDTOKVStoreValue
+ __OBJC_$_INSTANCE_METHODS_LACDTOLocationMonitor
+ __OBJC_$_INSTANCE_METHODS_LACDTOLocationProviderCRAdapter
+ __OBJC_$_INSTANCE_METHODS_LACDTOLocationProviderKVSAdapter
+ __OBJC_$_INSTANCE_METHODS_LACDTOLocationState
+ __OBJC_$_INSTANCE_METHODS_LACDTOLostModeController
+ __OBJC_$_INSTANCE_METHODS_LACDTOLostModeProviderAKAdapter
+ __OBJC_$_INSTANCE_METHODS_LACDTOLostModeProviderKVSAdapter
+ __OBJC_$_INSTANCE_METHODS_LACDTOLostModeState
+ __OBJC_$_INSTANCE_METHODS_LACDTOMutableEnvironment
+ __OBJC_$_INSTANCE_METHODS_LACDTOMutableFeatureState
+ __OBJC_$_INSTANCE_METHODS_LACDTOMutableLostModeFetchRequest
+ __OBJC_$_INSTANCE_METHODS_LACDTOMutablePolicyEvaluationRequest
+ __OBJC_$_INSTANCE_METHODS_LACDTOMutablePolicyEvaluationResult
+ __OBJC_$_INSTANCE_METHODS_LACDTONotificationManager
+ __OBJC_$_INSTANCE_METHODS_LACDTOPendingPolicyEvaluationController
+ __OBJC_$_INSTANCE_METHODS_LACDTOPolicyEvaluationController
+ __OBJC_$_INSTANCE_METHODS_LACDTORatchetNotificationCoolOff
+ __OBJC_$_INSTANCE_METHODS_LACDTORatchetState
+ __OBJC_$_INSTANCE_METHODS_LACDTORatchetStateMonitor
+ __OBJC_$_INSTANCE_METHODS_LACDTORatchetStateWithWatchdogs
+ __OBJC_$_INSTANCE_METHODS_LACDTOServiceXPCClient
+ __OBJC_$_INSTANCE_METHODS_LACDTOServiceXPCHost
+ __OBJC_$_INSTANCE_METHODS_LACDTOSignpostEvent
+ __OBJC_$_INSTANCE_METHODS_LACRatchetFlowManager(Base)
+ __OBJC_$_INSTANCE_METHODS__TtC23LocalAuthenticationCore25LACDTOEnvironmentProvider
+ __OBJC_$_INSTANCE_METHODS__TtC23LocalAuthenticationCore30LACUserDefaultsPersistentStore
+ __OBJC_$_INSTANCE_METHODS__TtC23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStore
+ __OBJC_$_INSTANCE_METHODS__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation
+ __OBJC_$_INSTANCE_METHODS__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation(LocalAuthenticationCore)
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOBiometryWatchdog
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOBiometryWatchdogPack
+ __OBJC_$_INSTANCE_VARIABLES_LACDTODarwinNotificationsController
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOEvent
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOEventBus
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOFeatureController
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOKVStoreValue
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOLocationMonitor
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOLocationProviderCRAdapter
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOLocationProviderKVSAdapter
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOLocationState
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOLostModeController
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOLostModeProviderAKAdapter
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOLostModeProviderKVSAdapter
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOLostModeState
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOMutableEnvironment
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOMutableFeatureState
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOMutableLostModeFetchRequest
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOMutablePolicyEvaluationRequest
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOMutablePolicyEvaluationResult
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOPendingPolicyEvaluationController
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOPolicyEvaluationController
+ __OBJC_$_INSTANCE_VARIABLES_LACDTORatchetNotificationCoolOff
+ __OBJC_$_INSTANCE_VARIABLES_LACDTORatchetState
+ __OBJC_$_INSTANCE_VARIABLES_LACDTORatchetStateMonitor
+ __OBJC_$_INSTANCE_VARIABLES_LACDTORatchetStateWithWatchdogs
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOServiceXPCClient
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOServiceXPCHost
+ __OBJC_$_INSTANCE_VARIABLES_LACDTOSignpostEvent
+ __OBJC_$_INSTANCE_VARIABLES_LACRatchetFlowManager
+ __OBJC_$_PROP_LIST_LACDTOBiometryWatchdog
+ __OBJC_$_PROP_LIST_LACDTOBiometryWatchdogPack
+ __OBJC_$_PROP_LIST_LACDTODarwinNotificationsController
+ __OBJC_$_PROP_LIST_LACDTOEnvironment
+ __OBJC_$_PROP_LIST_LACDTOEvent
+ __OBJC_$_PROP_LIST_LACDTOEventBus
+ __OBJC_$_PROP_LIST_LACDTOEventProducer
+ __OBJC_$_PROP_LIST_LACDTOFeatureController
+ __OBJC_$_PROP_LIST_LACDTOFeatureState
+ __OBJC_$_PROP_LIST_LACDTOLocationMonitor
+ __OBJC_$_PROP_LIST_LACDTOLocationProviderCRAdapter
+ __OBJC_$_PROP_LIST_LACDTOLocationProviderKVSAdapter
+ __OBJC_$_PROP_LIST_LACDTOLocationState
+ __OBJC_$_PROP_LIST_LACDTOLostModeController
+ __OBJC_$_PROP_LIST_LACDTOLostModeFetchRequest
+ __OBJC_$_PROP_LIST_LACDTOLostModeProviderAKAdapter
+ __OBJC_$_PROP_LIST_LACDTOLostModeProviderKVSAdapter
+ __OBJC_$_PROP_LIST_LACDTOLostModeState
+ __OBJC_$_PROP_LIST_LACDTOMutableEnvironment
+ __OBJC_$_PROP_LIST_LACDTOMutableFeatureState
+ __OBJC_$_PROP_LIST_LACDTOMutableLostModeFetchRequest
+ __OBJC_$_PROP_LIST_LACDTOMutablePolicyEvaluationRequest
+ __OBJC_$_PROP_LIST_LACDTOMutablePolicyEvaluationResult
+ __OBJC_$_PROP_LIST_LACDTOPendingPolicyEvaluation
+ __OBJC_$_PROP_LIST_LACDTOPendingPolicyEvaluationController
+ __OBJC_$_PROP_LIST_LACDTOPolicyEvaluation
+ __OBJC_$_PROP_LIST_LACDTOPolicyEvaluationController
+ __OBJC_$_PROP_LIST_LACDTOPolicyEvaluationRequest
+ __OBJC_$_PROP_LIST_LACDTOPolicyEvaluationResult
+ __OBJC_$_PROP_LIST_LACDTORatchetNotificationCoolOff
+ __OBJC_$_PROP_LIST_LACDTORatchetState
+ __OBJC_$_PROP_LIST_LACDTORatchetStateMonitor
+ __OBJC_$_PROP_LIST_LACDTORatchetStateWithWatchdogs
+ __OBJC_$_PROP_LIST_LACDTOServiceXPCClient
+ __OBJC_$_PROP_LIST_LACDTOServiceXPCHost
+ __OBJC_$_PROP_LIST_LACRatchetFlowManager
+ __OBJC_$_PROP_LIST_LACUNNotificationConfiguration
+ __OBJC_$_PROTOCOL_CLASS_METHODS_LACUNNotificationConfiguration
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACAuthFlowManaging
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOEnvironment
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOEnvironmentProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOEventBus
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOEventHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOEventProducer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOFeatureControlling
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOFeatureState
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOLocationProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOLostModeFetchRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOLostModeFetchService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOLostModeProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOPendingPolicyEvaluation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOPendingPolicyEvaluationController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOPendingPolicyEvaluationControllerObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOPolicyEvaluation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOPolicyEvaluationController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOPolicyEvaluationControllerObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOPolicyEvaluationRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOPolicyEvaluationResult
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTORatchetStateProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOServiceXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDTOServiceXPCClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACPersistentStore
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACRatchetFlowManaging
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACUNNotificationConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACAuthFlowManaging
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOEnvironment
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOEnvironmentProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOEventBus
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOEventHandler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOEventProducer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOFeatureControlling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOFeatureState
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOLocationProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOLostModeFetchRequest
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOLostModeFetchService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOLostModeProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOPendingPolicyEvaluation
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOPendingPolicyEvaluationController
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOPendingPolicyEvaluationControllerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOPolicyEvaluation
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOPolicyEvaluationController
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOPolicyEvaluationControllerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOPolicyEvaluationRequest
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOPolicyEvaluationResult
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTORatchetStateProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOServiceXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDTOServiceXPCClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACPersistentStore
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACRatchetFlowManaging
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACUNNotificationConfiguration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_LACAuthFlowManaging
+ __OBJC_$_PROTOCOL_REFS_LACDTOEnvironment
+ __OBJC_$_PROTOCOL_REFS_LACDTOEnvironmentProviding
+ __OBJC_$_PROTOCOL_REFS_LACDTOEventBus
+ __OBJC_$_PROTOCOL_REFS_LACDTOEventHandler
+ __OBJC_$_PROTOCOL_REFS_LACDTOEventProducer
+ __OBJC_$_PROTOCOL_REFS_LACDTOFeatureControlling
+ __OBJC_$_PROTOCOL_REFS_LACDTOFeatureState
+ __OBJC_$_PROTOCOL_REFS_LACDTOLocationProvider
+ __OBJC_$_PROTOCOL_REFS_LACDTOLostModeFetchRequest
+ __OBJC_$_PROTOCOL_REFS_LACDTOLostModeFetchService
+ __OBJC_$_PROTOCOL_REFS_LACDTOLostModeProvider
+ __OBJC_$_PROTOCOL_REFS_LACDTOPendingPolicyEvaluation
+ __OBJC_$_PROTOCOL_REFS_LACDTOPendingPolicyEvaluationController
+ __OBJC_$_PROTOCOL_REFS_LACDTOPendingPolicyEvaluationControllerObserver
+ __OBJC_$_PROTOCOL_REFS_LACDTOPolicyEvaluation
+ __OBJC_$_PROTOCOL_REFS_LACDTOPolicyEvaluationController
+ __OBJC_$_PROTOCOL_REFS_LACDTOPolicyEvaluationControllerObserver
+ __OBJC_$_PROTOCOL_REFS_LACDTOPolicyEvaluationRequest
+ __OBJC_$_PROTOCOL_REFS_LACDTOPolicyEvaluationResult
+ __OBJC_$_PROTOCOL_REFS_LACDTORatchetStateProvider
+ __OBJC_$_PROTOCOL_REFS_LACDTOServiceXPC
+ __OBJC_$_PROTOCOL_REFS_LACDTOServiceXPCClient
+ __OBJC_$_PROTOCOL_REFS_LACPersistentStore
+ __OBJC_$_PROTOCOL_REFS_LACRatchetFlowManaging
+ __OBJC_$_PROTOCOL_REFS_LACUNNotificationConfiguration
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_LACDTODarwinNotificationsController
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOEventBus
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOFeatureController
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOLocationMonitor
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOLocationProviderCRAdapter
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOLocationProviderKVSAdapter
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOLostModeController
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOLostModeProviderAKAdapter
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOLostModeProviderKVSAdapter
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOMutableEnvironment
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOMutableFeatureState
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOMutableLostModeFetchRequest
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOMutablePolicyEvaluationRequest
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOMutablePolicyEvaluationResult
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOPendingPolicyEvaluationController
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOPolicyEvaluationController
+ __OBJC_CLASS_PROTOCOLS_$_LACDTORatchetNotificationCoolOff
+ __OBJC_CLASS_PROTOCOLS_$_LACDTORatchetState
+ __OBJC_CLASS_PROTOCOLS_$_LACDTORatchetStateMonitor
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOServiceXPCClient
+ __OBJC_CLASS_PROTOCOLS_$_LACDTOServiceXPCHost
+ __OBJC_CLASS_PROTOCOLS_$_LACRatchetFlowManager(Base)
+ __OBJC_CLASS_RO_$_LACDTOBiometryWatchdog
+ __OBJC_CLASS_RO_$_LACDTOBiometryWatchdogPack
+ __OBJC_CLASS_RO_$_LACDTODarwinNotificationsController
+ __OBJC_CLASS_RO_$_LACDTOEnvironmentProviderFactory
+ __OBJC_CLASS_RO_$_LACDTOEvent
+ __OBJC_CLASS_RO_$_LACDTOEventBus
+ __OBJC_CLASS_RO_$_LACDTOFeatureController
+ __OBJC_CLASS_RO_$_LACDTOKVStoreValue
+ __OBJC_CLASS_RO_$_LACDTOLocationMonitor
+ __OBJC_CLASS_RO_$_LACDTOLocationProviderCRAdapter
+ __OBJC_CLASS_RO_$_LACDTOLocationProviderKVSAdapter
+ __OBJC_CLASS_RO_$_LACDTOLocationState
+ __OBJC_CLASS_RO_$_LACDTOLostModeController
+ __OBJC_CLASS_RO_$_LACDTOLostModeProviderAKAdapter
+ __OBJC_CLASS_RO_$_LACDTOLostModeProviderKVSAdapter
+ __OBJC_CLASS_RO_$_LACDTOLostModeState
+ __OBJC_CLASS_RO_$_LACDTOMutableEnvironment
+ __OBJC_CLASS_RO_$_LACDTOMutableFeatureState
+ __OBJC_CLASS_RO_$_LACDTOMutableLostModeFetchRequest
+ __OBJC_CLASS_RO_$_LACDTOMutablePolicyEvaluationRequest
+ __OBJC_CLASS_RO_$_LACDTOMutablePolicyEvaluationResult
+ __OBJC_CLASS_RO_$_LACDTONotificationManager
+ __OBJC_CLASS_RO_$_LACDTOPendingPolicyEvaluationController
+ __OBJC_CLASS_RO_$_LACDTOPolicyEvaluationController
+ __OBJC_CLASS_RO_$_LACDTORatchetNotificationCoolOff
+ __OBJC_CLASS_RO_$_LACDTORatchetState
+ __OBJC_CLASS_RO_$_LACDTORatchetStateMonitor
+ __OBJC_CLASS_RO_$_LACDTORatchetStateWithWatchdogs
+ __OBJC_CLASS_RO_$_LACDTOServiceXPCClient
+ __OBJC_CLASS_RO_$_LACDTOServiceXPCHost
+ __OBJC_CLASS_RO_$_LACDTOSignpostEvent
+ __OBJC_CLASS_RO_$_LACPersistentStoreFactory
+ __OBJC_CLASS_RO_$_LACRatchetFlowManager
+ __OBJC_LABEL_PROTOCOL_$_LACAuthFlowManaging
+ __OBJC_LABEL_PROTOCOL_$_LACDTOEnvironment
+ __OBJC_LABEL_PROTOCOL_$_LACDTOEnvironmentProviding
+ __OBJC_LABEL_PROTOCOL_$_LACDTOEventBus
+ __OBJC_LABEL_PROTOCOL_$_LACDTOEventHandler
+ __OBJC_LABEL_PROTOCOL_$_LACDTOEventProducer
+ __OBJC_LABEL_PROTOCOL_$_LACDTOFeatureControlling
+ __OBJC_LABEL_PROTOCOL_$_LACDTOFeatureState
+ __OBJC_LABEL_PROTOCOL_$_LACDTOLocationProvider
+ __OBJC_LABEL_PROTOCOL_$_LACDTOLostModeFetchRequest
+ __OBJC_LABEL_PROTOCOL_$_LACDTOLostModeFetchService
+ __OBJC_LABEL_PROTOCOL_$_LACDTOLostModeProvider
+ __OBJC_LABEL_PROTOCOL_$_LACDTOPendingPolicyEvaluation
+ __OBJC_LABEL_PROTOCOL_$_LACDTOPendingPolicyEvaluationController
+ __OBJC_LABEL_PROTOCOL_$_LACDTOPendingPolicyEvaluationControllerObserver
+ __OBJC_LABEL_PROTOCOL_$_LACDTOPolicyEvaluation
+ __OBJC_LABEL_PROTOCOL_$_LACDTOPolicyEvaluationController
+ __OBJC_LABEL_PROTOCOL_$_LACDTOPolicyEvaluationControllerObserver
+ __OBJC_LABEL_PROTOCOL_$_LACDTOPolicyEvaluationRequest
+ __OBJC_LABEL_PROTOCOL_$_LACDTOPolicyEvaluationResult
+ __OBJC_LABEL_PROTOCOL_$_LACDTORatchetStateProvider
+ __OBJC_LABEL_PROTOCOL_$_LACDTOServiceXPC
+ __OBJC_LABEL_PROTOCOL_$_LACDTOServiceXPCClient
+ __OBJC_LABEL_PROTOCOL_$_LACPersistentStore
+ __OBJC_LABEL_PROTOCOL_$_LACRatchetFlowManaging
+ __OBJC_LABEL_PROTOCOL_$_LACUNNotificationConfiguration
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_LACDTOBiometryWatchdog
+ __OBJC_METACLASS_RO_$_LACDTOBiometryWatchdogPack
+ __OBJC_METACLASS_RO_$_LACDTODarwinNotificationsController
+ __OBJC_METACLASS_RO_$_LACDTOEnvironmentProviderFactory
+ __OBJC_METACLASS_RO_$_LACDTOEvent
+ __OBJC_METACLASS_RO_$_LACDTOEventBus
+ __OBJC_METACLASS_RO_$_LACDTOFeatureController
+ __OBJC_METACLASS_RO_$_LACDTOKVStoreValue
+ __OBJC_METACLASS_RO_$_LACDTOLocationMonitor
+ __OBJC_METACLASS_RO_$_LACDTOLocationProviderCRAdapter
+ __OBJC_METACLASS_RO_$_LACDTOLocationProviderKVSAdapter
+ __OBJC_METACLASS_RO_$_LACDTOLocationState
+ __OBJC_METACLASS_RO_$_LACDTOLostModeController
+ __OBJC_METACLASS_RO_$_LACDTOLostModeProviderAKAdapter
+ __OBJC_METACLASS_RO_$_LACDTOLostModeProviderKVSAdapter
+ __OBJC_METACLASS_RO_$_LACDTOLostModeState
+ __OBJC_METACLASS_RO_$_LACDTOMutableEnvironment
+ __OBJC_METACLASS_RO_$_LACDTOMutableFeatureState
+ __OBJC_METACLASS_RO_$_LACDTOMutableLostModeFetchRequest
+ __OBJC_METACLASS_RO_$_LACDTOMutablePolicyEvaluationRequest
+ __OBJC_METACLASS_RO_$_LACDTOMutablePolicyEvaluationResult
+ __OBJC_METACLASS_RO_$_LACDTONotificationManager
+ __OBJC_METACLASS_RO_$_LACDTOPendingPolicyEvaluationController
+ __OBJC_METACLASS_RO_$_LACDTOPolicyEvaluationController
+ __OBJC_METACLASS_RO_$_LACDTORatchetNotificationCoolOff
+ __OBJC_METACLASS_RO_$_LACDTORatchetState
+ __OBJC_METACLASS_RO_$_LACDTORatchetStateMonitor
+ __OBJC_METACLASS_RO_$_LACDTORatchetStateWithWatchdogs
+ __OBJC_METACLASS_RO_$_LACDTOServiceXPCClient
+ __OBJC_METACLASS_RO_$_LACDTOServiceXPCHost
+ __OBJC_METACLASS_RO_$_LACDTOSignpostEvent
+ __OBJC_METACLASS_RO_$_LACPersistentStoreFactory
+ __OBJC_METACLASS_RO_$_LACRatchetFlowManager
+ __OBJC_PROTOCOL_$_LACAuthFlowManaging
+ __OBJC_PROTOCOL_$_LACDTOEnvironment
+ __OBJC_PROTOCOL_$_LACDTOEnvironmentProviding
+ __OBJC_PROTOCOL_$_LACDTOEventBus
+ __OBJC_PROTOCOL_$_LACDTOEventHandler
+ __OBJC_PROTOCOL_$_LACDTOEventProducer
+ __OBJC_PROTOCOL_$_LACDTOFeatureControlling
+ __OBJC_PROTOCOL_$_LACDTOFeatureState
+ __OBJC_PROTOCOL_$_LACDTOLocationProvider
+ __OBJC_PROTOCOL_$_LACDTOLostModeFetchRequest
+ __OBJC_PROTOCOL_$_LACDTOLostModeFetchService
+ __OBJC_PROTOCOL_$_LACDTOLostModeProvider
+ __OBJC_PROTOCOL_$_LACDTOPendingPolicyEvaluation
+ __OBJC_PROTOCOL_$_LACDTOPendingPolicyEvaluationController
+ __OBJC_PROTOCOL_$_LACDTOPendingPolicyEvaluationControllerObserver
+ __OBJC_PROTOCOL_$_LACDTOPolicyEvaluation
+ __OBJC_PROTOCOL_$_LACDTOPolicyEvaluationController
+ __OBJC_PROTOCOL_$_LACDTOPolicyEvaluationControllerObserver
+ __OBJC_PROTOCOL_$_LACDTOPolicyEvaluationRequest
+ __OBJC_PROTOCOL_$_LACDTOPolicyEvaluationResult
+ __OBJC_PROTOCOL_$_LACDTORatchetStateProvider
+ __OBJC_PROTOCOL_$_LACDTOServiceXPC
+ __OBJC_PROTOCOL_$_LACDTOServiceXPCClient
+ __OBJC_PROTOCOL_$_LACPersistentStore
+ __OBJC_PROTOCOL_$_LACRatchetFlowManaging
+ __OBJC_PROTOCOL_$_LACUNNotificationConfiguration
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_REFERENCE_$_LACDTOEnvironment
+ __OBJC_PROTOCOL_REFERENCE_$_LACDTOLostModeFetchRequest
+ __OBJC_PROTOCOL_REFERENCE_$_LACDTOPolicyEvaluationRequest
+ __OBJC_PROTOCOL_REFERENCE_$_LACDTOPolicyEvaluationResult
+ __OBJC_PROTOCOL_REFERENCE_$_LACDTOServiceXPC
+ __PROPERTIES__TtC23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStore
+ __PROPERTIES__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation
+ __PROTOCOLS__TtC23LocalAuthenticationCore25LACDTOEnvironmentProvider
+ __PROTOCOLS__TtC23LocalAuthenticationCore25LACDTOEnvironmentProvider.8
+ __PROTOCOLS__TtC23LocalAuthenticationCore30LACUserDefaultsPersistentStore
+ __PROTOCOLS__TtC23LocalAuthenticationCore30LACUserDefaultsPersistentStore.1
+ __PROTOCOLS__TtC23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStore
+ __PROTOCOLS__TtC23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStore.21
+ __PROTOCOLS__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation
+ __PROTOCOLS__TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation.12
+ __PROTOCOL_INSTANCE_METHODS__TtP23LocalAuthenticationCore38LACDTOPendingPolicyEvaluationStoreType_
+ __PROTOCOL_METHOD_TYPES__TtP23LocalAuthenticationCore38LACDTOPendingPolicyEvaluationStoreType_
+ __PROTOCOL_PROPERTIES__TtP23LocalAuthenticationCore38LACDTOPendingPolicyEvaluationStoreType_
+ __PROTOCOL_PROTOCOLS__TtP23LocalAuthenticationCore38LACDTOPendingPolicyEvaluationStoreType_
+ __PROTOCOL__TtP23LocalAuthenticationCore38LACDTOPendingPolicyEvaluationStoreType_
+ ___101-[LACDTOPolicyEvaluationController _evaluatePolicy:options:client:environment:evaluationBlock:reply:]_block_invoke
+ ___101-[LACDTOPolicyEvaluationController _evaluatePolicy:options:client:environment:evaluationBlock:reply:]_block_invoke_2
+ ___101-[LACDTOPolicyEvaluationController _evaluatePolicy:options:client:environment:evaluationBlock:reply:]_block_invoke_3
+ ___103-[LACDTOPendingPolicyEvaluationController _checkShouldAddPendingEvaluationRecordForRequest:completion:]_block_invoke
+ ___103-[LACDTOPendingPolicyEvaluationController _checkShouldKeepPendingEvaluationRecordForResult:completion:]_block_invoke
+ ___104-[LACDTOPendingPolicyEvaluationController _scheduleNotificationForPendingEvaluationRecord:after:maxAge:]_block_invoke
+ ___104-[LACDTOPendingPolicyEvaluationController _scheduleNotificationForPendingEvaluationRecord:after:maxAge:]_block_invoke.cold.1
+ ___108-[LACDTONotificationManager cancelPreviousSecurityDelayFinishedNotificationForPendingEvaluation:completion:]_block_invoke
+ ___115-[LACDTONotificationManager scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:maxAge:completion:]_block_invoke
+ ___115-[LACDTONotificationManager scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:maxAge:completion:]_block_invoke.1
+ ___115-[LACDTONotificationManager scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:maxAge:completion:]_block_invoke.1.cold.1
+ ___38-[LACDTOServiceXPCClient ratchetState]_block_invoke
+ ___38-[LACDTOServiceXPCClient ratchetState]_block_invoke.3
+ ___38-[LACDTOServiceXPCClient ratchetState]_block_invoke.3.cold.1
+ ___38-[LACDTOServiceXPCClient ratchetState]_block_invoke.cold.1
+ ___42-[LACDTOServiceXPCClient isFeatureEnabled]_block_invoke
+ ___42-[LACDTOServiceXPCClient isFeatureEnabled]_block_invoke.5
+ ___42-[LACDTOServiceXPCClient isFeatureEnabled]_block_invoke.5.cold.1
+ ___42-[LACDTOServiceXPCClient isFeatureEnabled]_block_invoke.cold.1
+ ___43-[LACDarwinNotificationCenter addObserver:]_block_invoke
+ ___43-[LACDarwinNotificationCenter hasObserver:]_block_invoke
+ ___44-[LACDTOServiceXPCClient isFeatureAvailable]_block_invoke
+ ___44-[LACDTOServiceXPCClient isFeatureAvailable]_block_invoke.8
+ ___44-[LACDTOServiceXPCClient isFeatureAvailable]_block_invoke.8.cold.1
+ ___44-[LACDTOServiceXPCClient isFeatureAvailable]_block_invoke.cold.1
+ ___44-[LACDTOServiceXPCClient isFeatureSupported]_block_invoke
+ ___44-[LACDTOServiceXPCClient isFeatureSupported]_block_invoke.7
+ ___44-[LACDTOServiceXPCClient isFeatureSupported]_block_invoke.7.cold.1
+ ___44-[LACDTOServiceXPCClient isFeatureSupported]_block_invoke.cold.1
+ ___44-[LACDarwinNotificationCenter observerCount]_block_invoke
+ ___45+[LACDTOSignpostEvent lostModeQueryDidFinish]_block_invoke
+ ___45+[LACDTOSignpostEvent lostModeQueryDidFinish]_block_invoke_2
+ ___45+[LACDTOSignpostEvent lostModeQueryWillStart]_block_invoke
+ ___45+[LACDTOSignpostEvent lostModeQueryWillStart]_block_invoke_2
+ ___46-[LACDarwinNotificationCenter removeObserver:]_block_invoke
+ ___48-[LACDTORatchetStateMonitor handleEvent:sender:]_block_invoke
+ ___49+[LACDTOSignpostEvent environmentUpdateDidFinish]_block_invoke
+ ___49+[LACDTOSignpostEvent environmentUpdateDidFinish]_block_invoke_2
+ ___49+[LACDTOSignpostEvent environmentUpdateWillStart]_block_invoke
+ ___49+[LACDTOSignpostEvent environmentUpdateWillStart]_block_invoke_2
+ ___49-[LACDarwinNotificationCenter removeAllObservers]_block_invoke
+ ___50-[LACDTOLostModeController lostModeBackgroundTask]_block_invoke
+ ___50-[LACDTOLostModeController lostModeBackgroundTask]_block_invoke_2
+ ___51+[LACDTOSignpostEvent locationStatusQueryDidFinish]_block_invoke
+ ___51+[LACDTOSignpostEvent locationStatusQueryDidFinish]_block_invoke_2
+ ___51+[LACDTOSignpostEvent locationStatusQueryWillStart]_block_invoke
+ ___51+[LACDTOSignpostEvent locationStatusQueryWillStart]_block_invoke_2
+ ___52-[LACDTOFeatureController fetchStateWithCompletion:]_block_invoke
+ ___52-[LACDTOFeatureController fetchStateWithCompletion:]_block_invoke_2
+ ___52-[LACDTOFeatureController fetchStateWithCompletion:]_block_invoke_3
+ ___52-[LACDTOFeatureController fetchStateWithCompletion:]_block_invoke_4
+ ___52-[LACDTOLocationMonitor _startMonitoringWithReason:]_block_invoke
+ ___52-[LACDTOLocationMonitor _startMonitoringWithReason:]_block_invoke.15
+ ___52-[LACDTOLocationMonitor locationStateBackgroundTask]_block_invoke
+ ___52-[LACDTOLocationMonitor locationStateBackgroundTask]_block_invoke_2
+ ___53-[LACDTOLostModeController fetchLostMode:completion:]_block_invoke
+ ___53-[LACDTOLostModeController fetchLostMode:completion:]_block_invoke.1
+ ___53-[LACDTORatchetStateMonitor _scheduleNextStatusCheck]_block_invoke
+ ___53-[LACDTORatchetStateMonitor _scheduleNextStatusCheck]_block_invoke.5
+ ___53-[LACDTOServiceXPCClient ratchetStateWithCompletion:]_block_invoke
+ ___54-[LACDTOServiceXPCClient _connectionWithErrorHandler:]_block_invoke
+ ___54-[LACDTOServiceXPCClient enableFeatureWithCompletion:]_block_invoke
+ ___55-[LACDTOFeatureController enableFeatureWithCompletion:]_block_invoke
+ ___55-[LACDTOFeatureController enableFeatureWithCompletion:]_block_invoke.21
+ ___55-[LACDTOFeatureController enableFeatureWithCompletion:]_block_invoke.21.cold.1
+ ___55-[LACDTOFeatureController enableFeatureWithCompletion:]_block_invoke.22
+ ___55-[LACDTOFeatureController enableFeatureWithCompletion:]_block_invoke.cold.1
+ ___55-[LACDTOPendingPolicyEvaluationController addObserver:]_block_invoke
+ ___55-[LACDTOPendingPolicyEvaluationController addObserver:]_block_invoke_2
+ ___56-[LACDTORatchetStateMonitor ratchetStateWithCompletion:]_block_invoke
+ ___56-[LACDarwinNotificationCenter addObserver:notification:]_block_invoke
+ ___62-[LACDTOServiceXPCClient checkCanEnableFeatureWithCompletion:]_block_invoke
+ ___62-[LACDTOServiceXPCClient checkIsFeatureEnabledWithCompletion:]_block_invoke
+ ___62-[LACDarwinNotificationCenter _addSubscriptionToNotification:]_block_invoke
+ ___62-[LACDarwinNotificationCenter _hasSubscriptionToNotification:]_block_invoke
+ ___62-[LACDarwinNotificationCenter stopListeningToAllNotifications]_block_invoke
+ ___63-[LACDTOFeatureController checkCanEnableFeatureWithCompletion:]_block_invoke
+ ___63-[LACDTOFeatureController checkCanEnableFeatureWithCompletion:]_block_invoke.19
+ ___63-[LACDTOFeatureController checkCanEnableFeatureWithCompletion:]_block_invoke.cold.1
+ ___63-[LACDTOFeatureController checkIsFeatureEnabledWithCompletion:]_block_invoke
+ ___63-[LACDTOFeatureController checkIsFeatureEnabledWithCompletion:]_block_invoke.cold.1
+ ___63-[LACDTOLostModeProviderAKAdapter lostModeStateWithCompletion:]_block_invoke
+ ___63-[LACDTOLostModeProviderAKAdapter lostModeStateWithCompletion:]_block_invoke_2
+ ___63-[LACDTOLostModeProviderAKAdapter lostModeStateWithCompletion:]_block_invoke_2.cold.1
+ ___64-[LACDTOLostModeProviderAKAdapter _lostModeStateWithCompletion:]_block_invoke
+ ___64-[LACDTOLostModeProviderAKAdapter _lostModeStateWithCompletion:]_block_invoke_2
+ ___64-[LACDTOLostModeProviderKVSAdapter lostModeStateWithCompletion:]_block_invoke
+ ___64-[LACDTOLostModeProviderKVSAdapter lostModeStateWithCompletion:]_block_invoke.cold.1
+ ___64-[LACDTOServiceXPCClient checkIsFeatureAvailableWithCompletion:]_block_invoke
+ ___64-[LACDTOServiceXPCClient checkIsFeatureSupportedWithCompletion:]_block_invoke
+ ___65-[LACDTOFeatureController checkIsFeatureAvailableWithCompletion:]_block_invoke
+ ___65-[LACDTOLocationMonitor checkIsInFamiliarLocationWithCompletion:]_block_invoke
+ ___65-[LACDTOLocationMonitor checkIsInFamiliarLocationWithCompletion:]_block_invoke.2
+ ___65-[LACDTOLocationMonitor checkIsInFamiliarLocationWithCompletion:]_block_invoke.2.cold.1
+ ___65-[LACDTORatchetStateMonitor ratchetStateWithWatchdogsCompletion:]_block_invoke
+ ___65-[LACDarwinNotificationCenter _notifyObserversAboutNotification:]_block_invoke
+ ___66-[LACDTOPendingPolicyEvaluationController _loadPendingEvaluations]_block_invoke
+ ___66-[LACDTOPendingPolicyEvaluationController _loadPendingEvaluations]_block_invoke.43
+ ___66-[LACDTOPendingPolicyEvaluationController _loadPendingEvaluations]_block_invoke.43.cold.1
+ ___66-[LACDTOPendingPolicyEvaluationController _loadPendingEvaluations]_block_invoke.cold.1
+ ___68-[LACDTOLocationMonitor _runLocationStateBackgroundTask:completion:]_block_invoke
+ ___68-[LACDTOPolicyEvaluationController _notifyObserversAboutEvaluation:]_block_invoke
+ ___69-[LACDTOPendingPolicyEvaluationController _handleSwitchToFinalState:]_block_invoke
+ ___71-[LACDTOPendingPolicyEvaluationController _handleSwitchToCoolOffState:]_block_invoke
+ ___71-[LACDTOPendingPolicyEvaluationController _resetRatchetWithCompletion:]_block_invoke
+ ___71-[LACDTOPendingPolicyEvaluationController _resetRatchetWithCompletion:]_block_invoke_2
+ ___73-[LACDTOFeatureController _fetchDeviceHintsCurrentConnection:completion:]_block_invoke
+ ___73-[LACDTOFeatureController _fetchDeviceHintsCurrentConnection:completion:]_block_invoke.cold.1
+ ___75-[LACDTOLocationProviderCRAdapter checkIsInFamiliarLocationWithCompletion:]_block_invoke
+ ___75-[LACDTOLocationProviderCRAdapter checkIsInFamiliarLocationWithCompletion:]_block_invoke_2
+ ___75-[LACDTOLocationProviderCRAdapter checkIsInFamiliarLocationWithCompletion:]_block_invoke_2.cold.1
+ ___75-[LACDTOPolicyEvaluationController _notifyObserversAboutEvaluation:result:]_block_invoke
+ ___76-[LACDTOFeatureController _setFeatureEnabled:context:connection:completion:]_block_invoke
+ ___76-[LACDTOFeatureController _setFeatureEnabled:context:connection:completion:]_block_invoke_2
+ ___76-[LACDTOLocationProviderKVSAdapter checkIsInFamiliarLocationWithCompletion:]_block_invoke
+ ___76-[LACDTOLocationProviderKVSAdapter checkIsInFamiliarLocationWithCompletion:]_block_invoke.cold.1
+ ___76-[LACDTOPendingPolicyEvaluationController _prunePendingEvaluationsWithUUID:]_block_invoke
+ ___77-[LACDTOLostModeController _runLostModeBackgroundTaskWithTimeout:completion:]_block_invoke
+ ___77-[LACDTOPendingPolicyEvaluationController _checkIsRatchetStateIn:completion:]_block_invoke
+ ___78-[LACDTOPendingPolicyEvaluationController _updatePendingEvaluationsWithBlock:]_block_invoke
+ ___79-[LACDTORatchetStateMonitor policyController:didFinishPolicyEvaluation:result:]_block_invoke
+ ___84-[LACDTOPendingPolicyEvaluationController _addPendingEvaluationRecord:currentState:]_block_invoke
+ ___86-[LACDTOPendingPolicyEvaluationController policyController:willStartPolicyEvaluation:]_block_invoke
+ ___87-[LACDTOPendingPolicyEvaluationController _canFinishPendingEvaluationsForRatchetState:]_block_invoke
+ ___88-[LACDTOPolicyEvaluationController _noAuthenticationOnFallbackEvaluationBlockWithBlock:]_block_invoke
+ ___88-[LACDTOPolicyEvaluationController _noAuthenticationOnFallbackEvaluationBlockWithBlock:]_block_invoke_2
+ ___88-[LACDTOPolicyEvaluationController evaluatePolicy:options:client:evaluationBlock:reply:]_block_invoke
+ ___89-[LACDTOServiceXPCClient cancelPendingEvaluationWithRatchetIdentifier:reason:completion:]_block_invoke
+ ___93-[LACDTOPendingPolicyEvaluationController policyController:didFinishPolicyEvaluation:result:]_block_invoke
+ ___94-[LACDTOPendingPolicyEvaluationController _addPendingEvaluationRecordForRequest:currentState:]_block_invoke
+ ___94-[LACDTOPendingPolicyEvaluationController _addPendingEvaluationRecordForRequest:currentState:]_block_invoke_2
+ ___97-[LACDTOPendingPolicyEvaluationController _cancelPreviousNotificationForPendingEvaluationRecord:]_block_invoke
+ ___99-[LACDTOPendingPolicyEvaluationController _removePendingEvaluationRecordWithIdentifier:completion:]_block_invoke
+ ___99-[LACDTOPendingPolicyEvaluationController _removePendingEvaluationRecordWithIdentifier:completion:]_block_invoke.21
+ ___99-[LACDTOPendingPolicyEvaluationController _removePendingEvaluationRecordWithIdentifier:completion:]_block_invoke_2
+ ___99-[LACDTOPendingPolicyEvaluationController _updatePendingEvaluationsWithUpdateBlock:observerFilter:]_block_invoke
+ ___AuthKitLibraryCore_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___CoreRoutineLibraryCore_block_invoke
+ ___LACDTBiometryWatchdogGlobalFallbackTime_block_invoke
+ ___LACDTOLostModeStateMaxAgeSeconds_block_invoke
+ ___LACLogDTOClient_block_invoke
+ ___LACLogDTOEnvironment_block_invoke
+ ___LACLogDTOEvaluation_block_invoke
+ ___LACLogDTOEvent_block_invoke
+ ___LACLogDTOFeature_block_invoke
+ ___LACLogDTOLocation_block_invoke
+ ___LACLogDTOLostMode_block_invoke
+ ___LACLogDTONotifications_block_invoke
+ ___LACLogDTOState_block_invoke
+ ___LACLogDTOStorage_block_invoke
+ ___LACLogDTOTimers_block_invoke
+ ___LACLogDTOUI_block_invoke
+ ___LACLogDTO_block_invoke
+ ___NSDictionary0__struct
+ ___assert_rtn
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e18_v16?0"NSString"8l
+ ___block_descriptor_32_e21_v16?0"NSHashTable"8l
+ ___block_descriptor_32_e22_v16?0"NSMutableSet"8l
+ ___block_descriptor_32_e29_v16?0"LACDTOLocationState"8l
+ ___block_descriptor_32_e40_v24?0"LACDTORatchetState"8"NSError"16l
+ ___block_descriptor_32_e59_B16?0"<LACDTOPendingPolicyEvaluationControllerObserver>"8l
+ ___block_descriptor_32_e77_B16?0"_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation"8l
+ ___block_descriptor_35_e32_"LACDTOMutableFeatureState"8?0l
+ ___block_descriptor_40_e22_v16?0"NSMutableSet"8l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32bs_e22_v16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32bs_e29_v16?0"LACDTOLocationState"8ls32l8
+ ___block_descriptor_40_e8_32bs_e29_v16?0"LACDTOLostModeState"8ls32l8
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_e8_32r_e20_v20?0B8"NSError"12lr32l8
+ ___block_descriptor_40_e8_32r_e21_v16?0"NSHashTable"8lr32l8
+ ___block_descriptor_40_e8_32r_e40_v24?0"LACDTORatchetState"8"NSError"16lr32l8
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32s_e21_v16?0"NSHashTable"8ls32l8
+ ___block_descriptor_40_e8_32s_e25_B32?0"NSNumber"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e31_B32?0"AKRemoteDevice"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e59_B16?0"<LACDTOPendingPolicyEvaluationControllerObserver>"8ls32l8
+ ___block_descriptor_40_e8_32s_e59_v16?0"<LACDTOPendingPolicyEvaluationControllerObserver>"8ls32l8
+ ___block_descriptor_40_e8_32s_e77_B16?0"_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation"8ls32l8
+ ___block_descriptor_40_e8_32w_e40_v16?0?<v?"LACBackgroundTaskResult">8lw32l8
+ ___block_descriptor_40_e8_32w_e40_v24?0"LACDTORatchetState"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e29_v16?0"LACDTOLocationState"8lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e29_v16?0"LACDTOLostModeState"8lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e31_v20?0B8"LACDTORatchetState"12lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e33_v16?0"LACBackgroundTaskResult"8lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e40_v24?0"LACDTOKVStoreValue"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e40_v24?0"LACDTORatchetState"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e41_v24?0"LACDTOLostModeState"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e48_v24?0"RTAuthorizedLocationStatus"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e53_v24?0"LACDTORatchetStateWithWatchdogs"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e95_v40?0q8"NSDictionary"16"<LACDTOPolicyEvaluationRequest>"24?<v?"NSDictionary""NSError">32ls32l8w40l8
+ ___block_descriptor_48_e8_32r_e22_v16?0"NSMutableSet"8lr32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e31_v20?0B8"LACDTORatchetState"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e40_v24?0"LACDTORatchetState"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e21_v16?0"NSHashTable"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e52_v16?0"<LACDTOPolicyEvaluationControllerObserver>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e29_v24?0"NSArray"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e31_v20?0B8"LACDTORatchetState"12lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e39_"LACDTORatchetNotificationCoolOff"8?0ls32l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_49_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_49_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_50_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e20_v20?0B8"NSError"12lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e34_v24?0"NSDictionary"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e59_v16?0"<LACDTOPendingPolicyEvaluationControllerObserver>"8ls40l8w48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e42_v24?0"AKDeviceListResponse"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e42_"LACDTOMutablePolicyEvaluationResult"8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e52_v16?0"<LACDTOPolicyEvaluationControllerObserver>"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e77_B16?0"_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e5_v8?0lw56l8s32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e74_"_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation"8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e43_"LACDTOMutablePolicyEvaluationRequest"8?0ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs56w_e20_v20?0B8"NSError"12lw56l8s48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_80_e8_32s40s48bs56bs64w_e41_v24?0"<LACDTOEnvironment>"8"NSError"16lw64l8s48l8s56l8s32l8s40l8
+ ___block_literal_global.10
+ ___block_literal_global.11
+ ___block_literal_global.13
+ ___block_literal_global.15
+ ___block_literal_global.16
+ ___block_literal_global.19
+ ___block_literal_global.2
+ ___block_literal_global.22
+ ___block_literal_global.23
+ ___block_literal_global.25
+ ___block_literal_global.26
+ ___block_literal_global.28
+ ___block_literal_global.3
+ ___block_literal_global.31
+ ___block_literal_global.34
+ ___block_literal_global.37
+ ___block_literal_global.38
+ ___block_literal_global.40
+ ___block_literal_global.42
+ ___block_literal_global.43
+ ___block_literal_global.46
+ ___block_literal_global.5
+ ___block_literal_global.7
+ ___block_literal_global.8
+ ___getAKAccountManagerClass_block_invoke
+ ___getAKAccountManagerClass_block_invoke.cold.1
+ ___getAKAppleIDAuthenticationControllerClass_block_invoke
+ ___getAKAppleIDAuthenticationControllerClass_block_invoke.cold.1
+ ___getAKDeviceListRequestContextClass_block_invoke
+ ___getAKDeviceListRequestContextClass_block_invoke.cold.1
+ ___getRTRoutineManagerClass_block_invoke
+ ___getRTRoutineManagerClass_block_invoke.cold.1
+ ___kCFBooleanTrue
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_1
+ __os_log_debug_impl
+ __os_log_error_impl
+ __os_signpost_emit_with_name_impl
+ __sl_dlopen
+ __swiftEmptyDictionarySingleton
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_reportUnimplementedInitializer
+ __unnamed_array_storage
+ __unnamed_array_storage.11
+ __unnamed_array_storage.23
+ __unnamed_array_storage.34
+ _abort_report_np
+ _associated conformance 23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOSHAASQ
+ _associated conformance 23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _audit_stringAuthKit
+ _audit_stringCoreRoutine
+ _block_copy_helper.17
+ _block_copy_helper.24
+ _block_copy_helper.31
+ _block_copy_helper.38
+ _block_copy_helper.61
+ _block_descriptor.19
+ _block_descriptor.2
+ _block_descriptor.22
+ _block_descriptor.26
+ _block_descriptor.33
+ _block_descriptor.34
+ _block_descriptor.36
+ _block_descriptor.37
+ _block_descriptor.38
+ _block_descriptor.39
+ _block_descriptor.40
+ _block_descriptor.63
+ _block_destroy_helper.18
+ _block_destroy_helper.25
+ _block_destroy_helper.32
+ _block_destroy_helper.39
+ _block_destroy_helper.62
+ _bzero
+ _dispatch_after
+ _dispatch_assert_queue$V2
+ _dispatch_async
+ _free
+ _getAKAccountManagerClass
+ _getAKAccountManagerClass.softClass
+ _getAKAppleIDAuthenticationControllerClass
+ _getAKAppleIDAuthenticationControllerClass.softClass
+ _getAKDeviceListRequestContextClass
+ _getAKDeviceListRequestContextClass.softClass
+ _getRTRoutineManagerClass
+ _getRTRoutineManagerClass.softClass
+ _objc_autorelease
+ _objc_getClass
+ _objc_msgSend$_addPendingEvaluationRecord:currentState:
+ _objc_msgSend$_addPendingEvaluationRecordForRequest:currentState:
+ _objc_msgSend$_canFinishPendingEvaluationsForRatchetState:
+ _objc_msgSend$_cancelPreviousNotificationForPendingEvaluationRecord:
+ _objc_msgSend$_checkDeviceHasBeenUnlockedSinceBoot
+ _objc_msgSend$_checkIsRatchetStateIn:completion:
+ _objc_msgSend$_checkShouldAddPendingEvaluationRecordForRequest:completion:
+ _objc_msgSend$_checkShouldKeepPendingEvaluationRecordForResult:completion:
+ _objc_msgSend$_connectionWithErrorHandler:
+ _objc_msgSend$_coolOffStartedTimestampForIdentifier:currentState:
+ _objc_msgSend$_errorCodesToFilterForOptions:
+ _objc_msgSend$_evaluatePolicy:options:client:environment:evaluationBlock:reply:
+ _objc_msgSend$_featureFlagKey
+ _objc_msgSend$_fetchDeviceHintsCurrentConnection:completion:
+ _objc_msgSend$_forEachObserver:
+ _objc_msgSend$_handleConnectionClose
+ _objc_msgSend$_handleRatchetStateChanged:
+ _objc_msgSend$_handleSwitchToCoolOffState:
+ _objc_msgSend$_handleSwitchToFinalState:
+ _objc_msgSend$_hasPendingEvaluationRecordForRequest:
+ _objc_msgSend$_loadPendingEvaluations
+ _objc_msgSend$_locationStateFromBackgroundTaskResult:
+ _objc_msgSend$_lostModeStateFromBackgroundTaskResult:
+ _objc_msgSend$_lostModeStateWithCompletion:
+ _objc_msgSend$_mapResult:error:filterCodes:completion:
+ _objc_msgSend$_noAuthenticationOnFallbackEvaluationBlockWithBlock:
+ _objc_msgSend$_notifyObserversAboutEvaluation:
+ _objc_msgSend$_notifyObserversAboutEvaluation:result:
+ _objc_msgSend$_prunePendingEvaluationsWithUUID:
+ _objc_msgSend$_ratchetCoolOffNotificationManager
+ _objc_msgSend$_remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$_removePendingEvaluationRecordWithIdentifier:completion:
+ _objc_msgSend$_resetRatchetWithCompletion:
+ _objc_msgSend$_runLocationStateBackgroundTask:completion:
+ _objc_msgSend$_runLostModeBackgroundTaskWithStrategy:completion:
+ _objc_msgSend$_runLostModeBackgroundTaskWithTimeout:completion:
+ _objc_msgSend$_scheduleNextStatusCheck
+ _objc_msgSend$_scheduleNotificationForPendingEvaluationRecord:after:maxAge:
+ _objc_msgSend$_setFeatureEnabled:context:connection:completion:
+ _objc_msgSend$_setValue:forKey:contextUUID:connection:completion:
+ _objc_msgSend$_shouldPrunePendingEvaluation:uuid:
+ _objc_msgSend$_startMonitoringWithReason:
+ _objc_msgSend$_stopMonitoringWithReason:
+ _objc_msgSend$_storeLostModeState:completion:
+ _objc_msgSend$_synchronizedObservers:
+ _objc_msgSend$_synchronizedSubscriptions:
+ _objc_msgSend$_synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$_updatePendingEvaluationsWithBlock:
+ _objc_msgSend$_updatePendingEvaluationsWithUpdateBlock:observerFilter:
+ _objc_msgSend$_verifyHasRequiredOptions:forPolicy:error:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addPendingEvaluation:
+ _objc_msgSend$allKeys
+ _objc_msgSend$allObjects
+ _objc_msgSend$allowsAuthenticationFallbacks
+ _objc_msgSend$altDSIDForAccount:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$biometryWatchdogDTO
+ _objc_msgSend$biometryWatchdogGlobal
+ _objc_msgSend$biometryWatchdogPack
+ _objc_msgSend$boolValue
+ _objc_msgSend$bytes
+ _objc_msgSend$callbackReason
+ _objc_msgSend$callbackURL
+ _objc_msgSend$cancelNotificationsWithIdentifiers:completion:
+ _objc_msgSend$cancelPendingEvaluationForClient:ratchetIdentifier:reason:completion:
+ _objc_msgSend$cancelPendingEvaluationWithRatchetIdentifier:reason:completion:
+ _objc_msgSend$cancelPreviousSecurityDelayFinishedNotificationForPendingEvaluation:completion:
+ _objc_msgSend$categoryIdentifier
+ _objc_msgSend$checkCanEnableFeatureWithCompletion:
+ _objc_msgSend$checkIsFeatureAvailableWithCompletion:
+ _objc_msgSend$checkIsFeatureEnabledWithCompletion:
+ _objc_msgSend$checkIsFeatureSupportedWithCompletion:
+ _objc_msgSend$checkIsInFamiliarLocationWithCompletion:
+ _objc_msgSend$compare:
+ _objc_msgSend$confirmed
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$continueWithSettings
+ _objc_msgSend$coolOffStarted
+ _objc_msgSend$createdAt
+ _objc_msgSend$currentConnection
+ _objc_msgSend$data
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$defaultLocationState
+ _objc_msgSend$defaultLostModeState
+ _objc_msgSend$defaultManager
+ _objc_msgSend$deviceList
+ _objc_msgSend$deviceListWithContext:completion:
+ _objc_msgSend$deviceRestrictionState
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$disableFeatureWithContext:completion:
+ _objc_msgSend$dispatchAfter:inQueue:repeat:block:
+ _objc_msgSend$dispatchEvent:sender:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$duration
+ _objc_msgSend$eStatus
+ _objc_msgSend$effectiveDuration
+ _objc_msgSend$enableFeatureWithCompletion:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$encodeLocalizationKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$endpoint:
+ _objc_msgSend$environment
+ _objc_msgSend$error:hasCode:
+ _objc_msgSend$errorWithCode:subcode:debugDescription:
+ _objc_msgSend$evaluationIdentifierForClient:ratchetIdentifier:
+ _objc_msgSend$eventBus
+ _objc_msgSend$featureState
+ _objc_msgSend$fetchAuthorizedLocationStatus:
+ _objc_msgSend$fetchEnvironmentForPolicy:options:completion:
+ _objc_msgSend$handleEvent:sender:
+ _objc_msgSend$handlesPolicy:options:
+ _objc_msgSend$hasBeenUnlockedSinceBoot
+ _objc_msgSend$hasBiometricEnrollmentsForCurrentUser
+ _objc_msgSend$hasExpiredBiometry
+ _objc_msgSend$hasHSA2Account
+ _objc_msgSend$hasLocationServicesEnabled
+ _objc_msgSend$hasNotifiedUserAboutCompletion
+ _objc_msgSend$hasPasscodeSetForCurrentUser
+ _objc_msgSend$hash
+ _objc_msgSend$identifier
+ _objc_msgSend$inFamiliarLocation
+ _objc_msgSend$indexOfObjectPassingTest:
+ _objc_msgSend$initWithBoolValue:
+ _objc_msgSend$initWithConnection:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithIdentifier:body:deeplinkURL:
+ _objc_msgSend$initWithIntegerValue:
+ _objc_msgSend$initWithIsInFamiliarLocation:confirmed:
+ _objc_msgSend$initWithIsInFamiliarLocation:confirmed:createdAt:
+ _objc_msgSend$initWithIsInLostMode:
+ _objc_msgSend$initWithIsInLostMode:confirmed:
+ _objc_msgSend$initWithIsInLostMode:confirmed:createdAt:
+ _objc_msgSend$initWithListenerEndpoint:
+ _objc_msgSend$initWithLocationProvider:featureController:ratchetStateProvider:lostModeController:
+ _objc_msgSend$initWithPersistentStore:workQueue:
+ _objc_msgSend$initWithRawValue:duration:resetDuration:uuid:
+ _objc_msgSend$initWithRawValue:optionalValue:
+ _objc_msgSend$initWithRawValue:value:
+ _objc_msgSend$initWithUserDefaults:
+ _objc_msgSend$initWithValue:
+ _objc_msgSend$initWithWorker:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isAvailable
+ _objc_msgSend$isBarking
+ _objc_msgSend$isDTOEnabled
+ _objc_msgSend$isEnabled
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$isInFamiliarLocation
+ _objc_msgSend$isInLostMode
+ _objc_msgSend$isInteractiveRatchetEvaluation
+ _objc_msgSend$isNotificationScheduledForDate:
+ _objc_msgSend$isPhone
+ _objc_msgSend$isSuccess
+ _objc_msgSend$isSupported
+ _objc_msgSend$isValid:
+ _objc_msgSend$loadPersistedEvaluationsWithCompletion:
+ _objc_msgSend$localizedStringFromDate:dateStyle:timeStyle:
+ _objc_msgSend$locationStateBackgroundTask
+ _objc_msgSend$locationStatusQueryDidFinish
+ _objc_msgSend$locationStatusQueryWillStart
+ _objc_msgSend$lostModeBackgroundTask
+ _objc_msgSend$lostModeQueryDidFinish
+ _objc_msgSend$lostModeQueryWillStart
+ _objc_msgSend$lostModeStateWithCompletion:
+ _objc_msgSend$maxAge
+ _objc_msgSend$maxThreshold
+ _objc_msgSend$minThreshold
+ _objc_msgSend$now
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$options
+ _objc_msgSend$pendingEvaluationController:updatedPendingEvaluation:
+ _objc_msgSend$pendingEvaluationControllerDidStartTrackingPendingEvaluations:
+ _objc_msgSend$pendingEvaluationControllerDidStopTrackingPendingEvaluations:
+ _objc_msgSend$pendingEvaluationWithIdentifier:
+ _objc_msgSend$pendingEvaluations
+ _objc_msgSend$persistEvaluations
+ _objc_msgSend$persistentDomainForName:
+ _objc_msgSend$policy
+ _objc_msgSend$policyController:didFinishPolicyEvaluation:result:
+ _objc_msgSend$policyController:willStartPolicyEvaluation:
+ _objc_msgSend$postNotification:
+ _objc_msgSend$postNotificationWithConfiguration:delay:completion:
+ _objc_msgSend$primaryAuthKitAccount
+ _objc_msgSend$processInfo
+ _objc_msgSend$ratchetState
+ _objc_msgSend$ratchetStateWithCompletion:
+ _objc_msgSend$ratchetStateWithWatchdogsCompletion:
+ _objc_msgSend$ratchetUUID
+ _objc_msgSend$rawValue
+ _objc_msgSend$reason
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$removePendingEvaluationWith:
+ _objc_msgSend$resetDuration
+ _objc_msgSend$resetRatchetWithCompletion:
+ _objc_msgSend$result
+ _objc_msgSend$resume
+ _objc_msgSend$scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:maxAge:completion:
+ _objc_msgSend$securityDelayEnded
+ _objc_msgSend$send
+ _objc_msgSend$serialNumber
+ _objc_msgSend$setAltDSID:
+ _objc_msgSend$setBody:
+ _objc_msgSend$setCallbackReason:
+ _objc_msgSend$setCallbackURL:
+ _objc_msgSend$setCoolOffStarted:
+ _objc_msgSend$setDefaultActionURL:
+ _objc_msgSend$setEnvironment:
+ _objc_msgSend$setError:
+ _objc_msgSend$setFetchDeviceSafetyState:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setIsAvailable:
+ _objc_msgSend$setIsEnabled:
+ _objc_msgSend$setIsSupported:
+ _objc_msgSend$setIsTimeSensitive:
+ _objc_msgSend$setLocationState:
+ _objc_msgSend$setMaxAge:
+ _objc_msgSend$setNotificationScheduledAt:
+ _objc_msgSend$setOptions:
+ _objc_msgSend$setPolicy:
+ _objc_msgSend$setRatchetState:
+ _objc_msgSend$setRatchetUUID:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setResult:
+ _objc_msgSend$setSerialNumbers:
+ _objc_msgSend$setSystemIconName:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setValue:forKey:completion:
+ _objc_msgSend$setValue:forKey:connection:completion:
+ _objc_msgSend$setValue:forKey:contextUUID:connection:completion:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$time
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$uuid
+ _objc_msgSend$valueForKey:completion:
+ _objc_msgSend$valueForKey:connection:completion:
+ _objc_msgSend$watchdogs
+ _objc_msgSend$workQueue
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retain_x10
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
+ _objectdestroy.22Tm
+ _objectdestroy.55Tm
+ _objectdestroyTm
+ _os_signpost_enabled
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _os_variant_allows_internal_security_policies
+ _os_variant_has_internal_content
+ _swift_allocError
+ _swift_beginAccess
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_deallocPartialClassInstance
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _symbolic $s23LocalAuthenticationCore38LACDTOPendingPolicyEvaluationStoreTypeP
+ _symbolic $sSY
+ _symbolic BD
+ _symbolic IeghH_
+ _symbolic IeyB_
+ _symbolic SDySS_____G 23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC
+ _symbolic SDy_____ypG s11AnyHashableV
+ _symbolic SNy_____G 10Foundation4DateV
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic SaySSG
+ _symbolic Say_____G 23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic Say_____GSg______pSgIeggg_ 23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC s5ErrorP
+ _symbolic ScPSg
+ _symbolic Si
+ _symbolic So14NSUserDefaultsC
+ _symbolic So17LACDTOEnvironment_pSgSo7NSErrorCSgIeyByy_
+ _symbolic So17LACDTOEnvironment_pSg______pSgIeggg_ s5ErrorP
+ _symbolic So17OS_dispatch_queueC
+ _symbolic So18LACDTOFeatureState_p
+ _symbolic So18LACPersistentStore_p
+ _symbolic So19LACDTOLocationStateC
+ _symbolic So19SwiftNativeNSObjectC
+ _symbolic So21LACRatchetFlowManagerCSgXw
+ _symbolic So21LACRatchetFlowManagerCSgXwz_Xx
+ _symbolic So22LACDTOLocationProvider_p
+ _symbolic So24LACDTOFeatureControlling_p
+ _symbolic So26LACDTOLostModeFetchService_p
+ _symbolic So26LACDTORatchetStateProvider_p
+ _symbolic So29LACDTOPendingPolicyEvaluation_p
+ _symbolic So6NSDataC
+ _symbolic So6NSDataCSgSo7NSErrorCSgIeyByy_
+ _symbolic So7NSArrayCSgSo7NSErrorCSgIeyByy_
+ _symbolic So8NSStringC
+ _symbolic _____ 23LocalAuthenticationCore25LACDTOEnvironmentProviderC
+ _symbolic _____ 23LocalAuthenticationCore30LACUserDefaultsPersistentStoreC
+ _symbolic _____ 23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC
+ _symbolic _____ 23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC
+ _symbolic _____ 23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLO
+ _symbolic _____ So17LACRatchetUIStateV
+ _symbolic _____ So26LACAuthUIPresentationStyleV
+ _symbolic _____5lower_AA5uppert 10Foundation4DateV
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____SgXw 23LocalAuthenticationCore25LACDTOEnvironmentProviderC
+ _symbolic _____SgXw 23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC
+ _symbolic _____SgXwz_Xx 23LocalAuthenticationCore25LACDTOEnvironmentProviderC
+ _symbolic _____SgXwz_Xx 23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC
+ _symbolic _____Sg_ABt 10Foundation3URLV
+ _symbolic _____Sg_ABt 10Foundation4DateV
+ _symbolic _____XDXMT 23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStoreC
+ _symbolic ______p s5ErrorP
+ _symbolic ______pSgIegg_Sg s5ErrorP
+ _symbolic ______ypt s11AnyHashableV
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_____G s18_DictionaryStorageC 23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluationC10CodingKeys33_4BC7126A1542EEEDCA6425CD3A877DA1LLO
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
+ _symbolic ypSg
+ _symbolic ytIeghHr_
CStrings:
+ "\x01\x11"
+ "\x04"
+ "\x05"
+ "\a"
+ "\x11"
+ "\x13"
+ "\x15"
+ "#"
+ "$defaultActor"
+ "%@ mapping error %@ to success"
+ "%s"
+ "%{public}@"
+ "%{public}@ DSLMode changed from: %@ to %@"
+ "%{public}@ Missing required RTRoutineManager dependency"
+ "%{public}@ did finish query"
+ "%{public}@ did finish query %@"
+ "%{public}@ did finish query with error %{public}@"
+ "%{public}@ did finish query with error: %{public}@"
+ "%{public}@ did finish query with error: (%{public}@)"
+ "%{public}@ did finish query with value: %@"
+ "%{public}@ ignoring redundant request to start"
+ "%{public}@ performing scheduled query"
+ "%{public}@ query finished with error %{public}@"
+ "%{public}@ starting monitor with an interval of %.2f secs with reason: %{public}@"
+ "%{public}@ stopping monitor with reason: %{public}@"
+ "%{public}@ will perform query with %.2f sec timeout"
+ "%{public}@ will skip query because current ratchet state allows it"
+ "%{public}@ will start query"
+ "%{public}@ will start query with '%@' strategy"
+ "%{public}@ will use cached value %@"
+ "-[LACDTOFeatureController checkCanEnableFeatureWithCompletion:]_block_invoke"
+ "-[LACDTOFeatureController enableFeatureWithCompletion:]_block_invoke"
+ "-[LACDTOPolicyEvaluationController initWithEnvironment:evaluationIdentifierFactory:device:]"
+ "1"
+ "<%@ %p>"
+ "@\"<LACAuthUIPresenting>\""
+ "@\"<LACDTODeviceInfoProvider>\""
+ "@\"<LACDTOEnvironment>\""
+ "@\"<LACDTOEnvironment>\"16@0:8"
+ "@\"<LACDTOEnvironmentProviding>\""
+ "@\"<LACDTOEventBus>\""
+ "@\"<LACDTOEventBus>\"16@0:8"
+ "@\"<LACDTOFeatureControlling>\""
+ "@\"<LACDTOFeatureState>\""
+ "@\"<LACDTOFeatureState>\"16@0:8"
+ "@\"<LACDTOKVStore>\""
+ "@\"<LACDTOLocationProvider>\""
+ "@\"<LACDTOLostModeProvider>\""
+ "@\"<LACDTOPendingPolicyEvaluationController>\""
+ "@\"<LACDTOPolicyEvaluationIdentifierFactory>\""
+ "@\"<LACDTORatchetHandler>\""
+ "@\"<LACDTORatchetStateProvider>\""
+ "@\"<LACDTOServiceXPCEndpointProvider>\""
+ "@\"<LACDarwinNotificationCenter>\""
+ "@\"<LACRatchetUIManaging>\""
+ "@\"<_TtP23LocalAuthenticationCore38LACDTOPendingPolicyEvaluationStoreType_>\""
+ "@\"LACBackgroundTask\""
+ "@\"LACDTOBiometryWatchdog\""
+ "@\"LACDTOBiometryWatchdogPack\""
+ "@\"LACDTOBiometryWatchdogPack\"16@0:8"
+ "@\"LACDTOLocationState\""
+ "@\"LACDTOLostModeState\""
+ "@\"LACDTOMutableFeatureState\"8@?0"
+ "@\"LACDTOMutablePolicyEvaluationRequest\"8@?0"
+ "@\"LACDTOMutablePolicyEvaluationResult\"8@?0"
+ "@\"LACDTONotificationManager\""
+ "@\"LACDTORatchetNotificationCoolOff\"8@?0"
+ "@\"LACDTORatchetState\""
+ "@\"LACDTORatchetState\"16@0:8"
+ "@\"NSArray\"16@0:8"
+ "@\"NSArray\"32@0:8q16@\"NSDictionary\"24"
+ "@\"NSData\""
+ "@\"NSDate\""
+ "@\"NSDate\"16@0:8"
+ "@\"NSDictionary\""
+ "@\"NSDictionary\"16@0:8"
+ "@\"NSError\"16@0:8"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSString\""
+ "@\"NSURL\""
+ "@\"NSURL\"16@0:8"
+ "@\"NSXPCConnection\""
+ "@\"RTRoutineManager\""
+ "@\"_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation\"24@0:8@\"NSString\"16"
+ "@\"_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation\"8@?0"
+ "@20@0:8B16"
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8B16B20"
+ "@32@0:8B16B20@24"
+ "@32@0:8q16q24"
+ "@40@0:8@16@24@32"
+ "@40@0:8q16q24@32"
+ "@44@0:8B16d20d28d36"
+ "@48@0:8@16@24@32@40"
+ "@48@0:8q16d24d32@40"
+ "@56@0:8@16@24@32@40@48"
+ "@?24@0:8@?16"
+ "AKAccountManager"
+ "AKAppleIDAuthenticationController"
+ "AKDeviceListRequestContext"
+ "AppleLanguagePreferencesChangedNotification"
+ "B16@?0@\"<LACDTOPendingPolicyEvaluationControllerObserver>\"8"
+ "B16@?0@\"_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation\"8"
+ "B24@0:8@\"NSDate\"16"
+ "B32@0:8@16@24"
+ "B32@0:8q16@\"NSDictionary\"24"
+ "B32@0:8q16@24"
+ "B32@?0@\"AKRemoteDevice\"8Q16^B24"
+ "B32@?0@\"NSNumber\"8Q16^B24"
+ "B40@0:8@16q24^@32"
+ "BestEffort"
+ "CONTINUE_WITH_SETTINGS"
+ "Canceling pending evaluation with reason: %@, identifier: %@, did find instance: %@"
+ "Could not determine altDISD for account"
+ "Could not determine device SN"
+ "Could not determine safety state. Device not found."
+ "Could not determine safety state. Missing value"
+ "Could not fetch biometric liveness (%{public}@)"
+ "Could not fetch feature available status (%{public}@)"
+ "Could not fetch feature enabled status (%{public}@)"
+ "Could not fetch feature supported status (%{public}@)"
+ "Could not fetch ratchet state (%{public}@)"
+ "Could not get synchronous remote object proxy (%{public}@)"
+ "Could not schedule notification for: %{public}@ (error:=%{public}@)"
+ "DSLMode: %@"
+ "DSLMode: %s"
+ "DTO"
+ "DTO policies are not available before first unlock"
+ "DTOEnvironmentUpdate"
+ "DTOLocationStateQuery"
+ "DTOLostModeQuery"
+ "DTO_Client"
+ "DTO_Environment"
+ "DTO_Evaluation"
+ "DTO_Event"
+ "DTO_Feature"
+ "DTO_Location"
+ "DTO_LostMode"
+ "DTO_Notifications"
+ "DTO_State"
+ "DTO_Storage"
+ "DTO_Timers"
+ "DTO_UI"
+ "Did not schedule notification for evaluation: %{public}@ due to error: %{public}@"
+ "Did register observer %@"
+ "Did register observer %@ of notification %@"
+ "Did remove observer %@"
+ "Did schedule notification after: %.2f secs expiring after: %.2f secs for %{public}@"
+ "Did update environment"
+ "Does need pending evaluation record for '%@' for current ratchet state: %@"
+ "Does not need pending evaluation record for '%@' after success"
+ "Does not need pending evaluation record for '%@' after user cancel"
+ "Does not need pending evaluation record for '%@' for current ratchet state: %@"
+ "ENTER_PASSCODE_IPHONE"
+ "Failed to persist pending evaluations with error %@"
+ "Feature not available because biometry is not enrolled"
+ "Feature not available because passcode is not set"
+ "Feature not supported for device type"
+ "Ignoring expiration date because is too close to the delivery date"
+ "LA.dto.lostModeEnabledMaxAgeSeconds"
+ "LA.dto.optionUseShortExpirationTimerMs"
+ "LACAuthFlowManaging"
+ "LACDTOBiometryWatchdog"
+ "LACDTOBiometryWatchdogPack"
+ "LACDTODarwinNotificationsController"
+ "LACDTOEnvironment"
+ "LACDTOEnvironmentProviderFactory"
+ "LACDTOEnvironmentProviding"
+ "LACDTOEvent"
+ "LACDTOEventBus"
+ "LACDTOEventHandler"
+ "LACDTOEventProducer"
+ "LACDTOFeatureController"
+ "LACDTOFeatureController.m"
+ "LACDTOFeatureControlling"
+ "LACDTOFeatureState"
+ "LACDTOKVStoreValue"
+ "LACDTOLocationMonitor"
+ "LACDTOLocationProvider"
+ "LACDTOLocationProviderCRAdapter"
+ "LACDTOLocationProviderKVSAdapter"
+ "LACDTOLocationState"
+ "LACDTOLostModeController"
+ "LACDTOLostModeFetchRequest"
+ "LACDTOLostModeFetchService"
+ "LACDTOLostModeProvider"
+ "LACDTOLostModeProviderAKAdapter"
+ "LACDTOLostModeProviderKVSAdapter"
+ "LACDTOLostModeState"
+ "LACDTOMutableEnvironment"
+ "LACDTOMutableFeatureState"
+ "LACDTOMutableLostModeFetchRequest"
+ "LACDTOMutablePolicyEvaluationRequest"
+ "LACDTOMutablePolicyEvaluationResult"
+ "LACDTONotificationManager"
+ "LACDTOPendingPolicyEvaluation"
+ "LACDTOPendingPolicyEvaluationController"
+ "LACDTOPendingPolicyEvaluationControllerObserver"
+ "LACDTOPolicyEvaluation"
+ "LACDTOPolicyEvaluationController"
+ "LACDTOPolicyEvaluationController.m"
+ "LACDTOPolicyEvaluationControllerObserver"
+ "LACDTOPolicyEvaluationRequest"
+ "LACDTOPolicyEvaluationResult"
+ "LACDTORatchetNotificationCoolOff"
+ "LACDTORatchetState"
+ "LACDTORatchetStateMonitor"
+ "LACDTORatchetStateProvider"
+ "LACDTORatchetStateRawValueCollapsed"
+ "LACDTORatchetStateRawValueNotStarted"
+ "LACDTORatchetStateRawValueReady"
+ "LACDTORatchetStateRawValueWaitingForCoolOff"
+ "LACDTORatchetStateRawValueWaitingForSecondAuthentication"
+ "LACDTORatchetStateWithWatchdogs"
+ "LACDTOServiceXPC"
+ "LACDTOServiceXPCClient"
+ "LACDTOServiceXPCHost"
+ "LACDTOSignpostEvent"
+ "LACPersistentStore"
+ "LACPersistentStoreFactory"
+ "LACPolicyLocationBasedDeviceOwnerAuthentication"
+ "LACPolicyLocationBasedDeviceOwnerAuthenticationWithBiometricRatchet"
+ "LACRatchetFlowManager"
+ "LACRatchetFlowManaging"
+ "LACUNNotificationConfiguration"
+ "LADTOEventRawValueFeatureEnabledStatusDidChange"
+ "LADTOEventRawValueLocationStatusDidChange"
+ "LADTOEventRawValueRatchetStateDidChange"
+ "Loaded pending evaluations %s"
+ "Loading pending evaluations"
+ "LocalAuthenticationCore.LACDTOEnvironmentProvider"
+ "LocalAuthenticationCore.LACDTOMutablePendingPolicyEvaluation"
+ "LocalAuthenticationCore.LACDTOPendingPolicyEvaluationStore"
+ "LocalAuthenticationCore.LACUserDefaultsPersistentStore"
+ "Missing AuthKit dependencies"
+ "Missing required option (%d) with type '%@'"
+ "NO"
+ "NSCoding"
+ "NSSecureCoding"
+ "OFF"
+ "ON"
+ "Pending evaluations detected"
+ "Pending evaluations finished"
+ "Performing ratchet state query"
+ "Persisted pending evaluations %s"
+ "Policy evaluation did finish: %@"
+ "Policy evaluation will start: %@"
+ "Pruning pending evaluations with uuid: %{public}@"
+ "Q"
+ "RTRoutineManager"
+ "Ratchet state changed from: %{public}@ to %{public}@"
+ "Request timed out after %.2f secs"
+ "Reseting Ratchet as there are no pending evaluations"
+ "SECURITY_DELAY_ENDED"
+ "Schedule ratchet state check in %.2f"
+ "Scheduled notification for evaluation: %{public}@ after: %.2f secs"
+ "Skip"
+ "Skipping cancellation of pending evaluation with reason: %@, identifier: %@"
+ "T@\"<LACAuthUIPresenting>\",R,N,V_presenter"
+ "T@\"<LACDTOEnvironment>\",&,N,V_environment"
+ "T@\"<LACDTOEnvironment>\",R,N"
+ "T@\"<LACDTOEventBus>\",&,N"
+ "T@\"<LACDTOEventBus>\",&,N,VeventBus"
+ "T@\"<LACDTOFeatureState>\",&,N,V_featureState"
+ "T@\"<LACDTOFeatureState>\",R,N"
+ "T@\"<LACRatchetUIManaging>\",R,N,V_uiManager"
+ "T@\"LACBackgroundTask\",&,N,V_locationStateBackgroundTask"
+ "T@\"LACBackgroundTask\",&,N,V_lostModeBackgroundTask"
+ "T@\"LACDTOBiometryWatchdog\",R,N,V_biometryWatchdogDTO"
+ "T@\"LACDTOBiometryWatchdog\",R,N,V_biometryWatchdogGlobal"
+ "T@\"LACDTOBiometryWatchdogPack\",&,N,V_biometryWatchdogPack"
+ "T@\"LACDTOBiometryWatchdogPack\",R,N"
+ "T@\"LACDTOBiometryWatchdogPack\",R,N,V_watchdogs"
+ "T@\"LACDTOLocationState\",&,N,V_locationState"
+ "T@\"LACDTONotificationManager\",&,N,V_notificationManager"
+ "T@\"LACDTORatchetState\",&,N,V_ratchetState"
+ "T@\"LACDTORatchetState\",R,N"
+ "T@\"LACDTORatchetState\",R,N,V_ratchetState"
+ "T@\"LACDTOSignpostEvent\",R,N"
+ "T@\"NSArray\",N,R"
+ "T@\"NSDate\",N,C"
+ "T@\"NSDate\",R,N"
+ "T@\"NSDate\",R,N,V_createdAt"
+ "T@\"NSDictionary\",&,N,V_options"
+ "T@\"NSDictionary\",&,N,V_result"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSError\",&,N,V_error"
+ "T@\"NSError\",R,N"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_workQueue"
+ "T@\"NSString\",&,N"
+ "T@\"NSString\",&,N,V_identifier"
+ "T@\"NSString\",&,N,Vbody"
+ "T@\"NSString\",&,N,Videntifier"
+ "T@\"NSString\",&,N,VsystemIconName"
+ "T@\"NSString\",&,N,Vtitle"
+ "T@\"NSString\",N,C"
+ "T@\"NSString\",N,R"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_uuid"
+ "T@\"NSURL\",&,N"
+ "T@\"NSURL\",&,N,VdefaultActionURL"
+ "T@\"NSURL\",N,C"
+ "T@\"NSURL\",R,N"
+ "TB,N"
+ "TB,N,R"
+ "TB,N,V_inFamiliarLocation"
+ "TB,N,V_isAvailable"
+ "TB,N,V_isDTOEnabled"
+ "TB,N,V_isEnabled"
+ "TB,N,V_isSupported"
+ "TB,N,VisTimeSensitive"
+ "TB,R"
+ "TB,R,N,V_confirmed"
+ "TB,R,N,V_isInFamiliarLocation"
+ "TB,R,N,V_isInLostMode"
+ "TB,R,N,V_isRunning"
+ "Td,N"
+ "Td,N,VmaxAge"
+ "Td,R,N"
+ "Td,R,N,V_duration"
+ "Td,R,N,V_maxThreshold"
+ "Td,R,N,V_minThreshold"
+ "Td,R,N,V_resetDuration"
+ "Td,R,N,V_time"
+ "The pending evaluation for %@ has no cool off timestamp yet"
+ "The pending evaluation for %@ is using the existing cool off timestamp: %@"
+ "The pending evaluation for %@ will use the current time for cool off timestamp: %@"
+ "Tq,N,V_policy"
+ "Tq,R,N,V_rawValue"
+ "Unable to find class %s"
+ "Unable to load pending evaluations with error: %{public}@"
+ "Unable to load pending evaluations, ratchet state failure: %{public}@"
+ "Updated pending evaluations after switch to cool off state: %@"
+ "Will add new pending evaluation with identifier: %@"
+ "Will dispatch event: %@ from: %@"
+ "Will remove pending evaluation with identifier: %@"
+ "Will schedule notification after: %.2f secs expiring after: %.2f secs for: %{public}@"
+ "Will update environment"
+ "XPC connection to LACDTOServiceXPC could not be created"
+ "XPC connection to LACDTOServiceXPC endpoint closed"
+ "YES"
+ "_TtC23LocalAuthenticationCore25LACDTOEnvironmentProvider"
+ "_TtC23LocalAuthenticationCore30LACUserDefaultsPersistentStore"
+ "_TtC23LocalAuthenticationCore34LACDTOPendingPolicyEvaluationStore"
+ "_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation"
+ "_TtP23LocalAuthenticationCore38LACDTOPendingPolicyEvaluationStoreType_"
+ "_addPendingEvaluationRecord:currentState:"
+ "_addPendingEvaluationRecordForRequest:currentState:"
+ "_biometryWatchdogDTO"
+ "_biometryWatchdogGlobal"
+ "_biometryWatchdogPack"
+ "_canFinishPendingEvaluationsForRatchetState:"
+ "_cancelPreviousNotificationForPendingEvaluationRecord:"
+ "_checkDeviceHasBeenUnlockedSinceBoot"
+ "_checkIsRatchetStateIn:completion:"
+ "_checkShouldAddPendingEvaluationRecordForRequest:completion:"
+ "_checkShouldKeepPendingEvaluationRecordForResult:completion:"
+ "_confirmed"
+ "_connection"
+ "_connectionLock"
+ "_connectionWithErrorHandler:"
+ "_coolOffStartedTimestampForIdentifier:currentState:"
+ "_createdAt"
+ "_data"
+ "_device"
+ "_deviceInfo"
+ "_duration"
+ "_endpointProvider"
+ "_environment"
+ "_errorCodesToFilterForOptions:"
+ "_evaluatePolicy:options:client:environment:evaluationBlock:reply:"
+ "_evaluationIdentifierFactory"
+ "_evaluationStore"
+ "_eventHandlers"
+ "_featureController"
+ "_featureFlagKey"
+ "_featureState"
+ "_fetchDeviceHintsCurrentConnection:completion:"
+ "_forEachObserver:"
+ "_handleConnectionClose"
+ "_handleRatchetStateChanged:"
+ "_handleSwitchToCoolOffState:"
+ "_handleSwitchToFinalState:"
+ "_hasPendingEvaluationRecordForRequest:"
+ "_identifier"
+ "_inFamiliarLocation"
+ "_isAvailable"
+ "_isDTOEnabled"
+ "_isEnabled"
+ "_isInFamiliarLocation"
+ "_isInLostMode"
+ "_isSupported"
+ "_kvStore"
+ "_loadPendingEvaluations"
+ "_locationProvider"
+ "_locationState"
+ "_locationStateBackgroundTask"
+ "_locationStateFromBackgroundTaskResult:"
+ "_lostModeBackgroundTask"
+ "_lostModeProvider"
+ "_lostModeState"
+ "_lostModeStateFromBackgroundTaskResult:"
+ "_lostModeStateWithCompletion:"
+ "_manager"
+ "_mapResult:error:filterCodes:completion:"
+ "_maxThreshold"
+ "_minThreshold"
+ "_noAuthenticationOnFallbackEvaluationBlockWithBlock:"
+ "_notificationManager"
+ "_notifyObserversAboutEvaluation:"
+ "_notifyObserversAboutEvaluation:result:"
+ "_observersLock"
+ "_options"
+ "_pendingEvaluationController"
+ "_policy"
+ "_presenter"
+ "_prunePendingEvaluationsWithUUID:"
+ "_ratchetCoolOffNotificationManager"
+ "_ratchetHandler"
+ "_ratchetState"
+ "_ratchetStateProvider"
+ "_rawValue"
+ "_remoteObjectProxyWithErrorHandler:"
+ "_removePendingEvaluationRecordWithIdentifier:completion:"
+ "_resetDuration"
+ "_resetRatchetWithCompletion:"
+ "_result"
+ "_runLocationStateBackgroundTask:completion:"
+ "_runLostModeBackgroundTaskWithStrategy:completion:"
+ "_runLostModeBackgroundTaskWithTimeout:completion:"
+ "_scheduleNextStatusCheck"
+ "_scheduleNotificationForPendingEvaluationRecord:after:maxAge:"
+ "_sendBlock"
+ "_setFeatureEnabled:context:connection:completion:"
+ "_setValue:forKey:contextUUID:connection:completion:"
+ "_shouldPrunePendingEvaluation:uuid:"
+ "_startMonitoringWithReason:"
+ "_stopMonitoringWithReason:"
+ "_store"
+ "_storeLostModeState:completion:"
+ "_subscriptionsLock"
+ "_synchronizedObservers:"
+ "_synchronizedSubscriptions:"
+ "_synchronousRemoteObjectProxyWithErrorHandler:"
+ "_time"
+ "_uiManager"
+ "_updatePendingEvaluationsWithBlock:"
+ "_updatePendingEvaluationsWithUpdateBlock:observerFilter:"
+ "_uuid"
+ "_verifyHasRequiredOptions:forPolicy:error:"
+ "_watchdogs"
+ "_workQueue"
+ "addEntriesFromDictionary:"
+ "addEventHandler:"
+ "addObjectsFromArray:"
+ "addPendingEvaluation:"
+ "allKeys"
+ "allObjects"
+ "allowsAuthenticationFallbacks"
+ "allowsAuthenticationFallbacks: %@"
+ "altDSIDForAccount:"
+ "arrayWithArray:"
+ "biometryWatchdogDTO"
+ "biometryWatchdogDTO: %@"
+ "biometryWatchdogGlobal"
+ "biometryWatchdogGlobal: %@"
+ "biometryWatchdogPack"
+ "biometryWatchdogPack: %@"
+ "boolValue"
+ "bundleForClass:"
+ "bytes"
+ "callbackReason"
+ "callbackReason: "
+ "callbackURL"
+ "cancelPendingEvaluationForClient:ratchetIdentifier:reason:completion:"
+ "cancelPendingEvaluationWithRatchetIdentifier:reason:completion:"
+ "cancelPreviousSecurityDelayFinishedNotificationForPendingEvaluation:completion:"
+ "checkCanEnableFeatureWithCompletion:"
+ "checkIsFeatureAvailableWithCompletion:"
+ "checkIsFeatureEnabledWithCompletion:"
+ "checkIsFeatureSupportedWithCompletion:"
+ "checkIsInFamiliarLocationWithCompletion:"
+ "com.apple.CoreAuthUI"
+ "com.apple.LocalAuthentication.ratchet.StateDidChange"
+ "com.apple.coreauthd.notifications.ratchetCoolOff"
+ "com.apple.private.LocalAuthentication.DTO"
+ "com.apple.private.LocalAuthentication.DTO.FallbackToNoAuth"
+ "com.apple.private.LocalAuthentication.DTO.ShortExpiration"
+ "compare:"
+ "confirmed"
+ "confirmed: %@"
+ "continueWithSettings"
+ "coolOffStarted"
+ "coolOffStarted: "
+ "createdAt"
+ "createdAt: %@"
+ "createdAtTimestamp: %.2f"
+ "currentConnection"
+ "d"
+ "d16@0:8"
+ "data"
+ "dataForKey:"
+ "dataForKey:completion:"
+ "dataWithBytes:length:"
+ "dateWithTimeIntervalSinceNow:"
+ "decodeDoubleForKey:"
+ "decodeIntegerForKey:"
+ "decodeObjectOfClass:forKey:"
+ "defaultLocationState"
+ "defaultLostModeState"
+ "defaultManager"
+ "deviceList"
+ "deviceListWithContext:completion:"
+ "deviceRestrictionState"
+ "dictionaryWithDictionary:"
+ "disableFeatureWithContext:completion:"
+ "dismissAnimated:completion:"
+ "dismissWithCompletion:"
+ "dispatchEvent:sender:"
+ "doubleValue"
+ "duration"
+ "duration: %.2f"
+ "eStatus"
+ "effectiveDuration"
+ "effectiveDuration: %.2f"
+ "enableFeatureWithCompletion:"
+ "encodeDouble:forKey:"
+ "encodeInteger:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "endpoint:"
+ "entitlementsForPolicy:options:"
+ "environment"
+ "environment != nil"
+ "environment: %@"
+ "environmentProviderWithLocationProvider:featureController:ratchetStateProvider:lostModeController:"
+ "environmentUpdateDidFinish"
+ "environmentUpdateWillStart"
+ "errorWithCode:subcode:"
+ "errorWithCode:subcode:debugDescription:"
+ "evaluatePolicy:options:client:evaluationBlock:reply:"
+ "evaluationIdentifierForClient:ratchetIdentifier:"
+ "eventBus"
+ "featureController"
+ "featureState"
+ "featureState: %@"
+ "fetchAuthorizedLocationStatus:"
+ "fetchEnvironmentForPolicy:options:completion:"
+ "fetchLostMode:completion:"
+ "fetchStateWithCompletion:"
+ "handleEvent:sender:"
+ "handlesPolicy:options:"
+ "hasBeenUnlockedSinceBoot"
+ "hasBiometricEnrollmentsForCurrentUser"
+ "hasExpiredBiometry"
+ "hasExpiredBiometry: %@"
+ "hasHSA2Account"
+ "hasLocationServicesEnabled"
+ "hasNotifiedUserAboutCompletion"
+ "hasPasscodeSetForCurrentUser"
+ "identifier: %@"
+ "inFamiliarLocation"
+ "indexOfObjectPassingTest:"
+ "init()"
+ "initWithBiometryWatchdogGlobal:biometryWatchdogDTO:"
+ "initWithBoolValue:"
+ "initWithCoder:"
+ "initWithData:"
+ "initWithEndpointProvider:"
+ "initWithEnvironment:evaluationIdentifierFactory:device:"
+ "initWithFeatureController:ratchetStateProvider:pendingEvaluationController:"
+ "initWithIdentifier:"
+ "initWithIdentifier:body:deeplinkURL:"
+ "initWithIntegerValue:"
+ "initWithIsInFamiliarLocation:confirmed:"
+ "initWithIsInFamiliarLocation:confirmed:createdAt:"
+ "initWithIsInLostMode:"
+ "initWithIsInLostMode:confirmed:"
+ "initWithIsInLostMode:confirmed:createdAt:"
+ "initWithIsRunning:time:minThreshold:maxThreshold:"
+ "initWithKVStore:"
+ "initWithKVStore:device:workQueue:"
+ "initWithListenerEndpoint:"
+ "initWithLocationProvider:featureController:ratchetStateProvider:lostModeController:"
+ "initWithLocationProvider:store:workQueue:"
+ "initWithLostModeProvider:store:workQueue:"
+ "initWithNotificationCenter:"
+ "initWithPersistentStore:workQueue:"
+ "initWithPresenter:uiManager:"
+ "initWithRatchetState:watchdogs:"
+ "initWithRatchetStateProvider:ratchetHandler:evaluationIdentifierFactory:persistentStore:workQueue:"
+ "initWithRatchetStateProvider:workQueue:"
+ "initWithRawValue:"
+ "initWithRawValue:duration:resetDuration:uuid:"
+ "initWithRawValue:optionalValue:"
+ "initWithRawValue:value:"
+ "initWithUserDefaults:"
+ "initWithWorkQueue:"
+ "initWithWorkQueue:deviceInfo:"
+ "interfaceWithProtocol:"
+ "invalidate"
+ "isAvailable"
+ "isAvailable || error != nil"
+ "isAvailable: %@"
+ "isBarking"
+ "isDTOEnabled"
+ "isDTOEnabled: %@"
+ "isEnabled"
+ "isEnabled: %@"
+ "isEqualToDictionary:"
+ "isFeatureAvailable"
+ "isFeatureAvailable: NO (%{public}@)"
+ "isFeatureAvailable: YES"
+ "isFeatureEnabled"
+ "isFeatureEnabled: %s"
+ "isFeatureEnabled: NO (%{public}@)"
+ "isFeatureEnabled: NO (error: %{public}@)"
+ "isFeatureEnabled: YES"
+ "isFeatureSupported"
+ "isFeatureSupported: NO (%{public}@)"
+ "isFeatureSupported: YES"
+ "isInFamiliarLocation"
+ "isInLostMode"
+ "isInLostMode: %@"
+ "isInteractiveRatchetEvaluation"
+ "isNotificationScheduledForDate:"
+ "isPhone"
+ "isPresented"
+ "isRunning: %@"
+ "isSuccess"
+ "isSupported"
+ "isSupported: %@"
+ "isValid:"
+ "isValid: %@"
+ "loadPersistedEvaluationsWithCompletion:"
+ "loadWithCompletionHandler:"
+ "localizedStringFromDate:dateStyle:timeStyle:"
+ "locationProvider"
+ "locationState"
+ "locationStateBackgroundTask"
+ "locationStatusQueryDidFinish"
+ "locationStatusQueryWillStart"
+ "lock.open.fill"
+ "lostModeBackgroundTask"
+ "lostModeController"
+ "lostModeQueryDidFinish"
+ "lostModeQueryWillStart"
+ "lostModeStateWithCompletion:"
+ "makePersistentStoreWithUserDefaults:"
+ "maxAge"
+ "maxAge: %.2f"
+ "maxThreshold"
+ "maxThreshold: %.2f"
+ "minThreshold"
+ "minThreshold: %.2f"
+ "notificationManager"
+ "notificationScheduledAt"
+ "notificationScheduledAt: "
+ "now"
+ "numberFromString:"
+ "numberWithBool:"
+ "numberWithInteger:"
+ "objectAtIndex:"
+ "options"
+ "options: %@"
+ "pendingEvaluationController:updatedPendingEvaluation:"
+ "pendingEvaluationControllerDidStartTrackingPendingEvaluations:"
+ "pendingEvaluationControllerDidStopTrackingPendingEvaluations:"
+ "pendingEvaluationWithIdentifier:"
+ "pendingEvaluations"
+ "pendingEvaluationsDict"
+ "persistEvaluations"
+ "persistentDomainForName:"
+ "policy"
+ "policy: %@"
+ "policy: %d"
+ "policyController:didFinishPolicyEvaluation:result:"
+ "policyController:willStartPolicyEvaluation:"
+ "presentWithStyle:animated:completion:"
+ "presentationStyle"
+ "presenter"
+ "primaryAuthKitAccount"
+ "processInfo"
+ "q"
+ "ratchetState"
+ "ratchetState: %@"
+ "ratchetStateProvider"
+ "ratchetStateWithCompletion:"
+ "ratchetStateWithWatchdogsCompletion:"
+ "ratchetUUID"
+ "rawValue"
+ "rawValue: %@"
+ "reason"
+ "remoteObjectProxyWithErrorHandler:"
+ "removeEventHandler:"
+ "removeObjectForKey:"
+ "removeObjectForKey:completion:"
+ "removePendingEvaluationWith:"
+ "resetDuration"
+ "resetDuration: %.2f"
+ "resetRatchetWithCompletion:"
+ "result"
+ "result: %@"
+ "resume"
+ "scheduleSecurityDelayFinishedNotificationForPendingEvaluation:after:maxAge:completion:"
+ "securityDelayEnded"
+ "send"
+ "sendWithMessage:"
+ "setAltDSID:"
+ "setBiometryWatchdogPack:"
+ "setCallbackReason:"
+ "setCallbackURL:"
+ "setCoolOffStarted:"
+ "setData:ForKey:completion:"
+ "setEnvironment:"
+ "setError:"
+ "setEventBus:"
+ "setExpirationDate:"
+ "setFeatureState:"
+ "setFetchDeviceSafetyState:"
+ "setIdentifier:"
+ "setInFamiliarLocation:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setIsAvailable:"
+ "setIsDTOEnabled:"
+ "setIsEnabled:"
+ "setIsSupported:"
+ "setIsTimeSensitive:"
+ "setLocationState:"
+ "setLocationStateBackgroundTask:"
+ "setLostModeBackgroundTask:"
+ "setMaxAge:"
+ "setNotificationManager:"
+ "setNotificationScheduledAt:"
+ "setOptions:"
+ "setPolicy:"
+ "setRatchetState:"
+ "setRatchetUUID:"
+ "setRemoteObjectInterface:"
+ "setResult:"
+ "setSerialNumbers:"
+ "setSystemIconName:"
+ "setValue:forKey:completion:"
+ "setValue:forKey:connection:completion:"
+ "setValue:forKey:contextUUID:connection:completion:"
+ "setWorkQueue:"
+ "showCoolOffSheetWithOptions:presentationCompletion:sheetCompletion:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine"
+ "standardUserDefaults"
+ "startController"
+ "store"
+ "storeKey"
+ "supportsSecureCoding"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "time"
+ "time: %.2f"
+ "timeIntervalSince1970"
+ "timeIntervalSinceDate:"
+ "transitionToState:withOptions:completion:"
+ "uiManager"
+ "userDefaults"
+ "uuid"
+ "uuid: %@"
+ "v16@?0@\"<LACDTOFeatureState>\"8"
+ "v16@?0@\"<LACDTOPendingPolicyEvaluationControllerObserver>\"8"
+ "v16@?0@\"<LACDTOPolicyEvaluationControllerObserver>\"8"
+ "v16@?0@\"LACDTOLocationState\"8"
+ "v16@?0@\"LACDTOLostModeState\"8"
+ "v16@?0@\"NSDictionary\"8"
+ "v16@?0@\"NSHashTable\"8"
+ "v16@?0@\"NSMutableSet\"8"
+ "v16@?0@\"NSString\"8"
+ "v16@?0@?<v@?@\"LACBackgroundTaskResult\">8"
+ "v20@0:8B16"
+ "v20@?0B8@\"LACDTORatchetState\"12"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"<LACDTOEventBus>\"16"
+ "v24@0:8@\"<LACDTOPendingPolicyEvaluationController>\"16"
+ "v24@0:8@\"<LACDTOPendingPolicyEvaluationControllerObserver>\"16"
+ "v24@0:8@\"<LACDTOPolicyEvaluationControllerObserver>\"16"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@\"NSURL\"16"
+ "v24@0:8@\"_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation\"16"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"<LACDTOFeatureState>\">16"
+ "v24@0:8@?<v@?@\"LACDTOLocationState\">16"
+ "v24@0:8@?<v@?@\"LACDTOLostModeState\">16"
+ "v24@0:8@?<v@?@\"LACDTORatchetState\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"LACDTORatchetStateWithWatchdogs\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@0:8d16"
+ "v24@0:8q16"
+ "v24@?0@\"<LACDTOEnvironment>\"8@\"NSError\"16"
+ "v24@?0@\"AKDeviceListResponse\"8@\"NSError\"16"
+ "v24@?0@\"LACDTOKVStoreValue\"8@\"NSError\"16"
+ "v24@?0@\"LACDTOLostModeState\"8@\"NSError\"16"
+ "v24@?0@\"LACDTORatchetState\"8@\"NSError\"16"
+ "v24@?0@\"LACDTORatchetStateWithWatchdogs\"8@\"NSError\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v24@?0@\"RTAuthorizedLocationStatus\"8@\"NSError\"16"
+ "v32@0:8@\"<LACDTOLostModeFetchRequest>\"16@?<v@?@\"LACDTOLostModeState\">24"
+ "v32@0:8@\"<LACDTOPendingPolicyEvaluationController>\"16@\"<LACDTOPendingPolicyEvaluation>\"24"
+ "v32@0:8@\"<LACDTOPolicyEvaluationController>\"16@\"<LACDTOPolicyEvaluationRequest>\"24"
+ "v32@0:8@\"LACDTOEvent\"16@24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@?16@?24"
+ "v32@0:8q16@?24"
+ "v40@0:8@\"<LACDTOPolicyEvaluationController>\"16@\"<LACDTOPolicyEvaluationRequest>\"24@\"<LACDTOPolicyEvaluationResult>\"32"
+ "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24@?<v@?>32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16@?24@?32"
+ "v40@0:8@16d24d32"
+ "v40@0:8q16@\"NSDictionary\"24@?<v@?@\"<LACDTOEnvironment>\"@\"NSError\">32"
+ "v40@0:8q16@24@?32"
+ "v40@?0q8@\"NSDictionary\"16@\"<LACDTOPolicyEvaluationRequest>\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v44@0:8B16@20@28@?36"
+ "v48@0:8@\"<LACXPCClientInfo>\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
+ "v48@0:8@16d24d32@?40"
+ "v56@0:8@16q24@32@40@?48"
+ "v56@0:8q16@\"NSDictionary\"24@\"<LACXPCClientInfo>\"32@?<v@?q@\"NSDictionary\"@\"<LACDTOPolicyEvaluationRequest>\"@?<v@?@\"NSDictionary\"@\"NSError\">>40@?<v@?@\"NSDictionary\"@\"NSError\">48"
+ "v56@0:8q16@24@32@?40@?48"
+ "v64@0:8q16@24@32@40@?48@?56"
+ "valueForKey:completion:"
+ "valueForKey:connection:completion:"
+ "watchdogs"
+ "watchdogs: %@"
+ "workQueue"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "Request timed out"

```
