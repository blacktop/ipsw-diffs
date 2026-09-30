## SearchFoundation

> `/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation`

```diff

-3500.91.2.0.0
-  __TEXT.__text: 0x385d24
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0x54aac
+3500.98.1.0.0
+  __TEXT.__text: 0x38c994
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x55534
   __TEXT.__const: 0x80
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__cstring: 0x6c6c
+  __TEXT.__gcc_except_tab: 0x94
+  __TEXT.__cstring: 0x6dd6
   __TEXT.__oslogstring: 0x19a
-  __TEXT.__unwind_info: 0x82b8
-  __TEXT.__objc_classname: 0x46fd
-  __TEXT.__objc_methname: 0x2ebb6
-  __TEXT.__objc_methtype: 0xf858
-  __TEXT.__objc_stubs: 0x19120
-  __DATA_CONST.__got: 0x1740
+  __TEXT.__unwind_info: 0x8380
+  __TEXT.__objc_classname: 0x4767
+  __TEXT.__objc_methname: 0x2f659
+  __TEXT.__objc_methtype: 0xfa42
+  __TEXT.__objc_stubs: 0x196c0
+  __DATA_CONST.__got: 0x1760
   __DATA_CONST.__const: 0xad0
-  __DATA_CONST.__objc_classlist: 0x1778
+  __DATA_CONST.__objc_classlist: 0x1798
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1630
+  __DATA_CONST.__objc_protolist: 0x1650
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7528
+  __DATA_CONST.__objc_selrefs: 0x7690
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1e68
-  __AUTH_CONST.__auth_got: 0x320
+  __DATA_CONST.__objc_superrefs: 0x1e88
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0xcd40
-  __AUTH_CONST.__objc_const: 0xa8d78
-  __AUTH.__objc_data: 0xbf40
-  __DATA.__objc_ivar: 0x4350
-  __DATA.__data: 0x10a58
+  __AUTH_CONST.__cfstring: 0xcfc0
+  __AUTH_CONST.__objc_const: 0xa9ff8
+  __AUTH.__objc_data: 0xc080
+  __DATA.__objc_ivar: 0x43f0
+  __DATA.__data: 0x10bd8
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x2b70
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C828982A-EFA1-3261-A6D0-A5027BAD5DDE
-  Functions: 17202
-  Symbols:   53019
-  CStrings:  13614
+  UUID: E6C3158D-ECF0-33D9-8200-015FDC910B72
+  Functions: 17330
+  Symbols:   53423
+  CStrings:  13774
 
Symbols:
+ +[SFFlightDateDescriptor supportsSecureCoding]
+ +[SFPegasusDisplayFields supportsSecureCoding]
+ -[RFLongItemStandardCardSection hasIs_fresh]
+ -[RFLongItemStandardCardSection is_fresh]
+ -[RFLongItemStandardCardSection setIs_fresh:]
+ -[SFEmbeddingState hasHasMetadataResults]
+ -[SFEmbeddingState hasMetadataResults]
+ -[SFEmbeddingState setHasMetadataResults:]
+ -[SFFlightDateDescriptor .cxx_destruct]
+ -[SFFlightDateDescriptor bufferMinutes]
+ -[SFFlightDateDescriptor copyWithZone:]
+ -[SFFlightDateDescriptor current]
+ -[SFFlightDateDescriptor dictionaryRepresentation]
+ -[SFFlightDateDescriptor encodeWithCoder:]
+ -[SFFlightDateDescriptor hash]
+ -[SFFlightDateDescriptor initWithCoder:]
+ -[SFFlightDateDescriptor isEqual:]
+ -[SFFlightDateDescriptor jsonData]
+ -[SFFlightDateDescriptor scheduled]
+ -[SFFlightDateDescriptor setBufferMinutes:]
+ -[SFFlightDateDescriptor setCurrent:]
+ -[SFFlightDateDescriptor setScheduled:]
+ -[SFFlightDateDescriptor(ProtobufInitializer) initWithProtobuf:]
+ -[SFFlightLeg gateArrivalTimes]
+ -[SFFlightLeg gateDepartureTimes]
+ -[SFFlightLeg hasPegasusDefinedState]
+ -[SFFlightLeg pegasusDefinedState]
+ -[SFFlightLeg pegasusDisplayFields]
+ -[SFFlightLeg runwayArrivalTimes]
+ -[SFFlightLeg runwayDepartureTimes]
+ -[SFFlightLeg setGateArrivalTimes:]
+ -[SFFlightLeg setGateDepartureTimes:]
+ -[SFFlightLeg setPegasusDefinedState:]
+ -[SFFlightLeg setPegasusDisplayFields:]
+ -[SFFlightLeg setRunwayArrivalTimes:]
+ -[SFFlightLeg setRunwayDepartureTimes:]
+ -[SFPegasusDisplayFields .cxx_destruct]
+ -[SFPegasusDisplayFields arrivalTime]
+ -[SFPegasusDisplayFields copyWithZone:]
+ -[SFPegasusDisplayFields departureTime]
+ -[SFPegasusDisplayFields dictionaryRepresentation]
+ -[SFPegasusDisplayFields displayStatus]
+ -[SFPegasusDisplayFields encodeWithCoder:]
+ -[SFPegasusDisplayFields hash]
+ -[SFPegasusDisplayFields initWithCoder:]
+ -[SFPegasusDisplayFields isEqual:]
+ -[SFPegasusDisplayFields jsonData]
+ -[SFPegasusDisplayFields setArrivalTime:]
+ -[SFPegasusDisplayFields setDepartureTime:]
+ -[SFPegasusDisplayFields setDisplayStatus:]
+ -[SFPegasusDisplayFields(ProtobufInitializer) initWithProtobuf:]
+ -[SFPhotosRankingInfo .cxx_destruct]
+ -[SFPhotosRankingInfo analyzedAndIndexedAssetsPercentage]
+ -[SFPhotosRankingInfo analyzedAssetsPercentage]
+ -[SFPhotosRankingInfo assetsRetrieved]
+ -[SFPhotosRankingInfo collectionsRetrieved]
+ -[SFPhotosRankingInfo embeddedAssetsPercentage]
+ -[SFPhotosRankingInfo hasAssetsRetrieved]
+ -[SFPhotosRankingInfo hasCollectionsRetrieved]
+ -[SFPhotosRankingInfo indexedAssetsPercentage]
+ -[SFPhotosRankingInfo setAnalyzedAndIndexedAssetsPercentage:]
+ -[SFPhotosRankingInfo setAnalyzedAssetsPercentage:]
+ -[SFPhotosRankingInfo setAssetsRetrieved:]
+ -[SFPhotosRankingInfo setCollectionsRetrieved:]
+ -[SFPhotosRankingInfo setEmbeddedAssetsPercentage:]
+ -[SFPhotosRankingInfo setIndexedAssetsPercentage:]
+ -[_SFPBEmbeddingState hasMetadataResults]
+ -[_SFPBEmbeddingState setHasMetadataResults:]
+ -[_SFPBFlightDateDescriptor .cxx_destruct]
+ -[_SFPBFlightDateDescriptor bufferMinutes]
+ -[_SFPBFlightDateDescriptor current]
+ -[_SFPBFlightDateDescriptor dictionaryRepresentation]
+ -[_SFPBFlightDateDescriptor hash]
+ -[_SFPBFlightDateDescriptor initWithDictionary:]
+ -[_SFPBFlightDateDescriptor initWithJSON:]
+ -[_SFPBFlightDateDescriptor isEqual:]
+ -[_SFPBFlightDateDescriptor jsonData]
+ -[_SFPBFlightDateDescriptor readFrom:]
+ -[_SFPBFlightDateDescriptor scheduled]
+ -[_SFPBFlightDateDescriptor setBufferMinutes:]
+ -[_SFPBFlightDateDescriptor setCurrent:]
+ -[_SFPBFlightDateDescriptor setScheduled:]
+ -[_SFPBFlightDateDescriptor writeTo:]
+ -[_SFPBFlightDateDescriptor(FacadeInitializer) initWithFacade:]
+ -[_SFPBFlightLeg gateArrivalTimes]
+ -[_SFPBFlightLeg gateDepartureTimes]
+ -[_SFPBFlightLeg pegasusDefinedState]
+ -[_SFPBFlightLeg pegasusDisplayFields]
+ -[_SFPBFlightLeg runwayArrivalTimes]
+ -[_SFPBFlightLeg runwayDepartureTimes]
+ -[_SFPBFlightLeg setGateArrivalTimes:]
+ -[_SFPBFlightLeg setGateDepartureTimes:]
+ -[_SFPBFlightLeg setPegasusDefinedState:]
+ -[_SFPBFlightLeg setPegasusDisplayFields:]
+ -[_SFPBFlightLeg setRunwayArrivalTimes:]
+ -[_SFPBFlightLeg setRunwayDepartureTimes:]
+ -[_SFPBPegasusDisplayFields .cxx_destruct]
+ -[_SFPBPegasusDisplayFields arrivalTime]
+ -[_SFPBPegasusDisplayFields departureTime]
+ -[_SFPBPegasusDisplayFields dictionaryRepresentation]
+ -[_SFPBPegasusDisplayFields displayStatus]
+ -[_SFPBPegasusDisplayFields hash]
+ -[_SFPBPegasusDisplayFields initWithDictionary:]
+ -[_SFPBPegasusDisplayFields initWithJSON:]
+ -[_SFPBPegasusDisplayFields isEqual:]
+ -[_SFPBPegasusDisplayFields jsonData]
+ -[_SFPBPegasusDisplayFields readFrom:]
+ -[_SFPBPegasusDisplayFields setArrivalTime:]
+ -[_SFPBPegasusDisplayFields setDepartureTime:]
+ -[_SFPBPegasusDisplayFields setDisplayStatus:]
+ -[_SFPBPegasusDisplayFields writeTo:]
+ -[_SFPBPegasusDisplayFields(FacadeInitializer) initWithFacade:]
+ -[_SFPBPhotosRankingInfo analyzedAndIndexedAssetsPercentage]
+ -[_SFPBPhotosRankingInfo analyzedAssetsPercentage]
+ -[_SFPBPhotosRankingInfo assetsRetrieved]
+ -[_SFPBPhotosRankingInfo collectionsRetrieved]
+ -[_SFPBPhotosRankingInfo embeddedAssetsPercentage]
+ -[_SFPBPhotosRankingInfo indexedAssetsPercentage]
+ -[_SFPBPhotosRankingInfo setAnalyzedAndIndexedAssetsPercentage:]
+ -[_SFPBPhotosRankingInfo setAnalyzedAssetsPercentage:]
+ -[_SFPBPhotosRankingInfo setAssetsRetrieved:]
+ -[_SFPBPhotosRankingInfo setCollectionsRetrieved:]
+ -[_SFPBPhotosRankingInfo setEmbeddedAssetsPercentage:]
+ -[_SFPBPhotosRankingInfo setIndexedAssetsPercentage:]
+ -[_SFPBRFLongItemStandardCardSection is_fresh]
+ -[_SFPBRFLongItemStandardCardSection setIs_fresh:]
+ GCC_except_table2767
+ GCC_except_table6412
+ GCC_except_table7968
+ _OBJC_CLASS_$_SFFlightDateDescriptor
+ _OBJC_CLASS_$_SFPegasusDisplayFields
+ _OBJC_CLASS_$__SFPBFlightDateDescriptor
+ _OBJC_CLASS_$__SFPBPegasusDisplayFields
+ _OBJC_IVAR_$_RFLongItemStandardCardSection._is_fresh
+ _OBJC_IVAR_$_SFEmbeddingState._hasMetadataResults
+ _OBJC_IVAR_$_SFFlightDateDescriptor._bufferMinutes
+ _OBJC_IVAR_$_SFFlightDateDescriptor._current
+ _OBJC_IVAR_$_SFFlightDateDescriptor._scheduled
+ _OBJC_IVAR_$_SFFlightLeg._gateArrivalTimes
+ _OBJC_IVAR_$_SFFlightLeg._gateDepartureTimes
+ _OBJC_IVAR_$_SFFlightLeg._pegasusDefinedState
+ _OBJC_IVAR_$_SFFlightLeg._pegasusDisplayFields
+ _OBJC_IVAR_$_SFFlightLeg._runwayArrivalTimes
+ _OBJC_IVAR_$_SFFlightLeg._runwayDepartureTimes
+ _OBJC_IVAR_$_SFPegasusDisplayFields._arrivalTime
+ _OBJC_IVAR_$_SFPegasusDisplayFields._departureTime
+ _OBJC_IVAR_$_SFPegasusDisplayFields._displayStatus
+ _OBJC_IVAR_$_SFPhotosRankingInfo._analyzedAndIndexedAssetsPercentage
+ _OBJC_IVAR_$_SFPhotosRankingInfo._analyzedAssetsPercentage
+ _OBJC_IVAR_$_SFPhotosRankingInfo._assetsRetrieved
+ _OBJC_IVAR_$_SFPhotosRankingInfo._collectionsRetrieved
+ _OBJC_IVAR_$_SFPhotosRankingInfo._embeddedAssetsPercentage
+ _OBJC_IVAR_$_SFPhotosRankingInfo._indexedAssetsPercentage
+ _OBJC_IVAR_$__SFPBEmbeddingState._hasMetadataResults
+ _OBJC_IVAR_$__SFPBFlightDateDescriptor._bufferMinutes
+ _OBJC_IVAR_$__SFPBFlightDateDescriptor._current
+ _OBJC_IVAR_$__SFPBFlightDateDescriptor._scheduled
+ _OBJC_IVAR_$__SFPBFlightLeg._gateArrivalTimes
+ _OBJC_IVAR_$__SFPBFlightLeg._gateDepartureTimes
+ _OBJC_IVAR_$__SFPBFlightLeg._pegasusDefinedState
+ _OBJC_IVAR_$__SFPBFlightLeg._pegasusDisplayFields
+ _OBJC_IVAR_$__SFPBFlightLeg._runwayArrivalTimes
+ _OBJC_IVAR_$__SFPBFlightLeg._runwayDepartureTimes
+ _OBJC_IVAR_$__SFPBPegasusDisplayFields._arrivalTime
+ _OBJC_IVAR_$__SFPBPegasusDisplayFields._departureTime
+ _OBJC_IVAR_$__SFPBPegasusDisplayFields._displayStatus
+ _OBJC_IVAR_$__SFPBPhotosRankingInfo._analyzedAndIndexedAssetsPercentage
+ _OBJC_IVAR_$__SFPBPhotosRankingInfo._analyzedAssetsPercentage
+ _OBJC_IVAR_$__SFPBPhotosRankingInfo._assetsRetrieved
+ _OBJC_IVAR_$__SFPBPhotosRankingInfo._collectionsRetrieved
+ _OBJC_IVAR_$__SFPBPhotosRankingInfo._embeddedAssetsPercentage
+ _OBJC_IVAR_$__SFPBPhotosRankingInfo._indexedAssetsPercentage
+ _OBJC_IVAR_$__SFPBRFLongItemStandardCardSection._is_fresh
+ _OBJC_METACLASS_$_SFFlightDateDescriptor
+ _OBJC_METACLASS_$_SFPegasusDisplayFields
+ _OBJC_METACLASS_$__SFPBFlightDateDescriptor
+ _OBJC_METACLASS_$__SFPBPegasusDisplayFields
+ _PARLogHandleForCategory.logHandles.0.34899
+ _PARLogHandleForCategory.logHandles.0.70609
+ _PARLogHandleForCategory.logHandles.1.34893
+ _PARLogHandleForCategory.logHandles.1.70606
+ _PARLogHandleForCategory.logHandles.2.34901
+ _PARLogHandleForCategory.logHandles.2.70611
+ _PARLogHandleForCategory.logHandles.3.34902
+ _PARLogHandleForCategory.logHandles.3.70612
+ _PARLogHandleForCategory.logHandles.4.34903
+ _PARLogHandleForCategory.logHandles.4.70614
+ _PARLogHandleForCategory.logHandles.5.34904
+ _PARLogHandleForCategory.logHandles.5.70615
+ _PARLogHandleForCategory.onceToken.34891
+ _PARLogHandleForCategory.onceToken.70605
+ __OBJC_$_CLASS_METHODS_SFFlightDateDescriptor
+ __OBJC_$_CLASS_METHODS_SFPegasusDisplayFields
+ __OBJC_$_CLASS_PROP_LIST_SFFlightDateDescriptor
+ __OBJC_$_CLASS_PROP_LIST_SFPegasusDisplayFields
+ __OBJC_$_CLASS_PROP_LIST__SFPBFlightDateDescriptor
+ __OBJC_$_CLASS_PROP_LIST__SFPBPegasusDisplayFields
+ __OBJC_$_INSTANCE_METHODS_SFFlightDateDescriptor(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS_SFPegasusDisplayFields(ProtobufInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBFlightDateDescriptor(FacadeInitializer)
+ __OBJC_$_INSTANCE_METHODS__SFPBPegasusDisplayFields(FacadeInitializer)
+ __OBJC_$_INSTANCE_VARIABLES_SFFlightDateDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_SFPegasusDisplayFields
+ __OBJC_$_INSTANCE_VARIABLES__SFPBFlightDateDescriptor
+ __OBJC_$_INSTANCE_VARIABLES__SFPBPegasusDisplayFields
+ __OBJC_$_PROP_LIST_RFLongItemStandardCardSection.253
+ __OBJC_$_PROP_LIST_SFEmbeddingState.134
+ __OBJC_$_PROP_LIST_SFFlightDateDescriptor
+ __OBJC_$_PROP_LIST_SFFlightDateDescriptor.91
+ __OBJC_$_PROP_LIST_SFFlightLeg.220
+ __OBJC_$_PROP_LIST_SFPegasusDisplayFields
+ __OBJC_$_PROP_LIST_SFPegasusDisplayFields.90
+ __OBJC_$_PROP_LIST_SFPhotosRankingInfo.140
+ __OBJC_$_PROP_LIST__SFPBEmbeddingState.5707
+ __OBJC_$_PROP_LIST__SFPBEngagementSignal.5769
+ __OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5793
+ __OBJC_$_PROP_LIST__SFPBExecuteMenuItemCommand.5808
+ __OBJC_$_PROP_LIST__SFPBExecuteToolCommand.5831
+ __OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5845
+ __OBJC_$_PROP_LIST__SFPBFillToolAppEntityParameterCommand.5868
+ __OBJC_$_PROP_LIST__SFPBFillToolAppParameterCommand.5883
+ __OBJC_$_PROP_LIST__SFPBFillToolFileParameterCommand.5898
+ __OBJC_$_PROP_LIST__SFPBFillToolParameterCommand.5905
+ __OBJC_$_PROP_LIST__SFPBFillToolPersonParameterCommand.5912
+ __OBJC_$_PROP_LIST__SFPBFindMyCardSection.5919
+ __OBJC_$_PROP_LIST__SFPBFlight.6005
+ __OBJC_$_PROP_LIST__SFPBFlightCardSection.6031
+ __OBJC_$_PROP_LIST__SFPBFlightCheckinCommand.6037
+ __OBJC_$_PROP_LIST__SFPBFlightDateDescriptor
+ __OBJC_$_PROP_LIST__SFPBFlightDateDescriptor.6068
+ __OBJC_$_PROP_LIST__SFPBFlightDetails.6082
+ __OBJC_$_PROP_LIST__SFPBFlightLeg.6288
+ __OBJC_$_PROP_LIST__SFPBFormattedText.6336
+ __OBJC_$_PROP_LIST__SFPBGradientColor.6364
+ __OBJC_$_PROP_LIST__SFPBGraphicalFloat.6378
+ __OBJC_$_PROP_LIST__SFPBGridCardSection.6385
+ __OBJC_$_PROP_LIST__SFPBHashBucketDetail.6415
+ __OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.6466
+ __OBJC_$_PROP_LIST__SFPBHeroCardSection.6473
+ __OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.6488
+ __OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.6507
+ __OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.6514
+ __OBJC_$_PROP_LIST__SFPBImage.6818
+ __OBJC_$_PROP_LIST__SFPBImageCopyItem.6825
+ __OBJC_$_PROP_LIST__SFPBImageDerivedColor.6832
+ __OBJC_$_PROP_LIST__SFPBImageOption.6860
+ __OBJC_$_PROP_LIST__SFPBImagesCardSection.6888
+ __OBJC_$_PROP_LIST__SFPBIndexState.6950
+ __OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.6965
+ __OBJC_$_PROP_LIST__SFPBInfoCardSection.6995
+ __OBJC_$_PROP_LIST__SFPBInfoTuple.7039
+ __OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.7062
+ __OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.7093
+ __OBJC_$_PROP_LIST__SFPBKeyValueTuple.7101
+ __OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.7131
+ __OBJC_$_PROP_LIST__SFPBLatLng.7153
+ __OBJC_$_PROP_LIST__SFPBLaunchAppCommand.7168
+ __OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.7207
+ __OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.7237
+ __OBJC_$_PROP_LIST__SFPBListenToCardSection.7268
+ __OBJC_$_PROP_LIST__SFPBLocalImage.7282
+ __OBJC_$_PROP_LIST__SFPBLocationTypeInfo.7297
+ __OBJC_$_PROP_LIST__SFPBMailRankingSignals.7831
+ __OBJC_$_PROP_LIST__SFPBMailResultDetails.7861
+ __OBJC_$_PROP_LIST__SFPBManageReservationCommand.7867
+ __OBJC_$_PROP_LIST__SFPBMapCardSection.7943
+ __OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.7958
+ __OBJC_$_PROP_LIST__SFPBMapRegion.8004
+ __OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.8019
+ __OBJC_$_PROP_LIST__SFPBMediaArtworkImage.8034
+ __OBJC_$_PROP_LIST__SFPBMediaDetail.8049
+ __OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.8163
+ __OBJC_$_PROP_LIST__SFPBMediaItem.8243
+ __OBJC_$_PROP_LIST__SFPBMediaMetadata.8323
+ __OBJC_$_PROP_LIST__SFPBMediaOffer.8362
+ __OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.8382
+ __OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.8413
+ __OBJC_$_PROP_LIST__SFPBMessageAttachment.8428
+ __OBJC_$_PROP_LIST__SFPBMessageCardSection.8480
+ __OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.8519
+ __OBJC_$_PROP_LIST__SFPBMiniCardSection.8526
+ __OBJC_$_PROP_LIST__SFPBMonogramImage.8549
+ __OBJC_$_PROP_LIST__SFPBMoreResults.8556
+ __OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.8579
+ __OBJC_$_PROP_LIST__SFPBNewsCardSection.8610
+ __OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.8629
+ __OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.8644
+ __OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.8675
+ __OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.8690
+ __OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.8705
+ __OBJC_$_PROP_LIST__SFPBOpenMediaCommand.8720
+ __OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.8727
+ __OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.8734
+ __OBJC_$_PROP_LIST__SFPBPatternModel.8773
+ __OBJC_$_PROP_LIST__SFPBPegasusDisplayFields
+ __OBJC_$_PROP_LIST__SFPBPegasusDisplayFields.8804
+ __OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.8834
+ __OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.8841
+ __OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.8912
+ __OBJC_$_PROP_LIST__SFPBPerformIntentCommand.8935
+ __OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.8942
+ __OBJC_$_PROP_LIST__SFPBPerson.8997
+ __OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.9004
+ __OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.9034
+ __OBJC_$_PROP_LIST__SFPBPhotosAlbumImage.9049
+ __OBJC_$_PROP_LIST__SFPBPhotosAttributes.9103
+ __OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.9139
+ __OBJC_$_PROP_LIST__SFPBPhotosMemoryImage.9154
+ __OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.9232
+ __OBJC_$_PROP_LIST__SFPBPin.9247
+ __OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.9280
+ __OBJC_$_PROP_LIST__SFPBPlayMediaCommand.9303
+ __OBJC_$_PROP_LIST__SFPBPlayVideoCommand.9310
+ __OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.9330
+ __OBJC_$_PROP_LIST__SFPBPointSize.9353
+ __OBJC_$_PROP_LIST__SFPBProduct.9384
+ __OBJC_$_PROP_LIST__SFPBProductAvailability.9406
+ __OBJC_$_PROP_LIST__SFPBProductCardSection.9421
+ __OBJC_$_PROP_LIST__SFPBProductInventory.9477
+ __OBJC_$_PROP_LIST__SFPBProductInventoryResult.9500
+ __OBJC_$_PROP_LIST__SFPBPunchout.9565
+ __OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.9723
+ __OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.9731
+ __OBJC_$_PROP_LIST__SFPBRFAppIconImage.9751
+ __OBJC_$_PROP_LIST__SFPBRFAspectRatio.9759
+ __OBJC_$_PROP_LIST__SFPBRFAttribution.9811
+ __OBJC_$_PROP_LIST__SFPBRFAvatarImage.9830
+ __OBJC_$_PROP_LIST__SFPBRFBadgedImage.9844
+ __OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9867
+ __OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9875
+ __OBJC_$_PROP_LIST__SFPBRFColor.9909
+ __OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.9915
+ __OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.9931
+ __OBJC_$_PROP_LIST__SFPBRFEngageable.9960
+ __OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.9995
+ __OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.10018
+ __OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.10103
+ __OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.10122
+ __OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.10129
+ __OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.10162
+ __OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.10169
+ __OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.10176
+ __OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.10183
+ __OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.10199
+ __OBJC_$_PROP_LIST__SFPBRFFont.10227
+ __OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.11346
+ __OBJC_$_PROP_LIST__SFPBRFFormattedText.10381
+ __OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.10396
+ __OBJC_$_PROP_LIST__SFPBRFImageElement.10416
+ __OBJC_$_PROP_LIST__SFPBRFImageSource.10515
+ __OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.10546
+ __OBJC_$_PROP_LIST__SFPBRFMapAnnotation.10576
+ __OBJC_$_PROP_LIST__SFPBRFMapCardSection.10643
+ __OBJC_$_PROP_LIST__SFPBRFMapMarker.10676
+ __OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.10707
+ __OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.10722
+ __OBJC_$_PROP_LIST__SFPBRFMapMarkerText.10730
+ __OBJC_$_PROP_LIST__SFPBRFMapPoint.10752
+ __OBJC_$_PROP_LIST__SFPBRFMonogramImage.10767
+ __OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.10782
+ __OBJC_$_PROP_LIST__SFPBRFOptionalBool.10789
+ __OBJC_$_PROP_LIST__SFPBRFOptionalFloat.10796
+ __OBJC_$_PROP_LIST__SFPBRFPreview.10803
+ __OBJC_$_PROP_LIST__SFPBRFPreviewList.10825
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.10840
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.10847
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.10855
+ __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.10862
+ __OBJC_$_PROP_LIST__SFPBRFRGBValue.10892
+ __OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.10904
+ __OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.10911
+ __OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.10918
+ __OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.10925
+ __OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.10932
+ __OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.10939
+ __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.10946
+ __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.10953
+ __OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.10968
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.10983
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.10990
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.11021
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.11028
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.11035
+ __OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.11059
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.11075
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemAttribution.11099
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.11106
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.11113
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableCardSection.11152
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableContent.11167
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.11187
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.11194
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.11233
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.11240
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.11247
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.11262
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.11277
+ __OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.11284
+ __OBJC_$_PROP_LIST__SFPBRFSymbolImage.11339
+ __OBJC_$_PROP_LIST__SFPBRFTableCell.11373
+ __OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.11403
+ __OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.11449
+ __OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.11514
+ __OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.11529
+ __OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.11535
+ __OBJC_$_PROP_LIST__SFPBRFTextElement.11579
+ __OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.11585
+ __OBJC_$_PROP_LIST__SFPBRFTextProperty.11615
+ __OBJC_$_PROP_LIST__SFPBRFUrlImage.11679
+ __OBJC_$_PROP_LIST__SFPBRFVisualElement.11698
+ __OBJC_$_PROP_LIST__SFPBRFVisualProperty.11720
+ __OBJC_$_PROP_LIST__SFPBRFVisualPropertyWithAction.11735
+ __OBJC_$_PROP_LIST__SFPBReferentialCommand.11742
+ __OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.11762
+ __OBJC_$_PROP_LIST__SFPBReminder.11777
+ __OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.11784
+ __OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.11815
+ __OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.11822
+ __OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.11876
+ __OBJC_$_PROP_LIST__SFPBResultEntity.11904
+ __OBJC_$_PROP_LIST__SFPBRichText.11944
+ __OBJC_$_PROP_LIST__SFPBRichTitleCardSection.12092
+ __OBJC_$_PROP_LIST__SFPBRowCardSection.12187
+ __OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.12202
+ __OBJC_$_PROP_LIST__SFPBSafariAttributes.12216
+ __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.12262
+ __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.12278
+ __OBJC_$_PROP_LIST__SFPBScene.12300
+ __OBJC_$_PROP_LIST__SFPBScoreboardCardSection.12344
+ __OBJC_$_PROP_LIST__SFPBSearchInAppCommand.12359
+ __OBJC_$_PROP_LIST__SFPBSearchSuggestion.12437
+ __OBJC_$_PROP_LIST__SFPBSearchWebCommand.12444
+ __OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.12452
+ __OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.12482
+ __OBJC_$_PROP_LIST__SFPBShareCommand.12515
+ __OBJC_$_PROP_LIST__SFPBShareItem.12548
+ __OBJC_$_PROP_LIST__SFPBShortcutsImage.12563
+ __OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.12578
+ __OBJC_$_PROP_LIST__SFPBShowContactCardCommand.12593
+ __OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.12644
+ __OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.12659
+ __OBJC_$_PROP_LIST__SFPBShowSFCardCommand.12674
+ __OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.12681
+ __OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.12688
+ __OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.12752
+ __OBJC_$_PROP_LIST__SFPBSplitCardSection.12819
+ __OBJC_$_PROP_LIST__SFPBSportsDetail.12834
+ __OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.12862
+ __OBJC_$_PROP_LIST__SFPBSportsItem.12869
+ __OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.12900
+ __OBJC_$_PROP_LIST__SFPBSportsTeam.12932
+ __OBJC_$_PROP_LIST__SFPBSpotlightEmbeddingState.12962
+ __OBJC_$_PROP_LIST__SFPBStockChartCardSection.12985
+ __OBJC_$_PROP_LIST__SFPBStoreButtonItem.13008
+ __OBJC_$_PROP_LIST__SFPBStringDictionary.13027
+ __OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.13078
+ __OBJC_$_PROP_LIST__SFPBStructuredLocation.13101
+ __OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.13134
+ __OBJC_$_PROP_LIST__SFPBSuggestionCardSection.13173
+ __OBJC_$_PROP_LIST__SFPBSymbolImage.13215
+ __OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.13239
+ __OBJC_$_PROP_LIST__SFPBTableColumnAlignment.13269
+ __OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.13337
+ __OBJC_$_PROP_LIST__SFPBTableRowCardSection.13357
+ __OBJC_$_PROP_LIST__SFPBText.13374
+ __OBJC_$_PROP_LIST__SFPBTextColumn.13396
+ __OBJC_$_PROP_LIST__SFPBTextColumnSection.13431
+ __OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.13442
+ __OBJC_$_PROP_LIST__SFPBTextCopyItem.13457
+ __OBJC_$_PROP_LIST__SFPBTimeZone.13464
+ __OBJC_$_PROP_LIST__SFPBTitleCardSection.13471
+ __OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.13478
+ __OBJC_$_PROP_LIST__SFPBToggleAudioCommand.13501
+ __OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.13525
+ __OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.13540
+ __OBJC_$_PROP_LIST__SFPBTopic.13583
+ __OBJC_$_PROP_LIST__SFPBTrack.13615
+ __OBJC_$_PROP_LIST__SFPBTrackListCardSection.13637
+ __OBJC_$_PROP_LIST__SFPBURL.13644
+ __OBJC_$_PROP_LIST__SFPBURLCopyItem.13651
+ __OBJC_$_PROP_LIST__SFPBURLImage.13666
+ __OBJC_$_PROP_LIST__SFPBURLShareItem.13673
+ __OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.13688
+ __OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.13703
+ __OBJC_$_PROP_LIST__SFPBUserActivityData.13734
+ __OBJC_$_PROP_LIST__SFPBUserActivityInfo.13757
+ __OBJC_$_PROP_LIST__SFPBUserReportRequest.13832
+ __OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.13863
+ __OBJC_$_PROP_LIST__SFPBViewEmailCommand.13869
+ __OBJC_$_PROP_LIST__SFPBWatchListButtonItem.13876
+ __OBJC_$_PROP_LIST__SFPBWatchListCardSection.13883
+ __OBJC_$_PROP_LIST__SFPBWatchListItem.13962
+ __OBJC_$_PROP_LIST__SFPBWatchNowCardSection.13976
+ __OBJC_$_PROP_LIST__SFPBWeatherColor.14023
+ __OBJC_$_PROP_LIST__SFPBWeatherDetails.14030
+ __OBJC_$_PROP_LIST__SFPBWebCardSection.14045
+ __OBJC_$_PROP_LIST__SFPBWorldMapCardSection.14068
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFFlightDateDescriptor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFPegasusDisplayFields
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBFlightDateDescriptor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFPBPegasusDisplayFields
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFFlightDateDescriptor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFPegasusDisplayFields
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBFlightDateDescriptor
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFPBPegasusDisplayFields
+ __OBJC_$_PROTOCOL_REFS_SFFlightDateDescriptor
+ __OBJC_$_PROTOCOL_REFS_SFPegasusDisplayFields
+ __OBJC_$_PROTOCOL_REFS__SFPBFlightDateDescriptor
+ __OBJC_$_PROTOCOL_REFS__SFPBPegasusDisplayFields
+ __OBJC_CLASS_PROTOCOLS_$_SFFlightDateDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_SFPegasusDisplayFields
+ __OBJC_CLASS_PROTOCOLS_$__SFPBFlightDateDescriptor
+ __OBJC_CLASS_PROTOCOLS_$__SFPBPegasusDisplayFields
+ __OBJC_CLASS_RO_$_SFFlightDateDescriptor
+ __OBJC_CLASS_RO_$_SFPegasusDisplayFields
+ __OBJC_CLASS_RO_$__SFPBFlightDateDescriptor
+ __OBJC_CLASS_RO_$__SFPBPegasusDisplayFields
+ __OBJC_LABEL_PROTOCOL_$_SFFlightDateDescriptor
+ __OBJC_LABEL_PROTOCOL_$_SFPegasusDisplayFields
+ __OBJC_LABEL_PROTOCOL_$__SFPBFlightDateDescriptor
+ __OBJC_LABEL_PROTOCOL_$__SFPBPegasusDisplayFields
+ __OBJC_METACLASS_RO_$_SFFlightDateDescriptor
+ __OBJC_METACLASS_RO_$_SFPegasusDisplayFields
+ __OBJC_METACLASS_RO_$__SFPBFlightDateDescriptor
+ __OBJC_METACLASS_RO_$__SFPBPegasusDisplayFields
+ __OBJC_PROTOCOL_$_SFFlightDateDescriptor
+ __OBJC_PROTOCOL_$_SFPegasusDisplayFields
+ __OBJC_PROTOCOL_$__SFPBFlightDateDescriptor
+ __OBJC_PROTOCOL_$__SFPBPegasusDisplayFields
+ __SFPBFlightDateDescriptorReadFrom
+ __SFPBPegasusDisplayFieldsReadFrom
+ ___PARLogHandleForCategory_block_invoke.34897
+ ___PARLogHandleForCategory_block_invoke.70608
+ ___block_literal_global.34892
+ ___block_literal_global.35673
+ ___block_literal_global.37402
+ ___block_literal_global.70621
+ ___getDispatchQueue_block_invoke.70625
+ _getDispatchQueue.70619
+ _getDispatchQueue.onceToken.70620
+ _getDispatchQueue.queue.70622
+ _objc_msgSend$analyzedAndIndexedAssetsPercentage
+ _objc_msgSend$analyzedAssetsPercentage
+ _objc_msgSend$arrivalTime
+ _objc_msgSend$assetsRetrieved
+ _objc_msgSend$bufferMinutes
+ _objc_msgSend$collectionsRetrieved
+ _objc_msgSend$current
+ _objc_msgSend$departureTime
+ _objc_msgSend$displayStatus
+ _objc_msgSend$embeddedAssetsPercentage
+ _objc_msgSend$gateArrivalTimes
+ _objc_msgSend$gateDepartureTimes
+ _objc_msgSend$hasAssetsRetrieved
+ _objc_msgSend$hasCollectionsRetrieved
+ _objc_msgSend$hasHasMetadataResults
+ _objc_msgSend$hasIs_fresh
+ _objc_msgSend$hasMetadataResults
+ _objc_msgSend$hasPegasusDefinedState
+ _objc_msgSend$indexedAssetsPercentage
+ _objc_msgSend$is_fresh
+ _objc_msgSend$pegasusDefinedState
+ _objc_msgSend$pegasusDisplayFields
+ _objc_msgSend$runwayArrivalTimes
+ _objc_msgSend$runwayDepartureTimes
+ _objc_msgSend$scheduled
+ _objc_msgSend$setAnalyzedAndIndexedAssetsPercentage:
+ _objc_msgSend$setAnalyzedAssetsPercentage:
+ _objc_msgSend$setArrivalTime:
+ _objc_msgSend$setAssetsRetrieved:
+ _objc_msgSend$setBufferMinutes:
+ _objc_msgSend$setCollectionsRetrieved:
+ _objc_msgSend$setCurrent:
+ _objc_msgSend$setDepartureTime:
+ _objc_msgSend$setDisplayStatus:
+ _objc_msgSend$setEmbeddedAssetsPercentage:
+ _objc_msgSend$setGateArrivalTimes:
+ _objc_msgSend$setGateDepartureTimes:
+ _objc_msgSend$setHasMetadataResults:
+ _objc_msgSend$setIndexedAssetsPercentage:
+ _objc_msgSend$setIs_fresh:
+ _objc_msgSend$setPegasusDefinedState:
+ _objc_msgSend$setPegasusDisplayFields:
+ _objc_msgSend$setRunwayArrivalTimes:
+ _objc_msgSend$setRunwayDepartureTimes:
+ _objc_msgSend$setScheduled:
+ _objc_sync_enter
+ _objc_sync_exit
- GCC_except_table2754
- GCC_except_table7900
- _PARLogHandleForCategory.logHandles.0.34905
- _PARLogHandleForCategory.logHandles.0.70263
- _PARLogHandleForCategory.logHandles.1.34899
- _PARLogHandleForCategory.logHandles.1.70260
- _PARLogHandleForCategory.logHandles.2.34907
- _PARLogHandleForCategory.logHandles.2.70265
- _PARLogHandleForCategory.logHandles.3.34908
- _PARLogHandleForCategory.logHandles.3.70266
- _PARLogHandleForCategory.logHandles.4.34909
- _PARLogHandleForCategory.logHandles.4.70268
- _PARLogHandleForCategory.logHandles.5.34910
- _PARLogHandleForCategory.logHandles.5.70269
- _PARLogHandleForCategory.onceToken.34897
- _PARLogHandleForCategory.onceToken.70259
- __OBJC_$_PROP_LIST_RFLongItemStandardCardSection.247
- __OBJC_$_PROP_LIST_SFEmbeddingState.128
- __OBJC_$_PROP_LIST_SFFlightLeg.181
- __OBJC_$_PROP_LIST_SFPhotosRankingInfo.101
- __OBJC_$_PROP_LIST__SFPBEmbeddingState.5699
- __OBJC_$_PROP_LIST__SFPBEngagementSignal.5761
- __OBJC_$_PROP_LIST__SFPBEntitySearchMetadata.5785
- __OBJC_$_PROP_LIST__SFPBExecuteMenuItemCommand.5800
- __OBJC_$_PROP_LIST__SFPBExecuteToolCommand.5823
- __OBJC_$_PROP_LIST__SFPBExpandInlineCommand.5837
- __OBJC_$_PROP_LIST__SFPBFillToolAppEntityParameterCommand.5860
- __OBJC_$_PROP_LIST__SFPBFillToolAppParameterCommand.5875
- __OBJC_$_PROP_LIST__SFPBFillToolFileParameterCommand.5890
- __OBJC_$_PROP_LIST__SFPBFillToolParameterCommand.5897
- __OBJC_$_PROP_LIST__SFPBFillToolPersonParameterCommand.5904
- __OBJC_$_PROP_LIST__SFPBFindMyCardSection.5911
- __OBJC_$_PROP_LIST__SFPBFlight.5997
- __OBJC_$_PROP_LIST__SFPBFlightCardSection.6023
- __OBJC_$_PROP_LIST__SFPBFlightCheckinCommand.6029
- __OBJC_$_PROP_LIST__SFPBFlightDetails.6043
- __OBJC_$_PROP_LIST__SFPBFlightLeg.6191
- __OBJC_$_PROP_LIST__SFPBFormattedText.6239
- __OBJC_$_PROP_LIST__SFPBGradientColor.6267
- __OBJC_$_PROP_LIST__SFPBGraphicalFloat.6281
- __OBJC_$_PROP_LIST__SFPBGridCardSection.6288
- __OBJC_$_PROP_LIST__SFPBHashBucketDetail.6318
- __OBJC_$_PROP_LIST__SFPBHashBucketDetail_HashDetail.6369
- __OBJC_$_PROP_LIST__SFPBHeroCardSection.6376
- __OBJC_$_PROP_LIST__SFPBHeroTitleCardSection.6391
- __OBJC_$_PROP_LIST__SFPBHorizontalButtonCardSection.6410
- __OBJC_$_PROP_LIST__SFPBHorizontalScrollCardSection.6417
- __OBJC_$_PROP_LIST__SFPBImage.6721
- __OBJC_$_PROP_LIST__SFPBImageCopyItem.6728
- __OBJC_$_PROP_LIST__SFPBImageDerivedColor.6735
- __OBJC_$_PROP_LIST__SFPBImageOption.6763
- __OBJC_$_PROP_LIST__SFPBImagesCardSection.6791
- __OBJC_$_PROP_LIST__SFPBIndexState.6853
- __OBJC_$_PROP_LIST__SFPBIndexedUserActivityCommand.6868
- __OBJC_$_PROP_LIST__SFPBInfoCardSection.6898
- __OBJC_$_PROP_LIST__SFPBInfoTuple.6942
- __OBJC_$_PROP_LIST__SFPBInvokeSiriCommand.6965
- __OBJC_$_PROP_LIST__SFPBKeyValueDataCardSection.6996
- __OBJC_$_PROP_LIST__SFPBKeyValueTuple.7004
- __OBJC_$_PROP_LIST__SFPBLargeTitleDetailedRowCardSection.7034
- __OBJC_$_PROP_LIST__SFPBLatLng.7056
- __OBJC_$_PROP_LIST__SFPBLaunchAppCommand.7071
- __OBJC_$_PROP_LIST__SFPBLeadingTrailingCardSection.7110
- __OBJC_$_PROP_LIST__SFPBLinkPresentationCardSection.7140
- __OBJC_$_PROP_LIST__SFPBListenToCardSection.7171
- __OBJC_$_PROP_LIST__SFPBLocalImage.7185
- __OBJC_$_PROP_LIST__SFPBLocationTypeInfo.7200
- __OBJC_$_PROP_LIST__SFPBMailRankingSignals.7734
- __OBJC_$_PROP_LIST__SFPBMailResultDetails.7764
- __OBJC_$_PROP_LIST__SFPBManageReservationCommand.7770
- __OBJC_$_PROP_LIST__SFPBMapCardSection.7846
- __OBJC_$_PROP_LIST__SFPBMapPlaceCardSection.7861
- __OBJC_$_PROP_LIST__SFPBMapRegion.7907
- __OBJC_$_PROP_LIST__SFPBMapsDetailedRowCardSection.7922
- __OBJC_$_PROP_LIST__SFPBMediaArtworkImage.7937
- __OBJC_$_PROP_LIST__SFPBMediaDetail.7952
- __OBJC_$_PROP_LIST__SFPBMediaInfoCardSection.8066
- __OBJC_$_PROP_LIST__SFPBMediaItem.8146
- __OBJC_$_PROP_LIST__SFPBMediaMetadata.8226
- __OBJC_$_PROP_LIST__SFPBMediaOffer.8265
- __OBJC_$_PROP_LIST__SFPBMediaPlayerCardSection.8285
- __OBJC_$_PROP_LIST__SFPBMediaRemoteControlCardSection.8316
- __OBJC_$_PROP_LIST__SFPBMessageAttachment.8331
- __OBJC_$_PROP_LIST__SFPBMessageCardSection.8383
- __OBJC_$_PROP_LIST__SFPBMetaInfoCardSection.8422
- __OBJC_$_PROP_LIST__SFPBMiniCardSection.8429
- __OBJC_$_PROP_LIST__SFPBMonogramImage.8452
- __OBJC_$_PROP_LIST__SFPBMoreResults.8459
- __OBJC_$_PROP_LIST__SFPBNamedProtobufMessage.8482
- __OBJC_$_PROP_LIST__SFPBNewsCardSection.8513
- __OBJC_$_PROP_LIST__SFPBNowPlayingCardSection.8532
- __OBJC_$_PROP_LIST__SFPBOpenAppClipCommand.8547
- __OBJC_$_PROP_LIST__SFPBOpenCalculationCommand.8578
- __OBJC_$_PROP_LIST__SFPBOpenCoreSpotlightItemCommand.8593
- __OBJC_$_PROP_LIST__SFPBOpenFileProviderItemCommand.8608
- __OBJC_$_PROP_LIST__SFPBOpenMediaCommand.8623
- __OBJC_$_PROP_LIST__SFPBOpenPunchoutCommand.8630
- __OBJC_$_PROP_LIST__SFPBOpenWebClipCommand.8637
- __OBJC_$_PROP_LIST__SFPBPatternModel.8676
- __OBJC_$_PROP_LIST__SFPBPerformContactActionCommand.8706
- __OBJC_$_PROP_LIST__SFPBPerformContactQueryCommand.8713
- __OBJC_$_PROP_LIST__SFPBPerformEntityQueryCommand.8784
- __OBJC_$_PROP_LIST__SFPBPerformIntentCommand.8807
- __OBJC_$_PROP_LIST__SFPBPerformPersonEntityQueryCommand.8814
- __OBJC_$_PROP_LIST__SFPBPerson.8869
- __OBJC_$_PROP_LIST__SFPBPersonHeaderCardSection.8876
- __OBJC_$_PROP_LIST__SFPBPhotosAggregatedInfo.8906
- __OBJC_$_PROP_LIST__SFPBPhotosAlbumImage.8921
- __OBJC_$_PROP_LIST__SFPBPhotosAttributes.8975
- __OBJC_$_PROP_LIST__SFPBPhotosLibraryImage.9011
- __OBJC_$_PROP_LIST__SFPBPhotosMemoryImage.9026
- __OBJC_$_PROP_LIST__SFPBPhotosRankingInfo.9056
- __OBJC_$_PROP_LIST__SFPBPin.9071
- __OBJC_$_PROP_LIST__SFPBPlayAudioButtonItem.9104
- __OBJC_$_PROP_LIST__SFPBPlayMediaCommand.9127
- __OBJC_$_PROP_LIST__SFPBPlayVideoCommand.9134
- __OBJC_$_PROP_LIST__SFPBPlayWatchListItemButtonItem.9154
- __OBJC_$_PROP_LIST__SFPBPointSize.9177
- __OBJC_$_PROP_LIST__SFPBProduct.9208
- __OBJC_$_PROP_LIST__SFPBProductAvailability.9230
- __OBJC_$_PROP_LIST__SFPBProductCardSection.9245
- __OBJC_$_PROP_LIST__SFPBProductInventory.9301
- __OBJC_$_PROP_LIST__SFPBProductInventoryResult.9324
- __OBJC_$_PROP_LIST__SFPBPunchout.9389
- __OBJC_$_PROP_LIST__SFPBQueryUnderstandingParse.9547
- __OBJC_$_PROP_LIST__SFPBQuickLookThumbnailImage.9555
- __OBJC_$_PROP_LIST__SFPBRFAppIconImage.9575
- __OBJC_$_PROP_LIST__SFPBRFAspectRatio.9583
- __OBJC_$_PROP_LIST__SFPBRFAttribution.9635
- __OBJC_$_PROP_LIST__SFPBRFAvatarImage.9654
- __OBJC_$_PROP_LIST__SFPBRFBadgedImage.9668
- __OBJC_$_PROP_LIST__SFPBRFBinaryButtonCardSection.9691
- __OBJC_$_PROP_LIST__SFPBRFButtonCardSection.9699
- __OBJC_$_PROP_LIST__SFPBRFColor.9733
- __OBJC_$_PROP_LIST__SFPBRFDefaultBrowserAppIconImage.9739
- __OBJC_$_PROP_LIST__SFPBRFDisambiguationTitleCardSection.9755
- __OBJC_$_PROP_LIST__SFPBRFEngageable.9784
- __OBJC_$_PROP_LIST__SFPBRFExpandableStandardCardSection.9819
- __OBJC_$_PROP_LIST__SFPBRFExpandingComponentContent.9842
- __OBJC_$_PROP_LIST__SFPBRFFactItemButtonCardSection.9927
- __OBJC_$_PROP_LIST__SFPBRFFactItemDetailedNumberCardSection.9946
- __OBJC_$_PROP_LIST__SFPBRFFactItemHeroButtonCardSection.9953
- __OBJC_$_PROP_LIST__SFPBRFFactItemHeroNumberCardSection.9986
- __OBJC_$_PROP_LIST__SFPBRFFactItemImageRightCardSection.9993
- __OBJC_$_PROP_LIST__SFPBRFFactItemShortHeroNumberCardSection.10000
- __OBJC_$_PROP_LIST__SFPBRFFactItemShortNumberCardSection.10007
- __OBJC_$_PROP_LIST__SFPBRFFactItemStandardCardSection.10023
- __OBJC_$_PROP_LIST__SFPBRFFont.10051
- __OBJC_$_PROP_LIST__SFPBRFFont_RFSystemFont.11162
- __OBJC_$_PROP_LIST__SFPBRFFormattedText.10205
- __OBJC_$_PROP_LIST__SFPBRFHighlightedSubstring.10220
- __OBJC_$_PROP_LIST__SFPBRFImageElement.10240
- __OBJC_$_PROP_LIST__SFPBRFImageSource.10339
- __OBJC_$_PROP_LIST__SFPBRFLongItemStandardCardSection.10362
- __OBJC_$_PROP_LIST__SFPBRFMapAnnotation.10392
- __OBJC_$_PROP_LIST__SFPBRFMapCardSection.10459
- __OBJC_$_PROP_LIST__SFPBRFMapMarker.10492
- __OBJC_$_PROP_LIST__SFPBRFMapMarkerIdentifier.10523
- __OBJC_$_PROP_LIST__SFPBRFMapMarkerImage.10538
- __OBJC_$_PROP_LIST__SFPBRFMapMarkerText.10546
- __OBJC_$_PROP_LIST__SFPBRFMapPoint.10568
- __OBJC_$_PROP_LIST__SFPBRFMonogramImage.10583
- __OBJC_$_PROP_LIST__SFPBRFMultiButtonCardSection.10598
- __OBJC_$_PROP_LIST__SFPBRFOptionalBool.10605
- __OBJC_$_PROP_LIST__SFPBRFOptionalFloat.10612
- __OBJC_$_PROP_LIST__SFPBRFPreview.10619
- __OBJC_$_PROP_LIST__SFPBRFPreviewList.10641
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderMarqueeCardSection.10656
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderRichCardSection.10663
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStackedImageCardSection.10671
- __OBJC_$_PROP_LIST__SFPBRFPrimaryHeaderStandardCardSection.10678
- __OBJC_$_PROP_LIST__SFPBRFRGBValue.10708
- __OBJC_$_PROP_LIST__SFPBRFReferenceCenteredCardSection.10720
- __OBJC_$_PROP_LIST__SFPBRFReferenceFootnoteCardSection.10727
- __OBJC_$_PROP_LIST__SFPBRFReferenceItemButtonCardSection.10734
- __OBJC_$_PROP_LIST__SFPBRFReferenceItemLogoCardSection.10741
- __OBJC_$_PROP_LIST__SFPBRFReferenceRichCardSection.10748
- __OBJC_$_PROP_LIST__SFPBRFReferenceStandardCardSection.10755
- __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderEmphasizedCardSection.10762
- __OBJC_$_PROP_LIST__SFPBRFSecondaryHeaderStandardCardSection.10769
- __OBJC_$_PROP_LIST__SFPBRFShowMoreOnTap.10784
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemPlayerCardSection.10799
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemReverseRichCardSection.10806
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichCardSection.10837
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemRichSearchResultCardSection.10844
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemStandardCardSection.10851
- __OBJC_$_PROP_LIST__SFPBRFSimpleItemVisualElementCardSection.10875
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemAlignedTextCardSection.10891
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemAttribution.10915
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemButtonCardSection.10922
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemDetailedTextCardSection.10929
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableCardSection.10968
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemExpandableContent.10983
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemImageRightCardSection.11003
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairCardSection.11010
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPairNumberCardSection.11049
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemPlayerCardSection.11056
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemShortNumberCardSection.11063
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemStandardCardSection.11078
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemSwitchV2CardSection.11093
- __OBJC_$_PROP_LIST__SFPBRFSummaryItemTextCardSection.11100
- __OBJC_$_PROP_LIST__SFPBRFSymbolImage.11155
- __OBJC_$_PROP_LIST__SFPBRFTableCell.11189
- __OBJC_$_PROP_LIST__SFPBRFTableColumnDefinition.11219
- __OBJC_$_PROP_LIST__SFPBRFTableContentColumnDefinition.11265
- __OBJC_$_PROP_LIST__SFPBRFTableHeaderCardSection.11330
- __OBJC_$_PROP_LIST__SFPBRFTableRowCardSection.11345
- __OBJC_$_PROP_LIST__SFPBRFTableSpacerColumnDefinition.11351
- __OBJC_$_PROP_LIST__SFPBRFTextElement.11395
- __OBJC_$_PROP_LIST__SFPBRFTextEncapsulation.11401
- __OBJC_$_PROP_LIST__SFPBRFTextProperty.11431
- __OBJC_$_PROP_LIST__SFPBRFUrlImage.11495
- __OBJC_$_PROP_LIST__SFPBRFVisualElement.11514
- __OBJC_$_PROP_LIST__SFPBRFVisualProperty.11536
- __OBJC_$_PROP_LIST__SFPBRFVisualPropertyWithAction.11551
- __OBJC_$_PROP_LIST__SFPBReferentialCommand.11558
- __OBJC_$_PROP_LIST__SFPBRejectPeopleInPhotoCommand.11578
- __OBJC_$_PROP_LIST__SFPBReminder.11593
- __OBJC_$_PROP_LIST__SFPBRequestAppClipInstallCommand.11600
- __OBJC_$_PROP_LIST__SFPBRequestProductPageCommand.11631
- __OBJC_$_PROP_LIST__SFPBRequestUserReportCommand.11638
- __OBJC_$_PROP_LIST__SFPBResponseWrapperCardSection.11692
- __OBJC_$_PROP_LIST__SFPBResultEntity.11720
- __OBJC_$_PROP_LIST__SFPBRichText.11760
- __OBJC_$_PROP_LIST__SFPBRichTitleCardSection.11908
- __OBJC_$_PROP_LIST__SFPBRowCardSection.12003
- __OBJC_$_PROP_LIST__SFPBRunVoiceShortcutCommand.12018
- __OBJC_$_PROP_LIST__SFPBSafariAttributes.12032
- __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsCardSection.12078
- __OBJC_$_PROP_LIST__SFPBSafariTableOfContentsItem.12094
- __OBJC_$_PROP_LIST__SFPBScene.12116
- __OBJC_$_PROP_LIST__SFPBScoreboardCardSection.12160
- __OBJC_$_PROP_LIST__SFPBSearchInAppCommand.12175
- __OBJC_$_PROP_LIST__SFPBSearchSuggestion.12253
- __OBJC_$_PROP_LIST__SFPBSearchWebCommand.12260
- __OBJC_$_PROP_LIST__SFPBSectionHeaderCardSection.12268
- __OBJC_$_PROP_LIST__SFPBSelectableGridCardSection.12298
- __OBJC_$_PROP_LIST__SFPBShareCommand.12331
- __OBJC_$_PROP_LIST__SFPBShareItem.12364
- __OBJC_$_PROP_LIST__SFPBShortcutsImage.12379
- __OBJC_$_PROP_LIST__SFPBShowAppStoreSheetCommand.12394
- __OBJC_$_PROP_LIST__SFPBShowContactCardCommand.12409
- __OBJC_$_PROP_LIST__SFPBShowPhotosOneUpViewCommand.12460
- __OBJC_$_PROP_LIST__SFPBShowPurchaseRequestSheetCommand.12475
- __OBJC_$_PROP_LIST__SFPBShowSFCardCommand.12490
- __OBJC_$_PROP_LIST__SFPBShowScreenTimeRequestSheetCommand.12497
- __OBJC_$_PROP_LIST__SFPBShowWrapperResponseViewCommand.12504
- __OBJC_$_PROP_LIST__SFPBSocialMediaPostCardSection.12568
- __OBJC_$_PROP_LIST__SFPBSplitCardSection.12635
- __OBJC_$_PROP_LIST__SFPBSportsDetail.12650
- __OBJC_$_PROP_LIST__SFPBSportsFollowButtonItem.12678
- __OBJC_$_PROP_LIST__SFPBSportsItem.12685
- __OBJC_$_PROP_LIST__SFPBSportsSubscriptionRequestItem.12716
- __OBJC_$_PROP_LIST__SFPBSportsTeam.12748
- __OBJC_$_PROP_LIST__SFPBSpotlightEmbeddingState.12778
- __OBJC_$_PROP_LIST__SFPBStockChartCardSection.12801
- __OBJC_$_PROP_LIST__SFPBStoreButtonItem.12824
- __OBJC_$_PROP_LIST__SFPBStringDictionary.12843
- __OBJC_$_PROP_LIST__SFPBStrokeAnimationCardSection.12894
- __OBJC_$_PROP_LIST__SFPBStructuredLocation.12917
- __OBJC_$_PROP_LIST__SFPBSubscribeForUpdatesCommand.12950
- __OBJC_$_PROP_LIST__SFPBSuggestionCardSection.12989
- __OBJC_$_PROP_LIST__SFPBSymbolImage.13031
- __OBJC_$_PROP_LIST__SFPBTableAlignmentSchema.13055
- __OBJC_$_PROP_LIST__SFPBTableColumnAlignment.13085
- __OBJC_$_PROP_LIST__SFPBTableHeaderRowCardSection.13153
- __OBJC_$_PROP_LIST__SFPBTableRowCardSection.13173
- __OBJC_$_PROP_LIST__SFPBText.13190
- __OBJC_$_PROP_LIST__SFPBTextColumn.13212
- __OBJC_$_PROP_LIST__SFPBTextColumnSection.13247
- __OBJC_$_PROP_LIST__SFPBTextColumnsCardSection.13258
- __OBJC_$_PROP_LIST__SFPBTextCopyItem.13273
- __OBJC_$_PROP_LIST__SFPBTimeZone.13280
- __OBJC_$_PROP_LIST__SFPBTitleCardSection.13287
- __OBJC_$_PROP_LIST__SFPBTitleSubtitleTuple.13294
- __OBJC_$_PROP_LIST__SFPBToggleAudioCommand.13317
- __OBJC_$_PROP_LIST__SFPBToggleButtonConfiguration.13341
- __OBJC_$_PROP_LIST__SFPBToggleWatchListStatusCommand.13356
- __OBJC_$_PROP_LIST__SFPBTopic.13399
- __OBJC_$_PROP_LIST__SFPBTrack.13431
- __OBJC_$_PROP_LIST__SFPBTrackListCardSection.13453
- __OBJC_$_PROP_LIST__SFPBURL.13460
- __OBJC_$_PROP_LIST__SFPBURLCopyItem.13467
- __OBJC_$_PROP_LIST__SFPBURLImage.13482
- __OBJC_$_PROP_LIST__SFPBURLShareItem.13489
- __OBJC_$_PROP_LIST__SFPBUpdateSearchQueryCommand.13504
- __OBJC_$_PROP_LIST__SFPBUpdateSportsFollowingStatusCommand.13519
- __OBJC_$_PROP_LIST__SFPBUserActivityData.13550
- __OBJC_$_PROP_LIST__SFPBUserActivityInfo.13573
- __OBJC_$_PROP_LIST__SFPBUserReportRequest.13648
- __OBJC_$_PROP_LIST__SFPBVerticalLayoutCardSection.13679
- __OBJC_$_PROP_LIST__SFPBViewEmailCommand.13685
- __OBJC_$_PROP_LIST__SFPBWatchListButtonItem.13692
- __OBJC_$_PROP_LIST__SFPBWatchListCardSection.13699
- __OBJC_$_PROP_LIST__SFPBWatchListItem.13778
- __OBJC_$_PROP_LIST__SFPBWatchNowCardSection.13792
- __OBJC_$_PROP_LIST__SFPBWeatherColor.13839
- __OBJC_$_PROP_LIST__SFPBWeatherDetails.13846
- __OBJC_$_PROP_LIST__SFPBWebCardSection.13861
- __OBJC_$_PROP_LIST__SFPBWorldMapCardSection.13884
- ___PARLogHandleForCategory_block_invoke.34903
- ___PARLogHandleForCategory_block_invoke.70262
- ___block_literal_global.34898
- ___block_literal_global.35679
- ___block_literal_global.37395
- ___block_literal_global.70275
- ___getDispatchQueue_block_invoke.70279
- _getDispatchQueue.70273
- _getDispatchQueue.onceToken.70274
- _getDispatchQueue.queue.70276
CStrings:
+ "@\"SFFlightDateDescriptor\""
+ "@\"SFFlightDateDescriptor\"16@0:8"
+ "@\"SFPegasusDisplayFields\""
+ "@\"SFPegasusDisplayFields\"16@0:8"
+ "@\"_SFPBFlightDateDescriptor\""
+ "@\"_SFPBFlightDateDescriptor\"16@0:8"
+ "@\"_SFPBPegasusDisplayFields\""
+ "@\"_SFPBPegasusDisplayFields\"16@0:8"
+ "D"
+ "SFFlightDateDescriptor"
+ "SFPegasusDisplayFields"
+ "T@\"NSDate\",C,N,V_arrivalTime"
+ "T@\"NSDate\",C,N,V_current"
+ "T@\"NSDate\",C,N,V_departureTime"
+ "T@\"NSDate\",C,N,V_scheduled"
+ "T@\"NSNumber\",C,N,V_analyzedAndIndexedAssetsPercentage"
+ "T@\"NSNumber\",C,N,V_analyzedAssetsPercentage"
+ "T@\"NSNumber\",C,N,V_bufferMinutes"
+ "T@\"NSNumber\",C,N,V_embeddedAssetsPercentage"
+ "T@\"NSNumber\",C,N,V_indexedAssetsPercentage"
+ "T@\"NSString\",C,N,V_displayStatus"
+ "T@\"SFFlightDateDescriptor\",&,N"
+ "T@\"SFFlightDateDescriptor\",&,N,V_gateArrivalTimes"
+ "T@\"SFFlightDateDescriptor\",&,N,V_gateDepartureTimes"
+ "T@\"SFFlightDateDescriptor\",&,N,V_runwayArrivalTimes"
+ "T@\"SFFlightDateDescriptor\",&,N,V_runwayDepartureTimes"
+ "T@\"SFPegasusDisplayFields\",&,N"
+ "T@\"SFPegasusDisplayFields\",&,N,V_pegasusDisplayFields"
+ "T@\"_SFPBDate\",&,N,V_arrivalTime"
+ "T@\"_SFPBDate\",&,N,V_current"
+ "T@\"_SFPBDate\",&,N,V_departureTime"
+ "T@\"_SFPBDate\",&,N,V_scheduled"
+ "T@\"_SFPBFlightDateDescriptor\",&,N"
+ "T@\"_SFPBFlightDateDescriptor\",&,N,V_gateArrivalTimes"
+ "T@\"_SFPBFlightDateDescriptor\",&,N,V_gateDepartureTimes"
+ "T@\"_SFPBFlightDateDescriptor\",&,N,V_runwayArrivalTimes"
+ "T@\"_SFPBFlightDateDescriptor\",&,N,V_runwayDepartureTimes"
+ "T@\"_SFPBPegasusDisplayFields\",&,N"
+ "T@\"_SFPBPegasusDisplayFields\",&,N,V_pegasusDisplayFields"
+ "TB,N,V_hasMetadataResults"
+ "TB,N,V_is_fresh"
+ "Tf,N,V_bufferMinutes"
+ "Ti,N,V_analyzedAndIndexedAssetsPercentage"
+ "Ti,N,V_analyzedAssetsPercentage"
+ "Ti,N,V_assetsRetrieved"
+ "Ti,N,V_collectionsRetrieved"
+ "Ti,N,V_embeddedAssetsPercentage"
+ "Ti,N,V_indexedAssetsPercentage"
+ "Ti,N,V_pegasusDefinedState"
+ "_SFPBFlightDateDescriptor"
+ "_SFPBPegasusDisplayFields"
+ "_analyzedAndIndexedAssetsPercentage"
+ "_analyzedAssetsPercentage"
+ "_arrivalTime"
+ "_assetsRetrieved"
+ "_bufferMinutes"
+ "_collectionsRetrieved"
+ "_current"
+ "_departureTime"
+ "_displayStatus"
+ "_embeddedAssetsPercentage"
+ "_gateArrivalTimes"
+ "_gateDepartureTimes"
+ "_hasMetadataResults"
+ "_indexedAssetsPercentage"
+ "_is_fresh"
+ "_pegasusDefinedState"
+ "_pegasusDisplayFields"
+ "_runwayArrivalTimes"
+ "_runwayDepartureTimes"
+ "_scheduled"
+ "analyzedAndIndexedAssetsPercentage"
+ "analyzedAssetsPercentage"
+ "arrivalTime"
+ "assetsRetrieved"
+ "bufferMinutes"
+ "collectionsRetrieved"
+ "current"
+ "departureTime"
+ "displayStatus"
+ "embeddedAssetsPercentage"
+ "gateArrivalTimes"
+ "gateDepartureTimes"
+ "hasAssetsRetrieved"
+ "hasCollectionsRetrieved"
+ "hasHasMetadataResults"
+ "hasIs_fresh"
+ "hasMetadataResults"
+ "hasPegasusDefinedState"
+ "indexedAssetsPercentage"
+ "isFresh"
+ "is_fresh"
+ "pegasusDefinedState"
+ "pegasusDisplayFields"
+ "runwayArrivalTimes"
+ "runwayDepartureTimes"
+ "scheduled"
+ "setAnalyzedAndIndexedAssetsPercentage:"
+ "setAnalyzedAssetsPercentage:"
+ "setArrivalTime:"
+ "setAssetsRetrieved:"
+ "setBufferMinutes:"
+ "setCollectionsRetrieved:"
+ "setCurrent:"
+ "setDepartureTime:"
+ "setDisplayStatus:"
+ "setEmbeddedAssetsPercentage:"
+ "setGateArrivalTimes:"
+ "setGateDepartureTimes:"
+ "setHasMetadataResults:"
+ "setIndexedAssetsPercentage:"
+ "setIs_fresh:"
+ "setPegasusDefinedState:"
+ "setPegasusDisplayFields:"
+ "setRunwayArrivalTimes:"
+ "setRunwayDepartureTimes:"
+ "setScheduled:"
+ "v24@0:8@\"SFFlightDateDescriptor\"16"
+ "v24@0:8@\"SFPegasusDisplayFields\"16"
+ "v24@0:8@\"_SFPBFlightDateDescriptor\"16"
+ "v24@0:8@\"_SFPBPegasusDisplayFields\"16"
+ "{?=\"is_quote\"b1\"has_background_platter\"b1\"is_fresh\"b1}"
+ "{?=\"queryStatus\"b1\"hasQueryEmbedding\"b1\"hasEmbeddingResults\"b1\"hasResults\"b1\"hasSuppressedResults\"b1\"hasKeywordResults\"b1\"hasHybridResults\"b1\"hasMetadataResults\"b1}"
+ "{?=\"status\"b1\"pegasusDefinedState\"b1}"
+ "{?=\"totalNumberOfAssetsIndexed\"b1\"totalNumberOfAssetsInLibrary\"b1\"totalNumberOfEmbeddingMatchedAssets\"b1\"totalNumberOfMetadataMatchedAssets\"b1\"assetEstimationOffAmount\"b1\"assetsRetrieved\"b1\"collectionsRetrieved\"b1}"
- "{?=\"is_quote\"b1\"has_background_platter\"b1}"
- "{?=\"queryStatus\"b1\"hasQueryEmbedding\"b1\"hasEmbeddingResults\"b1\"hasResults\"b1\"hasSuppressedResults\"b1\"hasKeywordResults\"b1\"hasHybridResults\"b1}"
- "{?=\"status\"b1}"
- "{?=\"totalNumberOfAssetsIndexed\"b1\"totalNumberOfAssetsInLibrary\"b1\"totalNumberOfEmbeddingMatchedAssets\"b1\"totalNumberOfMetadataMatchedAssets\"b1\"assetEstimationOffAmount\"b1}"

```
