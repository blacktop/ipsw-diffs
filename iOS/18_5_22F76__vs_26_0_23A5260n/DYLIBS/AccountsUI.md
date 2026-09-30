## AccountsUI

> `/System/Library/PrivateFrameworks/AccountsUI.framework/AccountsUI`

```diff

-351.1.0.0.0
-  __TEXT.__text: 0x4187c
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x1c5c
-  __TEXT.__cstring: 0x2fe6
-  __TEXT.__gcc_except_tab: 0xa2c
-  __TEXT.__const: 0x10
-  __TEXT.__dlopen_cstrs: 0x203
-  __TEXT.__oslogstring: 0x158f
+365.0.0.0.0
+  __TEXT.__text: 0x3e858
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0x1a5c
+  __TEXT.__cstring: 0x2dcf
+  __TEXT.__oslogstring: 0x12ce
+  __TEXT.__const: 0x8
+  __TEXT.__gcc_except_tab: 0x950
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x538
-  __TEXT.__objc_classname: 0x489
-  __TEXT.__objc_methname: 0x68a0
-  __TEXT.__objc_methtype: 0x1176
-  __TEXT.__objc_stubs: 0x5a20
-  __DATA_CONST.__got: 0x6d0
-  __DATA_CONST.__const: 0xa88
-  __DATA_CONST.__objc_classlist: 0xd8
+  __TEXT.__dlopen_cstrs: 0x1ae
+  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__objc_classname: 0x45f
+  __TEXT.__objc_methname: 0x62b1
+  __TEXT.__objc_methtype: 0x116d
+  __TEXT.__objc_stubs: 0x5520
+  __DATA_CONST.__got: 0x668
+  __DATA_CONST.__const: 0x9b0
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b88
+  __DATA_CONST.__objc_selrefs: 0x19d0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x308
-  __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x26a0
-  __AUTH_CONST.__objc_const: 0x3f48
+  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__cfstring: 0x2580
+  __AUTH_CONST.__objc_const: 0x3b08
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x1c4
-  __DATA.__data: 0x700
-  __DATA.__bss: 0x128
-  __DATA_DIRTY.__objc_data: 0xf0
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x17c
+  __DATA.__data: 0x748
+  __DATA.__bss: 0x118
+  __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 897BBCF6-CCAD-3219-8616-DAE27BBB5773
-  Functions: 627
-  Symbols:   2898
-  CStrings:  2057
+  UUID: DC19CC92-13E5-3C1A-A600-3D669347DD61
+  Functions: 576
+  Symbols:   2683
+  CStrings:  1926
 
Symbols:
+ +[ACUISetupViewController dataclassConfigurationControllerForAccount:name:specifier:completion:]
+ -[ACUIAccountCollectionLinkCell initWithStyle:reuseIdentifier:]
+ -[ACUIAccountCollectionLinkCell prepareForReuse]
+ -[ACUIAccountCollectionLinkCell refreshCellContentsWithSpecifier:]
+ -[ACUIAccountSummaryCell prepareForReuse]
+ -[ACUIAccountSummaryCell refreshCellContentsWithSpecifier:]
+ -[ACUIAddAccountViewController viewDidLoad]
+ -[ACUIIdentityPickerCell prepareForReuse]
+ -[ACUIIdentityPickerCell refreshCellContentsWithSpecifier:]
+ -[ACUISettingsController viewDidLoad]
+ GCC_except_table33
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table7
+ _ACAccountDataclassDeviceEnrollments
+ _AccountsUISettingsLibrary
+ _AccountsUISettingsLibraryCore
+ _AccountsUISettingsLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_ACUIIdentityPickerCell
+ _OBJC_IVAR_$_ACUIAddAccountViewController._modernAddFlow
+ _OBJC_METACLASS_$_ACUIIdentityPickerCell
+ __OBJC_$_INSTANCE_METHODS_ACUIIdentityPickerCell
+ __OBJC_CLASS_RO_$_ACUIIdentityPickerCell
+ __OBJC_METACLASS_RO_$_ACUIIdentityPickerCell
+ ___48-[ACUISettingsController _accountStoreDidChange]_block_invoke.72
+ ___62-[ACUIAddAccountViewController _addAccountSpecifierWasTapped:]_block_invoke.140
+ ___62-[ACUIAddAccountViewController _addAccountSpecifierWasTapped:]_block_invoke.142
+ ___69-[ACUIAddAccountViewController _createCustomControlledAccountTapped:]_block_invoke.188
+ ___69-[ACUIAddAccountViewController _createCustomControlledAccountTapped:]_block_invoke.189
+ ___87-[ACUIDataclassConfigurationViewController _setDataclass:enabled:onAccount:completion:]_block_invoke.151
+ ___96+[ACUISetupViewController dataclassConfigurationControllerForAccount:name:specifier:completion:]_block_invoke
+ ___AccountsUISettingsLibraryCore_block_invoke
+ ___block_literal_global.24
+ ___block_literal_global.370
+ ___block_literal_global.38
+ ___block_literal_global.53
+ ___block_literal_global.67
+ ___block_literal_global.76
+ ___block_literal_global.97
+ ___getACUISAddAccountControllerSwapClass_block_invoke
+ _audit_stringAccountsUISettings
+ _getACUISAddAccountControllerSwapClass
+ _getACUISAddAccountControllerSwapClass.softClass
+ _objc_msgSend$addChildViewController:
+ _objc_msgSend$bottomAnchor
+ _objc_msgSend$cellReuseIdentifier
+ _objc_msgSend$constraintEqualToAnchor:
+ _objc_msgSend$dataclassConfigurationControllerForAccount:name:specifier:completion:
+ _objc_msgSend$defaultContentConfiguration
+ _objc_msgSend$didMoveToParentViewController:
+ _objc_msgSend$layoutIfNeeded
+ _objc_msgSend$leadingAnchor
+ _objc_msgSend$modernAddFlowWrappedForViewController:
+ _objc_msgSend$registerClass:forCellReuseIdentifier:
+ _objc_msgSend$reloadSpecifier:
+ _objc_msgSend$setContentConfiguration:
+ _objc_msgSend$setReservedLayoutSize:
+ _objc_msgSend$size
+ _objc_msgSend$topAnchor
+ _objc_msgSend$trailingAnchor
- +[ACUIAppInstallCell specifierForAppWithDescription:target:action:]
- +[ACUIAppInstaller currentStoreFront]
- -[ACUIAccountCollectionLinkCell initWithStyle:reuseIdentifier:specifier:]
- -[ACUIAccountSummaryCell initWithStyle:reuseIdentifier:specifier:]
- -[ACUIAppDescription .cxx_destruct]
- -[ACUIAppDescription bundleID]
- -[ACUIAppDescription icon]
- -[ACUIAppDescription name]
- -[ACUIAppDescription persistentID]
- -[ACUIAppDescription publisher]
- -[ACUIAppDescription setBundleID:]
- -[ACUIAppDescription setIcon:]
- -[ACUIAppDescription setName:]
- -[ACUIAppDescription setPersistentID:]
- -[ACUIAppDescription setPublisher:]
- -[ACUIAppInstallCell .cxx_destruct]
- -[ACUIAppInstallCell _createInstallButton]
- -[ACUIAppInstallCell _createLabelForAppName:]
- -[ACUIAppInstallCell _createLabelForPublisher:]
- -[ACUIAppInstallCell _updateInstallButtonWithState:]
- -[ACUIAppInstallCell _updateSubviewsWithInstallState:]
- -[ACUIAppInstallCell initWithStyle:reuseIdentifier:specifier:]
- -[ACUIAppInstallCell installState]
- -[ACUIAppInstallCell layoutSubviews]
- -[ACUIAppInstallCell setInstallState:]
- -[ACUIAppInstallCell touchesBegan:withEvent:]
- -[ACUIAppInstallCell touchesCancelled:withEvent:]
- -[ACUIAppInstallCell touchesEnded:withEvent:]
- -[ACUIAppInstallCell touchesMoved:withEvent:]
- -[ACUIAppInstaller .cxx_destruct]
- -[ACUIAppInstaller _isGreenTeaAvailable]
- -[ACUIAppInstaller _performAvailabilityCheck:]
- -[ACUIAppInstaller _performReachabilityCheck:]
- -[ACUIAppInstaller _quicklyGenerateCachedReachabilityResultConsideringPublisherURL:]
- -[ACUIAppInstaller _setAvailableInStoreResult:]
- -[ACUIAppInstaller _setCachedReachabilityResult:]
- -[ACUIAppInstaller checkAvailabilityInStore:]
- -[ACUIAppInstaller delegate]
- -[ACUIAppInstaller fetchDownloadability:]
- -[ACUIAppInstaller initForAppWithDescription:]
- -[ACUIAppInstaller isAvailableInStore]
- -[ACUIAppInstaller isDownloadable]
- -[ACUIAppInstaller isInstalled]
- -[ACUIAppInstaller publisherURL]
- -[ACUIAppInstaller requiresReachabilityCheckToDetermineDownloadability]
- -[ACUIAppInstaller setDelegate:]
- -[ACUIAppInstaller setPublisherURL:]
- -[ACUIAppInstaller start]
- -[ACUIIdentityPickerViewController _updateCell:selected:]
- -[ACUIIdentityPickerViewController tableView:cellForRowAtIndexPath:]
- GCC_except_table11
- GCC_except_table13
- GCC_except_table18
- GCC_except_table31
- GCC_except_table5
- GCC_except_table51
- OBJC_IVAR_$_PSTableCell._specifier
- _ACUIAppIconKey
- _ACUIAppIsAlreadyInstalledKey
- _ACUIAppIsAvailableKey
- _ACUIAppNameKey
- _ACUIAppPublisherKey
- _CGRectGetMinX
- _IMAPLibrary
- _IMAPLibraryCore
- _IMAPLibraryCore.frameworkLibrary
- _MGGetBoolAnswer
- _OBJC_CLASS_$_ACUIAppDescription
- _OBJC_CLASS_$_ACUIAppInstallCell
- _OBJC_CLASS_$_ACUIAppInstaller
- _OBJC_CLASS_$_LSApplicationWorkspace
- _OBJC_CLASS_$_NSCharacterSet
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSURLConnection
- _OBJC_CLASS_$_NSURLRequest
- _OBJC_CLASS_$_SSDevice
- _OBJC_CLASS_$_SSItemLookupRequest
- _OBJC_CLASS_$_SSLookupRequest
- _OBJC_CLASS_$_SSPurchase
- _OBJC_CLASS_$_SSPurchaseRequest
- _OBJC_CLASS_$_UIImageView
- _OBJC_IVAR_$_ACUIAppDescription._bundleID
- _OBJC_IVAR_$_ACUIAppDescription._icon
- _OBJC_IVAR_$_ACUIAppDescription._name
- _OBJC_IVAR_$_ACUIAppDescription._persistentID
- _OBJC_IVAR_$_ACUIAppDescription._publisher
- _OBJC_IVAR_$_ACUIAppInstallCell._iconView
- _OBJC_IVAR_$_ACUIAppInstallCell._installButton
- _OBJC_IVAR_$_ACUIAppInstallCell._installState
- _OBJC_IVAR_$_ACUIAppInstallCell._nameLabel
- _OBJC_IVAR_$_ACUIAppInstallCell._publisherLabel
- _OBJC_IVAR_$_ACUIAppInstaller._app
- _OBJC_IVAR_$_ACUIAppInstaller._availableInStoreResult
- _OBJC_IVAR_$_ACUIAppInstaller._cachedReachabilityResult
- _OBJC_IVAR_$_ACUIAppInstaller._dateOfLastInstallationCheck
- _OBJC_IVAR_$_ACUIAppInstaller._dateOfLastReachabilityCheck
- _OBJC_IVAR_$_ACUIAppInstaller._delegate
- _OBJC_IVAR_$_ACUIAppInstaller._needsAvailableInStoreCheck
- _OBJC_IVAR_$_ACUIAppInstaller._publisherURL
- _OBJC_IVAR_$_ACUIAppInstaller._resultOfLastInstallationCheck
- _OBJC_METACLASS_$_ACUIAppDescription
- _OBJC_METACLASS_$_ACUIAppInstallCell
- _OBJC_METACLASS_$_ACUIAppInstaller
- _SBAddDownloadingIconForDisplayIdentifier
- _SSItemLookupParameterPersistentIdentifier
- _SSLookupKeyProfileLockup
- _SSLookupParameterBundleIdentifiers
- _StoreKitUILibrary
- _StoreKitUILibraryCore
- _StoreKitUILibraryCore.frameworkLibrary
- __OBJC_$_CLASS_METHODS_ACUIAppInstallCell
- __OBJC_$_CLASS_METHODS_ACUIAppInstaller
- __OBJC_$_INSTANCE_METHODS_ACUIAppDescription
- __OBJC_$_INSTANCE_METHODS_ACUIAppInstallCell
- __OBJC_$_INSTANCE_METHODS_ACUIAppInstaller
- __OBJC_$_INSTANCE_VARIABLES_ACUIAppDescription
- __OBJC_$_INSTANCE_VARIABLES_ACUIAppInstallCell
- __OBJC_$_INSTANCE_VARIABLES_ACUIAppInstaller
- __OBJC_$_PROP_LIST_ACUIAppDescription
- __OBJC_$_PROP_LIST_ACUIAppInstallCell
- __OBJC_$_PROP_LIST_ACUIAppInstaller
- __OBJC_CLASS_RO_$_ACUIAppDescription
- __OBJC_CLASS_RO_$_ACUIAppInstallCell
- __OBJC_CLASS_RO_$_ACUIAppInstaller
- __OBJC_METACLASS_RO_$_ACUIAppDescription
- __OBJC_METACLASS_RO_$_ACUIAppInstallCell
- __OBJC_METACLASS_RO_$_ACUIAppInstaller
- ___119+[ACUISetupViewController showDataclassConfigurationControllerForAccount:name:fromViewController:specifier:completion:]_block_invoke
- ___25-[ACUIAppInstaller start]_block_invoke
- ___34-[ACUIAppInstaller isDownloadable]_block_invoke
- ___38-[ACUIAppInstaller isAvailableInStore]_block_invoke
- ___46-[ACUIAppInstaller _performAvailabilityCheck:]_block_invoke
- ___46-[ACUIAppInstaller _performReachabilityCheck:]_block_invoke
- ___48-[ACUISettingsController _accountStoreDidChange]_block_invoke.65
- ___62-[ACUIAddAccountViewController _addAccountSpecifierWasTapped:]_block_invoke.135
- ___62-[ACUIAddAccountViewController _addAccountSpecifierWasTapped:]_block_invoke.137
- ___69-[ACUIAddAccountViewController _createCustomControlledAccountTapped:]_block_invoke.183
- ___69-[ACUIAddAccountViewController _createCustomControlledAccountTapped:]_block_invoke.184
- ___87-[ACUIDataclassConfigurationViewController _setDataclass:enabled:onAccount:completion:]_block_invoke.148
- ___IMAPLibraryCore_block_invoke
- ___StoreKitUILibraryCore_block_invoke
- ___block_descriptor_32_e8_v12?0B8l
- ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32bs40w_e38_v24?0"SSLookupResponse"8"NSError"16lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e5_v8?0ls32l8w48l8s40l8
- ___block_literal_global.18
- ___block_literal_global.29
- ___block_literal_global.35
- ___block_literal_global.351
- ___block_literal_global.50
- ___block_literal_global.61
- ___block_literal_global.69
- ___block_literal_global.92
- ___getIMAPAccountClass_block_invoke
- ___getSKUIItemOfferButtonClass_block_invoke
- ___os_log_helper_16_2_4_8_32_4_0_8_64_4_0
- _audit_stringIMAP
- _audit_stringStoreKitUI
- _getIMAPAccountClass
- _getIMAPAccountClass.softClass
- _getSKUIItemOfferButtonClass
- _getSKUIItemOfferButtonClass.softClass
- _objc_msgSend$ITunesStoreIdentifier
- _objc_msgSend$UTF8String
- _objc_msgSend$_checkmarkImage:
- _objc_msgSend$_createInstallButton
- _objc_msgSend$_createLabelForAppName:
- _objc_msgSend$_createLabelForPublisher:
- _objc_msgSend$_isGreenTeaAvailable
- _objc_msgSend$_performAvailabilityCheck:
- _objc_msgSend$_performReachabilityCheck:
- _objc_msgSend$_quicklyGenerateCachedReachabilityResultConsideringPublisherURL:
- _objc_msgSend$_setAvailableInStoreResult:
- _objc_msgSend$_setCachedReachabilityResult:
- _objc_msgSend$_updateCell:selected:
- _objc_msgSend$_updateInstallButtonWithState:
- _objc_msgSend$_updateSubviewsWithInstallState:
- _objc_msgSend$absoluteString
- _objc_msgSend$allItems
- _objc_msgSend$appInstallerWillStart:
- _objc_msgSend$appIsAvailableInStoreDidChange:
- _objc_msgSend$appIsDownloadableDidChange:
- _objc_msgSend$applicationIsInstalled:
- _objc_msgSend$bundleID
- _objc_msgSend$buttonAction
- _objc_msgSend$characterSetWithCharactersInString:
- _objc_msgSend$checkAvailabilityInStore:
- _objc_msgSend$date
- _objc_msgSend$defaultWorkspace
- _objc_msgSend$dictionaryWithObject:forKey:
- _objc_msgSend$fetchDownloadability:
- _objc_msgSend$icon
- _objc_msgSend$imageView
- _objc_msgSend$initWithImage:
- _objc_msgSend$initWithItem:
- _objc_msgSend$initWithPurchases:
- _objc_msgSend$persistentID
- _objc_msgSend$publisher
- _objc_msgSend$rangeOfCharacterFromSet:
- _objc_msgSend$requestWithURL:
- _objc_msgSend$sendSynchronousRequest:returningResponse:error:
- _objc_msgSend$setAlpha:
- _objc_msgSend$setKeyProfile:
- _objc_msgSend$setLocalizationStyle:
- _objc_msgSend$setTintColor:
- _objc_msgSend$setValue:forParameter:
- _objc_msgSend$setValue:forRequestParameter:
- _objc_msgSend$sharedApplication
- _objc_msgSend$start
- _objc_msgSend$startWithItemLookupBlock:
- _objc_msgSend$startWithLookupBlock:
- _objc_msgSend$statusCode
- _objc_msgSend$storeFrontIdentifier
- _objc_msgSend$stringValue
- _objc_msgSend$substringToIndex:
- _objc_msgSend$suspend
- _objc_msgSend$textLabel
- _objc_msgSend$timeIntervalSinceDate:
- _objc_msgSend$valueForProperty:
- _objc_sync_enter
- _objc_sync_exit
CStrings:
+ "+[ACUISetupViewController dataclassConfigurationControllerForAccount:name:specifier:completion:]"
+ "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
+ "@\"UIViewController\""
+ "@32@0:8q16@24"
+ "@48@0:8@16@24@32@?40"
+ "ACUIIdentityPickerCell"
+ "ACUISAddAccountControllerSwap"
+ "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
+ "Class getACUISAddAccountControllerSwapClass(void)_block_invoke"
+ "ModernAddFlow"
+ "PKPaymentAuthorizationModeBypassNative"
+ "_modernAddFlow"
+ "addChildViewController:"
+ "allowSelection"
+ "bottomAnchor"
+ "cellReuseIdentifier"
+ "checkmark"
+ "com.apple.graphic-icon.avp-setup"
+ "constraintEqualToAnchor:"
+ "dataclassConfigurationControllerForAccount:name:specifier:completion:"
+ "defaultContentConfiguration"
+ "didMoveToParentViewController:"
+ "identitySelected"
+ "initWithStyle:reuseIdentifier:"
+ "layoutIfNeeded"
+ "leadingAnchor"
+ "modernAddFlowWrappedForViewController:"
+ "prepareForReuse"
+ "refreshCellContentsWithSpecifier:"
+ "registerClass:forCellReuseIdentifier:"
+ "reloadSpecifier:"
+ "setContentConfiguration:"
+ "setReservedLayoutSize:"
+ "size"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AccountsUISettings.framework/AccountsUISettings"
+ "textField:editMenuForCharactersInRanges:suggestedActions:"
+ "textField:shouldChangeCharactersInRanges:replacementString:"
+ "topAnchor"
+ "trailingAnchor"
+ "void *AccountsUISettingsLibrary(void)"
- "%s (%d) \"%@ items matching PID %@ found.\""
- "%s (%d) \"ACUIAppInstaller currentStoreFront started with identifier '%@' and is returning storeFront '%@'\""
- "%s (%d) \"ACUIApplication %@ will begin downloading.\""
- "%s (%d) \"Contacting %@ to verify reachability of %@\""
- "%s (%d) \"Installation check for app %@ hasn't been done in a while.\""
- "%s (%d) \"Installation lookup result for bundle ID %@: %d\""
- "%s (%d) \"Reachability check for app %@ hasn't been done in a while.\""
- "%s (%d) \"Reachability check response had HTTP status code: %@\""
- "%s (%d) \"SS lookup failed to find an item for the app with PID: %@\""
- "%s (%d) \"Suspending current application to begin app install!\""
- "%s (%d) \"System reports having Green Tea capability as: %@\""
- "+[ACUIAppInstaller currentStoreFront]"
- "+[ACUISetupViewController showDataclassConfigurationControllerForAccount:name:fromViewController:specifier:completion:]"
- "-,"
- "-[ACUIAppInstaller _isGreenTeaAvailable]"
- "-[ACUIAppInstaller _performReachabilityCheck:]"
- "-[ACUIAppInstaller _performReachabilityCheck:]_block_invoke"
- "-[ACUIAppInstaller fetchDownloadability:]"
- "-[ACUIAppInstaller isInstalled]"
- "-[ACUIAppInstaller start]"
- "-[ACUIAppInstaller start]_block_invoke"
- "@\"<ACUIAppInstallerDelegate>\""
- "@\"ACUIAppDescription\""
- "@\"NSDate\""
- "@\"NSURL\""
- "@\"SKUIItemOfferButton\""
- "@\"UIImage\""
- "@\"UIImageView\""
- "@40@0:8q16@24@32"
- "ACUIAppDescription"
- "ACUIAppInstallCell"
- "ACUIAppInstallCell.m"
- "ACUIAppInstallIcon"
- "ACUIAppInstallName"
- "ACUIAppInstallPublisher"
- "ACUIAppInstaller"
- "ACUIAppIsAlreadyInstalled"
- "ACUIAppIsAvailable"
- "ACUISetupViewController.m"
- "ADD_ACCOUNT_TITLE"
- "B20@0:8B16"
- "Class getIMAPAccountClass(void)_block_invoke"
- "Class getSKUIItemOfferButtonClass(void)_block_invoke"
- "IMAPAccount"
- "INSTALLED"
- "INSTALLNOW"
- "ITunesStoreIdentifier"
- "SKUIItemOfferButton"
- "T@\"<ACUIAppInstallerDelegate>\",W,N,V_delegate"
- "T@\"NSString\",C,N,V_bundleID"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_persistentID"
- "T@\"NSString\",C,N,V_publisher"
- "T@\"NSURL\",&,N,V_publisherURL"
- "T@\"UIImage\",&,N,V_icon"
- "Ti,N,V_installState"
- "UNAVAILABLE"
- "UTF8String"
- "_app"
- "_availableInStoreResult"
- "_bundleID"
- "_cachedReachabilityResult"
- "_checkmarkImage:"
- "_createInstallButton"
- "_createLabelForAppName:"
- "_createLabelForPublisher:"
- "_dateOfLastInstallationCheck"
- "_dateOfLastReachabilityCheck"
- "_icon"
- "_iconView"
- "_installButton"
- "_installState"
- "_isGreenTeaAvailable"
- "_name"
- "_nameLabel"
- "_needsAvailableInStoreCheck"
- "_performAvailabilityCheck:"
- "_performReachabilityCheck:"
- "_persistentID"
- "_publisher"
- "_publisherLabel"
- "_publisherURL"
- "_quicklyGenerateCachedReachabilityResultConsideringPublisherURL:"
- "_resultOfLastInstallationCheck"
- "_setAvailableInStoreResult:"
- "_setCachedReachabilityResult:"
- "_updateCell:selected:"
- "_updateInstallButtonWithState:"
- "_updateSubviewsWithInstallState:"
- "a"
- "absoluteString"
- "allItems"
- "appInstallerWillStart:"
- "appIsAvailableInStoreDidChange:"
- "appIsDownloadableDidChange:"
- "applicationIsInstalled:"
- "bundle-id"
- "bundleID"
- "buttonAction"
- "characterSetWithCharactersInString:"
- "checkAvailabilityInStore:"
- "currentStoreFront"
- "date"
- "defaultWorkspace"
- "dictionaryWithObject:forKey:"
- "fetchDownloadability:"
- "green-tea"
- "i"
- "i16@0:8"
- "icon"
- "imageView"
- "initForAppWithDescription:"
- "initWithImage:"
- "initWithItem:"
- "initWithPurchases:"
- "initWithStyle:reuseIdentifier:specifier:"
- "installState"
- "isAvailableInStore"
- "isDownloadable"
- "persistentID"
- "publisher"
- "publisherURL"
- "rangeOfCharacterFromSet:"
- "requestWithURL:"
- "requiresReachabilityCheckToDetermineDownloadability"
- "sendSynchronousRequest:returningResponse:error:"
- "setAlpha:"
- "setBundleID:"
- "setIcon:"
- "setInstallState:"
- "setKeyProfile:"
- "setLocalizationStyle:"
- "setName:"
- "setPersistentID:"
- "setPublisher:"
- "setPublisherURL:"
- "setTintColor:"
- "setValue:forParameter:"
- "setValue:forRequestParameter:"
- "sharedApplication"
- "softlink:r:path:/System/Library/PrivateFrameworks/Message.framework/MailServices/IMAP.framework/IMAP"
- "softlink:r:path:/System/Library/PrivateFrameworks/StoreKitUI.framework/StoreKitUI"
- "specifierForAppWithDescription:target:action:"
- "start"
- "startWithItemLookupBlock:"
- "startWithLookupBlock:"
- "statusCode"
- "storeFrontIdentifier"
- "stringValue"
- "substringToIndex:"
- "suspend"
- "textLabel"
- "timeIntervalSinceDate:"
- "touchesBegan:withEvent:"
- "touchesCancelled:withEvent:"
- "touchesEnded:withEvent:"
- "touchesMoved:withEvent:"
- "v20@0:8i16"
- "v24@?0@\"SSLookupResponse\"8@\"NSError\"16"
- "valueForProperty:"
- "void *IMAPLibrary(void)"
- "void *StoreKitUILibrary(void)"

```
