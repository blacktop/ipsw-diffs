## MobileMulticastTransfer

> `/System/Library/PrivateFrameworks/MobileMulticastTransfer.framework/MobileMulticastTransfer`

```diff

-132.0.0.0.0
-  __TEXT.__text: 0x2ce94
+144.0.0.0.0
+  __TEXT.__text: 0x2d038
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x1550
+  __TEXT.__objc_methlist: 0x1578
   __TEXT.__const: 0x4908
-  __TEXT.__cstring: 0xdbb
-  __TEXT.__oslogstring: 0x367a
+  __TEXT.__cstring: 0xe08
+  __TEXT.__oslogstring: 0x3695
   __TEXT.__gcc_except_tab: 0x654
-  __TEXT.__unwind_info: 0xc98
+  __TEXT.__unwind_info: 0xca0
   __TEXT.__objc_classname: 0x31a
   __TEXT.__objc_methname: 0x3655
   __TEXT.__objc_methtype: 0x159a

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
   __AUTH_CONST.__auth_got: 0x650
-  __AUTH_CONST.__const: 0x2240
+  __AUTH_CONST.__const: 0x2260
   __AUTH_CONST.__cfstring: 0x940
-  __AUTH_CONST.__objc_const: 0x4928
+  __AUTH_CONST.__objc_const: 0x4968
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x268
+  __DATA.__objc_ivar: 0x270
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x30
   __DATA.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EE704DDA-3A47-351D-AA53-0DCD93D983C4
-  Functions: 1243
-  Symbols:   4370
-  CStrings:  1280
+  UUID: 8FF459F8-8999-32E2-9784-ADF8BD6EFE8B
+  Functions: 1248
+  Symbols:   4385
+  CStrings:  1282
 
Symbols:
+ -[MIBUFilePacketConsumer consumePackets:arrivalTime:withCompletion:inQueue:]
+ -[MIBUFilePacketConsumer consumePackets:arrivalTime:withCompletion:inQueue:].cold.1
+ -[MIBUFilePacketConsumer lossRate]
+ -[MIBUFilePacketConsumer packetsDiscarded]
+ GCC_except_table20
+ GCC_except_table35
+ _OBJC_IVAR_$_MIBUFilePacketConsumer._lossRate
+ _OBJC_IVAR_$_MIBUFilePacketConsumer._packetsDiscarded
+ ___36-[MIBUFilePacketConsumer _bootstrap]_block_invoke.10
+ ___36-[MIBUFilePacketConsumer _bootstrap]_block_invoke.10.cold.1
+ ___36-[MIBUFilePacketConsumer _bootstrap]_block_invoke.7
+ ___36-[MIBUFilePacketConsumer _bootstrap]_block_invoke.7.cold.1
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.36
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.36.cold.1
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.39
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.39.cold.1
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.44
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.44.cold.1
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.47
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.47.cold.1
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.50
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.50.cold.1
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.57
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.57.cold.1
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.60
+ ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.60.cold.1
+ ___59-[MIBUFilePacketConsumer _writePayloadToFile:forPacketUID:]_block_invoke.31
+ ___59-[MIBUFilePacketConsumer _writePayloadToFile:forPacketUID:]_block_invoke.31.cold.1
+ ___64-[MIBUFilePacketConsumer _consumePacket:withCompletion:inQueue:]_block_invoke.16
+ ___64-[MIBUFilePacketConsumer _consumePacket:withCompletion:inQueue:]_block_invoke.16.cold.1
+ ___64-[MIBUFilePacketConsumer _consumePacket:withCompletion:inQueue:]_block_invoke.19
+ ___64-[MIBUFilePacketConsumer _consumePacket:withCompletion:inQueue:]_block_invoke.22
+ ___64-[MIBUFilePacketConsumer _consumePacket:withCompletion:inQueue:]_block_invoke_2.23
+ ___76-[MIBUFilePacketConsumer consumePackets:arrivalTime:withCompletion:inQueue:]_block_invoke
+ ___76-[MIBUFilePacketConsumer consumePackets:arrivalTime:withCompletion:inQueue:]_block_invoke.cold.1
+ ___block_literal_global.46
+ ___block_literal_global.49
+ ___block_literal_global.52
+ ___block_literal_global.6
- GCC_except_table18
- GCC_except_table33
- ___36-[MIBUFilePacketConsumer _bootstrap]_block_invoke.5
- ___36-[MIBUFilePacketConsumer _bootstrap]_block_invoke.5.cold.1
- ___36-[MIBUFilePacketConsumer _bootstrap]_block_invoke.8
- ___36-[MIBUFilePacketConsumer _bootstrap]_block_invoke.8.cold.1
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.34
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.34.cold.1
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.37
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.37.cold.1
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.42
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.42.cold.1
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.45
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.45.cold.1
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.48
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.48.cold.1
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.55
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.55.cold.1
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.58
- ___45-[MIBUFilePacketConsumer _assembleOutputFile]_block_invoke.58.cold.1
- ___59-[MIBUFilePacketConsumer _writePayloadToFile:forPacketUID:]_block_invoke.29
- ___59-[MIBUFilePacketConsumer _writePayloadToFile:forPacketUID:]_block_invoke.29.cold.1
- ___64-[MIBUFilePacketConsumer _consumePacket:withCompletion:inQueue:]_block_invoke.14
- ___64-[MIBUFilePacketConsumer _consumePacket:withCompletion:inQueue:]_block_invoke.14.cold.1
- ___64-[MIBUFilePacketConsumer _consumePacket:withCompletion:inQueue:]_block_invoke.17
- ___64-[MIBUFilePacketConsumer _consumePacket:withCompletion:inQueue:]_block_invoke.20
- ___64-[MIBUFilePacketConsumer _consumePacket:withCompletion:inQueue:]_block_invoke_2.21
- ___block_literal_global.57
CStrings:
+ "%s is not implemented yet."
+ "-[MIBUFilePacketConsumer consumePackets:arrivalTime:withCompletion:inQueue:]"

```
