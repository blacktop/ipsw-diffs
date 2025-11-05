## com.apple.iokit.CoreAnalyticsFamily

> `com.apple.iokit.CoreAnalyticsFamily`

```diff

-419.60.7.0.0
-  __TEXT.__cstring: 0x1cd3
-  __TEXT.__os_log: 0x1639
-  __TEXT_EXEC.__text: 0x79ec
+430.100.6.0.0
+  __TEXT.__cstring: 0x1eae
+  __TEXT.__os_log: 0x1941
+  __TEXT_EXEC.__text: 0x9544
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x108
-  __DATA_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__auth_got: 0x1f8
   __DATA_CONST.__got: 0x78
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x30
   __DATA_CONST.__mod_term_func: 0x30
   __DATA_CONST.__const: 0x2e38
   __DATA_CONST.__kalloc_type: 0x2c0
-  UUID: 8CEB4D09-7816-31BA-9AFF-88E176098B89
-  Functions: 136
-  Symbols:   741
-  CStrings:  305
+  UUID: 0926C7F9-2271-3F18-901E-FE138A84E306
+  Functions: 251
+  Symbols:   875
+  CStrings:  327
 
Symbols:
+ IOCoreAnalyticsSendEvent.cold.1
+ IOCoreAnalyticsSendEvent.cold.2
+ IOCoreAnalyticsSendEvent.cold.3
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.1
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.10
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.11
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.12
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.13
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.14
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.15
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.16
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.2
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.3
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.4
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.5
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.6
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.7
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.8
+ _ZN16CoreAnalyticsHub15createReportersEv.cold.9
+ _ZN16CoreAnalyticsHub16serializePayloadEP8OSObjectP11OSSerializePm.cold.1
+ _ZN16CoreAnalyticsHub16serializePayloadEP8OSObjectP11OSSerializePm.cold.2
+ _ZN16CoreAnalyticsHub18setupNewUserClientEP4taskPvjP12OSDictionaryP12IOUserClient.cold.1
+ _ZN16CoreAnalyticsHub18setupNewUserClientEP4taskPvjP12OSDictionaryP12IOUserClient.cold.2
+ _ZN16CoreAnalyticsHub18setupNewUserClientEP4taskPvjP12OSDictionaryP12IOUserClient.cold.3
+ _ZN16CoreAnalyticsHub18setupNewUserClientEP4taskPvjP12OSDictionaryP12IOUserClient.cold.4
+ _ZN16CoreAnalyticsHub20__newUserClientGatedEP4taskPvjP12OSDictionaryPP12IOUserClient.cold.1
+ _ZN16CoreAnalyticsHub20getIndexForEventNameEP8OSString.cold.1
+ _ZN16CoreAnalyticsHub20getIndexForEventNameEP8OSString.cold.2
+ _ZN16CoreAnalyticsHub21sendUpEventAndPayloadEP8OSStringP8OSObject.cold.1
+ _ZN16CoreAnalyticsHub21sendUpEventAndPayloadEP8OSStringP8OSObject.cold.2
+ _ZN16CoreAnalyticsHub21sendUpEventAndPayloadEP8OSStringP8OSObject.cold.3
+ _ZN16CoreAnalyticsHub21testDemoNormalMessageEv.cold.1
+ _ZN16CoreAnalyticsHub21testDemoNormalMessageEv.cold.2
+ _ZN16CoreAnalyticsHub21testDemoNormalMessageEv.cold.3
+ _ZN16CoreAnalyticsHub21testDemoNormalMessageEv.cold.4
+ _ZN16CoreAnalyticsHub21testDemoNormalMessageEv.cold.5
+ _ZN16CoreAnalyticsHub24testDemoOversizedMessageEv.cold.1
+ _ZN16CoreAnalyticsHub24testDemoOversizedMessageEv.cold.2
+ _ZN16CoreAnalyticsHub24testDemoOversizedMessageEv.cold.3
+ _ZN16CoreAnalyticsHub24testDemoOversizedMessageEv.cold.4
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.1
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.10
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.11
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.12
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.13
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.14
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.15
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.16
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.2
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.3
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.4
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.5
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.6
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.7
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.8
+ _ZN16CoreAnalyticsHub5startEP9IOService.cold.9
+ _ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.1
+ _ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.2
+ _ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.3
+ _ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.4
+ _ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.5
+ _ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.6
+ _ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.7
+ _ZN17CoreAnalyticsPipe14initWithParamsENS_6ParamsE.cold.8
+ _ZN17CoreAnalyticsPipe22enqueueEventAndPayloadEP8OSStringP8OSObject.cold.1
+ _ZN17CoreAnalyticsPipe22enqueueEventAndPayloadEP8OSStringP8OSObject.cold.2
+ _ZN22CoreAnalyticsMessenger6attachEP9IOService.cold.1
+ _ZN23CoreAnalyticsUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN23CoreAnalyticsUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.2
+ _ZN23CoreAnalyticsUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.3
+ _ZN23CoreAnalyticsUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv.cold.1
+ _ZN23CoreAnalyticsUserClient5startEP9IOService.cold.1
+ _ZN23CoreAnalyticsUserClient5startEP9IOService.cold.2
+ _ZN23CoreAnalyticsUserClient5startEP9IOService.cold.3
+ _ZN27CoreAnalyticsTestUserClient12initWithTaskEP4taskPvjP12OSDictionary.cold.1
+ _ZN27CoreAnalyticsTestUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv.cold.1
+ _ZN27CoreAnalyticsTestUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv.cold.2
+ _ZN27CoreAnalyticsTestUserClient5startEP9IOService.cold.1
+ _ZN27CoreAnalyticsTestUserClient5startEP9IOService.cold.2
+ _ZN28CoreAnalyticsEventRatePolicy16initWithWorkloopEP10IOWorkLoop.cold.1
+ _ZN28CoreAnalyticsEventRatePolicy16initWithWorkloopEP10IOWorkLoop.cold.2
+ _ZN28CoreAnalyticsEventRatePolicy16initWithWorkloopEP10IOWorkLoop.cold.3
+ _ZN28CoreAnalyticsEventRatePolicy16initWithWorkloopEP10IOWorkLoop.cold.4
+ _ZN28CoreAnalyticsEventRatePolicy16initWithWorkloopEP10IOWorkLoop.cold.5
+ _ZN28CoreAnalyticsEventRatePolicy21zeroOutPerEventCountsEv.cold.1
+ _ZN28CoreAnalyticsEventRatePolicy22incrementCountForEventEP8OSString.cold.1
+ _ZN28CoreAnalyticsEventRatePolicy22incrementCountForEventEP8OSString.cold.2
+ _ZN28CoreAnalyticsEventRatePolicy24sendBudgetExceededReportEv.cold.1
+ _ZN28CoreAnalyticsEventRatePolicy24sendBudgetExceededReportEv.cold.2
+ _ZN28CoreAnalyticsEventRatePolicy24sendBudgetExceededReportEv.cold.3
+ _ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.1
+ _ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.10
+ _ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.2
+ _ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.3
+ _ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.4
+ _ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.5
+ _ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.6
+ _ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.7
+ _ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.8
+ _ZNK28CoreAnalyticsEventRatePolicy17createBudgetDictsEP7OSArray.cold.9
+ __ZN16CoreAnalyticsHub21testDemoNormalMessageEv
+ __ZN16CoreAnalyticsHub24testDemoOversizedMessageEv
+ __ZN16CoreAnalyticsHub34incrementEventNameSerializeFailureEP8OSString
+ __ZN16CoreAnalyticsHub35incrementEventNameSerializeTooLargeEP8OSString
+ __ZN16CoreAnalyticsHub37incrementEventNameSharedDataQueueFullEP8OSString
+ __ZZN16CoreAnalyticsHub15createReportersEvE11_os_log_fmt_9
+ __ZZN16CoreAnalyticsHub15createReportersEvE11_os_log_fmt__10_
+ __ZZN16CoreAnalyticsHub15createReportersEvE11_os_log_fmt__11_
+ __ZZN16CoreAnalyticsHub15createReportersEvE11_os_log_fmt__12_
+ __ZZN16CoreAnalyticsHub15createReportersEvE11_os_log_fmt__13_
+ __ZZN16CoreAnalyticsHub15createReportersEvE11_os_log_fmt__14_
+ __ZZN16CoreAnalyticsHub21sendUpEventAndPayloadEP8OSStringP8OSObjectE11_os_log_fmt_3
+ __ZZN16CoreAnalyticsHub21sendUpEventAndPayloadEP8OSStringP8OSObjectE20kalloc_type_view_479
+ __ZZN16CoreAnalyticsHub21sendUpEventAndPayloadEP8OSStringP8OSObjectE20kalloc_type_view_515
+ __ZZN16CoreAnalyticsHub21testDemoNormalMessageEvE11_os_log_fmt
+ __ZZN16CoreAnalyticsHub21testDemoNormalMessageEvE11_os_log_fmt_0
+ __ZZN16CoreAnalyticsHub21testDemoNormalMessageEvE11_os_log_fmt_1
+ __ZZN16CoreAnalyticsHub21testDemoNormalMessageEvE11_os_log_fmt_2
+ __ZZN16CoreAnalyticsHub21testDemoNormalMessageEvE11_os_log_fmt_4
+ __ZZN16CoreAnalyticsHub24testDemoOversizedMessageEvE11_os_log_fmt
+ __ZZN16CoreAnalyticsHub24testDemoOversizedMessageEvE11_os_log_fmt_0
+ __ZZN16CoreAnalyticsHub24testDemoOversizedMessageEvE11_os_log_fmt_1
+ __ZZN16CoreAnalyticsHub24testDemoOversizedMessageEvE11_os_log_fmt_2
+ __ZZN16CoreAnalyticsHub34incrementEventNameSerializeFailureEP8OSStringE11_os_log_fmt
+ __ZZN16CoreAnalyticsHub35incrementEventNameSerializeTooLargeEP8OSStringE11_os_log_fmt
+ __ZZN16CoreAnalyticsHub37incrementEventNameSharedDataQueueFullEP8OSStringE11_os_log_fmt
+ ___chkstk_darwin
+ ___chkstk_darwin_probe
+ _bzero
+ analytics_send_event_lazy.cold.1
- __ZZN16CoreAnalyticsHub21handleDemoTimerExpiryEP18IOTimerEventSourceE11_os_log_fmt_1
- __ZZN16CoreAnalyticsHub21handleDemoTimerExpiryEP18IOTimerEventSourceE11_os_log_fmt_2
- __ZZN16CoreAnalyticsHub21handleDemoTimerExpiryEP18IOTimerEventSourceE11_os_log_fmt_4
- __ZZN16CoreAnalyticsHub21sendUpEventAndPayloadEP8OSStringP8OSObjectE20kalloc_type_view_470
- __ZZN16CoreAnalyticsHub21sendUpEventAndPayloadEP8OSStringP8OSObjectE20kalloc_type_view_504
CStrings:
+ "%s::%d:Failed to add _eventNameSerializeFailure for %s\n"
+ "%s::%d:Failed to add _eventNameSerializeTooLarge for %s\n"
+ "%s::%d:Failed to add _eventNameSharedDataQueueFull for %s\n"
+ "%s::%d:Failed to create _eventNameSerializeFailure\n"
+ "%s::%d:Failed to create _eventNameSerializeTooLarge\n"
+ "%s::%d:Failed to create _eventNameSharedDataQueueFull\n"
+ "%s::%d:Failed to store _eventNameSerializeFailure\n"
+ "%s::%d:Failed to store _eventNameSerializeTooLarge\n"
+ "%s::%d:Failed to store _eventNameSharedDataQueueFull\n"
+ "%s::%d:Serialized data too large, dropping event with eventName %s\n"
+ "%s::%d:Testing Normal Event Messages\n"
+ "%s::%d:Testing Oversized Event Messages\n"
+ "12111112122212121111111111111111212121112"
+ "EventName SerializeFailure"
+ "EventName SerializeTooLarge"
+ "EventName SharedDataQueueFull"
+ "Serialized Message Too Large"
+ "com.apple.coreanalytics.kernel.verifyOversized"
+ "void CoreAnalyticsHub::incrementEventNameSerializeFailure(OSString *)"
+ "void CoreAnalyticsHub::incrementEventNameSerializeTooLarge(OSString *)"
+ "void CoreAnalyticsHub::incrementEventNameSharedDataQueueFull(OSString *)"
+ "void CoreAnalyticsHub::testDemoNormalMessage()"
+ "void CoreAnalyticsHub::testDemoOversizedMessage()"
- "12111112122212121111111111111212121112"

```
