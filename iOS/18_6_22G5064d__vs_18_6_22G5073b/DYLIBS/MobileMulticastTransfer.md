## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`

```diff

-63.140.19.0.0
-  __TEXT.__text: 0x2cf68
+63.140.21.0.0
+  __TEXT.__text: 0x2cf28
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x1520
+  __TEXT.__objc_methlist: 0x1508
   __TEXT.__const: 0x4908
   __TEXT.__cstring: 0xdbb
   __TEXT.__oslogstring: 0x367a
   __TEXT.__gcc_except_tab: 0x654
   __TEXT.__unwind_info: 0xc98
   __TEXT.__objc_classname: 0x31a
-  __TEXT.__objc_methname: 0x34ed
+  __TEXT.__objc_methname: 0x34dd
   __TEXT.__objc_methtype: 0x1350
   __TEXT.__objc_stubs: 0x28c0
   __DATA_CONST.__got: 0x1f0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xca0
+  __DATA_CONST.__objc_selrefs: 0xc98
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
   __AUTH_CONST.__auth_got: 0x650
   __AUTH_CONST.__const: 0x2240
   __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_const: 0x4908
-  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x5f0
   __DATA.__objc_ivar: 0x268

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 55F719E6-BB31-3EA5-8EAB-90F05DC2D756
-  Functions: 1244
-  Symbols:   4380
-  CStrings:  1268
+  UUID: 43B7372B-4098-3CDC-8A3B-220E1C243F60
+  Functions: 1242
+  Symbols:   4376
+  CStrings:  1267
 
Symbols:
+ GCC_except_table49
+ ___41-[MIBUNWServerController _startMulticast]_block_invoke.51
+ ___41-[MIBUNWServerController _startMulticast]_block_invoke.51.cold.1
+ ___41-[MIBUNWServerController _startMulticast]_block_invoke.54
+ ___41-[MIBUNWServerController _startMulticast]_block_invoke.54.cold.1
+ ___41-[MIBUNWServerController _startMulticast]_block_invoke.58
+ ___41-[MIBUNWServerController _startMulticast]_block_invoke.58.cold.1
+ ___42-[MIBUNWServerController _startNANService]_block_invoke.37
+ ___42-[MIBUNWServerController _startNANService]_block_invoke.37.cold.1
+ ___43-[MIBUNWServerController _startTCPListener]_block_invoke.27
+ ___43-[MIBUNWServerController _startTCPListener]_block_invoke.27.cold.1
+ ___43-[MIBUNWServerController _startTCPListener]_block_invoke.31
+ ___43-[MIBUNWServerController _startTCPListener]_block_invoke.31.cold.1
+ ___46-[MIBUNWServerController _setupFileSenderLoop]_block_invoke.65
+ ___49-[MIBUNWServerController _tearDownFileSenderLoop]_block_invoke.68
+ ___49-[MIBUNWServerController _tearDownFileSenderLoop]_block_invoke.68.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.136
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.136.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke.122
+ ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke.122.cold.1
+ ___49-[MIBUNWServerController clientListenerDidStart:]_block_invoke.107
+ ___49-[MIBUNWServerController clientListenerDidStart:]_block_invoke.107.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.127
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.127.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.130
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.130.cold.1
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.130.cold.2
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke_2.131
+ ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke_2.131.cold.1
+ ___54-[MIBUNWServerController _calculateEffectiveBandwidth]_block_invoke.73
+ ___54-[MIBUNWServerController _calculateEffectiveBandwidth]_block_invoke.73.cold.1
+ ___58-[MIBUNWServerController clientListenerDidStop:withError:]_block_invoke.112
+ ___58-[MIBUNWServerController clientListenerDidStop:withError:]_block_invoke.112.cold.1
+ ___67-[MIBUNWServerController clientListener:didReceiveNewClientDevice:]_block_invoke.117
+ ___67-[MIBUNWServerController clientListener:didReceiveNewClientDevice:]_block_invoke.117.cold.1
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.148
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.148.cold.1
+ ___73-[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:]_block_invoke.94
+ ___74-[MIBUNWServerController _adjustBatchSizeWithPacketDroppedInLastInterval:]_block_invoke.85
+ ___74-[MIBUNWServerController _adjustBatchSizeWithPacketDroppedInLastInterval:]_block_invoke.85.cold.1
+ ___block_literal_global.133
+ ___block_literal_global.53
+ ___block_literal_global.90
- -[MIBUNWServerController setPingInterval:]
- -[MIBUNWServerController setPingTimeout:]
- GCC_except_table48
- GCC_except_table51
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.56
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.56.cold.1
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.59
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.59.cold.1
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.63
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.63.cold.1
- ___42-[MIBUNWServerController _startNANService]_block_invoke.42
- ___42-[MIBUNWServerController _startNANService]_block_invoke.42.cold.1
- ___43-[MIBUNWServerController _startTCPListener]_block_invoke.32
- ___43-[MIBUNWServerController _startTCPListener]_block_invoke.32.cold.1
- ___43-[MIBUNWServerController _startTCPListener]_block_invoke.36
- ___43-[MIBUNWServerController _startTCPListener]_block_invoke.36.cold.1
- ___46-[MIBUNWServerController _setupFileSenderLoop]_block_invoke.70
- ___49-[MIBUNWServerController _tearDownFileSenderLoop]_block_invoke.73
- ___49-[MIBUNWServerController _tearDownFileSenderLoop]_block_invoke.73.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.146
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.146.cold.1
- ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke.127
- ___49-[MIBUNWServerController clientDeviceDidConnect:]_block_invoke.127.cold.1
- ___49-[MIBUNWServerController clientListenerDidStart:]_block_invoke.112
- ___49-[MIBUNWServerController clientListenerDidStart:]_block_invoke.112.cold.1
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.132
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.132.cold.1
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.135
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.135.cold.1
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke.135.cold.2
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke_2.136
- ___52-[MIBUNWServerController clientDeviceDidDisconnect:]_block_invoke_2.136.cold.1
- ___54-[MIBUNWServerController _calculateEffectiveBandwidth]_block_invoke.78
- ___54-[MIBUNWServerController _calculateEffectiveBandwidth]_block_invoke.78.cold.1
- ___58-[MIBUNWServerController clientListenerDidStop:withError:]_block_invoke.117
- ___58-[MIBUNWServerController clientListenerDidStop:withError:]_block_invoke.117.cold.1
- ___67-[MIBUNWServerController clientListener:didReceiveNewClientDevice:]_block_invoke.122
- ___67-[MIBUNWServerController clientListener:didReceiveNewClientDevice:]_block_invoke.122.cold.1
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.153
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.153.cold.1
- ___73-[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:]_block_invoke.99
- ___74-[MIBUNWServerController _adjustBatchSizeWithPacketDroppedInLastInterval:]_block_invoke.90
- ___74-[MIBUNWServerController _adjustBatchSizeWithPacketDroppedInLastInterval:]_block_invoke.90.cold.1
- ___block_literal_global.102
- ___block_literal_global.160
- ___block_literal_global.55
- ___block_literal_global.61
Functions (modified):
~ -[MIBUNWServerController initWithPacketProvider:hostAddress:hostPort:nanPort:groupAddress:groupPort:interfaceName:serviceName:countryCode:channelName:band:bandwidth:enableRateAdapter:controllerDelegate:] : 796 -> 756

Functions (removed):
- -[MIBUNWServerController setPingInterval:]
- -[MIBUNWServerController setPingTimeout:]
CStrings:
- "setPingTimeout:"

```
