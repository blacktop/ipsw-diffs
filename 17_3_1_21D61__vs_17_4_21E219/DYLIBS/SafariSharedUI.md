## SafariSharedUI

> `/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI`

```diff

-617.2.4.10.8
-  __TEXT.__text: 0x16faf8
-  __TEXT.__auth_stubs: 0x1440
-  __TEXT.__objc_methlist: 0xc7d4
-  __TEXT.__gcc_except_tab: 0x1ea1c
-  __TEXT.__const: 0xd70
-  __TEXT.__cstring: 0x1827b
-  __TEXT.__oslogstring: 0xae95
+618.1.15.10.11
+  __TEXT.__text: 0x16ff44
+  __TEXT.__auth_stubs: 0x1450
+  __TEXT.__objc_methlist: 0xc744
+  __TEXT.__gcc_except_tab: 0x1e96c
+  __TEXT.__cstring: 0x17f82
+  __TEXT.__const: 0x26e0
+  __TEXT.__oslogstring: 0xade1
   __TEXT.__ustring: 0x1f00
   __TEXT.__dlopen_cstrs: 0x3f8
-  __TEXT.__unwind_info: 0x9ca0
+  __TEXT.__unwind_info: 0x9cc4
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x27ae
-  __TEXT.__objc_methname: 0x3124b
-  __TEXT.__objc_methtype: 0x7768
-  __TEXT.__objc_stubs: 0x1c7c0
-  __DATA_CONST.__got: 0x7c8
-  __DATA_CONST.__const: 0x7480
-  __DATA_CONST.__objc_classlist: 0x7a8
-  __DATA_CONST.__objc_catlist: 0xe0
+  __TEXT.__objc_classname: 0x27d3
+  __TEXT.__objc_methname: 0x31661
+  __TEXT.__objc_methtype: 0x78c9
+  __TEXT.__objc_stubs: 0x1cbe0
+  __DATA_CONST.__got: 0x7b8
+  __DATA_CONST.__const: 0x74d0
+  __DATA_CONST.__objc_classlist: 0x7b0
+  __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x18a70
-  __DATA_CONST.__objc_selrefs: 0x8c88
+  __DATA_CONST.__objc_const: 0x18688
+  __DATA_CONST.__objc_selrefs: 0x8da0
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0xc90
+  __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_arraydata: 0x2150
-  __AUTH_CONST.__objc_const: 0x60b8
-  __AUTH_CONST.__cfstring: 0x17580
-  __AUTH_CONST.__const: 0x3a48
+  __AUTH_CONST.__const: 0x3aa8
+  __AUTH_CONST.__cfstring: 0x17100
+  __AUTH_CONST.__objc_const: 0x60b0
   __AUTH_CONST.__objc_intobj: 0xc48
-  __AUTH_CONST.__objc_arrayobj: 0x888
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH_CONST.__objc_dictobj: 0x370
+  __AUTH_CONST.__objc_arrayobj: 0x888
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xa38
-  __AUTH.__objc_data: 0x48d0
+  __AUTH_CONST.__objc_dictobj: 0x370
+  __AUTH_CONST.__auth_got: 0xa40
+  __AUTH.__objc_data: 0x4920
   __AUTH.__data: 0x70
   __DATA.__got_weak: 0xd0
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0xc70
-  __DATA.__objc_superrefs: 0x578
-  __DATA.__objc_ivar: 0x1378
-  __DATA.__data: 0x1f78
-  __DATA.__bss: 0x1050
+  __DATA.__objc_ivar: 0x1318
+  __DATA.__data: 0x1f80
+  __DATA.__bss: 0x1068
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__bss: 0x29
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/ContextKit.framework/ContextKit
   - /System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec
   - /System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7533
-  Symbols:   27010
-  CStrings:  11762
+  Functions: 7534
+  Symbols:   27025
+  CStrings:  11760
 
Symbols:
+ +[WBSSchemaDataExtractor fetchDataFromWebView:completion:]
+ +[WBSWebExtensionMatchPattern matchPatternWtihWebKitPattern:]
+ +[WBSWebExtensionMatchPattern matchPatternsWtihWebKitPatterns:]
+ +[_WBSBookmarkFolderTouchIconProviderInfo new]
+ +[_WBSWKApplicationManifestExtrasUtilities applicationCategoryTypeForCategories:]
+ -[NSString(SafariSharedUIExtras) _leadingGlyphInCTRunSafariIsRightToLeft:]
+ -[NSString(SafariSharedUIExtras) safari_hasLeadingEmojiSafariIsRightToLeft:]
+ -[NSString(SafariSharedUIExtras) safari_leadingEmojiSafariIsRightToLeft:]
+ -[WBSBiomeDonationManager(SafariSharedUI) _biomeWindowProperty:]
+ -[WBSBiomeDonationManager(SafariSharedUI) donateWindowProxyWithDomain:openedDomain:windowProxyProperty:accessedPropertyDirectly:]
+ -[WBSBookmarkFolderTouchIconProvider _registerInfo:forRequest:]
+ -[WBSBookmarkFolderTouchIconProvider _stopWatchingUpdatesForRequests:]
+ -[WBSBookmarkFolderTouchIconProvider cachedImageForFolderUUID:]
+ -[WBSBookmarkFolderTouchIconProvider canProvideUpdatesForRequest:]
+ -[WBSBookmarkFolderTouchIconProvider contentOfFolderDidUpdateWithUUID:]
+ -[WBSBookmarkFolderTouchIconProvider folderUUIDForRequest:]
+ -[WBSBookmarkFolderTouchIconProvider requestsWithFolderUUIDsDidBecomeInvalid:]
+ -[WBSBookmarkFolderTouchIconProvider subrequestsForRequest:maximumNumberOfSubrequests:]
+ -[WBSPageContextDataFetcher .cxx_destruct]
+ -[WBSPageContextDataFetcher clearExtractedSchemaData]
+ -[WBSPageContextDataFetcher delegate]
+ -[WBSPageContextDataFetcher fetchSchemaDataForWebView:]
+ -[WBSPageContextDataFetcher filteredSchemaData]
+ -[WBSPageContextDataFetcher setDelegate:]
+ -[WBSParsecSearchResult stringForType]
+ -[WBSPhishingAssetController didDownloadDataForRemotelyUpdatableDataController:]
+ -[WBSPhishingConfiguration initWithSnapshotData:error:]
+ -[WBSPhishingConfiguration snapshotData]
+ -[WBSSiteMetadataManager _enumerateTokens:usingSetUpBlock:dispatchBlock:]
+ -[WBSSiteMetadataManager _highestRequestPriorityForRequests:]
+ -[WBSSiteMetadataManager _registerRequest:isOneTimeRequest:queue:responseHandler:tokenSetUpBlock:]
+ -[WBSSiteMetadataManager _registerSubrequest:isOneTimeRequest:forRequests:queue:responseHandler:]
+ -[WBSSiteMetadataManager _registerToken:isCacheRequest:withProvider:]
+ -[WBSSiteMetadataManager _sendResponse:toResponseHandlersForRequests:didReceiveNewData:]
+ -[WBSSiteMetadataManager _updatePriorityOfRequest:]
+ -[WBSSiteMetadataManager cacheData:forRequest:]
+ -[WBSSiteMetadataManager preloadRequest:withPriority:queue:responseHandler:]
+ -[WBSSiteMetadataManager preloadRequests:withPriority:queue:responseHandler:]
+ -[WBSSiteMetadataManager registerOneTimeRequest:priority:queue:responseHandler:]
+ -[WBSSiteMetadataManager registerRequest:priority:queue:responseHandler:]
+ -[WBSSiteMetadataManager siteMetadataProvider:cacheData:forRequest:]
+ -[WBSSiteMetadataManager siteMetadataProvider:didFinishCachingDataWithToken:]
+ -[WBSSiteMetadataManager siteMetadataProvider:didReceiveResponse:ofType:didReceiveNewData:forRequests:]
+ -[WBSSiteMetadataManager siteMetadataProvider:registerOneTimeSubrequest:forRequests:queue:responseHandler:]
+ -[WBSSiteMetadataManager siteMetadataProvider:registerSubrequest:forRequests:queue:responseHandler:]
+ -[WBSTabGroupTouchIconProvider canProvideUpdatesForRequest:]
+ -[WBSTabGroupTouchIconProvider folderUUIDForRequest:]
+ -[WBSTabGroupTouchIconProvider subrequestsForRequest:maximumNumberOfSubrequests:]
+ -[WBSTemplateIconCache cacheData:forRequest:usingToken:]
+ -[WBSTemplateIconCacheRecord .cxx_destruct]
+ -[WBSTemplateIconCacheRecord canSaveToDisk]
+ -[WBSTemplateIconCacheRecord host]
+ -[WBSTemplateIconCacheRecord initWithHost:templateIconURL:themeColor:canSaveToDisk:]
+ -[WBSTemplateIconCacheRecord templateIconURL]
+ -[WBSTemplateIconCacheRecord themeColor]
+ -[WBSTemplateIconRequest initWithURL:title:monogramConfiguration:overrideForegroundColor:]
+ -[WBSWebExtensionCommand debugDescription]
+ -[WBSWebExtensionData dynamicRulesIDs]
+ -[WBSWebExtensionData initWithExtension:extensionsController:extensionBundleIdentifier:extensionIdentifier:uniqueIdentifier:baseURIHost:].cold.1
+ -[WBSWebExtensionData sessionRulesIDs]
+ -[WBSWebExtensionData setDynamicRulesIDs:]
+ -[WBSWebExtensionData setSessionRulesIDs:]
+ -[WBSWebExtensionData webKitExtension]
+ -[WBSWebExtensionMatchPattern initWithWebKitMatchPattern:]
+ -[WBSWebExtensionsController _webViewConfiguration]
+ -[WBSWebExtensionsController loadSuitableDiscoveredExtensions]
+ -[_WBSBookmarkFolderTouchIconProviderInfo .cxx_destruct]
+ -[_WBSBookmarkFolderTouchIconProviderInfo backgroundColors]
+ -[_WBSBookmarkFolderTouchIconProviderInfo initWithThumbnailImages:backgroundColors:touchIcon:]
+ -[_WBSBookmarkFolderTouchIconProviderInfo init]
+ -[_WBSBookmarkFolderTouchIconProviderInfo thumbnailImages]
+ -[_WBSBookmarkFolderTouchIconProviderInfo touchIcon]
+ -[_WBSBookmarkFolderTouchIconProviderRequestInfo .cxx_destruct]
+ -[_WBSBookmarkFolderTouchIconProviderRequestInfo backgroundColors]
+ -[_WBSBookmarkFolderTouchIconProviderRequestInfo hasScheduledCoalescedUpdate]
+ -[_WBSBookmarkFolderTouchIconProviderRequestInfo init]
+ -[_WBSBookmarkFolderTouchIconProviderRequestInfo setBackgroundColor:atIndex:]
+ -[_WBSBookmarkFolderTouchIconProviderRequestInfo setHasScheduledCoalescedUpdate:]
+ -[_WBSBookmarkFolderTouchIconProviderRequestInfo setSubrequestTokens:]
+ -[_WBSBookmarkFolderTouchIconProviderRequestInfo setSubrequests:]
+ -[_WBSBookmarkFolderTouchIconProviderRequestInfo setThumbnailImage:atIndex:]
+ -[_WBSBookmarkFolderTouchIconProviderRequestInfo subrequestTokens]
+ -[_WBSBookmarkFolderTouchIconProviderRequestInfo subrequests]
+ -[_WBSBookmarkFolderTouchIconProviderRequestInfo thumbnailImages]
+ -[_WBSSiteMetadataRequestInfo addCacheRequestToken:]
+ -[_WBSSiteMetadataRequestInfo addRequestToken:]
+ -[_WBSSiteMetadataRequestInfo canStopWatchingRequestAfterRemovingToken:]
+ -[_WBSSiteMetadataRequestInfo requestTokens]
+ -[_WBSSiteMetadataToken initWithRequest:isOneTimeRequest:queue:responseHandler:]
+ -[_WBSSiteMetadataToken parentRequests]
+ -[_WBSSiteMetadataToken queue]
+ -[_WBSSiteMetadataToken removeParentRequest:]
+ -[_WBSSiteMetadataToken setParentRequests:]
+ -[_WKApplicationManifest(SafariSharedUIExtras) safari_applicationCategoryType]
+ GCC_except_table123
+ GCC_except_table187
+ GCC_except_table210
+ GCC_except_table214
+ GCC_except_table216
+ GCC_except_table221
+ GCC_except_table241
+ GCC_except_table249
+ GCC_except_table258
+ GCC_except_table336
+ GCC_except_table382
+ GCC_except_table383
+ GCC_except_table388
+ GCC_except_table390
+ GCC_except_table397
+ GCC_except_table403
+ GCC_except_table404
+ GCC_except_table409
+ GCC_except_table411
+ GCC_except_table413
+ GCC_except_table417
+ OBJC_IVAR_$_WBSBiomeDonationManager._streamAccessQueue
+ _CFDictionaryCreateMutable
+ _OBJC_CLASS_$_BMSafariWindowProxy
+ _OBJC_CLASS_$_WBSBiomeDonationManager
+ _OBJC_CLASS_$_WBSDevice
+ _OBJC_CLASS_$_WBSPageContextDataFetcher
+ _OBJC_CLASS_$_WBSRemotelyUpdatableDataController
+ _OBJC_CLASS_$_WBSSchemaDataExtractor
+ _OBJC_CLASS_$_WBSTemplateIconCacheRecord
+ _OBJC_CLASS_$__WBSBookmarkFolderTouchIconProviderInfo
+ _OBJC_CLASS_$__WBSBookmarkFolderTouchIconProviderRequestInfo
+ _OBJC_CLASS_$__WBSWKApplicationManifestExtrasUtilities
+ _OBJC_CLASS_$__WKWebExtension
+ _OBJC_IVAR_$_WBSBookmarkFolderTouchIconProvider._bookmarkFolderIdentifiersToRequestSets
+ _OBJC_IVAR_$_WBSPageContextDataFetcher._delegate
+ _OBJC_IVAR_$_WBSPageContextDataFetcher._filteredSchemaData
+ _OBJC_IVAR_$_WBSSiteMetadataManager._requestsToCacheRequestTokens
+ _OBJC_IVAR_$_WBSSiteMetadataManager._requestsToSubrequestTokens
+ _OBJC_IVAR_$_WBSTemplateIconCache._pendingSVGImageRenderingRequestsThatCanBeSavedToDisk
+ _OBJC_IVAR_$_WBSTemplateIconCacheRecord._canSaveToDisk
+ _OBJC_IVAR_$_WBSTemplateIconCacheRecord._host
+ _OBJC_IVAR_$_WBSTemplateIconCacheRecord._templateIconURL
+ _OBJC_IVAR_$_WBSTemplateIconCacheRecord._themeColor
+ _OBJC_IVAR_$_WBSWebExtensionData._dynamicRulesIDs
+ _OBJC_IVAR_$_WBSWebExtensionData._sessionRulesIDs
+ _OBJC_IVAR_$_WBSWebExtensionData._webKitExtension
+ _OBJC_IVAR_$__WBSBookmarkFolderTouchIconProviderInfo._backgroundColors
+ _OBJC_IVAR_$__WBSBookmarkFolderTouchIconProviderInfo._thumbnailImages
+ _OBJC_IVAR_$__WBSBookmarkFolderTouchIconProviderInfo._touchIcon
+ _OBJC_IVAR_$__WBSBookmarkFolderTouchIconProviderRequestInfo._backgroundColors
+ _OBJC_IVAR_$__WBSBookmarkFolderTouchIconProviderRequestInfo._hasScheduledCoalescedUpdate
+ _OBJC_IVAR_$__WBSBookmarkFolderTouchIconProviderRequestInfo._subrequestTokens
+ _OBJC_IVAR_$__WBSBookmarkFolderTouchIconProviderRequestInfo._subrequests
+ _OBJC_IVAR_$__WBSBookmarkFolderTouchIconProviderRequestInfo._thumbnailImages
+ _OBJC_IVAR_$__WBSSiteMetadataRequestInfo._cacheRequestTokens
+ _OBJC_IVAR_$__WBSSiteMetadataRequestInfo._requestTokens
+ _OBJC_IVAR_$__WBSSiteMetadataToken._parentRequests
+ _OBJC_IVAR_$__WBSSiteMetadataToken._queue
+ _OBJC_METACLASS_$_WBSPageContextDataFetcher
+ _OBJC_METACLASS_$_WBSSchemaDataExtractor
+ _OBJC_METACLASS_$_WBSTemplateIconCacheRecord
+ _OBJC_METACLASS_$__WBSBookmarkFolderTouchIconProviderInfo
+ _OBJC_METACLASS_$__WBSBookmarkFolderTouchIconProviderRequestInfo
+ _OBJC_METACLASS_$__WBSWKApplicationManifestExtrasUtilities
+ _WBSTimestampForBiomeEventDonation
+ _WBS_LOG_CHANNEL_PREFIXSchemaDataLoading
+ _WBS_LOG_CHANNEL_PREFIXSchemaDataLoading.log
+ _WBS_LOG_CHANNEL_PREFIXSchemaDataLoading.onceToken
+ __OBJC_$_CATEGORY_NSString_$_WBSFaviconProviderNSStringExtras
+ __OBJC_$_CATEGORY_WBSBiomeDonationManager_$_SafariSharedUI
+ __OBJC_$_CLASS_METHODS_WBSSchemaDataExtractor
+ __OBJC_$_CLASS_METHODS__WBSBookmarkFolderTouchIconProviderInfo
+ __OBJC_$_CLASS_METHODS__WBSWKApplicationManifestExtrasUtilities
+ __OBJC_$_INSTANCE_METHODS_NSString(WBSFaviconProviderNSStringExtras|SafariSharedUIExtras)
+ __OBJC_$_INSTANCE_METHODS_WBSBiomeDonationManager(SafariSharedUI)
+ __OBJC_$_INSTANCE_METHODS_WBSPageContextDataFetcher
+ __OBJC_$_INSTANCE_METHODS_WBSTemplateIconCacheRecord
+ __OBJC_$_INSTANCE_METHODS__WBSBookmarkFolderTouchIconProviderInfo
+ __OBJC_$_INSTANCE_METHODS__WBSBookmarkFolderTouchIconProviderRequestInfo
+ __OBJC_$_INSTANCE_VARIABLES_WBSPageContextDataFetcher
+ __OBJC_$_INSTANCE_VARIABLES_WBSTemplateIconCacheRecord
+ __OBJC_$_INSTANCE_VARIABLES__WBSBookmarkFolderTouchIconProviderInfo
+ __OBJC_$_INSTANCE_VARIABLES__WBSBookmarkFolderTouchIconProviderRequestInfo
+ __OBJC_$_PROP_LIST_WBSPageContextDataFetcher
+ __OBJC_$_PROP_LIST_WBSParsecSearchGenericResult.74
+ __OBJC_$_PROP_LIST_WBSParsecSearchSimpleResult.84
+ __OBJC_$_PROP_LIST_WBSSearchProvider.277
+ __OBJC_$_PROP_LIST_WBSTemplateIconCacheRecord
+ __OBJC_$_PROP_LIST__WBSBookmarkFolderTouchIconProviderInfo
+ __OBJC_$_PROP_LIST__WBSBookmarkFolderTouchIconProviderRequestInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WBSRemotelyUpdatableDataControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WBSRemotelyUpdatableDataSnapshot
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WBSRemotelyUpdatableDataControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WBSRemotelyUpdatableDataSnapshot
+ __OBJC_$_PROTOCOL_REFS_WBSRemotelyUpdatableDataControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_WBSRemotelyUpdatableDataSnapshot
+ __OBJC_CLASS_RO_$_WBSPageContextDataFetcher
+ __OBJC_CLASS_RO_$_WBSSchemaDataExtractor
+ __OBJC_CLASS_RO_$_WBSTemplateIconCacheRecord
+ __OBJC_CLASS_RO_$__WBSBookmarkFolderTouchIconProviderInfo
+ __OBJC_CLASS_RO_$__WBSBookmarkFolderTouchIconProviderRequestInfo
+ __OBJC_CLASS_RO_$__WBSWKApplicationManifestExtrasUtilities
+ __OBJC_LABEL_PROTOCOL_$_WBSRemotelyUpdatableDataControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_WBSRemotelyUpdatableDataSnapshot
+ __OBJC_METACLASS_RO_$_WBSPageContextDataFetcher
+ __OBJC_METACLASS_RO_$_WBSSchemaDataExtractor
+ __OBJC_METACLASS_RO_$_WBSTemplateIconCacheRecord
+ __OBJC_METACLASS_RO_$__WBSBookmarkFolderTouchIconProviderInfo
+ __OBJC_METACLASS_RO_$__WBSBookmarkFolderTouchIconProviderRequestInfo
+ __OBJC_METACLASS_RO_$__WBSWKApplicationManifestExtrasUtilities
+ __OBJC_PROTOCOL_$_WBSRemotelyUpdatableDataControllerDelegate
+ __OBJC_PROTOCOL_$_WBSRemotelyUpdatableDataSnapshot
+ __UIImageGetCGImageRepresentation
+ __WBSSearchProviderShortNameOrderOnMac.definitionOrder.200
+ __WBSSearchProviderShortNameOrderOnMac.definitionOrder.204
+ __WBSSearchProviderShortNameOrderOnMac.onceToken.201
+ __WBSSearchProviderShortNameOrderOnMac.onceToken.205
+ ___103-[WBSSiteMetadataManager siteMetadataProvider:didReceiveResponse:ofType:didReceiveNewData:forRequests:]_block_invoke
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.460
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.460.cold.1
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.461
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.461.cold.1
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.462
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.463
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke_2.467
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke_2.467.cold.1
+ ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke.77
+ ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke.99
+ ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke_2.79
+ ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke_3.81
+ ___118-[WBSWebExtensionsController setKeyedData:inStorageOfType:forExtensionWithUniqueIdentifier:webView:completionHandler:]_block_invoke.345
+ ___122-[WBSWebExtensionsController updateDynamicDeclarativeNetRequestRulesForExtensionWithIdentifier:options:completionHandler:]_block_invoke_2
+ ___122-[WBSWebExtensionsController updateSessionDeclarativeNetRequestRulesForExtensionWithIdentifier:options:completionHandler:]_block_invoke_2
+ ___129-[WBSBiomeDonationManager(SafariSharedUI) donateWindowProxyWithDomain:openedDomain:windowProxyProperty:accessedPropertyDirectly:]_block_invoke
+ ___47-[WBSSiteMetadataManager cacheData:forRequest:]_block_invoke
+ ___47-[WBSSiteMetadataManager cacheData:forRequest:]_block_invoke_2
+ ___50-[WBSWebExtensionData _loadBackgroundPageWithURL:]_block_invoke.559
+ ___54-[WBSWebExtensionData _populateWebAccessibleResources]_block_invoke.347
+ ___54-[WBSWebExtensionData _populateWebAccessibleResources]_block_invoke.347.cold.1
+ ___55-[WBSPageContextDataFetcher fetchSchemaDataForWebView:]_block_invoke
+ ___55-[WBSPageContextDataFetcher fetchSchemaDataForWebView:]_block_invoke.cold.1
+ ___56-[WBSTemplateIconCache cacheData:forRequest:usingToken:]_block_invoke
+ ___56-[WBSTemplateIconCache cacheData:forRequest:usingToken:]_block_invoke_2
+ ___58+[WBSSchemaDataExtractor fetchDataFromWebView:completion:]_block_invoke
+ ___58+[WBSSchemaDataExtractor fetchDataFromWebView:completion:]_block_invoke.cold.1
+ ___58+[WBSSchemaDataExtractor fetchDataFromWebView:completion:]_block_invoke.cold.2
+ ___58+[WBSSchemaDataExtractor fetchDataFromWebView:completion:]_block_invoke.cold.3
+ ___58-[WBSSiteMetadataManager _internalCancelRequestWithToken:]_block_invoke.30
+ ___59-[WBSTouchIconFetchOperation _downloadPendingTouchIconURLs]_block_invoke.70
+ ___63+[WBSWebExtensionMatchPattern matchPatternsWtihWebKitPatterns:]_block_invoke
+ ___65-[WBSCloudExtensionStateManager _deleteCurrentDeviceFromCloudKit]_block_invoke.55
+ ___65-[WBSCloudExtensionStateManager _deleteCurrentDeviceFromCloudKit]_block_invoke.55.cold.1
+ ___71-[WBSBookmarkFolderTouchIconProvider contentOfFolderDidUpdateWithUUID:]_block_invoke
+ ___71-[WBSPhishingAssetController mobileAssetController:didBecomeAvailable:]_block_invoke.265
+ ___72-[WBSCloudExtensionStateManager _ensureCurrentDeviceIsSavedPeriodically]_block_invoke.70
+ ___73-[WBSSiteMetadataManager _enumerateTokens:usingSetUpBlock:dispatchBlock:]_block_invoke
+ ___73-[WBSSiteMetadataManager _enumerateTokens:usingSetUpBlock:dispatchBlock:]_block_invoke_2
+ ___73-[WBSSiteMetadataManager registerRequest:priority:queue:responseHandler:]_block_invoke
+ ___74-[WBSTouchIconFetchOperation didFetchTouchIconURLs:andFaviconURLs:forURL:]_block_invoke.78
+ ___77-[WBSSiteMetadataManager preloadRequests:withPriority:queue:responseHandler:]_block_invoke
+ ___77-[WBSSiteMetadataManager siteMetadataProvider:didFinishCachingDataWithToken:]_block_invoke
+ ___77-[WBSWebExtensionsController postMessage:fromPortWithID:fromExtensionWithID:]_block_invoke.300
+ ___78-[WBSBookmarkFolderTouchIconProvider requestsWithFolderUUIDsDidBecomeInvalid:]_block_invoke
+ ___78-[WBSTouchIconFetchOperation _downloadFirstValidImageWithURLs:failureHandler:]_block_invoke.66
+ ___79-[WBSWebExtensionsController _deleteStorageForExtensionWithComposedIdentifier:]_block_invoke.172
+ ___80-[WBSPhishingAssetController didDownloadDataForRemotelyUpdatableDataController:]_block_invoke
+ ___80-[WBSPhishingAssetController didDownloadDataForRemotelyUpdatableDataController:]_block_invoke_2
+ ___80-[WBSSiteMetadataManager registerOneTimeRequest:priority:queue:responseHandler:]_block_invoke
+ ___81-[WBSTabGroupTouchIconProvider subrequestsForRequest:maximumNumberOfSubrequests:]_block_invoke
+ ___84-[WBSWebExtensionData loadRegisteredContentScriptsFromStorageWithCompletionHandler:]_block_invoke.476
+ ___85-[WBSSiteMetadataManager _sendRequiresDownloadResponse:toResponseHandlersForRequest:]_block_invoke_2
+ ___86-[WBSBookmarkFolderTouchIconProvider _prepareResponseForRequest:allowDelayedResponse:]_block_invoke_2
+ ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke.414
+ ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke_2.415
+ ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke_2.415.cold.1
+ ___88-[WBSCloudExtensionStateManager _pruneInactiveDevicesFromCloudKitWithCompletionHandler:]_block_invoke.77
+ ___88-[WBSCloudExtensionStateManager _pruneInactiveDevicesFromCloudKitWithCompletionHandler:]_block_invoke.77.cold.1
+ ___88-[WBSSiteMetadataManager _sendResponse:toResponseHandlersForRequests:didReceiveNewData:]_block_invoke
+ ___88-[WBSSiteMetadataManager _sendResponse:toResponseHandlersForRequests:didReceiveNewData:]_block_invoke_2
+ ___88-[WBSSiteMetadataManager _sendResponse:toResponseHandlersForRequests:didReceiveNewData:]_block_invoke_3
+ ___91-[WBSWebExtensionsController _loadPermissionsFromStorageForWebExtension:completionHandler:]_block_invoke.304
+ ___97-[WBSSiteMetadataManager _registerSubrequest:isOneTimeRequest:forRequests:queue:responseHandler:]_block_invoke
+ ___98-[WBSSiteMetadataManager _registerRequest:isOneTimeRequest:queue:responseHandler:tokenSetUpBlock:]_block_invoke
+ ___WBS_LOG_CHANNEL_PREFIXSchemaDataLoading_block_invoke
+ ___block_descriptor_32_e31_B16?0"_WBSSiteMetadataToken"8l
+ ___block_descriptor_32_e33_v16?0"WBSSiteMetadataResponse"8l
+ ___block_descriptor_40_e31_v16?0"_WBSSiteMetadataToken"8l
+ ___block_descriptor_40_e66_"WBSWebExtensionMatchPattern"16?0"_WKWebExtensionMatchPattern"8l
+ ___block_descriptor_40_e8_32bs_e58_v32?0"NSObject<OS_dispatch_queue>"8"NSMutableSet"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e31_B16?0"_WBSSiteMetadataToken"8ls32l8
+ ___block_descriptor_40_e8_32s_e31_v16?0"_WBSSiteMetadataToken"8ls32l8
+ ___block_descriptor_40_ea8_32s_e18_B16?0"NSNumber"8ls32l8
+ ___block_descriptor_48_e8_32r_e43_"WBSTouchIconRequest"32?0"WBTab"8Q16^B24lr32l8
+ ___block_descriptor_48_e8_32s40s_e31_v16?0"_WBSSiteMetadataToken"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e56_"SFResultRankingFeedback"32?0"SFSearchResult"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e58_"SFSectionRankingFeedback"32?0"SFResultSection"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e34_v24?0"NSDictionary"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40w_e33_v16?0"WBSSiteMetadataResponse"8lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56s_e55_v32?0"WBSSiteMetadataRequest<WBSIconRequest>"8Q16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_ea8_32s40s48bs56r_e37_v32?08"WKFrameInfo"16"NSString"24ls32l8r56l8s40l8s48l8
+ ___block_descriptor_72_ea8_32s40s48s56s64s_e33_v16?0"WBSSiteMetadataResponse"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.150
+ ___block_literal_global.162
+ ___block_literal_global.180
+ ___block_literal_global.183
+ ___block_literal_global.186
+ ___block_literal_global.188
+ ___block_literal_global.190
+ ___block_literal_global.196
+ ___block_literal_global.197
+ ___block_literal_global.201
+ ___block_literal_global.203
+ ___block_literal_global.205
+ ___block_literal_global.207
+ ___block_literal_global.209
+ ___block_literal_global.211
+ ___block_literal_global.212
+ ___block_literal_global.214
+ ___block_literal_global.216
+ ___block_literal_global.218
+ ___block_literal_global.220
+ ___block_literal_global.222
+ ___block_literal_global.224
+ ___block_literal_global.243
+ ___block_literal_global.260
+ ___block_literal_global.289
+ ___block_literal_global.29
+ ___block_literal_global.302
+ ___block_literal_global.309
+ ___block_literal_global.315
+ ___block_literal_global.325
+ ___block_literal_global.330
+ ___block_literal_global.353
+ ___block_literal_global.359
+ ___block_literal_global.375
+ ___block_literal_global.395
+ ___block_literal_global.450
+ ___block_literal_global.465
+ ___block_literal_global.472
+ ___block_literal_global.475
+ ___block_literal_global.478
+ ___block_literal_global.498
+ ___block_literal_global.501
+ ___block_literal_global.511
+ ___block_literal_global.513
+ ___block_literal_global.534
+ ___block_literal_global.552
+ ___block_literal_global.57
+ ___block_literal_global.69
+ ___block_literal_global.72
+ ___block_literal_global.85
+ __unnamed_array_storage.1341
+ __unnamed_array_storage.1361
+ __unnamed_array_storage.146
+ __unnamed_array_storage.1476
+ __unnamed_array_storage.1805
+ __unnamed_array_storage.1833
+ __unnamed_array_storage.1845
+ __unnamed_array_storage.1846
+ __unnamed_array_storage.1878
+ __unnamed_array_storage.1884
+ __unnamed_array_storage.1911
+ __unnamed_array_storage.1917
+ __unnamed_array_storage.2139
+ __unnamed_array_storage.2151
+ __unnamed_array_storage.2197
+ __unnamed_array_storage.2209
+ __unnamed_array_storage.221
+ __unnamed_array_storage.2210
+ __unnamed_array_storage.249
+ __unnamed_array_storage.2752
+ __unnamed_array_storage.2755
+ __unnamed_array_storage.2761
+ __unnamed_array_storage.2764
+ __unnamed_array_storage.2767
+ __unnamed_array_storage.2768
+ __unnamed_array_storage.277
+ __unnamed_array_storage.2800
+ __unnamed_array_storage.2806
+ __unnamed_array_storage.2822
+ __unnamed_array_storage.2831
+ __unnamed_array_storage.2832
+ __unnamed_array_storage.286
+ __unnamed_array_storage.2870
+ __unnamed_array_storage.2882
+ __unnamed_array_storage.2885
+ __unnamed_array_storage.2888
+ __unnamed_array_storage.2889
+ __unnamed_array_storage.2915
+ __unnamed_array_storage.2930
+ __unnamed_array_storage.2936
+ __unnamed_array_storage.2942
+ __unnamed_array_storage.2943
+ __unnamed_array_storage.2996
+ __unnamed_array_storage.2999
+ __unnamed_array_storage.3002
+ __unnamed_array_storage.3003
+ __unnamed_array_storage.302
+ __unnamed_array_storage.3041
+ __unnamed_array_storage.3047
+ __unnamed_array_storage.3050
+ __unnamed_array_storage.3053
+ __unnamed_array_storage.3054
+ __unnamed_array_storage.3092
+ __unnamed_array_storage.3098
+ __unnamed_array_storage.31
+ __unnamed_array_storage.3101
+ __unnamed_array_storage.3104
+ __unnamed_array_storage.3105
+ __unnamed_array_storage.3128
+ __unnamed_array_storage.314
+ __unnamed_array_storage.325
+ __unnamed_array_storage.357
+ __unnamed_array_storage.363
+ __unnamed_array_storage.368
+ __unnamed_array_storage.382
+ __unnamed_array_storage.395
+ __unnamed_array_storage.410
+ __unnamed_array_storage.419
+ __unnamed_array_storage.424
+ __unnamed_array_storage.427
+ __unnamed_array_storage.430
+ __unnamed_array_storage.431
+ __unnamed_array_storage.443
+ __unnamed_array_storage.455
+ __unnamed_array_storage.456
+ __unnamed_array_storage.461
+ __unnamed_array_storage.508
+ _fetchDataFromWebView:completion:.schemaDataFetcherScriptSource
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _objc_msgSend$_backgroundContentIsServiceWorker
+ _objc_msgSend$_backgroundContentUsesModules
+ _objc_msgSend$_biomeWindowProperty:
+ _objc_msgSend$_enumerateTokens:usingSetUpBlock:dispatchBlock:
+ _objc_msgSend$_evaluateJavaScriptWithoutUserGesture:completionHandler:
+ _objc_msgSend$_highestRequestPriorityForRequests:
+ _objc_msgSend$_initWithID:kind:context:clientID:enableAppDistribution:
+ _objc_msgSend$_initWithManifestDictionary:
+ _objc_msgSend$_leadingGlyphInCTRunSafariIsRightToLeft:
+ _objc_msgSend$_registerInfo:forRequest:
+ _objc_msgSend$_registerRequest:isOneTimeRequest:queue:responseHandler:tokenSetUpBlock:
+ _objc_msgSend$_registerSubrequest:isOneTimeRequest:forRequests:queue:responseHandler:
+ _objc_msgSend$_registerToken:isCacheRequest:withProvider:
+ _objc_msgSend$_sendResponse:toResponseHandlersForRequests:didReceiveNewData:
+ _objc_msgSend$_stopWatchingUpdatesForRequests:
+ _objc_msgSend$_updatePriorityOfRequest:
+ _objc_msgSend$_windowProxyStream
+ _objc_msgSend$actionIconForSize:
+ _objc_msgSend$addCacheRequestToken:
+ _objc_msgSend$addRequestToken:
+ _objc_msgSend$alertControllerWithTitle:message:imageNamed:preferredStyle:
+ _objc_msgSend$applicationCategoryTypeForCategories:
+ _objc_msgSend$backgroundContentIsPersistent
+ _objc_msgSend$cacheData:forRequest:
+ _objc_msgSend$cacheData:forRequest:usingToken:
+ _objc_msgSend$cachedImageForFolderUUID:
+ _objc_msgSend$canProvideUpdatesForRequest:
+ _objc_msgSend$canSaveToDisk
+ _objc_msgSend$canStopWatchingRequestAfterRemovingToken:
+ _objc_msgSend$categories
+ _objc_msgSend$contentOfFolderDidUpdateWithUUID:
+ _objc_msgSend$currentDevice
+ _objc_msgSend$defaultLocale
+ _objc_msgSend$defaultSearchEngineMatchesExperiment
+ _objc_msgSend$deviceClass
+ _objc_msgSend$displayActionLabel
+ _objc_msgSend$displayDescription
+ _objc_msgSend$dynamicRulesIDs
+ _objc_msgSend$fetchDataFromWebView:completion:
+ _objc_msgSend$folderUUIDForRequest:
+ _objc_msgSend$iconForSize:
+ _objc_msgSend$initWithDataFormat:builtInListURL:downloadsDirectoryURL:resourceName:resourceVersion:updateDateDefaultsKey:updateInterval:snapshotClass:snapshotTransformerClass:
+ _objc_msgSend$initWithDomain:openedDomain:visited:property:accessedPropertyDirectly:
+ _objc_msgSend$initWithInput:triggerEvent:searchType:indexType:queryId:originatingApp:
+ _objc_msgSend$initWithRequest:isOneTimeRequest:queue:responseHandler:
+ _objc_msgSend$initWithResourceBaseURL:error:
+ _objc_msgSend$initWithSnapshotData:error:
+ _objc_msgSend$initWithWebKitMatchPattern:
+ _objc_msgSend$isBiomeStreamDonationAvailable
+ _objc_msgSend$pageContextDataFetcherDidFinishFetching:forURL:withError:
+ _objc_msgSend$parentRequests
+ _objc_msgSend$preloadRequest:withPriority:queue:responseHandler:
+ _objc_msgSend$preloadRequests:withPriority:queue:responseHandler:
+ _objc_msgSend$queue
+ _objc_msgSend$registerOneTimeRequest:priority:queue:responseHandler:
+ _objc_msgSend$registerRequest:priority:queue:responseHandler:
+ _objc_msgSend$removeParentRequest:
+ _objc_msgSend$removedTabGroupWithUUID:
+ _objc_msgSend$requestTokens
+ _objc_msgSend$requestsWithFolderUUIDsDidBecomeInvalid:
+ _objc_msgSend$schedule
+ _objc_msgSend$sendEvent:
+ _objc_msgSend$sessionRulesIDs
+ _objc_msgSend$setInspectable:
+ _objc_msgSend$setParentRequests:
+ _objc_msgSend$setSubrequests:
+ _objc_msgSend$siteMetadataProvider:didFinishCachingDataWithToken:
+ _objc_msgSend$siteMetadataProvider:didReceiveResponse:ofType:didReceiveNewData:forRequests:
+ _objc_msgSend$siteMetadataProvider:registerOneTimeSubrequest:forRequests:queue:responseHandler:
+ _objc_msgSend$siteMetadataProvider:registerSubrequest:forRequests:queue:responseHandler:
+ _objc_msgSend$subrequests
+ _objc_msgSend$subrequestsForRequest:maximumNumberOfSubrequests:
+ _objc_msgSend$supportsManifestVersion:
+ _objc_msgSend$templateIconURL
+ _objc_msgSend$timerWithInterval:repeats:queue:handler:
+ _objc_msgSend$trialABGroupIdentifier
+ _objc_msgSend$userAssignedName
+ _schemaDataExtractorSource
+ _schemaDataExtractorSourceLength
- +[WBSBookmarkFolderTouchIconProviderInfo new]
- +[WBSParsecActionButton schema]
- +[WBSParsecSearchResult typeForSFSearchResult:isOneLine:]
- +[WBSParsecSearchSportsAttributionExtraCompletionItem schema]
- -[NSString(SafariSharedUIExtras) safari_stringHasLeadingEmoji:]
- -[WBSBookmarkFolderTouchIconProvider _responseHandlerForRequest:thumbnailIndex:]
- -[WBSBookmarkFolderTouchIconProvider bookmarkUUIDForRequest:]
- -[WBSBookmarkFolderTouchIconProvider displayableFolderContentsForRequest:]
- -[WBSBookmarkFolderTouchIconProvider removeInfoForFolderWithUUID:]
- -[WBSBookmarkFolderTouchIconProvider removeInfoForFoldersWithUUIDs:]
- -[WBSBookmarkFolderTouchIconProvider touchIconRequestForBookmark:inFolderWithRequest:]
- -[WBSBookmarkFolderTouchIconProviderInfo .cxx_destruct]
- -[WBSBookmarkFolderTouchIconProviderInfo backgroundColors]
- -[WBSBookmarkFolderTouchIconProviderInfo initWithThumbnailImages:backgroundColors:touchIcon:]
- -[WBSBookmarkFolderTouchIconProviderInfo init]
- -[WBSBookmarkFolderTouchIconProviderInfo thumbnailImages]
- -[WBSBookmarkFolderTouchIconProviderInfo touchIcon]
- -[WBSBookmarkFolderTouchIconProviderRequestInfo .cxx_destruct]
- -[WBSBookmarkFolderTouchIconProviderRequestInfo backgroundColors]
- -[WBSBookmarkFolderTouchIconProviderRequestInfo hasScheduledCoalescedUpdate]
- -[WBSBookmarkFolderTouchIconProviderRequestInfo init]
- -[WBSBookmarkFolderTouchIconProviderRequestInfo setBackgroundColor:atIndex:]
- -[WBSBookmarkFolderTouchIconProviderRequestInfo setHasScheduledCoalescedUpdate:]
- -[WBSBookmarkFolderTouchIconProviderRequestInfo setSubrequestTokens:]
- -[WBSBookmarkFolderTouchIconProviderRequestInfo setThumbnailImage:atIndex:]
- -[WBSBookmarkFolderTouchIconProviderRequestInfo subrequestTokens]
- -[WBSBookmarkFolderTouchIconProviderRequestInfo thumbnailImages]
- -[WBSParsecActionButton .cxx_destruct]
- -[WBSParsecActionButton baseIcon]
- -[WBSParsecActionButton completion]
- -[WBSParsecActionButton icon]
- -[WBSParsecActionButton initWithDictionary:mediaKind:]
- -[WBSParsecActionButton isForAppleMusicResult]
- -[WBSParsecActionButton isForStreamingResult]
- -[WBSParsecActionButton isOverlay]
- -[WBSParsecActionButton itunesCompletion]
- -[WBSParsecActionButton itunesContentIdentifiers]
- -[WBSParsecActionButton itunesLabel]
- -[WBSParsecActionButton labelAlignment]
- -[WBSParsecActionButton label]
- -[WBSParsecActionButton mediaKind]
- -[WBSParsecActionButton offerType]
- -[WBSParsecActionButton punchoutAppBundleIdentifier]
- -[WBSParsecActionButton punchoutAppName]
- -[WBSParsecActionButton punchoutURL]
- -[WBSParsecActionButton type]
- -[WBSParsecLegacySearchResult actionButton]
- -[WBSParsecSearchGenericResult actionButton]
- -[WBSParsecSearchResult actionButton]
- -[WBSParsecSearchResult extraCompletionItem]
- -[WBSParsecSearchSportsAttributionExtraCompletionItem .cxx_destruct]
- -[WBSParsecSearchSportsAttributionExtraCompletionItem engagementDestination]
- -[WBSParsecSearchSportsAttributionExtraCompletionItem imageRepresentation]
- -[WBSParsecSearchSportsAttributionExtraCompletionItem initWithDictionary:]
- -[WBSParsecSearchSportsAttributionExtraCompletionItem label]
- -[WBSParsecSearchSportsAttributionExtraCompletionItem parsecDomainIdentifier]
- -[WBSParsecSearchSportsAttributionExtraCompletionItem parsecQueryID]
- -[WBSParsecSearchSportsAttributionExtraCompletionItem setParsecQueryID:]
- -[WBSParsecSearchSportsAttributionExtraCompletionItem sfSearchResultValue]
- -[WBSParsecSearchSportsAttributionExtraCompletionItem url]
- -[WBSPhishingAssetController didDownloadPlistForRemotePlistController:]
- -[WBSPhishingConfiguration initWithPlistData:error:]
- -[WBSPhishingConfiguration plistDataWithFormat:]
- -[WBSSiteMetadataManager _highestRequestPriorityForRequest:]
- -[WBSSiteMetadataManager _registerToken:withProvider:]
- -[WBSSiteMetadataManager _sendResponse:toResponseHandlersForRequest:didReceiveNewData:]
- -[WBSSiteMetadataManager siteMetadataProvider:registerOneTimeRequest:priority:responseHandler:]
- -[WBSSiteMetadataManager siteMetadataProvider:registerRequest:priority:responseHandler:]
- -[WBSTabGroupTouchIconProvider .cxx_destruct]
- -[WBSTabGroupTouchIconProvider _cancelRequestsAndClearCacheForTabGroup:]
- -[WBSTabGroupTouchIconProvider _cancelRequestsAndClearCacheForTabGroup:metadata:]
- -[WBSTabGroupTouchIconProvider bookmarkUUIDForRequest:]
- -[WBSTabGroupTouchIconProvider displayableFolderContentsForRequest:]
- -[WBSTabGroupTouchIconProvider init]
- -[WBSTabGroupTouchIconProvider touchIconRequestForBookmark:inFolderWithRequest:]
- -[WBSTabGroupTouchIconProvider updateIconForTabGroupIfNeeded:tabProvider:]
- -[WBSTemplateIconCache addTemplateIconAtURL:withThemeColor:forHost:toDisk:]
- -[WBSTemplateIconRequest initWithURL:extraInfo:]
- -[WBSTemplateIconRequest initWithURL:title:monogramConfiguration:overrideForegroundColor:saveToDisk:]
- -[WBSTemplateIconRequest saveToDisk]
- -[WBSWebExtensionCommand description]
- -[WBSWebExtensionData _populateDisplayStringsIfNeeded]
- -[WBSWebExtensionData _populateDisplayStringsIfNeeded].cold.1
- -[WBSWebExtensionData _populateDisplayStringsIfNeeded].cold.2
- -[WBSWebExtensionData currentAccessibleOrigins]
- -[WBSWebExtensionData extensionIconWithBaseURI:idealPointSize:validateAndReadResourceHandler:]
- -[WBSWebExtensionData extensionIconWithBaseURI:idealPointSize:validateAndReadResourceHandler:].cold.1
- -[WBSWebExtensionData extensionIconWithBaseURI:idealPointSize:validateAndReadResourceHandler:].cold.2
- -[WBSWebExtensionData manifestDictionary].cold.1
- -[WBSWebExtensionData numberOfDynamicRules]
- -[WBSWebExtensionData numberOfSessionRules]
- -[WBSWebExtensionData setNumberOfDynamicRules:]
- -[WBSWebExtensionData setNumberOfSessionRules:]
- -[WBSWebExtensionData toolbarImageWithBaseURI:idealPointSize:validateAndReadResourceHandler:]
- -[WBSWebExtensionData toolbarImageWithBaseURI:idealPointSize:validateAndReadResourceHandler:].cold.1
- -[WBSWebExtensionMatchPattern _initWithWebKitMatchPattern:]
- -[WBSWebExtensionsController _deviceName]
- -[_WBSSiteMetadataToken initWithOneTimeRequest:priority:responseHandler:]
- -[_WBSSiteMetadataToken initWithRequest:priority:responseHandler:]
- -[_WBSTabGroupIconMetadata .cxx_destruct]
- -[_WBSTabGroupIconMetadata _arrayOfThumbnailURLsShownInFolderIconFromTabsArray:]
- -[_WBSTabGroupIconMetadata _configuration]
- -[_WBSTabGroupIconMetadata hasSameIconAsTabGroup:]
- -[_WBSTabGroupIconMetadata iconImage]
- -[_WBSTabGroupIconMetadata initWithTabGroup:token:]
- -[_WBSTabGroupIconMetadata setIconImage:]
- -[_WBSTabGroupIconMetadata setToken:]
- -[_WBSTabGroupIconMetadata token]
- GCC_except_table166
- GCC_except_table209
- GCC_except_table218
- GCC_except_table219
- GCC_except_table247
- GCC_except_table339
- GCC_except_table385
- GCC_except_table386
- GCC_except_table394
- GCC_except_table396
- GCC_except_table400
- GCC_except_table406
- GCC_except_table407
- GCC_except_table414
- _MGGetSInt32Answer
- _NSDefaultRunLoopMode
- _OBJC_CLASS_$_WBSBookmarkFolderTouchIconProviderInfo
- _OBJC_CLASS_$_WBSBookmarkFolderTouchIconProviderRequestInfo
- _OBJC_CLASS_$_WBSParsecActionButton
- _OBJC_CLASS_$_WBSParsecSearchSportsAttributionExtraCompletionItem
- _OBJC_CLASS_$_WBSRemotePlistController
- _OBJC_CLASS_$__WBSTabGroupIconMetadata
- _OBJC_IVAR_$_WBSBookmarkFolderTouchIconProviderInfo._backgroundColors
- _OBJC_IVAR_$_WBSBookmarkFolderTouchIconProviderInfo._thumbnailImages
- _OBJC_IVAR_$_WBSBookmarkFolderTouchIconProviderInfo._touchIcon
- _OBJC_IVAR_$_WBSBookmarkFolderTouchIconProviderRequestInfo._backgroundColors
- _OBJC_IVAR_$_WBSBookmarkFolderTouchIconProviderRequestInfo._hasScheduledCoalescedUpdate
- _OBJC_IVAR_$_WBSBookmarkFolderTouchIconProviderRequestInfo._subrequestTokens
- _OBJC_IVAR_$_WBSBookmarkFolderTouchIconProviderRequestInfo._thumbnailImages
- _OBJC_IVAR_$_WBSParsecActionButton._baseIcon
- _OBJC_IVAR_$_WBSParsecActionButton._completion
- _OBJC_IVAR_$_WBSParsecActionButton._forStreamingResult
- _OBJC_IVAR_$_WBSParsecActionButton._icon
- _OBJC_IVAR_$_WBSParsecActionButton._itunesCompletion
- _OBJC_IVAR_$_WBSParsecActionButton._itunesContentIdentifiers
- _OBJC_IVAR_$_WBSParsecActionButton._itunesLabel
- _OBJC_IVAR_$_WBSParsecActionButton._label
- _OBJC_IVAR_$_WBSParsecActionButton._labelAlignment
- _OBJC_IVAR_$_WBSParsecActionButton._mediaKind
- _OBJC_IVAR_$_WBSParsecActionButton._offerType
- _OBJC_IVAR_$_WBSParsecActionButton._overlay
- _OBJC_IVAR_$_WBSParsecActionButton._punchoutAppBundleIdentifier
- _OBJC_IVAR_$_WBSParsecActionButton._punchoutAppName
- _OBJC_IVAR_$_WBSParsecActionButton._punchoutURL
- _OBJC_IVAR_$_WBSParsecActionButton._type
- _OBJC_IVAR_$_WBSParsecLegacySearchResult._actionButton
- _OBJC_IVAR_$_WBSParsecSearchGenericResult._actionButton
- _OBJC_IVAR_$_WBSParsecSearchSportsAttributionExtraCompletionItem._imageRepresentation
- _OBJC_IVAR_$_WBSParsecSearchSportsAttributionExtraCompletionItem._label
- _OBJC_IVAR_$_WBSParsecSearchSportsAttributionExtraCompletionItem._parsecQueryID
- _OBJC_IVAR_$_WBSParsecSearchSportsAttributionExtraCompletionItem._url
- _OBJC_IVAR_$_WBSParsecSearchSportsAttributionExtraCompletionItem.sfSearchResultValue
- _OBJC_IVAR_$_WBSTabGroupTouchIconProvider._tabGroupIconMetadataCache
- _OBJC_IVAR_$_WBSWebExtensionData._displayDescription
- _OBJC_IVAR_$_WBSWebExtensionData._displayName
- _OBJC_IVAR_$_WBSWebExtensionData._displayShortName
- _OBJC_IVAR_$_WBSWebExtensionData._displayVersion
- _OBJC_IVAR_$_WBSWebExtensionData._hasCachedIcon
- _OBJC_IVAR_$_WBSWebExtensionData._hasCachedPreferencesIcon
- _OBJC_IVAR_$_WBSWebExtensionData._hasCachedToolbarImage
- _OBJC_IVAR_$_WBSWebExtensionData._icon
- _OBJC_IVAR_$_WBSWebExtensionData._numberOfDynamicRules
- _OBJC_IVAR_$_WBSWebExtensionData._numberOfSessionRules
- _OBJC_IVAR_$_WBSWebExtensionData._parsedManifestDisplayStrings
- _OBJC_IVAR_$_WBSWebExtensionData._preferencesIcon
- _OBJC_IVAR_$_WBSWebExtensionData._toolbarImage
- _OBJC_IVAR_$_WBSWebExtensionData._version
- _OBJC_IVAR_$__WBSTabGroupIconMetadata._iconImage
- _OBJC_IVAR_$__WBSTabGroupIconMetadata._tabUrlArray
- _OBJC_IVAR_$__WBSTabGroupIconMetadata._token
- _OBJC_IVAR_$__WBSTabGroupIconMetadata._uuid
- _OBJC_METACLASS_$_WBSBookmarkFolderTouchIconProviderInfo
- _OBJC_METACLASS_$_WBSBookmarkFolderTouchIconProviderRequestInfo
- _OBJC_METACLASS_$_WBSParsecActionButton
- _OBJC_METACLASS_$_WBSParsecSearchSportsAttributionExtraCompletionItem
- _OBJC_METACLASS_$__WBSTabGroupIconMetadata
- _WBSParsecEngagementActionArea
- _WBSParsecEngagementActionAreaCard
- _WBSParsecEngagementActionAreaResult
- _WBSParsecEngagementActionCardType
- _WBSParsecEngagementActionDestination
- _WBSParsecEngagementActionTarget
- _WBSParsecEngagementActionTargetPlayButton
- _WBSParsecEngagementActionType
- _WBSParsecEngagementActionTypeEnterKey
- _WBSParsecITunesMediaKindAlbum
- _WBSParsecITunesMediaKindArtist
- _WBSParsecITunesMediaKindPlaylist
- _WBSParsecITunesMediaKindSong
- _WBSSearchProviderBaiduTrackingCodeIPodTouchKey
- _WBSSearchProviderDefinitionSearchURLTemplateIPodTouchKey
- __OBJC_$_CATEGORY_NSString_$_SafariSharedUIExtras
- __OBJC_$_CLASS_METHODS_WBSBookmarkFolderTouchIconProviderInfo
- __OBJC_$_CLASS_METHODS_WBSParsecActionButton
- __OBJC_$_CLASS_METHODS_WBSParsecSearchSportsAttributionExtraCompletionItem
- __OBJC_$_INSTANCE_METHODS_NSString(SafariSharedUIExtras|WBSFaviconProviderNSStringExtras)
- __OBJC_$_INSTANCE_METHODS_WBSBookmarkFolderTouchIconProviderInfo
- __OBJC_$_INSTANCE_METHODS_WBSBookmarkFolderTouchIconProviderRequestInfo
- __OBJC_$_INSTANCE_METHODS_WBSParsecActionButton
- __OBJC_$_INSTANCE_METHODS_WBSParsecSearchSportsAttributionExtraCompletionItem
- __OBJC_$_INSTANCE_METHODS__WBSTabGroupIconMetadata
- __OBJC_$_INSTANCE_VARIABLES_WBSBookmarkFolderTouchIconProviderInfo
- __OBJC_$_INSTANCE_VARIABLES_WBSBookmarkFolderTouchIconProviderRequestInfo
- __OBJC_$_INSTANCE_VARIABLES_WBSParsecActionButton
- __OBJC_$_INSTANCE_VARIABLES_WBSParsecSearchSportsAttributionExtraCompletionItem
- __OBJC_$_INSTANCE_VARIABLES_WBSTabGroupTouchIconProvider
- __OBJC_$_INSTANCE_VARIABLES__WBSTabGroupIconMetadata
- __OBJC_$_PROP_LIST_WBSBookmarkFolderTouchIconProviderInfo
- __OBJC_$_PROP_LIST_WBSBookmarkFolderTouchIconProviderRequestInfo
- __OBJC_$_PROP_LIST_WBSParsecActionButton
- __OBJC_$_PROP_LIST_WBSParsecSearchGenericResult.81
- __OBJC_$_PROP_LIST_WBSParsecSearchSimpleResult.83
- __OBJC_$_PROP_LIST_WBSParsecSearchSportsAttributionExtraCompletionItem
- __OBJC_$_PROP_LIST_WBSSearchProvider.276
- __OBJC_$_PROP_LIST__WBSTabGroupIconMetadata
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WBSRemotePlistControllerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_WBSRemotePlistSnapshot
- __OBJC_$_PROTOCOL_METHOD_TYPES_WBSRemotePlistControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_WBSRemotePlistSnapshot
- __OBJC_$_PROTOCOL_REFS_WBSRemotePlistControllerDelegate
- __OBJC_$_PROTOCOL_REFS_WBSRemotePlistSnapshot
- __OBJC_CLASS_PROTOCOLS_$_WBSParsecSearchSportsAttributionExtraCompletionItem
- __OBJC_CLASS_RO_$_WBSBookmarkFolderTouchIconProviderInfo
- __OBJC_CLASS_RO_$_WBSBookmarkFolderTouchIconProviderRequestInfo
- __OBJC_CLASS_RO_$_WBSParsecActionButton
- __OBJC_CLASS_RO_$_WBSParsecSearchSportsAttributionExtraCompletionItem
- __OBJC_CLASS_RO_$__WBSTabGroupIconMetadata
- __OBJC_LABEL_PROTOCOL_$_WBSRemotePlistControllerDelegate
- __OBJC_LABEL_PROTOCOL_$_WBSRemotePlistSnapshot
- __OBJC_METACLASS_RO_$_WBSBookmarkFolderTouchIconProviderInfo
- __OBJC_METACLASS_RO_$_WBSBookmarkFolderTouchIconProviderRequestInfo
- __OBJC_METACLASS_RO_$_WBSParsecActionButton
- __OBJC_METACLASS_RO_$_WBSParsecSearchSportsAttributionExtraCompletionItem
- __OBJC_METACLASS_RO_$__WBSTabGroupIconMetadata
- __OBJC_PROTOCOL_$_WBSRemotePlistControllerDelegate
- __OBJC_PROTOCOL_$_WBSRemotePlistSnapshot
- __WBSSearchProviderShortNameOrderOnMac.definitionOrder.212
- __WBSSearchProviderShortNameOrderOnMac.definitionOrder.216
- __WBSSearchProviderShortNameOrderOnMac.onceToken.213
- __WBSSearchProviderShortNameOrderOnMac.onceToken.217
- ___102-[WBSSiteMetadataManager siteMetadataProvider:didReceiveResponse:ofType:didReceiveNewData:forRequest:]_block_invoke
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.469
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.469.cold.1
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.470
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.470.cold.1
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.471
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.472
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke_2.476
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke_2.476.cold.1
- ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke.76
- ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke.98
- ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke_2.78
- ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke_3.80
- ___118-[WBSWebExtensionsController setKeyedData:inStorageOfType:forExtensionWithUniqueIdentifier:webView:completionHandler:]_block_invoke.342
- ___125+[WBSWebExtensionUtilities validateContentsOfDictionary:requiredKeys:optionalKeys:keyToExpectedValueType:outExceptionString:]_block_invoke.cold.1
- ___50-[WBSWebExtensionData _loadBackgroundPageWithURL:]_block_invoke.567
- ___50-[_WBSTabGroupIconMetadata hasSameIconAsTabGroup:]_block_invoke
- ___54-[WBSWebExtensionData _populateWebAccessibleResources]_block_invoke.350
- ___54-[WBSWebExtensionData _populateWebAccessibleResources]_block_invoke.350.cold.1
- ___58-[WBSSiteMetadataManager _internalCancelRequestWithToken:]_block_invoke.20
- ___59-[WBSTouchIconFetchOperation _downloadPendingTouchIconURLs]_block_invoke.69
- ___65-[WBSCloudExtensionStateManager _deleteCurrentDeviceFromCloudKit]_block_invoke.54
- ___65-[WBSCloudExtensionStateManager _deleteCurrentDeviceFromCloudKit]_block_invoke.54.cold.1
- ___67-[WBSSiteMetadataManager registerRequest:priority:responseHandler:]_block_invoke
- ___68-[WBSTabGroupTouchIconProvider displayableFolderContentsForRequest:]_block_invoke
- ___71-[WBSPhishingAssetController didDownloadPlistForRemotePlistController:]_block_invoke
- ___71-[WBSPhishingAssetController didDownloadPlistForRemotePlistController:]_block_invoke_2
- ___71-[WBSPhishingAssetController mobileAssetController:didBecomeAvailable:]_block_invoke.241
- ___71-[WBSSiteMetadataManager preloadRequests:withPriority:responseHandler:]_block_invoke
- ___72-[WBSCloudExtensionStateManager _ensureCurrentDeviceIsSavedPeriodically]_block_invoke.69
- ___74-[WBSSiteMetadataManager registerOneTimeRequest:priority:responseHandler:]_block_invoke
- ___74-[WBSTabGroupTouchIconProvider updateIconForTabGroupIfNeeded:tabProvider:]_block_invoke
- ___74-[WBSTouchIconFetchOperation didFetchTouchIconURLs:andFaviconURLs:forURL:]_block_invoke.77
- ___75-[WBSTemplateIconCache addTemplateIconAtURL:withThemeColor:forHost:toDisk:]_block_invoke
- ___75-[WBSTemplateIconCache addTemplateIconAtURL:withThemeColor:forHost:toDisk:]_block_invoke_2
- ___77-[WBSWebExtensionsController postMessage:fromPortWithID:fromExtensionWithID:]_block_invoke.297
- ___78-[WBSTouchIconFetchOperation _downloadFirstValidImageWithURLs:failureHandler:]_block_invoke.65
- ___79-[WBSWebExtensionsController _deleteStorageForExtensionWithComposedIdentifier:]_block_invoke.170
- ___80-[WBSBookmarkFolderTouchIconProvider _responseHandlerForRequest:thumbnailIndex:]_block_invoke
- ___80-[WBSBookmarkFolderTouchIconProvider _responseHandlerForRequest:thumbnailIndex:]_block_invoke_2
- ___84-[WBSWebExtensionData loadRegisteredContentScriptsFromStorageWithCompletionHandler:]_block_invoke.485
- ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke.417
- ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke_2.418
- ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke_2.418.cold.1
- ___87-[WBSSiteMetadataManager _sendResponse:toResponseHandlersForRequest:didReceiveNewData:]_block_invoke
- ___87-[WBSSiteMetadataManager _sendResponse:toResponseHandlersForRequest:didReceiveNewData:]_block_invoke_2
- ___88-[WBSCloudExtensionStateManager _pruneInactiveDevicesFromCloudKitWithCompletionHandler:]_block_invoke.76
- ___88-[WBSCloudExtensionStateManager _pruneInactiveDevicesFromCloudKitWithCompletionHandler:]_block_invoke.76.cold.1
- ___91-[WBSWebExtensionsController _loadPermissionsFromStorageForWebExtension:completionHandler:]_block_invoke.301
- ___block_descriptor_48_e8_32s40r_e22_v32?0"NSURL"8Q16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e52_"SFResultRankingFeedback"24?0"SFSearchResult"8Q16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e54_"SFSectionRankingFeedback"24?0"SFResultSection"8Q16ls32l8s40l8
- ___block_descriptor_48_e8_32s_e22_v32?0"WBTab"8Q16^B24ls32l8
- ___block_descriptor_56_e8_32s40r48w_e33_v16?0"WBSSiteMetadataResponse"8lw48l8r40l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e15_v32?08Q16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSTimer"8lw48l8s32l8s40l8
- ___block_descriptor_56_ea8_32s40bs_e18_v16?0"NSString"8ls40l8s32l8
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48w_e33_v16?0"WBSSiteMetadataResponse"8lw48l8s32l8s40l8
- ___block_descriptor_64_ea8_32s40s48bs56r_e24_v24?08"WKFrameInfo"16ls32l8r56l8s40l8s48l8
- ___block_descriptor_65_ea8_32s40s48s56s_e33_v16?0"WBSSiteMetadataResponse"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_65_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.152
- ___block_literal_global.161
- ___block_literal_global.179
- ___block_literal_global.182
- ___block_literal_global.184
- ___block_literal_global.185
- ___block_literal_global.187
- ___block_literal_global.189
- ___block_literal_global.199
- ___block_literal_global.202
- ___block_literal_global.204
- ___block_literal_global.206
- ___block_literal_global.208
- ___block_literal_global.210
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.219
- ___block_literal_global.221
- ___block_literal_global.223
- ___block_literal_global.241
- ___block_literal_global.257
- ___block_literal_global.293
- ___block_literal_global.299
- ___block_literal_global.306
- ___block_literal_global.312
- ___block_literal_global.322
- ___block_literal_global.327
- ___block_literal_global.352
- ___block_literal_global.355
- ___block_literal_global.378
- ___block_literal_global.398
- ___block_literal_global.449
- ___block_literal_global.456
- ___block_literal_global.463
- ___block_literal_global.484
- ___block_literal_global.495
- ___block_literal_global.506
- ___block_literal_global.509
- ___block_literal_global.519
- ___block_literal_global.521
- ___block_literal_global.542
- ___block_literal_global.56
- ___block_literal_global.560
- ___block_literal_global.68
- ___block_literal_global.78
- __unnamed_array_storage.130
- __unnamed_array_storage.1359
- __unnamed_array_storage.1379
- __unnamed_array_storage.1494
- __unnamed_array_storage.1823
- __unnamed_array_storage.1851
- __unnamed_array_storage.1863
- __unnamed_array_storage.1864
- __unnamed_array_storage.1896
- __unnamed_array_storage.1902
- __unnamed_array_storage.1929
- __unnamed_array_storage.1935
- __unnamed_array_storage.2157
- __unnamed_array_storage.2169
- __unnamed_array_storage.2215
- __unnamed_array_storage.2227
- __unnamed_array_storage.2228
- __unnamed_array_storage.233
- __unnamed_array_storage.26
- __unnamed_array_storage.261
- __unnamed_array_storage.2770
- __unnamed_array_storage.2773
- __unnamed_array_storage.2779
- __unnamed_array_storage.2782
- __unnamed_array_storage.2785
- __unnamed_array_storage.2786
- __unnamed_array_storage.2818
- __unnamed_array_storage.2824
- __unnamed_array_storage.2840
- __unnamed_array_storage.2849
- __unnamed_array_storage.2850
- __unnamed_array_storage.289
- __unnamed_array_storage.2891
- __unnamed_array_storage.2903
- __unnamed_array_storage.2906
- __unnamed_array_storage.2909
- __unnamed_array_storage.2910
- __unnamed_array_storage.2954
- __unnamed_array_storage.2960
- __unnamed_array_storage.2963
- __unnamed_array_storage.2967
- __unnamed_array_storage.298
- __unnamed_array_storage.3020
- __unnamed_array_storage.3023
- __unnamed_array_storage.3029
- __unnamed_array_storage.3030
- __unnamed_array_storage.3056
- __unnamed_array_storage.306
- __unnamed_array_storage.3071
- __unnamed_array_storage.3080
- __unnamed_array_storage.3083
- __unnamed_array_storage.3084
- __unnamed_array_storage.3110
- __unnamed_array_storage.3125
- __unnamed_array_storage.3131
- __unnamed_array_storage.3134
- __unnamed_array_storage.3137
- __unnamed_array_storage.3138
- __unnamed_array_storage.3164
- __unnamed_array_storage.337
- __unnamed_array_storage.338
- __unnamed_array_storage.364
- __unnamed_array_storage.369
- __unnamed_array_storage.406
- __unnamed_array_storage.407
- __unnamed_array_storage.409
- __unnamed_array_storage.422
- __unnamed_array_storage.423
- __unnamed_array_storage.426
- __unnamed_array_storage.429
- __unnamed_array_storage.432
- __unnamed_array_storage.439
- __unnamed_array_storage.452
- __unnamed_array_storage.458
- __unnamed_array_storage.470
- __unnamed_array_storage.471
- __unnamed_array_storage.499
- _defaultConfiguration
- _objc_msgSend$_arrayOfThumbnailURLsShownInFolderIconFromTabsArray:
- _objc_msgSend$_cancelRequestsAndClearCacheForTabGroup:
- _objc_msgSend$_cancelRequestsAndClearCacheForTabGroup:metadata:
- _objc_msgSend$_deviceName
- _objc_msgSend$_highestRequestPriorityForRequest:
- _objc_msgSend$_initWithWebKitMatchPattern:
- _objc_msgSend$_populateDisplayStringsIfNeeded
- _objc_msgSend$_registerToken:withProvider:
- _objc_msgSend$_responseHandlerForRequest:thumbnailIndex:
- _objc_msgSend$_sendResponse:toResponseHandlersForRequest:didReceiveNewData:
- _objc_msgSend$_setProcessDisplayName:
- _objc_msgSend$actionButton
- _objc_msgSend$bookmarkUUIDForRequest:
- _objc_msgSend$currentAccessibleOrigins
- _objc_msgSend$dataWithContentsOfFile:
- _objc_msgSend$displayableFolderContentsForRequest:
- _objc_msgSend$extensionIconWithBaseURI:idealPointSize:validateAndReadResourceHandler:
- _objc_msgSend$extraCompletionItem
- _objc_msgSend$hasSameIconAsTabGroup:
- _objc_msgSend$iconImage
- _objc_msgSend$initWithBuiltInListURL:downloadsDirectoryURL:resourceName:resourceVersion:updateDateDefaultsKey:updateInterval:snapshotClass:snapshotTransformerClass:
- _objc_msgSend$initWithDictionary:mediaKind:
- _objc_msgSend$initWithInput:triggerEvent:indexType:queryId:
- _objc_msgSend$initWithOneTimeRequest:priority:responseHandler:
- _objc_msgSend$initWithPlistData:error:
- _objc_msgSend$initWithRequest:priority:responseHandler:
- _objc_msgSend$initWithTabGroup:tabProvider:
- _objc_msgSend$initWithTabGroup:token:
- _objc_msgSend$isNamed
- _objc_msgSend$numberOfDynamicRules
- _objc_msgSend$numberOfSessionRules
- _objc_msgSend$processDisplayName
- _objc_msgSend$providerDelegate
- _objc_msgSend$removeInfoForFolderWithUUID:
- _objc_msgSend$setIconImage:
- _objc_msgSend$setNumberOfDynamicRules:
- _objc_msgSend$setNumberOfSessionRules:
- _objc_msgSend$siteMetadataProvider:registerOneTimeRequest:priority:responseHandler:
- _objc_msgSend$siteMetadataProvider:registerRequest:priority:responseHandler:
- _objc_msgSend$token
- _objc_msgSend$toolbarImageWithBaseURI:idealPointSize:validateAndReadResourceHandler:
- _objc_msgSend$touchIconRequestForBookmark:inFolderWithRequest:
- _objc_msgSend$typeForSFSearchResult:isOneLine:
- _objc_msgSend$updateIconForTabGroupIfNeeded:tabProvider:
- _objc_setProperty_atomic_copy
CStrings:
+ "\x01\x11\x18"
+ "\x02\x12"
+ "\x02\x19&"
+ "\r"
+ "\x0f\x1c\x14\x11\x11\x12\x16\x11\x12\x13\x11\x11\x1b"
+ "\x11\x12\x12"
+ "3"
+ "8618.1.15.10.11"
+ "<%@ %p (composed identifier \"%@\") %@>"
+ "@\"<WBSPageContextDataFetcherDelegate>\""
+ "@\"NSData\"16@0:8"
+ "@\"SFResultRankingFeedback\"32@?0@\"SFSearchResult\"8Q16^B24"
+ "@\"SFSectionRankingFeedback\"32@?0@\"SFResultSection\"8Q16^B24"
+ "@\"WBSRemotelyUpdatableDataController\""
+ "@\"WBSTouchIconRequest\"32@?0@\"WBTab\"8Q16^B24"
+ "@\"WBSWebExtensionMatchPattern\"16@?0@\"_WKWebExtensionMatchPattern\"8"
+ "@\"_WKWebExtension\""
+ "@32@0:8@16Q24"
+ "@44@0:8@16B24@28@?36"
+ "@52@0:8@16B24@28@36@?44"
+ "@52@0:8@16B24@28@?36@?44"
+ "@56@0:8@\"<WBSSiteMetadataProvider>\"16@\"WBSSiteMetadataRequest\"24@\"NSSet\"32@\"NSObject<OS_dispatch_queue>\"40@?<v@?@\"WBSSiteMetadataResponse\">48"
+ "B16@?0@\"NSNumber\"8"
+ "B16@?0@\"_WBSSiteMetadataToken\"8"
+ "B24@0:8@\"WBSRemotelyUpdatableDataController\"16"
+ "B40@0:8@16@\"WBSSiteMetadataRequest\"24@32"
+ "DebugDidTapAtLeastTwoReadingListArticles"
+ "Failed to execute script. Extension does not have access to this frame."
+ "Failed to extract Microdata from webpage: %{public}@"
+ "Fetching schema data failed with error: %{public}@"
+ "Fetching schema data returned nil result"
+ "Fetching schema data returned unexpected result: %{private}@"
+ "Found unrecognized key (%{private}@), not specified in required or optional keys."
+ "SchemaDataLoading"
+ "T@\"<WBSPageContextDataFetcherDelegate>\",W,N,V_delegate"
+ "T@\"<_CompletionListRankingObserverFeedbackGeneratorDelegate>\",?,W,N"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSArray\",C,N,V_subrequests"
+ "T@\"NSDictionary\",?,C,N"
+ "T@\"NSDictionary\",?,R,N"
+ "T@\"NSDictionary\",R,C,N,V_filteredSchemaData"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSSet\",?,R,N"
+ "T@\"NSSet\",C,N"
+ "T@\"NSSet\",C,N,V_dynamicRulesIDs"
+ "T@\"NSSet\",C,N,V_sessionRulesIDs"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",?,R,N"
+ "T@\"NSURL\",?,R,N"
+ "T@\"NSURL\",R,C,N,V_templateIconURL"
+ "T@\"UIColor\",?,R,N"
+ "T@\"UIImage\",?,R,N"
+ "T@\"WBSDispatchSourceTimer\",&,N,V_delayTimer"
+ "T@\"WBSQuerySuggestion\",?,&,N"
+ "T@\"_WKWebExtension\",R,N,V_webKitExtension"
+ "TB,?,N"
+ "TB,?,R,N"
+ "TB,?,R,N,GisGenerated"
+ "TB,R,N,V_canSaveToDisk"
+ "Tq,?,R,N"
+ "Unable to create WebKit extension with identifier %{private}@ with error: %{public}@"
+ "WBSPageContextDataFetcher"
+ "WBSRemotelyUpdatableDataControllerDelegate"
+ "WBSRemotelyUpdatableDataSnapshot"
+ "WBSSchemaDataExtractor"
+ "WBSTemplateIconCacheRecord"
+ "WebAppCategories"
+ "_WBSBookmarkFolderTouchIconProviderInfo"
+ "_WBSBookmarkFolderTouchIconProviderRequestInfo"
+ "_WBSWKApplicationManifestExtrasUtilities"
+ "_backgroundContentIsServiceWorker"
+ "_backgroundContentUsesModules"
+ "_biomeWindowProperty:"
+ "_bookmarkFolderIdentifiersToRequestSets"
+ "_cacheRequestTokens"
+ "_canSaveToDisk"
+ "_dynamicRulesIDs"
+ "_enumerateTokens:usingSetUpBlock:dispatchBlock:"
+ "_evaluateJavaScriptWithoutUserGesture:completionHandler:"
+ "_filteredSchemaData"
+ "_highestRequestPriorityForRequests:"
+ "_initWithID:kind:context:clientID:enableAppDistribution:"
+ "_initWithManifestDictionary:"
+ "_leadingGlyphInCTRunSafariIsRightToLeft:"
+ "_parentRequests"
+ "_pendingSVGImageRenderingRequestsThatCanBeSavedToDisk"
+ "_registerInfo:forRequest:"
+ "_registerRequest:isOneTimeRequest:queue:responseHandler:tokenSetUpBlock:"
+ "_registerSubrequest:isOneTimeRequest:forRequests:queue:responseHandler:"
+ "_registerToken:isCacheRequest:withProvider:"
+ "_requestTokens"
+ "_requestsToCacheRequestTokens"
+ "_requestsToSubrequestTokens"
+ "_sendResponse:toResponseHandlersForRequests:didReceiveNewData:"
+ "_sessionRulesIDs"
+ "_stopWatchingUpdatesForRequests:"
+ "_subrequests"
+ "_templateIconURL"
+ "_updatePriorityOfRequest:"
+ "_webKitExtension"
+ "_webViewConfiguration"
+ "_windowProxyStream"
+ "actionIconForSize:"
+ "addCacheRequestToken:"
+ "addRequestToken:"
+ "alert-translation"
+ "alertControllerWithTitle:message:imageNamed:preferredStyle:"
+ "applicationCategoryTypeForCategories:"
+ "backgroundContentIsPersistent"
+ "cacheData:forRequest:"
+ "cacheData:forRequest:usingToken:"
+ "cachedImageForFolderUUID:"
+ "canProvideUpdatesForRequest:"
+ "canSaveToDisk"
+ "canStopWatchingRequestAfterRemovingToken:"
+ "categories"
+ "clearExtractedSchemaData"
+ "com.apple.Safari.WBSBookmarkFolderTouchIconProvider.%@.%p._internalQueue"
+ "contentOfFolderDidUpdateWithUUID:"
+ "currentDevice"
+ "defaultLocale"
+ "defaultSearchEngineMatchesExperiment"
+ "deviceClass"
+ "didDownloadDataForRemotelyUpdatableDataController:"
+ "displayActionLabel"
+ "donateWindowProxyWithDomain:openedDomain:windowProxyProperty:accessedPropertyDirectly:"
+ "dynamicRulesIDs"
+ "fetchDataFromWebView:completion:"
+ "fetchSchemaDataForWebView:"
+ "filteredSchemaData"
+ "flight"
+ "folderUUIDForRequest:"
+ "i24@0:8q16"
+ "iconForSize:"
+ "initWithDataFormat:builtInListURL:downloadsDirectoryURL:resourceName:resourceVersion:updateDateDefaultsKey:updateInterval:snapshotClass:snapshotTransformerClass:"
+ "initWithDomain:openedDomain:visited:property:accessedPropertyDirectly:"
+ "initWithHost:templateIconURL:themeColor:canSaveToDisk:"
+ "initWithInput:triggerEvent:searchType:indexType:queryId:originatingApp:"
+ "initWithRequest:isOneTimeRequest:queue:responseHandler:"
+ "initWithResourceBaseURL:error:"
+ "initWithSnapshotData:error:"
+ "initWithURL:title:monogramConfiguration:overrideForegroundColor:"
+ "initWithWebKitMatchPattern:"
+ "isBiomeStreamDonationAvailable"
+ "matchPatternWtihWebKitPattern:"
+ "matchPatternsWtihWebKitPatterns:"
+ "pageContextDataFetcherDidFinishFetching:forURL:withError:"
+ "parentRequests"
+ "preloadRequest:withPriority:queue:responseHandler:"
+ "preloadRequests:withPriority:queue:responseHandler:"
+ "queue"
+ "registerOneTimeRequest:priority:queue:responseHandler:"
+ "registerRequest:priority:queue:responseHandler:"
+ "removeParentRequest:"
+ "removedTabGroupWithUUID:"
+ "requestTokens"
+ "requestsWithFolderUUIDsDidBecomeInvalid:"
+ "safari_applicationCategoryType"
+ "safari_hasLeadingEmojiSafariIsRightToLeft:"
+ "safari_leadingEmojiSafariIsRightToLeft:"
+ "schedule"
+ "sendEvent:"
+ "sessionRulesIDs"
+ "setDynamicRulesIDs:"
+ "setInspectable:"
+ "setParentRequests:"
+ "setSessionRulesIDs:"
+ "setSubrequests:"
+ "shouldRemotelyUpdatableDataControllerUpdateOnSchedule:"
+ "siteMetadataProvider:cacheData:forRequest:"
+ "siteMetadataProvider:didFinishCachingDataWithToken:"
+ "siteMetadataProvider:didReceiveResponse:ofType:didReceiveNewData:forRequests:"
+ "siteMetadataProvider:registerOneTimeSubrequest:forRequests:queue:responseHandler:"
+ "siteMetadataProvider:registerSubrequest:forRequests:queue:responseHandler:"
+ "snapshotData"
+ "stringForType"
+ "subrequests"
+ "subrequestsForRequest:maximumNumberOfSubrequests:"
+ "supportsManifestVersion:"
+ "tabGroupManager:didReloadAferSyncWithResult:"
+ "templateIconURL"
+ "timerWithInterval:repeats:queue:handler:"
+ "trialABGroupIdentifier"
+ "unkown"
+ "userAssignedName"
+ "v16@?0@\"_WBSSiteMetadataToken\"8"
+ "v24@0:8@\"WBSRemotelyUpdatableDataController\"16"
+ "v32@0:8@\"<WBSSiteMetadataProvider>\"16@24"
+ "v32@0:8@\"WBTabGroupManager\"16q24"
+ "v32@?0@\"NSObject<OS_dispatch_queue>\"8@\"NSMutableSet\"16^B24"
+ "v32@?0@\"WBSSiteMetadataRequest<WBSIconRequest>\"8Q16^B24"
+ "v32@?0@8@\"WKFrameInfo\"16@\"NSString\"24"
+ "v36@0:8@16B24@28"
+ "v40@0:8@\"<WBSSiteMetadataProvider>\"16@24@\"WBSSiteMetadataRequest\"32"
+ "v40@0:8@16@?24@?32"
+ "v52@0:8@\"<WBSSiteMetadataProvider>\"16@\"WBSSiteMetadataResponse\"24q32B40@\"NSSet\"44"
+ "webKitExtension"
+ "\xd1"
- "\x01\x11\x17"
- "\x01\x13"
- "\x02\x19'"
- "\v"
- "\x0f\x1c\x14\x11\x11\x12\x16\x11\x11\x16\x11\x12\x13\x11\x11\x16\""
- "\x1e"
- "!\x12"
- "1000539e"
- "1099c"
- "2"
- "8617.2.4.10.8"
- "<%@ %p (composed identifier \"%@\")>"
- "@\"NSData\"24@0:8Q16"
- "@\"SFResultRankingFeedback\"24@?0@\"SFSearchResult\"8Q16"
- "@\"SFSectionRankingFeedback\"24@?0@\"SFResultSection\"8Q16"
- "@\"WBSParsecActionButton\""
- "@\"WBSParsecActionButton\"16@0:8"
- "@\"WBSParsecSearchSportsAttributionExtraCompletionItem\"16@0:8"
- "@\"WBSRemotePlistController\""
- "@48@0:8@\"<WBSSiteMetadataProvider>\"16@\"WBSSiteMetadataRequest\"24q32@?<v@?@\"WBSSiteMetadataResponse\">40"
- "@48@0:8@16@24q32@?40"
- "@?32@0:8@16Q24"
- "B24@0:8@\"WBSRemotePlistController\"16"
- "DebugDidTapAtLeastFiveReadingListArticles"
- "DeviceClassNumber"
- "Failed to load `default_icon` image for the `browser_action` or `page_action` manifest entry."
- "Failed to load images in `default_icon` for the `browser_action` or `page_action` manifest entry."
- "Failed to load images in `icons` manifest entry."
- "Found unexpected key (%{private}@), not specified in required or optional keys."
- "Manifest has an empty or missing 'icons' section for extension with identifier %{private}@"
- "Manifest has an empty or missing 'name' for extension with identifier %{private}@"
- "Manifest has an empty or missing 'version' for extension with identifier %{private}@"
- "No icons specified for extension with identifier %{private}@"
- "No toolbar icons specified for extension with identifier %{private}@"
- "PLAY"
- "SearchURLTemplateIPodTouch"
- "T@\"<_CompletionListRankingObserverFeedbackGeneratorDelegate>\",W,N"
- "T@\"NSArray\",R,C,N,V_itunesContentIdentifiers"
- "T@\"NSDictionary\",C,N"
- "T@\"NSMutableSet\",R,N,V_tokens"
- "T@\"NSString\",R,C,N,V_completion"
- "T@\"NSString\",R,C,N,V_itunesCompletion"
- "T@\"NSString\",R,C,N,V_itunesLabel"
- "T@\"NSString\",R,C,N,V_labelAlignment"
- "T@\"NSString\",R,C,N,V_offerType"
- "T@\"NSString\",R,C,N,V_punchoutAppBundleIdentifier"
- "T@\"NSString\",R,C,N,V_punchoutAppName"
- "T@\"NSTimer\",&,N,V_delayTimer"
- "T@\"SFSearchResult\",R,N,VsfSearchResultValue"
- "T@\"UIImage\",C,V_iconImage"
- "T@\"WBSParsecActionButton\",R,N"
- "T@\"WBSParsecActionButton\",R,N,V_actionButton"
- "T@\"WBSParsecImageRepresentation\",R,N,V_baseIcon"
- "T@\"WBSParsecSearchSportsAttributionExtraCompletionItem\",R,N"
- "T@\"WBSQuerySuggestion\",&,N"
- "T@,&,N,V_token"
- "TB,N,V_requestedOptionalAccessToAllHosts"
- "TB,R,N,GisForAppleMusicResult"
- "TB,R,N,GisForStreamingResult,V_forStreamingResult"
- "TB,R,N,GisGenerated"
- "TB,R,N,GisOverlay,V_overlay"
- "Td,N,V_numberOfDynamicRules"
- "Td,N,V_numberOfSessionRules"
- "Unable to find manifest.json in the bundle for extension with identifier %{private}@"
- "WBSBookmarkFolderTouchIconProviderInfo"
- "WBSBookmarkFolderTouchIconProviderRequestInfo"
- "WBSParsecActionButton"
- "WBSParsecSearchSportsAttributionExtraCompletionItem"
- "WBSRemotePlistControllerDelegate"
- "WBSRemotePlistSnapshot"
- "_WBSTabGroupIconMetadata"
- "_actionButton"
- "_arrayOfThumbnailURLsShownInFolderIconFromTabsArray:"
- "_baseIcon"
- "_cancelRequestsAndClearCacheForTabGroup:"
- "_cancelRequestsAndClearCacheForTabGroup:metadata:"
- "_deviceName"
- "_displayDescription"
- "_displayShortName"
- "_displayVersion"
- "_forStreamingResult"
- "_hasCachedIcon"
- "_hasCachedPreferencesIcon"
- "_hasCachedToolbarImage"
- "_highestRequestPriorityForRequest:"
- "_iconImage"
- "_initWithWebKitMatchPattern:"
- "_itunesCompletion"
- "_itunesContentIdentifiers"
- "_itunesLabel"
- "_labelAlignment"
- "_numberOfDynamicRules"
- "_numberOfSessionRules"
- "_offerType"
- "_overlay"
- "_parsedManifestDisplayStrings"
- "_populateDisplayStringsIfNeeded"
- "_preferencesIcon"
- "_punchoutAppBundleIdentifier"
- "_punchoutAppName"
- "_registerToken:withProvider:"
- "_responseHandlerForRequest:thumbnailIndex:"
- "_sendResponse:toResponseHandlersForRequest:didReceiveNewData:"
- "_setProcessDisplayName:"
- "_tabGroupIconMetadataCache"
- "_tabUrlArray"
- "_token"
- "_toolbarImage"
- "_uuid"
- "actionButton"
- "action_area"
- "action_button"
- "action_card_type"
- "action_completion"
- "action_completion_itunes"
- "action_destination"
- "action_target"
- "action_type"
- "adam_ids"
- "addTemplateIconAtURL:withThemeColor:forHost:toDisk:"
- "attribution_image"
- "attribution_key"
- "attribution_url"
- "baiduTrackingCodeiPodTouch"
- "baseIcon"
- "base_icon"
- "bookmarkUUIDForRequest:"
- "com.apple.Safari.BookmarkFolderTouchIconProvider.internalQueue.%p"
- "com.apple.SafariShared.ParsecSportsAttributionErrorDomain"
- "currentAccessibleOrigins"
- "dataWithContentsOfFile:"
- "didDownloadPlistForRemotePlistController:"
- "displayableFolderContentsForRequest:"
- "enter"
- "extensionIconWithBaseURI:idealPointSize:validateAndReadResourceHandler:"
- "extraCompletionItem"
- "forAppleMusicResult"
- "forStreamingResult"
- "hasSameIconAsTabGroup:"
- "https://duckduckgo.com/?q={searchTerms}&t=ipod"
- "https://www.ecosia.org/search?q={searchTerms}&tts=st_asaf_ipod"
- "https://yandex.by/search/touch/?clid=1906724&text={searchTerms}"
- "https://yandex.com.tr/search/touch/?clid=1906724&text={searchTerms}"
- "https://yandex.com/search/touch/?clid=1906724&text={searchTerms}"
- "https://yandex.kz/search/touch/?clid=1906724&text={searchTerms}"
- "https://yandex.ru/search/touch/?clid=1906724&text={searchTerms}"
- "https://yandex.ua/search/touch/?clid=1906724&text={searchTerms}"
- "iconImage"
- "initWithBuiltInListURL:downloadsDirectoryURL:resourceName:resourceVersion:updateDateDefaultsKey:updateInterval:snapshotClass:snapshotTransformerClass:"
- "initWithDictionary:mediaKind:"
- "initWithInput:triggerEvent:indexType:queryId:"
- "initWithOneTimeRequest:priority:responseHandler:"
- "initWithPlistData:error:"
- "initWithRequest:priority:responseHandler:"
- "initWithTabGroup:token:"
- "initWithURL:title:monogramConfiguration:overrideForegroundColor:saveToDisk:"
- "isForAppleMusicResult"
- "isForStreamingResult"
- "isNamed"
- "isOverlay"
- "is_overlay"
- "itunesCompletion"
- "itunesContentIdentifiers"
- "itunesLabel"
- "labelAlignment"
- "label_align"
- "label_itunes"
- "manifest.json"
- "numberOfDynamicRules"
- "numberOfSessionRules"
- "offerType"
- "offer_type"
- "overlay"
- "plistDataWithFormat:"
- "punchoutAppBundleIdentifier"
- "punchoutAppName"
- "q28@0:8@16B24"
- "removeInfoForFolderWithUUID:"
- "removeInfoForFoldersWithUUIDs:"
- "safari_stringHasLeadingEmoji:"
- "saveToDisk"
- "saveToDiskKey"
- "setIconImage:"
- "setNumberOfDynamicRules:"
- "setNumberOfSessionRules:"
- "setToken:"
- "shouldRemotePlistControllerUpdateOnSchedule:"
- "siteMetadataProvider:registerOneTimeRequest:priority:responseHandler:"
- "siteMetadataProvider:registerRequest:priority:responseHandler:"
- "streaming"
- "token"
- "toolbarImageWithBaseURI:idealPointSize:validateAndReadResourceHandler:"
- "touchIconRequestForBookmark:inFolderWithRequest:"
- "typeForSFSearchResult:isOneLine:"
- "updateIconForTabGroupIfNeeded:tabProvider:"
- "v24@0:8@\"WBSRemotePlistController\"16"
- "v24@?0@8@\"WKFrameInfo\"16"
- "v32@?0@\"NSURL\"8Q16^B24"
- "v32@?0@\"WBTab\"8Q16^B24"

```
