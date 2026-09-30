## libNFC_HAL.dylib

> `/usr/lib/libNFC_HAL.dylib`

```diff

-353.4.0.0.0
-  __TEXT.__text: 0x179f0
+354.19.0.0.0
+  __TEXT.__text: 0x17cfc
   __TEXT.__auth_stubs: 0x7d0
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x2ae0
+  __TEXT.__cstring: 0x2af4
   __TEXT.__oslogstring: 0x2245
-  __TEXT.__unwind_info: 0x288
+  __TEXT.__unwind_info: 0x230
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x280
   __AUTH_CONST.__auth_got: 0x3e8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  Functions: 181
-  Symbols:   274
-  CStrings:  604
+  Functions: 171
+  Symbols:   277
+  CStrings:  605
 
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
