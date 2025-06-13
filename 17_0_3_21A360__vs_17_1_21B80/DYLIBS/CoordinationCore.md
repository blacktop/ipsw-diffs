## CoordinationCore

> `/System/Library/PrivateFrameworks/CoordinationCore.framework/CoordinationCore`

```diff

-196.0.3.0.0
-  __TEXT.__text: 0xbf414
+196.11.1.0.0
+  __TEXT.__text: 0xbf66c
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x84b0
+  __TEXT.__objc_methlist: 0x81f8
   __TEXT.__const: 0x278
-  __TEXT.__gcc_except_tab: 0x2f10
-  __TEXT.__cstring: 0x285d
-  __TEXT.__oslogstring: 0x8d95
-  __TEXT.__unwind_info: 0x2ff8
-  __TEXT.__objc_classname: 0x1821
-  __TEXT.__objc_methname: 0x11e3e
-  __TEXT.__objc_methtype: 0x3906
-  __TEXT.__objc_stubs: 0xd3e0
+  __TEXT.__gcc_except_tab: 0x2f24
+  __TEXT.__cstring: 0x27ba
+  __TEXT.__oslogstring: 0x8e96
+  __TEXT.__unwind_info: 0x2fec
+  __TEXT.__objc_classname: 0x1739
+  __TEXT.__objc_methname: 0x1203a
+  __TEXT.__objc_methtype: 0x3992
+  __TEXT.__objc_stubs: 0xd5e0
   __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0x3d80
-  __DATA_CONST.__objc_classlist: 0x5e0
+  __DATA_CONST.__const: 0x3d58
+  __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf6c0
-  __DATA_CONST.__objc_selrefs: 0x3a70
+  __DATA_CONST.__objc_const: 0xf600
+  __DATA_CONST.__objc_selrefs: 0x3af0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__objc_const: 0x4648
-  __AUTH_CONST.__cfstring: 0x24a0
-  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__objc_const: 0x40a8
+  __AUTH_CONST.__cfstring: 0x2420
+  __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x470
-  __AUTH.__objc_data: 0x2300
+  __AUTH.__objc_data: 0x1fe0
   __DATA.__objc_protorefs: 0x88
-  __DATA.__objc_classrefs: 0x798
-  __DATA.__objc_superrefs: 0x460
-  __DATA.__objc_ivar: 0x9c0
+  __DATA.__objc_classrefs: 0x748
+  __DATA.__objc_superrefs: 0x410
+  __DATA.__objc_ivar: 0x9b0
   __DATA.__data: 0x1920
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x17c0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35E6072C-808F-3830-8DA2-41425FAD8103
-  Functions: 4112
-  Symbols:   13330
-  CStrings:  5225
+  UUID: 69E5BB40-9122-3826-A068-050C91246696
+  Functions: 4083
+  Symbols:   13214
+  CStrings:  5228
 
Symbols:
+ -[COAlarmService _postCanDispatchChanged:forAccessory:toObserver:]
+ -[COAlarmService _postNotificationName:forAccessory:toAddOn:]
+ -[COAlarmService alarmAddOn:resetAccesory:]
+ -[COElectionInfo generationAndLeaderNotEqualTo:]
+ -[COElectionInfo hasGreaterGenerationThan:]
+ -[COInterestTracker _checkTriggerReset]
+ -[COInterestTracker _nextInterestSerial]
+ -[COInterestTracker _setInterest:]
+ -[COInterestTracker accessory]
+ -[COInterestTracker canDispatchWithPrimary:]
+ -[COInterestTracker initWithAccessory:delegate:primaryAvailable:secondary:]
+ -[COInterestTracker interestsSerial]
+ -[COInterestTracker remoteInterests]
+ -[COInterestTracker setInterestsSerial:]
+ -[COInterestTracker setRemoteInterests:]
+ -[COInterestTracker setTriggerReset:]
+ -[COInterestTracker triggerReset]
+ -[COMTTypedAction description]
+ -[COMeshAlarmAddOn interestTracker:setInterests:forMember:callback:]
+ -[COMeshAlarmAddOn interestTrackerTriggerReset:]
+ -[COMeshAlarmAddOn interestTrackerTriggerReset:].cold.1
+ -[COMeshAlarmAddOn setInterests:asAccessory:withCallback:]
+ -[COMeshTimerAddOn interestTracker:setInterests:forMember:callback:]
+ -[COMeshTimerAddOn interestTrackerTriggerReset:]
+ -[COMeshTimerAddOn interestTrackerTriggerReset:].cold.1
+ -[COMeshTimerAddOn setInterests:asAccessory:withCallback:]
+ -[CONodeManager _informDelegateAboutNodeAddition:oldState:]
+ -[CONodeManager _informDelegateAboutNodeRemoval:oldState:]
+ -[COTimerService _postCanDispatchChanged:forAccessory:toObserver:]
+ -[COTimerService _postNotificationName:forAccessory:toAddOn:]
+ -[COTimerService timerAddOn:resetAccesory:]
+ GCC_except_table140
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table154
+ GCC_except_table159
+ GCC_except_table164
+ GCC_except_table180
+ GCC_except_table184
+ GCC_except_table188
+ GCC_except_table203
+ GCC_except_table206
+ GCC_except_table209
+ GCC_except_table212
+ GCC_except_table218
+ GCC_except_table239
+ GCC_except_table255
+ GCC_except_table71
+ GCC_except_table75
+ GCC_except_table82
+ GCC_except_table87
+ _OBJC_IVAR_$_COInterestTracker._accessory
+ _OBJC_IVAR_$_COInterestTracker._interestsSerial
+ _OBJC_IVAR_$_COInterestTracker._remoteInterests
+ _OBJC_IVAR_$_COInterestTracker._triggerReset
+ _OUTLINED_FUNCTION_21
+ ___101-[CORapportTransport handleResponseToRequest:rapportRepresentation:options:error:responseHandler:at:]_block_invoke.127
+ ___34-[COInterestTracker _setInterest:]_block_invoke
+ ___43-[COAlarmService alarmAddOn:resetAccesory:]_block_invoke
+ ___43-[COMeshAlarmAddOn addAlarm:member:client:]_block_invoke.186
+ ___43-[COMeshAlarmAddOn addAlarm:member:client:]_block_invoke.186.cold.1
+ ___43-[COMeshAlarmAddOn addAlarm:member:client:]_block_invoke.187
+ ___43-[COMeshTimerAddOn addTimer:client:member:]_block_invoke.149
+ ___43-[COMeshTimerAddOn addTimer:client:member:]_block_invoke.149.cold.1
+ ___43-[COMeshTimerAddOn addTimer:client:member:]_block_invoke.150
+ ___43-[COTimerService timerAddOn:resetAccesory:]_block_invoke
+ ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke.192
+ ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke.192.cold.1
+ ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke.193
+ ___46-[COMeshAlarmAddOn updateAlarm:member:client:]_block_invoke.189
+ ___46-[COMeshAlarmAddOn updateAlarm:member:client:]_block_invoke.189.cold.1
+ ___46-[COMeshAlarmAddOn updateAlarm:member:client:]_block_invoke.190
+ ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke.155
+ ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke.155.cold.1
+ ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke.156
+ ___46-[COMeshTimerAddOn updateTimer:client:member:]_block_invoke.152
+ ___46-[COMeshTimerAddOn updateTimer:client:member:]_block_invoke.152.cold.1
+ ___46-[COMeshTimerAddOn updateTimer:client:member:]_block_invoke.153
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.148
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.150.cold.1
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.151
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.153
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.155
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.149
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.152
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.152.cold.1
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.154
+ ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.154.cold.1
+ ___50-[COMeshAlarmAddOn handleAlarmSnoozeNotification:]_block_invoke.218
+ ___50-[COMeshAlarmAddOn handleAlarmsAddedNotification:]_block_invoke.211
+ ___50-[COMeshTimerAddOn handleTimersAddedNotification:]_block_invoke.173
+ ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke.199
+ ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke.200
+ ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke.200.cold.1
+ ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke_2.201
+ ___52-[COMeshAlarmAddOn handleAlarmsRemovedNotification:]_block_invoke.212
+ ___52-[COMeshAlarmAddOn handleAlarmsUpdatedNotification:]_block_invoke.216
+ ___52-[COMeshTimerAddOn _concludeMerge:usingLocalTimers:]_block_invoke.140
+ ___52-[COMeshTimerAddOn handleTimerReadRequest:callback:]_block_invoke.161
+ ___52-[COMeshTimerAddOn handleTimersRemovedNotification:]_block_invoke.175
+ ___52-[COMeshTimerAddOn handleTimersUpdatedNotification:]_block_invoke.176
+ ___53-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:client:]_block_invoke.194
+ ___54-[COMeshAlarmAddOn dismissAlarmWithIdentifier:client:]_block_invoke.195
+ ___54-[COMeshAlarmAddOn dismissAlarmWithIdentifier:client:]_block_invoke.195.cold.1
+ ___54-[COMeshAlarmAddOn dismissAlarmWithIdentifier:client:]_block_invoke.197
+ ___54-[COMeshAlarmAddOn handleAlarmCreateRequest:callback:]_block_invoke.202
+ ___54-[COMeshAlarmAddOn handleAlarmCreateRequest:callback:]_block_invoke.202.cold.1
+ ___54-[COMeshAlarmAddOn handleAlarmDeleteRequest:callback:]_block_invoke.205
+ ___54-[COMeshAlarmAddOn handleAlarmDeleteRequest:callback:]_block_invoke.205.cold.1
+ ___54-[COMeshAlarmAddOn handleAlarmUpdateRequest:callback:]_block_invoke.204
+ ___54-[COMeshAlarmAddOn handleAlarmUpdateRequest:callback:]_block_invoke.204.cold.1
+ ___54-[COMeshTimerAddOn dismissTimerWithIdentifier:client:]_block_invoke.157
+ ___54-[COMeshTimerAddOn dismissTimerWithIdentifier:client:]_block_invoke.157.cold.1
+ ___54-[COMeshTimerAddOn dismissTimerWithIdentifier:client:]_block_invoke.159
+ ___54-[COMeshTimerAddOn handleTimerCreateRequest:callback:]_block_invoke.162
+ ___54-[COMeshTimerAddOn handleTimerCreateRequest:callback:]_block_invoke.162.cold.1
+ ___54-[COMeshTimerAddOn handleTimerDeleteRequest:callback:]_block_invoke.164
+ ___54-[COMeshTimerAddOn handleTimerDeleteRequest:callback:]_block_invoke.164.cold.1
+ ___54-[COMeshTimerAddOn handleTimerUpdateRequest:callback:]_block_invoke.163
+ ___54-[COMeshTimerAddOn handleTimerUpdateRequest:callback:]_block_invoke.163.cold.1
+ ___54-[CORapportTransport sendRequest:withResponseHandler:]_block_invoke.108
+ ___54-[CORapportTransport sendRequest:withResponseHandler:]_block_invoke_2.109
+ ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.207
+ ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.207.cold.1
+ ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.208
+ ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.209
+ ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.168
+ ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.168.cold.1
+ ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.169
+ ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.170
+ ___58-[COMeshAlarmAddOn setInterests:asAccessory:withCallback:]_block_invoke
+ ___58-[COMeshAlarmAddOn setInterests:asAccessory:withCallback:]_block_invoke.cold.1
+ ___58-[COMeshTimerAddOn setInterests:asAccessory:withCallback:]_block_invoke
+ ___58-[COMeshTimerAddOn setInterests:asAccessory:withCallback:]_block_invoke.cold.1
+ ___58-[CORapportTransport _setUpRegistrationCompletionHandlers]_block_invoke_2
+ ___58-[CORapportTransport _setUpRegistrationCompletionHandlers]_block_invoke_2.99
+ ___60-[COMeshAlarmAddOn canDispatchAsAccessory:asInstance:reply:]_block_invoke
+ ___60-[COMeshAlarmAddOn canDispatchAsAccessory:asInstance:reply:]_block_invoke.cold.1
+ ___60-[COMeshAlarmAddOn canDispatchAsAccessory:asInstance:reply:]_block_invoke.cold.2
+ ___60-[COMeshAlarmAddOn canDispatchAsAccessory:asInstance:reply:]_block_invoke.cold.3
+ ___60-[COMeshAlarmAddOn mediaSystemCompanionTransitionedFrom:to:]_block_invoke.242
+ ___60-[COMeshAlarmAddOn mediaSystemCompanionTransitionedFrom:to:]_block_invoke_2.243
+ ___60-[COMeshAlarmAddOn mediaSystemCompanionTransitionedFrom:to:]_block_invoke_3.244
+ ___60-[COMeshTimerAddOn canDispatchAsAccessory:asInstance:reply:]_block_invoke
+ ___60-[COMeshTimerAddOn canDispatchAsAccessory:asInstance:reply:]_block_invoke.cold.1
+ ___60-[COMeshTimerAddOn canDispatchAsAccessory:asInstance:reply:]_block_invoke.cold.2
+ ___61-[COMeshAlarmAddOn alarmsForAccessories:fromClient:callback:]_block_invoke.223
+ ___61-[COMeshAlarmAddOn alarmsForAccessories:fromClient:callback:]_block_invoke_2.224
+ ___61-[COMeshTimerAddOn timersForAccessories:fromClient:callback:]_block_invoke.181
+ ___64-[COMeshAlarmAddOn handleAlarmFiringAlarmDismissedNotification:]_block_invoke.217
+ ___64-[COMeshTimerAddOn handleTimerFiringTimerDismissedNotification:]_block_invoke.177
+ ___68-[COMeshAlarmAddOn interestTracker:setInterests:forMember:callback:]_block_invoke
+ ___68-[COMeshAlarmAddOn interestTracker:setInterests:forMember:callback:]_block_invoke.258
+ ___68-[COMeshAlarmAddOn interestTracker:setInterests:forMember:callback:]_block_invoke_2
+ ___68-[COMeshTimerAddOn interestTracker:setInterests:forMember:callback:]_block_invoke
+ ___68-[COMeshTimerAddOn interestTracker:setInterests:forMember:callback:]_block_invoke.200
+ ___68-[COMeshTimerAddOn interestTracker:setInterests:forMember:callback:]_block_invoke_2
+ ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.233
+ ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.233.cold.1
+ ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.234
+ ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.235
+ ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.237
+ ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.237.cold.1
+ ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.238
+ ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.238.cold.1
+ ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.239
+ ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.239.cold.1
+ ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke.262
+ ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke.264
+ ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke_2.263
+ ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke_2.263.cold.1
+ ___77-[CORapportTransport _updateRequestTimesFromRapportRepresentation:start:end:]_block_invoke.134
+ ___77-[COTimerService removeObserverForNotificationName:asAccessory:withCallback:]_block_invoke_2
+ ___77-[COTimerService removeObserverForNotificationName:asAccessory:withCallback:]_block_invoke_3
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.165
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.165.cold.1
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.165.cold.2
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.170
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.170.cold.1
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.170.cold.2
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.173
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.173.cold.1
+ ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke_2.175
+ ___88-[COAlarmService removeObserverForNotificationName:asAccessory:asInstance:withCallback:]_block_invoke_2
+ ___88-[COAlarmService removeObserverForNotificationName:asAccessory:asInstance:withCallback:]_block_invoke_3
+ ___95-[CORapportTransport handleRequestIdentifier:rapportRepresentation:options:responseHandler:at:]_block_invoke.122
+ ___95-[CORapportTransport handleRequestIdentifier:rapportRepresentation:options:responseHandler:at:]_block_invoke_2.126
+ ___97-[COAlarmService addObserverForNotificationName:asAccessory:asInstance:constraints:withCallback:]_block_invoke_2
+ ___97-[COTimerService addObserverForNotificationName:asAccessory:asInstance:constraints:withCallback:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e32_v24?0"COMTResult"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40w48w_e17_v16?0"NSError"8lw40l8w48l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e8_v12?0B8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48w56w_e5_v8?0lw48l8w56l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e17_v16?0"NSError"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_literal_global.164
+ ___block_literal_global.169
+ ___block_literal_global.215
+ _objc_msgSend$_checkTriggerReset
+ _objc_msgSend$_informDelegateAboutNodeAddition:oldState:
+ _objc_msgSend$_informDelegateAboutNodeRemoval:oldState:
+ _objc_msgSend$_nextInterestSerial
+ _objc_msgSend$_postCanDispatchChanged:forAccessory:toObserver:
+ _objc_msgSend$_postNotificationName:forAccessory:toAddOn:
+ _objc_msgSend$_setInterest:
+ _objc_msgSend$alarmAddOn:resetAccesory:
+ _objc_msgSend$canDispatchWithPrimary:
+ _objc_msgSend$generationAndLeaderNotEqualTo:
+ _objc_msgSend$hasGreaterGenerationThan:
+ _objc_msgSend$initWithAccessory:delegate:primaryAvailable:secondary:
+ _objc_msgSend$interestTracker:setInterests:forMember:callback:
+ _objc_msgSend$interestTrackerTriggerReset:
+ _objc_msgSend$interestsSerial
+ _objc_msgSend$isOpalEnabled
+ _objc_msgSend$remoteInterests
+ _objc_msgSend$setInterests:asAccessory:withCallback:
+ _objc_msgSend$setInterestsSerial:
+ _objc_msgSend$setRemoteInterests:
+ _objc_msgSend$setTriggerReset:
+ _objc_msgSend$timerAddOn:resetAccesory:
+ _objc_msgSend$triggerReset
- +[COMTAlarmDeleteAction supportsSecureCoding]
- +[COMTAlarmDeleteResult supportsSecureCoding]
- +[COMTAlarmReadAction supportsSecureCoding]
- +[COMTAlarmUpdateInterestAction supportsSecureCoding]
- +[COMTAlarmUpdateResult supportsSecureCoding]
- +[COMTTimerDeleteAction supportsSecureCoding]
- +[COMTTimerDeleteResult supportsSecureCoding]
- +[COMTTimerReadAction supportsSecureCoding]
- +[COMTTimerUpdateInterestAction supportsSecureCoding]
- +[COMTTimerUpdateResult supportsSecureCoding]
- -[COElectionInfo shouldTriggerElectionForElectionInfo:]
- -[COInterestTracker initWithDelegate:primaryAvailable:secondary:]
- -[COMTAlarmDeleteAction .cxx_destruct]
- -[COMTAlarmDeleteAction alarm]
- -[COMTAlarmDeleteAction copyWithZone:]
- -[COMTAlarmDeleteAction encodeWithCoder:]
- -[COMTAlarmDeleteAction initWithAlarm:]
- -[COMTAlarmDeleteAction initWithCoder:]
- -[COMTAlarmDeleteResult copyWithZone:]
- -[COMTAlarmDeleteResult encodeWithCoder:]
- -[COMTAlarmDeleteResult initWithActionIdentifier:]
- -[COMTAlarmDeleteResult initWithCoder:]
- -[COMTAlarmReadAction .cxx_destruct]
- -[COMTAlarmReadAction copyWithZone:]
- -[COMTAlarmReadAction encodeWithCoder:]
- -[COMTAlarmReadAction initWithCoder:]
- -[COMTAlarmReadAction initWithTargetIdentifiers:]
- -[COMTAlarmReadAction targetIdentifiers]
- -[COMTAlarmReadResult initChunkedWithActionIdentifier:]
- -[COMTAlarmReadResult isComplete]
- -[COMTAlarmUpdateInterestAction .cxx_destruct]
- -[COMTAlarmUpdateInterestAction encodeWithCoder:]
- -[COMTAlarmUpdateInterestAction initWithCoder:]
- -[COMTAlarmUpdateInterestAction initWithTargetIdentifiers:]
- -[COMTAlarmUpdateInterestAction targetIdentifiers]
- -[COMTAlarmUpdateResult copyWithZone:]
- -[COMTAlarmUpdateResult encodeWithCoder:]
- -[COMTAlarmUpdateResult initWithActionIdentifier:]
- -[COMTAlarmUpdateResult initWithCoder:]
- -[COMTTimerDeleteAction .cxx_destruct]
- -[COMTTimerDeleteAction copyWithZone:]
- -[COMTTimerDeleteAction encodeWithCoder:]
- -[COMTTimerDeleteAction initWithCoder:]
- -[COMTTimerDeleteAction initWithTimer:]
- -[COMTTimerDeleteAction timer]
- -[COMTTimerDeleteResult copyWithZone:]
- -[COMTTimerDeleteResult encodeWithCoder:]
- -[COMTTimerDeleteResult initWithActionIdentifier:]
- -[COMTTimerDeleteResult initWithCoder:]
- -[COMTTimerReadAction .cxx_destruct]
- -[COMTTimerReadAction copyWithZone:]
- -[COMTTimerReadAction encodeWithCoder:]
- -[COMTTimerReadAction initWithCoder:]
- -[COMTTimerReadAction initWithTargetIdentifiers:]
- -[COMTTimerReadAction targetIdentifiers]
- -[COMTTimerReadResult initChunkedWithActionIdentifier:]
- -[COMTTimerReadResult isComplete]
- -[COMTTimerUpdateInterestAction .cxx_destruct]
- -[COMTTimerUpdateInterestAction encodeWithCoder:]
- -[COMTTimerUpdateInterestAction initWithCoder:]
- -[COMTTimerUpdateInterestAction initWithTargetIdentifiers:]
- -[COMTTimerUpdateInterestAction targetIdentifiers]
- -[COMTTimerUpdateResult copyWithZone:]
- -[COMTTimerUpdateResult encodeWithCoder:]
- -[COMTTimerUpdateResult initWithActionIdentifier:]
- -[COMTTimerUpdateResult initWithCoder:]
- -[COMeshAlarmAddOn canDispatchAsAccessory:asInstance:reply:].cold.1
- -[COMeshAlarmAddOn canDispatchAsAccessory:asInstance:reply:].cold.2
- -[COMeshAlarmAddOn canDispatchAsAccessory:asInstance:reply:].cold.3
- -[COMeshAlarmAddOn interestTracker:setInterests:forMember:triggerReset:]
- -[COMeshAlarmAddOn setInterests:asAccessory:]
- -[COMeshTimerAddOn canDispatchAsAccessory:asInstance:reply:].cold.1
- -[COMeshTimerAddOn canDispatchAsAccessory:asInstance:reply:].cold.2
- -[COMeshTimerAddOn interestTracker:setInterests:forMember:triggerReset:]
- -[COMeshTimerAddOn setInterests:asAccessory:]
- GCC_except_table142
- GCC_except_table150
- GCC_except_table153
- GCC_except_table156
- GCC_except_table163
- GCC_except_table166
- GCC_except_table182
- GCC_except_table187
- GCC_except_table189
- GCC_except_table205
- GCC_except_table208
- GCC_except_table211
- GCC_except_table214
- GCC_except_table220
- GCC_except_table240
- GCC_except_table254
- GCC_except_table51
- GCC_except_table69
- GCC_except_table73
- GCC_except_table83
- _OBJC_CLASS_$_COMTAlarmDeleteAction
- _OBJC_CLASS_$_COMTAlarmDeleteResult
- _OBJC_CLASS_$_COMTAlarmReadAction
- _OBJC_CLASS_$_COMTAlarmUpdateInterestAction
- _OBJC_CLASS_$_COMTAlarmUpdateResult
- _OBJC_CLASS_$_COMTTimerDeleteAction
- _OBJC_CLASS_$_COMTTimerDeleteResult
- _OBJC_CLASS_$_COMTTimerReadAction
- _OBJC_CLASS_$_COMTTimerUpdateInterestAction
- _OBJC_CLASS_$_COMTTimerUpdateResult
- _OBJC_IVAR_$_COMTAlarmDeleteAction._alarm
- _OBJC_IVAR_$_COMTAlarmReadAction._targetIdentifiers
- _OBJC_IVAR_$_COMTAlarmReadResult._isComplete
- _OBJC_IVAR_$_COMTAlarmUpdateInterestAction._targetIdentifiers
- _OBJC_IVAR_$_COMTTimerDeleteAction._timer
- _OBJC_IVAR_$_COMTTimerReadAction._targetIdentifiers
- _OBJC_IVAR_$_COMTTimerReadResult._isComplete
- _OBJC_IVAR_$_COMTTimerUpdateInterestAction._targetIdentifiers
- _OBJC_METACLASS_$_COMTAlarmDeleteAction
- _OBJC_METACLASS_$_COMTAlarmDeleteResult
- _OBJC_METACLASS_$_COMTAlarmReadAction
- _OBJC_METACLASS_$_COMTAlarmUpdateInterestAction
- _OBJC_METACLASS_$_COMTAlarmUpdateResult
- _OBJC_METACLASS_$_COMTTimerDeleteAction
- _OBJC_METACLASS_$_COMTTimerDeleteResult
- _OBJC_METACLASS_$_COMTTimerReadAction
- _OBJC_METACLASS_$_COMTTimerUpdateInterestAction
- _OBJC_METACLASS_$_COMTTimerUpdateResult
- __OBJC_$_CLASS_METHODS_COMTAlarmDeleteAction
- __OBJC_$_CLASS_METHODS_COMTAlarmDeleteResult
- __OBJC_$_CLASS_METHODS_COMTAlarmReadAction
- __OBJC_$_CLASS_METHODS_COMTAlarmUpdateInterestAction
- __OBJC_$_CLASS_METHODS_COMTAlarmUpdateResult
- __OBJC_$_CLASS_METHODS_COMTTimerDeleteAction
- __OBJC_$_CLASS_METHODS_COMTTimerDeleteResult
- __OBJC_$_CLASS_METHODS_COMTTimerReadAction
- __OBJC_$_CLASS_METHODS_COMTTimerUpdateInterestAction
- __OBJC_$_CLASS_METHODS_COMTTimerUpdateResult
- __OBJC_$_INSTANCE_METHODS_COMTAlarmDeleteAction
- __OBJC_$_INSTANCE_METHODS_COMTAlarmDeleteResult
- __OBJC_$_INSTANCE_METHODS_COMTAlarmReadAction
- __OBJC_$_INSTANCE_METHODS_COMTAlarmUpdateInterestAction
- __OBJC_$_INSTANCE_METHODS_COMTAlarmUpdateResult
- __OBJC_$_INSTANCE_METHODS_COMTTimerDeleteAction
- __OBJC_$_INSTANCE_METHODS_COMTTimerDeleteResult
- __OBJC_$_INSTANCE_METHODS_COMTTimerReadAction
- __OBJC_$_INSTANCE_METHODS_COMTTimerUpdateInterestAction
- __OBJC_$_INSTANCE_METHODS_COMTTimerUpdateResult
- __OBJC_$_INSTANCE_VARIABLES_COMTAlarmDeleteAction
- __OBJC_$_INSTANCE_VARIABLES_COMTAlarmReadAction
- __OBJC_$_INSTANCE_VARIABLES_COMTAlarmUpdateInterestAction
- __OBJC_$_INSTANCE_VARIABLES_COMTTimerDeleteAction
- __OBJC_$_INSTANCE_VARIABLES_COMTTimerReadAction
- __OBJC_$_INSTANCE_VARIABLES_COMTTimerUpdateInterestAction
- __OBJC_$_PROP_LIST_COMTAlarmDeleteAction
- __OBJC_$_PROP_LIST_COMTAlarmReadAction
- __OBJC_$_PROP_LIST_COMTAlarmUpdateInterestAction
- __OBJC_$_PROP_LIST_COMTTimerDeleteAction
- __OBJC_$_PROP_LIST_COMTTimerReadAction
- __OBJC_$_PROP_LIST_COMTTimerUpdateInterestAction
- __OBJC_CLASS_RO_$_COMTAlarmDeleteAction
- __OBJC_CLASS_RO_$_COMTAlarmDeleteResult
- __OBJC_CLASS_RO_$_COMTAlarmReadAction
- __OBJC_CLASS_RO_$_COMTAlarmUpdateInterestAction
- __OBJC_CLASS_RO_$_COMTAlarmUpdateResult
- __OBJC_CLASS_RO_$_COMTTimerDeleteAction
- __OBJC_CLASS_RO_$_COMTTimerDeleteResult
- __OBJC_CLASS_RO_$_COMTTimerReadAction
- __OBJC_CLASS_RO_$_COMTTimerUpdateInterestAction
- __OBJC_CLASS_RO_$_COMTTimerUpdateResult
- __OBJC_METACLASS_RO_$_COMTAlarmDeleteAction
- __OBJC_METACLASS_RO_$_COMTAlarmDeleteResult
- __OBJC_METACLASS_RO_$_COMTAlarmReadAction
- __OBJC_METACLASS_RO_$_COMTAlarmUpdateInterestAction
- __OBJC_METACLASS_RO_$_COMTAlarmUpdateResult
- __OBJC_METACLASS_RO_$_COMTTimerDeleteAction
- __OBJC_METACLASS_RO_$_COMTTimerDeleteResult
- __OBJC_METACLASS_RO_$_COMTTimerReadAction
- __OBJC_METACLASS_RO_$_COMTTimerUpdateInterestAction
- __OBJC_METACLASS_RO_$_COMTTimerUpdateResult
- ___101-[CORapportTransport handleResponseToRequest:rapportRepresentation:options:error:responseHandler:at:]_block_invoke.126
- ___43-[COMeshAlarmAddOn addAlarm:member:client:]_block_invoke.188
- ___43-[COMeshAlarmAddOn addAlarm:member:client:]_block_invoke.188.cold.1
- ___43-[COMeshAlarmAddOn addAlarm:member:client:]_block_invoke.189
- ___43-[COMeshTimerAddOn addTimer:client:member:]_block_invoke.151
- ___43-[COMeshTimerAddOn addTimer:client:member:]_block_invoke.151.cold.1
- ___43-[COMeshTimerAddOn addTimer:client:member:]_block_invoke.152
- ___45-[COMeshAlarmAddOn setInterests:asAccessory:]_block_invoke
- ___45-[COMeshAlarmAddOn setInterests:asAccessory:]_block_invoke.cold.1
- ___45-[COMeshTimerAddOn setInterests:asAccessory:]_block_invoke
- ___45-[COMeshTimerAddOn setInterests:asAccessory:]_block_invoke.cold.1
- ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke.194
- ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke.198
- ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke_2.197
- ___46-[COMeshAlarmAddOn removeAlarm:member:client:]_block_invoke_2.197.cold.1
- ___46-[COMeshAlarmAddOn updateAlarm:member:client:]_block_invoke.191
- ___46-[COMeshAlarmAddOn updateAlarm:member:client:]_block_invoke.191.cold.1
- ___46-[COMeshAlarmAddOn updateAlarm:member:client:]_block_invoke.192
- ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke.157
- ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke.161
- ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke_2.160
- ___46-[COMeshTimerAddOn removeTimer:client:member:]_block_invoke_2.160.cold.1
- ___46-[COMeshTimerAddOn updateTimer:client:member:]_block_invoke.154
- ___46-[COMeshTimerAddOn updateTimer:client:member:]_block_invoke.154.cold.1
- ___46-[COMeshTimerAddOn updateTimer:client:member:]_block_invoke.155
- ___47-[COMeshTimerAddOn _timersForAccessory:member:]_block_invoke_3
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.147
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.149
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.149.cold.1
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.152
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke.154
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.148
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.151
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.151.cold.1
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.153
- ___47-[CORapportTransport _registerHandlersOnClient]_block_invoke_2.153.cold.1
- ___50-[COMeshAlarmAddOn handleAlarmSnoozeNotification:]_block_invoke.223
- ___50-[COMeshAlarmAddOn handleAlarmsAddedNotification:]_block_invoke.216
- ___50-[COMeshTimerAddOn handleTimersAddedNotification:]_block_invoke.178
- ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke.204
- ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke.205
- ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke.205.cold.1
- ___52-[COMeshAlarmAddOn handleAlarmReadRequest:callback:]_block_invoke_2.206
- ___52-[COMeshAlarmAddOn handleAlarmsRemovedNotification:]_block_invoke.217
- ___52-[COMeshAlarmAddOn handleAlarmsUpdatedNotification:]_block_invoke.221
- ___52-[COMeshTimerAddOn _concludeMerge:usingLocalTimers:]_block_invoke.142
- ___52-[COMeshTimerAddOn handleTimerReadRequest:callback:]_block_invoke.166
- ___52-[COMeshTimerAddOn handleTimersRemovedNotification:]_block_invoke.180
- ___52-[COMeshTimerAddOn handleTimersUpdatedNotification:]_block_invoke.181
- ___53-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:client:]_block_invoke.199
- ___54-[COMeshAlarmAddOn dismissAlarmWithIdentifier:client:]_block_invoke.200
- ___54-[COMeshAlarmAddOn dismissAlarmWithIdentifier:client:]_block_invoke.200.cold.1
- ___54-[COMeshAlarmAddOn dismissAlarmWithIdentifier:client:]_block_invoke.202
- ___54-[COMeshAlarmAddOn handleAlarmCreateRequest:callback:]_block_invoke.207
- ___54-[COMeshAlarmAddOn handleAlarmCreateRequest:callback:]_block_invoke.207.cold.1
- ___54-[COMeshAlarmAddOn handleAlarmDeleteRequest:callback:]_block_invoke.210
- ___54-[COMeshAlarmAddOn handleAlarmDeleteRequest:callback:]_block_invoke.210.cold.1
- ___54-[COMeshAlarmAddOn handleAlarmUpdateRequest:callback:]_block_invoke.209
- ___54-[COMeshAlarmAddOn handleAlarmUpdateRequest:callback:]_block_invoke.209.cold.1
- ___54-[COMeshTimerAddOn dismissTimerWithIdentifier:client:]_block_invoke.162
- ___54-[COMeshTimerAddOn dismissTimerWithIdentifier:client:]_block_invoke.162.cold.1
- ___54-[COMeshTimerAddOn dismissTimerWithIdentifier:client:]_block_invoke.164
- ___54-[COMeshTimerAddOn handleTimerCreateRequest:callback:]_block_invoke.167
- ___54-[COMeshTimerAddOn handleTimerCreateRequest:callback:]_block_invoke.167.cold.1
- ___54-[COMeshTimerAddOn handleTimerDeleteRequest:callback:]_block_invoke.169
- ___54-[COMeshTimerAddOn handleTimerDeleteRequest:callback:]_block_invoke.169.cold.1
- ___54-[COMeshTimerAddOn handleTimerUpdateRequest:callback:]_block_invoke.168
- ___54-[COMeshTimerAddOn handleTimerUpdateRequest:callback:]_block_invoke.168.cold.1
- ___54-[CORapportTransport sendRequest:withResponseHandler:]_block_invoke.107
- ___54-[CORapportTransport sendRequest:withResponseHandler:]_block_invoke_2.108
- ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.212
- ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.212.cold.1
- ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.213
- ___55-[COMeshAlarmAddOn handleAlarmDismissRequest:callback:]_block_invoke.214
- ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.173
- ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.173.cold.1
- ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.174
- ___55-[COMeshTimerAddOn handleTimerDismissRequest:callback:]_block_invoke.175
- ___60-[COMeshAlarmAddOn mediaSystemCompanionTransitionedFrom:to:]_block_invoke.247
- ___60-[COMeshAlarmAddOn mediaSystemCompanionTransitionedFrom:to:]_block_invoke_2.248
- ___60-[COMeshAlarmAddOn mediaSystemCompanionTransitionedFrom:to:]_block_invoke_3.249
- ___61-[COMeshAlarmAddOn alarmsForAccessories:fromClient:callback:]_block_invoke.228
- ___61-[COMeshAlarmAddOn alarmsForAccessories:fromClient:callback:]_block_invoke_2.229
- ___61-[COMeshTimerAddOn timersForAccessories:fromClient:callback:]_block_invoke.186
- ___64-[COMeshAlarmAddOn handleAlarmFiringAlarmDismissedNotification:]_block_invoke.222
- ___64-[COMeshTimerAddOn handleTimerFiringTimerDismissedNotification:]_block_invoke.182
- ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.238
- ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.238.cold.1
- ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.239
- ___70-[COMeshAlarmAddOn snoozeAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.240
- ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.242
- ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.242.cold.1
- ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.243
- ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.243.cold.1
- ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.244
- ___71-[COMeshAlarmAddOn dismissAlarmWithIdentifier:fromClient:withCallback:]_block_invoke.244.cold.1
- ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke.266
- ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke.268
- ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke_2.267
- ___71-[COMeshAlarmAddOn reapNonRepeatingAlarmsOlderThanDate:accessory:home:]_block_invoke_2.267.cold.1
- ___72-[COMeshAlarmAddOn interestTracker:setInterests:forMember:triggerReset:]_block_invoke
- ___72-[COMeshAlarmAddOn interestTracker:setInterests:forMember:triggerReset:]_block_invoke_2
- ___72-[COMeshAlarmAddOn interestTracker:setInterests:forMember:triggerReset:]_block_invoke_2.cold.1
- ___72-[COMeshTimerAddOn interestTracker:setInterests:forMember:triggerReset:]_block_invoke
- ___72-[COMeshTimerAddOn interestTracker:setInterests:forMember:triggerReset:]_block_invoke_2
- ___72-[COMeshTimerAddOn interestTracker:setInterests:forMember:triggerReset:]_block_invoke_2.cold.1
- ___77-[CORapportTransport _updateRequestTimesFromRapportRepresentation:start:end:]_block_invoke.133
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.167.cold.1
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.167.cold.2
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.169
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.172.cold.1
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.172.cold.2
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.175
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.175.cold.1
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke.176
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke_2.177
- ___84-[COMeshAlarmAddOn _alarmsForAccessory:allowLocalStorage:usingLeader:member:client:]_block_invoke_4
- ___95-[CORapportTransport handleRequestIdentifier:rapportRepresentation:options:responseHandler:at:]_block_invoke.121
- ___95-[CORapportTransport handleRequestIdentifier:rapportRepresentation:options:responseHandler:at:]_block_invoke_2.125
- ___block_descriptor_40_e8_32s_e26_"COMTAlarmReadAction"8?0ls32l8
- ___block_descriptor_40_e8_32s_e26_"COMTTimerReadAction"8?0ls32l8
- ___block_descriptor_40_e8_32s_e28_"COMTAlarmDeleteAction"8?0ls32l8
- ___block_descriptor_40_e8_32s_e28_"COMTTimerDeleteAction"8?0ls32l8
- ___block_descriptor_40_e8_32s_e36_"COMTAlarmUpdateInterestAction"8?0ls32l8
- ___block_descriptor_40_e8_32s_e36_"COMTTimerUpdateInterestAction"8?0ls32l8
- ___block_descriptor_49_e8_32s40w_e32_v24?0"COMTResult"8"NSError"16lw40l8s32l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.166
- ___block_literal_global.171
- ___block_literal_global.220
- _objc_msgSend$initWithDelegate:primaryAvailable:secondary:
- _objc_msgSend$initWithTargetIdentifiers:
- _objc_msgSend$interestTracker:setInterests:forMember:triggerReset:
- _objc_msgSend$isComplete
- _objc_msgSend$requestAction:members:activity:fallback:withCompletion:
- _objc_msgSend$setInterests:asAccessory:
- _objc_msgSend$shouldTriggerElectionForElectionInfo:
CStrings:
+ "%p failed to set interests for tracker %p via %p: %@"
+ "%p setting interests for tracker %p via %{public}@ to %{public}@"
+ "%p successfully set interests for tracker %p via %p"
+ "%p using interest tracker %p for can dispatch of %@"
+ "%{public}@ Our generation %llu is greater than the incoming generation %llu"
+ "%{public}@ The leader %@ and generation %llu for command  %@ on node has not changed"
+ "%{public}@ dispatching %{public}@ for %p to %p"
+ "196.11.1"
+ "<%@: %p, id = %@, type = %@>"
+ "@44@0:8@16@24B32@36"
+ "B20@0:8B16"
+ "TB,N,V_triggerReset"
+ "TQ,N,V_interestsSerial"
+ "TQ,N,V_remoteInterests"
+ "_checkTriggerReset"
+ "_informDelegateAboutNodeAddition:oldState:"
+ "_informDelegateAboutNodeRemoval:oldState:"
+ "_interestsSerial"
+ "_nextInterestSerial"
+ "_postCanDispatchChanged:forAccessory:toObserver:"
+ "_postNotificationName:forAccessory:toAddOn:"
+ "_remoteInterests"
+ "_setInterest:"
+ "_triggerReset"
+ "alarmAddOn:resetAccesory:"
+ "canDispatchWithPrimary:"
+ "com.apple.opal"
+ "generationAndLeaderNotEqualTo:"
+ "hasGreaterGenerationThan:"
+ "initWithAccessory:delegate:primaryAvailable:secondary:"
+ "interestTracker:setInterests:forMember:callback:"
+ "interestTrackerTriggerReset:"
+ "interestsSerial"
+ "isOpalEnabled"
+ "remoteInterests"
+ "setInterests:asAccessory:withCallback:"
+ "setInterestsSerial:"
+ "setRemoteInterests:"
+ "setTriggerReset:"
+ "timerAddOn:resetAccesory:"
+ "triggerReset"
+ "v24@0:8@\"COInterestTracker\"16"
+ "v32@0:8@\"COMeshAlarmAddOn\"16@\"NSUUID\"24"
+ "v32@0:8@\"COMeshTimerAddOn\"16@\"NSUUID\"24"
+ "v48@0:8@\"COInterestTracker\"16@\"NSSet\"24@\"COClusterMember\"32@?<v@?@\"NSError\">40"
- "%p failed to set interests for tracker %p: %@"
- "%p setting interests for tracker %p to %@"
- "%p successfully set interests for tracker %p"
- "%{public}@ dispatching %{public}@ to %p"
- "196.0.3"
- "@\"COMTAlarmDeleteAction\"8@?0"
- "@\"COMTAlarmReadAction\"8@?0"
- "@\"COMTAlarmUpdateInterestAction\"8@?0"
- "@\"COMTTimerDeleteAction\"8@?0"
- "@\"COMTTimerReadAction\"8@?0"
- "@\"COMTTimerUpdateInterestAction\"8@?0"
- "@36@0:8@16B24@28"
- "ARC"
- "ATI"
- "COMTAlarmDeleteAction"
- "COMTAlarmDeleteResult"
- "COMTAlarmReadAction"
- "COMTAlarmUpdateInterestAction"
- "COMTAlarmUpdateResult"
- "COMTTimerDeleteAction"
- "COMTTimerDeleteResult"
- "COMTTimerReadAction"
- "COMTTimerUpdateInterestAction"
- "COMTTimerUpdateResult"
- "DA"
- "DT"
- "TB,R,N,V_isComplete"
- "TRC"
- "TTI"
- "_isComplete"
- "initChunkedWithActionIdentifier:"
- "initWithDelegate:primaryAvailable:secondary:"
- "initWithTargetIdentifiers:"
- "interestTracker:setInterests:forMember:triggerReset:"
- "isComplete"
- "setInterests:asAccessory:"
- "shouldTriggerElectionForElectionInfo:"
- "v44@0:8@\"COInterestTracker\"16@\"NSSet\"24@\"COClusterMember\"32B40"

```
