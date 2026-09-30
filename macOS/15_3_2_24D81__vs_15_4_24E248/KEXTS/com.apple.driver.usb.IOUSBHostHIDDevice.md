## com.apple.driver.usb.IOUSBHostHIDDevice

> `com.apple.driver.usb.IOUSBHostHIDDevice`

```diff

-1402.60.3.0.0
+1402.100.21.0.0
   __TEXT.__cstring: 0xac4
   __TEXT.__os_log: 0x9af
-  __TEXT_EXEC.__text: 0x828c
+  __TEXT_EXEC.__text: 0x80ac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x1950
   __DATA_CONST.__kalloc_type: 0x200
-  UUID: 2099D88A-951F-3D56-AB8F-2F6C4496A2E6
+  UUID: FEB6D723-2580-3123-AF68-CCF0C3DAD790
   Functions: 106
   Symbols:   564
   CStrings:  140
Functions:
~ __ZN25AppleUSBHostBulkHIDDevice11handleStartEP9IOService : 1692 -> 1480
~ __ZN25AppleUSBHostBulkHIDDevice4freeEv : 168 -> 176
~ __ZN18IOUSBHostHIDDevice5startEP9IOService : 5412 -> 5364
~ __ZN18IOUSBHostHIDDevice4freeEv : 532 -> 536
~ __ZN18IOUSBHostHIDDevice11setPropertyEPK8OSSymbolP8OSObject : 1020 -> 1012
~ __ZN18IOUSBHostHIDDevice11handleStartEP9IOService : 3080 -> 3052
~ __ZNK18IOUSBHostHIDDevice20newCountryCodeNumberEv : 464 -> 460
~ __ZNK18IOUSBHostHIDDevice19newLocationIDNumberEv : 496 -> 492
~ __ZNK18IOUSBHostHIDDevice19newReportDescriptorEPP18IOMemoryDescriptor : 564 -> 560
~ __ZN18IOUSBHostHIDDevice9getReportEP18IOMemoryDescriptor15IOHIDReportTypej : 948 -> 932
~ __ZN18IOUSBHostHIDDevice9setReportEP18IOMemoryDescriptor15IOHIDReportTypej : 1004 -> 1000
~ __ZN18IOUSBHostHIDDevice9setReportEP18IOMemoryDescriptor15IOHIDReportTypejjP15IOHIDCompletion : 1940 -> 1932
~ __ZN18IOUSBHostHIDDevice16SetIdleMillisecsEt : 400 -> 396
~ __ZNK18IOUSBHostHIDDevice23newReportIntervalNumberEv : 748 -> 744
~ __ZN18IOUSBHostHIDDevice11setProtocolEt : 392 -> 388
~ __ZNK18IOUSBHostHIDDevice16getStringAtIndexEht : 736 -> 728
~ __ZNK18IOUSBHostHIDDevice16getHidDescriptorEhhPhPj : 592 -> 588
~ __ZNK18IOUSBHostHIDDevice21getHidDescriptorGatedEhhPhPj : 2528 -> 2452
~ __ZN18IOUSBHostHIDDevice22readInterruptPipeAsyncEv : 800 -> 796
~ __ZN18IOUSBHostHIDDevice27readInterruptPipeAsyncGatedEv : 2204 -> 2184
~ __ZN18IOUSBHostHIDDevice21interruptReadCompleteEPvij : 1956 -> 1936
~ __ZN18IOUSBHostHIDDevice14interruptRetryEP18IOTimerEventSource : 1084 -> 1072

```
