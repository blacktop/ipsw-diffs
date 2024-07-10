## SearchFoundation

> `/System/Library/PrivateFrameworks/SearchFoundation.framework/Versions/A/SearchFoundation`

```diff

-3400.129.1.0.0
-  __TEXT.__text: 0x39602c
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x31538
+3400.135.1.0.0
+  __TEXT.__text: 0x3999cc
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0x31bc8
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x64c8
+  __TEXT.__cstring: 0x65f8
   __TEXT.__oslogstring: 0x19a
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x7e98
-  __TEXT.__objc_classname: 0x42fa
-  __TEXT.__objc_methname: 0x2b9e2
-  __TEXT.__objc_methtype: 0xebd8
-  __TEXT.__objc_stubs: 0x175e0
-  __DATA_CONST.__got: 0x1628
-  __DATA_CONST.__const: 0x7b0
-  __DATA_CONST.__objc_classlist: 0x1648
+  __TEXT.__unwind_info: 0x7f70
+  __TEXT.__objc_classname: 0x4380
+  __TEXT.__objc_methname: 0x2c131
+  __TEXT.__objc_methtype: 0xedc9
+  __TEXT.__objc_stubs: 0x17a80
+  __DATA_CONST.__got: 0x1650
+  __DATA_CONST.__const: 0x880
+  __DATA_CONST.__objc_classlist: 0x1678
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1500
+  __DATA_CONST.__objc_protolist: 0x1530
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d18
+  __DATA_CONST.__objc_selrefs: 0x6e60
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1cd8
-  __AUTH_CONST.__auth_got: 0x230
+  __DATA_CONST.__objc_superrefs: 0x1d08
+  __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0xc040
-  __AUTH_CONST.__objc_const: 0xd8b50
-  __AUTH.__objc_data: 0x9380
-  __DATA.__objc_ivar: 0x3f98
-  __DATA.__data: 0xfc18
+  __AUTH_CONST.__cfstring: 0xc200
+  __AUTH_CONST.__objc_const: 0xda4b8
+  __AUTH.__objc_data: 0x9560
+  __DATA.__objc_ivar: 0x4024
+  __DATA.__data: 0xfe58
   __DATA.__bss: 0xe8
   __DATA_DIRTY.__objc_data: 0x4b50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 16470
-  Symbols:   34233
-  CStrings:  1559
+  Functions: 16606
+  Symbols:   34533
+  CStrings:  1573
 
Symbols:
+ +[SFPhotosAggregatedInfo supportsSecureCoding]
+ +[SFPhotosAttributes supportsSecureCoding]
+ +[SFPhotosRankingInfo supportsSecureCoding]
+ -[SFCommandEngagementFeedback photosAttributes]
+ -[SFCommandEngagementFeedback setPhotosAttributes:]
+ -[SFEndLocalSearchFeedback photosRankingInfo]
+ -[SFEndLocalSearchFeedback setPhotosRankingInfo:]
+ -[SFPhotosAggregatedInfo copyWithZone:]
+ -[SFPhotosAggregatedInfo dictionaryRepresentation]
+ -[SFPhotosAggregatedInfo encodeWithCoder:]
+ -[SFPhotosAggregatedInfo hasTotalNumberOfAssets]
+ -[SFPhotosAggregatedInfo hasTotalNumberOfEmbeddingMatchedAssets]
+ -[SFPhotosAggregatedInfo hasTotalNumberOfMetadataMatchedAssets]
+ -[SFPhotosAggregatedInfo hash]
+ -[SFPhotosAggregatedInfo initWithCoder:]
+ -[SFPhotosAggregatedInfo isEqual:]
+ -[SFPhotosAggregatedInfo jsonData]
+ -[SFPhotosAggregatedInfo setTotalNumberOfAssets:]
+ -[SFPhotosAggregatedInfo setTotalNumberOfEmbeddingMatchedAssets:]
+ -[SFPhotosAggregatedInfo setTotalNumberOfMetadataMatchedAssets:]
+ -[SFPhotosAggregatedInfo totalNumberOfAssets]
+ -[SFPhotosAggregatedInfo totalNumberOfEmbeddingMatchedAssets]
+ -[SFPhotosAggregatedInfo totalNumberOfMetadataMatchedAssets]
+ -[SFPhotosAggregatedInfo(ProtobufInitializer) initWithProtobuf:]
+ -[SFPhotosAttributes copyWithZone:]
+ -[SFPhotosAttributes dictionaryRepresentation]
+ -[SFPhotosAttributes encodeWithCoder:]
+ -[SFPhotosAttributes hasIsEmbeddingMatched]
+ -[SFPhotosAttributes hasIsFavorite]
+ -[SFPhotosAttributes hasIsMetadataMatched]
+ -[SFPhotosAttributes hasIsVideo]
+ -[SFPhotosAttributes hasPositionIndex]
+ -[SFPhotosAttributes hash]
+ -[SFPhotosAttributes initWithCoder:]
+ -[SFPhotosAttributes isEmbeddingMatched]
+ -[SFPhotosAttributes isEqual:]
+ -[SFPhotosAttributes isFavorite]
+ -[SFPhotosAttributes isMetadataMatched]
+ -[SFPhotosAttributes isVideo]
+ -[SFPhotosAttributes jsonData]
+ -[SFPhotosAttributes positionIndex]
+ -[SFPhotosAttributes setIsEmbeddingMatched:]
+ -[SFPhotosAttributes setIsFavorite:]
+ -[SFPhotosAttributes setIsMetadataMatched:]
+ -[SFPhotosAttributes setIsVideo:]
+ -[SFPhotosAttributes setPositionIndex:]
+ -[SFPhotosAttributes(ProtobufInitializer) initWithProtobuf:]
+ -[SFPhotosRankingInfo assetEstimationOffAmount]
+ -[SFPhotosRankingInfo copyWithZone:]
+ -[SFPhotosRankingInfo dictionaryRepresentation]
+ -[SFPhotosRankingInfo encodeWithCoder:]
+ -[SFPhotosRankingInfo hasAssetEstimationOffAmount]
+ -[SFPhotosRankingInfo hasTotalNumberOfAssetsInLibrary]
+ -[SFPhotosRankingInfo hasTotalNumberOfAssetsIndexed]
+ -[SFPhotosRankingInfo hasTotalNumberOfEmbeddingMatchedAssets]
+ -[SFPhotosRankingInfo hasTotalNumberOfMetadataMatchedAssets]
+ -[SFPhotosRankingInfo hash]
+ -[SFPhotosRankingInfo initWithCoder:]
+ -[SFPhotosRankingInfo isEqual:]
+ -[SFPhotosRankingInfo jsonData]
+ -[SFPhotosRankingInfo setAssetEstimationOffAmount:]
+ -[SFPhotosRankingInfo setTotalNumberOfAssetsInLibrary:]
+ -[SFPhotosRankingInfo setTotalNumberOfAssetsIndexed:]
+ -[SFPhotosRankingInfo setTotalNumberOfEmbeddingMatchedAssets:]
+ -[SFPhotosRankingInfo setTotalNumberOfMetadataMatchedAssets:]
+ -[SFPhotosRankingInfo totalNumberOfAssetsInLibrary]
+ -[SFPhotosRankingInfo totalNumberOfAssetsIndexed]
+ -[SFPhotosRankingInfo totalNumberOfEmbeddingMatchedAssets]
+ -[SFPhotosRankingInfo totalNumberOfMetadataMatchedAssets]
+ -[SFPhotosRankingInfo(ProtobufInitializer) initWithProtobuf:]
+ -[SFRankingFeedback setSpotlightQueryIntent:]
+ -[SFRankingFeedback spotlightQueryIntent]
+ -[SFSearchResult photosAggregatedInfo]
+ -[SFSearchResult photosAttributes]
+ -[SFSearchResult setPhotosAggregatedInfo:]
+ -[SFSearchResult setPhotosAttributes:]
+ -[SFStartLocalSearchFeedback isPhotosScopedSearch]
+ -[SFStartLocalSearchFeedback setIsPhotosScopedSearch:]
+ -[_SFPBPhotosAggregatedInfo dictionaryRepresentation]
+ -[_SFPBPhotosAggregatedInfo hash]
+ -[_SFPBPhotosAggregatedInfo initWithDictionary:]
+ -[_SFPBPhotosAggregatedInfo initWithJSON:]
+ -[_SFPBPhotosAggregatedInfo isEqual:]
+ -[_SFPBPhotosAggregatedInfo jsonData]
+ -[_SFPBPhotosAggregatedInfo readFrom:]
+ -[_SFPBPhotosAggregatedInfo setTotalNumberOfAssets:]
+ -[_SFPBPhotosAggregatedInfo setTotalNumberOfEmbeddingMatchedAssets:]
+ -[_SFPBPhotosAggregatedInfo setTotalNumberOfMetadataMatchedAssets:]
+ -[_SFPBPhotosAggregatedInfo totalNumberOfAssets]
+ -[_SFPBPhotosAggregatedInfo totalNumberOfEmbeddingMatchedAssets]
+ -[_SFPBPhotosAggregatedInfo totalNumberOfMetadataMatchedAssets]
+ -[_SFPBPhotosAggregatedInfo writeTo:]
+ -[_SFPBPhotosAggregatedInfo(FacadeInitializer) initWithFacade:]
+ -[_SFPBPhotosAttributes dictionaryRepresentation]
+ -[_SFPBPhotosAttributes hash]
+ -[_SFPBPhotosAttributes initWithDictionary:]
+ -[_SFPBPhotosAttributes initWithJSON:]
+ -[_SFPBPhotosAttributes isEmbeddingMatched]
+ -[_SFPBPhotosAttributes isEqual:]
+ -[_SFPBPhotosAttributes isFavorite]
+ -[_SFPBPhotosAttributes isMetadataMatched]
+ -[_SFPBPhotosAttributes isVideo]
+ -[_SFPBPhotosAttributes jsonData]
+ -[_SFPBPhotosAttributes positionIndex]
+ -[_SFPBPhotosAttributes readFrom:]
+ -[_SFPBPhotosAttributes setIsEmbeddingMatched:]
+ -[_SFPBPhotosAttributes setIsFavorite:]
+ -[_SFPBPhotosAttributes setIsMetadataMatched:]
+ -[_SFPBPhotosAttributes setIsVideo:]
+ -[_SFPBPhotosAttributes setPositionIndex:]
+ -[_SFPBPhotosAttributes writeTo:]
+ -[_SFPBPhotosAttributes(FacadeInitializer) initWithFacade:]
+ -[_SFPBPhotosRankingInfo assetEstimationOffAmount]
+ -[_SFPBPhotosRankingInfo dictionaryRepresentation]
+ -[_SFPBPhotosRankingInfo hash]
+ -[_SFPBPhotosRankingInfo initWithDictionary:]
+ -[_SFPBPhotosRankingInfo initWithJSON:]
+ -[_SFPBPhotosRankingInfo isEqual:]
+ -[_SFPBPhotosRankingInfo jsonData]
+ -[_SFPBPhotosRankingInfo readFrom:]
+ -[_SFPBPhotosRankingInfo setAssetEstimationOffAmount:]
+ -[_SFPBPhotosRankingInfo setTotalNumberOfAssetsInLibrary:]
+ -[_SFPBPhotosRankingInfo setTotalNumberOfAssetsIndexed:]
+ -[_SFPBPhotosRankingInfo setTotalNumberOfEmbeddingMatchedAssets:]
+ -[_SFPBPhotosRankingInfo setTotalNumberOfMetadataMatchedAssets:]
+ -[_SFPBPhotosRankingInfo totalNumberOfAssetsInLibrary]
+ -[_SFPBPhotosRankingInfo totalNumberOfAssetsIndexed]
+ -[_SFPBPhotosRankingInfo totalNumberOfEmbeddingMatchedAssets]
+ -[_SFPBPhotosRankingInfo totalNumberOfMetadataMatchedAssets]
+ -[_SFPBPhotosRankingInfo writeTo:]
+ -[_SFPBPhotosRankingInfo(FacadeInitializer) initWithFacade:]
+ GCC_except_table2700
+ GCC_except_table7528
+ OBJC_IVAR_$_SFCommandEngagementFeedback._photosAttributes
+ OBJC_IVAR_$_SFEndLocalSearchFeedback._photosRankingInfo
+ OBJC_IVAR_$_SFPhotosAggregatedInfo._has
+ OBJC_IVAR_$_SFPhotosAggregatedInfo._totalNumberOfAssets
+ OBJC_IVAR_$_SFPhotosAggregatedInfo._totalNumberOfEmbeddingMatchedAssets
+ OBJC_IVAR_$_SFPhotosAggregatedInfo._totalNumberOfMetadataMatchedAssets
+ OBJC_IVAR_$_SFPhotosAttributes._has
+ OBJC_IVAR_$_SFPhotosAttributes._isEmbeddingMatched
+ OBJC_IVAR_$_SFPhotosAttributes._isFavorite
+ OBJC_IVAR_$_SFPhotosAttributes._isMetadataMatched
+ OBJC_IVAR_$_SFPhotosAttributes._isVideo
+ OBJC_IVAR_$_SFPhotosAttributes._positionIndex
+ OBJC_IVAR_$_SFPhotosRankingInfo._assetEstimationOffAmount
+ OBJC_IVAR_$_SFPhotosRankingInfo._has
+ OBJC_IVAR_$_SFPhotosRankingInfo._totalNumberOfAssetsInLibrary
+ OBJC_IVAR_$_SFPhotosRankingInfo._totalNumberOfAssetsIndexed
+ OBJC_IVAR_$_SFPhotosRankingInfo._totalNumberOfEmbeddingMatchedAssets
+ OBJC_IVAR_$_SFPhotosRankingInfo._totalNumberOfMetadataMatchedAssets
+ OBJC_IVAR_$_SFRankingFeedback._spotlightQueryIntent
+ OBJC_IVAR_$_SFSearchResult._photosAggregatedInfo
+ OBJC_IVAR_$_SFSearchResult._photosAttributes
+ OBJC_IVAR_$_SFStartLocalSearchFeedback._isPhotosScopedSearch
+ OBJC_IVAR_$__SFPBPhotosAggregatedInfo._totalNumberOfAssets
+ OBJC_IVAR_$__SFPBPhotosAggregatedInfo._totalNumberOfEmbeddingMatchedAssets
+ OBJC_IVAR_$__SFPBPhotosAggregatedInfo._totalNumberOfMetadataMatchedAssets
+ OBJC_IVAR_$__SFPBPhotosAttributes._isEmbeddingMatched
+ OBJC_IVAR_$__SFPBPhotosAttributes._isFavorite
+ OBJC_IVAR_$__SFPBPhotosAttributes._isMetadataMatched
+ OBJC_IVAR_$__SFPBPhotosAttributes._isVideo
+ OBJC_IVAR_$__SFPBPhotosAttributes._positionIndex
+ OBJC_IVAR_$__SFPBPhotosRankingInfo._assetEstimationOffAmount
+ OBJC_IVAR_$__SFPBPhotosRankingInfo._totalNumberOfAssetsInLibrary
+ OBJC_IVAR_$__SFPBPhotosRankingInfo._totalNumberOfAssetsIndexed
+ OBJC_IVAR_$__SFPBPhotosRankingInfo._totalNumberOfEmbeddingMatchedAssets
+ OBJC_IVAR_$__SFPBPhotosRankingInfo._totalNumberOfMetadataMatchedAssets
+ PARLogHandleForCategory.logHandles.0.31811
+ PARLogHandleForCategory.logHandles.0.64067
+ PARLogHandleForCategory.logHandles.1.31805
+ PARLogHandleForCategory.logHandles.1.64063
+ PARLogHandleForCategory.logHandles.2.31813
+ PARLogHandleForCategory.logHandles.2.64068
+ PARLogHandleForCategory.logHandles.3.31814
+ PARLogHandleForCategory.logHandles.3.64070
+ PARLogHandleForCategory.logHandles.4.31815
+ PARLogHandleForCategory.logHandles.4.64071
+ PARLogHandleForCategory.logHandles.5.31816
+ PARLogHandleForCategory.logHandles.5.64072
+ PARLogHandleForCategory.onceToken.31803
+ PARLogHandleForCategory.onceToken.64062
+ _OBJC_$_PROP_LIST_SFPhotosAggregatedInfo.89
+ _OBJC_$_PROP_LIST_SFPhotosAttributes.103
+ _OBJC_$_PROP_LIST_SFPhotosRankingInfo.101
+ _OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.8378
+ _OBJC_$_PROP_LIST__SFPBPhotosAttributes.8424
+ _OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.8460
+ _OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.8490
+ _OBJC_$_PROP_LIST__SFPBPin.8505
+ _OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.8538
+ _OBJC_$_PROP_LIST__SFPBPlayMediaCommand.8561
+ _OBJC_$_PROP_LIST__SFPBPlayVideoCommand.8568
+ _OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.8588
+ _OBJC_$_PROP_LIST__SFPBPointSize.8611
+ _OBJC_$_PROP_LIST__SFPBProduct.8642
+ _OBJC_$_PROP_LIST__SFPBProductAvailability.8664
+ _OBJC_$_PROP_LIST__SFPBProductCardSection.8679
+ _OBJC_$_PROP_LIST__SFPBProductInventory.8735
+ _OBJC_$_PROP_LIST__SFPBProductInventoryResult.8758
+ _OBJC_$_PROP_LIST__SFPBPunchout.8815
+ _OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.8973
+ _OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.8988
+ _OBJC_$_PROP_LIST__SFPBRFAppIconImage.9008
+ _OBJC_$_PROP_LIST__SFPBRFAspectRatio.9016
+ _OBJC_$_PROP_LIST__SFPBRFAttribution.9068
+ _OBJC_$_PROP_LIST__SFPBRFAvatarImage.9087
+ _OBJC_$_PROP_LIST__SFPBRFBadgedImage.9101
+ _OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9124
+ _OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9132
+ _OBJC_$_PROP_LIST__SFPBRFColor.9166
+ _OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.9172
+ _OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.9188
+ _OBJC_$_PROP_LIST__SFPBRFEngageable.9217
+ _OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.9252
+ _OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.9275
+ _OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.9360
+ _OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.9379
+ _OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.9386
+ _OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.9419
+ _OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.9426
+ _OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.9433
+ _OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.9440
+ _OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.9456
+ _OBJC_$_PROP_LIST__SFPBRFFont.9476
+ _OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.10485
+ _OBJC_$_PROP_LIST__SFPBRFFormattedText.9630
+ _OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.9645
+ _OBJC_$_PROP_LIST__SFPBRFImageElement.9665
+ _OBJC_$_PROP_LIST__SFPBRFImageSource.9764
+ _OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.9787
+ _OBJC_$_PROP_LIST__SFPBRFMapAnnotation.9817
+ _OBJC_$_PROP_LIST__SFPBRFMapCardSection.9884
+ _OBJC_$_PROP_LIST__SFPBRFMapMarker.9917
+ _OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.9948
+ _OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.9963
+ _OBJC_$_PROP_LIST__SFPBRFMapMarkerText.9971
+ _OBJC_$_PROP_LIST__SFPBRFMapPoint.9993
+ _OBJC_$_PROP_LIST__SFPBRFMonogramImage.10008
+ _OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.10023
+ _OBJC_$_PROP_LIST__SFPBRFOptionalBool.10030
+ _OBJC_$_PROP_LIST__SFPBRFOptionalFloat.10037
+ _OBJC_$_PROP_LIST__SFPBRFPreview.10044
+ _OBJC_$_PROP_LIST__SFPBRFPreviewList.10066
+ _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.10081
+ _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.10088
+ _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.10096
+ _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.10103
+ _OBJC_$_PROP_LIST__SFPBRFRGBValue.10133
+ _OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.10145
+ _OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.10152
+ _OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.10159
+ _OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.10166
+ _OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.10173
+ _OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.10180
+ _OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.10187
+ _OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.10194
+ _OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.10209
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.10224
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.10231
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.10262
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.10269
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.10276
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.10292
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.10308
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.10315
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.10322
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.10342
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.10349
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.10372
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.10379
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.10386
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.10401
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.10416
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.10423
+ _OBJC_$_PROP_LIST__SFPBRFSymbolImage.10478
+ _OBJC_$_PROP_LIST__SFPBRFTableCell.10521
+ _OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.10551
+ _OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.10597
+ _OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.10662
+ _OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.10677
+ _OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.10683
+ _OBJC_$_PROP_LIST__SFPBRFTextElement.10727
+ _OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.10733
+ _OBJC_$_PROP_LIST__SFPBRFTextProperty.10763
+ _OBJC_$_PROP_LIST__SFPBRFUrlImage.10827
+ _OBJC_$_PROP_LIST__SFPBRFVisualElement.10846
+ _OBJC_$_PROP_LIST__SFPBRFVisualProperty.10868
+ _OBJC_$_PROP_LIST__SFPBReferentialCommand.10875
+ _OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.10895
+ _OBJC_$_PROP_LIST__SFPBReminder.10910
+ _OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.10917
+ _OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.10948
+ _OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.10955
+ _OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.11009
+ _OBJC_$_PROP_LIST__SFPBResultEntity.11037
+ _OBJC_$_PROP_LIST__SFPBRichText.11077
+ _OBJC_$_PROP_LIST__SFPBRichTitleCardSection.11225
+ _OBJC_$_PROP_LIST__SFPBRowCardSection.11320
+ _OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.11335
+ _OBJC_$_PROP_LIST__SFPBSafariAttributes.11349
+ _OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.11395
+ _OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.11411
+ _OBJC_$_PROP_LIST__SFPBScene.11433
+ _OBJC_$_PROP_LIST__SFPBScoreboardCardSection.11477
+ _OBJC_$_PROP_LIST__SFPBSearchInAppCommand.11492
+ _OBJC_$_PROP_LIST__SFPBSearchSuggestion.11574
+ _OBJC_$_PROP_LIST__SFPBSearchWebCommand.11581
+ _OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.11589
+ _OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.11619
+ _OBJC_$_PROP_LIST__SFPBShareCommand.11639
+ _OBJC_$_PROP_LIST__SFPBShareItem.11672
+ _OBJC_$_PROP_LIST__SFPBShortcutsImage.11687
+ _OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.11702
+ _OBJC_$_PROP_LIST__SFPBShowContactCardCommand.11717
+ _OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.11768
+ _OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.11783
+ _OBJC_$_PROP_LIST__SFPBShowSFCardCommand.11798
+ _OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.11805
+ _OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.11812
+ _OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.11876
+ _OBJC_$_PROP_LIST__SFPBSplitCardSection.11943
+ _OBJC_$_PROP_LIST__SFPBSportsDetail.11958
+ _OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.11978
+ _OBJC_$_PROP_LIST__SFPBSportsItem.11985
+ _OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.12016
+ _OBJC_$_PROP_LIST__SFPBSportsTeam.12048
+ _OBJC_$_PROP_LIST__SFPBStockChartCardSection.12071
+ _OBJC_$_PROP_LIST__SFPBStoreButtonItem.12094
+ _OBJC_$_PROP_LIST__SFPBStringDictionary.12113
+ _OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.12164
+ _OBJC_$_PROP_LIST__SFPBStructuredLocation.12187
+ _OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.12220
+ _OBJC_$_PROP_LIST__SFPBSuggestionCardSection.12259
+ _OBJC_$_PROP_LIST__SFPBSymbolImage.12301
+ _OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.12325
+ _OBJC_$_PROP_LIST__SFPBTableColumnAlignment.12355
+ _OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.12423
+ _OBJC_$_PROP_LIST__SFPBTableRowCardSection.12443
+ _OBJC_$_PROP_LIST__SFPBText.12460
+ _OBJC_$_PROP_LIST__SFPBTextColumn.12482
+ _OBJC_$_PROP_LIST__SFPBTextColumnSection.12517
+ _OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.12528
+ _OBJC_$_PROP_LIST__SFPBTextCopyItem.12543
+ _OBJC_$_PROP_LIST__SFPBTimeZone.12550
+ _OBJC_$_PROP_LIST__SFPBTitleCardSection.12557
+ _OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.12564
+ _OBJC_$_PROP_LIST__SFPBToggleAudioCommand.12587
+ _OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.12611
+ _OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.12626
+ _OBJC_$_PROP_LIST__SFPBTopic.12669
+ _OBJC_$_PROP_LIST__SFPBTrack.12701
+ _OBJC_$_PROP_LIST__SFPBTrackListCardSection.12723
+ _OBJC_$_PROP_LIST__SFPBURL.12730
+ _OBJC_$_PROP_LIST__SFPBURLImage.12745
+ _OBJC_$_PROP_LIST__SFPBURLShareItem.12752
+ _OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.12767
+ _OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.12782
+ _OBJC_$_PROP_LIST__SFPBUserActivityData.12813
+ _OBJC_$_PROP_LIST__SFPBUserActivityInfo.12836
+ _OBJC_$_PROP_LIST__SFPBUserReportRequest.12911
+ _OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.12942
+ _OBJC_$_PROP_LIST__SFPBViewEmailCommand.12948
+ _OBJC_$_PROP_LIST__SFPBWatchListButtonItem.12955
+ _OBJC_$_PROP_LIST__SFPBWatchListCardSection.12962
+ _OBJC_$_PROP_LIST__SFPBWatchListItem.13041
+ _OBJC_$_PROP_LIST__SFPBWatchNowCardSection.13055
+ _OBJC_$_PROP_LIST__SFPBWeatherColor.13070
+ _OBJC_$_PROP_LIST__SFPBWeatherDetails.13077
+ _OBJC_$_PROP_LIST__SFPBWebCardSection.13092
+ _OBJC_$_PROP_LIST__SFPBWorldMapCardSection.13115
+ _OBJC_CLASS_$_SFPhotosAggregatedInfo
+ _OBJC_CLASS_$_SFPhotosAttributes
+ _OBJC_CLASS_$_SFPhotosRankingInfo
+ _OBJC_CLASS_$__SFPBPhotosAggregatedInfo
+ _OBJC_CLASS_$__SFPBPhotosAttributes
+ _OBJC_CLASS_$__SFPBPhotosRankingInfo
+ _OBJC_METACLASS_$_SFPhotosAggregatedInfo
+ _OBJC_METACLASS_$_SFPhotosAttributes
+ _OBJC_METACLASS_$_SFPhotosRankingInfo
+ _OBJC_METACLASS_$__SFPBPhotosAggregatedInfo
+ _OBJC_METACLASS_$__SFPBPhotosAttributes
+ _OBJC_METACLASS_$__SFPBPhotosRankingInfo
+ __OBJC_$_CLASS_METHODS_SFPhotosAggregatedInfo
+ __OBJC_$_CLASS_METHODS_SFPhotosAttributes
+ __OBJC_$_CLASS_METHODS_SFPhotosRankingInfo
+ __OBJC_$_CLASS_PROP_LIST_SFPhotosAggregatedInfo
+ __OBJC_$_CLASS_PROP_LIST_SFPhotosAttributes
+ __OBJC_$_CLASS_PROP_LIST_SFPhotosRankingInfo
+ __OBJC_$_CLASS_PROP_LIST__SFPBPhotosAggregatedInfo
+ __OBJC_$_CLASS_PROP_LIST__SFPBPhotosAttributes
+ __OBJC_$_CLASS_PROP_LIST__SFPBPhotosRankingInfo
+ __OBJC_$_INSTANCE_METHODS_SFPhotosAggregatedInfo(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFPhotosAttributes(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFPhotosRankingInfo(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBPhotosAggregatedInfo(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBPhotosAttributes(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBPhotosRankingInfo(FacadeInitializer)
+ __OBJC_$_INSTANCE_VARIABLES_SFPhotosAggregatedInfo
+ __OBJC_$_INSTANCE_VARIABLES_SFPhotosAttributes
+ __OBJC_$_INSTANCE_VARIABLES_SFPhotosRankingInfo
+ __OBJC_$_INSTANCE_VARIABLES__SFPBPhotosAggregatedInfo
+ __OBJC_$_INSTANCE_VARIABLES__SFPBPhotosAttributes
+ __OBJC_$_INSTANCE_VARIABLES__SFPBPhotosRankingInfo
+ __OBJC_$_PROP_LIST_SFPhotosAggregatedInfo
+ __OBJC_$_PROP_LIST_SFPhotosAttributes
+ __OBJC_$_PROP_LIST_SFPhotosRankingInfo
+ __OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo
+ __OBJC_$_PROP_LIST__SFPBPhotosAttributes
+ __OBJC_$_PROP_LIST__SFPBPhotosRankingInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFPhotosAggregatedInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFPhotosAttributes
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFPhotosRankingInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBPhotosAggregatedInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBPhotosAttributes
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBPhotosRankingInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFPhotosAggregatedInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFPhotosAttributes
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFPhotosRankingInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBPhotosAggregatedInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBPhotosAttributes
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBPhotosRankingInfo
+ __OBJC_$_PROTOCOL_REFS_SFPhotosAggregatedInfo
+ __OBJC_$_PROTOCOL_REFS_SFPhotosAttributes
+ __OBJC_$_PROTOCOL_REFS_SFPhotosRankingInfo
+ __OBJC_$_PROTOCOL_REFS__SFPBPhotosAggregatedInfo
+ __OBJC_$_PROTOCOL_REFS__SFPBPhotosAttributes
+ __OBJC_$_PROTOCOL_REFS__SFPBPhotosRankingInfo
+ __OBJC_CLASS_PROTOCOLS_$_SFPhotosAggregatedInfo
+ __OBJC_CLASS_PROTOCOLS_$_SFPhotosAttributes
+ __OBJC_CLASS_PROTOCOLS_$_SFPhotosRankingInfo
+ __OBJC_CLASS_PROTOCOLS_$__SFPBPhotosAggregatedInfo
+ __OBJC_CLASS_PROTOCOLS_$__SFPBPhotosAttributes
+ __OBJC_CLASS_PROTOCOLS_$__SFPBPhotosRankingInfo
+ __OBJC_CLASS_RO_$_SFPhotosAggregatedInfo
+ __OBJC_CLASS_RO_$_SFPhotosAttributes
+ __OBJC_CLASS_RO_$_SFPhotosRankingInfo
+ __OBJC_CLASS_RO_$__SFPBPhotosAggregatedInfo
+ __OBJC_CLASS_RO_$__SFPBPhotosAttributes
+ __OBJC_CLASS_RO_$__SFPBPhotosRankingInfo
+ __OBJC_LABEL_PROTOCOL_$_SFPhotosAggregatedInfo
+ __OBJC_LABEL_PROTOCOL_$_SFPhotosAttributes
+ __OBJC_LABEL_PROTOCOL_$_SFPhotosRankingInfo
+ __OBJC_LABEL_PROTOCOL_$__SFPBPhotosAggregatedInfo
+ __OBJC_LABEL_PROTOCOL_$__SFPBPhotosAttributes
+ __OBJC_LABEL_PROTOCOL_$__SFPBPhotosRankingInfo
+ __OBJC_METACLASS_RO_$_SFPhotosAggregatedInfo
+ __OBJC_METACLASS_RO_$_SFPhotosAttributes
+ __OBJC_METACLASS_RO_$_SFPhotosRankingInfo
+ __OBJC_METACLASS_RO_$__SFPBPhotosAggregatedInfo
+ __OBJC_METACLASS_RO_$__SFPBPhotosAttributes
+ __OBJC_METACLASS_RO_$__SFPBPhotosRankingInfo
+ __OBJC_PROTOCOL_$_SFPhotosAggregatedInfo
+ __OBJC_PROTOCOL_$_SFPhotosAttributes
+ __OBJC_PROTOCOL_$_SFPhotosRankingInfo
+ __OBJC_PROTOCOL_$__SFPBPhotosAggregatedInfo
+ __OBJC_PROTOCOL_$__SFPBPhotosAttributes
+ __OBJC_PROTOCOL_$__SFPBPhotosRankingInfo
+ __PARLogHandleForCategory_block_invoke.31809
+ __PARLogHandleForCategory_block_invoke.64065
+ __SFPBPhotosAggregatedInfoReadFrom
+ __SFPBPhotosAttributesReadFrom
+ __SFPBPhotosRankingInfoReadFrom
+ __block_literal_global.31804
+ __block_literal_global.32548
+ __block_literal_global.34202
+ __block_literal_global.64078
+ __getDispatchQueue_block_invoke.64082
+ _objc_msgSend$assetEstimationOffAmount
+ _objc_msgSend$hasAssetEstimationOffAmount
+ _objc_msgSend$hasIsEmbeddingMatched
+ _objc_msgSend$hasIsFavorite
+ _objc_msgSend$hasIsMetadataMatched
+ _objc_msgSend$hasIsVideo
+ _objc_msgSend$hasPositionIndex
+ _objc_msgSend$hasTotalNumberOfAssets
+ _objc_msgSend$hasTotalNumberOfAssetsInLibrary
+ _objc_msgSend$hasTotalNumberOfAssetsIndexed
+ _objc_msgSend$hasTotalNumberOfEmbeddingMatchedAssets
+ _objc_msgSend$hasTotalNumberOfMetadataMatchedAssets
+ _objc_msgSend$isEmbeddingMatched
+ _objc_msgSend$isFavorite
+ _objc_msgSend$isMetadataMatched
+ _objc_msgSend$isVideo
+ _objc_msgSend$photosAggregatedInfo
+ _objc_msgSend$photosAttributes
+ _objc_msgSend$positionIndex
+ _objc_msgSend$setAssetEstimationOffAmount:
+ _objc_msgSend$setIsEmbeddingMatched:
+ _objc_msgSend$setIsFavorite:
+ _objc_msgSend$setIsMetadataMatched:
+ _objc_msgSend$setIsVideo:
+ _objc_msgSend$setPhotosAggregatedInfo:
+ _objc_msgSend$setPhotosAttributes:
+ _objc_msgSend$setPositionIndex:
+ _objc_msgSend$setTotalNumberOfAssets:
+ _objc_msgSend$setTotalNumberOfAssetsInLibrary:
+ _objc_msgSend$setTotalNumberOfAssetsIndexed:
+ _objc_msgSend$setTotalNumberOfEmbeddingMatchedAssets:
+ _objc_msgSend$setTotalNumberOfMetadataMatchedAssets:
+ _objc_msgSend$totalNumberOfAssets
+ _objc_msgSend$totalNumberOfAssetsInLibrary
+ _objc_msgSend$totalNumberOfAssetsIndexed
+ _objc_msgSend$totalNumberOfEmbeddingMatchedAssets
+ _objc_msgSend$totalNumberOfMetadataMatchedAssets
+ _objc_unsafeClaimAutoreleasedReturnValue
+ getDispatchQueue.64076
+ getDispatchQueue.onceToken.64077
+ getDispatchQueue.queue.64079
- GCC_except_table2658
- GCC_except_table7451
- PARLogHandleForCategory.logHandles.0.31540
- PARLogHandleForCategory.logHandles.0.63640
- PARLogHandleForCategory.logHandles.1.31534
- PARLogHandleForCategory.logHandles.1.63636
- PARLogHandleForCategory.logHandles.2.31542
- PARLogHandleForCategory.logHandles.2.63641
- PARLogHandleForCategory.logHandles.3.31543
- PARLogHandleForCategory.logHandles.3.63643
- PARLogHandleForCategory.logHandles.4.31544
- PARLogHandleForCategory.logHandles.4.63644
- PARLogHandleForCategory.logHandles.5.31545
- PARLogHandleForCategory.logHandles.5.63645
- PARLogHandleForCategory.onceToken.31532
- PARLogHandleForCategory.onceToken.63635
- _OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.8384
- _OBJC_$_PROP_LIST__SFPBPin.8399
- _OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.8432
- _OBJC_$_PROP_LIST__SFPBPlayMediaCommand.8455
- _OBJC_$_PROP_LIST__SFPBPlayVideoCommand.8462
- _OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.8482
- _OBJC_$_PROP_LIST__SFPBPointSize.8505
- _OBJC_$_PROP_LIST__SFPBProduct.8536
- _OBJC_$_PROP_LIST__SFPBProductAvailability.8558
- _OBJC_$_PROP_LIST__SFPBProductCardSection.8573
- _OBJC_$_PROP_LIST__SFPBProductInventory.8629
- _OBJC_$_PROP_LIST__SFPBProductInventoryResult.8652
- _OBJC_$_PROP_LIST__SFPBPunchout.8709
- _OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.8867
- _OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.8882
- _OBJC_$_PROP_LIST__SFPBRFAppIconImage.8902
- _OBJC_$_PROP_LIST__SFPBRFAspectRatio.8910
- _OBJC_$_PROP_LIST__SFPBRFAttribution.8962
- _OBJC_$_PROP_LIST__SFPBRFAvatarImage.8981
- _OBJC_$_PROP_LIST__SFPBRFBadgedImage.8995
- _OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9018
- _OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9026
- _OBJC_$_PROP_LIST__SFPBRFColor.9060
- _OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.9066
- _OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.9082
- _OBJC_$_PROP_LIST__SFPBRFEngageable.9111
- _OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.9146
- _OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.9169
- _OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.9254
- _OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.9273
- _OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.9280
- _OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.9313
- _OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.9320
- _OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.9327
- _OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.9334
- _OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.9350
- _OBJC_$_PROP_LIST__SFPBRFFont.9370
- _OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.10379
- _OBJC_$_PROP_LIST__SFPBRFFormattedText.9524
- _OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.9539
- _OBJC_$_PROP_LIST__SFPBRFImageElement.9559
- _OBJC_$_PROP_LIST__SFPBRFImageSource.9658
- _OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.9681
- _OBJC_$_PROP_LIST__SFPBRFMapAnnotation.9711
- _OBJC_$_PROP_LIST__SFPBRFMapCardSection.9778
- _OBJC_$_PROP_LIST__SFPBRFMapMarker.9811
- _OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.9842
- _OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.9857
- _OBJC_$_PROP_LIST__SFPBRFMapMarkerText.9865
- _OBJC_$_PROP_LIST__SFPBRFMapPoint.9887
- _OBJC_$_PROP_LIST__SFPBRFMonogramImage.9902
- _OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.9917
- _OBJC_$_PROP_LIST__SFPBRFOptionalBool.9924
- _OBJC_$_PROP_LIST__SFPBRFOptionalFloat.9931
- _OBJC_$_PROP_LIST__SFPBRFPreview.9938
- _OBJC_$_PROP_LIST__SFPBRFPreviewList.9960
- _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.9975
- _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.9982
- _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.9990
- _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.9997
- _OBJC_$_PROP_LIST__SFPBRFRGBValue.10027
- _OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.10039
- _OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.10046
- _OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.10053
- _OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.10060
- _OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.10067
- _OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.10074
- _OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.10081
- _OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.10088
- _OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.10103
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.10118
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.10125
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.10156
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.10163
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.10170
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.10186
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.10202
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.10209
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.10216
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.10236
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.10243
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.10266
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.10273
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.10280
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.10295
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.10310
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.10317
- _OBJC_$_PROP_LIST__SFPBRFSymbolImage.10372
- _OBJC_$_PROP_LIST__SFPBRFTableCell.10415
- _OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.10445
- _OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.10491
- _OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.10556
- _OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.10571
- _OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.10577
- _OBJC_$_PROP_LIST__SFPBRFTextElement.10621
- _OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.10627
- _OBJC_$_PROP_LIST__SFPBRFTextProperty.10657
- _OBJC_$_PROP_LIST__SFPBRFUrlImage.10721
- _OBJC_$_PROP_LIST__SFPBRFVisualElement.10740
- _OBJC_$_PROP_LIST__SFPBRFVisualProperty.10762
- _OBJC_$_PROP_LIST__SFPBReferentialCommand.10769
- _OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.10789
- _OBJC_$_PROP_LIST__SFPBReminder.10804
- _OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.10811
- _OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.10842
- _OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.10849
- _OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.10903
- _OBJC_$_PROP_LIST__SFPBResultEntity.10931
- _OBJC_$_PROP_LIST__SFPBRichText.10971
- _OBJC_$_PROP_LIST__SFPBRichTitleCardSection.11119
- _OBJC_$_PROP_LIST__SFPBRowCardSection.11214
- _OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.11229
- _OBJC_$_PROP_LIST__SFPBSafariAttributes.11243
- _OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.11289
- _OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.11305
- _OBJC_$_PROP_LIST__SFPBScene.11327
- _OBJC_$_PROP_LIST__SFPBScoreboardCardSection.11371
- _OBJC_$_PROP_LIST__SFPBSearchInAppCommand.11386
- _OBJC_$_PROP_LIST__SFPBSearchSuggestion.11468
- _OBJC_$_PROP_LIST__SFPBSearchWebCommand.11475
- _OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.11483
- _OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.11513
- _OBJC_$_PROP_LIST__SFPBShareCommand.11533
- _OBJC_$_PROP_LIST__SFPBShareItem.11566
- _OBJC_$_PROP_LIST__SFPBShortcutsImage.11581
- _OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.11596
- _OBJC_$_PROP_LIST__SFPBShowContactCardCommand.11611
- _OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.11662
- _OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.11677
- _OBJC_$_PROP_LIST__SFPBShowSFCardCommand.11692
- _OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.11699
- _OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.11706
- _OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.11770
- _OBJC_$_PROP_LIST__SFPBSplitCardSection.11837
- _OBJC_$_PROP_LIST__SFPBSportsDetail.11852
- _OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.11872
- _OBJC_$_PROP_LIST__SFPBSportsItem.11879
- _OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.11910
- _OBJC_$_PROP_LIST__SFPBSportsTeam.11942
- _OBJC_$_PROP_LIST__SFPBStockChartCardSection.11965
- _OBJC_$_PROP_LIST__SFPBStoreButtonItem.11988
- _OBJC_$_PROP_LIST__SFPBStringDictionary.12007
- _OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.12058
- _OBJC_$_PROP_LIST__SFPBStructuredLocation.12081
- _OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.12114
- _OBJC_$_PROP_LIST__SFPBSuggestionCardSection.12153
- _OBJC_$_PROP_LIST__SFPBSymbolImage.12195
- _OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.12219
- _OBJC_$_PROP_LIST__SFPBTableColumnAlignment.12249
- _OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.12317
- _OBJC_$_PROP_LIST__SFPBTableRowCardSection.12337
- _OBJC_$_PROP_LIST__SFPBText.12354
- _OBJC_$_PROP_LIST__SFPBTextColumn.12376
- _OBJC_$_PROP_LIST__SFPBTextColumnSection.12411
- _OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.12422
- _OBJC_$_PROP_LIST__SFPBTextCopyItem.12437
- _OBJC_$_PROP_LIST__SFPBTimeZone.12444
- _OBJC_$_PROP_LIST__SFPBTitleCardSection.12451
- _OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.12458
- _OBJC_$_PROP_LIST__SFPBToggleAudioCommand.12481
- _OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.12505
- _OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.12520
- _OBJC_$_PROP_LIST__SFPBTopic.12563
- _OBJC_$_PROP_LIST__SFPBTrack.12595
- _OBJC_$_PROP_LIST__SFPBTrackListCardSection.12617
- _OBJC_$_PROP_LIST__SFPBURL.12624
- _OBJC_$_PROP_LIST__SFPBURLImage.12639
- _OBJC_$_PROP_LIST__SFPBURLShareItem.12646
- _OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.12661
- _OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.12676
- _OBJC_$_PROP_LIST__SFPBUserActivityData.12707
- _OBJC_$_PROP_LIST__SFPBUserActivityInfo.12730
- _OBJC_$_PROP_LIST__SFPBUserReportRequest.12805
- _OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.12836
- _OBJC_$_PROP_LIST__SFPBViewEmailCommand.12842
- _OBJC_$_PROP_LIST__SFPBWatchListButtonItem.12849
- _OBJC_$_PROP_LIST__SFPBWatchListCardSection.12856
- _OBJC_$_PROP_LIST__SFPBWatchListItem.12935
- _OBJC_$_PROP_LIST__SFPBWatchNowCardSection.12949
- _OBJC_$_PROP_LIST__SFPBWeatherColor.12964
- _OBJC_$_PROP_LIST__SFPBWeatherDetails.12971
- _OBJC_$_PROP_LIST__SFPBWebCardSection.12986
- _OBJC_$_PROP_LIST__SFPBWorldMapCardSection.13009
- __PARLogHandleForCategory_block_invoke.31538
- __PARLogHandleForCategory_block_invoke.63638
- __block_literal_global.31533
- __block_literal_global.32277
- __block_literal_global.33925
- __block_literal_global.63651
- __getDispatchQueue_block_invoke.63655
- getDispatchQueue.63649
- getDispatchQueue.onceToken.63650
- getDispatchQueue.queue.63652
CStrings:
+ "_photosAggregatedInfo"
+ "_photosAttributes"
+ "_spotlightQueryIntent"
+ "assetEstimationOffAmount"
+ "isEmbeddingMatched"
+ "isFavorite"
+ "isMetadataMatched"
+ "isVideo"
+ "positionIndex"
+ "totalNumberOfAssets"
+ "totalNumberOfAssetsInLibrary"
+ "totalNumberOfAssetsIndexed"
+ "totalNumberOfEmbeddingMatchedAssets"
+ "totalNumberOfMetadataMatchedAssets"

```
