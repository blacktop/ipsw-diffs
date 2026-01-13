## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/Versions/A/MobileMulticastTransfer`

```diff

-153.80.3.0.0
-  __TEXT.__text: 0x307dc
+153.80.6.0.0
+  __TEXT.__text: 0x30d44
   __TEXT.__auth_stubs: 0xa80
   __TEXT.__objc_methlist: 0x1580
   __TEXT.__const: 0x48e0
-  __TEXT.__cstring: 0xeaf
-  __TEXT.__oslogstring: 0x385e
-  __TEXT.__gcc_except_tab: 0x654
-  __TEXT.__unwind_info: 0xd30
+  __TEXT.__cstring: 0xee6
+  __TEXT.__oslogstring: 0x38a8
+  __TEXT.__gcc_except_tab: 0x6d0
+  __TEXT.__unwind_info: 0xd48
   __TEXT.__objc_classname: 0x31a
-  __TEXT.__objc_methname: 0x3702
+  __TEXT.__objc_methname: 0x3787
   __TEXT.__objc_methtype: 0x1517
-  __TEXT.__objc_stubs: 0x2980
-  __DATA_CONST.__got: 0x1f0
+  __TEXT.__objc_stubs: 0x2a80
+  __DATA_CONST.__got: 0x200
   __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xce0
+  __DATA_CONST.__objc_selrefs: 0xd20
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
   __AUTH_CONST.__auth_got: 0x550
-  __AUTH_CONST.__const: 0x2b30
-  __AUTH_CONST.__cfstring: 0x980
-  __AUTH_CONST.__objc_const: 0x49a0
+  __AUTH_CONST.__const: 0x2b80
+  __AUTH_CONST.__cfstring: 0x9a0
+  __AUTH_CONST.__objc_const: 0x4980
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x278
+  __DATA.__objc_ivar: 0x274
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x38
   __DATA.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 28A38116-E823-365A-B681-017EB95946F9
-  Functions: 1308
-  Symbols:   2992
-  CStrings:  1296
+  UUID: FF7CE9D1-8B8B-3A97-B241-CF2A5673235A
+  Functions: 1310
+  Symbols:   3010
+  CStrings:  1307
 
Symbols:
+ -[MIBUNWClientController _checkOutWithError:].cold.3
+ -[MIBUNWClientController _checkOutWithError:].cold.4
+ GCC_except_table22
+ _OBJC_CLASS_$_NSCondition
+ _OBJC_CLASS_$_NSNotificationCenter
+ __42-[MIBUNWClientController _disableFirewall]_block_invoke.146
+ __42-[MIBUNWClientController _disableFirewall]_block_invoke.146.cold.1
+ __45-[MIBUNWClientController _checkOutWithError:]_block_invoke.46
+ __45-[MIBUNWClientController _checkOutWithError:]_block_invoke.46.cold.1
+ __45-[MIBUNWClientController _checkOutWithError:]_block_invoke_2.cold.1
+ __47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.94
+ __47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.94.cold.1
+ __47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.94.cold.2
+ __51-[MIBUNWClientController _updateControllerProgress]_block_invoke.78
+ __51-[MIBUNWClientController _updateControllerProgress]_block_invoke.78.cold.1
+ __51-[MIBUNWClientController _updateControllerProgress]_block_invoke.81
+ __51-[MIBUNWClientController _updateControllerProgress]_block_invoke.81.cold.1
+ __57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.120
+ __57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.120.cold.1
+ __57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.120.cold.2
+ __57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.123
+ __57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.123.cold.1
+ __57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.126
+ __57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.71
+ __57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.71.cold.1
+ __57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.74
+ __63-[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]_block_invoke.140
+ __63-[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]_block_invoke.140.cold.1
+ __64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.133
+ __64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.133.cold.1
+ __64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.62
+ __64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.62.cold.1
+ ___45-[MIBUNWClientController _checkOutWithError:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40s48r_e24_v16?0"NSNotification"8l
+ __block_literal_global.103
+ __block_literal_global.137
+ __block_literal_global.142
+ __block_literal_global.148
+ __block_literal_global.160
+ __block_literal_global.68
+ __block_literal_global.96
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$lock
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$signal
+ _objc_msgSend$unlock
+ _objc_msgSend$waitUntilDate:
- OBJC_IVAR_$_MIBUNWClientController._checkoutSem
- __42-[MIBUNWClientController _disableFirewall]_block_invoke.137
- __42-[MIBUNWClientController _disableFirewall]_block_invoke.137.cold.1
- __47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.84
- __47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.84.cold.1
- __47-[MIBUNWClientController pingThroughMulticast:]_block_invoke.84.cold.2
- __51-[MIBUNWClientController _updateControllerProgress]_block_invoke.68
- __51-[MIBUNWClientController _updateControllerProgress]_block_invoke.68.cold.1
- __51-[MIBUNWClientController _updateControllerProgress]_block_invoke.71
- __51-[MIBUNWClientController _updateControllerProgress]_block_invoke.71.cold.1
- __57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.111
- __57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.111.cold.1
- __57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.111.cold.2
- __57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.114
- __57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.114.cold.1
- __57-[MIBUNWClientController _handlePacketConsumerCompletion]_block_invoke.117
- __57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.61
- __57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.61.cold.1
- __57-[MIBUNWClientController _resetReceiveTimerWithInterval:]_block_invoke.64
- __63-[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]_block_invoke.131
- __63-[MIBUNWClientController _createTCPConnectionWithAddr:andPort:]_block_invoke.131.cold.1
- __64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.124
- __64-[MIBUNWClientController _createNANTCPConnectionUsingInterface:]_block_invoke.124.cold.1
- __64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.52
- __64-[MIBUNWClientController _startMulticastReceiverUsingInterface:]_block_invoke.52.cold.1
- __block_literal_global.130
- __block_literal_global.149
- __block_literal_global.58
CStrings:
+ "\n("
+ "%{public}@: Client checkout timed out! Retry left: %lu"
+ "%{public}@: Received client checkout ack notification!"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugBb1ZVyzEwElJI9tf8x8G27mFYq8pTfdZk/Library/Caches/com.apple.xbs/Sources/MobileInBoxUpdater/External/nanorq/wrkmat.c"
+ "ClientCheckoutAckNotification"
+ "addObserverForName:object:queue:usingBlock:"
+ "defaultCenter"
+ "lock"
+ "postNotificationName:object:userInfo:"
+ "removeObserver:"
+ "signal"
+ "unlock"
+ "v16@?0@\"NSNotification\"8"
+ "waitUntilDate:"
- "\v("
- "/AppleInternal/Library/BuildRoots/4~CDyougBwPjK8VUbtYYhX0xbULNw89GO75tR7y5U/Library/Caches/com.apple.xbs/Sources/MobileInBoxUpdater/External/nanorq/wrkmat.c"
- "Device checkout timed out after %ds"
- "_checkoutSem"

```
