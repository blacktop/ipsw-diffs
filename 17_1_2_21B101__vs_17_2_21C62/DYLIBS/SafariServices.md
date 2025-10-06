## SafariServices

> `/System/Library/Frameworks/SafariServices.framework/SafariServices`

```diff

-616.2.9.10.13
-  __TEXT.__text: 0x186fb8
-  __TEXT.__auth_stubs: 0x1820
-  __TEXT.__objc_methlist: 0x15230
+617.1.17.10.9
+  __TEXT.__text: 0x178514
+  __TEXT.__auth_stubs: 0x17e0
+  __TEXT.__objc_methlist: 0x149d8
   __TEXT.__const: 0x3ed8
-  __TEXT.__cstring: 0x10247
-  __TEXT.__gcc_except_tab: 0xc990
-  __TEXT.__oslogstring: 0x86d2
-  __TEXT.__ustring: 0x33d4
+  __TEXT.__cstring: 0xe368
+  __TEXT.__gcc_except_tab: 0xaf68
+  __TEXT.__oslogstring: 0x7865
+  __TEXT.__ustring: 0x33ce
   __TEXT.__dlopen_cstrs: 0x795
-  __TEXT.__unwind_info: 0x8b14
+  __TEXT.__unwind_info: 0x81d8
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x4e7a
-  __TEXT.__objc_methname: 0x5937f
-  __TEXT.__objc_methtype: 0x1201a
-  __TEXT.__objc_stubs: 0x36900
-  __DATA_CONST.__got: 0xc98
-  __DATA_CONST.__const: 0x6bf0
-  __DATA_CONST.__objc_classlist: 0xae0
-  __DATA_CONST.__objc_catlist: 0x168
-  __DATA_CONST.__objc_protolist: 0x850
+  __TEXT.__objc_classname: 0x4dcb
+  __TEXT.__objc_methname: 0x57e45
+  __TEXT.__objc_methtype: 0x11e6b
+  __TEXT.__objc_stubs: 0x35920
+  __DATA_CONST.__got: 0xc58
+  __DATA_CONST.__const: 0x6820
+  __DATA_CONST.__objc_classlist: 0xac0
+  __DATA_CONST.__objc_catlist: 0x160
+  __DATA_CONST.__objc_protolist: 0x840
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x31270
-  __DATA_CONST.__objc_selrefs: 0x103d0
+  __DATA_CONST.__objc_const: 0x30bb8
+  __DATA_CONST.__objc_selrefs: 0xfe50
   __DATA_CONST.__objc_arraydata: 0x768
-  __AUTH_CONST.__cfstring: 0xe1e0
-  __AUTH_CONST.__const: 0x1998
-  __AUTH_CONST.__objc_const: 0x8b80
-  __AUTH_CONST.__objc_intobj: 0xc90
+  __AUTH_CONST.__cfstring: 0xd500
+  __AUTH_CONST.__const: 0x18e8
+  __AUTH_CONST.__objc_const: 0x8990
+  __AUTH_CONST.__objc_intobj: 0xcc0
   __AUTH_CONST.__objc_arrayobj: 0xc00
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0xc28
-  __AUTH.__objc_data: 0x6040
+  __AUTH_CONST.__auth_got: 0xc08
+  __AUTH.__objc_data: 0x5f00
   __DATA.__objc_protorefs: 0xe8
-  __DATA.__objc_classrefs: 0x1950
-  __DATA.__objc_superrefs: 0x978
-  __DATA.__objc_ivar: 0x21e8
-  __DATA.__data: 0x6488
-  __DATA.__bss: 0x850
+  __DATA.__objc_classrefs: 0x1968
+  __DATA.__objc_superrefs: 0x950
+  __DATA.__objc_ivar: 0x217c
+  __DATA.__data: 0x63c8
+  __DATA.__bss: 0x828
   __DATA_DIRTY.__objc_data: 0xc80
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D9665CA2-A272-3E94-85A9-3673844E4F55
-  Functions: 9306
-  Symbols:   35783
-  CStrings:  18710
+  UUID: A832989B-8CA1-3D4D-9439-EC966EF27DC6
+  Functions: 8958
+  Symbols:   34673
+  CStrings:  18195
 
Symbols:
+ +[SFAccountCellData accountCellDataWithSavedAccount:warning:searchPattern:savedAccountIsOnlySavedAccountForHighLevelDomain:shouldShowReusedPasswordWarning:]
+ +[SFNavigationBarMetrics traitsAffectingBarMetrics]
+ +[SFPasswordPickerServiceViewController _rememberStateForSystemAutoFillWithSearchQuery:savedAccount:]
+ +[SFPasswordPickerServiceViewController _restoreStateForSystemAutoFillToAccountPickerConfiguration:]
+ +[SFPasswordPickerServiceViewController _shouldRestoreStateForSystemAutoFillForAppID:]
+ +[UIFont(SafariServicesExtras) safari_monospacedDigitFontForTextStyle:]
+ +[_SFAccountManagerAppearanceValues _excessiveLineHeightCharacterSet]
+ +[_SFAccountManagerAppearanceValues subtitleFontForNarrowCellWithText:]
+ +[_SFDownload _sharedQueue]
+ +[_SFFormAutoFillController _getExternalLoginCredentialSuggestionsForDomains:pageURL:webFrameIdentifier:completion:]
+ +[_SFFormAutoFillController _getExternalLoginCredentialSuggestionsForDomains:webFrameIdentifier:completion:]
+ -[SFAccountCellData initWithSavedAccount:warning:searchPattern:savedAccountIsOnlySavedAccountForHighLevelDomain:shouldShowReusedPasswordWarning:]
+ -[SFAccountCellData setShouldShowReusedPasswordWarning:]
+ -[SFAccountCellData shouldShowReusedPasswordWarning]
+ -[SFAccountDetailViewController _canUserDeleteSavedAccount]
+ -[SFAccountDetailViewController _groupPickerMenuButton]
+ -[SFAccountPickerConfiguration initialSearchQuery]
+ -[SFAccountPickerConfiguration savedAccountToInitiallyShowDetailsFor]
+ -[SFAccountPickerConfiguration setInitialSearchQuery:]
+ -[SFAccountPickerConfiguration setSavedAccountToInitiallyShowDetailsFor:]
+ -[SFAccountPickerViewController searchQuery]
+ -[SFAccountPickerViewController setSearchQuery:]
+ -[SFAccountTableViewCell _layoutReusedPasswordWarningImageViewIfNecessary]
+ -[SFAccountTableViewCell setSavedAccount:searchPattern:emphasizeUserName:isReusedPassword:]
+ -[SFAddToHomeScreenServiceViewController didCopyStagedCookiesToURL:sandboxExtensionToken:]
+ -[SFAddToHomeScreenViewController _copyCurrentCookiesToStagingDirectory]
+ -[SFAddToHomeScreenViewController _issueReadOnlySandboxExtensionForURL:]
+ -[SFAddToHomeScreenViewController _issueReadOnlySandboxExtensionForURL:].cold.1
+ -[SFAddToHomeScreenViewController _removeStageCookiesDirectoryIfNeeded]
+ -[SFAddToHomeScreenViewController _removeStageCookiesDirectoryIfNeeded].cold.1
+ -[SFAddToHomeScreenViewController _stagedCookiesDirectoryURL]
+ -[SFDownloadsBarButtonItemView initWithFrame:]
+ -[SFMoveAccountsToGroupPickerViewController _loadReusedPasswords]
+ -[SFPrivacyReportExplanationDetailItemView _preferredContentSizeCategoryDidChange]
+ -[SFPrivacyReportGridView _preferredContentSizeCategoryDidChange]
+ -[SFPrivacyReportTrackerDetailViewController _updateHeaderSizeForTraitChanges]
+ -[SFQRImageHeaderView initWithFrame:]
+ -[SFQRImageHeaderView userInterfaceStyleDidChange]
+ -[SFRecentlyDeletedAccountsViewController tableView:shouldHighlightRowAtIndexPath:]
+ -[SFSafariViewController _notifyServiceOfUpdatedTintColors]
+ -[SFSharedAccountsGroupInvitationViewController tableView:shouldHighlightRowAtIndexPath:]
+ -[SFVibrantCellSelectionBackgroundView updateSelectionEffect]
+ -[SFWebAppDataProvider updateWithStagedCookiesDirectoryURL:sandboxExtensionToken:]
+ -[SFWebAppDataProvider updateWithStagedCookiesDirectoryURL:sandboxExtensionToken:].cold.1
+ -[SFWebAppDataProvider updateWithStagedCookiesDirectoryURL:sandboxExtensionToken:].cold.2
+ -[SFWebAppDataProvider webClipViewController:didFinishWithResult:].cold.1
+ -[UIWebClip(SafariServicesExtras) _sf_stagedCookiesURL]
+ -[_SFAccountManagerViewController _cellDataFromSavedAccounts:]
+ -[_SFAccountManagerViewController _passwordOptionsCellForTableView:]
+ -[_SFAccountPickerTableViewController _indexPathForSavedAccount:]
+ -[_SFAccountPickerTableViewController _showAccountDetailsForSavedAccount:]
+ -[_SFAirDropAccountSharingAuthenticationContext authenticationPolicy]
+ -[_SFAutoFillInputView _preferredContentSizeCategoryDidChange]
+ -[_SFBrowserContentViewController _isPresentedAsSheet]
+ -[_SFBrowserContentViewController scrollViewDidZoom:]
+ -[_SFFormAutoFillController setTestController:]
+ -[_SFFormAutoFillController testController]
+ -[_SFFormMetadataController collectFormMetadataForTesting]
+ -[_SFFormMetadataController finishedAutoFillingOneTimeCode:inFrame:shouldSubmit:]
+ -[_SFNavigationBar _barMetricTraitsDidChange]
+ -[_SFOptionsGroupDetailLabel initWithFrame:]
+ -[_SFPasswordAuditingViewController tableView:shouldHighlightRowAtIndexPath:]
+ -[_SFSettingsAlertContentController setNeedsUpdatePreferredContentSize]
+ -[_SFWebProcessPlugInAutoFillPageController collectFormMetadataForTestingAtURL:]
+ GCC_except_table181
+ GCC_except_table185
+ GCC_except_table190
+ GCC_except_table202
+ GCC_except_table211
+ GCC_except_table213
+ GCC_except_table219
+ GCC_except_table226
+ GCC_except_table229
+ GCC_except_table252
+ GCC_except_table256
+ GCC_except_table259
+ GCC_except_table262
+ GCC_except_table265
+ GCC_except_table267
+ GCC_except_table271
+ GCC_except_table275
+ GCC_except_table277
+ GCC_except_table283
+ GCC_except_table287
+ GCC_except_table290
+ GCC_except_table295
+ GCC_except_table299
+ GCC_except_table304
+ GCC_except_table306
+ GCC_except_table311
+ GCC_except_table313
+ GCC_except_table317
+ GCC_except_table322
+ GCC_except_table330
+ GCC_except_table340
+ GCC_except_table341
+ GCC_except_table348
+ GCC_except_table351
+ GCC_except_table352
+ GCC_except_table360
+ GCC_except_table361
+ GCC_except_table366
+ GCC_except_table369
+ GCC_except_table372
+ GCC_except_table392
+ GCC_except_table405
+ GCC_except_table406
+ GCC_except_table411
+ GCC_except_table416
+ GCC_except_table417
+ GCC_except_table424
+ GCC_except_table427
+ GCC_except_table441
+ GCC_except_table442
+ GCC_except_table446
+ GCC_except_table447
+ GCC_except_table454
+ GCC_except_table455
+ GCC_except_table460
+ GCC_except_table465
+ GCC_except_table471
+ GCC_except_table472
+ GCC_except_table482
+ GCC_except_table489
+ GCC_except_table495
+ GCC_except_table498
+ GCC_except_table499
+ GCC_except_table505
+ GCC_except_table511
+ GCC_except_table512
+ GCC_except_table519
+ GCC_except_table525
+ GCC_except_table530
+ GCC_except_table534
+ GCC_except_table539
+ GCC_except_table545
+ GCC_except_table548
+ GCC_except_table549
+ _APP_SANDBOX_READ
+ _CTFontCopySystemUIFontExcessiveLineHeightCharacterSet
+ _OBJC_CLASS_$_PMPasswordOptionsController
+ _OBJC_CLASS_$_SFTraitBackgroundBlurEffect
+ _OBJC_CLASS_$_UITraitHorizontalSizeClass
+ _OBJC_CLASS_$_UITraitLegibilityWeight
+ _OBJC_CLASS_$_UITraitPreferredContentSizeCategory
+ _OBJC_CLASS_$_UITraitPresentationSemanticContext
+ _OBJC_CLASS_$_UITraitUserInterfaceStyle
+ _OBJC_CLASS_$_UITraitVerticalSizeClass
+ _OBJC_CLASS_$_WBSCookieTransferController
+ _OBJC_IVAR_$_SFAccountCellData._shouldShowReusedPasswordWarning
+ _OBJC_IVAR_$_SFAccountPickerConfiguration._initialSearchQuery
+ _OBJC_IVAR_$_SFAccountPickerConfiguration._savedAccountToInitiallyShowDetailsFor
+ _OBJC_IVAR_$_SFAccountTableViewCell._reusedPasswordWarningImageView
+ _OBJC_IVAR_$_SFMoveAccountsToGroupPickerViewController._reusedPasswords
+ _OBJC_IVAR_$__SFFormAutoFillController._testController
+ _SANDBOX_EXTENSION_DEFAULT
+ _UIBackgroundTaskInvalid
+ _WBSAuthenticationPolicyForPasswordManager
+ _WBSDebugAutoFillConsoleLoggingEnabledPreferenceKey
+ _WBS_LOG_CHANNEL_PREFIXPasswordsIcons
+ _WBS_LOG_CHANNEL_PREFIXPasswordsIcons.log
+ _WBS_LOG_CHANNEL_PREFIXPasswordsIcons.onceToken
+ __OBJC_$_INSTANCE_METHODS_NSString(ScreenTime)
+ __OBJC_$_PROP_LIST_SFAccountTableViewCell.118
+ __OBJC_$_PROTOCOL_REFS_SFReaderViewControllerDelegate
+ __ZL30lastUsedAppIDForSystemAutoFill
+ __ZL32lastSearchQueryForSystemAutoFill
+ __ZL37lastUsedSavedAccountForSystemAutoFill
+ __ZL50timeIntervalSinceReferenceDateOfLastSystemAutoFill
+ __ZN14SafariServices25ArticleFinderJSController27substituteURLForNextPageURLEPK15OpaqueJSContextPKPK13OpaqueJSValue
+ __ZN14SafariServices34WebProcessPlugInReaderJSController40prepareTestComparisonDataAfterActivationEN12SafariShared46ReaderTestComparisonDataPreparationOpportunityE
+ ___108+[_SFFormAutoFillController _getExternalLoginCredentialSuggestionsForDomains:webFrameIdentifier:completion:]_block_invoke
+ ___108+[_SFFormAutoFillController _getExternalLoginCredentialSuggestionsForDomains:webFrameIdentifier:completion:]_block_invoke_2
+ ___115-[_SFWebAppServiceViewController webViewController:requestNotificationPermissionForSecurityOrigin:decisionHandler:]_block_invoke.146
+ ___116+[_SFFormAutoFillController _getExternalLoginCredentialSuggestionsForDomains:pageURL:webFrameIdentifier:completion:]_block_invoke
+ ___116-[SFContentBlockerManager(SFPrivate) loadDeclarativeNetRequestContentBlockerWithIdentifier:rules:completionHandler:]_block_invoke.126
+ ___27+[_SFDownload _sharedQueue]_block_invoke
+ ___29-[_SFDownload removeFromDisk]_block_invoke
+ ___29-[_SFDownload removeFromDisk]_block_invoke_2
+ ___29-[_SFDownload removeFromDisk]_block_invoke_2.cold.1
+ ___42-[_SFDownload _importPlaceholderIfNeeded:]_block_invoke.132
+ ___42-[_SFDownload _importPlaceholderIfNeeded:]_block_invoke.133
+ ___42-[_SFDownload _importPlaceholderIfNeeded:]_block_invoke.133.cold.1
+ ___42-[_SFDownload _importPlaceholderIfNeeded:]_block_invoke.134
+ ___42-[_SFDownload _importPlaceholderIfNeeded:]_block_invoke.137
+ ___42-[_SFDownload _importPlaceholderIfNeeded:]_block_invoke.137.cold.1
+ ___46-[_SFDownload _importCompleteDownloadIfNeeded]_block_invoke.143
+ ___46-[_SFDownload _importCompleteDownloadIfNeeded]_block_invoke.144
+ ___47-[_SFDownload removeDataAndPlaceholderFromDisk]_block_invoke_2
+ ___47-[_SFDownload removeDataAndPlaceholderFromDisk]_block_invoke_3
+ ___47-[_SFDownload removeDataAndPlaceholderFromDisk]_block_invoke_3.cold.1
+ ___53-[_SFDownload _didImportFileAtURL:completionHandler:]_block_invoke.145
+ ___53-[_SFDownload _didImportFileAtURL:completionHandler:]_block_invoke_2.146
+ ___53-[_SFDownload _didImportFileAtURL:completionHandler:]_block_invoke_2.cold.1
+ ___60-[_SFDownload _didImportPlaceholderAtURL:completionHandler:]_block_invoke.139
+ ___61-[_SFWebProcessPlugIn webProcessPlugIn:initializeWithObject:]_block_invoke
+ ___62-[_SFAccountManagerViewController _cellDataFromSavedAccounts:]_block_invoke
+ ___65-[SFMoveAccountsToGroupPickerViewController _loadReusedPasswords]_block_invoke
+ ___65-[SFMoveAccountsToGroupPickerViewController _loadReusedPasswords]_block_invoke.54
+ ___65-[SFMoveAccountsToGroupPickerViewController _loadReusedPasswords]_block_invoke_2
+ ___65-[SFMoveAccountsToGroupPickerViewController _loadReusedPasswords]_block_invoke_2.cold.1
+ ___65-[SFMoveAccountsToGroupPickerViewController _loadReusedPasswords]_block_invoke_3
+ ___67-[SFContentBlockerManager(SFPrivate) _beginContentBlockerDiscovery]_block_invoke.109
+ ___67-[SFPasswordSavingServiceViewController showPromptWithToken:style:]_block_invoke.116
+ ___68-[_SFAccountManagerViewController _passwordOptionsCellForTableView:]_block_invoke
+ ___69+[_SFAccountManagerAppearanceValues _excessiveLineHeightCharacterSet]_block_invoke
+ ___69-[_SFPasswordAuditingViewController _reloadSavedAccountsForceUpdate:]_block_invoke.85
+ ___69-[_SFPasswordAuditingViewController _reloadSavedAccountsForceUpdate:]_block_invoke.87
+ ___69-[_SFPasswordAuditingViewController _reloadSavedAccountsForceUpdate:]_block_invoke.89
+ ___69-[_SFPasswordAuditingViewController _reloadSavedAccountsForceUpdate:]_block_invoke_2.92
+ ___71-[_SFFormAutoFillController didCollectURLsForPreFilling:atURL:inFrame:]_block_invoke.199
+ ___71-[_SFFormAutoFillController didCollectURLsForPreFilling:atURL:inFrame:]_block_invoke_2.200
+ ___71-[_SFFormAutoFillController didCollectURLsForPreFilling:atURL:inFrame:]_block_invoke_3.206
+ ___72-[SFAddToHomeScreenViewController _copyCurrentCookiesToStagingDirectory]_block_invoke
+ ___72-[SFAddToHomeScreenViewController _copyCurrentCookiesToStagingDirectory]_block_invoke.cold.1
+ ___72-[_SFWebAppServiceViewController processWebPushForWebAppWithIdentifier:]_block_invoke.256
+ ___73-[_SFAccountPickerTableViewController tableView:didSelectRowAtIndexPath:]_block_invoke.160
+ ___73-[_SFAuthenticationContext _evaluatePolicyForClient:userInitiated:reply:]_block_invoke.65
+ ___73-[_SFAuthenticationContext _evaluatePolicyForClient:userInitiated:reply:]_block_invoke_2.66
+ ___75-[SFContentBlockerManager(SFPrivate) setExtension:isEnabled:byUserGesture:]_block_invoke.120
+ ___75-[SFContentBlockerManager(SFPrivate) setExtension:isEnabled:byUserGesture:]_block_invoke.120.cold.1
+ ___75-[_SFWebAppServiceViewController clearWebViewAndWebsiteDataWithCompletion:]_block_invoke.121
+ ___75-[_SFWebAppServiceViewController clearWebViewAndWebsiteDataWithCompletion:]_block_invoke.121.cold.1
+ ___75-[_SFWebAppServiceViewController clearWebViewAndWebsiteDataWithCompletion:]_block_invoke.127
+ ___78-[SFPrivacyReportTrackerDetailViewController _updateHeaderSizeForTraitChanges]_block_invoke
+ ___79-[SFContentBlockerManager(SFPrivate) _recompileEnabledContentBlockersIfNeeded:]_block_invoke.117
+ ___79-[SFContentBlockerManager(SFPrivate) _recompileEnabledContentBlockersIfNeeded:]_block_invoke.117.cold.1
+ ___82-[SFWebAppDataProvider updateWithStagedCookiesDirectoryURL:sandboxExtensionToken:]_block_invoke
+ ___82-[_SFDownload _download:decideDestinationWithSuggestedFilename:completionHandler:]_block_invoke.221
+ ___82-[_SFDownload _download:decideDestinationWithSuggestedFilename:completionHandler:]_block_invoke.221.cold.1
+ ___Block_byref_object_copy_.197
+ ___Block_byref_object_dispose_.198
+ ___WBS_LOG_CHANNEL_PREFIXPasswordsIcons_block_invoke
+ ___block_descriptor_40_ea8_32s_e27_v16?0"WKContentRuleList"8ls32l8
+ ___block_descriptor_41_ea8_32s_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e32_v16?0"_SFSettingsAlertButton"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e45_"WBSSavedAccount"16?0"WBSPasswordWarning"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e29_v24?0"NSArray"8"NSError"16ls32l8w40l8
+ ___block_descriptor_48_ea8_32s40bs_e46_v16?0"ASPasskeyCredentialRequestParameters"8ls40l8s32l8
+ ___block_descriptor_49_ea8_32s40s_e22_v20?0B8"LAContext"12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8s40l8w56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8
+ ___block_literal_global.112
+ ___block_literal_global.140
+ ___block_literal_global.164
+ ___block_literal_global.195
+ ___block_literal_global.207
+ ___block_literal_global.21
+ ___block_literal_global.231
+ ___block_literal_global.252
+ ___block_literal_global.265
+ ___block_literal_global.316
+ ___block_literal_global.432
+ ___block_literal_global.436
+ ___block_literal_global.484
+ ___block_literal_global.487
+ ___block_literal_global.492
+ ___block_literal_global.496
+ ___block_literal_global.52
+ ___block_literal_global.85
+ ___block_literal_global.87
+ ___block_literal_global.95
+ __excessiveLineHeightCharacterSet.excessiveLineHeightCharacterSet
+ __excessiveLineHeightCharacterSet.onceToken
+ __sharedQueue.onceToken
+ __sharedQueue.queue
+ __unnamed_array_storage.63
+ __unnamed_array_storage.68
+ __unnamed_array_storage.78
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_msgSend$_canUserDeleteSavedAccount
+ _objc_msgSend$_cellDataFromSavedAccounts:
+ _objc_msgSend$_copyCurrentCookiesToStagingDirectory
+ _objc_msgSend$_excessiveLineHeightCharacterSet
+ _objc_msgSend$_getExternalLoginCredentialSuggestionsForDomains:pageURL:webFrameIdentifier:completion:
+ _objc_msgSend$_getExternalLoginCredentialSuggestionsForDomains:webFrameIdentifier:completion:
+ _objc_msgSend$_groupPickerMenuButton
+ _objc_msgSend$_indexPathForSavedAccount:
+ _objc_msgSend$_isPresentedAsSheet
+ _objc_msgSend$_issueReadOnlySandboxExtensionForURL:
+ _objc_msgSend$_layoutReusedPasswordWarningImageViewIfNecessary
+ _objc_msgSend$_loadReusedPasswords
+ _objc_msgSend$_passwordOptionsCellForTableView:
+ _objc_msgSend$_rememberStateForSystemAutoFillWithSearchQuery:savedAccount:
+ _objc_msgSend$_removeStageCookiesDirectoryIfNeeded
+ _objc_msgSend$_restoreStateForSystemAutoFillToAccountPickerConfiguration:
+ _objc_msgSend$_sf_stagedCookiesURL
+ _objc_msgSend$_sharedQueue
+ _objc_msgSend$_shouldRestoreStateForSystemAutoFillForAppID:
+ _objc_msgSend$_showAccountDetailsForSavedAccount:
+ _objc_msgSend$_stagedCookiesDirectoryURL
+ _objc_msgSend$abGroupIdentifier
+ _objc_msgSend$accountCellDataWithSavedAccount:warning:searchPattern:savedAccountIsOnlySavedAccountForHighLevelDomain:shouldShowReusedPasswordWarning:
+ _objc_msgSend$authenticationPolicy
+ _objc_msgSend$autoFillController:didCollectFormMetadataForTesting:forURL:
+ _objc_msgSend$autoFillControllerShouldCollectFormMetadataForTesting:
+ _objc_msgSend$collectFormMetadataForTesting
+ _objc_msgSend$collectFormMetadataForTestingAtURL:
+ _objc_msgSend$copyCookiesFromFolderAtURL:intoDataStore:
+ _objc_msgSend$copyCookiesFromWebView:intoFolderAtURL:completionHandler:
+ _objc_msgSend$copyItemAtURL:toURL:error:
+ _objc_msgSend$currentOneTimeCodesForWebBrowserWithWebsiteFrameURLs:fieldClassification:inContext:
+ _objc_msgSend$didCopyStagedCookiesToURL:sandboxExtensionToken:
+ _objc_msgSend$fetchAllCredentialIdentitiesMatchingDomains:completion:
+ _objc_msgSend$initWithSavedAccount:warning:searchPattern:savedAccountIsOnlySavedAccountForHighLevelDomain:shouldShowReusedPasswordWarning:
+ _objc_msgSend$initialSearchQuery
+ _objc_msgSend$isABTestingEnabled
+ _objc_msgSend$makePasswordOptionsViewController
+ _objc_msgSend$numberOfSavedAccountsInPersonalKeychainForHighLevelDomain:
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$reconfiguredItemIdentifiers
+ _objc_msgSend$registerForTraitChanges:withTarget:action:
+ _objc_msgSend$safari_absoluteStringWithoutFragment
+ _objc_msgSend$safari_accessingSecurityScopedResource:
+ _objc_msgSend$safari_ensurePathExtension:
+ _objc_msgSend$safari_hasFeedScheme
+ _objc_msgSend$safari_highLevelDomainFromHostFallingBackToHostOrAbsoluteString
+ _objc_msgSend$safari_isAppleNewsURL
+ _objc_msgSend$safari_isAppleOneURL
+ _objc_msgSend$safari_isConfigProfileMIMEType
+ _objc_msgSend$safari_isSafariViewServiceBundle
+ _objc_msgSend$safari_isXWebSearchURL
+ _objc_msgSend$safari_loadObjectOfClasses:completionHandler:
+ _objc_msgSend$safari_loadObjectsFromItemProviders:usingLoader:completionHandler:
+ _objc_msgSend$safari_stringByReplacingLastOccurrenceOfWhitespaceWithANonBreakingSpace
+ _objc_msgSend$safari_stringByReplacingMarkupCharactersWithHTMLEntities
+ _objc_msgSend$safari_topLevelDomain
+ _objc_msgSend$safari_traitsAffectingTextAppearance
+ _objc_msgSend$safari_userVisibleScheme
+ _objc_msgSend$savedAccountToInitiallyShowDetailsFor
+ _objc_msgSend$searchQuery
+ _objc_msgSend$setInitialSearchQuery:
+ _objc_msgSend$setIsAccessibilityElement:
+ _objc_msgSend$setNeedsUpdatePreferredContentSize
+ _objc_msgSend$setSavedAccount:searchPattern:emphasizeUserName:isReusedPassword:
+ _objc_msgSend$setSavedAccountToInitiallyShowDetailsFor:
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$subtitleFontForNarrowCellWithText:
+ _objc_msgSend$systemYellowColor
+ _objc_msgSend$temporaryDirectory
+ _objc_msgSend$testController
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$updateAllSavedAccountsWithPasswordsWithUser:protectionSpace:withNewPassword:
+ _objc_msgSend$updateSelectionEffect
+ _objc_msgSend$updateWithStagedCookiesDirectoryURL:sandboxExtensionToken:
+ _sandbox_extension_consume
+ _sandbox_extension_issue_file
+ _sandbox_extension_release
- +[NSBundle(SafariServicesExtras) _sf_isSafariViewServiceBundle]
- +[NSBundle(SafariServicesExtras) _sf_isWebSheetApplicationBundle]
- +[NSItemProvider(SafariServicesExtras) _sf_loadObjectsFromItemProviders:usingLoader:completionHandler:]
- +[NSString(SafariServicesExtras) _sf_safeBrowsingPreferencesPlistPath]
- +[_SFAccountManagerAppearanceValues subtitleFontForNarrowCell]
- +[_SFBrowserSavedState defaultBrowserStateDatabase]
- +[_SFBrowserSavedState defaultPPTBrowserStateDatabase]
- +[_SFBrowserSavedState ephemeralSavedState]
- +[_SFBrowserSavedState inMemoryDatabase]
- +[_SFBrowserSavedState setSharedBrowserSavedState:]
- +[_SFBrowserSavedState setShouldMergeAllWindowsIfNeeded:]
- +[_SFBrowserSavedState sharedBrowserSavedState]
- +[_SFBrowserSavedState shouldMergeAllWindowsIfNeeded]
- +[_SFBrowserWindowSettings setSharedSettings:]
- +[_SFBrowserWindowSettings settings]
- +[_SFFormAutoFillController _getExternalLoginCredentialSuggestionsForDomains:completion:]
- +[_SFFormAutoFillController _getExternalLoginCredentialSuggestionsForDomains:pageURL:completion:]
- -[NSItemProvider(SafariServicesExtras) _sf_loadObjectOfClasses:completionHandler:]
- -[NSString(SafariServicesExtras) _sf_ensurePathExtension:]
- -[NSString(SafariServicesExtras) sf_URLScheme]
- -[NSString(SafariServicesExtras) sf_isConfigProfileMIMEType]
- -[NSString(SafariServicesExtras) sf_isFeedScheme]
- -[NSString(SafariServicesExtras) sf_stringByAddingSoftBreaksBeforePeriods]
- -[NSString(SafariServicesExtras) sf_stringByReplacingLastOccurrenceOfWhitespaceWithANonBreakingSpace]
- -[NSString(SafariServicesExtras) sf_stringByReplacingMarkupCharactersWithHTMLEntities]
- -[NSURL(SafariServicesExtras) _sf_accessingSecurityScopedResource:]
- -[NSURL(SafariServicesExtras) _sf_highLevelDomainFromHostFallingBackToHostOrAbsoluteString]
- -[NSURL(SafariServicesExtras) _sf_isAppleOneURL]
- -[NSURL(SafariServicesExtras) _sf_itunesItemIdentifier]
- -[NSURL(SafariServicesExtras) _sf_topLevelDomain]
- -[NSURL(SafariServicesExtras) sf_absoluteStringWithoutFragment]
- -[NSURL(SafariServicesExtras) sf_isAppleNewsURL]
- -[NSURL(SafariServicesExtras) sf_isWebSearchURL]
- -[SFAccountCellData initWithSavedAccount:warning:searchPattern:savedAccountIsOnlySavedAccountForHighLevelDomain:]
- -[SFAccountDetailTOTPTableViewCell traitCollectionDidChange:]
- -[SFAddToHomeScreenServiceViewController loadURL:]
- -[SFAddToHomeScreenViewController initWithURL:completion:]
- -[SFBrowserStateSQLiteStore .cxx_destruct]
- -[SFBrowserStateSQLiteStore _cacheUUIDForTabStateData:]
- -[SFBrowserStateSQLiteStore _checkDatabaseIntegrity]
- -[SFBrowserStateSQLiteStore _checkDatabaseIntegrity].cold.1
- -[SFBrowserStateSQLiteStore _checkDatabaseIntegrity].cold.2
- -[SFBrowserStateSQLiteStore _closeDatabase]
- -[SFBrowserStateSQLiteStore _createFreshDatabaseSchema]
- -[SFBrowserStateSQLiteStore _createFreshDatabaseSchema].cold.1
- -[SFBrowserStateSQLiteStore _createTableForTabSession]
- -[SFBrowserStateSQLiteStore _createTableForTabSession].cold.1
- -[SFBrowserStateSQLiteStore _createTableForTabSession].cold.2
- -[SFBrowserStateSQLiteStore _createTableForTabs]
- -[SFBrowserStateSQLiteStore _createTableForTabs].cold.1
- -[SFBrowserStateSQLiteStore _createTableForTabs].cold.2
- -[SFBrowserStateSQLiteStore _databaseIDForBrowserWindow:]
- -[SFBrowserStateSQLiteStore _insertTabStateWithData:]
- -[SFBrowserStateSQLiteStore _insertTabStateWithData:].cold.1
- -[SFBrowserStateSQLiteStore _insertTabStateWithData:].cold.2
- -[SFBrowserStateSQLiteStore _isDatabaseOpen]
- -[SFBrowserStateSQLiteStore _isTabStateCached:]
- -[SFBrowserStateSQLiteStore _mergeAllWindowsIfNeeded]
- -[SFBrowserStateSQLiteStore _mergeAllWindowsIfNeeded].cold.1
- -[SFBrowserStateSQLiteStore _migrateFromLegacyPlistIfNeeded]
- -[SFBrowserStateSQLiteStore _migrateFromLegacyPlistWithPath:]
- -[SFBrowserStateSQLiteStore _migrateFromLegacyPlistWithPath:].cold.1
- -[SFBrowserStateSQLiteStore _migrateFromLegacyPlistWithPath:].cold.2
- -[SFBrowserStateSQLiteStore _migrateToCurrentSchemaVersionIfNeeded]
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion:]
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion:].cold.1
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion:].cold.2
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion:].cold.3
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion:].cold.4
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion:].cold.5
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_2]
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_2].cold.1
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_3]
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_3].cold.1
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_3].cold.2
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_3].cold.3
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_3].cold.4
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_3].cold.5
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_3].cold.6
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_3].cold.7
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_4]
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_4].cold.1
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_5]
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_5].cold.1
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_5].cold.2
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_5].cold.3
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_5].cold.4
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_5].cold.5
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_6]
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_6].cold.1
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_7]
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_7].cold.1
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_8]
- -[SFBrowserStateSQLiteStore _migrateToSchemaVersion_8].cold.1
- -[SFBrowserStateSQLiteStore _openDatabaseAndCheckIntegrity:]
- -[SFBrowserStateSQLiteStore _openDatabaseAndCheckIntegrity:].cold.1
- -[SFBrowserStateSQLiteStore _openDatabaseAndCheckIntegrity:].cold.2
- -[SFBrowserStateSQLiteStore _openDatabaseAndCheckIntegrity:].cold.3
- -[SFBrowserStateSQLiteStore _readSavedSessionStateDataForTabWithUUIDString:]
- -[SFBrowserStateSQLiteStore _readTabStatesWithBrowserWindowUUID:completion:]
- -[SFBrowserStateSQLiteStore _recoverFromDatabaseInconsistencyFromSchemaVersion3Migration]
- -[SFBrowserStateSQLiteStore _recoverFromDatabaseInconsistencyFromSchemaVersion3Migration].cold.1
- -[SFBrowserStateSQLiteStore _recoverFromDatabaseInconsistencyFromSchemaVersion3Migration].cold.2
- -[SFBrowserStateSQLiteStore _recoverFromDatabaseInconsistencyFromSchemaVersion3Migration].cold.3
- -[SFBrowserStateSQLiteStore _regenerateTabUUIDsForDeviceRestoration]
- -[SFBrowserStateSQLiteStore _regenerateTabUUIDsForDeviceRestoration].cold.1
- -[SFBrowserStateSQLiteStore _removeSavedSessionStateDataForTabsWithUUIDStrings:]
- -[SFBrowserStateSQLiteStore _removeSavedSessionStateDataForTabsWithUUIDStrings:].cold.1
- -[SFBrowserStateSQLiteStore _saveBrowserWindowStateWithData:]
- -[SFBrowserStateSQLiteStore _saveBrowserWindowStateWithData:].cold.1
- -[SFBrowserStateSQLiteStore _saveBrowserWindowStateWithData:].cold.2
- -[SFBrowserStateSQLiteStore _saveBrowserWindowStateWithDictionary:]
- -[SFBrowserStateSQLiteStore _schemaVersion]
- -[SFBrowserStateSQLiteStore _setDatabaseID:browserWindow:]
- -[SFBrowserStateSQLiteStore _setDatabaseSchemaVersion:]
- -[SFBrowserStateSQLiteStore _sqliteStatementForTabDeleting]
- -[SFBrowserStateSQLiteStore _tabStateDataForUUID:]
- -[SFBrowserStateSQLiteStore _tabUUIDsInWindow:]
- -[SFBrowserStateSQLiteStore _updateBrowserWindowStateWithDictionary:]
- -[SFBrowserStateSQLiteStore _updateBrowserWindowStateWithDictionary:].cold.1
- -[SFBrowserStateSQLiteStore _updateBrowserWindowStateWithDictionary:].cold.2
- -[SFBrowserStateSQLiteStore _updateBrowserWindowWithData:tabs:]
- -[SFBrowserStateSQLiteStore _updateBrowserWindowWithData:tabs:].cold.1
- -[SFBrowserStateSQLiteStore _updateBrowserWindowWithData:tabs:].cold.2
- -[SFBrowserStateSQLiteStore _updateOrInsertTabStateWithData:]
- -[SFBrowserStateSQLiteStore _updateTabStateWithData:]
- -[SFBrowserStateSQLiteStore _vacuum]
- -[SFBrowserStateSQLiteStore _vacuum].cold.1
- -[SFBrowserStateSQLiteStore browserWindows]
- -[SFBrowserStateSQLiteStore checkPointWriteAheadLog]
- -[SFBrowserStateSQLiteStore closeDatabase]
- -[SFBrowserStateSQLiteStore dealloc]
- -[SFBrowserStateSQLiteStore deleteRecentlyClosedWindowsWithProfileIdentifier:]
- -[SFBrowserStateSQLiteStore deleteSavedStatesForProfileWithIdentifier:]
- -[SFBrowserStateSQLiteStore deleteTabStateWithBrowserWindowUUID:andRemoveWindow:]
- -[SFBrowserStateSQLiteStore initWithDatabaseURL:]
- -[SFBrowserStateSQLiteStore init]
- -[SFBrowserStateSQLiteStore mergeAllWindows]
- -[SFBrowserStateSQLiteStore readSavedSessionStateDataForTabWithUUIDString:]
- -[SFBrowserStateSQLiteStore readTabStatesWithBrowserWindowUUID:completion:]
- -[SFBrowserStateSQLiteStore recentlyClosedWindows]
- -[SFBrowserStateSQLiteStore regenerateTabUUIDsForDeviceRestoration]
- -[SFBrowserStateSQLiteStore removeSavedSessionStateDataForTabsWithUUIDStrings:]
- -[SFBrowserStateSQLiteStore removeTabWithTabData:]
- -[SFBrowserStateSQLiteStore saveTabStateWithDictionary:]
- -[SFBrowserStateSQLiteStore setSecureDeleteEnabled:]
- -[SFBrowserStateSQLiteStore tabStateDataForUUID:]
- -[SFBrowserStateSQLiteStore tabStatesWithBrowserWindowUUID:]
- -[SFBrowserStateSQLiteStore updateBrowserWindowStateWithDictionary:completion:]
- -[SFBrowserStateSQLiteStore updateBrowserWindowWithData:tabs:]
- -[SFBrowserStateSQLiteStore updateSceneID:]
- -[SFBrowserStateSQLiteStore updateTabWithTabStateData:]
- -[SFDownloadsBarButtonItemView traitCollectionDidChange:]
- -[SFPrivacyReportExplanationDetailItemView traitCollectionDidChange:]
- -[SFPrivacyReportGridView traitCollectionDidChange:]
- -[SFPrivacyReportIconView traitCollectionDidChange:]
- -[SFPrivacyReportTrackerDetailViewController traitCollectionDidChange:]
- -[SFPrivacyReportViewController traitCollectionDidChange:]
- -[SFQRImageHeaderView traitCollectionDidChange:]
- -[SFReaderEnabledWebViewController traitCollectionDidChange:]
- -[SFRecentlyDeletedAccountsViewController tableView:willSelectRowAtIndexPath:]
- -[SFSafariViewController traitCollectionDidChange:]
- -[SFVibrantCellSelectionBackgroundView _selectionEffect]
- -[SFVibrantCellSelectionBackgroundView traitCollectionDidChange:]
- -[SFWebAppDataProvider _createWebClipFromWebView]
- -[SFWebAppDataProvider _createWebView]
- -[SFWebAppDataProvider _finishPreparingFromWebView]
- -[SFWebAppDataProvider prepareWithURL:]
- -[SFWebAppDataProvider webView:didFailNavigation:withError:]
- -[SFWebAppDataProvider webView:didFailNavigation:withError:].cold.1
- -[SFWebAppDataProvider webView:didFinishNavigation:]
- -[SFWebViewController _webView:runWebAuthenticationPanel:initiatedByFrame:completionHandler:]
- -[SFWebViewController panel:decidePolicyForLocalAuthenticatorWithCompletionHandler:]
- -[SFWebViewController panel:dismissWebAuthenticationPanelWithResult:]
- -[SFWebViewController panel:requestPINWithRemainingRetries:completionHandler:]
- -[SFWebViewController panel:selectAssertionResponse:source:completionHandler:]
- -[SFWebViewController panel:updateWebAuthenticationPanel:]
- -[_SFAccountManagerViewController _autoFillCellForTableView:]
- -[_SFAccountManagerViewController tableView:willSelectRowAtIndexPath:]
- -[_SFAutoFillInputView traitCollectionDidChange:]
- -[_SFBrowserSavedState .cxx_destruct]
- -[_SFBrowserSavedState _checkPointWriteAheadLogIfNeeded]
- -[_SFBrowserSavedState _historyItemsWereRemoved:]
- -[_SFBrowserSavedState _notifyThatRecentlyClosedTabsWereRemoved:]
- -[_SFBrowserSavedState _readBrowserControllersSavedState]
- -[_SFBrowserSavedState _readRecentlyClosedTabsStateIfNecessary]
- -[_SFBrowserSavedState _removeRecentlyClosedTabStateData:]
- -[_SFBrowserSavedState activeDocumentIsValidForBrowserControllerWithUUID:]
- -[_SFBrowserSavedState addRecentlyClosedTabs:]
- -[_SFBrowserSavedState browserWindows]
- -[_SFBrowserSavedState clearRecentlyClosedTabsForProfileWithIdentifier:]
- -[_SFBrowserSavedState clearSavedStatesForProfileWithIdentifier:closingDatabase:]
- -[_SFBrowserSavedState dealloc]
- -[_SFBrowserSavedState initWithDatabaseURL:]
- -[_SFBrowserSavedState loadSessionStateDataAndRemoveRecentlyClosedTab:]
- -[_SFBrowserSavedState readSavedSessionStateDataForTabWithUUID:]
- -[_SFBrowserSavedState recentlyClosedTabsForProfileWithIdentifier:]
- -[_SFBrowserSavedState regenerateTabUUIDsForDeviceRestoration]
- -[_SFBrowserSavedState removeRecentlyClosedTabWithStateData:]
- -[_SFBrowserSavedState removeTabStateWithTabData:]
- -[_SFBrowserSavedState removeTabsStateForBrowserControllerWithUUID:andRemoveWindow:]
- -[_SFBrowserSavedState saveTabStateData:]
- -[_SFBrowserSavedState saveTabsState:forBrowserControllerWithUUID:completion:]
- -[_SFBrowserSavedState savedTabsStateForBrowserControllerWithUUID:]
- -[_SFBrowserSavedState secureDeleteEnabled]
- -[_SFBrowserSavedState setActiveDocumentIsValid:forBrowserControllerWithUUID:]
- -[_SFBrowserSavedState setBrowserWindows:]
- -[_SFBrowserSavedState setSecureDeleteEnabled:]
- -[_SFBrowserSavedState shouldBeUsedDuringTest]
- -[_SFBrowserSavedState tabStateDataForUUID:]
- -[_SFBrowserSavedState updateBrowserWindowState:tabs:]
- -[_SFBrowserSavedState updateSceneID:]
- -[_SFBrowserWindowSettings .cxx_destruct]
- -[_SFBrowserWindowSettings _blankSnapshotKeyForPrivateBrowsing:syncableTabGroupUUID:]
- -[_SFBrowserWindowSettings _boolValueForKey:windowUUID:]
- -[_SFBrowserWindowSettings _initializeSettingsDictionaryIfNeeded]
- -[_SFBrowserWindowSettings _numberForKey:windowUUID:]
- -[_SFBrowserWindowSettings _setBool:forKey:windowUUID:]
- -[_SFBrowserWindowSettings _setString:forKey:windowUUID:]
- -[_SFBrowserWindowSettings _stringForKey:windowUUID:]
- -[_SFBrowserWindowSettings _synchronizeNow]
- -[_SFBrowserWindowSettings activeDocumentIsValidForWindowWithUUID:]
- -[_SFBrowserWindowSettings blankSnapshotGroupIdentifierForPrivateBrowsing:syncableTabGroupUUID:forWindowWithUUID:]
- -[_SFBrowserWindowSettings dataForKey:forWindowWithUUID:]
- -[_SFBrowserWindowSettings hasPrivateBrowsingWindow]
- -[_SFBrowserWindowSettings init]
- -[_SFBrowserWindowSettings invalidatesClosedWindows]
- -[_SFBrowserWindowSettings isShowingTabViewForWindowWithUUID:]
- -[_SFBrowserWindowSettings privateBrowsingEnabledForWindowWithUUID:]
- -[_SFBrowserWindowSettings removeWindowWithUUID:]
- -[_SFBrowserWindowSettings setActiveDocumentIsValid:forWindowWithUUID:]
- -[_SFBrowserWindowSettings setBlankSnapshotGroupIdentifier:forPrivateBrowsing:syncableTabGroupUUID:forWindowWithUUID:]
- -[_SFBrowserWindowSettings setData:forKey:forWindowWithUUID:]
- -[_SFBrowserWindowSettings setInvalidatesClosedWindows:]
- -[_SFBrowserWindowSettings setIsShowingTabView:forWindowWithUUID:]
- -[_SFBrowserWindowSettings setPrivateBrowsingEnabled:forWindowWithUUID:]
- -[_SFBrowserWindowSettings synchronize]
- -[_SFBrowserWindowSettings validateWindowSettingsWithUUIDs:]
- -[_SFBrowserWindowStateData .cxx_destruct]
- -[_SFBrowserWindowStateData UUIDString]
- -[_SFBrowserWindowStateData UUID]
- -[_SFBrowserWindowStateData activeDocumentIndex]
- -[_SFBrowserWindowStateData activePrivateDocumentIndex]
- -[_SFBrowserWindowStateData activeProfileIdentifier]
- -[_SFBrowserWindowStateData databaseID]
- -[_SFBrowserWindowStateData debugDescription]
- -[_SFBrowserWindowStateData dictionaryRepresentation]
- -[_SFBrowserWindowStateData initWithDictionaryRepresentation:]
- -[_SFBrowserWindowStateData initWithSQLiteRow:]
- -[_SFBrowserWindowStateData initWithUUIDString:sceneID:]
- -[_SFBrowserWindowStateData isActiveDocumentValid]
- -[_SFBrowserWindowStateData isEqual:]
- -[_SFBrowserWindowStateData isInDatabase]
- -[_SFBrowserWindowStateData isTabStateSuccessfullyLoaded]
- -[_SFBrowserWindowStateData legacyPlistFileVersion]
- -[_SFBrowserWindowStateData needsQuickUpdate]
- -[_SFBrowserWindowStateData sceneID]
- -[_SFBrowserWindowStateData setActiveDocumentIndex:]
- -[_SFBrowserWindowStateData setActivePrivateDocumentIndex:]
- -[_SFBrowserWindowStateData setActiveProfileIdentifier:]
- -[_SFBrowserWindowStateData setDatabaseID:]
- -[_SFBrowserWindowStateData setIsActiveDocumentValid:]
- -[_SFBrowserWindowStateData setIsTabStateSuccessfullyLoaded:]
- -[_SFBrowserWindowStateData setLegacyPlistFileVersion:]
- -[_SFBrowserWindowStateData setNeedsQuickUpdate:]
- -[_SFBrowserWindowStateData setSceneID:]
- -[_SFBrowserWindowStateData setType:]
- -[_SFBrowserWindowStateData setUUID:]
- -[_SFBrowserWindowStateData setUUIDString:]
- -[_SFBrowserWindowStateData type]
- -[_SFDownload removeFromDisk].cold.1
- -[_SFFormMetadataController finishedAutoFillingOneTimeCodeInFrame:shouldSubmit:]
- -[_SFNavigationBar traitCollectionDidChange:]
- -[_SFOptionsGroupDetailLabel traitCollectionDidChange:]
- -[_SFPasswordAuditingViewController traitCollectionDidChange:]
- -[_SFRecentWebSearchesController .cxx_destruct]
- -[_SFRecentWebSearchesController _migrateLegacyData]
- -[_SFRecentWebSearchesController _removeLegacyRecentSearchesData]
- -[_SFRecentWebSearchesController initWithPathToLegacySearchesFile:]
- -[_SFSettingsAlertButton traitCollectionDidChange:]
- -[_SFSettingsAlertContentController traitCollectionDidChange:]
- -[_SFTableLinkableFooterView traitCollectionDidChange:]
- -[_SFTranslationTargetLocaleAlertActionContentViewController traitCollectionDidChange:]
- GCC_except_table103
- GCC_except_table119
- GCC_except_table125
- GCC_except_table131
- GCC_except_table133
- GCC_except_table139
- GCC_except_table141
- GCC_except_table145
- GCC_except_table155
- GCC_except_table156
- GCC_except_table157
- GCC_except_table158
- GCC_except_table162
- GCC_except_table163
- GCC_except_table164
- GCC_except_table183
- GCC_except_table186
- GCC_except_table193
- GCC_except_table200
- GCC_except_table206
- GCC_except_table210
- GCC_except_table212
- GCC_except_table215
- GCC_except_table223
- GCC_except_table227
- GCC_except_table232
- GCC_except_table253
- GCC_except_table258
- GCC_except_table260
- GCC_except_table263
- GCC_except_table266
- GCC_except_table270
- GCC_except_table274
- GCC_except_table276
- GCC_except_table280
- GCC_except_table284
- GCC_except_table289
- GCC_except_table291
- GCC_except_table296
- GCC_except_table303
- GCC_except_table305
- GCC_except_table309
- GCC_except_table312
- GCC_except_table316
- GCC_except_table320
- GCC_except_table324
- GCC_except_table337
- GCC_except_table338
- GCC_except_table343
- GCC_except_table344
- GCC_except_table350
- GCC_except_table353
- GCC_except_table354
- GCC_except_table362
- GCC_except_table363
- GCC_except_table368
- GCC_except_table384
- GCC_except_table385
- GCC_except_table394
- GCC_except_table409
- GCC_except_table412
- GCC_except_table415
- GCC_except_table420
- GCC_except_table423
- GCC_except_table439
- GCC_except_table440
- GCC_except_table444
- GCC_except_table445
- GCC_except_table449
- GCC_except_table450
- GCC_except_table458
- GCC_except_table459
- GCC_except_table466
- GCC_except_table469
- GCC_except_table476
- GCC_except_table483
- GCC_except_table490
- GCC_except_table493
- GCC_except_table497
- GCC_except_table503
- GCC_except_table506
- GCC_except_table507
- GCC_except_table517
- GCC_except_table523
- GCC_except_table526
- GCC_except_table532
- GCC_except_table533
- GCC_except_table542
- GCC_except_table543
- GCC_except_table547
- _CPSharedResourcesDirectory
- _OBJC_CLASS_$_SFBrowserStateSQLiteStore
- _OBJC_CLASS_$_WBSSQLiteDatabase
- _OBJC_CLASS_$_WBSSQLiteStatement
- _OBJC_CLASS_$__SFBrowserSavedState
- _OBJC_CLASS_$__SFBrowserWindowSettings
- _OBJC_CLASS_$__SFBrowserWindowStateData
- _OBJC_IVAR_$_SFBrowserStateSQLiteStore._browserWindowDatabaseIDs
- _OBJC_IVAR_$_SFBrowserStateSQLiteStore._cachedTabDeleteStatement
- _OBJC_IVAR_$_SFBrowserStateSQLiteStore._database
- _OBJC_IVAR_$_SFBrowserStateSQLiteStore._databaseQueue
- _OBJC_IVAR_$_SFBrowserStateSQLiteStore._databaseURL
- _OBJC_IVAR_$_SFBrowserStateSQLiteStore._generateUUIDFunctionAttached
- _OBJC_IVAR_$_SFBrowserStateSQLiteStore._tabUUIDStrings
- _OBJC_IVAR_$__SFAccountManagerViewController._autoFillPasswordsCell
- _OBJC_IVAR_$__SFAccountManagerViewController._securityRecommendationsCell
- _OBJC_IVAR_$__SFAccountManagerViewController._viewGroupDetailsCell
- _OBJC_IVAR_$__SFBrowserSavedState._browserStateSQLiteStore
- _OBJC_IVAR_$__SFBrowserSavedState._browserWindows
- _OBJC_IVAR_$__SFBrowserSavedState._checkPointWriteAheadLogOnNextUpdate
- _OBJC_IVAR_$__SFBrowserSavedState._haveLoadedRecentlyClosedTabs
- _OBJC_IVAR_$__SFBrowserSavedState._recentlyClosedTabs
- _OBJC_IVAR_$__SFBrowserSavedState._secureDeleteEnabled
- _OBJC_IVAR_$__SFBrowserSavedState._shouldBeUsedDuringTest
- _OBJC_IVAR_$__SFBrowserSavedState._tabCountByWindowUUID
- _OBJC_IVAR_$__SFBrowserWindowSettings._invalidatesClosedWindows
- _OBJC_IVAR_$__SFBrowserWindowSettings._settingsDictionary
- _OBJC_IVAR_$__SFBrowserWindowSettings._synchronizeScheduled
- _OBJC_IVAR_$__SFBrowserWindowStateData._UUIDString
- _OBJC_IVAR_$__SFBrowserWindowStateData._activeDocumentIndex
- _OBJC_IVAR_$__SFBrowserWindowStateData._activePrivateDocumentIndex
- _OBJC_IVAR_$__SFBrowserWindowStateData._activeProfileIdentifier
- _OBJC_IVAR_$__SFBrowserWindowStateData._databaseID
- _OBJC_IVAR_$__SFBrowserWindowStateData._isActiveDocumentValid
- _OBJC_IVAR_$__SFBrowserWindowStateData._isTabStateSuccessfullyLoaded
- _OBJC_IVAR_$__SFBrowserWindowStateData._legacyPlistFileVersion
- _OBJC_IVAR_$__SFBrowserWindowStateData._needsQuickUpdate
- _OBJC_IVAR_$__SFBrowserWindowStateData._sceneID
- _OBJC_IVAR_$__SFBrowserWindowStateData._type
- _OBJC_IVAR_$__SFRecentWebSearchesController._pathToLegacySearchesFile
- _OBJC_METACLASS_$_SFBrowserStateSQLiteStore
- _OBJC_METACLASS_$__SFBrowserSavedState
- _OBJC_METACLASS_$__SFBrowserWindowSettings
- _OBJC_METACLASS_$__SFBrowserWindowStateData
- _SFMaximumRecentlyClosedTabCount
- _SFRecentlyClosedTabsWereAddedNotification
- _SFRecentlyClosedTabsWereRemovedNotification
- _SFRemovedTabStateDataKey
- _SFStatePersistenceLegacyPlistVersionKey
- _SFStatePersistenceWindowActivePrivateTabIndexKey
- _SFStatePersistenceWindowActiveProfileIdentifierKey
- _SFStatePersistenceWindowActiveTabIndexKey
- _SFStatePersistenceWindowPrivateTabsKey
- _SFStatePersistenceWindowSceneIDKey
- _SFStatePersistenceWindowTabsKey
- _SFStatePersistenceWindowUUIDKey
- _WBSHistoryItemsKey
- _WBSHistoryItemsWereRemovedNotification
- _WBS_LOG_CHANNEL_PREFIXItemProvider
- _WBS_LOG_CHANNEL_PREFIXItemProvider.log
- _WBS_LOG_CHANNEL_PREFIXItemProvider.onceToken
- _WBS_LOG_CHANNEL_PREFIXStatePersistence
- _WBS_LOG_CHANNEL_PREFIXStatePersistence.log
- _WBS_LOG_CHANNEL_PREFIXStatePersistence.onceToken
- __OBJC_$_CATEGORY_NSItemProvider_$_SafariServicesExtras
- __OBJC_$_CLASS_METHODS_NSItemProvider(SafariServicesExtras)
- __OBJC_$_CLASS_METHODS_NSString(ScreenTime|SafariServicesExtras)
- __OBJC_$_CLASS_METHODS__SFBrowserSavedState
- __OBJC_$_CLASS_METHODS__SFBrowserWindowSettings
- __OBJC_$_CLASS_PROP_LIST__SFBrowserSavedState
- __OBJC_$_CLASS_PROP_LIST__SFBrowserWindowSettings
- __OBJC_$_INSTANCE_METHODS_NSItemProvider(SafariServicesExtras)
- __OBJC_$_INSTANCE_METHODS_NSString(ScreenTime|SafariServicesExtras)
- __OBJC_$_INSTANCE_METHODS_SFBrowserStateSQLiteStore
- __OBJC_$_INSTANCE_METHODS__SFBrowserSavedState
- __OBJC_$_INSTANCE_METHODS__SFBrowserWindowSettings
- __OBJC_$_INSTANCE_METHODS__SFBrowserWindowStateData
- __OBJC_$_INSTANCE_VARIABLES_SFBrowserStateSQLiteStore
- __OBJC_$_INSTANCE_VARIABLES__SFBrowserSavedState
- __OBJC_$_INSTANCE_VARIABLES__SFBrowserWindowSettings
- __OBJC_$_INSTANCE_VARIABLES__SFBrowserWindowStateData
- __OBJC_$_INSTANCE_VARIABLES__SFRecentWebSearchesController
- __OBJC_$_PROP_LIST_SFAccountTableViewCell.107
- __OBJC_$_PROP_LIST_SFBrowserStateSQLiteStore
- __OBJC_$_PROP_LIST__SFBrowserSavedState
- __OBJC_$_PROP_LIST__SFBrowserWindowSettings
- __OBJC_$_PROP_LIST__SFBrowserWindowStateData
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__WKWebAuthenticationPanelDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES__WKWebAuthenticationPanelDelegate
- __OBJC_$_PROTOCOL_REFS_SafariPasswordManagersControllerDelegate
- __OBJC_$_PROTOCOL_REFS__WKWebAuthenticationPanelDelegate
- __OBJC_CLASS_RO_$_SFBrowserStateSQLiteStore
- __OBJC_CLASS_RO_$__SFBrowserSavedState
- __OBJC_CLASS_RO_$__SFBrowserWindowSettings
- __OBJC_CLASS_RO_$__SFBrowserWindowStateData
- __OBJC_LABEL_PROTOCOL_$_SafariPasswordManagersControllerDelegate
- __OBJC_LABEL_PROTOCOL_$__WKWebAuthenticationPanelDelegate
- __OBJC_METACLASS_RO_$_SFBrowserStateSQLiteStore
- __OBJC_METACLASS_RO_$__SFBrowserSavedState
- __OBJC_METACLASS_RO_$__SFBrowserWindowSettings
- __OBJC_METACLASS_RO_$__SFBrowserWindowStateData
- __OBJC_PROTOCOL_$_SafariPasswordManagersControllerDelegate
- __OBJC_PROTOCOL_$__WKWebAuthenticationPanelDelegate
- __SFDeviceSupportsHighQualityGraphics
- __SFPrivateBrowsingDefaultsKey
- __SFSafariNonContaineredSettingsDirectoryPath
- __SFWebKitWebAuthenticationDefaultsKey
- __Z16WTFCrashWithInfoiPKcS0_i
- __ZL12generateUUIDP15sqlite3_contextiPP13sqlite3_value
- __ZL22databaseURLForFileNameP8NSString
- __ZL29shouldMergeAllWindowsIfNeeded
- __ZL31sharedBrowserSavedStateInstance
- __ZN12SafariShared12JSControllerC2Ev
- __ZN12SafariShared22WBSSQLiteDatabaseFetchIJ19SFBrowserWindowTypeEEEP22WBSSQLiteRowEnumeratorP17WBSSQLiteDatabaseP8NSStringDpOT_
- __ZN12SafariShared22WBSSQLiteDatabaseFetchIJEEEP22WBSSQLiteRowEnumeratorP17WBSSQLiteDatabaseP8NSStringDpOT_
- __ZN12SafariShared22WBSSQLiteDatabaseFetchIJRU8__strongP8NSStringEEEP22WBSSQLiteRowEnumeratorP17WBSSQLiteDatabaseS2_DpOT_
- __ZN12SafariShared22WBSSQLiteDatabaseFetchIJU8__strongP8NSStringEEEP22WBSSQLiteRowEnumeratorP17WBSSQLiteDatabaseS2_DpOT_
- __ZN12SafariShared22WBSSQLiteDatabaseFetchIJlEEEP22WBSSQLiteRowEnumeratorP17WBSSQLiteDatabaseP8NSStringDpOT_
- __ZN12SafariShared25SuddenTerminationDisabler23enableSuddenTerminationEv
- __ZN12SafariShared25SuddenTerminationDisablerC1EP8NSString
- __ZN12SafariShared25SuddenTerminationDisablerD2Ev
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi10EbJbU8__strongP8NSStringlS3_S3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi10ElJbbU8__strongP8NSStringlS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi11EbJU8__strongP8NSStringlS3_S3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi11EbJbU8__strongP8NSStringlS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi12EU8__strongP8NSStringJlS3_S3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi12EbJU8__strongP8NSStringlS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi13EU8__strongP8NSStringJlS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi13ElJU8__strongP8NSStringS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi14EU8__strongP8NSStringJS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi14ElJU8__strongP8NSStringS3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi15EU8__strongP8NSStringJS3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1E19SFBrowserWindowTypeJRU8__strongKP8NSStringEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1ERmJlU8__strongP8NSStringiEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1EU8__strongP6NSDataJmU8__strongP8NSStringEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1EU8__strongP8NSStringJS3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1EU8__strongP8NSStringJS3_S3_S3_ldibblbbS3_lS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1EU8__strongP8NSStringJS3_S3_ldibblbbS3_lS3_S3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1EU8__strongP8NSStringJS3_lll19SFBrowserWindowTypeS3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1EU8__strongP8NSStringJU8__strongP6NSDatamEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1ElJU8__strongP8NSStringRKlS3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi1ElJl19SFBrowserWindowTypeRlEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi2EU8__strongP6NSDataJmEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi2EU8__strongP8NSStringJRKlS3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi2EU8__strongP8NSStringJS3_S3_ldibblbbS3_lS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi2EU8__strongP8NSStringJS3_ldibblbbS3_lS3_S3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi2EU8__strongP8NSStringJlll19SFBrowserWindowTypeS3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi2ElJ19SFBrowserWindowTypeRlEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi2ElJU8__strongP8NSStringiEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi2EmJU8__strongP8NSStringEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi3E19SFBrowserWindowTypeJRlEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi3ERKlJU8__strongP8NSStringEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi3EU8__strongP8NSStringJS3_ldibblbbS3_lS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi3EU8__strongP8NSStringJiEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi3EU8__strongP8NSStringJldibblbbS3_lS3_S3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi3ElJll19SFBrowserWindowTypeU8__strongP8NSStringEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi4EU8__strongP8NSStringJldibblbbS3_lS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi4ElJdibblbbU8__strongP8NSStringlS3_S3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi4ElJl19SFBrowserWindowTypeU8__strongP8NSStringEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi5EdJibblbbU8__strongP8NSStringlS3_S3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi5ElJ19SFBrowserWindowTypeU8__strongP8NSStringEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi5ElJdibblbbU8__strongP8NSStringlS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi6E19SFBrowserWindowTypeJU8__strongP8NSStringEEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi6EdJibblbbU8__strongP8NSStringlS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi6EiJbblbbU8__strongP8NSStringlS3_S3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi7EbJblbbU8__strongP8NSStringlS3_S3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi7EiJbblbbU8__strongP8NSStringlS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi8EbJblbbU8__strongP8NSStringlS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi8EbJlbbU8__strongP8NSStringlS3_S3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi9EbJlbbU8__strongP8NSStringlS3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared36_WBSSQLiteStatementBindAllParametersILi9ElJbbU8__strongP8NSStringlS3_S3_S3_EEEvP18WBSSQLiteStatementOT0_DpOT1_
- __ZN12SafariShared39_WBSSQLiteDatabaseExecuteAndReturnErrorIJ19SFBrowserWindowTypeRU8__strongKP8NSStringEEEiP17WBSSQLiteDatabasePU15__autoreleasingP7NSErrorS3_DpOT_
- __ZN12SafariShared39_WBSSQLiteDatabaseExecuteAndReturnErrorIJEEEiP17WBSSQLiteDatabasePU15__autoreleasingP7NSErrorP8NSStringDpOT_
- __ZN12SafariShared39_WBSSQLiteDatabaseExecuteAndReturnErrorIJU8__strongP6NSDatamU8__strongP8NSStringEEEiP17WBSSQLiteDatabasePU15__autoreleasingP7NSErrorS5_DpOT_
- __ZN12SafariShared39_WBSSQLiteDatabaseExecuteAndReturnErrorIJU8__strongP8NSStringS3_EEEiP17WBSSQLiteDatabasePU15__autoreleasingP7NSErrorS2_DpOT_
- __ZN12SafariShared39_WBSSQLiteDatabaseExecuteAndReturnErrorIJU8__strongP8NSStringS3_S3_ldibblbbS3_lS3_S3_S3_EEEiP17WBSSQLiteDatabasePU15__autoreleasingP7NSErrorS2_DpOT_
- __ZN12SafariShared39_WBSSQLiteDatabaseExecuteAndReturnErrorIJU8__strongP8NSStringS3_lll19SFBrowserWindowTypeS3_EEEiP17WBSSQLiteDatabasePU15__autoreleasingP7NSErrorS2_DpOT_
- __ZN12SafariShared39_WBSSQLiteDatabaseExecuteAndReturnErrorIJlU8__strongP8NSStringRKlS3_EEEiP17WBSSQLiteDatabasePU15__autoreleasingP7NSErrorS2_DpOT_
- __ZN12SafariShared39_WBSSQLiteDatabaseExecuteAndReturnErrorIJll19SFBrowserWindowTypeRlEEEiP17WBSSQLiteDatabasePU15__autoreleasingP7NSErrorP8NSStringDpOT_
- __ZN14SafariServices25ArticleFinderJSControllerC2EP23WKWebProcessPlugInFrameP29WKWebProcessPlugInScriptWorld
- __ZN3WTF9RetainPtrIPK18__CTFontDescriptorED1Ev
- __ZZ47+[_SFBrowserSavedState sharedBrowserSavedState]E9onceToken
- __ZZL25safariTabStateDatabaseURLvE23browserStateDatabaseURL
- __ZZL28safariPPTTabStateDatabaseURLvE26browserStatePPTDatabaseURL
- ___103+[NSItemProvider(SafariServicesExtras) _sf_loadObjectsFromItemProviders:usingLoader:completionHandler:]_block_invoke
- ___103+[NSItemProvider(SafariServicesExtras) _sf_loadObjectsFromItemProviders:usingLoader:completionHandler:]_block_invoke_2
- ___103+[NSItemProvider(SafariServicesExtras) _sf_loadObjectsFromItemProviders:usingLoader:completionHandler:]_block_invoke_3
- ___103+[NSItemProvider(SafariServicesExtras) _sf_loadObjectsFromItemProviders:usingLoader:completionHandler:]_block_invoke_4
- ___103+[NSItemProvider(SafariServicesExtras) _sf_loadObjectsFromItemProviders:usingLoader:completionHandler:]_block_invoke_5
- ___115-[_SFWebAppServiceViewController webViewController:requestNotificationPermissionForSecurityOrigin:decisionHandler:]_block_invoke.142
- ___116-[SFContentBlockerManager(SFPrivate) loadDeclarativeNetRequestContentBlockerWithIdentifier:rules:completionHandler:]_block_invoke.128
- ___36+[_SFBrowserWindowSettings settings]_block_invoke
- ___39-[_SFBrowserWindowSettings synchronize]_block_invoke
- ___42-[SFBrowserStateSQLiteStore closeDatabase]_block_invoke
- ___42-[_SFDownload _importPlaceholderIfNeeded:]_block_invoke.123
- ___42-[_SFDownload _importPlaceholderIfNeeded:]_block_invoke.124
- ___42-[_SFDownload _importPlaceholderIfNeeded:]_block_invoke.124.cold.1
- ___42-[_SFDownload _importPlaceholderIfNeeded:]_block_invoke.125
- ___42-[_SFDownload _importPlaceholderIfNeeded:]_block_invoke.128
- ___42-[_SFDownload _importPlaceholderIfNeeded:]_block_invoke.128.cold.1
- ___43-[SFBrowserStateSQLiteStore browserWindows]_block_invoke
- ___43-[SFBrowserStateSQLiteStore updateSceneID:]_block_invoke
- ___44-[SFBrowserStateSQLiteStore mergeAllWindows]_block_invoke
- ___44-[SFBrowserStateSQLiteStore mergeAllWindows]_block_invoke.cold.1
- ___44-[SFBrowserStateSQLiteStore mergeAllWindows]_block_invoke.cold.2
- ___44-[SFBrowserStateSQLiteStore mergeAllWindows]_block_invoke.cold.3
- ___46-[_SFDownload _importCompleteDownloadIfNeeded]_block_invoke.134
- ___46-[_SFDownload _importCompleteDownloadIfNeeded]_block_invoke.135
- ___47+[_SFBrowserSavedState sharedBrowserSavedState]_block_invoke
- ___47+[_SFBrowserSavedState sharedBrowserSavedState]_block_invoke_2
- ___47-[_SFDownload removeDataAndPlaceholderFromDisk]_block_invoke.cold.1
- ___49-[SFBrowserStateSQLiteStore initWithDatabaseURL:]_block_invoke
- ___49-[SFBrowserStateSQLiteStore tabStateDataForUUID:]_block_invoke
- ___49-[SFWebAppDataProvider _createWebClipFromWebView]_block_invoke
- ___49-[_SFBrowserSavedState _historyItemsWereRemoved:]_block_invoke
- ___49-[_SFBrowserSavedState _historyItemsWereRemoved:]_block_invoke_2
- ___50-[SFBrowserStateSQLiteStore recentlyClosedWindows]_block_invoke
- ___50-[SFBrowserStateSQLiteStore removeTabWithTabData:]_block_invoke
- ___50-[SFBrowserStateSQLiteStore removeTabWithTabData:]_block_invoke.cold.1
- ___52-[SFBrowserStateSQLiteStore checkPointWriteAheadLog]_block_invoke
- ___52-[SFBrowserStateSQLiteStore checkPointWriteAheadLog]_block_invoke.cold.1
- ___52-[SFBrowserStateSQLiteStore setSecureDeleteEnabled:]_block_invoke
- ___52-[SFWebAppDataProvider webView:didFinishNavigation:]_block_invoke
- ___53-[SFBrowserStateSQLiteStore _mergeAllWindowsIfNeeded]_block_invoke
- ___53-[SFBrowserStateSQLiteStore _mergeAllWindowsIfNeeded]_block_invoke.132
- ___53-[SFBrowserStateSQLiteStore _mergeAllWindowsIfNeeded]_block_invoke_2
- ___53-[SFBrowserStateSQLiteStore _migrateToSchemaVersion:]_block_invoke
- ___53-[SFBrowserStateSQLiteStore _migrateToSchemaVersion:]_block_invoke.cold.1
- ___53-[SFBrowserStateSQLiteStore _updateTabStateWithData:]_block_invoke
- ___53-[_SFDownload _didImportFileAtURL:completionHandler:]_block_invoke.136
- ___53-[_SFDownload _didImportFileAtURL:completionHandler:]_block_invoke.136.cold.1
- ___53-[_SFDownload _didImportFileAtURL:completionHandler:]_block_invoke.137
- ___55-[SFBrowserStateSQLiteStore _cacheUUIDForTabStateData:]_block_invoke
- ___55-[SFBrowserStateSQLiteStore updateTabWithTabStateData:]_block_invoke
- ___56-[SFBrowserStateSQLiteStore saveTabStateWithDictionary:]_block_invoke
- ___60-[SFBrowserStateSQLiteStore tabStatesWithBrowserWindowUUID:]_block_invoke
- ___60-[SFBrowserStateSQLiteStore tabStatesWithBrowserWindowUUID:]_block_invoke_2
- ___60-[_SFBrowserWindowSettings validateWindowSettingsWithUUIDs:]_block_invoke
- ___61-[_SFAccountManagerViewController _autoFillCellForTableView:]_block_invoke
- ___62-[SFBrowserStateSQLiteStore updateBrowserWindowWithData:tabs:]_block_invoke
- ___63+[NSBundle(SafariServicesExtras) _sf_isSafariViewServiceBundle]_block_invoke
- ___63-[SFBrowserStateSQLiteStore _updateBrowserWindowWithData:tabs:]_block_invoke
- ___63-[SFBrowserStateSQLiteStore _updateBrowserWindowWithData:tabs:]_block_invoke.cold.1
- ___65-[_SFBrowserWindowSettings _initializeSettingsDictionaryIfNeeded]_block_invoke
- ___67-[SFBrowserStateSQLiteStore regenerateTabUUIDsForDeviceRestoration]_block_invoke
- ___67-[SFContentBlockerManager(SFPrivate) _beginContentBlockerDiscovery]_block_invoke.111
- ___67-[SFPasswordSavingServiceViewController showPromptWithToken:style:]_block_invoke.117
- ___67-[_SFBrowserSavedState recentlyClosedTabsForProfileWithIdentifier:]_block_invoke
- ___69-[SFBrowserStateSQLiteStore _updateBrowserWindowStateWithDictionary:]_block_invoke
- ___69-[SFBrowserStateSQLiteStore _updateBrowserWindowStateWithDictionary:]_block_invoke.202
- ___69-[SFBrowserStateSQLiteStore _updateBrowserWindowStateWithDictionary:]_block_invoke_2
- ___69-[SFBrowserStateSQLiteStore _updateBrowserWindowStateWithDictionary:]_block_invoke_2.206
- ___69-[SFBrowserStateSQLiteStore _updateBrowserWindowStateWithDictionary:]_block_invoke_3
- ___69-[_SFPasswordAuditingViewController _reloadSavedAccountsForceUpdate:]_block_invoke.82
- ___69-[_SFPasswordAuditingViewController _reloadSavedAccountsForceUpdate:]_block_invoke.84
- ___69-[_SFPasswordAuditingViewController _reloadSavedAccountsForceUpdate:]_block_invoke.86
- ___69-[_SFPasswordAuditingViewController _reloadSavedAccountsForceUpdate:]_block_invoke_2.89
- ___70+[NSString(SafariServicesExtras) _sf_safeBrowsingPreferencesPlistPath]_block_invoke
- ___71-[SFBrowserStateSQLiteStore deleteSavedStatesForProfileWithIdentifier:]_block_invoke
- ___71-[SFPrivacyReportTrackerDetailViewController traitCollectionDidChange:]_block_invoke
- ___71-[_SFBrowserSavedState loadSessionStateDataAndRemoveRecentlyClosedTab:]_block_invoke
- ___71-[_SFFormAutoFillController didCollectURLsForPreFilling:atURL:inFrame:]_block_invoke.196
- ___71-[_SFFormAutoFillController didCollectURLsForPreFilling:atURL:inFrame:]_block_invoke_2.197
- ___71-[_SFFormAutoFillController didCollectURLsForPreFilling:atURL:inFrame:]_block_invoke_3.203
- ___72-[_SFBrowserSavedState clearRecentlyClosedTabsForProfileWithIdentifier:]_block_invoke
- ___72-[_SFWebAppServiceViewController processWebPushForWebAppWithIdentifier:]_block_invoke.254
- ___73-[_SFAccountPickerTableViewController tableView:didSelectRowAtIndexPath:]_block_invoke.157
- ___73-[_SFAuthenticationContext _evaluatePolicyForClient:userInitiated:reply:]_block_invoke.66
- ___73-[_SFAuthenticationContext _evaluatePolicyForClient:userInitiated:reply:]_block_invoke_2.67
- ___75-[SFBrowserStateSQLiteStore readSavedSessionStateDataForTabWithUUIDString:]_block_invoke
- ___75-[SFBrowserStateSQLiteStore readTabStatesWithBrowserWindowUUID:completion:]_block_invoke
- ___75-[SFContentBlockerManager(SFPrivate) setExtension:isEnabled:byUserGesture:]_block_invoke.122
- ___75-[SFContentBlockerManager(SFPrivate) setExtension:isEnabled:byUserGesture:]_block_invoke.122.cold.1
- ___75-[_SFWebAppServiceViewController clearWebViewAndWebsiteDataWithCompletion:]_block_invoke.123
- ___78-[SFBrowserStateSQLiteStore deleteRecentlyClosedWindowsWithProfileIdentifier:]_block_invoke
- ___79-[SFBrowserStateSQLiteStore removeSavedSessionStateDataForTabsWithUUIDStrings:]_block_invoke
- ___79-[SFBrowserStateSQLiteStore updateBrowserWindowStateWithDictionary:completion:]_block_invoke
- ___79-[SFContentBlockerManager(SFPrivate) _recompileEnabledContentBlockersIfNeeded:]_block_invoke.119
- ___79-[SFContentBlockerManager(SFPrivate) _recompileEnabledContentBlockersIfNeeded:]_block_invoke.119.cold.1
- ___81-[SFBrowserStateSQLiteStore deleteTabStateWithBrowserWindowUUID:andRemoveWindow:]_block_invoke
- ___82-[NSItemProvider(SafariServicesExtras) _sf_loadObjectOfClasses:completionHandler:]_block_invoke
- ___82-[NSItemProvider(SafariServicesExtras) _sf_loadObjectOfClasses:completionHandler:]_block_invoke.cold.1
- ___82-[NSItemProvider(SafariServicesExtras) _sf_loadObjectOfClasses:completionHandler:]_block_invoke.cold.2
- ___82-[_SFDownload _download:decideDestinationWithSuggestedFilename:completionHandler:]_block_invoke.212
- ___82-[_SFDownload _download:decideDestinationWithSuggestedFilename:completionHandler:]_block_invoke.212.cold.1
- ___89+[_SFFormAutoFillController _getExternalLoginCredentialSuggestionsForDomains:completion:]_block_invoke
- ___93-[SFMoveAccountsToGroupPickerViewController _checkReusedPasswordsAndPresentAlertIfNecessary:]_block_invoke.52
- ___93-[SFMoveAccountsToGroupPickerViewController _checkReusedPasswordsAndPresentAlertIfNecessary:]_block_invoke.cold.1
- ___93-[SFMoveAccountsToGroupPickerViewController _checkReusedPasswordsAndPresentAlertIfNecessary:]_block_invoke_3
- ___93-[SFMoveAccountsToGroupPickerViewController _checkReusedPasswordsAndPresentAlertIfNecessary:]_block_invoke_4
- ___97+[_SFFormAutoFillController _getExternalLoginCredentialSuggestionsForDomains:pageURL:completion:]_block_invoke
- ___Block_byref_object_copy_.194
- ___Block_byref_object_dispose_.195
- ___WBS_LOG_CHANNEL_PREFIXItemProvider_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXStatePersistence_block_invoke
- ___block_descriptor_32_e27_v16?0"WKContentRuleList"8l
- ___block_descriptor_32_e31_"NSURL"16?0"WBSHistoryItem"8l
- ___block_descriptor_32_e34_"NSString"16?0"SFTabStateData"8l
- ___block_descriptor_32_e38_"SFTabStateData"16?0"NSDictionary"8l
- ___block_descriptor_32_e45_"NSNumber"16?0"_SFBrowserWindowStateData"8l
- ___block_descriptor_40_e27_"_SFBrowserSavedState"8?0l
- ___block_descriptor_40_e8_32bs_e45_v24?0"<NSItemProviderReading>"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32s_e11_v24?08Q16ls32l8
- ___block_descriptor_40_e8_32s_e16_B16?0"NSUUID"8ls32l8
- ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
- ___block_descriptor_40_ea8_32s_e22_B24?0"NSString"8^B16ls32l8
- ___block_descriptor_40_ea8_32s_e22_v20?0B8"LAContext"12ls32l8
- ___block_descriptor_40_ea8_32s_e22_v24?0"NSString"8^B16ls32l8
- ___block_descriptor_40_ea8_32s_e24_B16?0"SFTabStateData"8ls32l8
- ___block_descriptor_40_ea8_32s_e31_B32?0"SFTabStateData"8Q16^B24ls32l8
- ___block_descriptor_40_ea8_32s_e39_v32?0"NSString"8"NSMutableSet"16^B24ls32l8
- ___block_descriptor_48_e8_32s40r_e28_B16?0"WBSPasswordWarning"8lr40l8s32l8
- ___block_descriptor_48_ea8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_48_ea8_32s40s_e24_B16?0"SFTabStateData"8ls32l8s40l8
- ___block_descriptor_48_ea8_32s40s_e5_i8?0ls32l8s40l8
- ___block_descriptor_48_ea8_32s_e31_v32?0"SFTabStateData"8Q16^B24ls32l8
- ___block_descriptor_48_ea8_32s_e5_v8?0ls32l8
- ___block_descriptor_49_e8_32s40s_e32_v16?0"_SFSettingsAlertButton"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e31_v32?0"NSItemProvider"8Q16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e8_v16?08ls40l8s32l8
- ___block_descriptor_56_e8_32s40s48r_e23_v16?0"UIAlertAction"8ls32l8s40l8r48l8
- ___block_descriptor_56_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_ea8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_56_ea8_32s40s_e31_v32?0"SFTabStateData"8Q16^B24ls32l8s40l8
- ___block_descriptor_56_ea8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_57_ea8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_64_ea8_32s40s48s56r_e25_v32?0"NSNumber"8Q16^B24ls32l8s40l8s48l8r56l8
- ___block_descriptor_64_ea8_32s40s48s56r_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8s48l8r56l8
- ___block_descriptor_72_e8_32s40bs48r56r64w_e29_v24?0"NSArray"8"NSError"16ls40l8w64l8r48l8r56l8s32l8
- ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0lr56l8s48l8r64l8s32l8s40l8
- ___block_literal_global.101
- ___block_literal_global.106
- ___block_literal_global.114
- ___block_literal_global.120
- ___block_literal_global.161
- ___block_literal_global.192
- ___block_literal_global.200
- ___block_literal_global.204
- ___block_literal_global.205
- ___block_literal_global.228
- ___block_literal_global.23
- ___block_literal_global.250
- ___block_literal_global.263
- ___block_literal_global.315
- ___block_literal_global.433
- ___block_literal_global.437
- ___block_literal_global.486
- ___block_literal_global.49
- ___block_literal_global.491
- ___block_literal_global.494
- ___block_literal_global.498
- ___block_literal_global.6
- ___block_literal_global.86
- ___block_literal_global.92
- __sf_isSafariViewServiceBundle.isSafariViewService
- __sf_isSafariViewServiceBundle.onceToken
- __sf_safeBrowsingPreferencesPlistPath.onceToken
- __sf_safeBrowsingPreferencesPlistPath.safeBrowsingPreferencesPlistPath
- __unnamed_array_storage.62
- __unnamed_array_storage.67
- __unnamed_array_storage.72
- __unnamed_array_storage.77
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_msgSend$_addLegacySearch:
- _objc_msgSend$_autoFillCellForTableView:
- _objc_msgSend$_blankSnapshotKeyForPrivateBrowsing:syncableTabGroupUUID:
- _objc_msgSend$_boolValueForKey:windowUUID:
- _objc_msgSend$_cacheUUIDForTabStateData:
- _objc_msgSend$_checkDatabaseIntegrity
- _objc_msgSend$_checkPointWriteAheadLogIfNeeded
- _objc_msgSend$_closeDatabase
- _objc_msgSend$_createFreshDatabaseSchema
- _objc_msgSend$_createTableForTabSession
- _objc_msgSend$_createTableForTabs
- _objc_msgSend$_createWebClipFromWebView
- _objc_msgSend$_createWebView
- _objc_msgSend$_databaseIDForBrowserWindow:
- _objc_msgSend$_finishPreparingFromWebView
- _objc_msgSend$_getExternalLoginCredentialSuggestionsForDomains:completion:
- _objc_msgSend$_getExternalLoginCredentialSuggestionsForDomains:pageURL:completion:
- _objc_msgSend$_initializeSettingsDictionaryIfNeeded
- _objc_msgSend$_insertTabStateWithData:
- _objc_msgSend$_isDatabaseOpen
- _objc_msgSend$_isTabStateCached:
- _objc_msgSend$_mergeAllWindowsIfNeeded
- _objc_msgSend$_migrateFromLegacyPlistIfNeeded
- _objc_msgSend$_migrateFromLegacyPlistWithPath:
- _objc_msgSend$_migrateToCurrentSchemaVersionIfNeeded
- _objc_msgSend$_migrateToSchemaVersion:
- _objc_msgSend$_migrateToSchemaVersion_2
- _objc_msgSend$_migrateToSchemaVersion_3
- _objc_msgSend$_migrateToSchemaVersion_4
- _objc_msgSend$_migrateToSchemaVersion_5
- _objc_msgSend$_migrateToSchemaVersion_6
- _objc_msgSend$_migrateToSchemaVersion_7
- _objc_msgSend$_migrateToSchemaVersion_8
- _objc_msgSend$_notifyThatRecentlyClosedTabsWereRemoved:
- _objc_msgSend$_numberForKey:windowUUID:
- _objc_msgSend$_openDatabaseAndCheckIntegrity:
- _objc_msgSend$_readBrowserControllersSavedState
- _objc_msgSend$_readRecentlyClosedTabsStateIfNecessary
- _objc_msgSend$_readSavedSessionStateDataForTabWithUUIDString:
- _objc_msgSend$_readTabStatesWithBrowserWindowUUID:completion:
- _objc_msgSend$_recoverFromDatabaseInconsistencyFromSchemaVersion3Migration
- _objc_msgSend$_regenerateTabUUIDsForDeviceRestoration
- _objc_msgSend$_removeLegacyRecentSearchesData
- _objc_msgSend$_removeRecentlyClosedTabStateData:
- _objc_msgSend$_removeSavedSessionStateDataForTabsWithUUIDStrings:
- _objc_msgSend$_saveBrowserWindowStateWithData:
- _objc_msgSend$_saveBrowserWindowStateWithDictionary:
- _objc_msgSend$_schemaVersion
- _objc_msgSend$_selectionEffect
- _objc_msgSend$_setBool:forKey:windowUUID:
- _objc_msgSend$_setDatabaseID:browserWindow:
- _objc_msgSend$_setDatabaseSchemaVersion:
- _objc_msgSend$_setString:forKey:windowUUID:
- _objc_msgSend$_sf_accessingSecurityScopedResource:
- _objc_msgSend$_sf_ensurePathExtension:
- _objc_msgSend$_sf_highLevelDomainFromHostFallingBackToHostOrAbsoluteString
- _objc_msgSend$_sf_isAppleOneURL
- _objc_msgSend$_sf_isSafariViewServiceBundle
- _objc_msgSend$_sf_loadObjectOfClasses:completionHandler:
- _objc_msgSend$_sf_loadObjectsFromItemProviders:usingLoader:completionHandler:
- _objc_msgSend$_sf_topLevelDomain
- _objc_msgSend$_sqliteStatementForTabDeleting
- _objc_msgSend$_stringForKey:windowUUID:
- _objc_msgSend$_synchronizeNow
- _objc_msgSend$_tabStateDataForUUID:
- _objc_msgSend$_tabUUIDsInWindow:
- _objc_msgSend$_updateBrowserWindowStateWithDictionary:
- _objc_msgSend$_updateBrowserWindowWithData:tabs:
- _objc_msgSend$_updateOrInsertTabStateWithData:
- _objc_msgSend$_updateTabStateWithData:
- _objc_msgSend$_vacuum
- _objc_msgSend$acceptedMIMETypes
- _objc_msgSend$activeDocumentIndex
- _objc_msgSend$activeDocumentIsValidForWindowWithUUID:
- _objc_msgSend$activePrivateDocumentIndex
- _objc_msgSend$activeProfileIdentifier
- _objc_msgSend$authenticatorDialogForPanel:dialogController:
- _objc_msgSend$bindData:atParameterIndex:
- _objc_msgSend$bindDouble:atParameterIndex:
- _objc_msgSend$bindInt64:atParameterIndex:
- _objc_msgSend$bindInt:atParameterIndex:
- _objc_msgSend$bindString:atParameterIndex:
- _objc_msgSend$boolAtIndex:
- _objc_msgSend$browserWindows
- _objc_msgSend$checkPointWriteAheadLog
- _objc_msgSend$checkpointWriteAheadLogWithLogFrameCount:checkpointedFrameCount:
- _objc_msgSend$close
- _objc_msgSend$closeDatabase
- _objc_msgSend$color
- _objc_msgSend$compare:options:
- _objc_msgSend$currentOneTimeCodesForWebBrowserWithWebsiteFrameURLs:fieldClassification:
- _objc_msgSend$dataAtIndex:
- _objc_msgSend$dataWithContentsOfURL:options:error:
- _objc_msgSend$databaseID
- _objc_msgSend$decidePolicyForLocalAuthenticatorWithCompletionHandler:
- _objc_msgSend$defaultBrowserStateDatabase
- _objc_msgSend$deleteRecentlyClosedWindowsWithProfileIdentifier:
- _objc_msgSend$deleteSavedStatesForProfileWithIdentifier:
- _objc_msgSend$deleteTabStateWithBrowserWindowUUID:andRemoveWindow:
- _objc_msgSend$execute
- _objc_msgSend$fetch
- _objc_msgSend$fetchQuery:
- _objc_msgSend$fragment
- _objc_msgSend$handleAutoFillDrillInForEditableSavedAccountTableViewController:
- _objc_msgSend$hasDifferentColorAppearanceComparedToTraitCollection:
- _objc_msgSend$inMemoryDatabase
- _objc_msgSend$inMemoryDatabaseURL
- _objc_msgSend$initWithDatabase:query:
- _objc_msgSend$initWithDatabase:query:error:
- _objc_msgSend$initWithDatabaseURL:
- _objc_msgSend$initWithDictionaryRepresentation:
- _objc_msgSend$initWithSQLiteRow:
- _objc_msgSend$initWithSavedAccount:warning:searchPattern:savedAccountIsOnlySavedAccountForHighLevelDomain:
- _objc_msgSend$initWithURL:queue:
- _objc_msgSend$initWithUUIDString:sceneID:
- _objc_msgSend$intAtIndex:
- _objc_msgSend$isParsecABTestingEnabled
- _objc_msgSend$lastErrorMessage
- _objc_msgSend$lastInsertRowID
- _objc_msgSend$lastResultCode
- _objc_msgSend$lastViewedTime
- _objc_msgSend$launchedToTest
- _objc_msgSend$legacyPlistFileVersion
- _objc_msgSend$loadObjectOfClass:completionHandler:
- _objc_msgSend$mergeAllWindows
- _objc_msgSend$needsQuickUpdate
- _objc_msgSend$nonPersistentDataStore
- _objc_msgSend$numberFromString:
- _objc_msgSend$numberOfSavedAccountsForHighLevelDomain:
- _objc_msgSend$openWithAccessType:error:
- _objc_msgSend$orderIndex
- _objc_msgSend$owningBrowserWindowDatabaseID
- _objc_msgSend$owningBrowserWindowUUIDString
- _objc_msgSend$panel
- _objc_msgSend$parsecABGroupIdentifier
- _objc_msgSend$passwordOptionsViewController:
- _objc_msgSend$prepareWithURL:
- _objc_msgSend$presentedAuthenticatorDialog
- _objc_msgSend$privateBrowsing
- _objc_msgSend$profileIdentifier
- _objc_msgSend$rangeOfCharacterFromSet:options:
- _objc_msgSend$readSavedSessionStateDataForTabWithUUIDString:
- _objc_msgSend$readerViewTopScrollOffset
- _objc_msgSend$readingListBookmarkID
- _objc_msgSend$recentlyClosedWindows
- _objc_msgSend$regenerateTabUUIDsForDeviceRestoration
- _objc_msgSend$removeObjectsInArray:
- _objc_msgSend$removeSavedSessionStateDataForTabsWithUUIDStrings:
- _objc_msgSend$removeTabStateWithTabData:
- _objc_msgSend$removeTabWithTabData:
- _objc_msgSend$removeTabsStateForBrowserControllerWithUUID:andRemoveWindow:
- _objc_msgSend$removeWindowWithUUID:
- _objc_msgSend$replaceOccurrencesOfString:withString:options:range:
- _objc_msgSend$reportErrorWithCode:statement:error:
- _objc_msgSend$requestPINWithRemainingRetries:completionHandler:
- _objc_msgSend$sceneID
- _objc_msgSend$selectAssertionResponse:source:completionHandler:
- _objc_msgSend$sessionStateData
- _objc_msgSend$setActiveDocumentIsValid:forWindowWithUUID:
- _objc_msgSend$setCredential:forProtectionSpace:
- _objc_msgSend$setDatabaseID:
- _objc_msgSend$setInspectable:
- _objc_msgSend$setIsForUpdateOnly:
- _objc_msgSend$setNeedsQuickUpdate:
- _objc_msgSend$setOwningBrowserWindowDatabaseID:
- _objc_msgSend$setOwningBrowserWindowUUIDString:
- _objc_msgSend$setSceneID:
- _objc_msgSend$setSecureDeleteEnabled:
- _objc_msgSend$setSessionStateData:
- _objc_msgSend$setShouldTakeUIBackgroundAssertion:
- _objc_msgSend$setUUIDString:
- _objc_msgSend$settings
- _objc_msgSend$sf_URLScheme
- _objc_msgSend$sf_absoluteStringWithoutFragment
- _objc_msgSend$sf_isAppleNewsURL
- _objc_msgSend$sf_isConfigProfileMIMEType
- _objc_msgSend$sf_isFeedScheme
- _objc_msgSend$sf_isWebSearchURL
- _objc_msgSend$sf_stringByReplacingLastOccurrenceOfWhitespaceWithANonBreakingSpace
- _objc_msgSend$sf_stringByReplacingMarkupCharactersWithHTMLEntities
- _objc_msgSend$shouldMergeAllWindowsIfNeeded
- _objc_msgSend$showingReader
- _objc_msgSend$skipSavingSessionState
- _objc_msgSend$skipUpdate
- _objc_msgSend$statement
- _objc_msgSend$stringAtIndex:
- _objc_msgSend$stringByAppendingPathExtension:
- _objc_msgSend$stringByReplacingCharactersInRange:withString:
- _objc_msgSend$subtitleFontForNarrowCell
- _objc_msgSend$tabGroupUUID
- _objc_msgSend$tabStateDataForUUID:
- _objc_msgSend$tabStatesWithBrowserWindowUUID:
- _objc_msgSend$uncompressedDataWithRawData:uncompressedSize:
- _objc_msgSend$uncompressedSessionStateDataSize
- _objc_msgSend$updateBrowserWindowState:tabs:
- _objc_msgSend$updateBrowserWindowStateWithDictionary:completion:
- _objc_msgSend$updateBrowserWindowWithData:tabs:
- _objc_msgSend$updateSceneID:
- _objc_msgSend$updateTabWithTabStateData:
- _objc_msgSend$updateWebAuthenticationPanel:
- _objc_msgSend$userVisibleURL
- _objc_msgSend$wasOpenedFromLink
- _settings.onceToken
- _sharedSettingsInstance
- _sqlite3_create_function_v2
- _sqlite3_result_text
CStrings:
+ "\x02\xf0\xf1"
+ "\x04\x12"
+ "\t3!\x14!\x11\x1f!\x13\x11\x14\x15C"
+ "\r\x12\x14\x12\x11\x11#\x15!"
+ "%\x17"
+ "@\"<_SFFormAutoFillTestController>\""
+ "@\"WBSSavedAccount\"16@?0@\"WBSPasswordWarning\"8"
+ "@48@0:8@16@24@32B40B44"
+ "Background task expired while waiting to delete web app data"
+ "Error loading password warnings. %{public}@"
+ "Failed to clean up staged cookies, URL: %@, error: %{public}@"
+ "Failed to consume sandbox extension, Sandbox Extension %@, errno = %d"
+ "Failed to copy cookies into temporary directory"
+ "Failed to copy staged cookies into webClip's directory %@"
+ "Failed to issue sandbox extension token for copying cookies, errno = %d"
+ "Failed to remove stageCookies at URL %@"
+ "PasswordsIcons"
+ "Received invalid paths to copy cookies from: %{public}@ to: %{public}@, for web clip with identifier: %{public}@"
+ "StagedCookies"
+ "T@\"<_SFFormAutoFillTestController>\",W,N,V_testController"
+ "T@\"NSString\",&,N,V_initialSearchQuery"
+ "T@\"WBSSavedAccount\",&,N,V_savedAccountToInitiallyShowDetailsFor"
+ "TB,N,V_shouldShowReusedPasswordWarning"
+ "_barMetricTraitsDidChange"
+ "_canUserDeleteSavedAccount"
+ "_cellDataFromSavedAccounts:"
+ "_copyCurrentCookiesToStagingDirectory"
+ "_excessiveLineHeightCharacterSet"
+ "_getExternalLoginCredentialSuggestionsForDomains:pageURL:webFrameIdentifier:completion:"
+ "_getExternalLoginCredentialSuggestionsForDomains:webFrameIdentifier:completion:"
+ "_groupPickerMenuButton"
+ "_indexPathForSavedAccount:"
+ "_initialSearchQuery"
+ "_isPresentedAsSheet"
+ "_issueReadOnlySandboxExtensionForURL:"
+ "_layoutReusedPasswordWarningImageViewIfNecessary"
+ "_loadReusedPasswords"
+ "_notifyServiceOfUpdatedTintColors"
+ "_passwordOptionsCellForTableView:"
+ "_preferredContentSizeCategoryDidChange"
+ "_rememberStateForSystemAutoFillWithSearchQuery:savedAccount:"
+ "_removeStageCookiesDirectoryIfNeeded"
+ "_restoreStateForSystemAutoFillToAccountPickerConfiguration:"
+ "_reusedPasswordWarningImageView"
+ "_reusedPasswords"
+ "_savedAccountToInitiallyShowDetailsFor"
+ "_sf_stagedCookiesURL"
+ "_sharedQueue"
+ "_shouldRestoreStateForSystemAutoFillForAppID:"
+ "_shouldShowReusedPasswordWarning"
+ "_showAccountDetailsForSavedAccount:"
+ "_stagedCookiesDirectoryURL"
+ "_testController"
+ "_updateHeaderSizeForTraitChanges"
+ "abGroupIdentifier"
+ "accountCellDataWithSavedAccount:warning:searchPattern:savedAccountIsOnlySavedAccountForHighLevelDomain:shouldShowReusedPasswordWarning:"
+ "authenticationPolicy"
+ "autoFillController:didCollectFormMetadataForTesting:forURL:"
+ "autoFillControllerShouldCollectFormMetadataForTesting:"
+ "autoFillDidInsertWithExplicitInvocationMode:"
+ "collectFormMetadataForTesting"
+ "collectFormMetadataForTestingAtURL:"
+ "com.apple.SafariViewService.deleteWebAppData"
+ "com.apple.mobilesafari.RemoveDownload"
+ "com.apple.mobilesafari.RemoveDownloadPlaceholder"
+ "com.apple.mobilesafari.SFDownloadFileQueue"
+ "copyCookiesFromFolderAtURL:intoDataStore:"
+ "copyCookiesFromWebView:intoFolderAtURL:completionHandler:"
+ "copyItemAtURL:toURL:error:"
+ "currentOneTimeCodesForWebBrowserWithWebsiteFrameURLs:fieldClassification:inContext:"
+ "didCopyStagedCookiesToURL:sandboxExtensionToken:"
+ "fetchAllCredentialIdentitiesMatchingDomains:completion:"
+ "finishedAutoFillingOneTimeCode:inFrame:shouldSubmit:"
+ "initWithSavedAccount:warning:searchPattern:savedAccountIsOnlySavedAccountForHighLevelDomain:shouldShowReusedPasswordWarning:"
+ "initialSearchQuery"
+ "isABTestingEnabled"
+ "makePasswordOptionsViewController"
+ "numberOfSavedAccountsInPersonalKeychainForHighLevelDomain:"
+ "passwordOptionsDrillIn"
+ "rangeOfCharacterFromSet:"
+ "reconfiguredItemIdentifiers"
+ "registerForTraitChanges:withTarget:action:"
+ "safari_absoluteStringWithoutFragment"
+ "safari_accessingSecurityScopedResource:"
+ "safari_ensurePathExtension:"
+ "safari_hasFeedScheme"
+ "safari_highLevelDomainFromHostFallingBackToHostOrAbsoluteString"
+ "safari_isAppleNewsURL"
+ "safari_isAppleOneURL"
+ "safari_isConfigProfileMIMEType"
+ "safari_isSafariViewServiceBundle"
+ "safari_isXWebSearchURL"
+ "safari_loadObjectOfClasses:completionHandler:"
+ "safari_loadObjectsFromItemProviders:usingLoader:completionHandler:"
+ "safari_monospacedDigitFontForTextStyle:"
+ "safari_stringByReplacingLastOccurrenceOfWhitespaceWithANonBreakingSpace"
+ "safari_stringByReplacingMarkupCharactersWithHTMLEntities"
+ "safari_topLevelDomain"
+ "safari_traitsAffectingTextAppearance"
+ "safari_userVisibleScheme"
+ "savedAccountToInitiallyShowDetailsFor"
+ "setInitialSearchQuery:"
+ "setIsAccessibilityElement:"
+ "setNeedsUpdatePreferredContentSize"
+ "setSavedAccount:searchPattern:emphasizeUserName:isReusedPassword:"
+ "setSavedAccountToInitiallyShowDetailsFor:"
+ "setShouldShowReusedPasswordWarning:"
+ "setTestController:"
+ "setWithSet:"
+ "shouldShowReusedPasswordWarning"
+ "subtitleFontForNarrowCellWithText:"
+ "systemYellowColor"
+ "temporaryDirectory"
+ "testController"
+ "timeIntervalSinceReferenceDate"
+ "updateAllSavedAccountsWithPasswordsWithUser:protectionSpace:withNewPassword:"
+ "updateSelectionEffect"
+ "updateWithStagedCookiesDirectoryURL:sandboxExtensionToken:"
+ "userInterfaceStyleDidChange"
+ "\xf0ѱ"
+ "\xf0\xf0\xf0\xf0A"
- "\x02\x11\x11"
- "\v ."
- "\v3!\x14!\x11\x1a\x17!\x13\x11%C"
- "\r\x12\x14\x12\x111#%!"
- "\"A"
- "%\x15"
- "&"
- "&#x27;"
- "&#x2F;"
- "&amp;"
- "&gt;"
- "&lt;"
- "&nbsp;"
- "&quot;"
- "'"
- "', '"
- "+[_SFBrowserSavedState setSharedBrowserSavedState:]"
- "/Library/Caches/com.apple.xbs/Sources/SafariServices/iOS/MobileSafari/SafariServices/_SFBrowserSavedState.mm"
- "/Library/Safari/SuspendState.plist"
- "<"
- "<%@:%p; UUID = %@; sceneID = %@>"
- "@\"NSNumber\"16@?0@\"_SFBrowserWindowStateData\"8"
- "@\"NSString\"16@?0@\"SFTabStateData\"8"
- "@\"NSURL\"16@?0@\"WBSHistoryItem\"8"
- "@\"SFAccountManagerDrillInTableViewCellWithTrailingNumber\""
- "@\"SFBrowserStateSQLiteStore\""
- "@\"SFTabStateData\"16@?0@\"NSDictionary\"8"
- "@\"WBSSQLiteDatabase\""
- "@\"WBSSQLiteStatement\""
- "@\"_SFBrowserSavedState\"8@?0"
- "ALTER TABLE browser_windows ADD COLUMN active_profile_identifier TEXT NOT NULL DEFAULT ''"
- "ALTER TABLE browser_windows ADD COLUMN scene_id TEXT"
- "ALTER TABLE tab_sessions RENAME TO tab_sessions_old"
- "ALTER TABLE tabs ADD COLUMN profile_uuid TEXT NOT NULL DEFAULT ''"
- "ALTER TABLE tabs ADD COLUMN tab_group_uuid TEXT NOT NULL DEFAULT ''"
- "ALTER TABLE tabs ADD COLUMN uncompressed_session_data_size INTEGER NOT NULL DEFAULT 0"
- "ALTER TABLE tabs RENAME TO tabs_old"
- "ActiveDocumentIsValid"
- "B16@?0@\"NSUUID\"8"
- "B16@?0@\"SFTabStateData\"8"
- "B24@?0@\"NSString\"8^B16"
- "B32@?0@\"SFTabStateData\"8Q16^B24"
- "BEGIN"
- "BEGIN TRANSACTION"
- "BrowserControllersSavedState"
- "BrowserState SQLite schema version (%d) does not match our supported schema version (%d) in store at %{public}@"
- "BrowserState.db"
- "BrowserStatePPT.db"
- "COMMIT"
- "COMMIT TRANSACTION"
- "CREATE INDEX tab_sessions__uuid ON tab_sessions (tab_uuid)"
- "CREATE INDEX tabs__uuid ON tabs (uuid)"
- "CREATE TABLE browser_windows (id INTEGER PRIMARY KEY AUTOINCREMENT,uuid TEXT NOT NULL,type INTEGER DEFAULT 0,active_document_index INTEGER DEFAULT 0,active_private_document_index INTEGER DEFAULT 0,active_document_is_valid BOOL DEFAULT 1,tab_state_successfully_loaded BOOL DEFAULT 0,legacy_plist_file_version INTEGER DEFAULT 0,scene_ID TEXT,active_profile_identifier TEXT NOT NULL DEFAULT '',CONSTRAINT uuid_type_index UNIQUE(uuid, type))"
- "CREATE TABLE tab_sessions (id INTEGER PRIMARY KEY AUTOINCREMENT,tab_uuid TEXT NOT NULL UNIQUE,session_data BLOB DEFAULT NULL,uncompressed_session_data_size INTEGER NOT NULL DEFAULT 0,FOREIGN KEY(tab_uuid) REFERENCES tabs(uuid) ON DELETE CASCADE ON UPDATE CASCADE)"
- "CREATE TABLE tabs (id INTEGER PRIMARY KEY AUTOINCREMENT,uuid TEXT NOT NULL UNIQUE,title TEXT,url TEXT COLLATE NOCASE,user_visible_url TEXT COLLATE NOCASE,order_index INTEGER NOT NULL,last_viewed_time REAL DEFAULT NULL,readinglist_bookmark_id INTEGER DEFAULT 0,opened_from_link BOOL DEFAULT 0,showing_reader BOOL DEFAULT 0,reader_view_top_scroll_offset INTEGER DEFAULT 0,private_browsing BOOL DEFAULT 0,displaying_standalone_image BOOL DEFAULT 0,browser_window_uuid TEXT NOT NULL,browser_window_id INTEGER NOT NULL,tab_group_uuid TEXT NOT NULL DEFAULT '',profile_uuid TEXT NOT NULL DEFAULT '',FOREIGN KEY(browser_window_id) REFERENCES browser_windows(id) ON DELETE CASCADE)"
- "Can't create Web Clip: web view failed to load with error: %@"
- "Checkpointed write ahead log. Log frame count: %d, checkpointed frame count: %d"
- "Content is corrupted in SuspendState.plist at %{public}@"
- "Could not load item: %{public}@"
- "DELETE FROM browser_windows WHERE active_profile_identifier = ?"
- "DELETE FROM browser_windows WHERE id = ?"
- "DELETE FROM browser_windows WHERE type = ? AND active_profile_identifier = ?"
- "DELETE FROM tab_sessions WHERE tab_uuid IN ('%@')"
- "DELETE FROM tabs WHERE browser_window_id = ?"
- "DELETE FROM tabs WHERE uuid = ?"
- "DROP INDEX IF EXISTS tab_sessions__uuid"
- "DROP INDEX IF EXISTS tabs__uuid"
- "DROP TABLE IF EXISTS tab_sessions"
- "DROP TABLE IF EXISTS tabs"
- "DROP TABLE IF EXISTS tabs_old"
- "DROP TABLE tab_sessions_old"
- "DROP TABLE tabs_old"
- "Database is in an inconsistent state on schema version 3. Atempting to recover"
- "Did not find object matching allowed classes: %{public}@"
- "Failed database integrity check"
- "Failed database integrity check: %{public}@"
- "Failed to add active_profile_identifier column: %{public}@ (%d)"
- "Failed to add profile_uuid column: %{public}@ (%d)"
- "Failed to add scene_id column to browser_windows table: %{public}@ (%d)"
- "Failed to add tab_group_uuid column: %{public}@ (%d)"
- "Failed to add uncompressed_session_data_size column to tabs table: %{public}@ (%d)"
- "Failed to check if tabs_old table exists. Sqlite error: %d"
- "Failed to checkpoint write ahead log: %{public}@ (%d)"
- "Failed to commit a transaction while updating tabs: %{public}@ (%d)"
- "Failed to commit the transaction while migrating database to schema version %d"
- "Failed to create table tab_sessions: %{public}@ (%d)"
- "Failed to create the browser_windows table: %{public}@ (%d)"
- "Failed to create the index for table: %{public}@ (%d)"
- "Failed to create the tab_sessions table: %{public}@ (%d)"
- "Failed to create the tabs table when removing session column: %{public}@ (%d)"
- "Failed to delete a profile window: %{public}@ (%d) (Profile: %{public}@)"
- "Failed to delete a tab: %{public}@ (%d)"
- "Failed to delete empty windows while merging: %{public}@ (%d)"
- "Failed to drop index in tab_sessions table: %{public}@ (%d)"
- "Failed to drop index in tabs table: %{public}@ (%d)"
- "Failed to drop tab_sessions table: %{public}@ (%d)"
- "Failed to drop tab_sessions_old table: %{public}@ (%d)"
- "Failed to drop tabs table: %{public}@ (%d)"
- "Failed to drop tabs_old table: %{public}@ (%d)"
- "Failed to enable write-ahead logging on BrowserState SQLite store at %{public}@"
- "Failed to insert a tab into the tabs table: %@ (%d)"
- "Failed to insert a tab session data into the tab_sessions table: %{public}@ (%d)"
- "Failed to insert browser window with UUID: %{public}@ (%d)"
- "Failed to migrate the database to schema version %d"
- "Failed to move tabs_old session data to tab_sessions table: %{public}@ (%d)"
- "Failed to move tabs_old table to tabs table: %{public}@ (%d)"
- "Failed to move tabs_session_old data to tab_sessions table: %{public}@ (%d)"
- "Failed to open tab state SQLite store at %{public}@."
- "Failed to read content from legacy SuspendState.plist at %{public}@"
- "Failed to recover from database inconsistency of schema version 3. Sqlite error: %d"
- "Failed to regenerate tab UUIDs: %{public}@ (%d)"
- "Failed to remove recently closed windows (Profile: %{public}@) from BrowserState.db: %{public}@ (%d)"
- "Failed to remove saved session state data for Recently Closed Tab from BrowserState.db: %{public}@ (%d)"
- "Failed to rename table tab_sessions to tab_sessions_old: %{public}@ (%d)"
- "Failed to rename table tabs to tabs_old: %{public}@ (%d)"
- "Failed to reset scene_id column: %{public}@ (%d)"
- "Failed to roll back transaction"
- "Failed to set the database schema version to %d: %{public}@ (%d)"
- "Failed to start a transaction while migrating database to schema version %d"
- "Failed to start a transaction while updating tabs: %{public}@ (%d)"
- "Failed to toggle secure_delete pragma: %{public}@ (%d) (%d)"
- "Failed to update a tab: %{public}@ (%d)"
- "Failed to update browser window with ID: %{public}@ (%d)"
- "Failed to update scene_id for window with UUID = %@: %{public}@ (%d)"
- "Failed to update tab id %d: %{public}@ (%d)"
- "Failed to vacuum database: %{public}@ (%d)"
- "INSERT INTO browser_windows (uuid, scene_id, active_document_index, active_private_document_index, legacy_plist_file_version, type, active_profile_identifier) VALUES (?, ?, ?, ?, ?, ?, ?)"
- "INSERT INTO tab_sessions (tab_uuid, session_data, uncompressed_session_data_size)SELECT tab_sessions_old.tab_uuid, tab_sessions_old.session_data, tab_sessions_old.uncompressed_session_data_size FROM tab_sessions_old"
- "INSERT INTO tab_sessions (tab_uuid, session_data, uncompressed_session_data_size)SELECT tabs_old.uuid, tabs_old.session_data, tabs_old.uncompressed_session_data_size FROM tabs_old"
- "INSERT INTO tab_sessions (tab_uuid, session_data, uncompressed_session_data_size)VALUES (?, ?, ?)"
- "INSERT INTO tabs (id, uuid, title, url, user_visible_url, order_index, last_viewed_time, readinglist_bookmark_id, opened_from_link, showing_reader, reader_view_top_scroll_offset, private_browsing, displaying_standalone_image, browser_window_uuid, browser_window_id)SELECT tabs_old.id, tabs_old.uuid, tabs_old.title, tabs_old.url, tabs_old.user_visible_url, tabs_old.order_index, tabs_old.last_viewed_time, tabs_old.readinglist_bookmark_id, tabs_old.opened_from_link, tabs_old.showing_reader, tabs_old.reader_view_top_scroll_offset, tabs_old.private_browsing, tabs_old.displaying_standalone_image, tabs_old.browser_window_uuid, tabs_old.browser_window_id FROM tabs_old"
- "INSERT INTO tabs (uuid, title, url, user_visible_url, order_index, last_viewed_time, readinglist_bookmark_id, opened_from_link, showing_reader, reader_view_top_scroll_offset, private_browsing, displaying_standalone_image, browser_window_uuid, browser_window_id, tab_group_uuid, profile_uuid)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
- "ItemProvider"
- "Legacy SuspendState.plist does not exist at %{public}@"
- "Library/Preferences/com.apple.Safari.SafeBrowsing.plist"
- "Loaded item of class: %{public}@"
- "Merge all windows: failed to begin transaction: %{public}@ (%d)"
- "Merge all windows: failed to commit transaction: %{public}@ (%d)"
- "Merge all windows: failed to roll back transaction: %{public}@ (%d)"
- "NormalBlankSnapshotGroupIdentifier"
- "Not migrating to an unsupported schema version %d"
- "PRAGMA foreign_keys = ON"
- "PRAGMA integrity_check(1)"
- "PRAGMA journal_mode = WAL"
- "PRAGMA secure_delete = OFF"
- "PRAGMA secure_delete = ON"
- "PRAGMA user_version"
- "PRAGMA user_version = %d"
- "PrivateBlankSnapshotGroupIdentifier"
- "ROLLBACK"
- "ROLLBACK TRANSACTION"
- "RecentSearches"
- "SELECT * FROM browser_windows WHERE uuid = ?"
- "SELECT COUNT(*) FROM browser_windows"
- "SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND (name = 'tabs_old' OR name = 'tab_sessions')"
- "SELECT id, browser_window_id FROM tabs ORDER BY order_index ASC"
- "SELECT id, uuid FROM browser_windows WHERE type = ? ORDER BY id DESC"
- "SELECT id, uuid, scene_id FROM browser_windows WHERE type = ?"
- "SELECT id, uuid, type FROM browser_windows ORDER BY id ASC"
- "SELECT tab_sessions.uncompressed_session_data_size, tab_sessions.session_data FROM tab_sessions WHERE tab_sessions.tab_uuid = ?"
- "SELECT tabs.id, tabs.uuid, tabs.title, tabs.url, tabs.user_visible_url, tabs.order_index, tabs.last_viewed_time, tabs.readinglist_bookmark_id, tabs.opened_from_link, tabs.showing_reader, tabs.reader_view_top_scroll_offset, tabs.private_browsing, tabs.displaying_standalone_image, tabs.browser_window_uuid, tabs.tab_group_uuid, tabs.profile_uuid FROM tabs WHERE browser_window_id = ? ORDER BY tabs.order_index ASC"
- "SELECT tabs.id, tabs.uuid, tabs.title, tabs.url, tabs.user_visible_url, tabs.order_index, tabs.last_viewed_time, tabs.readinglist_bookmark_id, tabs.opened_from_link, tabs.showing_reader, tabs.reader_view_top_scroll_offset, tabs.private_browsing, tabs.displaying_standalone_image, tabs.browser_window_uuid, tabs.tab_group_uuid, tabs.profile_uuid FROM tabs WHERE uuid = ?"
- "SFBrowserStateSQLiteStore"
- "SFRecentlyClosedTabsWereAdded"
- "SFRecentlyClosedTabsWereRemoved"
- "SFRemovedTabStateDataKey"
- "Safari appeared to crash when migrating from V2 to V3, skipping migrating this time"
- "SafariPasswordManagersControllerDelegate"
- "SafariStateBrowserWindowDatabaseID"
- "ShowingTabView"
- "Start migrating from tab state database from V2 to V3"
- "StatePersistence"
- "Successfully recovered from database inconsistency of schema version 3."
- "T@\"NSArray\",C,N,V_browserWindows"
- "T@\"NSString\",&,N,V_UUIDString"
- "T@\"NSString\",&,N,V_sceneID"
- "T@\"NSString\",C,N,V_activeProfileIdentifier"
- "T@\"NSUUID\",&,N"
- "T@\"_SFBrowserSavedState\",&,N"
- "T@\"_SFBrowserWindowSettings\",R,N"
- "TB,N,V_invalidatesClosedWindows"
- "TB,N,V_isActiveDocumentValid"
- "TB,N,V_isTabStateSuccessfullyLoaded"
- "TB,N,V_needsQuickUpdate"
- "TB,N,V_secureDeleteEnabled"
- "TB,R,N,V_shouldBeUsedDuringTest"
- "TabGroupBlankSnapshotGroupIdentifier"
- "TabStateMigrationInProgress"
- "Tq,N,V_activeDocumentIndex"
- "Tq,N,V_activePrivateDocumentIndex"
- "Tq,N,V_databaseID"
- "Tq,N,V_legacyPlistFileVersion"
- "Tq,N,V_type"
- "UPDATE browser_windows SET active_document_index = ?, active_private_document_index = ?, type = ? WHERE id = ?"
- "UPDATE browser_windows SET scene_id = ? WHERE uuid = ?"
- "UPDATE browser_windows SET scene_id = NULL"
- "UPDATE tab_sessions SET session_data = ?, uncompressed_session_data_size = ?WHERE tab_uuid = ?"
- "UPDATE tabs SET order_index = ?, browser_window_id = ?, browser_window_uuid = ? WHERE id = ?"
- "UPDATE tabs SET order_index = ?, browser_window_uuid = ?, browser_window_id = ?WHERE uuid = ?"
- "UPDATE tabs SET title = ?, url = ?, user_visible_url = ?, order_index = ?, last_viewed_time = ?, readinglist_bookmark_id = ?, opened_from_link = ?, showing_reader = ?, reader_view_top_scroll_offset = ?, private_browsing = ?, displaying_standalone_image = ?, browser_window_uuid = ?, browser_window_id = ?, tab_group_uuid = ?, profile_uuid = ?WHERE uuid = ?"
- "UPDATE tabs SET uuid = sf_generate_uuid()"
- "Unknown window type for tab id %{public}@ in window id %{public}@"
- "VACUUM"
- "_SFBrowserSavedState"
- "_SFBrowserWindowSettings"
- "_SFBrowserWindowStateData"
- "_UUIDString"
- "_WKWebAuthenticationPanelDelegate"
- "_activeDocumentIndex"
- "_activePrivateDocumentIndex"
- "_activeProfileIdentifier"
- "_addLegacySearch:"
- "_autoFillCellForTableView:"
- "_autoFillPasswordsCell"
- "_blankSnapshotKeyForPrivateBrowsing:syncableTabGroupUUID:"
- "_boolValueForKey:windowUUID:"
- "_browserStateSQLiteStore"
- "_browserWindowDatabaseIDs"
- "_browserWindows"
- "_cacheUUIDForTabStateData:"
- "_cachedTabDeleteStatement"
- "_checkDatabaseIntegrity"
- "_checkPointWriteAheadLogIfNeeded"
- "_checkPointWriteAheadLogOnNextUpdate"
- "_closeDatabase"
- "_createFreshDatabaseSchema"
- "_createTableForTabSession"
- "_createTableForTabs"
- "_createWebClipFromWebView"
- "_createWebView"
- "_database"
- "_databaseID"
- "_databaseIDForBrowserWindow:"
- "_databaseQueue"
- "_databaseURL"
- "_finishPreparingFromWebView"
- "_generateUUIDFunctionAttached"
- "_getExternalLoginCredentialSuggestionsForDomains:completion:"
- "_getExternalLoginCredentialSuggestionsForDomains:pageURL:completion:"
- "_haveLoadedRecentlyClosedTabs"
- "_historyItemsWereRemoved:"
- "_initializeSettingsDictionaryIfNeeded"
- "_insertTabStateWithData:"
- "_invalidatesClosedWindows"
- "_isActiveDocumentValid"
- "_isDatabaseOpen"
- "_isTabStateCached:"
- "_isTabStateSuccessfullyLoaded"
- "_legacyPlistFileVersion"
- "_mergeAllWindowsIfNeeded"
- "_migrateFromLegacyPlistIfNeeded"
- "_migrateFromLegacyPlistWithPath:"
- "_migrateLegacyData"
- "_migrateToCurrentSchemaVersionIfNeeded"
- "_migrateToSchemaVersion:"
- "_migrateToSchemaVersion_2"
- "_migrateToSchemaVersion_3"
- "_migrateToSchemaVersion_4"
- "_migrateToSchemaVersion_5"
- "_migrateToSchemaVersion_6"
- "_migrateToSchemaVersion_7"
- "_migrateToSchemaVersion_8"
- "_needsQuickUpdate"
- "_notifyThatRecentlyClosedTabsWereRemoved:"
- "_numberForKey:windowUUID:"
- "_openDatabaseAndCheckIntegrity:"
- "_pathToLegacySearchesFile"
- "_readBrowserControllersSavedState"
- "_readRecentlyClosedTabsStateIfNecessary"
- "_readSavedSessionStateDataForTabWithUUIDString:"
- "_readTabStatesWithBrowserWindowUUID:completion:"
- "_recentlyClosedTabs"
- "_recoverFromDatabaseInconsistencyFromSchemaVersion3Migration"
- "_regenerateTabUUIDsForDeviceRestoration"
- "_removeLegacyRecentSearchesData"
- "_removeRecentlyClosedTabStateData:"
- "_removeSavedSessionStateDataForTabsWithUUIDStrings:"
- "_saveBrowserWindowStateWithData:"
- "_saveBrowserWindowStateWithDictionary:"
- "_sceneID"
- "_schemaVersion"
- "_secureDeleteEnabled"
- "_securityRecommendationsCell"
- "_selectionEffect"
- "_setBool:forKey:windowUUID:"
- "_setDatabaseID:browserWindow:"
- "_setDatabaseSchemaVersion:"
- "_setString:forKey:windowUUID:"
- "_settingsDictionary"
- "_sf_accessingSecurityScopedResource:"
- "_sf_ensurePathExtension:"
- "_sf_highLevelDomainFromHostFallingBackToHostOrAbsoluteString"
- "_sf_isAppleOneURL"
- "_sf_isSafariViewServiceBundle"
- "_sf_isWebSheetApplicationBundle"
- "_sf_itunesItemIdentifier"
- "_sf_loadObjectOfClasses:completionHandler:"
- "_sf_loadObjectsFromItemProviders:usingLoader:completionHandler:"
- "_sf_safeBrowsingPreferencesPlistPath"
- "_sf_topLevelDomain"
- "_shouldBeUsedDuringTest"
- "_sqliteStatementForTabDeleting"
- "_stringForKey:windowUUID:"
- "_synchronizeNow"
- "_synchronizeScheduled"
- "_tabCountByWindowUUID"
- "_tabStateDataForUUID:"
- "_tabUUIDStrings"
- "_tabUUIDsInWindow:"
- "_updateBrowserWindowStateWithDictionary:"
- "_updateBrowserWindowWithData:tabs:"
- "_updateOrInsertTabStateWithData:"
- "_updateTabStateWithData:"
- "_vacuum"
- "_viewGroupDetailsCell"
- "acceptedMIMETypes"
- "activeDocumentIndex"
- "activeDocumentIsValidForBrowserControllerWithUUID:"
- "activeDocumentIsValidForWindowWithUUID:"
- "activePrivateDocumentIndex"
- "activeProfileIdentifier"
- "addRecentlyClosedTabs:"
- "ams-ui"
- "apple.news"
- "authenticatorDialogForPanel:dialogController:"
- "autoFillDrillIn"
- "bindData:atParameterIndex:"
- "bindDouble:atParameterIndex:"
- "bindInt64:atParameterIndex:"
- "bindInt:atParameterIndex:"
- "bindString:atParameterIndex:"
- "blankSnapshotGroupIdentifierForPrivateBrowsing:syncableTabGroupUUID:forWindowWithUUID:"
- "boolAtIndex:"
- "browserWindows"
- "checkPointWriteAheadLog"
- "checkpointWriteAheadLogWithLogFrameCount:checkpointedFrameCount:"
- "clearRecentlyClosedTabsForProfileWithIdentifier:"
- "clearSavedStatesForProfileWithIdentifier:closingDatabase:"
- "close"
- "closeDatabase"
- "color"
- "com.apple.MobileSafari.TabStateSQLiteStore"
- "com.apple.SafariServices.SavingBrowserState"
- "com.apple.SafariServices._SFBrowserSavedState.HistoryItemsWereRemoved"
- "com.apple.WebSheet"
- "compare:options:"
- "currentOneTimeCodesForWebBrowserWithWebsiteFrameURLs:fieldClassification:"
- "dataAtIndex:"
- "dataForKey:forWindowWithUUID:"
- "dataWithContentsOfURL:options:error:"
- "databaseID"
- "decidePolicyForLocalAuthenticatorWithCompletionHandler:"
- "defaultBrowserStateDatabase"
- "defaultPPTBrowserStateDatabase"
- "deleteRecentlyClosedWindowsWithProfileIdentifier:"
- "deleteSavedStatesForProfileWithIdentifier:"
- "deleteTabStateWithBrowserWindowUUID:andRemoveWindow:"
- "ephemeralSavedState"
- "execute"
- "feed"
- "feeds"
- "feedsearch"
- "fetch"
- "fetchQuery:"
- "finishedAutoFillingOneTimeCodeInFrame:shouldSubmit:"
- "fragment"
- "handleAutoFillDrillInForEditableSavedAccountTableViewController:"
- "hasDifferentColorAppearanceComparedToTraitCollection:"
- "hasPrivateBrowsingWindow"
- "i20@0:8i16"
- "i8@?0"
- "id"
- "inMemoryDatabase"
- "inMemoryDatabaseURL"
- "initWithDatabase:query:"
- "initWithDatabase:query:error:"
- "initWithDatabaseURL:"
- "initWithDictionaryRepresentation:"
- "initWithPathToLegacySearchesFile:"
- "initWithSQLiteRow:"
- "initWithSavedAccount:warning:searchPattern:savedAccountIsOnlySavedAccountForHighLevelDomain:"
- "initWithURL:completion:"
- "initWithURL:queue:"
- "initWithUUIDString:sceneID:"
- "intAtIndex:"
- "invalidatesClosedWindows"
- "isActiveDocumentValid"
- "isInDatabase"
- "isParsecABTestingEnabled"
- "isShowingTabViewForWindowWithUUID:"
- "isTabStateSuccessfullyLoaded"
- "itms-appss"
- "lastErrorMessage"
- "lastInsertRowID"
- "lastResultCode"
- "lastViewedTime"
- "legacyPlistFileVersion"
- "loadObjectOfClass:completionHandler:"
- "loadSessionStateDataAndRemoveRecentlyClosedTab:"
- "mergeAllWindows"
- "needsQuickUpdate"
- "nonPersistentDataStore"
- "numberFromString:"
- "numberOfSavedAccountsForHighLevelDomain:"
- "ok"
- "one.apple.com"
- "openWithAccessType:error:"
- "orderIndex"
- "owningBrowserWindowDatabaseID"
- "owningBrowserWindowUUIDString"
- "panel"
- "panel:decidePolicyForLocalAuthenticatorWithCompletionHandler:"
- "panel:dismissWebAuthenticationPanelWithResult:"
- "panel:requestLAContextForUserVerificationWithCompletionHandler:"
- "panel:requestPINWithRemainingRetries:completionHandler:"
- "panel:selectAssertionResponse:source:completionHandler:"
- "panel:updateWebAuthenticationPanel:"
- "parsecABGroupIdentifier"
- "passwordOptionsViewController:"
- "prepareWithURL:"
- "presentedAuthenticatorDialog"
- "privateBrowsing"
- "privateBrowsingEnabledForWindowWithUUID:"
- "profileIdentifier"
- "rangeOfCharacterFromSet:options:"
- "readSavedSessionStateDataForTabWithUUID:"
- "readSavedSessionStateDataForTabWithUUIDString:"
- "readTabStatesWithBrowserWindowUUID:completion:"
- "readerViewTopScrollOffset"
- "readingListBookmarkID"
- "recentlyClosedTabsForProfileWithIdentifier:"
- "recentlyClosedWindows"
- "regenerateTabUUIDsForDeviceRestoration"
- "removeObjectsInArray:"
- "removeRecentlyClosedTabWithStateData:"
- "removeSavedSessionStateDataForTabsWithUUIDStrings:"
- "removeTabStateWithTabData:"
- "removeTabWithTabData:"
- "removeTabsStateForBrowserControllerWithUUID:andRemoveWindow:"
- "removeWindowWithUUID:"
- "replaceOccurrencesOfString:withString:options:range:"
- "reportErrorWithCode:statement:error:"
- "requestPINWithRemainingRetries:completionHandler:"
- "saveTabStateData:"
- "saveTabStateWithDictionary:"
- "saveTabsState:forBrowserControllerWithUUID:completion:"
- "savedTabsStateForBrowserControllerWithUUID:"
- "sceneID"
- "secureDeleteEnabled"
- "selectAssertionResponse:source:completionHandler:"
- "sessionStateData"
- "setActiveDocumentIndex:"
- "setActiveDocumentIsValid:forBrowserControllerWithUUID:"
- "setActiveDocumentIsValid:forWindowWithUUID:"
- "setActivePrivateDocumentIndex:"
- "setActiveProfileIdentifier:"
- "setBlankSnapshotGroupIdentifier:forPrivateBrowsing:syncableTabGroupUUID:forWindowWithUUID:"
- "setBrowserWindows:"
- "setCredential:forProtectionSpace:"
- "setData:forKey:forWindowWithUUID:"
- "setDatabaseID:"
- "setInspectable:"
- "setInvalidatesClosedWindows:"
- "setIsActiveDocumentValid:"
- "setIsForUpdateOnly:"
- "setIsShowingTabView:forWindowWithUUID:"
- "setIsTabStateSuccessfullyLoaded:"
- "setLegacyPlistFileVersion:"
- "setNeedsQuickUpdate:"
- "setOwningBrowserWindowDatabaseID:"
- "setOwningBrowserWindowUUIDString:"
- "setPrivateBrowsingEnabled:forWindowWithUUID:"
- "setSceneID:"
- "setSecureDeleteEnabled:"
- "setSessionStateData:"
- "setSharedBrowserSavedState:"
- "setSharedSettings:"
- "setShouldMergeAllWindowsIfNeeded:"
- "setShouldTakeUIBackgroundAssertion:"
- "setUUIDString:"
- "settings"
- "sf_URLScheme"
- "sf_absoluteStringWithoutFragment"
- "sf_generate_uuid"
- "sf_isAppleNewsURL"
- "sf_isConfigProfileMIMEType"
- "sf_isFeedScheme"
- "sf_isWebSearchURL"
- "sf_stringByAddingSoftBreaksBeforePeriods"
- "sf_stringByReplacingLastOccurrenceOfWhitespaceWithANonBreakingSpace"
- "sf_stringByReplacingMarkupCharactersWithHTMLEntities"
- "sharedBrowserSavedState"
- "shouldBeUsedDuringTest"
- "shouldMergeAllWindowsIfNeeded"
- "skipSavingSessionState"
- "skipUpdate"
- "statement"
- "stringAtIndex:"
- "stringByAppendingPathExtension:"
- "stringByReplacingCharactersInRange:withString:"
- "subtitleFontForNarrowCell"
- "tabGroupUUID"
- "tabStateDataForUUID:"
- "tabStatesWithBrowserWindowUUID:"
- "uncompressedDataWithRawData:uncompressedSize:"
- "uncompressedSessionStateDataSize"
- "updateBrowserWindowState:tabs:"
- "updateBrowserWindowStateWithDictionary:completion:"
- "updateBrowserWindowWithData:tabs:"
- "updateSceneID:"
- "updateTabWithTabStateData:"
- "updateWebAuthenticationPanel:"
- "userVisibleURL"
- "v24@?0@\"<NSItemProviderReading>\"8@\"NSError\"16"
- "v24@?0@\"NSString\"8^B16"
- "v32@0:8@\"_WKWebAuthenticationPanel\"16@?<v@?@\"LAContext\">24"
- "v32@0:8@\"_WKWebAuthenticationPanel\"16@?<v@?q>24"
- "v32@0:8@\"_WKWebAuthenticationPanel\"16q24"
- "v32@?0@\"NSItemProvider\"8Q16^B24"
- "v32@?0@\"NSNumber\"8@\"NSArray\"16^B24"
- "v32@?0@\"NSString\"8@\"NSMutableSet\"16^B24"
- "v32@?0@\"SFTabStateData\"8Q16^B24"
- "v40@0:8@\"_WKWebAuthenticationPanel\"16Q24@?<v@?@\"NSString\">32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16^?24@?32"
- "v48@0:8@\"_WKWebAuthenticationPanel\"16@\"NSArray\"24q32@?<v@?@\"_WKWebAuthenticationAssertionResponse\">40"
- "validateWindowSettingsWithUUIDs:"
- "wasOpenedFromLink"
- "x-web-search"
- "\xf0\xc2\x11Aq"
- "\xf0\xf0\xf0\xf0Q"

```
