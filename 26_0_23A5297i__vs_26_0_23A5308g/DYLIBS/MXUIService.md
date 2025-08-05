## MXUIService

> `/System/Library/PrivateFrameworks/MXUIService.framework/MXUIService`

```diff

-270.70.1.0.0
-  __TEXT.__text: 0x82f8
+270.74.1.11.1
+  __TEXT.__text: 0x8994
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x804
-  __TEXT.__const: 0xe8
+  __TEXT.__objc_methlist: 0x84c
+  __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__cstring: 0x4c7
-  __TEXT.__oslogstring: 0x4a5
-  __TEXT.__unwind_info: 0x168
+  __TEXT.__cstring: 0x5a7
+  __TEXT.__oslogstring: 0x521
+  __TEXT.__unwind_info: 0x178
   __TEXT.__objc_classname: 0x12d
-  __TEXT.__objc_methname: 0x1ef7
-  __TEXT.__objc_methtype: 0x5e3
-  __TEXT.__objc_stubs: 0x1280
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0xf8
+  __TEXT.__objc_methname: 0x2014
+  __TEXT.__objc_methtype: 0x605
+  __TEXT.__objc_stubs: 0x1340
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7e0
+  __DATA_CONST.__objc_selrefs: 0x820
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x1d0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x320
-  __AUTH_CONST.__objc_const: 0x1658
+  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__objc_const: 0x1680
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xe8
+  __DATA.__objc_ivar: 0xec
   __DATA.__data: 0x300
   __DATA.__common: 0x48
   __DATA.__bss: 0x30

   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 675EF413-5E60-3148-A0CB-0972B22D7661
-  Functions: 92
-  Symbols:   594
-  CStrings:  536
+  UUID: 53B37FE7-FEEA-3733-AE96-F9DC1D17AD77
+  Functions: 97
+  Symbols:   613
+  CStrings:  553
 
Symbols:
+ -[MXUIServiceBanner _createDeviceReplacementBannerTextLabel:]
+ -[MXUIServiceBanner configureBannerViews]
+ -[MXUIServiceBanner configureInputDeviceReplacementPillForConnectedDevice:replacedDevice:]
+ -[MXUIService_BannerUIDelegate showInputDeviceReplacementPillForConnectedDevice:replacedDevice:]
+ GCC_except_table32
+ _OBJC_CLASS_$_NSString
+ _OBJC_IVAR_$_MXUIServiceBanner._useJindoPath
+ ___96-[MXUIService_BannerUIDelegate showInputDeviceReplacementPillForConnectedDevice:replacedDevice:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ _objc_msgSend$configureBannerViews
+ _objc_msgSend$configureInputDeviceReplacementPillForConnectedDevice:replacedDevice:
+ _objc_msgSend$initWithLeadingAccessoryView:
+ _objc_msgSend$initWithText:
+ _objc_msgSend$orangeColor
+ _objc_msgSend$stringWithFormat:
- GCC_except_table30
CStrings:
+ "-MXUIService- %s: Showing input device replacement pill (connectedDeviceName='%{public}@', replacedDeviceName='%{public}@')"
+ "-[MXUIServiceBanner configureInputDeviceReplacementPillForConnectedDevice:replacedDevice:]"
+ "-[MXUIService_BannerUIDelegate showInputDeviceReplacementPillForConnectedDevice:replacedDevice:]"
+ "DEVICEA_REPLACED_DEVICEB"
+ "_createDeviceReplacementBannerTextLabel:"
+ "_useJindoPath"
+ "configureBannerViews"
+ "configureInputDeviceReplacementPillForConnectedDevice:replacedDevice:"
+ "initWithLeadingAccessoryView:"
+ "initWithText:"
+ "microphone"
+ "orangeColor"
+ "showInputDeviceReplacementPillForConnectedDevice:replacedDevice:"
+ "stringWithFormat:"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"

```
