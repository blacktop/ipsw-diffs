## AppleWirelessChargingServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/AppleWirelessChargingServiceFilter.plugin/AppleWirelessChargingServiceFilter`

```diff

-382.1.8.0.0
-  __TEXT.__text: 0x29a8
+382.1.12.0.0
+  __TEXT.__text: 0x2de0
   __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x3cc
+  __TEXT.__objc_stubs: 0x400
+  __TEXT.__objc_methlist: 0x404
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x854
-  __TEXT.__oslogstring: 0x41a
-  __TEXT.__objc_methname: 0x81e
+  __TEXT.__cstring: 0x8a5
+  __TEXT.__oslogstring: 0x4d5
+  __TEXT.__objc_methname: 0x902
   __TEXT.__objc_classname: 0x6a
-  __TEXT.__objc_methtype: 0x3d9
+  __TEXT.__objc_methtype: 0x3e3
   __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__auth_got: 0x1d8
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x500
+  __DATA_CONST.__cfstring: 0x560
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x6f0
-  __DATA.__objc_selrefs: 0x268
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_const: 0x780
+  __DATA.__objc_selrefs: 0x290
+  __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4CE8B729-75A5-3357-8F9B-55BEB8D20EE0
-  Functions: 52
+  UUID: EB30123F-499E-3412-9C62-AC31D5627786
+  Functions: 58
   Symbols:   83
-  CStrings:  301
+  CStrings:  325
 
CStrings:
+ "%s line %d [Battery status not initialized]"
+ "%s line %d [CAData prepared: attached = NO, SoC = %ld]"
+ "%s line %d [CAData prepared: attached = YES, SoC = %ld]"
+ "%s line %d [authenticated = %x]"
+ "-[PencilData logAttachSoC]"
+ "Attached"
+ "C"
+ "C16@0:8"
+ "SOC"
+ "TC,R,N,V_attachSoCLogged"
+ "TC,R,N,V_authPassed"
+ "TC,R,N,V_batteryPercentageInitialized"
+ "_attachSoCLogged"
+ "_authPassed"
+ "_batteryPercentageInitialized"
+ "attachSoCLogged"
+ "authPassed"
+ "batteryPercentageInitialized"
+ "com.apple.MConnector.PencilAttachmentSOC"
+ "handleAuthPassed"
+ "logAttachSoC"

```
