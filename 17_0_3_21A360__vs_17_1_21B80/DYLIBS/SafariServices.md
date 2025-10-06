## SafariServices

> `/System/Library/Frameworks/SafariServices.framework/SafariServices`

```diff

-616.1.27.10.16
-  __TEXT.__text: 0x1850bc
+616.2.9.10.10
+  __TEXT.__text: 0x186fb8
   __TEXT.__auth_stubs: 0x1820
-  __TEXT.__objc_methlist: 0x15150
-  __TEXT.__const: 0x3ee8
-  __TEXT.__cstring: 0x101b3
-  __TEXT.__gcc_except_tab: 0xc894
-  __TEXT.__oslogstring: 0x8628
+  __TEXT.__objc_methlist: 0x15230
+  __TEXT.__const: 0x3ed8
+  __TEXT.__cstring: 0x10247
+  __TEXT.__gcc_except_tab: 0xc990
+  __TEXT.__oslogstring: 0x86d2
   __TEXT.__ustring: 0x33d4
   __TEXT.__dlopen_cstrs: 0x795
-  __TEXT.__unwind_info: 0x8a50
+  __TEXT.__unwind_info: 0x8b14
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x4e6a
-  __TEXT.__objc_methname: 0x58f65
-  __TEXT.__objc_methtype: 0x11fd3
-  __TEXT.__objc_stubs: 0x366c0
-  __DATA_CONST.__got: 0xc90
-  __DATA_CONST.__const: 0x6b18
-  __DATA_CONST.__objc_classlist: 0xae8
+  __TEXT.__objc_classname: 0x4e7a
+  __TEXT.__objc_methname: 0x5937f
+  __TEXT.__objc_methtype: 0x1201a
+  __TEXT.__objc_stubs: 0x36900
+  __DATA_CONST.__got: 0xc98
+  __DATA_CONST.__const: 0x6bf0
+  __DATA_CONST.__objc_classlist: 0xae0
   __DATA_CONST.__objc_catlist: 0x168
-  __DATA_CONST.__objc_protolist: 0x848
+  __DATA_CONST.__objc_protolist: 0x850
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x31198
-  __DATA_CONST.__objc_selrefs: 0x10308
-  __DATA_CONST.__objc_arraydata: 0x760
+  __DATA_CONST.__objc_const: 0x31270
+  __DATA_CONST.__objc_selrefs: 0x103d0
+  __DATA_CONST.__objc_arraydata: 0x768
   __AUTH_CONST.__cfstring: 0xe1e0
-  __AUTH_CONST.__const: 0x18d8
-  __AUTH_CONST.__objc_const: 0x8bc8
+  __AUTH_CONST.__const: 0x1998
+  __AUTH_CONST.__objc_const: 0x8b80
   __AUTH_CONST.__objc_intobj: 0xc90
-  __AUTH_CONST.__objc_arrayobj: 0xbe8
+  __AUTH_CONST.__objc_arrayobj: 0xc00
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0xc28
-  __AUTH.__objc_data: 0x6090
+  __AUTH.__objc_data: 0x6040
   __DATA.__objc_protorefs: 0xe8
-  __DATA.__objc_classrefs: 0x1958
-  __DATA.__objc_superrefs: 0x980
-  __DATA.__objc_ivar: 0x21d4
-  __DATA.__data: 0x6420
-  __DATA.__bss: 0x840
+  __DATA.__objc_classrefs: 0x1950
+  __DATA.__objc_superrefs: 0x978
+  __DATA.__objc_ivar: 0x21e8
+  __DATA.__data: 0x6488
+  __DATA.__bss: 0x850
   __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: F13475C4-7545-3B0F-A0A3-22A94C1BB7A0
-  Functions: 9265
-  Symbols:   35661
-  CStrings:  18670
+  UUID: 46C7D3E4-7993-347B-BEA7-F1829A9073A2
+  Functions: 9306
+  Symbols:   35783
+  CStrings:  18710
 
Symbols:
+ +[SFBrowserServiceViewController hostWindowSceneIdentifierForServiceWindowSceneIdentifier:]
+ +[SFBrowserServiceViewController setHostWindowSceneIdentifier:forServiceViewController:]
+ +[SFSafariLaunchPlaceholderView compatibilityPlaceholderWithAppName:destinationURL:forAuthentication:dismissalHandler:openHandler:]
+ -[SFAccountManagerPlatterWithDeclineButtonCell _configureDeclineButton]
+ -[SFAccountNoteTableViewCell layoutMarginsDidChange]
+ -[SFAccountPickerViewController buildMenuWithBuilder:]
+ -[SFAccountTableViewCell setSavedAccount:searchPattern:emphasizeUserName:shouldDifferentiateWithGroupName:]
+ -[SFAuthenticationViewController _presentViewController].cold.1
+ -[SFBrowserServiceViewController setHostWindowSceneIdentifier:]
+ -[SFFormAutocompleteState _addActionForAlertController:title:detail:handler:]
+ -[SFLinkPreviewHeaderContentView initWithStyle:]
+ -[SFLinkPreviewHeaderContentView secondaryLabelColor]
+ -[SFLinkPreviewHeaderContentView style]
+ -[SFRecentlyDeletedAccountsViewController _recoverSavedAccountsToMyPasswords:]
+ -[SFRecentlyDeletedAccountsViewController _recoverSelectedSavedAccountsToMyPasswords]
+ -[SFRecentlyDeletedAccountsViewController _recoverSelectedSharedAccountsMenu]
+ -[SFRecentlyDeletedAccountsViewController tableView:didEndEditingRowAtIndexPath:]
+ -[SFRecentlyDeletedAccountsViewController tableView:willBeginEditingRowAtIndexPath:]
+ -[SFSafariLaunchPlaceholderView _openTapped:]
+ -[SFSafariLaunchPlaceholderView _updateLargeButton]
+ -[SFSafariLaunchPlaceholderView initWithAppName:destinationURL:forAuthentication:dismissalHandler:openHandler:]
+ -[SFSafariLaunchPlaceholderView setShowContinueButton:]
+ -[SFSafariLaunchPlaceholderView showContinueButton]
+ -[SFSafariViewController _handleURLExternallyIfApplicableBypassingVisibilityCheck:]
+ -[SFSafariViewController _handleURLExternallyIfApplicableBypassingVisibilityCheck:].cold.1
+ -[SFSafariViewController _handleURLExternallyIfApplicableBypassingVisibilityCheck:].cold.2
+ -[UIFont(SafariServicesExtras) _sf_fontByAddingAttributes:]
+ -[UITableViewCell(SafariServicesExtras) sf_registerDynamicImageProvider:forTraitChanges:]
+ -[UITableViewCell(SafariServicesExtras) sf_registerDynamicImageProviderForSystemTraitsAffectingColorAppearance:]
+ -[_SFAccountManagerViewController _generatedPasswordSearchResultsCellForTableView:]
+ -[_SFFormAutoFillController authenticateIfNeededForAutoFillAuthenticationType:shouldForceAuthentication:withCompletion:]
+ -[_SFLinkPreviewHeader _initWithMinimumPreviewUI:isOnNativeHost:]
+ -[_SFLinkPreviewHeader opaqueSeparatorColor]
+ -[_SFPasswordAuditingViewController shouldSuppressAccountManagerLockedView]
+ -[_SFReloadOptionsController _requestStandardSiteWithURL:]
+ GCC_except_table203
+ _OBJC_IVAR_$_SFLinkPreviewHeaderContentView._style
+ _OBJC_IVAR_$_SFRecentlyDeletedAccountsViewController._userIsEditingCellInTableView
+ _OBJC_IVAR_$_SFSafariLaunchPlaceholderView._forAuthentication
+ _OBJC_IVAR_$_SFSafariLaunchPlaceholderView._largeButton
+ _OBJC_IVAR_$_SFSafariLaunchPlaceholderView._linkCaptionTextView
+ _OBJC_IVAR_$_SFSafariLaunchPlaceholderView._openHandler
+ _OBJC_IVAR_$_SFSafariLaunchPlaceholderView._showContinueButton
+ _OBJC_IVAR_$__SFLinkPreviewHeader._style
+ _SFViewControllerViewIsVisible
+ _UIMenuAutoFill
+ __OBJC_$_INSTANCE_METHODS_UIFont(SafariServicesExtras)
+ __OBJC_$_PROTOCOL_CLASS_METHODS_ASSafariViewServiceHostWindowSceneProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASSafariViewServiceHostWindowSceneProviding
+ __OBJC_$_PROTOCOL_REFS_ASSafariViewServiceHostWindowSceneProviding
+ __OBJC_LABEL_PROTOCOL_$_ASSafariViewServiceHostWindowSceneProviding
+ __OBJC_PROTOCOL_$_ASSafariViewServiceHostWindowSceneProviding
+ __ZL48hostWindowSceneIdentifierToServiceViewController
+ __ZL52hostWindowSceneIdentifierToServiceViewControllerLock
+ ___100-[_SFPageLoadErrorController handleLegacyTLSWithFailingURL:clickThroughURL:authenticationChallenge:]_block_invoke
+ ___101-[SFRecentlyDeletedAccountsViewController tableView:contextMenuConfigurationForRowAtIndexPath:point:]_block_invoke_4
+ ___101-[SFRecentlyDeletedAccountsViewController tableView:contextMenuConfigurationForRowAtIndexPath:point:]_block_invoke_5
+ ___103-[SFAccountManagerDrillInTableViewCellWithTrailingNumber configureCellWithGroup:numberOfSavedAccounts:]_block_invoke
+ ___114-[SFAccountManagerDrillInTableViewCellWithTrailingNumber configureGroupInvitationsDrillInWithNumberOfInvitations:]_block_invoke
+ ___115-[_SFWebAppServiceViewController webViewController:requestNotificationPermissionForSecurityOrigin:decisionHandler:]_block_invoke.142
+ ___121-[SFAccountManagerDrillInTableViewCellWithTrailingNumber configureForRecentlyDeletedWithNumberOfRecentlyDeletedAccounts:]_block_invoke
+ ___147-[SFAccountManagerDrillInTableViewCellWithTrailingNumber configureForSecurityRecommendationsWithNumberOfRecommendations:subtitleText:warningStyle:]_block_invoke
+ ___51-[SFSafariViewController _addLaunchPlaceholderView]_block_invoke_2
+ ___54-[SFAccountPickerViewController buildMenuWithBuilder:]_block_invoke
+ ___54-[SFAccountPickerViewController buildMenuWithBuilder:]_block_invoke_2
+ ___60-[SFFormAutocompleteState newAutoFillablePasskeysAvailable:]_block_invoke.350
+ ___61-[_SFAccountManagerViewController _autoFillCellForTableView:]_block_invoke
+ ___62-[_SFAccountManagerViewController _savedAccountStoreDidChange]_block_invoke.442
+ ___67-[_SFAccountManagerViewController _softDeleteAccountsAtIndexPaths:]_block_invoke.445
+ ___67-[_SFBookmarkInfoViewController _setFolderPickerExpanded:animated:]_block_invoke
+ ___68-[_SFPageLoadErrorController _loadCertificateWarningPageForContext:]_block_invoke
+ ___72-[_SFWebAppServiceViewController processWebPushForWebAppWithIdentifier:]_block_invoke.254
+ ___73-[_SFAccountPickerTableViewController tableView:didSelectRowAtIndexPath:]_block_invoke.157
+ ___74-[SFBrowserServiceViewController closeDatabasesOnBackgroundingOrDismissal]_block_invoke.218
+ ___75-[_SFWebAppServiceViewController clearWebViewAndWebsiteDataWithCompletion:]_block_invoke.123
+ ___77-[SFRecentlyDeletedAccountsViewController _recoverSelectedSharedAccountsMenu]_block_invoke
+ ___77-[SFRecentlyDeletedAccountsViewController _recoverSelectedSharedAccountsMenu]_block_invoke_2
+ ___78-[SFRecentlyDeletedAccountsViewController _recoverSavedAccountsToMyPasswords:]_block_invoke
+ ___83-[SFSafariViewController _handleURLExternallyIfApplicableBypassingVisibilityCheck:]_block_invoke
+ ___83-[_SFAccountManagerViewController _generatedPasswordSearchResultsCellForTableView:]_block_invoke
+ ___85-[_SFPageLoadErrorController showErrorPageWithTitle:bodyText:learnMoreLink:forError:]_block_invoke
+ ___87-[SFAccountDetailViewController QRCodeScannerViewController:didScanQRCodeWithURLValue:]_block_invoke.816
+ ___89-[UITableViewCell(SafariServicesExtras) sf_registerDynamicImageProvider:forTraitChanges:]_block_invoke
+ ___block_descriptor_32_e23_B16?0"UIMenuElement"8l
+ ___block_descriptor_32_e26_"NSArray"16?0"NSArray"8l
+ ___block_descriptor_32_e36_"UIImage"16?0"UITraitCollection"8l
+ ___block_descriptor_40_e8_32bs_e47_v24?0"UITableViewCell"8"UITraitCollection"16ls32l8
+ ___block_descriptor_40_e8_32s_e36_"UIImage"16?0"UITraitCollection"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e36_"UIImage"16?0"UITraitCollection"8ls32l8s40l8
+ ___block_descriptor_80_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e8_v12?0B8ls64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_98_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.120
+ ___block_literal_global.161
+ ___block_literal_global.204
+ ___block_literal_global.250
+ ___block_literal_global.263
+ ___block_literal_global.342
+ ___block_literal_global.345
+ ___block_literal_global.367
+ ___block_literal_global.433
+ ___block_literal_global.437
+ ___block_literal_global.462
+ ___block_literal_global.474
+ ___block_literal_global.48
+ ___block_literal_global.486
+ ___block_literal_global.489
+ ___block_literal_global.491
+ ___block_literal_global.494
+ ___block_literal_global.498
+ ___block_literal_global.99
+ __unnamed_array_storage.76
+ _dynamicImageTraitCollectionRegistrationKey
+ _eligibleForSlideInPresentation
+ _objc_msgSend$_addActionForAlertController:title:detail:handler:
+ _objc_msgSend$_cancelBarButtonItemTapped:
+ _objc_msgSend$_cancelEditing
+ _objc_msgSend$_configureDeclineButton
+ _objc_msgSend$_generatedPasswordSearchResultsCellForTableView:
+ _objc_msgSend$_initWithMinimumPreviewUI:isOnNativeHost:
+ _objc_msgSend$_recoverSavedAccountsToMyPasswords:
+ _objc_msgSend$_recoverSelectedSavedAccountsToMyPasswords
+ _objc_msgSend$_recoverSelectedSharedAccountsMenu
+ _objc_msgSend$_requestStandardSiteWithURL:
+ _objc_msgSend$_sceneIdentifier
+ _objc_msgSend$animateChanges:
+ _objc_msgSend$authenticateIfNeededForAutoFillAuthenticationType:shouldForceAuthentication:withCompletion:
+ _objc_msgSend$compatibilityPlaceholderWithAppName:destinationURL:forAuthentication:dismissalHandler:openHandler:
+ _objc_msgSend$fetchPasswordCredentialIdentitiesMatchingDomains:completion:
+ _objc_msgSend$newGroupButtonTitle
+ _objc_msgSend$registerForTraitChanges:withHandler:
+ _objc_msgSend$replaceChildrenOfMenuForIdentifier:fromChildrenBlock:
+ _objc_msgSend$setHostWindowSceneIdentifier:
+ _objc_msgSend$setHostWindowSceneIdentifier:forServiceViewController:
+ _objc_msgSend$setMaximumNumberOfLines:
+ _objc_msgSend$setSavedAccount:searchPattern:emphasizeUserName:shouldDifferentiateWithGroupName:
+ _objc_msgSend$setShowContinueButton:
+ _objc_msgSend$sf_registerDynamicImageProvider:forTraitChanges:
+ _objc_msgSend$sf_registerDynamicImageProviderForSystemTraitsAffectingColorAppearance:
+ _objc_msgSend$sheetPresentationController
+ _objc_msgSend$shouldRequireUserVerification
+ _objc_msgSend$shouldShowInternalUI
+ _objc_msgSend$systemTraitsAffectingColorAppearance
+ _objc_msgSend$unableToInviteContactBecauseOfUnsupportedDevicesAlertMessageWithContactName:
+ _objc_msgSend$unableToInviteMultipleContactsBecauseOfUnsupportedDevicesAlertMessage
+ _objc_msgSend$unregisterForTraitChanges:
+ _objc_msgSend$userMediaPermissionDialogWithHost:permissions:completionHandler:
- +[SFSafariLaunchPlaceholderView compatibilityPlaceholderWithAppName:destinationURL:forAuthentication:dismissalHandler:]
- -[SFAccountTableViewCell setSavedAccount:searchPattern:emphasizeUserName:savedAccountHasSameUsernameAndHighLevelDomainPairAsOtherSharedSavedAccount:]
- -[SFAutoFillPasswordsTableViewCell .cxx_destruct]
- -[SFAutoFillPasswordsTableViewCell _configureTitleLabelFont:]
- -[SFAutoFillPasswordsTableViewCell initWithStyle:reuseIdentifier:]
- -[SFAutoFillPasswordsTableViewCell traitCollectionDidChange:]
- -[SFLinkPreviewHeaderContentView initWithFrame:]
- -[SFRecentlyDeletedAccountsViewController _recoverSelectedAccountsToMyPasswords]
- -[SFRecentlyDeletedAccountsViewController _recoverSharedAccountsMenu]
- -[SFSafariLaunchPlaceholderView _updateLargeDismissButtonIfNeeded]
- -[SFSafariLaunchPlaceholderView initWithAppName:destinationURL:forAuthentication:dismissalHandler:]
- -[SFSafariViewController _handleURLExternally]
- -[_SFFormAutoFillController authenticateForAutoFillAuthenticationType:withCompletion:]
- GCC_except_table202
- _OBJC_CLASS_$_SFAutoFillPasswordsTableViewCell
- _OBJC_IVAR_$_SFAutoFillPasswordsTableViewCell._titleLabel
- _OBJC_IVAR_$_SFSafariLaunchPlaceholderView._largeDismissButton
- _OBJC_IVAR_$_SFSafariLaunchPlaceholderView._linkCaptionLabel
- _OBJC_METACLASS_$_SFAutoFillPasswordsTableViewCell
- __OBJC_$_INSTANCE_METHODS_SFAutoFillPasswordsTableViewCell
- __OBJC_$_INSTANCE_VARIABLES_SFAutoFillPasswordsTableViewCell
- __OBJC_CLASS_RO_$_SFAutoFillPasswordsTableViewCell
- __OBJC_METACLASS_RO_$_SFAutoFillPasswordsTableViewCell
- __SFAccountManagerMinimumFontScaleFactor
- ___115-[_SFWebAppServiceViewController webViewController:requestNotificationPermissionForSecurityOrigin:decisionHandler:]_block_invoke.141
- ___46-[SFSafariViewController _handleURLExternally]_block_invoke
- ___60-[SFFormAutocompleteState newAutoFillablePasskeysAvailable:]_block_invoke.347
- ___62-[_SFAccountManagerViewController _savedAccountStoreDidChange]_block_invoke.445
- ___67-[_SFAccountManagerViewController _softDeleteAccountsAtIndexPaths:]_block_invoke.448
- ___69-[SFRecentlyDeletedAccountsViewController _recoverSharedAccountsMenu]_block_invoke
- ___69-[SFRecentlyDeletedAccountsViewController _recoverSharedAccountsMenu]_block_invoke_2
- ___72-[_SFWebAppServiceViewController processWebPushForWebAppWithIdentifier:]_block_invoke.253
- ___73-[_SFAccountPickerTableViewController tableView:didSelectRowAtIndexPath:]_block_invoke.156
- ___74-[SFBrowserServiceViewController closeDatabasesOnBackgroundingOrDismissal]_block_invoke.216
- ___75-[_SFWebAppServiceViewController clearWebViewAndWebsiteDataWithCompletion:]_block_invoke.122
- ___80-[SFRecentlyDeletedAccountsViewController _recoverSelectedAccountsToMyPasswords]_block_invoke
- ___87-[SFAccountDetailViewController QRCodeScannerViewController:didScanQRCodeWithURLValue:]_block_invoke.815
- ___block_descriptor_80_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e8_v12?0B8ls72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_98_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s88l8s80l8
- ___block_literal_global.119
- ___block_literal_global.135
- ___block_literal_global.203
- ___block_literal_global.249
- ___block_literal_global.262
- ___block_literal_global.336
- ___block_literal_global.339
- ___block_literal_global.364
- ___block_literal_global.436
- ___block_literal_global.440
- ___block_literal_global.465
- ___block_literal_global.470
- ___block_literal_global.473
- ___block_literal_global.475
- ___block_literal_global.478
- ___block_literal_global.81
- ___block_literal_global.98
- _objc_msgSend$_configureTitleLabelFont:
- _objc_msgSend$_recoverSelectedAccountsToMyPasswords
- _objc_msgSend$_recoverSharedAccountsMenu
- _objc_msgSend$authenticateForAutoFillAuthenticationType:withCompletion:
- _objc_msgSend$compatibilityPlaceholderWithAppName:destinationURL:forAuthentication:dismissalHandler:
- _objc_msgSend$fetchCredentialIdentitiesMatchingDomains:completion:
- _objc_msgSend$insertSubview:below:
- _objc_msgSend$safari_localizedStringFromComponents:usingConjunctionForFinalJoiner:
- _objc_msgSend$setNumberOfWarnings:
- _objc_msgSend$setRotationDecider:
- _objc_msgSend$setSavedAccount:searchPattern:emphasizeUserName:savedAccountHasSameUsernameAndHighLevelDomainPairAsOtherSharedSavedAccount:
- _objc_msgSend$setSubtitleText:
- _objc_msgSend$setWarningStyle:
- _objc_msgSend$tableCellGrayTextColor
- _objc_msgSend$userMediaPermissionDialogWithHost:devices:completionHandler:
CStrings:
+ "\x02\x1f\x01\x14\x11%\x11#\x11\x12"
+ "\x02r"
+ "\a\x11\x11\x18\x11"
+ "\x19"
+ "%@ opened {some-url}."
+ "@\"NSArray\"16@?0@\"NSArray\"8"
+ "@\"NSString\"24@0:8@\"NSString\"16"
+ "@\"UIImage\"16@?0@\"UITraitCollection\"8"
+ "@52@0:8@16@24B32@?36@?44"
+ "ASSafariViewServiceHostWindowSceneProviding"
+ "Attempted to present SFAuthenticationViewController from a view controller that is being dismissed: %@"
+ "B16@?0@\"UIMenuElement\"8"
+ "Ignoring call to handle URL externally because SFSafariViewController is not visible."
+ "Ignoring call to handle URL externally because there was no window to present from."
+ "Open Web Browser"
+ "TB,N,V_showContinueButton"
+ "Tq,R,N,V_style"
+ "[Apple Internal] Passwords wasn't able to load any passwords. If you believe this device does have saved passwords on it, please tap here to file a bug with Tap-to-Radar. (If you need to hide this message, see rdar://114593091.)"
+ "_SFAuthenticationAlwaysUseFallbackPresentation"
+ "_addActionForAlertController:title:detail:handler:"
+ "_configureDeclineButton"
+ "_forAuthentication"
+ "_generatedPasswordSearchResultsCellForTableView:"
+ "_initWithMinimumPreviewUI:isOnNativeHost:"
+ "_largeButton"
+ "_linkCaptionTextView"
+ "_openHandler"
+ "_openTapped:"
+ "_recoverSavedAccountsToMyPasswords:"
+ "_recoverSelectedSavedAccountsToMyPasswords"
+ "_recoverSelectedSharedAccountsMenu"
+ "_requestStandardSiteWithURL:"
+ "_sceneIdentifier"
+ "_sf_fontByAddingAttributes:"
+ "_showContinueButton"
+ "animateChanges:"
+ "authenticateIfNeededForAutoFillAuthenticationType:shouldForceAuthentication:withCompletion:"
+ "buildMenuWithBuilder:"
+ "captureTextFromCamera:"
+ "com.reederapp.5.iOS"
+ "compatibilityPlaceholderWithAppName:destinationURL:forAuthentication:dismissalHandler:openHandler:"
+ "fetchPasswordCredentialIdentitiesMatchingDomains:completion:"
+ "hostWindowSceneIdentifierForServiceWindowSceneIdentifier:"
+ "newGroupButtonTitle"
+ "registerForTraitChanges:withHandler:"
+ "replaceChildrenOfMenuForIdentifier:fromChildrenBlock:"
+ "setHostWindowSceneIdentifier:"
+ "setHostWindowSceneIdentifier:forServiceViewController:"
+ "setMaximumNumberOfLines:"
+ "setSavedAccount:searchPattern:emphasizeUserName:shouldDifferentiateWithGroupName:"
+ "setShowContinueButton:"
+ "sf_registerDynamicImageProvider:forTraitChanges:"
+ "sf_registerDynamicImageProviderForSystemTraitsAffectingColorAppearance:"
+ "sheetPresentationController"
+ "shouldRequireUserVerification"
+ "shouldShowInternalUI"
+ "showContinueButton"
+ "systemTraitsAffectingColorAppearance"
+ "unableToInviteContactBecauseOfUnsupportedDevicesAlertMessageWithContactName:"
+ "unableToInviteMultipleContactsBecauseOfUnsupportedDevicesAlertMessage"
+ "unregisterForTraitChanges:"
+ "userMediaPermissionDialogWithHost:permissions:completionHandler:"
+ "v24@?0@\"UITableViewCell\"8@\"UITraitCollection\"16"
+ "v32@0:8@?16@24"
+ "{some-url}"
+ "\x91\xa1"
+ "\xf0\x91!\xf01"
- "\x02\x1f\x01\x16%\x11#\x11\x12"
- "\x02b"
- "\a\x13\x18\x11"
- "%@ does not have a device that can join the group."
- "%@ opened %@."
- "Camera"
- "Ignoring call to handle URL externally because SFSafariViewController is not yet installed in a window"
- "Microphone"
- "Not all group members have devices that can join the passwords group."
- "SFAutoFillPasswordsTableViewCell"
- "[Apple Internal] Passwords wasn't able to load any passwords. If you believe this device does have saved passwords on it, please tap here to file a bug with Tap-to-Radar."
- "_configureTitleLabelFont:"
- "_largeDismissButton"
- "_linkCaptionLabel"
- "_recoverSelectedAccountsToMyPasswords"
- "_recoverSharedAccountsMenu"
- "authenticateForAutoFillAuthenticationType:withCompletion:"
- "compatibilityPlaceholderWithAppName:destinationURL:forAuthentication:dismissalHandler:"
- "fetchCredentialIdentitiesMatchingDomains:completion:"
- "insertSubview:below:"
- "pause.fill"
- "play.fill"
- "safari_localizedStringFromComponents:usingConjunctionForFinalJoiner:"
- "setRotationDecider:"
- "setSavedAccount:searchPattern:emphasizeUserName:savedAccountHasSameUsernameAndHighLevelDomainPairAsOtherSharedSavedAccount:"
- "tableCellGrayTextColor"
- "userMediaPermissionDialogWithHost:devices:completionHandler:"
- "\xf0Q"
- "\xf0\xc1\xf01"

```
