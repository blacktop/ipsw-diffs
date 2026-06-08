## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`

```diff

-176.122.1.0.0
-  __TEXT.__text: 0x3801c
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x1698
-  __TEXT.__const: 0x4940
-  __TEXT.__cstring: 0xfe8
-  __TEXT.__oslogstring: 0x4fcd
-  __TEXT.__gcc_except_tab: 0x940
-  __TEXT.__unwind_info: 0xe98
-  __TEXT.__objc_classname: 0x332
-  __TEXT.__objc_methname: 0x3dfe
-  __TEXT.__objc_methtype: 0x15f7
-  __TEXT.__objc_stubs: 0x2f00
-  __DATA_CONST.__got: 0x248
+253.0.0.0.0
+  __TEXT.__text: 0x363d8
+  __TEXT.__objc_methlist: 0x1710
+  __TEXT.__const: 0x4950
+  __TEXT.__cstring: 0x104a
+  __TEXT.__oslogstring: 0x4f38
+  __TEXT.__gcc_except_tab: 0x74c
+  __TEXT.__unwind_info: 0xe60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x950
   __DATA_CONST.__objc_classlist: 0xa0
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe80
+  __DATA_CONST.__objc_selrefs: 0xee0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x620
-  __AUTH_CONST.__const: 0x3040
-  __AUTH_CONST.__cfstring: 0xae0
-  __AUTH_CONST.__objc_const: 0x4cf0
+  __DATA_CONST.__got: 0x258
+  __AUTH_CONST.__const: 0x2fe0
+  __AUTH_CONST.__cfstring: 0xb40
+  __AUTH_CONST.__objc_const: 0x4df0
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__objc_doubleobj: 0x20
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__auth_got: 0x658
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x2b8
+  __DATA.__objc_ivar: 0x2b4
   __DATA.__data: 0x5a0
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x28
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E2C3D3A3-72E6-33CC-AD6C-A1D94227EB8D
-  Functions: 1545
-  Symbols:   5467
-  CStrings:  1510
+  UUID: 0D7B53E7-D63D-31FE-A369-BE0F5427F1C2
+  Functions: 1536
+  Symbols:   5425
+  CStrings:  647
 
Symbols:
+ +[NSError(Serialization) errorFromDictionaryRepresentation:]
+ -[MIBUNANPublisher publisher:receivedCCADataForMulticastSession:ccaOBSS:ccaNonWiFi:]
+ -[MIBUNANPublisher publisher:receivedCCADataForMulticastSession:ccaOBSS:ccaNonWiFi:].cold.1
+ -[MIBUNWClientDevice unicastConnection:didReceiveMessage:].cold.5
+ -[MIBUNWServerController nanPublisher:didReceiveCCADataForMulticast:ccaOBSS:ccaNonWiFi:]
+ -[MIBURaptorQPacketConsumer _assembleUsingSummaryReport].cold.4
+ -[MIBURaptorQPacketConsumer consumingProgress]
+ -[NSError(Serialization) dictionaryRepresentation]
+ -[SKRaptorQDecoder targetSymbolCount]
+ _NSLocalizedFailureReasonErrorKey
+ _NSLocalizedRecoverySuggestionErrorKey
+ _OBJC_IVAR_$_MIBUNWClientController._lastBytesConsumed
+ _OBJC_IVAR_$_MIBUNWClientController._lastPacketsConsumed
+ _OBJC_IVAR_$_MIBUNWClientController._lastPacketsReceived
+ _OBJC_IVAR_$_MIBUNWClientController._packetsReceived
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSError_$_Serialization
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSError_$_Serialization
+ __OBJC_$_CATEGORY_NSError_$_Serialization
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.62
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.62.cold.1
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.67
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.67.cold.1
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.75
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.75.cold.1
+ ___35-[MIBUNANPublisher _startPublisher]_block_invoke.87
+ ___35-[MIBUNANPublisher _startPublisher]_block_invoke.87.cold.1
+ ___37-[MIBUNANPublisher publisherStarted:]_block_invoke.180
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.12
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.12.cold.1
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.15
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.15.cold.1
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.20
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.20.cold.1
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.25
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.25.cold.1
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.28
+ ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.28.cold.1
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.38
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.38.cold.1
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.41
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.45
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.45.cold.1
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.50
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.50.cold.1
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.54
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.54.cold.1
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.57
+ ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.57.cold.1
+ ___44-[MIBUNANPublisher _stopPublisherForReason:]_block_invoke.93
+ ___44-[MIBUNANPublisher _stopPublisherForReason:]_block_invoke.93.cold.1
+ ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.144.cold.1
+ ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.147
+ ___45-[MIBUNWServerDevice _handleIncomingMessage:]_block_invoke.44
+ ___45-[MIBUNWServerDevice _handleIncomingMessage:]_block_invoke.44.cold.1
+ ___46-[MIBURaptorQPacketConsumer consumingProgress]_block_invoke
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.119
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.119.cold.1
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.119.cold.2
+ ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.70
+ ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.70.cold.1
+ ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.74
+ ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.74.cold.1
+ ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.77
+ ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.77.cold.1
+ ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.133
+ ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.133.cold.1
+ ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.133.cold.2
+ ___50-[MIBUNANPublisher _stopMulticastPeerCleanUpTimer]_block_invoke.164.cold.1
+ ___50-[MIBUNANPublisher _stopMulticastPeerCleanUpTimer]_block_invoke.167
+ ___51-[MIBUNANPublisher _startMulticastPeerCleanUpTimer]_block_invoke.159
+ ___51-[MIBUNANPublisher publisher:terminatedWithReason:]_block_invoke.189
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.103
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.103.cold.1
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.106
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.106.cold.1
+ ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.59
+ ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.59.cold.1
+ ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.62
+ ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.62.cold.1
+ ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.65
+ ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.65.cold.1
+ ___53-[MIBUNANPublisher publisher:failedToStartWithError:]_block_invoke.183
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.71
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.71.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.74
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.74.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.77
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.77.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.80
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.80.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.83
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.83.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.86
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.86.cold.1
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.89
+ ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.89.cold.1
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.81
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.81.cold.1
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.84
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.84.cold.1
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.89
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.89.cold.1
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.92
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.92.cold.1
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.95
+ ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.95.cold.1
+ ___55-[MIBUNWClientController _receivedVeryFirstPacketArray]_block_invoke.136
+ ___55-[MIBUNWClientController _receivedVeryFirstPacketArray]_block_invoke.136.cold.1
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.150
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.150.cold.1
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.150.cold.2
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.151
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.151.cold.1
+ ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.100
+ ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.100.cold.1
+ ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.94
+ ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.94.cold.1
+ ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.97
+ ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.97.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.33
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.44
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.44.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.47
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.51.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.54
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.54.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.63
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.63.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.66
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.66.cold.1
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke_2.48
+ ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke_2.48.cold.1
+ ___57-[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]_block_invoke.171.cold.1
+ ___57-[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]_block_invoke.174
+ ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.17
+ ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.17.cold.1
+ ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.20
+ ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.20.cold.1
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.127
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.127.cold.1
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.130
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.130.cold.1
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.209.cold.2
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.209.cold.3
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.212.cold.1
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.215
+ ___61-[MIBUNANPublisher publisher:getKeysBlobForMulticastSession:]_block_invoke.228
+ ___61-[MIBUNANPublisher publisher:getKeysBlobForMulticastSession:]_block_invoke.228.cold.1
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.63
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.63.cold.1
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.66
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.66.cold.1
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.69
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.69.cold.1
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.73
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.73.cold.1
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.101
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.101.cold.1
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.107
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.107.cold.1
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.107.cold.2
+ ___69-[SKRaptorQEncoder encodeWithInputURL:packetSize:repairFactor:error:]_block_invoke.100
+ ___69-[SKRaptorQEncoder encodeWithInputURL:packetSize:repairFactor:error:]_block_invoke.86
+ ___69-[SKRaptorQEncoder encodeWithInputURL:packetSize:repairFactor:error:]_block_invoke.86.cold.1
+ ___69-[SKRaptorQEncoder encodeWithInputURL:packetSize:repairFactor:error:]_block_invoke.89
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.116
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.116.cold.1
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.122
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.122.cold.1
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.122.cold.2
+ ___71-[SKRaptorQEncoder _writeSBN:rq:repairFactor:inputIO:outputFile:error:]_block_invoke.107
+ ___71-[SKRaptorQEncoder _writeSBN:rq:repairFactor:inputIO:outputFile:error:]_block_invoke.107.cold.1
+ ___73-[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFiles:]_block_invoke.31
+ ___73-[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFiles:]_block_invoke.31.cold.1
+ ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.220
+ ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.220.cold.1
+ ___84-[MIBUNANPublisher publisher:receivedCCADataForMulticastSession:ccaOBSS:ccaNonWiFi:]_block_invoke
+ ___84-[MIBUNANPublisher publisher:receivedCCADataForMulticastSession:ccaOBSS:ccaNonWiFi:]_block_invoke.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.114
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.114.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.120
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.120.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.126
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.126.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.129
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.129.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.135
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.135.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.138
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.138.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.141
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.141.cold.1
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.144
+ ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.144.cold.1
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.197.cold.2
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.197.cold.3
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.197.cold.4
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.200.cold.1
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.203
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke_2.204
+ ___block_literal_global.105
+ ___block_literal_global.116
+ ___block_literal_global.118
+ ___block_literal_global.124
+ ___block_literal_global.128
+ ___block_literal_global.140
+ ___block_literal_global.206
+ ___block_literal_global.217
+ ___block_literal_global.224
+ ___block_literal_global.55
+ ___block_literal_global.79
+ ___block_literal_global.82
+ ___block_literal_global.85
+ ___block_literal_global.88
+ ___block_literal_global.91
+ ___block_literal_global.99
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$assemblyProgress
+ _objc_msgSend$consumingProgress
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$errorFromDictionaryRepresentation:
+ _objc_msgSend$initWithBasicParametersArray:extendedParametersArray:threshold:fileRanges:outputFiles:
+ _objc_msgSend$localizedFailureReason
+ _objc_msgSend$localizedRecoverySuggestion
+ _objc_msgSend$nanPublisher:didReceiveCCADataForMulticast:ccaOBSS:ccaNonWiFi:
+ _objc_msgSend$serverController:didReceiveCCADataForMulticast:ccaOBSS:ccaNonWiFi:
+ _objc_msgSend$targetSymbolCount
+ _objc_msgSend$userInfo
+ _objc_opt_isKindOfClass
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x8
- -[MIBURaptorQPacketConsumer _assembleWithCompletion:].cold.11
- -[MIBURaptorQPacketConsumer _bootstrap].cold.7
- -[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:].cold.12
- -[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:].cold.13
- -[MIBURaptorQPacketConsumer getAssemblyProgress]
- -[MIBURaptorQPacketConsumer initWithBasicParameters:extendedParameters:threshold:outputFile:]
- -[MIBURaptorQPacketConsumer initWithEncoderSummary:threshold:outputFile:]
- -[MIBURaptorQPacketConsumer initWithEncoderSummary:threshold:outputFile:].cold.1
- GCC_except_table32
- _OBJC_IVAR_$_MIBUNWClientController._packetExpected
- _OBJC_IVAR_$_MIBUNWClientController._packetReceived
- _OBJC_IVAR_$_MIBURaptorQPacketConsumer._assemblyProgress
- _OBJC_IVAR_$_MIBURaptorQPacketConsumer._multiFileMode
- _OBJC_IVAR_$_MIBURaptorQPacketConsumer._raptorQDecoder
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.59
- ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.59.cold.1
- ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.64
- ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.64.cold.1
- ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.69
- ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.69.cold.1
- ___35-[MIBUNANPublisher _startPublisher]_block_invoke.84
- ___35-[MIBUNANPublisher _startPublisher]_block_invoke.84.cold.1
- ___37-[MIBUNANPublisher publisherStarted:]_block_invoke.177
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.13
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.13.cold.1
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.16
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.16.cold.1
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.21
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.21.cold.1
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.26
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.26.cold.1
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.29
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.29.cold.1
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.32
- ___39-[MIBURaptorQPacketConsumer _bootstrap]_block_invoke.32.cold.1
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.39
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.39.cold.1
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.42
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.46
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.46.cold.1
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.51
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.51.cold.1
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.55
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.55.cold.1
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.58
- ___39-[MIBURaptorQPacketProvider _bootstrap]_block_invoke.58.cold.1
- ___44-[MIBUNANPublisher _stopPublisherForReason:]_block_invoke.90
- ___44-[MIBUNANPublisher _stopPublisherForReason:]_block_invoke.90.cold.1
- ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.141
- ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.141.cold.1
- ___45-[MIBUNWServerDevice _handleIncomingMessage:]_block_invoke.54
- ___45-[MIBUNWServerDevice _handleIncomingMessage:]_block_invoke.54.cold.1
- ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.120
- ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.120.cold.1
- ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.120.cold.2
- ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.71
- ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.71.cold.1
- ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.75
- ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.75.cold.1
- ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.78
- ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.78.cold.1
- ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.130
- ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.130.cold.1
- ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.130.cold.2
- ___50-[MIBUNANPublisher _stopMulticastPeerCleanUpTimer]_block_invoke.161
- ___50-[MIBUNANPublisher _stopMulticastPeerCleanUpTimer]_block_invoke.161.cold.1
- ___51-[MIBUNANPublisher _startMulticastPeerCleanUpTimer]_block_invoke.156
- ___51-[MIBUNANPublisher publisher:terminatedWithReason:]_block_invoke.186
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.104
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.104.cold.1
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.107
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.107.cold.1
- ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.60
- ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.60.cold.1
- ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.63
- ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.63.cold.1
- ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.66
- ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.66.cold.1
- ___53-[MIBUNANPublisher publisher:failedToStartWithError:]_block_invoke.180
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.102
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.102.cold.1
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.81
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.81.cold.1
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.84
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.84.cold.1
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.87
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.87.cold.1
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.90
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.90.cold.1
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.93
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.93.cold.1
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.96
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.96.cold.1
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.99
- ___53-[MIBURaptorQPacketConsumer _assembleWithCompletion:]_block_invoke.99.cold.1
- ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.82
- ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.82.cold.1
- ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.85
- ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.85.cold.1
- ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.90
- ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.90.cold.1
- ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.93
- ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.93.cold.1
- ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.96
- ___53-[MIBURaptorQPacketProvider _splitInputFileIfNeeded:]_block_invoke.96.cold.1
- ___55-[MIBUNWClientController _receivedVeryFirstPacketArray]_block_invoke.137
- ___55-[MIBUNWClientController _receivedVeryFirstPacketArray]_block_invoke.137.cold.1
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.147
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.147.cold.1
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.147.cold.2
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.148
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.148.cold.1
- ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.107
- ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.107.cold.1
- ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.110
- ___56-[MIBURaptorQPacketConsumer _assembleUsingSummaryReport]_block_invoke.110.cold.1
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.37
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.48
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.48.cold.1
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.55
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.55.cold.1
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.58
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.58.cold.1
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.67
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.67.cold.1
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.70
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.70.cold.1
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.73
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.73.cold.1
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.76
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke.76.cold.1
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke_2.52
- ___56-[MIBURaptorQPacketConsumer _consumePacket:arrivalTime:]_block_invoke_2.52.cold.1
- ___57-[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]_block_invoke.168
- ___57-[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]_block_invoke.168.cold.1
- ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.27
- ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.27.cold.1
- ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.30
- ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.30.cold.1
- ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.128
- ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.128.cold.1
- ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.131
- ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.131.cold.1
- ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.cold.4
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.206
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.206.cold.1
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.206.cold.2
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.206.cold.3
- ___61-[MIBUNANPublisher publisher:getKeysBlobForMulticastSession:]_block_invoke.223
- ___61-[MIBUNANPublisher publisher:getKeysBlobForMulticastSession:]_block_invoke.223.cold.1
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.64
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.64.cold.1
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.67
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.67.cold.1
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.70
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.70.cold.1
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.74
- ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.74.cold.1
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.104
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.104.cold.1
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.104.cold.2
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.98
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.98.cold.1
- ___69-[SKRaptorQEncoder encodeWithInputURL:packetSize:repairFactor:error:]_block_invoke.101
- ___69-[SKRaptorQEncoder encodeWithInputURL:packetSize:repairFactor:error:]_block_invoke.87
- ___69-[SKRaptorQEncoder encodeWithInputURL:packetSize:repairFactor:error:]_block_invoke.87.cold.1
- ___69-[SKRaptorQEncoder encodeWithInputURL:packetSize:repairFactor:error:]_block_invoke.90
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.113
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.113.cold.1
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.119
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.119.cold.1
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.119.cold.2
- ___71-[SKRaptorQEncoder _writeSBN:rq:repairFactor:inputIO:outputFile:error:]_block_invoke.108
- ___71-[SKRaptorQEncoder _writeSBN:rq:repairFactor:inputIO:outputFile:error:]_block_invoke.108.cold.1
- ___73-[MIBURaptorQPacketConsumer initWithEncoderSummary:threshold:outputFile:]_block_invoke
- ___73-[MIBURaptorQPacketConsumer initWithEncoderSummary:threshold:outputFile:]_block_invoke.cold.1
- ___73-[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFiles:]_block_invoke.32
- ___73-[MIBURaptorQPacketProvider initWithPayloadSize:repairFactor:inputFiles:]_block_invoke.32.cold.1
- ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.217
- ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.217.cold.1
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.124
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.124.cold.1
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.130
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.130.cold.1
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.136
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.136.cold.1
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.139
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.139.cold.1
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.145
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.145.cold.1
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.148
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.148.cold.1
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.151
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.151.cold.1
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.154
- ___87-[MIBURaptorQPacketConsumer reassembleFileFromParts:toOutputFile:maxBytesToRead:error:]_block_invoke.154.cold.1
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.194
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.194.cold.1
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.194.cold.2
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.194.cold.3
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.194.cold.4
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke_2.201
- ___block_literal_global.104
- ___block_literal_global.110
- ___block_literal_global.113
- ___block_literal_global.119
- ___block_literal_global.127
- ___block_literal_global.130
- ___block_literal_global.133
- ___block_literal_global.136
- ___block_literal_global.150
- ___block_literal_global.160
- ___block_literal_global.167
- ___block_literal_global.185
- ___block_literal_global.191
- ___block_literal_global.193
- ___block_literal_global.203
- ___block_literal_global.216
- ___block_literal_global.225
- ___block_literal_global.29
- ___block_literal_global.57
- ___block_literal_global.66
- _objc_msgSend$dictionaryWithObject:forKey:
- _objc_msgSend$getAssemblyProgress
- _objc_msgSend$initWithEncoderSummary:threshold:outputFile:
CStrings:
+ "\f"
+ "%{public}@: All needed packets received! Total packets consumed: %lu (%{iec-bytes}lu), Total cycle time: %0.3fs"
+ "%{public}@: Failed to deserialize summary: %@"
+ "%{public}@: File assembly done, total time taken: %.3fs"
+ "%{public}@: NAN publisher received CCA data - ccaIBSS: %u%%, ccaOBSS: %u%%, ccaNonWiFi: %u%%"
+ "%{public}@: state: %lu; progress = %0.3f%%"
+ "Encoder summary not available. Use initWithEncoderSummaryFile:threshold:outputFile: to initialize."
+ "FailureReason"
+ "Invalid decoder for fileNumber %u (expected 0-%lu)"
+ "Packets received in the last %lu secs: %lu (%{iec-bytes}lu); Packets consumed by RaptorQ: %lu (%{iec-bytes}lu); Effective bandwidth: %0.3f Mbps"
+ "RecoverySuggestion"
+ "UnderlyingError"
- "#16@0:8"
- "%{public}@: All needed packets received! Total packets consumed: %lu (=%lu bytes), Total cycle time: %fs"
- "%{public}@: File assembly done, total time taken: %fs"
- "%{public}@: failed to deserialize summary: %@"
- "%{public}@: state: %lu; packets: %lu/%lu (%lu missing), progress = %@"
- "%{public}@: state: %lu; progress = %@"
- ".cxx_destruct"
- "@\"<MIBUDataCollectorProtocol>\""
- "@\"<MIBUMulticastSocketDelegate>\""
- "@\"<MIBUNANPublisherDelegate>\""
- "@\"<MIBUNANSubscriberDelegate>\""
- "@\"<MIBUNWClientControllerDelegate>\""
- "@\"<MIBUNWClientDeviceDelegate>\""
- "@\"<MIBUNWClientListenerDelegate>\""
- "@\"<MIBUNWConnectionDelegate>\""
- "@\"<MIBUNWServerControllerDelegate>\""
- "@\"<MIBUNWServerDeviceDelegate>\""
- "@\"<MIBUPacketConsumable>\""
- "@\"<MIBUPacketProvidable>\""
- "@\"MIBUMulticastSocket\""
- "@\"MIBUNANPublisher\""
- "@\"MIBUNANSubscriber\""
- "@\"MIBUNWClientListener\""
- "@\"MIBUNWConnection\""
- "@\"MIBUNWServerDevice\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSFileHandle\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableIndexSet\""
- "@\"NSMutableOrderedSet\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSNumber\"16@0:8"
- "@\"NSObject<OS_dispatch_io>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_nw_connection>\""
- "@\"NSObject<OS_nw_listener>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSTimer\""
- "@\"SKRaptorQDecoder\""
- "@\"SKRaptorQEncoderSummary\""
- "@\"WiFiAwareDataSession\""
- "@\"WiFiAwarePublishConfiguration\""
- "@\"WiFiAwarePublisher\""
- "@\"WiFiAwareSubscribeConfiguration\""
- "@\"WiFiAwareSubscriber\""
- "@100@0:8@16@24@32@40Q48Q56Q64B72@76@84@92"
- "@116@0:8@16@24@32@40@48@56Q64Q72Q80B88@92@100@108"
- "@120@0:8@16@24@32@40@48@56@64@72Q80Q88Q96B104B108@112"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@28@0:8S16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8I16C20^@24"
- "@32@0:8Q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16Q24@32"
- "@40@0:8@16Q24Q32"
- "@40@0:8@16Q24^@32"
- "@40@0:8Q16Q24@32"
- "@44@0:8Q16I24Q28@36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16Q24Q32^@40"
- "@52@0:8@16@24@32B40@44"
- "@56@0:8@16@24Q32@40@48"
- "@56@0:8Q16I24I28Q32@40^@48"
- "@80@0:8@16@24@32Q40Q48Q56B64B68@72"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B32@0:8@16Q24"
- "B32@0:8@16^@24"
- "B32@0:8^@16^Q24"
- "B40@0:8Q16^@24^Q32"
- "B48@0:8@16@24@32^@40"
- "B56@0:8I16C20^{nanorq=}24^{ioctx=^?^?^?^?^?^?BB}32^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}40^@48"
- "B60@0:8C16^{nanorq=}20Q28^{ioctx=^?^?^?^?^?^?BB}36^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}44^@52"
- "C"
- "C16@0:8"
- "Failed to add symbol to RaptorQ decoder: %{public}@"
- "Failed to initialize RaptorQ decoder: %{public}@"
- "I"
- "I16@0:8"
- "I24@0:8Q16"
- "Initialize packet consumer with basic parameters: %llu, extended parameters: %u, threshold: %lu, output file: %{public}@"
- "Invalid fileNumber %u (expected 0-%lu)"
- "JSONObjectWithData:options:error:"
- "MIBUEncodedFileInfo"
- "MIBUExtension"
- "MIBUFilePacketConsumer"
- "MIBUFilePacketProvider"
- "MIBUMulticastSocket"
- "MIBUMulticastSocketDelegate"
- "MIBUNANPublisher"
- "MIBUNANPublisherDelegate"
- "MIBUNANSubscriber"
- "MIBUNANSubscriberDelegate"
- "MIBUNWClientController"
- "MIBUNWClientDevice"
- "MIBUNWClientDeviceDelegate"
- "MIBUNWClientListener"
- "MIBUNWClientListenerDelegate"
- "MIBUNWConnection"
- "MIBUNWConnectionDelegate"
- "MIBUNWDevice"
- "MIBUNWMessage"
- "MIBUNWServerController"
- "MIBUNWServerDevice"
- "MIBUNWServerDeviceDelegate"
- "MIBUPacketConsumable"
- "MIBUPacketProvidable"
- "MIBURaptorQPacketConsumer"
- "MIBURaptorQPacketProvider"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Packets received in the last %lu secs: %lu (Bytes: %lu); Bytes consumed by RaptorQ: %lu; Effective bandwidth: %0.5f Mbps"
- "Q16@0:8"
- "RaptorQ decoder has received enough encoded symbols! Cycle time between first and last packet: %f"
- "S"
- "S16@0:8"
- "SKRaptorQDecoder"
- "SKRaptorQEncoderSummary"
- "T#,R"
- "T@\"<MIBUNWClientDeviceDelegate>\",W,N,V_delegate"
- "T@\"NSArray\",&,N,V_rqEncodedFileURLs"
- "T@\"NSArray\",&,N,V_rqSourceSymbolCounts"
- "T@\"NSArray\",R,N,V_rqBasicParametersArray"
- "T@\"NSArray\",R,N,V_rqExtendedParametersArray"
- "T@\"NSDictionary\",&,N,V_payload"
- "T@\"NSDictionary\",R,N"
- "T@\"NSFileHandle\",&,N,V_fileHandle"
- "T@\"NSNumber\",R,C,N,V_progress"
- "T@\"NSNumber\",R,N,V_assemblyProgress"
- "T@\"NSNumber\",R,N,V_decodingProgress"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_syncSemaphore"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,N,V_clientIPv6Address"
- "T@\"NSString\",R,N,V_clientSerialNumber"
- "T@\"NSString\",R,N,V_remoteIPv6Address"
- "TB,R"
- "TC,N,V_sourceBlockNumber"
- "TI,N,V_fileNumber"
- "TI,N,V_rqExtendedParameters"
- "TI,R,N,V_rqExtendedParameters"
- "TQ,N"
- "TQ,N,V_batchSize"
- "TQ,N,V_clientCount"
- "TQ,N,V_peerTimeout"
- "TQ,N,V_retryLimit"
- "TQ,N,V_rqBasicParameters"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_bytesConsumed"
- "TQ,R,N,V_packetsConsumed"
- "TQ,R,N,V_packetsDiscarded"
- "TQ,R,N,V_rqBasicParameters"
- "TQ,R,N,V_state"
- "TS,N,V_type"
- "Td,R,N"
- "Td,R,N,V_lossRate"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "URLByDeletingLastPathComponent"
- "UTF8String"
- "Vv16@0:8"
- "WiFiAwareDataSessionDelegate"
- "WiFiAwarePublisherDelegate"
- "WiFiAwareSubscriberDelegate"
- "^{_NSZone=}16@0:8"
- "^{ioctx=^?^?^?^?^?^?BB}"
- "^{nanorq=}"
- "_SKRaptorQRReceptionDetails"
- "_activateProgressTimer"
- "_adjustBatchSizeWithPacketDroppedInLastInterval:"
- "_assembleOutputFile"
- "_assembleUsingSummaryReport"
- "_assembleWithCompletion:"
- "_assemblyProgress"
- "_atEOF"
- "_band"
- "_bandwidth"
- "_bandwidthTimer"
- "_basicParametersArray"
- "_batchSize"
- "_bootstrap"
- "_bytesConsumed"
- "_calculateEffectiveBandwidth"
- "_cancelTimerForWaitingState"
- "_channelName"
- "_checkOutAck"
- "_checkOutWithError:withSummary:"
- "_checkedInClients"
- "_clientCount"
- "_clientIPv6Address"
- "_clientSerialNumber"
- "_close"
- "_closeIOChannel"
- "_completed"
- "_connectOnDemand"
- "_connection"
- "_consumePacket:arrivalTime:"
- "_consumePacket:withCompletion:inQueue:"
- "_controllerDelegate"
- "_countryCode"
- "_createDataSessionWithDiscoveryResult:"
- "_createDispatchData"
- "_createNANTCPConnectionUsingInterface:"
- "_dataCollector"
- "_dataSession"
- "_dataSessionMapping"
- "_dataSessionTimer"
- "_deactivateProgressTimer"
- "_decodePacket:outPayload:outPacketCount:outPacketUID:"
- "_decodingProgress"
- "_delegate"
- "_disableFirewall"
- "_dispatchQueue"
- "_dispatchSource"
- "_encodePacketWithPayload:packetCount:packetUID:"
- "_encodedFileHandles"
- "_encodedFileURLs"
- "_encodedFiles"
- "_encodedSymbolSets"
- "_encoderSummaries"
- "_encoderSummary"
- "_extendedParametersArray"
- "_fetchIssued"
- "_fetchOneBatchOfPacketsFromProvider"
- "_fileChannel"
- "_fileCompletionStatus"
- "_fileHandle"
- "_fileNumber"
- "_fileRangeTable"
- "_fileRanges"
- "_firstESI"
- "_firstReceived"
- "_getRSSIofNAN:"
- "_getRemoteIPv6AddressFromConnection:"
- "_groupAddr"
- "_groupAddress"
- "_groupPort"
- "_handleFailureDueToError:"
- "_handleFetchCompletionWithResult:atEOF:packets:"
- "_handleInboundPackets:arrivalTime:"
- "_handleIncomingMessage:"
- "_handleMulticastPeerCleanUpTimerFired"
- "_handleNANDataSessionExpiredForPeer:"
- "_handleNewConnectionState:error:"
- "_handleNewListenerState:error:"
- "_handleNewNetworkConnection:"
- "_handlePacketConsumerCompletion"
- "_handleProgressTimerTick"
- "_handleReadDispatchSource"
- "_handleSourceCancelled"
- "_handleWriteDispatchSource"
- "_hasNext"
- "_hostAddress"
- "_hostPort"
- "_inputFile"
- "_inputFiles"
- "_inputIO"
- "_interfaceName"
- "_invalidate"
- "_invalidateNANTCPConnection"
- "_isComplete"
- "_largestESI"
- "_lastActivity"
- "_lastESI"
- "_listener"
- "_lossRate"
- "_messages"
- "_missingPackets"
- "_multiFileMode"
- "_multicastData:withCompletion:"
- "_multicastPeers"
- "_multicastSecurity"
- "_multicastSocket"
- "_multicastSocketSem"
- "_nanConfiguration"
- "_nanDevices"
- "_nanHostPort"
- "_nanIPv6AddrMapping"
- "_nanListener"
- "_nanPublisher"
- "_nanSubscriber"
- "_nanUnicastDevice"
- "_open"
- "_openIOChannel"
- "_originalBatchSize"
- "_outputFile"
- "_outputFiles"
- "_outputIO"
- "_packetConsumer"
- "_packetCount"
- "_packetCountsPerFile"
- "_packetDropBreakdown"
- "_packetDropSummary"
- "_packetDropped"
- "_packetExpected"
- "_packetFetched"
- "_packetID"
- "_packetProvider"
- "_packetReceived"
- "_packetSent"
- "_packetsConsumed"
- "_packetsDiscarded"
- "_partOutputFiles"
- "_partOutputFilesSizes"
- "_payload"
- "_payloadSize"
- "_peerCleanUpTimer"
- "_peerLastContact"
- "_peerTimeout"
- "_pingInterval"
- "_pingThroughMulticast:"
- "_pingTimeout"
- "_processPendingMessages:"
- "_progress"
- "_progressTimer"
- "_provideOnePacketWithCompletion:"
- "_providePacketsOfCount:withCompletion:inQueue:"
- "_publisherDelegate"
- "_publisherState"
- "_queue"
- "_raptorQDecoder"
- "_raptorQDecoders"
- "_rateAdapter"
- "_readIOChannelOfPacketCount:withCompletion:inQueue:"
- "_receivedVeryFirstPacketArray"
- "_receptionDetails"
- "_remoteIPv6Address"
- "_reopenIOChannel"
- "_repairFactor"
- "_retryCount"
- "_retryLimit"
- "_rewind"
- "_rq"
- "_rqBasicParameters"
- "_rqBasicParametersArray"
- "_rqEncodedFileURLs"
- "_rqExtendedParameters"
- "_rqExtendedParametersArray"
- "_rqSourceSymbolCounts"
- "_sbnStillReceiving"
- "_scheduleNextMessageReception"
- "_sendData:withCompletion:"
- "_sendMessage:"
- "_sendMessage:withCompletion:"
- "_sendOutgoingMessage:synchronous:shouldWait:"
- "_sendPacket:retryCount:withCompletion:"
- "_sendPackets:withCompletion:"
- "_serviceName"
- "_setupFileSenderLoop"
- "_setupTimerForWaitingState"
- "_socketDelegate"
- "_socketFD"
- "_sourceBlockNumber"
- "_splitInputFileIfNeeded:"
- "_start"
- "_startMulticastPeerCleanUpTimer"
- "_startMulticastReceiverUsingInterface:"
- "_startMulticastUsingInterface:"
- "_startNANService"
- "_startPublisher"
- "_startSubscriber"
- "_startTCPListener"
- "_startTime"
- "_state"
- "_stop"
- "_stopMulticast"
- "_stopMulticastPeerCleanUpTimer"
- "_stopMulticastReceiver"
- "_stopPublisherForReason:"
- "_stopSubscriberForReason:"
- "_stopWithReason:"
- "_subscriberDelegate"
- "_subscriberState"
- "_syncSemaphore"
- "_targetSymbolCounts"
- "_tcpDevices"
- "_tcpHostAddr"
- "_tcpHostPort"
- "_tcpListener"
- "_tearDownFileSenderLoop"
- "_terminateDataSessionWithPeer:withCompletion:"
- "_terminateMulticastSessionWithPeer:withCompletion:"
- "_threshold"
- "_type"
- "_unfairLock"
- "_updateControllerProgress"
- "_updatePacketDropBreakdown:"
- "_waitingTimer"
- "_workFolder"
- "_writeESI:sbn:rq:inputIO:outputFile:error:"
- "_writePayloadToFile:forPacketUID:"
- "_writeSBN:rq:repairFactor:inputIO:outputFile:error:"
- "addIndex:"
- "addKeyEvent:"
- "addKeyEvent:additionalData:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserverForName:object:queue:usingBlock:"
- "addPacket:error:"
- "addPacketsFromFilesInSummary:error:"
- "addTimer:forMode:"
- "appendBytes:length:"
- "appendData:"
- "appendFormat:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "assemble"
- "assembleUsingSummaryReport"
- "assembleWithCompletion:"
- "assemblyProgress"
- "attributesOfItemAtPath:error:"
- "autorelease"
- "batchSize"
- "boolValue"
- "bootstrap"
- "bytes"
- "bytesConsumed"
- "calculateSymbolLostRate"
- "checkIn"
- "checkOutWithError:withSummary:"
- "class"
- "clientControllerDidFailReceiving:error:"
- "clientControllerDidFinishAssembly:withStats:"
- "clientControllerDidFinishReceive:withStats:"
- "clientControllerDidStartAssembly:"
- "clientControllerDidStartReceive:"
- "clientCount"
- "clientDevice:didCheckOutWithError:withSummary:"
- "clientDevice:didPingWithPayload:"
- "clientDeviceDidCheckIn:"
- "clientDeviceDidConnect:"
- "clientDeviceDidDisconnect:"
- "clientIPv6Address"
- "clientListener:didReceiveNewClientDevice:"
- "clientListenerDidStart:"
- "clientListenerDidStop:withError:"
- "clientSerialNumber"
- "close"
- "closeAndReturnError:"
- "closeFile"
- "code"
- "componentsJoinedByString:"
- "configuration"
- "conformsToProtocol:"
- "connect"
- "consumePacket:arrivalTime:withCompletion:inQueue:"
- "consumePacket:withCompletion:inQueue:"
- "consumePackets:arrivalTime:withCompletion:inQueue:"
- "containsIndex:"
- "containsObject:"
- "contentsOfDirectoryAtPath:error:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createContent"
- "createContentContext"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createFileAtPath:contents:attributes:"
- "currentDeviceCapabilities"
- "currentRunLoop"
- "d"
- "d16@0:8"
- "data"
- "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:"
- "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
- "dataSession:failedToStartWithError:"
- "dataSession:receivedControlDataAddress:serviceSpecificInfo:onInterfaceIndex:"
- "dataSession:terminatedWithReason:"
- "dataSession:updatedPeerRSSI:"
- "dataSessionRequestStarted:"
- "dataWithCapacity:"
- "dataWithContentsOfFile:options:error:"
- "dataWithPropertyList:format:options:error:"
- "dateByAddingTimeInterval:"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "decodeAllSourceBlocks:discarded:"
- "decodeBlock:error:discarded:"
- "decodeInputURL:error:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodingProgress"
- "defaultCenter"
- "defaultManager"
- "delegate"
- "description"
- "dictionaryWithDictionary:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "disconnect"
- "discoveryInterfaceName"
- "domain"
- "doubleValue"
- "earlierDate:"
- "encodeInputFile:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodeWithInputURL:packetSize:repairFactor:dispatchQueue:completionHandler:"
- "encodeWithInputURL:packetSize:repairFactor:error:"
- "encoderSummaryFromFile:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "etherAddressString"
- "fileExistsAtPath:"
- "fileHandle"
- "fileHandleForReadingAtPath:"
- "fileHandleForReadingFromURL:error:"
- "fileHandleForWritingAtPath:"
- "fileHandleForWritingToURL:error:"
- "fileNumber"
- "fileRangeTable"
- "fileSize"
- "fileSystemRepresentation"
- "fileURLWithPath:"
- "firstObject"
- "generatePacketWithESI:sourceBlock:error:"
- "getAssemblyProgress"
- "getBytes:range:"
- "hasNext"
- "hash"
- "init"
- "initWithBasicParameters:extendedParameters:repairFactor:threshold:outputURL:error:"
- "initWithBasicParameters:extendedParameters:threshold:outputFile:"
- "initWithBasicParametersArray:extendedParametersArray:threshold:fileRanges:outputFiles:"
- "initWithCapacity:"
- "initWithChannelNumber:bandwidth:is2_4GHz:is5GHz:is6GHz:isDFS:extensionChannelAbove:"
- "initWithCoder:"
- "initWithConfiguration:"
- "initWithConfiguration:delegate:"
- "initWithConfiguration:messageFramer:dispatchQueue:statusDelegate:"
- "initWithContent:andContext:"
- "initWithDiscoveryResult:serviceType:serviceSpecificInfo:"
- "initWithEncoderSummary:threshold:outputFile:"
- "initWithEncoderSummaryFile:threshold:outputFile:"
- "initWithFireDate:interval:repeats:block:"
- "initWithFormat:arguments:"
- "initWithHostAddress:hostPort:interfaceName:connectOnDemand:statusDelegate:"
- "initWithIndexesInRange:"
- "initWithInputURL:symbolSize:error:"
- "initWithLinkIPv6AddressString:"
- "initWithLinkLocalIPv6Address:"
- "initWithMulticastIPv6Address:"
- "initWithMulticastIPv6AddressString:"
- "initWithNWConnection:"
- "initWithNWConnection:dispatchQueue:statusDelegate:"
- "initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:"
- "initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:controllerDelegate:"
- "initWithPayloadSize:inputFile:"
- "initWithPayloadSize:outputFile:"
- "initWithPayloadSize:repairFactor:inputFiles:"
- "initWithServiceName:"
- "initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:"
- "initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:"
- "initWithServiceType:securityConfiguration:"
- "initWithType:andPayload:"
- "initiatorDataAddress"
- "intValue"
- "integerValue"
- "invalidate"
- "ipv6AddressString"
- "ipv6LinkLocalAddress"
- "isActive"
- "isComplete"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastPathComponent"
- "length"
- "localInterfaceIndex"
- "localizedDescription"
- "lock"
- "lossRate"
- "missingCount"
- "missingSymbolCount"
- "multicastConfiguration"
- "multicastData:withCompletion:"
- "multicastSocket:didReceivePackets:atTime:"
- "multicastSocketDidStart:"
- "multicastSocketDidStop:withError:"
- "nanPublisher:didCreateDataSessionWithPeer:usingInterface:"
- "nanPublisher:didDestoryDataSessionWithPeer:"
- "nanPublisher:didGenerateSecurityKeys:"
- "nanPublisher:didReceiveData:fromPeer:"
- "nanPublisherDidStart:usingInterface:forRetry:"
- "nanPublisherDidStop:withError:willRetry:"
- "nanSubscriber:didReceiveData:"
- "nanSubscriberDetectedMulticastError:"
- "nanSubscriberDidStart:withPeerIPAddress:usingInterface:forRetry:"
- "nanSubscriberDidStop:withError:willRetry:"
- "nanSubscriberDidTerminateDataSession:"
- "now"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "numberWithUnsignedShort:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "open"
- "packetSize"
- "packetsConsumed"
- "packetsDiscarded"
- "path"
- "payload"
- "peerTimeout"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pingThroughMulticast:"
- "pingWithPayload:"
- "popFirstObject"
- "postNotificationName:object:userInfo:"
- "progress"
- "propertyListWithData:options:format:error:"
- "providePacketsOfCount:withCompletion:inQueue:"
- "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:"
- "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:"
- "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
- "publisher:dataTerminatedForHandle:reason:"
- "publisher:detectedMulticastError:fromMulticastReceiver:"
- "publisher:failedToStartWithError:"
- "publisher:getKeysBlobForMulticastSession:"
- "publisher:receivedDataBlobForMulticastSession:fromPeer:"
- "publisher:receivedMessage:fromSubscriberID:subscriberAddress:"
- "publisher:terminatedWithReason:"
- "publisherAddress"
- "publisherStarted:"
- "q16@0:8"
- "rangeOfString:"
- "rangeValue"
- "readDataOfLength:"
- "readDataUpToLength:error:"
- "reassembleFileFromParts:toOutputFile:maxBytesToRead:error:"
- "release"
- "remoteIPv6Address"
- "removeAllObjects"
- "removeIndex:"
- "removeItemAtPath:error:"
- "removeItemAtURL:error:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObserver:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "retryLimit"
- "rewind"
- "rqBasicParameters"
- "rqBasicParametersArray"
- "rqEncodedFileURLs"
- "rqExtendedParameters"
- "rqExtendedParametersArray"
- "rqSourceSymbolCounts"
- "rssi"
- "seekToOffset:error:"
- "self"
- "sendData:withCompletion:"
- "sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:"
- "sendMessage:withCompletion:"
- "sendOutgoingMessage:synchronous:"
- "sendPacket:withCompletion:"
- "serverController:didReceiveClientDeviceCheckIn:"
- "serverController:didReceiveClientDeviceCheckOut:withError:andSummary:"
- "serverController:didReceiveClientDeviceStatus:forDevice:"
- "serverController:didReceiveMulticastSecurityKeys:"
- "serverController:didReceiveNewClientDevice:"
- "serverDeviceDidCheckIn:"
- "serverDeviceDidCheckOut:"
- "serverDeviceDidConnect:"
- "serverDeviceDidDisconnect:"
- "serviceName"
- "setAuthenticationType:"
- "setBatchSize:"
- "setChannelInfo:"
- "setClientCount:"
- "setCountryCode:"
- "setDatapathConfiguration:"
- "setDelegate:"
- "setDynamicLinkRate:"
- "setFileHandle:"
- "setFileNumber:"
- "setKeyBlob:"
- "setKeyExchangeOverMedium:"
- "setMulticastAddress:"
- "setMulticastConfiguration:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPayload:"
- "setPeerTimeout:"
- "setRetryLimit:"
- "setRqBasicParameters:"
- "setRqEncodedFileURLs:"
- "setRqExtendedParameters:"
- "setRqSourceSymbolCounts:"
- "setSourceBlockNumber:"
- "setState:"
- "setSyncSemaphore:"
- "setType:"
- "setWithObjects:"
- "sharedFramer"
- "signal"
- "sourceBlockNumber"
- "start"
- "state"
- "stop"
- "stopMulticast"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByDeletingLastPathComponent"
- "stringByDeletingPathExtension"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "subscriber:detectedMulticastError:fromMulticastSender:"
- "subscriber:failedToStartWithError:"
- "subscriber:lostDiscoveryResultForPublishID:address:"
- "subscriber:receivedDataBlobForMulticastSession:fromPeer:"
- "subscriber:receivedDiscoveryResult:"
- "subscriber:receivedDiscoveyResult:"
- "subscriber:receivedMessage:fromPublishID:address:"
- "subscriber:terminatedWithReason:"
- "subscriberStarted:"
- "substringToIndex:"
- "sufficientSymbolsReceived"
- "superclass"
- "supportsSecureCoding"
- "symbolsShouldHaveReceived:"
- "syncSemaphore"
- "terminateDataSession:completionHandler:"
- "terminateDataSessionWithPeer:withCompletion:"
- "terminateMulticastSession:completionHandler:"
- "terminateMulticastSessionWithPeer:withCompletion:"
- "timeIntervalSinceDate:"
- "type"
- "unarchivedObjectOfClass:fromData:error:"
- "unicastConnection:didEnterNewState:"
- "unicastConnection:didReceiveMessage:"
- "unicastConnectionDidClose:withError:"
- "unicastConnectionDidOpen:"
- "unlock"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "unsignedLongValue"
- "unsignedShortValue"
- "updateClientStatus:forDevice:"
- "updateWithESI:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v20@0:8S16"
- "v24@0:8@\"MIBUMulticastSocket\"16"
- "v24@0:8@\"MIBUNANSubscriber\"16"
- "v24@0:8@\"MIBUNWClientDevice\"16"
- "v24@0:8@\"MIBUNWClientListener\"16"
- "v24@0:8@\"MIBUNWConnection\"16"
- "v24@0:8@\"MIBUNWServerDevice\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"WiFiAwareDataSession\"16"
- "v24@0:8@\"WiFiAwarePublisher\"16"
- "v24@0:8@\"WiFiAwareSubscriber\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8Q16"
- "v28@0:8@\"WiFiAwareDataSession\"16i24"
- "v28@0:8@16B24"
- "v28@0:8@16i24"
- "v28@0:8i16@20"
- "v32@0:8@\"MIBUMulticastSocket\"16@\"NSError\"24"
- "v32@0:8@\"MIBUNANPublisher\"16@\"NSData\"24"
- "v32@0:8@\"MIBUNANPublisher\"16@\"NSString\"24"
- "v32@0:8@\"MIBUNANSubscriber\"16@\"NSData\"24"
- "v32@0:8@\"MIBUNWClientDevice\"16@\"NSDictionary\"24"
- "v32@0:8@\"MIBUNWClientListener\"16@\"MIBUNWClientDevice\"24"
- "v32@0:8@\"MIBUNWClientListener\"16@\"NSError\"24"
- "v32@0:8@\"MIBUNWConnection\"16@\"MIBUNWMessage\"24"
- "v32@0:8@\"MIBUNWConnection\"16@\"NSError\"24"
- "v32@0:8@\"MIBUNWConnection\"16Q24"
- "v32@0:8@\"WiFiAwareDataSession\"16q24"
- "v32@0:8@\"WiFiAwarePublisher\"16@\"NSData\"24"
- "v32@0:8@\"WiFiAwarePublisher\"16q24"
- "v32@0:8@\"WiFiAwareSubscriber\"16@\"WiFiAwareDiscoveryResult\"24"
- "v32@0:8@\"WiFiAwareSubscriber\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16q24"
- "v32@0:8B16B20@24"
- "v36@0:8@\"MIBUNANPublisher\"16@\"NSError\"24B32"
- "v36@0:8@\"MIBUNANPublisher\"16@\"NSString\"24B32"
- "v36@0:8@\"MIBUNANSubscriber\"16@\"NSError\"24B32"
- "v36@0:8@\"WiFiAwareSubscriber\"16C24@\"WiFiMACAddress\"28"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24^B28"
- "v36@0:8@16C24@28"
- "v40@0:8@\"MIBUMulticastSocket\"16@\"NSMutableArray\"24@\"NSDate\"32"
- "v40@0:8@\"MIBUNANPublisher\"16@\"NSData\"24@\"NSString\"32"
- "v40@0:8@\"MIBUNANPublisher\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@\"MIBUNWClientDevice\"16@\"NSError\"24@\"NSDictionary\"32"
- "v40@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32"
- "v40@0:8@\"WiFiAwarePublisher\"16@\"NSData\"24@\"WiFiMACAddress\"32"
- "v40@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublisherDataSessionHandle\"24q32"
- "v40@0:8@\"WiFiAwarePublisher\"16q24@\"WiFiMACAddress\"32"
- "v40@0:8@\"WiFiAwareSubscriber\"16@\"NSData\"24@\"WiFiMACAddress\"32"
- "v40@0:8@\"WiFiAwareSubscriber\"16q24@\"WiFiMACAddress\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24q32"
- "v40@0:8@16@?24@32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16q24@32"
- "v40@0:8Q16@?24@32"
- "v40@0:8Q16@?<v@?BB@\"NSArray\">24@\"NSObject<OS_dispatch_queue>\"32"
- "v44@0:8@\"MIBUNANSubscriber\"16@\"NSString\"24@\"NSString\"32B40"
- "v44@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32I40"
- "v44@0:8@\"WiFiAwarePublisher\"16@\"NSData\"24C32@\"WiFiMACAddress\"36"
- "v44@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublisherDataSessionHandle\"24I32@\"WiFiAwarePublishDatapathServiceSpecificInfo\"36"
- "v44@0:8@\"WiFiAwareSubscriber\"16@\"NSData\"24C32@\"WiFiMACAddress\"36"
- "v44@0:8@16@24@32B40"
- "v44@0:8@16@24@32I40"
- "v44@0:8@16@24C32@36"
- "v44@0:8@16@24I32@36"
- "v48@0:8@\"NSMutableArray\"16@\"NSDate\"24@?<v@?QB>32@\"NSObject<OS_dispatch_queue>\"40"
- "v48@0:8@16@24@?32@40"
- "v48@0:8@16^@24^Q32^Q40"
- "v52@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublisherDataSessionHandle\"24I32@\"WiFiAwarePublishDatapathServiceSpecificInfo\"36@\"NSUUID\"44"
- "v52@0:8@16@24I32@36@44"
- "v56@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32@\"NSUUID\"40Q48"
- "v56@0:8@16@24@32@40Q48"
- "v56@0:8@16Q24Q32@40@?48"
- "v60@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublisherDataSessionHandle\"24I32@\"WiFiAwarePublishDatapathServiceSpecificInfo\"36@\"NSUUID\"44Q52"
- "v60@0:8@16@24I32@36@44Q52"
- "valueWithRange:"
- "waitUntilDate:"
- "writeData:"
- "writeData:error:"
- "writeToFile:options:error:"
- "writeToURL:options:error:"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
