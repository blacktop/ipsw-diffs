## NanoMusicSync

> `/System/Library/PrivateFrameworks/NanoMusicSync.framework/NanoMusicSync`

```diff

-2023.500.11.0.0
-  __TEXT.__text: 0x502bc
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x41b4
+2023.500.14.0.0
+  __TEXT.__text: 0x502d0
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__objc_methlist: 0x41cc
   __TEXT.__const: 0x230
-  __TEXT.__gcc_except_tab: 0xa84
-  __TEXT.__cstring: 0x34e0
+  __TEXT.__gcc_except_tab: 0xafc
+  __TEXT.__cstring: 0x349a
   __TEXT.__oslogstring: 0x7a18
-  __TEXT.__unwind_info: 0x12a8
-  __TEXT.__objc_classname: 0xa3e
-  __TEXT.__objc_methname: 0xbab3
-  __TEXT.__objc_methtype: 0x164f
-  __TEXT.__objc_stubs: 0x88a0
+  __TEXT.__unwind_info: 0x12e0
+  __TEXT.__objc_classname: 0xa71
+  __TEXT.__objc_methname: 0xb8fc
+  __TEXT.__objc_methtype: 0x169d
+  __TEXT.__objc_stubs: 0x8920
   __DATA_CONST.__got: 0x8f0
-  __DATA_CONST.__const: 0x1310
-  __DATA_CONST.__objc_classlist: 0x268
+  __DATA_CONST.__const: 0x1248
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c18
-  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_selrefs: 0x2c20
+  __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x478
+  __AUTH_CONST.__auth_got: 0x488
   __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x34c0
-  __AUTH_CONST.__objc_const: 0x6920
+  __AUTH_CONST.__cfstring: 0x34e0
+  __AUTH_CONST.__objc_const: 0x6a28
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x3a8
-  __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_ivar: 0x458
+  __AUTH.__objc_data: 0x1270
+  __DATA.__objc_ivar: 0x468
   __DATA.__data: 0x500
   __DATA.__bss: 0x80
-  __DATA_DIRTY.__objc_data: 0x640
+  __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x130
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 93E1C23C-7746-3CEF-981A-F6D7597A574F
-  Functions: 1706
-  Symbols:   6103
-  CStrings:  3450
+  UUID: 32EC7D00-74C4-39D5-9F0A-E23851216F74
+  Functions: 1704
+  Symbols:   6116
+  CStrings:  3457
 
Symbols:
+ +[NMSMusicRecommendationsRequestOperation _recentMusicDirectory]
+ +[NMSMusicRecommendationsRequestOperation _recentMusicDirectory].cold.1
+ -[NMSMusicRecommendationsRequestOperation .cxx_destruct]
+ -[NMSMusicRecommendationsRequestOperation _continueToHeavyRotationRequest]
+ -[NMSMusicRecommendationsRequestOperation _continueToLegacyEditorialRequest]
+ -[NMSMusicRecommendationsRequestOperation _continueToLegacyForYouRequest]
+ -[NMSMusicRecommendationsRequestOperation _continueToLibraryImport]
+ -[NMSMusicRecommendationsRequestOperation _continueToLibraryPinsRequest]
+ -[NMSMusicRecommendationsRequestOperation _continueToLibraryRecentMusicRecommedations]
+ -[NMSMusicRecommendationsRequestOperation _continueToProcessResults]
+ -[NMSMusicRecommendationsRequestOperation _continueToRecentMusicRequest]
+ -[NMSMusicRecommendationsRequestOperation _continueToStarterPackMultiplexRequest]
+ -[NMSMusicRecommendationsRequestOperation _continueToStarterPackRoomRequestWithURL:]
+ -[NMSMusicRecommendationsRequestOperation _finish]
+ -[NMSMusicRecommendationsRequestOperation _finish].cold.1
+ -[NMSMusicRecommendationsRequestOperation _heavyRotationCacheURL]
+ -[NMSMusicRecommendationsRequestOperation _isLibraryPinsSupported]
+ -[NMSMusicRecommendationsRequestOperation _performEditorialBrowseRequestWithCompletion:]
+ -[NMSMusicRecommendationsRequestOperation _performForYouRequestWithCompletion:]
+ -[NMSMusicRecommendationsRequestOperation _performHeavyRotationRequestWithCompletion:]
+ -[NMSMusicRecommendationsRequestOperation _performLegacyLibraryImportChangeRequestWithModelObjects:completion:]
+ -[NMSMusicRecommendationsRequestOperation _performLibraryImportChangeRequestWithModelObjects:completion:]
+ -[NMSMusicRecommendationsRequestOperation _performLibraryPinsRequestWithCompletion:]
+ -[NMSMusicRecommendationsRequestOperation _performLibraryRecentMusicRequestWithCompletion:]
+ -[NMSMusicRecommendationsRequestOperation _performStarterPackMultiplexRequestWithCompletion:]
+ -[NMSMusicRecommendationsRequestOperation _performStarterPackRoomRequestWithURL:completion:]
+ -[NMSMusicRecommendationsRequestOperation _starterPackMultiplexCacheURL]
+ -[NMSMusicRecommendationsRequestOperation _starterPackRoomCacheURL]
+ -[NMSMusicRecommendationsRequestOperation _unarchivedCombinedResponsesDictionary]
+ -[NMSMusicRecommendationsRequestOperation _unarchivedCombinedResponsesDictionary].cold.1
+ -[NMSMusicRecommendationsRequestOperation _writeData:toURL:]
+ -[NMSMusicRecommendationsRequestOperation _writeData:toURL:].cold.1
+ -[NMSMusicRecommendationsRequestOperation _writeData:toURL:].cold.2
+ -[NMSMusicRecommendationsRequestOperation execute]
+ -[NMSMusicRecommendationsRequestOperation initWithRequest:responseHandler:]
+ -[NMSMusicRecommendationsRequestOperationContext .cxx_destruct]
+ -[NMSMusicRecommendationsRequestOperationContext _hasDownloadableSongsForModelObject:]
+ -[NMSMusicRecommendationsRequestOperationContext _processRecentMusicItem:section:identifier:]
+ -[NMSMusicRecommendationsRequestOperationContext _processResponsesIfNeeded]
+ -[NMSMusicRecommendationsRequestOperationContext _recentMusicContainsModelObject:]
+ -[NMSMusicRecommendationsRequestOperationContext editorialBrowseResponse]
+ -[NMSMusicRecommendationsRequestOperationContext forYouResponse]
+ -[NMSMusicRecommendationsRequestOperationContext heavyRotationResponse]
+ -[NMSMusicRecommendationsRequestOperationContext libraryPinsResponse]
+ -[NMSMusicRecommendationsRequestOperationContext libraryRecentMusicResponse]
+ -[NMSMusicRecommendationsRequestOperationContext minimumNumberOfRecentMusicModelObjects]
+ -[NMSMusicRecommendationsRequestOperationContext modelObjects]
+ -[NMSMusicRecommendationsRequestOperationContext numberOfRecentMusicModelObjects]
+ -[NMSMusicRecommendationsRequestOperationContext recommendations]
+ -[NMSMusicRecommendationsRequestOperationContext setEditorialBrowseResponse:]
+ -[NMSMusicRecommendationsRequestOperationContext setForYouResponse:]
+ -[NMSMusicRecommendationsRequestOperationContext setHeavyRotationResponse:]
+ -[NMSMusicRecommendationsRequestOperationContext setLibraryPinsResponse:]
+ -[NMSMusicRecommendationsRequestOperationContext setLibraryRecentMusicResponse:]
+ -[NMSMusicRecommendationsRequestOperationContext setMinimumNumberOfRecentMusicModelObjects:]
+ -[NMSMusicRecommendationsRequestOperationContext setStarterPackResponse:]
+ -[NMSMusicRecommendationsRequestOperationContext starterPackResponse]
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table42
+ GCC_except_table47
+ GCC_except_table95
+ _OBJC_CLASS_$_MPAsyncOperation
+ _OBJC_CLASS_$_NMSMusicRecommendationsRequestOperation
+ _OBJC_CLASS_$_NMSMusicRecommendationsRequestOperationContext
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperation._context
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperation._queue
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperation._request
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperation._responseHandler
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperation._unarchivedCombinedResponsesDictionary
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperationContext._editorialBrowseResponse
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperationContext._forYouResponse
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperationContext._heavyRotationResponse
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperationContext._libraryPinsModelObjects
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperationContext._libraryPinsResponse
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperationContext._libraryRecentMusicResponse
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperationContext._minimumNumberOfRecentMusicModelObjects
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperationContext._recentMusicModelObjects
+ _OBJC_IVAR_$_NMSMusicRecommendationsRequestOperationContext._starterPackResponse
+ _OBJC_METACLASS_$_MPAsyncOperation
+ _OBJC_METACLASS_$_NMSMusicRecommendationsRequestOperation
+ _OBJC_METACLASS_$_NMSMusicRecommendationsRequestOperationContext
+ __OBJC_$_CLASS_METHODS_NMSMusicRecommendationsRequestOperation
+ __OBJC_$_INSTANCE_METHODS_NMSMusicRecommendationsRequestOperation
+ __OBJC_$_INSTANCE_METHODS_NMSMusicRecommendationsRequestOperationContext
+ __OBJC_$_INSTANCE_VARIABLES_NMSMusicRecommendationsRequestOperation
+ __OBJC_$_INSTANCE_VARIABLES_NMSMusicRecommendationsRequestOperationContext
+ __OBJC_$_PROP_LIST_NMSMusicRecommendationsRequestOperationContext
+ __OBJC_CLASS_RO_$_NMSMusicRecommendationsRequestOperation
+ __OBJC_CLASS_RO_$_NMSMusicRecommendationsRequestOperationContext
+ __OBJC_METACLASS_RO_$_NMSMusicRecommendationsRequestOperation
+ __OBJC_METACLASS_RO_$_NMSMusicRecommendationsRequestOperationContext
+ ___105-[NMSMusicRecommendationsRequestOperation _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke
+ ___105-[NMSMusicRecommendationsRequestOperation _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.132
+ ___105-[NMSMusicRecommendationsRequestOperation _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.132.cold.1
+ ___105-[NMSMusicRecommendationsRequestOperation _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.135
+ ___105-[NMSMusicRecommendationsRequestOperation _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.135.cold.1
+ ___111-[NMSMusicRecommendationsRequestOperation _performLegacyLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke
+ ___111-[NMSMusicRecommendationsRequestOperation _performLegacyLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.cold.1
+ ___64+[NMSMusicRecommendationsRequestOperation _recentMusicDirectory]_block_invoke
+ ___67-[NMSMusicRecommendationsRequestOperation _continueToLibraryImport]_block_invoke
+ ___67-[NMSMusicRecommendationsRequestOperation _continueToLibraryImport]_block_invoke_2
+ ___67-[NMSMusicRecommendationsRequestOperation _continueToLibraryImport]_block_invoke_3
+ ___72-[NMSMusicRecommendationsRequestOperation _continueToLibraryPinsRequest]_block_invoke
+ ___72-[NMSMusicRecommendationsRequestOperation _continueToLibraryPinsRequest]_block_invoke_2
+ ___73-[NMSMusicRecommendationsRequestOperation _continueToLegacyForYouRequest]_block_invoke
+ ___73-[NMSMusicRecommendationsRequestOperation _continueToLegacyForYouRequest]_block_invoke_2
+ ___74-[NMSMusicRecommendationsRequestOperation _continueToHeavyRotationRequest]_block_invoke
+ ___74-[NMSMusicRecommendationsRequestOperation _continueToHeavyRotationRequest]_block_invoke_2
+ ___75-[NMSMusicRecommendationsRequestOperationContext _processResponsesIfNeeded]_block_invoke
+ ___75-[NMSMusicRecommendationsRequestOperationContext _processResponsesIfNeeded]_block_invoke.231
+ ___75-[NMSMusicRecommendationsRequestOperationContext _processResponsesIfNeeded]_block_invoke.236
+ ___75-[NMSMusicRecommendationsRequestOperationContext _processResponsesIfNeeded]_block_invoke.237
+ ___75-[NMSMusicRecommendationsRequestOperationContext _processResponsesIfNeeded]_block_invoke.247
+ ___75-[NMSMusicRecommendationsRequestOperationContext _processResponsesIfNeeded]_block_invoke.248
+ ___75-[NMSMusicRecommendationsRequestOperationContext _processResponsesIfNeeded]_block_invoke.253
+ ___75-[NMSMusicRecommendationsRequestOperationContext _processResponsesIfNeeded]_block_invoke.254
+ ___75-[NMSMusicRecommendationsRequestOperationContext _processResponsesIfNeeded]_block_invoke.cold.1
+ ___75-[NMSMusicRecommendationsRequestOperationContext _processResponsesIfNeeded]_block_invoke_2
+ ___76-[NMSMusicRecommendationsRequestOperation _continueToLegacyEditorialRequest]_block_invoke
+ ___76-[NMSMusicRecommendationsRequestOperation _continueToLegacyEditorialRequest]_block_invoke_2
+ ___79-[NMSMusicRecommendationsRequestOperation _performForYouRequestWithCompletion:]_block_invoke
+ ___79-[NMSMusicRecommendationsRequestOperation _performForYouRequestWithCompletion:]_block_invoke.cold.1
+ ___81-[NMSMusicRecommendationsRequestOperation _continueToStarterPackMultiplexRequest]_block_invoke
+ ___81-[NMSMusicRecommendationsRequestOperation _continueToStarterPackMultiplexRequest]_block_invoke_2
+ ___82-[NMSMusicRecommendationsRequestOperationContext _recentMusicContainsModelObject:]_block_invoke
+ ___84-[NMSMusicRecommendationsRequestOperation _continueToStarterPackRoomRequestWithURL:]_block_invoke
+ ___84-[NMSMusicRecommendationsRequestOperation _continueToStarterPackRoomRequestWithURL:]_block_invoke_2
+ ___86-[NMSMusicRecommendationsRequestOperation _continueToLibraryRecentMusicRecommedations]_block_invoke
+ ___86-[NMSMusicRecommendationsRequestOperation _continueToLibraryRecentMusicRecommedations]_block_invoke_2
+ ___86-[NMSMusicRecommendationsRequestOperation _performHeavyRotationRequestWithCompletion:]_block_invoke
+ ___86-[NMSMusicRecommendationsRequestOperation _performHeavyRotationRequestWithCompletion:]_block_invoke.cold.1
+ ___88-[NMSMusicRecommendationsRequestOperation _performEditorialBrowseRequestWithCompletion:]_block_invoke
+ ___88-[NMSMusicRecommendationsRequestOperation _performEditorialBrowseRequestWithCompletion:]_block_invoke.cold.1
+ ___91-[NMSMusicRecommendationsRequestOperation _performLibraryRecentMusicRequestWithCompletion:]_block_invoke
+ ___91-[NMSMusicRecommendationsRequestOperation _performLibraryRecentMusicRequestWithCompletion:]_block_invoke.113
+ ___91-[NMSMusicRecommendationsRequestOperation _performLibraryRecentMusicRequestWithCompletion:]_block_invoke.121
+ ___91-[NMSMusicRecommendationsRequestOperation _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2
+ ___91-[NMSMusicRecommendationsRequestOperation _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2.115
+ ___91-[NMSMusicRecommendationsRequestOperation _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_3
+ ___91-[NMSMusicRecommendationsRequestOperation _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_3.120
+ ___91-[NMSMusicRecommendationsRequestOperation _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_3.120.cold.1
+ ___91-[NMSMusicRecommendationsRequestOperation _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_3.cold.1
+ ___92-[NMSMusicRecommendationsRequestOperation _performStarterPackRoomRequestWithURL:completion:]_block_invoke
+ ___92-[NMSMusicRecommendationsRequestOperation _performStarterPackRoomRequestWithURL:completion:]_block_invoke.cold.1
+ ___93-[NMSMusicRecommendationsRequestOperation _performStarterPackMultiplexRequestWithCompletion:]_block_invoke
+ ___93-[NMSMusicRecommendationsRequestOperation _performStarterPackMultiplexRequestWithCompletion:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32s_e48_v24?0"MPModelStoreBrowseResponse"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e58_v24?0"MPModelForYouRecommendationsResponse"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_literal_global.147
+ _objc_msgSend$_continueToHeavyRotationRequest
+ _objc_msgSend$_continueToLegacyEditorialRequest
+ _objc_msgSend$_continueToLegacyForYouRequest
+ _objc_msgSend$_continueToLibraryImport
+ _objc_msgSend$_continueToLibraryPinsRequest
+ _objc_msgSend$_continueToLibraryRecentMusicRecommedations
+ _objc_msgSend$_continueToProcessResults
+ _objc_msgSend$_continueToRecentMusicRequest
+ _objc_msgSend$_continueToStarterPackMultiplexRequest
+ _objc_msgSend$_continueToStarterPackRoomRequestWithURL:
+ _objc_msgSend$_finish
+ _objc_msgSend$currentQueue
+ _objc_msgSend$finish
+ _objc_msgSend$finishWithError:
+ _objc_msgSend$useCachedDataOnly
+ _objc_sync_enter
+ _objc_sync_exit
- +[NMSMusicRecommendationsRequest _recentMusicDirectory]
- +[NMSMusicRecommendationsRequest _recentMusicDirectory].cold.1
- -[NMSMusicRecommendationsRequest _continueToHeavyRotationRequestWithContext:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _continueToLegacyEditorialRequestWithContext:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _continueToLegacyForYouRequestWithContext:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _continueToLibraryImportWithContext:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _continueToLibraryPinsRequestWithContext:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _continueToLibraryRecentMusicRecommedationsWithContext:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _continueToProcessResultsWithContext:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _continueToRecentMusicRequestWithContext:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _continueToStarterPackMultiplexRequestWithContext:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _continueToStarterPackRoomRequestWithURL:context:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _finishWithContext:queue:responseHandler:]
- -[NMSMusicRecommendationsRequest _finishWithContext:queue:responseHandler:].cold.1
- -[NMSMusicRecommendationsRequest _heavyRotationCacheURL]
- -[NMSMusicRecommendationsRequest _isLibraryPinsSupported]
- -[NMSMusicRecommendationsRequest _performEditorialBrowseRequestWithCompletion:]
- -[NMSMusicRecommendationsRequest _performForYouRequestWithCompletion:]
- -[NMSMusicRecommendationsRequest _performHeavyRotationRequestWithCompletion:]
- -[NMSMusicRecommendationsRequest _performLegacyLibraryImportChangeRequestWithModelObjects:completion:]
- -[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]
- -[NMSMusicRecommendationsRequest _performLibraryPinsRequestWithCompletion:]
- -[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]
- -[NMSMusicRecommendationsRequest _performStarterPackMultiplexRequestWithCompletion:]
- -[NMSMusicRecommendationsRequest _performStarterPackRoomRequestWithURL:completion:]
- -[NMSMusicRecommendationsRequest _starterPackMultiplexCacheURL]
- -[NMSMusicRecommendationsRequest _starterPackRoomCacheURL]
- -[NMSMusicRecommendationsRequest _unarchivedCombinedResponsesDictionary]
- -[NMSMusicRecommendationsRequest _unarchivedCombinedResponsesDictionary].cold.1
- -[NMSMusicRecommendationsRequest _writeData:toURL:]
- -[NMSMusicRecommendationsRequest _writeData:toURL:].cold.1
- -[NMSMusicRecommendationsRequest _writeData:toURL:].cold.2
- -[NMSMusicRecommendationsRequest setUnarchivedCombinedResponsesDictionary:]
- -[NMSMusicRecommendationsRequest unarchivedCombinedResponsesDictionary]
- -[NMSMusicRecommendationsRequestContext .cxx_destruct]
- -[NMSMusicRecommendationsRequestContext _hasDownloadableSongsForModelObject:]
- -[NMSMusicRecommendationsRequestContext _processRecentMusicItem:section:identifier:]
- -[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]
- -[NMSMusicRecommendationsRequestContext _recentMusicContainsModelObject:]
- -[NMSMusicRecommendationsRequestContext editorialBrowseResponse]
- -[NMSMusicRecommendationsRequestContext forYouResponse]
- -[NMSMusicRecommendationsRequestContext heavyRotationResponse]
- -[NMSMusicRecommendationsRequestContext libraryPinsResponse]
- -[NMSMusicRecommendationsRequestContext libraryRecentMusicResponse]
- -[NMSMusicRecommendationsRequestContext minimumNumberOfRecentMusicModelObjects]
- -[NMSMusicRecommendationsRequestContext modelObjects]
- -[NMSMusicRecommendationsRequestContext numberOfRecentMusicModelObjects]
- -[NMSMusicRecommendationsRequestContext recommendations]
- -[NMSMusicRecommendationsRequestContext setEditorialBrowseResponse:]
- -[NMSMusicRecommendationsRequestContext setForYouResponse:]
- -[NMSMusicRecommendationsRequestContext setHeavyRotationResponse:]
- -[NMSMusicRecommendationsRequestContext setLibraryPinsResponse:]
- -[NMSMusicRecommendationsRequestContext setLibraryRecentMusicResponse:]
- -[NMSMusicRecommendationsRequestContext setMinimumNumberOfRecentMusicModelObjects:]
- -[NMSMusicRecommendationsRequestContext setStarterPackResponse:]
- -[NMSMusicRecommendationsRequestContext starterPackResponse]
- GCC_except_table43
- GCC_except_table97
- _OBJC_CLASS_$_NMSMusicRecommendationsRequestContext
- _OBJC_IVAR_$_NMSMusicRecommendationsRequest._unarchivedCombinedResponsesDictionary
- _OBJC_IVAR_$_NMSMusicRecommendationsRequestContext._editorialBrowseResponse
- _OBJC_IVAR_$_NMSMusicRecommendationsRequestContext._forYouResponse
- _OBJC_IVAR_$_NMSMusicRecommendationsRequestContext._heavyRotationResponse
- _OBJC_IVAR_$_NMSMusicRecommendationsRequestContext._libraryPinsModelObjects
- _OBJC_IVAR_$_NMSMusicRecommendationsRequestContext._libraryPinsResponse
- _OBJC_IVAR_$_NMSMusicRecommendationsRequestContext._libraryRecentMusicResponse
- _OBJC_IVAR_$_NMSMusicRecommendationsRequestContext._minimumNumberOfRecentMusicModelObjects
- _OBJC_IVAR_$_NMSMusicRecommendationsRequestContext._recentMusicModelObjects
- _OBJC_IVAR_$_NMSMusicRecommendationsRequestContext._starterPackResponse
- _OBJC_METACLASS_$_NMSMusicRecommendationsRequestContext
- __OBJC_$_CLASS_METHODS_NMSMusicRecommendationsRequest
- __OBJC_$_INSTANCE_METHODS_NMSMusicRecommendationsRequestContext
- __OBJC_$_INSTANCE_VARIABLES_NMSMusicRecommendationsRequestContext
- __OBJC_$_PROP_LIST_NMSMusicRecommendationsRequestContext
- __OBJC_CLASS_RO_$_NMSMusicRecommendationsRequestContext
- __OBJC_METACLASS_RO_$_NMSMusicRecommendationsRequestContext
- ___101-[NMSMusicRecommendationsRequest _continueToLegacyEditorialRequestWithContext:queue:responseHandler:]_block_invoke
- ___101-[NMSMusicRecommendationsRequest _continueToLegacyEditorialRequestWithContext:queue:responseHandler:]_block_invoke_2
- ___102-[NMSMusicRecommendationsRequest _performLegacyLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke
- ___102-[NMSMusicRecommendationsRequest _performLegacyLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.cold.1
- ___105-[NMSMusicRecommendationsRequest _continueToStarterPackRoomRequestWithURL:context:queue:responseHandler:]_block_invoke
- ___105-[NMSMusicRecommendationsRequest _continueToStarterPackRoomRequestWithURL:context:queue:responseHandler:]_block_invoke_2
- ___106-[NMSMusicRecommendationsRequest _continueToStarterPackMultiplexRequestWithContext:queue:responseHandler:]_block_invoke
- ___106-[NMSMusicRecommendationsRequest _continueToStarterPackMultiplexRequestWithContext:queue:responseHandler:]_block_invoke_2
- ___111-[NMSMusicRecommendationsRequest _continueToLibraryRecentMusicRecommedationsWithContext:queue:responseHandler:]_block_invoke
- ___111-[NMSMusicRecommendationsRequest _continueToLibraryRecentMusicRecommedationsWithContext:queue:responseHandler:]_block_invoke_2
- ___55+[NMSMusicRecommendationsRequest _recentMusicDirectory]_block_invoke
- ___61-[NMSMusicRecommendationsRequest performWithResponseHandler:]_block_invoke
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.218
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.223
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.224
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.234
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.235
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.240
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.241
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke.cold.1
- ___66-[NMSMusicRecommendationsRequestContext _processResponsesIfNeeded]_block_invoke_2
- ___70-[NMSMusicRecommendationsRequest _performForYouRequestWithCompletion:]_block_invoke
- ___70-[NMSMusicRecommendationsRequest _performForYouRequestWithCompletion:]_block_invoke.cold.1
- ___73-[NMSMusicRecommendationsRequestContext _recentMusicContainsModelObject:]_block_invoke
- ___77-[NMSMusicRecommendationsRequest _performHeavyRotationRequestWithCompletion:]_block_invoke
- ___77-[NMSMusicRecommendationsRequest _performHeavyRotationRequestWithCompletion:]_block_invoke.cold.1
- ___79-[NMSMusicRecommendationsRequest _performEditorialBrowseRequestWithCompletion:]_block_invoke
- ___79-[NMSMusicRecommendationsRequest _performEditorialBrowseRequestWithCompletion:]_block_invoke.cold.1
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke.86
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke.95
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2.88
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_2.96
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_3
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_3.90
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_3.cold.1
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_4
- ___82-[NMSMusicRecommendationsRequest _performLibraryRecentMusicRequestWithCompletion:]_block_invoke_4.cold.1
- ___83-[NMSMusicRecommendationsRequest _performStarterPackRoomRequestWithURL:completion:]_block_invoke
- ___83-[NMSMusicRecommendationsRequest _performStarterPackRoomRequestWithURL:completion:]_block_invoke.cold.1
- ___84-[NMSMusicRecommendationsRequest _performStarterPackMultiplexRequestWithCompletion:]_block_invoke
- ___84-[NMSMusicRecommendationsRequest _performStarterPackMultiplexRequestWithCompletion:]_block_invoke.cold.1
- ___92-[NMSMusicRecommendationsRequest _continueToLibraryImportWithContext:queue:responseHandler:]_block_invoke
- ___92-[NMSMusicRecommendationsRequest _continueToLibraryImportWithContext:queue:responseHandler:]_block_invoke_2
- ___92-[NMSMusicRecommendationsRequest _continueToLibraryImportWithContext:queue:responseHandler:]_block_invoke_3
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.107
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.107.cold.1
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.110
- ___96-[NMSMusicRecommendationsRequest _performLibraryImportChangeRequestWithModelObjects:completion:]_block_invoke.110.cold.1
- ___97-[NMSMusicRecommendationsRequest _continueToLibraryPinsRequestWithContext:queue:responseHandler:]_block_invoke
- ___97-[NMSMusicRecommendationsRequest _continueToLibraryPinsRequestWithContext:queue:responseHandler:]_block_invoke_2
- ___98-[NMSMusicRecommendationsRequest _continueToLegacyForYouRequestWithContext:queue:responseHandler:]_block_invoke
- ___98-[NMSMusicRecommendationsRequest _continueToLegacyForYouRequestWithContext:queue:responseHandler:]_block_invoke_2
- ___99-[NMSMusicRecommendationsRequest _continueToHeavyRotationRequestWithContext:queue:responseHandler:]_block_invoke
- ___99-[NMSMusicRecommendationsRequest _continueToHeavyRotationRequestWithContext:queue:responseHandler:]_block_invoke_2
- ___block_descriptor_48_e8_32bs40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e37_v24?0"MPModelResponse"8"NSError"16ls32l8s56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e48_v24?0"MPModelStoreBrowseResponse"8"NSError"16ls32l8s56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e58_v24?0"MPModelForYouRecommendationsResponse"8"NSError"16ls32l8s56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0lr56l8s32l8r64l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
- ___block_literal_global.124
- _objc_msgSend$_continueToHeavyRotationRequestWithContext:queue:responseHandler:
- _objc_msgSend$_continueToLegacyEditorialRequestWithContext:queue:responseHandler:
- _objc_msgSend$_continueToLegacyForYouRequestWithContext:queue:responseHandler:
- _objc_msgSend$_continueToLibraryImportWithContext:queue:responseHandler:
- _objc_msgSend$_continueToLibraryPinsRequestWithContext:queue:responseHandler:
- _objc_msgSend$_continueToLibraryRecentMusicRecommedationsWithContext:queue:responseHandler:
- _objc_msgSend$_continueToProcessResultsWithContext:queue:responseHandler:
- _objc_msgSend$_continueToRecentMusicRequestWithContext:queue:responseHandler:
- _objc_msgSend$_continueToStarterPackMultiplexRequestWithContext:queue:responseHandler:
- _objc_msgSend$_continueToStarterPackRoomRequestWithURL:context:queue:responseHandler:
- _objc_msgSend$_finishWithContext:queue:responseHandler:
CStrings:
+ "!"
+ "06fb3b8e-7ce9-4c98-a47e-87bcccb70ec1"
+ "54fc3688-3f2a-435a-a95d-2f1866839415"
+ "88d7381b-f0d1-498f-88d5-9f016a27eb4f"
+ "@\"NMSMusicRecommendationsRequest\""
+ "@\"NMSMusicRecommendationsRequestOperationContext\""
+ "@32@0:8@16@?24"
+ "NMSMusicRecommendationsRequestOperation"
+ "NMSMusicRecommendationsRequestOperationContext"
+ "_context"
+ "_continueToHeavyRotationRequest"
+ "_continueToLegacyEditorialRequest"
+ "_continueToLegacyForYouRequest"
+ "_continueToLibraryImport"
+ "_continueToLibraryPinsRequest"
+ "_continueToLibraryRecentMusicRecommedations"
+ "_continueToProcessResults"
+ "_continueToRecentMusicRequest"
+ "_continueToStarterPackMultiplexRequest"
+ "_continueToStarterPackRoomRequestWithURL:"
+ "_finish"
+ "_request"
+ "_responseHandler"
+ "c5092de9-70b8-41db-b2ab-80dd86ed41c7"
+ "c79d46d1-84cf-4208-aea0-39117f9770e7"
+ "com.apple.NanoMusicSync.NMSMusicRecommendationsRequest-%@"
+ "currentQueue"
+ "d718e4be-8067-432e-af41-7342473499d5"
+ "finish"
+ "finishWithError:"
- "06FB3B8E-332F-481C-B7DE-7E80973B07BF"
- "54FC3688-332F-481C-B7DE-7E80973B07BF"
- "88D7381B-332F-481C-B7DE-7E80973B07BF"
- "C5092DE9-332F-481C-B7DE-7E80973B07BF"
- "C79D46D1-332F-481C-B7DE-7E80973B07BF"
- "D718E4BE-332F-481C-B7DE-7E80973B07BF"
- "NMSMusicRecommendationsRequestContext"
- "T@\"NSDictionary\",&,N,V_unarchivedCombinedResponsesDictionary"
- "_continueToHeavyRotationRequestWithContext:queue:responseHandler:"
- "_continueToLegacyEditorialRequestWithContext:queue:responseHandler:"
- "_continueToLegacyForYouRequestWithContext:queue:responseHandler:"
- "_continueToLibraryImportWithContext:queue:responseHandler:"
- "_continueToLibraryPinsRequestWithContext:queue:responseHandler:"
- "_continueToLibraryRecentMusicRecommedationsWithContext:queue:responseHandler:"
- "_continueToProcessResultsWithContext:queue:responseHandler:"
- "_continueToRecentMusicRequestWithContext:queue:responseHandler:"
- "_continueToStarterPackMultiplexRequestWithContext:queue:responseHandler:"
- "_continueToStarterPackRoomRequestWithURL:context:queue:responseHandler:"
- "_finishWithContext:queue:responseHandler:"
- "com.apple.NanoMusicSync.NMSMusicRecommendationsRequest"
- "com.apple.NanoMusicSync.NMSMusicRecommendationsRequest.LibraryCompletion"
- "setUnarchivedCombinedResponsesDictionary:"
- "unarchivedCombinedResponsesDictionary"
- "v48@0:8@16@24@32@?40"

```
