## nanosystemsettingsd

> `/System/Library/PrivateFrameworks/NanoSystemSettings.framework/nanosystemsettingsd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`

```diff

-383.0.0.0.0
-  __TEXT.__text: 0x1d384
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_stubs: 0x3e00
-  __TEXT.__objc_methlist: 0x1c7c
-  __TEXT.__const: 0xea
-  __TEXT.__oslogstring: 0x2789
+386.0.0.0.0
+  __TEXT.__text: 0x21900
+  __TEXT.__auth_stubs: 0x9c0
+  __TEXT.__objc_stubs: 0x4480
+  __TEXT.__objc_methlist: 0x1ef4
+  __TEXT.__const: 0xf2
+  __TEXT.__oslogstring: 0x3113
   __TEXT.__objc_classname: 0x274
-  __TEXT.__objc_methtype: 0x1473
-  __TEXT.__cstring: 0x18e6
-  __TEXT.__objc_methname: 0x663d
-  __TEXT.__gcc_except_tab: 0xdc
+  __TEXT.__objc_methtype: 0x14dd
+  __TEXT.__cstring: 0x21f7
+  __TEXT.__objc_methname: 0x7147
+  __TEXT.__gcc_except_tab: 0x21c
   __TEXT.__swift5_typeref: 0x15
-  __TEXT.__unwind_info: 0x6a8
-  __DATA_CONST.__const: 0x8a0
-  __DATA_CONST.__cfstring: 0x1400
+  __TEXT.__unwind_info: 0x818
+  __DATA_CONST.__const: 0xb50
+  __DATA_CONST.__cfstring: 0x1600
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x4c8
-  __DATA_CONST.__got: 0x610
-  __DATA_CONST.__auth_ptr: 0x28
-  __DATA.__objc_const: 0x3b08
-  __DATA.__objc_selrefs: 0x17f8
-  __DATA.__objc_ivar: 0x168
+  __DATA_CONST.__auth_got: 0x4f0
+  __DATA_CONST.__got: 0x650
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA.__objc_const: 0x3e28
+  __DATA.__objc_selrefs: 0x19e8
+  __DATA.__objc_ivar: 0x1a0
   __DATA.__objc_data: 0x370
-  __DATA.__data: 0x5c8
+  __DATA.__data: 0x5d0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/ClockKit.framework/ClockKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 553
-  Symbols:   372
-  CStrings:  1549
+  Functions: 661
+  Symbols:   385
+  CStrings:  1727
 
Symbols:
+ _FBSOpenApplicationOptionKeyPromptUnlockDevice
+ _NSSStartSecurePairingRespMsgReadFrom
+ _NSStringFromRBSTaskState
+ _OBJC_CLASS_$_NSSCancelSecurePairingMsg
+ _OBJC_CLASS_$_NSSRequestSecurePairingFromGizmoMsg
+ _OBJC_CLASS_$_NSSSecurePairingAlertStatusMsg
+ _OBJC_CLASS_$_NSSStartSecurePairingMsg
+ _OBJC_CLASS_$_NSSStartSecurePairingRespMsg
+ _OBJC_CLASS_$_RBSProcessMonitor
+ _OBJC_CLASS_$_RBSProcessPredicate
+ _OBJC_CLASS_$_RBSProcessStateDescriptor
+ _RBSTaskStateIsRunning
+ _dispatch_queue_get_label
+ _objc_retain_x28
- __dispatch_main_q
CStrings:
+ "%@?%@=%d"
+ "%s: (%@) is no longer the watched request; ignoring"
+ "%s: (%@) is not the current request; leaving its status delivery alone"
+ "%s: Bridge is no longer running (task state: %{public}@)"
+ "%s: Bridge never reported secure pairing as finished for (%@); dropping the watch"
+ "%s: Bridge went away during request (%@); cancelling on the watch"
+ "%s: Could not find matching replyBlock for identifier: (%@)"
+ "%s: Could not parse incoming protobuf"
+ "%s: Secure pairing response - success: %{BOOL}d, error: %@"
+ "%s: answering with the status held for this request: (%ld)"
+ "%s: cancelling request (%@) at the client's request"
+ "%s: could not parse incoming protobuf; opening the flow without an entry point"
+ "%s: failed to open secure pairing URL (%{public}@) in Bridge"
+ "%s: hasEntryPoint: %{BOOL}d, entryPoint: (%d), bytes: (%lu)"
+ "%s: no longer watching Bridge"
+ "%s: no request identifier; not watching Bridge"
+ "%s: no secure pairing request in flight; nothing to cancel"
+ "%s: no secure pairing request to wait on"
+ "%s: nobody waiting; holding the status"
+ "%s: not watching Bridge; nothing to stop"
+ "%s: opened secure pairing URL (%{public}@) in Bridge (prompt-unlock if locked)"
+ "%s: releasing the client blocked on (%@): %@"
+ "%s: secure pairing finished for (%@); stopping the Bridge watch"
+ "%s: sent CancelSecurePairingMsg for (%@) — identifier: (%@), error: (%@)"
+ "%s: status is not for the current request (%@); dropping it"
+ "%s: status: (%ld), requestIdentifier: (%@)"
+ "%s: watching Bridge for request (%@)"
+ "-[NSSCompanionServer _beginWatchingBridgeForSecurePairingRequest:]"
+ "-[NSSCompanionServer _beginWatchingBridgeForSecurePairingRequest:]_block_invoke_2"
+ "-[NSSCompanionServer _bridgeWentAwayDuringSecurePairingRequest:]"
+ "-[NSSCompanionServer _endSecurePairingAlertStatusReportingForRequest:]"
+ "-[NSSCompanionServer _endWatchingBridgeForSecurePairing]"
+ "-[NSSCompanionServer _failSecurePairingAlertStatusRequestForIdentifier:error:]"
+ "-[NSSCompanionServer _sendCancelSecurePairingForRequest:]"
+ "-[NSSCompanionServer _sendCancelSecurePairingForRequest:]_block_invoke"
+ "-[NSSCompanionServer _startBridgeWatchExpirationTimer:]_block_invoke"
+ "-[NSSCompanionServer awaitSecurePairingAlertStatus:]"
+ "-[NSSCompanionServer awaitSecurePairingAlertStatus:]_block_invoke"
+ "-[NSSCompanionServer cancelSecurePairing:]"
+ "-[NSSCompanionServer cancelSecurePairing:]_block_invoke"
+ "-[NSSCompanionServer getLegalDocuments:]_block_invoke"
+ "-[NSSCompanionServer handleRequestSecurePairingFromGizmoMsg:]"
+ "-[NSSCompanionServer handleSecurePairingAlertStatusMsg:]"
+ "-[NSSCompanionServer handleStartSecurePairingRespMsg:]"
+ "-[NSSCompanionServer recordSoftwareUpdateSpaceFailure:osBeingUpdatedTo:completion:]_block_invoke"
+ "-[NSSCompanionServer securePairingDidFinish:]"
+ "-[NSSCompanionServer securePairingDidFinish:]_block_invoke"
+ "-[NSSCompanionServer startSecurePairing:]"
+ "-[NSSServer service:account:incomingResourceAtURL:metadata:fromID:context:]"
+ "-[NSSWatchFaceCoordinator _watchFacesForCurrentDeviceWithCompletion:]"
+ "-[NSSWatchFaceCoordinator selectWatchFaceIdentifier:forFocusModeIdentifier:completion:]_block_invoke"
+ "/var/mobile/tmp/BridgeDiagnosticLogsIncoming/"
+ "@\"RBSProcessMonitor\""
+ "@32@0:8@16^@24"
+ "AB"
+ "AQ"
+ "Claimed incoming resource from %@ to %@"
+ "Could not claim incoming resource %@ with error: %@; dropping it"
+ "Couldn't list diagnostic log staging directory %@ with error: %@"
+ "Couldn't reclaim orphaned diagnostic log staging directory %@ with error: %@"
+ "Displaced by a newer wait"
+ "Failed to claim file from %@ to %@ with error: %@"
+ "Failed to create %@ directory with error: %@; leaving the claimed log staged at %@"
+ "Failed to create staging directory %@ with error: %@"
+ "Failed to move %@ to %@ with error: %@; leaving the log staged"
+ "Failed to parse secure pairing response"
+ "Incoming resource metadata has no originalFilePath; leaving the claimed log staged at %@"
+ "Launching; \"NanoSystemSettingsDaemon-386\" \"348\""
+ "MindPalaceOnboardingEntryPoint"
+ "Moved file from %@ to %@"
+ "NSSWatchFaceCoordinator was deallocated"
+ "NSSWatchFaceCoordinator was deallocated before the request ran; failing it"
+ "NSSWatchFaceCoordinator was deallocated before the selection ran; failing it"
+ "NTKPersistentFaceCollection finished, calling %lu completion(s)"
+ "NanoRegistry read SLOW: %{public}s took %.3fs"
+ "NanoRegistry read begin: %{public}s (queue: %{public}s)"
+ "NanoRegistry read end: %{public}s (%.3fs)"
+ "No active paired device found"
+ "No active paired device; leaving the claimed log staged at %@"
+ "No secure pairing request is in flight"
+ "Nothing to claim in IDS's temp dir at %@"
+ "Q48@0:8Q16@24@32@?40"
+ "Reclaimed orphaned diagnostic log staging directory %@"
+ "Resetting because the active paired device changed from %{public}@ to %{public}@ (sparing requests from sequence %llu)"
+ "Secure pairing failed on watch"
+ "Secure pairing was cancelled on the companion"
+ "T@\"NSMutableArray\",&,N,V_pendingCompletions"
+ "T@\"NSMutableDictionary\",&,N,V_securePairingAlertStatusRequests"
+ "T@\"NSMutableDictionary\",&,N,V_startSecurePairingReplyTimers"
+ "T@\"NSMutableDictionary\",&,N,V_startSecurePairingRequests"
+ "T@\"NSMutableDictionary\",&,N,V_unreadSecurePairingAlertStatuses"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_notificationQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_registryQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_bridgeWatchExpirationTimer"
+ "T@\"NSString\",C,N,V_bridgeMonitorRequestIdentifier"
+ "T@\"NSString\",C,N,V_currentSecurePairingRequestIdentifier"
+ "T@\"RBSProcessMonitor\",&,N,V_bridgeProcessMonitor"
+ "TQ,N,V_activeDeviceResetSequenceCutoff"
+ "The secure pairing request this was waiting on has ended"
+ "[obliterateGizmo] no active paired device; cannot unpair"
+ "_activeDeviceRefreshQueued"
+ "_activeDeviceResetSequenceCutoff"
+ "_applyActivePairedDeviceID:sequenceCutoff:"
+ "_beginWatchingBridgeForSecurePairingRequest:"
+ "_bridgeMonitorRequestIdentifier"
+ "_bridgeProcessMonitor"
+ "_bridgeWatchExpirationTimer"
+ "_bridgeWentAwayDuringSecurePairingRequest:"
+ "_cancelSecurePairingRequest:answeringClientWith:"
+ "_currentSecurePairingRequestIdentifier"
+ "_endSecurePairingAlertStatusReportingForRequest:"
+ "_endWatchingBridgeForSecurePairing"
+ "_failSecurePairingAlertStatusRequestForIdentifier:error:"
+ "_invalidateRequestsBelowSequence:requests:timers:invoke:"
+ "_notificationQueue"
+ "_pendingCompletions"
+ "_registryQueue"
+ "_requestSequence"
+ "_securePairingAlertStatusRequests"
+ "_sendCancelSecurePairingForRequest:"
+ "_startBridgeWatchExpirationTimer:"
+ "_startSecurePairingReplyTimers"
+ "_startSecurePairingRequests"
+ "_unreadSecurePairingAlertStatuses"
+ "_watchFacesForCurrentDeviceWithCompletion:"
+ "absoluteString"
+ "activeDeviceResetSequenceCutoff"
+ "awaitSecurePairingAlertStatus:"
+ "bridge://presentation/securePairing"
+ "bridgeMonitorRequestIdentifier"
+ "bridgeProcessMonitor"
+ "bridgeWatchExpirationTimer"
+ "cancelSecurePairing"
+ "cancelSecurePairing:"
+ "claimIncomingResource:withError:"
+ "com.apple.nanosystemsettings.notifications"
+ "com.apple.nanosystemsettings.registry"
+ "com.apple.nanosystemsettings.watchface"
+ "currentSecurePairingRequestIdentifier"
+ "descriptor"
+ "entryPoint"
+ "fileURLWithPath:"
+ "handleRequestSecurePairingFromGizmoMsg:"
+ "handleSecurePairingAlertStatusMsg:"
+ "handleStartSecurePairingRespMsg:"
+ "hasEntryPoint"
+ "hasRequestIdentifier"
+ "invalidate"
+ "isDefaultPairedDeviceNearbyInDevices:"
+ "kNSSRequestSendSequenceAssociatedObjectKey"
+ "linkStagedFileForViewing:metadata:withError:"
+ "monitorWithConfiguration:"
+ "notificationQueue"
+ "openSensitiveURL:withOptions:"
+ "pendingCompletions"
+ "predicateMatchingBundleIdentifier:"
+ "reclaimOrphanedDiagnosticLogStagingDirectories"
+ "refreshActivePairedDeviceAndResetIfChanged"
+ "registryQueue"
+ "requestIdentifier"
+ "requestSecurePairing"
+ "securePairingAlertStatusRequests"
+ "securePairingDidFinish:"
+ "selectWatchFaceIdentifier:forFocusModeIdentifier:completion:"
+ "setActiveDeviceResetSequenceCutoff:"
+ "setBridgeMonitorRequestIdentifier:"
+ "setBridgeProcessMonitor:"
+ "setBridgeWatchExpirationTimer:"
+ "setCurrentSecurePairingRequestIdentifier:"
+ "setExpireAt:"
+ "setPendingCompletions:"
+ "setPredicates:"
+ "setRequestIdentifier:"
+ "setSecurePairingAlertStatusRequests:"
+ "setStartSecurePairingReplyTimers:"
+ "setStartSecurePairingRequests:"
+ "setStateDescriptor:"
+ "setUnreadSecurePairingAlertStatuses:"
+ "setUpdateHandler:"
+ "setValues:"
+ "setWatchFaceIdentifier committed - error: %@"
+ "startSecurePairing"
+ "startSecurePairing:"
+ "startSecurePairingReplyTimers"
+ "startSecurePairingRequests"
+ "startsecurepairing"
+ "state"
+ "status"
+ "taskState"
+ "unreadSecurePairingAlertStatuses"
+ "unsignedLongLongValue"
+ "v16@?0@\"<RBSProcessMonitorConfiguring>\"8"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?q@\"NSError\">16"
+ "v32@?0@\"RBSProcessMonitor\"8@\"RBSProcessHandle\"16@\"RBSProcessStateUpdate\"24"
+ "v32@?0@8@16^B24"
+ "warmNanoRegistry"
- "-[NSSWatchFaceCoordinator selectWatchFaceIdentifier:forFocusModeIdentifier:]"
- "-[NSSWatchFaceCoordinator watchFacesForCurrentDeviceWithCompletion:]"
- "@?"
- "@?16@0:8"
- "Can't copy file; transferred file path and/or destination path is nil\nTransferred File: %@\nNew Path: %@"
- "Copied file from %@ to %@"
- "Failed to copy file from %@ to %@ with error: %@"
- "Failed to create %@ directory with error: %@"
- "Launching; \"NanoSystemSettingsDaemon-383\" \"1470\""
- "NTKPersistentFaceCollection finished, calling completion"
- "Resetting because the active paired device changed from %{public}@ to %{public}@"
- "T@?,C,N,V_completion"
- "_completion"
- "_resetIfTheActivePairedDeviceChanges"
- "allValues"
- "completion"
- "linkFileForViewing:metadata:withError:"
- "selectWatchFaceIdentifier:forFocusModeIdentifier:"
- "setCompletion:"
```
