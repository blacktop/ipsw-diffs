## VideoSubscriberAccountUI

> `/System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI`

```diff

-511.1.1.0.0
-  __TEXT.__text: 0x5508c
+511.10.14.0.0
+  __TEXT.__text: 0x556c4
   __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x6b30
+  __TEXT.__objc_methlist: 0x6be0
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x4f8f
-  __TEXT.__gcc_except_tab: 0xddc
+  __TEXT.__cstring: 0x4fe3
+  __TEXT.__gcc_except_tab: 0xdec
   __TEXT.__oslogstring: 0x337f
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x14e8
-  __TEXT.__objc_classname: 0x1387
-  __TEXT.__objc_methname: 0x13f4e
-  __TEXT.__objc_methtype: 0x3296
-  __TEXT.__objc_stubs: 0xd920
+  __TEXT.__unwind_info: 0x14ec
+  __TEXT.__objc_classname: 0x13b0
+  __TEXT.__objc_methname: 0x1425c
+  __TEXT.__objc_methtype: 0x32bd
+  __TEXT.__objc_stubs: 0xda80
   __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x17d8
-  __DATA_CONST.__objc_classlist: 0x3e8
-  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__const: 0x17b8
+  __DATA_CONST.__objc_classlist: 0x3f0
+  __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x14798
-  __DATA_CONST.__objc_selrefs: 0x4378
+  __DATA_CONST.__objc_const: 0x148b0
+  __DATA_CONST.__objc_selrefs: 0x4400
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__objc_const: 0x2b68
-  __AUTH_CONST.__cfstring: 0x4260
+  __AUTH_CONST.__objc_const: 0x2bf0
+  __AUTH_CONST.__cfstring: 0x42e0
   __AUTH_CONST.__const: 0x580
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x448
-  __AUTH.__objc_data: 0x2490
+  __AUTH.__objc_data: 0x24e0
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x830
-  __DATA.__objc_superrefs: 0x300
-  __DATA.__objc_ivar: 0x938
+  __DATA.__objc_classrefs: 0x848
+  __DATA.__objc_superrefs: 0x308
+  __DATA.__objc_ivar: 0x948
   __DATA.__data: 0x17c0
   __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount
   - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI
+  - /System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/ITMLKit.framework/ITMLKit
   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport

   - /System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F3E316A3-522A-35EA-9B16-1C9DC5BBD995
-  Functions: 2621
-  Symbols:   9771
-  CStrings:  5340
+  UUID: 91EC2063-AFE6-3B4E-B133-7E2E1800B3BB
+  Functions: 2634
+  Symbols:   9825
+  CStrings:  5376
 
Symbols:
+ +[ASCLockupRequest(VSUIAdditions) tvProviderLockupRequestWithAdamID:]
+ -[VSAMSAppsValueTransformer platformAttributes:forDevice:]
+ -[VSAMSAppsValueTransformer responseDeviceFamilies:compatibleWithDevice:]
+ -[VSAMSIdentityProviderResponseDictionaryValueTransformer createProviderAppArtworkFromAttributes:]
+ -[VSAppDocumentController _getSupportedButtonTextsforTemplate:andElementKeys:supportedCount:]
+ -[VSAppDocumentController _getSupportedButtonTextsforTemplate:andElementKeys:supportedCount:].cold.1
+ -[VSApplication canRequireSystemTrust]
+ -[VSApplication setCanRequireSystemTrust:]
+ -[VSCredentialEntryTableView .cxx_destruct]
+ -[VSCredentialEntryTableView layoutSubviews]
+ -[VSCredentialEntryTableView setViewController:]
+ -[VSCredentialEntryTableView viewController]
+ -[VSCredentialEntryViewController_iOS tableViewClass]
+ -[VSIdentityProviderPickerViewController_iOS footerView]
+ -[VSIdentityProviderPickerViewController_iOS setFooterView:]
+ -[VSIdentityProviderPickerViewController_iOS tableView:viewForFooterInSection:]
+ -[VSNonChannelAppDecider bincompatDeviceFamily]
+ -[VSNonChannelAppDecider setBincompatDeviceFamily:]
+ _ASCLockupContextTVProvider
+ _ASCLockupKindApp
+ _OBJC_CLASS_$_ASCAdamID
+ _OBJC_CLASS_$_ASCLockupRequest
+ _OBJC_CLASS_$_UITableView
+ _OBJC_CLASS_$_VSCredentialEntryTableView
+ _OBJC_CLASS_$_VideosUISwiftExternal
+ _OBJC_IVAR_$_VSApplication._canRequireSystemTrust
+ _OBJC_IVAR_$_VSCredentialEntryTableView._viewController
+ _OBJC_IVAR_$_VSIdentityProviderPickerViewController_iOS._footerView
+ _OBJC_IVAR_$_VSNonChannelAppDecider._bincompatDeviceFamily
+ _OBJC_METACLASS_$_UITableView
+ _OBJC_METACLASS_$_VSCredentialEntryTableView
+ __OBJC_$_CATEGORY_ASCLockupRequest_$_VSUIAdditions
+ __OBJC_$_CLASS_METHODS_ASCLockupRequest(VSUIAdditions)
+ __OBJC_$_INSTANCE_METHODS_VSCredentialEntryTableView
+ __OBJC_$_INSTANCE_VARIABLES_VSCredentialEntryTableView
+ __OBJC_$_PROP_LIST_VSCredentialEntryTableView
+ __OBJC_CLASS_RO_$_VSCredentialEntryTableView
+ __OBJC_METACLASS_RO_$_VSCredentialEntryTableView
+ _kVSASCLockupRequestMediaClientID
+ _objc_msgSend$_setSectionContentInsetFollowsLayoutMargins:
+ _objc_msgSend$allowNonSystemTrust
+ _objc_msgSend$ascAppInstallerViewControllerWithTitle:subtitle:request:forceDSIDlessInstall:onFlowCompletion:
+ _objc_msgSend$bincompatOS
+ _objc_msgSend$bincompatPlatform
+ _objc_msgSend$canRequireSystemTrust
+ _objc_msgSend$createProviderAppArtworkFromAttributes:
+ _objc_msgSend$footerView
+ _objc_msgSend$initWithID:kind:context:
+ _objc_msgSend$initWithRootViewController:
+ _objc_msgSend$initWithStringValue:
+ _objc_msgSend$lockupRequestWithClientID:
+ _objc_msgSend$numberOfSections
+ _objc_msgSend$platformAttributes:forDevice:
+ _objc_msgSend$requireAuthenticationURLSystemTrust
+ _objc_msgSend$requireXHRRequestSystemTrust
+ _objc_msgSend$responseDeviceFamilies:compatibleWithDevice:
+ _objc_msgSend$setBincompatDeviceFamily:
+ _objc_msgSend$setCanRequireSystemTrust:
+ _objc_msgSend$setCanRequireSystemTrustForXHRs:
+ _objc_msgSend$setFooterView:
+ _objc_msgSend$setRequireAuthenticationURLSystemTrust:
+ _objc_msgSend$setRequireXHRRequestSystemTrust:
+ _objc_msgSend$setViewController:
+ _objc_msgSend$tvProviderLockupRequestWithAdamID:
+ _objc_msgSend$viewController
- -[VSAppDocumentController _getSupportedButtonTextsforTemplate:supportedCount:]
- -[VSAppDocumentController _getSupportedButtonTextsforTemplate:supportedCount:].cold.1
- -[VSIdentityProviderPickerViewController_iOS _updateSectionContentInsetWithAnimation:]
- -[VSIdentityProviderPickerViewController_iOS resizeFooterViewIfNeeded]
- _CGPointZero
- _OBJC_CLASS_$_VUIAppInstallerViewController
- _UILayoutFittingCompressedSize
- ___86-[VSIdentityProviderPickerViewController_iOS _updateSectionContentInsetWithAnimation:]_block_invoke
- ___block_descriptor_72_e8_32s_e5_v8?0ls32l8
- _objc_msgSend$_sectionContentInset
- _objc_msgSend$_updateSectionContentInsetWithAnimation:
- _objc_msgSend$addTarget:action:forEvents:
- _objc_msgSend$beginInstallingAppWithProgressHandler:completion:
- _objc_msgSend$initWithInstallable:
- _objc_msgSend$performWithoutAnimation:
- _objc_msgSend$resizeFooterViewIfNeeded
- _objc_msgSend$safeAreaInsets
- _objc_msgSend$sectionContentInsetInitialized
- _objc_msgSend$setConfirmationBody:
- _objc_msgSend$setConfirmationTitle:
- _objc_msgSend$setSectionContentInset:
- _objc_msgSend$setSectionContentInsetInitialized:
- _objc_msgSend$setTableFooterView:
- _objc_msgSend$tableFooterView
CStrings:
+ "!\x1f\x04"
+ "@\"VSCredentialEntryViewController_iOS\""
+ "CREDENTIAL_ENTRY_FOOTER_IOS"
+ "T@\"NSString\",C,N,V_bincompatDeviceFamily"
+ "T@\"UIView\",&,N,V_footerView"
+ "T@\"VSCredentialEntryViewController_iOS\",W,N,V_viewController"
+ "TB,N,V_canRequireSystemTrust"
+ "TVProvider"
+ "The textElement parameter must not be nil."
+ "VSCredentialEntryTableView"
+ "VSUIAdditions"
+ "_bincompatDeviceFamily"
+ "_canRequireSystemTrust"
+ "_footerView"
+ "_getSupportedButtonTextsforTemplate:andElementKeys:supportedCount:"
+ "_setSectionContentInsetFollowsLayoutMargins:"
+ "_viewController"
+ "allowNonSystemTrust"
+ "ascAppInstallerViewControllerWithTitle:subtitle:request:forceDSIDlessInstall:onFlowCompletion:"
+ "bincompatDeviceFamily"
+ "bincompatOS"
+ "bincompatPlatform"
+ "canRequireSystemTrust"
+ "createProviderAppArtworkFromAttributes:"
+ "footerView"
+ "initWithID:kind:context:"
+ "initWithRootViewController:"
+ "initWithStringValue:"
+ "lockupRequestWithClientID:"
+ "numberOfSections"
+ "platformAttributes:forDevice:"
+ "requireAuthenticationURLSystemTrust"
+ "requireXHRRequestSystemTrust"
+ "responseDeviceFamilies:compatibleWithDevice:"
+ "setBincompatDeviceFamily:"
+ "setCanRequireSystemTrust:"
+ "setCanRequireSystemTrustForXHRs:"
+ "setFooterView:"
+ "setRequireAuthenticationURLSystemTrust:"
+ "setRequireXHRRequestSystemTrust:"
+ "setViewController:"
+ "tableView:viewForFooterInSection:"
+ "tableViewClass"
+ "tvProviderLockupRequestWithAdamID:"
+ "viewController"
- "!\x1f\x03"
- "_getSupportedButtonTextsforTemplate:supportedCount:"
- "_sectionContentInset"
- "_updateSectionContentInsetWithAnimation:"
- "addTarget:action:forEvents:"
- "beginInstallingAppWithProgressHandler:completion:"
- "initWithInstallable:"
- "performWithoutAnimation:"
- "resizeFooterViewIfNeeded"
- "safeAreaInsets"
- "setConfirmationBody:"
- "setConfirmationTitle:"
- "setTableFooterView:"
- "tableFooterView"

```
