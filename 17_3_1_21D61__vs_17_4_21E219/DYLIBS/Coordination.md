## Coordination

> `/System/Library/PrivateFrameworks/Coordination.framework/Coordination`

```diff

-196.30.2.0.0
-  __TEXT.__text: 0x2c9e4
+196.40.16.0.0
+  __TEXT.__text: 0x2cb64
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x222c
+  __TEXT.__objc_methlist: 0x233c
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x92c
-  __TEXT.__cstring: 0x1257
+  __TEXT.__cstring: 0x1271
   __TEXT.__oslogstring: 0x28f7
-  __TEXT.__unwind_info: 0xcc8
-  __TEXT.__objc_classname: 0x8b7
-  __TEXT.__objc_methname: 0x5160
-  __TEXT.__objc_methtype: 0xf88
-  __TEXT.__objc_stubs: 0x3be0
+  __TEXT.__unwind_info: 0xcd4
+  __TEXT.__objc_classname: 0x8c9
+  __TEXT.__objc_methname: 0x5342
+  __TEXT.__objc_methtype: 0xf99
+  __TEXT.__objc_stubs: 0x3c40
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0xfb8
-  __DATA_CONST.__objc_classlist: 0x1b0
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x41e0
-  __DATA_CONST.__objc_selrefs: 0x1230
+  __DATA_CONST.__objc_const: 0x4270
+  __DATA_CONST.__objc_selrefs: 0x1290
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_classrefs: 0x2b0
+  __DATA_CONST.__objc_superrefs: 0x160
   __AUTH_CONST.__cfstring: 0x14a0
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__objc_const: 0x1550
+  __AUTH_CONST.__objc_const: 0x15e0
   __AUTH_CONST.__auth_got: 0x2d0
-  __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0x2a0
-  __DATA.__objc_superrefs: 0x158
-  __DATA.__objc_ivar: 0x2a8
+  __AUTH.__objc_data: 0xf00
+  __DATA.__objc_ivar: 0x2b4
   __DATA.__data: 0x900
   __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x230

   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E3D34E99-4990-3E84-A6DB-8DA7E7344AAD
-  Functions: 1096
-  Symbols:   3827
-  CStrings:  1692
+  UUID: 827CC003-1DC6-315D-BC8E-E73435FF8A27
+  Functions: 1117
+  Symbols:   3881
+  CStrings:  1714
 
Symbols:
+ +[COFeatureStatus isNoDaemonMessageChannelEnabled]
+ +[COMessageChannel messageChannelWithTopic:cluster:manualGrouping:]
+ -[COMessageChannel addGroupedHomeKitIdentifiers:]
+ -[COMessageChannel foundHandler]
+ -[COMessageChannel groupedHomeKitIdentifiers]
+ -[COMessageChannel lostHandler]
+ -[COMessageChannel registerMemberFoundHandler:]
+ -[COMessageChannel registerMemberLostHandler:]
+ -[COMessageChannel removeGroupedHomeKitIdentifiers:]
+ -[COMessageChannel setFoundHandler:]
+ -[COMessageChannel setLostHandler:]
+ -[_COMessageChannel activateWithCompletion:]
+ -[_COMessageChannel addGroupedHomeKitIdentifiers:]
+ -[_COMessageChannel broadcastRequest:recipientsCallback:responseCompletionHandler:]
+ -[_COMessageChannel initWithTopic:cluster:manualGrouping:]
+ -[_COMessageChannel registerHandler:forRequestClass:]
+ -[_COMessageChannel registerMemberFoundHandler:]
+ -[_COMessageChannel registerMemberLostHandler:]
+ -[_COMessageChannel removeGroupedHomeKitIdentifiers:]
+ -[_COMessageChannel sendRequest:members:withCompletionHandler:]
+ -[_COMessageChannel sendRequest:withCompletionHandler:]
+ GCC_except_table104
+ GCC_except_table171
+ GCC_except_table56
+ GCC_except_table60
+ GCC_except_table63
+ GCC_except_table87
+ GCC_except_table90
+ GCC_except_table97
+ _OBJC_CLASS_$__COMessageChannel
+ _OBJC_IVAR_$_COMessageChannel._foundHandler
+ _OBJC_IVAR_$_COMessageChannel._groupedHomeKitIdentifiers
+ _OBJC_IVAR_$_COMessageChannel._lostHandler
+ _OBJC_METACLASS_$__COMessageChannel
+ __OBJC_$_CLASS_METHODS_COMessageChannel
+ __OBJC_$_INSTANCE_METHODS__COMessageChannel
+ __OBJC_CLASS_RO_$__COMessageChannel
+ __OBJC_METACLASS_RO_$__COMessageChannel
+ ___27-[COAlarmManager addAlarm:]_block_invoke.155
+ ___27-[COAlarmManager addAlarm:]_block_invoke.155.cold.1
+ ___27-[COTimerManager addTimer:]_block_invoke.156
+ ___27-[COTimerManager addTimer:]_block_invoke.156.cold.1
+ ___30-[COAlarmManager removeAlarm:]_block_invoke.157
+ ___30-[COAlarmManager removeAlarm:]_block_invoke.157.cold.1
+ ___30-[COAlarmManager updateAlarm:]_block_invoke.156
+ ___30-[COAlarmManager updateAlarm:]_block_invoke.156.cold.1
+ ___30-[COTimerManager removeTimer:]_block_invoke.158
+ ___30-[COTimerManager removeTimer:]_block_invoke.158.cold.1
+ ___30-[COTimerManager updateTimer:]_block_invoke.157
+ ___30-[COTimerManager updateTimer:]_block_invoke.157.cold.1
+ ___33-[COAlarmManager removeObserver:]_block_invoke.161
+ ___33-[COAlarmManager removeObserver:]_block_invoke.161.cold.1
+ ___33-[COTimerManager removeObserver:]_block_invoke.161
+ ___33-[COTimerManager removeObserver:]_block_invoke.161.cold.1
+ ___38-[COTimerManager _timersForAccessory:]_block_invoke.130
+ ___38-[COTimerManager _timersForAccessory:]_block_invoke.130.cold.1
+ ___39-[COAlarmManager alarmsForAccessories:]_block_invoke.138
+ ___39-[COAlarmManager alarmsForAccessories:]_block_invoke.138.cold.1
+ ___39-[COAlarmManager alarmsForAccessories:]_block_invoke.140
+ ___39-[COTimerManager timersForAccessories:]_block_invoke.143
+ ___39-[COTimerManager timersForAccessories:]_block_invoke.143.cold.1
+ ___39-[COTimerManager timersForAccessories:]_block_invoke.145
+ ___42-[COClusterRoleMonitor _serviceConnection]_block_invoke.93
+ ___44-[COAlarmManager _registerObserverWithName:]_block_invoke.164
+ ___44-[COAlarmManager _registerObserverWithName:]_block_invoke.164.cold.1
+ ___44-[COAlarmManager snoozeAlarmWithIdentifier:]_block_invoke.158
+ ___44-[COAlarmManager snoozeAlarmWithIdentifier:]_block_invoke.158.cold.1
+ ___44-[COMessageChannel _activateWithCompletion:]_block_invoke.81
+ ___44-[COTimerManager _registerObserverWithName:]_block_invoke.164
+ ___44-[COTimerManager _registerObserverWithName:]_block_invoke.164.cold.1
+ ___45-[COAlarmManager alarmsForAccessoryMementos:]_block_invoke.147
+ ___45-[COAlarmManager alarmsForAccessoryMementos:]_block_invoke.147.cold.1
+ ___45-[COAlarmManager alarmsForAccessoryMementos:]_block_invoke.149
+ ___45-[COAlarmManager dismissAlarmWithIdentifier:]_block_invoke.159
+ ___45-[COAlarmManager dismissAlarmWithIdentifier:]_block_invoke.159.cold.1
+ ___45-[COTimerManager dismissTimerWithIdentifier:]_block_invoke.159
+ ___45-[COTimerManager dismissTimerWithIdentifier:]_block_invoke.159.cold.1
+ ___45-[COTimerManager timersForAccessoryMementos:]_block_invoke.152
+ ___45-[COTimerManager timersForAccessoryMementos:]_block_invoke.152.cold.1
+ ___45-[COTimerManager timersForAccessoryMementos:]_block_invoke.154
+ ___50-[COMessageChannel stopMessageSession:withNotice:]_block_invoke.70
+ ___51-[COAlarmManager _remoteInterfaceWithErrorHandler:]_block_invoke.125
+ ___51-[COAlarmManager _remoteInterfaceWithErrorHandler:]_block_invoke.125.cold.1
+ ___51-[COStateManager _remoteInterfaceWithErrorHandler:]_block_invoke.167
+ ___51-[COStateManager _remoteInterfaceWithErrorHandler:]_block_invoke.167.cold.1
+ ___51-[COTimerManager _remoteInterfaceWithErrorHandler:]_block_invoke.127
+ ___51-[COTimerManager _remoteInterfaceWithErrorHandler:]_block_invoke.127.cold.1
+ ___52-[COAlarmManager _canDispatchForAssociatedAccessory]_block_invoke.153
+ ___52-[COTimerManager _canDispatchForAssociatedAccessory]_block_invoke.134
+ ___53-[COMessageChannel _remoteInterfaceWithErrorHandler:]_block_invoke.154
+ ___53-[COMessageChannel _remoteInterfaceWithErrorHandler:]_block_invoke.154.cold.1
+ ___53-[COMessageChannel _startSessionWithProducer:member:]_block_invoke.172
+ ___56-[COCapabilityManager _remoteInterfaceWithErrorHandler:]_block_invoke.68
+ ___56-[COCapabilityManager _remoteInterfaceWithErrorHandler:]_block_invoke.68.cold.1
+ ___58-[COAlarmManager _alarmsForAccessory:includingSleepAlarm:]_block_invoke.128
+ ___58-[COAlarmManager _alarmsForAccessory:includingSleepAlarm:]_block_invoke.128.cold.1
+ ___61-[COMessageChannel _startSessionWithProducer:member:request:]_block_invoke.174
+ ___71-[COStateManager(Doorbell) delayForDoorbellChimeWithCompletionHandler:]_block_invoke.246
+ ___74-[COMessageChannel addSessionConsumerWithSubTopic:delegate:dispatchQueue:]_block_invoke.64
+ ___74-[COMessageChannel addSessionProducerWithSubTopic:delegate:dispatchQueue:]_block_invoke.59
+ ___75-[COMessageChannel _callbackProducersAndConsumersAfterActivationWithError:]_block_invoke.187
+ ___75-[COMessageChannel _callbackProducersAndConsumersAfterActivationWithError:]_block_invoke.188
+ ___75-[COMessageChannel _callbackProducersAndConsumersAfterActivationWithError:]_block_invoke_2.189
+ ___75-[COMessageChannel _deliverSuccessfullyStartedSession:withMember:consumer:]_block_invoke.164
+ ___85-[COStateManager(ClusterExamination) fetchCompositionForCluster:dispatchQueue:block:]_block_invoke.242
+ ___93-[COMessageChannel receivedRequestWithPayload:payloadType:requestID:fromMember:withCallback:]_block_invoke.74
+ ___93-[COMessageChannel receivedRequestWithPayload:payloadType:requestID:fromMember:withCallback:]_block_invoke.74.cold.1
+ ___93-[COMessageChannel receivedRequestWithPayload:payloadType:requestID:fromMember:withCallback:]_block_invoke.74.cold.2
+ ___block_literal_global.131
+ ___block_literal_global.133
+ ___block_literal_global.136
+ ___block_literal_global.139
+ ___block_literal_global.141
+ ___block_literal_global.145
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.176
+ _objc_msgSend$initWithTopic:cluster:
+ _objc_msgSend$initWithTopic:cluster:manualGrouping:
+ _objc_msgSend$isNoDaemonMessageChannelEnabled
- GCC_except_table103
- GCC_except_table161
- GCC_except_table55
- GCC_except_table59
- GCC_except_table62
- GCC_except_table69
- GCC_except_table85
- GCC_except_table89
- GCC_except_table92
- GCC_except_table96
- ___27-[COAlarmManager addAlarm:]_block_invoke.154
- ___27-[COAlarmManager addAlarm:]_block_invoke.154.cold.1
- ___27-[COTimerManager addTimer:]_block_invoke.155
- ___27-[COTimerManager addTimer:]_block_invoke.155.cold.1
- ___30-[COAlarmManager removeAlarm:]_block_invoke.156
- ___30-[COAlarmManager removeAlarm:]_block_invoke.156.cold.1
- ___30-[COAlarmManager updateAlarm:]_block_invoke.155
- ___30-[COAlarmManager updateAlarm:]_block_invoke.155.cold.1
- ___30-[COTimerManager removeTimer:]_block_invoke.157
- ___30-[COTimerManager removeTimer:]_block_invoke.157.cold.1
- ___30-[COTimerManager updateTimer:]_block_invoke.156
- ___30-[COTimerManager updateTimer:]_block_invoke.156.cold.1
- ___33-[COAlarmManager removeObserver:]_block_invoke.160
- ___33-[COAlarmManager removeObserver:]_block_invoke.160.cold.1
- ___33-[COTimerManager removeObserver:]_block_invoke.160
- ___33-[COTimerManager removeObserver:]_block_invoke.160.cold.1
- ___38-[COTimerManager _timersForAccessory:]_block_invoke.129
- ___38-[COTimerManager _timersForAccessory:]_block_invoke.129.cold.1
- ___39-[COAlarmManager alarmsForAccessories:]_block_invoke.136
- ___39-[COAlarmManager alarmsForAccessories:]_block_invoke.136.cold.1
- ___39-[COAlarmManager alarmsForAccessories:]_block_invoke.139
- ___39-[COTimerManager timersForAccessories:]_block_invoke.141
- ___39-[COTimerManager timersForAccessories:]_block_invoke.141.cold.1
- ___39-[COTimerManager timersForAccessories:]_block_invoke.144
- ___42-[COClusterRoleMonitor _serviceConnection]_block_invoke.92
- ___44-[COAlarmManager _registerObserverWithName:]_block_invoke.163
- ___44-[COAlarmManager _registerObserverWithName:]_block_invoke.163.cold.1
- ___44-[COAlarmManager snoozeAlarmWithIdentifier:]_block_invoke.157
- ___44-[COAlarmManager snoozeAlarmWithIdentifier:]_block_invoke.157.cold.1
- ___44-[COMessageChannel _activateWithCompletion:]_block_invoke.79
- ___44-[COTimerManager _registerObserverWithName:]_block_invoke.163
- ___44-[COTimerManager _registerObserverWithName:]_block_invoke.163.cold.1
- ___45-[COAlarmManager alarmsForAccessoryMementos:]_block_invoke.145
- ___45-[COAlarmManager alarmsForAccessoryMementos:]_block_invoke.145.cold.1
- ___45-[COAlarmManager alarmsForAccessoryMementos:]_block_invoke.148
- ___45-[COAlarmManager dismissAlarmWithIdentifier:]_block_invoke.158
- ___45-[COAlarmManager dismissAlarmWithIdentifier:]_block_invoke.158.cold.1
- ___45-[COTimerManager dismissTimerWithIdentifier:]_block_invoke.158
- ___45-[COTimerManager dismissTimerWithIdentifier:]_block_invoke.158.cold.1
- ___45-[COTimerManager timersForAccessoryMementos:]_block_invoke.150
- ___45-[COTimerManager timersForAccessoryMementos:]_block_invoke.150.cold.1
- ___45-[COTimerManager timersForAccessoryMementos:]_block_invoke.153
- ___50-[COMessageChannel stopMessageSession:withNotice:]_block_invoke.68
- ___51-[COAlarmManager _remoteInterfaceWithErrorHandler:]_block_invoke.124
- ___51-[COAlarmManager _remoteInterfaceWithErrorHandler:]_block_invoke.124.cold.1
- ___51-[COStateManager _remoteInterfaceWithErrorHandler:]_block_invoke.166
- ___51-[COStateManager _remoteInterfaceWithErrorHandler:]_block_invoke.166.cold.1
- ___51-[COTimerManager _remoteInterfaceWithErrorHandler:]_block_invoke.126
- ___51-[COTimerManager _remoteInterfaceWithErrorHandler:]_block_invoke.126.cold.1
- ___52-[COAlarmManager _canDispatchForAssociatedAccessory]_block_invoke.152
- ___52-[COTimerManager _canDispatchForAssociatedAccessory]_block_invoke.133
- ___53-[COMessageChannel _remoteInterfaceWithErrorHandler:]_block_invoke.151
- ___53-[COMessageChannel _remoteInterfaceWithErrorHandler:]_block_invoke.151.cold.1
- ___53-[COMessageChannel _startSessionWithProducer:member:]_block_invoke.169
- ___56-[COCapabilityManager _remoteInterfaceWithErrorHandler:]_block_invoke.67
- ___56-[COCapabilityManager _remoteInterfaceWithErrorHandler:]_block_invoke.67.cold.1
- ___58-[COAlarmManager _alarmsForAccessory:includingSleepAlarm:]_block_invoke.127
- ___58-[COAlarmManager _alarmsForAccessory:includingSleepAlarm:]_block_invoke.127.cold.1
- ___61-[COMessageChannel _startSessionWithProducer:member:request:]_block_invoke.171
- ___71-[COStateManager(Doorbell) delayForDoorbellChimeWithCompletionHandler:]_block_invoke.245
- ___74-[COMessageChannel addSessionConsumerWithSubTopic:delegate:dispatchQueue:]_block_invoke.62
- ___74-[COMessageChannel addSessionProducerWithSubTopic:delegate:dispatchQueue:]_block_invoke.57
- ___75-[COMessageChannel _callbackProducersAndConsumersAfterActivationWithError:]_block_invoke.184
- ___75-[COMessageChannel _callbackProducersAndConsumersAfterActivationWithError:]_block_invoke.185
- ___75-[COMessageChannel _callbackProducersAndConsumersAfterActivationWithError:]_block_invoke_2.186
- ___75-[COMessageChannel _deliverSuccessfullyStartedSession:withMember:consumer:]_block_invoke.161
- ___85-[COStateManager(ClusterExamination) fetchCompositionForCluster:dispatchQueue:block:]_block_invoke.241
- ___93-[COMessageChannel receivedRequestWithPayload:payloadType:requestID:fromMember:withCallback:]_block_invoke.72
- ___93-[COMessageChannel receivedRequestWithPayload:payloadType:requestID:fromMember:withCallback:]_block_invoke.72.cold.1
- ___93-[COMessageChannel receivedRequestWithPayload:payloadType:requestID:fromMember:withCallback:]_block_invoke.72.cold.2
- ___block_literal_global.130
- ___block_literal_global.132
- ___block_literal_global.135
- ___block_literal_global.138
- ___block_literal_global.140
- ___block_literal_global.144
- ___block_literal_global.149
- ___block_literal_global.151
- ___block_literal_global.173
CStrings:
+ "\x11\x13="
+ "@36@0:8@16@24B32"
+ "T@\"NSArray\",R,N,V_groupedHomeKitIdentifiers"
+ "T@\"NSString\",?,R,C"
+ "T@?,C,N,V_foundHandler"
+ "T@?,C,N,V_lostHandler"
+ "_COMessageChannel"
+ "_foundHandler"
+ "_groupedHomeKitIdentifiers"
+ "_lostHandler"
+ "addGroupedHomeKitIdentifiers:"
+ "foundHandler"
+ "groupedHomeKitIdentifiers"
+ "initWithTopic:cluster:manualGrouping:"
+ "isNoDaemonMessageChannelEnabled"
+ "lostHandler"
+ "messageChannelWithTopic:cluster:manualGrouping:"
+ "no_daemon_message_channel"
+ "registerMemberFoundHandler:"
+ "registerMemberLostHandler:"
+ "removeGroupedHomeKitIdentifiers:"
+ "setFoundHandler:"
+ "setLostHandler:"
- "\x11\x13:"

```
