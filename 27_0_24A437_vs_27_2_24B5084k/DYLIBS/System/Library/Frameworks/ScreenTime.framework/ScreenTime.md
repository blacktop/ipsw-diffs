## ScreenTime

> `/System/Library/Frameworks/ScreenTime.framework/ScreenTime`

```diff

-655.0.107.0.0
-  __TEXT.__text: 0x5690
-  __TEXT.__objc_methlist: 0x7ec
+655.1.6.1.0
+  __TEXT.__text: 0x58cc
+  __TEXT.__objc_methlist: 0x814
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x366
-  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__cstring: 0x38f
+  __TEXT.__gcc_except_tab: 0x110
   __TEXT.__oslogstring: 0x588
-  __TEXT.__unwind_info: 0x348
+  __TEXT.__unwind_info: 0x360
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x668
+  __DATA_CONST.__objc_selrefs: 0x690
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__got: 0x178
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0xf10
+  __AUTH_CONST.__cfstring: 0x240
+  __AUTH_CONST.__objc_const: 0xf40
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/Categories.framework/Categories
+  - /System/Library/PrivateFrameworks/FamilyControlsObjC.framework/FamilyControlsObjC
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 198
-  Symbols:   582
-  CStrings:  53
+  Functions: 203
+  Symbols:   593
+  CStrings:  54
 
Symbols:
+ -[STScreenTimeConfigurationObserver _cancelNotificationToken:]
+ -[STScreenTimeConfigurationObserver authorizationNotificationToken]
+ -[STScreenTimeConfigurationObserver setAuthorizationNotificationToken:]
+ GCC_except_table13
+ GCC_except_table18
+ GCC_except_table21
+ _FOAuthorizationRecordsChangedNotification
+ _OBJC_IVAR_$_STScreenTimeConfigurationObserver._authorizationNotificationToken
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_cancelNotificationToken:
+ _objc_msgSend$authorizationNotificationToken
+ _objc_msgSend$hasChildAuthorization
+ _objc_msgSend$setAuthorizationNotificationToken:
- GCC_except_table16
- GCC_except_table19
CStrings:
+ "webBrowserSettings.hasChildAuthorization"
```
