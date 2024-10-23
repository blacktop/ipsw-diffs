## SiriAudioSupport

> `/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport`

```diff

-3401.22.2.0.0
-  __TEXT.__text: 0x21b280
-  __TEXT.__auth_stubs: 0x37c0
+3402.51.1.1.2
+  __TEXT.__text: 0x224494
+  __TEXT.__auth_stubs: 0x38f0
   __TEXT.__objc_methlist: 0x81c
-  __TEXT.__const: 0x93e8
-  __TEXT.__cstring: 0xb100
-  __TEXT.__swift5_typeref: 0x3fa5
-  __TEXT.__swift5_fieldmd: 0x4280
-  __TEXT.__constg_swiftt: 0x59a4
+  __TEXT.__const: 0xa328
+  __TEXT.__cstring: 0xb330
+  __TEXT.__swift5_typeref: 0x4239
+  __TEXT.__swift5_fieldmd: 0x4494
+  __TEXT.__constg_swiftt: 0x5cb8
   __TEXT.__swift5_builtin: 0x2f8
-  __TEXT.__swift5_reflstr: 0x464c
-  __TEXT.__swift5_assocty: 0x570
+  __TEXT.__swift5_reflstr: 0x483c
+  __TEXT.__swift5_assocty: 0x648
   __TEXT.__swift5_protos: 0x118
-  __TEXT.__swift5_proto: 0x548
-  __TEXT.__swift5_types: 0x408
-  __TEXT.__swift5_capture: 0x54e4
-  __TEXT.__oslogstring: 0x1fdce
+  __TEXT.__swift5_proto: 0x630
+  __TEXT.__swift5_types: 0x43c
+  __TEXT.__swift5_capture: 0x5430
+  __TEXT.__oslogstring: 0x1f93e
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x45f8
-  __TEXT.__eh_frame: 0x255c
+  __TEXT.__unwind_info: 0x4aa8
+  __TEXT.__eh_frame: 0x3424
   __TEXT.__objc_classname: 0x19c
-  __TEXT.__objc_methname: 0x61fb
-  __TEXT.__objc_methtype: 0x5c5
-  __DATA_CONST.__got: 0x10f8
-  __DATA_CONST.__const: 0x818
-  __DATA_CONST.__objc_classlist: 0x2e0
+  __TEXT.__objc_methname: 0x6280
+  __TEXT.__objc_methtype: 0x696
+  __DATA_CONST.__got: 0x1118
+  __DATA_CONST.__const: 0x888
+  __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cd8
+  __DATA_CONST.__objc_selrefs: 0x1ce0
   __DATA_CONST.__objc_protorefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x1be0
-  __AUTH_CONST.__auth_ptr: 0x1610
-  __AUTH_CONST.__const: 0x15010
+  __AUTH_CONST.__auth_got: 0x1c78
+  __AUTH_CONST.__auth_ptr: 0x17f0
+  __AUTH_CONST.__const: 0x15388
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0xb268
-  __AUTH.__objc_data: 0x1008
-  __AUTH.__data: 0x5a60
-  __DATA.__data: 0x2c18
-  __DATA.__bss: 0x6f10
-  __DATA.__common: 0x280
+  __AUTH_CONST.__objc_const: 0xb518
+  __AUTH.__objc_data: 0x1128
+  __AUTH.__data: 0x5d20
+  __DATA.__data: 0x2ff8
+  __DATA.__bss: 0x8b90
+  __DATA.__common: 0x2e8
   __DATA_DIRTY.__objc_data: 0xd0
   __DATA_DIRTY.__data: 0x28
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/StoreKit.framework/StoreKit
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics
+  - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8450
-  Symbols:   1002
-  CStrings:  4086
+  Functions: 8760
+  Symbols:   998
+  CStrings:  4105
 
Symbols:
+ _OBJC_CLASS_$_LNEnvironment
+ __swift_FORCE_LOAD_$_swiftAppleArchive
- _MPMediaPlaylistPropertyCloudGlobalID
- _OBJC_CLASS_$_MPMediaCompoundAllPredicate
CStrings:
+ "AppIntentInvoker#followShowAppIntent has returned an error: %!@(MISSING)"
+ "AppIntentInvoker#followShowAppIntent response: %!s(MISSING)"
+ "AppIntentInvoker#invokeOpenMusicItemIntent OpenMusicItemAppIntent constructed with itemEntity: %!s(MISSING) and noticeEntity: %!s(MISSING)"
+ "AppIntentInvoker#invokeOpenMusicItemIntent response: %!s(MISSING)"
+ "AppIntentInvoker#invokeOpenPodcastChannelAppIntent response: %!s(MISSING)"
+ "AppIntentInvoker#invokeOpenPodcastEpisodeAppIntent response: %!s(MISSING)"
+ "AppIntentInvoker#invokeOpenPodcastShowAppIntent response: %!s(MISSING)"
+ "AppIntentInvoker#invokeOpenQueueAppIntent"
+ "AppIntentInvoker#invokeOpenQueueAppIntent response: %!s(MISSING)"
+ "AppIntentInvoker#invokeSearchMusicAppIntent response: %!s(MISSING)"
+ "AppIntentInvoker#invokeSearchMusicAppIntent with criteria: %!s(MISSING), searchSource: %!s(MISSING), and mediaType: %!s(MISSING)"
+ "HistoryStats cannot add instance from the future"
+ "Identifier#toMusicSiriRepresentation failed to create musicSiriRepresentation from source: %!s(MISSING), type: %!s(MISSING), and identifier: %!s(MISSING)"
+ "LastNowPlayingSignal#signal For bundle %!s(MISSING) - recency: %!s(MISSING) frequencies: %!s(MISSING)"
+ "MusicSiriRepresentation#from Failed to create valid URL for library content"
+ "MusicSiriRepresentation#from Failed to create valid URL for store content"
+ "MusicSiriRepresentation#from called with source = %!s(MISSING), type = %!s(MISSING), and identifier = %!s(MISSING)"
+ "MusicSiriRepresentation#from returning %!s(MISSING)"
+ "MusicSiriRepresentation#from unknown source type, returning nil"
+ "NowPlayingUsageProvider#affinity (lazy load) For bundle %!s(MISSING) - recency: %!s(MISSING) frequencies: %!s(MISSING)"
+ "OpenChannelAppIntent"
+ "OpenEpisodeAppIntent"
+ "OpenShowAppIntent"
+ "PrivateMediaIntentDataProviding#isUserConfidenceEnoughToBeRecognized %!{(MISSING)bool}d for confidence from PrivateMediaIntentData: %!l(MISSING)d"
+ "PrivateMediaIntentDataProviding#isUserConfidenceEnoughToBeRecognized %!{(MISSING)bool}d for confidence from SiriEnvironment.UserIdentityProvider: %!l(MISSING)d"
+ "PrivateMediaIntentDataProviding#isUserConfidenceEnoughToBeRecognized speakerID confidence: %!s(MISSING)"
+ "PrivateMediaIntentDataProviding#isUserConfidenceEnoughToBeRecognized userClassification confidence: %!s(MISSING)"
+ "PrivateMediaIntentDataProviding#sharedUserID and SiriEnvironment.UserIdentityProvider no sharedUserID"
+ "SiriKitTaskLoggingProvider#convertToSearchResults setting nls to %!{(MISSING)bool}d and %!{(MISSING)bool}d"
+ "_TtC16SiriAudioSupport16AppIntentInvoker"
+ "_TtC16SiriAudioSupport17PodcastShowEntity"
+ "_TtC16SiriAudioSupport20PodcastChannelEntity"
+ "_TtC16SiriAudioSupport20PodcastEpisodeEntity"
+ "_TtC16SiriAudioSupport22GenericMusicItemEntity"
+ "_TtC16SiriAudioSupport23AppIntentInvokerContext"
+ "addToQueue"
+ "addedToPlaylist"
+ "appIntentInvokerFailureMusic"
+ "appIntentInvokerFailurePodcasts"
+ "com.apple.nowplaying"
+ "defaultEnvironment"
+ "failedToConvertMusicSiriRepresentation"
+ "failedToConvertPlaybackIdentifier"
+ "favorited"
+ "handlePaymentSheetRequest:purchase:purchaseQueue:completion:"
+ "libraryAdded"
+ "localDispatcher"
+ "missingPommesResponse"
+ "noResultsDlg"
+ "noSearchResults"
+ "omif"
+ "openMediaItem"
+ "playAfter"
+ "playLast"
+ "playNext"
+ "purchase:handlePaymentSheetRequest:completion:"
+ "suggestLess"
+ "unfavorited"
+ "v40@0:8@\"AMSPurchase\"16@\"AMSPaymentSheetRequest\"24@?<v@?@\"AMSPaymentSheetResult\"@\"NSError\">32"
+ "v48@0:8@\"AMSPaymentSheetRequest\"16@\"AMSPurchase\"24@\"AMSPurchaseQueue\"32@?<v@?@\"AMSPaymentSheetResult\"@\"NSError\">40"
- "CompoundPredicateIsNil"
- "InvalidItemIdentifierType"
- "InvalidStoreItemIdentifierType"
- "LastNowPlayingSignal#signal For bundle %!s(MISSING) - recency: %!s(MISSING) frequencies: f2min:%!l(MISSING)d f10min:%!l(MISSING)d f1hr:%!l(MISSING)d f6hr:%!l(MISSING)d f1day:%!l(MISSING)d f7day:%!l(MISSING)d f28day:%!l(MISSING)d"
- "MediaIntentCommons#getSharedUserID from MultiUserConnectionProvider sharedUserID = %!s(MISSING)"
- "MediaIntentCommons#getSharedUserID from SiriEnvironment sharedUserID = %!s(MISSING), speakerIDConfidence = %!s(MISSING)"
- "MediaIntentCommons#getSharedUserID from intent sharedUserID = %!s(MISSING), speakerIDConfidence = %!s(MISSING)"
- "MediaIntentCommons#getSharedUserID self.privateMediaIntentData = %!s(MISSING)"
- "MediaIntentCommons#getSharedUserID sharedUserID not found"
- "No identifier received"
- "No local item storeID"
- "NoLocalItemStoreID"
- "NowPlayingUsageProvider#affinity (lazy load) For bundle %!s(MISSING) - recency: %!s(MISSING) frequencies: f2min:%!l(MISSING)d f10min:%!l(MISSING)d f1hr:%!l(MISSING)d f6hr:%!l(MISSING)d f1day:%!l(MISSING)d f7day:%!l(MISSING)d f28day:%!l(MISSING)d"
- "OnePredicateIsNil"
- "Pilot item: %!s(MISSING)"
- "PrivateMediaIntentDataProviding#isUserConfidenceEnoughToBeRecognized %!{(MISSING)bool}d for confidence: %!l(MISSING)d"
- "PrivateMediaIntentDataProviding#isUserConfidenceEnoughToBeRecognized speakerID confidence: %!l(MISSING)d"
- "PrivateMediaIntentDataProviding#sharedUserID no speakerIDInfo"
- "RemoteAlbumPlaybackHandler#preLoadQueueForMediaItemsFromStoreIdentifiers for %!{(MISSING)public}s with onlyPlayableItems: %!{(MISSING)bool,public}d"
- "RemotePlaybackHandler#playSelectedQuery No for-you cache"
- "RemotePlaybackHandler#preLoadQueue RemotePLaybackHandler#preLoadQueue Local search failed. Trying remote play"
- "RemotePlaybackHandler#preLoadQueue SharedUserID isn't empty and assetInfo is, passing to MediaItemsFromStoreIdentifiers"
- "RemotePlaybackHandler#preLoadQueueForMediaItemsFromStoreIdentifiers Unknown scheme passed in %!s(MISSING)"
- "RemoteSongPlaybackHandler#getItemsToPlay Found items in songQuery: %!{(MISSING)public}s. Appending to localItem list"
- "RemoteSongPlaybackHandler#getItemsToPlay Looking for only local items, attaching MPMediaItemPropertyIsLocal to MPMediaQuery"
- "RemoteSongPlaybackHandler#getItemsToPlay MPMediaCompoundPredicate is nil"
- "RemoteSongPlaybackHandler#getItemsToPlay No local item"
- "RemoteSongPlaybackHandler#getItemsToPlay Not looking for only localy items, attaching MPMediaItemPropertyIsPlayable to MPMediaQuery"
- "RemoteSongPlaybackHandler#getItemsToPlay One of the predicates is nil"
- "RemoteSongPlaybackHandler#getItemsToPlay Returning items to play %!{(MISSING)public}s"
- "RemoteSongPlaybackHandler#preLoadQueueForMediaItemsFromStoreIdentifiers Appending %!{(MISSING)public}s to storeIDsToPlay"
- "RemoteSongPlaybackHandler#preLoadQueueForMediaItemsFromStoreIdentifiers Attaching media library"
- "RemoteSongPlaybackHandler#preLoadQueueForMediaItemsFromStoreIdentifiers Collection doesn't have any subItems. Using collection identifier instead"
- "RemoteSongPlaybackHandler#preLoadQueueForMediaItemsFromStoreIdentifiers Content origin not store. contentOrigin: %!{(MISSING)public}s"
- "RemoteSongPlaybackHandler#preLoadQueueForMediaItemsFromStoreIdentifiers Number of items in selectedQuery: %!{(MISSING)public}s"
- "RemoteSongPlaybackHandler#preLoadQueueForMediaItemsFromStoreIdentifiers Unable to parse %!s(MISSING) as an int"
- "RemoteSongPlaybackHandler#preLoadQueueForMediaItemsFromStoreIdentifiers Unable to parse %!{(MISSING)public}s as an int"
- "RemoteSongPlaybackHandler#preLoadQueueForMediaItemsFromStoreIdentifiers searching locally for remote song"
- "SiriRemembersV1API.Aggregation#addInstance cannot add instance from the future"
- "Unable to parse %!s(MISSING) as an int"
- "UnknownSchemeInItemID"
- "albumsQuery"
- "playlistsQuery"

```
