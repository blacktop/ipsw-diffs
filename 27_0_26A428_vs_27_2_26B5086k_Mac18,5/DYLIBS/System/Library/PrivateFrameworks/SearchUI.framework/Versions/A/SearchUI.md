## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/Versions/A/SearchUI`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`

```diff

-673.0.12.400.0
-  __TEXT.__text: 0xcc2b8
-  __TEXT.__objc_methlist: 0xf664
-  __TEXT.__const: 0x2f34
-  __TEXT.__cstring: 0x3474
+685.1.2.0.0
+  __TEXT.__text: 0xcde94
+  __TEXT.__objc_methlist: 0xf75c
+  __TEXT.__const: 0x2f74
+  __TEXT.__cstring: 0x3534
   __TEXT.__oslogstring: 0x2635
-  __TEXT.__gcc_except_tab: 0x7ac
+  __TEXT.__gcc_except_tab: 0x7d0
   __TEXT.__ustring: 0xa8
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__swift5_typeref: 0x2c08
-  __TEXT.__constg_swiftt: 0x11bc
-  __TEXT.__swift5_reflstr: 0x56a
-  __TEXT.__swift5_fieldmd: 0x7a0
+  __TEXT.__swift5_typeref: 0x2c6e
+  __TEXT.__constg_swiftt: 0x1200
+  __TEXT.__swift5_reflstr: 0x58a
+  __TEXT.__swift5_fieldmd: 0x7bc
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x260
   __TEXT.__swift5_proto: 0x110
-  __TEXT.__swift5_types: 0xcc
-  __TEXT.__swift5_capture: 0x440
+  __TEXT.__swift5_types: 0xd0
+  __TEXT.__swift5_capture: 0x478
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift_as_entry: 0xf4
   __TEXT.__swift_as_ret: 0xdc
   __TEXT.__swift_as_cont: 0x164
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x46b8
+  __TEXT.__unwind_info: 0x4748
   __TEXT.__eh_frame: 0x1a20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x6a0
-  __DATA_CONST.__objc_classlist: 0x9c8
+  __DATA_CONST.__objc_classlist: 0x9d0
   __DATA_CONST.__objc_catlist: 0x408
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x85f8
+  __DATA_CONST.__objc_selrefs: 0x86a0
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x5c8
   __DATA_CONST.__objc_arraydata: 0xac0
-  __DATA_CONST.__got: 0x1e18
-  __AUTH_CONST.__const: 0x3c28
-  __AUTH_CONST.__cfstring: 0x3640
-  __AUTH_CONST.__objc_const: 0x1acf0
+  __DATA_CONST.__got: 0x1e28
+  __AUTH_CONST.__const: 0x3ce0
+  __AUTH_CONST.__cfstring: 0x36a0
+  __AUTH_CONST.__objc_const: 0x1ae30
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x9c0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x13f8
-  __AUTH.__objc_data: 0x3408
-  __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0xba0
-  __DATA.__data: 0x2648
+  __AUTH_CONST.__auth_got: 0x1410
+  __AUTH.__objc_data: 0x34b8
+  __AUTH.__data: 0x3c8
+  __DATA.__objc_ivar: 0xbac
+  __DATA.__data: 0x2658
   __DATA.__common: 0xe8
   __DATA_DIRTY.__objc_data: 0x3a08
-  __DATA_DIRTY.__data: 0xac0
-  __DATA_DIRTY.__bss: 0x1798
+  __DATA_DIRTY.__data: 0xb00
+  __DATA_DIRTY.__bss: 0x1790
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5907
-  Symbols:   13452
-  CStrings:  797
+  Functions: 5947
+  Symbols:   13511
+  CStrings:  803
 
Symbols:
+ +[SearchUIUtilities isCampoProcess]
+ +[SearchUIUtilities openApplicationOptionsSpotlightSource:]
+ +[SearchUIUtilities openPunchout:presentationSource:]
+ +[SearchUIUtilities openPunchout:presentationSource:completion:]
+ +[SearchUIUtilities openURL:presentationSource:withCompletion:]
+ +[SearchUIUtilities requestClipInstallWithURL:presentationSource:completion:]
+ -[SFCardSection(SearchUILeadingTrailingSectionModel) searchUILeadingTrailingSectionModel_leadingFractionalWidthForContainerWidth:]
+ -[SearchUICollectionViewController collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:]
+ -[SearchUICollectionViewController updateVisibilityOfHeaderSeparatorInSection:]
+ -[SearchUICollectionViewController updateVisibilityOfSeparator:inSection:]
+ -[SearchUICollectionViewDataSource applySnapshot:animated:completion:]
+ -[SearchUICollectionViewDataSource logSnapshotDiffFromCurrentSnapshot:toNewSnapshot:]
+ -[SearchUICommandEnvironment presentationSource]
+ -[SearchUICommandEnvironment setPresentationSource:]
+ -[SearchUIContactCache contactFetchCompletionQueue]
+ -[SearchUIContactCache contactFetchQueue]
+ -[SearchUIContactCache fetchAvailableContactsForIdentifiers:completionHandler:]
+ -[SearchUIDataSourceSnapshotBuilder generateUniqueIdentifierForBaseIdentifier:withUnavailableIdentifiers:]
+ -[SearchUILeadingTrailingSectionModel initWithCardSection:rowModels:result:queryId:section:builder:]
+ -[SearchUILeadingTrailingSectionModel rowModelsForCardSections:result:queryId:builder:]
+ OBJC_IVAR_$_SearchUICommandEnvironment._presentationSource
+ OBJC_IVAR_$_SearchUIContactCache._contactFetchCompletionQueue
+ OBJC_IVAR_$_SearchUIContactCache._contactFetchQueue
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$__TtC8SearchUI24SearchUISnippetUIMetrics
+ _OBJC_METACLASS_$__TtC8SearchUI24SearchUISnippetUIMetrics
+ _SearchUIContactCacheResultIsUnavailable
+ _SearchUIInsetFromPlatterToHighlightForStandardRow
+ __59-[SearchUICollectionViewController initWithNibName:bundle:]_block_invoke
+ __63+[SearchUIUtilities openURL:presentationSource:withCompletion:]_block_invoke
+ __64-[SearchUIContactCache computeObjectsForKeys:completionHandler:]_block_invoke
+ __70-[SearchUICollectionViewDataSource applySnapshot:animated:completion:]_block_invoke
+ __76+[SearchUILaunchAppHandler openApplicationWithBundleIdentifier:environment:]_block_invoke
+ __CLASS_METHODS__TtC8SearchUI24SearchUISnippetUIMetrics
+ __CLASS_PROPERTIES__TtC8SearchUI24SearchUISnippetUIMetrics
+ __DATA__TtC8SearchUI24SearchUISnippetUIMetrics
+ __INSTANCE_METHODS__TtC8SearchUI24SearchUISnippetUIMetrics
+ __METACLASS_DATA__TtC8SearchUI24SearchUISnippetUIMetrics
+ ___35+[SearchUIUtilities isCampoProcess]_block_invoke
+ ___58-[SearchUIPersonHeaderCardSectionView updateWithRowModel:]_block_invoke_3
+ ___63+[SearchUIUtilities openURL:presentationSource:withCompletion:]_block_invoke
+ ___64-[SearchUIContactCache computeObjectsForKeys:completionHandler:]_block_invoke
+ ___64-[SearchUIContactCache computeObjectsForKeys:completionHandler:]_block_invoke_2
+ ___70-[SearchUICollectionViewDataSource applySnapshot:animated:completion:]_block_invoke
+ ___70-[SearchUIContactCache fetchContactsForIdentifiers:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32w_e42_v16?0"SearchUICollectionViewDataSource"8l
+ ___block_descriptor_48_e8_32s40bs_e19_v16?0"CNContact"8l
+ ___block_descriptor_56_e8_32s40bs48r_e17_v16?0"NSArray"8l
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0l
+ ___copy_helper_block_e8_32s40b48r
+ ___destroy_helper_block_e8_32s40s48r
+ __swift__destructor
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$applySnapshot:animated:completion:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$contactFetchCompletionQueue
+ _objc_msgSend$contactFetchQueue
+ _objc_msgSend$fetchAvailableContactsForIdentifiers:completionHandler:
+ _objc_msgSend$generateUniqueIdentifierForBaseIdentifier:withUnavailableIdentifiers:
+ _objc_msgSend$initWithCardSection:rowModels:result:queryId:section:builder:
+ _objc_msgSend$isCampoProcess
+ _objc_msgSend$isTV
+ _objc_msgSend$islandPlatterCornerRadius
+ _objc_msgSend$logSnapshotDiffFromCurrentSnapshot:toNewSnapshot:
+ _objc_msgSend$openApplicationOptionsSpotlightSource:
+ _objc_msgSend$openPunchout:presentationSource:
+ _objc_msgSend$openPunchout:presentationSource:completion:
+ _objc_msgSend$openURL:presentationSource:withCompletion:
+ _objc_msgSend$presentationSource
+ _objc_msgSend$requestClipInstallWithURL:presentationSource:completion:
+ _objc_msgSend$rowModelsForCardSections:result:queryId:builder:
+ _objc_msgSend$searchUILeadingTrailingSectionModel_leadingFractionalWidthForContainerWidth:
+ _objc_msgSend$setPresentationSource:
+ _objc_msgSend$setUpdateCompletionBlock:
+ _objc_msgSend$updateVisibilityOfHeaderSeparatorInSection:
+ _objc_msgSend$updateVisibilityOfSeparator:inSection:
+ _objc_msgSend$viewDidUpdateHandler
+ _symbolic SSSgycSg
+ _symbolic So32SearchUICollectionViewControllerCSgXwz_Xx
+ _symbolic _____ 8SearchUI0A18UISnippetUIMetricsC
+ _symbolic _____y_____GSgXw 8SearchUI24SupplementaryHostingViewC AA6HeaderV
+ _symbolic _____y_____GSgXwz_Xx 8SearchUI24SupplementaryHostingViewC AA6HeaderV
+ isCampoProcess.isCampoProcess
+ isCampoProcess.onceToken
- +[SearchUIUtilities openApplicationOptions]
- -[SearchUIBackgroundColorView currentColorRequest]
- -[SearchUICollectionViewDataSource applySnapshot:animated:skipsDiffing:completion:]
- -[SearchUIDataSourceSnapshotBuilder generateIterativeIdentifierForBaseIdentifier:withUnavailableIdentifiers:]
- -[SearchUILeadingTrailingSectionModel initWithCardSection:rowModels:result:queryId:section:]
- -[SearchUILeadingTrailingSectionModel rowModelsForCardSections:result:queryId:]
- _SearchUISpotlightColumnTopMargin
- __44+[SearchUIUtilities openURL:withCompletion:]_block_invoke
- __76+[SearchUILaunchAppHandler openApplicationWithBundleIdentifier:environment:]_block_invoke_2
- __83-[SearchUICollectionViewDataSource applySnapshot:animated:skipsDiffing:completion:]_block_invoke
- ___43+[SearchUIUtilities openApplicationOptions]_block_invoke
- ___44+[SearchUIUtilities openURL:withCompletion:]_block_invoke
- ___76+[SearchUILaunchAppHandler openApplicationWithBundleIdentifier:environment:]_block_invoke_2
- ___83-[SearchUICollectionViewDataSource applySnapshot:animated:skipsDiffing:completion:]_block_invoke
- ___block_descriptor_40_e8_32s_e19_v16?0"CNContact"8l
- ___block_descriptor_49_e8_32bs40w_e5_v8?0l
- _objc_msgSend$applySnapshot:animated:skipsDiffing:completion:
- _objc_msgSend$generateIterativeIdentifierForBaseIdentifier:withUnavailableIdentifiers:
- _objc_msgSend$initWithCardSection:rowModels:result:queryId:section:
- _objc_msgSend$openApplicationOptions
- _objc_msgSend$openURL:withCompletion:
- _objc_msgSend$rowModelsForCardSections:result:queryId:
- openApplicationOptions.onceToken
- openApplicationWithBundleIdentifier:environment:.onceToken
- openApplicationWithBundleIdentifier:environment:.openApplicationService
- openApplicationWithBundleIdentifier:environment:.options
CStrings:
+ "\n  [NEW]  {%ld, %lu}"
+ "\n  [SKIP] {%ld, %lu}"
+ "Applied snapshot"
+ "Campo"
+ "Snapshot update summary:"
+ "com.apple.searchui.contactcache.completion"
+ "com.apple.searchui.contactcache.fetch"
+ "v16@?0@\"SearchUICollectionViewDataSource\"8"
- "%@-%ld"
- "Applied snapshot, skisDiffing %d"
```
