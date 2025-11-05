## com.apple.driver.usb.AppleUSBVHCICommonRSM

> `com.apple.driver.usb.AppleUSBVHCICommonRSM`

```diff

-1402.60.3.0.0
+1402.100.21.0.0
   __TEXT.__cstring: 0x13f8
   __TEXT.__os_log: 0x7f4
-  __TEXT_EXEC.__text: 0x5588
+  __TEXT_EXEC.__text: 0x5760
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x810
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: 2DAF2538-C5F2-3181-8CEF-511A35003781
+  UUID: D9583E7F-4E1F-3A51-BC94-729580CF7E23
   Functions: 92
   Symbols:   248
   CStrings:  84
Functions:
~ __ZN26AppleUSBVHCIRSMBufferQueue18initWithParametersEN23AppleUSBVHCIBufferQueue16tBufferQueueRoleEP12IORSMChannelPKN15StandardUSBVHCI11VHCIMessageEP22IOInterruptEventSource : 636 -> 640
~ __ZN26AppleUSBVHCIRSMBufferQueue4freeEv : 516 -> 512
~ __ZN26AppleUSBVHCIRSMBufferQueue5closeEv : 352 -> 356
~ __ZN26AppleUSBVHCIRSMBufferQueue14transferBufferEP18IOMemoryDescriptoryyj : 1688 -> 1704
~ __ZN26AppleUSBVHCIRSMBufferQueue13cancelBuffersEv : 1164 -> 1188
~ __ZN26AppleUSBVHCIRSMBufferQueue12getNextEventEv : 3144 -> 3120
~ __ZN26AppleUSBVHCIRSMBufferQueue11receiveDataEP22IORSMReceiveQueueEntry : 432 -> 416
~ __ZN26AppleUSBVHCIRSMBufferQueue13outCompletionEPP18IOMemoryDescriptori : 764 -> 772
~ __ZN27AppleUSBVHCIRSMMessageQueue18initWithParametersEP12IORSMChannelhP22IOInterruptEventSource : 296 -> 280
~ __ZN27AppleUSBVHCIRSMMessageQueue4freeEv : 232 -> 248
~ __ZN27AppleUSBVHCIRSMMessageQueue7disableEv : 1576 -> 1712
~ __ZN27AppleUSBVHCIRSMMessageQueue11sendMessageEPKN15StandardUSBVHCI11VHCIMessageEj : 3008 -> 3148
~ __ZN27AppleUSBVHCIRSMMessageQueue18processCompletionsEv : 760 -> 864
~ __ZN27AppleUSBVHCIRSMMessageQueue10completionEPN24AppleUSBVHCIMessageQueue14tMessageRecordEi : 1120 -> 1136
~ __ZN25AppleUSBVHCIRSMEventQueue18initWithParametersEh : 68 -> 72
~ __ZN25AppleUSBVHCIRSMEventQueue7disableEv : 524 -> 520
~ __ZN25AppleUSBVHCIRSMEventQueue12receiveEventEPKN15StandardUSBVHCI11VHCIMessageE : 1188 -> 1220
~ __ZN25AppleUSBVHCIRSMEventQueue12getNextEventEv : 408 -> 440

```
