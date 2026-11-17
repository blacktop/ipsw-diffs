## com.apple.driver.AppleUSBLightningAdapter

> `com.apple.driver.AppleUSBLightningAdapter`

```diff

-95.0.0.0.0
+95.60.2.0.0
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x135b
-  __TEXT.__os_log: 0xdbe
-  __TEXT_EXEC.__text: 0x5ce0
+  __TEXT.__os_log: 0xdf0
+  __TEXT_EXEC.__text: 0x5cec
   __TEXT_EXEC.__auth_stubs: 0x350
   __DATA.__data: 0xc4
   __DATA.__common: 0x60

   __DATA_CONST.__got: 0xa8
   Functions: 107
   Symbols:   0
-  CStrings:  180
+  CStrings:  181
 
Functions:
~ __ZN27AppleUSBLightningAdapterBOS18_getCapabilityDataEPKN11StandardUSB13BOSDescriptorE : 508 -> 504
~ sub_A1B0 -> sub_fffffe0009be76a0 : 44 -> 60
CStrings:
+ "!capabilityData"
+ "Could not find capabilityData!"
+ "Invalid platform descriptor length for MikeyBus info! (bLength: %u, expectedDescriptorLength: %u)"
+ "Invalid platform descriptor length! (bLength: %u, expectedDescriptorBaseLength: %u)"
+ "capabilityData->supportedFields: 0x%04X"
- "!pCapabilityData"
- "Could not find pCapabilityData!"
- "Invalid platform descriptor length!"
- "pCapabilityData->supportedFields: 0x%04X"
```
