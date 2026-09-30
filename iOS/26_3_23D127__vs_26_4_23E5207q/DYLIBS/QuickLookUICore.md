## QuickLookUICore

> `/System/Library/PrivateFrameworks/QuickLookUICore.framework/QuickLookUICore`

```diff

-1016.203.1.0.0
-  __TEXT.__text: 0x217c4
-  __TEXT.__auth_stubs: 0x8e0
+1016.205.2.0.0
+  __TEXT.__text: 0x230d4
+  __TEXT.__auth_stubs: 0x890
   __TEXT.__delay_stubs: 0x1c0
   __TEXT.__delay_helper: 0x25c
   __TEXT.__objc_methlist: 0x30bc
   __TEXT.__const: 0xe0
   __TEXT.__cstring: 0x1fbb
-  __TEXT.__gcc_except_tab: 0x914
+  __TEXT.__gcc_except_tab: 0x8d0
   __TEXT.__oslogstring: 0x186e
-  __TEXT.__unwind_info: 0xb28
+  __TEXT.__unwind_info: 0xb98
   __TEXT.__objc_classname: 0x5a8
   __TEXT.__objc_methname: 0x8d73
   __TEXT.__objc_methtype: 0x155f

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x20b0
   __DATA_CONST.__objc_superrefs: 0xc8
-  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH_CONST.__auth_got: 0x490
   __AUTH_CONST.__const: 0x1f0
   __AUTH_CONST.__cfstring: 0x2020
   __AUTH_CONST.__objc_const: 0x7480
   __AUTH_CONST.__objc_intobj: 0x138
-  __AUTH.__objc_data: 0x960
+  __AUTH.__objc_data: 0xa50
   __DATA.__objc_ivar: 0x39c
   __DATA.__data: 0x78c
-  __DATA.__bss: 0x170
-  __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__bss: 0x30
+  __DATA.__bss: 0x1a0
+  __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5ACFA237-0B8D-32F3-9C65-7BACF6352F6D
+  UUID: 391E86F4-E9AA-3156-B0CC-D81F69BDF1F7
   Functions: 1021
-  Symbols:   4035
+  Symbols:   4031
   CStrings:  2354
 
Symbols:
+ GCC_except_table22
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
Functions:
~ -[QLToolbarButtonItemRepresentation isEqual:] : 420 -> 440
~ -[QLToolbarButtonItemRepresentation setLongPressTarget:action:] : 224 -> 236
~ -[QLToolbarButtonItemRepresentation setLongPressGestureRecognizer:] : 20 -> 80
~ -[QLToolbarButtonOption initWithIdentifier:] : 124 -> 116
~ +[QLToolbarButtonOption cancelOption] : 132 -> 136
~ -[QLToolbarButtonOption isCancel] : 64 -> 68
~ -[QLToolbarButtonOption isEqual:] : 352 -> 384
~ -[QLToolbarButtonOption encodeWithCoder:] : 224 -> 240
~ -[QLToolbarButtonOption initWithCoder:] : 220 -> 228
~ -[QLToolbarButton initWithIdentifier:] : 136 -> 128
~ -[QLToolbarButton _barButtonImage] : 320 -> 360
~ -[QLToolbarButton barButtonWithTarget:action:maxSize:] : 628 -> 668
~ -[QLToolbarButton handleLongPress:] : 900 -> 940
~ -[QLToolbarButton isEqual:] : 952 -> 1024
~ -[QLToolbarButton encodeWithCoder:] : 592 -> 620
~ -[QLToolbarButton initWithCoder:] : 592 -> 616
~ _QLLocalizedStringFromTable : 128 -> 132
~ _QLLocalizedStringWithDefaultValue : 128 -> 132
~ _QLRunInMainThread : 116 -> 120
~ _QLRunInMainThreadSync : 116 -> 120
~ _QLRunInBackgroundThread : 140 -> 148
~ -[QLItem initWithPreviewItemProvider:contentType:previewTitle:fileSize:] : 272 -> 256
~ -[QLItem initWithData:contentType:previewTitle:] : 236 -> 220
~ -[QLItem initWithDataProvider:contentType:previewTitle:] : 236 -> 220
~ -[QLItem initWithURL:] : 188 -> 192
~ -[QLItem initWithURL:previewTitle:editingMode:] : 232 -> 236
~ -[QLItem initWithURLSandboxWrapper:] : 224 -> 232
~ -[QLItem initWithURL:MIMEType:] : 176 -> 172
~ -[QLItem initWithSearchableItemUniqueIdentifier:queryString:applicationBundleIdentifier:previewTitle:] : 240 -> 224
~ -[QLItem initWithSearchableItemUniqueIdentifier:applicationBundleIdentifier:] : 176 -> 168
~ +[QLItem itemWithPreviewItem:] : 736 -> 788
~ -[QLItem dealloc] : 112 -> 116
~ -[QLItem isEqual:] : 1448 -> 1604
~ ___28-[QLPreviewContext isEqual:]_block_invoke : 112 -> 108
~ -[QLItem internalCopy] : 512 -> 516
~ -[QLItem encodeWithCoder:] : 1656 -> 1816
~ -[QLItem initWithCoder:] : 1352 -> 1436
~ -[QLItem description] : 164 -> 176
~ -[QLItem clientPreviewOptions] : 188 -> 200
~ -[QLItem setPreviewOptions:] : 12 -> 64
~ -[QLItem clientPreviewItemDisplayState] : 188 -> 200
~ -[QLItem setPreviewItemDisplayState:] : 12 -> 64
~ -[QLItem isPromisedItem] : 148 -> 160
~ -[QLItem alternateShareURL] : 172 -> 188
~ -[QLItem fetcher] : 144 -> 148
~ -[QLItem setFetcher:] : 104 -> 108
~ -[QLItem createPreviewContext] : 588 -> 632
~ -[QLItem uuid] : 88 -> 92
~ -[QLItem itemSize] : 100 -> 112
~ -[QLItem previewItemURL] : 108 -> 120
~ -[QLItem thumbnailGenerator] : 96 -> 100
~ -[QLItem originalPreviewItem] : 16 -> 64
~ ___41-[QLItem setPreviewItemProviderProgress:]_block_invoke : 180 -> 196
~ -[QLItem previewItemTitle] : 312 -> 364
~ -[QLItem previewItemContentType] : 100 -> 112
~ -[QLItem generatedPreviewItemType] : 252 -> 256
~ -[QLItem shareableURL] : 228 -> 260
~ -[QLItem shouldCreateTemporaryDirectoryInHost] : 56 -> 60
~ -[QLItem internalShouldCreateTemporaryDirectoryInHost] : 420 -> 432
~ -[QLItem prepareSaveURL:] : 120 -> 124
~ -[QLItem saveURL] : 248 -> 280
~ -[QLItem setEditedCopy:] : 204 -> 212
~ -[QLItem supportsChromelessUI] : 180 -> 184
~ -[QLItem shouldOpenInFullScreen] : 132 -> 136
~ +[QLItem customExtensionCommunicationEncodedClasses] : 68 -> 84
~ ___52+[QLItem customExtensionCommunicationEncodedClasses]_block_invoke : 236 -> 240
~ +[QLItem encodedClasses] : 68 -> 84
~ ___24+[QLItem encodedClasses]_block_invoke : 164 -> 176
~ -[QLItem setOriginalPreviewItem:] : 12 -> 64
~ -[QLItem setPreviewItemURL:] : 12 -> 64
~ -[QLItem setItemSize:] : 12 -> 64
~ -[QLItem setThumbnailGenerator:] : 12 -> 64
~ -[QLItem setUTIAnalyzer:] : 12 -> 64
~ -[QLItem setPreviewItemContentType:] : 12 -> 64
~ -[QLItem setBackgroundColorOverride:] : 12 -> 64
~ -[QLItem setPreviewItemTitle:] : 12 -> 64
~ -[QLItem setLastSavedEditedCopy:] : 12 -> 64
~ -[QLItem setUuid:] : 12 -> 64
~ -[QLItem setInternalShouldCreateTemporaryDirectoryInHost:] : 12 -> 64
~ -[QLItem setSandboxingURLWrapper:] : 12 -> 64
~ -[QLItemProviderFetcher initWithContentType:fileSize:] : 176 -> 168
~ -[QLItemProviderFetcher fetchContentWithAllowedOutputClasses:inQueue:updateBlock:completionBlock:] : 248 -> 232
~ ___98-[QLItemProviderFetcher fetchContentWithAllowedOutputClasses:inQueue:updateBlock:completionBlock:]_block_invoke : 476 -> 488
~ -[QLItemProviderFetcher _updateCompletionBlockWithAllowedOutputClasses:URL:] : 192 -> 180
~ ___76-[QLItemProviderFetcher _updateCompletionBlockWithAllowedOutputClasses:URL:]_block_invoke : 404 -> 440
~ ___48-[QLItemProviderFetcher updatedURLWithProgress:]_block_invoke : 164 -> 176
~ -[QLItemProviderFetcher getURLWithDownloadTracker:completionHandler:] : 340 -> 332
~ ___69-[QLItemProviderFetcher getURLWithDownloadTracker:completionHandler:]_block_invoke_2 : 412 -> 408
~ -[QLItemProviderFetcher shareableItem] : 16 -> 64
~ -[QLItemProviderFetcher fetchedContent] : 72 -> 84
~ -[QLItemProviderFetcher itemSize] : 16 -> 64
~ ___40-[QLItemProviderFetcher newItemProvider]_block_invoke : 116 -> 120
~ -[QLItemProviderFetcher initWithCoder:] : 160 -> 164
~ -[QLItemProviderFetcher setLastContent:] : 20 -> 80
~ -[QLTextItemTransformer transformedContentsFromURL:context:error:] : 204 -> 216
~ -[QLTextItemTransformer transformedContentsFromData:context:error:] : 200 -> 208
~ +[QLTextItemTransformer attributedStringFromData:encoding:typeIdentifier:error:] : 76 -> 84
~ -[QLThreadInvoker initWithConnection:data:error:] : 188 -> 172
~ -[QLThreadInvoker connectionDidReceiveDataLengthReceived:] : 96 -> 100
~ _QLSLogHandle : 72 -> 80
~ +[QLPreviewConverterURLProtocol registerPreview:] : 100 -> 108
~ +[QLPreviewConverterURLProtocol _errorForNoPreview] : 248 -> 256
~ +[QLPreviewConverterURLProtocol unregisterURLs:andPreview:] : 116 -> 120
~ -[QLPreviewConverterParts setDelegate:] : 148 -> 152
~ +[QLPreviewConverterParts registerPreview:] : 408 -> 424
~ +[QLPreviewConverterParts unregisterPreview:] : 384 -> 392
~ -[QLPreviewConverterParts safeRequestForRequest:] : 600 -> 708
~ -[QLPreviewConverterParts startComputingPreview] : 104 -> 108
~ -[QLPreviewConverterParts computePreviewInThread] : 2184 -> 2284
~ -[QLPreviewConverterParts isCancelled] : 76 -> 132
~ -[QLPreviewConverterParts startDataRepresentationWithContentType:properties:] : 1316 -> 1396
~ -[QLPreviewConverterParts newAttachmentURLWithID:properties:] : 172 -> 176
~ -[QLPreviewConverterParts appendData:forURL:lastChunk:] : 732 -> 740
~ -[QLPreviewConverterParts setError:] : 112 -> 116
~ -[QLPreviewConverterParts previewRequest] : 116 -> 120
~ -[QLPreviewConverterParts previewResponse] : 228 -> 244
~ -[QLPreviewConverterParts setConnection:] : 20 -> 80
~ -[QLPreviewConverterParts setUrl:] : 20 -> 80
~ -[QLPreviewConverterParts setData:] : 20 -> 80
~ -[QLPreviewConverterParts setFileName:] : 20 -> 80
~ -[QLPreviewConverterParts setUti:] : 20 -> 80
~ -[QLPreviewConverterParts setPassword:] : 20 -> 80
~ -[QLDataFetcher initWithItem:contentType:] : 216 -> 220
~ -[QLDataFetcher initWithData:contentType:previewItemTitle:] : 220 -> 212
~ -[QLDataFetcher fetchContentWithAllowedOutputClasses:inQueue:updateBlock:completionBlock:] : 196 -> 188
~ ___90-[QLDataFetcher fetchContentWithAllowedOutputClasses:inQueue:updateBlock:completionBlock:]_block_invoke : 356 -> 364
~ -[QLDataFetcher itemSize] : 112 -> 116
~ -[QLDataFetcher _createTemporaryFileIfNeeded] : 800 -> 832
~ -[QLDataFetcher _deleteTempraryFileIfNeeded] : 340 -> 344
~ -[QLDataFetcher _temporaryFilename] : 108 -> 120
~ -[QLDataFetcher shareableItem] : 68 -> 80
~ -[QLDataFetcher prepareShareableItem:] : 104 -> 108
~ -[QLDataFetcher fetchedContent] : 96 -> 108
~ -[QLDataFetcher loadDataIfNeeded] : 184 -> 192
~ -[QLDataFetcher newItemProvider] : 476 -> 480
~ ___32-[QLDataFetcher newItemProvider]_block_invoke : 116 -> 120
~ ___32-[QLDataFetcher newItemProvider]_block_invoke_2 : 112 -> 116
~ -[QLDataFetcher initWithCoder:] : 276 -> 288
~ _QLPreviewControllerSupportsContentType : 316 -> 324
~ _QLPreviewGetSupportedMIMETypes : 88 -> 100
~ __QLLayoutIsRTL : 68 -> 72
~ _QLItemViewControllerVendorForURL : 120 -> 124
~ _QLItemViewControllerVendorForItem : 120 -> 124
~ -[QLKeyCommand initWithCoder:] : 132 -> 136
~ -[QLKeyCommand encodeWithCoder:] : 108 -> 116
~ -[QLKeyCommand setKeyCommand:] : 12 -> 64
~ +[QLItemFetcherFactory fetcherForPreviewItem:] : 976 -> 1068
~ +[QLItemFetcherFactory possibleFetcherClasses] : 68 -> 84
~ ___46+[QLItemFetcherFactory possibleFetcherClasses]_block_invoke : 164 -> 168
~ -[QLItemFetcher init] : 116 -> 120
~ -[QLItemFetcher registerObserver:withBlock:] : 180 -> 184
~ -[QLItemFetcher _notifyObservers] : 164 -> 172
~ ___33-[QLItemFetcher _notifyObservers]_block_invoke : 264 -> 268
~ -[QLItemFetcher encodeWithCoder:] : 96 -> 100
~ +[QLExtensionManager(_QLUtilities) extensionForItem:] : 172 -> 184
~ +[QLExtensionManager(_QLUtilities) ql_isPreviewExtensionThatHaveCustomPresentationViewForItem:] : 56 -> 60
~ +[QLExtensionManager(_QLUtilities) ql_previewExtensionCustomLoadingTimeForItem:] : 76 -> 84
~ +[QLExtensionManager(_QLUtilities) ql_applicationBundleIdentifierOfExtensionForItem:] : 76 -> 84
~ -[NSExtension(_QLPreviewControllerUtilities) ql_isPreviewExtensionThatHaveCustomPresentationView] : 88 -> 96
~ -[NSExtension(_QLPreviewControllerUtilities) ql_previewExtensionCustomLoadingTime] : 84 -> 92
~ +[QLSpotlightSearchableItemInfo spotlightInfoWithUniqueIdentifier:queryString:applicationBundleIdentifier:] : 152 -> 144
~ -[QLSpotlightSearchableItemInfo encodeWithCoder:] : 128 -> 136
~ -[QLSpotlightSearchableItemInfo initWithCoder:] : 236 -> 248
~ __getIWorkImportLibrary : 272 -> 268
~ _IWGenerateAtomicPreviewForURL : 372 -> 396
~ _QLIWorkCalculatePreview : 1808 -> 1840
~ _IWGenerateAtomicPreviewForData : 428 -> 452
~ -[NSURL(_QL_Utilities) _QLIsPackageURL] : 296 -> 288
~ -[NSURL(_QL_Utilities) _QLDownloadingStatusIsNotCurrent] : 324 -> 316
~ -[NSURL(_QL_Utilities) _QLIsHiddenFile] : 304 -> 296
~ -[NSURL(_QL_Utilities) _QLSingleFileSizeForURL:] : 304 -> 300
~ -[NSURL(_QL_Utilities) _QLUrlFileSize] : 892 -> 916
~ +[NSURL(_QL_Utilities) _QLCreateTemporaryDirectory:] : 456 -> 476
~ +[NSURL(_QL_Utilities) _QLTemporaryFileURLWithType:filename:] : 204 -> 228
~ +[NSURL(_QL_Utilities) _QLTemporaryFileURLWithType:uuid:] : 124 -> 132
~ +[NSURL(_QL_Utilities) _QLTemporaryFileURLWithType:forOriginalFileAtURL:temporaryFileURL:temporaryDirectoryURL:fallbackUUID:] : 596 -> 616
~ +[NSURL(_QL_Utilities) _QLCreateTemporaryDirectoryForOriginalFileAtURL:error:] : 364 -> 376
~ _PGCopyPreviewURLForPackageURL : 264 -> 272
~ _PGGeneratePreviewForURL : 152 -> 156
~ -[QLSpotlightFetcher initWithSearchableItemUniqueIdentifier:queryString:applicationBundleIdentifier:] : 260 -> 264
~ -[QLSpotlightFetcher fetchContentWithAllowedOutputClasses:inQueue:updateBlock:completionBlock:] : 196 -> 188
~ ___95-[QLSpotlightFetcher fetchContentWithAllowedOutputClasses:inQueue:updateBlock:completionBlock:]_block_invoke : 196 -> 200
~ -[QLSpotlightFetcher initWithCoder:] : 264 -> 276
~ -[QLGeneratorFetcher initWithURL:contentType:] : 168 -> 160
~ -[QLGeneratorFetcher _callCompletionBlockIfNecessary:withReply:error:] : 200 -> 192
~ -[QLGeneratorFetcher fetchContentWithAllowedOutputClasses:inQueue:updateBlock:completionBlock:] : 584 -> 592
~ ___95-[QLGeneratorFetcher fetchContentWithAllowedOutputClasses:inQueue:updateBlock:completionBlock:]_block_invoke : 840 -> 868
~ ___95-[QLGeneratorFetcher fetchContentWithAllowedOutputClasses:inQueue:updateBlock:completionBlock:]_block_invoke_3 : 140 -> 136
~ +[QLNetworkStateObserver sharedInstance] : 160 -> 176
~ -[QLNetworkStateObserver pushOperation] : 116 -> 120
~ -[QLNetworkStateObserver popOperation] : 116 -> 120
~ ___40-[QLNetworkStateObserver startObserving]_block_invoke : 832 -> 836
~ ___39-[QLNetworkStateObserver stopObserving]_block_invoke : 144 -> 148
~ -[QLNetworkStateObserver _updateNetworkActivityIndicator] : 144 -> 152
~ -[QLNetworkStateObserver _setNetworkState:] : 260 -> 256
~ -[QLNetworkStateObserver networkStateWithCompletionBlock:] : 196 -> 204
~ -[QLNetworkStateObserver updateState:] : 248 -> 244
~ +[QLNetworkStateObserver usingRemoteNetworkObserver] : 96 -> 104
~ +[QLNetworkStateObserver networkAccessShouldGoThroughCloudDocsDaemon] : 96 -> 104
~ -[QLNetworkStateObserver _updateRemoteObserver] : 120 -> 124
~ +[AVAsset(_QLUtilities) assetIsAutoloopMedia:completionHandler:] : 284 -> 280
~ ___64+[AVAsset(_QLUtilities) assetIsAutoloopMedia:completionHandler:]_block_invoke : 272 -> 292
~ -[AVAsset(_QLUtilities) ql_hasValidVideoTrack] : 352 -> 360
~ -[AVAsset(_QLUtilities) ql_imageSizeOfFirstVideoTrack] : 372 -> 380
~ -[QLPreviewItemEditedCopy initWithEditedCopyURL:temporaryDirectoryCreatedInHost:] : 428 -> 432
~ -[QLPreviewItemEditedCopy initWithEditedCopyURL:containerTemporaryURL:temporaryDirectoryCreatedInHost:] : 376 -> 372
~ -[QLPreviewItemEditedCopy containerStillExists] : 120 -> 132
~ -[QLPreviewItemEditedCopy markAsPurgeable] : 896 -> 904
~ -[QLPreviewItemEditedCopy removeFromDisk:] : 488 -> 492
~ -[QLPreviewItemEditedCopy isEqual:] : 580 -> 624
~ -[QLPreviewItemEditedCopy description] : 156 -> 168
~ -[QLPreviewItemEditedCopy url] : 80 -> 92
~ -[QLPreviewItemEditedCopy containerURL] : 80 -> 92
~ -[QLPreviewItemEditedCopy outputURLContentType] : 92 -> 100
~ -[QLPreviewItemEditedCopy encodeWithCoder:] : 252 -> 248
~ -[QLPreviewItemEditedCopy initWithCoder:] : 380 -> 400
~ -[QLPreviewItemEditedCopy setEditedCopyURLWrapper:] : 12 -> 64
~ -[QLPreviewItemEditedCopy setDirectoryURLWrapper:] : 12 -> 64
~ -[QLPreviewItemEditedCopy setEditedCopyURL:] : 12 -> 64
~ -[QLPreviewItemEditedCopy setHostTemporaryContainerURL:] : 12 -> 64
~ -[QLPreviewItemEditedCopy setUuid:] : 12 -> 64
~ ___104-[QLItemThumbnailGenerator generateThumbnailForItem:ofSize:minimumSize:scale:badgeType:completionBlock:]_block_invoke : 96 -> 100
~ -[QLItemThumbnailGenerator generateThumbnailRepresentationForItem:ofSize:minimumSize:scale:badgeType:completionBlock:] : 644 -> 656
~ ___118-[QLItemThumbnailGenerator generateThumbnailRepresentationForItem:ofSize:minimumSize:scale:badgeType:completionBlock:]_block_invoke : 376 -> 372
~ -[QLItemThumbnailGenerator _generateThumbnailWithURL:size:minimumDimension:scale:badgeType:completionHandler:] : 224 -> 220
~ -[QLItemThumbnailGenerator _generateThumbnailWithFPItem:size:minimumDimension:scale:badgeType:completionHandler:] : 224 -> 220
~ -[QLItemThumbnailGenerator _generateThumbnailWithData:contentType:size:minimumDimension:scale:badgeType:completionHandler:] : 244 -> 236
~ -[QLItemThumbnailGenerator _generateThumbnailForRequest:completionHandler:] : 208 -> 204
~ ___75-[QLItemThumbnailGenerator _generateThumbnailForRequest:completionHandler:]_block_invoke : 248 -> 244
~ -[QLItemThumbnailGenerator fetcherClassesForPreviewItem:] : 188 -> 184
~ ___57-[QLItemThumbnailGenerator fetcherClassesForPreviewItem:]_block_invoke : 200 -> 208
~ +[QLBasePreviewParts isBundleURL:] : 144 -> 156
~ -[QLBasePreviewParts computePreview] : 688 -> 720
~ _LPDFGeneratePreviewForURL : 176 -> 180
~ -[QLFPItemFetcher fetchContentWithAllowedOutputClasses:inQueue:updateBlock:completionBlock:] : 268 -> 244
~ -[QLFPItemFetcher _registerItemCollectionIfNeeded] : 348 -> 360
~ -[QLFPItemFetcher _urlHandler:] : 240 -> 244
~ ___31-[QLFPItemFetcher _urlHandler:]_block_invoke : 364 -> 360
~ ___40-[QLFPItemFetcher prepareShareableItem:]_block_invoke : 124 -> 132
~ -[QLFPItemFetcher initWithCoder:] : 160 -> 164
~ -[QLFPItemFetcher collection:didUpdateObservedItem:] : 20 -> 72
~ -[QLAppearance encodeWithCoder:] : 168 -> 176
~ -[QLAppearance description] : 192 -> 200
~ -[ARQuickLookPreviewItem initWithFileAtURL:] : 140 -> 132
~ -[ARQuickLookPreviewItem previewOptions] : 380 -> 404
~ -[ARQuickLookPreviewItem setCanonicalWebPageURL:] : 12 -> 64
~ -[ARQuickLookPreviewItem setFileURL:] : 12 -> 64
~ +[QLPreviewConverter convertibleMIMETypes] : 332 -> 372
~ +[QLPreviewConverter _officeMIMETypes] : 312 -> 324
~ +[QLPreviewConverter _iWorkMIMETypes] : 220 -> 232
~ +[QLPreviewConverter _rtfMIMETypes] : 172 -> 184
~ +[QLPreviewConverter _csvMIMETypes] : 172 -> 184
~ +[QLPreviewConverter _spreadSheetMIMETypes] : 224 -> 236
~ ___37+[QLPreviewConverter convertibleUTIs]_block_invoke : 412 -> 460
~ ___38+[QLPreviewConverter convertibleTypes]_block_invoke : 356 -> 368
~ +[QLPreviewConverter _officeUTIs] : 372 -> 384
~ +[QLPreviewConverter _iWorkUTIs] : 272 -> 284
~ +[QLPreviewConverter _rtfUTIs] : 172 -> 184
~ +[QLPreviewConverter _lpdfUTIs] : 164 -> 176
~ +[QLPreviewConverter _csvUTIs] : 164 -> 176
~ +[QLPreviewConverter _spreadSheetUTIs] : 264 -> 276
~ +[QLPreviewConverter isOfficeDocumentType:] : 112 -> 120
~ +[QLPreviewConverter isIWorkDocumentType:] : 112 -> 120
~ +[QLPreviewConverter isCSVDocumentType:] : 112 -> 120
~ +[QLPreviewConverter isLPDFDocumentType:] : 112 -> 120
~ +[QLPreviewConverter isRTFDocumentType:] : 112 -> 120
~ +[QLPreviewConverter isSpreadSheetDocumentType:] : 112 -> 120
~ -[QLPreviewConverter initWithURL:uti:options:] : 296 -> 300
~ -[QLPreviewConverter initWithData:name:uti:options:] : 276 -> 268
~ -[QLPreviewConverter initWithConnection:delegate:response:options:] : 444 -> 452
~ -[QLPreviewConverter previewFileName] : 76 -> 80
~ -[QLPreviewConverter previewUTI] : 76 -> 80
~ -[QLPreviewConverter previewParts] : 8 -> 56
~ -[QLPreviewConverter safeRequestForRequest:] : 128 -> 140
~ +[QLPreviewConverter isSafeURL:] : 92 -> 96
~ +[QLPreviewConverter isSafeRequest:] : 72 -> 76
~ -[QLPreviewConverter appendData:] : 156 -> 160
~ -[QLPreviewConverter appendDataArray:] : 744 -> 756
~ -[QLPreviewConverter _createDispatchIOChannel] : 608 -> 644
~ -[QLPreviewConverter _writeDataArrayIntoStream:] : 512 -> 520
~ -[QLItemTransformer transformedContentsFromURL:context:error:] : 8 -> 56
~ -[QLItemTransformer transformedContentsFromData:context:error:] : 8 -> 56
~ -[QLURLItemTransformer transformedContentsFromURL:context:error:] : 8 -> 56
~ -[QLDataItemTransformer transformedContentsFromData:context:error:] : 8 -> 56
~ -[QLUbiquitousItemFetcher fetchContentWithAllowedOutputClasses:inQueue:updateBlock:completionBlock:] : 840 -> 844
~ ___100-[QLUbiquitousItemFetcher fetchContentWithAllowedOutputClasses:inQueue:updateBlock:completionBlock:]_block_invoke : 628 -> 652
~ -[QLUbiquitousItemFetcher subscribeToPreviewItemProgress] : 192 -> 200
~ ___57-[QLUbiquitousItemFetcher subscribeToPreviewItemProgress]_block_invoke : 600 -> 608
~ -[QLUbiquitousItemFetcher observeValueForKeyPath:ofObject:change:context:] : 632 -> 624
~ -[QLUbiquitousItemFetcher dealloc] : 152 -> 156
~ -[QLUbiquitousItemFetcher isLongFetchOperation] : 124 -> 136
~ -[QLUbiquitousItemFetcher itemSize] : 172 -> 184
~ -[QLUbiquitousItemFetcher fetchedContent] : 68 -> 72
~ -[QLUbiquitousItemFetcher newItemProvider] : 240 -> 244
~ -[QLUbiquitousItemFetcher _removeUpdateBlockIfNeeded:] : 168 -> 176
~ -[QLUbiquitousItemFetcher _createURLForPackageIfNeeded] : 1084 -> 1116
~ ___55-[QLUbiquitousItemFetcher _createURLForPackageIfNeeded]_block_invoke : 316 -> 324
~ -[QLUbiquitousItemFetcher _deleteTempraryZipPackageFileIfNeeded] : 376 -> 388
~ -[QLUbiquitousItemFetcher initWithCoder:] : 276 -> 284
~ +[QLItem(PreviewInfo) supportedContentTypeIdentifiers] : 160 -> 176
~ ___54+[QLItem(PreviewInfo) supportedContentTypeIdentifiers]_block_invoke : 128 -> 140
~ +[QLItem(PreviewInfo) supportedContentTypes] : 160 -> 176
~ ___44+[QLItem(PreviewInfo) supportedContentTypes]_block_invoke : 128 -> 140
~ +[QLItem(PreviewInfo) webContentTypes] : 68 -> 84
~ ___38+[QLItem(PreviewInfo) webContentTypes]_block_invoke : 252 -> 264
~ +[QLItem(PreviewInfo) rtfContentTypes] : 68 -> 84
~ ___38+[QLItem(PreviewInfo) rtfContentTypes]_block_invoke : 116 -> 120
~ +[QLItem(PreviewInfo) contentTypeConformsToRTFD:] : 116 -> 124
~ +[QLItem(PreviewInfo) contentTypesToPreviewTypes] : 68 -> 84
~ ___49+[QLItem(PreviewInfo) contentTypesToPreviewTypes]_block_invoke : 1816 -> 1848
~ -[QLItem(PreviewInfo) _uncachedExtensionPreviewItemType] : 276 -> 284
~ -[QLItem(PreviewInfo) _uncachedPreviewItemTypeForContentType:] : 720 -> 728
~ -[QLItem(PreviewInfo) _getPreviewItemType] : 216 -> 224
~ -[QLItem(PreviewInfo) _getGeneratedItemType] : 148 -> 156
~ -[QLItem(PreviewInfo) _previewItemTypeForType:] : 296 -> 304
~ +[QLItem(PreviewInfo) _previewExtensionKindForContentType:firstPartyExtension:] : 176 -> 184
~ -[QLItem(PreviewInfo) previewExtensionTypeToUse] : 256 -> 272
~ -[QLItem(PreviewInfo) useExtensionThumbnail] : 316 -> 332
~ -[QLItem(PreviewInfo) maxLoadingTime] : 108 -> 112
~ _QLPackageCopyFirstURLMatchingPrefix : 264 -> 272
~ -[QLItemViewController setAppearance:animated:] : 132 -> 140
~ -[QLItemViewController setContentFrame:] : 200 -> 204
~ -[QLItemViewController notifyDelegateWantsChromelessBars] : 280 -> 292
~ -[QLItemViewController navigationBarShouldBeChromeless] : 108 -> 112
~ -[QLItemViewController toolbarShouldBeChromeless] : 156 -> 164
~ -[QLItemViewController updateScrollViewContentOffset:withPreviousAppearance:] : 820 -> 860
~ -[QLItemViewController loadPreviewControllerIfNeededWithContents:context:completionHandler:] : 592 -> 588
~ -[QLItemViewController canToggleFullScreen] : 100 -> 108
~ -[QLItemViewController registeredKeyCommands] : 388 -> 416
~ -[QLItemViewController handlePerformedKeyCommandIfNeeded:] : 116 -> 124
~ -[QLItemViewController _scrollScrollViewByPercentualOffset:] : 412 -> 444
~ ___60-[QLItemViewController _scrollScrollViewByPercentualOffset:]_block_invoke : 128 -> 136
~ -[QLItemViewController notifyDelegatesDidFailWithError:] : 140 -> 148
~ -[QLItemViewController draggableViewShouldStartDragSession:] : 100 -> 108
~ -[QLItemViewController _addDragInteractionIfNeeded] : 136 -> 140
~ -[QLItemViewController dragInteraction:itemsForBeginningSession:] : 464 -> 508
~ -[QLItemViewController _dragInteraction:dataOwnerForSession:] : 64 -> 68
~ -[QLItemViewController editedCopyToSaveChangesWithOutputType:completionHandler:] : 276 -> 272
~ ___80-[QLItemViewController editedCopyToSaveChangesWithOutputType:completionHandler:]_block_invoke : 656 -> 676
~ ___80-[QLItemViewController editedCopyToSaveChangesWithOutputType:completionHandler:]_block_invoke_2 : 232 -> 216
~ ___80-[QLItemViewController editedCopyToSaveChangesWithOutputType:completionHandler:]_block_invoke_3 : 296 -> 284
~ ___80-[QLItemViewController editedCopyToSaveChangesWithOutputType:completionHandler:]_block_invoke_4 : 240 -> 248
~ ___80-[QLItemViewController editedCopyToSaveChangesWithOutputType:completionHandler:]_block_invoke_5 : 112 -> 116
~ ___64-[QLItemViewController showSaveEditsProgressIndicatorAfterDelay]_block_invoke : 596 -> 632
~ -[QLItemViewController saveEditsQueue] : 116 -> 128
~ -[QLItemViewController updateInterfaceForSavingEdits] : 68 -> 72
~ -[QLItemViewController updateInterfaceAfterSavingEdits] : 68 -> 72
~ -[QLItemViewController description] : 164 -> 176
~ -[QLItemViewController additionalItemViewControllerDescription] : 108 -> 116
~ -[QLItemViewController setDragInteraction:] : 20 -> 80
~ -[QLItemViewController setSaveEditProgressView:] : 20 -> 80
~ -[QLItemViewController setSaveEditsQueue:] : 20 -> 80
~ -[QLPreviewContext isEqual:] : 972 -> 1056
~ -[QLPreviewContext encodeWithCoder:] : 988 -> 1080
~ -[QLPreviewContext initWithCoder:] : 840 -> 896
~ -[QLCustomMessageForwarder initWithPreviewDelegate:] : 116 -> 108
~ -[QLCustomItemViewController dismissPreviewController] : 64 -> 68
~ -[QLCustomItemViewController setFullScreen:] : 80 -> 84
~ ___69-[QLCustomItemViewController forwardMessageToHost:completionHandler:]_block_invoke_2 : 208 -> 196
~ -[QLCustomItemViewController setAppearance:animated:] : 140 -> 144
~ ___58-[QLCustomItemViewController getFrameWithCompletionBlock:]_block_invoke : 288 -> 296
~ _RTFGeneratePreviewForURL : 540 -> 544
~ _RTFGeneratePreviewForAttributedString : 444 -> 460
~ -[QLSingleItemThumbnailGenerator thumbnailGenerator] : 140 -> 144
~ -[QLSingleItemThumbnailGenerator _thumbnailVersionForItem:completionBlock:] : 516 -> 540
~ ___75-[QLSingleItemThumbnailGenerator _thumbnailVersionForItem:completionBlock:]_block_invoke : 564 -> 560
~ -[QLSingleItemThumbnailGenerator generateThumbnailWithSize:contentMode:completionBlock:] : 336 -> 320
~ ___88-[QLSingleItemThumbnailGenerator generateThumbnailWithSize:contentMode:completionBlock:]_block_invoke : 244 -> 256
~ -[QLSingleItemThumbnailGenerator _generateUncachedThumbnailWithSize:contentMode:thumbnailVersion:completionBlock:] : 344 -> 340
~ -[QLSingleItemThumbnailGenerator genericIconWithSize:] : 684 -> 724
~ -[QLSingleItemThumbnailGenerator initWithCoder:] : 164 -> 168
~ -[QLSingleItemThumbnailGenerator setThumbnailGenerator:] : 12 -> 64
~ +[UIColor(_QLUtilities) _ql_markupBackgroundColor] : 68 -> 84
~ ___50+[UIColor(_QLUtilities) _ql_markupBackgroundColor]_block_invoke : 292 -> 316
~ _OIGenerateAtomicPreviewForURL : 344 -> 348
~ _QLOfficeCalculatePreview : 1312 -> 1364
~ _OIGeneratePreviewForURLIfWrongContent : 656 -> 676
~ _OIGenerateAtomicPreviewForData : 408 -> 416
~ _OIGeneratePreviewForDataIfWrongContent : 616 -> 620
~ __QLGetOfficeFileTypeFromUTI : 556 -> 560
~ __QLRemoveSpaces : 156 -> 168
~ _QLTypeCopyUTIForURLAndMimeType : 448 -> 464
~ __QLTypeCopyUTIForFileNameAndMimeType : 960 -> 968
~ _QLTypeCopyBestMimeTypeForFileNameAndMimeType : 272 -> 268
~ __QLTypeCopyBestMimeTypeForUTI : 332 -> 348
~ _QLTypeCopyBestMimeTypeForURLAndMimeType : 304 -> 300
~ __QLUTIIsScriptableMediaType : 124 -> 128
~ __QLCopyArchiveExtensionIfIsArchiveFileName : 132 -> 140
~ __QLCopyPackageExtensionIfIsArchiveFileName : 272 -> 288
~ __QLTypeCopyPrivateUTIFromFileNameAndMimeType : 348 -> 384
~ __QLToolsGetKnownUTIs : 68 -> 84
~ ____QLToolsGetKnownUTIs_block_invoke : 160 -> 168
~ __QLGetMimeTypeForContentType : 148 -> 164
~ __QLTypeGetKnownExtensions : 68 -> 84
~ ____QLTypeGetKnownExtensions_block_invoke : 172 -> 184
~ __QLTypeGetKnownMimeTypes : 68 -> 84
~ ____QLTypeGetKnownMimeTypes_block_invoke : 172 -> 184
~ __QLContentTypeConformsToContentTypeInSet : 244 -> 236
~ -[QLImageItemContents initWithImage:] : 124 -> 116
~ -[QLImageItemContents initWithCoder:] : 140 -> 144
~ +[QLImageItemURLContents imageItemContentsWithImage:imageURL:] : 124 -> 120
~ -[QLImageItemURLContents encodeWithCoder:] : 32 -> 24
~ -[QLImageItemURLContents initWithCoder:] : 152 -> 148
~ -[QLImageItemURLContents imageURL] : 16 -> 8
~ -[QLImageItemURLContents setImageURL:] : 12 -> 8
~ -[QLImageItemURLContents .cxx_destruct] : 20 -> 12
~ +[QLImageItemDataContents imageItemContentsWithImage:imageData:] : 124 -> 120
~ -[QLImageItemDataContents encodeWithCoder:] : 32 -> 24
~ -[QLImageItemDataContents initWithCoder:] : 152 -> 148
~ -[QLImageItemDataContents imageData] : 16 -> 8
~ -[QLImageItemDataContents setImageData:] : 20 -> 64
~ -[QLImageItemDataContents .cxx_destruct] : 20 -> 12

```
