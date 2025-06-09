## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`

```diff

-63.120.35.0.0
-  __TEXT.__text: 0x2a1a0
-  __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_methlist: 0x1438
-  __TEXT.__const: 0x48f8
-  __TEXT.__cstring: 0xd57
-  __TEXT.__oslogstring: 0x3113
-  __TEXT.__gcc_except_tab: 0x618
-  __TEXT.__unwind_info: 0xbe0
-  __TEXT.__objc_classname: 0x2fb
-  __TEXT.__objc_methname: 0x32c9
-  __TEXT.__objc_methtype: 0x131b
-  __TEXT.__objc_stubs: 0x2600
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x798
-  __DATA_CONST.__objc_classlist: 0x90
+132.0.0.0.0
+  __TEXT.__text: 0x2ce94
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__objc_methlist: 0x1550
+  __TEXT.__const: 0x4908
+  __TEXT.__cstring: 0xdbb
+  __TEXT.__oslogstring: 0x367a
+  __TEXT.__gcc_except_tab: 0x654
+  __TEXT.__unwind_info: 0xc98
+  __TEXT.__objc_classname: 0x31a
+  __TEXT.__objc_methname: 0x3655
+  __TEXT.__objc_methtype: 0x159a
+  __TEXT.__objc_stubs: 0x28c0
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x818
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc10
+  __DATA_CONST.__objc_selrefs: 0xcc0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x638
-  __AUTH_CONST.__const: 0x1f60
-  __AUTH_CONST.__cfstring: 0x900
-  __AUTH_CONST.__objc_const: 0x4750
+  __DATA_CONST.__objc_superrefs: 0x98
+  __AUTH_CONST.__auth_got: 0x650
+  __AUTH_CONST.__const: 0x2240
+  __AUTH_CONST.__cfstring: 0x940
+  __AUTH_CONST.__objc_const: 0x4928
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x24c
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x268
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x30
   __DATA.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31795163-20B5-3039-AF22-F6E531490DED
-  Functions: 1169
-  Symbols:   4111
-  CStrings:  1214
+  UUID: EE704DDA-3A47-351D-AA53-0DCD93D983C4
+  Functions: 1243
+  Symbols:   4370
+  CStrings:  1280
 
Symbols:
+ -[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]
+ -[MIBUNANSubscriber _getRSSIofNAN:]
+ -[MIBUNANSubscriber _getRSSIofNAN:].cold.1
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.1
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.2
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.3
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.4
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.5
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.6
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.7
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.8
+ -[MIBUNWClientController _checkOutWithError:].cold.1
+ -[MIBUNWClientController _checkOutWithError:].cold.2
+ -[MIBUNWClientController _receivedVeryFirstPacketArray].cold.1
+ -[MIBUNWClientController nanSubscriberDidTerminateDataSession:]
+ -[MIBUNWClientController serverDeviceDidCheckOut:]
+ -[MIBUNWClientController serverDeviceDidCheckOut:].cold.1
+ -[MIBUNWClientController serverDeviceDidConnect:]
+ -[MIBUNWClientController serverDeviceDidConnect:].cold.1
+ -[MIBUNWClientDevice _checkOutAck]
+ -[MIBUNWClientDevice unicastConnectionDidClose:withError:]
+ -[MIBUNWClientDevice unicastConnectionDidClose:withError:].cold.1
+ -[MIBUNWClientDevice unicastConnectionDidOpen:]
+ -[MIBUNWClientDevice unicastConnectionDidOpen:].cold.1
+ -[MIBUNWConnection _cancelTimerForWaitingState]
+ -[MIBUNWConnection _setupTimerForWaitingState]
+ -[MIBUNWDevice _sendOutgoingMessage:synchronous:shouldWait:]
+ -[MIBUNWDevice _sendOutgoingMessage:synchronous:shouldWait:].cold.1
+ -[MIBUNWServerController clientDeviceDidConnect:]
+ -[MIBUNWServerController clientDeviceDidDisconnect:]
+ -[MIBUNWServerDevice _handleIncomingMessage:].cold.2
+ -[MIBUNWServerDevice _processPendingMessages:]
+ -[MIBUNWServerDevice _processPendingMessages:].cold.1
+ -[MIBUNWServerDevice unicastConnectionDidClose:withError:]
+ -[MIBUNWServerDevice unicastConnectionDidClose:withError:].cold.1
+ -[MIBUNWServerDevice unicastConnectionDidOpen:]
+ -[MIBUNWServerDevice unicastConnectionDidOpen:].cold.1
+ -[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:].cold.4
+ -[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:].cold.5
+ -[SKRaptorQDecoder initWithBasicParameters:extendedParameters:repairFactor:threshold:outputURL:error:]
+ -[SKRaptorQDecoder initWithBasicParameters:extendedParameters:repairFactor:threshold:outputURL:error:].cold.1
+ -[SKRaptorQDecoder initWithBasicParameters:extendedParameters:repairFactor:threshold:outputURL:error:].cold.2
+ -[SKRaptorQDecoder initWithBasicParameters:extendedParameters:repairFactor:threshold:outputURL:error:].cold.3
+ -[SKRaptorQEncoder _writeSBN:rq:repairFactor:inputIO:outputFile:error:].cold.2
+ -[SKRaptorQEncoder _writeSBN:rq:repairFactor:inputIO:outputFile:error:].cold.3
+ -[_SKRaptorQRReceptionDetails init]
+ -[_SKRaptorQRReceptionDetails symbolsShouldHaveReceived:]
+ -[_SKRaptorQRReceptionDetails symbolsShouldHaveReceived:].cold.1
+ -[_SKRaptorQRReceptionDetails updateWithESI:]
+ GCC_except_table16
+ GCC_except_table22
+ GCC_except_table31
+ GCC_except_table42
+ GCC_except_table51
+ GCC_except_table9
+ OBJC_IVAR_$_MIBUNWDevice._messages
+ _NSDefaultRunLoopMode
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_CLASS_$__SKRaptorQRReceptionDetails
+ _OBJC_IVAR_$_MIBUNANPublisher._dataSessionTimer
+ _OBJC_IVAR_$_MIBUNANSubscriber._dataCollector
+ _OBJC_IVAR_$_MIBUNWClientController._checkoutSem
+ _OBJC_IVAR_$_MIBUNWConnection._waitingTimer
+ _OBJC_IVAR_$_MIBUNWServerController._packetFetched
+ _OBJC_IVAR_$_SKRaptorQDecoder._receptionDetails
+ _OBJC_IVAR_$__SKRaptorQRReceptionDetails._firstESI
+ _OBJC_IVAR_$__SKRaptorQRReceptionDetails._largestESI
+ _OBJC_IVAR_$__SKRaptorQRReceptionDetails._lastESI
+ _OBJC_METACLASS_$__SKRaptorQRReceptionDetails
+ __OBJC_$_INSTANCE_METHODS__SKRaptorQRReceptionDetails
+ __OBJC_$_INSTANCE_VARIABLES__SKRaptorQRReceptionDetails
+ __OBJC_CLASS_RO_$__SKRaptorQRReceptionDetails
+ __OBJC_METACLASS_RO_$__SKRaptorQRReceptionDetails
+ ___102-[SKRaptorQDecoder initWithBasicParameters:extendedParameters:repairFactor:threshold:outputURL:error:]_block_invoke
+ ___102-[SKRaptorQDecoder initWithBasicParameters:extendedParameters:repairFactor:threshold:outputURL:error:]_block_invoke.29
+ ___102-[SKRaptorQDecoder initWithBasicParameters:extendedParameters:repairFactor:threshold:outputURL:error:]_block_invoke.29.cold.1
+ ___102-[SKRaptorQDecoder initWithBasicParameters:extendedParameters:repairFactor:threshold:outputURL:error:]_block_invoke.cold.1
+ ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke
+ ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.58
+ ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.58.cold.1
+ ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.62
+ ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.62.cold.1
+ ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.67
+ ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.67.cold.1
+ ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.cold.1
+ ___25-[MIBUNWConnection _open]_block_invoke.32
+ ___29-[MIBUNWDevice _sendMessage:]_block_invoke.8
+ ___29-[MIBUNWDevice _sendMessage:]_block_invoke.8.cold.1
+ ___29-[MIBUNWDevice _sendMessage:]_block_invoke.8.cold.2
+ ___34-[MIBUNWClientDevice _checkOutAck]_block_invoke
+ ___35-[MIBUNANSubscriber _getRSSIofNAN:]_block_invoke
+ ___35-[MIBUNANSubscriber _getRSSIofNAN:]_block_invoke.cold.1
+ ___37-[MIBUNANPublisher publisherStarted:]_block_invoke.132
+ ___37-[MIBUNANSubscriber _startSubscriber]_block_invoke.79
+ ___37-[MIBUNANSubscriber _startSubscriber]_block_invoke.79.cold.1
+ ___42-[MIBUNWClientController _disableFirewall]_block_invoke.133
+ ___42-[MIBUNWClientController _disableFirewall]_block_invoke.133.cold.1
+ ___45-[MIBUNWClientController _checkOutWithError:]_block_invoke
+ ___45-[MIBUNWClientController _checkOutWithError:]_block_invoke.cold.1
+ ___45-[MIBUNWServerDevice _handleIncomingMessage:]_block_invoke.39
+ ___45-[MIBUNWServerDevice _handleIncomingMessage:]_block_invoke.39.cold.1
+ ___46-[MIBUNANSubscriber _handleFailureDueToError:]_block_invoke.118
+ ___46-[MIBUNANSubscriber _handleFailureDueToError:]_block_invoke.118.cold.1
+ ___46-[MIBUNANSubscriber _handleFailureDueToError:]_block_invoke.121
+ ___46-[MIBUNANSubscriber _sendData:withCompletion:]_block_invoke.93
+ ___46-[MIBUNANSubscriber _sendData:withCompletion:]_block_invoke.93.cold.1
+ ___46-[MIBUNANSubscriber _sendData:withCompletion:]_block_invoke.93.cold.2
+ ___46-[MIBUNANSubscriber _stopSubscriberForReason:]_block_invoke.85
+ ___46-[MIBUNANSubscriber _stopSubscriberForReason:]_block_invoke.85.cold.1
+ ___46-[MIBUNWConnection _setupTimerForWaitingState]_block_invoke
+ ___46-[MIBUNWConnection _setupTimerForWaitingState]_block_invoke.cold.1
+ ___46-[MIBUNWConnection _setupTimerForWaitingState]_block_invoke_2
+ ___46-[MIBUNWConnection _setupTimerForWaitingState]_block_invoke_2.cold.1
+ ___46-[MIBUNWServerDevice _processPendingMessages:]_block_invoke
+ ___46-[MIBUNWServerDevice _processPendingMessages:]_block_invoke.cold.1
+ ___47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.84
+ ___47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.84.cold.1
+ ___47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.84.cold.2
+ ___47-[MIBUNWClientDevice unicastConnectionDidOpen:]_block_invoke
+ ___47-[MIBUNWClientDevice unicastConnectionDidOpen:]_block_invoke.cold.1
+ ___47-[MIBUNWServerDevice unicastConnectionDidOpen:]_block_invoke
+ ___47-[MIBUNWServerDevice unicastConnectionDidOpen:]_block_invoke.cold.1
+ ___48-[MIBUNWConnection _sendMessage:withCompletion:]_block_invoke.38
+ ___48-[MIBUNWDevice sendOutgoingMessage:synchronous:]_block_invoke
+ ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.71
+ ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.71.cold.1
+ ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.75
+ ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.75.cold.1
+ ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.78
+ ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.78.cold.1
+ ___49-[MIBUNWClientController serverDeviceDidConnect:]_block_invoke
+ ___49-[MIBUNWClientController serverDeviceDidConnect:]_block_invoke.cold.1
+ ___49-[MIBUNWConnection _scheduleNextMessageReception]_block_invoke.42
+ ___49-[MIBUNWConnection _scheduleNextMessageReception]_block_invoke.42.cold.1
+ ___49-[MIBUNWConnection _scheduleNextMessageReception]_block_invoke.42.cold.2
+ ___49-[MIBUNWConnection _scheduleNextMessageReception]_block_invoke.42.cold.3
+ ___49-[MIBUNWConnection _scheduleNextMessageReception]_block_invoke.45
+ ___49-[MIBUNWConnection _scheduleNextMessageReception]_block_invoke.45.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.141
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.141.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.146
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.146.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke
+ ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke.127
+ ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke.127.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke.cold.2
+ ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke_2
+ ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke_2.cold.1
+ ___50-[MIBUNWClientController serverDeviceDidCheckOut:]_block_invoke
+ ___50-[MIBUNWClientController serverDeviceDidCheckOut:]_block_invoke.cold.1
+ ___51-[MIBUNANPublisher publisher:terminatedWithReason:]_block_invoke.141
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.68
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.68.cold.1
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.71
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.71.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.132
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.132.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.135
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.135.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.135.cold.2
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.cold.2
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke_2
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke_2.136
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke_2.136.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke_2.cold.1
+ ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.60
+ ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.60.cold.1
+ ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.63
+ ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.63.cold.1
+ ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.66
+ ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.66.cold.1
+ ___53-[MIBUNANPublisher publisher:failedToStartWithError:]_block_invoke.135
+ ___53-[MIBUNANSubscriber subscriber:terminatedWithReason:]_block_invoke.132
+ ___54-[MIBUNANSubscriber dataSession:terminatedWithReason:]_block_invoke.156
+ ___54-[MIBUNANSubscriber dataSession:terminatedWithReason:]_block_invoke.156.cold.1
+ ___55-[MIBUNANSubscriber subscriber:failedToStartWithError:]_block_invoke.126
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.125
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.125.cold.1
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.125.cold.2
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.cold.1
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.126
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.126.cold.1
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.cold.1
+ ___56-[MIBUNANSubscriber dataSession:failedToStartWithError:]_block_invoke.150
+ ___56-[MIBUNANSubscriber subscriber:receivedDiscoveryResult:]_block_invoke.140
+ ___56-[MIBUNWConnection _getRemoteIPv6AddressFromConnection:]_block_invoke.60
+ ___56-[MIBUNWConnection _getRemoteIPv6AddressFromConnection:]_block_invoke.60.cold.1
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.107
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.107.cold.1
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.107.cold.2
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.110
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.110.cold.1
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.113
+ ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.61
+ ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.61.cold.1
+ ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.64
+ ___57-[_SKRaptorQRReceptionDetails symbolsShouldHaveReceived:]_block_invoke
+ ___57-[_SKRaptorQRReceptionDetails symbolsShouldHaveReceived:]_block_invoke.cold.1
+ ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.27
+ ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.27.cold.1
+ ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.30
+ ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.30.cold.1
+ ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.9
+ ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.9.cold.1
+ ___58-[MIBUNWClientDevice unicastConnectionDidClose:withError:]_block_invoke
+ ___58-[MIBUNWClientDevice unicastConnectionDidClose:withError:]_block_invoke.cold.1
+ ___58-[MIBUNWServerDevice unicastConnectionDidClose:withError:]_block_invoke
+ ___58-[MIBUNWServerDevice unicastConnectionDidClose:withError:]_block_invoke.cold.1
+ ___59-[MIBUNANSubscriber _createDataSessionWithDiscoveryResult:]_block_invoke.109
+ ___59-[MIBUNANSubscriber _createDataSessionWithDiscoveryResult:]_block_invoke.109.cold.1
+ ___60-[MIBUNWDevice _sendOutgoingMessage:synchronous:shouldWait:]_block_invoke
+ ___60-[MIBUNWDevice _sendOutgoingMessage:synchronous:shouldWait:]_block_invoke.cold.1
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.163
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.163.cold.1
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.163.cold.2
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.163.cold.3
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.166
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.166.cold.1
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.169
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.34
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.34.cold.1
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.37
+ ___61-[MIBURaptorQPacketProvider _provideOnePacketWithCompletion:]_block_invoke.37.cold.1
+ ___63-[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]_block_invoke.127
+ ___63-[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]_block_invoke.127.cold.1
+ ___63-[MIBUNWClientController nanSubscriberDidTerminateDataSession:]_block_invoke
+ ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.120
+ ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.120.cold.1
+ ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.52
+ ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.52.cold.1
+ ___71-[SKRaptorQEncoder _writeSBN:rq:repairFactor:inputIO:outputFile:error:]_block_invoke.108
+ ___71-[SKRaptorQEncoder _writeSBN:rq:repairFactor:inputIO:outputFile:error:]_block_invoke.108.cold.1
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.153
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.153.cold.1
+ ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.174
+ ___77-[MIBUNANSubscriber subscriber:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.145
+ ___81-[MIBUNANSubscriber dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:]_block_invoke.164
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.149
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.149.cold.1
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.149.cold.2
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.149.cold.3
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.152
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.152.cold.1
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.157
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke_2.159
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSTimer"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e34_v32?0"NSMutableIndexSet"8Q16^B24ls32l8r40l8r48l8
+ ___block_descriptor_57_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e17_v16?0"NSError"8lr48l8s32l8r56l8s40l8
+ ___block_literal_global.101
+ ___block_literal_global.108
+ ___block_literal_global.118
+ ___block_literal_global.123
+ ___block_literal_global.125
+ ___block_literal_global.142
+ ___block_literal_global.147
+ ___block_literal_global.148
+ ___block_literal_global.154
+ ___block_literal_global.158
+ ___block_literal_global.160
+ ___block_literal_global.162
+ ___block_literal_global.163
+ ___block_literal_global.165
+ ___block_literal_global.166
+ ___block_literal_global.168
+ ___block_literal_global.171
+ ___block_literal_global.173
+ ___block_literal_global.37
+ ___block_literal_global.41
+ ___block_literal_global.73
+ ___block_literal_global.94
+ _kMIBUSubscriberEventNanSubscriberDiscoveredResult
+ _nanorq_set_repair_factor
+ _nw_content_context_get_is_final
+ _objc_msgSend$_cancelTimerForWaitingState
+ _objc_msgSend$_checkOutAck
+ _objc_msgSend$_getRSSIofNAN:
+ _objc_msgSend$_handleNANDataSessionExpiredForPeer:
+ _objc_msgSend$_processPendingMessages:
+ _objc_msgSend$_sendOutgoingMessage:synchronous:shouldWait:
+ _objc_msgSend$_setupTimerForWaitingState
+ _objc_msgSend$addKeyEvent:additionalData:
+ _objc_msgSend$addTimer:forMode:
+ _objc_msgSend$clientDeviceDidConnect:
+ _objc_msgSend$clientDeviceDidDisconnect:
+ _objc_msgSend$currentRunLoop
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$initWithBasicParameters:extendedParameters:repairFactor:threshold:outputURL:error:
+ _objc_msgSend$initWithFireDate:interval:repeats:block:
+ _objc_msgSend$initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:
+ _objc_msgSend$nanSubscriberDidTerminateDataSession:
+ _objc_msgSend$rssi
+ _objc_msgSend$seekToOffset:error:
+ _objc_msgSend$serverDeviceDidCheckOut:
+ _objc_msgSend$serverDeviceDidConnect:
+ _objc_msgSend$symbolsShouldHaveReceived:
+ _objc_msgSend$unicastConnectionDidClose:withError:
+ _objc_msgSend$unicastConnectionDidOpen:
+ _objc_msgSend$updateWithESI:
+ _objc_retain_x10
+ _objc_retain_x6
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:]
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:].cold.1
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:].cold.2
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:].cold.3
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:].cold.4
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:].cold.5
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:].cold.6
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:].cold.7
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:].cold.8
- -[MIBUNWClientController serverDeviceDidBecomeReady:]
- -[MIBUNWClientController serverDeviceDidBecomeReady:].cold.1
- -[MIBUNWClientDevice unicastConnection:didEnterNewState:]
- -[MIBUNWServerDevice unicastConnection:didEnterNewState:]
- -[MIBUNWServerDevice unicastConnection:didEnterNewState:].cold.1
- -[MIBUNWServerDevice unicastConnectionDidStart:]
- -[MIBUNWServerDevice unicastConnectionDidStop:withError:]
- -[SKRaptorQDecoder initWithBasicParameters:extendedParameters:threshold:outputURL:error:]
- -[SKRaptorQDecoder initWithBasicParameters:extendedParameters:threshold:outputURL:error:].cold.1
- -[SKRaptorQDecoder initWithBasicParameters:extendedParameters:threshold:outputURL:error:].cold.2
- -[SKRaptorQDecoder initWithBasicParameters:extendedParameters:threshold:outputURL:error:].cold.3
- GCC_except_table12
- GCC_except_table27
- GCC_except_table40
- OBJC_IVAR_$_MIBUNWDevice._message
- _OBJC_IVAR_$_MIBUNWServerController._packetInFlight
- _OBJC_IVAR_$_SKRaptorQDecoder._lastTag
- ___140-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:]_block_invoke
- ___140-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:]_block_invoke.56
- ___140-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:]_block_invoke.56.cold.1
- ___140-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:]_block_invoke.60
- ___140-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:]_block_invoke.60.cold.1
- ___140-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:]_block_invoke.65
- ___140-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:]_block_invoke.65.cold.1
- ___140-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:]_block_invoke.cold.1
- ___25-[MIBUNWConnection _open]_block_invoke.30
- ___29-[MIBUNWDevice _sendMessage:]_block_invoke.6
- ___29-[MIBUNWDevice _sendMessage:]_block_invoke.6.cold.1
- ___29-[MIBUNWDevice _sendMessage:]_block_invoke.6.cold.2
- ___37-[MIBUNANPublisher publisherStarted:]_block_invoke.125
- ___37-[MIBUNANSubscriber _startSubscriber]_block_invoke.75
- ___37-[MIBUNANSubscriber _startSubscriber]_block_invoke.75.cold.1
- ___42-[MIBUNWClientController _disableFirewall]_block_invoke.131
- ___42-[MIBUNWClientController _disableFirewall]_block_invoke.131.cold.1
- ___46-[MIBUNANSubscriber _handleFailureDueToError:]_block_invoke.107
- ___46-[MIBUNANSubscriber _handleFailureDueToError:]_block_invoke.107.cold.1
- ___46-[MIBUNANSubscriber _handleFailureDueToError:]_block_invoke.110
- ___46-[MIBUNANSubscriber _sendData:withCompletion:]_block_invoke.89
- ___46-[MIBUNANSubscriber _sendData:withCompletion:]_block_invoke.89.cold.1
- ___46-[MIBUNANSubscriber _sendData:withCompletion:]_block_invoke.89.cold.2
- ___46-[MIBUNANSubscriber _stopSubscriberForReason:]_block_invoke.81
- ___46-[MIBUNANSubscriber _stopSubscriberForReason:]_block_invoke.81.cold.1
- ___47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.82
- ___47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.82.cold.1
- ___47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.82.cold.2
- ___48-[MIBUNWConnection _sendMessage:withCompletion:]_block_invoke.36
- ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.57
- ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.57.cold.1
- ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.61
- ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.61.cold.1
- ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.64
- ___48-[SKRaptorQDecoder decodeBlock:error:discarded:]_block_invoke.64.cold.1
- ___49-[MIBUNWConnection _scheduleNextMessageReception]_block_invoke.40
- ___49-[MIBUNWConnection _scheduleNextMessageReception]_block_invoke.40.cold.1
- ___49-[MIBUNWConnection _scheduleNextMessageReception]_block_invoke.40.cold.2
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.127
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.127.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.132
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.132.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.135
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.135.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.135.cold.2
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke_2.136
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke_2.136.cold.1
- ___51-[MIBUNANPublisher publisher:terminatedWithReason:]_block_invoke.134
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.66
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.66.cold.1
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.69
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.69.cold.1
- ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.46
- ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.46.cold.1
- ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.49
- ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.49.cold.1
- ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.52
- ___52-[SKRaptorQDecoder decodeAllSourceBlocks:discarded:]_block_invoke.52.cold.1
- ___53-[MIBUNANPublisher publisher:failedToStartWithError:]_block_invoke.128
- ___53-[MIBUNANSubscriber subscriber:terminatedWithReason:]_block_invoke.121
- ___53-[MIBUNWClientController serverDeviceDidBecomeReady:]_block_invoke
- ___53-[MIBUNWClientController serverDeviceDidBecomeReady:]_block_invoke.cold.1
- ___54-[MIBUNANSubscriber dataSession:terminatedWithReason:]_block_invoke.145
- ___54-[MIBUNANSubscriber dataSession:terminatedWithReason:]_block_invoke.145.cold.1
- ___55-[MIBUNANSubscriber subscriber:failedToStartWithError:]_block_invoke.115
- ___55-[MIBUNWClientController _receivedVeryFirstPacketArray]_block_invoke_2
- ___55-[MIBUNWClientController _receivedVeryFirstPacketArray]_block_invoke_2.cold.1
- ___56-[MIBUNANSubscriber dataSession:failedToStartWithError:]_block_invoke.139
- ___56-[MIBUNANSubscriber subscriber:receivedDiscoveryResult:]_block_invoke.129
- ___56-[MIBUNWConnection _getRemoteIPv6AddressFromConnection:]_block_invoke.51
- ___56-[MIBUNWConnection _getRemoteIPv6AddressFromConnection:]_block_invoke.51.cold.1
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.105
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.105.cold.1
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.105.cold.2
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.108
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.108.cold.1
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.111
- ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.59
- ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.59.cold.1
- ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.62
- ___57-[MIBUNWServerDevice unicastConnection:didEnterNewState:]_block_invoke
- ___57-[MIBUNWServerDevice unicastConnection:didEnterNewState:]_block_invoke.cold.1
- ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.22
- ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.22.cold.1
- ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.25
- ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.25.cold.1
- ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.4
- ___58-[MIBUNWClientDevice unicastConnection:didReceiveMessage:]_block_invoke.4.cold.1
- ___59-[MIBUNANSubscriber _createDataSessionWithDiscoveryResult:]_block_invoke.98
- ___59-[MIBUNANSubscriber _createDataSessionWithDiscoveryResult:]_block_invoke.98.cold.1
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.147
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.147.cold.1
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.147.cold.2
- ___63-[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]_block_invoke.125
- ___63-[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]_block_invoke.125.cold.1
- ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.118
- ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.118.cold.1
- ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.50
- ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.50.cold.1
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.143
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.143.cold.1
- ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.154
- ___77-[MIBUNANSubscriber subscriber:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.134
- ___81-[MIBUNANSubscriber dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:]_block_invoke.153
- ___89-[SKRaptorQDecoder initWithBasicParameters:extendedParameters:threshold:outputURL:error:]_block_invoke
- ___89-[SKRaptorQDecoder initWithBasicParameters:extendedParameters:threshold:outputURL:error:]_block_invoke.16
- ___89-[SKRaptorQDecoder initWithBasicParameters:extendedParameters:threshold:outputURL:error:]_block_invoke.16.cold.1
- ___89-[SKRaptorQDecoder initWithBasicParameters:extendedParameters:threshold:outputURL:error:]_block_invoke.cold.1
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.142
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.142.cold.1
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.142.cold.2
- ___block_descriptor_53_e8_32r40r_e34_v32?0"NSMutableIndexSet"8Q16^B24lr32l8r40l8
- ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
- ___block_literal_global.100
- ___block_literal_global.103
- ___block_literal_global.107
- ___block_literal_global.127
- ___block_literal_global.133
- ___block_literal_global.136
- ___block_literal_global.152
- ___block_literal_global.153
- ___block_literal_global.46
- ___block_literal_global.52
- ___block_literal_global.53
- ___block_literal_global.6
- ___block_literal_global.85
- _load_symbol_matrix
- _objc_msgSend$initWithBasicParameters:extendedParameters:threshold:outputURL:error:
- _objc_msgSend$initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:
- _objc_msgSend$serverDeviceDidBecomeReady:
CStrings:
+ "\v("
+ "%{public}@: Connection timed out after staying in waiting state for %d seconds."
+ "%{public}@: Current data session count after confirmation: %lu"
+ "%{public}@: Current data session count after termination: %lu"
+ "%{public}@: Failed to terminate NAN data session with peer: %{public}@"
+ "%{public}@: Ignore unknown client message :%u"
+ "%{public}@: NAN subscriber got NAN RSSI: %ld"
+ "%{public}@: Receive message got connection closed."
+ "%{public}@: TCP device checked out: %{public}@"
+ "%{public}@: Timer fired to expunge NAN data session with peer: %{public}@"
+ "%{public}@: Unicast connection closed."
+ "%{public}@: Unicast connection opened."
+ "%{public}@: device checked in: %{public}@"
+ "%{public}@: device connected: %{public}@"
+ "'"
+ "@56@0:8Q16I24I28Q32@40^@48"
+ "@92@0:8@16@24@32@40Q48Q56Q64B72@76@84"
+ "Cannot send outgoing message because there is no connection and on-demand connection is not enabled."
+ "Device checkout timed out after %ds"
+ "Failed to seek to offset 0 for file handle %{public}@: %{public}@"
+ "Giving up pending message because on-demand connection cannot be set up."
+ "I24@0:8Q16"
+ "NAN data session failed to stop: %ld"
+ "NAN device connected: %{public}@"
+ "NAN device disconnected: %{public}@"
+ "NAN multicast session data send failed: %ld"
+ "Packets sent: %lu, dropped: %lu in last %ds; Effective bandwidth: %0.5f Mbps, Total packet fetched: %lu, Total packet in flight: %lu, Total packet dropped: %lu, Total packet sent: %lu"
+ "RSSIofNAN"
+ "Reached end of file for %{public}@, will start from beginning."
+ "Repair factor should not be 0"
+ "Repair factor should not be 0, given packet can get lost during transfer."
+ "SubscriberNanSubscriberDiscoveredResult"
+ "TCP device connected: %{public}@"
+ "TCP device disconnected: %{public}@"
+ "_SKRaptorQRReceptionDetails"
+ "_cancelTimerForWaitingState"
+ "_checkOutAck"
+ "_checkoutSem"
+ "_dataSessionTimer"
+ "_firstESI"
+ "_getRSSIofNAN:"
+ "_handleNANDataSessionExpiredForPeer:"
+ "_largestESI"
+ "_largestESI / symbolCount = %lf (%u / %lu), not close to an integer. Using a non-integer repair factor, or a lot of packets get lost while host sends packets with largest esi?"
+ "_lastESI"
+ "_messages"
+ "_packetFetched"
+ "_processPendingMessages:"
+ "_receptionDetails"
+ "_sendOutgoingMessage:synchronous:shouldWait:"
+ "_setupTimerForWaitingState"
+ "_waitingTimer"
+ "addKeyEvent:additionalData:"
+ "addTimer:forMode:"
+ "clientDeviceDidConnect:"
+ "clientDeviceDidDisconnect:"
+ "currentRunLoop"
+ "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:"
+ "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
+ "dateWithTimeIntervalSinceNow:"
+ "initWithBasicParameters:extendedParameters:repairFactor:threshold:outputURL:error:"
+ "initWithFireDate:interval:repeats:block:"
+ "initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:"
+ "nanSubscriberDidTerminateDataSession:"
+ "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:"
+ "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
+ "rssi"
+ "seekToOffset:error:"
+ "serverDeviceDidCheckOut:"
+ "serverDeviceDidConnect:"
+ "symbolsShouldHaveReceived:"
+ "updateWithESI:"
+ "v16@?0@\"NSTimer\"8"
+ "v36@0:8@16B24^B28"
+ "v48@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32@\"NSUUID\"40"
+ "v48@0:8@16@24@32@40"
+ "v52@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublisherDataSessionHandle\"24I32@\"WiFiAwarePublishDatapathServiceSpecificInfo\"36@\"NSUUID\"44"
+ "v52@0:8@16@24I32@36@44"
+ "v56@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32@\"NSUUID\"40Q48"
+ "v56@0:8@16@24@32@40Q48"
+ "v60@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublisherDataSessionHandle\"24I32@\"WiFiAwarePublishDatapathServiceSpecificInfo\"36@\"NSUUID\"44Q52"
+ "v60@0:8@16@24I32@36@44Q52"
- "\n("
- "$"
- "%{public}@: Device checked in: %{public}@"
- "%{public}@: New connection state: %lu"
- "%{public}@: device became ready: %{public}@"
- "6"
- "@\"MIBUNWMessage\""
- "@52@0:8Q16I24Q28@36^@44"
- "NAN data session failed to stop: %@"
- "NAN multicast session data send failed: %@"
- "Packets sent: %lu, dropped: %lu in last %ds; Effective bandwidth: %0.5f Mbps, Total packet dropped: %lu"
- "_lastTag"
- "_message"
- "_packetInFlight"
- "initWithBasicParameters:extendedParameters:threshold:outputURL:error:"
- "initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:"
- "serverDeviceDidBecomeReady:"
- "unicastConnectionDidStart:"
- "unicastConnectionDidStop:withError:"

```
