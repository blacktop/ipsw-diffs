## dasd

> `/usr/libexec/dasd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
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
- `__TEXT.__info_plist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-2467.0.40.0.0
-  __TEXT.__text: 0x132874
-  __TEXT.__auth_stubs: 0x1e00
-  __TEXT.__objc_stubs: 0x15300
-  __TEXT.__objc_methlist: 0xf7a4
+2467.40.49.0.0
+  __TEXT.__text: 0x135a44
+  __TEXT.__auth_stubs: 0x1e80
+  __TEXT.__objc_stubs: 0x15760
+  __TEXT.__objc_methlist: 0xfa7c
   __TEXT.__const: 0x1268
-  __TEXT.__objc_methname: 0x24852
-  __TEXT.__cstring: 0xc516
-  __TEXT.__oslogstring: 0xfeb9
-  __TEXT.__objc_classname: 0x1808
-  __TEXT.__objc_methtype: 0x30c1
-  __TEXT.__gcc_except_tab: 0x3aa4
+  __TEXT.__objc_methname: 0x254eb
+  __TEXT.__cstring: 0xc976
+  __TEXT.__oslogstring: 0x104f9
+  __TEXT.__objc_classname: 0x1828
+  __TEXT.__objc_methtype: 0x3161
+  __TEXT.__gcc_except_tab: 0x3b10
   __TEXT.__dlopen_cstrs: 0x268
   __TEXT.__swift5_typeref: 0x8f8
   __TEXT.__swift5_capture: 0x1e4

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
   __TEXT.__info_plist: 0x563
-  __TEXT.__unwind_info: 0x5080
+  __TEXT.__unwind_info: 0x5178
   __TEXT.__eh_frame: 0xbb0
-  __DATA_CONST.__const: 0x4160
-  __DATA_CONST.__cfstring: 0xdae0
-  __DATA_CONST.__objc_classlist: 0x620
+  __DATA_CONST.__const: 0x4238
+  __DATA_CONST.__cfstring: 0xdf20
+  __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x518
+  __DATA_CONST.__objc_superrefs: 0x520
   __DATA_CONST.__objc_intobj: 0x1368
-  __DATA_CONST.__objc_arraydata: 0x1e0
-  __DATA_CONST.__objc_arrayobj: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x238
+  __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x168
-  __DATA_CONST.__auth_got: 0xf10
-  __DATA_CONST.__got: 0xaf8
+  __DATA_CONST.__auth_got: 0xf50
+  __DATA_CONST.__got: 0xb08
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x2b270
-  __DATA.__objc_selrefs: 0x7ca0
-  __DATA.__objc_ivar: 0x1190
-  __DATA.__objc_data: 0x3ff8
+  __DATA.__objc_const: 0x2b688
+  __DATA.__objc_selrefs: 0x7eb8
+  __DATA.__objc_ivar: 0x11e0
+  __DATA.__objc_data: 0x4048
   __DATA.__data: 0x1b18
-  __DATA.__bss: 0x11b0
+  __DATA.__bss: 0x11e0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6805
-  Symbols:   855
-  CStrings:  9639
+  Functions: 6895
+  Symbols:   865
+  CStrings:  9813
 
Symbols:
+ _IOIteratorNext
+ _IORegistryEntryCreateCFProperty
+ _IOServiceGetMatchingServices
+ _OBJC_CLASS_$__CDContextValue
+ _SCDynamicStoreSetDispatchQueue
+ __CDInformativeContextualChangeNewValueKey
+ __CDInformativeContextualChangeOldValueKey
+ _dispatch_assert_queue_not$V2
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
- _NSFileProtectionCompleteUntilFirstUserAuthentication
CStrings:
+ "%@ is %d"
+ "%@.%@"
+ "%@|v"
+ "%@|v%ld"
+ "%s unavailable across all AppleSmartBatteryPack nodes"
+ "(unknown)"
+ "@\"RBSProcessMonitor\""
+ "@\"_CDContextualChangeRegistration\""
+ "@32@0:8@16q24"
+ "Activity %s has no launch reason, skipping"
+ "AppLifecycleConsoleUserMonitor"
+ "AppLifecycleRecorder"
+ "AppleChargerData"
+ "AppleSmartBatteryPack"
+ "B36@0:8@16B24@28"
+ "B48@0:8Q16@24@32^@40"
+ "Backfilled %lu app lifecycle checkpoints"
+ "Backfilling app lifecycle checkpoints for %{public}@ - %{public}@"
+ "BatteryData"
+ "BatteryTemperatureReader returning value %ld (centi-C)"
+ "Convert stream: %@ : Failed to save %lu events: %@"
+ "Convert stream: %@ : Failed to save %lu final events: %@"
+ "Convert stream: %@ : Timed out waiting for conversion to complete"
+ "Donated checkpoint %lu for %{public}@ at %{public}@"
+ "ERROR Submitting Activity: %@ due to configuration limits. Please contact us to prevent this activity from getting rejected. Configuration: %@"
+ "Failed to create SCDynamicStore; macOS donations will be limited to startup"
+ "Failed to read App.InFocus: %{public}@"
+ "Failed to record checkpoint %lu for %{public}@: %{public}@"
+ "Failed to set console user notification keys"
+ "FastPass %{public}@ v%d consumed %.1fs this run, %.1fs cumulative"
+ "FastPass %{public}@ v%d has consumed %.1fs of its %.1fs budget, %.1fs remaining"
+ "FastPassConsumedRuntime"
+ "IdleStack thermal max (start/run): low %d/%d, medium %d/%d, high %d/%d"
+ "No console user; deferring backfill until login"
+ "No match for AppleSmartBatteryPack IOService"
+ "Nothing to backfill; resume point is not before the window end"
+ "Override status: %@"
+ "PolicyDeviceActivityIdleStackHighBlockRunOnEarlyThermal"
+ "PolicyDeviceActivityIdleStackHighBlockStartOnEarlyThermal"
+ "PolicyDeviceActivityIdleStackLowBlockRunOnEarlyThermal"
+ "PolicyDeviceActivityIdleStackLowBlockStartOnEarlyThermal"
+ "PolicyDeviceActivityIdleStackMediumBlockRunOnEarlyThermal"
+ "PolicyDeviceActivityIdleStackMediumBlockStartOnEarlyThermal"
+ "PolicyThermalIdleStackHighMaxAllowableToRun"
+ "PolicyThermalIdleStackHighMaxAllowableToStart"
+ "PolicyThermalIdleStackLowMaxAllowableToRun"
+ "PolicyThermalIdleStackLowMaxAllowableToStart"
+ "PolicyThermalIdleStackMediumMaxAllowableToRun"
+ "PolicyThermalIdleStackMediumMaxAllowableToStart"
+ "Registered for ContextStore foreground app changes"
+ "T@\"NSMutableSet\",&,N,V_suspendedBundleIDs"
+ "T@\"RBSProcessMonitor\",&,N,V_suspensionMonitor"
+ "TB,N,V_disableSpecialCasedThermalPolicyForDuo"
+ "TB,N,V_idleStackHighBlockRunOnEarlyThermal"
+ "TB,N,V_idleStackHighBlockStartOnEarlyThermal"
+ "TB,N,V_idleStackLowBlockRunOnEarlyThermal"
+ "TB,N,V_idleStackLowBlockStartOnEarlyThermal"
+ "TB,N,V_idleStackMediumBlockRunOnEarlyThermal"
+ "TB,N,V_idleStackMediumBlockStartOnEarlyThermal"
+ "TB,N,V_suspensionSendPending"
+ "Ti,N,V_idleStackHighRunMax"
+ "Ti,N,V_idleStackHighStartMax"
+ "Ti,N,V_idleStackLowRunMax"
+ "Ti,N,V_idleStackLowStartMax"
+ "Ti,N,V_idleStackMediumRunMax"
+ "Ti,N,V_idleStackMediumStartMax"
+ "Unable to get valid battery temperature from AppleSmartBattery"
+ "VirtualTemperature"
+ "_DASAppLifecycleRecorder"
+ "_disableSpecialCasedThermalPolicyForDuo"
+ "_foregroundAppRegistration"
+ "_idleStackHighBlockRunOnEarlyThermal"
+ "_idleStackHighBlockStartOnEarlyThermal"
+ "_idleStackHighRunMax"
+ "_idleStackHighStartMax"
+ "_idleStackLowBlockRunOnEarlyThermal"
+ "_idleStackLowBlockStartOnEarlyThermal"
+ "_idleStackLowRunMax"
+ "_idleStackLowStartMax"
+ "_idleStackMediumBlockRunOnEarlyThermal"
+ "_idleStackMediumBlockStartOnEarlyThermal"
+ "_idleStackMediumRunMax"
+ "_idleStackMediumStartMax"
+ "_liveDonationStartDate"
+ "_suspendedBundleIDs"
+ "_suspensionMonitor"
+ "_suspensionSendPending"
+ "absoluteTimestamp"
+ "accrueFastPassRuntimeForActivity:"
+ "activityTransferSize == %lu"
+ "addConsumedRuntime:forFastPass:semanticVersion:"
+ "appLifecycle"
+ "backfillCheckpointsUpToDate:"
+ "backfillHistoryPrecedingLiveWindow"
+ "batteryTemperatureReader"
+ "boolTrialFactor:default:"
+ "clearConsumedRuntimeForFastPass:resetAll:"
+ "com.apple.DocumentsApp"
+ "com.apple.MobileSMS"
+ "com.apple.Notes"
+ "com.apple.dasd.appLifecycle.foregroundApp"
+ "com.apple.dasd.appLifecycleBackfill"
+ "com.apple.dasd.appLifecycleRecorder"
+ "com.apple.iCal"
+ "com.apple.mail"
+ "com.apple.mobilecal"
+ "com.apple.mobilenotes"
+ "com.apple.mobileslideshow"
+ "com.apple.reminders"
+ "consumedRuntimeForFastPass:semanticVersion:"
+ "consumedRuntimeKeyForFastPass:semanticVersion:"
+ "d32@0:8@16q24"
+ "d40@0:8@16q24d32"
+ "defaultPathIsInexpensive"
+ "defaultPathIsUnconstrained"
+ "directBiomeWriterStreamNames"
+ "disableSpecialCasedThermalPolicyForDuo"
+ "donateTransitionForApp:foregrounded:atDate:"
+ "handleForegroundAppChange:"
+ "idleStackHighBlockRunOnEarlyThermal"
+ "idleStackHighBlockStartOnEarlyThermal"
+ "idleStackHighRunMax"
+ "idleStackHighStartMax"
+ "idleStackLowBlockRunOnEarlyThermal"
+ "idleStackLowBlockStartOnEarlyThermal"
+ "idleStackLowRunMax"
+ "idleStackLowStartMax"
+ "idleStackMaxAllowableForActivity:"
+ "idleStackMediumBlockRunOnEarlyThermal"
+ "idleStackMediumBlockStartOnEarlyThermal"
+ "idleStackMediumRunMax"
+ "idleStackMediumStartMax"
+ "inLongInactivityWindow"
+ "initInternal"
+ "initWithDKStreamIdentifier:"
+ "installConsoleUserObserver"
+ "installForegroundAppObserver"
+ "isConstrained"
+ "isExpensive"
+ "isHighPriorityIdleStackTask"
+ "isMediumPriorityIdleStackTask"
+ "isMindPalaceAmbientActivity"
+ "isMindPalaceUserInitiatedActivity"
+ "isThermallyConstrainedHardware"
+ "localNonWakingRegistrationWithIdentifier:contextualPredicate:clientIdentifier:callback:"
+ "maxBatteryTemperatureAcrossPacks"
+ "mindPalaceAmbient == 1"
+ "notChargingReasonUnionAcrossPacks"
+ "rawTrialLevelForFactor:"
+ "remainingRuntimeForFastPass:semanticVersion:budget:"
+ "reportCustomCheckpoint:forTask:atDate:error:"
+ "resumeDateBefore:"
+ "setDisableSpecialCasedThermalPolicyForDuo:"
+ "setIdleStackHighBlockRunOnEarlyThermal:"
+ "setIdleStackHighBlockStartOnEarlyThermal:"
+ "setIdleStackHighRunMax:"
+ "setIdleStackHighStartMax:"
+ "setIdleStackLowBlockRunOnEarlyThermal:"
+ "setIdleStackLowBlockStartOnEarlyThermal:"
+ "setIdleStackLowRunMax:"
+ "setIdleStackLowStartMax:"
+ "setIdleStackMediumBlockRunOnEarlyThermal:"
+ "setIdleStackMediumBlockStartOnEarlyThermal:"
+ "setIdleStackMediumRunMax:"
+ "setIdleStackMediumStartMax:"
+ "setSuspendedBundleIDs:"
+ "setSuspensionMonitor:"
+ "setSuspensionSendPending:"
+ "sharedRecorder"
+ "shouldBlockIdleStackActivityOnEarlyThermal:withContext:"
+ "startDonating"
+ "suspendedBundleIDs"
+ "suspensionMonitor"
+ "suspensionSendPending"
+ "v16@?0@\"_DKEvent\"8"
+ "v40@0:8d16@24q32"
+ "writeDirectStreamName: %@ : Processed events are not valid JSON objects, skipping with error %@"
+ "writeDirectStreamName: %@ : Timed out waiting for write to complete, numberOfWrittenEvents may be an undercount"
+ "writeDirectStreamName: %@ : written %lu events, total written so far: %lu"
+ "writeDirectStreamName:toFileHandle:withEventPredicate:withEventProvider:"
+ "writeExperiment: %@ : stream %@ is in directBiomeWriterStreamNames but has no direct writer wired up"
+ "writeStream: %@ : Timed out waiting for read to complete, numberOfWrittenEvents may be an undercount"
+ "\x85"
- " Size %lu upload:%d, [wifiLQM] Required=%ld, Observed=%ld, [cellLQM] Required=%ld Observed=%ld\n"
- "BatteryTemperatureReader returning value %@"
- "ERROR Submitting Activity: %@ due to configuration limits. Please contact das-core@group.apple.com to prevent this activity from getting rejected. Configuration: %@"
- "Temperature"
- "U"
- "Unable to get valid battery temperature: %@"
- "convertKeybagLockedStream:toKnowledgeStoreStream:"
- "inexpensivePathAvailable"
- "initWithDKStreamIdentifier:contentProtection:"
```
