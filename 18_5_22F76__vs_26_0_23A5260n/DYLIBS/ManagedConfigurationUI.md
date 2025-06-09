## ManagedConfigurationUI

> `/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI`

```diff

-20.5.1.2.0
-  __TEXT.__text: 0x252c8
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x3950
+43.0.0.0.0
+  __TEXT.__text: 0x24ad8
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_methlist: 0x3938
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x610
-  __TEXT.__cstring: 0x2eb4
+  __TEXT.__gcc_except_tab: 0x61c
+  __TEXT.__cstring: 0x2fa4
   __TEXT.__ustring: 0x46
-  __TEXT.__unwind_info: 0xcd0
-  __TEXT.__objc_classname: 0x9f7
-  __TEXT.__objc_methname: 0xaab8
-  __TEXT.__objc_methtype: 0x1f03
+  __TEXT.__unwind_info: 0xca0
+  __TEXT.__objc_classname: 0x9c6
+  __TEXT.__objc_methname: 0xab87
+  __TEXT.__objc_methtype: 0x1f40
   __TEXT.__objc_stubs: 0x7800
-  __DATA_CONST.__got: 0x738
-  __DATA_CONST.__const: 0xa60
-  __DATA_CONST.__objc_classlist: 0x1c8
-  __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0xe8
+  __DATA_CONST.__got: 0x740
+  __DATA_CONST.__const: 0xa38
+  __DATA_CONST.__objc_classlist: 0x1b8
+  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2830
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_selrefs: 0x2848
+  __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x420
+  __AUTH_CONST.__auth_got: 0x410
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x24c0
-  __AUTH_CONST.__objc_const: 0x56e8
+  __AUTH_CONST.__cfstring: 0x2620
+  __AUTH_CONST.__objc_const: 0x5630
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH.__objc_data: 0xfa0
-  __DATA.__objc_ivar: 0x2cc
-  __DATA.__data: 0xae0
-  __DATA.__bss: 0x90
+  __AUTH.__objc_data: 0xf00
+  __DATA.__objc_ivar: 0x2d8
+  __DATA.__data: 0xb40
+  __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__bss: 0x38
+  __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI
   - /System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences
+  - /System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary
   - /System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 03D731D2-662A-3FF6-9592-DBBB337D7BCC
-  Functions: 1113
-  Symbols:   4426
-  CStrings:  2582
+  UUID: 0992C3CB-06EF-34FE-97A2-5D891AA58961
+  Functions: 1111
+  Symbols:   4412
+  CStrings:  2615
 
Symbols:
+ +[MCUIBundleController _sharedInstance]
+ +[MCUIBundleController _sharedInstance].cold.1
+ +[MCUIBundleController mcuiTitle]
+ -[MCCertificatePickerController viewDidLoad]
+ -[MCInstallProfileViewController rightNavBarButton]
+ -[MCProfileTitlePageViewController _didFinishPINEntrySuccess:pin:]
+ -[MCProfileTitlePageViewController dmc_viewControllerHasBeenDismissed]
+ -[MCRemoveProfileViewController _showLeaveProvisionalRemoteManagementAlert]
+ -[MCUIAppSignerViewController setTrustCell:]
+ -[MCUIAppSignerViewController trustCell]
+ -[MCUIListController _mainQueue_setBeginMigrationButtonEnabled:]
+ -[MCUIListController mdmMigrationAvailableToken]
+ -[MCUIListController migrationIsAvailable]
+ -[MCUIListController setMdmMigrationAvailableToken:]
+ -[MCUIMCSpecifierProvider _presentErrorTitle:message:]
+ -[MCUIPINController setSubviewLayoutFrame:]
+ -[MCUIPINController subviewLayoutFrame]
+ -[MCUIPINController viewWillLayoutSubviews]
+ -[MCUISpecifierCell prepareForReuse]
+ -[MCUISpecifierProvider registerCustomCellClassesInTableView:]
+ -[MCURLListenerListController _startMigration]
+ _MCUIForHome
+ _MDMPendingMigrationCloudConfigurationDetailsChangedNotification
+ _OBJC_CLASS_$_DMCMigrationHelper
+ _OBJC_CLASS_$_DMCNavigationController
+ _OBJC_CLASS_$_DMCSpecifierProvider
+ _OBJC_IVAR_$_MCInstallProfileViewController._rightNavBarButton
+ _OBJC_IVAR_$_MCUIAppSignerViewController._trustCell
+ _OBJC_IVAR_$_MCUIListController._mdmMigrationAvailableToken
+ _OBJC_IVAR_$_MCUIPINController._subviewLayoutFrame
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DMCCustomClassSpecifierProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DMCViewController
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCCustomClassSpecifierProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCViewController
+ __OBJC_$_PROTOCOL_REFS_DMCViewController
+ __OBJC_CLASS_PROTOCOLS_$_MCUISpecifierProvider
+ __OBJC_LABEL_PROTOCOL_$_DMCCustomClassSpecifierProvider
+ __OBJC_LABEL_PROTOCOL_$_DMCViewController
+ __OBJC_PROTOCOL_$_DMCCustomClassSpecifierProvider
+ __OBJC_PROTOCOL_$_DMCViewController
+ ___39+[MCUIBundleController _sharedInstance]_block_invoke
+ ___45-[MCUIListController initWithNibName:bundle:]_block_invoke_3
+ ___46-[MCURLListenerListController _startMigration]_block_invoke
+ ___46-[MCURLListenerListController _startMigration]_block_invoke_2
+ ___64-[MCUIListController _mainQueue_setBeginMigrationButtonEnabled:]_block_invoke
+ ___66-[MCProfileTitlePageViewController _didFinishPINEntrySuccess:pin:]_block_invoke
+ ___75-[MCRemoveProfileViewController _showLeaveProvisionalRemoteManagementAlert]_block_invoke
+ ___block_literal_global.60
+ __sharedInstance.onceToken
+ __sharedInstance.sharedInstance
+ _kMDMSettingsURLProfilesUI
+ _objc_msgSend$DMCProfileSecondaryLabelColor
+ _objc_msgSend$_didFinishPINEntrySuccess:pin:
+ _objc_msgSend$_mainQueue_setBeginMigrationButtonEnabled:
+ _objc_msgSend$_presentErrorTitle:message:
+ _objc_msgSend$_sharedInstance
+ _objc_msgSend$_showLeaveProvisionalRemoteManagementAlert
+ _objc_msgSend$_startMigration
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$cellReuseIdentifier
+ _objc_msgSend$dmc_popToViewController:animated:
+ _objc_msgSend$dmc_popToViewController:pushViewController:
+ _objc_msgSend$dmc_popViewControllerAnimated:
+ _objc_msgSend$dmc_presentAlert:completion:
+ _objc_msgSend$dmc_pushViewController:animated:
+ _objc_msgSend$launchMigrationApplicationWithError:
+ _objc_msgSend$mcuiTitle
+ _objc_msgSend$popoverPresentationController
+ _objc_msgSend$registerCustomCellClassesInTableView:
+ _objc_msgSend$removeButton
+ _objc_msgSend$rightNavBarButton
+ _objc_msgSend$setBeginMigrationButtonEnabled:
+ _objc_msgSend$setSourceItem:
+ _objc_msgSend$setSubviewLayoutFrame:
+ _objc_msgSend$setTrustCell:
+ _objc_msgSend$specifiersForDebuggingEnrollment
+ _objc_msgSend$specifiersForMDMMigration
+ _objc_msgSend$table
+ _objc_msgSend$trustCell
+ _objc_msgSend$updateConfiguration:forSpecifier:subtitleColor:
- +[MCUIBundleController sharedInstance]
- +[MCUIBundleController sharedInstance].cold.1
- -[MCProfileTitlePageViewController viewControllerHasBeenDismissed]
- -[MCRemoveProfileViewController _showLeaveRemoteManagementAlert]
- -[MCRemoveProfileViewController _showRemovalWarningActionSheet]
- -[MCUIBundleController _sharedInitWithDataManager:]
- -[MCUIBundleController initWithParentListController:dataManager:]
- -[MCUIDismissalAwareNavigationController viewDidDisappear:]
- -[MCUIMCSpecifierProvider _presentModalNavController:]
- -[MCUIMCSpecifierProvider _presentViewController:]
- -[MCUIMCSpecifierProvider _showProfileDetailPageForUserEnrollmentProfile:]
- -[MCUINavigationViewController .cxx_destruct]
- -[MCUINavigationViewController didShowViewController:animated:]
- -[MCUINavigationViewController setShowViewControllerCompletionBlock:]
- -[MCUINavigationViewController shouldAutorotate]
- -[MCUINavigationViewController showViewControllerCompletionBlock]
- -[MCUINavigationViewController supportedInterfaceOrientations]
- -[MCUINavigationViewController viewDidLoad]
- -[MCURLListenerListController _presentNextController:withCompletion:]
- -[UIAlertController(MCUI) MCUIShowFromController:]
- -[UINavigationController(MCUI) popToViewController:pushViewController:animated:]
- -[UIViewController(MCUI) MCUIIsVisibleViewController]
- -[UIViewController(MCUI) MCUIPresentViewController:]
- -[UIViewController(MCUI) MCUITopViewController]
- GCC_except_table40
- _OBJC_CLASS_$_MCUIDismissalAwareNavigationController
- _OBJC_CLASS_$_MCUINavigationViewController
- _OBJC_IVAR_$_MCUINavigationViewController._showViewControllerCompletionBlock
- _OBJC_METACLASS_$_MCUIDismissalAwareNavigationController
- _OBJC_METACLASS_$_MCUINavigationViewController
- _OBJC_METACLASS_$_UINavigationController
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UINavigationController_$_MCUI
- __OBJC_$_CATEGORY_UINavigationController_$_MCUI
- __OBJC_$_INSTANCE_METHODS_MCUIDismissalAwareNavigationController
- __OBJC_$_INSTANCE_METHODS_MCUINavigationViewController
- __OBJC_$_INSTANCE_VARIABLES_MCUINavigationViewController
- __OBJC_$_PROP_LIST_MCUINavigationViewController
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MCUIDismissalAwareViewController
- __OBJC_$_PROTOCOL_METHOD_TYPES_MCUIDismissalAwareViewController
- __OBJC_$_PROTOCOL_REFS_MCUIDismissalAwareViewController
- __OBJC_CLASS_RO_$_MCUIDismissalAwareNavigationController
- __OBJC_CLASS_RO_$_MCUINavigationViewController
- __OBJC_LABEL_PROTOCOL_$_MCUIDismissalAwareViewController
- __OBJC_METACLASS_RO_$_MCUIDismissalAwareNavigationController
- __OBJC_METACLASS_RO_$_MCUINavigationViewController
- __OBJC_PROTOCOL_$_MCUIDismissalAwareViewController
- __OBJC_PROTOCOL_REFERENCE_$_MCUIDismissalAwareViewController
- ___38+[MCUIBundleController sharedInstance]_block_invoke
- ___50-[UIAlertController(MCUI) MCUIShowFromController:]_block_invoke
- ___56-[MCProfileTitlePageViewController didAcceptEnteredPIN:]_block_invoke
- ___56-[MCProfileTitlePageViewController didCancelEnteringPIN]_block_invoke
- ___63-[MCRemoveProfileViewController _showRemovalWarningActionSheet]_block_invoke
- ___64-[MCRemoveProfileViewController _showLeaveRemoteManagementAlert]_block_invoke
- ___69-[MCURLListenerListController _presentNextController:withCompletion:]_block_invoke
- ___block_descriptor_48_e8_32s40w_e8_v12?0B8lw40l8s32l8
- ___block_literal_global.26
- ___block_literal_global.47
- _objc_msgSend$MCUIShowFromController:
- _objc_msgSend$MCUITopViewController
- _objc_msgSend$_isTransitioning
- _objc_msgSend$_presentModalNavController:
- _objc_msgSend$_presentNextController:withCompletion:
- _objc_msgSend$_presentViewController:
- _objc_msgSend$_sharedInitWithDataManager:
- _objc_msgSend$_showLeaveRemoteManagementAlert
- _objc_msgSend$_showProfileDetailPageForUserEnrollmentProfile:
- _objc_msgSend$_showRemovalWarningActionSheet
- _objc_msgSend$conformsToProtocol:
- _objc_msgSend$detailTextLabel
- _objc_msgSend$initWithProfile:profileData:
- _objc_msgSend$initWithViewModel:
- _objc_msgSend$parentViewController
- _objc_msgSend$popToViewController:animated:
- _objc_msgSend$popToViewController:pushViewController:animated:
- _objc_msgSend$popViewControllerAnimated:
- _objc_msgSend$pushViewController:animated:
- _objc_msgSend$rootViewController
- _objc_msgSend$setModalPresentationStyle:
- _objc_msgSend$setShowViewControllerCompletionBlock:
- _objc_msgSend$setViewControllers:animated:
- _objc_msgSend$showViewControllerCompletionBlock
- _objc_msgSend$systemRedColor
- _objc_msgSend$trustedCodeSigningIdentities
- _objc_msgSend$viewControllerHasBeenDismissed
- _objc_msgSend$viewControllers
- _objc_msgSend$window
- _objc_retainAutoreleasedReturnValue
- _objc_unsafeClaimAutoreleasedReturnValue
- _sharedInstance.onceToken
- _sharedInstance.sharedInstance
CStrings:
+ "<"
+ "@\"MCUIApplicationTrustCell\""
+ "@\"UIBarButtonItem\""
+ "DMCCustomClassSpecifierProvider"
+ "DMCProfileSecondaryLabelColor"
+ "DMCViewController"
+ "Failed to register for MDM Migration availability notification"
+ "HOMEPOD"
+ "MCUIAppSigner: Provisioning profile UUID '%@' is not trusted"
+ "MCUIMCSpecifierProvider can no longer present a user enrollment profile"
+ "MCUIMCSpecifierProvider failed to deserialize profile"
+ "MDMMigration"
+ "MIGRATION_REBOOT_WARNING_TEXT"
+ "MIGRATION_REBOOT_WARNING_TITLE"
+ "MOBILE_DEVICE_MANAGEMENT_REMOVE_WARNING"
+ "MOBILE_DEVICE_MANAGEMENT_REMOVE_WARNING_YORKTOWN"
+ "PROFILE_ERROR_DESERIALIZE_FAIL"
+ "PROFILE_ERROR_PDUE_NOT_SUPPORTED"
+ "PROFILE_INSTALL_WARNING"
+ "PROFILE_UNABLE_TO_INSTALL"
+ "T@\"MCUIApplicationTrustCell\",&,N,V_trustCell"
+ "T@\"UIBarButtonItem\",R,N,V_rightNavBarButton"
+ "Ti,N,V_mdmMigrationAvailableToken"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_subviewLayoutFrame"
+ "WATCH"
+ "_didFinishPINEntrySuccess:pin:"
+ "_mainQueue_setBeginMigrationButtonEnabled:"
+ "_mdmMigrationAvailableToken"
+ "_presentErrorTitle:message:"
+ "_rightNavBarButton"
+ "_sharedInstance"
+ "_showLeaveProvisionalRemoteManagementAlert"
+ "_startMigration"
+ "_subviewLayoutFrame"
+ "_trustCell"
+ "cStringUsingEncoding:"
+ "cellReuseIdentifier"
+ "com.apple.Home"
+ "dmc_popToViewController:animated:"
+ "dmc_popToViewController:pushViewController:"
+ "dmc_popViewControllerAnimated:"
+ "dmc_presentAlert:completion:"
+ "dmc_pushViewController:animated:"
+ "dmc_viewControllerHasBeenDismissed"
+ "launchMigrationApplicationWithError:"
+ "mcuiTitle"
+ "mdmMigrationAvailableToken"
+ "migrationIsAvailable"
+ "popoverPresentationController"
+ "prepareForReuse"
+ "registerCustomCellClassesInTableView:"
+ "removeButton"
+ "rightNavBarButton"
+ "setBeginMigrationButtonEnabled:"
+ "setMdmMigrationAvailableToken:"
+ "setSourceItem:"
+ "setSubviewLayoutFrame:"
+ "setTrustCell:"
+ "specifiersForDebuggingEnrollment"
+ "specifiersForMDMMigration"
+ "subviewLayoutFrame"
+ "table"
+ "trustCell"
+ "updateConfiguration:forSpecifier:subtitleColor:"
+ "v28@0:8B16@20"
+ "viewWillLayoutSubviews"
- ";"
- "MCUI MC Specifier Provider failed to deserialize profile"
- "MCUIAppSigner: Could not find profile UUID for provisioning profile %@"
- "MCUIDismissalAwareNavigationController"
- "MCUIDismissalAwareViewController"
- "MCUIIsVisibleViewController"
- "MCUINavigationViewController"
- "MCUIPresentViewController:"
- "MCUIShowFromController:"
- "MCUITopViewController"
- "MOBILE_DEVICE_MANAGEMENT_REMOVE_WARNING_YORKTOWN_ADDITIONAL"
- "MOBILE_DEVICE_MANAGEMENT_REMOVE_WARNING_YORKTOWN_FULL"
- "T@?,C,N,V_showViewControllerCompletionBlock"
- "_isTransitioning"
- "_presentModalNavController:"
- "_presentNextController:withCompletion:"
- "_presentViewController:"
- "_sharedInitWithDataManager:"
- "_showLeaveRemoteManagementAlert"
- "_showProfileDetailPageForUserEnrollmentProfile:"
- "_showRemovalWarningActionSheet"
- "_showViewControllerCompletionBlock"
- "detailTextLabel"
- "didShowViewController:animated:"
- "initWithParentListController:"
- "initWithParentListController:dataManager:"
- "parentViewController"
- "popToViewController:animated:"
- "popToViewController:pushViewController:animated:"
- "popViewControllerAnimated:"
- "pushViewController:animated:"
- "rootViewController"
- "setModalPresentationStyle:"
- "setShowViewControllerCompletionBlock:"
- "setViewControllers:animated:"
- "settings-navigation://com.apple.Settings.General/ManagedConfigurationList"
- "shouldAutorotate"
- "showViewControllerCompletionBlock"
- "supportedInterfaceOrientations"
- "systemRedColor"
- "trustedCodeSigningIdentities"
- "viewControllerHasBeenDismissed"
- "viewControllers"
- "window"

```
