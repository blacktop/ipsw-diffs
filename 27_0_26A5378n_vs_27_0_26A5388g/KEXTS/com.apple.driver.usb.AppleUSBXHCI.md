## com.apple.driver.usb.AppleUSBXHCI

> `com.apple.driver.usb.AppleUSBXHCI`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-1617.0.3.0.0
-  __TEXT.__cstring: 0x5743
+1617.0.9.0.0
+  __TEXT.__cstring: 0x5722
   __TEXT.__os_log: 0x50f0
   __TEXT.__const: 0xb4
-  __TEXT_EXEC.__text: 0x4b114
+  __TEXT_EXEC.__text: 0x4b02c
   __TEXT_EXEC.__auth_stubs: 0x720
   __DATA.__data: 0xc8
   __DATA.__common: 0x3f8

   __DATA_CONST.__got: 0x120
   Functions: 844
   Symbols:   2288
-  CStrings:  550
+  CStrings:  548
 
Symbols:
+ __ZN19AppleUSBRequestPool15gatedGetCommandEPP9IOCommandb
- __ZN13IOCommandPool15gatedGetCommandEPP9IOCommandb
Functions:
~ __ZN30AppleUSBXHCIIsochronousRequest7prepareEv : 13120 -> 13264
~ __ZN16AppleUSBXHCIPort20initWithDeviceMemoryEP14IODeviceMemoryPN15StandardUSBXHCI33StandardUSBXHCIProtocolCapabilityEP15IORegistryEntry : 1572 -> 1384
~ __ZN16AppleUSBXHCIPort20initWithDeviceMemoryEP14IODeviceMemoryPN15StandardUSBXHCI33StandardUSBXHCIProtocolCapabilityEP12OSDictionary : 1184 -> 996
CStrings:
- "UsbCPortNumber"
- "usb-c-port-number"
```
