## dasd

> `/usr/libexec/dasd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`

```diff

-2467.60.9.0.0
-  __TEXT.__text: 0x17aeb4
-  __TEXT.__auth_stubs: 0x2290
-  __TEXT.__objc_stubs: 0x1be80
-  __TEXT.__objc_methlist: 0x13acc
-  __TEXT.__const: 0x1588
-  __TEXT.__objc_methname: 0x2fe45
-  __TEXT.__cstring: 0x10d86
-  __TEXT.__oslogstring: 0x17719
-  __TEXT.__objc_classname: 0x1d88
-  __TEXT.__objc_methtype: 0x4531
-  __TEXT.__gcc_except_tab: 0x50c4
-  __TEXT.__dlopen_cstrs: 0x552
+2467.60.20.0.0
+  __TEXT.__text: 0x181b30
+  __TEXT.__auth_stubs: 0x22a0
+  __TEXT.__objc_stubs: 0x1c9e0
+  __TEXT.__objc_methlist: 0x1427c
+  __TEXT.__const: 0x15c8
+  __TEXT.__objc_methname: 0x3101d
+  __TEXT.__cstring: 0x11376
+  __TEXT.__oslogstring: 0x17f69
+  __TEXT.__objc_classname: 0x1e28
+  __TEXT.__objc_methtype: 0x4691
+  __TEXT.__gcc_except_tab: 0x5330
+  __TEXT.__dlopen_cstrs: 0x602
   __TEXT.__swift5_typeref: 0x966
   __TEXT.__swift5_capture: 0x220
   __TEXT.__swift5_fieldmd: 0x44c

   __TEXT.__swift_as_cont: 0x80
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x6740
+  __TEXT.__unwind_info: 0x6970
   __TEXT.__eh_frame: 0xbd0
-  __DATA_CONST.__const: 0x50f8
-  __DATA_CONST.__cfstring: 0x12220
-  __DATA_CONST.__objc_classlist: 0x728
+  __DATA_CONST.__const: 0x5230
+  __DATA_CONST.__cfstring: 0x12820
+  __DATA_CONST.__objc_classlist: 0x750
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x5d8
-  __DATA_CONST.__objc_intobj: 0x17d0
+  __DATA_CONST.__objc_superrefs: 0x600
+  __DATA_CONST.__objc_intobj: 0x17e8
   __DATA_CONST.__objc_arraydata: 0x4f8
   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA_CONST.__auth_got: 0x1158
-  __DATA_CONST.__got: 0xe50
+  __DATA_CONST.__auth_got: 0x1160
+  __DATA_CONST.__got: 0xe60
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x35138
-  __DATA.__objc_selrefs: 0xa188
-  __DATA.__objc_ivar: 0x16f8
-  __DATA.__objc_data: 0x4a48
-  __DATA.__data: 0x2390
+  __DATA.__objc_const: 0x36658
+  __DATA.__objc_selrefs: 0xa560
+  __DATA.__objc_ivar: 0x17c8
+  __DATA.__objc_data: 0x4bd8
+  __DATA.__data: 0x2410
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8582
-  Symbols:   1024
-  CStrings:  12821
+  Functions: 8779
+  Symbols:   1027
+  CStrings:  13130
 
Symbols:
+ _NSCocoaErrorDomain
+ _NSURLIsExcludedFromBackupKey
+ _memchr
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
CStrings:
+ "/System/Library/DuetActivityScheduler/Scheduler/Resources/com.apple.dasd.taskAppMap.plist"
+ "@\"BIThermalPredictionClient\""
+ "@\"PowerUISmartChargeClient\""
+ "@\"_DASClientMetricsRecorder\""
+ "@\"_DASPersonalizedSchedulingMetrics\""
+ "App usage priorities v%lu accepted (previous %{public}@): %lu entries, %lu high, %lu low, %lu skipped, unchanged %{BOOL}d"
+ "App usage priorities v%lu rejected (%{public}@ v%lu, age %.0fs): %lu entries"
+ "App usage priorities v%lu rejected (%{public}@): %lu entries"
+ "Apps"
+ "B16@?0@8"
+ "B48@0:8@16Q24@32^@40"
+ "BIThermalPredictionClient"
+ "BIThermalPredictionDelegate"
+ "BIThermalPredictionErrorDomain"
+ "BatteryIntelligence unavailable; TLC prediction mitigations are off"
+ "Charge limit changed %ld -> %ld"
+ "Failed to exclude app usage priorities from backup: %@"
+ "Failed to persist app usage priorities: %@"
+ "Failed to persist personalized scheduling metrics: %@"
+ "Failed to report %{public}@ to TaskThroughput"
+ "FreezerModeliPad"
+ "Holds discretionary and intensive tasks while a sysdiagnose is captured."
+ "Invalid persisted app usage priorities"
+ "Invalid persisted personalized scheduling metrics"
+ "Listening for TLC predictions"
+ "Loaded app usage priorities v%lu: %lu entries, age %.0fs, stale %{BOOL}d"
+ "Loaded freezer ML model from Trial (isiPad: %d)"
+ "Loaded task app map: %lu prefixes, medium: %lu services, %lu feature codes, %lu prefixes, %lu name substrings, %lu skipped, %lu listed under more than one app"
+ "Loading compiled model from %@ (filename: %@)"
+ "Loading trial freezer ML model from factor: %@ (isiPad: %d)"
+ "MediumFeatureCodes"
+ "MediumNameSubstrings"
+ "MediumServices"
+ "MediumTaskPrefixes"
+ "MitigationValue"
+ "No persisted app usage priorities"
+ "No sysdiagnose stopped notification after %.0fs, releasing held tasks"
+ "No trial freezer model path configured for factor: %@"
+ "Persisted app usage priorities unavailable, will retry: %@"
+ "PersonalizedSchedulingEnabled"
+ "PersonalizedSchedulingSpotlightUsesAppPriority"
+ "PersonalizedSchedulingWeightHigh"
+ "PersonalizedSchedulingWeightLow"
+ "PersonalizedSchedulingWeightMedium"
+ "Please file a bug for – client %{public}@ attempted to read app usage priorities but lacked appropriate entitlement"
+ "Please file a bug for – client %{public}@ attempted to update app usage priorities but lacked appropriate entitlement"
+ "PowerUISmartChargeClient"
+ "Q48@0:8B16B20B24q28q36B44"
+ "QoSPolicyPostCSPNEnabled"
+ "Reported personalized scheduling metrics: completed %lu/%lu/%lu (low/medium/high)"
+ "Successfully loaded model from %@ (filename: %@)"
+ "Sysdiagnose started, holding discretionary and intensive tasks"
+ "Sysdiagnose stopped, releasing held tasks"
+ "T@\"BIThermalPredictionClient\",&,N,V_predictionClient"
+ "T@\"NSArray\",R,N,V_mediumNameSubstrings"
+ "T@\"NSArray\",R,N,V_mediumTaskPrefixes"
+ "T@\"NSArray\",R,N,V_prefixes"
+ "T@\"NSDate\",&,N,V_lastFlushDate"
+ "T@\"NSDate\",&,N,V_lastPersistDate"
+ "T@\"NSDictionary\",&,N,V_record"
+ "T@\"NSDictionary\",R,N,V_prefixToApp"
+ "T@\"NSDictionary\",R,N,V_priorities"
+ "T@\"NSMutableDictionary\",&,N,V_trackingKeysByActivity"
+ "T@\"NSSet\",R,N,V_mediumFeatureCodes"
+ "T@\"NSSet\",R,N,V_mediumServices"
+ "T@\"NSURL\",&,N,V_fileURL"
+ "T@\"PowerUISmartChargeClient\",&,N,V_smartChargeClient"
+ "T@\"_DASClientMetricsRecorder\",&,N,V_recorder"
+ "T@\"_DASPersonalizedSchedulingMetrics\",&,N,V_personalizedSchedulingMetrics"
+ "T@?,C,V_mitigationChangeHandler"
+ "TB,GisPostCSPNEnabled,V_postCSPNEnabled"
+ "TB,N"
+ "TB,N,V_loaded"
+ "TB,N,V_loggedLoadFailure"
+ "TB,V_lowerQoSEnabled"
+ "TB,V_mitigationsEnabled"
+ "TB,V_stopAllPluggedInUntil35CEnabled"
+ "TB,V_stopIntensiveEnabled"
+ "TB,V_stopPluggedInEnabled"
+ "TB,V_sysdiagnoseInProgress"
+ "TB,V_willHitTLC"
+ "TLC SOC floors: Floor1=%ld Floor2=%ld Floor3=%ld Floor4=%ld"
+ "TLC mitigation %{public}@ -> %{public}@ (predicted=%{BOOL}u SOC=%ld limit=%ld temp=%ld hit=%{BOOL}u)"
+ "TLC mitigations enabled: all=%{BOOL}u lowerQoS=%{BOOL}u stopIntensive=%{BOOL}u stopPluggedIn=%{BOOL}u stopAllPluggedInUntil35C=%{BOOL}u"
+ "TLC prediction"
+ "TLC prediction failed (%{public}@ %ld); treating as not predicted"
+ "TLC prediction: willHitTLC=%{BOOL}u confidence=%.3f"
+ "TLCMitigation"
+ "TLCMitigationLowerQoSEnabled"
+ "TLCMitigationSOCFloor1"
+ "TLCMitigationSOCFloor2"
+ "TLCMitigationSOCFloor3"
+ "TLCMitigationSOCFloor4"
+ "TLCMitigationStopIntensiveTasksEnabled"
+ "TLCMitigationStopPluggedInTasksEnabled"
+ "TLCMitigationStopPluggedInTasksUntil35CEnabled"
+ "TLCMitigationsEnabled"
+ "TQ,N,V_captureCount"
+ "TQ,V_tlcMitigation"
+ "Task app map unavailable: %@"
+ "Ti,N,V_startedToken"
+ "Ti,N,V_stoppedToken"
+ "Tq,V_chargeLimit"
+ "Tq,V_socFloor1"
+ "Tq,V_socFloor2"
+ "Tq,V_socFloor3"
+ "Tq,V_socFloor4"
+ "Trial factor %@ resolved to model path: %@"
+ "Trial: %{public}@ %{public}s, post-CSPN condition %{public}s"
+ "Trial: PersonalizedScheduling weights set to %.2f / %.2f / %.2f (high / medium / low)"
+ "Trial: PersonalizedSchedulingEnabled set to %d"
+ "Trial: PersonalizedSchedulingSpotlightUsesAppPriority set to %d"
+ "T{os_unfair_recursive_lock_s=[2I]},N,V_activityStateLock"
+ "T{os_unfair_recursive_lock_s=[2I]},N,V_applicationLaunchRequestsLock"
+ "T{os_unfair_recursive_lock_s=[2I]},N,V_lock"
+ "T{os_unfair_recursive_lock_s=[2I]},N,V_purgeableSpaceMapLock"
+ "URLByAppendingPathComponent:"
+ "[3Q]"
+ "[3d]"
+ "_DASAppUsagePriorityCache"
+ "_DASAppUsagePrioritySnapshot"
+ "_DASPersonalizedSchedulingMetrics"
+ "_DASSysdiagnosePolicy"
+ "_DASTaskAppMap"
+ "_captureCount"
+ "_chargeLimit"
+ "_completedCount"
+ "_completionTime"
+ "_fileURL"
+ "_lastFlushDate"
+ "_lastPersistDate"
+ "_loaded"
+ "_loggedLoadFailure"
+ "_lowerQoSEnabled"
+ "_mediumFeatureCodes"
+ "_mediumNameSubstrings"
+ "_mediumServices"
+ "_mediumTaskPrefixes"
+ "_mitigationChangeHandler"
+ "_mitigationsEnabled"
+ "_personalizedSchedulingMetrics"
+ "_phaseSchedulingEnabled"
+ "_postCSPNEnabled"
+ "_predictionClient"
+ "_prefixToApp"
+ "_prefixes"
+ "_priorities"
+ "_record"
+ "_recorder"
+ "_runtime"
+ "_smartChargeClient"
+ "_socFloor1"
+ "_socFloor2"
+ "_socFloor3"
+ "_socFloor4"
+ "_startedToken"
+ "_stopAllPluggedInUntil35CEnabled"
+ "_stopIntensiveEnabled"
+ "_stopPluggedInEnabled"
+ "_stoppedToken"
+ "_sysdiagnoseInProgress"
+ "_tlcMitigation"
+ "_tlcMitigationHandler"
+ "_trackingKeysByActivity"
+ "_weightHigh"
+ "_weightLow"
+ "_weightMedium"
+ "_willHitTLC"
+ "app:"
+ "appUsagePriorities.plist"
+ "appUsagePriority"
+ "appUsagePrioritySnapshotForActivities:date:"
+ "captureCount"
+ "chargeLimit"
+ "com.apple.das.private.usagepriorities"
+ "com.apple.das.private.usagepriorities.read"
+ "com.apple.das.sysdiagnose.statuschanged"
+ "com.apple.dasd.personalizedScheduling"
+ "com.apple.dasd.personalizedScheduling.high"
+ "com.apple.dasd.personalizedScheduling.low"
+ "com.apple.dasd.personalizedScheduling.medium"
+ "com.apple.dasd.personalizedSchedulingMetrics"
+ "com.apple.dasd.sysdiagnosepolicy"
+ "com.apple.dasd.tlcPredictionSeed"
+ "com.apple.sysdiagnose.sysdiagnoseStopped"
+ "compareActivity:withActivity:usagePriorities:"
+ "completedCount"
+ "completionTime"
+ "confidenceScore"
+ "csilqCSILQ"
+ "currentPriorities"
+ "d24@0:8q16"
+ "dataWithContentsOfURL:options:error:"
+ "dictionaryWithContentsOfURL:error:"
+ "didUpdateTLCPrediction:error:"
+ "failed to persist"
+ "feature:"
+ "fileURL"
+ "flushIfDueAtDate:"
+ "forgetTrackingKeysForActivity:"
+ "getAppUsagePrioritiesWithHandler:"
+ "getMCLLimitWithHandler:"
+ "handleSysdiagnoseStarted"
+ "handleSysdiagnoseStopped"
+ "handleSysdiagnoseTimeoutForCapture:"
+ "handleTLCPrediction:confidence:error:"
+ "initWithDirectory:"
+ "initWithFileURL:"
+ "initWithPriorities:date:"
+ "initWithRecorder:fileURL:"
+ "intensivePriorityForActivity:"
+ "invalid timestamp"
+ "isEqualToDictionary:"
+ "isMediumActivity:"
+ "isMediumActivity:lowercaseName:"
+ "isPersonalizedSchedulingEnabled"
+ "isPostCSPNEnabled"
+ "isStale"
+ "lastFlushDate"
+ "lastPersistDate"
+ "loadIfNeeded"
+ "loadRecordIfNeeded"
+ "loaded"
+ "loggedLoadFailure"
+ "lower QoS for intensive"
+ "lowerQoSEnabled"
+ "malformed priorities"
+ "mappedBundleIdentifierForLowercaseName:"
+ "mappedBundleIdentifierForTaskName:"
+ "mediumFeatureCodes"
+ "mediumNameSubstrings"
+ "mediumServices"
+ "mediumTaskPrefixes"
+ "mitigationAfterTrialGating:"
+ "mitigationChangeHandler"
+ "mitigationForPrediction:isPluggedIn:chargeIntentionallyStopped:batteryLevel:temperature:hitTLC:"
+ "mitigationsEnabled"
+ "nonIntensivePriorityForActivity:"
+ "notifyMitigationChanged"
+ "objCType"
+ "persistAtDate:"
+ "persistRecord:"
+ "persisted state unavailable"
+ "personalizedSchedulingMetrics"
+ "personalizedSchedulingMetrics.plist"
+ "phaseOrAppPriorityForActivity:"
+ "post-CSPN condition enabled"
+ "postCSPNEnabled"
+ "predictTLCWithError:"
+ "predicted TLC"
+ "predictionClient"
+ "prefixToApp"
+ "prefixes"
+ "priorities"
+ "prioritiesForActivities:fromAppPriorities:"
+ "priorityForActivity:"
+ "priorityForActivity:fromAppPriorities:"
+ "priorityForBundleIdentifier:"
+ "propertyListWithData:options:format:error:"
+ "q32@0:8@16q24"
+ "q40@0:8@16@24@32"
+ "receivedDate"
+ "recomputeMitigationOnQueue"
+ "record"
+ "recordEndOfActivity:completed:wasRunning:priority:atDate:"
+ "recordPersonalizedSchedulingMetricsForActivity:completed:wasRunning:"
+ "recorder"
+ "refreshChargeLimit"
+ "refreshPersonalizedSchedulingGateWithTrialManager:"
+ "refreshWeightsWithTrialManager:"
+ "registerTrackingKey:forActivity:inGroup:"
+ "runtime"
+ "seedTLCPrediction"
+ "setCaptureCount:"
+ "setChargeLimit:"
+ "setFileURL:"
+ "setLastFlushDate:"
+ "setLastPersistDate:"
+ "setLoaded:"
+ "setLoggedLoadFailure:"
+ "setLowerQoSEnabled:"
+ "setMitigationChangeHandler:"
+ "setMitigationsEnabled:"
+ "setPersonalizedSchedulingMetrics:"
+ "setPostCSPNEnabled:"
+ "setPredictionClient:"
+ "setRecord:"
+ "setRecorder:"
+ "setResourceValue:forKey:error:"
+ "setSmartChargeClient:"
+ "setSocFloor1:"
+ "setSocFloor2:"
+ "setSocFloor3:"
+ "setSocFloor4:"
+ "setSpotlightUsesAppPriority:"
+ "setStartedToken:"
+ "setStopAllPluggedInUntil35CEnabled:"
+ "setStopIntensiveEnabled:"
+ "setStopPluggedInEnabled:"
+ "setStoppedToken:"
+ "setSysdiagnoseInProgress:"
+ "setTlcMitigation:"
+ "setTrackingKeysByActivity:"
+ "setUpPredictionClient"
+ "setWillHitTLC:"
+ "shouldLowerQoSForPredictedTLC"
+ "smartChargeClient"
+ "snapshot"
+ "socFloor1"
+ "socFloor2"
+ "socFloor3"
+ "socFloor4"
+ "softlink:r:path:/System/Library/PrivateFrameworks/BatteryIntelligence.framework/BatteryIntelligence"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI"
+ "spotlightUsesAppPriority"
+ "stale"
+ "startedToken"
+ "stop intensive"
+ "stop pluggedIn-required"
+ "stop pluggedIn-required until 35C"
+ "stopAllPluggedInUntil35CEnabled"
+ "stopIntensiveEnabled"
+ "stopPluggedInEnabled"
+ "stoppedToken"
+ "sysdiagnose"
+ "sysdiagnoseInProgress"
+ "tlcMitigation"
+ "tlcMitigation == %@"
+ "trackingKeysByActivity"
+ "trialFlagEnabled:"
+ "trialSOCFloor:defaultValue:"
+ "unprotectedTrackerKeyForActivity:inGroup:"
+ "updateAppUsagePriorities:version:timestamp:withHandler:"
+ "updatePersonalizedSchedulingMetricsState"
+ "updatePriorities:version:timestamp:error:"
+ "updateSysdiagnoseInProgress:"
+ "v"
+ "v20@?0C8@\"NSError\"12"
+ "v24@0:8{os_unfair_recursive_lock_s=[2I]}16"
+ "v32@0:8@\"BIThermalPredictionOutput\"16@\"NSError\"24"
+ "v32@0:8@16B24B28"
+ "v36@0:8B16d20@28"
+ "v48@0:8@\"NSDictionary\"16Q24@\"NSDate\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@16B24B28q32@40"
+ "v48@0:8@16Q24@32@?40"
+ "version older than stored"
+ "weightForPriority:"
+ "willHitTLC"
+ "writeToURL:options:error:"
+ "{os_unfair_recursive_lock_s=\"_os_unfair_recursive_lock_opaque\"[2I]}"
+ "{os_unfair_recursive_lock_s=[2I]}16@0:8"
+ "\xa7"
- "6"
- "Cleared %lu remembered thermal tasks: %{public}@"
- "Loaded freezer ML model from Trial"
- "Loading compiled model from %@"
- "Loading trial freezer ML model"
- "No trial freezer model path configured"
- "Remembering %{public}@ (task ID %lu) for thermal pressure, %lu remembered"
- "Successfully loaded model from %@"
- "Sysdiagnose started, suspending running tasks if any"
- "TB,N,V_prohibitTasksOnTLC"
- "T{os_unfair_recursive_lock_s={os_unfair_lock_s=I}I},N,V_activityStateLock"
- "T{os_unfair_recursive_lock_s={os_unfair_lock_s=I}I},N,V_applicationLaunchRequestsLock"
- "T{os_unfair_recursive_lock_s={os_unfair_lock_s=I}I},N,V_lock"
- "T{os_unfair_recursive_lock_s={os_unfair_lock_s=I}I},N,V_purgeableSpaceMapLock"
- "_prohibitTasksOnTLC"
- "_thermalFirstEntryDate"
- "_thermalTaskIDs"
- "battery level"
- "batteryLevel == %@ AND temperature == %@"
- "charger disconnected"
- "com.apple.das.qos.batteryLevel"
- "com.apple.das.qos.thermalPressure"
- "didSuspendActivity:forQoSDowngradeWithReasons:"
- "handleSysdiagnoseStartEvent"
- "isPluggedInWithState:"
- "lifetime elapsed"
- "low battery"
- "periodic timer"
- "policy disabled"
- "prohibitTasksOnTLC"
- "prohibitTasksOnTLC is %{BOOL}u"
- "recent thermal suspension"
- "resetThermalMemoryWithReason:"
- "setProhibitTasksOnTLC:"
- "shouldIgnoreThermalPressure"
- "thermal pressure"
- "thermalMemoryFirstEntryDate"
- "thermalMemoryTaskIDs"
- "v24@0:8{os_unfair_recursive_lock_s={os_unfair_lock_s=I}I}16"
- "v32@?0@\"_DASActivity\"8@\"NSNumber\"16^B24"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"
- "{os_unfair_recursive_lock_s={os_unfair_lock_s=I}I}16@0:8"
- "\x91"
```
