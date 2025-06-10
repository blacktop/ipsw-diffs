## com.apple.driver.AudioDMAController-T8140

> `com.apple.driver.AudioDMAController-T8140`

```diff

-450.4.0.0.0
+500.80.0.0.0
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x7b20
-  __TEXT.__os_log: 0x417
-  __TEXT_EXEC.__text: 0x2c4b8
+  __TEXT.__cstring: 0x7d44
+  __TEXT.__os_log: 0x57b
+  __TEXT_EXEC.__text: 0x2e6d0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x150
-  __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x16b0
+  __DATA_CONST.__const: 0x1700
   __DATA_CONST.__kalloc_type: 0x400
-  UUID: D129EB2B-6DD5-3611-A4A0-6947CC40C10C
-  Functions: 411
+  UUID: 68A2B2F6-C678-381B-B39E-DCA85B17FD4F
+  Functions: 405
   Symbols:   0
-  CStrings:  799
+  CStrings:  817
 
CStrings:
+ "%s: %s::%s::%d:  %s: %s is set to %s.\n"
+ "%s::%s Adding provider %s failed with %s."
+ "%s::%s Could not construction %s."
+ "%s::%s _addExternalPowerProvider failed."
+ "%s::%s `theService` is a nullptr."
+ "%s@%s"
+ "121111121222121211121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111222112211122222222222222222222222222222222222222222111111111111111111111111111111111111212111222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "20:38:16"
+ "B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16"
+ "Could not disable critical LLT due to %s."
+ "Could not enable critical LLT due to %s."
+ "Critical LLT function disable request failed with %s."
+ "Critical LLT function enable request failed with %s."
+ "Disengaged"
+ "Engaged"
+ "EscalationDetectable"
+ "May 30 2025"
+ "Polling for ~%llu milliseconds."
+ "Service named %s is an ADMAC CED/SSW implementation."
+ "Service named %s is not an ADMAC CED/SSW implementation."
+ "Skipping child named %s"
+ "defang_reset_TO_check"
+ "function-vote_crit_llt_mode"
+ "i16@?0^{AudioDMAChannel=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{IOCommandGate}^{IOCommandPool}{queue_entry=^{queue_entry}^{queue_entry}}{?=B^{TransferRequest}}^{IOCommandPool}II^{OSDictionary}{queue_entry=^{queue_entry}^{queue_entry}}^{ADMATransferDescriptorBuilder}^{AudioDMAController}^{IOWorkLoop}II^{AudioDMAChannelStateMachine}^{_IORecursiveLock}^{ADMAChannelInterface}[256c]B(?=^{_adma_base_ns_txch_blk_v1}^{_adma_base_ns_rxch_blk_v1})^(_adma_base_ns_tdcs_tx_tdfifo_ch0_v1)^(_adma_base_ns_tdcs_tx_csfifo_ch0_v1)^(_adma_base_ns_tdcs_tx_pctfifo_ch0_v1)^{IODMAEventSource}^{AudioDMAChannelConfiguration}QI^{IOInterruptQueueEventSource}IBB^{OSSymbol}^{DMAChannelECProxyInterface}BBBBBQQ^II^{ExceptionJournalEntry}IIIQ^{IOHistogramReporter}^{IOHistogramReporter}^{IOHistogramReporter}^{IOHistogramReporter}^{IOSimpleReporter}[8Q]^{OSSet}^{IOReportLegend}QQB}8"
+ "processChannelOperation( AudioDMAChannelStateMachine::ADMACOPER_Finish) == kIOReturnSuccess"
+ "processChannelOperation(AudioDMAChannelStateMachine::ADMACOPER_Finish) == kIOReturnSuccess"
+ "static_cast<bool>(_criticalLLTFunction)"
+ "static_cast<bool>(theService)"
- "%s: %s::%s::%d: %s: _cedSSWHandle = %p, named %s.\n"
- "%s: %s::%s::%d: Skipping Child Name %s\n\n"
- "%s::%s CED/SSW service was not found."
- "1211111212221212111212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221112221122111222222222222222222222222222222222222222221111111111111111111111111111111111112121222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "20:45:19"
- "Apr 22 2025"
- "Off"
- "On"
- "i16@?0^{AudioDMAChannel=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{IOCommandGate}^{IOCommandPool}{queue_entry=^{queue_entry}^{queue_entry}}{?=B^{TransferRequest}}^{IOCommandPool}II^{OSDictionary}{queue_entry=^{queue_entry}^{queue_entry}}^{ADMATransferDescriptorBuilder}^{AudioDMAController}^{IOWorkLoop}II^{AudioDMAChannelStateMachine}^{_IORecursiveLock}^{ADMAChannelInterface}[256c]B(?=^{_adma_base_ns_txch_blk_v1}^{_adma_base_ns_rxch_blk_v1})^(_adma_base_ns_tdcs_tx_tdfifo_ch0_v1)^(_adma_base_ns_tdcs_tx_csfifo_ch0_v1)^(_adma_base_ns_tdcs_tx_pctfifo_ch0_v1)^{IODMAEventSource}^{AudioDMAChannelConfiguration}QI^{IOInterruptQueueEventSource}IBB^{OSSymbol}^{DMAChannelECProxyInterface}BBBBQQ^II^{ExceptionJournalEntry}IIIQ^{IOHistogramReporter}^{IOHistogramReporter}^{IOHistogramReporter}^{IOHistogramReporter}^{IOSimpleReporter}[8Q]^{OSSet}^{IOReportLegend}QQB}8"
- "static_cast<bool>(_cedSSWHandle)"

```
