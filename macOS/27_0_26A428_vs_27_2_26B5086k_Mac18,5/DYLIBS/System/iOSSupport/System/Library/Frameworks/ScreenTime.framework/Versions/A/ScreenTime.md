## ScreenTime

> `/System/iOSSupport/System/Library/Frameworks/ScreenTime.framework/Versions/A/ScreenTime`

```diff

-655.0.405.0.0
-  __TEXT.__text: 0x5858
-  __TEXT.__objc_methlist: 0x7f4
+655.1.6.1.0
+  __TEXT.__text: 0x5a90
+  __TEXT.__objc_methlist: 0x81c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x39f
-  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__cstring: 0x3c8
+  __TEXT.__gcc_except_tab: 0x110
   __TEXT.__oslogstring: 0x622
-  __TEXT.__unwind_info: 0x340
+  __TEXT.__unwind_info: 0x358
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x678
+  __DATA_CONST.__objc_selrefs: 0x6a0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__got: 0x160
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x260
-  __AUTH_CONST.__objc_const: 0xf48
+  __AUTH_CONST.__cfstring: 0x280
+  __AUTH_CONST.__objc_const: 0xf78
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/Categories.framework/Versions/A/Categories
+  - /System/Library/PrivateFrameworks/FamilyControlsObjC.framework/Versions/A/FamilyControlsObjC
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeCore
   - /System/Library/PrivateFrameworks/UsageTracking.framework/Versions/A/UsageTracking
   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 198
-  Symbols:   603
-  CStrings:  56
+  Functions: 203
+  Symbols:   614
+  CStrings:  57
 
Symbols:
+ -[STScreenTimeConfigurationObserver _cancelNotificationToken:]
+ -[STScreenTimeConfigurationObserver authorizationNotificationToken]
+ -[STScreenTimeConfigurationObserver setAuthorizationNotificationToken:]
+ GCC_except_table13
+ GCC_except_table18
+ GCC_except_table21
+ OBJC_IVAR_$_STScreenTimeConfigurationObserver._authorizationNotificationToken
+ _FOAuthorizationRecordsChangedNotification
+ __51-[STScreenTimeConfigurationObserver startObserving]_block_invoke
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_cancelNotificationToken:
+ _objc_msgSend$authorizationNotificationToken
+ _objc_msgSend$hasChildAuthorization
+ _objc_msgSend$setAuthorizationNotificationToken:
- GCC_except_table12
- GCC_except_table16
- GCC_except_table19
CStrings:
+ "webBrowserSettings.hasChildAuthorization"
```
