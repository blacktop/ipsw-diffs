## com.apple.iokit.IOAccessoryPortUSB

> `com.apple.iokit.IOAccessoryPortUSB`

```diff

-1044.40.2.0.0
+1044.100.2.0.0
   __TEXT.__cstring: 0x651
-  __TEXT_EXEC.__text: 0x28bc
+  __TEXT_EXEC.__text: 0x2524
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x20a
   __DATA.__common: 0x48

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x640
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: 5E39D8CC-CAB1-3329-99A4-A85DECC05B9B
+  UUID: 1C3FB527-2220-3EFC-BE7A-3F3DB8FEC727
   Functions: 46
   Symbols:   0
   CStrings:  51
Functions:
~ __ZN18IOAccessoryPortUSB5startEP9IOService : 1812 -> 1656
~ __ZN18IOAccessoryPortUSB24ignoreVbusDropThreadCallEPvS0_ : 444 -> 400
~ __ZN18IOAccessoryPortUSB14controlRequestEP22IOUSBDeviceSetupPacketPiPP18IOMemoryDescriptorPyP28IOUSBDeviceControlCompletion : 2168 -> 1896
~ sub_fffffe000a51e184 -> sub_fffffe0009bfebfc : 176 -> 168
~ sub_fffffe000a51e234 -> sub_fffffe0009bfeca4 : 380 -> 336
~ sub_fffffe000a51e3b0 -> sub_fffffe0009bfedf4 : 440 -> 408
~ __ZN18IOAccessoryPortUSB17transmitDataGatedEP18IOMemoryDescriptorj : 1204 -> 996
~ __ZN18IOAccessoryPortUSB12waitSendDoneEj : 104 -> 96
~ __ZN18IOAccessoryPortUSB19receiveNotificationEPvjP9IOServiceS0_m : 692 -> 636
~ __ZN18IOAccessoryPortUSB20setUSBRoleSwitchMaskEtt : 144 -> 136
~ sub_fffffe000a51ef84 -> sub_fffffe0009bff890 : 276 -> 268
~ __ZN18IOAccessoryPortUSB23usbRoleSwitchThreadCallEPvS0_ : 192 -> 184
~ sub_fffffe000a51f284 -> sub_fffffe0009bffb80 : 240 -> 220
~ __ZN18IOAccessoryPortUSB24controlReceiveCompletionEPviyP18IOMemoryDescriptor : 360 -> 328
~ __ZN18IOAccessoryPortUSB7messageEjP9IOServicePv.cold.1 : 180 -> 172
~ sub_fffffe000a51f590 -> sub_fffffe0009bffe50 : 140 -> 132

```
