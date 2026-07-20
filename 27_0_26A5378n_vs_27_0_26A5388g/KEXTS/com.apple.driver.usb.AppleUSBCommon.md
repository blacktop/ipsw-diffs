## com.apple.driver.usb.AppleUSBCommon

> `com.apple.driver.usb.AppleUSBCommon`

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
+1617.0.9.0.0
   __TEXT.__cstring: 0x365
   __TEXT.__const: 0x18
   __TEXT.__os_log: 0xef
-  __TEXT_EXEC.__text: 0x5f38
+  __TEXT_EXEC.__text: 0x606c
   __TEXT_EXEC.__auth_stubs: 0x3a0
   __DATA.__data: 0xc8
   __DATA.__common: 0x110

   __DATA_CONST.__kalloc_var: 0x140
   __DATA_CONST.__auth_got: 0x1d0
   __DATA_CONST.__got: 0x90
-  Functions: 218
+  Functions: 219
   Symbols:   444
   CStrings:  47
 
Symbols:
+ __ZN19AppleUSBRequestPool15gatedGetCommandEPP9IOCommandb
- __ZN13IOCommandPool15gatedGetCommandEPP9IOCommandb
Functions:
~ __ZN19AppleUSBRequestPool9gatedStopEv : 328 -> 372
~ __ZN19AppleUSBRequestPool10getCommandEb : 276 -> 140
+ __ZN19AppleUSBRequestPool15gatedGetCommandEPP9IOCommandb
~ __ZN19AppleUSBRequestPool13getCopyBufferEv : 192 -> 252
~ __ZN19AppleUSBRequestPool16returnCopyBufferEP24IOBufferMemoryDescriptor : 148 -> 220
~ __ZN19AppleUSBRequestPool13getDMACommandEv : 172 -> 208
~ __ZN19AppleUSBRequestPool16returnDMACommandEP12IODMACommand : 148 -> 220
```
