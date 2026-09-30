## SearchFoundation

> `/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation`

```diff

-3520.78.1.1.3
-  __TEXT.__text: 0x3d44cc
+3520.80.2.0.0
+  __TEXT.__text: 0x3d93c8
   __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x56744
+  __TEXT.__objc_methlist: 0x570ec
   __TEXT.__const: 0x80
   __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__gcc_except_tab: 0x98
-  __TEXT.__cstring: 0x6eb0
+  __TEXT.__cstring: 0x6ed6
   __TEXT.__oslogstring: 0x19a
-  __TEXT.__unwind_info: 0x94c8
-  __TEXT.__objc_classname: 0x4855
-  __TEXT.__objc_methname: 0x30169
-  __TEXT.__objc_methtype: 0xfe4f
-  __TEXT.__objc_stubs: 0x19c00
-  __DATA_CONST.__got: 0x17b0
+  __TEXT.__unwind_info: 0x9610
+  __TEXT.__objc_classname: 0x4903
+  __TEXT.__objc_methname: 0x3031b
+  __TEXT.__objc_methtype: 0xfeac
+  __TEXT.__objc_stubs: 0x19d20
+  __DATA_CONST.__got: 0x17d8
   __DATA_CONST.__const: 0xaa8
-  __DATA_CONST.__objc_classlist: 0x17e8
+  __DATA_CONST.__objc_classlist: 0x1828
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x16a0
+  __DATA_CONST.__objc_protolist: 0x16e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7850
+  __DATA_CONST.__objc_selrefs: 0x7898
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1ef8
+  __DATA_CONST.__objc_superrefs: 0x1f38
   __AUTH_CONST.__auth_got: 0x2f0
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0xd1e0
-  __AUTH_CONST.__objc_const: 0xac490
-  __AUTH.__objc_data: 0xc3a0
-  __DATA.__objc_ivar: 0x44c8
-  __DATA.__data: 0x10f98
+  __AUTH_CONST.__cfstring: 0xd240
+  __AUTH_CONST.__objc_const: 0xad710
+  __AUTH.__objc_data: 0xc620
+  __DATA.__objc_ivar: 0x451c
+  __DATA.__data: 0x11298
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x2b70
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34B6262E-D463-3ABD-AFFC-AC82DF80F141
-  Functions: 17574
-  Symbols:   54123
-  CStrings:  13961
+  UUID: 20DA62B0-2942-3007-BC31-1EC38B605384
+  Functions: 17703
+  Symbols:   54531
+  CStrings:  13999
 
Symbols:
+ +[SFCitationReferenceData supportsSecureCoding]
+ +[SFEntityLinkData supportsSecureCoding]
+ +[SFImageMontageData supportsSecureCoding]
+ +[SFImageReferenceData supportsSecureCoding]
+ -[SFCitationReferenceData .cxx_destruct]
+ -[SFCitationReferenceData card_section_on_tap]
+ -[SFCitationReferenceData copyWithZone:]
+ -[SFCitationReferenceData dictionaryRepresentation]
+ -[SFCitationReferenceData display_name]
+ -[SFCitationReferenceData encodeWithCoder:]
+ -[SFCitationReferenceData hash]
+ -[SFCitationReferenceData initWithCoder:]
+ -[SFCitationReferenceData isEqual:]
+ -[SFCitationReferenceData jsonData]
+ -[SFCitationReferenceData setCard_section_on_tap:]
+ -[SFCitationReferenceData setDisplay_name:]
+ -[SFCitationReferenceData(ProtobufInitializer) initWithProtobuf:]
+ -[SFEntityLinkData .cxx_destruct]
+ -[SFEntityLinkData command]
+ -[SFEntityLinkData copyWithZone:]
+ -[SFEntityLinkData dictionaryRepresentation]
+ -[SFEntityLinkData encodeWithCoder:]
+ -[SFEntityLinkData hash]
+ -[SFEntityLinkData initWithCoder:]
+ -[SFEntityLinkData isEqual:]
+ -[SFEntityLinkData jsonData]
+ -[SFEntityLinkData setCommand:]
+ -[SFEntityLinkData(ProtobufInitializer) initWithProtobuf:]
+ -[SFImageMontageData .cxx_destruct]
+ -[SFImageMontageData copyWithZone:]
+ -[SFImageMontageData dictionaryRepresentation]
+ -[SFImageMontageData encodeWithCoder:]
+ -[SFImageMontageData hash]
+ -[SFImageMontageData images]
+ -[SFImageMontageData initWithCoder:]
+ -[SFImageMontageData isEqual:]
+ -[SFImageMontageData jsonData]
+ -[SFImageMontageData setImages:]
+ -[SFImageMontageData(ProtobufInitializer) initWithProtobuf:]
+ -[SFImageReferenceData .cxx_destruct]
+ -[SFImageReferenceData attribution]
+ -[SFImageReferenceData command]
+ -[SFImageReferenceData copyWithZone:]
+ -[SFImageReferenceData dictionaryRepresentation]
+ -[SFImageReferenceData encodeWithCoder:]
+ -[SFImageReferenceData hasIs_prominent]
+ -[SFImageReferenceData hash]
+ -[SFImageReferenceData height]
+ -[SFImageReferenceData image_url]
+ -[SFImageReferenceData initWithCoder:]
+ -[SFImageReferenceData isEqual:]
+ -[SFImageReferenceData is_prominent]
+ -[SFImageReferenceData jsonData]
+ -[SFImageReferenceData setAttribution:]
+ -[SFImageReferenceData setCommand:]
+ -[SFImageReferenceData setHeight:]
+ -[SFImageReferenceData setImage_url:]
+ -[SFImageReferenceData setIs_prominent:]
+ -[SFImageReferenceData setWidth:]
+ -[SFImageReferenceData width]
+ -[SFImageReferenceData(ProtobufInitializer) initWithProtobuf:]
+ -[_SFPBCitationReferenceData .cxx_destruct]
+ -[_SFPBCitationReferenceData card_section_on_tap]
+ -[_SFPBCitationReferenceData dictionaryRepresentation]
+ -[_SFPBCitationReferenceData display_name]
+ -[_SFPBCitationReferenceData hash]
+ -[_SFPBCitationReferenceData initWithDictionary:]
+ -[_SFPBCitationReferenceData initWithJSON:]
+ -[_SFPBCitationReferenceData isEqual:]
+ -[_SFPBCitationReferenceData jsonData]
+ -[_SFPBCitationReferenceData readFrom:]
+ -[_SFPBCitationReferenceData setCard_section_on_tap:]
+ -[_SFPBCitationReferenceData setDisplay_name:]
+ -[_SFPBCitationReferenceData writeTo:]
+ -[_SFPBCitationReferenceData(FacadeInitializer) initWithFacade:]
+ -[_SFPBEntityLinkData .cxx_destruct]
+ -[_SFPBEntityLinkData command]
+ -[_SFPBEntityLinkData dictionaryRepresentation]
+ -[_SFPBEntityLinkData hash]
+ -[_SFPBEntityLinkData initWithDictionary:]
+ -[_SFPBEntityLinkData initWithJSON:]
+ -[_SFPBEntityLinkData isEqual:]
+ -[_SFPBEntityLinkData jsonData]
+ -[_SFPBEntityLinkData readFrom:]
+ -[_SFPBEntityLinkData setCommand:]
+ -[_SFPBEntityLinkData writeTo:]
+ -[_SFPBEntityLinkData(FacadeInitializer) initWithFacade:]
+ -[_SFPBImageMontageData .cxx_destruct]
+ -[_SFPBImageMontageData addImages:]
+ -[_SFPBImageMontageData clearImages]
+ -[_SFPBImageMontageData dictionaryRepresentation]
+ -[_SFPBImageMontageData hash]
+ -[_SFPBImageMontageData imagesAtIndex:]
+ -[_SFPBImageMontageData imagesCount]
+ -[_SFPBImageMontageData images]
+ -[_SFPBImageMontageData initWithDictionary:]
+ -[_SFPBImageMontageData initWithJSON:]
+ -[_SFPBImageMontageData isEqual:]
+ -[_SFPBImageMontageData jsonData]
+ -[_SFPBImageMontageData readFrom:]
+ -[_SFPBImageMontageData setImages:]
+ -[_SFPBImageMontageData writeTo:]
+ -[_SFPBImageMontageData(FacadeInitializer) initWithFacade:]
+ -[_SFPBImageReferenceData .cxx_destruct]
+ -[_SFPBImageReferenceData attribution]
+ -[_SFPBImageReferenceData command]
+ -[_SFPBImageReferenceData dictionaryRepresentation]
+ -[_SFPBImageReferenceData hash]
+ -[_SFPBImageReferenceData height]
+ -[_SFPBImageReferenceData image_url]
+ -[_SFPBImageReferenceData initWithDictionary:]
+ -[_SFPBImageReferenceData initWithJSON:]
+ -[_SFPBImageReferenceData isEqual:]
+ -[_SFPBImageReferenceData is_prominent]
+ -[_SFPBImageReferenceData jsonData]
+ -[_SFPBImageReferenceData readFrom:]
+ -[_SFPBImageReferenceData setAttribution:]
+ -[_SFPBImageReferenceData setCommand:]
+ -[_SFPBImageReferenceData setHeight:]
+ -[_SFPBImageReferenceData setImage_url:]
+ -[_SFPBImageReferenceData setIs_prominent:]
+ -[_SFPBImageReferenceData setWidth:]
+ -[_SFPBImageReferenceData width]
+ -[_SFPBImageReferenceData writeTo:]
+ -[_SFPBImageReferenceData(FacadeInitializer) initWithFacade:]
+ _OBJC_CLASS_$_SFCitationReferenceData
+ _OBJC_CLASS_$_SFEntityLinkData
+ _OBJC_CLASS_$_SFImageMontageData
+ _OBJC_CLASS_$_SFImageReferenceData
+ _OBJC_CLASS_$__SFPBCitationReferenceData
+ _OBJC_CLASS_$__SFPBEntityLinkData
+ _OBJC_CLASS_$__SFPBImageMontageData
+ _OBJC_CLASS_$__SFPBImageReferenceData
+ _OBJC_IVAR_$_SFCitationReferenceData._card_section_on_tap
+ _OBJC_IVAR_$_SFCitationReferenceData._display_name
+ _OBJC_IVAR_$_SFEntityLinkData._command
+ _OBJC_IVAR_$_SFImageMontageData._images
+ _OBJC_IVAR_$_SFImageReferenceData._attribution
+ _OBJC_IVAR_$_SFImageReferenceData._command
+ _OBJC_IVAR_$_SFImageReferenceData._has
+ _OBJC_IVAR_$_SFImageReferenceData._height
+ _OBJC_IVAR_$_SFImageReferenceData._image_url
+ _OBJC_IVAR_$_SFImageReferenceData._is_prominent
+ _OBJC_IVAR_$_SFImageReferenceData._width
+ _OBJC_IVAR_$__SFPBCitationReferenceData._card_section_on_tap
+ _OBJC_IVAR_$__SFPBCitationReferenceData._display_name
+ _OBJC_IVAR_$__SFPBEntityLinkData._command
+ _OBJC_IVAR_$__SFPBImageMontageData._images
+ _OBJC_IVAR_$__SFPBImageReferenceData._attribution
+ _OBJC_IVAR_$__SFPBImageReferenceData._command
+ _OBJC_IVAR_$__SFPBImageReferenceData._height
+ _OBJC_IVAR_$__SFPBImageReferenceData._image_url
+ _OBJC_IVAR_$__SFPBImageReferenceData._is_prominent
+ _OBJC_IVAR_$__SFPBImageReferenceData._width
+ _OBJC_METACLASS_$_SFCitationReferenceData
+ _OBJC_METACLASS_$_SFEntityLinkData
+ _OBJC_METACLASS_$_SFImageMontageData
+ _OBJC_METACLASS_$_SFImageReferenceData
+ _OBJC_METACLASS_$__SFPBCitationReferenceData
+ _OBJC_METACLASS_$__SFPBEntityLinkData
+ _OBJC_METACLASS_$__SFPBImageMontageData
+ _OBJC_METACLASS_$__SFPBImageReferenceData
+ __OBJC_$_CLASS_METHODS_SFCitationReferenceData
+ __OBJC_$_CLASS_METHODS_SFEntityLinkData
+ __OBJC_$_CLASS_METHODS_SFImageMontageData
+ __OBJC_$_CLASS_METHODS_SFImageReferenceData
+ __OBJC_$_CLASS_PROP_LIST_SFCitationReferenceData
+ __OBJC_$_CLASS_PROP_LIST_SFEntityLinkData
+ __OBJC_$_CLASS_PROP_LIST_SFImageMontageData
+ __OBJC_$_CLASS_PROP_LIST_SFImageReferenceData
+ __OBJC_$_CLASS_PROP_LIST__SFPBCitationReferenceData
+ __OBJC_$_CLASS_PROP_LIST__SFPBEntityLinkData
+ __OBJC_$_CLASS_PROP_LIST__SFPBImageMontageData
+ __OBJC_$_CLASS_PROP_LIST__SFPBImageReferenceData
+ __OBJC_$_INSTANCE_METHODS_SFCitationReferenceData(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFEntityLinkData(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFImageMontageData(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFImageReferenceData(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBCitationReferenceData(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBEntityLinkData(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBImageMontageData(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBImageReferenceData(FacadeInitializer)
+ __OBJC_$_INSTANCE_VARIABLES_SFCitationReferenceData
+ __OBJC_$_INSTANCE_VARIABLES_SFEntityLinkData
+ __OBJC_$_INSTANCE_VARIABLES_SFImageMontageData
+ __OBJC_$_INSTANCE_VARIABLES_SFImageReferenceData
+ __OBJC_$_INSTANCE_VARIABLES__SFPBCitationReferenceData
+ __OBJC_$_INSTANCE_VARIABLES__SFPBEntityLinkData
+ __OBJC_$_INSTANCE_VARIABLES__SFPBImageMontageData
+ __OBJC_$_INSTANCE_VARIABLES__SFPBImageReferenceData
+ __OBJC_$_PROP_LIST_SFCitationReferenceData
+ __OBJC_$_PROP_LIST_SFCitationReferenceData.85
+ __OBJC_$_PROP_LIST_SFEntityLinkData
+ __OBJC_$_PROP_LIST_SFEntityLinkData.77
+ __OBJC_$_PROP_LIST_SFImageMontageData
+ __OBJC_$_PROP_LIST_SFImageMontageData.77
+ __OBJC_$_PROP_LIST_SFImageReferenceData
+ __OBJC_$_PROP_LIST_SFImageReferenceData.115
+ __OBJC_$_PROP_LIST__SFPBCitationReferenceData
+ __OBJC_$_PROP_LIST__SFPBCitationReferenceData.3412
+ __OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.3443
+ __OBJC_$_PROP_LIST__SFPBClockImage.3473
+ __OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.3504
+ __OBJC_$_PROP_LIST__SFPBCollectionCardSection.3541
+ __OBJC_$_PROP_LIST__SFPBCollectionStyle.3599
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.3621
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.3635
+ __OBJC_$_PROP_LIST__SFPBCollectionStyleRow.3665
+ __OBJC_$_PROP_LIST__SFPBColor.3785
+ __OBJC_$_PROP_LIST__SFPBColorBarCardSection.3808
+ __OBJC_$_PROP_LIST__SFPBCombinedCardSection.3815
+ __OBJC_$_PROP_LIST__SFPBCommand.4631
+ __OBJC_$_PROP_LIST__SFPBCommandButtonItem.4646
+ __OBJC_$_PROP_LIST__SFPBCommandReference.4661
+ __OBJC_$_PROP_LIST__SFPBCommandRowCardSection.4684
+ __OBJC_$_PROP_LIST__SFPBCommandValue.4704
+ __OBJC_$_PROP_LIST__SFPBCompactRowCardSection.4719
+ __OBJC_$_PROP_LIST__SFPBContactButtonItem.4753
+ __OBJC_$_PROP_LIST__SFPBContactCopyItem.4768
+ __OBJC_$_PROP_LIST__SFPBContactImage.4803
+ __OBJC_$_PROP_LIST__SFPBCopyCommand.4821
+ __OBJC_$_PROP_LIST__SFPBCopyItem.4893
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightButtonItem.4920
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightCopyItem.4951
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightRankingSignals.5089
+ __OBJC_$_PROP_LIST__SFPBCoreSpotlightShareItem.5104
+ __OBJC_$_PROP_LIST__SFPBCreateCalendarEventCommand.5124
+ __OBJC_$_PROP_LIST__SFPBCreateContactCommand.5139
+ __OBJC_$_PROP_LIST__SFPBCreateReminderCommand.5159
+ __OBJC_$_PROP_LIST__SFPBDate.5173
+ __OBJC_$_PROP_LIST__SFPBDefaultPunchoutAppIconImage.5188
+ __OBJC_$_PROP_LIST__SFPBDescriptionCardSection.5301
+ __OBJC_$_PROP_LIST__SFPBDetailedRowCardSection.5475
+ __OBJC_$_PROP_LIST__SFPBDomainEngagementScore.5513
+ __OBJC_$_PROP_LIST__SFPBDomainSubscriptionRequestItem.5533
+ __OBJC_$_PROP_LIST__SFPBDrillDownMetadata.5640
+ __OBJC_$_PROP_LIST__SFPBDynamicURLImageResource.5694
+ __OBJC_$_PROP_LIST__SFPBEmailCommand.5701
+ __OBJC_$_PROP_LIST__SFPBEmbeddingState.5785
+ __OBJC_$_PROP_LIST__SFPBEngagementSignal.5847
+ __OBJC_$_PROP_LIST__SFPBEntityLinkData
+ __OBJC_$_PROP_LIST__SFPBEntityLinkData.5854
+ __OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5878
+ __OBJC_$_PROP_LIST__SFPBExecuteMenuItemCommand.5893
+ __OBJC_$_PROP_LIST__SFPBExecuteToolCommand.5916
+ __OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5930
+ __OBJC_$_PROP_LIST__SFPBFillToolAppEntityParameterCommand.5953
+ __OBJC_$_PROP_LIST__SFPBFillToolAppParameterCommand.5968
+ __OBJC_$_PROP_LIST__SFPBFillToolFileParameterCommand.5983
+ __OBJC_$_PROP_LIST__SFPBFillToolParameterCommand.5990
+ __OBJC_$_PROP_LIST__SFPBFillToolPersonParameterCommand.5997
+ __OBJC_$_PROP_LIST__SFPBFindMyCardSection.6004
+ __OBJC_$_PROP_LIST__SFPBFlight.6090
+ __OBJC_$_PROP_LIST__SFPBFlightCardSection.6116
+ __OBJC_$_PROP_LIST__SFPBFlightCheckinCommand.6122
+ __OBJC_$_PROP_LIST__SFPBFlightDateDescriptor.6153
+ __OBJC_$_PROP_LIST__SFPBFlightDetails.6167
+ __OBJC_$_PROP_LIST__SFPBFlightLeg.6373
+ __OBJC_$_PROP_LIST__SFPBFormattedText.6421
+ __OBJC_$_PROP_LIST__SFPBGradientColor.6449
+ __OBJC_$_PROP_LIST__SFPBGraphicalFloat.6463
+ __OBJC_$_PROP_LIST__SFPBGridCardSection.6470
+ __OBJC_$_PROP_LIST__SFPBHashBucketDetail.6500
+ __OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.6551
+ __OBJC_$_PROP_LIST__SFPBHeroCardSection.6558
+ __OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.6573
+ __OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.6592
+ __OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.6599
+ __OBJC_$_PROP_LIST__SFPBImage.6903
+ __OBJC_$_PROP_LIST__SFPBImageCopyItem.6910
+ __OBJC_$_PROP_LIST__SFPBImageDerivedColor.6917
+ __OBJC_$_PROP_LIST__SFPBImageMontageData
+ __OBJC_$_PROP_LIST__SFPBImageMontageData.6939
+ __OBJC_$_PROP_LIST__SFPBImageOption.6967
+ __OBJC_$_PROP_LIST__SFPBImageReferenceData
+ __OBJC_$_PROP_LIST__SFPBImageReferenceData.7014
+ __OBJC_$_PROP_LIST__SFPBImagesCardSection.7030
+ __OBJC_$_PROP_LIST__SFPBIndexState.7092
+ __OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.7107
+ __OBJC_$_PROP_LIST__SFPBInfoCardSection.7137
+ __OBJC_$_PROP_LIST__SFPBInfoTuple.7181
+ __OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.7204
+ __OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.7235
+ __OBJC_$_PROP_LIST__SFPBKeyValueTuple.7243
+ __OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.7273
+ __OBJC_$_PROP_LIST__SFPBLatLng.7295
+ __OBJC_$_PROP_LIST__SFPBLaunchAppCommand.7310
+ __OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.7349
+ __OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.7379
+ __OBJC_$_PROP_LIST__SFPBListenToCardSection.7407
+ __OBJC_$_PROP_LIST__SFPBLocalImage.7421
+ __OBJC_$_PROP_LIST__SFPBLocationTypeInfo.7436
+ __OBJC_$_PROP_LIST__SFPBMailRankingSignals.7970
+ __OBJC_$_PROP_LIST__SFPBMailResultDetails.8000
+ __OBJC_$_PROP_LIST__SFPBManageReservationCommand.8006
+ __OBJC_$_PROP_LIST__SFPBMapCardSection.8082
+ __OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.8097
+ __OBJC_$_PROP_LIST__SFPBMapRegion.8143
+ __OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.8158
+ __OBJC_$_PROP_LIST__SFPBMediaArtworkImage.8173
+ __OBJC_$_PROP_LIST__SFPBMediaDetail.8188
+ __OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.8302
+ __OBJC_$_PROP_LIST__SFPBMediaItem.8382
+ __OBJC_$_PROP_LIST__SFPBMediaMetadata.8462
+ __OBJC_$_PROP_LIST__SFPBMediaOffer.8501
+ __OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.8521
+ __OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.8552
+ __OBJC_$_PROP_LIST__SFPBMessageAttachment.8567
+ __OBJC_$_PROP_LIST__SFPBMessageCardSection.8619
+ __OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.8658
+ __OBJC_$_PROP_LIST__SFPBMiniCardSection.8665
+ __OBJC_$_PROP_LIST__SFPBMonogramImage.8688
+ __OBJC_$_PROP_LIST__SFPBMoreResults.8695
+ __OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.8718
+ __OBJC_$_PROP_LIST__SFPBNewsCardSection.8749
+ __OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.8768
+ __OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.8783
+ __OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.8814
+ __OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.8829
+ __OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.8844
+ __OBJC_$_PROP_LIST__SFPBOpenMediaCommand.8859
+ __OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.8866
+ __OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.8873
+ __OBJC_$_PROP_LIST__SFPBPasteCommand.8880
+ __OBJC_$_PROP_LIST__SFPBPatternModel.8919
+ __OBJC_$_PROP_LIST__SFPBPegasusDisplayFields.8950
+ __OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.8980
+ __OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.8987
+ __OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.9058
+ __OBJC_$_PROP_LIST__SFPBPerformIntentCommand.9081
+ __OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.9088
+ __OBJC_$_PROP_LIST__SFPBPerson.9140
+ __OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.9147
+ __OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.9177
+ __OBJC_$_PROP_LIST__SFPBPhotosAlbumImage.9192
+ __OBJC_$_PROP_LIST__SFPBPhotosAttributes.9246
+ __OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.9282
+ __OBJC_$_PROP_LIST__SFPBPhotosMemoryImage.9297
+ __OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.9375
+ __OBJC_$_PROP_LIST__SFPBPin.9390
+ __OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.9423
+ __OBJC_$_PROP_LIST__SFPBPlayMediaCommand.9446
+ __OBJC_$_PROP_LIST__SFPBPlayVideoCommand.9453
+ __OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.9473
+ __OBJC_$_PROP_LIST__SFPBPointSize.9482
+ __OBJC_$_PROP_LIST__SFPBProduct.9513
+ __OBJC_$_PROP_LIST__SFPBProductAvailability.9535
+ __OBJC_$_PROP_LIST__SFPBProductCardSection.9550
+ __OBJC_$_PROP_LIST__SFPBProductInventory.9606
+ __OBJC_$_PROP_LIST__SFPBProductInventoryResult.9629
+ __OBJC_$_PROP_LIST__SFPBPunchout.9694
+ __OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.9852
+ __OBJC_$_PROP_LIST__SFPBQuickLookCommand.9859
+ __OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.9867
+ __OBJC_$_PROP_LIST__SFPBRFAppIconImage.9895
+ __OBJC_$_PROP_LIST__SFPBRFAspectRatio.9903
+ __OBJC_$_PROP_LIST__SFPBRFAttribution.9960
+ __OBJC_$_PROP_LIST__SFPBRFAttributionSource.9994
+ __OBJC_$_PROP_LIST__SFPBRFAvatarImage.10013
+ __OBJC_$_PROP_LIST__SFPBRFBadgedImage.10027
+ __OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.10050
+ __OBJC_$_PROP_LIST__SFPBRFButtonCardSection.10058
+ __OBJC_$_PROP_LIST__SFPBRFColor.10092
+ __OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.10098
+ __OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.10106
+ __OBJC_$_PROP_LIST__SFPBRFEngageable.10135
+ __OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.10170
+ __OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.10193
+ __OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.10278
+ __OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.10297
+ __OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.10304
+ __OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.10337
+ __OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.10344
+ __OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.10351
+ __OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.10358
+ __OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.10374
+ __OBJC_$_PROP_LIST__SFPBRFFont.10402
+ __OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.11605
+ __OBJC_$_PROP_LIST__SFPBRFFormattedText.10554
+ __OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.10569
+ __OBJC_$_PROP_LIST__SFPBRFImageElement.10589
+ __OBJC_$_PROP_LIST__SFPBRFImageSource.10688
+ __OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.10727
+ __OBJC_$_PROP_LIST__SFPBRFMapAnnotation.10757
+ __OBJC_$_PROP_LIST__SFPBRFMapCardSection.10824
+ __OBJC_$_PROP_LIST__SFPBRFMapMarker.10857
+ __OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.10888
+ __OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.10903
+ __OBJC_$_PROP_LIST__SFPBRFMapMarkerText.10911
+ __OBJC_$_PROP_LIST__SFPBRFMapPoint.10933
+ __OBJC_$_PROP_LIST__SFPBRFMarkdownCardSection.10971
+ __OBJC_$_PROP_LIST__SFPBRFMonogramImage.10986
+ __OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.11001
+ __OBJC_$_PROP_LIST__SFPBRFOptionalBool.11008
+ __OBJC_$_PROP_LIST__SFPBRFOptionalFloat.11015
+ __OBJC_$_PROP_LIST__SFPBRFPreview.11022
+ __OBJC_$_PROP_LIST__SFPBRFPreviewList.11044
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.11059
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.11066
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.11074
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.11081
+ __OBJC_$_PROP_LIST__SFPBRFRGBValue.11111
+ __OBJC_$_PROP_LIST__SFPBRFReferenceAttributionCardSection.11155
+ __OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.11162
+ __OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.11169
+ __OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.11176
+ __OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.11183
+ __OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.11190
+ __OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.11197
+ __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.11204
+ __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.11211
+ __OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.11234
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.11249
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.11256
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.11287
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.11294
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.11301
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.11325
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.11341
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemAttribution.11365
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.11372
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.11379
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableCardSection.11411
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableContent.11426
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.11446
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.11453
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.11492
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.11499
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.11506
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.11521
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.11536
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.11543
+ __OBJC_$_PROP_LIST__SFPBRFSymbolImage.11598
+ __OBJC_$_PROP_LIST__SFPBRFTableCell.11632
+ __OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.11662
+ __OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.11708
+ __OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.11773
+ __OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.11788
+ __OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.11794
+ __OBJC_$_PROP_LIST__SFPBRFTextElement.11838
+ __OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.11844
+ __OBJC_$_PROP_LIST__SFPBRFTextProperty.11874
+ __OBJC_$_PROP_LIST__SFPBRFUrlImage.11938
+ __OBJC_$_PROP_LIST__SFPBRFVisualElement.11957
+ __OBJC_$_PROP_LIST__SFPBRFVisualProperty.11979
+ __OBJC_$_PROP_LIST__SFPBRFVisualPropertyWithAction.11994
+ __OBJC_$_PROP_LIST__SFPBReferentialCommand.12001
+ __OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.12021
+ __OBJC_$_PROP_LIST__SFPBReminder.12036
+ __OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.12043
+ __OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.12074
+ __OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.12081
+ __OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.12135
+ __OBJC_$_PROP_LIST__SFPBResultEntity.12163
+ __OBJC_$_PROP_LIST__SFPBRichText.12203
+ __OBJC_$_PROP_LIST__SFPBRichTitleCardSection.12351
+ __OBJC_$_PROP_LIST__SFPBRowCardSection.12446
+ __OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.12461
+ __OBJC_$_PROP_LIST__SFPBSafariAttributes.12475
+ __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.12521
+ __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.12537
+ __OBJC_$_PROP_LIST__SFPBScene.12559
+ __OBJC_$_PROP_LIST__SFPBScoreboardCardSection.12603
+ __OBJC_$_PROP_LIST__SFPBSearchInAppCommand.12618
+ __OBJC_$_PROP_LIST__SFPBSearchSuggestion.12696
+ __OBJC_$_PROP_LIST__SFPBSearchWebCommand.12703
+ __OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.12711
+ __OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.12741
+ __OBJC_$_PROP_LIST__SFPBShareCommand.12774
+ __OBJC_$_PROP_LIST__SFPBShareItem.12807
+ __OBJC_$_PROP_LIST__SFPBShortcutsImage.12822
+ __OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.12837
+ __OBJC_$_PROP_LIST__SFPBShowContactCardCommand.12852
+ __OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.12903
+ __OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.12918
+ __OBJC_$_PROP_LIST__SFPBShowSFCardCommand.12933
+ __OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.12940
+ __OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.12947
+ __OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.13011
+ __OBJC_$_PROP_LIST__SFPBSplitCardSection.13078
+ __OBJC_$_PROP_LIST__SFPBSportsDetail.13093
+ __OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.13121
+ __OBJC_$_PROP_LIST__SFPBSportsItem.13128
+ __OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.13159
+ __OBJC_$_PROP_LIST__SFPBSportsTeam.13191
+ __OBJC_$_PROP_LIST__SFPBSpotlightEmbeddingState.13221
+ __OBJC_$_PROP_LIST__SFPBStockChartCardSection.13244
+ __OBJC_$_PROP_LIST__SFPBStoreButtonItem.13267
+ __OBJC_$_PROP_LIST__SFPBStringDictionary.13286
+ __OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.13337
+ __OBJC_$_PROP_LIST__SFPBStructuredLocation.13360
+ __OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.13393
+ __OBJC_$_PROP_LIST__SFPBSuggestionCardSection.13432
+ __OBJC_$_PROP_LIST__SFPBSymbolImage.13474
+ __OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.13498
+ __OBJC_$_PROP_LIST__SFPBTableColumnAlignment.13528
+ __OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.13596
+ __OBJC_$_PROP_LIST__SFPBTableRowCardSection.13616
+ __OBJC_$_PROP_LIST__SFPBText.13633
+ __OBJC_$_PROP_LIST__SFPBTextColumn.13655
+ __OBJC_$_PROP_LIST__SFPBTextColumnSection.13690
+ __OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.13701
+ __OBJC_$_PROP_LIST__SFPBTextCopyItem.13716
+ __OBJC_$_PROP_LIST__SFPBTimeZone.13723
+ __OBJC_$_PROP_LIST__SFPBTitleCardSection.13730
+ __OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.13737
+ __OBJC_$_PROP_LIST__SFPBToggleAudioCommand.13760
+ __OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.13784
+ __OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.13799
+ __OBJC_$_PROP_LIST__SFPBTopic.13842
+ __OBJC_$_PROP_LIST__SFPBTrack.13874
+ __OBJC_$_PROP_LIST__SFPBTrackListCardSection.13896
+ __OBJC_$_PROP_LIST__SFPBURL.13903
+ __OBJC_$_PROP_LIST__SFPBURLCopyItem.13910
+ __OBJC_$_PROP_LIST__SFPBURLImage.13925
+ __OBJC_$_PROP_LIST__SFPBURLShareItem.13932
+ __OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.13947
+ __OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.13962
+ __OBJC_$_PROP_LIST__SFPBUserActivityData.13993
+ __OBJC_$_PROP_LIST__SFPBUserActivityInfo.14016
+ __OBJC_$_PROP_LIST__SFPBUserReportRequest.14091
+ __OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.14122
+ __OBJC_$_PROP_LIST__SFPBViewEmailCommand.14128
+ __OBJC_$_PROP_LIST__SFPBWatchListButtonItem.14135
+ __OBJC_$_PROP_LIST__SFPBWatchListCardSection.14142
+ __OBJC_$_PROP_LIST__SFPBWatchListItem.14221
+ __OBJC_$_PROP_LIST__SFPBWatchNowCardSection.14235
+ __OBJC_$_PROP_LIST__SFPBWeatherColor.14282
+ __OBJC_$_PROP_LIST__SFPBWeatherDetails.14289
+ __OBJC_$_PROP_LIST__SFPBWebCardSection.14304
+ __OBJC_$_PROP_LIST__SFPBWorldMapCardSection.14327
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFCitationReferenceData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFEntityLinkData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFImageMontageData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFImageReferenceData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBCitationReferenceData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBEntityLinkData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBImageMontageData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBImageReferenceData
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFCitationReferenceData
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFEntityLinkData
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFImageMontageData
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFImageReferenceData
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBCitationReferenceData
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBEntityLinkData
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBImageMontageData
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBImageReferenceData
+ __OBJC_$_PROTOCOL_REFS_SFCitationReferenceData
+ __OBJC_$_PROTOCOL_REFS_SFEntityLinkData
+ __OBJC_$_PROTOCOL_REFS_SFImageMontageData
+ __OBJC_$_PROTOCOL_REFS_SFImageReferenceData
+ __OBJC_$_PROTOCOL_REFS__SFPBCitationReferenceData
+ __OBJC_$_PROTOCOL_REFS__SFPBEntityLinkData
+ __OBJC_$_PROTOCOL_REFS__SFPBImageMontageData
+ __OBJC_$_PROTOCOL_REFS__SFPBImageReferenceData
+ __OBJC_CLASS_PROTOCOLS_$_SFCitationReferenceData
+ __OBJC_CLASS_PROTOCOLS_$_SFEntityLinkData
+ __OBJC_CLASS_PROTOCOLS_$_SFImageMontageData
+ __OBJC_CLASS_PROTOCOLS_$_SFImageReferenceData
+ __OBJC_CLASS_PROTOCOLS_$__SFPBCitationReferenceData
+ __OBJC_CLASS_PROTOCOLS_$__SFPBEntityLinkData
+ __OBJC_CLASS_PROTOCOLS_$__SFPBImageMontageData
+ __OBJC_CLASS_PROTOCOLS_$__SFPBImageReferenceData
+ __OBJC_CLASS_RO_$_SFCitationReferenceData
+ __OBJC_CLASS_RO_$_SFEntityLinkData
+ __OBJC_CLASS_RO_$_SFImageMontageData
+ __OBJC_CLASS_RO_$_SFImageReferenceData
+ __OBJC_CLASS_RO_$__SFPBCitationReferenceData
+ __OBJC_CLASS_RO_$__SFPBEntityLinkData
+ __OBJC_CLASS_RO_$__SFPBImageMontageData
+ __OBJC_CLASS_RO_$__SFPBImageReferenceData
+ __OBJC_LABEL_PROTOCOL_$_SFCitationReferenceData
+ __OBJC_LABEL_PROTOCOL_$_SFEntityLinkData
+ __OBJC_LABEL_PROTOCOL_$_SFImageMontageData
+ __OBJC_LABEL_PROTOCOL_$_SFImageReferenceData
+ __OBJC_LABEL_PROTOCOL_$__SFPBCitationReferenceData
+ __OBJC_LABEL_PROTOCOL_$__SFPBEntityLinkData
+ __OBJC_LABEL_PROTOCOL_$__SFPBImageMontageData
+ __OBJC_LABEL_PROTOCOL_$__SFPBImageReferenceData
+ __OBJC_METACLASS_RO_$_SFCitationReferenceData
+ __OBJC_METACLASS_RO_$_SFEntityLinkData
+ __OBJC_METACLASS_RO_$_SFImageMontageData
+ __OBJC_METACLASS_RO_$_SFImageReferenceData
+ __OBJC_METACLASS_RO_$__SFPBCitationReferenceData
+ __OBJC_METACLASS_RO_$__SFPBEntityLinkData
+ __OBJC_METACLASS_RO_$__SFPBImageMontageData
+ __OBJC_METACLASS_RO_$__SFPBImageReferenceData
+ __OBJC_PROTOCOL_$_SFCitationReferenceData
+ __OBJC_PROTOCOL_$_SFEntityLinkData
+ __OBJC_PROTOCOL_$_SFImageMontageData
+ __OBJC_PROTOCOL_$_SFImageReferenceData
+ __OBJC_PROTOCOL_$__SFPBCitationReferenceData
+ __OBJC_PROTOCOL_$__SFPBEntityLinkData
+ __OBJC_PROTOCOL_$__SFPBImageMontageData
+ __OBJC_PROTOCOL_$__SFPBImageReferenceData
+ __SFPBCitationReferenceDataReadFrom
+ __SFPBEntityLinkDataReadFrom
+ __SFPBImageMontageDataReadFrom
+ __SFPBImageReferenceDataReadFrom
+ _objc_msgSend$card_section_on_tap
+ _objc_msgSend$display_name
+ _objc_msgSend$hasIs_prominent
+ _objc_msgSend$image_url
+ _objc_msgSend$is_prominent
+ _objc_msgSend$setCard_section_on_tap:
+ _objc_msgSend$setDisplay_name:
+ _objc_msgSend$setImage_url:
+ _objc_msgSend$setIs_prominent:
- __OBJC_$_PROP_LIST__SFPBClearProactiveCategoryCommand.3417
- __OBJC_$_PROP_LIST__SFPBClockImage.3447
- __OBJC_$_PROP_LIST__SFPBCloudChannelsRequestItem.3478
- __OBJC_$_PROP_LIST__SFPBCollectionCardSection.3515
- __OBJC_$_PROP_LIST__SFPBCollectionStyle.3573
- __OBJC_$_PROP_LIST__SFPBCollectionStyleGrid.3595
- __OBJC_$_PROP_LIST__SFPBCollectionStyleHorizontallyScrolling.3609
- __OBJC_$_PROP_LIST__SFPBCollectionStyleRow.3639
- __OBJC_$_PROP_LIST__SFPBColor.3759
- __OBJC_$_PROP_LIST__SFPBColorBarCardSection.3782
- __OBJC_$_PROP_LIST__SFPBCombinedCardSection.3789
- __OBJC_$_PROP_LIST__SFPBCommand.4605
- __OBJC_$_PROP_LIST__SFPBCommandButtonItem.4620
- __OBJC_$_PROP_LIST__SFPBCommandReference.4635
- __OBJC_$_PROP_LIST__SFPBCommandRowCardSection.4658
- __OBJC_$_PROP_LIST__SFPBCommandValue.4678
- __OBJC_$_PROP_LIST__SFPBCompactRowCardSection.4693
- __OBJC_$_PROP_LIST__SFPBContactButtonItem.4727
- __OBJC_$_PROP_LIST__SFPBContactCopyItem.4742
- __OBJC_$_PROP_LIST__SFPBContactImage.4777
- __OBJC_$_PROP_LIST__SFPBCopyCommand.4795
- __OBJC_$_PROP_LIST__SFPBCopyItem.4867
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightButtonItem.4894
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightCopyItem.4925
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightRankingSignals.5063
- __OBJC_$_PROP_LIST__SFPBCoreSpotlightShareItem.5078
- __OBJC_$_PROP_LIST__SFPBCreateCalendarEventCommand.5098
- __OBJC_$_PROP_LIST__SFPBCreateContactCommand.5113
- __OBJC_$_PROP_LIST__SFPBCreateReminderCommand.5133
- __OBJC_$_PROP_LIST__SFPBDate.5147
- __OBJC_$_PROP_LIST__SFPBDefaultPunchoutAppIconImage.5162
- __OBJC_$_PROP_LIST__SFPBDescriptionCardSection.5275
- __OBJC_$_PROP_LIST__SFPBDetailedRowCardSection.5449
- __OBJC_$_PROP_LIST__SFPBDomainEngagementScore.5487
- __OBJC_$_PROP_LIST__SFPBDomainSubscriptionRequestItem.5507
- __OBJC_$_PROP_LIST__SFPBDrillDownMetadata.5614
- __OBJC_$_PROP_LIST__SFPBDynamicURLImageResource.5668
- __OBJC_$_PROP_LIST__SFPBEmailCommand.5675
- __OBJC_$_PROP_LIST__SFPBEmbeddingState.5759
- __OBJC_$_PROP_LIST__SFPBEngagementSignal.5821
- __OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5845
- __OBJC_$_PROP_LIST__SFPBExecuteMenuItemCommand.5860
- __OBJC_$_PROP_LIST__SFPBExecuteToolCommand.5883
- __OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5897
- __OBJC_$_PROP_LIST__SFPBFillToolAppEntityParameterCommand.5920
- __OBJC_$_PROP_LIST__SFPBFillToolAppParameterCommand.5935
- __OBJC_$_PROP_LIST__SFPBFillToolFileParameterCommand.5950
- __OBJC_$_PROP_LIST__SFPBFillToolParameterCommand.5957
- __OBJC_$_PROP_LIST__SFPBFillToolPersonParameterCommand.5964
- __OBJC_$_PROP_LIST__SFPBFindMyCardSection.5971
- __OBJC_$_PROP_LIST__SFPBFlight.6057
- __OBJC_$_PROP_LIST__SFPBFlightCardSection.6083
- __OBJC_$_PROP_LIST__SFPBFlightCheckinCommand.6089
- __OBJC_$_PROP_LIST__SFPBFlightDateDescriptor.6120
- __OBJC_$_PROP_LIST__SFPBFlightDetails.6134
- __OBJC_$_PROP_LIST__SFPBFlightLeg.6340
- __OBJC_$_PROP_LIST__SFPBFormattedText.6388
- __OBJC_$_PROP_LIST__SFPBGradientColor.6416
- __OBJC_$_PROP_LIST__SFPBGraphicalFloat.6430
- __OBJC_$_PROP_LIST__SFPBGridCardSection.6437
- __OBJC_$_PROP_LIST__SFPBHashBucketDetail.6467
- __OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.6518
- __OBJC_$_PROP_LIST__SFPBHeroCardSection.6525
- __OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.6540
- __OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.6559
- __OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.6566
- __OBJC_$_PROP_LIST__SFPBImage.6870
- __OBJC_$_PROP_LIST__SFPBImageCopyItem.6877
- __OBJC_$_PROP_LIST__SFPBImageDerivedColor.6884
- __OBJC_$_PROP_LIST__SFPBImageOption.6912
- __OBJC_$_PROP_LIST__SFPBImagesCardSection.6940
- __OBJC_$_PROP_LIST__SFPBIndexState.7002
- __OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.7017
- __OBJC_$_PROP_LIST__SFPBInfoCardSection.7047
- __OBJC_$_PROP_LIST__SFPBInfoTuple.7091
- __OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.7114
- __OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.7145
- __OBJC_$_PROP_LIST__SFPBKeyValueTuple.7153
- __OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.7183
- __OBJC_$_PROP_LIST__SFPBLatLng.7205
- __OBJC_$_PROP_LIST__SFPBLaunchAppCommand.7220
- __OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.7259
- __OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.7289
- __OBJC_$_PROP_LIST__SFPBListenToCardSection.7320
- __OBJC_$_PROP_LIST__SFPBLocalImage.7334
- __OBJC_$_PROP_LIST__SFPBLocationTypeInfo.7349
- __OBJC_$_PROP_LIST__SFPBMailRankingSignals.7883
- __OBJC_$_PROP_LIST__SFPBMailResultDetails.7913
- __OBJC_$_PROP_LIST__SFPBManageReservationCommand.7919
- __OBJC_$_PROP_LIST__SFPBMapCardSection.7995
- __OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.8010
- __OBJC_$_PROP_LIST__SFPBMapRegion.8056
- __OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.8071
- __OBJC_$_PROP_LIST__SFPBMediaArtworkImage.8086
- __OBJC_$_PROP_LIST__SFPBMediaDetail.8101
- __OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.8215
- __OBJC_$_PROP_LIST__SFPBMediaItem.8295
- __OBJC_$_PROP_LIST__SFPBMediaMetadata.8375
- __OBJC_$_PROP_LIST__SFPBMediaOffer.8414
- __OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.8434
- __OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.8465
- __OBJC_$_PROP_LIST__SFPBMessageAttachment.8480
- __OBJC_$_PROP_LIST__SFPBMessageCardSection.8532
- __OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.8571
- __OBJC_$_PROP_LIST__SFPBMiniCardSection.8578
- __OBJC_$_PROP_LIST__SFPBMonogramImage.8601
- __OBJC_$_PROP_LIST__SFPBMoreResults.8608
- __OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.8631
- __OBJC_$_PROP_LIST__SFPBNewsCardSection.8662
- __OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.8681
- __OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.8696
- __OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.8727
- __OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.8742
- __OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.8757
- __OBJC_$_PROP_LIST__SFPBOpenMediaCommand.8772
- __OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.8779
- __OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.8786
- __OBJC_$_PROP_LIST__SFPBPasteCommand.8793
- __OBJC_$_PROP_LIST__SFPBPatternModel.8832
- __OBJC_$_PROP_LIST__SFPBPegasusDisplayFields.8863
- __OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.8893
- __OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.8900
- __OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.8971
- __OBJC_$_PROP_LIST__SFPBPerformIntentCommand.8994
- __OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.9001
- __OBJC_$_PROP_LIST__SFPBPerson.9056
- __OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.9063
- __OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.9093
- __OBJC_$_PROP_LIST__SFPBPhotosAlbumImage.9108
- __OBJC_$_PROP_LIST__SFPBPhotosAttributes.9162
- __OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.9198
- __OBJC_$_PROP_LIST__SFPBPhotosMemoryImage.9213
- __OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.9291
- __OBJC_$_PROP_LIST__SFPBPin.9306
- __OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.9339
- __OBJC_$_PROP_LIST__SFPBPlayMediaCommand.9362
- __OBJC_$_PROP_LIST__SFPBPlayVideoCommand.9369
- __OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.9389
- __OBJC_$_PROP_LIST__SFPBPointSize.9412
- __OBJC_$_PROP_LIST__SFPBProduct.9443
- __OBJC_$_PROP_LIST__SFPBProductAvailability.9465
- __OBJC_$_PROP_LIST__SFPBProductCardSection.9480
- __OBJC_$_PROP_LIST__SFPBProductInventory.9536
- __OBJC_$_PROP_LIST__SFPBProductInventoryResult.9559
- __OBJC_$_PROP_LIST__SFPBPunchout.9624
- __OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.9782
- __OBJC_$_PROP_LIST__SFPBQuickLookCommand.9789
- __OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.9797
- __OBJC_$_PROP_LIST__SFPBRFAppIconImage.9825
- __OBJC_$_PROP_LIST__SFPBRFAspectRatio.9833
- __OBJC_$_PROP_LIST__SFPBRFAttribution.9890
- __OBJC_$_PROP_LIST__SFPBRFAttributionSource.9931
- __OBJC_$_PROP_LIST__SFPBRFAvatarImage.9950
- __OBJC_$_PROP_LIST__SFPBRFBadgedImage.9964
- __OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9987
- __OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9995
- __OBJC_$_PROP_LIST__SFPBRFColor.10029
- __OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.10035
- __OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.10043
- __OBJC_$_PROP_LIST__SFPBRFEngageable.10072
- __OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.10107
- __OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.10130
- __OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.10215
- __OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.10234
- __OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.10241
- __OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.10274
- __OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.10281
- __OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.10288
- __OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.10295
- __OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.10311
- __OBJC_$_PROP_LIST__SFPBRFFont.10339
- __OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.11542
- __OBJC_$_PROP_LIST__SFPBRFFormattedText.10491
- __OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.10506
- __OBJC_$_PROP_LIST__SFPBRFImageElement.10526
- __OBJC_$_PROP_LIST__SFPBRFImageSource.10625
- __OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.10664
- __OBJC_$_PROP_LIST__SFPBRFMapAnnotation.10694
- __OBJC_$_PROP_LIST__SFPBRFMapCardSection.10761
- __OBJC_$_PROP_LIST__SFPBRFMapMarker.10794
- __OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.10825
- __OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.10840
- __OBJC_$_PROP_LIST__SFPBRFMapMarkerText.10848
- __OBJC_$_PROP_LIST__SFPBRFMapPoint.10870
- __OBJC_$_PROP_LIST__SFPBRFMarkdownCardSection.10908
- __OBJC_$_PROP_LIST__SFPBRFMonogramImage.10923
- __OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.10938
- __OBJC_$_PROP_LIST__SFPBRFOptionalBool.10945
- __OBJC_$_PROP_LIST__SFPBRFOptionalFloat.10952
- __OBJC_$_PROP_LIST__SFPBRFPreview.10959
- __OBJC_$_PROP_LIST__SFPBRFPreviewList.10981
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.10996
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.11003
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.11011
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.11018
- __OBJC_$_PROP_LIST__SFPBRFRGBValue.11048
- __OBJC_$_PROP_LIST__SFPBRFReferenceAttributionCardSection.11092
- __OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.11099
- __OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.11106
- __OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.11113
- __OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.11120
- __OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.11127
- __OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.11134
- __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.11141
- __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.11148
- __OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.11171
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.11186
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.11193
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.11224
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.11231
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.11238
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.11262
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.11278
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemAttribution.11302
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.11309
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.11316
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableCardSection.11348
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableContent.11363
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.11383
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.11390
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.11429
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.11436
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.11443
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.11458
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.11473
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.11480
- __OBJC_$_PROP_LIST__SFPBRFSymbolImage.11535
- __OBJC_$_PROP_LIST__SFPBRFTableCell.11569
- __OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.11599
- __OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.11645
- __OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.11710
- __OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.11725
- __OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.11731
- __OBJC_$_PROP_LIST__SFPBRFTextElement.11775
- __OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.11781
- __OBJC_$_PROP_LIST__SFPBRFTextProperty.11811
- __OBJC_$_PROP_LIST__SFPBRFUrlImage.11875
- __OBJC_$_PROP_LIST__SFPBRFVisualElement.11894
- __OBJC_$_PROP_LIST__SFPBRFVisualProperty.11916
- __OBJC_$_PROP_LIST__SFPBRFVisualPropertyWithAction.11931
- __OBJC_$_PROP_LIST__SFPBReferentialCommand.11938
- __OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.11958
- __OBJC_$_PROP_LIST__SFPBReminder.11973
- __OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.11980
- __OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.12011
- __OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.12018
- __OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.12072
- __OBJC_$_PROP_LIST__SFPBResultEntity.12100
- __OBJC_$_PROP_LIST__SFPBRichText.12140
- __OBJC_$_PROP_LIST__SFPBRichTitleCardSection.12288
- __OBJC_$_PROP_LIST__SFPBRowCardSection.12383
- __OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.12398
- __OBJC_$_PROP_LIST__SFPBSafariAttributes.12412
- __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.12458
- __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.12474
- __OBJC_$_PROP_LIST__SFPBScene.12496
- __OBJC_$_PROP_LIST__SFPBScoreboardCardSection.12540
- __OBJC_$_PROP_LIST__SFPBSearchInAppCommand.12555
- __OBJC_$_PROP_LIST__SFPBSearchSuggestion.12633
- __OBJC_$_PROP_LIST__SFPBSearchWebCommand.12640
- __OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.12648
- __OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.12678
- __OBJC_$_PROP_LIST__SFPBShareCommand.12711
- __OBJC_$_PROP_LIST__SFPBShareItem.12744
- __OBJC_$_PROP_LIST__SFPBShortcutsImage.12759
- __OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.12774
- __OBJC_$_PROP_LIST__SFPBShowContactCardCommand.12789
- __OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.12840
- __OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.12855
- __OBJC_$_PROP_LIST__SFPBShowSFCardCommand.12870
- __OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.12877
- __OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.12884
- __OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.12948
- __OBJC_$_PROP_LIST__SFPBSplitCardSection.13015
- __OBJC_$_PROP_LIST__SFPBSportsDetail.13030
- __OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.13058
- __OBJC_$_PROP_LIST__SFPBSportsItem.13065
- __OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.13096
- __OBJC_$_PROP_LIST__SFPBSportsTeam.13128
- __OBJC_$_PROP_LIST__SFPBSpotlightEmbeddingState.13158
- __OBJC_$_PROP_LIST__SFPBStockChartCardSection.13181
- __OBJC_$_PROP_LIST__SFPBStoreButtonItem.13204
- __OBJC_$_PROP_LIST__SFPBStringDictionary.13223
- __OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.13274
- __OBJC_$_PROP_LIST__SFPBStructuredLocation.13297
- __OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.13330
- __OBJC_$_PROP_LIST__SFPBSuggestionCardSection.13369
- __OBJC_$_PROP_LIST__SFPBSymbolImage.13411
- __OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.13435
- __OBJC_$_PROP_LIST__SFPBTableColumnAlignment.13465
- __OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.13533
- __OBJC_$_PROP_LIST__SFPBTableRowCardSection.13553
- __OBJC_$_PROP_LIST__SFPBText.13570
- __OBJC_$_PROP_LIST__SFPBTextColumn.13592
- __OBJC_$_PROP_LIST__SFPBTextColumnSection.13627
- __OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.13638
- __OBJC_$_PROP_LIST__SFPBTextCopyItem.13653
- __OBJC_$_PROP_LIST__SFPBTimeZone.13660
- __OBJC_$_PROP_LIST__SFPBTitleCardSection.13667
- __OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.13674
- __OBJC_$_PROP_LIST__SFPBToggleAudioCommand.13697
- __OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.13721
- __OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.13736
- __OBJC_$_PROP_LIST__SFPBTopic.13779
- __OBJC_$_PROP_LIST__SFPBTrack.13811
- __OBJC_$_PROP_LIST__SFPBTrackListCardSection.13833
- __OBJC_$_PROP_LIST__SFPBURL.13840
- __OBJC_$_PROP_LIST__SFPBURLCopyItem.13847
- __OBJC_$_PROP_LIST__SFPBURLImage.13862
- __OBJC_$_PROP_LIST__SFPBURLShareItem.13869
- __OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.13884
- __OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.13899
- __OBJC_$_PROP_LIST__SFPBUserActivityData.13930
- __OBJC_$_PROP_LIST__SFPBUserActivityInfo.13953
- __OBJC_$_PROP_LIST__SFPBUserReportRequest.14028
- __OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.14059
- __OBJC_$_PROP_LIST__SFPBViewEmailCommand.14065
- __OBJC_$_PROP_LIST__SFPBWatchListButtonItem.14072
- __OBJC_$_PROP_LIST__SFPBWatchListCardSection.14079
- __OBJC_$_PROP_LIST__SFPBWatchListItem.14158
- __OBJC_$_PROP_LIST__SFPBWatchNowCardSection.14172
- __OBJC_$_PROP_LIST__SFPBWeatherColor.14219
- __OBJC_$_PROP_LIST__SFPBWeatherDetails.14226
- __OBJC_$_PROP_LIST__SFPBWebCardSection.14241
- __OBJC_$_PROP_LIST__SFPBWorldMapCardSection.14264
CStrings:
+ "@\"_SFPBImageReferenceData\"24@0:8Q16"
+ "SFCitationReferenceData"
+ "SFEntityLinkData"
+ "SFImageMontageData"
+ "SFImageReferenceData"
+ "T@\"NSString\",C,N,V_attribution"
+ "T@\"NSString\",C,N,V_display_name"
+ "T@\"NSString\",C,N,V_image_url"
+ "T@\"SFCardSection\",&,N,V_card_section_on_tap"
+ "T@\"_SFPBCardSection\",&,N,V_card_section_on_tap"
+ "TB,N,V_is_prominent"
+ "Ti,N,V_height"
+ "Ti,N,V_width"
+ "_SFPBCitationReferenceData"
+ "_SFPBEntityLinkData"
+ "_SFPBImageMontageData"
+ "_SFPBImageReferenceData"
+ "_card_section_on_tap"
+ "_display_name"
+ "_image_url"
+ "_is_prominent"
+ "cardSectionOnTap"
+ "card_section_on_tap"
+ "display_name"
+ "hasIs_prominent"
+ "imageUrl"
+ "image_url"
+ "isProminent"
+ "is_prominent"
+ "setCard_section_on_tap:"
+ "setDisplay_name:"
+ "setImage_url:"
+ "setIs_prominent:"
+ "v24@0:8@\"_SFPBImageReferenceData\"16"
+ "{?=\"is_prominent\"b1}"

```
