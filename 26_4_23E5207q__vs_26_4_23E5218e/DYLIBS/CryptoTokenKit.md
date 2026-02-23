## CryptoTokenKit

> `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit`

```diff

-805.100.40.0.0
-  __TEXT.__text: 0x487c8
+805.100.44.0.0
+  __TEXT.__text: 0x49b30
   __TEXT.__auth_stubs: 0xd00
   __TEXT.__delay_helper: 0x1f0
-  __TEXT.__objc_methlist: 0x4604
-  __TEXT.__gcc_except_tab: 0x15fc
-  __TEXT.__const: 0x2a0
-  __TEXT.__cstring: 0x2ce6
-  __TEXT.__oslogstring: 0x3487
+  __TEXT.__objc_methlist: 0x4634
+  __TEXT.__gcc_except_tab: 0x1648
+  __TEXT.__const: 0x2b8
+  __TEXT.__cstring: 0x2cf0
+  __TEXT.__oslogstring: 0x34c9
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__swift5_typeref: 0x2a
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x1788
+  __TEXT.__unwind_info: 0x17b0
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0xc19
-  __TEXT.__objc_methname: 0x8d28
-  __TEXT.__objc_methtype: 0x220b
-  __TEXT.__objc_stubs: 0x6980
+  __TEXT.__objc_methname: 0x8e48
+  __TEXT.__objc_methtype: 0x227b
+  __TEXT.__objc_stubs: 0x69c0
   __DATA_CONST.__got: 0x5e8
-  __DATA_CONST.__const: 0x16e0
+  __DATA_CONST.__const: 0x17d0
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2160
+  __DATA_CONST.__objc_selrefs: 0x2188
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x690
   __AUTH_CONST.__const: 0xb18
   __AUTH_CONST.__cfstring: 0x2580
-  __AUTH_CONST.__objc_const: 0x8618
+  __AUTH_CONST.__objc_const: 0x8638
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x570
+  __DATA.__objc_ivar: 0x574
   __DATA.__data: 0xe64
   __DATA.__bss: 0x1c8
   __DATA.__common: 0x11

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: CCA237B8-F5CA-35CE-B0A0-58C31B134673
-  Functions: 2017
-  Symbols:   7148
-  CStrings:  3090
+  UUID: E98A1B63-F474-3678-ADD8-9C795D35CBD9
+  Functions: 2029
+  Symbols:   7185
+  CStrings:  3101
 
Symbols:
+ -[TKSmartCard calculateChunkInfoForIns:data:offset:chained:isCase4:]
+ -[TKSmartCard handleApduResponse:body:le:isCase4:synchronous:error:reply:]
+ -[TKSmartCard inSlotQueueExecuteBlock:synchronous:]
+ -[TKSmartCard querySessionSynchronous:reply:]
+ -[TKSmartCard querySessionSynchronous:reply:].cold.1
+ -[TKSmartCard remoteSessionWithErrorHandler:synchronous:]
+ -[TKSmartCard transmitRequest:synchronous:reply:]
+ -[TKSmartCard transmitRequest:synchronous:reply:].cold.1
+ -[TKSmartCard transmitRequest:synchronous:reply:].cold.2
+ -[TKSmartCard transmitRequest:synchronous:reply:].cold.3
+ -[TKSmartCard transmitSynchronouslyChunkedIns:p1:p2:data:offset:realLe:chained:isCase4:responseBody:sw:error:]
+ -[TKSmartCard validateSendInsPreconditionsWithError:]
+ -[TKSmartCard validateSendInsPreconditionsWithError:].cold.1
+ GCC_except_table143
+ GCC_except_table174
+ GCC_except_table178
+ _OBJC_IVAR_$_TKSmartCard._apduQueue
+ ___110-[TKSmartCard transmitSynchronouslyChunkedIns:p1:p2:data:offset:realLe:chained:isCase4:responseBody:sw:error:]_block_invoke
+ ___110-[TKSmartCard transmitSynchronouslyChunkedIns:p1:p2:data:offset:realLe:chained:isCase4:responseBody:sw:error:]_block_invoke_2
+ ___110-[TKSmartCard transmitSynchronouslyChunkedIns:p1:p2:data:offset:realLe:chained:isCase4:responseBody:sw:error:]_block_invoke_3
+ ___110-[TKSmartCard transmitSynchronouslyChunkedIns:p1:p2:data:offset:realLe:chained:isCase4:responseBody:sw:error:]_block_invoke_4
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke.310
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_2.311
+ ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_3.312
+ ___43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke.375
+ ___43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke_2
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke.316
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke.318
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke.320
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke.325
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke_2
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke_2.317
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke_2.317.cold.1
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke_2.319
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke_2.319.cold.1
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke_2.324
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke_2.324.cold.1
+ ___45-[TKSmartCard querySessionSynchronous:reply:]_block_invoke_2.cold.1
+ ___46-[TKSmartCard sendIns:p1:p2:data:le:sw:error:]_block_invoke_2
+ ___46-[TKSmartCard sendIns:p1:p2:data:le:sw:error:]_block_invoke_3
+ ___49-[TKSmartCard transmitRequest:synchronous:reply:]_block_invoke
+ ___49-[TKSmartCard transmitRequest:synchronous:reply:]_block_invoke.340
+ ___49-[TKSmartCard transmitRequest:synchronous:reply:]_block_invoke.cold.1
+ ___74-[TKSmartCard handleApduResponse:body:le:isCase4:synchronous:error:reply:]_block_invoke
+ ___85-[TKSmartCard transmitChunkedIns:p1:p2:data:fromOffset:realLe:chained:isCase4:reply:]_block_invoke_3
+ ___block_descriptor_108_e8_32s40s48bs56w_e5_v8?0lw56l8s32l8s48l8s40l8
+ ___block_descriptor_108_e8_32s40s48s56bs_e28_v24?0"NSData"8"NSError"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_108_e8_32s40s48s56r64r72r80r88r_e5_v8?0lr56l8s32l8r64l8r72l8r80l8r88l8s40l8s48l8
+ ___block_descriptor_49_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e67_v32?0"<TKProtocolSmartCardSession>"8"NSDictionary"16"NSError"24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40r48r_e31_v28?0"NSData"8S16"NSError"20ls32l8r40l8r48l8
+ ___block_descriptor_65_e8_32s40s48bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_67_e8_32s40s48bs56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40r48r56r_e28_v24?0"NSData"8"NSError"16ls32l8r40l8r48l8r56l8
+ ___block_literal_global.314
+ ___block_literal_global.323
+ ___block_literal_global.335
+ ___block_literal_global.348
+ ___block_literal_global.351
+ ___block_literal_global.353
+ ___block_literal_global.912
+ _objc_msgSend$calculateChunkInfoForIns:data:offset:chained:isCase4:
+ _objc_msgSend$handleApduResponse:body:le:isCase4:synchronous:error:reply:
+ _objc_msgSend$inSlotQueueExecuteBlock:synchronous:
+ _objc_msgSend$querySessionSynchronous:reply:
+ _objc_msgSend$remoteSessionWithErrorHandler:synchronous:
+ _objc_msgSend$setData:
+ _objc_msgSend$transmitRequest:synchronous:reply:
+ _objc_msgSend$transmitSynchronouslyChunkedIns:p1:p2:data:offset:realLe:chained:isCase4:responseBody:sw:error:
+ _objc_msgSend$validateSendInsPreconditionsWithError:
- -[TKSmartCard handleApduResponse:body:le:isCase4:error:reply:]
- -[TKSmartCard inSlotQueueExecuteBlock:]
- -[TKSmartCard querySessionWithReply:]
- -[TKSmartCard querySessionWithReply:].cold.1
- -[TKSmartCard remoteSessionWithErrorHandler:]
- -[TKSmartCard sendIns:p1:p2:data:le:reply:].cold.1
- -[TKSmartCard transmitRequest:reply:].cold.1
- -[TKSmartCard transmitRequest:reply:].cold.2
- -[TKSmartCard transmitRequest:reply:].cold.3
- GCC_except_table142
- GCC_except_table163
- GCC_except_table166
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.315
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.317
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.319
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke.324
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.316
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.316.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.318
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.318.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.323
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.323.cold.1
- ___37-[TKSmartCard querySessionWithReply:]_block_invoke_2.cold.1
- ___37-[TKSmartCard transmitRequest:reply:]_block_invoke
- ___37-[TKSmartCard transmitRequest:reply:]_block_invoke.339
- ___37-[TKSmartCard transmitRequest:reply:]_block_invoke.cold.1
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke.309
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_2.310
- ___39-[TKSmartCard releaseSessionWithReply:]_block_invoke_3.311
- ___43-[TKSmartCard sendIns:p1:p2:data:le:reply:]_block_invoke.374
- ___62-[TKSmartCard handleApduResponse:body:le:isCase4:error:reply:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e67_v32?0"<TKProtocolSmartCardSession>"8"NSDictionary"16"NSError"24ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_94_e8_32s40s48bs56r_e28_v24?0"NSData"8"NSError"16ls32l8s48l8s40l8r56l8
- ___block_literal_global.313
- ___block_literal_global.322
- ___block_literal_global.334
- ___block_literal_global.350
- ___block_literal_global.352
- ___block_literal_global.902
- _objc_msgSend$handleApduResponse:body:le:isCase4:error:reply:
- _objc_msgSend$inSlotQueueExecuteBlock:
- _objc_msgSend$querySessionWithReply:
- _objc_msgSend$remoteSessionWithErrorHandler:
- _objc_msgSend$setSynchronous:
- _objc_msgSend$synchronous
- _objc_msgSend$transmitRequest:reply:
CStrings:
+ "%{public}@: transmitRequest got reply len=%lu %{private}@ (err=%{public}@)"
+ "%{public}@: transmitRequest: len=%lu %{private}@"
+ "/Library/Caches/com.apple.xbs/BFFB2279-F3E0-47A0-BD38-A44DAD2DFC5B/TemporaryDirectory.pT4o9R/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/Library/Caches/com.apple.xbs/BFFB2279-F3E0-47A0-BD38-A44DAD2DFC5B/TemporaryDirectory.pT4o9R/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/BFFB2279-F3E0-47A0-BD38-A44DAD2DFC5B/TemporaryDirectory.pT4o9R/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "@28@0:8@?16B24"
+ "B84@0:8C16C20C24@28^Q36Q44B52B56@60^S68^@76"
+ "_apduQueue"
+ "apduQueue"
+ "calculateChunkInfoForIns:data:offset:chained:isCase4:"
+ "handleApduResponse:body:le:isCase4:synchronous:error:reply:"
+ "inSlotQueueExecuteBlock:synchronous:"
+ "querySessionSynchronous:reply:"
+ "remoteSessionWithErrorHandler:synchronous:"
+ "rsp: %04x len:%lu %{private}@"
+ "setData:"
+ "sync req: %02x %02x%02x len=%lu %{private}@ le:%@"
+ "transmitRequest:synchronous:reply:"
+ "transmitSynchronouslyChunkedIns:p1:p2:data:offset:realLe:chained:isCase4:responseBody:sw:error:"
+ "v28@0:8@?16B24"
+ "v64@0:8@16@24Q32B40B44@48@?56"
+ "validateSendInsPreconditionsWithError:"
+ "{?={_NSRange=QQ}QBB}44@0:8C16@20Q28B36B40"
- "%{public}@: transmitRequest got reply %@ (err=%{public}@)"
- "%{public}@: transmitRequest:%@"
- "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/Library/Caches/com.apple.xbs/91704D56-10B0-4F78-9261-2D8182226F2A/TemporaryDirectory.Ypy3IC/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "handleApduResponse:body:le:isCase4:error:reply:"
- "inSlotQueueExecuteBlock:"
- "querySessionWithReply:"
- "remoteSessionWithErrorHandler:"
- "req: %02x %02x%02x %@ le:%@"
- "rsp: %04x len:%lu:%@"
- "v60@0:8@16@24Q32B40@44@?52"

```
