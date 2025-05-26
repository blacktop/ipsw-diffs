## MobileStore

> `/private/var/staged_system_apps/MobileStore.app/MobileStore`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0x52d0
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0x18e0
+  __TEXT.__text: 0x5484
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_stubs: 0x1900
   __TEXT.__objc_methlist: 0x2c4
   __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__cstring: 0x73e
-  __TEXT.__objc_methname: 0x236c
+  __TEXT.__gcc_except_tab: 0xe4
+  __TEXT.__cstring: 0x791
+  __TEXT.__objc_methname: 0x2385
   __TEXT.__objc_classname: 0xe2
   __TEXT.__objc_methtype: 0xe02
   __TEXT.__oslogstring: 0x7d
   __TEXT.__unwind_info: 0x1c8
-  __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_got: 0x220
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x350
   __DATA_CONST.__cfstring: 0x8e0
   __DATA_CONST.__objc_classlist: 0x28

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x1338
-  __DATA.__objc_selrefs: 0x710
+  __DATA.__objc_selrefs: 0x718
   __DATA.__objc_classrefs: 0x198
   __DATA.__objc_superrefs: 0x28
   __DATA.__objc_ivar: 0x44

   - /System/Library/Frameworks/StoreKit.framework/StoreKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/MobileStoreUI.framework/MobileStoreUI
   - /System/Library/PrivateFrameworks/MusicStoreUI.framework/MusicStoreUI

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 92
-  Symbols:   141
-  CStrings:  536
+  Symbols:   144
+  CStrings:  541
 
Symbols:
+ _SUUIConfigurationKeyStopPages
+ __os_feature_enabled_impl
+ _os_variant_has_internal_content
CStrings:
+ "MobileStore"
+ "always_show_tv_stop_pages"
+ "arrayWithObjects:count:"
+ "loadValueForConfigurationKeys:completionBlock:"
+ "stop_page_respected_onboarding"
+ "tv_stop_pages"
- "loadValueForConfigurationKey:completionBlock:"

```
