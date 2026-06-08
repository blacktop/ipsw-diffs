## com.apple.driver.AppleUSBDeviceMux

> `com.apple.driver.AppleUSBDeviceMux`

```diff

-560.100.4.0.0
+569.0.0.0.0
   __TEXT.__const: 0x34
-  __TEXT.__cstring: 0x1322
-  __TEXT_EXEC.__text: 0x5890
+  __TEXT.__cstring: 0x1359
+  __TEXT_EXEC.__text: 0x58e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x68
   __DATA.__bss: 0x4
-  __DATA_CONST.__auth_got: 0x260
-  __DATA_CONST.__got: 0x50
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x780
   __DATA_CONST.__kalloc_type: 0x440
-  UUID: 33BD3F2D-BA74-3013-B0AC-86BEB57678FC
+  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__got: 0x50
+  UUID: 5A19ADAE-B7FD-3658-8DE7-C5363AA55487
   Functions: 98
   Symbols:   0
-  CStrings:  144
+  CStrings:  145
 
Functions:
~ __ZN17AppleUSBDeviceMux22asyncMbufWriteCompleteEP6__mbufij -> sub_fffffe0009a8103c : 600 -> 604
~ __ZN17AppleUSBDeviceMux12startUSBReadEv -> sub_fffffe0009a81464 : 620 -> 640
~ __ZN17AppleUSBDeviceMux7messageEjP9IOServicePv -> sub_fffffe0009a82180 : 836 -> 892
~ __ZN17AppleUSBDeviceMux17handleMuxTCPInputEP6__mbuf -> sub_fffffe0009a83518 : 1600 -> 1608
CStrings:
+ "22:50:55"
+ "AppleUSBDeviceMux::%s - kMessageInterfaceWasSuspended\n"
+ "May 27 2026"
- "20:29:48"
- "Apr 23 2026"

```
