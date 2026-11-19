## MediaPlayer

> `/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/A/MediaPlayer`

```diff

-4026.140.2.0.0
-  __TEXT.__text: 0x21b390
-  __TEXT.__objc_methlist: 0x2196c
+4026.240.1.0.0
+  __TEXT.__text: 0x21bacc
+  __TEXT.__objc_methlist: 0x2179c
   __TEXT.__const: 0x4d90
-  __TEXT.__cstring: 0x29ba5
-  __TEXT.__oslogstring: 0xfee0
-  __TEXT.__gcc_except_tab: 0xa428
+  __TEXT.__cstring: 0x29ce5
+  __TEXT.__oslogstring: 0xfe90
+  __TEXT.__gcc_except_tab: 0xa480
   __TEXT.__dlopen_cstrs: 0x25c
   __TEXT.__ustring: 0x1dc
   __TEXT.__constg_swiftt: 0x32c

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x9ee8
+  __TEXT.__unwind_info: 0x9ed8
   __TEXT.__eh_frame: 0x4a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xadd8
-  __DATA_CONST.__objc_classlist: 0x1130
+  __DATA_CONST.__const: 0xae08
+  __DATA_CONST.__objc_classlist: 0x1110
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x103c8
+  __DATA_CONST.__objc_selrefs: 0x10390
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0xbc8
-  __DATA_CONST.__objc_arraydata: 0x818
-  __DATA_CONST.__got: 0x1e90
-  __AUTH_CONST.__const: 0x4b00
-  __AUTH_CONST.__cfstring: 0x204a0
-  __AUTH_CONST.__objc_const: 0x38898
+  __DATA_CONST.__objc_superrefs: 0xbb0
+  __DATA_CONST.__objc_arraydata: 0x828
+  __DATA_CONST.__got: 0x1ed8
+  __AUTH_CONST.__const: 0x4b80
+  __AUTH_CONST.__cfstring: 0x20600
+  __AUTH_CONST.__objc_const: 0x38288
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x348
-  __AUTH_CONST.__objc_arrayobj: 0xe70
+  __AUTH_CONST.__objc_arrayobj: 0xea0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__auth_got: 0x1c70
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x7130
+  __AUTH.__objc_data: 0x6ff0
   __AUTH.__data: 0x100
-  __DATA.__objc_ivar: 0x2278
+  __DATA.__objc_ivar: 0x2228
   __DATA.__data: 0x2c30
-  __DATA.__bss: 0x1bd0
+  __DATA.__bss: 0x1bf0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x3b10
   __DATA_DIRTY.__data: 0x100

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13729
-  Symbols:   30051
-  CStrings:  5940
+  Functions: 13703
+  Symbols:   29984
+  CStrings:  5950
 
Symbols:
+ +[MPModelAlbum __MPModelPropertyAlbumCloudChannelName__MAPPING_MISSING__]
+ +[MPModelAlbum __MPModelPropertyAlbumIsFollowed__MAPPING_MISSING__]
+ +[MPModelAlbum __MPModelPropertyAlbumShouldShowCountdownTimer__MAPPING_MISSING__]
+ +[MPModelAlbum __cloudChannelName_KEY]
+ +[MPModelAlbum __isFollowed_KEY]
+ +[MPModelAlbum __shouldShowCountdownTimer_KEY]
+ +[MPModelRadioStation __MPModelPropertyRadioStationEditorialArtworks__MAPPING_MISSING__]
+ +[MPModelRadioStation __editorialArtworksBlock_KEY]
+ -[MPAVRoute isActuallyW1Route]
+ -[MPAVRoute isWXRoute]
+ -[MPModelRadioStation editorialArtworks]
+ -[MPStoreItemMetadata expectedAvailableDateTime]
+ -[MPVolumeHardwareButtonController _isForeground]
+ -[MPVolumeHardwareButtonController _registerForButtonNotifications]
+ -[MPVolumeHardwareButtonController _unregisterForButtonNotifications]
+ -[MPVolumeHardwareButtonController _updateButtonNotificationRegistration]
+ GCC_except_table170
+ GCC_except_table193
+ MPArtworkResizeOperationDrawSerializationQueue.sOnceToken
+ MPArtworkResizeOperationDrawSerializationQueue.sQueue
+ OBJC_IVAR_$_MPVolumeHardwareButtonController._didEverRegisterForButtonNotifications
+ _MPModelPropertyAlbumCloudChannelName
+ _MPModelPropertyAlbumIsFollowed
+ _MPModelPropertyAlbumShouldShowCountdownTimer
+ _MPModelPropertyRadioStationEditorialArtworks
+ _MPStoreItemMetadataEditorialArtworkKindSuperHeroTall
+ _MPStorePlatformDateAndTimeFromString.sOnceToken
+ _MPStorePlatformDateAndTimeFromString.storePlatformDateAndTimeFormatter
+ _MRNowPlayingInfoContentTypeBook
+ _MRNowPlayingInfoContentTypeGeneric
+ _MRNowPlayingInfoContentTypeMusic
+ _MRNowPlayingInfoContentTypePodcast
+ _MRNowPlayingInfoContentTypeRadio
+ _MRNowPlayingInfoMediaTypeAudio
+ _MRNowPlayingInfoMediaTypeVideo
+ _UISceneDidActivateNotification
+ _UISceneDidDisconnectNotification
+ _UISceneDidEnterBackgroundNotification
+ __MRMediaRemoteStrictMediaTypeForMPNowPlayingMediaType
+ ___32-[MPArtworkResizeOperation main]_block_invoke_2
+ ___53-[MPStoreItemMetadata editorialArtworksRequestTokens]_block_invoke_2
+ ___99-[MPStoreModelRadioStationBuilder modelObjectWithStoreItemMetadata:sourceModelObject:userIdentity:]_block_invoke_8
+ ___99-[MPStoreModelRadioStationBuilder modelObjectWithStoreItemMetadata:sourceModelObject:userIdentity:]_block_invoke_9
+ ___MPArtworkResizeOperationDrawSerializationQueue_block_invoke
+ ___MPStorePlatformInitPropertyAlbumMap_block_invoke_13
+ ____MPMediaKitInitPropertyAlbumMap_block_invoke_21
+ ____MPStorePlatformDateAndTimeFromString_block_invoke
+ ____MPStorePlatformInitPropertyAlbumMap_block_invoke_15
+ ___block_descriptor_105_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_40_e8_32s_e22_v16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32s_e43_"NSDictionary"16?0"MPModelRadioStation"8ls32l8
+ _kMRMediaRemoteNowPlayingInfoContentType
+ _kMRMediaRemoteNowPlayingInfoStrictMediaType
+ _objc_msgSend$_isForeground
+ _objc_msgSend$_registerForButtonNotifications
+ _objc_msgSend$_unregisterForButtonNotifications
+ _objc_msgSend$_updateButtonNotificationRegistration
+ _objc_msgSend$activationState
+ _objc_msgSend$connectedScenes
+ _objc_msgSend$expectedAvailableDateTime
+ _objc_msgSend$isActuallyW1Route
+ _objc_msgSend$isWXDeviceWithModelID:
+ _objc_msgSend$isWatch
+ _objc_msgSend$setCloudChannelName:
+ _objc_msgSend$setIsFollowed:
+ _objc_msgSend$setShouldShowCountdownTimer:
- +[MPCloudEntityUpdateRegistration allLibraryAlbumsRegistration]
- -[MPCloudController registerForUpdatesWithRegistration:updateHandler:completionHandler:]
- -[MPCloudController unregisterForUpdatesUsingHandle:]
- -[MPCloudController unregisterUpdatesForChannelID:reason:]
- -[MPCloudEntityUpdate .cxx_destruct]
- -[MPCloudEntityUpdate _initWithICUpdate:]
- -[MPCloudEntityUpdate channelIDs]
- -[MPCloudEntityUpdate copyWithZone:]
- -[MPCloudEntityUpdate description]
- -[MPCloudEntityUpdate error]
- -[MPCloudEntityUpdate pushMessage]
- -[MPCloudEntityUpdate resubscribeReason]
- -[MPCloudEntityUpdate type]
- -[MPCloudEntityUpdate unsubscribeReason]
- -[MPCloudEntityUpdatePushMessage .cxx_destruct]
- -[MPCloudEntityUpdatePushMessage _initWithICPushMessage:]
- -[MPCloudEntityUpdatePushMessage channelID]
- -[MPCloudEntityUpdatePushMessage contentType]
- -[MPCloudEntityUpdatePushMessage copyWithZone:]
- -[MPCloudEntityUpdatePushMessage description]
- -[MPCloudEntityUpdatePushMessage goLiveDate]
- -[MPCloudEntityUpdatePushMessage isRelevantForCatalogEntity]
- -[MPCloudEntityUpdatePushMessage isRelevantForLibraryEntity]
- -[MPCloudEntityUpdatePushMessage receivedDate]
- -[MPCloudEntityUpdatePushMessage relevanceBitmask]
- -[MPCloudEntityUpdatePushMessage storeID]
- -[MPCloudEntityUpdatePushMessage storefront]
- -[MPCloudEntityUpdateRegistration .cxx_destruct]
- -[MPCloudEntityUpdateRegistration _icConfiguration]
- -[MPCloudEntityUpdateRegistration channelID]
- -[MPCloudEntityUpdateRegistration copyWithZone:]
- -[MPCloudEntityUpdateRegistration description]
- -[MPCloudEntityUpdateRegistration entityType]
- -[MPCloudEntityUpdateRegistration expectedReleaseDate]
- -[MPCloudEntityUpdateRegistration initWithChannelID:entityType:storeID:reason:expectedReleaseDate:]
- -[MPCloudEntityUpdateRegistration observesAllLibraryAlbums]
- -[MPCloudEntityUpdateRegistration reason]
- -[MPCloudEntityUpdateRegistration storeID]
- -[MPPlaybackContextRemotePlaybackQueue .cxx_destruct]
- -[MPPlaybackContextRemotePlaybackQueue asMusicPlaybackContextWithOptions:error:]
- -[MPPlaybackContextRemotePlaybackQueue description]
- -[MPPlaybackContextRemotePlaybackQueue initWithPlaybackContext:]
- -[MPPlaybackContextRemotePlaybackQueue isRequestingImmediatePlayback]
- -[MPPlaybackContextRemotePlaybackQueue privateListeningOverride]
- -[MPPlaybackContextRemotePlaybackQueue replaceIntent]
- -[MPPlaybackContextRemotePlaybackQueue setReplaceIntent:]
- -[MPPlaybackContextRemotePlaybackQueue siriAssetInfo]
- -[MPPlaybackContextRemotePlaybackQueue siriRecommendationIdentifier]
- -[MPPlaybackContextRemotePlaybackQueue siriWHAMetricsInfo]
- -[MPVolumeHardwareButtonController _applicationDidBecomeActiveNotification]
- -[MPVolumeHardwareButtonController _registerForButtonNotificationsIfNeeded]
- -[MPVolumeHardwareButtonController _unregisterForButtonNotificationsIfNeeded]
- GCC_except_table198
- OBJC_IVAR_$_MPCloudEntityUpdate._channelIDs
- OBJC_IVAR_$_MPCloudEntityUpdate._error
- OBJC_IVAR_$_MPCloudEntityUpdate._pushMessage
- OBJC_IVAR_$_MPCloudEntityUpdate._resubscribeReason
- OBJC_IVAR_$_MPCloudEntityUpdate._type
- OBJC_IVAR_$_MPCloudEntityUpdate._unsubscribeReason
- OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._channelID
- OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._contentType
- OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._goLiveDate
- OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._receivedDate
- OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._relevanceBitmask
- OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._storeID
- OBJC_IVAR_$_MPCloudEntityUpdatePushMessage._storefront
- OBJC_IVAR_$_MPCloudEntityUpdateRegistration._channelID
- OBJC_IVAR_$_MPCloudEntityUpdateRegistration._entityType
- OBJC_IVAR_$_MPCloudEntityUpdateRegistration._expectedReleaseDate
- OBJC_IVAR_$_MPCloudEntityUpdateRegistration._observesAllLibraryAlbums
- OBJC_IVAR_$_MPCloudEntityUpdateRegistration._reason
- OBJC_IVAR_$_MPCloudEntityUpdateRegistration._storeID
- OBJC_IVAR_$_MPPlaybackContextRemotePlaybackQueue._playbackContext
- OBJC_IVAR_$_MPPlaybackContextRemotePlaybackQueue._replaceIntent
- _OBJC_CLASS_$_ICCloudAPNSChannelRegistrationConfiguration
- _OBJC_CLASS_$_ICCloudEntityUpdateRegistrationToken
- _OBJC_CLASS_$_MPCloudEntityUpdate
- _OBJC_CLASS_$_MPCloudEntityUpdatePushMessage
- _OBJC_CLASS_$_MPCloudEntityUpdateRegistration
- _OBJC_CLASS_$_MPPlaybackContextRemotePlaybackQueue
- _OBJC_METACLASS_$_MPCloudEntityUpdate
- _OBJC_METACLASS_$_MPCloudEntityUpdatePushMessage
- _OBJC_METACLASS_$_MPCloudEntityUpdateRegistration
- _OBJC_METACLASS_$_MPPlaybackContextRemotePlaybackQueue
- __OBJC_$_CLASS_METHODS_MPCloudEntityUpdateRegistration
- __OBJC_$_INSTANCE_METHODS_MPCloudEntityUpdate
- __OBJC_$_INSTANCE_METHODS_MPCloudEntityUpdatePushMessage
- __OBJC_$_INSTANCE_METHODS_MPCloudEntityUpdateRegistration
- __OBJC_$_INSTANCE_METHODS_MPPlaybackContextRemotePlaybackQueue
- __OBJC_$_INSTANCE_VARIABLES_MPCloudEntityUpdate
- __OBJC_$_INSTANCE_VARIABLES_MPCloudEntityUpdatePushMessage
- __OBJC_$_INSTANCE_VARIABLES_MPCloudEntityUpdateRegistration
- __OBJC_$_INSTANCE_VARIABLES_MPPlaybackContextRemotePlaybackQueue
- __OBJC_$_PROP_LIST_MPCloudEntityUpdate
- __OBJC_$_PROP_LIST_MPCloudEntityUpdatePushMessage
- __OBJC_$_PROP_LIST_MPCloudEntityUpdateRegistration
- __OBJC_CLASS_PROTOCOLS_$_MPCloudEntityUpdate
- __OBJC_CLASS_PROTOCOLS_$_MPCloudEntityUpdatePushMessage
- __OBJC_CLASS_PROTOCOLS_$_MPCloudEntityUpdateRegistration
- __OBJC_CLASS_RO_$_MPCloudEntityUpdate
- __OBJC_CLASS_RO_$_MPCloudEntityUpdatePushMessage
- __OBJC_CLASS_RO_$_MPCloudEntityUpdateRegistration
- __OBJC_CLASS_RO_$_MPPlaybackContextRemotePlaybackQueue
- __OBJC_METACLASS_RO_$_MPCloudEntityUpdate
- __OBJC_METACLASS_RO_$_MPCloudEntityUpdatePushMessage
- __OBJC_METACLASS_RO_$_MPCloudEntityUpdateRegistration
- __OBJC_METACLASS_RO_$_MPPlaybackContextRemotePlaybackQueue
- ___88-[MPCloudController registerForUpdatesWithRegistration:updateHandler:completionHandler:]_block_invoke
- ___88-[MPCloudController registerForUpdatesWithRegistration:updateHandler:completionHandler:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e29_v16?0"ICCloudEntityUpdate"8ls32l8
- ___block_descriptor_40_e8_32bs_e58_v24?0"ICCloudEntityUpdateRegistrationToken"8"NSError"16ls32l8
- ___block_descriptor_49_e8_32s_e5_v8?0ls32l8
- _objc_msgSend$_icConfiguration
- _objc_msgSend$_initWithICPushMessage:
- _objc_msgSend$_initWithICUpdate:
- _objc_msgSend$_registerForButtonNotificationsIfNeeded
- _objc_msgSend$_unregisterForButtonNotificationsIfNeeded
- _objc_msgSend$allLibraryAlbumsConfiguration
- _objc_msgSend$channelID
- _objc_msgSend$channelIDs
- _objc_msgSend$contentType
- _objc_msgSend$goLiveDate
- _objc_msgSend$initWithChannelID:entityType:storeID:reason:expectedReleaseDate:
- _objc_msgSend$privateListeningOverride
- _objc_msgSend$pushMessage
- _objc_msgSend$receivedDate
- _objc_msgSend$registerForUpdatesWithConfiguration:updateHandler:completionHandler:
- _objc_msgSend$relevanceBitmask
- _objc_msgSend$resubscribeReason
- _objc_msgSend$storefront
- _objc_msgSend$unregisterForUpdatesToMonitoredEntityUsingToken:
- _objc_msgSend$unregisterUpdatesForChannelID:reason:
- _objc_msgSend$unsubscribeReason
CStrings:
+ "@\"NSDictionary\"16@?0@\"MPModelRadioStation\"8"
+ "HomeAccessory"
+ "MPModelPropertyAlbumCloudChannelName"
+ "MPModelPropertyAlbumIsFollowed"
+ "MPModelPropertyAlbumShouldShowCountdownTimer"
+ "MPModelPropertyRadioStationEditorialArtworks"
+ "MPVolumeHardwareButtonController.m"
+ "Translator was missing mapping for MPModelPropertyAlbumCloudChannelName"
+ "Translator was missing mapping for MPModelPropertyAlbumIsFollowed"
+ "Translator was missing mapping for MPModelPropertyAlbumShouldShowCountdownTimer"
+ "Translator was missing mapping for MPModelPropertyRadioStationEditorialArtworks"
+ "UIApplication and scene state must be read on the main thread."
+ "[HardwareButtonController] Registering for hardware volume button events"
+ "[HardwareButtonController] Unregistering for hardware volume button events"
+ "attributes.expectedAvailableDateTime"
+ "com.apple.mediaplayer.artworkservice.resizing.drawSerialization"
+ "editorialCard"
+ "expectedAvailableDateTime"
+ "plainEditorialCard"
- "<%@ %p channelID=%@ contentType=%ld storeID=%lld storefront=%@ goLiveDate=%@ relevanceBitmask=0x%llx receivedDate=%@>"
- "<%@ %p channelID=%@ entityType=%ld storeID=%lld reason=%ld expectedReleaseDate=%@ observesAllLibraryAlbums=%d>"
- "<%@ %p type=%ld pushMessage=%@ error=%@ channelIDs=%@ unsubscribeReason=%ld resubscribeReason=%ld>"
- "<%@: %p, playbackContext=%@>"
- "MPCloudController - register got unexpected token class %@; treating as failure."
- "MPCloudController - unregister received handle of unexpected class %@; ignoring."
- "MPCloudController - unregister received nil handle; ignoring."
- "v16@?0@\"ICCloudEntityUpdate\"8"
- "v24@?0@\"ICCloudEntityUpdateRegistrationToken\"8@\"NSError\"16"
```
