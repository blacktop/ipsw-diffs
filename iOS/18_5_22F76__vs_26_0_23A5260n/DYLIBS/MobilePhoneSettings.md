## MobilePhoneSettings

> `/System/Library/PreferenceBundles/MobilePhoneSettings.bundle/MobilePhoneSettings`

```diff

-2975.600.42.2.1
-  __TEXT.__text: 0x540c
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0x808
-  __TEXT.__cstring: 0x78d
+3011.100.2.2.10
+  __TEXT.__text: 0x559c
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x850
+  __TEXT.__cstring: 0x7f3
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__oslogstring: 0x18b
+  __TEXT.__gcc_except_tab: 0xc4
+  __TEXT.__oslogstring: 0x1aa
   __TEXT.__unwind_info: 0x1e8
-  __TEXT.__objc_classname: 0x189
-  __TEXT.__objc_methname: 0x1a80
-  __TEXT.__objc_methtype: 0x464
-  __TEXT.__objc_stubs: 0x18e0
-  __DATA_CONST.__got: 0x158
+  __TEXT.__objc_classname: 0x1b7
+  __TEXT.__objc_methname: 0x1b98
+  __TEXT.__objc_methtype: 0x4dc
+  __TEXT.__objc_stubs: 0x1980
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x800
+  __DATA_CONST.__objc_selrefs: 0x840
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__auth_got: 0x1e0
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__objc_const: 0xd90
+  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__objc_const: 0xdf0
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x5c
-  __DATA.__data: 0x300
+  __DATA.__objc_ivar: 0x60
+  __DATA.__data: 0x360
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppSystemSettingsUI.framework/AppSystemSettingsUI
+  - /System/Library/PrivateFrameworks/CallsDialer.framework/CallsDialer
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences
   - /System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI

   - /System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 302C800C-3855-3624-B992-AFB991EBA8AE
-  Functions: 143
-  Symbols:   752
-  CStrings:  505
+  UUID: E82C9A32-70B1-3B58-B59D-033D4E4F27CF
+  Functions: 146
+  Symbols:   775
+  CStrings:  527
 
Symbols:
+ -[VMAccountsViewController accountsChangesListener]
+ -[VMAccountsViewController handleVoicemailManagerAccountsDidChange]
+ -[VMAccountsViewController setAccountsChangesListener:]
+ _OBJC_CLASS_$_PSSpecifier
+ _OBJC_IVAR_$_VMAccountsViewController._accountsChangesListener
+ _PSBundleOverridePrincipalClassKey
+ _PSBundlePathForPreferenceBundle
+ _PSDetailControllerClassKey
+ _PSLazilyLoadedBundleKey
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AUSystemSettingsSpecifiersProviderDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AUSystemSettingsSpecifiersProviderDelegate
+ __OBJC_$_PROTOCOL_REFS_AUSystemSettingsSpecifiersProviderDelegate
+ __OBJC_LABEL_PROTOCOL_$_AUSystemSettingsSpecifiersProviderDelegate
+ __OBJC_PROTOCOL_$_AUSystemSettingsSpecifiersProviderDelegate
+ ___67-[VMAccountsViewController handleVoicemailManagerAccountsDidChange]_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.62
+ ___block_literal_global.65
+ ___kCFBooleanTrue
+ _objc_msgSend$handleVoicemailManagerAccountsDidChange
+ _objc_msgSend$identifier
+ _objc_msgSend$preferenceSpecifierNamed:target:set:get:detail:cell:edit:
+ _objc_msgSend$setControllerLoadAction:
+ _objc_msgSend$setProperty:forKey:
- ___82-[VMAccountsViewController handleVMVoicemailManagerAccountsDidChangeNotification:]_block_invoke
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_literal_global.44
- ___block_literal_global.47
CStrings:
+ "%@ is handling VoicemailManagerAccountsDidChange"
+ "@"
+ "AUSystemSettingsSpecifiersProviderDelegate"
+ "BLOCKED_CONTACTS"
+ "BlocklistSettings"
+ "PHBlocklistSettingsListController"
+ "T@,&,N,V_accountsChangesListener"
+ "UNKNOWN_NUMBERS_GROUP_SPACER_END"
+ "_accountsChangesListener"
+ "accountsChangesListener"
+ "handleVoicemailManagerAccountsDidChange"
+ "identifier"
+ "lazyLoadBundle:"
+ "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
+ "setAccountsChangesListener:"
+ "setControllerLoadAction:"
+ "setProperty:forKey:"
+ "v24@0:8@\"AUSystemSettingsSpecifiersProvider\"16"
+ "v36@0:8@\"AUSystemSettingsSpecifiersProvider\"16@\"UIViewController\"24B32"
- "%@ is handling %@"

```
