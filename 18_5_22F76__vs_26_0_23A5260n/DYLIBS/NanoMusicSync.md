## NanoMusicSync

> `/System/Library/PrivateFrameworks/NanoMusicSync.framework/NanoMusicSync`

```diff

-2022.500.7.0.0
-  __TEXT.__text: 0x4d4e0
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_methlist: 0x418c
-  __TEXT.__const: 0x240
-  __TEXT.__gcc_except_tab: 0xaf4
-  __TEXT.__cstring: 0x34d7
-  __TEXT.__oslogstring: 0x7706
-  __TEXT.__dlopen_cstrs: 0xf3
-  __TEXT.__unwind_info: 0x1278
+2023.100.45.0.0
+  __TEXT.__text: 0x4d898
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_methlist: 0x41a4
+  __TEXT.__const: 0x230
+  __TEXT.__gcc_except_tab: 0xa78
+  __TEXT.__cstring: 0x34f4
+  __TEXT.__oslogstring: 0x79ba
+  __TEXT.__unwind_info: 0x1240
   __TEXT.__objc_classname: 0xa3e
-  __TEXT.__objc_methname: 0xb925
+  __TEXT.__objc_methname: 0xba4a
   __TEXT.__objc_methtype: 0x15a0
-  __TEXT.__objc_stubs: 0x8700
-  __DATA_CONST.__got: 0x8a0
-  __DATA_CONST.__const: 0x1358
+  __TEXT.__objc_stubs: 0x88a0
+  __DATA_CONST.__got: 0x8f0
+  __DATA_CONST.__const: 0x1310
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bb8
+  __DATA_CONST.__objc_selrefs: 0x2c10
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x4c8
+  __AUTH_CONST.__auth_got: 0x4a8
   __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x34a0
-  __AUTH_CONST.__objc_const: 0x68c0
+  __AUTH_CONST.__cfstring: 0x34c0
+  __AUTH_CONST.__objc_const: 0x6910
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__objc_intobj: 0x3c0
+  __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_ivar: 0x450
-  __DATA.__data: 0x4f8
+  __DATA.__objc_ivar: 0x458
+  __DATA.__data: 0x500
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x640
-  __DATA_DIRTY.__bss: 0x160
+  __DATA_DIRTY.__bss: 0x130
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
+  - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/ATFoundation.framework/ATFoundation
   - /System/Library/PrivateFrameworks/AirTraffic.framework/AirTraffic
   - /System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MusicLibrary.framework/MusicLibrary

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/PodcastsFoundation.framework/PodcastsFoundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 83A36FC6-BABA-3607-90EC-3B4E4FCE282E
-  Functions: 1700
-  Symbols:   6086
-  CStrings:  3430
+  UUID: 341E7973-35D6-3BF8-B965-CE73F5598FD7
+  Functions: 1699
+  Symbols:   6089
+  CStrings:  3446
 
Symbols:
+ -[NMSEpisodeFetchRequestItemEnumerator _getNextItem]
+ -[NMSMusicRecommendation _tiledArtworkRequestWithPersistentIDs:]
+ -[NMSMusicRecommendationManager _handleCloudControllerIsCloudEnabledDidChangeNotification:]
+ -[NMSMusicRecommendationsRequest _continueToLibraryPinsRequestWithContext:queue:responseHandler:]
+ -[NMSMusicRecommendationsRequest _isLibraryPinsSupported]
+ -[NMSMusicRecommendationsRequest _performLibraryPinsRequestWithCompletion:]
+ -[NMSMusicRecommendationsRequestContext libraryPinsResponse]
+ -[NMSMusicRecommendationsRequestContext setLibraryPinsResponse:]
+ GCC_except_table172
+ GCC_except_table202
+ GCC_except_table43
+ GCC_except_table97
+ _ML3TrackPropertyAlbumArtistPersistentID
+ _ML3TrackPropertyIsMusicVideo
+ _MPCloudControllerIsCloudEnabledDidChangeNotification
+ _MPModelPropertyArtistArtwork
+ _MPModelPropertyLibraryPinPosition
+ _MPModelPropertySongArtwork
+ _MPModelRelationshipLibraryPinAlbum
+ _MPModelRelationshipLibraryPinArtist
+ _MPModelRelationshipLibraryPinPlaylist
+ _MPModelRelationshipLibraryPinSong
+ _NMSRecommendationLibraryPinsIdentifier
+ _OBJC_CLASS_$_AKAccountManager
+ _OBJC_CLASS_$_LSBundleProxy
+ _OBJC_CLASS_$_MPCloudController
+ _OBJC_CLASS_$_MPModelArtist
+ _OBJC_CLASS_$_MPModelLibraryPinKind
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestContext._libraryPinsModelObjects
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestContext._libraryPinsResponse
+ ___130+[NMSMediaItemGroup _itemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:]_block_invoke
+ ___40-[NMSMusicRecommendation artworkCatalog]_block_invoke_2.cold.5
+ ___40-[NMSMusicRecommendation artworkCatalog]_block_invoke_2.cold.6
+ ___40-[NMSMusicRecommendation artworkCatalog]_block_invoke_2.cold.7
+ ___40-[NMSMusicRecommendation artworkCatalog]_block_invoke_2.cold.8
+ ___52-[NMSEpisodeFetchRequestItemEnumerator _getNextItem]_block_invoke
+ ___64-[NMSMusicRecommendationManager _sortedContainersBasedOnRecency]_block_invoke.107
+ ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.234
+ ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.235
+ ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.240
+ ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.241
+ ___74-[NMSMusicRecommendationManager _handleMediaLibraryDidChangeNotification:]_block_invoke.89
+ ___74-[NMSMusicRecommendationManager fetchRecommendationsWithQueue:completion:]_block_invoke.79
+ ___74-[NMSMusicRecommendationManager fetchRecommendationsWithQueue:completion:]_block_invoke.80
+ ___74-[NMSMusicRecommendationManager fetchRecommendationsWithQueue:completion:]_block_invoke.82
+ ___75-[NMSMusicRecommendationManager _handleActiveAccountDidChangeNotification:]_block_invoke.87
+ ___80-[NMSMusicRecommendationManager _handlePairedDeviceDidBecomeActiveNotification:]_block_invoke.92
+ ___80-[NMSMusicRecommendationManager _handleSubscriptionStatusDidChangeNotification:]_block_invoke.86
+ ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke.86
+ ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke.95
+ ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2.88
+ ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2.96
+ ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_3.90
+ ___89-[NMSMusicRecommendationManager _handleRecommendationStoreContentsDidChangeNotification:]_block_invoke.88
+ ___91-[NMSMusicRecommendationManager _handleCloudControllerIsCloudEnabledDidChangeNotification:]_block_invoke
+ ___91-[NMSMusicRecommendationManager _handleCloudControllerIsCloudEnabledDidChangeNotification:]_block_invoke.91
+ ___91-[NMSMusicRecommendationManager _handleMediaLibraryDynamicPropertiesDidChangeNotification:]_block_invoke.90
+ ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.107
+ ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.107.cold.1
+ ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.110
+ ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.110.cold.1
+ ___97-[NMSMusicRecommendationsRequest _continueToLibraryPinsRequestWithContext:queue:responseHandler:]_block_invoke
+ ___97-[NMSMusicRecommendationsRequest _continueToLibraryPinsRequestWithContext:queue:responseHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e47_v32?0"MPModelLibraryPin"8"NSIndexPath"16^B24ls32l8
+ ___block_descriptor_41_e8_32s_e20_v40?0q8r^16Q24^B32ls32l8
+ ___block_literal_global.124
+ ___block_literal_global.125
+ _objc_msgSend$_continueToLibraryPinsRequestWithContext:queue:responseHandler:
+ _objc_msgSend$_getNextItem
+ _objc_msgSend$_isLibraryPinsSupported
+ _objc_msgSend$_performLibraryPinsRequestWithCompletion:
+ _objc_msgSend$_setError
+ _objc_msgSend$_tiledArtworkRequestWithPersistentIDs:
+ _objc_msgSend$anyObject
+ _objc_msgSend$downloadBehavior
+ _objc_msgSend$filteringOptions
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$isCloudLibraryEnabled
+ _objc_msgSend$position
+ _objc_msgSend$setFilteringOptions:
+ _objc_msgSend$setItemSortDescriptors:
+ _objc_msgSend$setLibraryPinsResponse:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$sharedCloudController
- -[MPModelPlaylist(LastUpdatedString) nms_compactLastUpdatedString]
- -[MPModelPlaylist(LastUpdatedString) nms_shouldShowLastUpdatedString]
- -[NMSMediaPinningManager _handleMediaLibraryEntitiesAddedOrRemovedNotification:]
- -[NMSMusicRecommendation _tiledArtworkRequestForPlaylists:albums:]
- -[NMSMusicRecommendationManager _handleMediaLibraryEntitiesAddedOrRemovedNotification:]
- -[NMSRecommendationMediaItemGroup _fetchDownloadableItemsForIDs:]
- GCC_except_table11
- GCC_except_table174
- GCC_except_table204
- GCC_except_table23
- GCC_except_table38
- GCC_except_table39
- GCC_except_table90
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _AuthKitLibraryCore.frameworkLibrary
- _MobileCoreServicesLibraryCore.frameworkLibrary
- _OBJC_CLASS_$_ML3TruthPredicate
- ___48-[NMSEpisodeFetchRequestItemEnumerator nextItem]_block_invoke
- ___64-[NMSMusicRecommendationManager _sortedContainersBasedOnRecency]_block_invoke.102
- ___65-[NMSRecommendationMediaItemGroup _fetchDownloadableItemsForIDs:]_block_invoke
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.206
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.207
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.217
- ___74-[NMSMusicRecommendationManager _handleMediaLibraryDidChangeNotification:]_block_invoke.85
- ___74-[NMSMusicRecommendationManager fetchRecommendationsWithQueue:completion:]_block_invoke.74
- ___74-[NMSMusicRecommendationManager fetchRecommendationsWithQueue:completion:]_block_invoke.75
- ___74-[NMSMusicRecommendationManager fetchRecommendationsWithQueue:completion:]_block_invoke.77
- ___75-[NMSMusicRecommendationManager _handleActiveAccountDidChangeNotification:]_block_invoke.82
- ___80-[NMSMediaPinningManager _handleMediaLibraryEntitiesAddedOrRemovedNotification:]_block_invoke
- ___80-[NMSMusicRecommendationManager _handlePairedDeviceDidBecomeActiveNotification:]_block_invoke.87
- ___80-[NMSMusicRecommendationManager _handleSubscriptionStatusDidChangeNotification:]_block_invoke.81
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke.80
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke.90
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2.82
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2.91
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_3.84
- ___87-[NMSMusicRecommendationManager _handleMediaLibraryEntitiesAddedOrRemovedNotification:]_block_invoke
- ___87-[NMSMusicRecommendationManager _handleMediaLibraryEntitiesAddedOrRemovedNotification:]_block_invoke.84
- ___89-[NMSMusicRecommendationManager _handleRecommendationStoreContentsDidChangeNotification:]_block_invoke.83
- ___91-[NMSMusicRecommendationManager _handleMediaLibraryDynamicPropertiesDidChangeNotification:]_block_invoke.86
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.101
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.101.cold.1
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.104
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.104.cold.1
- ___AuthKitLibraryCore_block_invoke
- ___MobileCoreServicesLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_48_e8_32s40r_e20_v40?0q8r^16Q24^B32lr40l8s32l8
- ___block_literal_global.107
- ___block_literal_global.132
- ___getAKAccountManagerClass_block_invoke
- ___getAKAccountManagerClass_block_invoke.cold.1
- ___getLSBundleProxyClass_block_invoke
- ___getLSBundleProxyClass_block_invoke.cold.1
- __sl_dlopen
- _abort_report_np
- _audit_stringAuthKit
- _audit_stringMobileCoreServices
- _free
- _getAKAccountManagerClass.softClass
- _getLSBundleProxyClass
- _getLSBundleProxyClass.softClass
- _objc_getClass
- _objc_msgSend$_tiledArtworkRequestForPlaylists:albums:
- _objc_msgSend$nmu_dateWithDeltaDays:
- _objc_msgSend$nmu_displayStringWithOptions:
- _objc_msgSend$startOfDayForDate:
- _objc_msgSend$truePredicate
CStrings:
+ "C5092DE9-70B8-41DB-B2AB-80DD86ED41C7"
+ "Library Pins Recommendations"
+ "LibraryPins"
+ "T@\"MPModelResponse\",&,N,V_libraryPinsResponse"
+ "The recommendation [%{public}@] is a song, but the song information is missing. This is likely to manifest as missing artwork in Music's settings in the Watch app."
+ "The recommendation [%{public}@] is an artist, but the artist information is missing. This is likely to manifest as missing artwork in Music's settings in the Watch app."
+ "The recommended artist [%{public}@] is missing its artwork catalog. This is likely to manifest as missing artwork in Music's settings in the Watch app."
+ "The recommended song [%{public}@] is missing its artwork catalog. This is likely to manifest as missing artwork in Music's settings in the Watch app."
+ "[Recommendation] (Processing) (Library Pins) Picked item: %{public}@"
+ "[Recommendation] Is Cloud Enabled did change. Reloading recommendations."
+ "_continueToLibraryPinsRequestWithContext:queue:responseHandler:"
+ "_getNextItem"
+ "_handleCloudControllerIsCloudEnabledDidChangeNotification:"
+ "_isLibraryPinsSupported"
+ "_libraryPinsModelObjects"
+ "_libraryPinsResponse"
+ "_performLibraryPinsRequestWithCompletion:"
+ "_setError"
+ "_tiledArtworkRequestWithPersistentIDs:"
+ "anyObject"
+ "downloadBehavior"
+ "filteringOptions"
+ "getBytes:range:"
+ "hasError"
+ "isCloudLibraryEnabled"
+ "libraryPinsResponse"
+ "position"
+ "setFilteringOptions:"
+ "setItemSortDescriptors:"
+ "setLibraryPinsResponse:"
+ "setPosition:"
+ "sharedCloudController"
+ "v32@?0@\"MPModelLibraryPin\"8@\"NSIndexPath\"16^B24"
- "AKAccountManager"
- "LAST_UPDATED_SHORT_SUBTITLE"
- "LSBundleProxy"
- "Unable to find class %s"
- "Updated %@"
- "[Recommendation] Media Library entities added or removed. Reloading recommendations."
- "_fetchDownloadableItemsForIDs:"
- "_handleMediaLibraryEntitiesAddedOrRemovedNotification:"
- "_tiledArtworkRequestForPlaylists:albums:"
- "nms_compactLastUpdatedString"
- "nms_shouldShowLastUpdatedString"
- "nmu_dateWithDeltaDays:"
- "nmu_displayStringWithOptions:"
- "softlink:r:path:/System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices"
- "softlink:r:path:/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit"
- "startOfDayForDate:"
- "truePredicate"

```
