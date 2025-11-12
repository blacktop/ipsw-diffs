## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`

```diff

-805.60.2.0.0
-  __TEXT.__text: 0x4726c
+805.60.5.0.0
+  __TEXT.__text: 0x47420
   __TEXT.__auth_stubs: 0xd80
   __TEXT.__delay_helper: 0x1b4
-  __TEXT.__objc_methlist: 0x452c
+  __TEXT.__objc_methlist: 0x454c
   __TEXT.__gcc_except_tab: 0x1670
   __TEXT.__const: 0x298
   __TEXT.__cstring: 0x2bd8

   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__swift5_typeref: 0x2a
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x16e8
+  __TEXT.__unwind_info: 0x16f8
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0xc19
-  __TEXT.__objc_methname: 0x8b5e
-  __TEXT.__objc_methtype: 0x2185
-  __TEXT.__objc_stubs: 0x67e0
+  __TEXT.__objc_methname: 0x8b7e
+  __TEXT.__objc_methtype: 0x21aa
+  __TEXT.__objc_stubs: 0x6820
   __DATA_CONST.__got: 0x5e0
   __DATA_CONST.__const: 0x16e0
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20f0
+  __DATA_CONST.__objc_selrefs: 0x2100
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0xb18
   __AUTH_CONST.__cfstring: 0x2560
-  __AUTH_CONST.__objc_const: 0x8610
+  __AUTH_CONST.__objc_const: 0x8618
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x320

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 99381CED-F58A-35BE-B8DA-5362F8599D6B
-  Functions: 1956
-  Symbols:   6943
-  CStrings:  3067
+  UUID: E161C0E3-6557-3D40-A0D7-7347F2EA8580
+  Functions: 1960
+  Symbols:   6953
+  CStrings:  3070
 
Symbols:
+ -[TKSmartCardSlot escape:reply:]
+ -[TKSmartCardSlotEngine sendEscape:reply:]
+ GCC_except_table123
+ GCC_except_table138
+ GCC_except_table142
+ GCC_except_table163
+ GCC_except_table166
+ GCC_except_table169
+ GCC_except_table76
+ GCC_except_table95
+ ___30-[TKSmartCardSlotEngine reset]_block_invoke.212
+ ___30-[TKSmartCardSlotEngine reset]_block_invoke.212.cold.1
+ ___32-[TKSmartCardSlot escape:reply:]_block_invoke
+ ___32-[TKSmartCardSlot makeSmartCard]_block_invoke.220
+ ___34-[TKSmartCardSlotEngine terminate]_block_invoke.241
+ ___34-[TKSmartCardSlotEngine terminate]_block_invoke.241.cold.1
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.315
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.317
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.319
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke.324
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.316
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.316.cold.1
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.318
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.318.cold.1
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.323
+ ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.323.cold.1
+ ___37-[TKSmartCard transmitRequest:reply:]_block_invoke.339
+ ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.221
+ ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.221.cold.1
+ ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.224
+ ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.225
+ ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.225.cold.1
+ ___37-[TKSmartCardSlotEngine setProtocol:]_block_invoke.216
+ ___37-[TKSmartCardSlotEngine setProtocol:]_block_invoke.216.cold.1
+ ___38-[TKSmartCardSlotEngine leaveSession:]_block_invoke.230
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke.309
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_2.310
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_3.311
+ ___43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke.374
+ ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.408
+ ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.408.cold.1
+ ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.411
+ ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.411.cold.1
+ ___46-[TKSmartCardSlotEngine scheduleIdlePowerDown]_block_invoke.220
+ ___52-[TKSmartCardSlot simulateCardReinsertionWithError:]_block_invoke.231
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.214
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.214.cold.1
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.215
+ ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.215.cold.1
+ ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.228
+ ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.228.cold.1
+ ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.228.cold.2
+ ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.229
+ ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.229.cold.1
+ ___block_literal_global.211
+ ___block_literal_global.214
+ ___block_literal_global.218
+ ___block_literal_global.219
+ ___block_literal_global.223
+ ___block_literal_global.227
+ ___block_literal_global.243
+ ___block_literal_global.313
+ ___block_literal_global.322
+ ___block_literal_global.334
+ ___block_literal_global.350
+ ___block_literal_global.352
+ ___block_literal_global.407
+ ___block_literal_global.410
+ ___block_literal_global.415
+ ___block_literal_global.443
+ ___block_literal_global.902
+ _objc_msgSend$engine:escape:
+ _objc_msgSend$sendEscape:reply:
- GCC_except_table121
- GCC_except_table137
- GCC_except_table140
- GCC_except_table161
- GCC_except_table164
- GCC_except_table167
- GCC_except_table74
- GCC_except_table93
- ___30-[TKSmartCardSlotEngine reset]_block_invoke.210
- ___30-[TKSmartCardSlotEngine reset]_block_invoke.210.cold.1
- ___32-[TKSmartCardSlot makeSmartCard]_block_invoke.218
- ___34-[TKSmartCardSlotEngine terminate]_block_invoke.239
- ___34-[TKSmartCardSlotEngine terminate]_block_invoke.239.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.312
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.314
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.316
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.321
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.313
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.313.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.315
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.315.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.320
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.320.cold.1
- ___37-[TKSmartCard transmitRequest:reply:]_block_invoke.336
- ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.219
- ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.219.cold.1
- ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.222
- ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.223
- ___37-[TKSmartCardSlotEngine cardPresent:]_block_invoke.223.cold.1
- ___37-[TKSmartCardSlotEngine setProtocol:]_block_invoke.214
- ___37-[TKSmartCardSlotEngine setProtocol:]_block_invoke.214.cold.1
- ___38-[TKSmartCardSlotEngine leaveSession:]_block_invoke.228
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke.306
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_2.307
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_3.308
- ___43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke.371
- ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.406
- ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.406.cold.1
- ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.409
- ___43-[TKSmartCardSessionEngine transmit:reply:]_block_invoke.409.cold.1
- ___46-[TKSmartCardSlotEngine scheduleIdlePowerDown]_block_invoke.218
- ___52-[TKSmartCardSlot simulateCardReinsertionWithError:]_block_invoke.229
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.211
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.211.cold.1
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.212
- ___55-[TKSmartCardSlot connectToEndpoint:synchronous:reply:]_block_invoke.212.cold.1
- ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.226
- ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.226.cold.1
- ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.226.cold.2
- ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.227
- ___58-[TKSmartCardSlotEngine connectCardSessionWithParameters:]_block_invoke.227.cold.1
- ___block_literal_global.209
- ___block_literal_global.212
- ___block_literal_global.216
- ___block_literal_global.217
- ___block_literal_global.221
- ___block_literal_global.241
- ___block_literal_global.310
- ___block_literal_global.319
- ___block_literal_global.331
- ___block_literal_global.344
- ___block_literal_global.349
- ___block_literal_global.405
- ___block_literal_global.408
- ___block_literal_global.411
- ___block_literal_global.441
- ___block_literal_global.899
CStrings:
+ "escape:reply:"
+ "sendEscape:reply:"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSData\">24"

```
