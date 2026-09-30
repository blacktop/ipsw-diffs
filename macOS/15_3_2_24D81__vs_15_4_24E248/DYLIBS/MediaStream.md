## MediaStream

> `/System/Library/PrivateFrameworks/MediaStream.framework/Versions/A/MediaStream`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x15e78
+751.0.104.0.0
+  __TEXT.__text: 0x15e28
   __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x1460
+  __TEXT.__objc_methlist: 0x18e4
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x110
   __TEXT.__oslogstring: 0x172c
   __TEXT.__cstring: 0x10fa
   __TEXT.__ustring: 0x74
-  __TEXT.__unwind_info: 0x778
+  __TEXT.__unwind_info: 0x780
   __TEXT.__objc_classname: 0x263
   __TEXT.__objc_methname: 0x4185
   __TEXT.__objc_methtype: 0xa21

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe30
+  __DATA_CONST.__objc_selrefs: 0xee0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
   __AUTH_CONST.__auth_got: 0x380
   __AUTH_CONST.__const: 0xac0
   __AUTH_CONST.__cfstring: 0xf00
-  __AUTH_CONST.__objc_const: 0x2a40
+  __AUTH_CONST.__objc_const: 0x21d0
   __AUTH.__objc_data: 0x690
   __DATA.__objc_ivar: 0x14c
   __DATA.__data: 0x308

   - /System/Library/PrivateFrameworks/CoreMediaStream.framework/Versions/A/CoreMediaStream
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5352CC23-2FDB-333A-978C-ABC673804FFC
+  UUID: F837C8AA-49BA-3916-85E4-593161EAC403
   Functions: 609
   Symbols:   1581
   CStrings:  1137
Functions:
~ -[MSMSPlatform init] : 320 -> 316
~ -[XPCServiceListener initWithServiceName:queue:delegate:] : 520 -> 516
~ -[XPCNSClientConnection sendMessage:data:withHandler:] : 360 -> 356
~ __insertMessage : 648 -> 644
~ -[XPCClientConnection _reallySendMessage:handler:sequence:retryCount:] : 852 -> 848
~ ___72-[MSAuthenticationManager didEncounterAuthenticationFailureForPersonID:]_block_invoke_2 : 396 -> 392
~ __72-[MSAuthenticationManager didEncounterAuthenticationFailureForPersonID:]_block_invoke_2.14 : 236 -> 240
~ -[MSConnection init] : 368 -> 364
~ -[MSMSPlatform _mayPerformFileTransfer] : 128 -> 136
~ -[MSPauseManager _removeTimerUUID:] : 240 -> 236
~ -[MSPauseManager pingPauseUUID:] : 448 -> 436
~ ___48-[MSASConnection setIsUIForeground:forPersonID:]_block_invoke : 484 -> 488
~ ___42-[MSPowerBudget setIsFileTransferAllowed:]_block_invoke : 380 -> 384
~ -[MSASPlatformImplementation MSASPersonIDIsAllowedToDownloadAssets:] : 432 -> 420
~ -[MSASPlatformImplementation MSASIsAllowedToUploadAssets] : 236 -> 220
~ -[MSASPlatformImplementation MSASIsAllowedToTransferMetadata] : 236 -> 220
~ -[XPCRequest initWithMessage:sequence:connection:] : 396 -> 392
~ -[XPCServiceConnection workQueueShutDown] : 244 -> 240
~ -[XPCNSServiceConnection XPCServiceConnection:didReceiveRequest:sequenceNumber:] : 160 -> 156

```
