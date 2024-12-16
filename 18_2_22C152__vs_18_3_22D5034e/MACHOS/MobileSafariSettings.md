## MobileSafariSettings

> `/System/Library/PreferenceBundles/MobileSafariSettings.bundle/MobileSafariSettings`

```diff

-7620.1.16.10.11
-  __TEXT.__text: 0x4ea48
+7620.2.2.0.0
+  __TEXT.__text: 0x4ed88
   __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_stubs: 0xbe80
-  __TEXT.__objc_methlist: 0x3560
-  __TEXT.__objc_methname: 0x104e8
+  __TEXT.__objc_stubs: 0xbec0
+  __TEXT.__objc_methlist: 0x3578
+  __TEXT.__objc_methname: 0x10573
   __TEXT.__objc_classname: 0x1032
   __TEXT.__objc_methtype: 0x23f9
   __TEXT.__const: 0x354
-  __TEXT.__cstring: 0x4fd4
+  __TEXT.__cstring: 0x50d4
   __TEXT.__ustring: 0x70a
-  __TEXT.__gcc_except_tab: 0x1d0c
+  __TEXT.__gcc_except_tab: 0x1da4
   __TEXT.__oslogstring: 0x953
   __TEXT.__constg_swiftt: 0x10c
   __TEXT.__swift5_typeref: 0x16e

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x1458
+  __TEXT.__unwind_info: 0x1468
   __TEXT.__eh_frame: 0x40
   __DATA_CONST.__auth_got: 0x710
   __DATA_CONST.__got: 0xd08
   __DATA_CONST.__auth_ptr: 0x110
-  __DATA_CONST.__const: 0x1e88
-  __DATA_CONST.__cfstring: 0x4840
+  __DATA_CONST.__const: 0x1ea8
+  __DATA_CONST.__cfstring: 0x48e0
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x108

   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA.__objc_const: 0x85b0
-  __DATA.__objc_selrefs: 0x39c0
-  __DATA.__objc_ivar: 0x49c
+  __DATA.__objc_selrefs: 0x39d0
+  __DATA.__objc_ivar: 0x498
   __DATA.__objc_data: 0x1ca8
   __DATA.__data: 0xe80
-  __DATA.__bss: 0x4a0
+  __DATA.__bss: 0x4b0
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1457
-  Symbols:   5077
-  CStrings:  3428
+  Functions: 1460
+  Symbols:   5085
+  CStrings:  3438
 
Symbols:
+ +[SafariSettingsController isContentFilteringEnabled]
+ +[SafariSettingsController isScreenTimeManagedByParent]
+ -[SafariSettingsController _updateUserRestrictedState]
+ GCC_except_table115
+ GCC_except_table120
+ GCC_except_table186
+ GCC_except_table43
+ GCC_except_table46
+ GCC_except_table50
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table62
+ GCC_except_table69
+ GCC_except_table74
+ ___54-[CreateEditProfileViewController deleteButtonTapped:]_block_invoke_3
+ ___54-[SafariSettingsController _updateUserRestrictedState]_block_invoke
+ ___54-[SafariSettingsController _updateUserRestrictedState]_block_invoke_2
+ __block_literal_global.187
+ __isContentFilteringEnabled
+ __isScreenTimeManagedByParent
+ _objc_msgSend$_updateUserRestrictedState
+ _objc_msgSend$determineIfScreenTimeIsManagedByParentWithCompletionHandler:
+ _objc_msgSend$isContentFilteringEnabled
+ _objc_msgSend$isScreenTimeManagedByParent
- -[SafariSettingsController _updatePrivateBrowsingAvailability]
- GCC_except_table113
- GCC_except_table118
- GCC_except_table184
- GCC_except_table45
- GCC_except_table47
- GCC_except_table49
- GCC_except_table51
- GCC_except_table52
- GCC_except_table59
- GCC_except_table61
- GCC_except_table63
- GCC_except_table72
- OBJC_IVAR_$_SafariSettingsController._isPrivateBrowsingAvailable
- ___62-[SafariSettingsController _updatePrivateBrowsingAvailability]_block_invoke
- ___62-[SafariSettingsController _updatePrivateBrowsingAvailability]_block_invoke_2
- _objc_msgSend$_updatePrivateBrowsingAvailability
- _objc_msgSend$determineIfPrivateBrowsingIsAvailableWithCompletionHandler:
CStrings:
+ "Screen Time Settings"
+ "TB,R,N,GisContentFilteringEnabled"
+ "TB,R,N,GisScreenTimeManagedByParent"
+ "Unable To Delete Profile Due To Content Filter Explanation"
+ "Unable To Delete Profile Due To Screen Time Managed By Parent Explanation"
+ "Unable To Delete Profile Title"
+ "_updateUserRestrictedState"
+ "contentFilteringEnabled"
+ "determineIfScreenTimeIsManagedByParentWithCompletionHandler:"
+ "isContentFilteringEnabled"
+ "isScreenTimeManagedByParent"
+ "screenTimeManagedByParent"
+ "settings-navigation://com.apple.Settings.ScreenTime/CONTENT_PRIVACY"
- "_isPrivateBrowsingAvailable"
- "_updatePrivateBrowsingAvailability"
- "determineIfPrivateBrowsingIsAvailableWithCompletionHandler:"

```
