## HearingModeService_Private

> `/System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private`

```diff

-30.59.1.9.0
-  __TEXT.__text: 0x12e98
+31.5.2.1.2
+  __TEXT.__text: 0x13040
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_methlist: 0xc64
+  __TEXT.__objc_methlist: 0xc6c
   __TEXT.__const: 0x86
   __TEXT.__gcc_except_tab: 0x514
-  __TEXT.__cstring: 0x50e2
-  __TEXT.__unwind_info: 0x5f0
+  __TEXT.__cstring: 0x51ad
+  __TEXT.__unwind_info: 0x5f8
   __TEXT.__objc_classname: 0x14d
-  __TEXT.__objc_methname: 0x367e
+  __TEXT.__objc_methname: 0x36e2
   __TEXT.__objc_methtype: 0x8ef
-  __TEXT.__objc_stubs: 0x3200
-  __DATA_CONST.__got: 0x1f0
+  __TEXT.__objc_stubs: 0x3280
+  __DATA_CONST.__got: 0x200
   __DATA_CONST.__const: 0x858
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xea0
+  __DATA_CONST.__objc_selrefs: 0xec0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x268

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C0E39102-AE3E-333E-8A91-6A896F6F55B3
-  Functions: 435
-  Symbols:   1658
-  CStrings:  1133
+  UUID: 780C4A55-7149-3F78-9121-23C9142E3BF1
+  Functions: 438
+  Symbols:   1670
+  CStrings:  1140
 
Symbols:
+ -[HMOcclusionNotification _deviceIconForProductID:]
+ -[HMOcclusionNotification _deviceIconForProductID:].cold.1
+ -[HMOcclusionNotification _deviceIconForProductID:].cold.2
+ -[HMOcclusionNotification _iconTypeForProductID:]
+ _OBJC_CLASS_$_UNNotificationIcon
+ _OBJC_CLASS_$_UTType
+ _objc_msgSend$_deviceIconForProductID:
+ _objc_msgSend$_iconTypeForProductID:
+ _objc_msgSend$_typeWithBluetoothProductID:vendorID:
+ _objc_msgSend$iconForSystemImageNamed:
+ _objc_msgSend$iconWithUTI:
+ _objc_msgSend$setIcon:
- -[HMOcclusionNotification _getSystemIconName:]
- _objc_msgSend$_getSystemIconName:
- _objc_msgSend$setIconName:
CStrings:
+ "-[HMOcclusionNotification _deviceIconForProductID:]"
+ "No icon type found for product ID: %lu, falling back to default product ID: %lu"
+ "Unable to find icon type for default product ID: %lu. Using SF Symbol"
+ "_deviceIconForProductID:"
+ "_iconTypeForProductID:"
+ "_typeWithBluetoothProductID:vendorID:"
+ "airpods.pro"
+ "iconForSystemImageNamed:"
+ "iconWithUTI:"
+ "setIcon:"
- "_getSystemIconName:"
- "airpodspro"
- "setIconName:"

```
