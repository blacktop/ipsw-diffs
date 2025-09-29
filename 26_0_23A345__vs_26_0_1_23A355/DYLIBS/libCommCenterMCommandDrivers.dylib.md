## libCommCenterMCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib`

```diff

-13091.1.14.0.0
-  __TEXT.__text: 0x215340
+13091.1.17.0.0
+  __TEXT.__text: 0x2153ac
   __TEXT.__auth_stubs: 0x2c00
   __TEXT.__init_offsets: 0x8
   __TEXT.__const: 0x26890

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 47C63192-36B8-374E-91BC-9F6410CD28BE
+  UUID: E7D3D2A1-1BEB-3AFF-AB02-12C7DC6D8251
   Functions: 12328
   Symbols:   37568
   CStrings:  3971
Functions:
~ ____ZN31QMIMav13ActivationCommandDriver9bootstrapEN8dispatch13group_sessionENSt3__110shared_ptrI40ActivationCommandDriverDelegateInterfaceEE_block_invoke_3 : 5144 -> 5152
~ ____ZNK31QMIMav13ActivationCommandDriver16parseMutableTlvsER14ActivationInfoRKN3bsp18ActivationRegister10IndicationE_block_invoke_15 : 148 -> 196
~ __ZN14ActivationInfoC2ERKS_ : 292 -> 300
~ ____ZN26QMIActivationCommandDriver21issueActivationTicketERKNSt3__16vectorIhNS0_9allocatorIhEEEE_block_invoke_2 : 2048 -> 2056
~ ____ZN26QMIActivationCommandDriver21queryActivationStatusEv_block_invoke_2 : 2336 -> 2340
~ ___Block_byref_object_copy_ : 548 -> 556
~ ____ZL17parseOptionalTLVsIN3bsp22SendActivationManifest8ResponseEEvPKN3ctu11OsLogLoggerER14ActivationInfoT__block_invoke_7 : 144 -> 156
~ ____ZL17parseOptionalTLVsIN3bsp18GetActivationState8ResponseEEvPKN3ctu11OsLogLoggerER14ActivationInfoT__block_invoke_7 : 144 -> 156

```
