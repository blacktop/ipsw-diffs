## com.apple.iokit.IOAccessoryPortUSB

> `com.apple.iokit.IOAccessoryPortUSB`

```diff

-1004.80.3.0.1
+1016.100.10.0.0
   __TEXT.__cstring: 0x651
-  __TEXT_EXEC.__text: 0x2850
+  __TEXT_EXEC.__text: 0x2934
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x20a
   __DATA.__common: 0x48

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0xa00
   __DATA_CONST.__kalloc_type: 0x40
-  UUID: A3E0AEC3-C85F-31EB-A11B-118A7225559B
-  Functions: 43
-  Symbols:   398
+  UUID: C6ACD9D2-F8D6-3CD4-A30E-00DE32CE301E
+  Functions: 46
+  Symbols:   401
   CStrings:  51
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _ZN18IOAccessoryPortUSB7messageEjP9IOServicePv.cold.1
+ _ZN18IOAccessoryPortUSB7messageEjP9IOServicePv.cold.2
Functions:
- __ZN18IOAccessoryPortUSB23usbRoleSwitchThreadCallEPvS0_
~ __ZN18IOAccessoryPortUSB14controlRequestEP22IOUSBDeviceSetupPacketPiPP18IOMemoryDescriptorPyP28IOUSBDeviceControlCompletion : 2092 -> 2168
~ __ZN18IOAccessoryPortUSB4freeEv : 384 -> 388
- __ZN18IOAccessoryPortUSB12isIgnoreVBUSEv
~ __ZN18IOAccessoryPortUSB17transmitDataGatedEP18IOMemoryDescriptorj : 1252 -> 1256
- __ZN18IOAccessoryPortUSB24controlReceiveCompletionEPviyP18IOMemoryDescriptor
~ __ZN18IOAccessoryPortUSB20setUSBRoleSwitchMaskEtt : 152 -> 144
~ __ZN18IOAccessoryPortUSB7messageEjP9IOServicePv : 440 -> 276
+ _OUTLINED_FUNCTION_0

```
