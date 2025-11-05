## com.apple.driver.AppleUSBDeviceMux

> `com.apple.driver.AppleUSBDeviceMux`

```diff

-540.80.1.0.0
+543.0.0.0.0
   __TEXT.__const: 0x34
-  __TEXT.__cstring: 0x1313
-  __TEXT_EXEC.__text: 0x5a14
+  __TEXT.__cstring: 0x1322
+  __TEXT_EXEC.__text: 0x5b1c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x68

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xcc0
   __DATA_CONST.__kalloc_type: 0x440
-  UUID: EA45636A-7E00-3BA1-911B-82FAF4111377
+  UUID: DF41C132-2D5E-3EEC-A085-CF57A112255F
   Functions: 97
   Symbols:   521
   CStrings:  144
Symbols:
+ __ZZN17AppleUSBDeviceMux14resyncWithHostEvE21kalloc_type_view_3193
+ __ZZN17AppleUSBDeviceMux14sendMuxSegmentEP17BulkUSBMuxSessionE21kalloc_type_view_2939
+ __ZZN17AppleUSBDeviceMux18asyncWriteCompleteEP14USBWriteBufferijE21kalloc_type_view_2336
- __ZZN17AppleUSBDeviceMux14resyncWithHostEvE21kalloc_type_view_3186
- __ZZN17AppleUSBDeviceMux14sendMuxSegmentEP17BulkUSBMuxSessionE21kalloc_type_view_2932
- __ZZN17AppleUSBDeviceMux18asyncWriteCompleteEP14USBWriteBufferijE21kalloc_type_view_2322
Functions:
~ __ZN17AppleUSBDeviceMux5startEP9IOService : 1076 -> 1092
~ __ZN17AppleUSBDeviceMux18asyncWriteCompleteEP14USBWriteBufferij : 1064 -> 1084
~ __ZN17AppleUSBDeviceMux14resyncWithHostEv : 492 -> 488
~ __ZN17AppleUSBDeviceMux4freeEv : 360 -> 364
~ __ZN17AppleUSBDeviceMux14cleanupSessionEP17BulkUSBMuxSession : 360 -> 380
~ __ZN17AppleUSBDeviceMux7messageEjP9IOServicePv : 876 -> 900
~ __ZN17AppleUSBDeviceMux11reportStatsEb : 192 -> 196
~ __ZN17AppleUSBDeviceMux14sendMuxSegmentEP17BulkUSBMuxSession : 964 -> 980
~ __ZN17AppleUSBDeviceMux19handleConnectResultEP17BulkUSBMuxSessioni : 648 -> 668
~ __ZN17AppleUSBDeviceMux10sendMuxRSTEP17BulkUSBMuxSessionbPKcz : 92 -> 96
~ __ZN17AppleUSBDeviceMux14writeMbufToUSBEP6__mbufj : 632 -> 652
~ __ZN17AppleUSBDeviceMux10newSessionEP6tcphdr : 976 -> 972
~ __ZN17AppleUSBDeviceMux17handleMuxTCPInputEP6__mbuf : 1592 -> 1600
~ __ZN17AppleUSBDeviceMux21handleMuxVersionInputEP6__mbuf : 420 -> 384
~ __ZN17AppleUSBDeviceMux14writeMbufToUSBEP6__mbuf : 264 -> 324
~ __ZN17AppleUSBDeviceMux14handleMuxInputEP6__mbuf : 1964 -> 1960
~ __ZN17AppleUSBDeviceMux14writeToUSBPipeEP14USBWriteBuffer : 576 -> 592
~ __ZN17AppleUSBDeviceMux13startUSBWriteEP14USBWriteBufferjb : 340 -> 360
~ __ZN17AppleUSBDeviceMux7vmuxLogEhbPKcPc : 348 -> 364
~ __ZN17AppleUSBDeviceMux11vsendMuxRSTEP6tcphdrbPKcPc : 428 -> 444
~ __ZN17AppleUSBDeviceMux10sendMuxACKEP17BulkUSBMuxSession : 416 -> 444
CStrings:
+ "%s failed to allocate IOMemoryDescriptor withRanges (%lu ranges)\n"
+ "21:17:11"
+ "Mar 19 2025"
- "20:50:17"
- "Error: negotiated unsupported protocol version %d\n"
- "Jan 10 2025"

```
