## SearchFoundation

> `/System/Library/PrivateFrameworks/SearchFoundation.framework/Versions/A/SearchFoundation`

```diff

-3403.3.3.0.0
-  __TEXT.__text: 0x3a8af8
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x32518
-  __TEXT.__const: 0x88
+3404.77.2.14.1
+  __TEXT.__text: 0x3b0428
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_methlist: 0x52284
+  __TEXT.__const: 0x90
+  __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x682f
+  __TEXT.__cstring: 0x68bb
   __TEXT.__oslogstring: 0x19a
-  __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x8128
-  __TEXT.__objc_classname: 0x43e7
-  __TEXT.__objc_methname: 0x2ce7b
-  __TEXT.__objc_methtype: 0xef8b
-  __TEXT.__objc_stubs: 0x182e0
-  __DATA_CONST.__got: 0x1670
+  __TEXT.__unwind_info: 0x7e18
+  __TEXT.__objc_classname: 0x441c
+  __TEXT.__objc_methname: 0x2d2c8
+  __TEXT.__objc_methtype: 0xf04f
+  __TEXT.__objc_stubs: 0x18500
+  __DATA_CONST.__got: 0x1680
   __DATA_CONST.__const: 0x8f0
-  __DATA_CONST.__objc_classlist: 0x1698
+  __DATA_CONST.__objc_classlist: 0x16a8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1550
+  __DATA_CONST.__objc_protolist: 0x1560
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7078
+  __DATA_CONST.__objc_selrefs: 0x71b0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1d38
-  __AUTH_CONST.__auth_got: 0x230
+  __DATA_CONST.__objc_superrefs: 0x1d50
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0xc5c0
-  __AUTH_CONST.__objc_const: 0xdeb68
-  __AUTH.__objc_data: 0x96a0
-  __DATA.__objc_ivar: 0x4144
-  __DATA.__data: 0xffd8
+  __AUTH_CONST.__cfstring: 0xc6a0
+  __AUTH_CONST.__objc_const: 0xa3050
+  __AUTH.__objc_data: 0x9740
+  __DATA.__objc_ivar: 0x4180
+  __DATA.__data: 0x10098
   __DATA.__bss: 0xe8
   __DATA_DIRTY.__objc_data: 0x4b50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C5651ABD-BD1A-3AC4-BE7E-C42C328FE4DA
-  Functions: 16803
-  Symbols:   34929
-  CStrings:  13137
+  UUID: 74C3181B-81B9-3F42-8716-E471935DDD46
+  Functions: 16693
+  Symbols:   35053
+  CStrings:  13203
 
Symbols:
+ +[SFExecuteMenuItemCommand supportsSecureCoding]
+ -[SFCardSection racFeedbackLoggingContent]
+ -[SFCardSection racFeedbackSubfeatureId]
+ -[SFCardSection setRacFeedbackLoggingContent:]
+ -[SFCardSection setRacFeedbackSubfeatureId:]
+ -[SFExecuteMenuItemCommand .cxx_destruct]
+ -[SFExecuteMenuItemCommand applicationBundleIdentifier]
+ -[SFExecuteMenuItemCommand copyWithZone:]
+ -[SFExecuteMenuItemCommand dictionaryRepresentation]
+ -[SFExecuteMenuItemCommand encodeWithCoder:]
+ -[SFExecuteMenuItemCommand hash]
+ -[SFExecuteMenuItemCommand initWithCoder:]
+ -[SFExecuteMenuItemCommand isEqual:]
+ -[SFExecuteMenuItemCommand jsonData]
+ -[SFExecuteMenuItemCommand menuItemIdentifier]
+ -[SFExecuteMenuItemCommand setApplicationBundleIdentifier:]
+ -[SFExecuteMenuItemCommand setMenuItemIdentifier:]
+ -[SFExecuteMenuItemCommand(ProtobufInitializer) initWithProtobuf:]
+ -[SFExecuteToolCommand setToolInvocationData:]
+ -[SFExecuteToolCommand toolInvocationData]
+ -[SFPerformEntityQueryCommand enabledDomains]
+ -[SFPerformEntityQueryCommand filterQueries]
+ -[SFPerformEntityQueryCommand setEnabledDomains:]
+ -[SFPerformEntityQueryCommand setFilterQueries:]
+ -[_SFPBCardSection getRacFeedbackLoggingContent:forKey:]
+ -[_SFPBCardSection racFeedbackLoggingContent]
+ -[_SFPBCardSection racFeedbackSubfeatureId]
+ -[_SFPBCardSection setRacFeedbackLoggingContent:]
+ -[_SFPBCardSection setRacFeedbackLoggingContent:forKey:]
+ -[_SFPBCardSection setRacFeedbackSubfeatureId:]
+ -[_SFPBCommand executeMenuItemCommand]
+ -[_SFPBCommand setExecuteMenuItemCommand:]
+ -[_SFPBExecuteMenuItemCommand .cxx_destruct]
+ -[_SFPBExecuteMenuItemCommand applicationBundleIdentifier]
+ -[_SFPBExecuteMenuItemCommand dictionaryRepresentation]
+ -[_SFPBExecuteMenuItemCommand hash]
+ -[_SFPBExecuteMenuItemCommand initWithDictionary:]
+ -[_SFPBExecuteMenuItemCommand initWithJSON:]
+ -[_SFPBExecuteMenuItemCommand isEqual:]
+ -[_SFPBExecuteMenuItemCommand jsonData]
+ -[_SFPBExecuteMenuItemCommand menuItemIdentifier]
+ -[_SFPBExecuteMenuItemCommand readFrom:]
+ -[_SFPBExecuteMenuItemCommand setApplicationBundleIdentifier:]
+ -[_SFPBExecuteMenuItemCommand setMenuItemIdentifier:]
+ -[_SFPBExecuteMenuItemCommand writeTo:]
+ -[_SFPBExecuteMenuItemCommand(FacadeInitializer) initWithFacade:]
+ -[_SFPBExecuteToolCommand setToolInvocationData:]
+ -[_SFPBExecuteToolCommand toolInvocationData]
+ -[_SFPBPerformEntityQueryCommand addEnabledDomains:]
+ -[_SFPBPerformEntityQueryCommand addFilterQueries:]
+ -[_SFPBPerformEntityQueryCommand clearEnabledDomains]
+ -[_SFPBPerformEntityQueryCommand clearFilterQueries]
+ -[_SFPBPerformEntityQueryCommand enabledDomainsAtIndex:]
+ -[_SFPBPerformEntityQueryCommand enabledDomainsCount]
+ -[_SFPBPerformEntityQueryCommand enabledDomains]
+ -[_SFPBPerformEntityQueryCommand filterQueriesAtIndex:]
+ -[_SFPBPerformEntityQueryCommand filterQueriesCount]
+ -[_SFPBPerformEntityQueryCommand filterQueries]
+ -[_SFPBPerformEntityQueryCommand setEnabledDomains:]
+ -[_SFPBPerformEntityQueryCommand setFilterQueries:]
+ GCC_except_table7648
+ OBJC_IVAR_$_SFCardSection._racFeedbackLoggingContent
+ OBJC_IVAR_$_SFCardSection._racFeedbackSubfeatureId
+ OBJC_IVAR_$_SFExecuteMenuItemCommand._applicationBundleIdentifier
+ OBJC_IVAR_$_SFExecuteMenuItemCommand._menuItemIdentifier
+ OBJC_IVAR_$_SFExecuteToolCommand._toolInvocationData
+ OBJC_IVAR_$_SFPerformEntityQueryCommand._enabledDomains
+ OBJC_IVAR_$_SFPerformEntityQueryCommand._filterQueries
+ OBJC_IVAR_$__SFPBCardSection._racFeedbackLoggingContent
+ OBJC_IVAR_$__SFPBCardSection._racFeedbackSubfeatureId
+ OBJC_IVAR_$__SFPBCommand._executeMenuItemCommand
+ OBJC_IVAR_$__SFPBExecuteMenuItemCommand._applicationBundleIdentifier
+ OBJC_IVAR_$__SFPBExecuteMenuItemCommand._menuItemIdentifier
+ OBJC_IVAR_$__SFPBExecuteToolCommand._toolInvocationData
+ OBJC_IVAR_$__SFPBPerformEntityQueryCommand._enabledDomains
+ OBJC_IVAR_$__SFPBPerformEntityQueryCommand._filterQueries
+ PARLogHandleForCategory.logHandles.0.33252
+ PARLogHandleForCategory.logHandles.0.67030
+ PARLogHandleForCategory.logHandles.1.33246
+ PARLogHandleForCategory.logHandles.1.67026
+ PARLogHandleForCategory.logHandles.2.33254
+ PARLogHandleForCategory.logHandles.2.67031
+ PARLogHandleForCategory.logHandles.3.33255
+ PARLogHandleForCategory.logHandles.3.67033
+ PARLogHandleForCategory.logHandles.4.33256
+ PARLogHandleForCategory.logHandles.4.67034
+ PARLogHandleForCategory.logHandles.5.33257
+ PARLogHandleForCategory.logHandles.5.67035
+ PARLogHandleForCategory.onceToken.33244
+ PARLogHandleForCategory.onceToken.67025
+ _OBJC_$_PROP_LIST_RFBinaryButtonCardSection.228
+ _OBJC_$_PROP_LIST_RFButtonCardSection.223
+ _OBJC_$_PROP_LIST_RFDisambiguationTitleCardSection.232
+ _OBJC_$_PROP_LIST_RFExpandableStandardCardSection.232
+ _OBJC_$_PROP_LIST_RFFactItemButtonCardSection.286
+ _OBJC_$_PROP_LIST_RFFactItemDetailedNumberCardSection.252
+ _OBJC_$_PROP_LIST_RFFactItemHeroButtonCardSection.237
+ _OBJC_$_PROP_LIST_RFFactItemHeroNumberCardSection.249
+ _OBJC_$_PROP_LIST_RFFactItemImageRightCardSection.237
+ _OBJC_$_PROP_LIST_RFFactItemShortHeroNumberCardSection.258
+ _OBJC_$_PROP_LIST_RFFactItemShortNumberCardSection.258
+ _OBJC_$_PROP_LIST_RFFactItemStandardCardSection.258
+ _OBJC_$_PROP_LIST_RFLongItemStandardCardSection.238
+ _OBJC_$_PROP_LIST_RFMapCardSection.256
+ _OBJC_$_PROP_LIST_RFMultiButtonCardSection.229
+ _OBJC_$_PROP_LIST_RFPrimaryHeaderMarqueeCardSection.246
+ _OBJC_$_PROP_LIST_RFPrimaryHeaderRichCardSection.256
+ _OBJC_$_PROP_LIST_RFPrimaryHeaderStackedImageCardSection.234
+ _OBJC_$_PROP_LIST_RFPrimaryHeaderStandardCardSection.242
+ _OBJC_$_PROP_LIST_RFReferenceCenteredCardSection.247
+ _OBJC_$_PROP_LIST_RFReferenceFootnoteCardSection.247
+ _OBJC_$_PROP_LIST_RFReferenceItemButtonCardSection.223
+ _OBJC_$_PROP_LIST_RFReferenceItemLogoCardSection.223
+ _OBJC_$_PROP_LIST_RFReferenceRichCardSection.246
+ _OBJC_$_PROP_LIST_RFReferenceStandardCardSection.232
+ _OBJC_$_PROP_LIST_RFSecondaryHeaderEmphasizedCardSection.223
+ _OBJC_$_PROP_LIST_RFSecondaryHeaderStandardCardSection.223
+ _OBJC_$_PROP_LIST_RFSimpleItemPlayerCardSection.248
+ _OBJC_$_PROP_LIST_RFSimpleItemReverseRichCardSection.248
+ _OBJC_$_PROP_LIST_RFSimpleItemRichCardSection.268
+ _OBJC_$_PROP_LIST_RFSimpleItemRichSearchResultCardSection.268
+ _OBJC_$_PROP_LIST_RFSimpleItemStandardCardSection.249
+ _OBJC_$_PROP_LIST_RFSimpleItemVisualElementCardSection.257
+ _OBJC_$_PROP_LIST_RFSummaryItemAlignedTextCardSection.258
+ _OBJC_$_PROP_LIST_RFSummaryItemButtonCardSection.276
+ _OBJC_$_PROP_LIST_RFSummaryItemDetailedTextCardSection.257
+ _OBJC_$_PROP_LIST_RFSummaryItemImageRightCardSection.253
+ _OBJC_$_PROP_LIST_RFSummaryItemPairCardSection.272
+ _OBJC_$_PROP_LIST_RFSummaryItemPairNumberCardSection.302
+ _OBJC_$_PROP_LIST_RFSummaryItemPlayerCardSection.256
+ _OBJC_$_PROP_LIST_RFSummaryItemShortNumberCardSection.263
+ _OBJC_$_PROP_LIST_RFSummaryItemStandardCardSection.257
+ _OBJC_$_PROP_LIST_RFSummaryItemSwitchV2CardSection.256
+ _OBJC_$_PROP_LIST_RFSummaryItemTextCardSection.244
+ _OBJC_$_PROP_LIST_RFTableHeaderCardSection.245
+ _OBJC_$_PROP_LIST_RFTableRowCardSection.241
+ _OBJC_$_PROP_LIST_SFActivityIndicatorCardSection.222
+ _OBJC_$_PROP_LIST_SFAppIconCardSection.227
+ _OBJC_$_PROP_LIST_SFAppLinkCardSection.230
+ _OBJC_$_PROP_LIST_SFArchiveViewCardSection.225
+ _OBJC_$_PROP_LIST_SFAttributionFooterCardSection.251
+ _OBJC_$_PROP_LIST_SFAudioPlaybackCardSection.265
+ _OBJC_$_PROP_LIST_SFButtonCardSection.235
+ _OBJC_$_PROP_LIST_SFButtonListCardSection.233
+ _OBJC_$_PROP_LIST_SFCollectionCardSection.255
+ _OBJC_$_PROP_LIST_SFColorBarCardSection.239
+ _OBJC_$_PROP_LIST_SFCombinedCardSection.223
+ _OBJC_$_PROP_LIST_SFCommandRowCardSection.250
+ _OBJC_$_PROP_LIST_SFCompactRowCardSection.249
+ _OBJC_$_PROP_LIST_SFDescriptionCardSection.320
+ _OBJC_$_PROP_LIST_SFDetailedRowCardSection.350
+ _OBJC_$_PROP_LIST_SFExecuteMenuItemCommand.107
+ _OBJC_$_PROP_LIST_SFExecuteToolCommand.108
+ _OBJC_$_PROP_LIST_SFFindMyCardSection.223
+ _OBJC_$_PROP_LIST_SFFlightCardSection.237
+ _OBJC_$_PROP_LIST_SFGridCardSection.223
+ _OBJC_$_PROP_LIST_SFHeroCardSection.255
+ _OBJC_$_PROP_LIST_SFHeroTitleCardSection.248
+ _OBJC_$_PROP_LIST_SFHorizontalButtonCardSection.223
+ _OBJC_$_PROP_LIST_SFHorizontalScrollCardSection.234
+ _OBJC_$_PROP_LIST_SFImagesCardSection.232
+ _OBJC_$_PROP_LIST_SFInfoCardSection.234
+ _OBJC_$_PROP_LIST_SFKeyValueDataCardSection.232
+ _OBJC_$_PROP_LIST_SFLargeTitleDetailedRowCardSection.241
+ _OBJC_$_PROP_LIST_SFLeadingTrailingCardSection.240
+ _OBJC_$_PROP_LIST_SFLinkPresentationCardSection.240
+ _OBJC_$_PROP_LIST_SFListenToCardSection.235
+ _OBJC_$_PROP_LIST_SFMapCardSection.279
+ _OBJC_$_PROP_LIST_SFMapPlaceCardSection.239
+ _OBJC_$_PROP_LIST_SFMapsDetailedRowCardSection.236
+ _OBJC_$_PROP_LIST_SFMediaInfoCardSection.291
+ _OBJC_$_PROP_LIST_SFMediaPlayerCardSection.233
+ _OBJC_$_PROP_LIST_SFMediaRemoteControlCardSection.236
+ _OBJC_$_PROP_LIST_SFMessageCardSection.255
+ _OBJC_$_PROP_LIST_SFMetaInfoCardSection.249
+ _OBJC_$_PROP_LIST_SFMiniCardSection.240
+ _OBJC_$_PROP_LIST_SFNewsCardSection.259
+ _OBJC_$_PROP_LIST_SFNowPlayingCardSection.230
+ _OBJC_$_PROP_LIST_SFPerformEntityQueryCommand.179
+ _OBJC_$_PROP_LIST_SFPersonHeaderCardSection.223
+ _OBJC_$_PROP_LIST_SFProductCardSection.225
+ _OBJC_$_PROP_LIST_SFResponseWrapperCardSection.246
+ _OBJC_$_PROP_LIST_SFRichTitleCardSection.389
+ _OBJC_$_PROP_LIST_SFRowCardSection.306
+ _OBJC_$_PROP_LIST_SFSafariTableOfContentsCardSection.241
+ _OBJC_$_PROP_LIST_SFScoreboardCardSection.249
+ _OBJC_$_PROP_LIST_SFSectionHeaderCardSection.226
+ _OBJC_$_PROP_LIST_SFSelectableGridCardSection.232
+ _OBJC_$_PROP_LIST_SFSocialMediaPostCardSection.283
+ _OBJC_$_PROP_LIST_SFSplitCardSection.255
+ _OBJC_$_PROP_LIST_SFStockChartCardSection.234
+ _OBJC_$_PROP_LIST_SFStrokeAnimationCardSection.238
+ _OBJC_$_PROP_LIST_SFSuggestionCardSection.275
+ _OBJC_$_PROP_LIST_SFTableHeaderRowCardSection.242
+ _OBJC_$_PROP_LIST_SFTableRowCardSection.275
+ _OBJC_$_PROP_LIST_SFTextColumnsCardSection.239
+ _OBJC_$_PROP_LIST_SFTitleCardSection.236
+ _OBJC_$_PROP_LIST_SFTrackListCardSection.230
+ _OBJC_$_PROP_LIST_SFVerticalLayoutCardSection.260
+ _OBJC_$_PROP_LIST_SFWatchListCardSection.226
+ _OBJC_$_PROP_LIST_SFWatchNowCardSection.231
+ _OBJC_$_PROP_LIST_SFWebCardSection.222
+ _OBJC_$_PROP_LIST_SFWorldMapCardSection.231
+ _OBJC_$_PROP_LIST__SFPBCardSection.1895
+ _OBJC_$_PROP_LIST__SFPBCardSectionValue.3332
+ _OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.3363
+ _OBJC_$_PROP_LIST__SFPBClockImage.3393
+ _OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.3424
+ _OBJC_$_PROP_LIST__SFPBCollectionCardSection.3461
+ _OBJC_$_PROP_LIST__SFPBCollectionStyle.3519
+ _OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.3541
+ _OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.3555
+ _OBJC_$_PROP_LIST__SFPBCollectionStyleRow.3585
+ _OBJC_$_PROP_LIST__SFPBColor.3705
+ _OBJC_$_PROP_LIST__SFPBColorBarCardSection.3728
+ _OBJC_$_PROP_LIST__SFPBCombinedCardSection.3735
+ _OBJC_$_PROP_LIST__SFPBCommand.4460
+ _OBJC_$_PROP_LIST__SFPBCommandButtonItem.4475
+ _OBJC_$_PROP_LIST__SFPBCommandReference.4490
+ _OBJC_$_PROP_LIST__SFPBCommandRowCardSection.4513
+ _OBJC_$_PROP_LIST__SFPBCommandValue.4533
+ _OBJC_$_PROP_LIST__SFPBCompactRowCardSection.4548
+ _OBJC_$_PROP_LIST__SFPBContactButtonItem.4582
+ _OBJC_$_PROP_LIST__SFPBContactCopyItem.4597
+ _OBJC_$_PROP_LIST__SFPBContactImage.4632
+ _OBJC_$_PROP_LIST__SFPBCopyCommand.4652
+ _OBJC_$_PROP_LIST__SFPBCopyItem.4711
+ _OBJC_$_PROP_LIST__SFPBCoreSpotlightButtonItem.4738
+ _OBJC_$_PROP_LIST__SFPBCoreSpotlightCopyItem.4769
+ _OBJC_$_PROP_LIST__SFPBCoreSpotlightRankingSignals.4907
+ _OBJC_$_PROP_LIST__SFPBCoreSpotlightShareItem.4922
+ _OBJC_$_PROP_LIST__SFPBCreateCalendarEventCommand.4942
+ _OBJC_$_PROP_LIST__SFPBCreateContactCommand.4957
+ _OBJC_$_PROP_LIST__SFPBCreateReminderCommand.4977
+ _OBJC_$_PROP_LIST__SFPBDate.4991
+ _OBJC_$_PROP_LIST__SFPBDefaultPunchoutAppIconImage.5006
+ _OBJC_$_PROP_LIST__SFPBDescriptionCardSection.5119
+ _OBJC_$_PROP_LIST__SFPBDetailedRowCardSection.5293
+ _OBJC_$_PROP_LIST__SFPBDomainEngagementScore.5331
+ _OBJC_$_PROP_LIST__SFPBDomainSubscriptionRequestItem.5351
+ _OBJC_$_PROP_LIST__SFPBDrillDownMetadata.5458
+ _OBJC_$_PROP_LIST__SFPBDynamicURLImageResource.5512
+ _OBJC_$_PROP_LIST__SFPBEmailCommand.5519
+ _OBJC_$_PROP_LIST__SFPBEngagementSignal.5581
+ _OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5605
+ _OBJC_$_PROP_LIST__SFPBExecuteMenuItemCommand.5620
+ _OBJC_$_PROP_LIST__SFPBExecuteToolCommand.5643
+ _OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5657
+ _OBJC_$_PROP_LIST__SFPBFindMyCardSection.5664
+ _OBJC_$_PROP_LIST__SFPBFlight.5750
+ _OBJC_$_PROP_LIST__SFPBFlightCardSection.5776
+ _OBJC_$_PROP_LIST__SFPBFlightCheckinCommand.5782
+ _OBJC_$_PROP_LIST__SFPBFlightDetails.5796
+ _OBJC_$_PROP_LIST__SFPBFlightLeg.5936
+ _OBJC_$_PROP_LIST__SFPBFormattedText.5984
+ _OBJC_$_PROP_LIST__SFPBGradientColor.6012
+ _OBJC_$_PROP_LIST__SFPBGraphicalFloat.6026
+ _OBJC_$_PROP_LIST__SFPBGridCardSection.6033
+ _OBJC_$_PROP_LIST__SFPBHashBucketDetail.6063
+ _OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.6114
+ _OBJC_$_PROP_LIST__SFPBHeroCardSection.6121
+ _OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.6136
+ _OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.6155
+ _OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.6162
+ _OBJC_$_PROP_LIST__SFPBImage.6440
+ _OBJC_$_PROP_LIST__SFPBImageCopyItem.6447
+ _OBJC_$_PROP_LIST__SFPBImageDerivedColor.6454
+ _OBJC_$_PROP_LIST__SFPBImageOption.6482
+ _OBJC_$_PROP_LIST__SFPBImagesCardSection.6510
+ _OBJC_$_PROP_LIST__SFPBIndexState.6556
+ _OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.6571
+ _OBJC_$_PROP_LIST__SFPBInfoCardSection.6601
+ _OBJC_$_PROP_LIST__SFPBInfoTuple.6645
+ _OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.6660
+ _OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.6691
+ _OBJC_$_PROP_LIST__SFPBKeyValueTuple.6699
+ _OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.6729
+ _OBJC_$_PROP_LIST__SFPBLatLng.6751
+ _OBJC_$_PROP_LIST__SFPBLaunchAppCommand.6758
+ _OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.6797
+ _OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.6827
+ _OBJC_$_PROP_LIST__SFPBListenToCardSection.6858
+ _OBJC_$_PROP_LIST__SFPBLocalImage.6872
+ _OBJC_$_PROP_LIST__SFPBLocationTypeInfo.6887
+ _OBJC_$_PROP_LIST__SFPBMailRankingSignals.7421
+ _OBJC_$_PROP_LIST__SFPBMailResultDetails.7451
+ _OBJC_$_PROP_LIST__SFPBManageReservationCommand.7457
+ _OBJC_$_PROP_LIST__SFPBMapCardSection.7533
+ _OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.7548
+ _OBJC_$_PROP_LIST__SFPBMapRegion.7594
+ _OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.7609
+ _OBJC_$_PROP_LIST__SFPBMediaArtworkImage.7624
+ _OBJC_$_PROP_LIST__SFPBMediaDetail.7639
+ _OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.7753
+ _OBJC_$_PROP_LIST__SFPBMediaItem.7833
+ _OBJC_$_PROP_LIST__SFPBMediaMetadata.7913
+ _OBJC_$_PROP_LIST__SFPBMediaOffer.7952
+ _OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.7972
+ _OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.8003
+ _OBJC_$_PROP_LIST__SFPBMessageAttachment.8018
+ _OBJC_$_PROP_LIST__SFPBMessageCardSection.8070
+ _OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.8109
+ _OBJC_$_PROP_LIST__SFPBMiniCardSection.8116
+ _OBJC_$_PROP_LIST__SFPBMonogramImage.8139
+ _OBJC_$_PROP_LIST__SFPBMoreResults.8146
+ _OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.8169
+ _OBJC_$_PROP_LIST__SFPBNewsCardSection.8200
+ _OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.8219
+ _OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.8234
+ _OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.8265
+ _OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.8280
+ _OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.8295
+ _OBJC_$_PROP_LIST__SFPBOpenMediaCommand.8310
+ _OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.8317
+ _OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.8324
+ _OBJC_$_PROP_LIST__SFPBPatternModel.8363
+ _OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.8393
+ _OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.8400
+ _OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.8471
+ _OBJC_$_PROP_LIST__SFPBPerformIntentCommand.8494
+ _OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.8501
+ _OBJC_$_PROP_LIST__SFPBPerson.8556
+ _OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.8563
+ _OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.8593
+ _OBJC_$_PROP_LIST__SFPBPhotosAttributes.8647
+ _OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.8683
+ _OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.8713
+ _OBJC_$_PROP_LIST__SFPBPin.8728
+ _OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.8761
+ _OBJC_$_PROP_LIST__SFPBPlayMediaCommand.8784
+ _OBJC_$_PROP_LIST__SFPBPlayVideoCommand.8791
+ _OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.8811
+ _OBJC_$_PROP_LIST__SFPBPointSize.8834
+ _OBJC_$_PROP_LIST__SFPBProduct.8865
+ _OBJC_$_PROP_LIST__SFPBProductAvailability.8887
+ _OBJC_$_PROP_LIST__SFPBProductCardSection.8902
+ _OBJC_$_PROP_LIST__SFPBProductInventory.8958
+ _OBJC_$_PROP_LIST__SFPBProductInventoryResult.8981
+ _OBJC_$_PROP_LIST__SFPBPunchout.9046
+ _OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.9204
+ _OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.9219
+ _OBJC_$_PROP_LIST__SFPBRFAppIconImage.9239
+ _OBJC_$_PROP_LIST__SFPBRFAspectRatio.9247
+ _OBJC_$_PROP_LIST__SFPBRFAttribution.9299
+ _OBJC_$_PROP_LIST__SFPBRFAvatarImage.9318
+ _OBJC_$_PROP_LIST__SFPBRFBadgedImage.9332
+ _OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9355
+ _OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9363
+ _OBJC_$_PROP_LIST__SFPBRFColor.9397
+ _OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.9403
+ _OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.9419
+ _OBJC_$_PROP_LIST__SFPBRFEngageable.9448
+ _OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.9483
+ _OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.9506
+ _OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.9591
+ _OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.9610
+ _OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.9617
+ _OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.9650
+ _OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.9657
+ _OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.9664
+ _OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.9671
+ _OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.9687
+ _OBJC_$_PROP_LIST__SFPBRFFont.9715
+ _OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.10748
+ _OBJC_$_PROP_LIST__SFPBRFFormattedText.9869
+ _OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.9884
+ _OBJC_$_PROP_LIST__SFPBRFImageElement.9904
+ _OBJC_$_PROP_LIST__SFPBRFImageSource.10003
+ _OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.10026
+ _OBJC_$_PROP_LIST__SFPBRFMapAnnotation.10056
+ _OBJC_$_PROP_LIST__SFPBRFMapCardSection.10123
+ _OBJC_$_PROP_LIST__SFPBRFMapMarker.10156
+ _OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.10187
+ _OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.10202
+ _OBJC_$_PROP_LIST__SFPBRFMapMarkerText.10210
+ _OBJC_$_PROP_LIST__SFPBRFMapPoint.10232
+ _OBJC_$_PROP_LIST__SFPBRFMonogramImage.10247
+ _OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.10262
+ _OBJC_$_PROP_LIST__SFPBRFOptionalBool.10269
+ _OBJC_$_PROP_LIST__SFPBRFOptionalFloat.10276
+ _OBJC_$_PROP_LIST__SFPBRFPreview.10283
+ _OBJC_$_PROP_LIST__SFPBRFPreviewList.10305
+ _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.10320
+ _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.10327
+ _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.10335
+ _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.10342
+ _OBJC_$_PROP_LIST__SFPBRFRGBValue.10372
+ _OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.10384
+ _OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.10391
+ _OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.10398
+ _OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.10405
+ _OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.10412
+ _OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.10419
+ _OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.10426
+ _OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.10433
+ _OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.10448
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.10463
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.10470
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.10501
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.10508
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.10515
+ _OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.10539
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.10555
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.10562
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.10569
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.10589
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.10596
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.10635
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.10642
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.10649
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.10664
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.10679
+ _OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.10686
+ _OBJC_$_PROP_LIST__SFPBRFSymbolImage.10741
+ _OBJC_$_PROP_LIST__SFPBRFTableCell.10776
+ _OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.10806
+ _OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.10852
+ _OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.10917
+ _OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.10932
+ _OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.10938
+ _OBJC_$_PROP_LIST__SFPBRFTextElement.10982
+ _OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.10988
+ _OBJC_$_PROP_LIST__SFPBRFTextProperty.11018
+ _OBJC_$_PROP_LIST__SFPBRFUrlImage.11082
+ _OBJC_$_PROP_LIST__SFPBRFVisualElement.11101
+ _OBJC_$_PROP_LIST__SFPBRFVisualProperty.11123
+ _OBJC_$_PROP_LIST__SFPBRFVisualPropertyWithAction.11138
+ _OBJC_$_PROP_LIST__SFPBReferentialCommand.11145
+ _OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.11165
+ _OBJC_$_PROP_LIST__SFPBReminder.11180
+ _OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.11187
+ _OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.11218
+ _OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.11225
+ _OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.11279
+ _OBJC_$_PROP_LIST__SFPBResultEntity.11307
+ _OBJC_$_PROP_LIST__SFPBRichText.11347
+ _OBJC_$_PROP_LIST__SFPBRichTitleCardSection.11495
+ _OBJC_$_PROP_LIST__SFPBRowCardSection.11590
+ _OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.11605
+ _OBJC_$_PROP_LIST__SFPBSafariAttributes.11619
+ _OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.11665
+ _OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.11681
+ _OBJC_$_PROP_LIST__SFPBScene.11703
+ _OBJC_$_PROP_LIST__SFPBScoreboardCardSection.11747
+ _OBJC_$_PROP_LIST__SFPBSearchInAppCommand.11762
+ _OBJC_$_PROP_LIST__SFPBSearchSuggestion.11840
+ _OBJC_$_PROP_LIST__SFPBSearchWebCommand.11847
+ _OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.11855
+ _OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.11885
+ _OBJC_$_PROP_LIST__SFPBShareCommand.11905
+ _OBJC_$_PROP_LIST__SFPBShareItem.11938
+ _OBJC_$_PROP_LIST__SFPBShortcutsImage.11953
+ _OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.11968
+ _OBJC_$_PROP_LIST__SFPBShowContactCardCommand.11983
+ _OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.12034
+ _OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.12049
+ _OBJC_$_PROP_LIST__SFPBShowSFCardCommand.12064
+ _OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.12071
+ _OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.12078
+ _OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.12142
+ _OBJC_$_PROP_LIST__SFPBSplitCardSection.12209
+ _OBJC_$_PROP_LIST__SFPBSportsDetail.12224
+ _OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.12252
+ _OBJC_$_PROP_LIST__SFPBSportsItem.12259
+ _OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.12290
+ _OBJC_$_PROP_LIST__SFPBSportsTeam.12322
+ _OBJC_$_PROP_LIST__SFPBStockChartCardSection.12345
+ _OBJC_$_PROP_LIST__SFPBStoreButtonItem.12368
+ _OBJC_$_PROP_LIST__SFPBStringDictionary.12387
+ _OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.12438
+ _OBJC_$_PROP_LIST__SFPBStructuredLocation.12461
+ _OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.12494
+ _OBJC_$_PROP_LIST__SFPBSuggestionCardSection.12533
+ _OBJC_$_PROP_LIST__SFPBSymbolImage.12575
+ _OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.12599
+ _OBJC_$_PROP_LIST__SFPBTableColumnAlignment.12629
+ _OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.12697
+ _OBJC_$_PROP_LIST__SFPBTableRowCardSection.12717
+ _OBJC_$_PROP_LIST__SFPBText.12734
+ _OBJC_$_PROP_LIST__SFPBTextColumn.12756
+ _OBJC_$_PROP_LIST__SFPBTextColumnSection.12791
+ _OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.12802
+ _OBJC_$_PROP_LIST__SFPBTextCopyItem.12817
+ _OBJC_$_PROP_LIST__SFPBTimeZone.12824
+ _OBJC_$_PROP_LIST__SFPBTitleCardSection.12831
+ _OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.12838
+ _OBJC_$_PROP_LIST__SFPBToggleAudioCommand.12861
+ _OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.12885
+ _OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.12900
+ _OBJC_$_PROP_LIST__SFPBTopic.12943
+ _OBJC_$_PROP_LIST__SFPBTrack.12975
+ _OBJC_$_PROP_LIST__SFPBTrackListCardSection.12997
+ _OBJC_$_PROP_LIST__SFPBURL.13004
+ _OBJC_$_PROP_LIST__SFPBURLImage.13019
+ _OBJC_$_PROP_LIST__SFPBURLShareItem.13026
+ _OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.13041
+ _OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.13056
+ _OBJC_$_PROP_LIST__SFPBUserActivityData.13087
+ _OBJC_$_PROP_LIST__SFPBUserActivityInfo.13110
+ _OBJC_$_PROP_LIST__SFPBUserReportRequest.13185
+ _OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.13216
+ _OBJC_$_PROP_LIST__SFPBViewEmailCommand.13222
+ _OBJC_$_PROP_LIST__SFPBWatchListButtonItem.13229
+ _OBJC_$_PROP_LIST__SFPBWatchListCardSection.13236
+ _OBJC_$_PROP_LIST__SFPBWatchListItem.13315
+ _OBJC_$_PROP_LIST__SFPBWatchNowCardSection.13329
+ _OBJC_$_PROP_LIST__SFPBWeatherColor.13376
+ _OBJC_$_PROP_LIST__SFPBWeatherDetails.13383
+ _OBJC_$_PROP_LIST__SFPBWebCardSection.13398
+ _OBJC_$_PROP_LIST__SFPBWorldMapCardSection.13421
+ _OBJC_CLASS_$_SFExecuteMenuItemCommand
+ _OBJC_CLASS_$__SFPBExecuteMenuItemCommand
+ _OBJC_METACLASS_$_SFExecuteMenuItemCommand
+ _OBJC_METACLASS_$__SFPBExecuteMenuItemCommand
+ __OBJC_$_CLASS_METHODS_SFExecuteMenuItemCommand
+ __OBJC_$_CLASS_PROP_LIST_SFExecuteMenuItemCommand
+ __OBJC_$_CLASS_PROP_LIST__SFPBExecuteMenuItemCommand
+ __OBJC_$_INSTANCE_METHODS_SFExecuteMenuItemCommand(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBExecuteMenuItemCommand(FacadeInitializer)
+ __OBJC_$_INSTANCE_VARIABLES_SFExecuteMenuItemCommand
+ __OBJC_$_INSTANCE_VARIABLES__SFPBExecuteMenuItemCommand
+ __OBJC_$_PROP_LIST_SFExecuteMenuItemCommand
+ __OBJC_$_PROP_LIST__SFPBExecuteMenuItemCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFExecuteMenuItemCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBExecuteMenuItemCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFExecuteMenuItemCommand
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBExecuteMenuItemCommand
+ __OBJC_$_PROTOCOL_REFS_SFExecuteMenuItemCommand
+ __OBJC_$_PROTOCOL_REFS__SFPBExecuteMenuItemCommand
+ __OBJC_CLASS_PROTOCOLS_$_SFExecuteMenuItemCommand
+ __OBJC_CLASS_PROTOCOLS_$__SFPBExecuteMenuItemCommand
+ __OBJC_CLASS_RO_$_SFExecuteMenuItemCommand
+ __OBJC_CLASS_RO_$__SFPBExecuteMenuItemCommand
+ __OBJC_LABEL_PROTOCOL_$_SFExecuteMenuItemCommand
+ __OBJC_LABEL_PROTOCOL_$__SFPBExecuteMenuItemCommand
+ __OBJC_METACLASS_RO_$_SFExecuteMenuItemCommand
+ __OBJC_METACLASS_RO_$__SFPBExecuteMenuItemCommand
+ __OBJC_PROTOCOL_$_SFExecuteMenuItemCommand
+ __OBJC_PROTOCOL_$__SFPBExecuteMenuItemCommand
+ __PARLogHandleForCategory_block_invoke.33250
+ __PARLogHandleForCategory_block_invoke.67028
+ __SFPBExecuteMenuItemCommandReadFrom
+ ___55-[SFCardSection(ProtobufInitializer) initWithProtobuf:]_block_invoke
+ __block_literal_global.33245
+ __block_literal_global.34017
+ __block_literal_global.35723
+ __block_literal_global.67041
+ __getDispatchQueue_block_invoke.67045
+ _objc_msgSend$addEnabledDomains:
+ _objc_msgSend$addFilterQueries:
+ _objc_msgSend$enabledDomains
+ _objc_msgSend$executeMenuItemCommand
+ _objc_msgSend$filterQueries
+ _objc_msgSend$menuItemIdentifier
+ _objc_msgSend$racFeedbackLoggingContent
+ _objc_msgSend$racFeedbackSubfeatureId
+ _objc_msgSend$setEnabledDomains:
+ _objc_msgSend$setExecuteMenuItemCommand:
+ _objc_msgSend$setFilterQueries:
+ _objc_msgSend$setMenuItemIdentifier:
+ _objc_msgSend$setRacFeedbackLoggingContent:
+ _objc_msgSend$setRacFeedbackLoggingContent:forKey:
+ _objc_msgSend$setRacFeedbackSubfeatureId:
+ _objc_msgSend$setToolInvocationData:
+ _objc_msgSend$toolInvocationData
+ getDispatchQueue.67039
+ getDispatchQueue.onceToken.67040
+ getDispatchQueue.queue.67042
- GCC_except_table7622
- PARLogHandleForCategory.logHandles.0.32579
- PARLogHandleForCategory.logHandles.0.65857
- PARLogHandleForCategory.logHandles.1.32573
- PARLogHandleForCategory.logHandles.1.65853
- PARLogHandleForCategory.logHandles.2.32581
- PARLogHandleForCategory.logHandles.2.65858
- PARLogHandleForCategory.logHandles.3.32582
- PARLogHandleForCategory.logHandles.3.65860
- PARLogHandleForCategory.logHandles.4.32583
- PARLogHandleForCategory.logHandles.4.65861
- PARLogHandleForCategory.logHandles.5.32584
- PARLogHandleForCategory.logHandles.5.65862
- PARLogHandleForCategory.onceToken.32571
- PARLogHandleForCategory.onceToken.65852
- _OBJC_$_PROP_LIST_RFBinaryButtonCardSection.219
- _OBJC_$_PROP_LIST_RFButtonCardSection.214
- _OBJC_$_PROP_LIST_RFDisambiguationTitleCardSection.223
- _OBJC_$_PROP_LIST_RFExpandableStandardCardSection.223
- _OBJC_$_PROP_LIST_RFFactItemButtonCardSection.277
- _OBJC_$_PROP_LIST_RFFactItemDetailedNumberCardSection.243
- _OBJC_$_PROP_LIST_RFFactItemHeroButtonCardSection.228
- _OBJC_$_PROP_LIST_RFFactItemHeroNumberCardSection.240
- _OBJC_$_PROP_LIST_RFFactItemImageRightCardSection.228
- _OBJC_$_PROP_LIST_RFFactItemShortHeroNumberCardSection.249
- _OBJC_$_PROP_LIST_RFFactItemShortNumberCardSection.249
- _OBJC_$_PROP_LIST_RFFactItemStandardCardSection.249
- _OBJC_$_PROP_LIST_RFLongItemStandardCardSection.229
- _OBJC_$_PROP_LIST_RFMapCardSection.247
- _OBJC_$_PROP_LIST_RFMultiButtonCardSection.220
- _OBJC_$_PROP_LIST_RFPrimaryHeaderMarqueeCardSection.237
- _OBJC_$_PROP_LIST_RFPrimaryHeaderRichCardSection.247
- _OBJC_$_PROP_LIST_RFPrimaryHeaderStackedImageCardSection.225
- _OBJC_$_PROP_LIST_RFPrimaryHeaderStandardCardSection.233
- _OBJC_$_PROP_LIST_RFReferenceCenteredCardSection.238
- _OBJC_$_PROP_LIST_RFReferenceFootnoteCardSection.238
- _OBJC_$_PROP_LIST_RFReferenceItemButtonCardSection.214
- _OBJC_$_PROP_LIST_RFReferenceItemLogoCardSection.214
- _OBJC_$_PROP_LIST_RFReferenceRichCardSection.237
- _OBJC_$_PROP_LIST_RFReferenceStandardCardSection.223
- _OBJC_$_PROP_LIST_RFSecondaryHeaderEmphasizedCardSection.214
- _OBJC_$_PROP_LIST_RFSecondaryHeaderStandardCardSection.214
- _OBJC_$_PROP_LIST_RFSimpleItemPlayerCardSection.239
- _OBJC_$_PROP_LIST_RFSimpleItemReverseRichCardSection.239
- _OBJC_$_PROP_LIST_RFSimpleItemRichCardSection.259
- _OBJC_$_PROP_LIST_RFSimpleItemRichSearchResultCardSection.259
- _OBJC_$_PROP_LIST_RFSimpleItemStandardCardSection.240
- _OBJC_$_PROP_LIST_RFSimpleItemVisualElementCardSection.248
- _OBJC_$_PROP_LIST_RFSummaryItemAlignedTextCardSection.249
- _OBJC_$_PROP_LIST_RFSummaryItemButtonCardSection.267
- _OBJC_$_PROP_LIST_RFSummaryItemDetailedTextCardSection.248
- _OBJC_$_PROP_LIST_RFSummaryItemImageRightCardSection.244
- _OBJC_$_PROP_LIST_RFSummaryItemPairCardSection.263
- _OBJC_$_PROP_LIST_RFSummaryItemPairNumberCardSection.293
- _OBJC_$_PROP_LIST_RFSummaryItemPlayerCardSection.247
- _OBJC_$_PROP_LIST_RFSummaryItemShortNumberCardSection.254
- _OBJC_$_PROP_LIST_RFSummaryItemStandardCardSection.248
- _OBJC_$_PROP_LIST_RFSummaryItemSwitchV2CardSection.247
- _OBJC_$_PROP_LIST_RFSummaryItemTextCardSection.235
- _OBJC_$_PROP_LIST_RFTableHeaderCardSection.236
- _OBJC_$_PROP_LIST_RFTableRowCardSection.232
- _OBJC_$_PROP_LIST_SFActivityIndicatorCardSection.213
- _OBJC_$_PROP_LIST_SFAppIconCardSection.218
- _OBJC_$_PROP_LIST_SFAppLinkCardSection.221
- _OBJC_$_PROP_LIST_SFArchiveViewCardSection.216
- _OBJC_$_PROP_LIST_SFAttributionFooterCardSection.242
- _OBJC_$_PROP_LIST_SFAudioPlaybackCardSection.256
- _OBJC_$_PROP_LIST_SFButtonCardSection.226
- _OBJC_$_PROP_LIST_SFButtonListCardSection.224
- _OBJC_$_PROP_LIST_SFCollectionCardSection.246
- _OBJC_$_PROP_LIST_SFColorBarCardSection.230
- _OBJC_$_PROP_LIST_SFCombinedCardSection.214
- _OBJC_$_PROP_LIST_SFCommandRowCardSection.241
- _OBJC_$_PROP_LIST_SFCompactRowCardSection.240
- _OBJC_$_PROP_LIST_SFDescriptionCardSection.311
- _OBJC_$_PROP_LIST_SFDetailedRowCardSection.341
- _OBJC_$_PROP_LIST_SFExecuteToolCommand.102
- _OBJC_$_PROP_LIST_SFFindMyCardSection.214
- _OBJC_$_PROP_LIST_SFFlightCardSection.228
- _OBJC_$_PROP_LIST_SFGridCardSection.214
- _OBJC_$_PROP_LIST_SFHeroCardSection.246
- _OBJC_$_PROP_LIST_SFHeroTitleCardSection.239
- _OBJC_$_PROP_LIST_SFHorizontalButtonCardSection.214
- _OBJC_$_PROP_LIST_SFHorizontalScrollCardSection.225
- _OBJC_$_PROP_LIST_SFImagesCardSection.223
- _OBJC_$_PROP_LIST_SFInfoCardSection.225
- _OBJC_$_PROP_LIST_SFKeyValueDataCardSection.223
- _OBJC_$_PROP_LIST_SFLargeTitleDetailedRowCardSection.232
- _OBJC_$_PROP_LIST_SFLeadingTrailingCardSection.231
- _OBJC_$_PROP_LIST_SFLinkPresentationCardSection.231
- _OBJC_$_PROP_LIST_SFListenToCardSection.226
- _OBJC_$_PROP_LIST_SFMapCardSection.270
- _OBJC_$_PROP_LIST_SFMapPlaceCardSection.230
- _OBJC_$_PROP_LIST_SFMapsDetailedRowCardSection.227
- _OBJC_$_PROP_LIST_SFMediaInfoCardSection.282
- _OBJC_$_PROP_LIST_SFMediaPlayerCardSection.224
- _OBJC_$_PROP_LIST_SFMediaRemoteControlCardSection.227
- _OBJC_$_PROP_LIST_SFMessageCardSection.246
- _OBJC_$_PROP_LIST_SFMetaInfoCardSection.240
- _OBJC_$_PROP_LIST_SFMiniCardSection.231
- _OBJC_$_PROP_LIST_SFNewsCardSection.250
- _OBJC_$_PROP_LIST_SFNowPlayingCardSection.221
- _OBJC_$_PROP_LIST_SFPerformEntityQueryCommand.165
- _OBJC_$_PROP_LIST_SFPersonHeaderCardSection.214
- _OBJC_$_PROP_LIST_SFProductCardSection.216
- _OBJC_$_PROP_LIST_SFResponseWrapperCardSection.237
- _OBJC_$_PROP_LIST_SFRichTitleCardSection.380
- _OBJC_$_PROP_LIST_SFRowCardSection.297
- _OBJC_$_PROP_LIST_SFSafariTableOfContentsCardSection.232
- _OBJC_$_PROP_LIST_SFScoreboardCardSection.240
- _OBJC_$_PROP_LIST_SFSectionHeaderCardSection.217
- _OBJC_$_PROP_LIST_SFSelectableGridCardSection.223
- _OBJC_$_PROP_LIST_SFSocialMediaPostCardSection.274
- _OBJC_$_PROP_LIST_SFSplitCardSection.246
- _OBJC_$_PROP_LIST_SFStockChartCardSection.225
- _OBJC_$_PROP_LIST_SFStrokeAnimationCardSection.229
- _OBJC_$_PROP_LIST_SFSuggestionCardSection.266
- _OBJC_$_PROP_LIST_SFTableHeaderRowCardSection.233
- _OBJC_$_PROP_LIST_SFTableRowCardSection.266
- _OBJC_$_PROP_LIST_SFTextColumnsCardSection.230
- _OBJC_$_PROP_LIST_SFTitleCardSection.227
- _OBJC_$_PROP_LIST_SFTrackListCardSection.221
- _OBJC_$_PROP_LIST_SFVerticalLayoutCardSection.251
- _OBJC_$_PROP_LIST_SFWatchListCardSection.217
- _OBJC_$_PROP_LIST_SFWatchNowCardSection.222
- _OBJC_$_PROP_LIST_SFWebCardSection.213
- _OBJC_$_PROP_LIST_SFWorldMapCardSection.222
- _OBJC_$_PROP_LIST__SFPBCardSection.1869
- _OBJC_$_PROP_LIST__SFPBCardSectionValue.3306
- _OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.3337
- _OBJC_$_PROP_LIST__SFPBClockImage.3367
- _OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.3398
- _OBJC_$_PROP_LIST__SFPBCollectionCardSection.3435
- _OBJC_$_PROP_LIST__SFPBCollectionStyle.3493
- _OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.3515
- _OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.3529
- _OBJC_$_PROP_LIST__SFPBCollectionStyleRow.3559
- _OBJC_$_PROP_LIST__SFPBColor.3679
- _OBJC_$_PROP_LIST__SFPBColorBarCardSection.3702
- _OBJC_$_PROP_LIST__SFPBCombinedCardSection.3709
- _OBJC_$_PROP_LIST__SFPBCommand.4421
- _OBJC_$_PROP_LIST__SFPBCommandButtonItem.4436
- _OBJC_$_PROP_LIST__SFPBCommandReference.4451
- _OBJC_$_PROP_LIST__SFPBCommandRowCardSection.4474
- _OBJC_$_PROP_LIST__SFPBCommandValue.4494
- _OBJC_$_PROP_LIST__SFPBCompactRowCardSection.4509
- _OBJC_$_PROP_LIST__SFPBContactButtonItem.4543
- _OBJC_$_PROP_LIST__SFPBContactCopyItem.4558
- _OBJC_$_PROP_LIST__SFPBContactImage.4593
- _OBJC_$_PROP_LIST__SFPBCopyCommand.4613
- _OBJC_$_PROP_LIST__SFPBCopyItem.4672
- _OBJC_$_PROP_LIST__SFPBCoreSpotlightButtonItem.4699
- _OBJC_$_PROP_LIST__SFPBCoreSpotlightCopyItem.4730
- _OBJC_$_PROP_LIST__SFPBCoreSpotlightRankingSignals.4868
- _OBJC_$_PROP_LIST__SFPBCoreSpotlightShareItem.4883
- _OBJC_$_PROP_LIST__SFPBCreateCalendarEventCommand.4903
- _OBJC_$_PROP_LIST__SFPBCreateContactCommand.4918
- _OBJC_$_PROP_LIST__SFPBCreateReminderCommand.4938
- _OBJC_$_PROP_LIST__SFPBDate.4952
- _OBJC_$_PROP_LIST__SFPBDefaultPunchoutAppIconImage.4967
- _OBJC_$_PROP_LIST__SFPBDescriptionCardSection.5080
- _OBJC_$_PROP_LIST__SFPBDetailedRowCardSection.5254
- _OBJC_$_PROP_LIST__SFPBDomainEngagementScore.5292
- _OBJC_$_PROP_LIST__SFPBDomainSubscriptionRequestItem.5312
- _OBJC_$_PROP_LIST__SFPBDrillDownMetadata.5419
- _OBJC_$_PROP_LIST__SFPBDynamicURLImageResource.5473
- _OBJC_$_PROP_LIST__SFPBEmailCommand.5480
- _OBJC_$_PROP_LIST__SFPBEngagementSignal.5542
- _OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5566
- _OBJC_$_PROP_LIST__SFPBExecuteToolCommand.5581
- _OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5595
- _OBJC_$_PROP_LIST__SFPBFindMyCardSection.5602
- _OBJC_$_PROP_LIST__SFPBFlight.5688
- _OBJC_$_PROP_LIST__SFPBFlightCardSection.5714
- _OBJC_$_PROP_LIST__SFPBFlightCheckinCommand.5720
- _OBJC_$_PROP_LIST__SFPBFlightDetails.5734
- _OBJC_$_PROP_LIST__SFPBFlightLeg.5874
- _OBJC_$_PROP_LIST__SFPBFormattedText.5922
- _OBJC_$_PROP_LIST__SFPBGradientColor.5950
- _OBJC_$_PROP_LIST__SFPBGraphicalFloat.5964
- _OBJC_$_PROP_LIST__SFPBGridCardSection.5971
- _OBJC_$_PROP_LIST__SFPBHashBucketDetail.6001
- _OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.6052
- _OBJC_$_PROP_LIST__SFPBHeroCardSection.6059
- _OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.6074
- _OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.6093
- _OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.6100
- _OBJC_$_PROP_LIST__SFPBImage.6378
- _OBJC_$_PROP_LIST__SFPBImageCopyItem.6385
- _OBJC_$_PROP_LIST__SFPBImageDerivedColor.6392
- _OBJC_$_PROP_LIST__SFPBImageOption.6420
- _OBJC_$_PROP_LIST__SFPBImagesCardSection.6448
- _OBJC_$_PROP_LIST__SFPBIndexState.6494
- _OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.6509
- _OBJC_$_PROP_LIST__SFPBInfoCardSection.6539
- _OBJC_$_PROP_LIST__SFPBInfoTuple.6583
- _OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.6598
- _OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.6629
- _OBJC_$_PROP_LIST__SFPBKeyValueTuple.6637
- _OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.6667
- _OBJC_$_PROP_LIST__SFPBLatLng.6689
- _OBJC_$_PROP_LIST__SFPBLaunchAppCommand.6696
- _OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.6735
- _OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.6765
- _OBJC_$_PROP_LIST__SFPBListenToCardSection.6796
- _OBJC_$_PROP_LIST__SFPBLocalImage.6810
- _OBJC_$_PROP_LIST__SFPBLocationTypeInfo.6825
- _OBJC_$_PROP_LIST__SFPBMailRankingSignals.7359
- _OBJC_$_PROP_LIST__SFPBMailResultDetails.7389
- _OBJC_$_PROP_LIST__SFPBManageReservationCommand.7395
- _OBJC_$_PROP_LIST__SFPBMapCardSection.7471
- _OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.7486
- _OBJC_$_PROP_LIST__SFPBMapRegion.7532
- _OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.7547
- _OBJC_$_PROP_LIST__SFPBMediaArtworkImage.7562
- _OBJC_$_PROP_LIST__SFPBMediaDetail.7577
- _OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.7691
- _OBJC_$_PROP_LIST__SFPBMediaItem.7771
- _OBJC_$_PROP_LIST__SFPBMediaMetadata.7851
- _OBJC_$_PROP_LIST__SFPBMediaOffer.7890
- _OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.7910
- _OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.7941
- _OBJC_$_PROP_LIST__SFPBMessageAttachment.7956
- _OBJC_$_PROP_LIST__SFPBMessageCardSection.8008
- _OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.8047
- _OBJC_$_PROP_LIST__SFPBMiniCardSection.8054
- _OBJC_$_PROP_LIST__SFPBMonogramImage.8077
- _OBJC_$_PROP_LIST__SFPBMoreResults.8084
- _OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.8107
- _OBJC_$_PROP_LIST__SFPBNewsCardSection.8138
- _OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.8157
- _OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.8172
- _OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.8203
- _OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.8218
- _OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.8233
- _OBJC_$_PROP_LIST__SFPBOpenMediaCommand.8248
- _OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.8255
- _OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.8262
- _OBJC_$_PROP_LIST__SFPBPatternModel.8301
- _OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.8331
- _OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.8338
- _OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.8385
- _OBJC_$_PROP_LIST__SFPBPerformIntentCommand.8408
- _OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.8415
- _OBJC_$_PROP_LIST__SFPBPerson.8470
- _OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.8477
- _OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.8507
- _OBJC_$_PROP_LIST__SFPBPhotosAttributes.8561
- _OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.8597
- _OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.8627
- _OBJC_$_PROP_LIST__SFPBPin.8642
- _OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.8675
- _OBJC_$_PROP_LIST__SFPBPlayMediaCommand.8698
- _OBJC_$_PROP_LIST__SFPBPlayVideoCommand.8705
- _OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.8725
- _OBJC_$_PROP_LIST__SFPBPointSize.8748
- _OBJC_$_PROP_LIST__SFPBProduct.8779
- _OBJC_$_PROP_LIST__SFPBProductAvailability.8801
- _OBJC_$_PROP_LIST__SFPBProductCardSection.8816
- _OBJC_$_PROP_LIST__SFPBProductInventory.8872
- _OBJC_$_PROP_LIST__SFPBProductInventoryResult.8895
- _OBJC_$_PROP_LIST__SFPBPunchout.8960
- _OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.9118
- _OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.9133
- _OBJC_$_PROP_LIST__SFPBRFAppIconImage.9153
- _OBJC_$_PROP_LIST__SFPBRFAspectRatio.9161
- _OBJC_$_PROP_LIST__SFPBRFAttribution.9213
- _OBJC_$_PROP_LIST__SFPBRFAvatarImage.9232
- _OBJC_$_PROP_LIST__SFPBRFBadgedImage.9246
- _OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9269
- _OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9277
- _OBJC_$_PROP_LIST__SFPBRFColor.9311
- _OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.9317
- _OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.9333
- _OBJC_$_PROP_LIST__SFPBRFEngageable.9362
- _OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.9397
- _OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.9420
- _OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.9505
- _OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.9524
- _OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.9531
- _OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.9564
- _OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.9571
- _OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.9578
- _OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.9585
- _OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.9601
- _OBJC_$_PROP_LIST__SFPBRFFont.9629
- _OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.10662
- _OBJC_$_PROP_LIST__SFPBRFFormattedText.9783
- _OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.9798
- _OBJC_$_PROP_LIST__SFPBRFImageElement.9818
- _OBJC_$_PROP_LIST__SFPBRFImageSource.9917
- _OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.9940
- _OBJC_$_PROP_LIST__SFPBRFMapAnnotation.9970
- _OBJC_$_PROP_LIST__SFPBRFMapCardSection.10037
- _OBJC_$_PROP_LIST__SFPBRFMapMarker.10070
- _OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.10101
- _OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.10116
- _OBJC_$_PROP_LIST__SFPBRFMapMarkerText.10124
- _OBJC_$_PROP_LIST__SFPBRFMapPoint.10146
- _OBJC_$_PROP_LIST__SFPBRFMonogramImage.10161
- _OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.10176
- _OBJC_$_PROP_LIST__SFPBRFOptionalBool.10183
- _OBJC_$_PROP_LIST__SFPBRFOptionalFloat.10190
- _OBJC_$_PROP_LIST__SFPBRFPreview.10197
- _OBJC_$_PROP_LIST__SFPBRFPreviewList.10219
- _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.10234
- _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.10241
- _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.10249
- _OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.10256
- _OBJC_$_PROP_LIST__SFPBRFRGBValue.10286
- _OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.10298
- _OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.10305
- _OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.10312
- _OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.10319
- _OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.10326
- _OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.10333
- _OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.10340
- _OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.10347
- _OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.10362
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.10377
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.10384
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.10415
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.10422
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.10429
- _OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.10453
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.10469
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.10476
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.10483
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.10503
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.10510
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.10549
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.10556
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.10563
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.10578
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.10593
- _OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.10600
- _OBJC_$_PROP_LIST__SFPBRFSymbolImage.10655
- _OBJC_$_PROP_LIST__SFPBRFTableCell.10690
- _OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.10720
- _OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.10766
- _OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.10831
- _OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.10846
- _OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.10852
- _OBJC_$_PROP_LIST__SFPBRFTextElement.10896
- _OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.10902
- _OBJC_$_PROP_LIST__SFPBRFTextProperty.10932
- _OBJC_$_PROP_LIST__SFPBRFUrlImage.10996
- _OBJC_$_PROP_LIST__SFPBRFVisualElement.11015
- _OBJC_$_PROP_LIST__SFPBRFVisualProperty.11037
- _OBJC_$_PROP_LIST__SFPBRFVisualPropertyWithAction.11052
- _OBJC_$_PROP_LIST__SFPBReferentialCommand.11059
- _OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.11079
- _OBJC_$_PROP_LIST__SFPBReminder.11094
- _OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.11101
- _OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.11132
- _OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.11139
- _OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.11193
- _OBJC_$_PROP_LIST__SFPBResultEntity.11221
- _OBJC_$_PROP_LIST__SFPBRichText.11261
- _OBJC_$_PROP_LIST__SFPBRichTitleCardSection.11409
- _OBJC_$_PROP_LIST__SFPBRowCardSection.11504
- _OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.11519
- _OBJC_$_PROP_LIST__SFPBSafariAttributes.11533
- _OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.11579
- _OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.11595
- _OBJC_$_PROP_LIST__SFPBScene.11617
- _OBJC_$_PROP_LIST__SFPBScoreboardCardSection.11661
- _OBJC_$_PROP_LIST__SFPBSearchInAppCommand.11676
- _OBJC_$_PROP_LIST__SFPBSearchSuggestion.11758
- _OBJC_$_PROP_LIST__SFPBSearchWebCommand.11765
- _OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.11773
- _OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.11803
- _OBJC_$_PROP_LIST__SFPBShareCommand.11823
- _OBJC_$_PROP_LIST__SFPBShareItem.11856
- _OBJC_$_PROP_LIST__SFPBShortcutsImage.11871
- _OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.11886
- _OBJC_$_PROP_LIST__SFPBShowContactCardCommand.11901
- _OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.11952
- _OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.11967
- _OBJC_$_PROP_LIST__SFPBShowSFCardCommand.11982
- _OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.11989
- _OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.11996
- _OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.12060
- _OBJC_$_PROP_LIST__SFPBSplitCardSection.12127
- _OBJC_$_PROP_LIST__SFPBSportsDetail.12142
- _OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.12170
- _OBJC_$_PROP_LIST__SFPBSportsItem.12177
- _OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.12208
- _OBJC_$_PROP_LIST__SFPBSportsTeam.12240
- _OBJC_$_PROP_LIST__SFPBStockChartCardSection.12263
- _OBJC_$_PROP_LIST__SFPBStoreButtonItem.12286
- _OBJC_$_PROP_LIST__SFPBStringDictionary.12305
- _OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.12356
- _OBJC_$_PROP_LIST__SFPBStructuredLocation.12379
- _OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.12412
- _OBJC_$_PROP_LIST__SFPBSuggestionCardSection.12451
- _OBJC_$_PROP_LIST__SFPBSymbolImage.12493
- _OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.12517
- _OBJC_$_PROP_LIST__SFPBTableColumnAlignment.12547
- _OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.12615
- _OBJC_$_PROP_LIST__SFPBTableRowCardSection.12635
- _OBJC_$_PROP_LIST__SFPBText.12652
- _OBJC_$_PROP_LIST__SFPBTextColumn.12674
- _OBJC_$_PROP_LIST__SFPBTextColumnSection.12709
- _OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.12720
- _OBJC_$_PROP_LIST__SFPBTextCopyItem.12735
- _OBJC_$_PROP_LIST__SFPBTimeZone.12742
- _OBJC_$_PROP_LIST__SFPBTitleCardSection.12749
- _OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.12756
- _OBJC_$_PROP_LIST__SFPBToggleAudioCommand.12779
- _OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.12803
- _OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.12818
- _OBJC_$_PROP_LIST__SFPBTopic.12861
- _OBJC_$_PROP_LIST__SFPBTrack.12893
- _OBJC_$_PROP_LIST__SFPBTrackListCardSection.12915
- _OBJC_$_PROP_LIST__SFPBURL.12922
- _OBJC_$_PROP_LIST__SFPBURLImage.12937
- _OBJC_$_PROP_LIST__SFPBURLShareItem.12944
- _OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.12959
- _OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.12974
- _OBJC_$_PROP_LIST__SFPBUserActivityData.13005
- _OBJC_$_PROP_LIST__SFPBUserActivityInfo.13028
- _OBJC_$_PROP_LIST__SFPBUserReportRequest.13103
- _OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.13134
- _OBJC_$_PROP_LIST__SFPBViewEmailCommand.13140
- _OBJC_$_PROP_LIST__SFPBWatchListButtonItem.13147
- _OBJC_$_PROP_LIST__SFPBWatchListCardSection.13154
- _OBJC_$_PROP_LIST__SFPBWatchListItem.13233
- _OBJC_$_PROP_LIST__SFPBWatchNowCardSection.13247
- _OBJC_$_PROP_LIST__SFPBWeatherColor.13294
- _OBJC_$_PROP_LIST__SFPBWeatherDetails.13301
- _OBJC_$_PROP_LIST__SFPBWebCardSection.13316
- _OBJC_$_PROP_LIST__SFPBWorldMapCardSection.13339
- __PARLogHandleForCategory_block_invoke.32577
- __PARLogHandleForCategory_block_invoke.65855
- __block_literal_global.32572
- __block_literal_global.33334
- __block_literal_global.35027
- __block_literal_global.65868
- __getDispatchQueue_block_invoke.65872
- _fmod
- getDispatchQueue.65866
- getDispatchQueue.onceToken.65867
- getDispatchQueue.queue.65869
CStrings:
+ "?\t"
+ "?\n"
+ "@\"_SFPBExecuteMenuItemCommand\""
+ "@\"_SFPBExecuteMenuItemCommand\"16@0:8"
+ "B32@0:8^@16@\"NSString\"24"
+ "B32@0:8^@16@24"
+ "SFExecuteMenuItemCommand"
+ "T@\"NSArray\",C,N,V_enabledDomains"
+ "T@\"NSArray\",C,N,V_filterQueries"
+ "T@\"NSData\",C,N,V_toolInvocationData"
+ "T@\"NSDictionary\",C,N,V_racFeedbackLoggingContent"
+ "T@\"NSMutableDictionary\",&,N"
+ "T@\"NSMutableDictionary\",&,N,V_racFeedbackLoggingContent"
+ "T@\"NSString\",C,N,V_menuItemIdentifier"
+ "T@\"NSString\",C,N,V_racFeedbackSubfeatureId"
+ "T@\"_SFPBExecuteMenuItemCommand\",&,N"
+ "T@\"_SFPBExecuteMenuItemCommand\",&,N,V_executeMenuItemCommand"
+ "_SFPBExecuteMenuItemCommand"
+ "_enabledDomains"
+ "_executeMenuItemCommand"
+ "_filterQueries"
+ "_menuItemIdentifier"
+ "_racFeedbackLoggingContent"
+ "_racFeedbackSubfeatureId"
+ "_toolInvocationData"
+ "addEnabledDomains:"
+ "addFilterQueries:"
+ "clearEnabledDomains"
+ "clearFilterQueries"
+ "enabledDomains"
+ "enabledDomainsAtIndex:"
+ "enabledDomainsCount"
+ "executeMenuItemCommand"
+ "filterQueries"
+ "filterQueriesAtIndex:"
+ "filterQueriesCount"
+ "getRacFeedbackLoggingContent:forKey:"
+ "menuItemIdentifier"
+ "racFeedbackLoggingContent"
+ "racFeedbackSubfeatureId"
+ "setEnabledDomains:"
+ "setExecuteMenuItemCommand:"
+ "setFilterQueries:"
+ "setMenuItemIdentifier:"
+ "setRacFeedbackLoggingContent:"
+ "setRacFeedbackLoggingContent:forKey:"
+ "setRacFeedbackSubfeatureId:"
+ "setToolInvocationData:"
+ "toolInvocationData"
+ "v24@0:8@\"_SFPBExecuteMenuItemCommand\"16"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v32@0:8@16@24"

```
