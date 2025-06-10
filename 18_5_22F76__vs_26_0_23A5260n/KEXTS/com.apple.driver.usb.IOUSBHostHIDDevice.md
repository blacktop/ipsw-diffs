## com.apple.driver.usb.IOUSBHostHIDDevice

> `com.apple.driver.usb.IOUSBHostHIDDevice`

```diff

-1402.100.21.0.0
+1493.0.6.0.0
   __TEXT.__cstring: 0xac4
   __TEXT.__os_log: 0x9af
-  __TEXT_EXEC.__text: 0x7e34
+  __TEXT_EXEC.__text: 0x7e1c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf20
   __DATA_CONST.__kalloc_type: 0x200
-  UUID: A71AC364-19C5-3D42-B939-E951A696CE29
+  UUID: C8FA3780-48C8-3517-9BD8-365AEDDFA739
   Functions: 86
   Symbols:   0
   CStrings:  140
Functions:
~ __ZN18IOUSBHostHIDDevice11handleStartEP9IOService : 3036 -> 3024
~ sub_fffffff00a82a9d4 -> sub_fffffff00ac4c4d8 : 984 -> 988
~ __ZN18IOUSBHostHIDDevice9setReportEP18IOMemoryDescriptor15IOHIDReportTypejjP15IOHIDCompletion : 1908 -> 1904
~ sub_fffffff00a82bfdc -> sub_fffffff00ac4dae0 : 580 -> 576
~ __ZN18IOUSBHostHIDDevice22readInterruptPipeAsyncEv : 788 -> 784
~ __ZN18IOUSBHostHIDDevice27readInterruptPipeAsyncGatedEv : 2176 -> 2172

```
