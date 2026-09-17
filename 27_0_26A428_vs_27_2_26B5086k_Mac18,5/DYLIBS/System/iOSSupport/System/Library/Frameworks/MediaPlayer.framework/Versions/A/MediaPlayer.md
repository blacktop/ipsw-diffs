## MediaPlayer

> `/System/iOSSupport/System/Library/Frameworks/MediaPlayer.framework/Versions/A/MediaPlayer`

```diff

-4026.140.2.0.0
-  __TEXT.__text: 0x20d444
-  __TEXT.__objc_methlist: 0x2196c
+4026.200.12.0.0
+  __TEXT.__text: 0x20dea8
+  __TEXT.__objc_methlist: 0x21964
   __TEXT.__const: 0x4d90
-  __TEXT.__cstring: 0x29ba5
+  __TEXT.__cstring: 0x29dd5
   __TEXT.__oslogstring: 0xfee0
-  __TEXT.__gcc_except_tab: 0xa428
+  __TEXT.__gcc_except_tab: 0xa480
   __TEXT.__dlopen_cstrs: 0x25c
   __TEXT.__ustring: 0x1dc
   __TEXT.__constg_swiftt: 0x32c

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xc1f0
+  __TEXT.__unwind_info: 0xc240
   __TEXT.__eh_frame: 0x4a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xadd8
-  __DATA_CONST.__objc_classlist: 0x1130
+  __DATA_CONST.__const: 0xae58
+  __DATA_CONST.__objc_classlist: 0x1128
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x103c8
+  __DATA_CONST.__objc_selrefs: 0x10428
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0xbc8
   __DATA_CONST.__objc_arraydata: 0x818
-  __DATA_CONST.__got: 0x1e90
-  __AUTH_CONST.__const: 0x4b00
-  __AUTH_CONST.__cfstring: 0x204a0
-  __AUTH_CONST.__objc_const: 0x38898
+  __DATA_CONST.__got: 0x1ee0
+  __AUTH_CONST.__const: 0x4b20
+  __AUTH_CONST.__cfstring: 0x205c0
+  __AUTH_CONST.__objc_const: 0x38828
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0xe70
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__auth_got: 0x1c70
-  __AUTH.__objc_data: 0x7130
+  __AUTH.__objc_data: 0x70e0
   __AUTH.__data: 0x100
-  __DATA.__objc_ivar: 0x2278
+  __DATA.__objc_ivar: 0x2270
   __DATA.__data: 0x2c30
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x3b10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13729
-  Symbols:   30051
-  CStrings:  5940
+  Functions: 13736
+  Symbols:   30071
+  CStrings:  5951
 
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
+ MPArtworkResizeOperationDrawSerializationQueue.sOnceToken
+ MPArtworkResizeOperationDrawSerializationQueue.sQueue
+ _MPModelPropertyAlbumCloudChannelName
+ _MPModelPropertyAlbumIsFollowed
+ _MPModelPropertyAlbumShouldShowCountdownTimer
+ _MPModelPropertyRadioStationEditorialArtworks
+ _MPStoreItemMetadataEditorialArtworkKindSuperHeroTall
+ _MRNowPlayingInfoContentTypeBook
+ _MRNowPlayingInfoContentTypeGeneric
+ _MRNowPlayingInfoContentTypeMusic
+ _MRNowPlayingInfoContentTypePodcast
+ _MRNowPlayingInfoContentTypeRadio
+ _MRNowPlayingInfoMediaTypeAudio
+ _MRNowPlayingInfoMediaTypeVideo
+ __MRMediaRemoteStrictMediaTypeForMPNowPlayingMediaType
+ ___32-[MPArtworkResizeOperation main]_block_invoke_2
+ ___53-[MPStoreItemMetadata editorialArtworksRequestTokens]_block_invoke_2
+ ___99-[MPStoreModelRadioStationBuilder modelObjectWithStoreItemMetadata:sourceModelObject:userIdentity:]_block_invoke_8
+ ___99-[MPStoreModelRadioStationBuilder modelObjectWithStoreItemMetadata:sourceModelObject:userIdentity:]_block_invoke_9
+ ___MPArtworkResizeOperationDrawSerializationQueue_block_invoke
+ ___block_descriptor_105_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_40_e8_32s_e22_v16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32s_e43_"NSDictionary"16?0"MPModelRadioStation"8ls32l8
+ _kMRMediaRemoteNowPlayingInfoContentType
+ _kMRMediaRemoteNowPlayingInfoStrictMediaType
+ _objc_msgSend$isActuallyW1Route
+ _objc_msgSend$isWXDeviceWithModelID:
+ _objc_msgSend$setCloudChannelName:
+ _objc_msgSend$setIsFollowed:
+ _objc_msgSend$setShouldShowCountdownTimer:
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
- OBJC_IVAR_$_MPPlaybackContextRemotePlaybackQueue._playbackContext
- OBJC_IVAR_$_MPPlaybackContextRemotePlaybackQueue._replaceIntent
- _OBJC_CLASS_$_MPPlaybackContextRemotePlaybackQueue
- _OBJC_METACLASS_$_MPPlaybackContextRemotePlaybackQueue
- __OBJC_$_INSTANCE_METHODS_MPPlaybackContextRemotePlaybackQueue
- __OBJC_$_INSTANCE_VARIABLES_MPPlaybackContextRemotePlaybackQueue
- __OBJC_CLASS_RO_$_MPPlaybackContextRemotePlaybackQueue
- __OBJC_METACLASS_RO_$_MPPlaybackContextRemotePlaybackQueue
- ___block_descriptor_49_e8_32s_e5_v8?0ls32l8
- _objc_msgSend$privateListeningOverride
CStrings:
+ "@\"NSDictionary\"16@?0@\"MPModelRadioStation\"8"
+ "MPModelPropertyAlbumCloudChannelName"
+ "MPModelPropertyAlbumIsFollowed"
+ "MPModelPropertyAlbumShouldShowCountdownTimer"
+ "MPModelPropertyRadioStationEditorialArtworks"
+ "Translator was missing mapping for MPModelPropertyAlbumCloudChannelName"
+ "Translator was missing mapping for MPModelPropertyAlbumIsFollowed"
+ "Translator was missing mapping for MPModelPropertyAlbumShouldShowCountdownTimer"
+ "Translator was missing mapping for MPModelPropertyRadioStationEditorialArtworks"
+ "com.apple.mediaplayer.artworkservice.resizing.drawSerialization"
+ "editorialCard"
+ "plainEditorialCard"
- "<%@: %p, playbackContext=%@>"
```
