## com.apple.iokit.IOUSBHostFamily

> `com.apple.iokit.IOUSBHostFamily`

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
-  __TEXT.__cstring: 0xa538
-  __TEXT.__os_log: 0x87c2
+1617.0.9.0.0
+  __TEXT.__cstring: 0xa41b
+  __TEXT.__os_log: 0x8717
   __TEXT.__const: 0x2018
-  __TEXT_EXEC.__text: 0x9ac74
+  __TEXT_EXEC.__text: 0x9ac18
   __TEXT_EXEC.__auth_stubs: 0xd50
   __DATA.__data: 0x1f0
   __DATA.__common: 0x970

   __DATA_CONST.__auth_got: 0x6a8
   __DATA_CONST.__got: 0x1f0
   Functions: 2334
-  Symbols:   4171
-  CStrings:  1159
+  Symbols:   4169
+  CStrings:  1156
 
Symbols:
+ __ZN19AppleUSBRequestPool15gatedGetCommandEPP9IOCommandb
- __ZN13IOCommandPool15gatedGetCommandEPP9IOCommandb
- __ZZN26AppleUSBHostResourcesTypeC33allocateDownstreamBusCurrentGatedEP9IOServiceRjS2_E11_os_log_fmt_1
- __ZZN26AppleUSBHostResourcesTypeC33allocateDownstreamBusCurrentGatedEP9IOServiceRjS2_E11_os_log_fmt_2
Functions:
~ __ZN11StandardUSB27getNextCapabilityDescriptorEPKNS_13BOSDescriptorEPKNS_26DeviceCapabilityDescriptorE : 100 -> 148
~ __ZN11StandardUSB35validateDeviceCapabilityDescriptorsEPKNS_13BOSDescriptorE : 252 -> 272
~ __ZN26AppleUSBHostResourcesTypeC33allocateDownstreamBusCurrentGatedEP9IOServiceRjS2_ : 2564 -> 2404
CStrings:
+ "smc-port-number"
+ "usb-c-port-number"
- "%s@%s: %s::%s: Client %p is requesting %umA wake and %umA sleep for port %u\n"
- "%s@%s: %s::%s: Client %p port %u has EDT current overrides of %umA wake and %umA sleep\n"
- "%s@%s: %s::%s: Granting %umA wake and %umA sleep based on override for port %u\n"
- "%s@%s: %s::%s: Port %u %umA/%umA wake and %umA/%umA sleep\n"
- "UsbCPortNumber"
```
