## com.apple.driver.usb.AppleUSBVHCIRSM

> `com.apple.driver.usb.AppleUSBVHCIRSM`

```diff

-1402.60.3.0.0
+1402.100.21.0.0
   __TEXT.__cstring: 0xafd
   __TEXT.__os_log: 0x195
-  __TEXT_EXEC.__text: 0x22ac
+  __TEXT_EXEC.__text: 0x22d4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xff0
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 28FCF9CA-03B1-3156-ACE9-43C758EE568B
+  UUID: 6CECB426-16A9-356A-9115-3C2A43BF0B69
   Functions: 62
   Symbols:   510
   CStrings:  31
Functions:
~ __ZN15AppleUSBVHCIRSM4freeEv : 184 -> 200
~ __ZN15AppleUSBVHCIRSM19stopThreadCallGatedEv : 656 -> 652
~ __ZN15AppleUSBVHCIRSM27maxCapabilityForDomainStateEm : 556 -> 552
~ __ZN15AppleUSBVHCIRSM17processInterruptsEN12AppleUSBVHCI14tInterruptMaskEb : 316 -> 324
~ __ZN15AppleUSBVHCIRSM17createBufferQueueEPKN15StandardUSBVHCI11VHCIMessageE : 864 -> 868
~ __ZN15AppleUSBVHCIRSM15pullReceiveDataEP26AppleUSBVHCIRSMBufferQueue : 2488 -> 2520
~ __ZN15AppleUSBVHCIRSM18rsmReceiveCallbackEP12IORSMChannelPKvyh : 624 -> 612

```
