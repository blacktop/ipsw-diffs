## com.apple.driver.usb.AppleUSBVHCI

> `com.apple.driver.usb.AppleUSBVHCI`

```diff

-  __TEXT.__cstring: 0x26c8
+  __TEXT.__cstring: 0x26c7
   __TEXT.__os_log: 0x1aea
   __TEXT.__const: 0x50
   __TEXT_EXEC.__text: 0x19a9c

   __DATA.__common: 0x240
   __DATA_CONST.__mod_init_func: 0x48
   __DATA_CONST.__mod_term_func: 0x48
-  __DATA_CONST.__const: 0x4e98
+  __DATA_CONST.__const: 0x4ea8
   __DATA_CONST.__kalloc_type: 0x380
   __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0xd0
   Functions: 438
-  Symbols:   1511
+  Symbols:   1513
   CStrings:  345
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __ZN22AppleUSBHostController18addMapperReferenceEv
+ __ZN22AppleUSBHostController19deferBufferTeardownEP24IOBufferMemoryDescriptor
+ __ZN22AppleUSBHostController20blockMapperReferenceEv
+ __ZN22AppleUSBHostController21tryAddMapperReferenceEv
+ __ZN22AppleUSBHostController22unblockMapperReferenceEv
- __ZN22AppleUSBHostController14registerBufferEP24IOBufferMemoryDescriptor
- __ZN22AppleUSBHostController16unregisterBufferEP24IOBufferMemoryDescriptor
- __ZN22AppleUSBHostController18addMapperReferenceEb
CStrings:
+ "12111112122212121121111122222222222222222222222222222222222222222222222222222222222222221212112111112222222222222222121122222222222222222222222222222222222222222222222221211111111122212222222212111111111111121111111111111111111111111111111122"
- "121111121222121211211111222222222222222222222222222222222222222222222222222222222222222212121121111122222222222222221211222222222222222222222222222222222222222222222222212111111111222112222222212111111111111121111111111111111111111111111111122"

```
