## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

```diff

-755.1.1.0.0
-  __TEXT.__text: 0x56c34
+760.2.1.0.0
+  __TEXT.__text: 0x56b14
   __TEXT.__auth_stubs: 0x1380
-  __TEXT.__objc_methlist: 0x68c8
+  __TEXT.__objc_methlist: 0x68a8
   __TEXT.__const: 0x140
   __TEXT.__gcc_except_tab: 0x1470
   __TEXT.__oslogstring: 0x4133
-  __TEXT.__cstring: 0x2d68
+  __TEXT.__cstring: 0x2d5b
   __TEXT.__dlopen_cstrs: 0xf8
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x1de0
-  __TEXT.__objc_classname: 0x1062
-  __TEXT.__objc_methname: 0xb926
+  __TEXT.__unwind_info: 0x1dd4
+  __TEXT.__objc_classname: 0x1054
+  __TEXT.__objc_methname: 0xb9ce
   __TEXT.__objc_methtype: 0x259a
-  __TEXT.__objc_stubs: 0x8560
+  __TEXT.__objc_stubs: 0x8520
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0x13b0
-  __DATA_CONST.__objc_classlist: 0x438
+  __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xab08
-  __DATA_CONST.__objc_selrefs: 0x2c00
+  __DATA_CONST.__objc_const: 0xaae0
+  __DATA_CONST.__objc_selrefs: 0x2c08
   __AUTH_CONST.__const: 0xa38
-  __AUTH_CONST.__cfstring: 0x4b80
-  __AUTH_CONST.__objc_const: 0x3fd0
+  __AUTH_CONST.__cfstring: 0x4b60
+  __AUTH_CONST.__objc_const: 0x3f88
   __AUTH_CONST.__auth_got: 0x9d0
-  __AUTH.__objc_data: 0x1090
+  __AUTH.__objc_data: 0x1040
   __DATA.__objc_protorefs: 0x28
   __DATA.__objc_classrefs: 0x560
-  __DATA.__objc_superrefs: 0x380
+  __DATA.__objc_superrefs: 0x378
   __DATA.__objc_ivar: 0x19c
-  __DATA.__data: 0x1ef0
+  __DATA.__data: 0x1f50
   __DATA.__thread_vars: 0x18
   __DATA.__thread_bss: 0x8
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x57c
+  __DATA_DIRTY.__objc_ivar: 0x580
   __DATA_DIRTY.__objc_data: 0x19a0
   __DATA_DIRTY.__bss: 0x4b8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BB21ADF3-E5B5-3397-AEDA-82DA3F1AC9C7
-  Functions: 2438
-  Symbols:   8494
+  UUID: 95D042D7-8CBF-3C49-9886-26DD61177FEF
+  Functions: 2436
+  Symbols:   8484
   CStrings:  4421
 
Symbols:
+ -[HMFWiFiNetworkInfo initWithMACAddress:SSID:BSSID:gatewayIPAddress:gatewayMACAddress:]
+ -[HMFWiFiNetworkInfo networkBSSID]
+ -[HMFWiFiNetworkInfo networkGatewayIPAddress]
+ -[HMFWiFiNetworkInfo networkGatewayMACAddress]
+ _HMFProductInfoDawnBOSVersion
+ _HMFProductInfoLighthouseBOSVersion
+ _HMFProductInfoStarlightBOSVersion
+ _HMFProductInfoSunburstBOSVersion
- -[HMFRingBuffer .cxx_destruct]
- -[HMFRingBuffer addObject:]
- -[HMFRingBuffer buffer]
- -[HMFRingBuffer capacity]
- -[HMFRingBuffer containsObject:]
- -[HMFRingBuffer initWithCapacity:]
- _OBJC_CLASS_$_HMFRingBuffer
- _OBJC_METACLASS_$_HMFRingBuffer
- __OBJC_$_INSTANCE_METHODS_HMFRingBuffer
- __OBJC_$_INSTANCE_VARIABLES_HMFRingBuffer
- __OBJC_$_PROP_LIST_HMFRingBuffer
- __OBJC_CLASS_RO_$_HMFRingBuffer
- __OBJC_METACLASS_RO_$_HMFRingBuffer
- _objc_msgSend$buffer
- _objc_msgSend$capacity
CStrings:
+ "T@\"NSString\",R,C,V_networkBSSID"
+ "T@\"NSString\",R,C,V_networkGatewayIPAddress"
+ "T@\"NSString\",R,C,V_networkGatewayMACAddress"
+ "_networkBSSID"
+ "_networkGatewayIPAddress"
+ "_networkGatewayMACAddress"
+ "networkBSSID"
+ "networkGatewayIPAddress"
+ "networkGatewayMACAddress"
- "HMFRingBuffer"
- "T@\"NSMutableArray\",R,V_buffer"
- "TQ,R,V_capacity"
- "_buffer"
- "_capacity"
- "buffer"
- "capacity"
- "capacity > 0"

```
