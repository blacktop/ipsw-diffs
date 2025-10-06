## Preferences

> `/System/Library/PrivateFrameworks/Preferences.framework/Preferences`

```diff

-5215.5.15.0.0
-  __TEXT.__text: 0xdd6f8
-  __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_methlist: 0xaae8
+5215.5.18.0.0
+  __TEXT.__text: 0xde678
+  __TEXT.__auth_stubs: 0x1790
+  __TEXT.__objc_methlist: 0xab98
   __TEXT.__const: 0x1fc
   __TEXT.__gcc_except_tab: 0x1dbc
-  __TEXT.__cstring: 0xe1eb
+  __TEXT.__cstring: 0xe38f
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x2014
   __TEXT.__oslogstring: 0x3564
-  __TEXT.__unwind_info: 0x396c
-  __TEXT.__objc_classname: 0x1d4e
-  __TEXT.__objc_methname: 0x1e77c
-  __TEXT.__objc_methtype: 0x4534
-  __TEXT.__objc_stubs: 0x16f20
+  __TEXT.__unwind_info: 0x39a4
+  __TEXT.__objc_classname: 0x1d67
+  __TEXT.__objc_methname: 0x1e9d4
+  __TEXT.__objc_methtype: 0x4550
+  __TEXT.__objc_stubs: 0x17120
   __DATA_CONST.__got: 0x5e8
-  __DATA_CONST.__const: 0x3bc0
-  __DATA_CONST.__objc_classlist: 0x6f8
+  __DATA_CONST.__const: 0x3bc8
+  __DATA_CONST.__objc_classlist: 0x700
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10b48
-  __DATA_CONST.__objc_selrefs: 0x71a8
+  __DATA_CONST.__objc_const: 0x10c30
+  __DATA_CONST.__objc_selrefs: 0x7248
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_classrefs: 0x8f8
-  __DATA_CONST.__objc_superrefs: 0x4a8
+  __DATA_CONST.__objc_classrefs: 0x908
+  __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x2d0
-  __AUTH_CONST.__cfstring: 0xcf20
-  __AUTH_CONST.__objc_const: 0x5278
-  __AUTH_CONST.__const: 0xc00
+  __AUTH_CONST.__cfstring: 0xd100
+  __AUTH_CONST.__objc_const: 0x52c0
+  __AUTH_CONST.__const: 0xc20
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xbd0
-  __AUTH.__objc_data: 0x3ac0
-  __DATA.__objc_ivar: 0xbc4
+  __AUTH_CONST.__auth_got: 0xbd8
+  __AUTH.__objc_data: 0x3b10
+  __DATA.__objc_ivar: 0xbd0
   __DATA.__data: 0x1b8a
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x948

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/Netrb.framework/Netrb
+  - /System/Library/PrivateFrameworks/SEService.framework/SEService
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 2F895CBE-A582-30F8-9B6A-8360B766F025
-  Functions: 5002
-  Symbols:   17507
-  CStrings:  10029
+  UUID: 7DC98AF1-1380-3802-BF4B-D209B1C5C338
+  Functions: 5020
+  Symbols:   17573
+  CStrings:  10084
 
Symbols:
+ -[PSNFCDefaultAppSpecifier .cxx_destruct]
+ -[PSNFCDefaultAppSpecifier context]
+ -[PSNFCDefaultAppSpecifier dealloc]
+ -[PSNFCDefaultAppSpecifier defaultNFCApp:]
+ -[PSNFCDefaultAppSpecifier delegate]
+ -[PSNFCDefaultAppSpecifier initWithBundleID:delegate:onChange:]
+ -[PSNFCDefaultAppSpecifier setDefaultNFCApp:specifier:]
+ -[PSNFCDefaultAppSpecifier setDelegate:]
+ -[PSSystemPolicyForApp contactlessNFCSideButtonSpecifiers]
+ -[PSSystemPolicyForApp contactlessNFCSpecifiers]
+ -[PSSystemPolicyForApp getDoubleClickForNFC:]
+ -[PSSystemPolicyForApp nfcContext]
+ -[PSSystemPolicyForApp setDoubleClickForNFC:specifier:]
+ -[PSSystemPolicyForApp setNfcContext:]
+ GCC_except_table102
+ GCC_except_table107
+ _MGGetSInt32Answer
+ _OBJC_CLASS_$_PSNFCDefaultAppSpecifier
+ _OBJC_CLASS_$_SESNFCAppSettingsContext
+ _OBJC_IVAR_$_PSNFCDefaultAppSpecifier._context
+ _OBJC_IVAR_$_PSNFCDefaultAppSpecifier._delegate
+ _OBJC_IVAR_$_PSSystemPolicyForApp._nfcContext
+ _OBJC_METACLASS_$_PSNFCDefaultAppSpecifier
+ _PSListItemsControllerSpecifierKey
+ __OBJC_$_INSTANCE_METHODS_PSNFCDefaultAppSpecifier
+ __OBJC_$_INSTANCE_VARIABLES_PSNFCDefaultAppSpecifier
+ __OBJC_$_PROP_LIST_PSNFCDefaultAppSpecifier
+ __OBJC_CLASS_RO_$_PSNFCDefaultAppSpecifier
+ __OBJC_METACLASS_RO_$_PSNFCDefaultAppSpecifier
+ ___48-[PSSystemPolicyForApp contactlessNFCSpecifiers]_block_invoke
+ ___55-[PSNFCDefaultAppSpecifier setDefaultNFCApp:specifier:]_block_invoke
+ ___55-[PSNFCDefaultAppSpecifier setDefaultNFCApp:specifier:]_block_invoke_2
+ ___58-[PSSystemPolicyForApp contactlessNFCSideButtonSpecifiers]_block_invoke
+ ___block_literal_global.463
+ ___block_literal_global.524
+ ___block_literal_global.540
+ _objc_msgSend$alertMessageForDefaultAppChangeTo:
+ _objc_msgSend$bundleId
+ _objc_msgSend$contactlessNFCSideButtonSpecifiers
+ _objc_msgSend$contactlessNFCSpecifiers
+ _objc_msgSend$contextWithBundleId:onChange:
+ _objc_msgSend$defaultAppCandidates
+ _objc_msgSend$doubleClickToggleVisibilityType
+ _objc_msgSend$getDefaultNFCApplication
+ _objc_msgSend$initWithBundleID:delegate:onChange:
+ _objc_msgSend$isDoubleClickEnabled
+ _objc_msgSend$localizedDisplayName
+ _objc_msgSend$nfcContext
+ _objc_msgSend$setDefaultNFCApplication:
+ _objc_msgSend$setDoubleClickEnabled:
+ _objc_msgSend$setNfcContext:
+ _objc_msgSend$shouldShowDefaultNFCAppPicker
- GCC_except_table96
- ___block_literal_global.489
- ___block_literal_global.505
CStrings:
+ "&'"
+ "@\"SESNFCAppSettingsContext\""
+ "CANCEL_BUTTON"
+ "CHANGE_DEFAULT_CONTACTLESS_APP_ALERT_TITLE"
+ "CONTINUE_BUTTON"
+ "ContactlessAndCredentialSettings_Localizable"
+ "DEFAULT_CONTACTLESS_APP_FOOTER"
+ "DEFAULT_CONTACTLESS_APP_TITLE"
+ "DOUBLE_CLICK_FOR_NFC"
+ "DOUBLE_CLICK_FOR_NFC_GROUP"
+ "DOUBLE_CLICK_HOME_BUTTON"
+ "DOUBLE_CLICK_HOME_BUTTON_FOOTER"
+ "DOUBLE_CLICK_SIDE_BUTTON"
+ "DOUBLE_CLICK_SIDE_BUTTON_FOOTER"
+ "JwLB44/jEB8aFDpXQ16Tuw"
+ "NFC_DEFAULT_APP_GROUP"
+ "PSListItemsControllerSpecifierKey"
+ "PSNFCDefaultAppSpecifier"
+ "T@\"SESNFCAppSettingsContext\",&,N,V_nfcContext"
+ "T@\"SESNFCAppSettingsContext\",R,N,V_context"
+ "_nfcContext"
+ "alertMessageForDefaultAppChangeTo:"
+ "bundleId"
+ "contactlessNFCSideButtonSpecifiers"
+ "contactlessNFCSpecifiers"
+ "contextWithBundleId:onChange:"
+ "defaultAppCandidates"
+ "defaultNFCApp:"
+ "doubleClickToggleVisibilityType"
+ "getDefaultNFCApplication"
+ "getDoubleClickForNFC:"
+ "initWithBundleID:delegate:onChange:"
+ "isDoubleClickEnabled"
+ "localizedDisplayName"
+ "nfcContext"
+ "setDefaultNFCApp:specifier:"
+ "setDefaultNFCApplication:"
+ "setDoubleClickEnabled:"
+ "setDoubleClickForNFC:specifier:"
+ "setNfcContext:"
+ "shouldShowDefaultNFCAppPicker"
- "&&"

```
