## USBHost

> `/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`

```diff

-  __TEXT.__text: 0x18870
+  __TEXT.__text: 0x18944
   __TEXT.__objc_methlist: 0x1204
   __TEXT.__const: 0x160
   __TEXT.__oslogstring: 0x2da4
-  __TEXT.__cstring: 0x19bb
-  __TEXT.__gcc_except_tab: 0x3b8
-  __TEXT.__unwind_info: 0x528
+  __TEXT.__cstring: 0x19ac
+  __TEXT.__gcc_except_tab: 0x3c4
+  __TEXT.__unwind_info: 0x538
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9b8
+  __DATA_CONST.__const: 0x9d8
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb78
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__got: 0x278
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x17e0
+  __AUTH_CONST.__cfstring: 0x17c0
   __AUTH_CONST.__objc_const: 0x2320
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x538
+  __AUTH_CONST.__auth_got: 0x540
   __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x24c
   __DATA.__data: 0x240
-  __DATA.__bss: 0xd8
+  __DATA.__bss: 0xe0
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x2c
   __DATA_DIRTY.__bss: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 594
-  Symbols:   2684
-  CStrings:  687
+  Functions: 596
+  Symbols:   2693
+  CStrings:  684
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _ACCTransportEANative_SessionSocketReadyNotification
+ _ACCUserDefaultsKey_EnableManager2ForTransport
+ _ACCUserDefaultsKey_OverrideMPPAuthSupported
+ _CFUUIDCreate
+ _CFUUIDCreateString
+ __gDeviceUUID
+ _kCFACCUserDefaultsKey_EnableManager2ForTransport
+ _kCFACCUserDefaultsKey_OverrideMPPAuthSupported
+ _platform_systemInfo_copyDeviceUUID
+ _platform_systemInfo_resetDeviceUUID
+ _usbUtil_copyInterfaceAndNameString
- _MGGetStringAnswer
- _usbUtil_getInterfaceAndNameString
CStrings:
+ "EnableManager2ForTransport"
+ "OverrideMPPAuthSupported"
+ "usbUtil_copyInterfaceAndNameString"
- "Accessory Manufacturer"
- "Accessory Model"
- "Accessory Name"
- "iAP Interface"
- "usbUtil_getInterfaceAndNameString"

```
