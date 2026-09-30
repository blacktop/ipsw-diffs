## com.apple.iokit.IOUSBHostFamily

> `com.apple.iokit.IOUSBHostFamily`

```diff

 1504.100.61.0.0
-  __TEXT.__cstring: 0xa091
-  __TEXT.__os_log: 0x84e4
+  __TEXT.__cstring: 0xa0f2
+  __TEXT.__os_log: 0x8562
   __TEXT.__const: 0x2008
-  __TEXT_EXEC.__text: 0x914c0
+  __TEXT_EXEC.__text: 0x916c4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x1f0
-  __DATA.__common: 0x910
+  __DATA.__common: 0x920
   __DATA.__bss: 0x10
   __DATA_CONST.__auth_got: 0x6a8
   __DATA_CONST.__got: 0x1f8

   __DATA_CONST.__const: 0xc268
   __DATA_CONST.__kalloc_type: 0x1b00
   __DATA_CONST.__kalloc_var: 0x280
-  UUID: 029A29FA-369E-36B9-B3C4-C7320D93454A
+  UUID: 453537FF-0E6A-3F80-9212-300B4129FDDF
   Functions: 1913
   Symbols:   0
-  CStrings:  1619
+  CStrings:  1624
 
Functions:
~ __ZN11StandardUSB25validateEndpointBurstSizeEjPKNS_18EndpointDescriptorEPKNS_37SuperSpeedEndpointCompanionDescriptorEPKNS_52SuperSpeedPlusIsochronousEndpointCompanionDescriptorE : 1504 -> 1928
~ __ZN16AppleUSBHostPort5startEP9IOService : 10012 -> 10072
~ __GLOBAL__sub_I_AppleUSBHostPort.cpp : 968 -> 1000
CStrings:
+ "%s::%s: USB 4.0 9.4.3.4: endpoint 0x%02x invalid bMaxBurst %d\n"
+ "40 Gbps"
+ "80 Gbps"
+ "UsbProtocol (4.0)"

```
