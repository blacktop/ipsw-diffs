## terminusd

> `/usr/libexec/terminusd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-914.0.34.0.4
-  __TEXT.__text: 0x1fb010
-  __TEXT.__auth_stubs: 0x3ed0
-  __TEXT.__objc_stubs: 0x9020
-  __TEXT.__objc_methlist: 0x58c4
+914.40.22.0.0
+  __TEXT.__text: 0x1fb854
+  __TEXT.__auth_stubs: 0x3ef0
+  __TEXT.__objc_stubs: 0x8e00
+  __TEXT.__objc_methlist: 0x5594
   __TEXT.__const: 0x73c
   __TEXT.__swift5_typeref: 0x4ce
-  __TEXT.__cstring: 0x525cf
+  __TEXT.__cstring: 0x52a43
   __TEXT.__swift5_capture: 0x4a4
-  __TEXT.__objc_methtype: 0x4346
+  __TEXT.__objc_methtype: 0x433b
   __TEXT.__oslogstring: 0x2dee
   __TEXT.__constg_swiftt: 0x1f8
   __TEXT.__swift5_reflstr: 0x8b
   __TEXT.__swift5_fieldmd: 0xf0
   __TEXT.__objc_classname: 0x14dc
-  __TEXT.__objc_methname: 0x13205
+  __TEXT.__objc_methname: 0x129b5
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x18

   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift_as_cont: 0xdc
-  __TEXT.__gcc_except_tab: 0x628c
-  __TEXT.__unwind_info: 0x3eb0
+  __TEXT.__gcc_except_tab: 0x62c8
+  __TEXT.__unwind_info: 0x3e98
   __TEXT.__eh_frame: 0xe90
-  __DATA_CONST.__const: 0x4eb0
-  __DATA_CONST.__cfstring: 0xdf80
+  __DATA_CONST.__const: 0x4f18
+  __DATA_CONST.__cfstring: 0xe280
   __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1a0

   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x1f78
-  __DATA_CONST.__got: 0xec0
+  __DATA_CONST.__auth_got: 0x1f88
+  __DATA_CONST.__got: 0xf00
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA.__objc_const: 0x1a0e8
-  __DATA.__objc_selrefs: 0x2d00
-  __DATA.__objc_ivar: 0x2074
+  __DATA.__objc_const: 0x19f78
+  __DATA.__objc_selrefs: 0x2b60
+  __DATA.__objc_ivar: 0x208c
   __DATA.__objc_data: 0x38f0
   __DATA.__data: 0x1938
   __DATA.__common: 0x18

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3973
-  Symbols:   1536
-  CStrings:  11674
+  Functions: 3908
+  Symbols:   1547
+  CStrings:  11628
 
Symbols:
+ _CFUserNotificationCreate
+ _CFUserNotificationReceiveResponse
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ __swift_FORCE_LOAD_$_swiftIntents
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationAlternateButtonTitleKey
+ _kCFUserNotificationDefaultButtonTitleKey
+ _nrXPCKeyAdditionalData
CStrings:
+ "%s%.30s:%-4d %@: Received additional pairing data length=%lu"
+ "%s%.30s:%-4d %@: Update additional data rejected: missing data payload"
+ "%s%.30s:%-4d %@: Update additional data rejected: pairing already in progress with a target"
+ "%s%.30s:%-4d NRDTriggerTapToRadar: CFUserNotificationCreate failed: %d"
+ "%s%.30s:%-4d NRDTriggerTapToRadar: suppressed for %@ (rate-limited)"
+ "%s%.30s:%-4d detected mismatch in connect peripheral states for %@: terminusd peripheral.state=%@, bluetoothd retrieveConnectingPeripherals contains device=%s"
+ "-[NRDevicePairingDirector handleUpdateAdditionalDataRequest:operation:forConnection:]"
+ "212336"
+ "675393"
+ "914.40.22"
+ "Classification"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Connecting"
+ "Description"
+ "Disconnecting"
+ "Dismiss"
+ "File Radar"
+ "Keywords"
+ "MeshRoomDistributionForClusters"
+ "NRDTTRLastPromptTime"
+ "NRDTriggerTapToRadar"
+ "NRDTriggerTapToRadar_block_invoke_2"
+ "Not Applicable"
+ "Other Bug"
+ "Reproducibility"
+ "Title"
+ "URL"
+ "[%@] terminusd reported issues"
+ "_didSendAdditionalData"
+ "_outgoingAdditionalData"
+ "_pendingUpdateBlocks"
+ "_previouslyMismatchedConnectingPeripheralIdentifiers"
+ "_processingUpdateBlocks"
+ "_remoteAdditionalData"
+ "all"
+ "an unknown issue (type %u)"
+ "com.apple.terminusd.ttr"
+ "connect peripheral mismatch"
+ "data stall"
+ "defaultWorkspace"
+ "openURL:configuration:completionHandler:"
+ "queryItemWithName:value:"
+ "setAdditionalData:"
+ "setQueryItems:"
+ "tap-to-radar://new"
+ "terminusd detected a %@. Tap 'File Radar' to capture a sysdiagnose."
+ "terminusd detected an issue"
+ "terminusd has detected a connectivity issue - %@ (type: %@)\n\nPlease attach a sysdiagnose taken near the time of this prompt."
+ "timeIntervalSinceReferenceDate"
- "%s%.30s:%-4d detected mismatch in connect peripheral states for %@"
- "914.0.34.0.4"
- "Advice exceeds %u seconds"
- "NRAutoLinkUpgrade"
- "T@\"NSNumber\",&,N,V_lastReceivedAdviceID"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_aggregateStatsTimerSource"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_wifiAdviceMonitorTimerSource"
- "T@?,C,N,V_updateBlock"
- "TB,N,V_cancelled"
- "TB,N,V_hasActiveNonDefaultAdvice"
- "TB,N,V_hasReportedHonoredStatusToSymptoms"
- "TB,N,V_hasReportedUpgradeStatusToSymptoms"
- "TB,N,V_started"
- "TC,N,V_battery"
- "TC,N,V_thermalLevel"
- "TC,N,V_type"
- "TQ,N,V_advice"
- "TQ,N,V_endAdvice"
- "TQ,N,V_endReason"
- "TQ,N,V_identifier"
- "TQ,N,V_lastAdvisoryTime"
- "TQ,N,V_lastNonDefaultAdvisoryTime"
- "TQ,N,V_lastReceivedAdvice"
- "TQ,N,V_lastReceivedReason"
- "TQ,N,V_rateOfAdvicePerHour"
- "TQ,N,V_reason"
- "TQ,N,V_timeOfBTClassicAdvice"
- "TQ,N,V_timeOfWiFiAdvice"
- "TQ,N,V_totalCountForBTClassicAdvice"
- "TQ,N,V_totalCountForNonDefaultAdvice"
- "TQ,N,V_totalCountForWiFiAdvice"
- "TQ,N,V_totalReceivedUpdates"
- "Td,N,V_timeSinceLastAdvice"
- "Td,N,V_totalDurationForBTClassicAdvice"
- "Td,N,V_totalDurationForWiFiAdvice"
- "Td,N,V_totalIntervalForNonDefaultAdvice"
- "WiFiAdvice"
- "advice"
- "aggregateStatsTimerSource"
- "armAggregateStatsTimerSource"
- "armWiFiAdviceMonitorTimerSource"
- "hasActiveNonDefaultAdvice"
- "hasReportedHonoredStatusToSymptoms"
- "hasReportedUpgradeStatusToSymptoms"
- "invalidateAggregateStatsTimerSource"
- "invalidateWiFiAdviceMonitorTimerSource"
- "lastAdvisoryTime"
- "lastNonDefaultAdvisoryTime"
- "lastReceivedAdvice"
- "lastReceivedAdviceID"
- "lastReceivedReason"
- "rateOfAdvicePerHour"
- "reason"
- "setAdvice:"
- "setAggregateStatsTimerSource:"
- "setBattery:"
- "setCancelled:"
- "setEndAdvice:"
- "setEndReason:"
- "setHasActiveNonDefaultAdvice:"
- "setHasReportedHonoredStatusToSymptoms:"
- "setHasReportedUpgradeStatusToSymptoms:"
- "setLastAdvisoryTime:"
- "setLastNonDefaultAdvisoryTime:"
- "setLastReceivedAdvice:"
- "setLastReceivedAdviceID:"
- "setLastReceivedReason:"
- "setRateOfAdvicePerHour:"
- "setReason:"
- "setStarted:"
- "setThermalLevel:"
- "setTimeOfBTClassicAdvice:"
- "setTimeOfWiFiAdvice:"
- "setTimeSinceLastAdvice:"
- "setTotalCountForBTClassicAdvice:"
- "setTotalCountForNonDefaultAdvice:"
- "setTotalCountForWiFiAdvice:"
- "setTotalDurationForBTClassicAdvice:"
- "setTotalDurationForWiFiAdvice:"
- "setTotalIntervalForNonDefaultAdvice:"
- "setTotalReceivedUpdates:"
- "setUpdateBlock:"
- "setWifiAdviceMonitorTimerSource:"
- "thermalLevel"
- "timeOfBTClassicAdvice"
- "timeOfWiFiAdvice"
- "totalCountForBTClassicAdvice"
- "totalCountForNonDefaultAdvice"
- "totalCountForWiFiAdvice"
- "totalDurationForBTClassicAdvice"
- "totalDurationForWiFiAdvice"
- "totalIntervalForNonDefaultAdvice"
- "totalReceivedUpdates"
- "updateBlock"
- "v24@0:8d16"
- "wifiAdviceMonitorTimerSource"
- "\xd1"
```
