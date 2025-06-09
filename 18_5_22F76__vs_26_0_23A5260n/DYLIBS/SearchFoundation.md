## SearchFoundation

> `/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation`

```diff

-3405.13.1.0.0
-  __TEXT.__text: 0x36bfe4
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x53e9c
+3500.91.2.0.0
+  __TEXT.__text: 0x385d24
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_methlist: 0x54aac
   __TEXT.__const: 0x80
   __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x6a16
+  __TEXT.__cstring: 0x6c6c
   __TEXT.__oslogstring: 0x19a
-  __TEXT.__unwind_info: 0x81d8
-  __TEXT.__objc_classname: 0x46a1
-  __TEXT.__objc_methname: 0x2e094
-  __TEXT.__objc_methtype: 0xf694
-  __TEXT.__objc_stubs: 0x18b00
-  __DATA_CONST.__got: 0x1738
+  __TEXT.__unwind_info: 0x82b8
+  __TEXT.__objc_classname: 0x46fd
+  __TEXT.__objc_methname: 0x2ebb6
+  __TEXT.__objc_methtype: 0xf858
+  __TEXT.__objc_stubs: 0x19120
+  __DATA_CONST.__got: 0x1740
   __DATA_CONST.__const: 0xad0
-  __DATA_CONST.__objc_classlist: 0x1758
+  __DATA_CONST.__objc_classlist: 0x1778
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1610
+  __DATA_CONST.__objc_protolist: 0x1630
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7360
+  __DATA_CONST.__objc_selrefs: 0x7528
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1e48
-  __AUTH_CONST.__auth_got: 0x318
+  __DATA_CONST.__objc_superrefs: 0x1e68
+  __AUTH_CONST.__auth_got: 0x320
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0xc9a0
-  __AUTH_CONST.__objc_const: 0xa6ab8
-  __AUTH.__objc_data: 0xbdb0
-  __DATA.__objc_ivar: 0x4284
-  __DATA.__data: 0x108d8
+  __AUTH_CONST.__cfstring: 0xcd40
+  __AUTH_CONST.__objc_const: 0xa8d78
+  __AUTH.__objc_data: 0xbf40
+  __DATA.__objc_ivar: 0x4350
+  __DATA.__data: 0x10a58
   __DATA.__bss: 0xc8
-  __DATA_DIRTY.__objc_data: 0x2bc0
+  __DATA_DIRTY.__objc_data: 0x2b70
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17A5842D-ADFD-334B-BB9F-1AE1F630C486
-  Functions: 17051
-  Symbols:   52560
-  CStrings:  13430
+  UUID: C828982A-EFA1-3261-A6D0-A5027BAD5DDE
+  Functions: 17202
+  Symbols:   53019
+  CStrings:  13614
 
Symbols:
+ +[SFEmbeddingState supportsSecureCoding]
+ +[SFSpotlightEmbeddingState supportsSecureCoding]
+ -[RFSummaryItemExpandableCardSection attribution_caveat]
+ -[RFSummaryItemExpandableCardSection setAttribution_caveat:]
+ -[RFSummaryItemExpandableCardSection setThumbnail:]
+ -[RFSummaryItemExpandableCardSection thumbnail]
+ -[RFSummaryItemExpandableContent command_reference]
+ -[RFSummaryItemExpandableContent setCommand_reference:]
+ -[SFCardSection applicationBundleIdentifier]
+ -[SFCardSection copyableItems]
+ -[SFCardSection setApplicationBundleIdentifier:]
+ -[SFCardSection setCopyableItems:]
+ -[SFEmbeddingState .cxx_destruct]
+ -[SFEmbeddingState copyWithZone:]
+ -[SFEmbeddingState dictionaryRepresentation]
+ -[SFEmbeddingState encodeWithCoder:]
+ -[SFEmbeddingState hasEmbeddingResults]
+ -[SFEmbeddingState hasHasEmbeddingResults]
+ -[SFEmbeddingState hasHasHybridResults]
+ -[SFEmbeddingState hasHasKeywordResults]
+ -[SFEmbeddingState hasHasQueryEmbedding]
+ -[SFEmbeddingState hasHasResults]
+ -[SFEmbeddingState hasHasSuppressedResults]
+ -[SFEmbeddingState hasHybridResults]
+ -[SFEmbeddingState hasKeywordResults]
+ -[SFEmbeddingState hasQueryEmbedding]
+ -[SFEmbeddingState hasQueryStatus]
+ -[SFEmbeddingState hasResults]
+ -[SFEmbeddingState hasSuppressedResults]
+ -[SFEmbeddingState hash]
+ -[SFEmbeddingState initWithCoder:]
+ -[SFEmbeddingState isEqual:]
+ -[SFEmbeddingState jsonData]
+ -[SFEmbeddingState queryStatus]
+ -[SFEmbeddingState setHasEmbeddingResults:]
+ -[SFEmbeddingState setHasHybridResults:]
+ -[SFEmbeddingState setHasKeywordResults:]
+ -[SFEmbeddingState setHasQueryEmbedding:]
+ -[SFEmbeddingState setHasResults:]
+ -[SFEmbeddingState setHasSuppressedResults:]
+ -[SFEmbeddingState setQueryStatus:]
+ -[SFEmbeddingState setSpotlightEmbeddingState:]
+ -[SFEmbeddingState spotlightEmbeddingState]
+ -[SFEmbeddingState(ProtobufInitializer) initWithProtobuf:]
+ -[SFEndLocalSearchFeedback embeddingState]
+ -[SFEndLocalSearchFeedback initWithStartSearch:queryUnderstandingParse:l1ToL2ResultCount:coreSpotlightIndexCount:embeddingState:]
+ -[SFEndLocalSearchFeedback setEmbeddingState:]
+ -[SFFlightLeg lastUpdatedTime]
+ -[SFFlightLeg setLastUpdatedTime:]
+ -[SFIndexState embeddedMessageCount]
+ -[SFIndexState embeddedMessagePercentage]
+ -[SFIndexState setEmbeddedMessageCount:]
+ -[SFIndexState setEmbeddedMessagePercentage:]
+ -[SFInvokeSiriCommand hasServiceProvider]
+ -[SFInvokeSiriCommand serviceProvider]
+ -[SFInvokeSiriCommand setServiceProvider:]
+ -[SFLaunchAppCommand hasIsOnenessApplication]
+ -[SFLaunchAppCommand isOnenessApplication]
+ -[SFLaunchAppCommand setIsOnenessApplication:]
+ -[SFPerformEntityQueryCommand bundleIdentifier]
+ -[SFPerformEntityQueryCommand setBundleIdentifier:]
+ -[SFSpotlightEmbeddingState .cxx_destruct]
+ -[SFSpotlightEmbeddingState copyWithZone:]
+ -[SFSpotlightEmbeddingState dictionaryRepresentation]
+ -[SFSpotlightEmbeddingState embeddedPhotosAssetsCount]
+ -[SFSpotlightEmbeddingState embeddedPhotosAssetsPercentage]
+ -[SFSpotlightEmbeddingState encodeWithCoder:]
+ -[SFSpotlightEmbeddingState hash]
+ -[SFSpotlightEmbeddingState initWithCoder:]
+ -[SFSpotlightEmbeddingState isEqual:]
+ -[SFSpotlightEmbeddingState jsonData]
+ -[SFSpotlightEmbeddingState setEmbeddedPhotosAssetsCount:]
+ -[SFSpotlightEmbeddingState setEmbeddedPhotosAssetsPercentage:]
+ -[SFSpotlightEmbeddingState setTotalPhotosAssetsCount:]
+ -[SFSpotlightEmbeddingState totalPhotosAssetsCount]
+ -[SFSpotlightEmbeddingState(ProtobufInitializer) initWithProtobuf:]
+ -[SFStartLocalSearchFeedback coreSpotlightIndexUsed]
+ -[SFStartLocalSearchFeedback initWithInput:triggerEvent:searchType:indexType:queryId:originatingApp:coreSpotlightIndexUsed:]
+ -[SFStartLocalSearchFeedback isSemanticSearchEligible]
+ -[SFStartLocalSearchFeedback setCoreSpotlightIndexUsed:]
+ -[SFStartLocalSearchFeedback setIsSemanticSearchEligible:]
+ -[SFStartLocalSearchFeedback setSpotlightBrowsingSearchScope:]
+ -[SFStartLocalSearchFeedback setSpotlightInitialPageType:]
+ -[SFStartLocalSearchFeedback spotlightBrowsingSearchScope]
+ -[SFStartLocalSearchFeedback spotlightInitialPageType]
+ -[SFVisibleResultsFeedback isFilterBarShown]
+ -[SFVisibleResultsFeedback setIsFilterBarShown:]
+ -[_SFPBCardSection addCopyableItems:]
+ -[_SFPBCardSection applicationBundleIdentifier]
+ -[_SFPBCardSection clearCopyableItems]
+ -[_SFPBCardSection copyableItemsAtIndex:]
+ -[_SFPBCardSection copyableItemsCount]
+ -[_SFPBCardSection copyableItems]
+ -[_SFPBCardSection setApplicationBundleIdentifier:]
+ -[_SFPBCardSection setCopyableItems:]
+ -[_SFPBEmbeddingState .cxx_destruct]
+ -[_SFPBEmbeddingState dictionaryRepresentation]
+ -[_SFPBEmbeddingState hasEmbeddingResults]
+ -[_SFPBEmbeddingState hasHybridResults]
+ -[_SFPBEmbeddingState hasKeywordResults]
+ -[_SFPBEmbeddingState hasQueryEmbedding]
+ -[_SFPBEmbeddingState hasResults]
+ -[_SFPBEmbeddingState hasSuppressedResults]
+ -[_SFPBEmbeddingState hash]
+ -[_SFPBEmbeddingState initWithDictionary:]
+ -[_SFPBEmbeddingState initWithJSON:]
+ -[_SFPBEmbeddingState isEqual:]
+ -[_SFPBEmbeddingState jsonData]
+ -[_SFPBEmbeddingState queryStatus]
+ -[_SFPBEmbeddingState readFrom:]
+ -[_SFPBEmbeddingState setHasEmbeddingResults:]
+ -[_SFPBEmbeddingState setHasHybridResults:]
+ -[_SFPBEmbeddingState setHasKeywordResults:]
+ -[_SFPBEmbeddingState setHasQueryEmbedding:]
+ -[_SFPBEmbeddingState setHasResults:]
+ -[_SFPBEmbeddingState setHasSuppressedResults:]
+ -[_SFPBEmbeddingState setQueryStatus:]
+ -[_SFPBEmbeddingState setSpotlightEmbeddingState:]
+ -[_SFPBEmbeddingState spotlightEmbeddingState]
+ -[_SFPBEmbeddingState writeTo:]
+ -[_SFPBEmbeddingState(FacadeInitializer) initWithFacade:]
+ -[_SFPBFlightLeg lastUpdatedTime]
+ -[_SFPBFlightLeg setLastUpdatedTime:]
+ -[_SFPBIndexState embeddedMessageCount]
+ -[_SFPBIndexState embeddedMessagePercentage]
+ -[_SFPBIndexState setEmbeddedMessageCount:]
+ -[_SFPBIndexState setEmbeddedMessagePercentage:]
+ -[_SFPBInvokeSiriCommand serviceProvider]
+ -[_SFPBInvokeSiriCommand setServiceProvider:]
+ -[_SFPBLaunchAppCommand isOnenessApplication]
+ -[_SFPBLaunchAppCommand setIsOnenessApplication:]
+ -[_SFPBPerformEntityQueryCommand bundleIdentifier]
+ -[_SFPBPerformEntityQueryCommand setBundleIdentifier:]
+ -[_SFPBRFSummaryItemExpandableCardSection attribution_caveat]
+ -[_SFPBRFSummaryItemExpandableCardSection setAttribution_caveat:]
+ -[_SFPBRFSummaryItemExpandableCardSection setThumbnail:]
+ -[_SFPBRFSummaryItemExpandableCardSection thumbnail]
+ -[_SFPBRFSummaryItemExpandableContent command_reference]
+ -[_SFPBRFSummaryItemExpandableContent setCommand_reference:]
+ -[_SFPBSpotlightEmbeddingState dictionaryRepresentation]
+ -[_SFPBSpotlightEmbeddingState embeddedPhotosAssetsCount]
+ -[_SFPBSpotlightEmbeddingState embeddedPhotosAssetsPercentage]
+ -[_SFPBSpotlightEmbeddingState hash]
+ -[_SFPBSpotlightEmbeddingState initWithDictionary:]
+ -[_SFPBSpotlightEmbeddingState initWithJSON:]
+ -[_SFPBSpotlightEmbeddingState isEqual:]
+ -[_SFPBSpotlightEmbeddingState jsonData]
+ -[_SFPBSpotlightEmbeddingState readFrom:]
+ -[_SFPBSpotlightEmbeddingState setEmbeddedPhotosAssetsCount:]
+ -[_SFPBSpotlightEmbeddingState setEmbeddedPhotosAssetsPercentage:]
+ -[_SFPBSpotlightEmbeddingState setTotalPhotosAssetsCount:]
+ -[_SFPBSpotlightEmbeddingState totalPhotosAssetsCount]
+ -[_SFPBSpotlightEmbeddingState writeTo:]
+ -[_SFPBSpotlightEmbeddingState(FacadeInitializer) initWithFacade:]
+ GCC_except_table2754
+ GCC_except_table7900
+ _OBJC_CLASS_$_SFEmbeddingState
+ _OBJC_CLASS_$_SFSpotlightEmbeddingState
+ _OBJC_CLASS_$__SFPBEmbeddingState
+ _OBJC_CLASS_$__SFPBSpotlightEmbeddingState
+ _OBJC_IVAR_$_RFSummaryItemExpandableCardSection._attribution_caveat
+ _OBJC_IVAR_$_RFSummaryItemExpandableCardSection._thumbnail
+ _OBJC_IVAR_$_RFSummaryItemExpandableContent._command_reference
+ _OBJC_IVAR_$_SFCardSection._applicationBundleIdentifier
+ _OBJC_IVAR_$_SFCardSection._copyableItems
+ _OBJC_IVAR_$_SFEmbeddingState._has
+ _OBJC_IVAR_$_SFEmbeddingState._hasEmbeddingResults
+ _OBJC_IVAR_$_SFEmbeddingState._hasHybridResults
+ _OBJC_IVAR_$_SFEmbeddingState._hasKeywordResults
+ _OBJC_IVAR_$_SFEmbeddingState._hasQueryEmbedding
+ _OBJC_IVAR_$_SFEmbeddingState._hasResults
+ _OBJC_IVAR_$_SFEmbeddingState._hasSuppressedResults
+ _OBJC_IVAR_$_SFEmbeddingState._queryStatus
+ _OBJC_IVAR_$_SFEmbeddingState._spotlightEmbeddingState
+ _OBJC_IVAR_$_SFEndLocalSearchFeedback._embeddingState
+ _OBJC_IVAR_$_SFFlightLeg._lastUpdatedTime
+ _OBJC_IVAR_$_SFIndexState._embeddedMessageCount
+ _OBJC_IVAR_$_SFIndexState._embeddedMessagePercentage
+ _OBJC_IVAR_$_SFInvokeSiriCommand._has
+ _OBJC_IVAR_$_SFInvokeSiriCommand._serviceProvider
+ _OBJC_IVAR_$_SFLaunchAppCommand._has
+ _OBJC_IVAR_$_SFLaunchAppCommand._isOnenessApplication
+ _OBJC_IVAR_$_SFPerformEntityQueryCommand._bundleIdentifier
+ _OBJC_IVAR_$_SFSpotlightEmbeddingState._embeddedPhotosAssetsCount
+ _OBJC_IVAR_$_SFSpotlightEmbeddingState._embeddedPhotosAssetsPercentage
+ _OBJC_IVAR_$_SFSpotlightEmbeddingState._totalPhotosAssetsCount
+ _OBJC_IVAR_$_SFStartLocalSearchFeedback._coreSpotlightIndexUsed
+ _OBJC_IVAR_$_SFStartLocalSearchFeedback._isSemanticSearchEligible
+ _OBJC_IVAR_$_SFStartLocalSearchFeedback._spotlightBrowsingSearchScope
+ _OBJC_IVAR_$_SFStartLocalSearchFeedback._spotlightInitialPageType
+ _OBJC_IVAR_$_SFVisibleResultsFeedback._isFilterBarShown
+ _OBJC_IVAR_$__SFPBCardSection._applicationBundleIdentifier
+ _OBJC_IVAR_$__SFPBCardSection._copyableItems
+ _OBJC_IVAR_$__SFPBEmbeddingState._hasEmbeddingResults
+ _OBJC_IVAR_$__SFPBEmbeddingState._hasHybridResults
+ _OBJC_IVAR_$__SFPBEmbeddingState._hasKeywordResults
+ _OBJC_IVAR_$__SFPBEmbeddingState._hasQueryEmbedding
+ _OBJC_IVAR_$__SFPBEmbeddingState._hasResults
+ _OBJC_IVAR_$__SFPBEmbeddingState._hasSuppressedResults
+ _OBJC_IVAR_$__SFPBEmbeddingState._queryStatus
+ _OBJC_IVAR_$__SFPBEmbeddingState._spotlightEmbeddingState
+ _OBJC_IVAR_$__SFPBFlightLeg._lastUpdatedTime
+ _OBJC_IVAR_$__SFPBIndexState._embeddedMessageCount
+ _OBJC_IVAR_$__SFPBIndexState._embeddedMessagePercentage
+ _OBJC_IVAR_$__SFPBInvokeSiriCommand._serviceProvider
+ _OBJC_IVAR_$__SFPBLaunchAppCommand._isOnenessApplication
+ _OBJC_IVAR_$__SFPBPerformEntityQueryCommand._bundleIdentifier
+ _OBJC_IVAR_$__SFPBRFSummaryItemExpandableCardSection._attribution_caveat
+ _OBJC_IVAR_$__SFPBRFSummaryItemExpandableCardSection._thumbnail
+ _OBJC_IVAR_$__SFPBRFSummaryItemExpandableContent._command_reference
+ _OBJC_IVAR_$__SFPBSpotlightEmbeddingState._embeddedPhotosAssetsCount
+ _OBJC_IVAR_$__SFPBSpotlightEmbeddingState._embeddedPhotosAssetsPercentage
+ _OBJC_IVAR_$__SFPBSpotlightEmbeddingState._totalPhotosAssetsCount
+ _OBJC_METACLASS_$_SFEmbeddingState
+ _OBJC_METACLASS_$_SFSpotlightEmbeddingState
+ _OBJC_METACLASS_$__SFPBEmbeddingState
+ _OBJC_METACLASS_$__SFPBSpotlightEmbeddingState
+ _PARLogHandleForCategory.logHandles.0.34905
+ _PARLogHandleForCategory.logHandles.0.70263
+ _PARLogHandleForCategory.logHandles.1.34899
+ _PARLogHandleForCategory.logHandles.1.70260
+ _PARLogHandleForCategory.logHandles.2.34907
+ _PARLogHandleForCategory.logHandles.2.70265
+ _PARLogHandleForCategory.logHandles.3.34908
+ _PARLogHandleForCategory.logHandles.3.70266
+ _PARLogHandleForCategory.logHandles.4.34909
+ _PARLogHandleForCategory.logHandles.4.70268
+ _PARLogHandleForCategory.logHandles.5.34910
+ _PARLogHandleForCategory.logHandles.5.70269
+ _PARLogHandleForCategory.onceToken.34897
+ _PARLogHandleForCategory.onceToken.70259
+ __OBJC_$_CLASS_METHODS_SFEmbeddingState
+ __OBJC_$_CLASS_METHODS_SFSpotlightEmbeddingState
+ __OBJC_$_CLASS_PROP_LIST_SFEmbeddingState
+ __OBJC_$_CLASS_PROP_LIST_SFSpotlightEmbeddingState
+ __OBJC_$_CLASS_PROP_LIST__SFPBEmbeddingState
+ __OBJC_$_CLASS_PROP_LIST__SFPBSpotlightEmbeddingState
+ __OBJC_$_INSTANCE_METHODS_SFEmbeddingState(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFSpotlightEmbeddingState(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBEmbeddingState(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBSpotlightEmbeddingState(FacadeInitializer)
+ __OBJC_$_INSTANCE_VARIABLES_SFEmbeddingState
+ __OBJC_$_INSTANCE_VARIABLES_SFSpotlightEmbeddingState
+ __OBJC_$_INSTANCE_VARIABLES__SFPBEmbeddingState
+ __OBJC_$_INSTANCE_VARIABLES__SFPBSpotlightEmbeddingState
+ __OBJC_$_PROP_LIST_RFBinaryButtonCardSection.237
+ __OBJC_$_PROP_LIST_RFButtonCardSection.232
+ __OBJC_$_PROP_LIST_RFDisambiguationTitleCardSection.241
+ __OBJC_$_PROP_LIST_RFExpandableStandardCardSection.241
+ __OBJC_$_PROP_LIST_RFFactItemButtonCardSection.295
+ __OBJC_$_PROP_LIST_RFFactItemDetailedNumberCardSection.261
+ __OBJC_$_PROP_LIST_RFFactItemHeroButtonCardSection.246
+ __OBJC_$_PROP_LIST_RFFactItemHeroNumberCardSection.258
+ __OBJC_$_PROP_LIST_RFFactItemImageRightCardSection.246
+ __OBJC_$_PROP_LIST_RFFactItemShortHeroNumberCardSection.267
+ __OBJC_$_PROP_LIST_RFFactItemShortNumberCardSection.267
+ __OBJC_$_PROP_LIST_RFFactItemStandardCardSection.267
+ __OBJC_$_PROP_LIST_RFLongItemStandardCardSection.247
+ __OBJC_$_PROP_LIST_RFMapCardSection.265
+ __OBJC_$_PROP_LIST_RFMultiButtonCardSection.238
+ __OBJC_$_PROP_LIST_RFPrimaryHeaderMarqueeCardSection.255
+ __OBJC_$_PROP_LIST_RFPrimaryHeaderRichCardSection.265
+ __OBJC_$_PROP_LIST_RFPrimaryHeaderStackedImageCardSection.243
+ __OBJC_$_PROP_LIST_RFPrimaryHeaderStandardCardSection.251
+ __OBJC_$_PROP_LIST_RFReferenceCenteredCardSection.256
+ __OBJC_$_PROP_LIST_RFReferenceFootnoteCardSection.256
+ __OBJC_$_PROP_LIST_RFReferenceItemButtonCardSection.232
+ __OBJC_$_PROP_LIST_RFReferenceItemLogoCardSection.232
+ __OBJC_$_PROP_LIST_RFReferenceRichCardSection.255
+ __OBJC_$_PROP_LIST_RFReferenceStandardCardSection.241
+ __OBJC_$_PROP_LIST_RFSecondaryHeaderEmphasizedCardSection.232
+ __OBJC_$_PROP_LIST_RFSecondaryHeaderStandardCardSection.232
+ __OBJC_$_PROP_LIST_RFSimpleItemPlayerCardSection.257
+ __OBJC_$_PROP_LIST_RFSimpleItemReverseRichCardSection.257
+ __OBJC_$_PROP_LIST_RFSimpleItemRichCardSection.277
+ __OBJC_$_PROP_LIST_RFSimpleItemRichSearchResultCardSection.277
+ __OBJC_$_PROP_LIST_RFSimpleItemStandardCardSection.258
+ __OBJC_$_PROP_LIST_RFSimpleItemVisualElementCardSection.266
+ __OBJC_$_PROP_LIST_RFSummaryItemAlignedTextCardSection.267
+ __OBJC_$_PROP_LIST_RFSummaryItemButtonCardSection.285
+ __OBJC_$_PROP_LIST_RFSummaryItemDetailedTextCardSection.266
+ __OBJC_$_PROP_LIST_RFSummaryItemExpandableCardSection.275
+ __OBJC_$_PROP_LIST_RFSummaryItemExpandableContent.89
+ __OBJC_$_PROP_LIST_RFSummaryItemImageRightCardSection.262
+ __OBJC_$_PROP_LIST_RFSummaryItemPairCardSection.281
+ __OBJC_$_PROP_LIST_RFSummaryItemPairNumberCardSection.311
+ __OBJC_$_PROP_LIST_RFSummaryItemPlayerCardSection.265
+ __OBJC_$_PROP_LIST_RFSummaryItemShortNumberCardSection.272
+ __OBJC_$_PROP_LIST_RFSummaryItemStandardCardSection.266
+ __OBJC_$_PROP_LIST_RFSummaryItemSwitchV2CardSection.265
+ __OBJC_$_PROP_LIST_RFSummaryItemTextCardSection.253
+ __OBJC_$_PROP_LIST_RFTableHeaderCardSection.254
+ __OBJC_$_PROP_LIST_RFTableRowCardSection.250
+ __OBJC_$_PROP_LIST_SFActivityIndicatorCardSection.231
+ __OBJC_$_PROP_LIST_SFAppIconCardSection.231
+ __OBJC_$_PROP_LIST_SFAppLinkCardSection.239
+ __OBJC_$_PROP_LIST_SFArchiveViewCardSection.234
+ __OBJC_$_PROP_LIST_SFAttributionFooterCardSection.260
+ __OBJC_$_PROP_LIST_SFAudioPlaybackCardSection.274
+ __OBJC_$_PROP_LIST_SFButtonCardSection.244
+ __OBJC_$_PROP_LIST_SFButtonListCardSection.242
+ __OBJC_$_PROP_LIST_SFCollectionCardSection.264
+ __OBJC_$_PROP_LIST_SFColorBarCardSection.248
+ __OBJC_$_PROP_LIST_SFCombinedCardSection.232
+ __OBJC_$_PROP_LIST_SFCommandRowCardSection.259
+ __OBJC_$_PROP_LIST_SFCompactRowCardSection.258
+ __OBJC_$_PROP_LIST_SFDescriptionCardSection.329
+ __OBJC_$_PROP_LIST_SFDetailedRowCardSection.359
+ __OBJC_$_PROP_LIST_SFEmbeddingState
+ __OBJC_$_PROP_LIST_SFEmbeddingState.128
+ __OBJC_$_PROP_LIST_SFFindMyCardSection.232
+ __OBJC_$_PROP_LIST_SFFlightCardSection.246
+ __OBJC_$_PROP_LIST_SFFlightLeg.181
+ __OBJC_$_PROP_LIST_SFGridCardSection.232
+ __OBJC_$_PROP_LIST_SFHeroCardSection.264
+ __OBJC_$_PROP_LIST_SFHeroTitleCardSection.257
+ __OBJC_$_PROP_LIST_SFHorizontalButtonCardSection.232
+ __OBJC_$_PROP_LIST_SFHorizontalScrollCardSection.243
+ __OBJC_$_PROP_LIST_SFImagesCardSection.241
+ __OBJC_$_PROP_LIST_SFIndexState.107
+ __OBJC_$_PROP_LIST_SFInfoCardSection.243
+ __OBJC_$_PROP_LIST_SFInvokeSiriCommand.114
+ __OBJC_$_PROP_LIST_SFKeyValueDataCardSection.241
+ __OBJC_$_PROP_LIST_SFLargeTitleDetailedRowCardSection.250
+ __OBJC_$_PROP_LIST_SFLaunchAppCommand.113
+ __OBJC_$_PROP_LIST_SFLeadingTrailingCardSection.249
+ __OBJC_$_PROP_LIST_SFLinkPresentationCardSection.249
+ __OBJC_$_PROP_LIST_SFListenToCardSection.244
+ __OBJC_$_PROP_LIST_SFMapCardSection.288
+ __OBJC_$_PROP_LIST_SFMapPlaceCardSection.248
+ __OBJC_$_PROP_LIST_SFMapsDetailedRowCardSection.245
+ __OBJC_$_PROP_LIST_SFMediaInfoCardSection.300
+ __OBJC_$_PROP_LIST_SFMediaPlayerCardSection.242
+ __OBJC_$_PROP_LIST_SFMediaRemoteControlCardSection.245
+ __OBJC_$_PROP_LIST_SFMessageCardSection.264
+ __OBJC_$_PROP_LIST_SFMetaInfoCardSection.258
+ __OBJC_$_PROP_LIST_SFMiniCardSection.249
+ __OBJC_$_PROP_LIST_SFNewsCardSection.268
+ __OBJC_$_PROP_LIST_SFNowPlayingCardSection.239
+ __OBJC_$_PROP_LIST_SFPerformEntityQueryCommand.184
+ __OBJC_$_PROP_LIST_SFPersonHeaderCardSection.232
+ __OBJC_$_PROP_LIST_SFProductCardSection.234
+ __OBJC_$_PROP_LIST_SFResponseWrapperCardSection.255
+ __OBJC_$_PROP_LIST_SFRichTitleCardSection.398
+ __OBJC_$_PROP_LIST_SFRowCardSection.315
+ __OBJC_$_PROP_LIST_SFSafariTableOfContentsCardSection.250
+ __OBJC_$_PROP_LIST_SFScoreboardCardSection.258
+ __OBJC_$_PROP_LIST_SFSectionHeaderCardSection.235
+ __OBJC_$_PROP_LIST_SFSelectableGridCardSection.241
+ __OBJC_$_PROP_LIST_SFSocialMediaPostCardSection.292
+ __OBJC_$_PROP_LIST_SFSplitCardSection.264
+ __OBJC_$_PROP_LIST_SFSpotlightEmbeddingState
+ __OBJC_$_PROP_LIST_SFSpotlightEmbeddingState.87
+ __OBJC_$_PROP_LIST_SFStockChartCardSection.243
+ __OBJC_$_PROP_LIST_SFStrokeAnimationCardSection.247
+ __OBJC_$_PROP_LIST_SFSuggestionCardSection.284
+ __OBJC_$_PROP_LIST_SFTableHeaderRowCardSection.251
+ __OBJC_$_PROP_LIST_SFTableRowCardSection.284
+ __OBJC_$_PROP_LIST_SFTextColumnsCardSection.248
+ __OBJC_$_PROP_LIST_SFTitleCardSection.245
+ __OBJC_$_PROP_LIST_SFTrackListCardSection.239
+ __OBJC_$_PROP_LIST_SFVerticalLayoutCardSection.269
+ __OBJC_$_PROP_LIST_SFWatchListCardSection.235
+ __OBJC_$_PROP_LIST_SFWatchNowCardSection.240
+ __OBJC_$_PROP_LIST_SFWebCardSection.231
+ __OBJC_$_PROP_LIST_SFWorldMapCardSection.240
+ __OBJC_$_PROP_LIST__SFPBCardSection.1910
+ __OBJC_$_PROP_LIST__SFPBCardSectionValue.3360
+ __OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.3391
+ __OBJC_$_PROP_LIST__SFPBClockImage.3421
+ __OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.3452
+ __OBJC_$_PROP_LIST__SFPBCollectionCardSection.3489
+ __OBJC_$_PROP_LIST__SFPBCollectionStyle.3547
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.3569
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.3583
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleRow.3613
+ __OBJC_$_PROP_LIST__SFPBColor.3733
+ __OBJC_$_PROP_LIST__SFPBColorBarCardSection.3756
+ __OBJC_$_PROP_LIST__SFPBCombinedCardSection.3763
+ __OBJC_$_PROP_LIST__SFPBCommand.4553
+ __OBJC_$_PROP_LIST__SFPBCommandButtonItem.4568
+ __OBJC_$_PROP_LIST__SFPBCommandReference.4583
+ __OBJC_$_PROP_LIST__SFPBCommandRowCardSection.4606
+ __OBJC_$_PROP_LIST__SFPBCommandValue.4626
+ __OBJC_$_PROP_LIST__SFPBCompactRowCardSection.4641
+ __OBJC_$_PROP_LIST__SFPBContactButtonItem.4675
+ __OBJC_$_PROP_LIST__SFPBContactCopyItem.4690
+ __OBJC_$_PROP_LIST__SFPBContactImage.4725
+ __OBJC_$_PROP_LIST__SFPBEmbeddingState
+ __OBJC_$_PROP_LIST__SFPBEmbeddingState.5699
+ __OBJC_$_PROP_LIST__SFPBEngagementSignal.5761
+ __OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5785
+ __OBJC_$_PROP_LIST__SFPBExecuteMenuItemCommand.5800
+ __OBJC_$_PROP_LIST__SFPBExecuteToolCommand.5823
+ __OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5837
+ __OBJC_$_PROP_LIST__SFPBFillToolAppEntityParameterCommand.5860
+ __OBJC_$_PROP_LIST__SFPBFillToolAppParameterCommand.5875
+ __OBJC_$_PROP_LIST__SFPBFillToolFileParameterCommand.5890
+ __OBJC_$_PROP_LIST__SFPBFillToolParameterCommand.5897
+ __OBJC_$_PROP_LIST__SFPBFillToolPersonParameterCommand.5904
+ __OBJC_$_PROP_LIST__SFPBFindMyCardSection.5911
+ __OBJC_$_PROP_LIST__SFPBFlight.5997
+ __OBJC_$_PROP_LIST__SFPBFlightCardSection.6023
+ __OBJC_$_PROP_LIST__SFPBFlightCheckinCommand.6029
+ __OBJC_$_PROP_LIST__SFPBFlightDetails.6043
+ __OBJC_$_PROP_LIST__SFPBFlightLeg.6191
+ __OBJC_$_PROP_LIST__SFPBFormattedText.6239
+ __OBJC_$_PROP_LIST__SFPBGradientColor.6267
+ __OBJC_$_PROP_LIST__SFPBGraphicalFloat.6281
+ __OBJC_$_PROP_LIST__SFPBGridCardSection.6288
+ __OBJC_$_PROP_LIST__SFPBHashBucketDetail.6318
+ __OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.6369
+ __OBJC_$_PROP_LIST__SFPBHeroCardSection.6376
+ __OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.6391
+ __OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.6410
+ __OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.6417
+ __OBJC_$_PROP_LIST__SFPBImage.6721
+ __OBJC_$_PROP_LIST__SFPBImageCopyItem.6728
+ __OBJC_$_PROP_LIST__SFPBImageDerivedColor.6735
+ __OBJC_$_PROP_LIST__SFPBImageOption.6763
+ __OBJC_$_PROP_LIST__SFPBImagesCardSection.6791
+ __OBJC_$_PROP_LIST__SFPBIndexState.6853
+ __OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.6868
+ __OBJC_$_PROP_LIST__SFPBInfoCardSection.6898
+ __OBJC_$_PROP_LIST__SFPBInfoTuple.6942
+ __OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.6965
+ __OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.6996
+ __OBJC_$_PROP_LIST__SFPBKeyValueTuple.7004
+ __OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.7034
+ __OBJC_$_PROP_LIST__SFPBLatLng.7056
+ __OBJC_$_PROP_LIST__SFPBLaunchAppCommand.7071
+ __OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.7110
+ __OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.7140
+ __OBJC_$_PROP_LIST__SFPBListenToCardSection.7171
+ __OBJC_$_PROP_LIST__SFPBLocalImage.7185
+ __OBJC_$_PROP_LIST__SFPBLocationTypeInfo.7200
+ __OBJC_$_PROP_LIST__SFPBMailRankingSignals.7734
+ __OBJC_$_PROP_LIST__SFPBMailResultDetails.7764
+ __OBJC_$_PROP_LIST__SFPBManageReservationCommand.7770
+ __OBJC_$_PROP_LIST__SFPBMapCardSection.7846
+ __OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.7861
+ __OBJC_$_PROP_LIST__SFPBMapRegion.7907
+ __OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.7922
+ __OBJC_$_PROP_LIST__SFPBMediaArtworkImage.7937
+ __OBJC_$_PROP_LIST__SFPBMediaDetail.7952
+ __OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.8066
+ __OBJC_$_PROP_LIST__SFPBMediaItem.8146
+ __OBJC_$_PROP_LIST__SFPBMediaMetadata.8226
+ __OBJC_$_PROP_LIST__SFPBMediaOffer.8265
+ __OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.8285
+ __OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.8316
+ __OBJC_$_PROP_LIST__SFPBMessageAttachment.8331
+ __OBJC_$_PROP_LIST__SFPBMessageCardSection.8383
+ __OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.8422
+ __OBJC_$_PROP_LIST__SFPBMiniCardSection.8429
+ __OBJC_$_PROP_LIST__SFPBMonogramImage.8452
+ __OBJC_$_PROP_LIST__SFPBMoreResults.8459
+ __OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.8482
+ __OBJC_$_PROP_LIST__SFPBNewsCardSection.8513
+ __OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.8532
+ __OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.8547
+ __OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.8578
+ __OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.8593
+ __OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.8608
+ __OBJC_$_PROP_LIST__SFPBOpenMediaCommand.8623
+ __OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.8630
+ __OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.8637
+ __OBJC_$_PROP_LIST__SFPBPatternModel.8676
+ __OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.8706
+ __OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.8713
+ __OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.8784
+ __OBJC_$_PROP_LIST__SFPBPerformIntentCommand.8807
+ __OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.8814
+ __OBJC_$_PROP_LIST__SFPBPerson.8869
+ __OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.8876
+ __OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.8906
+ __OBJC_$_PROP_LIST__SFPBPhotosAlbumImage.8921
+ __OBJC_$_PROP_LIST__SFPBPhotosAttributes.8975
+ __OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.9011
+ __OBJC_$_PROP_LIST__SFPBPhotosMemoryImage.9026
+ __OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.9056
+ __OBJC_$_PROP_LIST__SFPBPin.9071
+ __OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.9104
+ __OBJC_$_PROP_LIST__SFPBPlayMediaCommand.9127
+ __OBJC_$_PROP_LIST__SFPBPlayVideoCommand.9134
+ __OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.9154
+ __OBJC_$_PROP_LIST__SFPBPointSize.9177
+ __OBJC_$_PROP_LIST__SFPBProduct.9208
+ __OBJC_$_PROP_LIST__SFPBProductAvailability.9230
+ __OBJC_$_PROP_LIST__SFPBProductCardSection.9245
+ __OBJC_$_PROP_LIST__SFPBProductInventory.9301
+ __OBJC_$_PROP_LIST__SFPBProductInventoryResult.9324
+ __OBJC_$_PROP_LIST__SFPBPunchout.9389
+ __OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.9547
+ __OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.9555
+ __OBJC_$_PROP_LIST__SFPBRFAppIconImage.9575
+ __OBJC_$_PROP_LIST__SFPBRFAspectRatio.9583
+ __OBJC_$_PROP_LIST__SFPBRFAttribution.9635
+ __OBJC_$_PROP_LIST__SFPBRFAvatarImage.9654
+ __OBJC_$_PROP_LIST__SFPBRFBadgedImage.9668
+ __OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9691
+ __OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9699
+ __OBJC_$_PROP_LIST__SFPBRFColor.9733
+ __OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.9739
+ __OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.9755
+ __OBJC_$_PROP_LIST__SFPBRFEngageable.9784
+ __OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.9819
+ __OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.9842
+ __OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.9927
+ __OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.9946
+ __OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.9953
+ __OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.9986
+ __OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.9993
+ __OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.10000
+ __OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.10007
+ __OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.10023
+ __OBJC_$_PROP_LIST__SFPBRFFont.10051
+ __OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.11162
+ __OBJC_$_PROP_LIST__SFPBRFFormattedText.10205
+ __OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.10220
+ __OBJC_$_PROP_LIST__SFPBRFImageElement.10240
+ __OBJC_$_PROP_LIST__SFPBRFImageSource.10339
+ __OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.10362
+ __OBJC_$_PROP_LIST__SFPBRFMapAnnotation.10392
+ __OBJC_$_PROP_LIST__SFPBRFMapCardSection.10459
+ __OBJC_$_PROP_LIST__SFPBRFMapMarker.10492
+ __OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.10523
+ __OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.10538
+ __OBJC_$_PROP_LIST__SFPBRFMapMarkerText.10546
+ __OBJC_$_PROP_LIST__SFPBRFMapPoint.10568
+ __OBJC_$_PROP_LIST__SFPBRFMonogramImage.10583
+ __OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.10598
+ __OBJC_$_PROP_LIST__SFPBRFOptionalBool.10605
+ __OBJC_$_PROP_LIST__SFPBRFOptionalFloat.10612
+ __OBJC_$_PROP_LIST__SFPBRFPreview.10619
+ __OBJC_$_PROP_LIST__SFPBRFPreviewList.10641
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.10656
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.10663
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.10671
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.10678
+ __OBJC_$_PROP_LIST__SFPBRFRGBValue.10708
+ __OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.10720
+ __OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.10727
+ __OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.10734
+ __OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.10741
+ __OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.10748
+ __OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.10755
+ __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.10762
+ __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.10769
+ __OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.10784
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.10799
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.10806
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.10837
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.10844
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.10851
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.10875
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.10891
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemAttribution.10915
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.10922
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.10929
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableCardSection.10968
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableContent.10983
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.11003
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.11010
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.11049
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.11056
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.11063
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.11078
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.11093
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.11100
+ __OBJC_$_PROP_LIST__SFPBRFSymbolImage.11155
+ __OBJC_$_PROP_LIST__SFPBRFTableCell.11189
+ __OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.11219
+ __OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.11265
+ __OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.11330
+ __OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.11345
+ __OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.11351
+ __OBJC_$_PROP_LIST__SFPBRFTextElement.11395
+ __OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.11401
+ __OBJC_$_PROP_LIST__SFPBRFTextProperty.11431
+ __OBJC_$_PROP_LIST__SFPBRFUrlImage.11495
+ __OBJC_$_PROP_LIST__SFPBRFVisualElement.11514
+ __OBJC_$_PROP_LIST__SFPBRFVisualProperty.11536
+ __OBJC_$_PROP_LIST__SFPBRFVisualPropertyWithAction.11551
+ __OBJC_$_PROP_LIST__SFPBReferentialCommand.11558
+ __OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.11578
+ __OBJC_$_PROP_LIST__SFPBReminder.11593
+ __OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.11600
+ __OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.11631
+ __OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.11638
+ __OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.11692
+ __OBJC_$_PROP_LIST__SFPBResultEntity.11720
+ __OBJC_$_PROP_LIST__SFPBRichText.11760
+ __OBJC_$_PROP_LIST__SFPBRichTitleCardSection.11908
+ __OBJC_$_PROP_LIST__SFPBRowCardSection.12003
+ __OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.12018
+ __OBJC_$_PROP_LIST__SFPBSafariAttributes.12032
+ __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.12078
+ __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.12094
+ __OBJC_$_PROP_LIST__SFPBScene.12116
+ __OBJC_$_PROP_LIST__SFPBScoreboardCardSection.12160
+ __OBJC_$_PROP_LIST__SFPBSearchInAppCommand.12175
+ __OBJC_$_PROP_LIST__SFPBSearchSuggestion.12253
+ __OBJC_$_PROP_LIST__SFPBSearchWebCommand.12260
+ __OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.12268
+ __OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.12298
+ __OBJC_$_PROP_LIST__SFPBShareCommand.12331
+ __OBJC_$_PROP_LIST__SFPBShareItem.12364
+ __OBJC_$_PROP_LIST__SFPBShortcutsImage.12379
+ __OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.12394
+ __OBJC_$_PROP_LIST__SFPBShowContactCardCommand.12409
+ __OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.12460
+ __OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.12475
+ __OBJC_$_PROP_LIST__SFPBShowSFCardCommand.12490
+ __OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.12497
+ __OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.12504
+ __OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.12568
+ __OBJC_$_PROP_LIST__SFPBSplitCardSection.12635
+ __OBJC_$_PROP_LIST__SFPBSportsDetail.12650
+ __OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.12678
+ __OBJC_$_PROP_LIST__SFPBSportsItem.12685
+ __OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.12716
+ __OBJC_$_PROP_LIST__SFPBSportsTeam.12748
+ __OBJC_$_PROP_LIST__SFPBSpotlightEmbeddingState
+ __OBJC_$_PROP_LIST__SFPBSpotlightEmbeddingState.12778
+ __OBJC_$_PROP_LIST__SFPBStockChartCardSection.12801
+ __OBJC_$_PROP_LIST__SFPBStoreButtonItem.12824
+ __OBJC_$_PROP_LIST__SFPBStringDictionary.12843
+ __OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.12894
+ __OBJC_$_PROP_LIST__SFPBStructuredLocation.12917
+ __OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.12950
+ __OBJC_$_PROP_LIST__SFPBSuggestionCardSection.12989
+ __OBJC_$_PROP_LIST__SFPBSymbolImage.13031
+ __OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.13055
+ __OBJC_$_PROP_LIST__SFPBTableColumnAlignment.13085
+ __OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.13153
+ __OBJC_$_PROP_LIST__SFPBTableRowCardSection.13173
+ __OBJC_$_PROP_LIST__SFPBText.13190
+ __OBJC_$_PROP_LIST__SFPBTextColumn.13212
+ __OBJC_$_PROP_LIST__SFPBTextColumnSection.13247
+ __OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.13258
+ __OBJC_$_PROP_LIST__SFPBTextCopyItem.13273
+ __OBJC_$_PROP_LIST__SFPBTimeZone.13280
+ __OBJC_$_PROP_LIST__SFPBTitleCardSection.13287
+ __OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.13294
+ __OBJC_$_PROP_LIST__SFPBToggleAudioCommand.13317
+ __OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.13341
+ __OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.13356
+ __OBJC_$_PROP_LIST__SFPBTopic.13399
+ __OBJC_$_PROP_LIST__SFPBTrack.13431
+ __OBJC_$_PROP_LIST__SFPBTrackListCardSection.13453
+ __OBJC_$_PROP_LIST__SFPBURL.13460
+ __OBJC_$_PROP_LIST__SFPBURLCopyItem.13467
+ __OBJC_$_PROP_LIST__SFPBURLImage.13482
+ __OBJC_$_PROP_LIST__SFPBURLShareItem.13489
+ __OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.13504
+ __OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.13519
+ __OBJC_$_PROP_LIST__SFPBUserActivityData.13550
+ __OBJC_$_PROP_LIST__SFPBUserActivityInfo.13573
+ __OBJC_$_PROP_LIST__SFPBUserReportRequest.13648
+ __OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.13679
+ __OBJC_$_PROP_LIST__SFPBViewEmailCommand.13685
+ __OBJC_$_PROP_LIST__SFPBWatchListButtonItem.13692
+ __OBJC_$_PROP_LIST__SFPBWatchListCardSection.13699
+ __OBJC_$_PROP_LIST__SFPBWatchListItem.13778
+ __OBJC_$_PROP_LIST__SFPBWatchNowCardSection.13792
+ __OBJC_$_PROP_LIST__SFPBWeatherColor.13839
+ __OBJC_$_PROP_LIST__SFPBWeatherDetails.13846
+ __OBJC_$_PROP_LIST__SFPBWebCardSection.13861
+ __OBJC_$_PROP_LIST__SFPBWorldMapCardSection.13884
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFEmbeddingState
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFSpotlightEmbeddingState
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBEmbeddingState
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBSpotlightEmbeddingState
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFEmbeddingState
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFSpotlightEmbeddingState
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBEmbeddingState
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBSpotlightEmbeddingState
+ __OBJC_$_PROTOCOL_REFS_SFEmbeddingState
+ __OBJC_$_PROTOCOL_REFS_SFSpotlightEmbeddingState
+ __OBJC_$_PROTOCOL_REFS__SFPBEmbeddingState
+ __OBJC_$_PROTOCOL_REFS__SFPBSpotlightEmbeddingState
+ __OBJC_CLASS_PROTOCOLS_$_SFEmbeddingState
+ __OBJC_CLASS_PROTOCOLS_$_SFSpotlightEmbeddingState
+ __OBJC_CLASS_PROTOCOLS_$__SFPBEmbeddingState
+ __OBJC_CLASS_PROTOCOLS_$__SFPBSpotlightEmbeddingState
+ __OBJC_CLASS_RO_$_SFEmbeddingState
+ __OBJC_CLASS_RO_$_SFSpotlightEmbeddingState
+ __OBJC_CLASS_RO_$__SFPBEmbeddingState
+ __OBJC_CLASS_RO_$__SFPBSpotlightEmbeddingState
+ __OBJC_LABEL_PROTOCOL_$_SFEmbeddingState
+ __OBJC_LABEL_PROTOCOL_$_SFSpotlightEmbeddingState
+ __OBJC_LABEL_PROTOCOL_$__SFPBEmbeddingState
+ __OBJC_LABEL_PROTOCOL_$__SFPBSpotlightEmbeddingState
+ __OBJC_METACLASS_RO_$_SFEmbeddingState
+ __OBJC_METACLASS_RO_$_SFSpotlightEmbeddingState
+ __OBJC_METACLASS_RO_$__SFPBEmbeddingState
+ __OBJC_METACLASS_RO_$__SFPBSpotlightEmbeddingState
+ __OBJC_PROTOCOL_$_SFEmbeddingState
+ __OBJC_PROTOCOL_$_SFSpotlightEmbeddingState
+ __OBJC_PROTOCOL_$__SFPBEmbeddingState
+ __OBJC_PROTOCOL_$__SFPBSpotlightEmbeddingState
+ __SFPBEmbeddingStateReadFrom
+ __SFPBSpotlightEmbeddingStateReadFrom
+ ___PARLogHandleForCategory_block_invoke.34903
+ ___PARLogHandleForCategory_block_invoke.70262
+ ___block_literal_global.34898
+ ___block_literal_global.35679
+ ___block_literal_global.37395
+ ___block_literal_global.70275
+ ___getDispatchQueue_block_invoke.70279
+ _getDispatchQueue.70273
+ _getDispatchQueue.onceToken.70274
+ _getDispatchQueue.queue.70276
+ _objc_msgSend$_setError
+ _objc_msgSend$attribution_caveat
+ _objc_msgSend$embeddedMessageCount
+ _objc_msgSend$embeddedMessagePercentage
+ _objc_msgSend$embeddedPhotosAssetsCount
+ _objc_msgSend$embeddedPhotosAssetsPercentage
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasEmbeddingResults
+ _objc_msgSend$hasError
+ _objc_msgSend$hasHasEmbeddingResults
+ _objc_msgSend$hasHasHybridResults
+ _objc_msgSend$hasHasKeywordResults
+ _objc_msgSend$hasHasQueryEmbedding
+ _objc_msgSend$hasHasResults
+ _objc_msgSend$hasHasSuppressedResults
+ _objc_msgSend$hasHybridResults
+ _objc_msgSend$hasIsOnenessApplication
+ _objc_msgSend$hasKeywordResults
+ _objc_msgSend$hasQueryEmbedding
+ _objc_msgSend$hasQueryStatus
+ _objc_msgSend$hasResults
+ _objc_msgSend$hasServiceProvider
+ _objc_msgSend$hasSuppressedResults
+ _objc_msgSend$initWithStartSearch:queryUnderstandingParse:l1ToL2ResultCount:coreSpotlightIndexCount:
+ _objc_msgSend$isFilterBarShown
+ _objc_msgSend$isOnenessApplication
+ _objc_msgSend$lastUpdatedTime
+ _objc_msgSend$position
+ _objc_msgSend$queryStatus
+ _objc_msgSend$serviceProvider
+ _objc_msgSend$setAttribution_caveat:
+ _objc_msgSend$setEmbeddedMessageCount:
+ _objc_msgSend$setEmbeddedMessagePercentage:
+ _objc_msgSend$setEmbeddedPhotosAssetsCount:
+ _objc_msgSend$setEmbeddedPhotosAssetsPercentage:
+ _objc_msgSend$setHasEmbeddingResults:
+ _objc_msgSend$setHasHybridResults:
+ _objc_msgSend$setHasKeywordResults:
+ _objc_msgSend$setHasQueryEmbedding:
+ _objc_msgSend$setHasResults:
+ _objc_msgSend$setHasSuppressedResults:
+ _objc_msgSend$setIsOnenessApplication:
+ _objc_msgSend$setLastUpdatedTime:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setQueryStatus:
+ _objc_msgSend$setServiceProvider:
+ _objc_msgSend$setSpotlightEmbeddingState:
+ _objc_msgSend$setTotalPhotosAssetsCount:
+ _objc_msgSend$spotlightEmbeddingState
+ _objc_msgSend$totalPhotosAssetsCount
+ _objc_unsafeClaimAutoreleasedReturnValue
- -[SFAppIconCardSection applicationBundleIdentifier]
- -[SFAppIconCardSection setApplicationBundleIdentifier:]
- -[SFStartLocalSearchFeedback coreSpotlightIndexTypeUsed]
- -[SFStartLocalSearchFeedback initWithInput:triggerEvent:searchType:indexType:queryId:originatingApp:coreSpotlightIndexTypeUsed:]
- -[SFStartLocalSearchFeedback setCoreSpotlightIndexTypeUsed:]
- GCC_except_table2751
- GCC_except_table7816
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _OBJC_IVAR_$_SFAppIconCardSection._applicationBundleIdentifier
- _OBJC_IVAR_$_SFStartLocalSearchFeedback._coreSpotlightIndexTypeUsed
- _PARLogHandleForCategory.logHandles.0.33653
- _PARLogHandleForCategory.logHandles.0.68867
- _PARLogHandleForCategory.logHandles.1.33647
- _PARLogHandleForCategory.logHandles.1.68864
- _PARLogHandleForCategory.logHandles.2.33655
- _PARLogHandleForCategory.logHandles.2.68869
- _PARLogHandleForCategory.logHandles.3.33656
- _PARLogHandleForCategory.logHandles.3.68870
- _PARLogHandleForCategory.logHandles.4.33657
- _PARLogHandleForCategory.logHandles.4.68872
- _PARLogHandleForCategory.logHandles.5.33658
- _PARLogHandleForCategory.logHandles.5.68873
- _PARLogHandleForCategory.onceToken.33645
- _PARLogHandleForCategory.onceToken.68863
- __OBJC_$_PROP_LIST_RFBinaryButtonCardSection.228
- __OBJC_$_PROP_LIST_RFButtonCardSection.223
- __OBJC_$_PROP_LIST_RFDisambiguationTitleCardSection.232
- __OBJC_$_PROP_LIST_RFExpandableStandardCardSection.232
- __OBJC_$_PROP_LIST_RFFactItemButtonCardSection.286
- __OBJC_$_PROP_LIST_RFFactItemDetailedNumberCardSection.252
- __OBJC_$_PROP_LIST_RFFactItemHeroButtonCardSection.237
- __OBJC_$_PROP_LIST_RFFactItemHeroNumberCardSection.249
- __OBJC_$_PROP_LIST_RFFactItemImageRightCardSection.237
- __OBJC_$_PROP_LIST_RFFactItemShortHeroNumberCardSection.258
- __OBJC_$_PROP_LIST_RFFactItemShortNumberCardSection.258
- __OBJC_$_PROP_LIST_RFFactItemStandardCardSection.258
- __OBJC_$_PROP_LIST_RFLongItemStandardCardSection.238
- __OBJC_$_PROP_LIST_RFMapCardSection.256
- __OBJC_$_PROP_LIST_RFMultiButtonCardSection.229
- __OBJC_$_PROP_LIST_RFPrimaryHeaderMarqueeCardSection.246
- __OBJC_$_PROP_LIST_RFPrimaryHeaderRichCardSection.256
- __OBJC_$_PROP_LIST_RFPrimaryHeaderStackedImageCardSection.234
- __OBJC_$_PROP_LIST_RFPrimaryHeaderStandardCardSection.242
- __OBJC_$_PROP_LIST_RFReferenceCenteredCardSection.247
- __OBJC_$_PROP_LIST_RFReferenceFootnoteCardSection.247
- __OBJC_$_PROP_LIST_RFReferenceItemButtonCardSection.223
- __OBJC_$_PROP_LIST_RFReferenceItemLogoCardSection.223
- __OBJC_$_PROP_LIST_RFReferenceRichCardSection.246
- __OBJC_$_PROP_LIST_RFReferenceStandardCardSection.232
- __OBJC_$_PROP_LIST_RFSecondaryHeaderEmphasizedCardSection.223
- __OBJC_$_PROP_LIST_RFSecondaryHeaderStandardCardSection.223
- __OBJC_$_PROP_LIST_RFSimpleItemPlayerCardSection.248
- __OBJC_$_PROP_LIST_RFSimpleItemReverseRichCardSection.248
- __OBJC_$_PROP_LIST_RFSimpleItemRichCardSection.268
- __OBJC_$_PROP_LIST_RFSimpleItemRichSearchResultCardSection.268
- __OBJC_$_PROP_LIST_RFSimpleItemStandardCardSection.249
- __OBJC_$_PROP_LIST_RFSimpleItemVisualElementCardSection.257
- __OBJC_$_PROP_LIST_RFSummaryItemAlignedTextCardSection.258
- __OBJC_$_PROP_LIST_RFSummaryItemButtonCardSection.276
- __OBJC_$_PROP_LIST_RFSummaryItemDetailedTextCardSection.257
- __OBJC_$_PROP_LIST_RFSummaryItemExpandableCardSection.252
- __OBJC_$_PROP_LIST_RFSummaryItemExpandableContent.80
- __OBJC_$_PROP_LIST_RFSummaryItemImageRightCardSection.253
- __OBJC_$_PROP_LIST_RFSummaryItemPairCardSection.272
- __OBJC_$_PROP_LIST_RFSummaryItemPairNumberCardSection.302
- __OBJC_$_PROP_LIST_RFSummaryItemPlayerCardSection.256
- __OBJC_$_PROP_LIST_RFSummaryItemShortNumberCardSection.263
- __OBJC_$_PROP_LIST_RFSummaryItemStandardCardSection.257
- __OBJC_$_PROP_LIST_RFSummaryItemSwitchV2CardSection.256
- __OBJC_$_PROP_LIST_RFSummaryItemTextCardSection.244
- __OBJC_$_PROP_LIST_RFTableHeaderCardSection.245
- __OBJC_$_PROP_LIST_RFTableRowCardSection.241
- __OBJC_$_PROP_LIST_SFActivityIndicatorCardSection.222
- __OBJC_$_PROP_LIST_SFAppIconCardSection.227
- __OBJC_$_PROP_LIST_SFAppLinkCardSection.230
- __OBJC_$_PROP_LIST_SFArchiveViewCardSection.225
- __OBJC_$_PROP_LIST_SFAttributionFooterCardSection.251
- __OBJC_$_PROP_LIST_SFAudioPlaybackCardSection.265
- __OBJC_$_PROP_LIST_SFButtonCardSection.235
- __OBJC_$_PROP_LIST_SFButtonListCardSection.233
- __OBJC_$_PROP_LIST_SFCollectionCardSection.255
- __OBJC_$_PROP_LIST_SFColorBarCardSection.239
- __OBJC_$_PROP_LIST_SFCombinedCardSection.223
- __OBJC_$_PROP_LIST_SFCommandRowCardSection.250
- __OBJC_$_PROP_LIST_SFCompactRowCardSection.249
- __OBJC_$_PROP_LIST_SFDescriptionCardSection.320
- __OBJC_$_PROP_LIST_SFDetailedRowCardSection.350
- __OBJC_$_PROP_LIST_SFFindMyCardSection.223
- __OBJC_$_PROP_LIST_SFFlightCardSection.237
- __OBJC_$_PROP_LIST_SFFlightLeg.176
- __OBJC_$_PROP_LIST_SFGridCardSection.223
- __OBJC_$_PROP_LIST_SFHeroCardSection.255
- __OBJC_$_PROP_LIST_SFHeroTitleCardSection.248
- __OBJC_$_PROP_LIST_SFHorizontalButtonCardSection.223
- __OBJC_$_PROP_LIST_SFHorizontalScrollCardSection.234
- __OBJC_$_PROP_LIST_SFImagesCardSection.232
- __OBJC_$_PROP_LIST_SFIndexState.97
- __OBJC_$_PROP_LIST_SFInfoCardSection.234
- __OBJC_$_PROP_LIST_SFInvokeSiriCommand.102
- __OBJC_$_PROP_LIST_SFKeyValueDataCardSection.232
- __OBJC_$_PROP_LIST_SFLargeTitleDetailedRowCardSection.241
- __OBJC_$_PROP_LIST_SFLaunchAppCommand.102
- __OBJC_$_PROP_LIST_SFLeadingTrailingCardSection.240
- __OBJC_$_PROP_LIST_SFLinkPresentationCardSection.240
- __OBJC_$_PROP_LIST_SFListenToCardSection.235
- __OBJC_$_PROP_LIST_SFMapCardSection.279
- __OBJC_$_PROP_LIST_SFMapPlaceCardSection.239
- __OBJC_$_PROP_LIST_SFMapsDetailedRowCardSection.236
- __OBJC_$_PROP_LIST_SFMediaInfoCardSection.291
- __OBJC_$_PROP_LIST_SFMediaPlayerCardSection.233
- __OBJC_$_PROP_LIST_SFMediaRemoteControlCardSection.236
- __OBJC_$_PROP_LIST_SFMessageCardSection.255
- __OBJC_$_PROP_LIST_SFMetaInfoCardSection.249
- __OBJC_$_PROP_LIST_SFMiniCardSection.240
- __OBJC_$_PROP_LIST_SFNewsCardSection.259
- __OBJC_$_PROP_LIST_SFNowPlayingCardSection.230
- __OBJC_$_PROP_LIST_SFPerformEntityQueryCommand.179
- __OBJC_$_PROP_LIST_SFPersonHeaderCardSection.223
- __OBJC_$_PROP_LIST_SFProductCardSection.225
- __OBJC_$_PROP_LIST_SFResponseWrapperCardSection.246
- __OBJC_$_PROP_LIST_SFRichTitleCardSection.389
- __OBJC_$_PROP_LIST_SFRowCardSection.306
- __OBJC_$_PROP_LIST_SFSafariTableOfContentsCardSection.241
- __OBJC_$_PROP_LIST_SFScoreboardCardSection.249
- __OBJC_$_PROP_LIST_SFSectionHeaderCardSection.226
- __OBJC_$_PROP_LIST_SFSelectableGridCardSection.232
- __OBJC_$_PROP_LIST_SFSocialMediaPostCardSection.283
- __OBJC_$_PROP_LIST_SFSplitCardSection.255
- __OBJC_$_PROP_LIST_SFStockChartCardSection.234
- __OBJC_$_PROP_LIST_SFStrokeAnimationCardSection.238
- __OBJC_$_PROP_LIST_SFSuggestionCardSection.275
- __OBJC_$_PROP_LIST_SFTableHeaderRowCardSection.242
- __OBJC_$_PROP_LIST_SFTableRowCardSection.275
- __OBJC_$_PROP_LIST_SFTextColumnsCardSection.239
- __OBJC_$_PROP_LIST_SFTitleCardSection.236
- __OBJC_$_PROP_LIST_SFTrackListCardSection.230
- __OBJC_$_PROP_LIST_SFVerticalLayoutCardSection.260
- __OBJC_$_PROP_LIST_SFWatchListCardSection.226
- __OBJC_$_PROP_LIST_SFWatchNowCardSection.231
- __OBJC_$_PROP_LIST_SFWebCardSection.222
- __OBJC_$_PROP_LIST_SFWorldMapCardSection.231
- __OBJC_$_PROP_LIST__SFPBCardSection.1895
- __OBJC_$_PROP_LIST__SFPBCardSectionValue.3345
- __OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.3376
- __OBJC_$_PROP_LIST__SFPBClockImage.3406
- __OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.3437
- __OBJC_$_PROP_LIST__SFPBCollectionCardSection.3474
- __OBJC_$_PROP_LIST__SFPBCollectionStyle.3532
- __OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.3554
- __OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.3568
- __OBJC_$_PROP_LIST__SFPBCollectionStyleRow.3598
- __OBJC_$_PROP_LIST__SFPBColor.3718
- __OBJC_$_PROP_LIST__SFPBColorBarCardSection.3741
- __OBJC_$_PROP_LIST__SFPBCombinedCardSection.3748
- __OBJC_$_PROP_LIST__SFPBCommand.4538
- __OBJC_$_PROP_LIST__SFPBCommandButtonItem.4553
- __OBJC_$_PROP_LIST__SFPBCommandReference.4568
- __OBJC_$_PROP_LIST__SFPBCommandRowCardSection.4591
- __OBJC_$_PROP_LIST__SFPBCommandValue.4611
- __OBJC_$_PROP_LIST__SFPBCompactRowCardSection.4626
- __OBJC_$_PROP_LIST__SFPBContactButtonItem.4660
- __OBJC_$_PROP_LIST__SFPBContactCopyItem.4675
- __OBJC_$_PROP_LIST__SFPBContactImage.4710
- __OBJC_$_PROP_LIST__SFPBEngagementSignal.5685
- __OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5709
- __OBJC_$_PROP_LIST__SFPBExecuteMenuItemCommand.5724
- __OBJC_$_PROP_LIST__SFPBExecuteToolCommand.5747
- __OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5761
- __OBJC_$_PROP_LIST__SFPBFillToolAppEntityParameterCommand.5784
- __OBJC_$_PROP_LIST__SFPBFillToolAppParameterCommand.5799
- __OBJC_$_PROP_LIST__SFPBFillToolFileParameterCommand.5814
- __OBJC_$_PROP_LIST__SFPBFillToolParameterCommand.5821
- __OBJC_$_PROP_LIST__SFPBFillToolPersonParameterCommand.5828
- __OBJC_$_PROP_LIST__SFPBFindMyCardSection.5835
- __OBJC_$_PROP_LIST__SFPBFlight.5921
- __OBJC_$_PROP_LIST__SFPBFlightCardSection.5947
- __OBJC_$_PROP_LIST__SFPBFlightCheckinCommand.5953
- __OBJC_$_PROP_LIST__SFPBFlightDetails.5967
- __OBJC_$_PROP_LIST__SFPBFlightLeg.6107
- __OBJC_$_PROP_LIST__SFPBFormattedText.6155
- __OBJC_$_PROP_LIST__SFPBGradientColor.6183
- __OBJC_$_PROP_LIST__SFPBGraphicalFloat.6197
- __OBJC_$_PROP_LIST__SFPBGridCardSection.6204
- __OBJC_$_PROP_LIST__SFPBHashBucketDetail.6234
- __OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.6285
- __OBJC_$_PROP_LIST__SFPBHeroCardSection.6292
- __OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.6307
- __OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.6326
- __OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.6333
- __OBJC_$_PROP_LIST__SFPBImage.6637
- __OBJC_$_PROP_LIST__SFPBImageCopyItem.6644
- __OBJC_$_PROP_LIST__SFPBImageDerivedColor.6651
- __OBJC_$_PROP_LIST__SFPBImageOption.6679
- __OBJC_$_PROP_LIST__SFPBImagesCardSection.6707
- __OBJC_$_PROP_LIST__SFPBIndexState.6753
- __OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.6768
- __OBJC_$_PROP_LIST__SFPBInfoCardSection.6798
- __OBJC_$_PROP_LIST__SFPBInfoTuple.6842
- __OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.6857
- __OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.6888
- __OBJC_$_PROP_LIST__SFPBKeyValueTuple.6896
- __OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.6926
- __OBJC_$_PROP_LIST__SFPBLatLng.6948
- __OBJC_$_PROP_LIST__SFPBLaunchAppCommand.6955
- __OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.6994
- __OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.7024
- __OBJC_$_PROP_LIST__SFPBListenToCardSection.7055
- __OBJC_$_PROP_LIST__SFPBLocalImage.7069
- __OBJC_$_PROP_LIST__SFPBLocationTypeInfo.7084
- __OBJC_$_PROP_LIST__SFPBMailRankingSignals.7618
- __OBJC_$_PROP_LIST__SFPBMailResultDetails.7648
- __OBJC_$_PROP_LIST__SFPBManageReservationCommand.7654
- __OBJC_$_PROP_LIST__SFPBMapCardSection.7730
- __OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.7745
- __OBJC_$_PROP_LIST__SFPBMapRegion.7791
- __OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.7806
- __OBJC_$_PROP_LIST__SFPBMediaArtworkImage.7821
- __OBJC_$_PROP_LIST__SFPBMediaDetail.7836
- __OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.7950
- __OBJC_$_PROP_LIST__SFPBMediaItem.8030
- __OBJC_$_PROP_LIST__SFPBMediaMetadata.8110
- __OBJC_$_PROP_LIST__SFPBMediaOffer.8149
- __OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.8169
- __OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.8200
- __OBJC_$_PROP_LIST__SFPBMessageAttachment.8215
- __OBJC_$_PROP_LIST__SFPBMessageCardSection.8267
- __OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.8306
- __OBJC_$_PROP_LIST__SFPBMiniCardSection.8313
- __OBJC_$_PROP_LIST__SFPBMonogramImage.8336
- __OBJC_$_PROP_LIST__SFPBMoreResults.8343
- __OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.8366
- __OBJC_$_PROP_LIST__SFPBNewsCardSection.8397
- __OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.8416
- __OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.8431
- __OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.8462
- __OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.8477
- __OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.8492
- __OBJC_$_PROP_LIST__SFPBOpenMediaCommand.8507
- __OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.8514
- __OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.8521
- __OBJC_$_PROP_LIST__SFPBPatternModel.8560
- __OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.8590
- __OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.8597
- __OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.8668
- __OBJC_$_PROP_LIST__SFPBPerformIntentCommand.8691
- __OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.8698
- __OBJC_$_PROP_LIST__SFPBPerson.8753
- __OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.8760
- __OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.8790
- __OBJC_$_PROP_LIST__SFPBPhotosAlbumImage.8805
- __OBJC_$_PROP_LIST__SFPBPhotosAttributes.8859
- __OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.8895
- __OBJC_$_PROP_LIST__SFPBPhotosMemoryImage.8910
- __OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.8940
- __OBJC_$_PROP_LIST__SFPBPin.8955
- __OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.8988
- __OBJC_$_PROP_LIST__SFPBPlayMediaCommand.9011
- __OBJC_$_PROP_LIST__SFPBPlayVideoCommand.9018
- __OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.9038
- __OBJC_$_PROP_LIST__SFPBPointSize.9061
- __OBJC_$_PROP_LIST__SFPBProduct.9092
- __OBJC_$_PROP_LIST__SFPBProductAvailability.9114
- __OBJC_$_PROP_LIST__SFPBProductCardSection.9129
- __OBJC_$_PROP_LIST__SFPBProductInventory.9185
- __OBJC_$_PROP_LIST__SFPBProductInventoryResult.9208
- __OBJC_$_PROP_LIST__SFPBPunchout.9273
- __OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.9431
- __OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.9439
- __OBJC_$_PROP_LIST__SFPBRFAppIconImage.9459
- __OBJC_$_PROP_LIST__SFPBRFAspectRatio.9467
- __OBJC_$_PROP_LIST__SFPBRFAttribution.9519
- __OBJC_$_PROP_LIST__SFPBRFAvatarImage.9538
- __OBJC_$_PROP_LIST__SFPBRFBadgedImage.9552
- __OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9575
- __OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9583
- __OBJC_$_PROP_LIST__SFPBRFColor.9617
- __OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.9623
- __OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.9639
- __OBJC_$_PROP_LIST__SFPBRFEngageable.9668
- __OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.9703
- __OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.9726
- __OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.9811
- __OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.9830
- __OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.9837
- __OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.9870
- __OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.9877
- __OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.9884
- __OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.9891
- __OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.9907
- __OBJC_$_PROP_LIST__SFPBRFFont.9935
- __OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.11038
- __OBJC_$_PROP_LIST__SFPBRFFormattedText.10089
- __OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.10104
- __OBJC_$_PROP_LIST__SFPBRFImageElement.10124
- __OBJC_$_PROP_LIST__SFPBRFImageSource.10223
- __OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.10246
- __OBJC_$_PROP_LIST__SFPBRFMapAnnotation.10276
- __OBJC_$_PROP_LIST__SFPBRFMapCardSection.10343
- __OBJC_$_PROP_LIST__SFPBRFMapMarker.10376
- __OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.10407
- __OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.10422
- __OBJC_$_PROP_LIST__SFPBRFMapMarkerText.10430
- __OBJC_$_PROP_LIST__SFPBRFMapPoint.10452
- __OBJC_$_PROP_LIST__SFPBRFMonogramImage.10467
- __OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.10482
- __OBJC_$_PROP_LIST__SFPBRFOptionalBool.10489
- __OBJC_$_PROP_LIST__SFPBRFOptionalFloat.10496
- __OBJC_$_PROP_LIST__SFPBRFPreview.10503
- __OBJC_$_PROP_LIST__SFPBRFPreviewList.10525
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.10540
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.10547
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.10555
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.10562
- __OBJC_$_PROP_LIST__SFPBRFRGBValue.10592
- __OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.10604
- __OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.10611
- __OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.10618
- __OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.10625
- __OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.10632
- __OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.10639
- __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.10646
- __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.10653
- __OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.10668
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.10683
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.10690
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.10721
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.10728
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.10735
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.10759
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.10775
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemAttribution.10799
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.10806
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.10813
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableCardSection.10844
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableContent.10859
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.10879
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.10886
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.10925
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.10932
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.10939
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.10954
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.10969
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.10976
- __OBJC_$_PROP_LIST__SFPBRFSymbolImage.11031
- __OBJC_$_PROP_LIST__SFPBRFTableCell.11065
- __OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.11095
- __OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.11141
- __OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.11206
- __OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.11221
- __OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.11227
- __OBJC_$_PROP_LIST__SFPBRFTextElement.11271
- __OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.11277
- __OBJC_$_PROP_LIST__SFPBRFTextProperty.11307
- __OBJC_$_PROP_LIST__SFPBRFUrlImage.11371
- __OBJC_$_PROP_LIST__SFPBRFVisualElement.11390
- __OBJC_$_PROP_LIST__SFPBRFVisualProperty.11412
- __OBJC_$_PROP_LIST__SFPBRFVisualPropertyWithAction.11427
- __OBJC_$_PROP_LIST__SFPBReferentialCommand.11434
- __OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.11454
- __OBJC_$_PROP_LIST__SFPBReminder.11469
- __OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.11476
- __OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.11507
- __OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.11514
- __OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.11568
- __OBJC_$_PROP_LIST__SFPBResultEntity.11596
- __OBJC_$_PROP_LIST__SFPBRichText.11636
- __OBJC_$_PROP_LIST__SFPBRichTitleCardSection.11784
- __OBJC_$_PROP_LIST__SFPBRowCardSection.11879
- __OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.11894
- __OBJC_$_PROP_LIST__SFPBSafariAttributes.11908
- __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.11954
- __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.11970
- __OBJC_$_PROP_LIST__SFPBScene.11992
- __OBJC_$_PROP_LIST__SFPBScoreboardCardSection.12036
- __OBJC_$_PROP_LIST__SFPBSearchInAppCommand.12051
- __OBJC_$_PROP_LIST__SFPBSearchSuggestion.12129
- __OBJC_$_PROP_LIST__SFPBSearchWebCommand.12136
- __OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.12144
- __OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.12174
- __OBJC_$_PROP_LIST__SFPBShareCommand.12207
- __OBJC_$_PROP_LIST__SFPBShareItem.12240
- __OBJC_$_PROP_LIST__SFPBShortcutsImage.12255
- __OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.12270
- __OBJC_$_PROP_LIST__SFPBShowContactCardCommand.12285
- __OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.12336
- __OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.12351
- __OBJC_$_PROP_LIST__SFPBShowSFCardCommand.12366
- __OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.12373
- __OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.12380
- __OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.12444
- __OBJC_$_PROP_LIST__SFPBSplitCardSection.12511
- __OBJC_$_PROP_LIST__SFPBSportsDetail.12526
- __OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.12554
- __OBJC_$_PROP_LIST__SFPBSportsItem.12561
- __OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.12592
- __OBJC_$_PROP_LIST__SFPBSportsTeam.12624
- __OBJC_$_PROP_LIST__SFPBStockChartCardSection.12647
- __OBJC_$_PROP_LIST__SFPBStoreButtonItem.12670
- __OBJC_$_PROP_LIST__SFPBStringDictionary.12689
- __OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.12740
- __OBJC_$_PROP_LIST__SFPBStructuredLocation.12763
- __OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.12796
- __OBJC_$_PROP_LIST__SFPBSuggestionCardSection.12835
- __OBJC_$_PROP_LIST__SFPBSymbolImage.12877
- __OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.12901
- __OBJC_$_PROP_LIST__SFPBTableColumnAlignment.12931
- __OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.12999
- __OBJC_$_PROP_LIST__SFPBTableRowCardSection.13019
- __OBJC_$_PROP_LIST__SFPBText.13036
- __OBJC_$_PROP_LIST__SFPBTextColumn.13058
- __OBJC_$_PROP_LIST__SFPBTextColumnSection.13093
- __OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.13104
- __OBJC_$_PROP_LIST__SFPBTextCopyItem.13119
- __OBJC_$_PROP_LIST__SFPBTimeZone.13126
- __OBJC_$_PROP_LIST__SFPBTitleCardSection.13133
- __OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.13140
- __OBJC_$_PROP_LIST__SFPBToggleAudioCommand.13163
- __OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.13187
- __OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.13202
- __OBJC_$_PROP_LIST__SFPBTopic.13245
- __OBJC_$_PROP_LIST__SFPBTrack.13277
- __OBJC_$_PROP_LIST__SFPBTrackListCardSection.13299
- __OBJC_$_PROP_LIST__SFPBURL.13306
- __OBJC_$_PROP_LIST__SFPBURLCopyItem.13313
- __OBJC_$_PROP_LIST__SFPBURLImage.13328
- __OBJC_$_PROP_LIST__SFPBURLShareItem.13335
- __OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.13350
- __OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.13365
- __OBJC_$_PROP_LIST__SFPBUserActivityData.13396
- __OBJC_$_PROP_LIST__SFPBUserActivityInfo.13419
- __OBJC_$_PROP_LIST__SFPBUserReportRequest.13494
- __OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.13525
- __OBJC_$_PROP_LIST__SFPBViewEmailCommand.13531
- __OBJC_$_PROP_LIST__SFPBWatchListButtonItem.13538
- __OBJC_$_PROP_LIST__SFPBWatchListCardSection.13545
- __OBJC_$_PROP_LIST__SFPBWatchListItem.13624
- __OBJC_$_PROP_LIST__SFPBWatchNowCardSection.13638
- __OBJC_$_PROP_LIST__SFPBWeatherColor.13685
- __OBJC_$_PROP_LIST__SFPBWeatherDetails.13692
- __OBJC_$_PROP_LIST__SFPBWebCardSection.13707
- __OBJC_$_PROP_LIST__SFPBWorldMapCardSection.13730
- ___PARLogHandleForCategory_block_invoke.33651
- ___PARLogHandleForCategory_block_invoke.68866
- ___block_literal_global.33646
- ___block_literal_global.34418
- ___block_literal_global.36122
- ___block_literal_global.68879
- ___getDispatchQueue_block_invoke.68883
- _getDispatchQueue.68877
- _getDispatchQueue.onceToken.68878
- _getDispatchQueue.queue.68880
- _objc_msgSend$setCoreSpotlightIndexTypeUsed:
CStrings:
+ "%@ - result: %@ - buttons: %@ - card sections: %@ - isFilterBarShown: %@"
+ "?\v"
+ "@\"SFEmbeddingState\""
+ "@\"SFSpotlightEmbeddingState\""
+ "@\"SFSpotlightEmbeddingState\"16@0:8"
+ "@\"_SFPBSpotlightEmbeddingState\""
+ "@\"_SFPBSpotlightEmbeddingState\"16@0:8"
+ "@48@0:8@16@24I32I36@40"
+ "NO"
+ "SFEmbeddingState"
+ "SFSpotlightEmbeddingState"
+ "T@\"NSDate\",C,N,V_lastUpdatedTime"
+ "T@\"NSNumber\",C,N,V_embeddedMessageCount"
+ "T@\"NSNumber\",C,N,V_embeddedMessagePercentage"
+ "T@\"NSNumber\",C,N,V_embeddedPhotosAssetsCount"
+ "T@\"NSNumber\",C,N,V_embeddedPhotosAssetsPercentage"
+ "T@\"NSNumber\",C,N,V_totalPhotosAssetsCount"
+ "T@\"RFTextProperty\",&,N,V_attribution_caveat"
+ "T@\"SFCopyItem\",N"
+ "T@\"SFCopyItem\",N,V_copyableItems"
+ "T@\"SFEmbeddingState\",N,V_embeddingState"
+ "T@\"SFSpotlightEmbeddingState\",&,N"
+ "T@\"SFSpotlightEmbeddingState\",&,N,V_spotlightEmbeddingState"
+ "T@\"_SFPBDate\",&,N,V_lastUpdatedTime"
+ "T@\"_SFPBRFTextProperty\",&,N,V_attribution_caveat"
+ "T@\"_SFPBSpotlightEmbeddingState\",&,N"
+ "T@\"_SFPBSpotlightEmbeddingState\",&,N,V_spotlightEmbeddingState"
+ "TB,N,V_hasEmbeddingResults"
+ "TB,N,V_hasHybridResults"
+ "TB,N,V_hasKeywordResults"
+ "TB,N,V_hasQueryEmbedding"
+ "TB,N,V_hasResults"
+ "TB,N,V_hasSuppressedResults"
+ "TB,N,V_isFilterBarShown"
+ "TB,N,V_isOnenessApplication"
+ "TB,N,V_isSemanticSearchEligible"
+ "Ti,N,V_embeddedMessageCount"
+ "Ti,N,V_embeddedMessagePercentage"
+ "Ti,N,V_embeddedPhotosAssetsCount"
+ "Ti,N,V_embeddedPhotosAssetsPercentage"
+ "Ti,N,V_queryStatus"
+ "Ti,N,V_serviceProvider"
+ "Ti,N,V_spotlightBrowsingSearchScope"
+ "Ti,N,V_spotlightInitialPageType"
+ "Ti,N,V_totalPhotosAssetsCount"
+ "YES"
+ "_SFPBEmbeddingState"
+ "_SFPBSpotlightEmbeddingState"
+ "_attribution_caveat"
+ "_embeddedMessageCount"
+ "_embeddedMessagePercentage"
+ "_embeddedPhotosAssetsCount"
+ "_embeddedPhotosAssetsPercentage"
+ "_embeddingState"
+ "_hasEmbeddingResults"
+ "_hasHybridResults"
+ "_hasKeywordResults"
+ "_hasQueryEmbedding"
+ "_hasResults"
+ "_hasSuppressedResults"
+ "_isFilterBarShown"
+ "_isOnenessApplication"
+ "_isSemanticSearchEligible"
+ "_lastUpdatedTime"
+ "_queryStatus"
+ "_serviceProvider"
+ "_setError"
+ "_spotlightBrowsingSearchScope"
+ "_spotlightEmbeddingState"
+ "_spotlightInitialPageType"
+ "_totalPhotosAssetsCount"
+ "attributionCaveat"
+ "attribution_caveat"
+ "embeddedMessageCount"
+ "embeddedMessagePercentage"
+ "embeddedPhotosAssetsCount"
+ "embeddedPhotosAssetsPercentage"
+ "embeddingState"
+ "getBytes:range:"
+ "hasEmbeddingResults"
+ "hasError"
+ "hasHasEmbeddingResults"
+ "hasHasHybridResults"
+ "hasHasKeywordResults"
+ "hasHasQueryEmbedding"
+ "hasHasResults"
+ "hasHasSuppressedResults"
+ "hasHybridResults"
+ "hasIsOnenessApplication"
+ "hasKeywordResults"
+ "hasQueryEmbedding"
+ "hasQueryStatus"
+ "hasResults"
+ "hasServiceProvider"
+ "hasSuppressedResults"
+ "initWithInput:triggerEvent:searchType:indexType:queryId:originatingApp:coreSpotlightIndexUsed:"
+ "initWithStartSearch:queryUnderstandingParse:l1ToL2ResultCount:coreSpotlightIndexCount:embeddingState:"
+ "isFilterBarShown"
+ "isOnenessApplication"
+ "isSemanticSearchEligible"
+ "lastUpdatedTime"
+ "position"
+ "queryStatus"
+ "serviceProvider"
+ "setAttribution_caveat:"
+ "setEmbeddedMessageCount:"
+ "setEmbeddedMessagePercentage:"
+ "setEmbeddedPhotosAssetsCount:"
+ "setEmbeddedPhotosAssetsPercentage:"
+ "setEmbeddingState:"
+ "setHasEmbeddingResults:"
+ "setHasHybridResults:"
+ "setHasKeywordResults:"
+ "setHasQueryEmbedding:"
+ "setHasResults:"
+ "setHasSuppressedResults:"
+ "setIsFilterBarShown:"
+ "setIsOnenessApplication:"
+ "setIsSemanticSearchEligible:"
+ "setLastUpdatedTime:"
+ "setPosition:"
+ "setQueryStatus:"
+ "setServiceProvider:"
+ "setSpotlightBrowsingSearchScope:"
+ "setSpotlightEmbeddingState:"
+ "setSpotlightInitialPageType:"
+ "setTotalPhotosAssetsCount:"
+ "spotlightBrowsingSearchScope"
+ "spotlightEmbeddingState"
+ "spotlightInitialPageType"
+ "totalPhotosAssetsCount"
+ "v24@0:8@\"SFSpotlightEmbeddingState\"16"
+ "v24@0:8@\"_SFPBSpotlightEmbeddingState\"16"
+ "{?=\"isOnenessApplication\"b1}"
+ "{?=\"queryStatus\"b1\"hasQueryEmbedding\"b1\"hasEmbeddingResults\"b1\"hasResults\"b1\"hasSuppressedResults\"b1\"hasKeywordResults\"b1\"hasHybridResults\"b1}"
+ "{?=\"serviceProvider\"b1}"
- "%@ - result: %@ - buttons: %@ - card sections: %@"
- "?\t"
- "?\n"
- "Ti,N,V_coreSpotlightIndexTypeUsed"
- "_coreSpotlightIndexTypeUsed"
- "coreSpotlightIndexTypeUsed"
- "initWithInput:triggerEvent:searchType:indexType:queryId:originatingApp:coreSpotlightIndexTypeUsed:"
- "setCoreSpotlightIndexTypeUsed:"

```
