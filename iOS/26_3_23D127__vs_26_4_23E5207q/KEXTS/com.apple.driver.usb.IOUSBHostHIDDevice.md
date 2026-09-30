## com.apple.driver.usb.IOUSBHostHIDDevice

> `com.apple.driver.usb.IOUSBHostHIDDevice`

```diff

-1504.80.40.0.0
+1504.100.57.0.0
   __TEXT.__cstring: 0xac4
   __TEXT.__os_log: 0x9af
-  __TEXT_EXEC.__text: 0x7e1c
+  __TEXT_EXEC.__text: 0x71ac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf20
   __DATA_CONST.__kalloc_type: 0x200
-  UUID: 96858A1D-2977-38A2-8C8D-A2E7BA2EA345
+  UUID: 5D00E78E-0CF5-38A8-BBB9-0999AAA28433
   Functions: 86
   Symbols:   0
   CStrings:  140
Functions:
~ __ZN25AppleUSBHostBulkHIDDevice11handleStartEP9IOService : 1480 -> 1316
~ sub_fffffe000ad81280 -> sub_fffffe000a3b498c : 176 -> 160
~ __ZN18IOUSBHostHIDDevice5startEP9IOService : 5316 -> 4488
~ sub_fffffe000ad82b04 -> sub_fffffe000a3b5ec4 : 160 -> 152
~ sub_fffffe000ad82ba4 -> sub_fffffe000a3b5f5c : 320 -> 268
~ sub_fffffe000ad82ce4 -> sub_fffffe000a3b6068 : 536 -> 460
~ __ZN18IOUSBHostHIDDevice11setPropertyEPK8OSSymbolP8OSObject : 988 -> 832
~ sub_fffffe000ad832d8 -> sub_fffffe000a3b6574 : 32 -> 28
~ sub_fffffe000ad832f8 -> sub_fffffe000a3b6590 : 32 -> 28
~ sub_fffffe000ad83318 -> sub_fffffe000a3b65ac : 32 -> 28
~ sub_fffffe000ad83338 -> sub_fffffe000a3b65c8 : 32 -> 28
~ sub_fffffe000ad83358 -> sub_fffffe000a3b65e4 : 32 -> 28
~ sub_fffffe000ad83378 -> sub_fffffe000a3b6600 : 32 -> 28
~ __ZN18IOUSBHostHIDDevice11handleStartEP9IOService : 3024 -> 2736
~ sub_fffffe000ad84004 -> sub_fffffe000a3b7168 : 112 -> 104
~ sub_fffffe000ad84074 -> sub_fffffe000a3b71d0 : 112 -> 104
~ sub_fffffe000ad840e4 -> sub_fffffe000a3b7238 : 112 -> 104
~ sub_fffffe000ad84154 -> sub_fffffe000a3b72a0 : 460 -> 416
~ __ZNK18IOUSBHostHIDDevice19newLocationIDNumberEv : 484 -> 428
~ sub_fffffe000ad84504 -> sub_fffffe000a3b75ec : 176 -> 168
~ sub_fffffe000ad845b4 -> sub_fffffe000a3b7694 : 176 -> 168
~ sub_fffffe000ad84664 -> sub_fffffe000a3b773c : 176 -> 168
~ __ZNK18IOUSBHostHIDDevice19newReportDescriptorEPP18IOMemoryDescriptor : 560 -> 520
~ __ZN18IOUSBHostHIDDevice9getReportEP18IOMemoryDescriptor15IOHIDReportTypej : 916 -> 828
~ sub_fffffe000ad84ce8 -> sub_fffffe000a3b7d38 : 988 -> 928
~ __ZN18IOUSBHostHIDDevice9setReportEP18IOMemoryDescriptor15IOHIDReportTypejjP15IOHIDCompletion : 1904 -> 1764
~ sub_fffffe000ad85868 -> sub_fffffe000a3b87f0 : 396 -> 364
~ sub_fffffe000ad859f4 -> sub_fffffe000a3b895c : 392 -> 352
~ __ZNK18IOUSBHostHIDDevice23newReportIntervalNumberEv : 736 -> 624
~ sub_fffffe000ad85e94 -> sub_fffffe000a3b8d64 : 388 -> 356
~ __ZNK18IOUSBHostHIDDevice16getStringAtIndexEht : 728 -> 672
~ sub_fffffe000ad862f0 -> sub_fffffe000a3b9168 : 576 -> 552
~ __ZNK18IOUSBHostHIDDevice21getHidDescriptorGatedEhhPhPj : 2452 -> 2248
~ __ZN18IOUSBHostHIDDevice22readInterruptPipeAsyncEv : 784 -> 744
~ __ZN18IOUSBHostHIDDevice27readInterruptPipeAsyncGatedEv : 2172 -> 1940
~ __ZN18IOUSBHostHIDDevice21interruptReadCompleteEPvij : 1928 -> 1780
~ __ZN18IOUSBHostHIDDevice14interruptRetryEP18IOTimerEventSource : 1064 -> 904
~ sub_fffffe000ad88668 -> sub_fffffe000a3bb1b8 : 208 -> 192

```
