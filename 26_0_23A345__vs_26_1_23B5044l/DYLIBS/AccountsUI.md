## AccountsUI

> `/System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI`

```diff

-365.0.0.0.0
-  __TEXT.__text: 0x3e858
+367.0.0.0.0
+  __TEXT.__text: 0x3bc2c
   __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x1a5c
-  __TEXT.__cstring: 0x2dcf
+  __TEXT.__objc_methlist: 0x1a14
+  __TEXT.__cstring: 0x2c66
   __TEXT.__oslogstring: 0x12ce
   __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0x950
+  __TEXT.__gcc_except_tab: 0x930
   __TEXT.__ustring: 0x10
-  __TEXT.__dlopen_cstrs: 0x1ae
-  __TEXT.__unwind_info: 0x4c8
-  __TEXT.__objc_classname: 0x45f
-  __TEXT.__objc_methname: 0x62b1
-  __TEXT.__objc_methtype: 0x116d
-  __TEXT.__objc_stubs: 0x5520
-  __DATA_CONST.__got: 0x668
-  __DATA_CONST.__const: 0x9b0
+  __TEXT.__dlopen_cstrs: 0xc6
+  __TEXT.__unwind_info: 0x4a0
+  __TEXT.__objc_classname: 0x45c
+  __TEXT.__objc_methname: 0x60fb
+  __TEXT.__objc_methtype: 0x11a5
+  __TEXT.__objc_stubs: 0x5260
+  __DATA_CONST.__got: 0x678
+  __DATA_CONST.__const: 0x980
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19d0
+  __DATA_CONST.__objc_selrefs: 0x1918
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x2e0
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x2580
-  __AUTH_CONST.__objc_const: 0x3b08
+  __AUTH_CONST.__cfstring: 0x2540
+  __AUTH_CONST.__objc_const: 0x3a28
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0x17c
+  __DATA.__objc_ivar: 0x160
   __DATA.__data: 0x748
-  __DATA.__bss: 0x118
+  __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7EC85582-5097-3D6E-B3F7-B2A964B9AEA2
-  Functions: 576
-  Symbols:   2683
-  CStrings:  1926
+  UUID: 6DE62BE2-7FDF-3520-9C72-3F772B3B3A02
+  Functions: 557
+  Symbols:   2608
+  CStrings:  1886
 
Symbols:
+ +[ACUIAccountSummaryCell _enabledDataclassesTextForAccount:]
+ +[ACUIAccountSummaryCell _numberFormatter]
+ -[ACUIAccountViewProvidersManager viewControllerClassForViewingAccount:specifier:presentingVC:]
+ _ACAccountDataclassContactsSearch
+ _ACAccountDataclassDeviceLocator
+ _ACAccountDataclassNetworkVPN
+ _ACAccountDataclassSharedStreams
+ _OBJC_CLASS_$_NSListFormatter
+ _OBJC_CLASS_$_PSSubtitleDisclosureTableCell
+ _PSTableCellSubtitleTextKey
+ ___48-[ACUISettingsController _accountStoreDidChange]_block_invoke.59
+ ___block_literal_global.74
+ ___block_literal_global.95
+ _objc_msgSend$_enabledDataclassesTextForAccount:
+ _objc_msgSend$applicationState
+ _objc_msgSend$initWithBundleIdentifier:fetchingPlaceholder:error:
+ _objc_msgSend$localizedStringByJoiningStrings:
+ _objc_msgSend$viewControllerClassForViewingAccount:specifier:presentingVC:
+ _objc_opt_self
- -[ACUIAccountSummaryCell .cxx_destruct]
- -[ACUIAccountSummaryCell _dataclassesLabel]
- -[ACUIAccountSummaryCell _enabledDataclassesTextForWidth:]
- -[ACUIAccountSummaryCell _font]
- -[ACUIAccountSummaryCell _numberFormatter]
- -[ACUIAccountSummaryCell hideDataclass:]
- -[ACUIAccountSummaryCell layoutSubviews]
- -[ACUIAccountSummaryCell prepareForReuse]
- -[ACUIAccountSummaryCell refreshCellContentsWithSpecifier:]
- -[ACUISettingsController navigationItem]
- GCC_except_table52
- GCC_except_table54
- _OBJC_CLASS_$_LSApplicationProxy
- _OBJC_CLASS_$_UIListContentConfiguration
- _OBJC_IVAR_$_ACUIAccountSummaryCell._account
- _OBJC_IVAR_$_ACUIAccountSummaryCell._dataclassesLabel
- _OBJC_IVAR_$_ACUIAccountSummaryCell._desiredValue
- _OBJC_IVAR_$_ACUIAccountSummaryCell._enabledDataclasses
- _OBJC_IVAR_$_ACUIAccountSummaryCell._style
- _OBJC_IVAR_$_ACUIAccountSummaryCell._supportedDataclasses
- _OBJC_IVAR_$_ACUIAccountSummaryCell._useCustomDetailsText
- _UIContentSizeCategoryIsAccessibilityCategory
- _UIRectGetMaxX
- __OBJC_$_INSTANCE_METHODS_ACUIAccountSummaryCell
- __OBJC_$_INSTANCE_VARIABLES_ACUIAccountSummaryCell
- ___48-[ACUISettingsController _accountStoreDidChange]_block_invoke.72
- ___block_literal_global.76
- ___block_literal_global.97
- ___getiCloudCalendarUnifiedSettingsProviderObjcClass_block_invoke
- ___getiCloudMailUnifiedSettingsProviderObjcClass_block_invoke
- ___iCloudCalendarUnifiedSettingsLibraryCore_block_invoke
- ___iCloudMailUnifiedSettingsLibraryCore_block_invoke
- _audit_stringiCloudCalendarUnifiedSettings
- _audit_stringiCloudMailUnifiedSettings
- _getiCloudCalendarUnifiedSettingsProviderObjcClass
- _getiCloudCalendarUnifiedSettingsProviderObjcClass.softClass
- _getiCloudMailUnifiedSettingsProviderObjcClass
- _getiCloudMailUnifiedSettingsProviderObjcClass.softClass
- _iCloudCalendarUnifiedSettingsLibrary
- _iCloudCalendarUnifiedSettingsLibraryCore
- _iCloudCalendarUnifiedSettingsLibraryCore.frameworkLibrary
- _iCloudMailUnifiedSettingsLibrary
- _iCloudMailUnifiedSettingsLibraryCore
- _iCloudMailUnifiedSettingsLibraryCore.frameworkLibrary
- _kAccountDataclassMessages
- _kAccountDataclassSharedStreams
- _kAccountDataclassStocks
- _objc_msgSend$_dataclassesLabel
- _objc_msgSend$_enabledDataclassesTextForWidth:
- _objc_msgSend$_font
- _objc_msgSend$_shouldReverseLayoutDirection
- _objc_msgSend$appState
- _objc_msgSend$applicationProxyForIdentifier:
- _objc_msgSend$autoupdatingCurrentLocale
- _objc_msgSend$contentView
- _objc_msgSend$detailTextLabel
- _objc_msgSend$floatValue
- _objc_msgSend$font
- _objc_msgSend$initWithPresenter:
- _objc_msgSend$isInstalled
- _objc_msgSend$navigateToiCloudCalendarSettingsWithDeeplink:
- _objc_msgSend$navigateToiCloudMailSettingsWithDeeplink:
- _objc_msgSend$numberWithDouble:
- _objc_msgSend$preferredContentSizeCategory
- _objc_msgSend$removeObject:
- _objc_msgSend$secondaryTextProperties
- _objc_msgSend$setBackButtonTitle:
- _objc_msgSend$setLocale:
- _objc_msgSend$setNeedsLayout
- _objc_msgSend$setNumberStyle:
- _objc_msgSend$setOpaque:
- _objc_msgSend$sizeWithAttributes:
- _objc_msgSend$subtitleCellConfiguration
- _objc_msgSend$traitCollection
CStrings:
+ "#40@0:8@\"ACAccount\"16@\"PSSpecifier\"24@\"UIViewController\"32"
+ "#40@0:8@16@24@32"
+ "_enabledDataclassesTextForAccount:"
+ "applicationState"
+ "initWithBundleIdentifier:fetchingPlaceholder:error:"
+ "localizedStringByJoiningStrings:"
+ "viewControllerClassForViewingAccount:specifier:presentingVC:"
- "@\"NSSet\""
- "@24@0:8d16"
- "ACUISettingsController.m"
- "COMBINED_STRING"
- "Class getiCloudCalendarUnifiedSettingsProviderObjcClass(void)_block_invoke"
- "Class getiCloudMailUnifiedSettingsProviderObjcClass(void)_block_invoke"
- "_dataclassesLabel"
- "_desiredValue"
- "_enabledDataclasses"
- "_enabledDataclassesTextForWidth:"
- "_font"
- "_shouldReverseLayoutDirection"
- "_style"
- "_supportedDataclasses"
- "_useCustomDetailsText"
- "appState"
- "applicationProxyForIdentifier:"
- "autoupdatingCurrentLocale"
- "contentView"
- "detailTextLabel"
- "floatValue"
- "font"
- "hideDataclass:"
- "iCloudCalendarUnifiedSettingsProviderObjc"
- "iCloudMailUnifiedSettingsProviderObjc"
- "initWithPresenter:"
- "isInstalled"
- "navigateToiCloudCalendarSettingsWithDeeplink:"
- "navigateToiCloudMailSettingsWithDeeplink:"
- "numberWithDouble:"
- "preferredContentSizeCategory"
- "removeObject:"
- "secondaryTextProperties"
- "setBackButtonTitle:"
- "setLocale:"
- "setNeedsLayout"
- "setNumberStyle:"
- "setOpaque:"
- "sizeWithAttributes:"
- "softlink:r:path:/System/Library/PrivateFrameworks/iCloudCalendarUnifiedSettings.framework/iCloudCalendarUnifiedSettings"
- "softlink:r:path:/System/Library/PrivateFrameworks/iCloudMailUnifiedSettings.framework/iCloudMailUnifiedSettings"
- "subtitleCellConfiguration"
- "traitCollection"
- "void *iCloudCalendarUnifiedSettingsLibrary(void)"
- "void *iCloudMailUnifiedSettingsLibrary(void)"

```
