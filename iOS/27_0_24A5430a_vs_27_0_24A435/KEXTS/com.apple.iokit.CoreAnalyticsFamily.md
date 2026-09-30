## com.apple.iokit.CoreAnalyticsFamily

> `com.apple.iokit.CoreAnalyticsFamily`

```diff

 569.0.5.0.0
   __TEXT.__cstring: 0x1eae
   __TEXT.__os_log: 0x1941
-  __TEXT_EXEC.__text: 0x8548
+  __TEXT_EXEC.__text: 0x885c
   __TEXT_EXEC.__auth_stubs: 0x3f0
   __DATA.__data: 0xc4
   __DATA.__common: 0x108
Functions:
~ sub_fffffe0009ad9700 -> sub_fffffe0009b69250 : 68 -> 72
~ sub_fffffe0009ad9754 -> sub_fffffe0009b692a8 : 104 -> 108
~ __ZN28CoreAnalyticsEventRatePolicy12withWorkloopEP10IOWorkLoop : 168 -> 172
~ __ZN28CoreAnalyticsEventRatePolicy16initWithWorkloopEP10IOWorkLoop : 576 -> 580
~ __ZN28CoreAnalyticsEventRatePolicy24handleNewMeasurementSpanEP18IOTimerEventSource : 60 -> 64
~ sub_fffffe0009ad9ae0 -> sub_fffffe0009b69644 : 208 -> 212
~ __ZN28CoreAnalyticsEventRatePolicy21zeroOutPerEventCountsEv : 508 -> 512
~ __ZN28CoreAnalyticsEventRatePolicy22incrementCountForEventEP8OSString : 444 -> 448
~ __ZN28CoreAnalyticsEventRatePolicy24sendBudgetExceededReportEv : 500 -> 504
~ __ZN28CoreAnalyticsEventRatePolicy14isRateExceededEP8OSString : 116 -> 120
~ __ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray : 1132 -> 1136
~ __GLOBAL__sub_I_CoreAnalyticsEventRatePolicy.cpp : 80 -> 84
~ __ZN16CoreAnalyticsHub9MetaClassC1Ev : 72 -> 76
~ sub_fffffe0009ada750 -> sub_fffffe0009b6a2d4 : 52 -> 56
~ sub_fffffe0009ada784 -> sub_fffffe0009b6a30c : 52 -> 56
~ sub_fffffe0009ada7c8 -> sub_fffffe0009b6a354 : 68 -> 72
~ sub_fffffe0009ada834 -> sub_fffffe0009b6a3c4 : 72 -> 76
~ sub_fffffe0009ada87c -> sub_fffffe0009b6a410 : 104 -> 108
~ sub_fffffe0009ada8f8 -> sub_fffffe0009b6a490 : 88 -> 92
~ sub_fffffe0009ada950 -> sub_fffffe0009b6a4ec : 88 -> 92
~ __ZN16CoreAnalyticsHub5startEP9IOService : 1432 -> 1436
~ __ZN16CoreAnalyticsHub21sendUpEventAndPayloadEP8OSStringP8OSObject : 1028 -> 1032
~ sub_fffffe0009adb344 -> sub_fffffe0009b6aeec : 96 -> 100
~ __ZN16CoreAnalyticsHub20handleNagTimerExpiryEP18IOTimerEventSource : 220 -> 224
~ __ZN16CoreAnalyticsHub21handleDemoTimerExpiryEP18IOTimerEventSource : 200 -> 204
~ __ZN16CoreAnalyticsHub32handleUserClientRetryTimerExpiryEP18IOTimerEventSource : 112 -> 116
~ __ZN16CoreAnalyticsHub15createReportersEv : 1392 -> 1396
~ __ZN16CoreAnalyticsHub13publishLegendEv : 288 -> 292
~ _IOCoreAnalyticsSendEvent : 144 -> 148
~ __ZN16CoreAnalyticsHub4stopEP9IOService : 164 -> 168
~ __ZN16CoreAnalyticsHub4freeEv : 380 -> 384
~ sub_fffffe0009adbf88 -> sub_fffffe0009b6bb54 : 176 -> 180
~ __ZN16CoreAnalyticsHub20__newUserClientGatedEP4taskPvjP12OSDictionaryPP12IOUserClient : 272 -> 276
~ sub_fffffe0009adc168 -> sub_fffffe0009b6bd3c : 84 -> 88
~ __ZN16CoreAnalyticsHub18setupNewUserClientEP4taskPvjP12OSDictionaryP12IOUserClient : 252 -> 256
~ __ZN16CoreAnalyticsHub14setClientGatedEP23CoreAnalyticsUserClient : 312 -> 316
~ __ZN16CoreAnalyticsHub5closeEP9IOServicej : 76 -> 80
~ __ZN16CoreAnalyticsHub27incrementEventNameRateLimitEP8OSString : 316 -> 320
~ __ZN16CoreAnalyticsHub24incrementEventNameFailedEP8OSString : 316 -> 320
~ __ZN16CoreAnalyticsHub16serializePayloadEP8OSObjectP11OSSerializePm : 208 -> 212
~ __ZN16CoreAnalyticsHub26incrementEventNameReceivedEP8OSString : 316 -> 320
~ __ZN16CoreAnalyticsHub37incrementEventNameSharedDataQueueFullEP8OSString : 316 -> 320
~ __ZN16CoreAnalyticsHub35incrementEventNameSerializeTooLargeEP8OSString : 316 -> 320
~ __ZN16CoreAnalyticsHub34incrementEventNameSerializeFailureEP8OSString : 316 -> 320
~ __ZN16CoreAnalyticsHub20getIndexForEventNameEP8OSString : 344 -> 348
~ sub_fffffe0009adce2c -> sub_fffffe0009b6ca30 : 144 -> 148
~ __ZN16CoreAnalyticsHub21testDemoNormalMessageEv : 636 -> 640
~ __ZN16CoreAnalyticsHub24testDemoOversizedMessageEv : 556 -> 560
~ _analytics_send_event_lazy : 112 -> 116
~ sub_fffffe0009add3dc -> sub_fffffe0009b6cff0 : 80 -> 84
~ sub_fffffe0009add50c -> sub_fffffe0009b6d124 : 68 -> 72
~ sub_fffffe0009add560 -> sub_fffffe0009b6d17c : 104 -> 108
~ sub_fffffe0009add5c8 -> sub_fffffe0009b6d1e8 : 220 -> 224
~ sub_fffffe0009add6a4 -> sub_fffffe0009b6d2c8 : 120 -> 124
~ __ZN22CoreAnalyticsMessenger13startMessagesEv : 212 -> 216
~ __ZN22CoreAnalyticsMessenger6attachEP9IOService : 208 -> 212
~ __ZN22CoreAnalyticsMessenger6detachEP9IOService : 140 -> 144
~ sub_fffffe0009add94c -> sub_fffffe0009b6d580 : 144 -> 148
~ sub_fffffe0009add9e4 -> sub_fffffe0009b6d61c : 80 -> 84
~ sub_fffffe0009adda54 -> sub_fffffe0009b6d690 : 68 -> 72
~ sub_fffffe0009addaa8 -> sub_fffffe0009b6d6e8 : 104 -> 108
~ __ZN17CoreAnalyticsPipe10withParamsENS_6ParamsE : 236 -> 240
~ __ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE : 376 -> 380
~ sub_fffffe0009addd74 -> sub_fffffe0009b6d9c0 : 400 -> 404
~ __ZN17CoreAnalyticsPipe22enqueueEventAndPayloadEP8OSStringP8OSObject : 300 -> 304
~ __os_log_internal : 648 -> 652
~ __GLOBAL__sub_I_CoreAnalyticsPipe.cpp : 80 -> 84
~ sub_fffffe0009ade384 -> sub_fffffe0009b6dfe0 : 68 -> 72
~ sub_fffffe0009ade3d8 -> sub_fffffe0009b6e038 : 104 -> 108
~ __ZN27CoreAnalyticsTestUserClient4freeEv : 124 -> 128
~ __ZN27CoreAnalyticsTestUserClient5startEP9IOService : 340 -> 344
~ __ZN27CoreAnalyticsTestUserClient4stopEP9IOService : 232 -> 236
~ __ZN27CoreAnalyticsTestUserClient12initWithTaskEP4taskPvjP12OSDictionary : 156 -> 160
~ __ZN27CoreAnalyticsTestUserClient11clientCloseEv : 156 -> 160
~ __ZN27CoreAnalyticsTestUserClient10clientDiedEv : 160 -> 164
~ __ZN27CoreAnalyticsTestUserClient12didTerminateEP9IOServicejPb : 156 -> 160
~ __ZN27CoreAnalyticsTestUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 508 -> 512
~ __GLOBAL__sub_I_CoreAnalyticsTestUserClient.cpp : 80 -> 84
~ sub_fffffe0009adebe0 -> sub_fffffe0009b6e868 : 68 -> 72
~ sub_fffffe0009adec34 -> sub_fffffe0009b6e8c0 : 104 -> 108
~ sub_fffffe0009adecb0 -> sub_fffffe0009b6e940 : 88 -> 92
~ __ZN23CoreAnalyticsUserClient20goto_configureFilterEPS_PvP25IOExternalMethodArguments : 112 -> 116
~ __ZN23CoreAnalyticsUserClient4freeEv : 152 -> 156
~ __ZN23CoreAnalyticsUserClient5startEP9IOService : 344 -> 348
~ __ZN23CoreAnalyticsUserClient4stopEP9IOService : 332 -> 336
~ __ZN23CoreAnalyticsUserClient12initWithTaskEP4taskPvjP12OSDictionary : 244 -> 248
~ __ZN23CoreAnalyticsUserClient16checkEntitlementEP4task : 324 -> 328
~ __ZN23CoreAnalyticsUserClient11clientCloseEv : 200 -> 204
~ __ZN23CoreAnalyticsUserClient10clientDiedEv : 132 -> 136
~ __ZN23CoreAnalyticsUserClient12didTerminateEP9IOServicejPb : 156 -> 160
~ __ZN23CoreAnalyticsUserClient24registerNotificationPortEP8ipc_portjy : 192 -> 196
~ __ZN23CoreAnalyticsUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor : 392 -> 396
~ __ZN23CoreAnalyticsUserClient14sendDataToUserEPhm : 320 -> 324
~ __GLOBAL__sub_I_CoreAnalyticsUserClient.cpp : 80 -> 84
~ __ZN28CoreAnalyticsEventRatePolicy16initWithWorkloopEP10IOWorkLoop.cold.1 : 84 -> 88
~ __ZN28CoreAnalyticsEventRatePolicy16initWithWorkloopEP10IOWorkLoop.cold.2 : 84 -> 88
~ __ZN28CoreAnalyticsEventRatePolicy16initWithWorkloopEP10IOWorkLoop.cold.3 : 84 -> 88
~ __ZN28CoreAnalyticsEventRatePolicy16initWithWorkloopEP10IOWorkLoop.cold.4 : 84 -> 88
~ __ZN28CoreAnalyticsEventRatePolicy16initWithWorkloopEP10IOWorkLoop.cold.5 : 176 -> 180
~ sub_fffffe0009adfbd4 -> sub_fffffe0009b6f8b0 : 136 -> 140
~ __ZN28CoreAnalyticsEventRatePolicy22incrementCountForEventEP8OSString.cold.1 : 224 -> 228
~ sub_fffffe0009adfd3c -> sub_fffffe0009b6fa20 : 152 -> 156
~ __ZN28CoreAnalyticsEventRatePolicy24sendBudgetExceededReportEv.cold.1 : 64 -> 68
~ __ZN28CoreAnalyticsEventRatePolicy24sendBudgetExceededReportEv.cold.2 : 88 -> 92
~ __ZN28CoreAnalyticsEventRatePolicy24sendBudgetExceededReportEv.cold.3 : 88 -> 92
~ __ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.1 : 52 -> 56
~ __ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.2 : 52 -> 56
~ __ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.3 : 52 -> 56
~ __ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.4 : 88 -> 92
~ __ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.5 : 52 -> 56
~ __ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.6 : 52 -> 56
~ __ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.7 : 52 -> 56
~ __ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.8 : 52 -> 56
~ sub_fffffe0009ae0088 -> sub_fffffe0009b6fd9c : 152 -> 156
~ __ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.10 : 88 -> 92
~ __ZN16CoreAnalyticsHub22analyticsSendEventLazyEP8OSStringP8OSObject : 196 -> 200
~ sub_fffffe0009ae023c -> sub_fffffe0009b6ff5c : 124 -> 128
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.1 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.2 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.3 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.4 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.5 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.6 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.7 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.8 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.9 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.10 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.11 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.12 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.13 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.14 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.15 : 80 -> 84
~ __ZN16CoreAnalyticsHub5startEP9IOService.cold.16 : 80 -> 84
~ __ZN16CoreAnalyticsHub21sendUpEventAndPayloadEP8OSStringP8OSObject.cold.1 : 60 -> 64
~ __ZN16CoreAnalyticsHub21sendUpEventAndPayloadEP8OSStringP8OSObject.cold.2 : 88 -> 92
~ __ZN16CoreAnalyticsHub21sendUpEventAndPayloadEP8OSStringP8OSObject.cold.3 : 100 -> 104
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.1 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.2 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.3 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.4 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.5 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.6 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.7 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.8 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.9 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.10 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.11 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.12 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.13 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.14 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.15 : 52 -> 56
~ __ZN16CoreAnalyticsHub15createReportersEv.cold.16 : 52 -> 56
~ _IOCoreAnalyticsSendEvent.cold.1 : 96 -> 100
~ _IOCoreAnalyticsSendEvent.cold.2 : 84 -> 88
~ _IOCoreAnalyticsSendEvent.cold.3 : 84 -> 88
~ __ZN16CoreAnalyticsHub20__newUserClientGatedEP4taskPvjP12OSDictionaryPP12IOUserClient.cold.1 : 96 -> 100
~ __ZN16CoreAnalyticsHub18setupNewUserClientEP4taskPvjP12OSDictionaryP12IOUserClient.cold.1 : 60 -> 64
~ __ZN16CoreAnalyticsHub18setupNewUserClientEP4taskPvjP12OSDictionaryP12IOUserClient.cold.2 : 60 -> 64
~ __ZN16CoreAnalyticsHub18setupNewUserClientEP4taskPvjP12OSDictionaryP12IOUserClient.cold.3 : 60 -> 64
~ __ZN16CoreAnalyticsHub18setupNewUserClientEP4taskPvjP12OSDictionaryP12IOUserClient.cold.4 : 60 -> 64
~ __ZN16CoreAnalyticsHub16serializePayloadEP8OSObjectP11OSSerializePm.cold.1 : 60 -> 64
~ __ZN16CoreAnalyticsHub16serializePayloadEP8OSObjectP11OSSerializePm.cold.2 : 60 -> 64
~ __ZN16CoreAnalyticsHub20getIndexForEventNameEP8OSString.cold.1 : 96 -> 100
~ __ZN16CoreAnalyticsHub20getIndexForEventNameEP8OSString.cold.2 : 60 -> 64
~ sub_fffffe0009ae0f5c -> sub_fffffe0009b70d3c : 84 -> 88
~ sub_fffffe0009ae0fb0 -> sub_fffffe0009b70d94 : 92 -> 96
~ __ZN16CoreAnalyticsHub21testDemoNormalMessageEv.cold.3 : 84 -> 88
~ __ZN16CoreAnalyticsHub24testDemoOversizedMessageEv.cold.3 : 92 -> 96
~ sub_fffffe0009ae10bc -> sub_fffffe0009b70eac : 92 -> 96
~ __ZN16CoreAnalyticsHub24testDemoOversizedMessageEv.cold.1 : 84 -> 88
~ sub_fffffe0009ae116c -> sub_fffffe0009b70f64 : 84 -> 88
~ sub_fffffe0009ae11c0 -> sub_fffffe0009b70fbc : 100 -> 104
~ sub_fffffe0009ae1224 -> sub_fffffe0009b71024 : 100 -> 104
~ _analytics_send_event_lazy.cold.1 : 128 -> 132
~ __ZN22CoreAnalyticsMessenger6attachEP9IOService.cold.1 : 76 -> 80
~ __ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.1 : 88 -> 92
~ __ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.2 : 148 -> 152
~ __ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.3 : 148 -> 152
~ __ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.4 : 148 -> 152
~ __ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.5 : 148 -> 152
~ __ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.6 : 148 -> 152
~ __ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.7 : 148 -> 152
~ __ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.8 : 148 -> 152
~ __ZN17CoreAnalyticsPipe22enqueueEventAndPayloadEP8OSStringP8OSObject.cold.1 : 164 -> 168
~ __ZN17CoreAnalyticsPipe22enqueueEventAndPayloadEP8OSStringP8OSObject.cold.2 : 128 -> 132
~ __ZN27CoreAnalyticsTestUserClient5startEP9IOService.cold.1 : 84 -> 88
~ __ZN27CoreAnalyticsTestUserClient5startEP9IOService.cold.2 : 84 -> 88
~ __ZN27CoreAnalyticsTestUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1 : 84 -> 88
~ __ZN27CoreAnalyticsTestUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv.cold.1 : 84 -> 88
~ __ZN27CoreAnalyticsTestUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv.cold.2 : 84 -> 88
~ __ZN23CoreAnalyticsUserClient5startEP9IOService.cold.1 : 60 -> 64
~ __ZN23CoreAnalyticsUserClient5startEP9IOService.cold.2 : 60 -> 64
~ __ZN23CoreAnalyticsUserClient5startEP9IOService.cold.3 : 60 -> 64
~ __ZN23CoreAnalyticsUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1 : 60 -> 64
~ sub_fffffe0009ae1b70 -> sub_fffffe0009b719c8 : 60 -> 64
~ __ZN23CoreAnalyticsUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.3 : 60 -> 64
~ __ZN23CoreAnalyticsUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv.cold.1 : 80 -> 84
```
