## AppleEthernetRL

> `/System/Library/Extensions/AppleEthernetRL.kext/AppleEthernetRL`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-175.40.1.0.0
+175.40.2.0.0
   __TEXT.__cstring: 0x2ad5
   __TEXT.__const: 0x22888
   __TEXT.__os_log: 0x75
-  __TEXT_EXEC.__text: 0x27b60
+  __TEXT_EXEC.__text: 0x27bf0
   __TEXT_EXEC.__auth_stubs: 0x720
   __DATA.__data: 0x1e8
   __DATA.__common: 0x128

   __DATA_CONST.__kalloc_var: 0x320
   __DATA_CONST.__auth_got: 0x390
   __DATA_CONST.__got: 0xc0
-  Functions: 580
+  Functions: 581
   Symbols:   1154
   CStrings:  344
 
Symbols:
+ __Z10re_rar_setP8re_softcPh
+ __ZN15AppleEthernetRL18setHardwareAddressEP10ether_addr
- __ZL10re_rar_setP8re_softcPh
- __ZN26IOSkywalkEthernetInterface18setHardwareAddressEP10ether_addr
Functions:
+ __Z10re_rar_setP8re_softcPh
- __ZL10re_rar_setP8re_softcPh
+ __ZN15AppleEthernetRL18setHardwareAddressEP10ether_addr
```
