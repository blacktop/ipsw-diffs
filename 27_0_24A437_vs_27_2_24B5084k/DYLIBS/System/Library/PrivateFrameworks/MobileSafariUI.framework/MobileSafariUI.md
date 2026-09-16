## MobileSafariUI

> `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-625.1.29.10.29
-  __TEXT.__text: 0x2d7d68
-  __TEXT.__objc_methlist: 0x24d5c
-  __TEXT.__const: 0x4e50
-  __TEXT.__gcc_except_tab: 0x1f4f4
-  __TEXT.__cstring: 0x10a84
+625.2.4.1.0
+  __TEXT.__text: 0x2d85c0
+  __TEXT.__objc_methlist: 0x24db4
+  __TEXT.__const: 0x4e60
+  __TEXT.__gcc_except_tab: 0x1f60c
+  __TEXT.__cstring: 0x10ae4
   __TEXT.__dlopen_cstrs: 0x7e6
-  __TEXT.__oslogstring: 0xb21f
+  __TEXT.__oslogstring: 0xb26f
   __TEXT.__ustring: 0x11da
   __TEXT.__swift5_typeref: 0x6499
   __TEXT.__constg_swiftt: 0x1f38

   __TEXT.__swift5_fieldmd: 0x1000
   __TEXT.__swift5_builtin: 0x1cc
   __TEXT.__swift5_assocty: 0x560
-  __TEXT.__swift5_capture: 0x2508
+  __TEXT.__swift5_capture: 0x2528
   __TEXT.__swift5_proto: 0x200
   __TEXT.__swift5_types: 0x160
   __TEXT.__swift_as_entry: 0x110

   __TEXT.__swift_as_cont: 0x2ac
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x12408
+  __TEXT.__unwind_info: 0x12430
   __TEXT.__eh_frame: 0x3834
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x98c0
+  __DATA_CONST.__const: 0x9938
   __DATA_CONST.__objc_classlist: 0xa20
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xbe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x186f0
+  __DATA_CONST.__objc_selrefs: 0x187b8
   __DATA_CONST.__objc_protorefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x690
   __DATA_CONST.__objc_arraydata: 0x368
-  __DATA_CONST.__got: 0x37f8
-  __AUTH_CONST.__const: 0x88e0
-  __AUTH_CONST.__cfstring: 0xdd20
-  __AUTH_CONST.__objc_const: 0x33458
+  __DATA_CONST.__got: 0x3810
+  __AUTH_CONST.__const: 0x8930
+  __AUTH_CONST.__cfstring: 0xdd80
+  __AUTH_CONST.__objc_const: 0x33470
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x4c8
+  __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_doubleobj: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16270
-  Symbols:   33034
-  CStrings:  3283
+  Functions: 16283
+  Symbols:   33072
+  CStrings:  3286
 
Symbols:
+ -[Application _scheduleUsageRetentionSettingsSnapshot]
+ -[BrowserController _beginSiriReaderConnection:title:text:identifier:readerContext:activeTabDocument:activationSource:invocationDescription:]
+ -[BrowserRootViewController isUsingTopCapsule]
+ -[BrowserWindowController _persistLocalTabGroupUUID:forSceneID:]
+ -[BrowserWindowController _persistedLocalTabGroupUUIDForSceneID:]
+ -[BrowserWindowController _removePersistedLocalTabGroupUUIDForSceneID:]
+ -[SearchSuggestionProvider getKeyForQueryString:isCFSearch:]
+ -[SearchSuggestionProvider previousCommittedQuery]
+ -[SearchSuggestionProvider setPreviousCommittedQuery:]
+ -[TabDocument _donateUsageRetentionEventsForExtensionsRunningOnURL:]
+ -[URLCompletionProvider _doUpdateForPrefix:completionQuery:withSearchParameters:]
+ GCC_except_table1014
+ GCC_except_table1021
+ GCC_except_table1326
+ GCC_except_table1330
+ GCC_except_table1332
+ GCC_except_table1335
+ GCC_except_table1338
+ GCC_except_table1346
+ GCC_except_table1353
+ GCC_except_table1361
+ GCC_except_table1363
+ GCC_except_table1436
+ GCC_except_table451
+ GCC_except_table578
+ GCC_except_table588
+ GCC_except_table590
+ GCC_except_table600
+ GCC_except_table622
+ GCC_except_table626
+ GCC_except_table654
+ GCC_except_table662
+ GCC_except_table696
+ GCC_except_table709
+ GCC_except_table808
+ GCC_except_table817
+ GCC_except_table827
+ GCC_except_table830
+ GCC_except_table835
+ GCC_except_table840
+ GCC_except_table850
+ GCC_except_table864
+ GCC_except_table872
+ GCC_except_table886
+ GCC_except_table914
+ GCC_except_table918
+ GCC_except_table923
+ GCC_except_table927
+ GCC_except_table930
+ GCC_except_table945
+ GCC_except_table946
+ GCC_except_table962
+ GCC_except_table965
+ _OBJC_CLASS_$_WBSAppleAccountInformationProvider
+ _OBJC_CLASS_$_WBSSearchSuggestionsCacheKey
+ _OBJC_IVAR_$_CompletionProvider._completionsCache
+ _OBJC_IVAR_$_SearchSuggestionProvider._previousCommittedQuery
+ _WBSPrefixNavigationalIntentThreshold
+ __SFLocalTabGroupUUIDsBySceneIDDefaultsKey
+ ___141-[BrowserController _beginSiriReaderConnection:title:text:identifier:readerContext:activeTabDocument:activationSource:invocationDescription:]_block_invoke
+ ___141-[BrowserController _beginSiriReaderConnection:title:text:identifier:readerContext:activeTabDocument:activationSource:invocationDescription:]_block_invoke_2
+ ___141-[BrowserController _beginSiriReaderConnection:title:text:identifier:readerContext:activeTabDocument:activationSource:invocationDescription:]_block_invoke_3
+ ___54-[Application _scheduleUsageRetentionSettingsSnapshot]_block_invoke
+ ___78-[TabController _updateContextKitSuggestionsForTabGroupWithCompletionHandler:]_block_invoke_4
+ ___block_descriptor_112_ea8_32s40s48s56s64s72s80s88r96w_e17_v16?0"UIImage"8lr88l8w96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_40_ea8_32bs_e36_v24?0"LPLinkMetadata"8"NSError"16ls32l8
+ ___block_descriptor_56_ea8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ _objc_msgSend$_doUpdateForPrefix:completionQuery:withSearchParameters:
+ _objc_msgSend$_persistLocalTabGroupUUID:forSceneID:
+ _objc_msgSend$_persistedLocalTabGroupUUIDForSceneID:
+ _objc_msgSend$_removePersistedLocalTabGroupUUIDForSceneID:
+ _objc_msgSend$_scheduleUsageRetentionSettingsSnapshot
+ _objc_msgSend$clearDonatedEventsSinceDate:
+ _objc_msgSend$donateBookmarkCreated
+ _objc_msgSend$donateBookmarkOpenedWebsite
+ _objc_msgSend$donateDistractionControlEnabled
+ _objc_msgSend$donateExtensionRanOnWebsiteWithType:
+ _objc_msgSend$donateFavoriteCreated
+ _objc_msgSend$donateFavoriteOpenedWebsite
+ _objc_msgSend$donatePrivacyReportOpenedWithKind:
+ _objc_msgSend$donatePrivateBrowsingForeground
+ _objc_msgSend$donateProfileOpenedWebsite
+ _objc_msgSend$donateProfileSwitched
+ _objc_msgSend$donateReaderEnabled
+ _objc_msgSend$donateReaderOpenedWebsite
+ _objc_msgSend$donateSearchEngineWithIdentifier:
+ _objc_msgSend$donateSettingsSnapshotWithNonDefaultProfile:iCloudTabsEnabled:syncEnabled:extensionsEnabled:
+ _objc_msgSend$donateStartPageEdited
+ _objc_msgSend$donateStartPageOpenedWebsite
+ _objc_msgSend$donateTabGroupCreated
+ _objc_msgSend$donateTabGroupEdited
+ _objc_msgSend$donateTabGroupOpened
+ _objc_msgSend$donateTabGroupOpenedWebsite
+ _objc_msgSend$enabledCount
+ _objc_msgSend$extensionStatisticsReport
+ _objc_msgSend$hasInjectedContentDataForURL:
+ _objc_msgSend$initWithQueryString:previousCommittedQuery:
+ _objc_msgSend$initWithUUID:localTabGroup:sceneID:
+ _objc_msgSend$isUsingTopCapsule
+ _objc_msgSend$localTabGroupWithUUID:
+ _objc_msgSend$mostRecentSearchQueryForSuggestionPersonalization
+ _objc_msgSend$performPageLevelAutoFillWithoutAuthentication:options:generatedPassword:earliestOneTimeCodeDate:staleOneTimeCodeThresholdDate:watchdogTimeout:completionHandler:
+ _objc_msgSend$safari_isMagicExtension
+ _objc_msgSend$setPreviousCommittedQuery:
+ _objc_msgSend$staleOneTimeCodeThresholdDate
+ _objc_msgSend$updateSuggestionsRequestWithSearchTerms:previousQuery:userAgentString:completionHandler:
- -[BrowserRootViewController usesLoweredBar]
- -[URLCompletionProvider _doUpdateForPrefix:filterResultsUsingProfileIdentifier:withSearchParameters:]
- GCC_except_table1027
- GCC_except_table1225
- GCC_except_table1312
- GCC_except_table1317
- GCC_except_table1327
- GCC_except_table1331
- GCC_except_table1334
- GCC_except_table1337
- GCC_except_table1341
- GCC_except_table1347
- GCC_except_table1354
- GCC_except_table1362
- GCC_except_table1435
- GCC_except_table368
- GCC_except_table577
- GCC_except_table583
- GCC_except_table592
- GCC_except_table624
- GCC_except_table634
- GCC_except_table646
- GCC_except_table678
- GCC_except_table690
- GCC_except_table697
- GCC_except_table725
- GCC_except_table741
- GCC_except_table749
- GCC_except_table791
- GCC_except_table798
- GCC_except_table821
- GCC_except_table822
- GCC_except_table871
- GCC_except_table889
- GCC_except_table902
- GCC_except_table921
- GCC_except_table928
- GCC_except_table942
- GCC_except_table958
- GCC_except_table959
- GCC_except_table979
- GCC_except_table984
- _OBJC_CLASS_$_SFExperimentTriggeredFeedback
- _OBJC_IVAR_$_CompletionProvider._completionsByString
- _OBJC_IVAR_$_URLCompletionProvider._bookmarkProvider
- ___45-[StartPageController _resumeBrowsingSection]_block_invoke_10
- ___48-[BrowserController _siriReadThisMenuInvocation]_block_invoke
- ___48-[BrowserController _siriReadThisMenuInvocation]_block_invoke_2
- ___49-[BrowserController _siriReadThisVocalInvocation]_block_invoke
- ___49-[BrowserController _siriReadThisVocalInvocation]_block_invoke_2
- ___75+[TabMenuProvider menuForClusterWithID:title:tabCount:location:dataSource:]_block_invoke_9
- ___block_descriptor_96_ea8_32s40s48s56s64s72s80r88w_e36_v24?0"LPLinkMetadata"8"NSError"16lw88l8r80l8s32l8s40l8s48l8s56l8s64l8s72l8
- _objc_msgSend$_doUpdateForPrefix:filterResultsUsingProfileIdentifier:withSearchParameters:
- _objc_msgSend$_externalClusterFeedbackMenuElements
- _objc_msgSend$checkServerCompletionForPrefixNavigationalIntent
- _objc_msgSend$codePathUUIDForHideIgnoredSiriSuggestedWebsites
- _objc_msgSend$didFinishLoad
- _objc_msgSend$didHideRepeatedlyIgnoredSiriSuggestedSiteWithFeedbackEvent:
- _objc_msgSend$inExperiment
- _objc_msgSend$isAllowFavoritesInFrequentlyVisitedEnabled
- _objc_msgSend$performDelayedLaunchOperations
- _objc_msgSend$performPageLevelAutoFillWithoutAuthentication:options:generatedPassword:earliestOneTimeCodeDate:watchdogTimeout:completionHandler:
- _objc_msgSend$prefixNavigationalIntentThreshold
- _objc_msgSend$setCodepathId:
- _objc_msgSend$shouldEmitTriggerLoggingForHidingIgnoredSiriSuggestedWebsite
- _objc_msgSend$shouldHideIgnoredSiriSuggestedSites
- _objc_msgSend$thresholdForHidingIgnoredSiriSuggestedSites
- _objc_msgSend$updateSuggestionsRequestWithSearchTerms:userAgentString:completionHandler:
- _objc_msgSend$usesLoweredBar
CStrings:
+ "Creating new window: uuid = %{public}@, sceneID = %{public}@, reconnected local tab group = %{public}@, retained persisted local tab group = %{public}@"
+ "LastUsageRetentionSettingsSnapshotTime"
+ "Safari requested starting playback because of %{public}@"
+ "Timed out waiting for link metadata; starting playback without a leading image"
+ "app intent based invocation"
+ "menu based invocation"
- "Creating new window: uuid = %{public}@, sceneID = %{public}@"
- "Safari requested starting playback because of app intent based invocation"
- "Safari requested starting playback because of menu based invocation"
```
