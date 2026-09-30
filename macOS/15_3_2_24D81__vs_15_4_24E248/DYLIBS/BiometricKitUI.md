## BiometricKitUI

> `/System/Library/PrivateFrameworks/BiometricKitUI.framework/Versions/A/BiometricKitUI`

```diff

-625.0.0.0.0
-  __TEXT.__text: 0x25228
+646.4.2.0.0
+  __TEXT.__text: 0x252b8
   __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x1cf8
+  __TEXT.__objc_methlist: 0x2238
   __TEXT.__const: 0x7b8
-  __TEXT.__cstring: 0x1a88
-  __TEXT.__gcc_except_tab: 0x820
-  __TEXT.__oslogstring: 0x25f2
+  __TEXT.__cstring: 0x1a80
+  __TEXT.__gcc_except_tab: 0x888
+  __TEXT.__oslogstring: 0x262f
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x788
+  __TEXT.__unwind_info: 0x7a8
   __TEXT.__objc_classname: 0x485
-  __TEXT.__objc_methname: 0x5d9e
-  __TEXT.__objc_methtype: 0x1143
-  __TEXT.__objc_stubs: 0x4da0
-  __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0xe0
+  __TEXT.__objc_methname: 0x5dff
+  __TEXT.__objc_methtype: 0x114e
+  __TEXT.__objc_stubs: 0x4e20
+  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17c8
+  __DATA_CONST.__objc_selrefs: 0x1990
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0x150
+  __DATA_CONST.__objc_arraydata: 0x180
   __AUTH_CONST.__auth_got: 0x348
-  __AUTH_CONST.__const: 0x590
+  __AUTH_CONST.__const: 0x5a0
   __AUTH_CONST.__cfstring: 0x2480
-  __AUTH_CONST.__objc_const: 0x5380
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_const: 0x4a58
+  __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x10

   __DATA.__bss: 0x50
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
+  - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
-  - /System/Library/Frameworks/IOBluetooth.framework/Versions/A/IOBluetooth
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/LocalAuthentication.framework/Versions/A/LocalAuthentication
   - /System/Library/Frameworks/Quartz.framework/Versions/A/Quartz

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A382EFA1-472E-30B0-8389-E6F09621BCEF
+  UUID: 45C43147-00D7-37E1-8253-0A88FFECC5DD
   Functions: 775
-  Symbols:   2211
-  CStrings:  2134
+  Symbols:   2225
+  CStrings:  2141
 
Symbols:
+ +[BKUIDevice sharedInstance].cold.1
+ +[BKUIFunctionBarController sharedInstance].cold.1
+ +[BiometricKitUI sharedInstance].cold.1
+ -[BKUIDeviceImageView isA2xxDevice:]
+ GCC_except_table13
+ GCC_except_table35
+ GCC_except_table77
+ _BKUILoggingFacility.cold.1
+ _NSAccessibilityLayoutChangedNotification
+ _NSAccessibilityUIElementsKey
+ _OBJC_CLASS_$_CBDiscovery
+ _OBJC_CLASS_$_NSSet
+ _OUTLINED_FUNCTION_4
+ __118-[BKMesaSecureIntentProvider _getSecureIntentForAccessory:enrollmentOperation:showErrorToRetry:withCompletionHandler:]_block_invoke.42
+ ___block_descriptor_40_e8_32s_e35_B24?0"CBDevice"8"NSDictionary"16l
+ _objc_msgSend$colorCodeBest
+ _objc_msgSend$containsObject:
+ _objc_msgSend$devicesWithDiscoveryFlags:error:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$isA2xxDevice:
+ _objc_msgSend$numberWithUnsignedInteger:
- GCC_except_table14
- _OBJC_CLASS_$_IOBluetoothDevice
- __118-[BKMesaSecureIntentProvider _getSecureIntentForAccessory:enrollmentOperation:showErrorToRetry:withCompletionHandler:]_block_invoke.38
- ___block_descriptor_32_e44_B24?0"IOBluetoothDevice"8"NSDictionary"16l
- __block_literal_global.136
- _objc_msgSend$colorID
- _objc_msgSend$pairedDevices
CStrings:
+ "A2xx: AssetPaths not found :%@"
+ "A2xx: Color ID [%i], Color key [%@], imageColorSufix [%@], imageName [%@]"
+ "A2xx: Color code not found for productID [%@] colorID [%@]. Default to Silver"
+ "A2xx: Found #%@ devices from #%@ Paired devices"
+ "A2xx: Found 0 device, Paired devices [#%@] %@"
+ "A2xx: Paired devices [#%@] %@"
+ "B20@0:8S16"
+ "B24@?0@\"CBDevice\"8@\"NSDictionary\"16"
+ "colorCodeBest"
+ "containsObject:"
+ "devicesWithDiscoveryFlags:error:"
+ "initWithArray:"
+ "isA2xxDevice:"
+ "keyboardCase:%@ keyBoardKeys:%@ keyBoardSensor:%@"
+ "numberWithUnsignedInteger:"
- "B24@?0@\"IOBluetoothDevice\"8@\"NSDictionary\"16"
- "Color ID %i, Color key :%@, imageColorSufix :%@, colorDictionary %@, imageName: %@ "
- "Color code not found for productID %@ colorID:%@. Default to Silver"
- "MagicKeyboard assetPaths not found :%@"
- "MagicKeyboard not connected, all connected BT items:%@"
- "colorID"
- "keyboardCase:%@ keyBoardKeys%@ keyBoardSensor:%@"
- "pairedDevices"

```
