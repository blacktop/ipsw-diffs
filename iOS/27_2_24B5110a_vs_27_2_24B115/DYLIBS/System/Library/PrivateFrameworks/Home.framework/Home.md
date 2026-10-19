## Home

> `/System/Library/PrivateFrameworks/Home.framework/Home`

```diff

-1269.2.5.1.4
-  __TEXT.__text: 0x3b198c
-  __TEXT.__objc_methlist: 0x2cedc
-  __TEXT.__const: 0x59f0
+1269.2.5.1.5
+  __TEXT.__text: 0x3c0070
+  __TEXT.__objc_methlist: 0x2dc34
+  __TEXT.__const: 0x5a80
   __TEXT.__dlopen_cstrs: 0x4b
   __TEXT.__swift5_typeref: 0x2d26
-  __TEXT.__oslogstring: 0x1e0f6
+  __TEXT.__oslogstring: 0x1e78a
   __TEXT.__swift5_reflstr: 0xee3
   __TEXT.__swift5_assocty: 0x320
   __TEXT.__swift5_fieldmd: 0x1258
   __TEXT.__constg_swiftt: 0x22cc
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__cstring: 0x356a0
+  __TEXT.__cstring: 0x35d2d
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__swift5_proto: 0x260
+  __TEXT.__swift5_proto: 0x268
   __TEXT.__swift5_types: 0x1a4
   __TEXT.__swift5_capture: 0x10d8
   __TEXT.__swift_as_entry: 0x280
   __TEXT.__swift_as_ret: 0x258
   __TEXT.__swift_as_cont: 0x520
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__gcc_except_tab: 0x4d2c
+  __TEXT.__gcc_except_tab: 0x4dd0
   __TEXT.__ustring: 0x72
-  __TEXT.__unwind_info: 0x122e0
-  __TEXT.__eh_frame: 0x75d0
+  __TEXT.__unwind_info: 0x127d0
+  __TEXT.__eh_frame: 0x7600
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11390
-  __DATA_CONST.__objc_classlist: 0x18a8
-  __DATA_CONST.__objc_catlist: 0x418
-  __DATA_CONST.__objc_protolist: 0x960
+  __DATA_CONST.__const: 0x11708
+  __DATA_CONST.__objc_classlist: 0x18c0
+  __DATA_CONST.__objc_catlist: 0x438
+  __DATA_CONST.__objc_protolist: 0x978
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13358
+  __DATA_CONST.__objc_selrefs: 0x136c0
   __DATA_CONST.__objc_protorefs: 0x430
-  __DATA_CONST.__objc_superrefs: 0x1328
-  __DATA_CONST.__objc_arraydata: 0x3f8
-  __DATA_CONST.__got: 0x3330
-  __AUTH_CONST.__const: 0xf6d8
-  __AUTH_CONST.__cfstring: 0x27be0
-  __AUTH_CONST.__objc_const: 0x4c998
-  __AUTH_CONST.__objc_intobj: 0x23b8
+  __DATA_CONST.__objc_superrefs: 0x1338
+  __DATA_CONST.__objc_arraydata: 0x400
+  __DATA_CONST.__got: 0x3360
+  __AUTH_CONST.__const: 0xfe68
+  __AUTH_CONST.__cfstring: 0x27fa0
+  __AUTH_CONST.__objc_const: 0x4df08
+  __AUTH_CONST.__objc_intobj: 0x2460
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x2250
-  __AUTH.__objc_data: 0xa608
+  __AUTH.__objc_data: 0xa658
   __AUTH.__data: 0x15a0
-  __DATA.__objc_ivar: 0x1618
-  __DATA.__data: 0x7a50
+  __DATA.__objc_ivar: 0x1630
+  __DATA.__data: 0x7b70
   __DATA.__objc_stublist: 0x10
   __DATA.__common: 0x158
-  __DATA_DIRTY.__objc_ivar: 0xcb8
-  __DATA_DIRTY.__objc_data: 0x67a0
+  __DATA_DIRTY.__objc_ivar: 0xcf4
+  __DATA_DIRTY.__objc_data: 0x6840
   __DATA_DIRTY.__data: 0xf40
-  __DATA_DIRTY.__bss: 0x1e60
+  __DATA_DIRTY.__bss: 0x1e78
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 21414
-  Symbols:   30488
-  CStrings:  8645
+  Functions: 21805
+  Symbols:   30937
+  CStrings:  8715
 
Symbols:
+ +[HFAccessoryType mediaGroupType]
+ +[HFMediaGroupBuilder homeKitRepresentationClass]
+ +[HFMediaHelper isContainedWithinMediaGroup:]
+ +[HFMediaHelper isPermanentSpeakerGroup:]
+ +[HFNamingComponents namingComponentFromMediaGroup:]
+ +[NSURL(HFAdditions) hf_homeTheaterLearnMoreURL]
+ -[HFHomeKitDispatcher mediaGroupsController]
+ -[HFHomeKitMediaGroupsController .cxx_destruct]
+ -[HFHomeKitMediaGroupsController _notifyObserversOfReceivedMediaGroup:]
+ -[HFHomeKitMediaGroupsController addObserver:]
+ -[HFHomeKitMediaGroupsController didUpdateItemsContainingMediaGroup:]
+ -[HFHomeKitMediaGroupsController initWithHomeManager:]
+ -[HFHomeKitMediaGroupsController mediaGroupsController:didReceiveGroup:]
+ -[HFHomeKitMediaGroupsController mediaGroupsController:didRemoveGroup:]
+ -[HFHomeKitMediaGroupsController observers]
+ -[HFHomeKitMediaGroupsController removeObserver:]
+ -[HFItemManager _itemsToUpdateForMediaGroupChange:]
+ -[HFItemManager(HomeKitDelegates) didUpdateItemsContainingMediaGroup:]
+ -[HFMediaAccessoryItem _decorateWithMediaGroupSpecificKeys:]
+ -[HFMediaAccessoryItem _decorateWithSurroundSetupKeys:]
+ -[HFMediaAccessoryItem didReceiveMediaGroup:]
+ -[HFMediaAccessoryItem isAirPortExpressInPermanentSpeakerGroup]
+ -[HFMediaAccessoryItem isAudioReceiverInPermanentSpeakerGroup]
+ -[HFMediaAccessoryItem isContainedWithinPermanentSpeakerGroup]
+ -[HFMediaAccessoryItem isDumbSpeakerInPermanentSpeakerGroup]
+ -[HFMediaAccessoryItem isHAPSpeakerInPermanentSpeakerGroup]
+ -[HFMediaAccessoryItem isHomePodStereoPairInPermanentSpeakerGroup]
+ -[HFMediaAccessoryItem isHomeTheaterSystem]
+ -[HFMediaAccessoryItem isPermanentSpeakerGroupWithAtLeastOneHomePod]
+ -[HFMediaAccessoryItem isPermanentSpeakerGroup]
+ -[HFMediaAccessoryItem isSingleHomePodInPermanentSpeakerGroup]
+ -[HFMediaAccessoryItem mediaGroupSetupDataSource]
+ -[HFMediaAccessoryItem setMediaGroupSetupDataSource:]
+ -[HFMediaAccessoryItemUpdateRequest _disambiguateHomeTheaterResponses:forHomeTheaterSystem:]
+ -[HFMediaGroupAccessoryType description]
+ -[HFMediaGroupAccessoryType hash]
+ -[HFMediaGroupAccessoryType isEqual:]
+ -[HFMediaGroupBuilder .cxx_destruct]
+ -[HFMediaGroupBuilder _appleTVForHomeTheaterSystem:inHome:]
+ -[HFMediaGroupBuilder _arbitrateMusicAccount]
+ -[HFMediaGroupBuilder _commitChangesToMediaGroupBuilderWithUnconfiguredSystems:]
+ -[HFMediaGroupBuilder _commitMediaSystemBuilders]
+ -[HFMediaGroupBuilder _defaultName]
+ -[HFMediaGroupBuilder _handleRedundantMediaSystemBuilder:]
+ -[HFMediaGroupBuilder _rooms]
+ -[HFMediaGroupBuilder _updateAssistantAccessControl]
+ -[HFMediaGroupBuilder _updateHomeTheaterGroupName:homeTheaterSystem:]
+ -[HFMediaGroupBuilder _updateRooms]
+ -[HFMediaGroupBuilder _updateValueForContextType:]
+ -[HFMediaGroupBuilder accessories]
+ -[HFMediaGroupBuilder accountArbitrator]
+ -[HFMediaGroupBuilder addDestination:]
+ -[HFMediaGroupBuilder addMediaSystemBuilder:]
+ -[HFMediaGroupBuilder areMultipleSpeakersSelected]
+ -[HFMediaGroupBuilder canMakeStereoPairInstead]
+ -[HFMediaGroupBuilder commitItem]
+ -[HFMediaGroupBuilder componentDestinations]
+ -[HFMediaGroupBuilder configuredName]
+ -[HFMediaGroupBuilder existingGroupIsEqualToSelectedSpeakers]
+ -[HFMediaGroupBuilder firstSelectedMediaDestinationIdentifier]
+ -[HFMediaGroupBuilder firstSetupSourceMediaContainer]
+ -[HFMediaGroupBuilder hasSetName]
+ -[HFMediaGroupBuilder hasSetRoom]
+ -[HFMediaGroupBuilder homePodsPerRoomThatCanBeCreatedIntoStereoPairs]
+ -[HFMediaGroupBuilder homeTheaterSystem]
+ -[HFMediaGroupBuilder iconDescriptor]
+ -[HFMediaGroupBuilder initWithMediaProfileContainer:inHome:]
+ -[HFMediaGroupBuilder isCreatingMediaGroup]
+ -[HFMediaGroupBuilder isFavorite]
+ -[HFMediaGroupBuilder isFirstSelectedMediaDestination:]
+ -[HFMediaGroupBuilder mediaGroup]
+ -[HFMediaGroupBuilder mediaProfileContainers]
+ -[HFMediaGroupBuilder mediaSystemBuilders]
+ -[HFMediaGroupBuilder name]
+ -[HFMediaGroupBuilder namingComponent]
+ -[HFMediaGroupBuilder originalName]
+ -[HFMediaGroupBuilder removeDestination:]
+ -[HFMediaGroupBuilder removeItemFromHome:]
+ -[HFMediaGroupBuilder removeItemFromHome]
+ -[HFMediaGroupBuilder removeMediaSystemBuilder:]
+ -[HFMediaGroupBuilder roomBuilder]
+ -[HFMediaGroupBuilder room]
+ -[HFMediaGroupBuilder setAccountArbitrator:]
+ -[HFMediaGroupBuilder setComponentDestinations:]
+ -[HFMediaGroupBuilder setConfiguredName:]
+ -[HFMediaGroupBuilder setFirstSelectedMediaDestinationIdentifier:]
+ -[HFMediaGroupBuilder setHasSetName:]
+ -[HFMediaGroupBuilder setHasSetRoom:]
+ -[HFMediaGroupBuilder setHomeTheaterSystem:]
+ -[HFMediaGroupBuilder setIconDescriptor:]
+ -[HFMediaGroupBuilder setIsCreatingMediaGroup:]
+ -[HFMediaGroupBuilder setIsFavorite:]
+ -[HFMediaGroupBuilder setMediaGroup:]
+ -[HFMediaGroupBuilder setMediaSystemBuilders:]
+ -[HFMediaGroupBuilder setName:]
+ -[HFMediaGroupBuilder setNamingComponent:]
+ -[HFMediaGroupBuilder setRoom:]
+ -[HFMediaGroupBuilder setRoomBuilder:]
+ -[HFMediaGroupBuilder setShowInHomeDashboard:]
+ -[HFMediaGroupBuilder setSurroundSetupSessionUUID:]
+ -[HFMediaGroupBuilder showInHomeDashboard]
+ -[HFMediaGroupBuilder supportsFavoriting]
+ -[HFMediaGroupBuilder surroundSetupSessionUUID]
+ -[HFNamingComponents isHomeTheaterSystem]
+ -[HFNamingComponents isMediaGroup]
+ -[HFNamingComponents setIsHomeTheaterSystem:]
+ -[HFNamingComponents setIsMediaGroup:]
+ -[HMHome(Additions) hf_accessoryForMediaDestinationIdentifier:]
+ -[HMHome(Additions) hf_containerForMediaDestinationIdentifier:]
+ -[HMHome(Additions) hf_homeTheaterGroupForMediaProfileContainer:]
+ -[HMHome(Additions) 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:]
+ -[HMHome(Additions) hf_homeTheaterWithIdentifier:]
+ -[HMHome(Additions) hf_mediaGroupForAccessory:]
+ -[HMHome(Additions) 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:]
+ -[HMHome(Additions) hf_mediaGroupForSystem:]
+ -[HMHome(Additions) hf_surroundSystemForHomeTheater:]
+ -[HMHomeTheaterSystem(AccessoryLikeObjectDataSource) hf_rootAccessoryLikeHomeKitObject]
+ -[HMHomeTheaterSystem(HFAdditions) _surroundIconDescriptorWithConfiguration:surroundSystem:]
+ -[HMHomeTheaterSystem(HFAdditions) hf_appleTV]
+ -[HMHomeTheaterSystem(HFAdditions) hf_iconDescriptorWithConfiguration:]
+ -[HMHomeTheaterSystem(HFAdditions) hf_mediaProfileContainers]
+ -[HMHomeTheaterSystem(HFAdditions) hf_supportsRenaming]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) accessories]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) hf_backingAccessory]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) hf_canSpanMultipleRooms]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) hf_home]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) hf_isInRoom:]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) hf_mediaRouteIdentifier]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) hf_parentRoom]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) hf_showsAudioSettings]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) hf_speakerGroup]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) hf_supportsHomeTheater]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) homeKitObject]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) mediaProfiles]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) mediaSession]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) numberOfItemsContainedWithinGroup]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) symptomsHandler]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) symptoms]
+ -[HMHomeTheaterSystem(HFMediaGroupAdditions) topSymptomsHandlerAccessory]
+ -[HMMediaGroup(AbstractionAdditions) hf_accessoryLikeObject]
+ -[HMMediaGroup(AccessoryLikeObjectDataSource) hf_rootAccessoryLikeHomeKitObject]
+ -[HMMediaGroup(HFAdditions) _speakerSymbolTypeFromHomePodVariant:]
+ -[HMMediaGroup(HFAdditions) hf_homePodAccessories]
+ -[HMMediaGroup(HFAdditions) hf_iconDescriptorWithConfiguration:]
+ -[HMMediaGroup(HFAdditions) hf_mediaProfileContainers]
+ -[HMMediaGroup(HFAdditions) hf_mediaProfiles]
+ -[HMMediaGroup(HFAdditions) hf_mediaSystems]
+ -[HMMediaGroup(HFAdditions) hf_roomsOfHomePods]
+ -[HMMediaGroup(HFAdditions) hf_rooms]
+ -[HMMediaGroup(HFHomeKitObjectConformance) hf_isValidObject]
+ -[HMMediaGroup(HFHomeKitObjectConformance) home]
+ -[HMMediaGroup(HFHomeKitObjectConformance) uniqueIdentifier]
+ -[HMMediaGroup(HFIncludedContextProtocol) hf_hasSetForContextType:]
+ -[HMMediaGroup(HFIncludedContextProtocol) hf_isOnForContextType:]
+ -[HMMediaGroup(HFIncludedContextProtocol) hf_shouldBeOnForContextType:]
+ -[HMMediaGroup(HFIncludedContextProtocol) hf_shouldHideForContextType:]
+ -[HMMediaGroup(HFIncludedContextProtocol) hf_updateValue:forContextType:]
+ -[HMMediaGroup(HFMediaGroupAdditions) accessories]
+ -[HMMediaGroup(HFMediaGroupAdditions) hasValidSettings]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_accessoryType]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_appleMusicCurrentLoggedInAccountDSID]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_appleMusicCurrentLoggedInAccount]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_associatedAccessories]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_backingAccessory]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_canShowInControlCenter]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_canSpanMultipleRooms]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_categoryCapitalizedLocalizedDescription]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_categoryLowercaseLocalizedDescription]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_containedCharacteristics]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_containedProfiles]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_containedServices]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_dateAdded]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_dependentHomeKitObjectsForDownstreamItems]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_destination]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_deviceIdentifiers]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_displayName]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_effectiveIsFavorite]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_effectiveShowInHomeDashboard]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_fetchLog:timeout:]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_fetchLogListWithTimeout:]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_hasSetFavorite]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_hasSetShowInHomeDashboard]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_hasSetVisibleInHomeStatus]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_homeKitObject]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_homePodIsCapableOfShowingSplitAccountError]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_homePodMediaAccountIsMismatchedWithHomeMediaAccount]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_homePodSupportsMultiUserLanguage]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_homePodSupportsMultiUser]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_homePodsSpanMultipleRooms]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_home]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_identify]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_idsDeviceIdentifierWithError:]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_isAccessorySettingsReachable]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_isAppleMusicReachable]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_isCurrentAccessory]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_isEitherHomePodMediaAccountOrHomeMediaAccountPresent]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_isFavorite]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_isForcedVisibleInHomeStatus]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_isIdentifiable]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_isInRoom:]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_isMatterOnlyAccessory]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_isReachable]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_isSpeakerGrouped]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_isVisibleInHomeStatus]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_itemClass]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_mediaRouteIdentifier]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_mediaValueSource]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_moveToRoom:]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_parentRoom]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_preferredMediaUser]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_preferredUserSelectionType]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_safeRoom]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_setTileSize:]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_settingsAdapterManager]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_settingsValueManager]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_shouldShowInFavorites]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_showInHomeDashboard]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_showsAudioSettings]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_siriLanguageOptionsManager]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_spansMultipleRooms]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_stateDumpBuilderWithContext:]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_supportsAppleIntelligenceReport]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_supportsHomeStatus]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_supportsHomeTheater]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_supportsMediaActions]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_supportsMultiUser]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_supportsMusicAlarm]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_supportsPreferredMediaUser]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_supportsSoftwareUpdate]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_supportsSpeakerGrouping]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_supportsStereoPairing]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_tileSize]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_updateDateAdded:]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_updateIsFavorite:]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_updateIsVisibleInHomeStatus:]
+ -[HMMediaGroup(HFMediaGroupAdditions) hf_updateShowInHomeDashboard:]
+ -[HMMediaGroup(HFMediaGroupAdditions) homeKitObject]
+ -[HMMediaGroup(HFMediaGroupAdditions) homekitObjectIdentifiers]
+ -[HMMediaGroup(HFMediaGroupAdditions) isContainedWithinItemGroup]
+ -[HMMediaGroup(HFMediaGroupAdditions) isItemGroup]
+ -[HMMediaGroup(HFMediaGroupAdditions) mediaProfiles]
+ -[HMMediaGroup(HFMediaGroupAdditions) mediaSession]
+ -[HMMediaGroup(HFMediaGroupAdditions) numberOfItemsContainedWithinGroup]
+ -[HMMediaGroup(HFMediaGroupAdditions) settings]
+ -[HMMediaGroup(HFMediaGroupAdditions) symptomsHandler]
+ -[HMMediaGroup(HFMediaGroupAdditions) symptoms]
+ -[HMMediaGroup(HFMediaGroupAdditions) topSymptomsHandlerAccessory]
+ -[HMMediaGroup(HFReordering) hf_serviceNameComponents]
+ -[HMMediaGroupsController(HFAdditions) hf_homeTheaterSystemGroups]
+ -[HMMediaGroupsController(HFAdditions) hf_psgGroups]
+ -[HMMediaGroupsController(HFAdditions) hf_surroundSystemGroups]
+ -[HMMediaProfile(HFMediaAccessoryProfileAdditions) hf_homePodsSpanMultipleRooms]
+ -[HMMediaProfile(HFMediaAccessoryProfileAdditions) hf_isSpeakerGrouped]
+ -[HMMediaProfile(HFMediaAccessoryProfileAdditions) hf_spansMultipleRooms]
+ -[HMMediaProfile(HFMediaAccessoryProfileAdditions) hf_supportsSpeakerGrouping]
+ -[HMMediaSystem(HFMediaAccessoryProfileAdditions) hf_homePodsSpanMultipleRooms]
+ -[HMMediaSystem(HFMediaAccessoryProfileAdditions) hf_isSpeakerGrouped]
+ -[HMMediaSystem(HFMediaAccessoryProfileAdditions) hf_spansMultipleRooms]
+ -[HMMediaSystem(HFMediaAccessoryProfileAdditions) hf_supportsSpeakerGrouping]
+ -[HMSurroundSystem(AccessoryLikeObjectDataSource) hf_rootAccessoryLikeHomeKitObject]
+ GCC_except_table277
+ GCC_except_table282
+ GCC_except_table306
+ GCC_except_table313
+ GCC_except_table345
+ GCC_except_table423
+ GCC_except_table433
+ GCC_except_table436
+ GCC_except_table437
+ GCC_except_table439
+ GCC_except_table440
+ GCC_except_table446
+ GCC_except_table449
+ GCC_except_table450
+ GCC_except_table452
+ GCC_except_table453
+ GCC_except_table460
+ GCC_except_table463
+ GCC_except_table479
+ GCC_except_table480
+ GCC_except_table482
+ GCC_except_table485
+ GCC_except_table489
+ GCC_except_table490
+ GCC_except_table492
+ GCC_except_table493
+ _HFImageIconIdentifierSurroundMixed
+ _HFImageIconIdentifierSurroundMixedTile
+ _HFPreferencesIgnoreSpeakerGroupingErrors
+ _HFPreferencesIgnoreSpeakerGroupingErrorsKey
+ _HFResultRoomSpeakerCountKey
+ _OBJC_CLASS_$_HFHomeKitMediaGroupsController
+ _OBJC_CLASS_$_HFMediaGroupAccessoryType
+ _OBJC_CLASS_$_HFMediaGroupBuilder
+ _OBJC_CLASS_$_HMHomeTheaterSystem
+ _OBJC_CLASS_$_HMMediaGroup
+ _OBJC_CLASS_$_HMMediaGroupsController
+ _OBJC_CLASS_$_HMSurroundSystem
+ _OBJC_IVAR_$_HFHomeKitDispatcher._mediaGroupsController
+ _OBJC_IVAR_$_HFHomeKitMediaGroupsController._observers
+ _OBJC_IVAR_$_HFMediaGroupBuilder._hasSetName
+ _OBJC_IVAR_$_HFMediaGroupBuilder._hasSetRoom
+ _OBJC_IVAR_$_HFNamingComponents._isHomeTheaterSystem
+ _OBJC_IVAR_$_HFNamingComponents._isMediaGroup
+ _OBJC_METACLASS_$_HFHomeKitMediaGroupsController
+ _OBJC_METACLASS_$_HFMediaGroupAccessoryType
+ _OBJC_METACLASS_$_HFMediaGroupBuilder
+ __OBJC_$_CATEGORY_HMHomeTheaterSystem_$_AccessoryLikeObjectDataSource
+ __OBJC_$_CATEGORY_HMMediaGroup_$_AccessoryLikeObjectDataSource
+ __OBJC_$_CATEGORY_HMMediaGroupsController_$_HFAdditions
+ __OBJC_$_CATEGORY_HMSurroundSystem_$_AccessoryLikeObjectDataSource
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_HMMediaGroupsController_$_HFAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_HMSurroundSystem_$_AccessoryLikeObjectDataSource
+ __OBJC_$_CLASS_METHODS_HFMediaGroupBuilder
+ __OBJC_$_INSTANCE_METHODS_HFHomeKitMediaGroupsController
+ __OBJC_$_INSTANCE_METHODS_HFMediaGroupAccessoryType
+ __OBJC_$_INSTANCE_METHODS_HFMediaGroupBuilder
+ __OBJC_$_INSTANCE_METHODS_HMHomeTheaterSystem(AccessoryLikeObjectDataSource|HFAdditions|HFMediaGroupAdditions)
+ __OBJC_$_INSTANCE_METHODS_HMMediaGroup(AccessoryLikeObjectDataSource|AbstractionAdditions|HFIncludedContextProtocol|HFAdditions|HFReordering|HFHomeKitObjectConformance|HFMediaGroupAdditions)
+ __OBJC_$_INSTANCE_VARIABLES_HFHomeKitMediaGroupsController
+ __OBJC_$_INSTANCE_VARIABLES_HFMediaGroupBuilder
+ __OBJC_$_PROP_LIST_HFHomeKitMediaGroupsController
+ __OBJC_$_PROP_LIST_HFMediaGroupBuilder
+ __OBJC_$_PROP_LIST_HMMediaGroupsController_$_HFAdditions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HFHomeKitMediaGroupsControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMMediaGroupsControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMMediaGroupsControllerDelegate_Deprecated
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HFHomeKitMediaGroupsControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMediaGroupsControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMediaGroupsControllerDelegate_Deprecated
+ __OBJC_$_PROTOCOL_REFS_HFHomeKitMediaGroupsControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_HMMediaGroupsControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_HMMediaGroupsControllerDelegate_Deprecated
+ __OBJC_CLASS_PROTOCOLS_$_HFHomeKitMediaGroupsController
+ __OBJC_CLASS_PROTOCOLS_$_HFMediaGroupBuilder
+ __OBJC_CLASS_PROTOCOLS_$_HMHomeTheaterSystem(AccessoryLikeObjectDataSource|HFAdditions|HFMediaGroupAdditions)
+ __OBJC_CLASS_PROTOCOLS_$_HMMediaGroup(AccessoryLikeObjectDataSource|AbstractionAdditions|HFIncludedContextProtocol|HFAdditions|HFReordering|HFHomeKitObjectConformance|HFMediaGroupAdditions)
+ __OBJC_CLASS_RO_$_HFHomeKitMediaGroupsController
+ __OBJC_CLASS_RO_$_HFMediaGroupAccessoryType
+ __OBJC_CLASS_RO_$_HFMediaGroupBuilder
+ __OBJC_LABEL_PROTOCOL_$_HFHomeKitMediaGroupsControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMMediaGroupsControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMMediaGroupsControllerDelegate_Deprecated
+ __OBJC_METACLASS_RO_$_HFHomeKitMediaGroupsController
+ __OBJC_METACLASS_RO_$_HFMediaGroupAccessoryType
+ __OBJC_METACLASS_RO_$_HFMediaGroupBuilder
+ __OBJC_PROTOCOL_$_HFHomeKitMediaGroupsControllerDelegate
+ __OBJC_PROTOCOL_$_HMMediaGroupsControllerDelegate
+ __OBJC_PROTOCOL_$_HMMediaGroupsControllerDelegate_Deprecated
+ ___33+[HFAccessoryType mediaGroupType]_block_invoke_2
+ ___33-[HFMediaGroupBuilder commitItem]_block_invoke
+ ___33-[HFMediaGroupBuilder commitItem]_block_invoke_2
+ ___37-[HMMediaGroup(HFAdditions) hf_rooms]_block_invoke
+ ___41-[HFMediaGroupBuilder removeItemFromHome]_block_invoke
+ ___41-[HFMediaGroupBuilder removeItemFromHome]_block_invoke_2
+ ___41-[HFMediaGroupBuilder removeItemFromHome]_block_invoke_3
+ ___43-[HFMediaAccessoryItemProvider reloadItems]_block_invoke_5
+ ___43-[HFMediaAccessoryItemProvider reloadItems]_block_invoke_6
+ ___43-[HFMediaAccessoryItemProvider reloadItems]_block_invoke_7
+ ___43-[HFMediaAccessoryItemProvider reloadItems]_block_invoke_8
+ ___44-[HMHome(Additions) hf_mediaGroupForSystem:]_block_invoke
+ ___44-[HMMediaGroup(HFAdditions) hf_mediaSystems]_block_invoke
+ ___44-[HMMediaGroup(HFAdditions) hf_mediaSystems]_block_invoke_2
+ ___45-[HFMediaAccessoryItem supportsPlaybackState]_block_invoke
+ ___45-[HFMediaGroupBuilder mediaProfileContainers]_block_invoke
+ ___45-[HFMediaGroupBuilder mediaProfileContainers]_block_invoke_2
+ ___45-[HMMediaGroup(HFAdditions) hf_mediaProfiles]_block_invoke
+ ___45-[HMMediaGroup(HFAdditions) hf_mediaProfiles]_block_invoke_2
+ ___46-[HFMediaSystemBuilder mediaProfileContainers]_block_invoke
+ ___46-[HMHomeTheaterSystem(HFAdditions) hf_appleTV]_block_invoke
+ ___47-[HFMediaGroupBuilder canMakeStereoPairInstead]_block_invoke
+ ___47-[HMHome(Additions) hf_mediaGroupForAccessory:]_block_invoke
+ ___47-[HMMediaGroup(HFAdditions) hf_roomsOfHomePods]_block_invoke
+ ___47-[HMMediaGroup(HFMediaGroupAdditions) settings]_block_invoke
+ ___47-[HMMediaGroup(HFMediaGroupAdditions) symptoms]_block_invoke
+ ___49-[HFMediaGroupBuilder _commitMediaSystemBuilders]_block_invoke
+ ___49-[HFMediaGroupBuilder _commitMediaSystemBuilders]_block_invoke_2
+ ___49-[HFMediaGroupBuilder _commitMediaSystemBuilders]_block_invoke_3
+ ___50-[HFMediaGroupBuilder _updateValueForContextType:]_block_invoke
+ ___50-[HFMediaGroupBuilder _updateValueForContextType:]_block_invoke_2
+ ___50-[HFMediaGroupBuilder _updateValueForContextType:]_block_invoke_3
+ ___50-[HMHome(Additions) hf_homeTheaterWithIdentifier:]_block_invoke
+ ___50-[HMMediaGroup(HFAdditions) hf_homePodAccessories]_block_invoke
+ ___50-[HMMediaGroup(HFMediaGroupAdditions) hf_safeRoom]_block_invoke
+ ___50-[HMMediaGroup(HFMediaGroupAdditions) hf_tileSize]_block_invoke
+ ___51-[HFSymptomStatusItem _subclass_updateWithOptions:]_block_invoke_5
+ ___51-[HMMediaGroup(HFMediaGroupAdditions) hf_isInRoom:]_block_invoke
+ ___52-[HMMediaGroup(HFMediaGroupAdditions) hf_parentRoom]_block_invoke
+ ___52-[HMMediaGroup(HFMediaGroupAdditions) mediaProfiles]_block_invoke
+ ___52-[HMMediaGroupsController(HFAdditions) hf_psgGroups]_block_invoke
+ ___53-[HMHome(Additions) hf_surroundSystemForHomeTheater:]_block_invoke
+ ___53-[HMMediaGroup(HFMediaGroupAdditions) hf_isReachable]_block_invoke
+ ___53-[HMMediaGroup(HFMediaGroupAdditions) hf_moveToRoom:]_block_invoke
+ ___54-[HMMediaGroup(HFAdditions) hf_mediaProfileContainers]_block_invoke
+ ___54-[HMMediaGroup(HFMediaGroupAdditions) hf_setTileSize:]_block_invoke
+ ___54-[HMMediaGroup(HFMediaGroupAdditions) hf_setTileSize:]_block_invoke_2
+ ___55-[HMHome(Additions) hf_allUniqueMediaProfileContainers]_block_invoke_3
+ ___55-[HMHome(Additions) hf_allUniqueMediaProfileContainers]_block_invoke_4
+ ___58-[HFMediaGroupBuilder _handleRedundantMediaSystemBuilder:]_block_invoke
+ ___58-[HFMediaGroupBuilder _handleRedundantMediaSystemBuilder:]_block_invoke_2
+ ___58-[HFMediaGroupBuilder _handleRedundantMediaSystemBuilder:]_block_invoke_3
+ ___58-[HFMediaGroupBuilder _handleRedundantMediaSystemBuilder:]_block_invoke_4
+ ___59-[HFMediaGroupBuilder _appleTVForHomeTheaterSystem:inHome:]_block_invoke
+ ___59-[HMHome(Additions) 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:]_block_invoke
+ ___59-[HMHomeTheaterSystem(HFMediaGroupAdditions) mediaProfiles]_block_invoke
+ ___59-[HMMediaGroup(HFMediaGroupAdditions) hf_containedServices]_block_invoke
+ ___59-[HMMediaGroup(HFMediaGroupAdditions) hf_supportsMultiUser]_block_invoke
+ ___60-[HFMediaGroupBuilder initWithMediaProfileContainer:inHome:]_block_invoke
+ ___60-[HFMediaGroupBuilder initWithMediaProfileContainer:inHome:]_block_invoke_2
+ ___60-[HFMediaGroupBuilder initWithMediaProfileContainer:inHome:]_block_invoke_3
+ ___60-[HMMediaGroup(HFHomeKitObjectConformance) hf_isValidObject]_block_invoke
+ ___60-[HMMediaGroup(HFMediaGroupAdditions) hf_isCurrentAccessory]_block_invoke
+ ___60-[HMMediaGroup(HFMediaGroupAdditions) hf_supportsMusicAlarm]_block_invoke
+ ___61-[HMHomeTheaterSystem(HFAdditions) hf_mediaProfileContainers]_block_invoke
+ ___62-[HMMediaGroup(HFMediaGroupAdditions) hf_supportsMediaActions]_block_invoke
+ ___63-[HMHome(Additions) hf_accessoryForMediaDestinationIdentifier:]_block_invoke
+ ___63-[HMHome(Additions) hf_containerForMediaDestinationIdentifier:]_block_invoke
+ ___63-[HMMediaGroup(HFMediaGroupAdditions) hf_isAppleMusicReachable]_block_invoke
+ ___63-[HMMediaGroup(HFMediaGroupAdditions) homekitObjectIdentifiers]_block_invoke
+ ___63-[HMMediaGroupsController(HFAdditions) hf_surroundSystemGroups]_block_invoke
+ ___64-[HMMediaGroup(HFAdditions) hf_iconDescriptorWithConfiguration:]_block_invoke
+ ___65-[HMMediaGroup(HFIncludedContextProtocol) hf_isOnForContextType:]_block_invoke
+ ___66-[HMMediaGroup(HFMediaGroupAdditions) hf_containedCharacteristics]_block_invoke
+ ___66-[HMMediaGroup(HFMediaGroupAdditions) hf_homePodSupportsMultiUser]_block_invoke
+ ___66-[HMMediaGroupsController(HFAdditions) hf_homeTheaterSystemGroups]_block_invoke
+ ___67-[HMMediaGroup(HFIncludedContextProtocol) hf_hasSetForContextType:]_block_invoke
+ ___68-[HFMediaAccessoryItem isPermanentSpeakerGroupWithAtLeastOneHomePod]_block_invoke
+ ___68-[HMMediaGroup(HFMediaGroupAdditions) hf_siriLanguageOptionsManager]_block_invoke
+ ___68-[HMMediaGroup(HFMediaGroupAdditions) hf_supportsPreferredMediaUser]_block_invoke
+ ___69-[HFMediaGroupBuilder _updateHomeTheaterGroupName:homeTheaterSystem:]_block_invoke
+ ___69-[HFMediaGroupBuilder homePodsPerRoomThatCanBeCreatedIntoStereoPairs]_block_invoke
+ ___69-[HFMediaGroupBuilder homePodsPerRoomThatCanBeCreatedIntoStereoPairs]_block_invoke_2
+ ___69-[HFMediaGroupBuilder homePodsPerRoomThatCanBeCreatedIntoStereoPairs]_block_invoke_3
+ ___69-[HFMediaGroupBuilder homePodsPerRoomThatCanBeCreatedIntoStereoPairs]_block_invoke_4
+ ___69-[HFMediaGroupBuilder homePodsPerRoomThatCanBeCreatedIntoStereoPairs]_block_invoke_5
+ ___69-[HMMediaGroup(HFMediaGroupAdditions) hf_isForcedVisibleInHomeStatus]_block_invoke
+ ___70-[HMMediaGroup(HFMediaGroupAdditions) hf_isAccessorySettingsReachable]_block_invoke
+ ___71-[HMHomeTheaterSystem(HFAdditions) hf_iconDescriptorWithConfiguration:]_block_invoke
+ ___71-[HMMediaGroup(HFIncludedContextProtocol) hf_shouldHideForContextType:]_block_invoke
+ ___73-[HMHomeTheaterSystem(HFMediaGroupAdditions) topSymptomsHandlerAccessory]_block_invoke
+ ___73-[HMHomeTheaterSystem(HFMediaGroupAdditions) topSymptomsHandlerAccessory]_block_invoke_2
+ ___74-[HFMediaPlaybackActionBuilder mediaProfileContainersForAccessories:home:]_block_invoke_4
+ ___74-[HFMediaPlaybackActionBuilder mediaProfileContainersForAccessories:home:]_block_invoke_5
+ ___78-[HMMediaGroup(HFMediaGroupAdditions) hf_appleMusicCurrentLoggedInAccountDSID]_block_invoke
+ ___80-[HFMediaGroupBuilder _commitChangesToMediaGroupBuilderWithUnconfiguredSystems:]_block_invoke
+ ___80-[HFMediaGroupBuilder _commitChangesToMediaGroupBuilderWithUnconfiguredSystems:]_block_invoke_2
+ ___80-[HFMediaGroupBuilder _commitChangesToMediaGroupBuilderWithUnconfiguredSystems:]_block_invoke_3
+ ___80-[HFMediaGroupBuilder _commitChangesToMediaGroupBuilderWithUnconfiguredSystems:]_block_invoke_4
+ ___80-[HFMediaGroupBuilder _commitChangesToMediaGroupBuilderWithUnconfiguredSystems:]_block_invoke_5
+ ___80-[HFMediaGroupBuilder _commitChangesToMediaGroupBuilderWithUnconfiguredSystems:]_block_invoke_6
+ ___80-[HFMediaGroupBuilder _commitChangesToMediaGroupBuilderWithUnconfiguredSystems:]_block_invoke_7
+ ___84-[HMMediaGroup(HFMediaGroupAdditions) hf_homePodIsCapableOfShowingSplitAccountError]_block_invoke
+ ___92-[HFMediaAccessoryItemUpdateRequest _disambiguateHomeTheaterResponses:forHomeTheaterSystem:]_block_invoke
+ ___92-[HMHomeTheaterSystem(HFAdditions) _surroundIconDescriptorWithConfiguration:surroundSystem:]_block_invoke
+ ___98+[HFItemProviderUtilities _servicesForHome:canShowInControlCentre:withLimit:includes:ignoreUUIDs:]_block_invoke_11
+ ___block_descriptor_32_e22_16?0"HMMediaGroup"8l
+ ___block_descriptor_32_e22_B16?0"HMMediaGroup"8l
+ ___block_descriptor_32_e30_16?0"<HMMediaDestination>"8l
+ ___block_descriptor_32_e30_16?0"HFMediaSystemBuilder"8l
+ ___block_descriptor_32_e31_"NSNumber"16?0"HMAccessory"8l
+ ___block_descriptor_32_e48_"<NSCopying>"16?0"<HFMediaProfileContainer>"8l
+ ___block_descriptor_40_e8_32s_e22_B16?0"HMMediaGroup"8ls32l8
+ ___block_descriptor_40_e8_32s_e24_v16?0"HMMediaProfile"8ls32l8
+ ___block_descriptor_40_e8_32s_e29_B16?0"HMHomeTheaterSystem"8ls32l8
+ ___block_descriptor_40_e8_32s_e29_v16?0"HMHomeTheaterSystem"8ls32l8
+ ___block_descriptor_40_e8_32s_e30_16?0"<HMMediaDestination>"8ls32l8
+ ___block_descriptor_40_e8_32s_e30_B16?0"HFMediaSystemBuilder"8ls32l8
+ ___block_descriptor_40_e8_32s_e31_"NSNumber"16?0"HMAccessory"8ls32l8
+ ___block_descriptor_40_e8_32w_e25_v16?0?<v?"NSError">8lw32l8
+ ___block_descriptor_48_e8_32s40s_e22_B16?0"HMMediaGroup"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e23_v16?0"HMMediaSystem"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e27_v16?0"<HFHomeKitObject>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e35_B16?0"<HFMediaProfileContainer>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e27_"NAFuture"16?0"NSArray"8ls32l8
+ ___block_descriptor_48_e8_32s_e8_v16?08ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e29_v32?0"HMMediaGroup"8Q16^B24ls48l8s32l8s40l8
- GCC_except_table162
- GCC_except_table169
- GCC_except_table276
- GCC_except_table281
- GCC_except_table327
- GCC_except_table405
- GCC_except_table415
- GCC_except_table418
- GCC_except_table419
- GCC_except_table421
- GCC_except_table422
- GCC_except_table427
- GCC_except_table428
- GCC_except_table431
- GCC_except_table432
- GCC_except_table434
- GCC_except_table435
- GCC_except_table442
- GCC_except_table443
- GCC_except_table456
- GCC_except_table457
- GCC_except_table462
- GCC_except_table464
- GCC_except_table467
- GCC_except_table471
- GCC_except_table472
- GCC_except_table51
CStrings:
+ "%@ Media Profile Container %@ contains profiles with different selected language options: %@ compared with %@"
+ "%@:%@ : Can't update home theater group name, no audioDestinationController found for Apple TV: %@"
+ "%@:%@ : Creating New Group: %{BOOL}d / Existing Group: updating components %{BOOL}d/ updating name %{BOOL}d"
+ "%@:%@ : commit media system builders future succeeded... on to next"
+ "%@:%@ Could not find media group with identifier or destinationIdentifiers matching audioDestinationIdentifier: %@"
+ "%@:%@ nil home for home theater system. Returning HF_CURRENT_HOME."
+ "%@:%@ nil home. This is lame. If we  are ungrouping a media group, this is expected (though lame), but otherwise we should fix this case. (See code comment above.)"
+ "%@:%@: rooms for mediaGroup %@"
+ "%s Creating new HFHomeKitSettingsAdapterManager for HMMediaGroup %@"
+ "%s: No elements found for media group %@"
+ "%s: No leaf elements found for media group %@"
+ "-[HMMediaGroup(HFIncludedContextProtocol) hf_updateValue:forContextType:]"
+ "-[HMMediaGroup(HFMediaGroupAdditions) hf_settingsAdapterManager]"
+ "@\"<NSCopying>\"16@?0@\"<HFMediaProfileContainer>\"8"
+ "@\"NSNumber\"16@?0@\"HMAccessory\"8"
+ "@16@?0@\"<HMMediaDestination>\"8"
+ "@16@?0@\"HFMediaSystemBuilder\"8"
+ "@16@?0@\"HMMediaGroup\"8"
+ "Accessory Supports Music Alarm (%@) mediaProfileContainer %@"
+ "AirPort Express In PermanentSpeakerGroup"
+ "AppleTV In HomeTheaterSystem"
+ "Audio Receiver in PermanentSpeakerGroup"
+ "B16@?0@\"HFMediaSystemBuilder\"8"
+ "B16@?0@\"HMHomeTheaterSystem\"8"
+ "B16@?0@\"HMMediaGroup\"8"
+ "Did find media group object: %@, from accessory: %@"
+ "Dumb Speaker In PermanentSpeakerGroup"
+ "HAP Speaker In PermanentSpeakerGroup"
+ "HFImageIconIdentifierSurroundMixed"
+ "HFImageIconIdentifierSurroundMixedTile"
+ "HFMediaGroupBuilder.createMediaGroup"
+ "HFMediaGroupBuilder.updateApplicationDataForContextType"
+ "HFMediaGroupBuilder.updateMediaGroup"
+ "HFNamingComponents_DefaultHomeTheaterName_Capitalized"
+ "HFNamingComponents_DefaultSpeakerGroupName_Capitalized"
+ "HFNamingComponents_DefaultSpeakerGroupName_Lowercase"
+ "HFResultRoomSpeakerCountKey"
+ "HFSensitiveStrings-AudioGrouping"
+ "HFTitleSurroundSetupTile"
+ "HF_PermanentSpeakerGroups"
+ "HMMediaGroup is a composite of several objects, and does not support fetching logs"
+ "Hiding setting group %@ for %@ because it is contained within a media group"
+ "Home theater system has symptoms: %@"
+ "Home theater system: %@, has symptoms: %@"
+ "HomePod StereoPair In PermanentSpeakerGroup"
+ "HomeTheaterSurround"
+ "IgnoreSpeakerGroupingErrors"
+ "Include in status is not configured by HFMediaGroupBuilder."
+ "Media group accessory: %@, has symptoms: %@"
+ "Media system is part of home theater, returning group: %@"
+ "Permanent Speaker Group"
+ "Removing media group '%@' from home '%@'"
+ "Single HomePod In PermanentSpeakerGroup"
+ "Surround system is part of home theater, returning home theater group: %@"
+ "d0d2700c4dee4686a15d55"
+ "hf_speakerGroup: FOUND matching group by destinationIdentifiers: %@"
+ "hf_speakerGroup: FOUND matching group by identifier: %@"
+ "hf_speakerGroup: checking group %@ identifier=%@, destinationIdentifiers=%@"
+ "hf_speakerGroup: looking for audioDestinationIdentifier=%@ in %lu groups"
+ "hifispeaker.2.fill"
+ "hifispeaker.and.homepod.fill"
+ "hifispeaker.and.homepodmini.fill"
+ "homepod.and.appletv.fill"
+ "homepod.and.homepodmini.fill"
+ "homepodmini.and.appletv.fill"
+ "https://support.apple.com/en-us/102357"
+ "mediaGroupType"
+ "v16@?0@\"HMHomeTheaterSystem\"8"
+ "v16@?0@\"HMMediaProfile\"8"
+ "v32@?0@\"HMMediaGroup\"8Q16^B24"
```
