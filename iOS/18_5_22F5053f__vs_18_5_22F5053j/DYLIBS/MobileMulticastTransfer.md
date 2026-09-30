## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`

```diff

-63.120.33.0.0
-  __TEXT.__text: 0x29dac
+63.120.35.0.0
+  __TEXT.__text: 0x2a1a0
   __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_methlist: 0x1420
+  __TEXT.__objc_methlist: 0x1438
   __TEXT.__const: 0x48f8
-  __TEXT.__cstring: 0xd41
-  __TEXT.__oslogstring: 0x30f5
+  __TEXT.__cstring: 0xd57
+  __TEXT.__oslogstring: 0x3113
   __TEXT.__gcc_except_tab: 0x618
-  __TEXT.__unwind_info: 0xbc8
+  __TEXT.__unwind_info: 0xbe0
   __TEXT.__objc_classname: 0x2fb
-  __TEXT.__objc_methname: 0x326b
+  __TEXT.__objc_methname: 0x32c9
   __TEXT.__objc_methtype: 0x131b
-  __TEXT.__objc_stubs: 0x25a0
+  __TEXT.__objc_stubs: 0x2600
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x798
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbf8
+  __DATA_CONST.__objc_selrefs: 0xc10
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x90
   __AUTH_CONST.__auth_got: 0x638
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x1f40
-  __AUTH_CONST.__cfstring: 0x8c0
-  __AUTH_CONST.__objc_const: 0x4730
+  __AUTH_CONST.__const: 0x1f60
+  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__objc_const: 0x4750
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x248
+  __DATA.__objc_ivar: 0x24c
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x30
   __DATA.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1165
-  Symbols:   4096
-  CStrings:  1146
+  Functions: 1169
+  Symbols:   4111
+  CStrings:  1153
 
Symbols:
+ -[MIBUNWServerController _calculateEffectiveBandwidth].cold.2
+ -[MIBUNWServerController _packetDropSummary]
+ -[MIBUNWServerController _updatePacketDropBreakdown:]
+ GCC_except_table48
+ _OBJC_IVAR_$_MIBUNWServerController._packetDropBreakdown
+ ___41-[MIBUNWServerController _startMulticast]_block_invoke.56
+ ___41-[MIBUNWServerController _startMulticast]_block_invoke.56.cold.1
+ ___41-[MIBUNWServerController _startMulticast]_block_invoke.59
+ ___41-[MIBUNWServerController _startMulticast]_block_invoke.59.cold.1
+ ___41-[MIBUNWServerController _startMulticast]_block_invoke.63
+ ___41-[MIBUNWServerController _startMulticast]_block_invoke.63.cold.1
+ ___42-[MIBUNWServerController _startNANService]_block_invoke.42
+ ___42-[MIBUNWServerController _startNANService]_block_invoke.42.cold.1
+ ___43-[MIBUNWServerController _startTCPListener]_block_invoke.32
+ ___43-[MIBUNWServerController _startTCPListener]_block_invoke.32.cold.1
+ ___43-[MIBUNWServerController _startTCPListener]_block_invoke.36
+ ___43-[MIBUNWServerController _startTCPListener]_block_invoke.36.cold.1
+ ___46-[MIBUNWServerController _setupFileSenderLoop]_block_invoke.70
+ ___49-[MIBUNWServerController _tearDownFileSenderLoop]_block_invoke.73
+ ___49-[MIBUNWServerController _tearDownFileSenderLoop]_block_invoke.73.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.127
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.127.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.132
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.132.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.135
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.135.cold.1
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.135.cold.2
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke_2.136
+ ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke_2.136.cold.1
+ ___49-[MIBUNWServerController clientListenerDidStart:]_block_invoke.112
+ ___49-[MIBUNWServerController clientListenerDidStart:]_block_invoke.112.cold.1
+ ___54-[MIBUNWServerController _calculateEffectiveBandwidth]_block_invoke.78
+ ___54-[MIBUNWServerController _calculateEffectiveBandwidth]_block_invoke.78.cold.1
+ ___58-[MIBUNWServerController clientListenerDidStop:withError:]_block_invoke.117
+ ___58-[MIBUNWServerController clientListenerDidStop:withError:]_block_invoke.117.cold.1
+ ___67-[MIBUNWServerController clientListener:didReceiveNewClientDevice:]_block_invoke.122
+ ___67-[MIBUNWServerController clientListener:didReceiveNewClientDevice:]_block_invoke.122.cold.1
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.143
+ ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.143.cold.1
+ ___73-[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:]_block_invoke.99
+ ___74-[MIBUNWServerController _adjustBatchSizeWithPacketDroppedInLastInterval:]_block_invoke.90
+ ___74-[MIBUNWServerController _adjustBatchSizeWithPacketDroppedInLastInterval:]_block_invoke.90.cold.1
+ ___block_literal_global.111
+ ___block_literal_global.119
+ ___block_literal_global.134
+ ___block_literal_global.140
+ ___block_literal_global.145
+ ___block_literal_global.55
+ ___block_literal_global.72
+ _objc_msgSend$_packetDropSummary
+ _objc_msgSend$_updatePacketDropBreakdown:
+ _objc_msgSend$componentsJoinedByString:
- GCC_except_table45
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.55
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.55.cold.1
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.58
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.58.cold.1
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.62
- ___41-[MIBUNWServerController _startMulticast]_block_invoke.62.cold.1
- ___42-[MIBUNWServerController _startNANService]_block_invoke.41
- ___42-[MIBUNWServerController _startNANService]_block_invoke.41.cold.1
- ___43-[MIBUNWServerController _startTCPListener]_block_invoke.31
- ___43-[MIBUNWServerController _startTCPListener]_block_invoke.31.cold.1
- ___43-[MIBUNWServerController _startTCPListener]_block_invoke.35
- ___43-[MIBUNWServerController _startTCPListener]_block_invoke.35.cold.1
- ___46-[MIBUNWServerController _setupFileSenderLoop]_block_invoke.69
- ___49-[MIBUNWServerController _tearDownFileSenderLoop]_block_invoke.72
- ___49-[MIBUNWServerController _tearDownFileSenderLoop]_block_invoke.72.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.115
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.115.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.120
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.120.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.123
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.123.cold.1
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke.123.cold.2
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke_2.124
- ___49-[MIBUNWServerController clientDeviceDidCheckIn:]_block_invoke_2.124.cold.1
- ___49-[MIBUNWServerController clientListenerDidStart:]_block_invoke.100
- ___49-[MIBUNWServerController clientListenerDidStart:]_block_invoke.100.cold.1
- ___58-[MIBUNWServerController clientListenerDidStop:withError:]_block_invoke.105
- ___58-[MIBUNWServerController clientListenerDidStop:withError:]_block_invoke.105.cold.1
- ___67-[MIBUNWServerController clientListener:didReceiveNewClientDevice:]_block_invoke.110
- ___67-[MIBUNWServerController clientListener:didReceiveNewClientDevice:]_block_invoke.110.cold.1
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.131
- ___72-[MIBUNWServerController clientDevice:didCheckOutWithError:withSummary:]_block_invoke.131.cold.1
- ___73-[MIBUNWServerController _handleFetchCompletionWithResult:atEOF:packets:]_block_invoke.88
- ___74-[MIBUNWServerController _adjustBatchSizeWithPacketDroppedInLastInterval:]_block_invoke.79
- ___74-[MIBUNWServerController _adjustBatchSizeWithPacketDroppedInLastInterval:]_block_invoke.79.cold.1
- ___block_literal_global.117
- ___block_literal_global.37
- ___block_literal_global.76
- ___block_literal_global.99
CStrings:
+ "\nB\x19"
+ "%@ with errorno %@"
+ ", "
+ "Dropped packets breakdown: %@"
+ "_packetDropBreakdown"
+ "_packetDropSummary"
+ "_updatePacketDropBreakdown:"
+ "componentsJoinedByString:"
- "\nA\x19"

```
