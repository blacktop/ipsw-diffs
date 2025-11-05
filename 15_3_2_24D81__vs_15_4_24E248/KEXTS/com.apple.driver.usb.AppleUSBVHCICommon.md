## com.apple.driver.usb.AppleUSBVHCICommon

> `com.apple.driver.usb.AppleUSBVHCICommon`

```diff

-1402.60.3.0.0
+1402.100.21.0.0
   __TEXT.__const: 0x24
   __TEXT.__cstring: 0x91f
   __TEXT.__os_log: 0x411
-  __TEXT_EXEC.__text: 0x4148
+  __TEXT_EXEC.__text: 0x4414
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0xd8

   __DATA_CONST.__mod_term_func: 0x28
   __DATA_CONST.__const: 0xd98
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 128FE568-9CF4-32D9-A79C-2AA3EFB2DACB
+  UUID: 0677FA8E-5CD8-37F1-AB96-4A44CB1145D3
   Functions: 126
   Symbols:   267
   CStrings:  64
Functions:
~ __ZN22AppleUSBVHCIEventQueue4initEv : 144 -> 148
~ __ZN23AppleUSBVHCIBufferQueue4initEv : 140 -> 144
~ __ZN23AppleUSBVHCIBufferQueue4freeEv : 124 -> 136
~ __ZN24AppleUSBVHCIMessageQueue4initEv : 144 -> 148
~ __ZN25AppleUSBVHCITransferQueue18initWithParametersEtjPKN15StandardUSBVHCI11VHCIMessageEP23AppleUSBVHCIBufferQueueP24AppleUSBVHCIMessageQueueP10IOWorkLoop : 956 -> 964
~ __ZN25AppleUSBVHCITransferQueue4freeEv : 628 -> 640
~ __ZN25AppleUSBVHCITransferQueue11sendMessageEPN15StandardUSBVHCI11VHCIMessageE : 192 -> 232
~ __ZN25AppleUSBVHCITransferQueue12storeMessageEPKN15StandardUSBVHCI11VHCIMessageEj : 164 -> 236
~ __ZN25AppleUSBVHCITransferQueue12getNextEventEv : 180 -> 228
~ __ZN25AppleUSBVHCITransferQueue12processEventEPKN15StandardUSBVHCI11VHCIMessageE : 224 -> 296
~ __ZN25AppleUSBVHCITransferQueue5closeEv : 488 -> 484
~ __ZN25AppleUSBVHCITransferQueue12abortRequestEi : 508 -> 500
~ __ZN25AppleUSBVHCITransferQueue16abortAllRequestsEiP9IOService : 656 -> 664
~ __ZN25AppleUSBVHCITransferQueue11hasRequestsEv : 20 -> 24
~ __ZN25AppleUSBVHCITransferQueue18pollForCompletionsEj : 1168 -> 1160
~ __ZN25AppleUSBVHCITransferQueue16activateRequestsEv : 648 -> 652
~ __ZN25AppleUSBVHCITransferQueue15completeRequestEP15AppleUSBRequest : 464 -> 468
~ __ZN25AppleUSBVHCITransferQueue13setQueueStateEN15StandardUSBVHCI18tVHCIEndpointStateE : 224 -> 272
~ __ZN24AppleUSBVHCICommandQueue4freeEv : 120 -> 124
~ __ZN24AppleUSBVHCICommandQueue21notifyCommandCompleteEPKN15StandardUSBVHCI11VHCIMessageE : 1308 -> 1404
~ __ZN24AppleUSBVHCICommandQueue14executeCommandEPN15StandardUSBVHCI11VHCIMessageEj : 2244 -> 2536

```
