## com.apple.driver.AppleUSBDeviceMux

> `com.apple.driver.AppleUSBDeviceMux`

```diff

-543.0.0.0.0
+554.0.0.0.0
   __TEXT.__const: 0x34
   __TEXT.__cstring: 0x1322
-  __TEXT_EXEC.__text: 0x5a10
+  __TEXT_EXEC.__text: 0x5b08
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x68

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x780
   __DATA_CONST.__kalloc_type: 0x440
-  UUID: 81ED0958-38A6-31D4-9AFD-D08AD56FF54E
+  UUID: 9F52F9D9-51B0-31F7-98C2-D2DE0E420C70
   Functions: 97
   Symbols:   0
   CStrings:  144
Functions:
~ __ZN17AppleUSBDeviceMux18asyncWriteCompleteEP14USBWriteBufferij : 1080 -> 1116
~ __ZN17AppleUSBDeviceMux22asyncMbufWriteCompleteEP6__mbufij : 588 -> 608
~ sub_fffffff009c5b98c -> sub_fffffff009f9c114 : 356 -> 404
~ __ZN17AppleUSBDeviceMux7messageEjP9IOServicePv : 900 -> 924
~ __ZN17AppleUSBDeviceMux11reportStatsEb : 196 -> 192
~ __ZN17AppleUSBDeviceMux14sendMuxSegmentEP17BulkUSBMuxSession : 964 -> 980
~ __ZN17AppleUSBDeviceMux19handleConnectResultEP17BulkUSBMuxSessioni : 652 -> 668
~ sub_fffffff009c5cc54 -> sub_fffffff009f9d440 : 636 -> 652
~ __ZN17AppleUSBDeviceMux14handleMuxInputEP6__mbuf : 1952 -> 1948
~ __ZN17AppleUSBDeviceMux14writeToUSBPipeEP14USBWriteBuffer : 568 -> 584
~ __ZN17AppleUSBDeviceMux13startUSBWriteEP14USBWriteBufferjb : 344 -> 360
~ sub_fffffff009c5ea10 -> sub_fffffff009f9f228 : 348 -> 364
~ __ZN17AppleUSBDeviceMux11vsendMuxRSTEP6tcphdrbPKcPc : 428 -> 444
~ sub_fffffff009c5ed18 -> sub_fffffff009f9f550 : 428 -> 444
CStrings:
+ "19:20:18"
+ "May 30 2025"
- "20:31:26"
- "Apr 22 2025"

```
