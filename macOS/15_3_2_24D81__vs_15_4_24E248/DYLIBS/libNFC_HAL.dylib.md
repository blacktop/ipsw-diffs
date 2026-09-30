## libNFC_HAL.dylib

> `/usr/lib/libNFC_HAL.dylib`

```diff

-353.3.0.0.0
-  __TEXT.__text: 0x16224
+354.27.0.0.0
+  __TEXT.__text: 0x16534
   __TEXT.__auth_stubs: 0x7c0
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x2777
+  __TEXT.__cstring: 0x278b
   __TEXT.__oslogstring: 0x1fc5
-  __TEXT.__unwind_info: 0x280
+  __TEXT.__unwind_info: 0x248
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x208
   __AUTH_CONST.__auth_got: 0x3e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  UUID: AA88F4B1-7EEC-3630-8D62-FB7886622A08
-  Functions: 184
-  Symbols:   272
-  CStrings:  586
+  UUID: 23E0D619-CEBC-30EA-9987-973F36A46532
+  Functions: 174
+  Symbols:   275
+  CStrings:  587
 
Symbols:
+ _NFHardwareInterfaceEnableLog
+ _NFHardwareSerialDebugLogEnable
+ _NFHardwareSerialEnableLog
CStrings:
+ "((NFHardwareSerialInternal*)(serial->internal))->currentWriteBuffer == ((void*)0)"
+ "_phTmlNfc_SerialLogEnable"
+ "buffer!=((void*)0)"
+ "devicePath != ((void*)0)"
+ "pBuffer!=((void*)0)"
+ "pConfig!=((void*)0)"
+ "pHwRef!=((void*)0)"
- "((NFHardwareSerialInternal*)(serial->internal))->currentWriteBuffer == ((void *)0)"
- "buffer!=((void *)0)"
- "devicePath != ((void *)0)"
- "pBuffer!=((void *)0)"
- "pConfig!=((void *)0)"
- "pHwRef!=((void *)0)"

```
