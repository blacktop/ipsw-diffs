## NanoMusicSync

> `/System/Library/PrivateFrameworks/NanoMusicSync.framework/NanoMusicSync`

```diff

-2021.100.60.0.0
-  __TEXT.__text: 0x53f84
-  __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_methlist: 0x412c
+2021.200.14.0.0
+  __TEXT.__text: 0x4e9bc
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__objc_methlist: 0x3ebc
   __TEXT.__const: 0x180
-  __TEXT.__gcc_except_tab: 0x900
-  __TEXT.__cstring: 0x3ae7
-  __TEXT.__oslogstring: 0x7a01
+  __TEXT.__gcc_except_tab: 0x85c
+  __TEXT.__cstring: 0x35fc
+  __TEXT.__oslogstring: 0x7635
   __TEXT.__dlopen_cstrs: 0xf3
-  __TEXT.__unwind_info: 0x13a8
-  __TEXT.__objc_classname: 0xb65
-  __TEXT.__objc_methname: 0xc7ef
-  __TEXT.__objc_methtype: 0x1921
-  __TEXT.__objc_stubs: 0x91e0
-  __DATA_CONST.__got: 0x4a8
-  __DATA_CONST.__const: 0x1798
-  __DATA_CONST.__objc_classlist: 0x2a0
+  __TEXT.__unwind_info: 0x1280
+  __TEXT.__objc_classname: 0xa82
+  __TEXT.__objc_methname: 0xbfa9
+  __TEXT.__objc_methtype: 0x18c1
+  __TEXT.__objc_stubs: 0x8a20
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__const: 0x1450
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5860
-  __DATA_CONST.__objc_selrefs: 0x2d48
+  __DATA_CONST.__objc_const: 0x5540
+  __DATA_CONST.__objc_selrefs: 0x2b58
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__cfstring: 0x3660
-  __AUTH_CONST.__objc_const: 0x20a0
+  __AUTH_CONST.__cfstring: 0x3560
+  __AUTH_CONST.__objc_const: 0x1ea8
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__objc_intobj: 0x498
-  __AUTH_CONST.__auth_got: 0x508
-  __AUTH.__objc_data: 0x13b0
-  __DATA.__objc_classrefs: 0x5d8
-  __DATA.__objc_superrefs: 0x1f0
-  __DATA.__objc_ivar: 0x488
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__objc_intobj: 0x450
+  __AUTH_CONST.__auth_got: 0x4f8
+  __AUTH.__objc_data: 0x11d0
+  __DATA.__objc_classrefs: 0x590
+  __DATA.__objc_superrefs: 0x1d8
+  __DATA.__objc_ivar: 0x468
   __DATA.__data: 0x560
-  __DATA.__bss: 0xa8
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__bss: 0x168
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1822
-  Symbols:   6533
-  CStrings:  3232
+  Functions: 1735
+  Symbols:   6198
+  CStrings:  3106
 
Symbols:
+ -[NMSMusicRecommendationsResponse initWithCachedData:recommendations:]
+ __OBJC_$_CLASS_METHODS_NMSMusicRecommendationManager
+ __OBJC_$_INSTANCE_METHODS_NMSMusicRecommendationManager
+ ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.206
+ ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.207
+ ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.217
+ ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.218
+ ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.223
+ ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.224
+ ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke.80
+ ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke.90
+ ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2.82
+ ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2.91
+ ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_3.84
+ ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.101
+ ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.101.cold.1
+ ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.104
+ ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.104.cold.1
+ ___block_literal_global.112
+ _objc_msgSend$initWithCachedData:recommendations:
- +[NMSAccountInfo activeStoreAccountInfo]
- +[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:]
- +[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:].cold.1
- +[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:].cold.2
- -[NMSAccountInfo .cxx_destruct]
- -[NMSAccountInfo _handleAccountStoreDidChangeNotification:]
- -[NMSAccountInfo _updateActiveAccount]
- -[NMSAccountInfo activeAccount]
- -[NMSAccountInfo dealloc]
- -[NMSAccountInfo init]
- -[NMSAccountInfo preloadActiveAccount]
- -[NMSModelRecommendationsLibraryRequest newOperationWithResponseHandler:]
- -[NMSModelRecommendationsLibraryRequestOperation .cxx_destruct]
- -[NMSModelRecommendationsLibraryRequestOperation _modelObjectWithCachedArtworkFromModelObject:]
- -[NMSModelRecommendationsLibraryRequestOperation _mpIdentifierSetsFromStringIdentifiers:]
- -[NMSModelRecommendationsLibraryRequestOperation _requestAlbums]
- -[NMSModelRecommendationsLibraryRequestOperation _requestContainerWithClass:]
- -[NMSModelRecommendationsLibraryRequestOperation _requestPlaylistsEntries]
- -[NMSModelRecommendationsLibraryRequestOperation _requestPlaylists]
- -[NMSModelRecommendationsLibraryRequestOperation _requestSongs]
- -[NMSModelRecommendationsLibraryRequestOperation execute]
- -[NMSModelRecommendationsLibraryRequestOperation request]
- -[NMSModelRecommendationsLibraryRequestOperation responseHandler]
- -[NMSModelRecommendationsLibraryRequestOperation setRequest:]
- -[NMSModelRecommendationsLibraryRequestOperation setResponseHandler:]
- -[NMSModelRecommendationsLibraryResponse _handleMusicRecommendationArtworkDidUpdateNotification:]
- -[NMSModelRecommendationsLibraryResponse _handleMusicRecommendationsDidUpdateNotification:]
- -[NMSModelRecommendationsLibraryResponse dealloc]
- -[NMSModelRecommendationsLibraryResponse initWithRequest:]
- -[NMSMusicRecommendationManager(ModelObject) nms_deselectRecommendationIfNecessaryForModelObject:]
- -[NMSMusicRecommendationManager(ModelObject) nms_fetchRecentMusicRecommendationWithQueue:completionHandler:]
- -[NMSMusicRecommendationManager(ModelObject) nms_fetchSelectedRecommendationSectionTypesForModelObject:queue:completionHandler:]
- -[NMSMusicRecommendationsRequest _continueToLegacyLibraryImportWithContext:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _continueToLegacyLookupWithContext:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _performLegacyLookupRequestWithModelObjects:completion:]
- -[NMSMusicRecommendationsRequestContext importedStoreContainerItemMappings]
- -[NMSMusicRecommendationsRequestContext lookupResponse]
- -[NMSMusicRecommendationsRequestContext setLookupResponse:]
- -[NMSMusicRecommendationsResponse importedStoreContainerItemMappings]
- -[NMSMusicRecommendationsResponse initWithCachedData:importedStoreContainerItemMappings:recommendations:]
- -[NMSStoreModelLookupRequest .cxx_destruct]
- -[NMSStoreModelLookupRequest containerIDs]
- -[NMSStoreModelLookupRequest copyWithZone:]
- -[NMSStoreModelLookupRequest newOperationWithResponseHandler:]
- -[NMSStoreModelLookupRequest setContainerIDs:]
- -[NMSStoreModelLookupRequestOperation configurationForLoadingModelDataWithStoreURLBag:error:]
- -[NMSStoreModelLookupRequestOperation produceResponseWithLoadedOutput:completion:]
- GCC_except_table101
- GCC_except_table6
- GCC_except_table71
- GCC_except_table75
- _ACAccountStoreDidChangeNotification
- _AMSError
- _MPModelPropertyFileAssetFileSize
- _MPModelPropertySongDiscNumber
- _MPModelPropertySongKeepLocalEnableState
- _MPModelPropertySongTitle
- _MPModelPropertySongTrackNumber
- _MPModelRelationshipPlaylistEntrySong
- _MPModelRelationshipSongLocalFileAsset
- _NMSAccountInfoActiveAccountDidChangeNotification
- _NSIntersectionRange
- _NSLocalizedDescriptionKey
- _OBJC_CLASS_$_MPAsyncOperation
- _OBJC_CLASS_$_MPModelLibraryResponse
- _OBJC_CLASS_$_MPStoreItemMetadataResponse
- _OBJC_CLASS_$_MPStoreModelRequest
- _OBJC_CLASS_$_MPStoreModelRequestConfiguration
- _OBJC_CLASS_$_MPStoreModelRequestOperation
- _OBJC_CLASS_$_MPStoreModelSongBuilder
- _OBJC_CLASS_$_NMSAccountInfo
- _OBJC_CLASS_$_NMSModelRecommendationsLibraryRequest
- _OBJC_CLASS_$_NMSModelRecommendationsLibraryRequestOperation
- _OBJC_CLASS_$_NMSModelRecommendationsLibraryResponse
- _OBJC_CLASS_$_NMSStoreModelLookupRequest
- _OBJC_CLASS_$_NMSStoreModelLookupRequestOperation
- _OBJC_CLASS_$_NSNumberFormatter
- _OBJC_IVAR_$_NMSAccountInfo._accountStore
- _OBJC_IVAR_$_NMSAccountInfo._activeAccount
- _OBJC_IVAR_$_NMSAccountInfo._queue
- _OBJC_IVAR_$_NMSModelRecommendationsLibraryRequestOperation._request
- _OBJC_IVAR_$_NMSModelRecommendationsLibraryRequestOperation._responseHandler
- _OBJC_IVAR_$_NMSMusicRecommendationsRequestContext._lookupResponse
- _OBJC_IVAR_$_NMSMusicRecommendationsResponse._importedStoreContainerItemMappings
- _OBJC_IVAR_$_NMSStoreModelLookupRequest._containerIDs
- _OBJC_METACLASS_$_MPAsyncOperation
- _OBJC_METACLASS_$_MPModelLibraryRequest
- _OBJC_METACLASS_$_MPModelLibraryResponse
- _OBJC_METACLASS_$_MPStoreModelRequest
- _OBJC_METACLASS_$_MPStoreModelRequestOperation
- _OBJC_METACLASS_$_NMSAccountInfo
- _OBJC_METACLASS_$_NMSModelRecommendationsLibraryRequest
- _OBJC_METACLASS_$_NMSModelRecommendationsLibraryRequestOperation
- _OBJC_METACLASS_$_NMSModelRecommendationsLibraryResponse
- _OBJC_METACLASS_$_NMSStoreModelLookupRequest
- _OBJC_METACLASS_$_NMSStoreModelLookupRequestOperation
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- __OBJC_$_CLASS_METHODS_NMSAccountInfo
- __OBJC_$_CLASS_METHODS_NMSMusicRecommendationManager(ModelObject)
- __OBJC_$_CLASS_PROP_LIST_NMSAccountInfo
- __OBJC_$_INSTANCE_METHODS_NMSAccountInfo
- __OBJC_$_INSTANCE_METHODS_NMSModelRecommendationsLibraryRequest
- __OBJC_$_INSTANCE_METHODS_NMSModelRecommendationsLibraryRequestOperation
- __OBJC_$_INSTANCE_METHODS_NMSModelRecommendationsLibraryResponse
- __OBJC_$_INSTANCE_METHODS_NMSMusicRecommendationManager(ModelObject)
- __OBJC_$_INSTANCE_METHODS_NMSStoreModelLookupRequest
- __OBJC_$_INSTANCE_METHODS_NMSStoreModelLookupRequestOperation
- __OBJC_$_INSTANCE_VARIABLES_NMSAccountInfo
- __OBJC_$_INSTANCE_VARIABLES_NMSModelRecommendationsLibraryRequestOperation
- __OBJC_$_INSTANCE_VARIABLES_NMSStoreModelLookupRequest
- __OBJC_$_PROP_LIST_NMSAccountInfo
- __OBJC_$_PROP_LIST_NMSModelRecommendationsLibraryRequestOperation
- __OBJC_$_PROP_LIST_NMSStoreModelLookupRequest
- __OBJC_CLASS_RO_$_NMSAccountInfo
- __OBJC_CLASS_RO_$_NMSModelRecommendationsLibraryRequest
- __OBJC_CLASS_RO_$_NMSModelRecommendationsLibraryRequestOperation
- __OBJC_CLASS_RO_$_NMSModelRecommendationsLibraryResponse
- __OBJC_CLASS_RO_$_NMSStoreModelLookupRequest
- __OBJC_CLASS_RO_$_NMSStoreModelLookupRequestOperation
- __OBJC_METACLASS_RO_$_NMSAccountInfo
- __OBJC_METACLASS_RO_$_NMSModelRecommendationsLibraryRequest
- __OBJC_METACLASS_RO_$_NMSModelRecommendationsLibraryRequestOperation
- __OBJC_METACLASS_RO_$_NMSModelRecommendationsLibraryResponse
- __OBJC_METACLASS_RO_$_NMSStoreModelLookupRequest
- __OBJC_METACLASS_RO_$_NMSStoreModelLookupRequestOperation
- ___108-[NMSMusicRecommendationManager(ModelObject) nms_fetchRecentMusicRecommendationWithQueue:completionHandler:]_block_invoke
- ___128-[NMSMusicRecommendationManager(ModelObject) nms_fetchSelectedRecommendationSectionTypesForModelObject:queue:completionHandler:]_block_invoke
- ___136+[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:]_block_invoke
- ___136+[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:]_block_invoke_2
- ___136+[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:]_block_invoke_3
- ___136+[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:]_block_invoke_3.cold.1
- ___136+[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:]_block_invoke_3.cold.2
- ___136+[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:]_block_invoke_4
- ___136+[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:]_block_invoke_5
- ___31-[NMSAccountInfo activeAccount]_block_invoke
- ___38-[NMSAccountInfo _updateActiveAccount]_block_invoke
- ___38-[NMSAccountInfo _updateActiveAccount]_block_invoke_2
- ___38-[NMSAccountInfo _updateActiveAccount]_block_invoke_2.cold.1
- ___38-[NMSAccountInfo preloadActiveAccount]_block_invoke
- ___40+[NMSAccountInfo activeStoreAccountInfo]_block_invoke
- ___59-[NMSAccountInfo _handleAccountStoreDidChangeNotification:]_block_invoke
- ___63-[NMSModelRecommendationsLibraryRequestOperation _requestSongs]_block_invoke
- ___63-[NMSModelRecommendationsLibraryRequestOperation _requestSongs]_block_invoke_2
- ___63-[NMSModelRecommendationsLibraryRequestOperation _requestSongs]_block_invoke_3
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.220
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.221
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.230
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.231
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.236
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.237
- ___74-[NMSModelRecommendationsLibraryRequestOperation _requestPlaylistsEntries]_block_invoke
- ___74-[NMSModelRecommendationsLibraryRequestOperation _requestPlaylistsEntries]_block_invoke_2
- ___74-[NMSModelRecommendationsLibraryRequestOperation _requestPlaylistsEntries]_block_invoke_3
- ___74-[NMSModelRecommendationsLibraryRequestOperation _requestPlaylistsEntries]_block_invoke_4
- ___75-[NMSMusicRecommendationsRequestContext importedStoreContainerItemMappings]_block_invoke
- ___75-[NMSMusicRecommendationsRequestContext importedStoreContainerItemMappings]_block_invoke_2
- ___77-[NMSModelRecommendationsLibraryRequestOperation _requestContainerWithClass:]_block_invoke
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke.82
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke.92
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2.84
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2.93
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_3.86
- ___89-[NMSModelRecommendationsLibraryRequestOperation _mpIdentifierSetsFromStringIdentifiers:]_block_invoke
- ___89-[NMSMusicRecommendationsRequest _performLegacyLookupRequestWithModelObjects:completion:]_block_invoke
- ___89-[NMSMusicRecommendationsRequest _performLegacyLookupRequestWithModelObjects:completion:]_block_invoke.cold.1
- ___91-[NMSModelRecommendationsLibraryResponse _handleMusicRecommendationsDidUpdateNotification:]_block_invoke
- ___91-[NMSMusicRecommendationsRequest _continueToLegacyLookupWithContext:queue:responseHandler:]_block_invoke
- ___91-[NMSMusicRecommendationsRequest _continueToLegacyLookupWithContext:queue:responseHandler:]_block_invoke_2
- ___95-[NMSModelRecommendationsLibraryRequestOperation _modelObjectWithCachedArtworkFromModelObject:]_block_invoke
- ___95-[NMSModelRecommendationsLibraryRequestOperation _modelObjectWithCachedArtworkFromModelObject:]_block_invoke_2
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.103
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.103.cold.1
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.106
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.106.cold.1
- ___98-[NMSMusicRecommendationManager(ModelObject) nms_deselectRecommendationIfNecessaryForModelObject:]_block_invoke
- ___98-[NMSMusicRecommendationsRequest _continueToLegacyLibraryImportWithContext:queue:responseHandler:]_block_invoke
- ___98-[NMSMusicRecommendationsRequest _continueToLegacyLibraryImportWithContext:queue:responseHandler:]_block_invoke_2
- ___block_descriptor_32_e23_v16?0"MPModelObject"8l
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
- ___block_descriptor_40_e8_32s_e28_v32?08"NSIndexPath"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e30_v16?0"MPModelPlaylistEntry"8ls32l8
- ___block_descriptor_40_e8_32s_e31_v24?0"ACAccount"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32s_e37_q24?0"MPModelSong"8"MPModelSong"16ls32l8
- ___block_descriptor_40_e8_32s_e55_q24?0"MPModelPlaylistEntry"8"MPModelPlaylistEntry"16ls32l8
- ___block_descriptor_48_e8_32r_e32_v32?0"MPIdentifierSet"8Q16^B24lu40l8r32l8
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e37_v24?0"MPModelResponse"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e25_v16?0"MPIdentifierSet"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e25_v16?0"MPModelPlaylist"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e43_"MPArtworkCatalog"16?0"MPModelPlaylist"8ls32l8s40l8
- ___block_descriptor_48_e8_32s_e17_v16?0"NSArray"8ls32l8u40l8
- ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"8q16^B24ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40s_e30_v32?0"MPModelObject"8q16^B24ls32l8u48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16ls32l8s56l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48r_e30_v32?0"MPModelObject"8q16^B24lu56l8s32l8r48l8s40l8
- ___block_descriptor_65_e8_32s40s48r_e44_v24?0"MPModelLibraryResponse"8"NSError"16lu56l8s32l8r48l8s40l8
- ___block_descriptor_72_e8_32s40s48w_e44_v24?0"MPModelLibraryResponse"8"NSError"16lw48l8s32l8s40l8
- ___block_literal_global.114
- ___block_literal_global.134
- ___block_literal_global.177
- _activeStoreAccountInfo.instance
- _activeStoreAccountInfo.onceToken
- _objc_msgSend$_continueToLegacyLookupWithContext:queue:responseHandler:
- _objc_msgSend$_invalidate
- _objc_msgSend$_legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:
- _objc_msgSend$_modelObjectWithCachedArtworkFromModelObject:
- _objc_msgSend$_mpIdentifierSetsFromStringIdentifiers:
- _objc_msgSend$_performLegacyLibraryImportChangeRequestWithModelObjects:completion:
- _objc_msgSend$_performLegacyLookupRequestWithModelObjects:completion:
- _objc_msgSend$_requestAlbums
- _objc_msgSend$_requestContainerWithClass:
- _objc_msgSend$_requestPlaylists
- _objc_msgSend$_requestPlaylistsEntries
- _objc_msgSend$_requestSongs
- _objc_msgSend$allSupportedProperties
- _objc_msgSend$appendItem:
- _objc_msgSend$artworkCacheExistsForToken:
- _objc_msgSend$childStoreItemMetadatas
- _objc_msgSend$containerIDs
- _objc_msgSend$contentRange
- _objc_msgSend$copyWithIdentifiers:block:
- _objc_msgSend$fileSize
- _objc_msgSend$filteringOptions
- _objc_msgSend$finish
- _objc_msgSend$finishWithError:
- _objc_msgSend$ic_activeStoreAccountWithCompletion:
- _objc_msgSend$importedStoreContainerItemMappings
- _objc_msgSend$indexOfObject:
- _objc_msgSend$initWithCachedData:importedStoreContainerItemMappings:recommendations:
- _objc_msgSend$initWithRequestedItemIdentifiers:reason:
- _objc_msgSend$initWithRequestedPropertySet:
- _objc_msgSend$itemIdentifiers
- _objc_msgSend$itemKind
- _objc_msgSend$itemProperties
- _objc_msgSend$itemsForContainer:
- _objc_msgSend$label
- _objc_msgSend$localFileAsset
- _objc_msgSend$lookupResponse
- _objc_msgSend$modelClass
- _objc_msgSend$modelObjectWithStoreItemMetadata:userIdentity:
- _objc_msgSend$nms_setRecommendationObject:
- _objc_msgSend$nms_universalStoreLookupID
- _objc_msgSend$numberFromString:
- _objc_msgSend$propertySetByCombiningWithPropertySet:
- _objc_msgSend$relationships
- _objc_msgSend$scopedContainers
- _objc_msgSend$setArtworkCatalogBlock:
- _objc_msgSend$setContainerIDs:
- _objc_msgSend$setFilteringOptions:
- _objc_msgSend$setImportedObjects:
- _objc_msgSend$setItemSortDescriptors:
- _objc_msgSend$setItems:forContainer:
- _objc_msgSend$setLookupResponse:
- _objc_msgSend$setRequest:
- _objc_msgSend$setResponseHandler:
- _objc_msgSend$setScopedContainers:
- _objc_msgSend$setSectionKind:
- _objc_msgSend$setSong:
- _objc_msgSend$sharedLibraryRequestQueue
- _objc_msgSend$song
- _objc_msgSend$start
- _objc_msgSend$storeItemMetadataForItemIdentifier:
- _objc_msgSend$subscriptionAdamID
- _objc_msgSend$unionOrderedSet:
- _objc_msgSend$userIdentity
CStrings:
+ "\x02\x16"
+ "initWithCachedData:recommendations:"
- "\x02\x17"
- "%@ %s NMSMediaItemGroup: Failed to fetch songs due to empty containers with type: %{public}@"
- "%@ %s NMSMediaItemGroup: Failed to fetch songs for containers with type %{public}@: %{public}@ due to %{public}@"
- "%@ %s NMSMediaItemGroup: Failed to fetch songs for containers with type: %{public}@"
- "%@ %s NMSMediaItemGroup: Fetched %tu songs for containers %{public}@, items @ %{public}@"
- "+[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:]"
- "+[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:]_block_invoke"
- "+[NMSMediaItemGroup _legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:]_block_invoke_3"
- "0`"
- "1@`"
- "1`"
- "@\"MPArtworkCatalog\"16@?0@\"MPModelPlaylist\"8"
- "@\"NMSModelRecommendationsLibraryRequest\""
- "@\"NMSMutableMediaSyncInfo\""
- "@40@0:8@16@24@32"
- "@`"
- "Failed to fetch account: %@"
- "ICAgeVerificationStatus requires verification. Filtering out all explicit content"
- "LibraryAutomaticDownloads"
- "ModelObject"
- "NMSAccountInfo"
- "NMSAccountInfoActiveAccountDidChangeNotification"
- "NMSModelRecommendationsLibraryRequest"
- "NMSModelRecommendationsLibraryRequestOperation"
- "NMSModelRecommendationsLibraryResponse"
- "NMSStoreModelLookupRequest"
- "NMSStoreModelLookupRequestOperation"
- "Pinned Items For "
- "Requesting recommendation playlist entries requires a list of item identifiers."
- "Requesting recommendation playlist entries requires a scoped container MPModelPlaylist."
- "Requesting recommendation songs requires a list of item identifiers."
- "Requesting recommendation songs requires a scoped container MPModelAlbum."
- "Requesting recommendations with type: %@ is not supported"
- "Songs for %@"
- "T@\"ACAccount\",R,N"
- "T@\"MPModelResponse\",&,N,V_lookupResponse"
- "T@\"NMSAccountInfo\",R"
- "T@\"NMSModelRecommendationsLibraryRequest\",C,N,V_request"
- "T@\"NMSMutableMediaSyncInfo\",R,N"
- "T@\"NMSMutableMediaSyncInfo\",R,N,V_importedStoreContainerItemMappings"
- "T@\"NSArray\",C,N,V_containerIDs"
- "T@?,C,N,V_responseHandler"
- "[Account] Active account has changed from %@ to %@"
- "[Account] Active account is %@"
- "[Account] Received account store did change notification."
- "[Recommendation] (Lookup) %{public}@ failed with error: %{public}@"
- "[Recommendation] (Lookup) Got response: %@"
- "[Recommendation] (Lookup) Ignored object with existing library identifier: %{public}@"
- "[Recommendation] (Lookup) Ignored object with missing store lookup identifier: %{public}@"
- "[Recommendation] (Lookup) Performing request: %{public}@"
- "_containerIDs"
- "_continueToLegacyLibraryImportWithContext:queue:responseHandler:"
- "_continueToLegacyLookupWithContext:queue:responseHandler:"
- "_handleMusicRecommendationArtworkDidUpdateNotification:"
- "_handleMusicRecommendationsDidUpdateNotification:"
- "_importedStoreContainerItemMappings"
- "_invalidate"
- "_legacyItemsForContainerClass:containerIDs:includingNonLibraryContent:includingDownloadedContentOnly:manuallyAdded:"
- "_lookupResponse"
- "_modelObjectWithCachedArtworkFromModelObject:"
- "_mpIdentifierSetsFromStringIdentifiers:"
- "_performLegacyLookupRequestWithModelObjects:completion:"
- "_request"
- "_requestAlbums"
- "_requestContainerWithClass:"
- "_requestPlaylists"
- "_requestPlaylistsEntries"
- "_requestSongs"
- "_responseHandler"
- "activeStoreAccountInfo"
- "allSupportedProperties"
- "appendItem:"
- "childStoreItemMetadatas"
- "com.apple.NanoMusicSync.NMSAccountInfo"
- "containerIDs"
- "contentRange"
- "copyWithIdentifiers:block:"
- "fileSize"
- "filteringOptions"
- "finish"
- "finishWithError:"
- "ic_activeStoreAccountWithCompletion:"
- "importedStoreContainerItemMappings"
- "indexOfObject:"
- "initWithCachedData:importedStoreContainerItemMappings:recommendations:"
- "initWithRequestedItemIdentifiers:reason:"
- "initWithRequestedPropertySet:"
- "itemIdentifiers"
- "itemKind"
- "itemProperties"
- "label"
- "localFileAsset"
- "lookupResponse"
- "modelClass"
- "modelObjectWithStoreItemMetadata:userIdentity:"
- "nms_deselectRecommendationIfNecessaryForModelObject:"
- "nms_fetchRecentMusicRecommendationWithQueue:completionHandler:"
- "nms_fetchSelectedRecommendationSectionTypesForModelObject:queue:completionHandler:"
- "numberFromString:"
- "preloadActiveAccount"
- "propertySetByCombiningWithPropertySet:"
- "q24@?0@\"MPModelPlaylistEntry\"8@\"MPModelPlaylistEntry\"16"
- "q24@?0@\"MPModelSong\"8@\"MPModelSong\"16"
- "relationships"
- "responseHandler"
- "scopedContainers"
- "setArtworkCatalogBlock:"
- "setContainerIDs:"
- "setFilteringOptions:"
- "setItemSortDescriptors:"
- "setLookupResponse:"
- "setRequest:"
- "setResponseHandler:"
- "setScopedContainers:"
- "setSectionKind:"
- "setSong:"
- "song"
- "storeItemMetadataForItemIdentifier:"
- "subscriptionAdamID"
- "unionOrderedSet:"
- "userIdentity"
- "v16@?0@\"MPModelObject\"8"
- "v16@?0@\"MPModelPlaylist\"8"
- "v16@?0@\"MPModelPlaylistEntry\"8"
- "v24@0:8#16"
- "v24@?0@\"ACAccount\"8@\"NSError\"16"
- "v32@?0@\"NSString\"8q16^B24"
- "v32@?0@8@\"NSIndexPath\"16^B24"

```
