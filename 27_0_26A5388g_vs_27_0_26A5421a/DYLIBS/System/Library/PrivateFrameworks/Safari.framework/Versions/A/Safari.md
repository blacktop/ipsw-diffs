## Safari

> `/System/Library/PrivateFrameworks/Safari.framework/Versions/A/Safari`

```diff

-625.1.24.11.2
-  __TEXT.__text: 0x7ed650
-  __TEXT.__objc_methlist: 0x5e1ec
-  __TEXT.__cstring: 0x45d2b
-  __TEXT.__gcc_except_tab: 0xcfa48
-  __TEXT.__const: 0xa996
+625.1.29.11.25
+  __TEXT.__text: 0x7ec81c
+  __TEXT.__objc_methlist: 0x5e134
+  __TEXT.__cstring: 0x45da8
+  __TEXT.__gcc_except_tab: 0xcfde0
+  __TEXT.__const: 0xa8e8
   __TEXT.__ustring: 0x11390
-  __TEXT.__oslogstring: 0x24a21
+  __TEXT.__oslogstring: 0x2439c
   __TEXT.__dlopen_cstrs: 0x468
-  __TEXT.__swift5_typeref: 0x9156
+  __TEXT.__swift5_typeref: 0x9140
+  __TEXT.__swift5_capture: 0x1988
   __TEXT.__constg_swiftt: 0x2d0c
-  __TEXT.__swift5_builtin: 0x208
-  __TEXT.__swift5_reflstr: 0x2a70
-  __TEXT.__swift5_fieldmd: 0x21f4
+  __TEXT.__swift5_reflstr: 0x2a7b
   __TEXT.__swift5_assocty: 0x4b8
-  __TEXT.__swift5_capture: 0x1988
+  __TEXT.__swift5_fieldmd: 0x21f4
+  __TEXT.__swift5_builtin: 0x208
   __TEXT.__swift5_proto: 0x238
   __TEXT.__swift5_types: 0x254
   __TEXT.__swift_as_entry: 0x114

   __TEXT.__swift_as_cont: 0x1c8
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3ede8
+  __TEXT.__unwind_info: 0x3eef8
   __TEXT.__eh_frame: 0x3230
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4ba0
-  __DATA_CONST.__objc_classlist: 0x2348
+  __DATA_CONST.__const: 0x4b40
+  __DATA_CONST.__objc_classlist: 0x2330
   __DATA_CONST.__objc_catlist: 0x308
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1260
+  __DATA_CONST.__objc_protolist: 0x1258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33db8
+  __DATA_CONST.__objc_selrefs: 0x33e50
   __DATA_CONST.__objc_protorefs: 0x2d0
-  __DATA_CONST.__objc_superrefs: 0x1970
-  __DATA_CONST.__objc_arraydata: 0xc08
+  __DATA_CONST.__objc_superrefs: 0x1958
+  __DATA_CONST.__objc_arraydata: 0xc28
   __DATA_CONST.__got: 0x4ac8
-  __AUTH_CONST.__const: 0x20ba8
-  __AUTH_CONST.__cfstring: 0x38fa0
-  __AUTH_CONST.__objc_const: 0x8a008
+  __AUTH_CONST.__const: 0x20b78
+  __AUTH_CONST.__cfstring: 0x38de0
+  __AUTH_CONST.__objc_const: 0x89ca8
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_intobj: 0x1458
+  __AUTH_CONST.__objc_intobj: 0x14d0
   __AUTH_CONST.__objc_dictobj: 0x5f0
   __AUTH_CONST.__objc_doubleobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x5a0
+  __AUTH_CONST.__objc_arrayobj: 0x5b8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x4030
-  __AUTH.__objc_data: 0x10258
-  __AUTH.__data: 0x1e70
-  __DATA.__objc_ivar: 0x65d4
-  __DATA.__data: 0xfdd0
+  __AUTH_CONST.__auth_got: 0x4028
+  __AUTH.__objc_data: 0x101b8
+  __AUTH.__data: 0x1e80
+  __DATA.__objc_ivar: 0x65d0
+  __DATA.__data: 0xfd70
   __DATA.__objc_stublist: 0x20
-  __DATA.__bss: 0x56a0
+  __DATA.__bss: 0x56d0
   __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_data: 0x8f10
-  __DATA_DIRTY.__data: 0x870
+  __DATA_DIRTY.__objc_data: 0x8ec0
+  __DATA_DIRTY.__data: 0x860
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0x1238
   __DATA_DIRTY.__common: 0x30

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 41743
-  Symbols:   83644
-  CStrings:  11018
+  Functions: 41725
+  Symbols:   83620
+  CStrings:  10998
 
Symbols:
+ +[FeatureAvailability _douyinSearchProviderIsAvailble]
+ -[AppController downloadsManager:shouldAllowDownload:onWebView:fromAccountableHost:originatingURL:completionHandler:]
+ -[AppController tabClusteringPolicy]
+ -[AutomaticPasswordChangeSession oneTimeCodeProviderForAutomaticPasswordChangeController:]
+ -[BrowserApplication _browserWindowControllerWithAttachedAppSSOSheetForKeyWindow]
+ -[BrowserTabViewItem presentClusterOnboardingTipIfNeeded]
+ -[BrowserViewController openerAccountableHostAtCreation]
+ -[BrowserViewController setOpenerAccountableHostAtCreation:]
+ -[BrowserWindowController _canCloseTabsWithoutClosingWindow:]
+ -[BrowserWindowController _requestAuthorizationForAuthorizationRight:completionHandler:]
+ -[BrowserWindowController didRequestAuthorizationForExtensionCreationWithMagicExtensionsController:completionHandler:]
+ -[BrowserWindowController didRequestAuthorizationForExtensionRefinementWithMagicExtensionsController:completionHandler:]
+ -[BrowserWindowController dismissClusterOnboardingTipIfNeeded]
+ -[BrowserWindowController moveWebExtensionTab:beforeTab:error:]
+ -[BrowserWindowController performClose:]
+ -[BrowserWindowController presentClusterOnboardingTipFrom:]
+ -[CombinedFavoritesController _sendPendingFavoritesContentsChange]
+ -[DownloadProgressEntry _initWithRequest:bytesLoaded:bytesExpected:error:download:downloadFile:postDownloadFile:downloadStage:identifier:mayOpenWhenDone:shouldAvoidPersistingIdentifyingInformation:profileIdentifier:]
+ -[DownloadProgressEntry downloadBundleURL]
+ -[DownloadProgressEntry setDownloadBundleURL:]
+ -[DownloadProgressEntry willBeginDownloadWithBundleURL:filename:]
+ -[DownloadsManager _consumeCapturedAccountableHostForTriggeringObject:]
+ -[DownloadsManager captureAccountableHost:forNavigationActionOrResponse:]
+ -[DownloadsManager discardCapturedAccountableHostForNavigationActionOrResponse:]
+ -[DownloadsManager downloadDidStart:triggeredByNavigationActionOrResponse:]
+ -[DownloadsManager downloadProgressEntry:didResumeWithDownload:willRequestDownloadDestination:]
+ -[NSWindow(SafariNSWindowExtras) safari_endAllSheetsWithReturnCode:]
+ -[PageTestHandler oneTimeCodeProviderForAutomaticPasswordChangeController:]
+ -[ReadingListDataStore _bookmarksDidChange:]
+ -[ReadingListDataStore _bookmarksWereAddedOrRemoved:]
+ -[RestrictedSandboxBroker cancelUnarchivingOperationInDownloadBundleAtURL:completionHandler:]
+ -[RestrictedSandboxBroker deleteUnusedDownloadBundleAtURL:completionHandler:]
+ -[RestrictedSandboxBroker extractDownloadedArchiveWithURL:ofType:completionHandler:]
+ -[RestrictedSandboxBroker getDownloadBundleForFileAtURL:completionHandler:]
+ -[RestrictedSandboxBroker moveDownloadBundleAtURLToTrash:completionHandler:]
+ -[RestrictedSandboxBroker moveDownloadedFilesAtURLs:fromDownloadBundleAtURL:completionHandler:]
+ -[RestrictedSandboxBroker updateFractionCompleted:forDownloadBundleAtURL:completionHandler:]
+ -[SafariSandboxBroker _canonicalDownloadBundleURL:]
+ -[SafariSandboxBroker _deleteUnusedDownloadBundleAtURL:completionHandler:]
+ -[SafariSandboxBroker _downloadBundleURLContainingURL:]
+ -[SafariSandboxBroker _extractDownloadedArchiveWithURL:ofType:completionHandler:]
+ -[SafariSandboxBroker _getDownloadBundleForFileAtURL:completionHandler:]
+ -[SafariSandboxBroker _isDownloadBundleURL:]
+ -[SafariSandboxBroker _moveDownloadBundleAtURLToTrash:completionHandler:]
+ -[SafariSandboxBroker _moveDownloadedFilesWithURLs:fromDownloadBundleAtURL:completionHandler:]
+ -[SafariSandboxBroker _removeLegacyDownloadMetadata]
+ -[SafariSandboxBroker _updateFractionCompleted:forDownloadBundleAtURL:completionHandler:]
+ -[SafariSandboxBroker cancelUnarchivingOperationInDownloadBundleAtURL:completionHandler:]
+ -[SafariSandboxBroker deleteUnusedDownloadBundleAtURL:completionHandler:]
+ -[SafariSandboxBroker extractDownloadedArchiveWithURL:ofType:completionHandler:]
+ -[SafariSandboxBroker getDownloadBundleForFileAtURL:completionHandler:]
+ -[SafariSandboxBroker moveDownloadBundleAtURLToTrash:completionHandler:]
+ -[SafariSandboxBroker moveDownloadedFilesAtURLs:fromDownloadBundleAtURL:completionHandler:]
+ -[SafariSandboxBroker updateFractionCompleted:forDownloadBundleAtURL:completionHandler:]
+ -[SafariSandboxBrokerConnection cancelUnarchivingOperationInDownloadBundleAtURL:completionHandler:]
+ -[SafariSandboxBrokerConnection deleteUnusedDownloadBundleAtURL:completionHandler:]
+ -[SafariSandboxBrokerConnection extractDownloadedArchiveWithURL:ofType:completionHandler:]
+ -[SafariSandboxBrokerConnection getDownloadBundleForFileAtURL:completionHandler:]
+ -[SafariSandboxBrokerConnection moveDownloadBundleAtURLToTrash:completionHandler:]
+ -[SafariSandboxBrokerConnection moveDownloadedFilesAtURLs:fromDownloadBundleAtURL:completionHandler:]
+ -[SafariSandboxBrokerConnection updateFractionCompleted:forDownloadBundleAtURL:completionHandler:]
+ -[StartPageCollectionViewController _applyPendingDiffableSnapshotRebuildIfNeeded]
+ -[StartPageCollectionViewController _setNeedsRebuildAndApplyDiffableSnapshotAnimatingDifferences:]
+ -[StartPageCollectionViewController startPageCollectionSectionProvider:updateVisibilityOfSectionsWithDataAvailable:animated:]
+ -[StartPageCollectionViewController startPageCollectionSectionProviderDataDidChange:animated:]
+ -[StartPageCollectionViewControllerAnimator startPageCollectionSectionProvider:updateVisibilityOfSectionsWithDataAvailable:animated:]
+ -[StartPageCollectionViewControllerAnimator startPageCollectionSectionProviderDataDidChange:animated:]
+ -[StartPageReadingListSectionProvider _reloadCachedReadingListItems]
+ -[StartPageResumeBrowsingSectionProvider _reloadDataAnimated:]
+ -[UnifiedTabBar _gestureRecognizersViewConfigForMouseEmulation]
+ -[UnifiedTabBar _handleSidecarScrollGesture:]
+ -[UnifiedTabBar _maximumHorizontalScrollOrigin]
+ -[UnifiedTabBar _setUpSidecarScrollGestureRecognizer]
+ -[UnifiedTabBar gestureRecognizer:shouldRequireFailureOfGestureRecognizer:]
+ GCC_except_table1012
+ GCC_except_table1027
+ GCC_except_table1043
+ GCC_except_table1045
+ GCC_except_table1053
+ GCC_except_table1055
+ GCC_except_table1066
+ GCC_except_table1081
+ GCC_except_table1097
+ GCC_except_table1102
+ GCC_except_table1133
+ GCC_except_table1135
+ GCC_except_table1168
+ GCC_except_table1174
+ GCC_except_table1202
+ GCC_except_table1213
+ GCC_except_table1228
+ GCC_except_table1234
+ GCC_except_table1262
+ GCC_except_table1265
+ GCC_except_table1267
+ GCC_except_table1268
+ GCC_except_table1303
+ GCC_except_table1304
+ GCC_except_table1310
+ GCC_except_table1327
+ GCC_except_table1330
+ GCC_except_table1352
+ GCC_except_table1353
+ GCC_except_table1376
+ GCC_except_table1387
+ GCC_except_table1392
+ GCC_except_table1393
+ GCC_except_table1397
+ GCC_except_table1406
+ GCC_except_table1407
+ GCC_except_table1421
+ GCC_except_table1422
+ GCC_except_table1425
+ GCC_except_table1437
+ GCC_except_table1450
+ GCC_except_table1465
+ GCC_except_table1469
+ GCC_except_table1473
+ GCC_except_table1475
+ GCC_except_table1484
+ GCC_except_table1486
+ GCC_except_table1496
+ GCC_except_table1500
+ GCC_except_table1509
+ GCC_except_table1510
+ GCC_except_table1511
+ GCC_except_table1521
+ GCC_except_table1525
+ GCC_except_table1526
+ GCC_except_table1547
+ GCC_except_table1556
+ GCC_except_table1557
+ GCC_except_table1567
+ GCC_except_table1572
+ GCC_except_table1574
+ GCC_except_table1585
+ GCC_except_table1588
+ GCC_except_table1595
+ GCC_except_table1597
+ GCC_except_table1598
+ GCC_except_table1608
+ GCC_except_table1615
+ GCC_except_table1621
+ GCC_except_table1624
+ GCC_except_table1627
+ GCC_except_table1630
+ GCC_except_table1636
+ GCC_except_table1651
+ GCC_except_table1652
+ GCC_except_table1653
+ GCC_except_table1673
+ GCC_except_table1675
+ GCC_except_table1691
+ GCC_except_table1692
+ GCC_except_table1693
+ GCC_except_table1696
+ GCC_except_table1703
+ GCC_except_table1707
+ GCC_except_table1709
+ GCC_except_table1716
+ GCC_except_table1723
+ GCC_except_table1729
+ GCC_except_table1734
+ GCC_except_table1737
+ GCC_except_table1746
+ GCC_except_table1747
+ GCC_except_table1748
+ GCC_except_table1749
+ GCC_except_table1750
+ GCC_except_table1759
+ GCC_except_table1762
+ GCC_except_table1763
+ GCC_except_table1771
+ GCC_except_table1775
+ GCC_except_table1777
+ GCC_except_table1779
+ GCC_except_table388
+ GCC_except_table417
+ GCC_except_table532
+ GCC_except_table537
+ GCC_except_table593
+ GCC_except_table607
+ GCC_except_table610
+ GCC_except_table612
+ GCC_except_table615
+ GCC_except_table643
+ GCC_except_table645
+ GCC_except_table677
+ GCC_except_table697
+ GCC_except_table705
+ GCC_except_table756
+ GCC_except_table851
+ GCC_except_table854
+ GCC_except_table873
+ GCC_except_table948
+ OBJC_IVAR_$_BrowserNavigationDelegate._mainFrameNavigationToAccountableHost
+ OBJC_IVAR_$_BrowserViewController._openerAccountableHostAtCreation
+ OBJC_IVAR_$_CombinedFavoritesController._pendingFavoritesContentsChange
+ OBJC_IVAR_$_CombinedFavoritesController._pendingFavoritesContentsChangeHasMultipleModifiedBookmarks
+ OBJC_IVAR_$_CombinedFavoritesController._pendingFavoritesContentsChangeModifiedBookmark
+ OBJC_IVAR_$_DownloadsManager._navigationActionOrResponseToAccountableHost
+ OBJC_IVAR_$_DownloadsManager._resumedDownloadsWillRequestDownloadDestination
+ OBJC_IVAR_$_DownloadsManager._wkDownloadToPrecomputedAccountableHost
+ OBJC_IVAR_$_ReadingListDataStore._pendingItemsUpdate
+ OBJC_IVAR_$_SafariSandboxBroker._bundleURLsAllowingOverwrite
+ OBJC_IVAR_$_SafariSandboxBroker._unarchiversByBundleURL
+ OBJC_IVAR_$_StartPageCollectionViewController._isApplyingDiffableSnapshot
+ OBJC_IVAR_$_StartPageCollectionViewController._pendingDiffableSnapshotRebuildAnimatesDifferences
+ OBJC_IVAR_$_StartPageCollectionViewController._pendingSnapshotRebuild
+ OBJC_IVAR_$_StartPageReadingListSectionProvider._pendingItemsReload
+ OBJC_IVAR_$_UnifiedTabBar._sidecarScrollGestureRecognizer
+ OBJC_IVAR_$_UnifiedTabBar._sidecarTouchScrollStartOriginX
+ _OBJC_CLASS_$_WBSRunLoopCoalescedUpdate
+ _OBJC_CLASS_$_WBSSearchEngineBannerActivityTracker
+ _WBSDownloadFileUnarchiverErrorDomain
+ _WBSTabClusteringPolicyKey
+ __117-[AppController downloadsManager:shouldAllowDownload:onWebView:fromAccountableHost:originatingURL:completionHandler:]_block_invoke
+ __64-[DownloadsManager getDownloadLocationURLWithCompletionHandler:]_block_invoke
+ __73-[CombinedFavoritesController initWithTouchIconCache:topSitesController:]_block_invoke
+ __73-[SafariSandboxBroker _moveDownloadBundleAtURLToTrash:completionHandler:]_block_invoke
+ __87-[BrowserNavigationDelegate webView:decidePolicyForNavigationResponse:decisionHandler:]_block_invoke
+ __97-[BrowserNavigationDelegate webView:decidePolicyForNavigationAction:preferences:decisionHandler:]_block_invoke
+ __ZGVZ51-[AuthorizationRequest initWithAuthorizationRight:]E26watchAuthorizationRequests
+ __ZGVZ81-[BrowserApplication _browserWindowControllerWithAttachedAppSSOSheetForKeyWindow]E32authorizationViewControllerClass
+ __ZL27bookmarkIsReadingListFolderP17SafariWebBookmark
+ __ZZ51-[AuthorizationRequest initWithAuthorizationRight:]E26watchAuthorizationRequests
+ __ZZ81-[BrowserApplication _browserWindowControllerWithAttachedAppSSOSheetForKeyWindow]E32authorizationViewControllerClass
+ ___101-[SafariSandboxBrokerConnection moveDownloadedFilesAtURLs:fromDownloadBundleAtURL:completionHandler:]_block_invoke
+ ___115-[FormCredentialsCompletionControllerObjCAdapter performPasskeyAssertionUsingCredentialIdentity:requestParameters:]_block_invoke_2
+ ___117-[AppController downloadsManager:shouldAllowDownload:onWebView:fromAccountableHost:originatingURL:completionHandler:]_block_invoke
+ ___133-[StartPageCollectionViewControllerAnimator startPageCollectionSectionProvider:updateVisibilityOfSectionsWithDataAvailable:animated:]_block_invoke
+ ___44-[ReadingListDataStore initWithStoredTitle:]_block_invoke
+ ___61-[StartPageCollectionViewController _setupDiffableDataSource]_block_invoke_2
+ ___65-[StartPageReadingListSectionProvider initWithCompactAppearance:]_block_invoke
+ ___66-[CombinedFavoritesController _sendPendingFavoritesContentsChange]_block_invoke
+ ___71-[SafariSandboxBroker getDownloadBundleForFileAtURL:completionHandler:]_block_invoke
+ ___72-[SafariSandboxBroker moveDownloadBundleAtURLToTrash:completionHandler:]_block_invoke
+ ___73-[SafariSandboxBroker _moveDownloadBundleAtURLToTrash:completionHandler:]_block_invoke
+ ___73-[SafariSandboxBroker deleteUnusedDownloadBundleAtURL:completionHandler:]_block_invoke
+ ___80-[SafariSandboxBroker extractDownloadedArchiveWithURL:ofType:completionHandler:]_block_invoke
+ ___81-[SafariSandboxBroker _extractDownloadedArchiveWithURL:ofType:completionHandler:]_block_invoke
+ ___81-[SafariSandboxBroker _extractDownloadedArchiveWithURL:ofType:completionHandler:]_block_invoke_2
+ ___81-[SafariSandboxBrokerConnection getDownloadBundleForFileAtURL:completionHandler:]_block_invoke
+ ___82-[SafariSandboxBrokerConnection moveDownloadBundleAtURLToTrash:completionHandler:]_block_invoke
+ ___83-[SafariSandboxBrokerConnection deleteUnusedDownloadBundleAtURL:completionHandler:]_block_invoke
+ ___88-[SafariSandboxBroker updateFractionCompleted:forDownloadBundleAtURL:completionHandler:]_block_invoke
+ ___89-[SafariSandboxBroker cancelUnarchivingOperationInDownloadBundleAtURL:completionHandler:]_block_invoke
+ ___90-[SafariSandboxBrokerConnection extractDownloadedArchiveWithURL:ofType:completionHandler:]_block_invoke
+ ___91-[SafariSandboxBroker moveDownloadedFilesAtURLs:fromDownloadBundleAtURL:completionHandler:]_block_invoke
+ ___94-[SafariSandboxBroker _moveDownloadedFilesWithURLs:fromDownloadBundleAtURL:completionHandler:]_block_invoke
+ ___96-[DownloadsManager download:decideDestinationUsingResponse:suggestedFilename:completionHandler:]_block_invoke_3
+ ___98-[SafariSandboxBrokerConnection updateFractionCompleted:forDownloadBundleAtURL:completionHandler:]_block_invoke
+ ___99-[SafariSandboxBrokerConnection cancelUnarchivingOperationInDownloadBundleAtURL:completionHandler:]_block_invoke
+ ____ZN6Safari35FormCredentialsCompletionController21performListItemActionEPKNS_18CompletionListItemE24ShouldSubmitAfterFillingP9LAContextRbS7__block_invoke_2
+ ___block_descriptor_40_e8_32bs_e51_v40?0"NSURL"8"NSData"16"NSString"24"NSError"32l
+ ___block_descriptor_40_ea8_32s_e23_v20?0"WKDownload"8B16l
+ ___block_descriptor_40_ea8_32s_e40_v32?0"NSURL"8"NSString"16"NSError"24l
+ ___block_descriptor_48_ea8_32bs40bs_e40_v32?0"NSURL"8"NSString"16"NSError"24l
+ ___block_descriptor_48_ea8_32s40s_e38_v32?0"NSURL"8"NSData"16"NSError"24l
+ ___block_descriptor_49_ea8_32s40bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_50_ea8_32s40bs_e5_v8?0l
+ ___block_descriptor_50_ea8_32s40s_e28_v16?0"NSAnimationContext"8l
+ ___block_descriptor_56_e8_32s40bs_e51_v24?0"<SafariSandboxBrokerProtocol>"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_64_ea8_32s40s48s56bs_e33_v24?0q8"WKWebpagePreferences"16l
+ ___block_descriptor_65_e8_32s40s48r56r_e31_B32?0"NSString"8"NSURL"16Q24l
+ ___block_descriptor_72_ea8_32s40s48s56s64bs_e40_v32?0"NSURL"8"NSString"16"NSError"24l
+ __swift_closure_destructor.17Tm
+ _dlopen
+ _downloadBundleCreationNSDate
+ _objc_msgSend$_applyPendingDiffableSnapshotRebuildIfNeeded
+ _objc_msgSend$_browserWindowControllerWithAttachedAppSSOSheetForKeyWindow
+ _objc_msgSend$_canCloseTabsWithoutClosingWindow:
+ _objc_msgSend$_canonicalDownloadBundleURL:
+ _objc_msgSend$_consumeCapturedAccountableHostForTriggeringObject:
+ _objc_msgSend$_deleteUnusedDownloadBundleAtURL:completionHandler:
+ _objc_msgSend$_downloadBundleURLContainingURL:
+ _objc_msgSend$_extractDownloadedArchiveWithURL:ofType:completionHandler:
+ _objc_msgSend$_getDownloadBundleForFileAtURL:completionHandler:
+ _objc_msgSend$_initWithRequest:bytesLoaded:bytesExpected:error:download:downloadFile:postDownloadFile:downloadStage:identifier:mayOpenWhenDone:shouldAvoidPersistingIdentifyingInformation:profileIdentifier:
+ _objc_msgSend$_isDownloadBundleURL:
+ _objc_msgSend$_maximumHorizontalScrollOrigin
+ _objc_msgSend$_moveDownloadBundleAtURLToTrash:completionHandler:
+ _objc_msgSend$_moveDownloadedFilesWithURLs:fromDownloadBundleAtURL:completionHandler:
+ _objc_msgSend$_reloadCachedReadingListItems
+ _objc_msgSend$_reloadDataAnimated:
+ _objc_msgSend$_removeLegacyDownloadMetadata
+ _objc_msgSend$_requestAuthorizationForAuthorizationRight:completionHandler:
+ _objc_msgSend$_sendPendingFavoritesContentsChange
+ _objc_msgSend$_setNeedsRebuildAndApplyDiffableSnapshotAnimatingDifferences:
+ _objc_msgSend$_setUpSidecarScrollGestureRecognizer
+ _objc_msgSend$_updateFractionCompleted:forDownloadBundleAtURL:completionHandler:
+ _objc_msgSend$cancelUnarchivingOperationInDownloadBundleAtURL:completionHandler:
+ _objc_msgSend$captureAccountableHost:forNavigationActionOrResponse:
+ _objc_msgSend$closeCurrentTab:
+ _objc_msgSend$deleteUnusedDownloadBundleAtURL:completionHandler:
+ _objc_msgSend$discardCapturedAccountableHostForNavigationActionOrResponse:
+ _objc_msgSend$dismissClusterOnboardingTipIfNeeded
+ _objc_msgSend$downloadDidStart:triggeredByNavigationActionOrResponse:
+ _objc_msgSend$downloadProgressEntry:didResumeWithDownload:willRequestDownloadDestination:
+ _objc_msgSend$downloadsManager:shouldAllowDownload:onWebView:fromAccountableHost:originatingURL:completionHandler:
+ _objc_msgSend$extractDownloadedArchiveWithURL:ofType:completionHandler:
+ _objc_msgSend$getDownloadBundleForFileAtURL:completionHandler:
+ _objc_msgSend$isScheduled
+ _objc_msgSend$mainFrameNavigation
+ _objc_msgSend$moveDownloadBundleAtURLToTrash:completionHandler:
+ _objc_msgSend$moveDownloadedFilesAtURLs:fromDownloadBundleAtURL:completionHandler:
+ _objc_msgSend$noteAppNavigationInWebView:category:
+ _objc_msgSend$openerAccountableHostAtCreation
+ _objc_msgSend$performIfScheduled
+ _objc_msgSend$presentClusterOnboardingTipFrom:
+ _objc_msgSend$presentClusterOnboardingTipIfNeeded
+ _objc_msgSend$promoCategoryForNavigationURL:
+ _objc_msgSend$resetForWebView:
+ _objc_msgSend$safari_accountableHostWithOpenerHost:hasUserGesture:
+ _objc_msgSend$safari_endAllSheetsWithReturnCode:
+ _objc_msgSend$safari_fileURL
+ _objc_msgSend$safari_topOriginHost
+ _objc_msgSend$schedule
+ _objc_msgSend$setCancellableByScrollGesture:
+ _objc_msgSend$setDownloadBundleURL:
+ _objc_msgSend$setOneTimeCodeAppearsToHaveBeenFilledInItsEntirety:
+ _objc_msgSend$setOpenerAccountableHostAtCreation:
+ _objc_msgSend$startPageCollectionSectionProvider:updateVisibilityOfSectionsWithDataAvailable:animated:
+ _objc_msgSend$startPageCollectionSectionProviderDataDidChange:animated:
+ _objc_msgSend$tabClusteringPolicy
+ _objc_msgSend$translationInView:
+ _objc_msgSend$updateFractionCompleted:forDownloadBundleAtURL:completionHandler:
+ _objc_msgSend$userDidOpenRelatedTabsView
+ _objc_msgSend$willBeginDownloadWithBundleURL:filename:
+ downloadBundleCreationNSDate
- +[SafariSandboxDownloadBundleToken supportsSecureCoding]
- +[WindowControlShadowView windowControlShadowViewWithWindow:]
- -[AppController downloadsManager:shouldAllowDownload:onWebView:fromSecurityOrigin:originatingURL:completionHandler:]
- -[AppController showRelatedTabsPreviewEnabled]
- -[BrowserViewController pageContextDataFetcherGetPageContext:]
- -[DownloadProgressEntry _addCertificateToKeyChain]
- -[DownloadProgressEntry _extensionTokenForSandboxToken:withDownloadBundleAtURL:]
- -[DownloadProgressEntry _initWithRequest:bytesLoaded:bytesExpected:error:download:downloadFile:postDownloadFile:downloadStage:identifier:sandboxIdentifier:mayOpenWhenDone:shouldAvoidPersistingIdentifyingInformation:profileIdentifier:]
- -[DownloadProgressEntry cachedDownloadBundleURL]
- -[DownloadProgressEntry sandboxIdentifier]
- -[DownloadProgressEntry setCachedDownloadBundleURL:]
- -[DownloadProgressEntry willBeginDownloadWithBundleToken:]
- -[DownloadsManager downloadProgressEntry:didResumeWithDownload:]
- -[NSData(SafariExtras) safari_certificateFromMultipartData]
- -[ReadingListDataStore _readingListModelDataDidChange:]
- -[RestrictedSandboxBroker cancelUnarchivingOperationForDownloadWithIdentifier:completionHandler:]
- -[RestrictedSandboxBroker clearDownloadIdentifiersNotIncludedIn:completionHandler:]
- -[RestrictedSandboxBroker deleteUnusedDownloadBundleWithIdentifier:completionHandler:]
- -[RestrictedSandboxBroker extractDownloadedArchiveWithURL:ofType:forDownloadWithIdentifier:completionHandler:]
- -[RestrictedSandboxBroker getDownloadBundleURLForDownloadWithIdentifier:completionHandler:]
- -[RestrictedSandboxBroker moveDownloadBundleWithIdentifierToTrash:completionHandler:]
- -[RestrictedSandboxBroker moveDownloadedFilesAtURLs:inDownloadWithIdentifier:completionHandler:]
- -[RestrictedSandboxBroker updateFractionCompleted:forDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBroker _clearDownloadIdentifiersNotIncludedIn:completionHandler:]
- -[SafariSandboxBroker _deleteUnusedDownloadBundleWithIdentifier:completionHandler:]
- -[SafariSandboxBroker _dictionaryRepresentationsForEntries:]
- -[SafariSandboxBroker _downloadEntryForIdentifier:]
- -[SafariSandboxBroker _entriesOfClass:forDictionaryRepresentations:]
- -[SafariSandboxBroker _extractDownloadedArchiveWithURL:ofType:forDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBroker _getDownloadBundleURLForDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBroker _loadDownloadEntriesIfNeeded]
- -[SafariSandboxBroker _moveDownloadBundleWithIdentifierToTrash:completionHandler:]
- -[SafariSandboxBroker _moveDownloadedFilesWithURLs:inDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBroker _readDownloadDataFromOldLocationIfNeeded]
- -[SafariSandboxBroker _saveSandboxMetadata]
- -[SafariSandboxBroker _updateFractionCompleted:forDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBroker cancelUnarchivingOperationForDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBroker clearDownloadIdentifiersNotIncludedIn:completionHandler:]
- -[SafariSandboxBroker deleteUnusedDownloadBundleWithIdentifier:completionHandler:]
- -[SafariSandboxBroker extractDownloadedArchiveWithURL:ofType:forDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBroker getDownloadBundleURLForDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBroker moveDownloadBundleWithIdentifierToTrash:completionHandler:]
- -[SafariSandboxBroker moveDownloadedFilesAtURLs:inDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBroker updateFractionCompleted:forDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBrokerConnection cancelUnarchivingOperationForDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBrokerConnection clearDownloadIdentifiersNotIncludedIn:completionHandler:]
- -[SafariSandboxBrokerConnection deleteUnusedDownloadBundleWithIdentifier:completionHandler:]
- -[SafariSandboxBrokerConnection extractDownloadedArchiveWithURL:ofType:forDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBrokerConnection getDownloadBundleURLForDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBrokerConnection moveDownloadBundleWithIdentifierToTrash:completionHandler:]
- -[SafariSandboxBrokerConnection moveDownloadedFilesAtURLs:inDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxBrokerConnection updateFractionCompleted:forDownloadWithIdentifier:completionHandler:]
- -[SafariSandboxDownloadBundleToken .cxx_destruct]
- -[SafariSandboxDownloadBundleToken copyWithZone:]
- -[SafariSandboxDownloadBundleToken downloadBundleURL]
- -[SafariSandboxDownloadBundleToken downloadFilename]
- -[SafariSandboxDownloadBundleToken downloadIdentifier]
- -[SafariSandboxDownloadBundleToken encodeWithCoder:]
- -[SafariSandboxDownloadBundleToken initWithCoder:]
- -[SafariSandboxDownloadBundleToken initWithDownloadIdentifier:sandboxToken:downloadBundleURL:downloadFilename:]
- -[SafariSandboxDownloadBundleToken sandboxToken]
- -[UnifiedField isDetailStringHighlightedForFieldEditor:]
- -[UnifiedFieldEditor shouldDrawInsertionPoint]
- -[WindowControlShadowView .cxx_destruct]
- -[WindowControlShadowView initWithFrame:]
- -[WindowControlShadowView layout]
- -[WindowControlShadowView mouseDown:]
- -[WindowControlShadowView viewDidMoveToWindow]
- -[WindowControlShadowView viewWillMoveToWindow:]
- -[_SandboxDownloadEntry .cxx_destruct]
- -[_SandboxDownloadEntry allowsOverwrite]
- -[_SandboxDownloadEntry dictionaryRepresentation]
- -[_SandboxDownloadEntry downloadBundleBookmarkData]
- -[_SandboxDownloadEntry downloadBundleURLError:]
- -[_SandboxDownloadEntry downloadFilename]
- -[_SandboxDownloadEntry identifier]
- -[_SandboxDownloadEntry initWithDictionaryRepresentation:]
- -[_SandboxDownloadEntry init]
- -[_SandboxDownloadEntry setAllowsOverwrite:]
- -[_SandboxDownloadEntry setDownloadBundleBookmarkData:]
- -[_SandboxDownloadEntry setDownloadBundleURL:error:]
- -[_SandboxDownloadEntry setDownloadFilename:]
- -[_SandboxDownloadEntry setIdentifier:]
- -[_SandboxDownloadEntry setSuggestedFilename:]
- -[_SandboxDownloadEntry setUnarchiver:]
- -[_SandboxDownloadEntry suggestedFilename]
- -[_SandboxDownloadEntry unarchiver]
- GCC_except_table1008
- GCC_except_table1076
- GCC_except_table1091
- GCC_except_table1124
- GCC_except_table1140
- GCC_except_table1154
- GCC_except_table1182
- GCC_except_table1203
- GCC_except_table1208
- GCC_except_table1221
- GCC_except_table1224
- GCC_except_table1236
- GCC_except_table1241
- GCC_except_table1246
- GCC_except_table1250
- GCC_except_table1251
- GCC_except_table1278
- GCC_except_table1311
- GCC_except_table1312
- GCC_except_table1335
- GCC_except_table1349
- GCC_except_table1350
- GCC_except_table1351
- GCC_except_table1354
- GCC_except_table1408
- GCC_except_table1429
- GCC_except_table1430
- GCC_except_table1447
- GCC_except_table1481
- GCC_except_table1485
- GCC_except_table1488
- GCC_except_table1489
- GCC_except_table1490
- GCC_except_table1492
- GCC_except_table1494
- GCC_except_table1507
- GCC_except_table1512
- GCC_except_table1516
- GCC_except_table1517
- GCC_except_table1518
- GCC_except_table1519
- GCC_except_table1533
- GCC_except_table1534
- GCC_except_table1537
- GCC_except_table1555
- GCC_except_table1564
- GCC_except_table1575
- GCC_except_table1580
- GCC_except_table1581
- GCC_except_table1590
- GCC_except_table1593
- GCC_except_table1596
- GCC_except_table1603
- GCC_except_table1605
- GCC_except_table1614
- GCC_except_table1616
- GCC_except_table1629
- GCC_except_table1631
- GCC_except_table1635
- GCC_except_table1638
- GCC_except_table1640
- GCC_except_table1644
- GCC_except_table1659
- GCC_except_table1660
- GCC_except_table1661
- GCC_except_table1681
- GCC_except_table1683
- GCC_except_table1699
- GCC_except_table1701
- GCC_except_table1704
- GCC_except_table1708
- GCC_except_table1710
- GCC_except_table1714
- GCC_except_table1719
- GCC_except_table1724
- GCC_except_table1725
- GCC_except_table1731
- GCC_except_table1742
- GCC_except_table1744
- GCC_except_table1755
- GCC_except_table1770
- GCC_except_table1774
- GCC_except_table1776
- GCC_except_table1778
- GCC_except_table522
- GCC_except_table567
- GCC_except_table616
- GCC_except_table650
- GCC_except_table686
- GCC_except_table830
- GCC_except_table837
- GCC_except_table850
- GCC_except_table858
- GCC_except_table865
- GCC_except_table877
- GCC_except_table898
- GCC_except_table904
- GCC_except_table925
- GCC_except_table932
- GCC_except_table935
- GCC_except_table943
- OBJC_IVAR_$_BrowserWindow._windowControlShadowView
- OBJC_IVAR_$_DownloadProgressEntry._downloadSandboxTokenQueue
- OBJC_IVAR_$_DownloadProgressEntry._sandboxIdentifier
- OBJC_IVAR_$_DownloadProgressEntry._sandboxTokenForBundle
- OBJC_IVAR_$_SafariSandboxBroker._downloadMetadataFileURL
- OBJC_IVAR_$_SafariSandboxBroker._identifiersToDownloadEntries
- OBJC_IVAR_$_SafariSandboxDownloadBundleToken._downloadBundleURL
- OBJC_IVAR_$_SafariSandboxDownloadBundleToken._downloadFilename
- OBJC_IVAR_$_SafariSandboxDownloadBundleToken._downloadIdentifier
- OBJC_IVAR_$_SafariSandboxDownloadBundleToken._sandboxToken
- OBJC_IVAR_$_WindowControlShadowView._controlRelativeFrames
- OBJC_IVAR_$_WindowControlShadowView._shadowImageView
- OBJC_IVAR_$__SandboxDownloadEntry._allowsOverwrite
- OBJC_IVAR_$__SandboxDownloadEntry._downloadBundleBookmarkData
- OBJC_IVAR_$__SandboxDownloadEntry._downloadFilename
- OBJC_IVAR_$__SandboxDownloadEntry._identifier
- OBJC_IVAR_$__SandboxDownloadEntry._suggestedFilename
- OBJC_IVAR_$__SandboxDownloadEntry._unarchiver
- _CFDataDeleteBytes
- _CGContextFillEllipseInRect
- _CRLFSet
- _CSSMOID_PKCS7_SignedData
- _NetscapeCertSequenceTemplate
- _OBJC_CLASS_$_SafariSandboxDownloadBundleToken
- _OBJC_CLASS_$_WindowControlShadowView
- _OBJC_CLASS_$__SandboxDownloadEntry
- _OBJC_METACLASS_$_SafariSandboxDownloadBundleToken
- _OBJC_METACLASS_$_WindowControlShadowView
- _OBJC_METACLASS_$__SandboxDownloadEntry
- _SecAddCertificatesToKeychainFromData
- _SecCertificateAddToKeychain
- _WBSAutoTabClusteringEnabledKey
- _WBSAutoTabClusteringImmediateModeEnabledKey
- _WBSEnableGraphicIconsInCompletionListKey
- __116-[AppController downloadsManager:shouldAllowDownload:onWebView:fromSecurityOrigin:originatingURL:completionHandler:]_block_invoke
- __33-[WindowControlShadowView layout]_block_invoke
- __80-[DownloadProgressEntry _extensionTokenForSandboxToken:withDownloadBundleAtURL:]_block_invoke
- __82-[SafariSandboxBroker _moveDownloadBundleWithIdentifierToTrash:completionHandler:]_block_invoke
- __96-[DownloadsManager download:decideDestinationUsingResponse:suggestedFilename:completionHandler:]_block_invoke_2
- __OBJC_$_CLASS_METHODS_SafariSandboxDownloadBundleToken
- __OBJC_$_CLASS_METHODS_WindowControlShadowView
- __OBJC_$_CLASS_PROP_LIST_SafariSandboxDownloadBundleToken
- __OBJC_$_INSTANCE_METHODS_SafariSandboxDownloadBundleToken
- __OBJC_$_INSTANCE_METHODS_WindowControlShadowView
- __OBJC_$_INSTANCE_METHODS__SandboxDownloadEntry
- __OBJC_$_INSTANCE_VARIABLES_SafariSandboxDownloadBundleToken
- __OBJC_$_INSTANCE_VARIABLES_WindowControlShadowView
- __OBJC_$_INSTANCE_VARIABLES__SandboxDownloadEntry
- __OBJC_$_PROP_LIST_SafariSandboxDownloadBundleToken
- __OBJC_$_PROP_LIST__SandboxDownloadEntry
- __OBJC_$_PROP_LIST__SandboxEntry
- __OBJC_$_PROTOCOL_CLASS_METHODS__SandboxEntry
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__SandboxEntry
- __OBJC_$_PROTOCOL_METHOD_TYPES__SandboxEntry
- __OBJC_$_PROTOCOL_REFS__SandboxEntry
- __OBJC_CLASS_PROTOCOLS_$_SafariSandboxDownloadBundleToken
- __OBJC_CLASS_PROTOCOLS_$__SandboxDownloadEntry
- __OBJC_CLASS_RO_$_SafariSandboxDownloadBundleToken
- __OBJC_CLASS_RO_$_WindowControlShadowView
- __OBJC_CLASS_RO_$__SandboxDownloadEntry
- __OBJC_LABEL_PROTOCOL_$__SandboxEntry
- __OBJC_METACLASS_RO_$_SafariSandboxDownloadBundleToken
- __OBJC_METACLASS_RO_$_WindowControlShadowView
- __OBJC_METACLASS_RO_$__SandboxDownloadEntry
- __OBJC_PROTOCOL_$__SandboxEntry
- ___101-[SafariSandboxBrokerConnection updateFractionCompleted:forDownloadWithIdentifier:completionHandler:]_block_invoke
- ___102-[SafariSandboxBrokerConnection moveDownloadedFilesAtURLs:inDownloadWithIdentifier:completionHandler:]_block_invoke
- ___103-[SafariSandboxBrokerConnection cancelUnarchivingOperationForDownloadWithIdentifier:completionHandler:]_block_invoke
- ___106-[SafariSandboxBroker extractDownloadedArchiveWithURL:ofType:forDownloadWithIdentifier:completionHandler:]_block_invoke
- ___107-[SafariSandboxBroker _extractDownloadedArchiveWithURL:ofType:forDownloadWithIdentifier:completionHandler:]_block_invoke
- ___107-[SafariSandboxBroker _extractDownloadedArchiveWithURL:ofType:forDownloadWithIdentifier:completionHandler:]_block_invoke_2
- ___116-[AppController downloadsManager:shouldAllowDownload:onWebView:fromSecurityOrigin:originatingURL:completionHandler:]_block_invoke
- ___116-[SafariSandboxBrokerConnection extractDownloadedArchiveWithURL:ofType:forDownloadWithIdentifier:completionHandler:]_block_invoke
- ___124-[StartPageCollectionViewControllerAnimator startPageCollectionSectionProvider:updateVisibilityOfSectionsWithDataAvailable:]_block_invoke
- ___33-[WindowControlShadowView layout]_block_invoke
- ___60-[SafariSandboxBroker _dictionaryRepresentationsForEntries:]_block_invoke
- ___61+[WindowControlShadowView windowControlShadowViewWithWindow:]_block_invoke
- ___62-[DownloadProgressEntry attemptToRevealWithCompletionHandler:]_block_invoke
- ___62-[DownloadProgressEntry attemptToRevealWithCompletionHandler:]_block_invoke_2
- ___70-[DownloadsManager _loadDownloadHistoryIfNeededWithCompletionHandler:]_block_invoke_2
- ___77-[CombinedFavoritesController _favoritesContentsChangedWithModifiedBookmark:]_block_invoke
- ___79-[SafariSandboxBroker clearDownloadIdentifiersNotIncludedIn:completionHandler:]_block_invoke
- ___80-[DownloadProgressEntry _extensionTokenForSandboxToken:withDownloadBundleAtURL:]_block_invoke
- ___81-[SafariSandboxBroker moveDownloadBundleWithIdentifierToTrash:completionHandler:]_block_invoke
- ___82-[SafariSandboxBroker _moveDownloadBundleWithIdentifierToTrash:completionHandler:]_block_invoke
- ___82-[SafariSandboxBroker deleteUnusedDownloadBundleWithIdentifier:completionHandler:]_block_invoke
- ___83-[SafariSandboxBroker _deleteUnusedDownloadBundleWithIdentifier:completionHandler:]_block_invoke
- ___87-[SafariSandboxBroker getDownloadBundleURLForDownloadWithIdentifier:completionHandler:]_block_invoke
- ___88-[SafariSandboxBroker _getDownloadBundleURLForDownloadWithIdentifier:completionHandler:]_block_invoke
- ___89-[SafariSandboxBrokerConnection clearDownloadIdentifiersNotIncludedIn:completionHandler:]_block_invoke
- ___91-[SafariSandboxBroker updateFractionCompleted:forDownloadWithIdentifier:completionHandler:]_block_invoke
- ___91-[SafariSandboxBrokerConnection moveDownloadBundleWithIdentifierToTrash:completionHandler:]_block_invoke
- ___92-[SafariSandboxBroker moveDownloadedFilesAtURLs:inDownloadWithIdentifier:completionHandler:]_block_invoke
- ___92-[SafariSandboxBrokerConnection deleteUnusedDownloadBundleWithIdentifier:completionHandler:]_block_invoke
- ___93-[SafariSandboxBroker cancelUnarchivingOperationForDownloadWithIdentifier:completionHandler:]_block_invoke
- ___95-[SafariSandboxBroker _moveDownloadedFilesWithURLs:inDownloadWithIdentifier:completionHandler:]_block_invoke
- ___97-[SafariSandboxBrokerConnection getDownloadBundleURLForDownloadWithIdentifier:completionHandler:]_block_invoke
- ___block_descriptor_40_e8_32bs_e54_v24?0"SafariSandboxDownloadBundleToken"8"NSError"16l
- ___block_descriptor_40_e8_32s_e25_"NSValue"16?0"NSView"8l
- ___block_descriptor_40_e8_32s_e39_B40?0{CGRect={CGPoint=dd}{CGSize=dd}}8l
- ___block_descriptor_40_e8_32s_e40_v32?0"NSUUID"8"<_SandboxEntry>"16^B24l
- ___block_descriptor_40_ea8_32bs_e54_v24?0"SafariSandboxDownloadBundleToken"8"NSError"16l
- ___block_descriptor_40_ea8_32s_e20_v16?0"WKDownload"8l
- ___block_descriptor_40_ea8_32s_e54_v24?0"SafariSandboxDownloadBundleToken"8"NSError"16l
- ___block_descriptor_48_ea8_32bs40bs_e54_v24?0"SafariSandboxDownloadBundleToken"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8l
- ___block_descriptor_56_e8_32s40s48s_e27_q24?0"NSView"8"NSView"16l
- ___block_descriptor_64_e8_32s40s48bs_e51_v24?0"<SafariSandboxBrokerProtocol>"8"NSError"16l
- ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"NSDictionary"8"NSError"16l
- ___block_descriptor_72_ea8_32s40s48s56s64bs_e54_v24?0"SafariSandboxDownloadBundleToken"8"NSError"16l
- ___block_descriptor_73_e8_32s40s48s56r64r_e31_B32?0"NSString"8"NSURL"16Q24l
- __swift_closure_destructor.34Tm
- _addCertificateToKeychainFromData
- _kSecAsn1SequenceOfAnyTemplate
- _objc_msgSend$_addCertificateToKeyChain
- _objc_msgSend$_addPostDownloadFileWithURL:
- _objc_msgSend$_clearDownloadIdentifiersNotIncludedIn:completionHandler:
- _objc_msgSend$_deleteUnusedDownloadBundleWithIdentifier:completionHandler:
- _objc_msgSend$_dictionaryRepresentationsForEntries:
- _objc_msgSend$_downloadEntryForIdentifier:
- _objc_msgSend$_entriesOfClass:forDictionaryRepresentations:
- _objc_msgSend$_extensionTokenForSandboxToken:withDownloadBundleAtURL:
- _objc_msgSend$_extractDownloadedArchiveWithURL:ofType:forDownloadWithIdentifier:completionHandler:
- _objc_msgSend$_getDownloadBundleURLForDownloadWithIdentifier:completionHandler:
- _objc_msgSend$_initWithRequest:bytesLoaded:bytesExpected:error:download:downloadFile:postDownloadFile:downloadStage:identifier:sandboxIdentifier:mayOpenWhenDone:shouldAvoidPersistingIdentifyingInformation:profileIdentifier:
- _objc_msgSend$_loadDownloadEntriesIfNeeded
- _objc_msgSend$_moveDownloadBundleWithIdentifierToTrash:completionHandler:
- _objc_msgSend$_moveDownloadedFilesWithURLs:inDownloadWithIdentifier:completionHandler:
- _objc_msgSend$_readDownloadDataFromOldLocationIfNeeded
- _objc_msgSend$_safari_indexOfCString:
- _objc_msgSend$_safari_indexOfCharacterInCString:startOffset:
- _objc_msgSend$_saveSandboxMetadata
- _objc_msgSend$_shouldShowControlViewShadowsForAppearance:
- _objc_msgSend$_updateFractionCompleted:forDownloadWithIdentifier:completionHandler:
- _objc_msgSend$alloc
- _objc_msgSend$allowsOverwrite
- _objc_msgSend$cachedDownloadBundleURL
- _objc_msgSend$cancelUnarchivingOperationForDownloadWithIdentifier:completionHandler:
- _objc_msgSend$clearDownloadIdentifiersNotIncludedIn:completionHandler:
- _objc_msgSend$deleteUnusedDownloadBundleWithIdentifier:completionHandler:
- _objc_msgSend$downloadBundleURLError:
- _objc_msgSend$downloadFilename
- _objc_msgSend$downloadIdentifier
- _objc_msgSend$downloadProgressEntry:didResumeWithDownload:
- _objc_msgSend$downloadsManager:shouldAllowDownload:onWebView:fromSecurityOrigin:originatingURL:completionHandler:
- _objc_msgSend$extractDownloadedArchiveWithURL:ofType:forDownloadWithIdentifier:completionHandler:
- _objc_msgSend$getDownloadBundleURLForDownloadWithIdentifier:completionHandler:
- _objc_msgSend$initWithDownloadIdentifier:sandboxToken:downloadBundleURL:downloadFilename:
- _objc_msgSend$isDetailStringHighlightedForFieldEditor:
- _objc_msgSend$moveDownloadBundleWithIdentifierToTrash:completionHandler:
- _objc_msgSend$moveDownloadedFilesAtURLs:inDownloadWithIdentifier:completionHandler:
- _objc_msgSend$safari_certificateFromMultipartData
- _objc_msgSend$safari_windowControlViews
- _objc_msgSend$sandboxIdentifier
- _objc_msgSend$sandboxToken
- _objc_msgSend$setAllowsOverwrite:
- _objc_msgSend$setCachedDownloadBundleURL:
- _objc_msgSend$setDownloadBundleURL:error:
- _objc_msgSend$setDownloadFilename:
- _objc_msgSend$setSuggestedFilename:
- _objc_msgSend$setUnarchiver:
- _objc_msgSend$showRelatedTabsPreviewEnabled
- _objc_msgSend$unarchiver
- _objc_msgSend$updateFractionCompleted:forDownloadWithIdentifier:completionHandler:
- _objc_msgSend$willBeginDownloadWithBundleToken:
- _objc_msgSend$windowControlShadowViewWithWindow:
- _symbolic SaySo11WebBookmarkCG
CStrings:
+ "&channel=41"
+ "/AppleInternal/Library/Frameworks/ContextStagingIntents.framework/ContextStagingIntents"
+ "A new file was added at destination %{sensitive, mask.hash}@ right after it was deleted because it contained the same content as downloaded file at %{sensitive, mask.hash}@ before it could be moved in its place, attempting with the next unique file name"
+ "A new file was added at destination %{sensitive, mask.hash}@ right after it was deleted to be overwritten by user request before file at %{sensitive, mask.hash}@ could be moved in its place, attempting with the next unique file name"
+ "Already attempted to overwrite a file to move downloaded file at %{sensitive, mask.hash}@ by user request, do not attempt again"
+ "Attempting to delete file at %{sensitive, mask.hash}@ to be overwritten by user request with file at %{sensitive, mask.hash}@"
+ "Begin moving files from download bundle"
+ "Cannot replace file at %{sensitive}@ with file at %{sensitive}@ because they are not identical, attempting with the next unique file name"
+ "Checking if existing file at %{sensitive, mask.hash}@ contains the same data as downloaded file at %{sensitive, mask.hash}@"
+ "Could not capture download bundle bookmark for entry %{public}@: %{public}@"
+ "Could not delete download bundle at URL %{sensitive, mask.hash}@, error: %{public}@"
+ "Could not issue sandbox extension to recover download bundle"
+ "Could not issue sandbox extension to recover download bundle %@"
+ "Could not open file descriptor on download bundle at URL: %@, error: %@"
+ "Could not open file descriptor on download bundle, error: %{public}@"
+ "Could not open file descriptor on download destination at URL: %@, error: %@"
+ "Could not open file descriptor on download destination, error: %{public}@"
+ "Could not read tags on download bundle at URL: %@, error: %@"
+ "Could not read tags on download bundle, error: %{public}@"
+ "Could not set download fraction completed attribute on file: %{private}@ with POSIX error code: %d"
+ "Could not set download fraction completed attribute with POSIX error code: %d"
+ "Did delete download bundle at URL %{sensitive, mask.hash}@"
+ "Did fail to refresh download bundle URL for entry %{public}@ with URL %{sensitive, mask.hash}@, error: %{public}@; recreating bundle"
+ "Did finish moving downloaded files from download bundle %@, moved files: %@, renamed files: %@"
+ "Did finish moving downloaded files from download bundle success: %d"
+ "Did move download bundle %@ to trash at %@"
+ "Did move download bundle to trash"
+ "Did successfully delete file at %{sensitive, mask.hash}@ to be overwritten by user request with file at %{sensitive, mask.hash}@"
+ "Did successfully delete file at %{sensitive, mask.hash}@ to be replaced with identical downloaded file at %{sensitive, mask.hash}@"
+ "Download path %@ is not inside download bundle %@"
+ "Download path %{sensitive, mask.hash}@ is not in bundle at %{sensitive, mask.hash}@, ignoring, error: %{public}@"
+ "Download path is not in download bundle"
+ "DownloadEntryBundleBookmarkBlob"
+ "Failed to delete download bundle"
+ "Failed to delete download bundle at %{private}@"
+ "Failed to delete previous file at %{sensitive}@ to be overwritten by user request with file at %{sensitive}@, error: %{public}@"
+ "Failed to move download bundle to trash, error: %{public}@"
+ "Failed to move downloaded file at %{sensitive, mask.hash}@ to destination %{sensitive, mask.hash}@ because the file already exists"
+ "Failed to move downloaded file at %{sensitive, mask.hash}@ to final location, error: %{public}@"
+ "Failed to resolve download bundle bookmark for entry %{public}@: %{public}@"
+ "LibraryScrollView"
+ "Moving downloaded file %{sensitive, mask.hash}@ from download bundle"
+ "Out of bounds access of search results."
+ "Q\xf0\xf0\xf0!3"
+ "Refusing to delete a download bundle the caller does not have access to"
+ "Refusing to delete an invalid download bundle"
+ "Refusing to delete an unused download bundle the caller does not have access to"
+ "Refusing to delete an unused invalid download bundle"
+ "Refusing to extract archive that is not inside a download bundle the caller has access to"
+ "Refusing to move files out of a download bundle the caller does not have access to"
+ "Refusing to move files out of an invalid download bundle"
+ "Refusing to recover a download bundle: no download bundle found at the given path"
+ "Refusing to remove quarantine hard attribute from a file the caller does not have access to"
+ "Refusing to update the fraction completed a download bundle the caller does not have access to"
+ "Refusing to update the fraction completed an invalid download bundle"
+ "SOUIAuthorizationViewController"
+ "Safari detected an app or service that interfered with clicking. Are you sure you want to create this extension?"
+ "Safari detected an app or service that interfered with clicking. Are you sure you want to update this extension?"
+ "Tabs cannot be moved in this window"
+ "Touch ID to create an extension."
+ "Touch ID to update an extension."
+ "Unable to lazy load ContextStagingIntents framework: %s"
+ "UnifiedTabBar._sidecarScrollGestureRecognizer"
+ "Will begin moving downloaded files from download bundle"
+ "Will begin moving downloaded files from download bundle %@ to folder: %@ moved filenames: %@"
+ "Will delete download bundle at URL %{sensitive, mask.hash}@"
+ "Will move download bundle %@ to trash"
+ "Will move download bundle to trash"
+ "an internal error occurred"
+ "v20@?0@\"WKDownload\"8B16"
+ "v32@?0@\"NSURL\"8@\"NSData\"16@\"NSError\"24"
+ "v32@?0@\"NSURL\"8@\"NSString\"16@\"NSError\"24"
+ "v40@?0@\"NSURL\"8@\"NSData\"16@\"NSString\"24@\"NSError\"32"
+ "\xf0\x91a"
+ "\xf0\xf0\xf0\xf0Q"
- "&channel=42"
- "--"
- "@\"NSValue\"16@?0@\"NSView\"8"
- "A new file was added at destination %{sensitive, mask.hash}@ right after it was deleted because it contained the same content as downloaded file at %{sensitive, mask.hash}@ before it could be moved in its place for download with identifier %{public}@, attempting with the next unique file name"
- "A new file was added at destination %{sensitive, mask.hash}@ right after it was deleted to be overwritten by user request before file at %{sensitive, mask.hash}@ could be moved in its place for download with identifier %{public}@, attempting with the next unique file name"
- "Added certificate to keychain"
- "AllowsOverwrite"
- "Already attempted to overwrite a file to move downloaded file at %{sensitive, mask.hash}@ by user request for download with identifier %{public}@, do not attempt again"
- "Attempting to delete file at %{sensitive, mask.hash}@ to be overwritten by user request with file at %{sensitive, mask.hash}@ for download with identifier: %{public}@"
- "Begin moving files from download bundle with identifier %{public}@"
- "BrowserWindow._windowControlShadowView"
- "Cannot replace file at %{sensitive}@ with file at %{sensitive}@ for download with identifier: %{public}@ because they are not identical, attempting with the next unique file name"
- "Checking if existing file at %{sensitive, mask.hash}@ contains the same data as downloaded file at %{sensitive, mask.hash}@ for download with identifier: %{public}@"
- "Cloud not generate downloadBundleBookmarkData for URL %@ error: %@"
- "Cloud not generate downloadBundleURL for download identifier %{public}@ error: %@"
- "Could not consume token for download's bundle at URL %{sensitive, mask.hash}@ with error: %{public}@"
- "Could not delete download bundle at URL %{sensitive, mask.hash}@ with identifier %{public}@, error: %{public}@"
- "Could not delete sandbox metadata file at %{private}@: %{public}@"
- "Could not delete sandbox metadata file: %{public}@"
- "Could not find download bundle at %@ for download identifier %{public}@ error: %@"
- "Could not find download bundle for download identifier %{public}@ error: %{public}@"
- "Could not generate downloadBundleBookmarkData: %{public}@"
- "Could not generate downloadBundleURL for download identifier %{public}@ error: %@"
- "Could not generate downloadBundleURL for download identifier %{public}@ error: %{public}@"
- "Could not generate downloadBundleURL for download identifier %{public}@ error: %{public}@ %{sensitive}@"
- "Could not issue sandbox extension to download bundle %@ for identifier %{public}@"
- "Could not issue sandbox extension to download bundle for identifier %{public}@"
- "Could not open file descriptor on download bundle at URL: %@ for download identifier %{public}@, error: %@"
- "Could not open file descriptor on download bundle for download identifier %{public}@, error: %{public}@"
- "Could not open file descriptor on download destination at URL: %@ for download identifier %{public}@, error: %@"
- "Could not open file descriptor on download destination for download identifier %{public}@, error: %{public}@"
- "Could not read tags on download bundle at URL: %@ for download identifier %{public}@, error: %@"
- "Could not read tags on download bundle for download identifier %{public}@, error: %{public}@"
- "Could not save sandbox metadata file at %{private}@: %{public}@"
- "Could not save sandbox metadata file: %{public}@"
- "Could not set download fraction completed attribute for download identifier %{public}@ on file: %{private}@ with POSIX error code: %d"
- "Could not set download fraction completed attribute for download identifier %{public}@ with POSIX error code: %d"
- "Deleted empty download metadata file"
- "Dictionary representation contains an unreadable identifier %{public}@"
- "Dictionary representation contains empty download bundle bookmark data"
- "Dictionary representation contains empty download filename"
- "Did delete download bundle at URL %{sensitive, mask.hash}@ with identifier %{public}@"
- "Did fail to refresh download bundle URL for entry %{public}@ with URL %{sensitive, mask.hash}@, error: %{public}@"
- "Did finish moving downloaded files from download bundle %@ with identifier %{public}@, moved files: %@, renamed files: %@"
- "Did finish moving downloaded files from download bundle with identifier %{public}@ success: %d"
- "Did move download bundle with identifier %{public}@ download bundle %@ to trash at %@"
- "Did move download bundle with identifier to trash %{public}@"
- "Did successfully delete file at %{sensitive, mask.hash}@ to be overwritten by user request with file at %{sensitive, mask.hash}@ for download with identifier: %{public}@"
- "Did successfully delete file at %{sensitive, mask.hash}@ to be replaced with identical downloaded file at %{sensitive, mask.hash}@ for download with identifier: %{public}@"
- "Download path %@ is not inside download bundle %@ with identifier: %{public}@"
- "Download path %{sensitive, mask.hash}@ is not in bundle at %{sensitive, mask.hash}@ for download with identifier: %{public}@, ignoring, error: %{public}@"
- "Download path is not in download bundle with identifier: %{public}@"
- "DownloadBundleBookmarkData"
- "DownloadBundleURL"
- "DownloadEntries"
- "DownloadEntrySandboxIdentifier"
- "DownloadFilename"
- "DownloadIdentifier"
- "Failed to add certificate to keychain"
- "Failed to delete download bundle for identifier %{public}@ at %{private}@"
- "Failed to delete download bundle for identifier: %{public}@"
- "Failed to delete previous file at %{sensitive}@ to be overwritten by user request with file at %{sensitive}@ for download with identifier: %{public}@, error: %{public}@"
- "Failed to move downloaded file at %{sensitive, mask.hash}@ to destination %{sensitive, mask.hash}@ for download with identifier %{public}@ because the file already exists"
- "Failed to move downloaded file at %{sensitive, mask.hash}@ to final location for download with identifier: %{public}@ error: %{public}@"
- "Failed to moved download bundle with identifier %{public}@ error: %{public}@"
- "Invalid download entry with identifier: %{public}@"
- "Moving downloaded file %{sensitive, mask.hash}@ from download bundle for download with identifier: %{public}@"
- "Q\xf0\xf0\xf13"
- "SandboxToken"
- "SaveEntries"
- "Saved %ld download bundle entries to metadata file"
- "Saved %ld web page save entries to metadata file"
- "SuggestedFilename"
- "Will begin moving downloaded files for download with identifier %{public}@ download bundle %@ to folder: %@ moved filenames: %@"
- "Will begin moving downloaded files from download bundle with identifier %{public}@"
- "Will delete download bundle at URL %{sensitive, mask.hash}@ with identifier %{public}@"
- "Will move download bundle with identifier %{public}@ download bundle %@"
- "Will move download bundle with identifier to trash %{public}@"
- "WindowControlShadowView._shadowImageView"
- "application/x-x509-email-cert"
- "application/x-x509-user-cert"
- "com.apple.Safari.%@.%p.downloadSandboxTokenQueue"
- "com.apple.keychainaccess"
- "comgoogleapp"
- "googlechrome"
- "intent"
- "multipart/mixed"
- "p7s"
- "scheme=googlechrome"
- "v24@?0@\"SafariSandboxDownloadBundleToken\"8@\"NSError\"16"
- "v32@?0@\"NSUUID\"8@\"<_SandboxEntry>\"16^B24"
- "x509-user-cert"
- "\xf0\xb1"
- "\xf0\xc1a"
- "\xf0\xf0\xf0\xf01"
```
