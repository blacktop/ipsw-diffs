## MediaPlayer

> `/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/A/MediaPlayer`

```diff

-4024.400.1.0.0
-  __TEXT.__text: 0x1e3b50
-  __TEXT.__auth_stubs: 0x2f00
-  __TEXT.__objc_methlist: 0x1d018
-  __TEXT.__const: 0x39b0
-  __TEXT.__cstring: 0x26955
-  __TEXT.__gcc_except_tab: 0x8534
-  __TEXT.__oslogstring: 0xcc23
+4024.540.1.0.0
+  __TEXT.__text: 0x1f0f60
+  __TEXT.__auth_stubs: 0x2fb0
+  __TEXT.__objc_methlist: 0x20460
+  __TEXT.__const: 0x39d0
+  __TEXT.__cstring: 0x27135
+  __TEXT.__gcc_except_tab: 0x873c
+  __TEXT.__oslogstring: 0xd707
   __TEXT.__dlopen_cstrs: 0x25c
   __TEXT.__ustring: 0x1dc
   __TEXT.__constg_swiftt: 0x80

   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x8e28
+  __TEXT.__unwind_info: 0x90d8
   __TEXT.__eh_frame: 0xd0
-  __TEXT.__objc_classname: 0x48d2
-  __TEXT.__objc_methname: 0x4c2e1
-  __TEXT.__objc_methtype: 0xf873
-  __TEXT.__objc_stubs: 0x25360
-  __DATA_CONST.__got: 0x1bd0
-  __DATA_CONST.__const: 0xa220
-  __DATA_CONST.__objc_classlist: 0x1090
+  __TEXT.__objc_classname: 0x4993
+  __TEXT.__objc_methname: 0x4e19d
+  __TEXT.__objc_methtype: 0xfa81
+  __TEXT.__objc_stubs: 0x26240
+  __DATA_CONST.__got: 0x1c50
+  __DATA_CONST.__const: 0xa5b0
+  __DATA_CONST.__objc_classlist: 0x10c0
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe9c8
+  __DATA_CONST.__objc_selrefs: 0xf8c0
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0xb60
-  __DATA_CONST.__objc_arraydata: 0x778
-  __AUTH_CONST.__auth_got: 0x1798
+  __DATA_CONST.__objc_superrefs: 0xb90
+  __DATA_CONST.__objc_arraydata: 0x780
+  __AUTH_CONST.__auth_got: 0x17f0
   __AUTH_CONST.__const: 0x3f00
-  __AUTH_CONST.__cfstring: 0x1e8e0
-  __AUTH_CONST.__objc_const: 0x3aab0
-  __AUTH_CONST.__objc_intobj: 0x438
-  __AUTH_CONST.__objc_arrayobj: 0xd98
-  __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH.__objc_data: 0x8de0
+  __AUTH_CONST.__cfstring: 0x1ef40
+  __AUTH_CONST.__objc_const: 0x36b40
+  __AUTH_CONST.__objc_intobj: 0x420
+  __AUTH_CONST.__objc_arrayobj: 0xdb0
+  __AUTH_CONST.__objc_doubleobj: 0x50
+  __AUTH.__objc_data: 0x8fc0
   __AUTH.__data: 0xd8
-  __DATA.__objc_ivar: 0x2068
-  __DATA.__data: 0x2850
-  __DATA.__bss: 0xdf0
+  __DATA.__objc_ivar: 0x215c
+  __DATA.__data: 0x2860
+  __DATA.__bss: 0xe00
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__bss: 0xd8

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 894EFFDD-4E71-37C6-A81C-F9E561AB3390
-  Functions: 12368
-  Symbols:   28645
-  CStrings:  22409
+  UUID: B9661875-78D2-3AC6-9642-A096763E278A
+  Functions: 12783
+  Symbols:   29690
+  CStrings:  22874
 
Symbols:
+ +[MPAVOutputDeviceRoutingDataSource _globalAudioSessionLock].cold.1
+ +[MPAVRoutingController _getActiveRouteWithTimeout:type:completion:].cold.1
+ +[MPAVRoutingController _sharedWorkerQueue].cold.1
+ +[MPAVRoutingController getProactiveRecommendedRouteWithCompletion:]
+ +[MPAVRoutingController getProactiveRecommendedRouteWithTimeout:completion:]
+ +[MPAVRoutingController systemRoute].cold.1
+ +[MPArtworkCatalog _artworkLoadQueue].cold.1
+ +[MPArtworkCatalog _registeredIdentifiableDataSourceAndTokenClasses].cold.1
+ +[MPArtworkConfiguration systemConfiguration].cold.1
+ +[MPBaseEntityTranslator buildSchemaIfNeeded].cold.1
+ +[MPBaseEntityTranslator createTranslatorForMPModelClass:].cold.1
+ +[MPCloudController _controllerWithUserIdentity:createIfRequired:].cold.1
+ +[MPCloudController controllers].cold.1
+ +[MPCloudController globalSerialQueue].cold.1
+ +[MPCloudController isMediaApplication].cold.1
+ +[MPCloudController sharedCloudController].cold.1
+ +[MPCloudServiceStatusController controllers].cold.1
+ +[MPCloudServiceStatusController globalSerialQueue].cold.1
+ +[MPCloudServiceStatusController sharedController].cold.1
+ +[MPContentTasteController controllers].cold.1
+ +[MPContentTasteController globalSerialQueue].cold.1
+ +[MPContentTasteController sharedController].cold.1
+ +[MPHomeManagerObserver sharedObserver].cold.1
+ +[MPHomeMonitor sharedMonitor].cold.1
+ +[MPIdentifierSet emptyIdentifierSet].cold.1
+ +[MPMediaItem dynamicProperties].cold.1
+ +[MPMediaItemCollection representativePersistentIDPropertyForGroupingType:].cold.1
+ +[MPMediaItemCollection sortTitlePropertyForGroupingType:].cold.1
+ +[MPMediaItemCollection titlePropertyForGroupingType:].cold.1
+ +[MPMediaKitEntityTranslator buildSchemaIfNeeded].cold.1
+ +[MPMediaKitEntityTranslator createTranslatorForMPModelClass:].cold.1
+ +[MPMediaLibrary _deviceMediaLibraryWithUserIdentity:createIfRequired:].cold.1
+ +[MPMediaLibrary _sharedCloudServiceStatusMonitor].cold.1
+ +[MPMediaLibrary deviceMediaLibrary].cold.1
+ +[MPMediaLibrary initialize].cold.1
+ +[MPMediaLibraryPrivacyContext sharedContextForCurrentProcess].cold.1
+ +[MPMediaQuery initFilteringDisabled].cold.1
+ +[MPMediaRemoteEntityTranslator buildSchemaIfNeeded].cold.1
+ +[MPModelKind _kindWithModelClass:cacheKey:block:].cold.1
+ +[MPModelKind identityKind].cold.1
+ +[MPModelObject performWithoutEnforcement:].cold.1
+ +[MPModelObject performWithoutEnforcement:].cold.2
+ +[MPModelPlaylist __MPModelPropertyPlaylistEditSessionID__MAPPING_MISSING__]
+ +[MPModelPlaylist __MPModelPropertyPlaylistPortraitArtwork__MAPPING_MISSING__]
+ +[MPModelPlaylist __editSessionID_KEY]
+ +[MPModelPlaylist __portraitArtworkCatalogBlock_KEY]
+ +[MPModelPlaylistEntry newUniversalIdentifier]
+ +[MPModelPodcastEpisode __MPModelPropertyPodcastEpisodeSubtitleShort__MAPPING_MISSING__]
+ +[MPModelPodcastEpisode __MPModelPropertyPodcastEpisodeSubtitle__MAPPING_MISSING__]
+ +[MPModelPodcastEpisode __subtitleShort_KEY]
+ +[MPModelPodcastEpisode __subtitle_KEY]
+ +[MPModelRadioStation __MPModelPropertyRadioStationEditorialArtwork__MAPPING_MISSING__]
+ +[MPModelRadioStation __editorialArtworkCatalogBlock_KEY]
+ +[MPModelRequest sharedNetworkQueue].cold.1
+ +[MPModelRequest sharedQueue].cold.1
+ +[MPMusicPlayerController applicationQueuePlayer].cold.1
+ +[MPMusicPlayerController systemMusicPlayer].cold.1
+ +[MPNetworkObserver sharedNetworkObserver].cold.1
+ +[MPNowPlayingInfoCenter defaultCenter].cold.1
+ +[MPNowPlayingInfoCenter serviceQueue].cold.1
+ +[MPNowPlayingSession nowPlayingSessionForPlayerID:]
+ +[MPNowPlayingSession nowPlayingSessionForPlayerPath:]
+ +[MPPlayableContentManager _deviceIsCarplayCapable].cold.1
+ +[MPPlayableContentManager sharedContentManager].cold.1
+ +[MPPlaybackUserDefaults standardUserDefaults].cold.1
+ +[MPRemoteCommandCenter sharedCommandCenter].cold.1
+ +[MPRemotePlaybackQueue queueWithMediaRemotePlaybackQueue:options:].cold.1
+ +[MPRequest responseClass].cold.1
+ +[MPResponse builderProtocol].cold.1
+ +[MPRestrictionsMonitor sharedRestrictionsMonitor].cold.1
+ +[MPSectionedIdentifierList _performWithoutRequiringExclusivity:].cold.1
+ +[MPServerObjectDatabase setXPCHostApplicationIdentifier:].cold.1
+ +[MPServerObjectDatabaseMediaKitImportRequest _unsupportedMediaKitTypes].cold.1
+ +[MPServerObjectDatabaseMediaKitImportRequest _unsupportedParentChildRelationships].cold.1
+ +[MPServerObjectDatabaseStorePlatformImportRequest _unsupportedParentChildRelationships].cold.1
+ +[MPServerObjectDatabaseStorePlatformImportRequest _unsupportedStorePlatformKinds].cold.1
+ +[MPStoreArtworkDataSource sharedStoreArtworkDataSource].cold.1
+ +[MPStoreAssetInfoPlaybackCache sharedCache].cold.1
+ +[MPStoreItemMetadata storeServerCalendar].cold.1
+ +[MPStoreItemMetadataRequestController sharedStoreItemMetadataRequestController].cold.1
+ +[MPStoreLibraryPersonalizationRequest preferredQueue].cold.1
+ +[MPStorePlatformEntityTranslator buildSchemaIfNeeded].cold.1
+ +[MPTiledArtworkDataSource sharedDataSource].cold.1
+ +[MPVolumeHUDController sharedInstance].cold.1
+ +[MPVolumeHardwareButtonController sharedController].cold.1
+ +[MPiTunesLibraryEntityTranslator buildSchemaIfNeeded].cold.1
+ +[_MPMediaSearchStringPredicate predicateWithSearchString:forProperties:].cold.1
+ +[_MPMediaSearchStringPredicate predicateWithSearchString:forProperties:].cold.2
+ +[_MPNowPlayingInfoTransportableSessionRequest requestWithMediaRemoteRequest:]
+ -[AVPlayerItem(MPAdditions) nowPlayingInfo]
+ -[AVPlayerItem(MPAdditions) setNowPlayingInfo:]
+ -[ITMediaItem defaultValueForProperty:isKnownProperty:].cold.1
+ -[ITMediaItem propertyForMPMediaEntityProperty:].cold.1
+ -[ITMediaLibrary localizedSectionIndexTitles].cold.1
+ -[MPAVEndpointRoute setEndpointWrapper:].cold.1
+ -[MPAVEndpointRoutingDataSource setRoutingContextUID:].cold.1
+ -[MPAVItem _copyPlayerItem].cold.1
+ -[MPAVItem _pickupContentItemFrom:].cold.1
+ -[MPAVItem addAdjunctError:].cold.1
+ -[MPAVItem subtitleShort]
+ -[MPAVItem subtitle]
+ -[MPAVOutputDeviceRoute initWithOutputDevices:].cold.1
+ -[MPAVOutputDeviceRoutingDataSource addRouteToGroup:completion:].cold.1
+ -[MPAVOutputDeviceRoutingDataSource removeRouteFromGroup:completion:].cold.1
+ -[MPAVOutputDeviceRoutingDataSource routeIsLeaderOfEndpoint:].cold.1
+ -[MPAVOutputDeviceRoutingDataSource setRoutingContextUID:].cold.1
+ -[MPAVRoute isB465Route]
+ -[MPAVRouteConnection initWithExternalDeviceObject:].cold.1
+ -[MPAVRoutingController _pickRoute:completion:].cold.1
+ -[MPAVTelevisionRoute initWithTelevision:].cold.1
+ -[MPAbstractNetworkArtworkDataSource _requestForCatalog:kind:size:].cold.1
+ -[MPAbstractNetworkArtworkDataSource areRepresentationsAvailableForCatalog:].cold.1
+ -[MPAbstractNetworkArtworkDataSource requestForCatalog:size:].cold.1
+ -[MPAbstractNetworkArtworkDataSource supportedSizesForCatalog:].cold.1
+ -[MPAdTimeRange copyWithZone:]
+ -[MPAdTimeRange description]
+ -[MPAdTimeRange initWithTimeRange:]
+ -[MPAdTimeRange isEqual:]
+ -[MPAdTimeRange setTimeRange:]
+ -[MPAdTimeRange timeRange]
+ -[MPArtworkConfiguration sizesToAutogenerateForMediaType:artworkType:artworkVariantType:]
+ -[MPArtworkConfiguration supportedSizesForMediaType:artworkType:artworkVariantType:]
+ -[MPAsyncOperation execute].cold.1
+ -[MPBaseEntityTranslator mapUnsupportedPropertyKey:].cold.1
+ -[MPBaseEntityTranslator mapUnsupportedPropertyKey:].cold.2
+ -[MPBaseEntityTranslator mapUnsupportedRelationshipKey:].cold.1
+ -[MPBaseEntityTranslator setSourcePreprocessorBlock:].cold.1
+ -[MPChangeDetails appendItemMoveFromIndexPath:toIndexPath:updated:].cold.1
+ -[MPChangeDetails appendItemUpdateForPreviousIndexPath:finalIndexPath:].cold.1
+ -[MPChangeDetails appendSectionMoveFromIndex:toIndex:updated:].cold.1
+ -[MPChangeDetails appendSectionUpdateForPreviousIndex:finalIndex:].cold.1
+ -[MPChangeDetails applyUIKitWorkarounds].cold.1
+ -[MPChangeDetails isValidForPreviousCount:finalCount:reason:].cold.1
+ -[MPChangeDetails removeItemMoveFromIndexPath:].cold.1
+ -[MPChangeDetails removeItemUpdateForPreviousIndexPath:].cold.1
+ -[MPChangeDetails removeSectionMoveFromIndex:].cold.1
+ -[MPChangeDetails removeSectionUpdateForPreviousIndex:].cold.1
+ -[MPChangeDetails setUpdatedItemIndexPaths:].cold.1
+ -[MPChangeDetails setUpdatedSections:].cold.1
+ -[MPCloudController canSetItemProperty:].cold.1
+ -[MPCloudController canSetPlaylistProperty:].cold.1
+ -[MPCloudController fetchRecommendedContentWithSeedTrackID:seedTrackIDType:count:completion:].cold.1
+ -[MPCloudController loadArtworkForEntityPersistentID:entityType:artworkType:artworkSourceType:artworkVariantType:completionHandler:]
+ -[MPCloudController updateJaliscoMediaLibraryWithReason:completionHandler:].cold.1
+ -[MPConcreteMediaEntityPropertiesCache cacheValue:forProperty:persistValueInBackgroundBlock:].cold.1
+ -[MPConcreteMediaItem _initWithPersistentID:library:propertiesCache:].cold.1
+ -[MPContentItem initWithIdentifier:].cold.1
+ -[MPDelegateAccountCommandEvent .cxx_destruct]
+ -[MPDelegateAccountCommandEvent delegateAccountDataType]
+ -[MPDelegateAccountCommandEvent delegateAccountData]
+ -[MPDelegateAccountCommandEvent initWithCommand:mediaRemoteType:options:]
+ -[MPDispatchQueueExclusiveAccessToken assertHasExclusiveAccessForOwner:].cold.1
+ -[MPIdentifierSet hash].cold.1
+ -[MPIdentifierSet hash].cold.10
+ -[MPIdentifierSet hash].cold.11
+ -[MPIdentifierSet hash].cold.12
+ -[MPIdentifierSet hash].cold.13
+ -[MPIdentifierSet hash].cold.14
+ -[MPIdentifierSet hash].cold.15
+ -[MPIdentifierSet hash].cold.16
+ -[MPIdentifierSet hash].cold.17
+ -[MPIdentifierSet hash].cold.18
+ -[MPIdentifierSet hash].cold.19
+ -[MPIdentifierSet hash].cold.2
+ -[MPIdentifierSet hash].cold.20
+ -[MPIdentifierSet hash].cold.21
+ -[MPIdentifierSet hash].cold.22
+ -[MPIdentifierSet hash].cold.23
+ -[MPIdentifierSet hash].cold.24
+ -[MPIdentifierSet hash].cold.25
+ -[MPIdentifierSet hash].cold.26
+ -[MPIdentifierSet hash].cold.27
+ -[MPIdentifierSet hash].cold.28
+ -[MPIdentifierSet hash].cold.3
+ -[MPIdentifierSet hash].cold.4
+ -[MPIdentifierSet hash].cold.5
+ -[MPIdentifierSet hash].cold.6
+ -[MPIdentifierSet hash].cold.7
+ -[MPIdentifierSet hash].cold.8
+ -[MPIdentifierSet hash].cold.9
+ -[MPIdentifierSet setLibraryIdentifiersWithDatabaseID:block:].cold.1
+ -[MPIdentifierSet setPersonalStoreIdentifiersWithPersonID:block:].cold.1
+ -[MPLibraryKeepLocalStatusObserverConfiguration hash].cold.1
+ -[MPLibraryKeepLocalStatusObserverConfiguration hash].cold.2
+ -[MPLibraryKeepLocalStatusObserverConfiguration hash].cold.3
+ -[MPLibraryKeepLocalStatusObserverConfiguration hash].cold.4
+ -[MPLocalPickerQueryViewController tableView:cellForRowAtIndexPath:].cold.1
+ -[MPLocalPickerSimpleQueryViewController tableView:cellForRowAtIndexPath:].cold.1
+ -[MPMediaCompoundPredicate initWithProtobufferDecodableObject:library:].cold.1
+ -[MPMediaConditionalPredicate initWithProtobufferDecodableObject:library:].cold.1
+ -[MPMediaItem encodeWithCoder:].cold.1
+ -[MPMediaItem existsInLibrary].cold.1
+ -[MPMediaItem gaplessHeuristicInfo:durationInSamples:lastPacketsResync:encodingDelay:encodingDrain:].cold.1
+ -[MPMediaItem gaplessHeuristicInfo:durationInSamples:lastPacketsResync:encodingDelay:encodingDrain:].cold.2
+ -[MPMediaItem isRental].cold.1
+ -[MPMediaItem valueForProperty:].cold.1
+ -[MPMediaItem valuesForProperties:].cold.1
+ -[MPMediaItemCollection encodeWithCoder:].cold.1
+ -[MPMediaItemCollection initWithCoder:].cold.1
+ -[MPMediaKitEntityPayloadTransformer initWithType:transformedType:].cold.1
+ -[MPMediaKitEntityTranslator mapRelationshipKey:toModelClass:mediaKitType:].cold.1
+ -[MPMediaLibrary encodeWithCoder:].cold.1
+ -[MPMediaLibrary initWithCoder:].cold.1
+ -[MPMediaLibrary setValues:forProperties:forItemPersistentIDs:].cold.1
+ -[MPMediaLibraryArtworkRequest hash].cold.1
+ -[MPMediaLibraryArtworkRequest hash].cold.2
+ -[MPMediaLibraryArtworkRequest hash].cold.3
+ -[MPMediaLibraryArtworkRequest hash].cold.4
+ -[MPMediaLibraryArtworkRequest hash].cold.5
+ -[MPMediaLibraryArtworkRequest hash].cold.6
+ -[MPMediaLibraryArtworkRequest initWithLibrary:identifier:entityType:artworkType:mediaType:variantType:]
+ -[MPMediaLibraryArtworkRequest variantType]
+ -[MPMediaLibraryDataProviderMacOS adjustedValueForMPProperty:ofEntity:withDefaultValue:].cold.1
+ -[MPMediaLibraryDataProviderMacOS name].cold.1
+ -[MPMediaPersistentIDsPredicate initWithProtobufferDecodableObject:library:].cold.1
+ -[MPMediaPickerController viewDidLoad].cold.1
+ -[MPMediaPropertyPredicate initWithProtobufferDecodableObject:library:].cold.1
+ -[MPMediaQuery _valueForAggregateFunction:onProperty:entityType:].cold.1
+ -[MPMediaQuery initWithProtobufferDecodableObject:library:].cold.1
+ -[MPMediaQueryCriteria excludesEntitiesWithBlankNames].cold.1
+ -[MPModalPresentationWindow presentAlertController:animated:completion:].cold.1
+ -[MPModelGenericObject mergeWithObject:].cold.1
+ -[MPModelGenericObject mergeWithObject:].cold.2
+ -[MPModelLibraryPlaylistEditChangeDetails .cxx_destruct]
+ -[MPModelLibraryPlaylistEditChangeDetails _descriptionForType:]
+ -[MPModelLibraryPlaylistEditChangeDetails _initWithType:itemIdentifier:]
+ -[MPModelLibraryPlaylistEditChangeDetails changesApplied]
+ -[MPModelLibraryPlaylistEditChangeDetails copyWithZone:]
+ -[MPModelLibraryPlaylistEditChangeDetails description]
+ -[MPModelLibraryPlaylistEditChangeDetails initWithType:]
+ -[MPModelLibraryPlaylistEditChangeDetails initWithType:itemIdentifier:]
+ -[MPModelLibraryPlaylistEditChangeDetails isLastItem]
+ -[MPModelLibraryPlaylistEditChangeDetails itemIdentifier]
+ -[MPModelLibraryPlaylistEditChangeDetails itemPositionIdentifier]
+ -[MPModelLibraryPlaylistEditChangeDetails item]
+ -[MPModelLibraryPlaylistEditChangeDetails playlistName]
+ -[MPModelLibraryPlaylistEditChangeDetails previousPlaylistName]
+ -[MPModelLibraryPlaylistEditChangeDetails previousPositionIdentifier]
+ -[MPModelLibraryPlaylistEditChangeDetails previousReferenceIdentifier]
+ -[MPModelLibraryPlaylistEditChangeDetails referenceItemIdentifier]
+ -[MPModelLibraryPlaylistEditChangeDetails referenceItemPositionIdentifier]
+ -[MPModelLibraryPlaylistEditChangeDetails referenceItem]
+ -[MPModelLibraryPlaylistEditChangeDetails setChangesApplied:]
+ -[MPModelLibraryPlaylistEditChangeDetails setIsLastItem:]
+ -[MPModelLibraryPlaylistEditChangeDetails setItem:]
+ -[MPModelLibraryPlaylistEditChangeDetails setItemIdentifier:]
+ -[MPModelLibraryPlaylistEditChangeDetails setItemPositionIdentifier:]
+ -[MPModelLibraryPlaylistEditChangeDetails setPlaylistName:]
+ -[MPModelLibraryPlaylistEditChangeDetails setPreviousPlaylistName:]
+ -[MPModelLibraryPlaylistEditChangeDetails setPreviousPositionIdentifier:]
+ -[MPModelLibraryPlaylistEditChangeDetails setPreviousReferenceIdentifier:]
+ -[MPModelLibraryPlaylistEditChangeDetails setReferenceItem:]
+ -[MPModelLibraryPlaylistEditChangeDetails setReferenceItemIdentifier:]
+ -[MPModelLibraryPlaylistEditChangeDetails setReferenceItemPositionIdentifier:]
+ -[MPModelLibraryPlaylistEditChangeDetails type]
+ -[MPModelLibraryPlaylistEditController _applyChanges:toTransaction:completion:]
+ -[MPModelLibraryPlaylistEditController _createTrackIdentifierListWithInitialEntries:initialObjects:completion:]
+ -[MPModelLibraryPlaylistEditController _currentPlaylist]
+ -[MPModelLibraryPlaylistEditController _currentTrackList]
+ -[MPModelLibraryPlaylistEditController _endTransactionCommittingChanges:]
+ -[MPModelLibraryPlaylistEditController _endTransactionCommittingChanges:].cold.1
+ -[MPModelLibraryPlaylistEditController _initWithLibrary:playlist:initialTrackList:initialItemList:playlistEntryProperties:authorProfile:]
+ -[MPModelLibraryPlaylistEditController _insertObjects:afterEntry:completion:]
+ -[MPModelLibraryPlaylistEditController _isLastEntry:]
+ -[MPModelLibraryPlaylistEditController _logEditorState]
+ -[MPModelLibraryPlaylistEditController _movePlaylistEntry:afterEntry:]
+ -[MPModelLibraryPlaylistEditController _removePlaylistEntries:]
+ -[MPModelLibraryPlaylistEditController _setPlaylistName:]
+ -[MPModelLibraryPlaylistEditController _startNewTransaction]
+ -[MPModelLibraryPlaylistEditController _startTransactionWithIdentifier:]
+ -[MPModelLibraryPlaylistEditController _startTransactionWithIdentifier:].cold.1
+ -[MPModelLibraryPlaylistEditController appendObject:completion:]
+ -[MPModelLibraryPlaylistEditController appendObjects:completion:]
+ -[MPModelLibraryPlaylistEditController applyChanges:completion:]
+ -[MPModelLibraryPlaylistEditController debugDescriptionForItem:inSection:].cold.1
+ -[MPModelLibraryPlaylistEditController editSessionID]
+ -[MPModelLibraryPlaylistEditController initWithLibrary:initialItemList:playlistEntryProperties:authorProfile:]
+ -[MPModelLibraryPlaylistEditController initialTrackList]
+ -[MPModelLibraryPlaylistEditController insertObject:afterEntry:completion:]
+ -[MPModelLibraryPlaylistEditController insertObjectAtStart:completion:]
+ -[MPModelLibraryPlaylistEditController insertObjects:afterEntry:completion:]
+ -[MPModelLibraryPlaylistEditController insertObjectsAtStart:completion:]
+ -[MPModelLibraryPlaylistEditController isRedoAvailable]
+ -[MPModelLibraryPlaylistEditController isUndoAvailable]
+ -[MPModelLibraryPlaylistEditController maxUndoLimit]
+ -[MPModelLibraryPlaylistEditController movePlaylistEntry:afterEntry:]
+ -[MPModelLibraryPlaylistEditController movePlaylistEntryToStart:]
+ -[MPModelLibraryPlaylistEditController performTransactionWithBlock:]
+ -[MPModelLibraryPlaylistEditController performTransactionWithIdentifier:block:]
+ -[MPModelLibraryPlaylistEditController redoNextTransactionWithCompletion:]
+ -[MPModelLibraryPlaylistEditController removeAllPlaylistEntries]
+ -[MPModelLibraryPlaylistEditController removePlaylistEntries:]
+ -[MPModelLibraryPlaylistEditController removePlaylistEntry:]
+ -[MPModelLibraryPlaylistEditController setEditSessionID:]
+ -[MPModelLibraryPlaylistEditController setMaxUndoLimit:]
+ -[MPModelLibraryPlaylistEditController setPlaylistName:]
+ -[MPModelLibraryPlaylistEditController transactionsSinceIdentifier:]
+ -[MPModelLibraryPlaylistEditController undoPreviousTransactionWithCompletion:]
+ -[MPModelLibraryPlaylistEditDataSource loadEntriesWithCompletion:].cold.1
+ -[MPModelLibraryPlaylistEditPlaylistEntryDataSource initWithPlaylistEntries:].cold.1
+ -[MPModelLibraryPlaylistEditTrackDataSource initWithTrackObjects:].cold.1
+ -[MPModelLibraryPlaylistEditTransactionDetails .cxx_destruct]
+ -[MPModelLibraryPlaylistEditTransactionDetails _initWithIdentifier:referenceIdentifier:changes:]
+ -[MPModelLibraryPlaylistEditTransactionDetails addChange:]
+ -[MPModelLibraryPlaylistEditTransactionDetails addChanges:]
+ -[MPModelLibraryPlaylistEditTransactionDetails changes]
+ -[MPModelLibraryPlaylistEditTransactionDetails copyWithZone:]
+ -[MPModelLibraryPlaylistEditTransactionDetails description]
+ -[MPModelLibraryPlaylistEditTransactionDetails identifier]
+ -[MPModelLibraryPlaylistEditTransactionDetails initWithIdentifier:]
+ -[MPModelLibraryPlaylistEditTransactionDetails initWithIdentifier:changes:]
+ -[MPModelLibraryPlaylistEditTransactionDetails initWithIdentifier:referenceIdentifier:]
+ -[MPModelLibraryPlaylistEditTransactionDetails referenceIdentifier]
+ -[MPModelLibraryPlaylistEditTransactionDetails setChanges:]
+ -[MPModelObject initWithCoder:].cold.1
+ -[MPModelObject mergeWithObject:].cold.1
+ -[MPModelObject setValue:forModelKey:].cold.1
+ -[MPModelObject setValue:forModelKey:].cold.2
+ -[MPModelObject valueForModelKey:].cold.1
+ -[MPModelObject valueForModelKey:].cold.2
+ -[MPModelPlaylist portraitArtworkCatalog]
+ -[MPModelRadioStation editorialArtworkCatalog]
+ -[MPModelRequest newOperationWithResponseHandler:].cold.1
+ -[MPModelResponse initWithRequest:].cold.1
+ -[MPModelSortDescriptor hash].cold.1
+ -[MPModelSortDescriptor hash].cold.2
+ -[MPMusicPlayerApplicationController _setApplicationMusicPlayerTransitionType:withDuration:].cold.1
+ -[MPMusicPlayerController _establishConnectionIfNeeded].cold.1
+ -[MPMusicPlayerController _handleMediaServicesLost:]
+ -[MPMusicPlayerController _handleMediaServicesReset:]
+ -[MPMusicPlayerController _wakeServerIfConnectedForReason:]
+ -[MPMusicPlayerController initWithClientIdentifier:queue:].cold.1
+ -[MPMusicPlayerPlayParameters hash].cold.1
+ -[MPMusicPlayerPlayParameters hash].cold.2
+ -[MPMusicPlayerPlayParameters hash].cold.3
+ -[MPMusicPlayerPlayParameters hash].cold.4
+ -[MPMusicPlayerPlayParameters hash].cold.5
+ -[MPMusicPlayerPlayParameters hash].cold.6
+ -[MPMusicPlayerQueueDescriptor _init].cold.1
+ -[MPMusicPlayerQueueDescriptor isEmpty].cold.1
+ -[MPNondurableMediaItem setValue:forKey:].cold.1
+ -[MPNondurableMediaItem valueForProperty:].cold.1
+ -[MPNowPlayingContentItem setSubtitleShort:]
+ -[MPNowPlayingContentItem subtitleShort]
+ -[MPNowPlayingInfoCenter _getTransportablePlaybackSessionRepresentationWithRequest:completion:]
+ -[MPNowPlayingInfoCenter _onDataSourceQueue_getContentItemIDsInRange:completion:].cold.1
+ -[MPNowPlayingInfoCenter initWithPlayerPath:].cold.1
+ -[MPNowPlayingInfoCenter(NowPlayingInfo) _onQueue_pushNowPlayingInfoAndRetry:].cold.1
+ -[MPNowPlayingParticipant initWithIdentifier:].cold.1
+ -[MPNowPlayingParticipant initWithIdentifier:mediaRemoteUserIdentity:].cold.1
+ -[MPNowPlayingParticipant initWithIdentifier:mediaRemoteUserIdentity:].cold.2
+ -[MPNowPlayingParticipant initWithMediaRemoteContentItem:].cold.1
+ -[MPNowPlayingParticipant initWithMediaRemoteUserIdentity:].cold.1
+ -[MPNowPlayingSession .cxx_destruct]
+ -[MPNowPlayingSession _playerItemNowPlayingInfoDidChange:]
+ -[MPNowPlayingSession activePlayerDidChangeNotification:]
+ -[MPNowPlayingSession adTimeRangesEndObserverToken]
+ -[MPNowPlayingSession adTimeRangesStartObserverToken]
+ -[MPNowPlayingSession addPlayer:]
+ -[MPNowPlayingSession addPlayerItemObservers:]
+ -[MPNowPlayingSession addPlayerObservers:]
+ -[MPNowPlayingSession audioSession]
+ -[MPNowPlayingSession automaticallyPublishesNowPlayingInfo]
+ -[MPNowPlayingSession baseNowPlayingInfo]
+ -[MPNowPlayingSession becomeActiveIfPossibleWithCompletion:]
+ -[MPNowPlayingSession canBecomeActive]
+ -[MPNowPlayingSession creditsTimeObserverToken]
+ -[MPNowPlayingSession currentAdTimeRanges]
+ -[MPNowPlayingSession currentAssetNetCreditsStartTime]
+ -[MPNowPlayingSession currentAssetNetDuration]
+ -[MPNowPlayingSession dealloc]
+ -[MPNowPlayingSession delegate]
+ -[MPNowPlayingSession effectivePlaybackRateWithPlayer:]
+ -[MPNowPlayingSession endpointWithCompletion:]
+ -[MPNowPlayingSession endpointWithCompletion:].cold.1
+ -[MPNowPlayingSession extractNowPlayingInfoFromPlayersAndUpdateAdRanges]
+ -[MPNowPlayingSession hasInvalidAdTimeRange:totalDuration:]
+ -[MPNowPlayingSession initWithPlayerPath:routingContextID:]
+ -[MPNowPlayingSession initWithPlayerPath:routingContextID:].cold.1
+ -[MPNowPlayingSession initWithPlayers:]
+ -[MPNowPlayingSession initWithPlayers:].cold.1
+ -[MPNowPlayingSession invalidate]
+ -[MPNowPlayingSession isActive]
+ -[MPNowPlayingSession isPictureInPictureEnabled]
+ -[MPNowPlayingSession mediaExperienceIDs]
+ -[MPNowPlayingSession mxSessionIDKeyPath]
+ -[MPNowPlayingSession mxSessionIDs]
+ -[MPNowPlayingSession netTimeForGrossTime:]
+ -[MPNowPlayingSession nowPlayingInfoCenter]
+ -[MPNowPlayingSession nowPlayingInfoCenter].cold.1
+ -[MPNowPlayingSession observeValueForKeyPath:ofObject:change:context:]
+ -[MPNowPlayingSession playerItemDidPlayToEnd:]
+ -[MPNowPlayingSession playerItemPlaybackStalled:]
+ -[MPNowPlayingSession playerItemTimeJumped:]
+ -[MPNowPlayingSession playerPath]
+ -[MPNowPlayingSession playerPictureInPictureEnabledDidChangeNotification:]
+ -[MPNowPlayingSession playerRateDidChange:]
+ -[MPNowPlayingSession playerSet]
+ -[MPNowPlayingSession players]
+ -[MPNowPlayingSession privateQueue]
+ -[MPNowPlayingSession remoteCommandCenter]
+ -[MPNowPlayingSession removePlayer:]
+ -[MPNowPlayingSession removePlayerItemObservers:]
+ -[MPNowPlayingSession removePlayerObservers:]
+ -[MPNowPlayingSession routingContextID]
+ -[MPNowPlayingSession setActive:]
+ -[MPNowPlayingSession setAdTimeRangesEndObserverToken:]
+ -[MPNowPlayingSession setAdTimeRangesStartObserverToken:]
+ -[MPNowPlayingSession setAutomaticallyPublishesNowPlayingInfo:]
+ -[MPNowPlayingSession setBaseNowPlayingInfo:]
+ -[MPNowPlayingSession setCanBecomeActive:]
+ -[MPNowPlayingSession setCreditsTimeObserverToken:]
+ -[MPNowPlayingSession setCurrentAdTimeRanges:]
+ -[MPNowPlayingSession setCurrentAssetNetCreditsStartTime:]
+ -[MPNowPlayingSession setCurrentAssetNetDuration:]
+ -[MPNowPlayingSession setDelegate:]
+ -[MPNowPlayingSession setNowPlayingInfoCenter:]
+ -[MPNowPlayingSession setPictureInPictureEnabled:]
+ -[MPNowPlayingSession setPlayerSet:]
+ -[MPNowPlayingSession setPrivateQueue:]
+ -[MPNowPlayingSession updateAudioSession:]
+ -[MPNowPlayingSession updateMediaExperienceIDs]
+ -[MPNowPlayingSession updateNowPlayingInfo]
+ -[MPPThreadKeyExclusiveAccessToken assertHasExclusiveAccessForOwner:].cold.1
+ -[MPPThreadKeyExclusiveAccessToken assertHasExclusiveAccessForOwner:].cold.2
+ -[MPPlaybackArchive hash].cold.1
+ -[MPPlaybackArchive hash].cold.10
+ -[MPPlaybackArchive hash].cold.11
+ -[MPPlaybackArchive hash].cold.12
+ -[MPPlaybackArchive hash].cold.2
+ -[MPPlaybackArchive hash].cold.3
+ -[MPPlaybackArchive hash].cold.4
+ -[MPPlaybackArchive hash].cold.5
+ -[MPPlaybackArchive hash].cold.6
+ -[MPPlaybackArchive hash].cold.7
+ -[MPPlaybackArchive hash].cold.8
+ -[MPPlaybackArchive hash].cold.9
+ -[MPPlaybackArchive setBundleIdentifier:].cold.1
+ -[MPPlaybackArchive setDisplayProperties:].cold.1
+ -[MPPlaybackArchive setFallbackStoreIdentifier:].cold.1
+ -[MPPlaybackArchive setSessionIdentifier:type:data:].cold.1
+ -[MPPlaybackArchive setSupportedOptions:].cold.1
+ -[MPPlaybackArchive setType:].cold.1
+ -[MPPlaybackArchiveDisplayProperties hash].cold.1
+ -[MPPlaybackArchiveDisplayProperties hash].cold.2
+ -[MPPlaybackArchiveDisplayProperties setArtworkImageData:].cold.1
+ -[MPPlaybackArchiveDisplayProperties setArtworkImageURL:].cold.1
+ -[MPPlaybackArchiveDisplayProperties setSubtitle:].cold.1
+ -[MPPlaybackArchiveDisplayProperties setTitle:].cold.1
+ -[MPPlaybackSessionCommandInfo hash].cold.1
+ -[MPPlaybackSessionCommandInfo hash].cold.2
+ -[MPPlaybackSessionCommandInfo hash].cold.3
+ -[MPPlaybackSessionCommandInfo hash].cold.4
+ -[MPQueueFeeder getRepresentativeMetadataForPlaybackContext:properties:completion:].cold.1
+ -[MPQueueFeeder identifierRegistryWithExclusiveAccess:].cold.1
+ -[MPQueueFeeder identifierRegistryWithExclusiveAccessReturningBOOL:].cold.1
+ -[MPQueueFeeder identifierRegistryWithExclusiveAccessReturningInteger:].cold.1
+ -[MPQueueFeeder identifierRegistryWithExclusiveAccessReturningObject:].cold.1
+ -[MPQueueFeeder replaceIdentifierRegistry:].cold.1
+ -[MPQueueFeederIdentifierRegistry applyChanges:identifierSetLookupBlock:itemIdentifierLookupBlock:]
+ -[MPQueueFeederIdentifierRegistry identifierSetForItem:].cold.1
+ -[MPRemoteCommandCenter _createRemoteCommandWithConcreteClass:mediaRemoteType:].cold.1
+ -[MPRemoteCommandCenter _locked_reevaluateCanBeNowPlayingApplication]
+ -[MPRemoteCommandCenter delegateAccountCommand]
+ -[MPRemoteCommandCenter initWithPlayerPath:].cold.1
+ -[MPRequestResponseController setRequest:].cold.1
+ -[MPRequestResponseController setResponse:].cold.1
+ -[MPRestrictionsMonitor _isRunningInStoreDemoMode].cold.1
+ -[MPRouteLabel _marketingNames].cold.1
+ -[MPRouteLabel setMinimumEndCharacterCount:].cold.1
+ -[MPSectionedCollection indexPathForGlobalIndex:].cold.1
+ -[MPSectionedIdentifierList _addBranchToEntry:entries:withExclusiveAccessToken:].cold.1
+ -[MPSectionedIdentifierList _itemEntry:sectionIdentifier:withExclusiveAccessToken:].cold.1
+ -[MPSectionedIdentifierList _tailEntryForSectionIdentifier:withExclusiveAccessToken:].cold.1
+ -[MPSectionedIdentifierList dataSourceInsertItems:afterItem:inSection:].cold.1
+ -[MPSectionedIdentifierList dataSourceInsertItemsAtHead:inSection:].cold.1
+ -[MPSectionedIdentifierList dataSourceInsertItemsAtTail:inSection:].cold.1
+ -[MPSectionedIdentifierList performWithExclusiveAccess:].cold.1
+ -[MPSectionedIdentifierList performWithExclusiveAccessAndReturnBOOL:].cold.1
+ -[MPSectionedIdentifierList performWithExclusiveAccessAndReturnInteger:].cold.1
+ -[MPSectionedIdentifierList performWithExclusiveAccessAndReturnObject:].cold.1
+ -[MPSectionedIdentifierList(Debugging) _debugDescriptionWithEnumerator:lengths:].cold.1
+ -[MPSectionedIdentifierListEntry addBranch:forceBranchDepthIncrease:].cold.1
+ -[MPSectionedIdentifierListEntry addBranch:forceBranchDepthIncrease:].cold.2
+ -[MPSectionedIdentifierListEntry addBranch:forceBranchDepthIncrease:].cold.3
+ -[MPSectionedIdentifierListEnumerator initWithSectionedIdentifierList:options:startEntry:endEntry:withExclusiveAccessToken:].cold.1
+ -[MPSectionedIdentifierListEnumerator initWithSectionedIdentifierList:options:startEntry:endEntry:withExclusiveAccessToken:].cold.2
+ -[MPSectionedIdentifierListReverseEnumerator initWithSectionedIdentifierList:options:startEntry:endEntry:withExclusiveAccessToken:].cold.1
+ -[MPServerObjectDatabase _modelObjectMatchingIdentifierSet:propertySet:error:].cold.1
+ -[MPServerObjectDatabaseAssetImportRequest performWithDatabaseOperations:error:].cold.1
+ -[MPServerObjectDatabaseMediaKitImportRequest _sinfDataFromSinfType:payload:].cold.1
+ -[MPServerObjectDatabaseMetadataImportRequest performWithDatabaseOperations:augmentingPayload:].cold.1
+ -[MPSetPlaybackSessionCommand requirements]
+ -[MPSetPlaybackSessionCommand setRequirements:]
+ -[MPShuffleableSectionedIdentifierList dataSourceInsertItems:afterItem:inSection:].cold.1
+ -[MPShuffleableSectionedIdentifierList dataSourceInsertItemsAtHead:inSection:].cold.1
+ -[MPShuffleableSectionedIdentifierList dataSourceInsertItemsAtTail:inSection:].cold.1
+ -[MPStoreItemMetadata _musicAPIDateFormatter].cold.1
+ -[MPStoreItemMetadata _storePlatformLastModifiedDateFormatter].cold.1
+ -[MPStoreItemMetadata _storePlatformReleaseDateFormatter].cold.1
+ -[MPStoreItemMetadata recommendationID]
+ -[MPStoreItemMetadataRequest enableRequestNotifications]
+ -[MPStoreItemMetadataRequest requestContextTag]
+ -[MPStoreItemMetadataRequest setRequestContextTag:]
+ -[MPVolumeController setDataSource:].cold.1
+ -[MPVolumeControllerRouteDataSource initWithGroupRoute:outputDeviceRoute:].cold.1
+ -[MPVolumeControllerRouteDataSource initWithGroupRoute:outputDeviceRoute:].cold.2
+ -[MPVolumeHUDController removeDeallocHandlerFromDisplay:]
+ -[MPVolumeHUDController setUpDeallocHandlerForDisplay:]
+ -[MPVolumeSlider setRoute:].cold.1
+ -[NSString(ITSorting) stringByTrimmingIgnoredLeadingCharacters].cold.1
+ -[NSString(MPArtworkColorAnalyzerAlgorithmiTunesAdditions) MP_colorFromHexString].cold.1
+ -[_MPActiveUserChangeMonitor _cancelNotificationTimerWithReason:].cold.1
+ -[_MPActiveUserChangeMonitor _startNotificationTimerWithEventHandler:].cold.1
+ -[_MPIdentifierListSectionProxy insertItems:afterItem:].cold.1
+ -[_MPIdentifierListSectionProxy moveItem:afterItem:].cold.1
+ -[_MPMediaLibraryArtworkVisualIdenticalityIdentifier hash].cold.1
+ -[_MPMediaLibraryArtworkVisualIdenticalityIdentifier hash].cold.2
+ -[_MPMediaSearchStringPredicate initWithProtobufferDecodableObject:library:].cold.1
+ -[_MPMiddlewareChainBuilderProxy respondsToSelector:]
+ -[_MPMusicPlayerControllerArtworkToken .cxx_destruct]
+ -[_MPMusicPlayerControllerArtworkToken initWithArtworkIdentifier:contentItemID:]
+ -[_MPNowPlayingInfoTransportableSessionRequest destinationCommandInfo]
+ -[_MPNowPlayingInfoTransportableSessionRequest destinationPlayerPath]
+ -[_MPSSILImplementation _appendShuffledItems:withExclusiveAccessToken:].cold.1
+ -[_MPSSILImplementation dataSourceInsertItems:afterItem:inSection:].cold.1
+ -[_MPSSILImplementation dataSourceInsertItemsAtHead:inSection:].cold.1
+ -[_MPSSILImplementation dataSourceInsertItemsAtTail:inSection:].cold.1
+ -[_MPServerObjectDatabaseImporter importAssetSinf:type:forIdentifier:hashedPersonID:flavor:sinfPayload:].cold.1
+ -[_MPServerObjectDatabaseImporter importAssetSinf:type:forIdentifier:hashedPersonID:flavor:sinfPayload:].cold.2
+ -[_MPServerObjectDatabaseImporter importAssetSinf:type:forIdentifier:hashedPersonID:flavor:sinfPayload:].cold.3
+ -[_MPServerObjectDatabaseImporter importAssetSinf:type:forIdentifier:hashedPersonID:flavor:sinfPayload:].cold.4
+ -[_MPServerObjectDatabaseImporter importAssetURL:forIdentifiers:flavor:expirationDate:].cold.1
+ -[_MPServerObjectDatabaseImporter importObject:type:identifiers:source:expiration:].cold.1
+ -[_MPServerObjectDatabaseImporter importObject:type:identifiers:source:expiration:].cold.2
+ -[_MPServerObjectDatabaseImporter relateIdentifiers:toParentIdentifiers:parentVersionHash:childKey:order:].cold.1
+ -[_MPServerObjectDatabaseImporter relateIdentifiers:toParentIdentifiers:parentVersionHash:childKey:order:].cold.2
+ -[_MPServerObjectDatabaseImporter removeRelationshipsForParentIdentifiers:childKey:].cold.1
+ -[_MPServerObjectDatabaseImporter removeRelationshipsForParentIdentifiers:childKey:].cold.2
+ GCC_except_table106
+ GCC_except_table112
+ GCC_except_table125
+ GCC_except_table139
+ GCC_except_table147
+ GCC_except_table152
+ GCC_except_table168
+ GCC_except_table171
+ GCC_except_table71
+ GCC_except_table98
+ MPAVGetBatteryLevelFromRouteDescription.cold.1
+ MPAVGetBatteryLevelFromRouteDescription.cold.2
+ MPChangeDetailOperationGenerateEx.cold.1
+ MPChangeDetailOperationGenerateEx.cold.10
+ MPChangeDetailOperationGenerateEx.cold.11
+ MPChangeDetailOperationGenerateEx.cold.12
+ MPChangeDetailOperationGenerateEx.cold.13
+ MPChangeDetailOperationGenerateEx.cold.14
+ MPChangeDetailOperationGenerateEx.cold.15
+ MPChangeDetailOperationGenerateEx.cold.2
+ MPChangeDetailOperationGenerateEx.cold.3
+ MPChangeDetailOperationGenerateEx.cold.4
+ MPChangeDetailOperationGenerateEx.cold.5
+ MPChangeDetailOperationGenerateEx.cold.6
+ MPChangeDetailOperationGenerateEx.cold.7
+ MPChangeDetailOperationGenerateEx.cold.8
+ MPChangeDetailOperationGenerateEx.cold.9
+ MPModelPropertyMappingMissing.cold.1
+ MPSharedBackgroundTaskProvider.cold.1
+ MPiTunesLibraryDurationMillisecondsToSecondsTransform.cold.1
+ OBJC_IVAR_$_MPAdTimeRange._timeRange
+ OBJC_IVAR_$_MPDelegateAccountCommandEvent._delegateAccountData
+ OBJC_IVAR_$_MPDelegateAccountCommandEvent._delegateAccountDataType
+ OBJC_IVAR_$_MPMediaLibraryArtworkRequest._variantType
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._changesApplied
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._isLastItem
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._item
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._itemIdentifier
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._itemPositionIdentifier
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._playlistName
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._previousPlaylistName
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._previousPositionIdentifier
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._previousReferenceIdentifier
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._referenceItem
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._referenceItemIdentifier
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._referenceItemPositionIdentifier
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditChangeDetails._type
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditController._accessQueue
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditController._completedTransactions
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditController._currentLastItemIdentifier
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditController._currentTransaction
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditController._editSessionID
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditController._initialTrackObjectList
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditController._itemIdentifierToPositionIdentifierMap
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditController._lastAppliedTransactionIndex
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditController._maxUndoLimit
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditController._notificationsSuspended
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditController._playlistEntriesByIdentifier
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditController._positionIdentifierToItemIdentifierMap
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditTransactionDetails._changes
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditTransactionDetails._identifier
+ OBJC_IVAR_$_MPModelLibraryPlaylistEditTransactionDetails._referenceIdentifier
+ OBJC_IVAR_$_MPMusicPlayerController._mediaServiceLost
+ OBJC_IVAR_$_MPNowPlayingSession._active
+ OBJC_IVAR_$_MPNowPlayingSession._adTimeRangesEndObserverToken
+ OBJC_IVAR_$_MPNowPlayingSession._adTimeRangesStartObserverToken
+ OBJC_IVAR_$_MPNowPlayingSession._audioSession
+ OBJC_IVAR_$_MPNowPlayingSession._automaticallyPublishesNowPlayingInfo
+ OBJC_IVAR_$_MPNowPlayingSession._baseNowPlayingInfo
+ OBJC_IVAR_$_MPNowPlayingSession._canBecomeActive
+ OBJC_IVAR_$_MPNowPlayingSession._creditsTimeObserverToken
+ OBJC_IVAR_$_MPNowPlayingSession._currentAdTimeRanges
+ OBJC_IVAR_$_MPNowPlayingSession._currentAssetNetCreditsStartTime
+ OBJC_IVAR_$_MPNowPlayingSession._currentAssetNetDuration
+ OBJC_IVAR_$_MPNowPlayingSession._delegate
+ OBJC_IVAR_$_MPNowPlayingSession._invalidated
+ OBJC_IVAR_$_MPNowPlayingSession._mxSessionIDs
+ OBJC_IVAR_$_MPNowPlayingSession._nowPlayingInfoCenter
+ OBJC_IVAR_$_MPNowPlayingSession._pictureInPictureEnabled
+ OBJC_IVAR_$_MPNowPlayingSession._playerPath
+ OBJC_IVAR_$_MPNowPlayingSession._playerSet
+ OBJC_IVAR_$_MPNowPlayingSession._privateQueue
+ OBJC_IVAR_$_MPNowPlayingSession._remoteCommandCenter
+ OBJC_IVAR_$_MPNowPlayingSession._routingContextID
+ OBJC_IVAR_$_MPRemoteCommandCenter._delegateAccountCommand
+ OBJC_IVAR_$_MPSetPlaybackSessionCommand._requirements
+ OBJC_IVAR_$_MPStoreItemMetadataRequest._requestContextTag
+ OBJC_IVAR_$_MPStoreItemMetadataRequest._requestNotificationsEnabled
+ OBJC_IVAR_$__MPMusicPlayerControllerArtworkToken._artworkIdentifier
+ OBJC_IVAR_$__MPMusicPlayerControllerArtworkToken._contentItemID
+ OBJC_IVAR_$__MPNowPlayingInfoTransportableSessionRequest._destinationCommandInfo
+ OBJC_IVAR_$__MPNowPlayingInfoTransportableSessionRequest._destinationPlayerPath
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSS_ypTt0g5
+ _AVAudioSessionMediaServicesWereLostNotification
+ _AVAudioSessionMediaServicesWereResetNotification
+ _AVPlayerItemPlaybackStalledNotification
+ _AVPlayerItemTimeJumpedNotification
+ _AVPlayerRateDidChangeNotification
+ _CMTimeAdd
+ _CMTimeCompare
+ _CMTimeRangeContainsTime
+ _CMTimeRangeCopyDescription
+ _CMTimeRangeEqual
+ _CMTimeRangeGetIntersection
+ _CMTimeRangeMake
+ _CMTimeSubtract
+ _MPChangeDetailOperationNodeRelease.cold.1
+ _MPCopyChildContentItemsCallback.cold.1
+ _MPMediaKitCalendar.cold.1
+ _MPMediaKitDateAndTimeFromString.cold.1
+ _MPMediaKitDateFromString.cold.1
+ _MPMediaPlaylistPropertyEditSessionID
+ _MPModelLibraryPlaylistEditErrorDomain
+ _MPModelPropertyPlaylistEditSessionID
+ _MPModelPropertyPlaylistPortraitArtwork
+ _MPModelPropertyPodcastEpisodeSubtitle
+ _MPModelPropertyPodcastEpisodeSubtitleShort
+ _MPModelPropertyRadioStationEditorialArtwork
+ _MPNowPlayingInfoPropertyForMRMediaRemoteNowPlayingInfoProperty.cold.1
+ _MPNowPlayingInfoPropertyToMRMediaRemoteNowPlayingInfoPropertyMapping.cold.1
+ _MPNowPlayingPublisherPlayerItemDurationObserverContext
+ _MPNowPlayingPublisherPlayerItemObserverContext
+ _MPNowPlayingPublisherPlayerTimeControlObserverContext
+ _MPPlayerItemNowPlayingInfoDidChangeNotification
+ _MPPropertyToITLibPropertyMap.cold.1
+ _MPStoreItemMetadataEditorialArtworkKindBackgroundStatic1x1
+ _MPStorePlatformCalendar.cold.1
+ _MPStorePlatformDateFromString.cold.1
+ _MPTitlePropertyForPidProperty.cold.1
+ _MRMediaRemoteCanBecomeActivePlayer
+ _MRMediaRemoteGetPictureInPictureStatusForPlayer
+ _MRMediaRemoteSetMXSessionIDForPlayer
+ _MRMediaRemoteSetPictureInPictureStatusForPlayer
+ _MRMediaRemoteSetWantsNowPlayingNotifications
+ _NSKeyValueChangeOldKey
+ _OBJC_CLASS_$_MPAdTimeRange
+ _OBJC_CLASS_$_MPDelegateAccountCommandEvent
+ _OBJC_CLASS_$_MPModelLibraryPlaylistEditChangeDetails
+ _OBJC_CLASS_$_MPModelLibraryPlaylistEditTransactionDetails
+ _OBJC_CLASS_$_MPNowPlayingSession
+ _OBJC_CLASS_$_MRAVLightweightReconnaissanceSession
+ _OBJC_CLASS_$__MPMusicPlayerControllerArtworkToken
+ _OBJC_METACLASS_$_MPAdTimeRange
+ _OBJC_METACLASS_$_MPDelegateAccountCommandEvent
+ _OBJC_METACLASS_$_MPModelLibraryPlaylistEditChangeDetails
+ _OBJC_METACLASS_$_MPModelLibraryPlaylistEditTransactionDetails
+ _OBJC_METACLASS_$_MPNowPlayingSession
+ _OBJC_METACLASS_$__MPMusicPlayerControllerArtworkToken
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __111-[MPModelLibraryPlaylistEditController _createTrackIdentifierListWithInitialEntries:initialObjects:completion:]_block_invoke.88
+ __35-[MPRequest performWithCompletion:]_block_invoke_2.cold.1
+ __36-[MPMusicPlayerController onServer:]_block_invoke.158
+ __36-[MPMusicPlayerController onServer:]_block_invoke.159
+ __42+[NSBundle(MPAdditions) mediaPlayerBundle]_block_invoke.cold.1
+ __42-[MPMusicPlayerController _validateServer]_block_invoke.151
+ __45-[MPMediaEntityResultSetArray objectAtIndex:]_block_invoke.cold.1
+ __46-[MPNowPlayingSession setCurrentAdTimeRanges:]_block_invoke.74
+ __47-[MPAVRoutingControllerSelectionQueue _dequeue]_block_invoke.455
+ __48-[MPAVRoutingControllerSelectionQueue _enqueue:]_block_invoke.450
+ __48-[MPAVRoutingControllerSelectionQueue _enqueue:]_block_invoke.454
+ __48-[MPPlaybackUserDefaults _loadAccountProperties]_block_invoke.307
+ __54-[MPRequestResponseController _onQueue_reloadIfNeeded]_block_invoke.94.cold.1
+ __54-[MPRequestResponseController _onQueue_reloadIfNeeded]_block_invoke_2.cold.1
+ __56-[MPAVRoutingControllerSelectionQueue addPendingRoutes:]_block_invoke.442
+ __56-[MPModelLibraryPlaylistEditController initialTrackList]_block_invoke.cold.1
+ __57-[MPModelLibraryPlaylistEditController _currentTrackList]_block_invoke.101
+ __57-[MPServerObjectDatabase _initWithDatabaseCreationBlock:]_block_invoke.cold.1
+ __57-[MPServerObjectDatabase _initWithDatabaseCreationBlock:]_block_invoke.cold.2
+ __60-[MPMediaPickerController_Appex requestRemoteViewController]_block_invoke.169.cold.1
+ __62-[MPModelLibraryPlaylistEditDataSource _reloadWithCompletion:]_block_invoke.24
+ __62-[MPModelLibraryPlaylistEditDataSource _reloadWithCompletion:]_block_invoke.29
+ __62-[MPModelLibraryPlaylistEditDataSource _reloadWithCompletion:]_block_invoke_2.31
+ __64-[MPModelLibraryPlaylistEditController applyChanges:completion:]_block_invoke.50
+ __64-[MPSectionedIdentifierList dataSourceEndTransactionForSection:]_block_invoke.cold.1
+ __64-[MPSectionedIdentifierList dataSourceMoveItemToHead:inSection:]_block_invoke.cold.1
+ __64-[MPSectionedIdentifierList dataSourceMoveItemToHead:inSection:]_block_invoke.cold.2
+ __64-[MPSectionedIdentifierList dataSourceMoveItemToHead:inSection:]_block_invoke.cold.3
+ __64-[MPSectionedIdentifierList dataSourceMoveItemToTail:inSection:]_block_invoke.cold.1
+ __64-[MPSectionedIdentifierList dataSourceMoveItemToTail:inSection:]_block_invoke.cold.2
+ __64-[MPSectionedIdentifierList dataSourceMoveItemToTail:inSection:]_block_invoke.cold.3
+ __66-[MPSectionedIdentifierList dataSourceBeginTransactionForSection:]_block_invoke.cold.1
+ __67-[MPModelLibraryPlaylistEditController beginEditingWithCompletion:]_block_invoke.26
+ __67-[MPSectionedIdentifierList dataSourceInsertItemsAtHead:inSection:]_block_invoke.cold.1
+ __67-[MPSectionedIdentifierList dataSourceInsertItemsAtTail:inSection:]_block_invoke.cold.1
+ __68-[MPModelLibraryPlaylistEditController transactionsSinceIdentifier:]_block_invoke.cold.1
+ __68-[MPSectionedIdentifierList dataSourceMoveItem:afterItem:inSection:]_block_invoke.cold.1
+ __68-[MPSectionedIdentifierList dataSourceMoveItem:afterItem:inSection:]_block_invoke.cold.2
+ __69-[MPAVRoutingControllerSelectionQueue removePendingRoutes:withError:]_block_invoke.446
+ __69-[MPSectionedIdentifierList moveItem:fromSection:afterHeadOfSection:]_block_invoke.cold.1
+ __69-[MPSectionedIdentifierList moveItem:fromSection:afterTailOfSection:]_block_invoke.cold.1
+ __69-[MPSectionedIdentifierList moveItem:fromSection:afterTailOfSection:]_block_invoke.cold.2
+ __69-[MPSectionedIdentifierList replaceDataSource:forSection:completion:]_block_invoke.cold.1
+ __70-[MPMusicPlayerController prepareToPlayWithCompletionHandler:timeout:]_block_invoke.101
+ __70-[MPMusicPlayerController prepareToPlayWithCompletionHandler:timeout:]_block_invoke.102
+ __70-[MPMusicPlayerController prepareToPlayWithCompletionHandler:timeout:]_block_invoke.98
+ __70-[MPMusicPlayerController prepareToPlayWithCompletionHandler:timeout:]_block_invoke.99
+ __72-[MPRequestResponseController setNeedsReloadForSignificantRequestChange]_block_invoke.34.cold.1
+ __73-[MPAVRoutingControllerSelectionQueue cancelInProgressSelectionForRoute:]_block_invoke.439
+ __74-[MPModelLibraryPlaylistEditController redoNextTransactionWithCompletion:]_block_invoke.49
+ __75-[MPMusicPlayerController onServerAsync:errorHandler:timeout:retryEnabled:]_block_invoke.162
+ __75-[MPMusicPlayerController onServerAsync:errorHandler:timeout:retryEnabled:]_block_invoke.166
+ __75-[MPMusicPlayerController onServerAsync:errorHandler:timeout:retryEnabled:]_block_invoke.168
+ __75-[MPSectionedIdentifierList firstSectionMatching:containingItem:inSection:]_block_invoke.cold.1
+ __76-[MPNowPlayingInfoCenter _invalidatePlaybackQueueImmediatelyWithCompletion:]_block_invoke.99
+ __76-[MPNowPlayingInfoCenter _invalidatePlaybackQueueImmediatelyWithCompletion:]_block_invoke_4.cold.1
+ __76-[MPNowPlayingInfoCenter _onQueue_registerPlaybackQueueDataSourceCallbacks:]_block_invoke_13.cold.1
+ __77-[MPModelLibraryPlaylistEditController _insertObjects:afterEntry:completion:]_block_invoke.82
+ __77-[MPModelLibraryPlaylistEditController _insertObjects:afterEntry:completion:]_block_invoke.83
+ __77-[MPNowPlayingInfoCenter _contentItemForIdentifier:alreadyOnDataSourceQueue:]_block_invoke_2.cold.1
+ __78-[MPModelLibraryPlaylistEditController undoPreviousTransactionWithCompletion:]_block_invoke.45
+ __79-[MPModelLibraryPlaylistEditController _applyChanges:toTransaction:completion:]_block_invoke.73
+ __79-[MPModelLibraryPlaylistEditController _applyChanges:toTransaction:completion:]_block_invoke.77
+ __79-[MPModelLibraryPlaylistEditController performTransactionWithIdentifier:block:]_block_invoke.cold.1
+ __80-[MPAbstractNetworkArtworkDataSource _bestVideoArtworkRepresentationForCatalog:]_block_invoke.225
+ __80-[MPShuffleableSectionedIdentifierList moveItem:fromSection:afterHeadOfSection:]_block_invoke_2.cold.1
+ __80-[MPShuffleableSectionedIdentifierList moveItem:fromSection:afterTailOfSection:]_block_invoke_2.cold.1
+ __81-[MPNowPlayingInfoCenter _onDataSourceQueue_getContentItemIDsInRange:completion:]_block_invoke.108
+ __81-[MPSectionedIdentifierList addDataSource:section:afterHeadOfSection:completion:]_block_invoke.cold.1
+ __81-[MPSectionedIdentifierList addDataSource:section:afterTailOfSection:completion:]_block_invoke.cold.1
+ __81-[MPSectionedIdentifierList addDataSource:section:afterTailOfSection:completion:]_block_invoke.cold.2
+ __82-[MPSectionedIdentifierList addDataSource:section:afterItem:inSection:completion:]_block_invoke.cold.1
+ __82-[MPSectionedIdentifierList addDataSource:section:beforeTailOfSection:completion:]_block_invoke.cold.1
+ __82-[MPSectionedIdentifierList addDataSource:section:beforeTailOfSection:completion:]_block_invoke.cold.2
+ __95-[MPNowPlayingInfoCenter _getTransportablePlaybackSessionRepresentationWithRequest:completion:]_block_invoke_2.cold.1
+ __99-[MPAbstractNetworkArtworkDataSource loadRepresentationOfKind:forArtworkCatalog:completionHandler:]_block_invoke.163
+ __99-[MPAbstractNetworkArtworkDataSource loadRepresentationOfKind:forArtworkCatalog:completionHandler:]_block_invoke.190
+ __DeallocHandlerGuardKey
+ __MPGetModelToTranslatorMap.cold.1
+ __NSStringFromMPMediaEntityType
+ __NSStringFromMPMediaLibraryArtworkType
+ __NSStringFromMPMediaLibraryArtworkVariantType
+ __OBJC_$_CLASS_METHODS_MPNowPlayingSession
+ __OBJC_$_INSTANCE_METHODS_AVPlayerItem(MPAVItemAdditions|MPNowPlayingInfoLanguageOptionAdditions|MPAdditions)
+ __OBJC_$_INSTANCE_METHODS_MPAdTimeRange
+ __OBJC_$_INSTANCE_METHODS_MPDelegateAccountCommandEvent
+ __OBJC_$_INSTANCE_METHODS_MPModelLibraryPlaylistEditChangeDetails
+ __OBJC_$_INSTANCE_METHODS_MPModelLibraryPlaylistEditTransactionDetails
+ __OBJC_$_INSTANCE_METHODS_MPNowPlayingSession
+ __OBJC_$_INSTANCE_METHODS__MPMusicPlayerControllerArtworkToken
+ __OBJC_$_INSTANCE_VARIABLES_MPAdTimeRange
+ __OBJC_$_INSTANCE_VARIABLES_MPDelegateAccountCommandEvent
+ __OBJC_$_INSTANCE_VARIABLES_MPModelLibraryPlaylistEditChangeDetails
+ __OBJC_$_INSTANCE_VARIABLES_MPModelLibraryPlaylistEditTransactionDetails
+ __OBJC_$_INSTANCE_VARIABLES_MPNowPlayingSession
+ __OBJC_$_INSTANCE_VARIABLES__MPMusicPlayerControllerArtworkToken
+ __OBJC_$_PROP_LIST_MPAdTimeRange
+ __OBJC_$_PROP_LIST_MPDelegateAccountCommandEvent
+ __OBJC_$_PROP_LIST_MPModelLibraryPlaylistEditChangeDetails
+ __OBJC_$_PROP_LIST_MPModelLibraryPlaylistEditTransactionDetails
+ __OBJC_$_PROP_LIST_MPNowPlayingSession
+ __OBJC_CLASS_PROTOCOLS_$_MPAdTimeRange
+ __OBJC_CLASS_RO_$_MPAdTimeRange
+ __OBJC_CLASS_RO_$_MPDelegateAccountCommandEvent
+ __OBJC_CLASS_RO_$_MPModelLibraryPlaylistEditChangeDetails
+ __OBJC_CLASS_RO_$_MPModelLibraryPlaylistEditTransactionDetails
+ __OBJC_CLASS_RO_$_MPNowPlayingSession
+ __OBJC_CLASS_RO_$__MPMusicPlayerControllerArtworkToken
+ __OBJC_METACLASS_RO_$_MPAdTimeRange
+ __OBJC_METACLASS_RO_$_MPDelegateAccountCommandEvent
+ __OBJC_METACLASS_RO_$_MPModelLibraryPlaylistEditChangeDetails
+ __OBJC_METACLASS_RO_$_MPModelLibraryPlaylistEditTransactionDetails
+ __OBJC_METACLASS_RO_$_MPNowPlayingSession
+ __OBJC_METACLASS_RO_$__MPMusicPlayerControllerArtworkToken
+ __ZNKSt3__16vectorIU8__strongP13ITMediaEntityNS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIlNS_9allocatorIlEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt12out_of_rangeC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP11ITMediaItemEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP12ITMediaAlbumEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP12ITMediaGenreEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP13ITMediaArtistEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP15ITMediaComposerEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP15ITMediaPlaylistEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP17ITMediaCollectionEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP18ITMediaAlbumArtistEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIlU8__strongP15MPIdentifierSetEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE28__node_insert_unique_performB8ne190102EPNS_11__hash_nodeIyPvEE
+ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE28__node_insert_unique_prepareB8ne190102EmRy
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIU8__strongP13ITMediaEntityEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIlEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIxEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
+ __ZNSt3__124__sort5_maybe_branchlessB8ne190102INS_17_ClassicAlgPolicyERZ43-[ITMediaLibraryQueryResultSet sortResults]E3$_0PU8__strongP13ITMediaEntityLi0EEEvT1_S8_S8_S8_S8_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZ43-[ITMediaLibraryQueryResultSet sortResults]E3$_0PU8__strongP13ITMediaEntityEEbT1_S8_T0_
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16vectorIU8__strongP13ITMediaEntityNS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE16__init_with_sizeB8ne190102IPxS5_EEvT_T0_m
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE18__assign_with_sizeB8ne190102IPxS5_EEvT_T0_l
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZ43-[ITMediaLibraryQueryResultSet sortResults]E3$_0PU8__strongP13ITMediaEntityEEjT1_S8_S8_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZ43-[ITMediaLibraryQueryResultSet sortResults]E3$_0PU8__strongP13ITMediaEntityEEvT1_S8_S8_S8_T0_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___111-[MPModelLibraryPlaylistEditController _createTrackIdentifierListWithInitialEntries:initialObjects:completion:]_block_invoke
+ ___132-[MPCloudController loadArtworkForEntityPersistentID:entityType:artworkType:artworkSourceType:artworkVariantType:completionHandler:]_block_invoke
+ ___132-[MPCloudController loadArtworkForEntityPersistentID:entityType:artworkType:artworkSourceType:artworkVariantType:completionHandler:]_block_invoke_2
+ ___34-[MPNowPlayingInfoAudioRoute type]_block_invoke
+ ___38-[MPNowPlayingInfoAudioRoute setType:]_block_invoke
+ ___43-[MPNowPlayingSession netTimeForGrossTime:]_block_invoke
+ ___44-[MPModelLibraryPlaylistEditController name]_block_invoke
+ ___44-[MPNowPlayingContentItem setSubtitleShort:]_block_invoke
+ ___46-[MPNowPlayingSession endpointWithCompletion:]_block_invoke
+ ___46-[MPNowPlayingSession setCurrentAdTimeRanges:]_block_invoke
+ ___47-[MPNowPlayingSession updateMediaExperienceIDs]_block_invoke
+ ___49-[MPModelLibraryPlaylistEditController userImage]_block_invoke
+ ___50-[MPNowPlayingSession setPictureInPictureEnabled:]_block_invoke
+ ___53-[MPModelLibraryPlaylistEditController editSessionID]_block_invoke
+ ___53-[MPModelLibraryPlaylistEditController setUserImage:]_block_invoke
+ ___54-[MPModelLibraryPlaylistEditController parentPlaylist]_block_invoke
+ ___55-[MPModelLibraryPlaylistEditController descriptionText]_block_invoke
+ ___55-[MPModelLibraryPlaylistEditController isRedoAvailable]_block_invoke
+ ___55-[MPModelLibraryPlaylistEditController isUndoAvailable]_block_invoke
+ ___55-[MPVolumeHUDController setUpDeallocHandlerForDisplay:]_block_invoke
+ ___56-[MPModelLibraryPlaylistEditController _currentPlaylist]_block_invoke
+ ___56-[MPModelLibraryPlaylistEditController _currentPlaylist]_block_invoke_2
+ ___56-[MPModelLibraryPlaylistEditController initialTrackList]_block_invoke
+ ___56-[MPModelLibraryPlaylistEditController isPublicPlaylist]_block_invoke
+ ___56-[MPModelLibraryPlaylistEditController setPlaylistName:]_block_invoke
+ ___57-[MPModelLibraryPlaylistEditController _currentTrackList]_block_invoke
+ ___57-[MPModelLibraryPlaylistEditController isCuratorPlaylist]_block_invoke
+ ___57-[MPModelLibraryPlaylistEditController isVisiblePlaylist]_block_invoke
+ ___57-[MPModelLibraryPlaylistEditController setEditSessionID:]_block_invoke
+ ___57-[MPNowPlayingSession activePlayerDidChangeNotification:]_block_invoke
+ ___58-[MPModelLibraryPlaylistEditController coverArtworkRecipe]_block_invoke
+ ___58-[MPModelLibraryPlaylistEditController setParentPlaylist:]_block_invoke
+ ___58-[MPModelLibraryPlaylistEditController setPublicPlaylist:]_block_invoke
+ ___58-[MPNowPlayingSession setCurrentAssetNetCreditsStartTime:]_block_invoke
+ ___59-[MPModelLibraryPlaylistEditController setCuratorPlaylist:]_block_invoke
+ ___59-[MPModelLibraryPlaylistEditController setDescriptionText:]_block_invoke
+ ___59-[MPModelLibraryPlaylistEditController setVisiblePlaylist:]_block_invoke
+ ___59-[MPMusicPlayerController _wakeServerIfConnectedForReason:]_block_invoke
+ ___59-[MPMusicPlayerController _wakeServerIfConnectedForReason:]_block_invoke_2
+ ___59-[MPNowPlayingSession hasInvalidAdTimeRange:totalDuration:]_block_invoke
+ ___59-[MPNowPlayingSession initWithPlayerPath:routingContextID:]_block_invoke
+ ___60-[MPModelLibraryPlaylistEditController setInitialTrackList:]_block_invoke
+ ___60-[MPNowPlayingSession becomeActiveIfPossibleWithCompletion:]_block_invoke
+ ___60-[MPNowPlayingSession becomeActiveIfPossibleWithCompletion:]_block_invoke_2
+ ___62-[MPModelLibraryPlaylistEditController removePlaylistEntries:]_block_invoke
+ ___62-[MPModelLibraryPlaylistEditController setCoverArtworkRecipe:]_block_invoke
+ ___64-[MPModelLibraryPlaylistEditController applyChanges:completion:]_block_invoke
+ ___64-[MPModelLibraryPlaylistEditController removeAllPlaylistEntries]_block_invoke
+ ___65-[MPModelLibraryPlaylistEditController appendObjects:completion:]_block_invoke
+ ___65-[MPModelLibraryPlaylistEditController appendObjects:completion:]_block_invoke_2
+ ___68-[MPModelLibraryPlaylistEditController transactionsSinceIdentifier:]_block_invoke
+ ___68-[MPModelLibraryPlaylistEditController transactionsSinceIdentifier:]_block_invoke_2
+ ___68-[MPModelLibraryPlaylistEditController transactionsSinceIdentifier:]_block_invoke_3
+ ___69-[MPModelLibraryPlaylistEditController movePlaylistEntry:afterEntry:]_block_invoke
+ ___72-[MPModelLibraryPlaylistEditController insertObjectsAtStart:completion:]_block_invoke
+ ___72-[MPModelLibraryPlaylistEditController insertObjectsAtStart:completion:]_block_invoke_2
+ ___72-[MPNowPlayingSession extractNowPlayingInfoFromPlayersAndUpdateAdRanges]_block_invoke
+ ___74-[MPModelLibraryPlaylistEditController redoNextTransactionWithCompletion:]_block_invoke
+ ___74-[MPNowPlayingSession playerPictureInPictureEnabledDidChangeNotification:]_block_invoke
+ ___74-[MPNowPlayingSession playerPictureInPictureEnabledDidChangeNotification:]_block_invoke_2
+ ___76-[MPModelLibraryPlaylistEditController insertObjects:afterEntry:completion:]_block_invoke
+ ___76-[MPModelLibraryPlaylistEditController insertObjects:afterEntry:completion:]_block_invoke_2
+ ___77-[MPModelLibraryPlaylistEditController _insertObjects:afterEntry:completion:]_block_invoke
+ ___77-[MPModelLibraryPlaylistEditController _insertObjects:afterEntry:completion:]_block_invoke_2
+ ___78-[MPModelLibraryPlaylistEditController undoPreviousTransactionWithCompletion:]_block_invoke
+ ___79-[MPModelLibraryPlaylistEditController _applyChanges:toTransaction:completion:]_block_invoke
+ ___79-[MPModelLibraryPlaylistEditController _applyChanges:toTransaction:completion:]_block_invoke_2
+ ___79-[MPModelLibraryPlaylistEditController _applyChanges:toTransaction:completion:]_block_invoke_3
+ ___79-[MPModelLibraryPlaylistEditController _applyChanges:toTransaction:completion:]_block_invoke_4
+ ___79-[MPModelLibraryPlaylistEditController performTransactionWithIdentifier:block:]_block_invoke
+ ___95-[MPNowPlayingInfoCenter _getTransportablePlaybackSessionRepresentationWithRequest:completion:]_block_invoke
+ ___95-[MPNowPlayingInfoCenter _getTransportablePlaybackSessionRepresentationWithRequest:completion:]_block_invoke_2
+ ___95-[MPNowPlayingInfoCenter _getTransportablePlaybackSessionRepresentationWithRequest:completion:]_block_invoke_3
+ ___95-[MPNowPlayingInfoCenter _getTransportablePlaybackSessionRepresentationWithRequest:completion:]_block_invoke_4
+ ___99-[MPModelLibraryPlaylistEditController sectionedIdentifierList:dataSourceDidChangeItems:inSection:]_block_invoke
+ ___99-[MPModelLibraryPlaylistEditController sectionedIdentifierList:dataSourceDidChangeItems:inSection:]_block_invoke_2
+ ___99-[MPQueueFeederIdentifierRegistry applyChanges:identifierSetLookupBlock:itemIdentifierLookupBlock:]_block_invoke
+ ___99-[MPQueueFeederIdentifierRegistry applyChanges:identifierSetLookupBlock:itemIdentifierLookupBlock:]_block_invoke_2
+ ___99-[MPQueueFeederIdentifierRegistry applyChanges:identifierSetLookupBlock:itemIdentifierLookupBlock:]_block_invoke_3
+ ___99-[MPQueueFeederIdentifierRegistry applyChanges:identifierSetLookupBlock:itemIdentifierLookupBlock:]_block_invoke_4
+ ___99-[MPStoreModelRadioStationBuilder modelObjectWithStoreItemMetadata:sourceModelObject:userIdentity:]_block_invoke_6
+ ___99-[MPStoreModelRadioStationBuilder modelObjectWithStoreItemMetadata:sourceModelObject:userIdentity:]_block_invoke_7
+ ___MPBeginLoadingContentCallback_block_invoke.cold.1
+ ___MPContentItemsForIdentifiersCallback_block_invoke.cold.1
+ ___MPInitiatePlaybackCallback_block_invoke.cold.1
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80s88w_e71_v40?0"NSURLSessionDataTask"8"NSData"16"NSURLResponse"24"NSError"32ls32l8s40l8s48l8s56l8w88l8s64l8s72l8s80l8
+ ___block_descriptor_32_e18_"NSString"16?0q8l
+ ___block_descriptor_32_e41_q24?0"MPAdTimeRange"8"MPAdTimeRange"16l
+ ___block_descriptor_32_e55_v16?0"MPMusicPlayerControllerNowPlayingTimeSnapshot"8l
+ ___block_descriptor_40_e8_32bs_e66_v24?0"MPModelLibraryPlaylistEditTransactionDetails"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e25_v16?0"MPModelPlaylist"8ls32l8
+ ___block_descriptor_40_e8_32s_e47_v32?0"NSString"8"MPModelPlaylistEntry"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e18_B16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e23_v20?0B8^{__CFError=}12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e23_"MPArtworkCatalog"8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40bs48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_57_e8_32s40bs48w_e29_v24?0"NSArray"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_58_e8_32s40s48s_e14_"NSArray"8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32r_e30_v32?0"MPAdTimeRange"8Q16^B24lr32l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e12_v24?0Q8^B16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e30_v32?0"MPAdTimeRange"8Q16^B24lr48l8s32l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e30_v16?0"MPModelPlaylistEntry"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s_e30_v16?0"MPModelPlaylistEntry"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___nowPlayingSessionMap
+ __block_literal_global.117
+ __block_literal_global.123
+ __block_literal_global.125
+ __block_literal_global.156
+ __block_literal_global.161
+ __block_literal_global.228
+ __block_literal_global.288
+ __block_literal_global.290
+ __block_literal_global.496
+ __block_literal_global.510
+ __block_literal_global.518
+ __block_literal_global.526
+ __block_literal_global.528
+ __block_literal_global.542
+ __block_literal_global.550
+ __block_literal_global.564
+ __block_literal_global.566
+ __block_literal_global.571
+ __block_literal_global.573
+ __block_literal_global.581
+ __block_literal_global.591
+ __block_literal_global.593
+ __block_literal_global.594
+ __block_literal_global.604
+ __block_literal_global.621
+ __block_literal_global.623
+ __block_literal_global.628
+ __block_literal_global.630
+ __block_literal_global.641
+ __block_literal_global.643
+ __block_literal_global.657
+ __block_literal_global.680
+ __block_literal_global.688
+ __block_literal_global.696
+ __block_literal_global.710
+ __block_literal_global.715
+ __block_literal_global.720
+ __block_literal_global.722
+ __block_literal_global.724
+ __block_literal_global.732
+ __block_literal_global.740
+ __block_literal_global.745
+ __block_literal_global.753
+ __block_literal_global.758
+ __block_literal_global.763
+ __block_literal_global.765
+ __block_literal_global.782
+ __block_literal_global.784
+ __block_literal_global.804
+ __block_literal_global.806
+ __block_literal_global.811
+ __block_literal_global.818
+ __block_literal_global.820
+ __block_literal_global.822
+ __block_literal_global.830
+ __block_literal_global.835
+ __block_literal_global.843
+ __block_literal_global.845
+ __block_literal_global.853
+ __block_literal_global.96
+ __os_log_fault_impl
+ _dispatch_suspend
+ _kMRMediaRemoteActivePlayerDidChange
+ _kMRMediaRemoteCommandInfoPlaybackSessionRequirements
+ _kMRMediaRemoteOptionDelegateAccountData
+ _kMRMediaRemoteOptionDelegateAccountDataType
+ _kMRMediaRemotePlayerPictureInPictureDidChange
+ _objc_msgSend$_applyChanges:toTransaction:completion:
+ _objc_msgSend$_becomeActiveIfPossibleWithCompletion:
+ _objc_msgSend$_createTrackIdentifierListWithInitialEntries:initialObjects:completion:
+ _objc_msgSend$_currentPlaylist
+ _objc_msgSend$_currentTrackList
+ _objc_msgSend$_endTransactionCommittingChanges:
+ _objc_msgSend$_getTransportablePlaybackSessionRepresentationWithRequest:completion:
+ _objc_msgSend$_initWithIdentifier:referenceIdentifier:changes:
+ _objc_msgSend$_initWithLibrary:playlist:initialTrackList:initialItemList:playlistEntryProperties:authorProfile:
+ _objc_msgSend$_initWithType:itemIdentifier:
+ _objc_msgSend$_insertObjects:afterEntry:completion:
+ _objc_msgSend$_isLastEntry:
+ _objc_msgSend$_locked_reevaluateCanBeNowPlayingApplication
+ _objc_msgSend$_logEditorState
+ _objc_msgSend$_movePlaylistEntry:afterEntry:
+ _objc_msgSend$_removePlaylistEntries:
+ _objc_msgSend$_setPlaylistName:
+ _objc_msgSend$_startNewTransaction
+ _objc_msgSend$_startTransactionWithIdentifier:
+ _objc_msgSend$_wakeServerIfConnectedForReason:
+ _objc_msgSend$addBoundaryTimeObserverForTimes:queue:usingBlock:
+ _objc_msgSend$addChange:
+ _objc_msgSend$addChanges:
+ _objc_msgSend$addPlayerItemObservers:
+ _objc_msgSend$addPlayerObservers:
+ _objc_msgSend$appendObjects:completion:
+ _objc_msgSend$applyChanges:identifierSetLookupBlock:itemIdentifierLookupBlock:
+ _objc_msgSend$automaticallyPublishesNowPlayingInfo
+ _objc_msgSend$baseNowPlayingInfo
+ _objc_msgSend$canBeNowPlayingApplication
+ _objc_msgSend$changes
+ _objc_msgSend$changesApplied
+ _objc_msgSend$currentAdTimeRanges
+ _objc_msgSend$currentAssetNetCreditsStartTime
+ _objc_msgSend$currentAssetNetDuration
+ _objc_msgSend$currentDate
+ _objc_msgSend$destinationCommandInfo
+ _objc_msgSend$destinationPlayerPath
+ _objc_msgSend$editSessionID
+ _objc_msgSend$effectivePlaybackRateWithPlayer:
+ _objc_msgSend$enableRequestNotifications
+ _objc_msgSend$extractNowPlayingInfoFromPlayersAndUpdateAdRanges
+ _objc_msgSend$getProactiveRecommendedRouteWithTimeout:completion:
+ _objc_msgSend$hasInvalidAdTimeRange:totalDuration:
+ _objc_msgSend$importContainerArtworkForSagaID:artworkVariantType:completionHandler:
+ _objc_msgSend$initWithArtworkIdentifier:contentItemID:
+ _objc_msgSend$initWithIdentifier:referenceIdentifier:
+ _objc_msgSend$initWithLibrary:identifier:entityType:artworkType:mediaType:variantType:
+ _objc_msgSend$initWithPlayerPath:routingContextID:
+ _objc_msgSend$initWithType:
+ _objc_msgSend$initWithType:itemIdentifier:
+ _objc_msgSend$insertObjects:afterEntry:completion:
+ _objc_msgSend$insertObjectsAtStart:completion:
+ _objc_msgSend$isB465Route
+ _objc_msgSend$isDeletedItem:inSection:
+ _objc_msgSend$isLastItem
+ _objc_msgSend$itemPositionIdentifier
+ _objc_msgSend$loadArtworkForEntityPersistentID:entityType:artworkType:artworkSourceType:artworkVariantType:completionHandler:
+ _objc_msgSend$localResolvedPlayerPathFromPlayerPath:
+ _objc_msgSend$movePlaylistEntry:afterEntry:
+ _objc_msgSend$mxSessionIDKeyPath
+ _objc_msgSend$netTimeForGrossTime:
+ _objc_msgSend$newUniversalIdentifier
+ _objc_msgSend$nowPlayingSession:audioSessionDidChange:
+ _objc_msgSend$nowPlayingSessionDidChangeActive:
+ _objc_msgSend$nowPlayingSessionDidChangeCanBecomeActive:
+ _objc_msgSend$nowPlayingSessionForPlayerPath:
+ _objc_msgSend$performTransactionWithIdentifier:block:
+ _objc_msgSend$playerSet
+ _objc_msgSend$players
+ _objc_msgSend$playlistEntries
+ _objc_msgSend$playlistName
+ _objc_msgSend$portraitArtworkCatalogBlock
+ _objc_msgSend$previousPlaylistName
+ _objc_msgSend$previousPositionIdentifier
+ _objc_msgSend$previousReferenceIdentifier
+ _objc_msgSend$privateQueue
+ _objc_msgSend$referenceItem
+ _objc_msgSend$referenceItemPositionIdentifier
+ _objc_msgSend$removeDeallocHandlerFromDisplay:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$removeObserver:forKeyPath:
+ _objc_msgSend$removePlayerItemObservers:
+ _objc_msgSend$removePlayerObservers:
+ _objc_msgSend$removePlaylistEntries:
+ _objc_msgSend$removePlaylistEntry:
+ _objc_msgSend$requestContextTag
+ _objc_msgSend$requestWithMediaRemoteRequest:
+ _objc_msgSend$routingContextID
+ _objc_msgSend$searchEndpointsForRoutingContextUID:timeout:reason:queue:completion:
+ _objc_msgSend$seekForwardCommand
+ _objc_msgSend$setAdTimeRangesEndObserverToken:
+ _objc_msgSend$setAdTimeRangesStartObserverToken:
+ _objc_msgSend$setBaseNowPlayingInfo:
+ _objc_msgSend$setCanBecomeActive:
+ _objc_msgSend$setChanges:
+ _objc_msgSend$setChangesApplied:
+ _objc_msgSend$setCreditsTimeObserverToken:
+ _objc_msgSend$setCurrentAdTimeRanges:
+ _objc_msgSend$setCurrentAssetNetCreditsStartTime:
+ _objc_msgSend$setCurrentAssetNetDuration:
+ _objc_msgSend$setDisabledReason:
+ _objc_msgSend$setEditSessionID:
+ _objc_msgSend$setForceDisabled:
+ _objc_msgSend$setIsLastItem:
+ _objc_msgSend$setItem:
+ _objc_msgSend$setItemPositionIdentifier:
+ _objc_msgSend$setNowPlayingInfo:
+ _objc_msgSend$setPlaylistName:
+ _objc_msgSend$setPreviousPlaylistName:
+ _objc_msgSend$setPreviousPositionIdentifier:
+ _objc_msgSend$setPreviousReferenceIdentifier:
+ _objc_msgSend$setReferenceItem:
+ _objc_msgSend$setReferenceItemIdentifier:
+ _objc_msgSend$setReferenceItemPositionIdentifier:
+ _objc_msgSend$setSubtitleShort:
+ _objc_msgSend$setTag:
+ _objc_msgSend$setUpDeallocHandlerForDisplay:
+ _objc_msgSend$sizesToAutogenerateForMediaType:artworkType:artworkVariantType:
+ _objc_msgSend$specialSeekForwardCommand
+ _objc_msgSend$subtitleShort
+ _objc_msgSend$supportedSizesForMediaType:artworkType:artworkVariantType:
+ _objc_msgSend$timeControlStatus
+ _objc_msgSend$timeRange
+ _objc_msgSend$updateMediaExperienceIDs
+ _objc_msgSend$updateNowPlayingInfo
+ _objc_msgSend$variantType
+ _objc_retain_x7
+ initWithPlayerPath:routingContextID:.onceToken
- +[_MPNowPlayingInfoTransportableSessionRequest requestWithIdentifier:preferredSessionType:]
- -[MPModelLibraryPlaylistEditController _createTrackIdentifierListWithInitialEntries:completion:]
- -[MPModelLibraryPlaylistEditController _initWithLibrary:playlist:initialTrackList:playlistEntryProperties:authorProfile:]
- -[MPNowPlayingInfoCenter _getTransportablePlaybackSessionRepresentationWithIdentifier:preferredSessionType:completion:]
- -[MPRemoteCommandCenter _locked_updateCanBeNowPlayingApplicationIfNeeded]
- GCC_except_table113
- GCC_except_table126
- GCC_except_table150
- GCC_except_table151
- GCC_except_table165
- GCC_except_table166
- GCC_except_table187
- GCC_except_table58
- GCC_except_table92
- GCC_except_table99
- OBJC_IVAR_$_MPModelLibraryPlaylistEditController._lock
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCSS_ypTgm5
- _$sSS3key_yp5valuetML
- _$sSS3key_yp5valuetMa
- _$sSS3key_yp5valuetSgML
- _$sSS3key_yp5valuetSgMa
- _$sSS3key_yp5valuetSgWOb
- _MPChangeDetailOperationMaximumElementCount
- _MRPlaybackSessionRequestCopyIdentifier
- _MRPlaybackSessionRequestCopyType
- _MSVDeviceIsHomePod
- __36-[MPMusicPlayerController onServer:]_block_invoke.140
- __36-[MPMusicPlayerController onServer:]_block_invoke.141
- __42-[MPMusicPlayerController _validateServer]_block_invoke.137
- __47-[MPAVRoutingControllerSelectionQueue _dequeue]_block_invoke.453
- __48-[MPAVRoutingControllerSelectionQueue _enqueue:]_block_invoke.448
- __48-[MPAVRoutingControllerSelectionQueue _enqueue:]_block_invoke.452
- __48-[MPPlaybackUserDefaults _loadAccountProperties]_block_invoke.311
- __56-[MPAVRoutingControllerSelectionQueue addPendingRoutes:]_block_invoke.440
- __56-[MPModelLibraryPlaylistEditController currentTrackList]_block_invoke.16
- __62-[MPModelLibraryPlaylistEditDataSource _reloadWithCompletion:]_block_invoke.27
- __62-[MPModelLibraryPlaylistEditDataSource _reloadWithCompletion:]_block_invoke.32
- __62-[MPModelLibraryPlaylistEditDataSource _reloadWithCompletion:]_block_invoke_2.34
- __69-[MPAVRoutingControllerSelectionQueue removePendingRoutes:withError:]_block_invoke.444
- __70-[MPMusicPlayerController prepareToPlayWithCompletionHandler:timeout:]_block_invoke.83
- __70-[MPMusicPlayerController prepareToPlayWithCompletionHandler:timeout:]_block_invoke.84
- __70-[MPMusicPlayerController prepareToPlayWithCompletionHandler:timeout:]_block_invoke.87
- __70-[MPMusicPlayerController prepareToPlayWithCompletionHandler:timeout:]_block_invoke.88
- __73-[MPAVRoutingControllerSelectionQueue cancelInProgressSelectionForRoute:]_block_invoke.437
- __75-[MPMusicPlayerController onServerAsync:errorHandler:timeout:retryEnabled:]_block_invoke.144
- __75-[MPMusicPlayerController onServerAsync:errorHandler:timeout:retryEnabled:]_block_invoke.148
- __75-[MPMusicPlayerController onServerAsync:errorHandler:timeout:retryEnabled:]_block_invoke.150
- __76-[MPNowPlayingInfoCenter _invalidatePlaybackQueueImmediatelyWithCompletion:]_block_invoke.100
- __80-[MPAbstractNetworkArtworkDataSource _bestVideoArtworkRepresentationForCatalog:]_block_invoke.224
- __81-[MPNowPlayingInfoCenter _onDataSourceQueue_getContentItemIDsInRange:completion:]_block_invoke.109
- __99-[MPAbstractNetworkArtworkDataSource loadRepresentationOfKind:forArtworkCatalog:completionHandler:]_block_invoke.162
- __99-[MPAbstractNetworkArtworkDataSource loadRepresentationOfKind:forArtworkCatalog:completionHandler:]_block_invoke.188
- __OBJC_$_INSTANCE_METHODS_AVPlayerItem(MPAVItemAdditions|MPNowPlayingInfoLanguageOptionAdditions)
- __OBJC_$_PROP_LIST_AVPlayerItem_$_MPAVItemAdditions
- __ZNKSt3__16vectorIU8__strongP13ITMediaEntityNS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIlNS_9allocatorIlEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt12out_of_rangeC1B8ne180100EPKc
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIxU6__weakPU41objcproto30MPCacheableConcreteMediaEntity13MPMediaEntityEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne180100EPS9_
- __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE28__node_insert_unique_performB8ne180100EPNS_11__hash_nodeIyPvEE
- __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE28__node_insert_unique_prepareB8ne180100EmRy
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIU8__strongP13ITMediaEntityEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIlEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIxEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne180100EPKc
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP11ITMediaItemEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP12ITMediaAlbumEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP12ITMediaGenreEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP13ITMediaArtistEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP15ITMediaComposerEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP15ITMediaPlaylistEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP17ITMediaCollectionEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyU8__strongP18ITMediaAlbumArtistEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__124__sort5_maybe_branchlessB8ne180100INS_17_ClassicAlgPolicyERZ43-[ITMediaLibraryQueryResultSet sortResults]E3$_0PU8__strongP13ITMediaEntityLi0EEEvT1_S8_S8_S8_S8_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZ43-[ITMediaLibraryQueryResultSet sortResults]E3$_0PU8__strongP13ITMediaEntityEEbT1_S8_T0_
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__16vectorIU8__strongP13ITMediaEntityNS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIxNS_9allocatorIxEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIxNS_9allocatorIxEEE16__init_with_sizeB8ne180100IPxS5_EEvT_T0_m
- __ZNSt3__16vectorIxNS_9allocatorIxEEE18__assign_with_sizeB8ne180100IPxS5_EEvT_T0_l
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZ43-[ITMediaLibraryQueryResultSet sortResults]E3$_0PU8__strongP13ITMediaEntityEEjT1_S8_S8_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZ43-[ITMediaLibraryQueryResultSet sortResults]E3$_0PU8__strongP13ITMediaEntityEEvT1_S8_S8_S8_T0_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___113-[MPCloudController loadArtworkForEntityPersistentID:entityType:artworkType:artworkSourceType:completionHandler:]_block_invoke
- ___113-[MPCloudController loadArtworkForEntityPersistentID:entityType:artworkType:artworkSourceType:completionHandler:]_block_invoke_2
- ___119-[MPNowPlayingInfoCenter _getTransportablePlaybackSessionRepresentationWithIdentifier:preferredSessionType:completion:]_block_invoke
- ___119-[MPNowPlayingInfoCenter _getTransportablePlaybackSessionRepresentationWithIdentifier:preferredSessionType:completion:]_block_invoke_2
- ___119-[MPNowPlayingInfoCenter _getTransportablePlaybackSessionRepresentationWithIdentifier:preferredSessionType:completion:]_block_invoke_3
- ___119-[MPNowPlayingInfoCenter _getTransportablePlaybackSessionRepresentationWithIdentifier:preferredSessionType:completion:]_block_invoke_4
- ___56-[MPModelLibraryPlaylistEditController currentTrackList]_block_invoke_2
- ___64-[MPNowPlayingInfoCenter _getMetadataForContentItem:completion:]_block_invoke_2
- ___73-[MPQueueFeederIdentifierRegistry applyChanges:identifierSetLookupBlock:]_block_invoke_2
- ___73-[MPQueueFeederIdentifierRegistry applyChanges:identifierSetLookupBlock:]_block_invoke_3
- ___73-[MPQueueFeederIdentifierRegistry applyChanges:identifierSetLookupBlock:]_block_invoke_4
- ___73-[MPRemoteCommandCenter _locked_updateCanBeNowPlayingApplicationIfNeeded]_block_invoke
- ___96-[MPModelLibraryPlaylistEditController _createTrackIdentifierListWithInitialEntries:completion:]_block_invoke
- ___block_descriptor_40_e8_32s_e63_v32?0"NSString"8"MPModelLibraryPlaylistEditDataSource"16^B24ls32l8
- ___block_descriptor_48_e8_32w40w_e23_"MPArtworkCatalog"8?0lw32l8w40l8
- ___block_descriptor_56_e8_32s40s48bs_e12_v24?0Q8^B16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48r_e22_v24?0"NSString"8^B16ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s_e30_v16?0"MPModelPlaylistEntry"8ls32l8s40l8
- ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_97_e8_32s40s48s56s64s72w_e71_v40?0"NSURLSessionDataTask"8"NSData"16"NSURLResponse"24"NSError"32ls32l8s40l8w72l8s48l8s56l8s64l8
- __block_literal_global.136
- __block_literal_global.224
- __block_literal_global.248
- __block_literal_global.250
- __block_literal_global.292
- __block_literal_global.294
- __block_literal_global.490
- __block_literal_global.504
- __block_literal_global.512
- __block_literal_global.520
- __block_literal_global.522
- __block_literal_global.536
- __block_literal_global.544
- __block_literal_global.558
- __block_literal_global.560
- __block_literal_global.565
- __block_literal_global.567
- __block_literal_global.575
- __block_literal_global.585
- __block_literal_global.587
- __block_literal_global.588
- __block_literal_global.598
- __block_literal_global.615
- __block_literal_global.617
- __block_literal_global.622
- __block_literal_global.624
- __block_literal_global.635
- __block_literal_global.637
- __block_literal_global.651
- __block_literal_global.674
- __block_literal_global.682
- __block_literal_global.704
- __block_literal_global.709
- __block_literal_global.714
- __block_literal_global.716
- __block_literal_global.718
- __block_literal_global.726
- __block_literal_global.734
- __block_literal_global.739
- __block_literal_global.747
- __block_literal_global.752
- __block_literal_global.757
- __block_literal_global.759
- __block_literal_global.776
- __block_literal_global.778
- __block_literal_global.798
- __block_literal_global.800
- __block_literal_global.805
- __block_literal_global.810
- __block_literal_global.812
- __block_literal_global.814
- __block_literal_global.824
- __block_literal_global.829
- __block_literal_global.837
- __block_literal_global.839
- __block_literal_global.847
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_MediaPlayer
- _fmod
- _objc_msgSend$_createTrackIdentifierListWithInitialEntries:completion:
- _objc_msgSend$_getTransportablePlaybackSessionRepresentationWithIdentifier:preferredSessionType:completion:
- _objc_msgSend$_initWithLibrary:playlist:initialTrackList:playlistEntryProperties:authorProfile:
- _objc_msgSend$_locked_updateCanBeNowPlayingApplicationIfNeeded
- _objc_msgSend$importContainerArtworkForSagaID:completionHandler:
- _objc_msgSend$requestWithIdentifier:preferredSessionType:
- _objc_msgSend$sizesToAutogenerateForMediaType:artworkType:
- _objc_msgSend$supportedSizesForMediaType:artworkType:
- _objc_retain_x10
CStrings:
+ "%{public}@ ADD failed to find the reference item in change %{public}@"
+ "%{public}@ Applied changes: %{public}@"
+ "%{public}@ Applying change %{public}@"
+ "%{public}@ Applying changes to undo previous change: %{public}@"
+ "%{public}@ Applying changes: %{public}@"
+ "%{public}@ Attempting to undo unexpected change: %{public}@"
+ "%{public}@ Calling completion with loaded representation: %{public}@ and error: %{public}@ for request: %{public}@"
+ "%{public}@ Created data task: %{public}@ for request: %{public}@"
+ "%{public}@ Encountered error while requesting artwork for NSURLSessionDataTask: %{public}@. %{public}@ for request: %{public}@"
+ "%{public}@ Ending transaction %{public}@"
+ "%{public}@ Failed to apply change %{public}@. err=%{public}@"
+ "%{public}@ Failed to apply incoming changes. err=%{public}@"
+ "%{public}@ Failed to redo. err=%{public}@"
+ "%{public}@ Failed to undo previous change. err=%{public}@"
+ "%{public}@ Finished append items"
+ "%{public}@ Finished append items error=%{public}@"
+ "%{public}@ Finished inserting items"
+ "%{public}@ Finished inserting items error=%{public}@"
+ "%{public}@ Finished prepending items"
+ "%{public}@ Finished prepending items error=%{public}@"
+ "%{public}@ Getting best fit for artwork of type %d, (%f x %f) in %@"
+ "%{public}@ Loaded image representation: %{public}@ with URLSessionDataTask: %{public}@ for request: %{public}@. It took %f seconds to complete"
+ "%{public}@ MOVE failed to find the item in change %{public}@"
+ "%{public}@ MOVE failed to find the reference item in change %{public}@"
+ "%{public}@ REMOVE failed to find the reference item in change %{public}@"
+ "%{public}@ Redoing transaction: %{public}@"
+ "%{public}@ Returning %lu transactions since '%{public}@': %{public}@"
+ "%{public}@ Starting new transaction %{public}@"
+ "%{public}@ Successfully completed move"
+ "%{public}@ Successfully completed remove"
+ "%{public}@ Successfully performed redo of transaction %{public}@"
+ "%{public}@ Successfully performed undo of %{public}@ producing transaction %{public}@"
+ "%{public}@ Summary:\nTrack List:\n%{public}@\nChanges (--> [%ld]): %{public}@"
+ "%{public}@ Undoing transaction: %{public}@"
+ "%{public}@ encountered unexpected NSURLResponse: %{public}@ for request: %{public}@"
+ "%{public}@ found exact fit for artwork of type %d. size (%f x %f)"
+ "%{public}@ no exact fit for artwork of type %d, size (%f x %f). using best size (%fx%f)"
+ "%{public}@ redo called when not available - ignoring"
+ "%{public}@ undo called when not available - ignoring"
+ "(%p %@; posID %@)"
+ "-[MPNowPlayingSession setAutomaticallyPublishesNowPlayingInfo:]"
+ "76,8229"
+ "<%@ %p: %@=%@>"
+ "<%@ %p: [%@] %@>"
+ "<%@ %p: [%@]>"
+ "<%@: %p - %@> %s %d"
+ "<%@: %p - %@> invalidated"
+ "<%@: %p status=%@ dialog=%@ error=%@>"
+ "<%@: %p> _playerItemNowPlayingInfoDidChange"
+ "<%@: %p> effective playback rate 0 due to ad"
+ "<%@: %p> effective playback rate 0 due to non-playing time control"
+ "<%@: %p> enter ad break end boundary time observer block"
+ "<%@: %p> enter ad break start boundary time observer block"
+ "<%@: %p> enter credits boundary time observer block"
+ "<%@: %p> exit ad break end boundary time observer block"
+ "<%@: %p> exit ad break start boundary time observer block"
+ "<%@: %p> exit credits boundary time observer block"
+ "<%@: %p> player has no player item: %@"
+ "<%@: %p> player item has no nowPlayingInfo dictionary: %@"
+ "<%@: %p> playerItemDidPlayToEnd"
+ "<%@: %p> playerItemPlaybackStalled"
+ "<%@: %p> playerItemTimeJumped"
+ "<%@: %p> playerRateDidChange"
+ "<%@:%p libraryID=%llu entityType=%@ artworkType=%@ variantType=%@"
+ "@\"<MPNowPlayingSessionDelegate>\""
+ "@\"AVAudioSession\""
+ "@\"MPModelLibraryPlaylistEditTransactionDetails\""
+ "@\"MPNowPlayingInfoCenter\""
+ "@\"MRPlayerPath\"16@0:8"
+ "@\"NSArray\"8@?0"
+ "@40@0:8Q16q24q32"
+ "@64@0:8@16@24@32@40@48@56"
+ "@64@0:8@16Q24q32q40Q48q56"
+ "@64@0:8{?={?=qiIq}{?=qiIq}}16"
+ "ADD <%@ %p [%@ / %@]> AFTER <%@ %p [%@ / %@]>"
+ "Add"
+ "Already have a transaction started"
+ "Already have a transaction started!"
+ "B16@?0@\"NSString\"8"
+ "CC"
+ "Cannot have two MPNowPlayingSession for the same playerPath: %@"
+ "Failed to update MXSessionIDs: %{public}@ for player path: %{public}@. Error: %{public}@"
+ "MOVE <%@ %p [%@ / %@ --> %@]> AFTER <%@ %p [%@ / %@]>"
+ "MPAdTimeRange"
+ "MPDelegateAccountCommandEvent"
+ "MPModelLibraryPlaylistEditChangeDetails"
+ "MPModelLibraryPlaylistEditErrorDomain"
+ "MPModelLibraryPlaylistEditTransactionDetails"
+ "MPModelPropertyPlaylistEditSessionID"
+ "MPModelPropertyPlaylistPortraitArtwork"
+ "MPModelPropertyPodcastEpisodeSubtitle"
+ "MPModelPropertyPodcastEpisodeSubtitleShort"
+ "MPModelPropertyRadioStationEditorialArtwork"
+ "MPNowPlayingSession"
+ "MPNowPlayingSession must be initialized with one or more AVPlayer instances."
+ "MPNowPlayingSession.endpointWithCompletion"
+ "MPNowPlayingSession.m"
+ "MPPlayerItemNowPlayingInfoDidChangeNotification"
+ "Move"
+ "No current transaction to end"
+ "No initial data source with identifier %@"
+ "PROPERTY (name='%@')"
+ "Property"
+ "REMOVE <%@ %p> %@"
+ "REMOVE ALL (%lu items)"
+ "Remove"
+ "RemoveAll"
+ "RuntimeIssues"
+ "T@\"<MPNowPlayingSessionDelegate>\",W,N,V_delegate"
+ "T@\"AVAudioSession\",R,N"
+ "T@\"MPModelObject\",&,N,V_item"
+ "T@\"MPModelObject\",&,N,V_referenceItem"
+ "T@\"MPNowPlayingInfoCenter\",&,N,V_nowPlayingInfoCenter"
+ "T@\"MPRemoteCommand\",R,N,V_delegateAccountCommand"
+ "T@\"MPRemoteCommandCenter\",R,N,V_remoteCommandCenter"
+ "T@\"MRPlayerPath\",R,N"
+ "T@\"MRPlayerPath\",R,N,V_destinationPlayerPath"
+ "T@\"NSArray\",&,N,V_currentAdTimeRanges"
+ "T@\"NSArray\",C,N,V_changes"
+ "T@\"NSArray\",C,N,V_changesApplied"
+ "T@\"NSData\",R,N,V_delegateAccountData"
+ "T@\"NSDictionary\",&,N,V_baseNowPlayingInfo"
+ "T@\"NSDictionary\",C,N,V_requirements"
+ "T@\"NSDictionary\",R,N,V_destinationCommandInfo"
+ "T@\"NSMutableSet\",&,N,V_playerSet"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_privateQueue"
+ "T@\"NSSet\",R,N,V_mxSessionIDs"
+ "T@\"NSString\",C,N,V_itemIdentifier"
+ "T@\"NSString\",C,N,V_itemPositionIdentifier"
+ "T@\"NSString\",C,N,V_playlistName"
+ "T@\"NSString\",C,N,V_previousPlaylistName"
+ "T@\"NSString\",C,N,V_previousPositionIdentifier"
+ "T@\"NSString\",C,N,V_previousReferenceIdentifier"
+ "T@\"NSString\",C,N,V_referenceItemIdentifier"
+ "T@\"NSString\",C,N,V_referenceItemPositionIdentifier"
+ "T@\"NSString\",R,C,N,V_referenceIdentifier"
+ "T@\"NSString\",R,N,V_delegateAccountDataType"
+ "T@\"NSString\",R,N,V_routingContextID"
+ "T@,&,N,V_adTimeRangesEndObserverToken"
+ "T@,&,N,V_adTimeRangesStartObserverToken"
+ "T@,&,N,V_creditsTimeObserverToken"
+ "T@,&,N,V_requestContextTag"
+ "TB,N,GisPictureInPictureEnabled,V_pictureInPictureEnabled"
+ "TB,N,V_automaticallyPublishesNowPlayingInfo"
+ "TB,N,V_canBecomeActive"
+ "TB,N,V_isLastItem"
+ "TB,R,N,GisB465Route"
+ "TB,R,N,GisRedoAvailable"
+ "TB,R,N,GisUndoAvailable"
+ "TQ,N,V_maxUndoLimit"
+ "Td,N,V_currentAssetNetCreditsStartTime"
+ "Td,N,V_currentAssetNetDuration"
+ "Tq,R,N,V_variantType"
+ "Translator was missing mapping for MPModelPropertyPlaylistEditSessionID"
+ "Translator was missing mapping for MPModelPropertyPlaylistPortraitArtwork"
+ "Translator was missing mapping for MPModelPropertyPodcastEpisodeSubtitle"
+ "Translator was missing mapping for MPModelPropertyPodcastEpisodeSubtitleShort"
+ "Translator was missing mapping for MPModelPropertyRadioStationEditorialArtwork"
+ "T{?={?=qiIq}{?=qiIq}},N,V_timeRange"
+ "Unknown Type"
+ "Unknown change type in change %@"
+ "WARNING: using MPNowPlayingInfoCenter is unsupported when using automatic publishing."
+ "Wake server reason:%{public}@"
+ "[RCC] reevaluateCanBeNowPlayingApplication: canBeNowPlayingApplication=%{BOOL}u playerPath=%{public}@ commands=%{public}@"
+ "_DeallocHandlerGuardKey"
+ "_MPMusicPlayerControllerArtworkToken"
+ "__MPModelPropertyPlaylistEditSessionID__MAPPING_MISSING__"
+ "__MPModelPropertyPlaylistPortraitArtwork__MAPPING_MISSING__"
+ "__MPModelPropertyPodcastEpisodeSubtitleShort__MAPPING_MISSING__"
+ "__MPModelPropertyPodcastEpisodeSubtitle__MAPPING_MISSING__"
+ "__MPModelPropertyRadioStationEditorialArtwork__MAPPING_MISSING__"
+ "__editSessionID_KEY"
+ "__portraitArtworkCatalogBlock_KEY"
+ "__subtitleShort_KEY"
+ "__subtitle_KEY"
+ "_adTimeRangesEndObserverToken"
+ "_adTimeRangesStartObserverToken"
+ "_applyChanges:toTransaction:completion:"
+ "_audioSession"
+ "_automaticallyPublishesNowPlayingInfo"
+ "_baseNowPlayingInfo"
+ "_canBecomeActive"
+ "_changes"
+ "_changesApplied"
+ "_completedTransactions"
+ "_createTrackIdentifierListWithInitialEntries:initialObjects:completion:"
+ "_creditsTimeObserverToken"
+ "_currentAdTimeRanges"
+ "_currentAssetNetCreditsStartTime"
+ "_currentAssetNetDuration"
+ "_currentLastItemIdentifier"
+ "_currentPlaylist"
+ "_currentTrackList"
+ "_currentTransaction"
+ "_delegateAccountCommand"
+ "_delegateAccountData"
+ "_delegateAccountDataType"
+ "_descriptionForType:"
+ "_destinationCommandInfo"
+ "_destinationPlayerPath"
+ "_editSessionID"
+ "_endTransactionCommittingChanges:"
+ "_getTransportablePlaybackSessionRepresentationWithRequest:completion:"
+ "_handleMediaServicesLost:"
+ "_handleMediaServicesReset:"
+ "_initWithIdentifier:referenceIdentifier:changes:"
+ "_initWithLibrary:playlist:initialTrackList:initialItemList:playlistEntryProperties:authorProfile:"
+ "_initWithType:itemIdentifier:"
+ "_initialTrackObjectList"
+ "_insertObjects:afterEntry:completion:"
+ "_isLastEntry:"
+ "_isLastItem"
+ "_itemIdentifierToPositionIdentifierMap"
+ "_itemPositionIdentifier"
+ "_lastAppliedTransactionIndex"
+ "_locked_reevaluateCanBeNowPlayingApplication"
+ "_logEditorState"
+ "_maxUndoLimit"
+ "_mediaServiceLost"
+ "_movePlaylistEntry:afterEntry:"
+ "_mxSessionIDs"
+ "_notificationsSuspended"
+ "_nowPlayingInfoCenter"
+ "_pictureInPictureEnabled"
+ "_playerItemNowPlayingInfoDidChange:"
+ "_playerSet"
+ "_playlistName"
+ "_positionIdentifierToItemIdentifierMap"
+ "_previousPlaylistName"
+ "_previousPositionIdentifier"
+ "_previousReferenceIdentifier"
+ "_privateQueue"
+ "_referenceIdentifier"
+ "_referenceItem"
+ "_referenceItemIdentifier"
+ "_referenceItemPositionIdentifier"
+ "_remoteCommandCenter"
+ "_removePlaylistEntries:"
+ "_requestContextTag"
+ "_requestNotificationsEnabled"
+ "_requirements"
+ "_routingContextID"
+ "_setPlaylistName:"
+ "_startNewTransaction"
+ "_startTransactionWithIdentifier:"
+ "_timeRange"
+ "_variantType"
+ "_wakeServerIfConnectedForReason:"
+ "activePlayerDidChangeNotification:"
+ "adTimeRangesEndObserverToken"
+ "adTimeRangesStartObserverToken"
+ "addBoundaryTimeObserverForTimes:queue:usingBlock:"
+ "addChange:"
+ "addChanges:"
+ "addPlayer:"
+ "addPlayerItemObservers:"
+ "addPlayerObservers:"
+ "appendObject:completion:"
+ "appendObjects:completion:"
+ "applyChanges:completion:"
+ "applyChanges:identifierSetLookupBlock:itemIdentifierLookupBlock:"
+ "attributes.editorialArtwork.backgroundStatic1x1"
+ "audioSession"
+ "automaticallyPublishesNowPlayingInfo"
+ "avt"
+ "b465Route"
+ "backgroundStatic1x1"
+ "baseNowPlayingInfo"
+ "becomeActiveIfPossibleWithCompletion:"
+ "canBecomeActive"
+ "changes"
+ "changesApplied"
+ "com.apple.MediaPlayer.MPModelLibraryPlaylistEditController.accessQueue"
+ "creditsTimeObserverToken"
+ "currentAdTimeRanges"
+ "currentAssetNetCreditsStartTime"
+ "currentAssetNetDuration"
+ "currentDate"
+ "delegateAccountCommand"
+ "delegateAccountData"
+ "delegateAccountDataType"
+ "destinationCommandInfo"
+ "destinationPlayerPath"
+ "editSessionID"
+ "effectivePlaybackRateWithPlayer:"
+ "enableRequestNotifications"
+ "endpointWithCompletion:"
+ "extractNowPlayingInfoFromPlayersAndUpdateAdRanges"
+ "f24@0:8@16"
+ "getProactiveRecommendedRouteWithCompletion:"
+ "getProactiveRecommendedRouteWithTimeout:completion:"
+ "hasInvalidAdTimeRange:totalDuration:"
+ "home:didUpdateActionSet:isExecuting:"
+ "importContainerArtworkForSagaID:artworkVariantType:completionHandler:"
+ "initWithArtworkIdentifier:contentItemID:"
+ "initWithIdentifier:changes:"
+ "initWithIdentifier:referenceIdentifier:"
+ "initWithLibrary:identifier:entityType:artworkType:mediaType:variantType:"
+ "initWithLibrary:initialItemList:playlistEntryProperties:authorProfile:"
+ "initWithPlayerPath:routingContextID:"
+ "initWithPlayers:"
+ "initWithTimeRange:"
+ "initWithType:itemIdentifier:"
+ "initialTrackList"
+ "insertObject:afterEntry:completion:"
+ "insertObjectAtStart:completion:"
+ "insertObjects:afterEntry:completion:"
+ "insertObjectsAtStart:completion:"
+ "isB465Route"
+ "isLastItem"
+ "isPictureInPictureEnabled"
+ "isRedoAvailable"
+ "isUndoAvailable"
+ "itemPositionIdentifier"
+ "loadArtworkForEntityPersistentID:entityType:artworkType:artworkSourceType:artworkVariantType:completionHandler:"
+ "localResolvedPlayerPathFromPlayerPath:"
+ "maxUndoLimit"
+ "mediaExperienceIDs"
+ "motion"
+ "motionPreviewFrame"
+ "movePlaylistEntry:afterEntry:"
+ "movePlaylistEntryToStart:"
+ "mxSessionID"
+ "mxSessionIDKeyPath"
+ "mxSessionIDs"
+ "netTimeForGrossTime:"
+ "newUniversalIdentifier"
+ "nowPlayingInfoCenter"
+ "nowPlayingSession:audioSessionDidChange:"
+ "nowPlayingSessionDidChangeActive:"
+ "nowPlayingSessionDidChangeCanBecomeActive:"
+ "nowPlayingSessionForPlayerID:"
+ "nowPlayingSessionForPlayerPath:"
+ "performTransactionWithIdentifier:block:"
+ "pictureInPictureEnabled"
+ "playerItemDidPlayToEnd:"
+ "playerItemPlaybackStalled:"
+ "playerItemTimeJumped:"
+ "playerPictureInPictureEnabledDidChangeNotification:"
+ "playerRateDidChange:"
+ "playerSet"
+ "players"
+ "portrait"
+ "portraitArtworkCatalog"
+ "portraitArtworkCatalogBlock"
+ "portraitMotion"
+ "previousPlaylistName"
+ "previousPositionIdentifier"
+ "previousReferenceIdentifier"
+ "privateQueue"
+ "q24@?0@\"MPAdTimeRange\"8@\"MPAdTimeRange\"16"
+ "recommendationId"
+ "redo called when not available"
+ "redoAvailable"
+ "redoNextTransactionWithCompletion:"
+ "referenceIdentifier"
+ "referenceItem"
+ "referenceItemIdentifier"
+ "referenceItemPositionIdentifier"
+ "remoteCommandCenter"
+ "removeAllPlaylistEntries"
+ "removeDeallocHandlerFromDisplay:"
+ "removeObjectsForKeys:"
+ "removeObserver:forKeyPath:"
+ "removePlayer:"
+ "removePlayerItemObservers:"
+ "removePlayerObservers:"
+ "removePlaylistEntries:"
+ "removePlaylistEntry:"
+ "requestContextTag"
+ "requestWithMediaRemoteRequest:"
+ "requirements"
+ "routingContextID"
+ "searchEndpointsForRoutingContextUID:timeout:reason:queue:completion:"
+ "setAdTimeRangesEndObserverToken:"
+ "setAdTimeRangesStartObserverToken:"
+ "setAutomaticallyPublishesNowPlayingInfo:"
+ "setBaseNowPlayingInfo:"
+ "setCanBecomeActive:"
+ "setChanges:"
+ "setChangesApplied:"
+ "setCreditsTimeObserverToken:"
+ "setCurrentAdTimeRanges:"
+ "setCurrentAssetNetCreditsStartTime:"
+ "setCurrentAssetNetDuration:"
+ "setEditSessionID:"
+ "setIsLastItem:"
+ "setItem:"
+ "setItemIdentifier:"
+ "setItemPositionIdentifier:"
+ "setMaxUndoLimit:"
+ "setNowPlayingInfoCenter:"
+ "setPictureInPictureEnabled:"
+ "setPlayerSet:"
+ "setPlaylistName:"
+ "setPreviousPlaylistName:"
+ "setPreviousPositionIdentifier:"
+ "setPreviousReferenceIdentifier:"
+ "setPrivateQueue:"
+ "setReferenceItem:"
+ "setReferenceItemIdentifier:"
+ "setReferenceItemPositionIdentifier:"
+ "setRequestContextTag:"
+ "setRequirements:"
+ "setSubtitleShort:"
+ "setTag:"
+ "setTimeRange:"
+ "setUpDeallocHandlerForDisplay:"
+ "sizesToAutogenerateForMediaType:artworkType:artworkVariantType:"
+ "subtitleShort"
+ "supportedSizesForMediaType:artworkType:artworkVariantType:"
+ "timeControlStatus"
+ "timeRange"
+ "transactionsSinceIdentifier called while there is an open transaction"
+ "transactionsSinceIdentifier:"
+ "undo called when not available"
+ "undoAvailable"
+ "undoPreviousTransactionWithCompletion:"
+ "updateAudioSession:"
+ "updateMediaExperienceIDs"
+ "updateNowPlayingInfo"
+ "v20@?0B8^{__CFError=}12"
+ "v24@?0@\"MPModelLibraryPlaylistEditTransactionDetails\"8@\"NSError\"16"
+ "v32@?0@\"MPAdTimeRange\"8Q16^B24"
+ "v32@?0@\"NSString\"8@\"MPModelPlaylistEntry\"16^B24"
+ "v36@0:8@\"HMHome\"16@\"HMActionSet\"24B32"
+ "v64@0:8q16q24q32q40q48@?56"
+ "v64@0:8{?={?=qiIq}{?=qiIq}}16"
+ "variantType"
+ "{?=\"initialized\"b1\"beats1\"b1\"name\"b1\"editorNotes\"b1\"shortEditorNotes\"b1\"explicit\"b1\"type\"b1\"subtype\"b1\"artwork\"b1\"stationGlyph\"b1\"editorialArtwork\"b1\"attributionLabel\"b1\"providerName\"b1\"live\"b1\"startingAirDate\"b1\"endingAirDate\"b1\"subscriptionRequired\"b1}"
+ "{?=\"start\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"duration\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}}"
+ "{?=qiIq}40@0:8{?=qiIq}16"
+ "{?={?=qiIq}{?=qiIq}}16@0:8"
+ "\xf0\xf0\xf0\xb1"
- "%{public}@ Calling completion with loaded representation: %{public}@ and error: %{public}@"
- "%{public}@ Created data task for request: %{public}@"
- "%{public}@ Encountered error while requesting artwork for NSURLSessionDataTask: %{public}@. %{public}@"
- "%{public}@ Failed to append items. err=%{public}@"
- "%{public}@ Failed to insert items. err=%{public}@"
- "%{public}@ Loaded image representation: %{public}@ with URLSessionDataTask: %{public}@"
- "%{public}@ appending items %{public}@ "
- "%{public}@ encountered unexpected NSURLResponse: %{public}@"
- "%{public}@ inserting items at start %{public}@ "
- "(%@; %@)"
- "<%@:%p libraryID=%llu entityType=%ld artworkType=%ld"
- "C3"
- "[RCC] _updateCanBeNowPlayingApplicationIfNeeded: canBeNowPlayingApplication=%{BOOL}u playerPath=%{public}@ commands=%{public}@"
- "_createTrackIdentifierListWithInitialEntries:completion:"
- "_getTransportablePlaybackSessionRepresentationWithIdentifier:preferredSessionType:completion:"
- "_initWithLibrary:playlist:initialTrackList:playlistEntryProperties:authorProfile:"
- "_locked_updateCanBeNowPlayingApplicationIfNeeded"
- "importContainerArtworkForSagaID:completionHandler:"
- "key value "
- "requestWithIdentifier:preferredSessionType:"
- "user:didUpdatePersonManagerSettings:"
- "v32@?0@\"NSString\"8@\"MPModelLibraryPlaylistEditDataSource\"16^B24"
- "{?=\"initialized\"b1\"beats1\"b1\"name\"b1\"editorNotes\"b1\"shortEditorNotes\"b1\"explicit\"b1\"type\"b1\"subtype\"b1\"artwork\"b1\"stationGlyph\"b1\"attributionLabel\"b1\"providerName\"b1\"live\"b1\"startingAirDate\"b1\"endingAirDate\"b1\"subscriptionRequired\"b1}"
- "\xf0\xf0\xf0\xa1"

```
