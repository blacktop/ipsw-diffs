## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-529.3.0.0.0
-  __TEXT.__text: 0xc4114
-  __TEXT.__auth_stubs: 0x19a0
-  __TEXT.__objc_methlist: 0xf484
-  __TEXT.__const: 0xd64
+535.0.0.0.0
+  __TEXT.__text: 0xc57f0
+  __TEXT.__auth_stubs: 0x19c0
+  __TEXT.__objc_methlist: 0xf57c
+  __TEXT.__const: 0xdd4
   __TEXT.__gcc_except_tab: 0x84c
-  __TEXT.__cstring: 0x3237
-  __TEXT.__oslogstring: 0x18cf
+  __TEXT.__cstring: 0x3257
+  __TEXT.__oslogstring: 0x19d0
   __TEXT.__ustring: 0x102
   __TEXT.__dlopen_cstrs: 0x26e
-  __TEXT.__constg_swiftt: 0x334
-  __TEXT.__swift5_typeref: 0xeba
-  __TEXT.__swift5_fieldmd: 0x210
+  __TEXT.__constg_swiftt: 0x360
+  __TEXT.__swift5_typeref: 0xee8
+  __TEXT.__swift5_fieldmd: 0x220
   __TEXT.__swift5_capture: 0x148
   __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_reflstr: 0x1d6
-  __TEXT.__swift5_proto: 0x28
+  __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_assocty: 0xb0
-  __TEXT.__unwind_info: 0x3770
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0x3790
   __TEXT.__eh_frame: 0x210
   __TEXT.__objc_classname: 0x34de
-  __TEXT.__objc_methname: 0x28ff9
-  __TEXT.__objc_methtype: 0x7375
-  __TEXT.__objc_stubs: 0x202c0
-  __DATA_CONST.__got: 0x730
+  __TEXT.__objc_methname: 0x292af
+  __TEXT.__objc_methtype: 0x7392
+  __TEXT.__objc_stubs: 0x20460
+  __DATA_CONST.__got: 0x6e8
   __DATA_CONST.__const: 0x23a8
   __DATA_CONST.__objc_classlist: 0xae0
   __DATA_CONST.__objc_catlist: 0x428
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x175c0
-  __DATA_CONST.__objc_selrefs: 0x8f28
+  __DATA_CONST.__objc_const: 0x176f0
+  __DATA_CONST.__objc_selrefs: 0x8fc0
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__objc_const: 0xade0
-  __AUTH_CONST.__const: 0x1288
-  __AUTH_CONST.__cfstring: 0x2f40
+  __AUTH_CONST.__const: 0x12c8
+  __AUTH_CONST.__cfstring: 0x2fa0
   __AUTH_CONST.__objc_doubleobj: 0x130
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_ptr: 0x50
-  __AUTH_CONST.__auth_got: 0xce0
+  __AUTH_CONST.__auth_got: 0xcf0
   __AUTH.__objc_data: 0x29a8
   __AUTH.__data: 0x1e0
   __DATA.__objc_protorefs: 0x38
   __DATA.__objc_classrefs: 0x1920
   __DATA.__objc_superrefs: 0x7d8
-  __DATA.__objc_ivar: 0xd4c
-  __DATA.__data: 0x2910
-  __DATA.__bss: 0x680
+  __DATA.__objc_ivar: 0xd50
+  __DATA.__data: 0x2908
+  __DATA.__bss: 0x690
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x4468
-  __DATA_DIRTY.__data: 0x120
+  __DATA_DIRTY.__data: 0x110
   __DATA_DIRTY.__bss: 0x378
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5616
-  Symbols:   20432
-  CStrings:  8412
+  Functions: 5643
+  Symbols:   20489
+  CStrings:  8442
 
Symbols:
+ +[SearchUIRequestUserReportHandler contextMenuForCardSection:result:feedbackRequest:environment:]
+ +[SearchUIWatchListUtilities buttonForChannelDetails:punchoutURLs:tvAppDeeplinkURL:isEntitled:isContinuing:isContainerItem:hasDescriptiveSeasonTitle:seasonNumber:episodeNumber:isHorizontallySrollingStyle:]
+ +[SnippetUIUtilities performSFCommand:rowModel:delegate:]
+ +[SnippetUIUtilities presentingViewController:delegate:]
+ +[SnippetUIUtilities supportsConfigurationForCombinedRowModel:]
+ -[SearchUIAppIconCardSectionView containerView:willMeasureArrangedSubviewsFittingSize:forReason:]
+ -[SearchUICardSectionCollectionViewCell performSFCommand:]
+ -[SearchUICardSectionCollectionViewCell presentingViewController]
+ -[SearchUICardSectionTableCell createButtons::]
+ -[SearchUICardSectionTableCell performSFCommand:]
+ -[SearchUICardSectionTableCell presentingViewController]
+ -[SearchUICardViewController shouldForceEnableThreeDTouch:]
+ -[SearchUICollectionViewCell applyLayoutAttributes:]
+ -[SearchUICombinedCardSectionTableCell createButtons::]
+ -[SearchUICombinedCardSectionTableCell performSFCommand:]
+ -[SearchUICombinedCardSectionTableCell presentingViewController]
+ -[SearchUICombinedCollectionViewCell performSFCommand:]
+ -[SearchUICombinedCollectionViewCell presentingViewController]
+ -[SearchUICopyItemHandler supportsCopy]
+ -[SearchUICoreSpotlightAppTopHitAsyncSectionLoader defaultFetchAttributes]
+ -[SearchUIGridSectionModel setCornerMaskRulesOnRowModels:forColumnCount:]
+ -[SearchUIHomeScreenAppIconView focusHighlightCornerRadius]
+ -[SearchUIHomeScreenAppIconView keyCommands]
+ -[SearchUIHomeScreenAppIconView launchWithShift]
+ -[SearchUIMultiResultAppCollectionCell hoverHighlightMargins]
+ -[SearchUIMultiResultAppCollectionCell setHoverHighlightMargins:]
+ -[SearchUIRequestUserReportHandler defaultSymbolName]
+ -[SearchUITableViewCell contextMenuActionProvider]
+ _OBJC_IVAR_$_SearchUIMultiResultAppCollectionCell._hoverHighlightMargins
+ __OBJC_CLASS_PROTOCOLS_$_SearchUICardSectionTableCell
+ __OBJC_CLASS_PROTOCOLS_$_SearchUICombinedCardSectionTableCell
+ ___73-[SearchUIGridSectionModel setCornerMaskRulesOnRowModels:forColumnCount:]_block_invoke
+ ___74-[SearchUICoreSpotlightAppTopHitAsyncSectionLoader defaultFetchAttributes]_block_invoke
+ ___79-[SearchUIOpenFileProviderItemHandler performCommand:triggerEvent:environment:]_block_invoke_2
+ ___97+[SearchUIRequestUserReportHandler contextMenuForCardSection:result:feedbackRequest:environment:]_block_invoke
+ _defaultFetchAttributes.fetchAttributes
+ _defaultFetchAttributes.onceToken
+ _objc_msgSend$buttonForChannelDetails:punchoutURLs:tvAppDeeplinkURL:isEntitled:isContinuing:isContainerItem:hasDescriptiveSeasonTitle:seasonNumber:episodeNumber:isHorizontallySrollingStyle:
+ _objc_msgSend$contextMenuForCardSection:result:feedbackRequest:environment:
+ _objc_msgSend$defaultFetchAttributes
+ _objc_msgSend$focusHighlightCornerRadius
+ _objc_msgSend$forceEnable3DTouch
+ _objc_msgSend$initWithIdentifier:bundleIdentifier:protectionClass:attributeKeys:attributeValues:type:completion:
+ _objc_msgSend$minimumInteritemSpacing
+ _objc_msgSend$minimumLineSpacing
+ _objc_msgSend$performSFCommand:rowModel:delegate:
+ _objc_msgSend$presentingViewController:delegate:
+ _objc_msgSend$setCornerMaskRulesOnRowModels:forColumnCount:
+ _objc_msgSend$setHoverHighlightMargins:
+ _objc_msgSend$setSpotlightBackingResult:
+ _objc_msgSend$shouldForceEnableThreeDTouch:
+ _objc_msgSend$spotlightItem
+ _objc_msgSend$startAccessingSecurityScopedResource
+ _objc_msgSend$stopAccessingSecurityScopedResource
+ _objc_msgSend$supportsConfigurationForCombinedRowModel:
+ _rankingPrefetchedAttributesArray
+ _swift_conformsToProtocol2
+ _symbolic $s8SearchUI19SwiftUIConfigurableP
+ _symbolic So13SFCardSectionCm
+ _symbolic So6UIViewC
- +[SearchUIWatchListUtilities buttonForChannelDetails:punchoutURLs:isEntitled:isContinuing:isContainerItem:hasDescriptiveSeasonTitle:seasonNumber:episodeNumber:isHorizontallySrollingStyle:]
- -[SearchUIAppIconCardSectionView containerView:layoutFrameForArrangedSubview:withProposedFrame:]
- -[SearchUIAppTopHitAsyncSectionLoader expectsSubtitle]
- -[SearchUIAppTopHitAsyncSectionLoader placeholderCardSections]
- -[SearchUICardSectionTableCell initWithRowModel:feedbackDelegate:]
- -[SearchUICombinedCardSectionTableCell initWithRowModel:feedbackDelegate:]
- -[SearchUIGridSectionModel setCornerMaskRulesOnRowModelsForColumnCount:]
- _MDItemBackgroundRunnable
- _MDItemContentType
- _MDItemContentURL
- _MDItemDisplayName
- _MDItemExternalID
- _MDItemFileProviderID
- _MDItemRunnableShortcutsAccessorySymbol
- _MDItemRunnableShortcutsActionIdentifier
- _MDItemRunnableShortcutsData
- _MDItemThumbnailDataPath
- _MDItemThumbnailSymbolName
- _MDItemThumbnailURL
- ___47-[SearchUIRequestUserReportHandler contextMenu]_block_invoke
- ___72-[SearchUIGridSectionModel setCornerMaskRulesOnRowModelsForColumnCount:]_block_invoke
- _objc_msgSend$buttonForChannelDetails:punchoutURLs:isEntitled:isContinuing:isContainerItem:hasDescriptiveSeasonTitle:seasonNumber:episodeNumber:isHorizontallySrollingStyle:
- _objc_msgSend$expectsSubtitle
- _objc_msgSend$initWithIdentifier:bundleIdentifier:protectionClass:attributeKeys:attributeValues:
- _objc_msgSend$setCornerMaskRulesOnRowModelsForColumnCount:
- _objc_msgSend$supportsConfiguration
- _symbolic So13SFCardSectionCSg
CStrings:
+ "@\"UIViewController\"16@0:8"
+ "@76@0:8@16@24@32B40B44B48B52@56@64B72"
+ "Failed to fetch Spotlight AppTopHit results for bundle %@ using sectionLoader %@: %@"
+ "Fetching Spotlight AppTopHit results for bundle %@ using sectionLoader %@"
+ "Priority"
+ "Successfully fetched Spotlight AppTopHit results for bundle %@ using sectionLoader %@. Count: %lu"
+ "T@?,R"
+ "T{CGSize=dd},V_hoverHighlightMargins"
+ "_hoverHighlightMargins"
+ "applyLayoutAttributes:"
+ "buttonForChannelDetails:punchoutURLs:tvAppDeeplinkURL:isEntitled:isContinuing:isContainerItem:hasDescriptiveSeasonTitle:seasonNumber:episodeNumber:isHorizontallySrollingStyle:"
+ "contextMenuActionProvider"
+ "contextMenuForCardSection:result:feedbackRequest:environment:"
+ "defaultFetchAttributes"
+ "exclamationmark.bubble"
+ "focusHighlightCornerRadius"
+ "forceEnable3DTouch"
+ "hoverHighlightMargins"
+ "initWithIdentifier:bundleIdentifier:protectionClass:attributeKeys:attributeValues:type:completion:"
+ "keyCommands"
+ "launchWithShift"
+ "minimumInteritemSpacing"
+ "minimumLineSpacing"
+ "performSFCommand:rowModel:delegate:"
+ "presentingViewController:delegate:"
+ "setCornerMaskRulesOnRowModels:forColumnCount:"
+ "setHoverHighlightMargins:"
+ "setSpotlightBackingResult:"
+ "shouldForceEnableThreeDTouch:"
+ "spotlightItem"
+ "startAccessingSecurityScopedResource"
+ "stopAccessingSecurityScopedResource"
+ "supportsConfigurationForCombinedRowModel:"
+ "verticalMarginPercentageForConfigurationOfIconView:"
- "@68@0:8@16@24B32B36B40B44@48@56B64"
- "buttonForChannelDetails:punchoutURLs:isEntitled:isContinuing:isContainerItem:hasDescriptiveSeasonTitle:seasonNumber:episodeNumber:isHorizontallySrollingStyle:"
- "expectsSubtitle"
- "initWithIdentifier:bundleIdentifier:protectionClass:attributeKeys:attributeValues:"
- "setCornerMaskRulesOnRowModelsForColumnCount:"

```
