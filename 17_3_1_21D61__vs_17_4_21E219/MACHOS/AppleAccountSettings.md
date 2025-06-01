## AppleAccountSettings

> `/System/Library/PreferenceBundles/AccountSettings/AppleAccountSettings.bundle/AppleAccountSettings`

```diff

-494.4.12.0.0
-  __TEXT.__text: 0x5bf28
+494.14.1.0.0
+  __TEXT.__text: 0x5cf7c
   __TEXT.__auth_stubs: 0xa10
-  __TEXT.__objc_stubs: 0xba00
-  __TEXT.__objc_methlist: 0x3ae8
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x2e86
-  __TEXT.__objc_methname: 0xf309
-  __TEXT.__oslogstring: 0x5b11
+  __TEXT.__objc_stubs: 0xbba0
+  __TEXT.__objc_methlist: 0x3b80
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x2f6a
+  __TEXT.__objc_methname: 0xf4f3
+  __TEXT.__oslogstring: 0x5c4d
   __TEXT.__objc_classname: 0xb3f
-  __TEXT.__objc_methtype: 0x34bc
-  __TEXT.__gcc_except_tab: 0x980
+  __TEXT.__objc_methtype: 0x34cd
+  __TEXT.__gcc_except_tab: 0x96c
   __TEXT.__dlopen_cstrs: 0x31d
-  __TEXT.__unwind_info: 0x16c4
+  __TEXT.__unwind_info: 0x16d0
   __DATA_CONST.__auth_got: 0x518
-  __DATA_CONST.__got: 0x5e0
-  __DATA_CONST.__const: 0x1990
-  __DATA_CONST.__cfstring: 0x37c0
+  __DATA_CONST.__got: 0x5e8
+  __DATA_CONST.__const: 0x1a20
+  __DATA_CONST.__cfstring: 0x38c0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x848
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xd8
-  __DATA.__objc_const: 0x11938
-  __DATA.__objc_selrefs: 0x36d8
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x840
-  __DATA.__objc_superrefs: 0x160
-  __DATA.__objc_ivar: 0x6d4
+  __DATA.__objc_const: 0x11978
+  __DATA.__objc_selrefs: 0x3740
+  __DATA.__objc_ivar: 0x6dc
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0xd80
   __DATA.__bss: 0x138

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F2647281-5E26-338D-A3C8-6E4E68B6FBE6
-  Functions: 1771
-  Symbols:   730
-  CStrings:  4248
+  UUID: D6A4BD3F-AAAB-38B4-994B-93DAB3E51A75
+  Functions: 1789
+  Symbols:   729
+  CStrings:  4288
 
Symbols:
+ _OBJC_CLASS_$_AAUIFeatureFlags
+ _PSControlIsLoadingKey
- _OBJC_CLASS_$_AAUIInviteMessageFlowController
- _OBJC_METACLASS_$_AAUIInviteMessageFlowController
- __AAUILogGreenTea
CStrings:
+ "@40@0:8@16@24d32"
+ "AAUIiCloudViewController dealloc."
+ "Account is nil, not displaying account settings cell."
+ "Account is nil, not displaying account summary cell."
+ "Adding spinner to specifier: %@"
+ "Apps syncing to drive request got an error. Bailing."
+ "CHANGE_PASSWORD_LINK"
+ "CHANGE_PASSWORD_LINK_SECONDARY_ACCOUNT"
+ "Fetched apps syncing to drive: %@, error: %@"
+ "Fetched storage used: %@, error: %@"
+ "ICLOUD_ADP_SPECIFIER_NAME"
+ "Missing strongSelf. AAUIiCloudViewController has been deallocated."
+ "Missing strongSelf. Stopping fetchCloudStorageSummary flow."
+ "PASSWORD_CHANGE_LABEL"
+ "PASSWORD_CHANGE_LABEL_SECONDARY_ACCOUNT"
+ "Setting up %@ storage used specifier with storage used %lld"
+ "Setting up apps syncing to drive specifier with number of apps syncing: %d"
+ "Storage used request got an error. Bailing."
+ "T@\"AACustodianshipInfo\",?,C,N"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"RUIObjectModel\",?,&,N"
+ "T@\"RUIServerHookResponse\",?,&,N"
+ "T@\"UIImage\",?,C,N"
+ "T@\"UIImage\",?,C,N,V_image"
+ "T@\"UIView\",?,C,N"
+ "T@\"UIView\",?,C,N,V_contentView"
+ "T@\"UIView\",?,C,N,V_secondaryView"
+ "Tq,?,N"
+ "Tq,?,N,V_contentViewLayout"
+ "_appsSyncingToDriveRequestDidError"
+ "_changePasswordLinkWasTapped"
+ "_isDemoAccount"
+ "_isSplitView"
+ "_loadCloudStorageSummary"
+ "_storageUsedRequestDidError"
+ "accountSettingsSpecifier"
+ "addBackgroundForImage:withBackgroundColor:yShift:"
+ "configurationWithWeight:"
+ "demoAccountForAccount:"
+ "groupSpecifierAccountSummary"
+ "https://appleid.apple.com"
+ "initWithNavigationItem:hideBackButton:"
+ "insertSubview:belowSubview:"
+ "isAccountDataclassListRedesignEnabled"
+ "isSecondaryAccount"
+ "localizedStringWithFormat:"
+ "specifierForAccountSettingsCell"
+ "systemImageNamed:withConfiguration:"
- "AAUICDPWebSpecifierProvider: ADP state changed, reloading specifier"
- "AAUICDPWebSpecifierProvider: fetched ADP state in background: %d"
- "AAUICDPWebSpecifierProvider: fetching ADP state in background"
- "Failed to fetch apps syncing to drive with error: %@"
- "Failed to fetch storage used data with error: %@"
- "T@\"AACustodianshipInfo\",C,N"
- "T@\"NSString\",C,N"
- "T@\"RUIObjectModel\",&,N"
- "T@\"RUIServerHookResponse\",&,N"
- "T@\"UIImage\",C,N"
- "T@\"UIImage\",C,N,V_image"
- "T@\"UIView\",C,N"
- "T@\"UIView\",C,N,V_contentView"
- "T@\"UIView\",C,N,V_secondaryView"
- "Tq,N"
- "Tq,N,V_contentViewLayout"
- "initWithNavigationItem:"
- "insertSubview:below:"

```
