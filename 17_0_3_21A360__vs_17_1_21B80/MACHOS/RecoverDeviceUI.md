## RecoverDeviceUI

> `/Applications/RecoverDeviceUI.app/RecoverDeviceUI`

```diff

-1856.2.2.0.0
-  __TEXT.__text: 0x4600
+1856.42.1.0.0
+  __TEXT.__text: 0x471c
   __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x2fc
+  __TEXT.__objc_stubs: 0xd60
+  __TEXT.__objc_methlist: 0x2ec
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__cstring: 0x436
+  __TEXT.__gcc_except_tab: 0x1a8
+  __TEXT.__cstring: 0x3f7
   __TEXT.__oslogstring: 0x93a
-  __TEXT.__objc_methname: 0x1a47
+  __TEXT.__objc_methname: 0x1a25
   __TEXT.__objc_classname: 0xcc
   __TEXT.__objc_methtype: 0xbf7
-  __TEXT.__unwind_info: 0xf8
+  __TEXT.__unwind_info: 0xfc
   __DATA_CONST.__auth_got: 0x1a0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x168
-  __DATA_CONST.__cfstring: 0x4e0
+  __DATA_CONST.__cfstring: 0x4c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1368
-  __DATA.__objc_selrefs: 0x3f0
+  __DATA.__objc_const: 0x1338
+  __DATA.__objc_selrefs: 0x3e8
   __DATA.__objc_classrefs: 0x98
   __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x40
+  __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 80
-  Symbols:   767
-  CStrings:  446
+  Functions: 79
+  Symbols:   759
+  CStrings:  442
 
Symbols:
+ -[RecoverDeviceUIExtensionRemoteViewController kLocalizedDeviceType]
+ -[RecoverDeviceUIExtensionRemoteViewController setKLocalizedDeviceType:]
+ -[RecoverDeviceUIExtensionRemoteViewController uiImage]
+ OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._kLocalizedDeviceType
+ __62-[RecoverDeviceUIExtensionRemoteViewController viewDidAppear:]_block_invoke.331
+ __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.326
+ __70-[RecoverDeviceUIExtensionRemoteViewController showOverallResultCard:]_block_invoke.308
+ __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.311
+ _objc_msgSend$kLocalizedDeviceType
+ _objc_msgSend$setKLocalizedDeviceType:
+ _objc_msgSend$uiImage
- -[RecoverDeviceUIExtensionRemoteViewController deviceType]
- -[RecoverDeviceUIExtensionRemoteViewController isBatteryPowered]
- -[RecoverDeviceUIExtensionRemoteViewController setDeviceType:]
- -[RecoverDeviceUIExtensionRemoteViewController setIsBatteryPowered:]
- OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._deviceType
- OBJC_IVAR_$_RecoverDeviceUIExtensionRemoteViewController._isBatteryPowered
- __62-[RecoverDeviceUIExtensionRemoteViewController viewDidAppear:]_block_invoke.343
- __68-[RecoverDeviceUIExtensionRemoteViewController recoverButtonPressed]_block_invoke.338
- __70-[RecoverDeviceUIExtensionRemoteViewController showOverallResultCard:]_block_invoke.320
- __94-[RecoverDeviceUIExtensionRemoteViewController showCollectCodeCard:inFlags:inThrottleSeconds:]_block_invoke.323
- _objc_msgSend$deviceType
- _objc_msgSend$isBatteryPowered
- _objc_msgSend$setDeviceType:
- _objc_msgSend$setIsBatteryPowered:
CStrings:
+ "%@_%@"
+ "OVERALL_RESULT_SUCCESS_DESCRIPTION"
+ "T@\"NSString\",&,N,V_kLocalizedDeviceType"
+ "_kLocalizedDeviceType"
+ "kLocalizedDeviceType"
+ "setKLocalizedDeviceType:"
+ "uiImage"
- "OVERALL_RESULT_SUCCESS_DESCRIPTION_CHARGER"
- "OVERALL_RESULT_SUCCESS_DESCRIPTION_POWER"
- "T@\"NSString\",&,N,V_deviceType"
- "TB,V_isBatteryPowered"
- "_deviceType"
- "_isBatteryPowered"
- "checkmark.seal.fill"
- "deviceType"
- "isBatteryPowered"
- "setDeviceType:"
- "setIsBatteryPowered:"

```
