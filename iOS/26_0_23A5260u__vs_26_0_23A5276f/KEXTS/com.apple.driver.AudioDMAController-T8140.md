## com.apple.driver.AudioDMAController-T8140

> `com.apple.driver.AudioDMAController-T8140`

```diff

-500.80.0.0.0
-  __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x7d44
-  __TEXT.__os_log: 0x57b
-  __TEXT_EXEC.__text: 0x2e6d0
+500.85.0.0.0
+  __TEXT.__const: 0x210
+  __TEXT.__cstring: 0x73a1
+  __TEXT.__os_log: 0x553
+  __TEXT_EXEC.__text: 0x2ce98
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x248
   __DATA.__common: 0x150
-  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__auth_got: 0x378
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__mod_init_func: 0x28
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x1700
+  __DATA_CONST.__const: 0x1720
   __DATA_CONST.__kalloc_type: 0x400
-  UUID: 68A2B2F6-C678-381B-B39E-DCA85B17FD4F
-  Functions: 405
+  UUID: 1AB8139F-A752-34EE-9250-8F5266199CCF
+  Functions: 446
   Symbols:   0
-  CStrings:  817
+  CStrings:  746
 
CStrings:
+ "\"<%c%c%c%c %s> Data buffer %s - Maximum AXI latency: 0x%08x \" \"DATABUFFSTAT: 0x%08x AXI%s_Outstanding: 0x%08x.\" @%s:%d"
+ "01:00:42"
+ "121111121222121211111211211111121112222222222222222222222222222222221111112212112221212222222111112222222211222"
+ "Jun 17 2025"
+ "Rd"
+ "Wr"
+ "bool AudioDMAController::_filterInterruptAction(IOFilterInterruptEventSource *)"
+ "i16@?0^{AudioDMAChannel=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{IOCommandGate}^{IOCommandPool}{queue_entry=^{queue_entry}^{queue_entry}}{?=B^{TransferRequest}}^{IOCommandPool}II^{OSDictionary}{queue_entry=^{queue_entry}^{queue_entry}}^{ADMATransferDescriptorBuilder}^{AudioDMAController}^{IOWorkLoop}II^{AudioDMAChannelStateMachine}^{_IORecursiveLock}^{ADMAChannelInterface}[256c]B(?=^{_adma_base_ns_txch_blk_v1}^{_adma_base_ns_rxch_blk_v1})^(_adma_base_ns_tdcs_tx_tdfifo_ch0_v1)^(_adma_base_ns_tdcs_tx_csfifo_ch0_v1)^(_adma_base_ns_tdcs_tx_pctfifo_ch0_v1)^{IODMAEventSource}^{AudioDMAChannelConfiguration}QI^{IOInterruptQueueEventSource}IBB^{OSSymbol}^{DMAChannelECProxyInterface}BBBBBQQ^II^{ExceptionJournalEntry}III[8I]Q^{IOHistogramReporter}^{IOHistogramReporter}^{IOHistogramReporter}^{IOHistogramReporter}^{IOSimpleReporter}[8Q]^{OSSet}^{IOReportLegend}QQB}8"
+ "overrun"
+ "static_cast<bool>(_controllerIES)"
+ "underrun"
- "!_liveTransferRequest.isSet"
- "\"%llu %s:%s \" \"Data buffer overrun - Maximum AXI latency: 0x%08x.\" @%s:%d"
- "\"%llu %s:%s \" \"Data buffer underrun - Maximum AXI latency: 0x%08x.\" @%s:%d"
- "%s: Legacy DMA done for a %s  transfer."
- "(((&_pendingTransferCommands)) == (((&_pendingTransferCommands)->next))) == false"
- "(length + offset) <= (preparedOffset + preparedLength)"
- "/Library/Caches/com.apple.xbs/Sources/AudioDMAController/v4p0/Kext/Source/AudioDMAChannel.cpp"
- "12111112122212121111121121111112111222222222222222222222222222222222111111221211222121222111112222222211222"
- "20:38:16"
- "May 30 2025"
- "_activeTransferCommands != nullptr"
- "_activeTransferCommands->getCount() < 8"
- "_admaCSFIFOBlock != nullptr"
- "_admaPCTFIFOBlock != nullptr"
- "_admaTDFIFOBlock != nullptr"
- "_admaTxChannelCSRBlock != nullptr"
- "_aperturesSet"
- "_channelECProxyServiceName == nullptr"
- "_channelIES != nullptr"
- "_channelTimestampJitterHistReporter != nullptr"
- "_channelWorkLoop != nullptr"
- "_channelWorkLoop->addEventSource(_channelIES) == 0"
- "_channelWorkLoop->addEventSource(_suspendGate) == 0"
- "_configuration != nullptr"
- "_dmaCmplToProcTimingHistReporter != nullptr"
- "_dmaTransferCommandPool != nullptr"
- "_dmaTransferTimeHistReporter != nullptr"
- "_evolved"
- "_evolvedDMACommandPool != nullptr"
- "_exceptionCounterReporter != nullptr"
- "_exceptionJournal != nullptr"
- "_lastNHistoricalSecondDifferenceValues != nullptr"
- "_maxMemoryAccessLatencyACLKHistReporter != nullptr"
- "_suspendGate != nullptr"
- "_tdBuilder != nullptr"
- "_theMachine != nullptr"
- "_theMachine == nullptr"
- "_theMachine->canStartTransfer()"
- "_theMachine->getCurrentState() != AudioDMAChannelStateMachine::ADMACChannelState::ADMACSMS_CSSP"
- "_theMachine->isOperationAllowed( AudioDMAChannelStateMachine::ADMACChannelOperation::ADMACOPER_GetConfiguration)"
- "_validConfig()"
- "activeTransferIterator != nullptr"
- "admaCmd != nullptr"
- "admaCmd->init()"
- "admaTransferCommand != nullptr"
- "almostFullThreshold > lowThreshold"
- "apertureCount != 0"
- "apertureCount <= s_ApertureCount"
- "chApertures != nullptr"
- "chApertures[aperture] != 0"
- "commandAlias != nullptr"
- "commandToComplete != nullptr"
- "configurationAlias != nullptr"
- "currentFIFODepth != nullptr"
- "descriptorCount <= ADMA4p0::kTDFIFODepth"
- "dmaCommand != nullptr"
- "dmaesAlias != nullptr"
- "emptySlots >= descriptorCount"
- "finalFIFODepth != nullptr"
- "i16@?0^{AudioDMAChannel=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{IOCommandGate}^{IOCommandPool}{queue_entry=^{queue_entry}^{queue_entry}}{?=B^{TransferRequest}}^{IOCommandPool}II^{OSDictionary}{queue_entry=^{queue_entry}^{queue_entry}}^{ADMATransferDescriptorBuilder}^{AudioDMAController}^{IOWorkLoop}II^{AudioDMAChannelStateMachine}^{_IORecursiveLock}^{ADMAChannelInterface}[256c]B(?=^{_adma_base_ns_txch_blk_v1}^{_adma_base_ns_rxch_blk_v1})^(_adma_base_ns_tdcs_tx_tdfifo_ch0_v1)^(_adma_base_ns_tdcs_tx_csfifo_ch0_v1)^(_adma_base_ns_tdcs_tx_pctfifo_ch0_v1)^{IODMAEventSource}^{AudioDMAChannelConfiguration}QI^{IOInterruptQueueEventSource}IBB^{OSSymbol}^{DMAChannelECProxyInterface}BBBBBQQ^II^{ExceptionJournalEntry}IIIQ^{IOHistogramReporter}^{IOHistogramReporter}^{IOHistogramReporter}^{IOHistogramReporter}^{IOSimpleReporter}[8Q]^{OSSet}^{IOReportLegend}QQB}8"
- "inRequest.fullTransferSize >= inRequest.zeroTransferSize"
- "mach_absolute_time() < timeoutDeadline"
- "operationSucceeded"
- "returnBoolean == true"
- "returnStatus == true"
- "segmentCount <= ADMA4p0::kTDFIFODepth"
- "segmentCount >= 1"
- "static_cast<bool>(_channelECProxy)"
- "static_cast<bool>(_channelECProxyServiceName)"
- "static_cast<bool>(_theMachineLock)"
- "static_cast<bool>(inServiceName)"
- "static_cast<bool>(ioc)"
- "static_cast<bool>(proxyMatchingDict)"
- "status"
- "status == true"
- "tdFIFOStatus.full == 0"
- "timedOut == false"
- "transferDescriptor != nullptr"
- "transferThreshold > almostEmptyThreshold"
- "trueFIFODepth >= _configuration->getFIFOStartTrigger()"
- "trueFIFODepth >= s_rxThresholdBottomClamp"
- "validConfiguration != nullptr"

```
