## com.apple.iokit.IOUSBDeviceFamily

> `com.apple.iokit.IOUSBDeviceFamily`

```diff

-  __TEXT.__cstring: 0x3401
+  __TEXT.__cstring: 0x341d
   __TEXT.__const: 0x260
   __TEXT.__os_log: 0x21fc
-  __TEXT_EXEC.__text: 0x2c9f4
+  __TEXT_EXEC.__text: 0x2cabc
   __TEXT_EXEC.__auth_stubs: 0x700
   __DATA.__data: 0xc8
   __DATA.__common: 0x218

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 739
   Symbols:   1506
-  CStrings:  553
+  CStrings:  554
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ __ZZN21IOUSBDeviceController11freeRequestEP24_IOUSBDeviceIORequestTagE21kalloc_type_view_1824
+ __ZZN21IOUSBDeviceController15allocateRequestEvE21kalloc_type_view_1817
- __ZZN21IOUSBDeviceController11freeRequestEP24_IOUSBDeviceIORequestTagE21kalloc_type_view_1817
- __ZZN21IOUSBDeviceController15allocateRequestEvE21kalloc_type_view_1810
Functions:
~ __ZN20IOUSBDeviceInterface19copyDescriptorGatedEPNS_33tInternalCopyDescriptorParametersERi : 952 -> 1028
~ __ZN21IOUSBDeviceController15prepareDefaultsEP9IOService : 4516 -> 4640
CStrings:
+ "driver-registration-timeout"

```
