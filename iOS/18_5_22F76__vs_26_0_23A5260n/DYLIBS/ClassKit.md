## ClassKit

> `/System/Library/Frameworks/ClassKit.framework/ClassKit`

```diff

-150.4.11.0.0
-  __TEXT.__text: 0x866c4
-  __TEXT.__auth_stubs: 0xa60
+151.0.8.0.0
+  __TEXT.__text: 0x86434
+  __TEXT.__auth_stubs: 0xa40
+  __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0x8aec
-  __TEXT.__const: 0x140
-  __TEXT.__dlopen_cstrs: 0x6a
-  __TEXT.__cstring: 0x6918
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x6933
   __TEXT.__oslogstring: 0x351e
-  __TEXT.__gcc_except_tab: 0xc84
+  __TEXT.__gcc_except_tab: 0xc74
   __TEXT.__ustring: 0x2e
-  __TEXT.__unwind_info: 0x21b0
+  __TEXT.__unwind_info: 0x21a0
   __TEXT.__objc_classname: 0xb96
-  __TEXT.__objc_methname: 0x106f0
+  __TEXT.__objc_methname: 0x10703
   __TEXT.__objc_methtype: 0x1d6c
   __TEXT.__objc_stubs: 0xab80
-  __DATA_CONST.__got: 0x5b0
-  __DATA_CONST.__const: 0x1ed0
+  __DATA_CONST.__got: 0x5b8
+  __DATA_CONST.__const: 0x1e98
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x100

   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x540
+  __AUTH_CONST.__auth_got: 0x530
   __AUTH_CONST.__const: 0xe40
   __AUTH_CONST.__cfstring: 0x8120
   __AUTH_CONST.__objc_const: 0xd850
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_ivar: 0x378
-  __DATA.__data: 0xc08
+  __DATA.__data: 0xc0c
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_ivar: 0x614
   __DATA_DIRTY.__objc_data: 0x20d0
-  __DATA_DIRTY.__bss: 0x678
+  __DATA_DIRTY.__bss: 0x668
   __DATA_DIRTY.__common: 0xd0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/ClassKitNotificationUI.framework/ClassKitNotificationUI
   - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
   - /System/Library/PrivateFrameworks/ManagedOrganizationContacts.framework/ManagedOrganizationContacts
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FC275D1D-8DAC-3386-8110-B1597D97137A
-  Functions: 3224
-  Symbols:   757
+  UUID: 6C107D5B-891B-35FB-9BDE-DDA77CB60825
+  Functions: 3221
+  Symbols:   756
   CStrings:  5642
 
Symbols:
+ _OBJC_CLASS_$_CLSNotificationBannerDisplayManager
+ _dlopen
- __sl_dlopen
- _abort_report_np
- _objc_getClass
CStrings:
+ "/System/Library/PrivateFrameworks/ClassKitNotificationUI.framework/ClassKitNotificationUI"
+ "T@\"NSPersonNameComponents\",?,R"
+ "T@\"NSString\",?,R"
+ "T@\"NSString\",C,V_appleID"
+ "T@\"NSString\",C,V_emailAddress"
+ "T@\"NSString\",C,V_familyName"
+ "T@\"NSString\",C,V_givenName"
+ "T@\"NSString\",C,V_grade"
+ "T@\"NSString\",C,V_iCloudUserID"
+ "T@\"NSString\",C,V_middleName"
+ "T@\"NSString\",C,V_orgID"
+ "T@\"NSString\",C,V_personNumber"
+ "T@\"NSString\",C,V_phoneticFamilyName"
+ "T@\"NSString\",C,V_phoneticGivenName"
+ "T@\"NSString\",C,V_phoneticMiddleName"
+ "T@\"NSString\",C,V_searchText"
+ "T@\"NSString\",R"
+ "TB,GisEditable,V_isEditable"
+ "TB,GisFederatedAccount,V_federatedAccount"
+ "TB,GisProgressTrackingAllowed,V_progressTrackingAllowed"
+ "TB,GisSearchable,V_isSearchable"
+ "Tq,V_axmAccountStatus"
+ "Tq,V_passcodeType"
+ "Tq,V_sourceType"
- "%s"
- "CLSNotificationBannerDisplayManager"
- "T@\"NSPersonNameComponents\",?,R,N"
- "T@\"NSString\",?,R,N"
- "T@\"NSString\",C,N,V_appleID"
- "T@\"NSString\",C,N,V_emailAddress"
- "T@\"NSString\",C,N,V_familyName"
- "T@\"NSString\",C,N,V_givenName"
- "T@\"NSString\",C,N,V_grade"
- "T@\"NSString\",C,N,V_iCloudUserID"
- "T@\"NSString\",C,N,V_middleName"
- "T@\"NSString\",C,N,V_orgID"
- "T@\"NSString\",C,N,V_personNumber"
- "T@\"NSString\",C,N,V_phoneticFamilyName"
- "T@\"NSString\",C,N,V_phoneticGivenName"
- "T@\"NSString\",C,N,V_phoneticMiddleName"
- "TB,N,GisEditable,V_isEditable"
- "TB,N,GisFederatedAccount,V_federatedAccount"
- "TB,N,GisProgressTrackingAllowed,V_progressTrackingAllowed"
- "TB,N,GisSearchable,V_isSearchable"
- "Tq,N,V_axmAccountStatus"
- "Tq,N,V_passcodeType"
- "Unable to find class %s"
- "softlink:r:path:/System/Library/PrivateFrameworks/ClassKitNotificationUI.framework/ClassKitNotificationUI"

```
