## ScreenTime

> `/System/Library/Frameworks/ScreenTime.framework/Versions/A/ScreenTime`

```diff

-655.0.405.0.0
-  __TEXT.__text: 0x63a8
-  __TEXT.__objc_methlist: 0x7fc
+655.1.6.1.0
+  __TEXT.__text: 0x65e0
+  __TEXT.__objc_methlist: 0x824
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x42d
-  __TEXT.__gcc_except_tab: 0xf4
+  __TEXT.__cstring: 0x456
+  __TEXT.__gcc_except_tab: 0x114
   __TEXT.__oslogstring: 0x626
-  __TEXT.__unwind_info: 0x380
+  __TEXT.__unwind_info: 0x390
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x698
+  __DATA_CONST.__objc_selrefs: 0x6c0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__got: 0x168
   __AUTH_CONST.__const: 0x570
-  __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0xfb8
+  __AUTH_CONST.__cfstring: 0x2e0
+  __AUTH_CONST.__objc_const: 0xfe8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/Categories.framework/Versions/A/Categories
+  - /System/Library/PrivateFrameworks/FamilyControlsObjC.framework/Versions/A/FamilyControlsObjC
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/Versions/A/ScreenTimeCore
   - /System/Library/PrivateFrameworks/UsageTracking.framework/Versions/A/UsageTracking
   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 214
-  Symbols:   607
-  CStrings:  59
+  Functions: 219
+  Symbols:   617
+  CStrings:  60
 
Symbols:
+ -[STScreenTimeConfigurationObserver _cancelNotificationToken:]
+ -[STScreenTimeConfigurationObserver authorizationNotificationToken]
+ -[STScreenTimeConfigurationObserver setAuthorizationNotificationToken:]
+ GCC_except_table20
+ GCC_except_table25
+ OBJC_IVAR_$_STScreenTimeConfigurationObserver._authorizationNotificationToken
+ _FOAuthorizationRecordsChangedNotification
+ __51-[STScreenTimeConfigurationObserver startObserving]_block_invoke
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_cancelNotificationToken:
+ _objc_msgSend$authorizationNotificationToken
+ _objc_msgSend$hasChildAuthorization
+ _objc_msgSend$setAuthorizationNotificationToken:
- GCC_except_table12
- GCC_except_table18
- GCC_except_table23
CStrings:
+ "webBrowserSettings.hasChildAuthorization"
```
