## ospredictiond

> `/usr/libexec/ospredictiond`

```diff

-234.120.3.0.0
-  __TEXT.__text: 0x63354
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_stubs: 0x8c60
-  __TEXT.__objc_methlist: 0x8aa0
-  __TEXT.__const: 0x308
-  __TEXT.__cstring: 0x4c1a
-  __TEXT.__objc_methname: 0x14054
-  __TEXT.__oslogstring: 0x5a68
-  __TEXT.__objc_classname: 0xd51
-  __TEXT.__objc_methtype: 0x232b
-  __TEXT.__gcc_except_tab: 0x9a8
-  __TEXT.__unwind_info: 0x16d8
-  __DATA_CONST.__auth_got: 0x408
-  __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__const: 0xf58
-  __DATA_CONST.__cfstring: 0x59e0
-  __DATA_CONST.__objc_classlist: 0x3b0
+269.0.0.0.0
+  __TEXT.__text: 0x65cec
+  __TEXT.__auth_stubs: 0x960
+  __TEXT.__objc_stubs: 0x9440
+  __TEXT.__objc_methlist: 0x9158
+  __TEXT.__const: 0x448
+  __TEXT.__cstring: 0x5424
+  __TEXT.__objc_methname: 0x14d53
+  __TEXT.__oslogstring: 0x6d52
+  __TEXT.__objc_classname: 0xdd8
+  __TEXT.__objc_methtype: 0x23b5
+  __TEXT.__gcc_except_tab: 0x86c
+  __TEXT.__ustring: 0x2a
+  __TEXT.__unwind_info: 0x1448
+  __DATA_CONST.__const: 0x10f0
+  __DATA_CONST.__cfstring: 0x6160
+  __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x330
-  __DATA_CONST.__objc_intobj: 0x210
-  __DATA_CONST.__objc_arraydata: 0x13a8
-  __DATA_CONST.__objc_dictobj: 0x140
-  __DATA_CONST.__objc_arrayobj: 0x438
-  __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0xf830
-  __DATA.__objc_selrefs: 0x3910
-  __DATA.__objc_ivar: 0xd20
-  __DATA.__objc_data: 0x24e0
+  __DATA_CONST.__objc_superrefs: 0x368
+  __DATA_CONST.__objc_intobj: 0x270
+  __DATA_CONST.__objc_arraydata: 0x13f0
+  __DATA_CONST.__objc_dictobj: 0x190
+  __DATA_CONST.__objc_arrayobj: 0x480
+  __DATA_CONST.__objc_doubleobj: 0x70
+  __DATA_CONST.__auth_got: 0x4c0
+  __DATA_CONST.__got: 0x410
+  __DATA.__objc_const: 0x10400
+  __DATA.__objc_selrefs: 0x3bf0
+  __DATA.__objc_ivar: 0xdac
+  __DATA.__objc_data: 0x2760
   __DATA.__data: 0x720
-  __DATA.__bss: 0x1a0
+  __DATA.__bss: 0x1c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9BA4545D-3487-3536-9AE3-98BF7441245A
-  Functions: 3085
-  Symbols:   255
-  CStrings:  5258
+  UUID: 5CC7C1EA-F026-3743-BCFB-C46C1B257A79
+  Functions: 3269
+  Symbols:   287
+  CStrings:  5651
 
Symbols:
+ _CFArrayGetCount
+ _CFArrayGetTypeID
+ _CFArrayGetValueAtIndex
+ _CFDictionaryGetTypeID
+ _CFDictionaryGetValue
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _CFRelease
+ _IOPMGetUserActivityLevel
+ _MGCopyAnswer
+ _MKBDeviceFormattedForContentProtection
+ _MKBDeviceUnlockedSinceBoot
+ _MLModelVersionStringKey
+ _NSFileProtectionComplete
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
+ _NSFileProtectionNone
+ _OBJC_CLASS_$_CPMSStateReader
+ _OBJC_CLASS_$_RadiosPreferences
+ _OBJC_CLASS_$__CDContextualChangeRegistration
+ _OBJC_CLASS_$__CDContextualPredicate
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _kCFBooleanTrue
+ _notify_register_check
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
- _OBJC_CLASS_$__OSDataProtectionStateMonitor
CStrings:
+ "%@%ld"
+ "(nil, will use bundle model)"
+ "/System/Library/PrivateFrameworks/OSIntelligence.framework/assets_COREOS_PREDICTION_INACTIVITY/engageModel_iPad"
+ "@\"MLMultiArray\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@\"NSUUID\""
+ "@\"OSChargingWatchPredictor\""
+ "@\"_OSDataProtectionManager\""
+ "@24@0:8@?16"
+ "@?"
+ "@?16@0:8"
+ "AbsoluteCapacity"
+ "Active_display: %.1f (activityLevel: %llu)"
+ "AlgoTemperature (°C)"
+ "Battery power consumption data not available"
+ "Battery telemetry snapshot: %@"
+ "Battery temperature value not available in Pmax state"
+ "Battery temperature: %.2f °C"
+ "BatteryData"
+ "Built activity history from lock data: %lu active intervals from %lu unlock events"
+ "COREOS_PREDICTION_TTE"
+ "CPMS Pmax state check: error code = %d, state available = %@"
+ "CPMS snapshot timestamp: %@"
+ "CPMSPPMBatteryPowerConsumptionPMU10s: %u mW"
+ "Could not load hybrid_model.mlmodelc in the bundle resource"
+ "Created TTE input features with %ld resampled bins (padded to %lu)"
+ "Current battery level for snapshot: %.2f%%"
+ "CycleCount"
+ "Debug: overriding drain predictor mode from %ld to %ld"
+ "DesignCapacity"
+ "Dispatching engage-only inchworm prediction at %@, timeSinceInactive=%.0fs"
+ "Error creating TTE feature provider: %@"
+ "Error creating TTE temporal features array: %@"
+ "Error creating input features for TTE model"
+ "Error creating static features array: %@"
+ "Error loading TTE model: %@"
+ "Error running TTE model prediction: %@"
+ "Failed to create TTE input features"
+ "Failed to get CPMS Pmax state: %d"
+ "Got %lu CPMS control state snapshots"
+ "Heuristic: SoC %ld%% <= threshold %ld%%, returning threshold crossed (shadow=%d, loggingID=%ld)"
+ "IOPMGetUserActivityLevel failed: 0x%08x, defaulting Active_display to 0.0"
+ "Invalid TTE model output"
+ "Invalid output feature from TTE model"
+ "Loaded %lu telemetry snapshots from ring buffer"
+ "NO"
+ "No CPMS control state snapshots available"
+ "No ring buffer metadata found — no telemetry snapshots"
+ "NominalChargeCapacity"
+ "OSITTESnapshotBatteryThreshold"
+ "OSIntelligence framework bundle not loaded, using hardcoded path"
+ "PasswordConfigured"
+ "PasswordProtected"
+ "Persisted telemetry snapshot to slot %@. writeIndex=%ld, count=%ld"
+ "PowerUI"
+ "Qmax"
+ "Reading metadata from iPad engage model"
+ "Ring buffer count is 0 — no telemetry snapshots"
+ "SELF.%@.value.externalConnected = %@ AND SELF.%@.value <= %@"
+ "Static TTE V4 feature - NCCP: %.4f (NCC=%ld, DesignCap=%ld)"
+ "Static TTE V4 feature - WeightedRa: %.1f mOhm"
+ "Static TTE feature - airplaneMode: %d"
+ "Static TTE feature - batteryLevel: %.2f%%"
+ "Static TTE feature - cycleCount: %ld"
+ "Static TTE feature - designCapacity: %ld"
+ "Static TTE feature - gameMode: %d (notify result: %d, state: %llu)"
+ "Static TTE feature - lowPowerMode: %d"
+ "Static TTE feature - sysCap2_cpms: %u"
+ "Static TTE features collected: %@"
+ "System capability data not available"
+ "T@\"MLModel\",&,N,V_trialModel"
+ "T@\"MLMultiArray\",&,N,V_static_features"
+ "T@\"MLMultiArray\",&,N,V_temporal_features"
+ "T@\"MLMultiArray\",&,N,V_var_80"
+ "T@\"NSMutableDictionary\",R,N,V_availableState"
+ "T@\"NSMutableDictionary\",R,N,V_handlers"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_notifyQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_stateQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_snapshotTimer"
+ "T@\"NSString\",&,N,V_trialModelPath"
+ "T@\"NSUUID\",R,N,V_handlerUUID"
+ "T@\"OSChargingWatchPredictor\",&,N,V_predictor"
+ "T@\"_OSDataProtectionManager\",R,N,V_manager"
+ "T@?,C,N,V_changeHandler"
+ "TB,N,V_isEngageOnly"
+ "TB,N,V_isShadowEvaluation"
+ "TB,N,V_snapshotCollectionActive"
+ "TB,R,N,V_deviceFormatedForContentProtection"
+ "TB,R,N,V_notifyEnabled"
+ "TTE low battery warning: about to send to queue"
+ "TTE low battery warning: logit=%.4f, P(TTE<10min)=%.4f"
+ "TTE model logging ID: %ld"
+ "TTE model raw output: %@"
+ "TTE model version: %@"
+ "TTE resample: forward-filled bin %lu"
+ "TTE resample: produced %lu bins from %lu raw snapshots (trimmed %lu leading empty bins)"
+ "TTE temporal bin[%ld]: temp=%.2f, power=%.2f, display=%.2f, batLevel=%.2f"
+ "TTE: Deleted telemetry snapshot history (ring buffer cleared)"
+ "TTE: Restored ring buffer state: writeIndex=%ld, count=%ld"
+ "TTE: Snapshot battery threshold set to %ld%%"
+ "TTE: Started dispatch timer with %.0fs interval"
+ "TTE: Stopped snapshot collection (conditions no longer met)"
+ "TTE: Stopped snapshot collection and cleared history"
+ "TTE: UI SoC = %ld%%, heuristic threshold = %ld%%"
+ "TTE: about to get features"
+ "TTE: features loaded"
+ "TTE: got %lu raw snapshots"
+ "TTE: got %lu resampled bins"
+ "TTE: got static features"
+ "TTE: model loaded"
+ "TTE: on queue start"
+ "TTE: socChangeCallback - UI SoC: %ld%%, externalConnected: %d, shouldCollect: %d"
+ "TTE_HeuristicSoCThreshold"
+ "TTE_IsShadowEvaluation"
+ "TTE_Model"
+ "Ti,N,V_gameConsoleModeToken"
+ "Ti,R,N,V_notifyToken"
+ "Tq,N,V_heuristicSoCThreshold"
+ "Tq,N,V_mode"
+ "Tq,N,V_snapshotBatteryThreshold"
+ "Tq,N,V_snapshotCount"
+ "Tq,N,V_writeIndex"
+ "Trial: %{public}@:%d"
+ "Trial: %{public}@:%ld"
+ "Trial: %{public}@:%{public}@"
+ "Trial: failed to compile TTE model from %{public}@: %@"
+ "Trial: failed to get level for %{public}@, defaulting to 1"
+ "Trial: failed to get level for %{public}@, defaulting to NO"
+ "Trial: failed to load compiled TTE model: %@"
+ "Trial: loading TTE model on demand from %{public}@"
+ "Triggering socChangeCallback"
+ "Triggering timeTillDischargeWithError"
+ "UI SoC for snapshot: %ld%%"
+ "Unknown drain predictor mode: %ld"
+ "WeightedRa"
+ "YES"
+ "_OSDataProtectionManager"
+ "_OSDataProtectionStateMonitor"
+ "_OSLockDerivedActivityHistory"
+ "_OSTTESnapshotCollector"
+ "_OSWatchInactivityPredictor"
+ "_availableState"
+ "_changeHandler"
+ "_deviceFormatedForContentProtection"
+ "_gameConsoleModeToken"
+ "_handlerUUID"
+ "_handlers"
+ "_heuristicSoCThreshold"
+ "_isEngageOnly"
+ "_isShadowEvaluation"
+ "_manager"
+ "_mode"
+ "_notifyEnabled"
+ "_notifyQueue"
+ "_snapshotBatteryThreshold"
+ "_snapshotCollectionActive"
+ "_snapshotCount"
+ "_snapshotTimer"
+ "_stateQueue"
+ "_static_features"
+ "_temporal_features"
+ "_trialModel"
+ "_trialModelPath"
+ "_var_80"
+ "_writeIndex"
+ "absoluteBatteryLevel"
+ "absoluteBatteryLevel: AbsoluteCapacity is not a CFNumber"
+ "absoluteBatteryLevel: AbsoluteCapacity not found"
+ "absoluteBatteryLevel: BatteryData is not a CFDictionary"
+ "absoluteBatteryLevel: BatteryData not found"
+ "absoluteBatteryLevel: Failed to create properties dictionary"
+ "absoluteBatteryLevel: Failed to get IOPMPowerSource"
+ "absoluteBatteryLevel: First element of Qmax array is not a CFNumber"
+ "absoluteBatteryLevel: Invalid values - current=%d, max=%d"
+ "absoluteBatteryLevel: Qmax array is empty"
+ "absoluteBatteryLevel: Qmax has unexpected type (typeID=%ld)"
+ "absoluteBatteryLevel: Qmax not found in BatteryData"
+ "absoluteLevel"
+ "activeDisplayState"
+ "activityHistoryFromLockHistory"
+ "airplaneMode"
+ "allValues"
+ "applyShadowMetadataToResult:"
+ "assets_COREOS_PREDICTION_INACTIVITY/engageModel_iPad"
+ "availableState"
+ "battery.tte"
+ "batteryLevel"
+ "batteryPowerConsumption"
+ "batteryPowerConsumption10s"
+ "batteryTemperature"
+ "bundlePath"
+ "bundleWithIdentifier:"
+ "changeHandler"
+ "chunk_engage_duration"
+ "client"
+ "collectAndPersistSnapshot"
+ "collectStaticTTEFeatures"
+ "com.apple.DuetActivityScheduler.DataProtection.notify"
+ "com.apple.DuetActivityScheduler.DataProtection.state"
+ "com.apple.OSIntelligence.WatchInactivityPredictor"
+ "com.apple.mobile.keybagd.lock_status"
+ "com.apple.osintelligence.battery.pluginChange"
+ "com.apple.osintelligence.battery.queue"
+ "com.apple.osintelligence.battery.socChange"
+ "com.apple.osintelligence.drainPredictor.setMode"
+ "com.apple.osintelligence.inactivity.watchInactivityPredictor"
+ "com.apple.osintelligence.inactivityprediction.twostage.inchworm"
+ "com.apple.osintelligence.inactivityprediction.watchInactivityPredictor"
+ "com.apple.osintelligence.lowBatteryWarning"
+ "com.apple.osintelligence.socChangeCallback"
+ "com.apple.osintelligence.testTTE"
+ "com.apple.osintelligence.tte"
+ "com.apple.system.console.mode.changed"
+ "copyCPMSControlStateSnapshots"
+ "copyCPMSPmaxState:"
+ "cycleCount"
+ "dataProtectionClassA"
+ "dataProtectionClassD"
+ "deleteSnapshotHistory"
+ "deregisterStateChangeHandler:"
+ "designCapacity"
+ "deviceFormatedForContentProtection"
+ "deviceHasBeenUnlockedSinceBoot"
+ "deviceIsLocked"
+ "deviceIsPasswordConfigured"
+ "engageOnlyInchwormPredictionAtDate:withTimeSinceInactive:withOptions:withError:"
+ "featureValueWithMultiArray:"
+ "gameConsoleModeToken"
+ "gameMode"
+ "getTTEInputFeatures"
+ "handleKeyBagLockNotification"
+ "handleSnapshotTimerFire"
+ "handlerUUID"
+ "handlers"
+ "hasEnoughHistoryForIPadInactivityPrediction"
+ "heuristicSoCThreshold"
+ "hybrid_model"
+ "hybrid_modelInput"
+ "hybrid_modelOutput"
+ "iPad chunk %lu features (%u): %{public}@"
+ "iPad chunk %lu: confidence=%.3f, level=%ld, duration=%.2fh"
+ "iPad does not have enough history yet for iPad predictor."
+ "iPad engage model error at chunk %lu: %@"
+ "iPad engage model failed to load; cannot read metadata"
+ "iPad engage model not found at %{public}@, falling back to framework bundle at %{public}@"
+ "iPad engage-only mode: chunkEngageDuration=%.0f sec, maxChunks=%lu, recommendedWaitTime=%.0f sec"
+ "iPad inchworm starting: model=%@, chunks=%lu, chunkDuration=%.0fs, features=%lu, activityIntervals=%lu, waitedTime=%.0fs"
+ "iPad inchworm stopping at chunk %lu: confidence below high threshold"
+ "iPad inchworm total: duration=%.2fh, confidence=%.3f"
+ "iPad two-stage mode: recommendedWaitTime=%.0f sec"
+ "iPad user has recently traveled; using the rule-based model."
+ "iPad using default two stage ML model (feature disabled or enough iPhone-level history)."
+ "iPad with enough history; using iPad predictor path."
+ "inactivity.watchInactivityPredictor"
+ "initWithTemporal_features:static_features:"
+ "initWithVar_80:"
+ "isDataAvailableForClassA"
+ "isDataAvailableForClassC"
+ "isEngageOnly"
+ "isShadowEvaluation"
+ "keyPathForLowPowerModeStatus"
+ "loadTelemetrySnapshots"
+ "localWakingRegistrationWithIdentifier:contextualPredicate:clientIdentifier:callback:"
+ "lowBatteryWarningWithError:"
+ "lowPowerMode"
+ "manager"
+ "max_chunks"
+ "modelLoggingID"
+ "model_logging_id"
+ "nccpRatio"
+ "nil engage model"
+ "notifyEnabled"
+ "notifyQueue"
+ "numberWithUnsignedInt:"
+ "obc_watch_engage_and_duration"
+ "persistTelemetrySnapshot:"
+ "predicateForChangeAtKeyPath:"
+ "predicateForKeyPath:withFormat:"
+ "predictionFromTemporal_features:static_features:error:"
+ "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "registerCallback:"
+ "registerStateChangeHandler:"
+ "requires_duration_model"
+ "resampleSnapshotsTo3MinBins:"
+ "runtimeWarning"
+ "setGameConsoleModeToken:"
+ "setHeuristicSoCThreshold:"
+ "setIsEngageOnly:"
+ "setIsShadowEvaluation:"
+ "setIsShadowModel:"
+ "setLowBatteryProbability:"
+ "setLowBatteryWarningThresholdCrossed:"
+ "setMode:"
+ "setModelID:"
+ "setModelLoggingID:"
+ "setSnapshotBatteryThreshold:"
+ "setSnapshotCollectionActive:"
+ "setSnapshotCount:"
+ "setSnapshotTimer:"
+ "setStatic_features:"
+ "setTemporal_features:"
+ "setTrialModel:"
+ "setTrialModelPath:"
+ "setUpBatteryMonitoring"
+ "setVar_80:"
+ "setWriteIndex:"
+ "shape"
+ "snapshotBatteryLevel"
+ "snapshotBatteryThreshold"
+ "snapshotCollectionActive"
+ "snapshotCount"
+ "snapshotTimer"
+ "socChangeCallback"
+ "stateQueue"
+ "static_features"
+ "sysCap2_cpms (1s capability): %u mW"
+ "systemCapability"
+ "systemCapability1s"
+ "temporal_features"
+ "timeTillDischargeV1WithError:"
+ "trialModel"
+ "trialModelPath"
+ "tteRingBufferCount"
+ "tteRingBufferWriteIndex"
+ "tteSnapshot_"
+ "type"
+ "unnotifiedIsDataAvailableForClassC"
+ "updateSnapshotTimerIfNeeded:"
+ "v24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "var_80"
+ "weightedRa"
+ "writeIndex"
- "Low SOC prediction is currently not supported!"
- "Reading metadata from loaded models"
- "iPad engage model not found at %{public}@, falling back to Trial default"
- "iPad using default two stage ML model (feature disabled)."
- "iPad with CoreSmartPowerNapIPad enabled; using iPad predictor path."

```
