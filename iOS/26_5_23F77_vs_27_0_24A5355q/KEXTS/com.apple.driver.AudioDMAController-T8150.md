## com.apple.driver.AudioDMAController-T8150

> `com.apple.driver.AudioDMAController-T8150`

```diff

-540.26.0.0.0
+600.43.0.0.0
   __TEXT.__const: 0x200 sha256:364be9d663a8dd2f882d48dc27278dca2c530addb1d14ca53148a830ae0159c3
-  __TEXT.__cstring: 0x7623 sha256:83c4159af47490308d2893b04298e805a95d4ec67d2b63d286c3f4ac5e0aa152
-  __TEXT.__os_log: 0x587 sha256:777a6dccaf1ccbb6ee43d696a12b6938eae1b53bf635dae8692f7f795042d001
-  __TEXT_EXEC.__text: 0x2ab10 sha256:4e706d25227bc457b7d2a5548ffa864401316de886f0a3f5a3b0676b29b57fa5
+  __TEXT.__cstring: 0x759b sha256:13dca7b5278c27a016fa687b8f58eb34342c63ddfe07caad8c359e4b8bc62700
+  __TEXT.__os_log: 0x5f3 sha256:b64ac4c9dfeeaf1181f8c8fd15c5dcdb7c60ea4eec25c0cdbc00a16e304ee641
+  __TEXT_EXEC.__text: 0x2a9d0 sha256:71ba41d2aa33228cf13981aa5d35bc1a541def44bb102f6268600c0d0f84352b
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x248 sha256:72e402fca9f3020eb7d5ca075a32249da5d3446673341159861fe54146fc434f
+  __DATA.__data: 0x248 sha256:07241c7a42e1afdc869c9a1d2547e587adcc7168d395cbb941ef462fe15645b5
   __DATA.__common: 0x150 sha256:52a3e0804d93dc525ec3c67ef8ac5b01756ecf0513e36f3c19435e4c82cb5d29
-  __DATA_CONST.__auth_got: 0x380 sha256:a73c47a6fc52b66ae98a4ace6b27d6561a0b1ca3fe5b752bde313834b314fac7
-  __DATA_CONST.__got: 0xe8 sha256:a528e1f1b9f6c50649c1eedde674ff55b22ecf72e3fb50871ea9ded0168f97e4
-  __DATA_CONST.__mod_init_func: 0x28 sha256:22a63afe17338550ecd328b99b43d5abcd433e18226000ac52ca30da5051abfa
-  __DATA_CONST.__mod_term_func: 0x20 sha256:f27184bce9d3c77ac6f685d70bf27207692a78e9f97b65ae17957956492c1b24
-  __DATA_CONST.__const: 0x1740 sha256:e833ea94789729b302e8c066950e7f88b2ef3bc0235ed24629b41b9e9e5c1ab7
-  __DATA_CONST.__kalloc_type: 0x400 sha256:d8bf74f372a70baa946d2b7d83e37e364be7c19e2c612330ec4345151e3a2c14
-  UUID: 07EC33C5-FB2C-3F0C-9106-3A5A4CD0C96D
-  Functions: 466
+  __DATA_CONST.__mod_init_func: 0x28 sha256:ad7f57bf687c16ed81919956bb1c205e2c21a3977d0dd0181edfe28e4b18ae98
+  __DATA_CONST.__mod_term_func: 0x20 sha256:a2738db257fdc58ff7b5280ae3c8abc8db400c504f1abfe0855f886da6811c76
+  __DATA_CONST.__const: 0x1760 sha256:f073a00d484443e93830773d480045bf7c35b6948c9716915c277c5e238a7c1b
+  __DATA_CONST.__kalloc_type: 0x400 sha256:e59f6b4d4e4df78cd9f02557542c3c4235830c0f0e525c3661f725581f3fe066
+  __DATA_CONST.__auth_got: 0x380 sha256:e06340d405cbe924f2dc760db5f6e941c96c30a8021e80146adf5a971ddd47f4
+  __DATA_CONST.__got: 0xe8 sha256:aad13050a02caaa8056a2794e0e13b7a51eaeb0b3faae73bb72989fe5f2f0c78
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
