## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`

```diff

-176.100.32.0.0
-  __TEXT.__text: 0x36a18
+176.100.41.0.0
+  __TEXT.__text: 0x3801c
   __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x1620
-  __TEXT.__const: 0x4930
-  __TEXT.__cstring: 0xfd0
-  __TEXT.__oslogstring: 0x4d30
-  __TEXT.__gcc_except_tab: 0x884
-  __TEXT.__unwind_info: 0xe48
+  __TEXT.__objc_methlist: 0x1698
+  __TEXT.__const: 0x4940
+  __TEXT.__cstring: 0xfe8
+  __TEXT.__oslogstring: 0x4fcd
+  __TEXT.__gcc_except_tab: 0x940
+  __TEXT.__unwind_info: 0xe98
   __TEXT.__objc_classname: 0x332
-  __TEXT.__objc_methname: 0x3c2c
-  __TEXT.__objc_methtype: 0x159e
-  __TEXT.__objc_stubs: 0x2da0
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x908
+  __TEXT.__objc_methname: 0x3dfe
+  __TEXT.__objc_methtype: 0x15f7
+  __TEXT.__objc_stubs: 0x2f00
+  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__const: 0x950
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe20
+  __DATA_CONST.__objc_selrefs: 0xe80
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
   __AUTH_CONST.__auth_got: 0x620
-  __AUTH_CONST.__const: 0x2ec0
+  __AUTH_CONST.__const: 0x3040
   __AUTH_CONST.__cfstring: 0xae0
-  __AUTH_CONST.__objc_const: 0x4be8
+  __AUTH_CONST.__objc_const: 0x4cf0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x2a0
+  __DATA.__objc_ivar: 0x2b8
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x38
   __DATA.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9CFA762D-89D8-3C68-8B13-132FD9A8AF88
-  Functions: 1509
-  Symbols:   5339
-  CStrings:  1477
+  UUID: 0F2BDE74-4273-3A41-9381-842BFB6ED4A4
+  Functions: 1545
+  Symbols:   5467
+  CStrings:  1510
 
Symbols:
+ -[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]
+ -[MIBUNANPublisher _startMulticastPeerCleanUpTimer]
+ -[MIBUNANPublisher _startMulticastPeerCleanUpTimer].cold.1
+ -[MIBUNANPublisher _stopMulticastPeerCleanUpTimer]
+ -[MIBUNANPublisher _stopMulticastPeerCleanUpTimer].cold.1
+ -[MIBUNANPublisher _stopMulticastPeerCleanUpTimer].cold.2
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:].cold.1
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:].cold.2
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:].cold.3
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:].cold.4
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:].cold.5
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:].cold.6
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:].cold.7
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:].cold.8
+ -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:].cold.9
+ -[MIBUNANPublisher peerTimeout]
+ -[MIBUNANPublisher publisher:getKeysBlobForMulticastSession:]
+ -[MIBUNANPublisher publisher:getKeysBlobForMulticastSession:].cold.1
+ -[MIBUNANPublisher publisher:getKeysBlobForMulticastSession:].cold.2
+ -[MIBUNANPublisher setPeerTimeout:]
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:]
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:].cold.1
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:].cold.2
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:].cold.3
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:].cold.4
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:].cold.5
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:].cold.6
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:].cold.7
+ -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:].cold.8
+ -[MIBUNWClientController _activateProgressTimer]
+ -[MIBUNWClientController _activateProgressTimer].cold.1
+ -[MIBUNWClientController _deactivateProgressTimer]
+ -[MIBUNWClientController _deactivateProgressTimer].cold.1
+ -[MIBUNWClientController _handleProgressTimerTick]
+ -[MIBUNWClientController _handleProgressTimerTick].cold.1
+ -[MIBUNWClientController _stopMulticast]
+ -[MIBUNWClientController _stopMulticast].cold.1
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:].cold.1
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:].cold.10
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:].cold.2
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:].cold.3
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:].cold.4
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:].cold.5
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:].cold.6
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:].cold.7
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:].cold.8
+ -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:].cold.9
+ -[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:controllerDelegate:]
+ -[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:controllerDelegate:].cold.1
+ -[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:controllerDelegate:].cold.2
+ -[MIBUNWServerController nanPublisher:didGenerateSecurityKeys:]
+ -[MIBUNWServerController peerTimeout]
+ -[MIBUNWServerController setPeerTimeout:]
+ GCC_except_table72
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_IVAR_$_MIBUNANPublisher._multicastPeers
+ _OBJC_IVAR_$_MIBUNANPublisher._peerCleanUpTimer
+ _OBJC_IVAR_$_MIBUNANPublisher._peerLastContact
+ _OBJC_IVAR_$_MIBUNANPublisher._peerTimeout
+ _OBJC_IVAR_$_MIBUNWClientController._progressTimer
+ _OBJC_IVAR_$_MIBUNWServerController._multicastSecurity
+ _OBJC_IVAR_$_MIBUNWServerController._peerTimeout
+ _OBJC_IVAR_$_MIBUNWServerController._rateAdapter
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.59
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.59.cold.1
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.64
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.64.cold.1
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.69
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.69.cold.1
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.72
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.72.cold.1
+ ___140-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:]_block_invoke.cold.1
+ ___166-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:]_block_invoke
+ ___166-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:]_block_invoke.58
+ ___166-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:]_block_invoke.58.cold.1
+ ___166-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:]_block_invoke.62
+ ___166-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:]_block_invoke.62.cold.1
+ ___166-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:]_block_invoke.67
+ ___166-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:]_block_invoke.67.cold.1
+ ___166-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:]_block_invoke.cold.1
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.22
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.22.cold.1
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.25
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.25.cold.1
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.28
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.28.cold.1
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.32
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.32.cold.1
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.35
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.35.cold.1
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.39
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.39.cold.1
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.42
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.42.cold.1
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.46
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.46.cold.1
+ ___195-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:]_block_invoke.cold.1
+ ___201-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:controllerDelegate:]_block_invoke
+ ___201-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:controllerDelegate:]_block_invoke.5
+ ___201-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:controllerDelegate:]_block_invoke.5.cold.1
+ ___201-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:controllerDelegate:]_block_invoke.cold.1
+ ___35-[MIBUNANPublisher _startPublisher]_block_invoke.84
+ ___35-[MIBUNANPublisher _startPublisher]_block_invoke.84.cold.1
+ ___37-[MIBUNANPublisher publisherStarted:]_block_invoke.177
+ ___39-[MIBUNWClientController stopMulticast]_block_invoke.51
+ ___39-[MIBUNWClientController stopMulticast]_block_invoke.54
+ ___39-[MIBUNWClientController stopMulticast]_block_invoke.54.cold.1
+ ___40-[MIBUNWClientController _stopMulticast]_block_invoke
+ ___40-[MIBUNWClientController _stopMulticast]_block_invoke.cold.1
+ ___42-[MIBUNWClientController _disableFirewall]_block_invoke.177
+ ___42-[MIBUNWClientController _disableFirewall]_block_invoke.177.cold.1
+ ___42-[MIBUNWClientController _disableFirewall]_block_invoke.180
+ ___42-[MIBUNWClientController _disableFirewall]_block_invoke.180.cold.1
+ ___44-[MIBUNANPublisher _stopPublisherForReason:]_block_invoke.90
+ ___44-[MIBUNANPublisher _stopPublisherForReason:]_block_invoke.90.cold.1
+ ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.141
+ ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.141.cold.1
+ ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.144
+ ___47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.59
+ ___48-[MIBUNWClientController _activateProgressTimer]_block_invoke
+ ___48-[MIBUNWClientController _activateProgressTimer]_block_invoke.98
+ ___48-[MIBUNWClientController _activateProgressTimer]_block_invoke.cold.1
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.120
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.120.cold.1
+ ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.120.cold.2
+ ___48-[MIBUNWClientController _stopMulticastReceiver]_block_invoke.93
+ ___48-[MIBUNWClientController _stopMulticastReceiver]_block_invoke.93.cold.1
+ ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.130
+ ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.130.cold.1
+ ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.130.cold.2
+ ___50-[MIBUNANPublisher _stopMulticastPeerCleanUpTimer]_block_invoke
+ ___50-[MIBUNANPublisher _stopMulticastPeerCleanUpTimer]_block_invoke.161
+ ___50-[MIBUNANPublisher _stopMulticastPeerCleanUpTimer]_block_invoke.161.cold.1
+ ___50-[MIBUNANPublisher _stopMulticastPeerCleanUpTimer]_block_invoke.164
+ ___50-[MIBUNANPublisher _stopMulticastPeerCleanUpTimer]_block_invoke.cold.1
+ ___50-[MIBUNWClientController _deactivateProgressTimer]_block_invoke
+ ___50-[MIBUNWClientController _deactivateProgressTimer]_block_invoke.cold.1
+ ___50-[MIBUNWClientController _handleProgressTimerTick]_block_invoke
+ ___50-[MIBUNWClientController _handleProgressTimerTick]_block_invoke.cold.1
+ ___51-[MIBUNANPublisher _startMulticastPeerCleanUpTimer]_block_invoke
+ ___51-[MIBUNANPublisher _startMulticastPeerCleanUpTimer]_block_invoke.156
+ ___51-[MIBUNANPublisher _startMulticastPeerCleanUpTimer]_block_invoke.cold.1
+ ___51-[MIBUNANPublisher _startMulticastPeerCleanUpTimer]_block_invoke_2
+ ___51-[MIBUNANPublisher publisher:terminatedWithReason:]_block_invoke.186
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.104
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.104.cold.1
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.107
+ ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.107.cold.1
+ ___53-[MIBUNANPublisher publisher:failedToStartWithError:]_block_invoke.180
+ ___55-[MIBUNWClientController _receivedVeryFirstPacketArray]_block_invoke.137
+ ___55-[MIBUNWClientController _receivedVeryFirstPacketArray]_block_invoke.137.cold.1
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.147
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.147.cold.1
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.147.cold.2
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.148
+ ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.148.cold.1
+ ___57-[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]_block_invoke
+ ___57-[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]_block_invoke.168
+ ___57-[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]_block_invoke.168.cold.1
+ ___57-[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]_block_invoke.171
+ ___57-[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]_block_invoke.cold.1
+ ___57-[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]_block_invoke.cold.2
+ ___57-[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]_block_invoke_2
+ ___57-[MIBUNANPublisher _handleMulticastPeerCleanUpTimerFired]_block_invoke_2.cold.1
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.152
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.152.cold.1
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.155
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.155.cold.1
+ ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.158
+ ___59-[MIBUNWClientController multicastSocketDidStop:withError:]_block_invoke.195
+ ___59-[MIBUNWClientController multicastSocketDidStop:withError:]_block_invoke.195.cold.1
+ ___59-[MIBUNWClientController multicastSocketDidStop:withError:]_block_invoke.198
+ ___59-[MIBUNWClientController multicastSocketDidStop:withError:]_block_invoke.198.cold.1
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.128
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.128.cold.1
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.131
+ ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.131.cold.1
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.206
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.206.cold.1
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.206.cold.2
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.206.cold.3
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.209
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.209.cold.1
+ ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.212
+ ___61-[MIBUNANPublisher publisher:getKeysBlobForMulticastSession:]_block_invoke
+ ___61-[MIBUNANPublisher publisher:getKeysBlobForMulticastSession:]_block_invoke.223
+ ___61-[MIBUNANPublisher publisher:getKeysBlobForMulticastSession:]_block_invoke.223.cold.1
+ ___61-[MIBUNANPublisher publisher:getKeysBlobForMulticastSession:]_block_invoke.cold.1
+ ___63-[MIBUNWClientController nanSubscriberDidTerminateDataSession:]_block_invoke.209
+ ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.166
+ ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.166.cold.1
+ ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.169
+ ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.169.cold.1
+ ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.85
+ ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.85.cold.1
+ ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.88
+ ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.88.cold.1
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.104
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.104.cold.1
+ ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.104.cold.2
+ ___67-[MIBUNWClientController nanSubscriberDidStop:withError:willRetry:]_block_invoke.206
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.119
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.119.cold.1
+ ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.119.cold.2
+ ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.217
+ ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.217.cold.1
+ ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke_2
+ ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke_2.cold.1
+ ___90-[MIBUNWClientController nanSubscriberDidStart:withPeerIPAddress:usingInterface:forRetry:]_block_invoke.203
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.194
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.194.cold.1
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.194.cold.2
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.194.cold.3
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.194.cold.4
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.197
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.197.cold.1
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.200
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke_2.201
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke_3
+ ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke_3.cold.1
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSTimer"8lw32l8
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSTimer"8lw40l8s32l8
+ ___block_literal_global.113
+ ___block_literal_global.119
+ ___block_literal_global.127
+ ___block_literal_global.130
+ ___block_literal_global.133
+ ___block_literal_global.136
+ ___block_literal_global.143
+ ___block_literal_global.146
+ ___block_literal_global.170
+ ___block_literal_global.173
+ ___block_literal_global.176
+ ___block_literal_global.191
+ ___block_literal_global.194
+ ___block_literal_global.197
+ ___block_literal_global.200
+ ___block_literal_global.203
+ ___block_literal_global.213
+ ___block_literal_global.216
+ ___block_literal_global.222
+ ___block_literal_global.225
+ ___block_literal_global.61
+ ___block_literal_global.67
+ ___block_literal_global.97
+ _objc_msgSend$_activateProgressTimer
+ _objc_msgSend$_deactivateProgressTimer
+ _objc_msgSend$_handleMulticastPeerCleanUpTimerFired
+ _objc_msgSend$_handleProgressTimerTick
+ _objc_msgSend$_startMulticastPeerCleanUpTimer
+ _objc_msgSend$_stopMulticastPeerCleanUpTimer
+ _objc_msgSend$configuration
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$earlierDate:
+ _objc_msgSend$initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:
+ _objc_msgSend$initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:
+ _objc_msgSend$multicastConfiguration
+ _objc_msgSend$nanPublisher:didGenerateSecurityKeys:
+ _objc_msgSend$serverController:didReceiveMulticastSecurityKeys:
+ _objc_msgSend$setKeyBlob:
+ _objc_msgSend$setKeyExchangeOverMedium:
+ _objc_msgSend$setPeerTimeout:
+ _os_variant_has_internal_content
- -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]
- -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.1
- -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.2
- -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.3
- -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.4
- -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.5
- -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.6
- -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.7
- -[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:].cold.8
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.1
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.2
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.3
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.4
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.5
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.6
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.7
- -[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:].cold.8
- -[MIBUNWClientController _activateReceiveTimer]
- -[MIBUNWClientController _activateReceiveTimer].cold.1
- -[MIBUNWClientController _handleReceiveTimerTick]
- -[MIBUNWClientController _handleReceiveTimerTick].cold.1
- -[MIBUNWClientController _resetReceiveTimerWithInterval:]
- -[MIBUNWClientController _resetReceiveTimerWithInterval:].cold.1
- -[MIBUNWClientController _resetReceiveTimerWithInterval:].cold.2
- -[MIBUNWClientController _stopMulticast:]
- -[MIBUNWClientController _stopMulticast:].cold.1
- -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]
- -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.1
- -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.2
- -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.3
- -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.4
- -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.5
- -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.6
- -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.7
- -[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:].cold.8
- -[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]
- -[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:].cold.1
- -[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:].cold.2
- _OBJC_IVAR_$_MIBUNWClientController._receiveTimer
- _OBJC_IVAR_$_MIBUNWServerController._enableRA
- ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke
- ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.57
- ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.57.cold.1
- ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.62
- ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.62.cold.1
- ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.67
- ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.67.cold.1
- ___128-[MIBUNANPublisher initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:]_block_invoke.cold.1
- ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke
- ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.58
- ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.58.cold.1
- ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.62
- ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.62.cold.1
- ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.67
- ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.67.cold.1
- ___154-[MIBUNANSubscriber initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:]_block_invoke.cold.1
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.22
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.22.cold.1
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.25
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.25.cold.1
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.28
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.28.cold.1
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.32
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.32.cold.1
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.35
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.35.cold.1
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.39
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.39.cold.1
- ___183-[MIBUNWClientController initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:]_block_invoke.cold.1
- ___189-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]_block_invoke
- ___189-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]_block_invoke.5
- ___189-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]_block_invoke.5.cold.1
- ___189-[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:]_block_invoke.cold.1
- ___35-[MIBUNANPublisher _startPublisher]_block_invoke.78
- ___35-[MIBUNANPublisher _startPublisher]_block_invoke.78.cold.1
- ___37-[MIBUNANPublisher publisherStarted:]_block_invoke.149
- ___39-[MIBUNWClientController stopMulticast]_block_invoke.44
- ___39-[MIBUNWClientController stopMulticast]_block_invoke.47
- ___39-[MIBUNWClientController stopMulticast]_block_invoke.47.cold.1
- ___41-[MIBUNWClientController _stopMulticast:]_block_invoke
- ___41-[MIBUNWClientController _stopMulticast:]_block_invoke.cold.1
- ___42-[MIBUNWClientController _disableFirewall]_block_invoke.173
- ___42-[MIBUNWClientController _disableFirewall]_block_invoke.173.cold.1
- ___42-[MIBUNWClientController _disableFirewall]_block_invoke.176
- ___42-[MIBUNWClientController _disableFirewall]_block_invoke.176.cold.1
- ___44-[MIBUNANPublisher _stopPublisherForReason:]_block_invoke.84
- ___44-[MIBUNANPublisher _stopPublisherForReason:]_block_invoke.84.cold.1
- ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.135
- ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.135.cold.1
- ___45-[MIBUNANPublisher _handleFailureDueToError:]_block_invoke.138
- ___47-[MIBUNWClientController _activateReceiveTimer]_block_invoke
- ___47-[MIBUNWClientController _activateReceiveTimer]_block_invoke.cold.1
- ___47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.52
- ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.116
- ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.116.cold.1
- ___48-[MIBUNWClientController _pingThroughMulticast:]_block_invoke.116.cold.2
- ___48-[MIBUNWClientController _stopMulticastReceiver]_block_invoke.86
- ___48-[MIBUNWClientController _stopMulticastReceiver]_block_invoke.86.cold.1
- ___49-[MIBUNWClientController _handleReceiveTimerTick]_block_invoke
- ___49-[MIBUNWClientController _handleReceiveTimerTick]_block_invoke.cold.1
- ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.124
- ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.124.cold.1
- ___50-[MIBUNANPublisher _multicastData:withCompletion:]_block_invoke.124.cold.2
- ___51-[MIBUNANPublisher publisher:terminatedWithReason:]_block_invoke.158
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.100
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.100.cold.1
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.103
- ___51-[MIBUNWClientController _updateControllerProgress]_block_invoke.103.cold.1
- ___53-[MIBUNANPublisher publisher:failedToStartWithError:]_block_invoke.152
- ___55-[MIBUNWClientController _receivedVeryFirstPacketArray]_block_invoke.133
- ___55-[MIBUNWClientController _receivedVeryFirstPacketArray]_block_invoke.133.cold.1
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.141
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.141.cold.1
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke.141.cold.2
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.142
- ___56-[MIBUNANPublisher _handleNANDataSessionExpiredForPeer:]_block_invoke_2.142.cold.1
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.148
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.148.cold.1
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.151
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.151.cold.1
- ___57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.154
- ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke
- ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.93
- ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.93.cold.1
- ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.96
- ___57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.cold.1
- ___59-[MIBUNWClientController multicastSocketDidStop:withError:]_block_invoke.191
- ___59-[MIBUNWClientController multicastSocketDidStop:withError:]_block_invoke.191.cold.1
- ___59-[MIBUNWClientController multicastSocketDidStop:withError:]_block_invoke.194
- ___59-[MIBUNWClientController multicastSocketDidStop:withError:]_block_invoke.194.cold.1
- ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.124
- ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.124.cold.1
- ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.127
- ___60-[MIBUNWClientController _handleInboundPackets:arrivalTime:]_block_invoke.127.cold.1
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.180
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.180.cold.1
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.180.cold.2
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.180.cold.3
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.183
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.183.cold.1
- ___61-[MIBUNANPublisher publisher:dataTerminatedForHandle:reason:]_block_invoke.186
- ___63-[MIBUNWClientController nanSubscriberDidTerminateDataSession:]_block_invoke.205
- ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.162
- ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.162.cold.1
- ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.165
- ___64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.165.cold.1
- ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.78
- ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.78.cold.1
- ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.81
- ___64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.81.cold.1
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.92
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.92.cold.1
- ___65-[MIBUNANPublisher _terminateDataSessionWithPeer:withCompletion:]_block_invoke.98.cold.2
- ___67-[MIBUNWClientController nanSubscriberDidStop:withError:willRetry:]_block_invoke.202
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.107
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.107.cold.1
- ___70-[MIBUNANPublisher _terminateMulticastSessionWithPeer:withCompletion:]_block_invoke.113.cold.2
- ___75-[MIBUNANPublisher publisher:receivedDataBlobForMulticastSession:fromPeer:]_block_invoke.191
- ___90-[MIBUNWClientController nanSubscriberDidStart:withPeerIPAddress:usingInterface:forRetry:]_block_invoke.199
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.166
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.166.cold.1
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.166.cold.2
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.166.cold.3
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.169
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.169.cold.1
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke.174
- ___93-[MIBUNANPublisher publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:]_block_invoke_2.176
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSTimer"8ls32l8s40l8
- ___block_literal_global.105
- ___block_literal_global.118
- ___block_literal_global.140
- ___block_literal_global.148
- ___block_literal_global.165
- ___block_literal_global.180
- ___block_literal_global.198
- ___block_literal_global.201
- ___block_literal_global.204
- ___block_literal_global.207
- ___block_literal_global.209
- ___block_literal_global.85
- ___block_literal_global.88
- _objc_msgSend$_activateReceiveTimer
- _objc_msgSend$_handleReceiveTimerTick
- _objc_msgSend$_resetReceiveTimerWithInterval:
- _objc_msgSend$_stopMulticast:
- _objc_msgSend$initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:
- _objc_msgSend$initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:
- _objc_retain_x8
CStrings:
+ "  channelName: %lu, band: %lu, bandwidth: %lu, rateAdapter: %d"
+ "  multicastKeysBlob: %lu"
+ "  multicastKeysBlob: %{public}@"
+ "%{public}@"
+ "%{public}@: Activating progress timer with interval: %llu (sec)"
+ "%{public}@: Cleaning up multicast peer whose last contact is earlier than the cutoff: %{public}@"
+ "%{public}@: Configuring rate adapter=%{bool}d, multicast security=%{bool}d"
+ "%{public}@: Deactivating progress timer..."
+ "%{public}@: Failed to create WiFiAwareMulticastConfiguration."
+ "%{public}@: Found inactive multicast peer: %{public}@ Last contact: %{public}@"
+ "%{public}@: Multicast peer clean up timer already stopped."
+ "%{public}@: NAN publisher generated security keys blob: %lu (bytes)"
+ "%{public}@: NAN publisher generated security keys blob: %{public}@"
+ "%{public}@: Remove multicast peer already in the record: %{public}@"
+ "%{public}@: Skip updating last contact date for orphaned peer: %{public}@"
+ "%{public}@: Starting multicast peer clean up timer with interval: %lu (secs); peer timeout: %lu (secs)"
+ "%{public}@: Stopping multicast peer clean up timer!"
+ "%{public}@: ping through multicast: %lu bytes"
+ "%{public}@: pingThroughMulticast called."
+ "%{public}@: state: %lu; progress = %@"
+ "("
+ "/Library/Caches/com.apple.xbs/9DBB5909-E8C7-40F4-AC9B-9807A6FFC125/TemporaryDirectory.XhCZbY/Sources/MobileInBoxUpdater/External/nanorq/wrkmat.c"
+ "@\"NSMutableOrderedSet\""
+ "@\"NSTimer\""
+ "@100@0:8@16@24@32@40Q48Q56Q64B72@76@84@92"
+ "@116@0:8@16@24@32@40@48@56Q64Q72Q80B88@92@100@108"
+ "@120@0:8@16@24@32@40@48@56@64@72Q80Q88Q96B104B108@112"
+ "@80@0:8@16@24@32Q40Q48Q56B64B68@72"
+ "Initializing MIBUNWServerController with TCP host: %{public}@:%{public}@, NAN port: %{public}@, multicast group: %{public}@:%{public}@, service: %{public}@, country: %{public}@, channel: %lu, band: %lu, bandwidth: %lu, RA enabled: %d MC security: %d"
+ "Packets received in the last %lu secs: %lu (Bytes: %lu); Bytes consumed by RaptorQ: %lu; Effective bandwidth: %0.5f Mbps"
+ "T@\"NSNumber\",R,C,N,V_progress"
+ "TQ,N,V_peerTimeout"
+ "_activateProgressTimer"
+ "_deactivateProgressTimer"
+ "_handleMulticastPeerCleanUpTimerFired"
+ "_handleProgressTimerTick"
+ "_multicastPeers"
+ "_multicastSecurity"
+ "_peerCleanUpTimer"
+ "_peerLastContact"
+ "_peerTimeout"
+ "_progressTimer"
+ "_rateAdapter"
+ "_startMulticastPeerCleanUpTimer"
+ "_stopMulticastPeerCleanUpTimer"
+ "com.apple.inboxupdaterd"
+ "configuration"
+ "dateByAddingTimeInterval:"
+ "earlierDate:"
+ "initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:controllerDelegate:dataCollector:"
+ "initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:controllerDelegate:"
+ "initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:rateAdapter:multicastSecurity:publisherDelegate:"
+ "initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:rateAdapter:multicastKeysBlob:subscriberDelegate:dataCollector:"
+ "multicastConfiguration"
+ "nanPublisher:didGenerateSecurityKeys:"
+ "peerTimeout"
+ "serverController:didReceiveMulticastSecurityKeys:"
+ "setKeyBlob:"
+ "setKeyExchangeOverMedium:"
+ "setPeerTimeout:"
+ "v32@0:8@\"MIBUNANPublisher\"16@\"NSData\"24"
- "  channelName: %lu, band: %lu, bandwidth: %lu, enableRA: %d"
- "%{public}@: Activate receive timer with interval: %llu (sec)"
- "%{public}@: Cancelling ongoing receive timer"
- "%{public}@: Failed to create WiFiAwareMulticastConfiguration"
- "%{public}@: Failed to create WiFiAwareMulticastConfiguration, skipping enabling Rate Adapter..."
- "%{public}@: Resetting receive timer with interval: %llu (sec)"
- "%{public}@: ping through multicast: %@"
- "%{public}@: pingThroughMulticast called with payload: %{public}@"
- "%{public}@: state :%lu; progress = %@"
- "/Library/Caches/com.apple.xbs/C913B9B7-33E5-435D-90A9-395071BD0A5E/TemporaryDirectory.KMrRKZ/Sources/MobileInBoxUpdater/External/nanorq/wrkmat.c"
- "@108@0:8@16@24@32@40@48@56Q64Q72Q80B88@92@100"
- "@116@0:8@16@24@32@40@48@56@64@72Q80Q88Q96B104@108"
- "@76@0:8@16@24@32Q40Q48Q56B64@68"
- "@92@0:8@16@24@32@40Q48Q56Q64B72@76@84"
- "Initializing MIBUNWServerController with TCP host: %{public}@:%{public}@, NAN port: %{public}@, multicast group: %{public}@:%{public}@, service: %{public}@, country: %{public}@, channel: %lu, band: %lu, bandwidth: %lu, RA enabled: %d"
- "Packets received in the last %llus: %lu; Bytes consumed in last %llus: %lu; Effective bandwidth: %0.5f Mbps"
- "T@\"NSNumber\",R,N,V_progress"
- "_activateReceiveTimer"
- "_enableRA"
- "_handleReceiveTimerTick"
- "_receiveTimer"
- "_resetReceiveTimerWithInterval:"
- "_stopMulticast:"
- "initWithPacketConsumer:hostPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:dataCollector:"
- "initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:"
- "initWithServiceName:groupAddress:countryCode:channelName:band:bandwidth:enableRateAdapter:publisherDelegate:"
- "initWithServiceName:groupAddress:groupPort:countryCode:channelName:band:bandwidth:enableRateAdapter:subscriberDelegate:dataCollector:"

```
