## com.apple.driver.AudioDMAController-T8150

> `com.apple.driver.AudioDMAController-T8150`

```diff

-540.26.0.0.0
+600.43.0.0.0
   __TEXT.__const: 0x200
-  __TEXT.__cstring: 0x7623
-  __TEXT.__os_log: 0x587
-  __TEXT_EXEC.__text: 0x2ab10
+  __TEXT.__cstring: 0x759b
+  __TEXT.__os_log: 0x5f3
+  __TEXT_EXEC.__text: 0x2a9d0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x150
-  __DATA_CONST.__auth_got: 0x380
-  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x1740
+  __DATA_CONST.__const: 0x1760
   __DATA_CONST.__kalloc_type: 0x400
-  UUID: 07EC33C5-FB2C-3F0C-9106-3A5A4CD0C96D
-  Functions: 466
+  __DATA_CONST.__auth_got: 0x380
+  __DATA_CONST.__got: 0xe8
+  UUID: 86FF8040-A9C3-3658-90BC-A03A2C160541
+  Functions: 467
   Symbols:   0
-  CStrings:  756
+  CStrings:  754
 
CStrings:
+ "%s is not ready to suspend yet with state = %s."
+ "%s: Cannot suspend at this time."
+ "%s: inCb (%p) returned %s."
+ "(_dmaChannelCountTx <= ADMAGenDefines::kMaximumChannelCount && _dmaChannelCountRx <= ADMAGenDefines::kMaximumChannelCount)"
+ "02:46:15"
+ "Jun  5 2026"
+ "i16@?0^{AudioDMAChannel=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{IOCommandGate}^{IOCommandPool}{queue_entry=^{queue_entry}^{queue_entry}}{?=B^{TransferRequest}}^{IOCommandPool}II^{OSDictionary}{queue_entry=^{queue_entry}^{queue_entry}}^{ADMATransferDescriptorBuilder}^{AudioDMAController}^{IOWorkLoop}II^{AudioDMAChannelStateMachine}^{_IORecursiveLock}^{ADMAChannelInterface}[256c]B(?=^{_adma_base_ns_txch_blk_v3}^{_adma_base_ns_rxch_blk_v3})^(_adma_base_ns_tdcs_tx_tdfifo_ch0_v1)^(_adma_base_ns_tdcs_tx_csfifo_ch0_v1)^(_adma_base_ns_tdcs_tx_pctfifo_ch0_v1)^{IODMAEventSource}^{AudioDMAChannelConfiguration}QI^{IOInterruptQueueEventSource}IBB^{OSSymbol}^{DMAChannelECProxyInterface}BBBBBQQ^II^{ExceptionJournalEntry}III[8I]Q^{IOHistogramReporter}^{IOHistogramReporter}^{IOHistogramReporter}^{IOHistogramReporter}^{IOSimpleReporter}[8Q]^{OSSet}^{IOReportLegend}QQBB}8"
- "%s::%s Cannot suspend controller at this time."
- "%s::%s Not ready to suspend %s yet."
- "%s::%s inCb (%p) returned %s."
- "(_dmaChannelCountTx <= ADMA4p0::kMaximumChannelCount && _dmaChannelCountRx <= ADMA4p0::kMaximumChannelCount)"
- "20:41:05"
- "Apr 23 2026"
- "empty == false"
- "getNextInterruptRefCon"
- "i16@?0^{AudioDMAChannel=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{IOCommandGate}^{IOCommandPool}{queue_entry=^{queue_entry}^{queue_entry}}{?=B^{TransferRequest}}^{IOCommandPool}II^{OSDictionary}{queue_entry=^{queue_entry}^{queue_entry}}^{ADMATransferDescriptorBuilder}^{AudioDMAController}^{IOWorkLoop}II^{AudioDMAChannelStateMachine}^{_IORecursiveLock}^{ADMAChannelInterface}[256c]B(?=^{_adma_base_ns_txch_blk_v3}^{_adma_base_ns_rxch_blk_v3})^(_adma_base_ns_tdcs_tx_tdfifo_ch0_v1)^(_adma_base_ns_tdcs_tx_csfifo_ch0_v1)^(_adma_base_ns_tdcs_tx_pctfifo_ch0_v1)^{IODMAEventSource}^{AudioDMAChannelConfiguration}QI^{IOInterruptQueueEventSource}IBB^{OSSymbol}^{DMAChannelECProxyInterface}BBBBBQQ^II^{ExceptionJournalEntry}III[8I]Q^{IOHistogramReporter}^{IOHistogramReporter}^{IOHistogramReporter}^{IOHistogramReporter}^{IOSimpleReporter}[8Q]^{OSSet}^{IOReportLegend}QQB}8"

```
