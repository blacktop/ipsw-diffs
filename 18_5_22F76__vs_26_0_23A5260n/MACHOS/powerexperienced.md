## powerexperienced

> `/usr/libexec/powerexperienced`

```diff

-57.100.8.0.0
-  __TEXT.__text: 0xcbc0
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_stubs: 0x1d20
-  __TEXT.__objc_methlist: 0x12d4
-  __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x831
-  __TEXT.__objc_methname: 0x22d9
-  __TEXT.__oslogstring: 0x1155
-  __TEXT.__objc_classname: 0x263
-  __TEXT.__objc_methtype: 0x659
+103.0.0.502.1
+  __TEXT.__text: 0x1596c
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_stubs: 0x2fa0
+  __TEXT.__objc_methlist: 0x1e34
+  __TEXT.__const: 0x128
+  __TEXT.__cstring: 0xece
+  __TEXT.__objc_methname: 0x3727
+  __TEXT.__oslogstring: 0x2153
+  __TEXT.__objc_classname: 0x3dd
+  __TEXT.__objc_methtype: 0x7db
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__dlopen_cstrs: 0x8d
-  __TEXT.__unwind_info: 0x388
-  __DATA_CONST.__auth_got: 0x358
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x5d0
-  __DATA_CONST.__cfstring: 0x7a0
-  __DATA_CONST.__objc_classlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x50
+  __TEXT.__unwind_info: 0x568
+  __DATA_CONST.__auth_got: 0x350
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__const: 0x820
+  __DATA_CONST.__cfstring: 0xec0
+  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2bf8
-  __DATA.__objc_selrefs: 0x9b0
-  __DATA.__objc_ivar: 0x11c
-  __DATA.__objc_data: 0x5a0
-  __DATA.__data: 0x3c0
-  __DATA.__bss: 0x170
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_intobj: 0x90
+  __DATA.__objc_const: 0x4908
+  __DATA.__objc_selrefs: 0xed8
+  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_data: 0x7d0
+  __DATA.__data: 0x600
+  __DATA.__bss: 0x204
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode
+  - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence
   - /System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7A87D316-18CC-3006-9631-3ACCD726AE36
-  Functions: 402
-  Symbols:   140
-  CStrings:  815
+  UUID: EA559D13-39D0-3A1C-91D9-BC0D8E081267
+  Functions: 687
+  Symbols:   160
+  CStrings:  1321
 
Symbols:
+ _AVSystemController_CallIsActiveDidChangeNotification
+ _AVSystemController_CallIsActiveNotificationParameter
+ _AVSystemController_SomeSessionIsPlayingDidChangeNotification
+ _AVSystemController_SomeSessionIsPlayingDidChangeNotificationParameter_Sessions
+ _AVSystemController_SubscribeToNotificationsAttribute
+ _IOPMAssertionCreateWithProperties
+ _IOPMAssertionRelease
+ _OBJC_CLASS_$_AVSystemController
+ _OBJC_CLASS_$_CMSuppressionEvent
+ _OBJC_CLASS_$_CMSuppressionManager
+ _OBJC_CLASS_$_ContextualPowerModesClient
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_PMPowerMitigationSession
+ _OBJC_CLASS_$__OSIBatteryLifeManager
+ _OBJC_CLASS_$__PMCoreSmartPowerNap
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ __dispatch_main_q
+ _kOSThermalNotificationPressureLevelName
+ _kPowerMitigationsManagerService
+ _kPowerMitigationsManagerServiceStartupNotify
- ___error
- _posix_spawn
- _strerror
CStrings:
+ "#!A"
+ "4!"
+ "@\"CMSuppressionManager\""
+ "@\"NSMutableSet\""
+ "@\"NSOperationQueue\""
+ "@\"PMPowerMitigationSession\""
+ "@\"SMCSensorExchangeHelper\""
+ "@\"_OSIBatteryLifeManager\""
+ "Accepted new connection from pid %d"
+ "ActiveWarmWorkload"
+ "AssertName"
+ "AssertType"
+ "Audio session ended"
+ "Audio session started"
+ "AudioSession"
+ "C"
+ "Charging, cooloff and early thermal warning. ChargingCoolOff"
+ "Charging, not in use and TP Light. ChargingTPLight"
+ "Charging, not in use and no TP. Default charging"
+ "ChargingCoolOff"
+ "ChargingWarm"
+ "Clearing defaults"
+ "Clearing state"
+ "ContextualPowerTargetsCallbackProtocol"
+ "ContextualPowerTargetsProtocol"
+ "Created power assertion with ID %u"
+ "Current systemWideLevel: %ld"
+ "Default"
+ "DefaultCharging"
+ "DefaultMode"
+ "Detected in pocket. Recording time"
+ "Detected not in pocket"
+ "Device facedown"
+ "Device facedown state unknown"
+ "Device has been unlocked since last boot. Restoring state"
+ "Device hasn't been unlocked since last boot. Clearing state"
+ "Device in pocket"
+ "Device in use and warm"
+ "Device not facedown"
+ "Device suppression"
+ "Device unknown suppression"
+ "Device unsuppress"
+ "Emergency charge"
+ "Error fetching initial OSIBLMitigationLevel %@"
+ "Evaluating mitigationLevel on new LPM state: %ld"
+ "Evaluating power targets for device context change %@"
+ "Evaluating systemWide mitigations"
+ "Failed to connect to service. Error: %@"
+ "Failed to create a power assertion 0x%x"
+ "Failed to register for AV System Controller notifications %@"
+ "Failed to register for LPM notifications"
+ "Failed to register for PS time remaining changes"
+ "Failed to register for early thermal warning"
+ "Failed to register for test defaults change"
+ "Failed to register for thermal warning"
+ "Failed to update CLPC with power target for workload %llu. Error: %@"
+ "Failed to update client"
+ "Failed to write SDSM key. Error 0x%x"
+ "Failed to write SMC key WAXC"
+ "FitnessIntelligenceWorkoutVoice"
+ "I"
+ "I16@0:8"
+ "IBLM"
+ "IBLM MitigationLevel has changed from: %ld to: %ld"
+ "IBLM MitigationLevel is unchanged. MitigationLevel: %ld"
+ "InBoxSoftwareUpdate"
+ "InBoxUpdateMode"
+ "InBoxUpdateMode not supported on this platform"
+ "InBoxUpdteMode"
+ "InPocketMonitor"
+ "InPocketMonitorDelegate"
+ "Init PowerTargetController"
+ "LPM"
+ "Mobile charger attached"
+ "Mobile charger detached"
+ "Mobile charger detached. Clearing policy"
+ "MobileCharger attached"
+ "MobileCharger detached"
+ "MobileChargingController"
+ "MobileChargingController not supported on this platform"
+ "MobileChargingScenarioActiveUse"
+ "MobileChargingScenarioBoost"
+ "MobileChargingScenarioEmergency"
+ "MobileChargingScenarioInPocketEmergency"
+ "MobileChargingScenarioInPocketNominal"
+ "MobileChargingScenarioNone"
+ "New mitigation %@"
+ "New systemWideMitigationLevel: %ld"
+ "No active mitigations"
+ "No change to systemWideMitigationLevel. Current Level: %ld"
+ "No trial experiments"
+ "OBCTopOff"
+ "Out of pocket active use"
+ "Out of pocket emergencyCharge %@, boostMode %@"
+ "PMPowerMitigationsServiceCallbackProtocol"
+ "PMPowerMitigationsServiceProtocol"
+ "Phone call ended"
+ "Phone call started"
+ "PhoneCall"
+ "PowerMitigationSession_Duration"
+ "PowerMitigationSession_Level"
+ "PowerMitigationSession_Reason"
+ "PowerMitigationSession_Source"
+ "PowerMitigationsManager"
+ "PowerTargetController"
+ "PowerTargetController not supported on this platform"
+ "PowerTargetControllerClient"
+ "PowerTargetControllerService"
+ "PowerTargetControllerService: listener: accepted new connection from pid %d"
+ "PowerTargetControllerService: listener: accpeted new connection from pid %d"
+ "PowerTargetControllerService: rejected new connection from pid %d. Not entitled"
+ "Prepickup"
+ "Received audio session notification %@"
+ "Received early thermal notification %@"
+ "Received new battery drain prediction: %@"
+ "Received phone call notification %@"
+ "Received suppression event %@"
+ "Registered for AV System Controller notifications"
+ "Registering PID: %d"
+ "Registering client %@"
+ "Registering for drain level prediction updates with BatteryLifeManager."
+ "RegulateBGTarget"
+ "RegulateEnable"
+ "RegulatePackagePowerTargetDefault"
+ "RegulatePackagePowerTargetWarm"
+ "RegulateUtilityTarget"
+ "Released power assertion with ID %u"
+ "Restoring mitigation %lu"
+ "Restoring state from defaults"
+ "Saving state to defaults"
+ "Sending mitigationLevel update to PID: %d"
+ "Setting ignoreUSBDeviceMode to %d"
+ "Setting timer to fire in %f to evaluate boost mode"
+ "SoftwareUpdateTask"
+ "System"
+ "T@\"CMSuppressionManager\",&,V_suppresionManager"
+ "T@\"NSDate\",&,V_attachTime"
+ "T@\"NSDate\",&,V_inPocketEndTime"
+ "T@\"NSDate\",&,V_inPocketStartTime"
+ "T@\"NSMutableSet\",&,N,V_activeModes"
+ "T@\"NSMutableSet\",&,V_clients"
+ "T@\"NSOperationQueue\",&,V_suppressionQueue"
+ "T@\"NSString\",&,V_currentMode"
+ "T@\"NSUserDefaults\",&,N,V_testDefaults"
+ "T@\"NSUserDefaults\",&,V_testDefaults"
+ "T@\"PMPowerMitigationSession\",&,V_powerMitigationSession"
+ "T@\"ResourceHint\",&,V_audioSessionResourceHint"
+ "T@\"ResourceHint\",&,V_legacyAudioResourceHint"
+ "T@\"ResourceHint\",&,V_phoneCallResourceHint"
+ "T@\"ResourceManager\",&,V_resourceManager"
+ "T@\"SMCSensorExchangeHelper\",&,N,V_smcHelper"
+ "T@\"SMCSensorExchangeHelper\",&,V_smcHelper"
+ "T@\"_OSIBatteryLifeManager\",&,V_batteryLifeManager"
+ "TB,N,V_appliesThermalPolicy"
+ "TB,V_enable"
+ "TB,V_experimentActive"
+ "TB,V_ignoreUSBDeviceMode"
+ "TB,V_inPocket"
+ "TB,V_isLPMActive"
+ "TB,V_mobileChargerAttached"
+ "TB,V_state"
+ "TB,V_supportedPlatform"
+ "TI,V_assertionID"
+ "TQ,V_chargingScenario"
+ "TQ,V_currentChargingOption"
+ "TQ,V_currentMitigation"
+ "TQ,V_currentPowerOption"
+ "TQ,V_option"
+ "TQ,V_prePickupCold"
+ "TQ,V_prePickupDefault"
+ "TQ,V_prePickupWarm"
+ "Td,V_boostModeMaxEngagement"
+ "Test defaults have changed"
+ "Tf,V_bgPowerTarget"
+ "Tf,V_utilityPowerTarget"
+ "TimeoutSeconds"
+ "Tq,V_iblmMitigationLevel"
+ "Trial ended, treatmentID %@, experimentID %@, deploymentID %d"
+ "Trial started. treatmentID %@, experimentID %@, deploymentID %d"
+ "Trial updated. treatmentID %@, experimentID %@, deploymentID %d"
+ "Trial:No trial value for CLPC tuning option. Resetting to default"
+ "Trial:No trial value for Regulate BG Power Target"
+ "Trial:No trial value for Regulate Default Power Target"
+ "Trial:No trial value for Regulate Utility Power Target"
+ "Trial:No trial value for Regulate Warm Power Target"
+ "Trial:No trial value for disabling Regulate"
+ "Trial:Regulate BG Power Target = %f"
+ "Trial:Regulate Enabled = %d"
+ "Trial:Regulate Package Power Target Default = %lld"
+ "Trial:Regulate Package Power Target Warm = %lld"
+ "Trial:Regulate Utility Power Target = %f"
+ "USBDeviceMode is active. Not applying any power budgets"
+ "UTF8String"
+ "Unable to update initial state for client %@"
+ "Updated CLPC with power target for workload %llu value %f"
+ "Updating CLPCInternal client RPC buffer size to 16k"
+ "Updating CLTM with mobile charging policy: %@, %f"
+ "Updating CLTM with thermal policy %@"
+ "Updating Inductive charging power policy %@"
+ "Updating from test context %@:%@"
+ "Updating mobile charging policy to sceanrio %@"
+ "Updating mobile charging policy: Charging %@, power %@"
+ "Updating thermal policy for %@"
+ "_PowerTargetControllerProtocolPrivate"
+ "_activeModes"
+ "_appliesThermalPolicy"
+ "_assertionID"
+ "_attachTime"
+ "_audioSessionResourceHint"
+ "_batteryLifeManager"
+ "_bgPowerTarget"
+ "_boostModeMaxEngagement"
+ "_chargingScenario"
+ "_currentChargingOption"
+ "_currentMitigation"
+ "_currentMode"
+ "_currentPowerOption"
+ "_enable"
+ "_experimentActive"
+ "_iblmMitigationLevel"
+ "_ignoreUSBDeviceMode"
+ "_inPocket"
+ "_inPocketEndTime"
+ "_inPocketStartTime"
+ "_isLPMActive"
+ "_legacyAudioResourceHint"
+ "_mobileChargerAttached"
+ "_option"
+ "_phoneCallResourceHint"
+ "_powerMitigationSession"
+ "_prePickupCold"
+ "_prePickupDefault"
+ "_prePickupWarm"
+ "_smcHelper"
+ "_suppresionManager"
+ "_suppressionQueue"
+ "_testDefaults"
+ "_utilityPowerTarget"
+ "activeModes"
+ "activeUse"
+ "addObserver:selector:name:object:"
+ "appliesThermalPolicy"
+ "arrayWithObjects:count:"
+ "assertionID"
+ "attachTime"
+ "audioSessionResourceHint"
+ "batteryData %llu"
+ "batteryLifeManager"
+ "bgPowerTarget"
+ "booleanValue"
+ "boostMode"
+ "boostModeEnagementDuration"
+ "boostModeMaxEngagement"
+ "chargingScenario"
+ "clearPolicy"
+ "com.apple.powerexperience.powertargetcontroller.update"
+ "com.apple.powerexperienced.powermitigationsmanager"
+ "com.apple.powerexperienced.powertargetcontroller"
+ "com.apple.powerexperienced.powertargetcontrollerservice"
+ "com.apple.powerexperienced.test.devicecontext"
+ "com.apple.powerexperienced.test.mobilecharingcontroller"
+ "com.apple.powerexperienced.testdevicecontext.changed"
+ "com.apple.powerexperienced.testmobilechargingcontroller.changed"
+ "com.apple.system.earlythermalnotification"
+ "com.apple.system.lowpowermode"
+ "com.apple.system.powersources.timeremaining"
+ "count"
+ "currentChargingOption"
+ "currentMitigation"
+ "currentMode"
+ "currentPowerOption"
+ "defaultCenter"
+ "deploymentId"
+ "devicecontext"
+ "didTrialEnd:"
+ "didTrialStart:"
+ "didTrialUpdate:"
+ "didUpdateToMitigation:fromMitigation:"
+ "doubleValue"
+ "emergencyCharge"
+ "enable"
+ "engagementReason"
+ "evaluateChargingPolicy"
+ "evaluateChargingPolicy at the end of boost mode"
+ "evaluateMitigations"
+ "evaluatePowerController"
+ "evaluatePowerMode: %@: %d display %d, carPlaySession %d, nFCSession %d, audioSession %d, sleepInProgress %d, wakeInProgress %d, onenessSession %d, siriAudio %d, fitnessIntelligence %d, pluggedIn %d (allowOnCharger: %d)"
+ "evaluatePowerTargets"
+ "experimentActive"
+ "experimentId"
+ "experimentIdentifier %@"
+ "f"
+ "f16@0:8"
+ "facedownState"
+ "handleAudioSessionNotification:"
+ "handleEarlyThermalWarning"
+ "handleLPMStateChange"
+ "handleMobileChargerStatus"
+ "handlePhoneCallNotification:"
+ "handleTestDefaultsChange"
+ "handleTestDefaultsUpdate"
+ "handleThermalWarning"
+ "handleUpdatedDrainLevelPrediction:"
+ "iblmMitigationLevel"
+ "ignoreUSBDeviceMode"
+ "inPocket"
+ "inPocketEndTime"
+ "inPocketStartTime"
+ "inPocketStateHasChanged:"
+ "initAVSystemControllerNotifications"
+ "initCSPNNotifications"
+ "initEarlyThermalWarning"
+ "initLowPowerModeChange"
+ "initPSTimeRemainingChange"
+ "initPocketDetection"
+ "initTestDefaultsChange"
+ "initThermalWarning"
+ "initWithClientType:"
+ "initWithConnection:identifier:"
+ "initWithSource:reason:level:duration:"
+ "initialStateUpdateForClient:"
+ "inpocketmonitor"
+ "instancesRespondToSelector:"
+ "integerValue"
+ "isActiveWarm"
+ "isChargingCoolOff"
+ "isChargingTPLite"
+ "isDefaultCharging"
+ "isDeviceInUse"
+ "isLPMActive"
+ "isOBCTopOff"
+ "kCSPNStateContext"
+ "kEarlyThermalContext"
+ "kInPocketContext"
+ "kLPMStateStateContext"
+ "kMobileChargerContext"
+ "kThermalPressureContext"
+ "legacyAudioResourceHint"
+ "level"
+ "mitigation"
+ "mitigationDescription"
+ "mitigationWithError:"
+ "mobileChargerAttached"
+ "mobilechargingcontroller"
+ "now"
+ "numberWithDouble:"
+ "numberWithInteger:"
+ "option"
+ "phoneCallResourceHint"
+ "powerMitigationSession"
+ "powermitigationsmanager"
+ "powertargetcontroller"
+ "powertargetcontrollerservice"
+ "prePickupCold"
+ "prePickupDefault"
+ "prePickupWarm"
+ "q"
+ "q16@0:8"
+ "recordMobileChargerAttach"
+ "registerForDrainLevelPredictionForClient:withithUpdateHandler:"
+ "registerForDrainLevelPredictions"
+ "registerForPowerMitigations"
+ "registerForTestDefaultsChange"
+ "registerWithCallback:callback:"
+ "registerWithIdentifier:"
+ "registerWithIdentifier:queue:callback:"
+ "removeMitigations"
+ "removeObject:"
+ "sessionSource"
+ "setActiveModes:"
+ "setAppliesThermalPolicy:"
+ "setAssertionID:"
+ "setAttachTime:"
+ "setAttribute:forKey:error:"
+ "setAudioSessionResourceHint:"
+ "setBatteryLifeManager:"
+ "setBgPowerTarget:"
+ "setBoostModeMaxEngagement:"
+ "setChargingScenario:"
+ "setCurrentChargingOption:"
+ "setCurrentMitigation:"
+ "setCurrentMode:"
+ "setCurrentPowerOption:"
+ "setDefaultTargets"
+ "setEnable:"
+ "setExperimentActive:"
+ "setIblmMitigationLevel:"
+ "setIgnoreUSBDeviceMode:"
+ "setInPocket:"
+ "setInPocketEndTime:"
+ "setInPocketStartTime:"
+ "setIsLPMActive:"
+ "setLegacyAudioResourceHint:"
+ "setMaxConcurrentOperationCount:"
+ "setMobileChargerAttached:"
+ "setOption:"
+ "setPhoneCallResourceHint:"
+ "setPowerBudgetForWorkload:value:"
+ "setPowerMitigationSession:"
+ "setPrePickupCold:"
+ "setPrePickupDefault:"
+ "setPrePickupWarm:"
+ "setSmcHelper:"
+ "setSuppresionManager:"
+ "setSuppressionQueue:"
+ "setTestDefaults:"
+ "setUnderlyingQueue:"
+ "setUtilityPowerTarget:"
+ "setWorkloadPowerBudget:options:error:"
+ "sharedAVSystemController"
+ "shouldOverrideCPMMode"
+ "shouldRestoreState"
+ "smcHelper"
+ "startMonitoring"
+ "startSuppressionUpdatesToQueue:withOptions:withHandler:"
+ "suppresionManager"
+ "suppressionQueue"
+ "systemWideMitigationLevel"
+ "test defaults have changed"
+ "testDefaults"
+ "timeDuration"
+ "timeSinceAttach %f "
+ "treatmentId"
+ "unsignedLongValue"
+ "updateBGUtilityPowerTargets:"
+ "updateCLTMMobileChargingPolicy:"
+ "updateCLTMThermalPolicy:"
+ "updateChargingPolicyWithTemperature:andPower:"
+ "updateClients"
+ "updateClients:andLevel:"
+ "updateClientsWithNewMitigations:fromMitigations:"
+ "updateDelegates:"
+ "updateIgnoreUSBDeviceMode:withReply:"
+ "updateInductiveChargingPowerPolicy:"
+ "updatePackagePowerTargets:options:"
+ "updatePowerAssertion"
+ "updatePowerTargetForMode:withState:andOptions:"
+ "updateState:andLevel:"
+ "updateThermalPolicy"
+ "userInfo"
+ "utilityPowerTarget"
+ "v12@?0C8"
+ "v16@?0@\"_OSIBLMitigation\"8"
+ "v20@0:8I16"
+ "v20@0:8f16"
+ "v20@?0B8@\"NSString\"12"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8q16"
+ "v24@?0@\"CMSuppressionEvent\"8@\"NSError\"16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?B>20"
+ "v28@0:8B16Q20"
+ "v28@0:8Q16f24"
+ "v32@0:8@\"PMPowerMitigationSession\"16@\"PMPowerMitigationSession\"24"
+ "v32@0:8Q16Q24"
+ "v36@0:8@16B24Q28"
- "/usr/local/bin/clpcctrl"
- "Error setting lower HiP target %s"
- "ReducedHiPTarget"
- "T@\"ResourceHint\",&,V_audioResourceHint"
- "Trial experiment status. treatmentID %@, rolloutID %@, experimentID %@"
- "Trial:No trial value for CLPC tuning option"
- "Updating CLPC with power target 400mW for HiP"
- "Updating CLPCInternal client RPC buffer size tp 16k"
- "_audioResourceHint"
- "audioResourceHint"
- "evaluatePowerMode: %@: %d display %d, carPlaySession %d, nFCSession %d, audioSession %d, sleepInProgress %d, wakeInProgress %d, onenessSession %d, siriAudio %d, pluggedIn %d (allowOnCharger: %d)"
- "pkg-hip-static-power-target=0.4"
- "rolloutIdentifiersWithNamespaceName:"
- "setAudioResourceHint:"
- "treatmentIdWithNamespaceName:"

```
