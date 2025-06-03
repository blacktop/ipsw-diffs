## CoordinationCore

> `/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore`

```diff

-196.11.1.0.0
-  __TEXT.__text: 0xbf66c
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x81f8
+196.21.1.0.0
+  __TEXT.__text: 0xc485c
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_methlist: 0x84c8
   __TEXT.__const: 0x278
-  __TEXT.__gcc_except_tab: 0x2f24
-  __TEXT.__cstring: 0x27ba
-  __TEXT.__oslogstring: 0x8e96
-  __TEXT.__unwind_info: 0x2fec
-  __TEXT.__objc_classname: 0x1739
-  __TEXT.__objc_methname: 0x1203a
-  __TEXT.__objc_methtype: 0x3992
-  __TEXT.__objc_stubs: 0xd5e0
-  __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0x3d58
-  __DATA_CONST.__objc_classlist: 0x590
+  __TEXT.__gcc_except_tab: 0x2fbc
+  __TEXT.__cstring: 0x2841
+  __TEXT.__oslogstring: 0x94b8
+  __TEXT.__unwind_info: 0x3104
+  __TEXT.__objc_classname: 0x175f
+  __TEXT.__objc_methname: 0x1286e
+  __TEXT.__objc_methtype: 0x39f7
+  __TEXT.__objc_stubs: 0xdc20
+  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__const: 0x3d60
+  __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x218
+  __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf600
-  __DATA_CONST.__objc_selrefs: 0x3af0
+  __DATA_CONST.__objc_const: 0xfaa0
+  __DATA_CONST.__objc_selrefs: 0x3ca8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__objc_const: 0x40a8
-  __AUTH_CONST.__cfstring: 0x2420
+  __AUTH_CONST.__objc_const: 0x40f0
+  __AUTH_CONST.__cfstring: 0x2560
   __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x470
-  __AUTH.__objc_data: 0x1fe0
+  __AUTH_CONST.__auth_got: 0x4a0
+  __AUTH.__objc_data: 0x2030
   __DATA.__objc_protorefs: 0x88
-  __DATA.__objc_classrefs: 0x748
-  __DATA.__objc_superrefs: 0x410
-  __DATA.__objc_ivar: 0x9b0
-  __DATA.__data: 0x1920
+  __DATA.__objc_classrefs: 0x768
+  __DATA.__objc_superrefs: 0x418
+  __DATA.__objc_ivar: 0xa08
+  __DATA.__data: 0x1980
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x17c0
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HomeKit.framework/HomeKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 69E5BB40-9122-3826-A068-050C91246696
-  Functions: 4083
-  Symbols:   13214
-  CStrings:  5228
+  UUID: 2FA26329-AE02-30EB-95C1-5B7763EC4ABE
+  Functions: 4167
+  Symbols:   13485
+  CStrings:  5382
 
Symbols:
+ -[COAlarmReadRequest eTag]
+ -[COAlarmReadRequest setETag:]
+ -[COAlarmReadResponse initNotModifiedWithDeletes:]
+ -[COAlarmReadResponse notModified]
+ -[COConstituent _timeAwareUUID]
+ -[COCoordinationService _setupIDSServerBag]
+ -[COCoordinationService idsServerBagDidUpdate:]
+ -[COCoordinationService idsServerBag]
+ -[COCoordinationService setIdsServerBag:]
+ -[COElectionInfo hasSameGenerationAndLeader:]
+ -[COIDSServerBag .cxx_destruct]
+ -[COIDSServerBag _onqueue_configureTimer]
+ -[COIDSServerBag _onqueue_serverBagNumberValueForKey:]
+ -[COIDSServerBag _onqueue_serverBagValueForKey:]
+ -[COIDSServerBag _onqueue_timerFired]
+ -[COIDSServerBag _onqueue_updateCachedValuesWithServerValues]
+ -[COIDSServerBag _withLock:]
+ -[COIDSServerBag configure]
+ -[COIDSServerBag currentTimerDelay]
+ -[COIDSServerBag delegate]
+ -[COIDSServerBag dispatchQueue]
+ -[COIDSServerBag idsServerBag]
+ -[COIDSServerBag init]
+ -[COIDSServerBag isFastFoldEnabled]
+ -[COIDSServerBag isIPDiffingEnabled]
+ -[COIDSServerBag keySuffix]
+ -[COIDSServerBag refreshTimer]
+ -[COIDSServerBag setCurrentTimerDelay:]
+ -[COIDSServerBag setDelegate:]
+ -[COIDSServerBag setFastFoldEnabled:]
+ -[COIDSServerBag setIpDiffing:]
+ -[COIDSServerBag setIpDiffingEnabled:]
+ -[COMeshAlarmAddOn _broadcastMerge:withTruth:]
+ -[COMeshAlarmAddOn _finishMerge:]
+ -[COMeshAlarmAddOn _finishMerge:].cold.1
+ -[COMeshAlarmAddOn _finishMerge:].cold.2
+ -[COMeshAlarmAddOn _reloadIndexWithCompletion:]
+ -[COMeshAlarmAddOn alarmIndex]
+ -[COMeshAlarmAddOn mergeAlarms]
+ -[COMeshAlarmAddOn setAlarmIndex:]
+ -[COMeshAlarmAddOn setMergeAlarms:]
+ -[COMeshController _setupCoordinationPrefsObserver]
+ -[COMeshController _tearDownCoordinationPrefsObserver]
+ -[COMeshController coordinationDefaults]
+ -[COMeshController observeValueForKeyPath:ofObject:change:context:]
+ -[COMeshController setCoordinationDefaults:]
+ -[COMeshTimerAddOn _broadcastMerge:withTruth:]
+ -[COMeshTimerAddOn _finishMerge:]
+ -[COMeshTimerAddOn _finishMerge:].cold.1
+ -[COMeshTimerAddOn _finishMerge:].cold.2
+ -[COMeshTimerAddOn _reloadIndexWithCompletion:]
+ -[COMeshTimerAddOn mergeTimers]
+ -[COMeshTimerAddOn setMergeTimers:]
+ -[COMeshTimerAddOn setTimerIndex:]
+ -[COMeshTimerAddOn timerIndex]
+ -[CONodeController _electionInfoByDiffingCurrentElectionInfo:]
+ -[CONodeController _updateKnownDiscovery:]
+ -[CONodeController knownDiscoveryRecords]
+ -[CONodeController setKnownDiscoveryRecords:]
+ -[CONodeManager fast_fold_nodeController:didReceiveElectionCmd:withCompletionHandler:]
+ -[CORapportTransport activationHandler]
+ -[CORapportTransport isActivated]
+ -[CORapportTransport setActivationHandler:]
+ -[CORapportTransport sourceHasBeenActivated]
+ -[COTimerReadRequest eTag]
+ -[COTimerReadRequest setETag:]
+ -[COTimerReadResponse initNotModifiedWithDeletes:]
+ -[COTimerReadResponse notModified]
+ GCC_except_table100
+ GCC_except_table147
+ GCC_except_table155
+ GCC_except_table158
+ GCC_except_table166
+ GCC_except_table168
+ GCC_except_table171
+ GCC_except_table187
+ GCC_except_table191
+ GCC_except_table192
+ GCC_except_table195
+ GCC_except_table197
+ GCC_except_table210
+ GCC_except_table213
+ GCC_except_table216
+ GCC_except_table219
+ GCC_except_table225
+ GCC_except_table246
+ GCC_except_table262
+ GCC_except_table55
+ GCC_except_table67
+ GCC_except_table73
+ GCC_except_table77
+ GCC_except_table80
+ GCC_except_table81
+ GCC_except_table83
+ GCC_except_table94
+ _CC_SHA1_Final
+ _CC_SHA1_Init
+ _CC_SHA1_Update
+ _COCoordinationServiceDefaultsFastFoldEnabled
+ _COCoordinationServiceDefaultsIPDiffingEnabled
+ _IsAppleInternalBuild
+ _OBJC_CLASS_$_CODefaults
+ _OBJC_CLASS_$_COIDSServerBag
+ _OBJC_CLASS_$_IDSServerBag
+ _OBJC_CLASS_$_SKPresenceOptions
+ _OBJC_IVAR_$_COAlarmReadRequest._eTag
+ _OBJC_IVAR_$_COAlarmReadResponse._notModified
+ _OBJC_IVAR_$_COCoordinationService._idsServerBag
+ _OBJC_IVAR_$_COIDSServerBag._currentTimerDelay
+ _OBJC_IVAR_$_COIDSServerBag._delegate
+ _OBJC_IVAR_$_COIDSServerBag._dispatchQueue
+ _OBJC_IVAR_$_COIDSServerBag._fastFoldEnabled
+ _OBJC_IVAR_$_COIDSServerBag._idsServerBag
+ _OBJC_IVAR_$_COIDSServerBag._ipDiffingEnabled
+ _OBJC_IVAR_$_COIDSServerBag._keySuffix
+ _OBJC_IVAR_$_COIDSServerBag._lock
+ _OBJC_IVAR_$_COIDSServerBag._refreshTimer
+ _OBJC_IVAR_$_COMeshAlarmAddOn._alarmIndex
+ _OBJC_IVAR_$_COMeshAlarmAddOn._mergeAlarms
+ _OBJC_IVAR_$_COMeshController._coordinationDefaults
+ _OBJC_IVAR_$_COMeshTimerAddOn._mergeTimers
+ _OBJC_IVAR_$_COMeshTimerAddOn._timerIndex
+ _OBJC_IVAR_$_CONodeController._expectedRegisteredCommandCount
+ _OBJC_IVAR_$_CONodeController._knownDiscoveryRecords
+ _OBJC_IVAR_$_CORapportTransport._activationHandler
+ _OBJC_IVAR_$_COTimerReadRequest._eTag
+ _OBJC_IVAR_$_COTimerReadResponse._notModified
+ _OBJC_METACLASS_$_COIDSServerBag
+ _OUTLINED_FUNCTION_22
+ __OBJC_$_INSTANCE_METHODS_COIDSServerBag
+ __OBJC_$_INSTANCE_VARIABLES_COIDSServerBag
+ __OBJC_$_PROP_LIST_COIDSServerBag
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_COIDSServerBagDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_COIDSServerBagDelegate
+ __OBJC_$_PROTOCOL_REFS_COIDSServerBagDelegate
+ __OBJC_CLASS_RO_$_COIDSServerBag
+ __OBJC_LABEL_PROTOCOL_$_COIDSServerBagDelegate
+ __OBJC_METACLASS_RO_$_COIDSServerBag
+ __OBJC_PROTOCOL_$_COIDSServerBagDelegate
+ ___24-[COMeshController stop]_block_invoke.70
+ ___24-[COMeshController stop]_block_invoke.71
+ ___24-[COMeshController stop]_block_invoke_2.73
+ ___25-[COMeshController start]_block_invoke.69
+ ___27-[COIDSServerBag configure]_block_invoke
+ ___31-[COIDSServerBag setIpDiffing:]_block_invoke
+ ___33-[COMeshAlarmAddOn _finishMerge:]_block_invoke
+ ___33-[COMeshAlarmAddOn _finishMerge:]_block_invoke.136
+ ___33-[COMeshAlarmAddOn _finishMerge:]_block_invoke.138
+ ___33-[COMeshAlarmAddOn _finishMerge:]_block_invoke_2
+ ___33-[COMeshAlarmAddOn _finishMerge:]_block_invoke_3
+ ___33-[COMeshTimerAddOn _finishMerge:]_block_invoke
+ ___33-[COMeshTimerAddOn _finishMerge:]_block_invoke.142
+ ___33-[COMeshTimerAddOn _finishMerge:]_block_invoke.144
+ ___33-[COMeshTimerAddOn _finishMerge:]_block_invoke_2
+ ___33-[COMeshTimerAddOn _finishMerge:]_block_invoke_3
+ ___35-[COIDSServerBag isFastFoldEnabled]_block_invoke
+ ___36-[COIDSServerBag isIPDiffingEnabled]_block_invoke
+ ___37-[COIDSPresence _usersChangedInHome:]_block_invoke.38.cold.1
+ ___37-[COIDSPresence _usersChangedInHome:]_block_invoke.40
+ ___37-[COIDSPresence _usersChangedInHome:]_block_invoke.41
+ ___37-[COIDSPresence _usersChangedInHome:]_block_invoke.41.cold.1
+ ___37-[COIDSPresence _usersChangedInHome:]_block_invoke.41.cold.2
+ ___37-[COIDSServerBag setFastFoldEnabled:]_block_invoke
+ ___37-[COMeshController sendNotification:]_block_invoke.83
+ ___38-[COIDSPresence _synchronizePresence:]_block_invoke.35
+ ___38-[COIDSPresence _synchronizePresence:]_block_invoke.35.cold.1
+ ___38-[COIDSPresence _synchronizePresence:]_block_invoke.35.cold.2
+ ___38-[COIDSPresence _synchronizePresence:]_block_invoke.35.cold.3
+ ___38-[COIDSPresence _synchronizePresence:]_block_invoke.36
+ ___39-[COMeshController _logElectionSummary]_block_invoke.122
+ ___39-[COMeshController _logElectionSummary]_block_invoke.123
+ ___39-[COMeshController sendCommand:toPeer:]_block_invoke.79
+ ___39-[COMeshController sendCommand:toPeer:]_block_invoke.79.cold.1
+ ___41-[COIDSServerBag _onqueue_configureTimer]_block_invoke
+ ___42-[COMeshController _processQueuedCommands]_block_invoke.88
+ ___42-[COMeshController _processQueuedCommands]_block_invoke.90
+ ___42-[COMeshController _processQueuedCommands]_block_invoke_2.89
+ ___42-[COMeshController _processQueuedCommands]_block_invoke_2.91
+ ___43-[COCoordinationService _continueMigration]_block_invoke.36
+ ___43-[COMeshAlarmAddOn addAlarm:member:client:]_block_invoke.191
+ ___43-[COMeshAlarmAddOn addAlarm:member:client:]_block_invoke.191.cold.1
+ ___43-[COMeshAlarmAddOn addAlarm:member:client:]_block_invoke.192
+ ___43-[COMeshTimerAddOn addTimer:client:member:]_block_invoke.154
+ ___43-[COMeshTimerAddOn addTimer:client:member:]_block_invoke.154.cold.1
+ ___43-[COMeshTimerAddOn addTimer:client:member:]_block_invoke.155
+ ___44-[COMeshAlarmAddOn _alarmManagerAlarmFired:]_block_invoke.151
+ ___44-[COMeshAlarmAddOn _alarmManagerAlarmFired:]_block_invoke.151.cold.1
+ ___44-[COMeshAlarmAddOn _alarmManagerStateReset:]_block_invoke
+ ___44-[COMeshAlarmAddOn _alarmManagerStateReset:]_block_invoke.cold.1
+ ___44-[COMeshTimerAddOn _timerManagerStateReset:]_block_invoke
+ ___44-[COMeshTimerAddOn _timerManagerStateReset:]_block_invoke.cold.1
+ ___46-[COMeshAlarmAddOn _broadcastMerge:withTruth:]_block_invoke
+ ___46-[COMeshAlarmAddOn _broadcastMerge:withTruth:]_block_invoke_2
+ ___46-[COMeshAlarmAddOn _broadcastMerge:withTruth:]_block_invoke_2.cold.1
+ ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke.197
+ ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke.197.cold.1
+ ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke.198
+ ___46-[COMeshAlarmAddOn updateAlarm:member:client:]_block_invoke.194
+ ___46-[COMeshAlarmAddOn updateAlarm:member:client:]_block_invoke.194.cold.1
+ ___46-[COMeshAlarmAddOn updateAlarm:member:client:]_block_invoke.195
+ ___46-[COMeshTimerAddOn _broadcastMerge:withTruth:]_block_invoke
+ ___46-[COMeshTimerAddOn _broadcastMerge:withTruth:]_block_invoke_2
+ ___46-[COMeshTimerAddOn _broadcastMerge:withTruth:]_block_invoke_2.cold.1
+ ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke.160
+ ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke.160.cold.1
+ ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke.161
+ ___46-[COMeshTimerAddOn updateTimer:client:member:]_block_invoke.157
+ ___46-[COMeshTimerAddOn updateTimer:client:member:]_block_invoke.157.cold.1
+ ___46-[COMeshTimerAddOn updateTimer:client:member:]_block_invoke.158
+ ___47-[COMeshAlarmAddOn _reloadIndexWithCompletion:]_block_invoke
+ ___47-[COMeshAlarmAddOn _reloadIndexWithCompletion:]_block_invoke.139
+ ___47-[COMeshAlarmAddOn _reloadIndexWithCompletion:]_block_invoke.cold.1
+ ___47-[COMeshAlarmAddOn _reloadIndexWithCompletion:]_block_invoke_2
+ ___47-[COMeshAlarmAddOn _reloadIndexWithCompletion:]_block_invoke_3
+ ___47-[COMeshTimerAddOn _reloadIndexWithCompletion:]_block_invoke
+ ___47-[COMeshTimerAddOn _reloadIndexWithCompletion:]_block_invoke.145
+ ___47-[COMeshTimerAddOn _reloadIndexWithCompletion:]_block_invoke.cold.1
+ ___47-[COMeshTimerAddOn _reloadIndexWithCompletion:]_block_invoke_2
+ ___47-[COMeshTimerAddOn _reloadIndexWithCompletion:]_block_invoke_3
+ ___50-[COMeshAlarmAddOn handleAlarmSnoozeNotification:]_block_invoke.223
+ ___50-[COMeshAlarmAddOn handleAlarmsAddedNotification:]_block_invoke.216
+ ___50-[COMeshTimerAddOn handleTimersAddedNotification:]_block_invoke.178
+ ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke.204
+ ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke.205
+ ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke.205.cold.1
+ ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke_2.206
+ ___52-[COMeshAlarmAddOn handleAlarmsRemovedNotification:]_block_invoke.217
+ ___52-[COMeshAlarmAddOn handleAlarmsUpdatedNotification:]_block_invoke.221
+ ___52-[COMeshController node:didReceiveError:forCommand:]_block_invoke.182
+ ___52-[COMeshController node:didReceiveError:forCommand:]_block_invoke.183
+ ___52-[COMeshTimerAddOn handleTimerReadRequest:callback:]_block_invoke.166
+ ___52-[COMeshTimerAddOn handleTimersRemovedNotification:]_block_invoke.180
+ ___52-[COMeshTimerAddOn handleTimersUpdatedNotification:]_block_invoke.181
+ ___53-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:client:]_block_invoke.199
+ ___54-[COMeshAlarmAddOn dismissAlarmWithIdentifier:client:]_block_invoke.200
+ ___54-[COMeshAlarmAddOn dismissAlarmWithIdentifier:client:]_block_invoke.200.cold.1
+ ___54-[COMeshAlarmAddOn dismissAlarmWithIdentifier:client:]_block_invoke.202
+ ___54-[COMeshAlarmAddOn handleAlarmCreateRequest:callback:]_block_invoke.207
+ ___54-[COMeshAlarmAddOn handleAlarmCreateRequest:callback:]_block_invoke.207.cold.1
+ ___54-[COMeshAlarmAddOn handleAlarmDeleteRequest:callback:]_block_invoke.210
+ ___54-[COMeshAlarmAddOn handleAlarmDeleteRequest:callback:]_block_invoke.210.cold.1
+ ___54-[COMeshAlarmAddOn handleAlarmUpdateRequest:callback:]_block_invoke.209
+ ___54-[COMeshAlarmAddOn handleAlarmUpdateRequest:callback:]_block_invoke.209.cold.1
+ ___54-[COMeshTimerAddOn dismissTimerWithIdentifier:client:]_block_invoke.162
+ ___54-[COMeshTimerAddOn dismissTimerWithIdentifier:client:]_block_invoke.162.cold.1
+ ___54-[COMeshTimerAddOn dismissTimerWithIdentifier:client:]_block_invoke.164
+ ___54-[COMeshTimerAddOn handleTimerCreateRequest:callback:]_block_invoke.167
+ ___54-[COMeshTimerAddOn handleTimerCreateRequest:callback:]_block_invoke.167.cold.1
+ ___54-[COMeshTimerAddOn handleTimerDeleteRequest:callback:]_block_invoke.169
+ ___54-[COMeshTimerAddOn handleTimerDeleteRequest:callback:]_block_invoke.169.cold.1
+ ___54-[COMeshTimerAddOn handleTimerUpdateRequest:callback:]_block_invoke.168
+ ___54-[COMeshTimerAddOn handleTimerUpdateRequest:callback:]_block_invoke.168.cold.1
+ ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.212
+ ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.212.cold.1
+ ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.213
+ ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.214
+ ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.173
+ ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.173.cold.1
+ ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.174
+ ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.175
+ ___60-[COMeshAlarmAddOn mediaSystemCompanionTransitionedFrom:to:]_block_invoke.247
+ ___60-[COMeshAlarmAddOn mediaSystemCompanionTransitionedFrom:to:]_block_invoke_2.248
+ ___60-[COMeshAlarmAddOn mediaSystemCompanionTransitionedFrom:to:]_block_invoke_3.249
+ ___61-[COMeshAlarmAddOn alarmsForAccessories:fromClient:callback:]_block_invoke.228
+ ___61-[COMeshAlarmAddOn alarmsForAccessories:fromClient:callback:]_block_invoke_2.229
+ ___61-[COMeshTimerAddOn timersForAccessories:fromClient:callback:]_block_invoke.186
+ ___64-[COMeshAlarmAddOn handleAlarmFiringAlarmDismissedNotification:]_block_invoke.222
+ ___64-[COMeshTimerAddOn handleTimerFiringTimerDismissedNotification:]_block_invoke.182
+ ___68-[COMeshAlarmAddOn interestTracker:setInterests:forMember:callback:]_block_invoke.263
+ ___68-[COMeshTimerAddOn interestTracker:setInterests:forMember:callback:]_block_invoke.205
+ ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.238
+ ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.238.cold.1
+ ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.239
+ ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.240
+ ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.242
+ ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.242.cold.1
+ ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.243
+ ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.243.cold.1
+ ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.244
+ ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.244.cold.1
+ ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke.267
+ ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke.269
+ ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke_2.268
+ ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke_2.268.cold.1
+ ___73-[COMeshController _finalizeCompletionOfNode:memberOfMesh:eventProvider:]_block_invoke.177
+ ___77-[COMeshController _performElectionGeneration:source:allowingPostTransition:]_block_invoke.96
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.166
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.175
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.175.cold.1
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.175.cold.2
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.177
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.178
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.178.cold.1
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.179
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke_2.180
+ ___86-[CONodeManager fast_fold_nodeController:didReceiveElectionCmd:withCompletionHandler:]_block_invoke
+ ___89-[COCoordinationService _linkServicesToMeshController:withClusterIdentifier:forClusters:]_block_invoke.49
+ ___Block_byref_object_copy_.47
+ ___Block_byref_object_dispose_.48
+ ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSArray"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e69_v40?0"COMeshRequest"8"COMeshNode"16"COMeshResponse"24"NSError"32lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40w_e5_v8?0lw40l8u48l8s32l8
+ ___block_literal_global.174
+ ___block_literal_global.220
+ __unnamed_array_storage.39
+ _eTagForAlarms
+ _eTagForTimers
+ _exit
+ _objc_msgSend$_broadcastMerge:withTruth:
+ _objc_msgSend$_electionInfoByDiffingCurrentElectionInfo:
+ _objc_msgSend$_finishMerge:
+ _objc_msgSend$_onqueue_configureTimer
+ _objc_msgSend$_onqueue_serverBagNumberValueForKey:
+ _objc_msgSend$_onqueue_serverBagValueForKey:
+ _objc_msgSend$_onqueue_timerFired
+ _objc_msgSend$_onqueue_updateCachedValuesWithServerValues
+ _objc_msgSend$_reloadIndexWithCompletion:
+ _objc_msgSend$_setupCoordinationPrefsObserver
+ _objc_msgSend$_setupIDSServerBag
+ _objc_msgSend$_tearDownCoordinationPrefsObserver
+ _objc_msgSend$_timeAwareUUID
+ _objc_msgSend$_updateKnownDiscovery:
+ _objc_msgSend$alarmIndex
+ _objc_msgSend$appendString:
+ _objc_msgSend$configure
+ _objc_msgSend$containsString:
+ _objc_msgSend$coordinationBundleID
+ _objc_msgSend$currentTimerDelay
+ _objc_msgSend$distantFuture
+ _objc_msgSend$distantPast
+ _objc_msgSend$eTag
+ _objc_msgSend$fast_fold_nodeController:didReceiveElectionCmd:withCompletionHandler:
+ _objc_msgSend$hasSameGenerationAndLeader:
+ _objc_msgSend$idsServerBag
+ _objc_msgSend$idsServerBagDidUpdate:
+ _objc_msgSend$initNotModifiedWithDeletes:
+ _objc_msgSend$initWithPresenceIdentifier:options:
+ _objc_msgSend$initWithServiceIdentifier:
+ _objc_msgSend$isActivated
+ _objc_msgSend$isFastFoldEnabled
+ _objc_msgSend$isIPDiffingEnabled
+ _objc_msgSend$isIPDiscoveryDiffingEnabled
+ _objc_msgSend$keySuffix
+ _objc_msgSend$knownDiscoveryRecords
+ _objc_msgSend$mergeAlarms
+ _objc_msgSend$mergeTimers
+ _objc_msgSend$notModified
+ _objc_msgSend$refreshTimer
+ _objc_msgSend$removeObserver:forKeyPath:
+ _objc_msgSend$setAlarmIndex:
+ _objc_msgSend$setCurrentTimerDelay:
+ _objc_msgSend$setETag:
+ _objc_msgSend$setFastFoldEnabled:
+ _objc_msgSend$setIpDiffing:
+ _objc_msgSend$setMergeAlarms:
+ _objc_msgSend$setMergeTimers:
+ _objc_msgSend$setTimerIndex:
+ _objc_msgSend$sharedInstanceForBagType:
+ _objc_msgSend$sourceHasBeenActivated
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringWithCapacity:
+ _objc_msgSend$timerIndex
+ _objc_msgSend$userDefaultsForIdentifer:
+ _sleep
- -[COElectionInfo generationAndLeaderNotEqualTo:]
- -[COMeshAlarmAddOn _alarmManagerStateReset:].cold.1
- -[COMeshAlarmAddOn _concludeMerge:usingLocalAlarms:]
- -[COMeshAlarmAddOn _concludeMerge:usingLocalAlarms:].cold.1
- -[COMeshAlarmAddOn _concludeMerge:usingLocalAlarms:].cold.2
- -[COMeshAlarmAddOn _finishMerge]
- -[COMeshTimerAddOn _concludeMerge:usingLocalTimers:]
- -[COMeshTimerAddOn _concludeMerge:usingLocalTimers:].cold.1
- -[COMeshTimerAddOn _concludeMerge:usingLocalTimers:].cold.2
- -[COMeshTimerAddOn _finishMerge]
- -[COMeshTimerAddOn _timerManagerStateReset:].cold.1
- GCC_except_table140
- GCC_except_table148
- GCC_except_table151
- GCC_except_table154
- GCC_except_table159
- GCC_except_table164
- GCC_except_table180
- GCC_except_table184
- GCC_except_table185
- GCC_except_table188
- GCC_except_table190
- GCC_except_table203
- GCC_except_table206
- GCC_except_table209
- GCC_except_table212
- GCC_except_table218
- GCC_except_table239
- GCC_except_table255
- GCC_except_table71
- GCC_except_table75
- GCC_except_table79
- GCC_except_table87
- ___24-[COMeshController stop]_block_invoke.64
- ___24-[COMeshController stop]_block_invoke.65
- ___24-[COMeshController stop]_block_invoke_2.67
- ___25-[COMeshController start]_block_invoke.63
- ___31-[COMeshAlarmAddOn _startMerge]_block_invoke_2.cold.1
- ___31-[COMeshTimerAddOn _startMerge]_block_invoke_2.cold.1
- ___32-[COMeshAlarmAddOn _finishMerge]_block_invoke
- ___32-[COMeshAlarmAddOn _finishMerge]_block_invoke_2
- ___32-[COMeshTimerAddOn _finishMerge]_block_invoke
- ___32-[COMeshTimerAddOn _finishMerge]_block_invoke_2
- ___37-[COIDSPresence _usersChangedInHome:]_block_invoke.36
- ___37-[COIDSPresence _usersChangedInHome:]_block_invoke.36.cold.1
- ___37-[COIDSPresence _usersChangedInHome:]_block_invoke.39
- ___37-[COIDSPresence _usersChangedInHome:]_block_invoke.39.cold.1
- ___37-[COIDSPresence _usersChangedInHome:]_block_invoke.39.cold.2
- ___37-[COMeshController sendNotification:]_block_invoke.77
- ___38-[COIDSPresence _synchronizePresence:]_block_invoke.33
- ___38-[COIDSPresence _synchronizePresence:]_block_invoke.33.cold.1
- ___38-[COIDSPresence _synchronizePresence:]_block_invoke.33.cold.2
- ___38-[COIDSPresence _synchronizePresence:]_block_invoke.33.cold.3
- ___38-[COIDSPresence _synchronizePresence:]_block_invoke.34
- ___39-[COMeshController _logElectionSummary]_block_invoke.116
- ___39-[COMeshController _logElectionSummary]_block_invoke.117
- ___39-[COMeshController sendCommand:toPeer:]_block_invoke.73
- ___39-[COMeshController sendCommand:toPeer:]_block_invoke.73.cold.1
- ___42-[COMeshController _processQueuedCommands]_block_invoke.82
- ___42-[COMeshController _processQueuedCommands]_block_invoke.84
- ___42-[COMeshController _processQueuedCommands]_block_invoke_2.83
- ___42-[COMeshController _processQueuedCommands]_block_invoke_2.85
- ___43-[COCoordinationService _continueMigration]_block_invoke.35
- ___43-[COMeshAlarmAddOn addAlarm:member:client:]_block_invoke.186
- ___43-[COMeshAlarmAddOn addAlarm:member:client:]_block_invoke.186.cold.1
- ___43-[COMeshAlarmAddOn addAlarm:member:client:]_block_invoke.187
- ___43-[COMeshTimerAddOn addTimer:client:member:]_block_invoke.149
- ___43-[COMeshTimerAddOn addTimer:client:member:]_block_invoke.149.cold.1
- ___43-[COMeshTimerAddOn addTimer:client:member:]_block_invoke.150
- ___44-[COMeshAlarmAddOn _alarmManagerAlarmFired:]_block_invoke.147
- ___44-[COMeshAlarmAddOn _alarmManagerAlarmFired:]_block_invoke.147.cold.1
- ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke.192
- ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke.192.cold.1
- ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke.193
- ___46-[COMeshAlarmAddOn updateAlarm:member:client:]_block_invoke.189
- ___46-[COMeshAlarmAddOn updateAlarm:member:client:]_block_invoke.189.cold.1
- ___46-[COMeshAlarmAddOn updateAlarm:member:client:]_block_invoke.190
- ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke.155
- ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke.155.cold.1
- ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke.156
- ___46-[COMeshTimerAddOn updateTimer:client:member:]_block_invoke.152
- ___46-[COMeshTimerAddOn updateTimer:client:member:]_block_invoke.152.cold.1
- ___46-[COMeshTimerAddOn updateTimer:client:member:]_block_invoke.153
- ___50-[COMeshAlarmAddOn handleAlarmSnoozeNotification:]_block_invoke.218
- ___50-[COMeshAlarmAddOn handleAlarmsAddedNotification:]_block_invoke.211
- ___50-[COMeshTimerAddOn handleTimersAddedNotification:]_block_invoke.173
- ___52-[COMeshAlarmAddOn _concludeMerge:usingLocalAlarms:]_block_invoke
- ___52-[COMeshAlarmAddOn _concludeMerge:usingLocalAlarms:]_block_invoke.135
- ___52-[COMeshAlarmAddOn _concludeMerge:usingLocalAlarms:]_block_invoke_2
- ___52-[COMeshAlarmAddOn _concludeMerge:usingLocalAlarms:]_block_invoke_3
- ___52-[COMeshAlarmAddOn _concludeMerge:usingLocalAlarms:]_block_invoke_4
- ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke.199
- ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke.200
- ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke.200.cold.1
- ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke_2.201
- ___52-[COMeshAlarmAddOn handleAlarmsRemovedNotification:]_block_invoke.212
- ___52-[COMeshAlarmAddOn handleAlarmsUpdatedNotification:]_block_invoke.216
- ___52-[COMeshController node:didReceiveError:forCommand:]_block_invoke.176
- ___52-[COMeshController node:didReceiveError:forCommand:]_block_invoke.177
- ___52-[COMeshTimerAddOn _concludeMerge:usingLocalTimers:]_block_invoke
- ___52-[COMeshTimerAddOn _concludeMerge:usingLocalTimers:]_block_invoke.140
- ___52-[COMeshTimerAddOn _concludeMerge:usingLocalTimers:]_block_invoke_2
- ___52-[COMeshTimerAddOn _concludeMerge:usingLocalTimers:]_block_invoke_3
- ___52-[COMeshTimerAddOn _concludeMerge:usingLocalTimers:]_block_invoke_4
- ___52-[COMeshTimerAddOn handleTimerReadRequest:callback:]_block_invoke.161
- ___52-[COMeshTimerAddOn handleTimersRemovedNotification:]_block_invoke.175
- ___52-[COMeshTimerAddOn handleTimersUpdatedNotification:]_block_invoke.176
- ___53-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:client:]_block_invoke.194
- ___54-[COMeshAlarmAddOn dismissAlarmWithIdentifier:client:]_block_invoke.195
- ___54-[COMeshAlarmAddOn dismissAlarmWithIdentifier:client:]_block_invoke.195.cold.1
- ___54-[COMeshAlarmAddOn dismissAlarmWithIdentifier:client:]_block_invoke.197
- ___54-[COMeshAlarmAddOn handleAlarmCreateRequest:callback:]_block_invoke.202
- ___54-[COMeshAlarmAddOn handleAlarmCreateRequest:callback:]_block_invoke.202.cold.1
- ___54-[COMeshAlarmAddOn handleAlarmDeleteRequest:callback:]_block_invoke.205
- ___54-[COMeshAlarmAddOn handleAlarmDeleteRequest:callback:]_block_invoke.205.cold.1
- ___54-[COMeshAlarmAddOn handleAlarmUpdateRequest:callback:]_block_invoke.204
- ___54-[COMeshAlarmAddOn handleAlarmUpdateRequest:callback:]_block_invoke.204.cold.1
- ___54-[COMeshTimerAddOn dismissTimerWithIdentifier:client:]_block_invoke.157
- ___54-[COMeshTimerAddOn dismissTimerWithIdentifier:client:]_block_invoke.157.cold.1
- ___54-[COMeshTimerAddOn dismissTimerWithIdentifier:client:]_block_invoke.159
- ___54-[COMeshTimerAddOn handleTimerCreateRequest:callback:]_block_invoke.162
- ___54-[COMeshTimerAddOn handleTimerCreateRequest:callback:]_block_invoke.162.cold.1
- ___54-[COMeshTimerAddOn handleTimerDeleteRequest:callback:]_block_invoke.164
- ___54-[COMeshTimerAddOn handleTimerDeleteRequest:callback:]_block_invoke.164.cold.1
- ___54-[COMeshTimerAddOn handleTimerUpdateRequest:callback:]_block_invoke.163
- ___54-[COMeshTimerAddOn handleTimerUpdateRequest:callback:]_block_invoke.163.cold.1
- ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.207
- ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.207.cold.1
- ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.208
- ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.209
- ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.168
- ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.168.cold.1
- ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.169
- ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.170
- ___60-[COMeshAlarmAddOn mediaSystemCompanionTransitionedFrom:to:]_block_invoke.242
- ___60-[COMeshAlarmAddOn mediaSystemCompanionTransitionedFrom:to:]_block_invoke_2.243
- ___60-[COMeshAlarmAddOn mediaSystemCompanionTransitionedFrom:to:]_block_invoke_3.244
- ___61-[COMeshAlarmAddOn alarmsForAccessories:fromClient:callback:]_block_invoke.223
- ___61-[COMeshAlarmAddOn alarmsForAccessories:fromClient:callback:]_block_invoke_2.224
- ___61-[COMeshTimerAddOn timersForAccessories:fromClient:callback:]_block_invoke.181
- ___64-[COMeshAlarmAddOn handleAlarmFiringAlarmDismissedNotification:]_block_invoke.217
- ___64-[COMeshTimerAddOn handleTimerFiringTimerDismissedNotification:]_block_invoke.177
- ___68-[COMeshAlarmAddOn interestTracker:setInterests:forMember:callback:]_block_invoke.258
- ___68-[COMeshTimerAddOn interestTracker:setInterests:forMember:callback:]_block_invoke.200
- ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.233
- ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.233.cold.1
- ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.234
- ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.235
- ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.237
- ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.237.cold.1
- ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.238
- ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.238.cold.1
- ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.239
- ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.239.cold.1
- ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke.262
- ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke.264
- ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke_2.263
- ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke_2.263.cold.1
- ___73-[COMeshController _finalizeCompletionOfNode:memberOfMesh:eventProvider:]_block_invoke.171
- ___77-[COMeshController _performElectionGeneration:source:allowingPostTransition:]_block_invoke.90
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.161
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.165
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.165.cold.1
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.165.cold.2
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.167
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.173
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.173.cold.1
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.174
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke_2.175
- ___89-[COCoordinationService _linkServicesToMeshController:withClusterIdentifier:forClusters:]_block_invoke.48
- ___Block_byref_object_copy_.46
- ___Block_byref_object_dispose_.47
- ___block_descriptor_40_e8_32w_e69_v40?0"COMeshRequest"8"COMeshNode"16"COMeshResponse"24"NSError"32lw32l8
- ___block_descriptor_64_e8_32bs40r48w_e5_v8?0lw48l8u56l8r40l8s32l8
- ___block_descriptor_64_e8_32s40bs48r_e5_v8?0ls32l8u56l8r48l8s40l8
- ___block_literal_global.164
- ___block_literal_global.215
- __unnamed_array_storage.40
- _objc_msgSend$_concludeMerge:usingLocalAlarms:
- _objc_msgSend$_concludeMerge:usingLocalTimers:
- _objc_msgSend$_finishMerge
- _objc_msgSend$generationAndLeaderNotEqualTo:
- _objc_msgSend$initWithPresenceIdentifier:
CStrings:
+ ""
+ "\x11%\x11M5"
+ "\x12\x13\x11"
+ "#\"'"
+ "%02x"
+ "%p IDS server bag updated"
+ "%p Notifying delegate of server bag update"
+ "%p Server bag refresh timer fired"
+ "%p Updating fast fold enabled from %@ to %@"
+ "%p Updating ip diffing enabled from %@ to %@"
+ "%p alarm index reloaded; updated: %s"
+ "%p broadcasting merge %p with eTag %{public}@"
+ "%p failed to fetch alarms for index: %{public}@"
+ "%p failed to fetch timers for index: %{public}@"
+ "%p fast fold changed. Exiting process"
+ "%p ignoring broadcast for merge %p"
+ "%p ip diffing changed. Exiting process"
+ "%p not emitting state reset, alarms not updated"
+ "%p not emitting state reset, timers not updated"
+ "%p observed an update to fast fold enablement. new value = %d"
+ "%p observed an update to ip diffing enablement. new value = %d"
+ "%p request info: filter: %d, merge: %d, eTag: %@"
+ "%p response is not-modified for %@"
+ "%p serverBagValueForKey %@ returned %@"
+ "%p setting up IDSServer Bag"
+ "%p setting up observers to watch coordination prefs"
+ "%p timer index reloaded; updated: %s"
+ "%{public}@ completing deferred activation"
+ "%{public}@ deferring activation since source transport is not yet active"
+ "%{public}@ node started election %@"
+ "%{public}@ upgrading election generation from %llu to %llu"
+ "-internal"
+ "... returning alarms list and deletes\n%@"
+ "... returning not-modified"
+ "... returning skip-in-merge"
+ "/\x03"
+ "0P`"
+ "1&"
+ "196.21.1"
+ "2\x19"
+ "@\"<COIDSServerBagDelegate>\""
+ "@\"COIDSServerBag\""
+ "@\"IDSServerBag\""
+ "@\"NSNumber\""
+ "COIDSServerBag"
+ "COIDSServerBagDelegate"
+ "Clock not synchronized, going to poll."
+ "Clock not synchronized. Using distant future %llu"
+ "Clock synchronized. time = %llu"
+ "IDSServerBag"
+ "Initializing using key suffix %@ with initial timer interval of %fs"
+ "Received an updated bag value for fast fold %@. Writing to prefs"
+ "Received an updated bag value for ip diffing %@. Writing to prefs"
+ "T@\"<COIDSServerBagDelegate>\",W,N,V_delegate"
+ "T@\"COIDSServerBag\",&,N,V_idsServerBag"
+ "T@\"IDSServerBag\",R,V_idsServerBag"
+ "T@\"NSArray\",&,N,V_mergeAlarms"
+ "T@\"NSArray\",&,N,V_mergeTimers"
+ "T@\"NSMutableDictionary\",&,N,V_alarmIndex"
+ "T@\"NSMutableDictionary\",&,N,V_knownDiscoveryRecords"
+ "T@\"NSMutableDictionary\",&,N,V_timerIndex"
+ "T@\"NSNumber\",&,N,GisFastFoldEnabled,V_fastFoldEnabled"
+ "T@\"NSNumber\",&,N,GisIPDiffingEnabled,V_ipDiffingEnabled"
+ "T@\"NSObject<OS_dispatch_queue>\",R,V_dispatchQueue"
+ "T@\"NSObject<OS_dispatch_source>\",R,V_refreshTimer"
+ "T@\"NSString\",&,N,V_eTag"
+ "T@\"NSString\",R,C,V_keySuffix"
+ "T@\"NSUserDefaults\",&,N,V_coordinationDefaults"
+ "TB,R,N,V_notModified"
+ "Tq,V_currentTimerDelay"
+ "_alarmIndex"
+ "_broadcastMerge:withTruth:"
+ "_coordinationDefaults"
+ "_currentTimerDelay"
+ "_eTag"
+ "_electionInfoByDiffingCurrentElectionInfo:"
+ "_expectedRegisteredCommandCount"
+ "_fastFoldEnabled"
+ "_finishMerge:"
+ "_idsServerBag"
+ "_ipDiffingEnabled"
+ "_keySuffix"
+ "_knownDiscoveryRecords"
+ "_mergeAlarms"
+ "_mergeTimers"
+ "_notModified"
+ "_onqueue_configureTimer"
+ "_onqueue_serverBagNumberValueForKey:"
+ "_onqueue_serverBagValueForKey:"
+ "_onqueue_timerFired"
+ "_onqueue_updateCachedValuesWithServerValues"
+ "_refreshTimer"
+ "_reloadIndexWithCompletion:"
+ "_setupCoordinationPrefsObserver"
+ "_setupIDSServerBag"
+ "_tearDownCoordinationPrefsObserver"
+ "_timeAwareUUID"
+ "_timerIndex"
+ "_updateKnownDiscovery:"
+ "alarmIndex"
+ "appendString:"
+ "co-fastFold-enabled"
+ "co-ipDiffing-enabled"
+ "configure"
+ "containsString:"
+ "coordinated"
+ "coordinationBundleID"
+ "coordinationDefaults"
+ "currentTimerDelay"
+ "distantFuture"
+ "distantPast"
+ "eTag"
+ "etag"
+ "fastFoldEnabled"
+ "fast_fold_nodeController:didReceiveElectionCmd:withCompletionHandler:"
+ "hasSameGenerationAndLeader:"
+ "home-mesh"
+ "idsServerBag"
+ "idsServerBagDidUpdate:"
+ "initNotModifiedWithDeletes:"
+ "initWithPresenceIdentifier:options:"
+ "initWithServiceIdentifier:"
+ "ipDiffingEnabled"
+ "isActivated"
+ "isFastFoldEnabled"
+ "isIPDiffingEnabled"
+ "isIPDiscoveryDiffingEnabled"
+ "keySuffix"
+ "knownDiscoveryRecords"
+ "mergeAlarms"
+ "mergeTimers"
+ "no"
+ "notModified"
+ "refreshTimer"
+ "removeObserver:forKeyPath:"
+ "setAlarmIndex:"
+ "setCoordinationDefaults:"
+ "setCurrentTimerDelay:"
+ "setETag:"
+ "setFastFoldEnabled:"
+ "setIdsServerBag:"
+ "setIpDiffing:"
+ "setIpDiffingEnabled:"
+ "setKnownDiscoveryRecords:"
+ "setMergeAlarms:"
+ "setMergeTimers:"
+ "setTimerIndex:"
+ "sha1:"
+ "sharedInstanceForBagType:"
+ "sourceHasBeenActivated"
+ "stringByAppendingString:"
+ "stringWithCapacity:"
+ "timerIndex"
+ "unmodified"
+ "userDefaultsForIdentifer:"
+ "v24@0:8@\"COIDSServerBag\"16"
+ "yes"
- "\x11%\x11L5"
- "\x12\x18"
- "#\"&"
- "0@P`"
- "1%"
- "196.11.1"
- "1@`"
- "_concludeMerge:usingLocalAlarms:"
- "_concludeMerge:usingLocalTimers:"
- "_finishMerge"
- "generationAndLeaderNotEqualTo:"
- "initWithPresenceIdentifier:"

```
