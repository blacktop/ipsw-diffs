## mobilerepaird

> `/usr/libexec/mobilerepaird`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-1307.60.20.0.0
-  __TEXT.__text: 0x201e0
-  __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_stubs: 0x3b40
-  __TEXT.__objc_methlist: 0x1a74
-  __TEXT.__const: 0x172
-  __TEXT.__gcc_except_tab: 0xa10
-  __TEXT.__objc_methname: 0x4781
-  __TEXT.__cstring: 0x444d
-  __TEXT.__oslogstring: 0x3626
-  __TEXT.__objc_classname: 0x5af
-  __TEXT.__objc_methtype: 0xe63
+1307.60.23.0.0
+  __TEXT.__text: 0x25340
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_stubs: 0x44e0
+  __TEXT.__objc_methlist: 0x1d44
+  __TEXT.__const: 0x1a2
+  __TEXT.__gcc_except_tab: 0xca0
+  __TEXT.__objc_methname: 0x528a
+  __TEXT.__cstring: 0x4692
+  __TEXT.__oslogstring: 0x4e4a
+  __TEXT.__objc_classname: 0x5cf
+  __TEXT.__objc_methtype: 0xf0f
   __TEXT.__ustring: 0x12a
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x3b
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xa18
-  __DATA_CONST.__const: 0xdb0
-  __DATA_CONST.__cfstring: 0x41e0
-  __DATA_CONST.__objc_classlist: 0x170
+  __TEXT.__unwind_info: 0xbf8
+  __DATA_CONST.__const: 0x10c0
+  __DATA_CONST.__cfstring: 0x43e0
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x4e8
-  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__auth_got: 0x510
+  __DATA_CONST.__got: 0x4f0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x3128
-  __DATA.__objc_selrefs: 0x11e0
-  __DATA.__objc_ivar: 0x148
-  __DATA.__objc_data: 0xec0
+  __DATA.__objc_const: 0x33b0
+  __DATA.__objc_selrefs: 0x1460
+  __DATA.__objc_ivar: 0x170
+  __DATA.__objc_data: 0xf10
   __DATA.__data: 0x4c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BatteryDischarge.framework/BatteryDischarge
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
+  - /System/Library/PrivateFrameworks/DeviceConfiguration.framework/DeviceConfiguration
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 685
-  Symbols:   299
-  CStrings:  1699
+  Functions: 793
+  Symbols:   309
+  CStrings:  1901
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_CRShipModeServerNotifier
+ _OBJC_CLASS_$_DCSystemConsumer
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
CStrings:
+ ""
+ " — at the deadline"
+ " — capped, will re-derive"
+ "@\"DCSubscriptionToken\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@24@0:8^@16"
+ "CRShipModeDeviceConfigurationConsumer"
+ "CRShipModeDeviceConfigurationConsumer: %@ changed"
+ "CRShipModeDeviceConfigurationConsumer: a ship-mode action did not finish within %.0fs; releasing it so later declaration changes are not blocked"
+ "CRShipModeDeviceConfigurationConsumer: a ship-mode action is still running; the latest declared value will be applied when it finishes"
+ "CRShipModeDeviceConfigurationConsumer: activateShipMode: already in ship mode with partner claim %{public}@; cannot ship unclaimed — leaving state unchanged"
+ "CRShipModeDeviceConfigurationConsumer: activateShipMode: claim check timed out after %.0fs; shipping without a claim check"
+ "CRShipModeDeviceConfigurationConsumer: activateShipMode: clearing partner claim %{public}@ before shipping unclaimed"
+ "CRShipModeDeviceConfigurationConsumer: activateShipMode: marker says already in ship mode; nothing to do (no server contact)"
+ "CRShipModeDeviceConfigurationConsumer: activateShipMode: server already reports in ship mode (no claim); nothing to do"
+ "CRShipModeDeviceConfigurationConsumer: activateShipMode: status fetch failed (%{public}@); shipping without a claim check"
+ "CRShipModeDeviceConfigurationConsumer: applying ship-mode=%{public}@"
+ "CRShipModeDeviceConfigurationConsumer: applying the declaration change that arrived meanwhile"
+ "CRShipModeDeviceConfigurationConsumer: armed in-process undo retry (in %.0fs)"
+ "CRShipModeDeviceConfigurationConsumer: armed undo-retry task (in %.0fs)"
+ "CRShipModeDeviceConfigurationConsumer: cannot undo — active partner claim %{public}@"
+ "CRShipModeDeviceConfigurationConsumer: clearing partner claim failed: %{public}@"
+ "CRShipModeDeviceConfigurationConsumer: deactivateShipMode: marker says not in ship mode; releasing any local lock only (no server contact)"
+ "CRShipModeDeviceConfigurationConsumer: deactivateShipMode: marker unknown and the battery is not derated; nothing to undo (no server contact)"
+ "CRShipModeDeviceConfigurationConsumer: disarmed undo-retry task"
+ "CRShipModeDeviceConfigurationConsumer: disengageBatteryShipChargeLimit failed: %{public}@"
+ "CRShipModeDeviceConfigurationConsumer: failed to register undo-retry task"
+ "CRShipModeDeviceConfigurationConsumer: failed to subscribe to %@: %{public}@"
+ "CRShipModeDeviceConfigurationConsumer: fetchShipModeStatus failed: %{public}@"
+ "CRShipModeDeviceConfigurationConsumer: getConfigurationSyncFor failed: %{public}@"
+ "CRShipModeDeviceConfigurationConsumer: in-process undo retry already pending"
+ "CRShipModeDeviceConfigurationConsumer: in-process undo retry firing"
+ "CRShipModeDeviceConfigurationConsumer: in-process undo retry skipped; task attempt running"
+ "CRShipModeDeviceConfigurationConsumer: marker is not in-ship-mode but the lock is still engaged; finishing the undo (marker %{public}s)"
+ "CRShipModeDeviceConfigurationConsumer: no shipModeDesiredState set; leaving current ship-mode state unchanged"
+ "CRShipModeDeviceConfigurationConsumer: retrying pending undo"
+ "CRShipModeDeviceConfigurationConsumer: server already reports not in ship mode; skipping the disable notify"
+ "CRShipModeDeviceConfigurationConsumer: server declined undo (will retry): %{public}@"
+ "CRShipModeDeviceConfigurationConsumer: server reports in ship mode; setting the marker to TRUE"
+ "CRShipModeDeviceConfigurationConsumer: server reports not in ship mode; setting the marker to FALSE"
+ "CRShipModeDeviceConfigurationConsumer: setTaskExpiredWithRetryAfter %.0fs failed: %{public}@; completing instead"
+ "CRShipModeDeviceConfigurationConsumer: submitDischarge failed: %{public}@"
+ "CRShipModeDeviceConfigurationConsumer: undo retry in %.0fs (deadline already passed; server refused anyway)"
+ "CRShipModeDeviceConfigurationConsumer: undo retry in %.0fs (no anchor or no server timer)"
+ "CRShipModeDeviceConfigurationConsumer: undo retry in %.0fs (server timer %.0fs, remaining %.0fs%s)"
+ "CRShipModeDeviceConfigurationConsumer: undo retry skipped; a ship-mode action is already running"
+ "CRShipModeDeviceConfigurationConsumer: undo retry task backed off %.0fs"
+ "CRShipModeDeviceConfigurationConsumer: undo retry task expired"
+ "CRShipModeDeviceConfigurationConsumer: undo still pending; task will back off %.0fs"
+ "CRShipModeDeviceConfigurationConsumer: undo-retry %{public}s failed: %{public}@"
+ "CRShipModeDeviceConfigurationConsumer: undo-retry cancel failed: %{public}@"
+ "CRShipModeDeviceConfigurationConsumer: unexpected type for %@: %@"
+ "CRShipModeDeviceConfigurationConsumer: unknown ShipModeTimerUnit %{public}@"
+ "CRShipModeDeviceConfigurationConsumer: unknown ship-mode value %{public}@"
+ "CRShipModeHelper: fetchShipModeResumeState → %{public}s (eligible=%d marker=%d)"
+ "CRShipModeHelper: fetchShipModeUndoInProgress → %d"
+ "CRShipModeHelper: ship lock marker cleared, keeping the session's entry timestamp/provenance (outcome of a server request not known)"
+ "CRShipModeHelper: ship lock marker set to IN ship mode (server confirmed TRUE, or definitely refused the request)"
+ "CRShipModeHelper: ship lock marker set to NOT in ship mode"
+ "CRShipModeHelper: undo in progress = %d"
+ "CRShipModeLockMarkerWrittenAt"
+ "CRShipModeOperationScheduler: bare notify for %{public}@ confirmed disabled; recording FALSE"
+ "CRShipModeOperationScheduler: bare notify for %{public}@ confirmed enabled; recording TRUE"
+ "CRShipModeOperationScheduler: cancelled operation %{public}@ at its enable notify; the server's ship-mode bit is no longer known"
+ "CRShipModeOperationScheduler: disable notify for %{public}@ definitely failed; restoring the confirmed in-ship-mode marker cleared before the POST"
+ "CRShipModeOperationScheduler: lost request did not change the server; recording FALSE"
+ "CRShipModeOperationScheduler: lost request left the server in ship mode with the lock off; recording TRUE"
+ "CRShipModeOperationScheduler: network available; verifying the outcome of a lost ship-mode request"
+ "CRShipModeOperationScheduler: notify for %{public}@ abandoned: the operation was cancelled or replaced before the POST"
+ "CRShipModeOperationScheduler: notify for %{public}@ failed ambiguously (the server may have applied it); verifying live"
+ "CRShipModeOperationScheduler: status check did not get a reply within %lus"
+ "CRShipModeOperationScheduler: status check failed: %{public}@"
+ "CRShipModeUndoInProgress"
+ "FALSE: locally"
+ "None"
+ "Q"
+ "Q20@0:8B16"
+ "T@\"DCSubscriptionToken\",&,N,V_subscriptionToken"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_undoRetryTimer"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_undoRetryTransaction"
+ "T@?,C,N,V_exclusiveWatchdogReport"
+ "TB,N,V_exclusiveInFlight"
+ "TB,N,V_exclusivePending"
+ "TB,N,V_notifyAuthorizationRevoked"
+ "TB,N,V_notifyWasShipModeTransition"
+ "TB,N,V_undoRetryInTaskContext"
+ "TQ,N,V_exclusiveGeneration"
+ "Td,N,V_pendingUndoRetryDelay"
+ "_armInProcessUndoRetryAfter:"
+ "_armUndoRetryWithServerResponse:"
+ "_beginExclusiveQueueingIfBusy:"
+ "_disarmUndoRetry"
+ "_endExclusive:"
+ "_exclusiveGeneration"
+ "_exclusiveInFlight"
+ "_exclusivePending"
+ "_exclusiveWatchdogReport"
+ "_invalidateShipModeStateAfterAmbiguousNotifyFor:"
+ "_notifyAuthorizationRevoked"
+ "_notifyWasShipModeTransition"
+ "_pendingUndoRetryDelay"
+ "_recordServerShipModeTruth:"
+ "_registerUndoRetryTask"
+ "_releaseShipLockAfterFailedNotifyFor:stateUncertain:"
+ "_scheduleLostOutcomeVerificationActivity"
+ "_sendNotifyPOSTForOp:opID:authorizedByShipMode:transition:"
+ "_submitShipModeDischargeThen:"
+ "_subscriptionToken"
+ "_undoRetryDelayForServerResponse:"
+ "_undoRetryInTaskContext"
+ "_undoRetryTimer"
+ "_undoRetryTransaction"
+ "_verifyLostOutcomeViaServer:"
+ "activateShipMode"
+ "activateShipModeWithCompletion:"
+ "applyCurrentConfiguration"
+ "cancelTaskRequestWithIdentifier:error:"
+ "chainFailedWithReply:"
+ "checkShipModeStatusAndReconcileEnabled:disabled:indeterminate:activity:"
+ "clearShipModeLockMarkerKeepingSession"
+ "com.apple.CoreRepair"
+ "com.apple.mobilerepair.shipmode.desiredstate"
+ "com.apple.mobilerepaird.shipmode.status-check.arbiter"
+ "com.apple.mobilerepaird.shipmode.undo-retry"
+ "com.apple.mobilerepaird.shipmode.verify-outcome"
+ "currentDesiredStateWithError:"
+ "d24@0:8@16"
+ "dateWithTimeIntervalSince1970:"
+ "day"
+ "deactivateShipMode"
+ "deactivateShipModeWithCompletion:"
+ "device.power.battery-ship-mode.notification"
+ "doubleValue"
+ "exclusiveGeneration"
+ "exclusiveInFlight"
+ "exclusivePending"
+ "exclusiveWatchdogReport"
+ "fetchShipModeStatusWithCompletion:"
+ "fetchShipModeUndoInProgressWithReply:"
+ "getConfigurationSyncFor returned nil with no error"
+ "getConfigurationSyncFor:error:"
+ "hasPrefix:"
+ "hour"
+ "initWithIdentifier:"
+ "isShipModeUndoInProgress"
+ "marker-not-in-ship-mode"
+ "minute"
+ "normal"
+ "notifyAuthorizationRevoked"
+ "notifyErrorLeavesServerStateUncertain:"
+ "notifyWasShipModeTransition"
+ "objectForKey:"
+ "pendingUndoRetryDelay"
+ "postShipModeDDMStatusChangedNotification"
+ "reconcileUncertainShipModeStateIfNeeded"
+ "recordInShipModeViaTradeIn:"
+ "recordNotInShipMode"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "restoreInShipMode"
+ "retryUndoIfPending"
+ "retryUndoIfPendingWithCompletion:"
+ "second"
+ "setExclusiveGeneration:"
+ "setExclusiveInFlight:"
+ "setExclusivePending:"
+ "setExclusiveWatchdogReport:"
+ "setExpirationHandler:"
+ "setNotifyAuthorizationRevoked:"
+ "setNotifyWasShipModeTransition:"
+ "setPendingUndoRetryDelay:"
+ "setScheduleAfter:"
+ "setShipModeUndoInProgress:"
+ "setShouldWakeDevice:"
+ "setSubscriptionToken:"
+ "setTaskCompleted"
+ "setTaskExpiredWithRetryAfter:error:"
+ "setTrySchedulingBefore:"
+ "setUndoRetryInTaskContext:"
+ "setUndoRetryTimer:"
+ "setUndoRetryTransaction:"
+ "sharedConsumer"
+ "sharedNotifier"
+ "shipModeDesiredState"
+ "shipModeDesiredState was not a string"
+ "shipModeLocalState"
+ "shipModeLockMarkerWrittenAt"
+ "shipModeTimerDuration"
+ "shipModeTimerUnit"
+ "shiplock-eval(daemon-start): lock engaged and a Prepare to Ship operation is in flight; it resumes on its own — not treating the lock as orphaned"
+ "shiplock-eval(daemon-start): marker says not in ship mode but lock engaged; releasing locally (no server query)"
+ "shiplock-eval: server reports ship mode disabled but a Prepare to Ship operation is in flight; it owns the lock — leaving it engaged"
+ "shippable"
+ "start"
+ "submit"
+ "submitShipModeNotificationWithEnabled:deviceError:partnerID:completion:"
+ "submitShipModeNotificationWithEnabled:deviceError:partnerID:markUnknownBeforeSend:reply:"
+ "submitTaskRequest:error:"
+ "subscribeToChangesFor:error:changeHandler:"
+ "subscriptionToken"
+ "taskRequestForIdentifier:"
+ "timeIntervalSinceNow"
+ "undoRetryInTaskContext"
+ "undoRetryTimer"
+ "undoRetryTransaction"
+ "unknown: via the server"
+ "update"
+ "updateTaskRequest:error:"
+ "v16@?0@\"BGSystemTask\"8"
+ "v16@?0@\"NSSet\"8"
+ "v28@0:8@16B24"
+ "v40@0:8@16@24B32B36"
+ "v44@0:8B16B20@24B32@?36"
+ "v48@0:8@?16@?24@?32@40"
- "CRShipModeHelper: fetchShipModeResumeState → None (eligible=%d marker=%d)"
- "TB,N,V_notifyAuthorizedByShipMode"
- "_notifyAuthorizedByShipMode"
- "_releaseShipLockAfterFailedNotifyFor:"
- "com.apple.mobilerepaird.shipmode.server-check.arbiter"
- "isShipModeLockMarkerPresent"
- "notifyAuthorizedByShipMode"
- "recordShipModeLockMarkerPresentViaTradeIn:"
- "setNotifyAuthorizedByShipMode:"
- "shiplock-eval: server status query failed: %{public}@; deferring for XPC retry"
- "shiplock-eval: server status query reply did not arrive within %lus; deferring for XPC retry"
```
