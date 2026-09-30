## com.apple.driver.usb.cdc.ncm

> `com.apple.driver.usb.cdc.ncm`

```diff

-404.0.0.0.0
-  __TEXT.__cstring: 0x2414
+404.40.2.0.0
+  __TEXT.__cstring: 0x248b
   __TEXT.__const: 0xca
-  __TEXT_EXEC.__text: 0xca0c
+  __TEXT_EXEC.__text: 0xcae8
   __TEXT_EXEC.__auth_stubs: 0x5c0
   __DATA.__data: 0xc8
   __DATA.__common: 0x100

   __DATA_CONST.__got: 0x88
   Functions: 355
   Symbols:   0
-  CStrings:  239
+  CStrings:  241
 
Functions:
~ sub_fffffe0009bf1ebc -> sub_fffffe0009bd39ac : 156 -> 252
~ __ZN15AppleUSBNCMData7armReadEP15InputPipeRecord : 404 -> 528
CStrings:
+ "Patching invalid NCM 1.1 NTB parameter wNdpInAlignment %d\n"
+ "Patching invalid NCM 1.1 NTB parameter wNdpOutAlignment %d\n"
```
