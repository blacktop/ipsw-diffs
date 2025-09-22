## ClassKit

> `/System/Library/Frameworks/ClassKit.framework/ClassKit`

```diff

-151.0.10.0.0
-  __TEXT.__text: 0x86670
-  __TEXT.__auth_stubs: 0xa40
-  __TEXT.__delay_helper: 0xc8
+151.1.1.0.0
+  __TEXT.__text: 0x86910
+  __TEXT.__auth_stubs: 0xa60
   __TEXT.__objc_methlist: 0x8b04
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x6952
+  __TEXT.__dlopen_cstrs: 0x6a
+  __TEXT.__cstring: 0x6937
   __TEXT.__oslogstring: 0x353a
-  __TEXT.__gcc_except_tab: 0xc74
+  __TEXT.__gcc_except_tab: 0xc84
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0x21f0
+  __TEXT.__unwind_info: 0x2200
   __TEXT.__objc_classname: 0xb96
   __TEXT.__objc_methname: 0x1076f
   __TEXT.__objc_methtype: 0x1d6c
   __TEXT.__objc_stubs: 0xab80
-  __DATA_CONST.__got: 0x5b8
-  __DATA_CONST.__const: 0x1e98
+  __DATA_CONST.__got: 0x5b0
+  __DATA_CONST.__const: 0x1ed8
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x100

   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x530
+  __AUTH_CONST.__auth_got: 0x540
   __AUTH_CONST.__const: 0xe40
   __AUTH_CONST.__cfstring: 0x8160
   __AUTH_CONST.__objc_const: 0xd8a0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_ivar: 0x378
-  __DATA.__data: 0xc0c
+  __DATA.__data: 0xc08
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_ivar: 0x61c
   __DATA_DIRTY.__objc_data: 0x20d0
-  __DATA_DIRTY.__bss: 0x668
+  __DATA_DIRTY.__bss: 0x678
   __DATA_DIRTY.__common: 0xd0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
-  - /System/Library/PrivateFrameworks/ClassKitNotificationUI.framework/ClassKitNotificationUI
   - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
   - /System/Library/PrivateFrameworks/ManagedOrganizationContacts.framework/ManagedOrganizationContacts
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 66893561-5A85-3895-B454-CE601FF73ADD
-  Functions: 3223
-  Symbols:   756
-  CStrings:  5652
+  UUID: BD61396F-9DC7-33FA-8618-FDF8CB33C3C4
+  Functions: 3226
+  Symbols:   757
+  CStrings:  5655
 
Symbols:
+ __sl_dlopen
+ _abort_report_np
+ _objc_getClass
- _OBJC_CLASS_$_CLSNotificationBannerDisplayManager
- _dlopen
CStrings:
+ "%s"
+ "CLSNotificationBannerDisplayManager"
+ "Unable to find class %s"
+ "softlink:r:path:/System/Library/PrivateFrameworks/ClassKitNotificationUI.framework/ClassKitNotificationUI"
- "/System/Library/PrivateFrameworks/ClassKitNotificationUI.framework/ClassKitNotificationUI"

```
