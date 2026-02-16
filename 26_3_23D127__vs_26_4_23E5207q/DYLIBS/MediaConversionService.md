## MediaConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService`

```diff

-832.0.107.0.0
-  __TEXT.__text: 0x1b534
-  __TEXT.__auth_stubs: 0x7a0
+840.1.220.0.0
+  __TEXT.__text: 0x1c0c0
+  __TEXT.__auth_stubs: 0x740
   __TEXT.__objc_methlist: 0x1b74
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x6ac
+  __TEXT.__gcc_except_tab: 0x5ec
   __TEXT.__cstring: 0x49cd
   __TEXT.__oslogstring: 0x23af
-  __TEXT.__unwind_info: 0x6b8
+  __TEXT.__unwind_info: 0x6d8
   __TEXT.__objc_classname: 0x452
   __TEXT.__objc_methname: 0x6194
   __TEXT.__objc_methtype: 0x9b5

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x4a8
-  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x2d00
   __AUTH_CONST.__objc_const: 0x2988

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 037B210C-3ABA-3B27-88F5-6BFBAFEF10E6
-  Functions: 610
-  Symbols:   2465
+  UUID: 7F89D9A2-8DBF-394A-8E20-2D40D3C6930C
+  Functions: 611
+  Symbols:   2459
   CStrings:  1934
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
Functions:
+ sub_2636d21d8
~ -[PAVideoConversionServiceClient requestStatusWithCompletionHandler:] : 200 -> 204
~ -[PAVideoConversionServiceClient invalidateAfterPendingRequestCompletion] : 136 -> 140
~ ___73-[PAVideoConversionServiceClient invalidateAfterPendingRequestCompletion]_block_invoke : 356 -> 360
~ -[PAVideoConversionServiceClient updateProgress:] : 264 -> 280
~ ___49-[PAVideoConversionServiceClient updateProgress:]_block_invoke : 164 -> 172
~ -[PAVideoConversionServiceClient transitionToInvalidatedState] : 112 -> 120
~ -[PAVideoConversionServiceClient handleRequestCompletionForIdentifier:] : 244 -> 252
~ -[PAVideoConversionServiceClient extractStillImageFromVideoAtSourceURL:toDestinationURL:options:completionHandler:] : 2216 -> 2264
~ ___115-[PAVideoConversionServiceClient extractStillImageFromVideoAtSourceURL:toDestinationURL:options:completionHandler:]_block_invoke : 332 -> 328
~ ___115-[PAVideoConversionServiceClient extractStillImageFromVideoAtSourceURL:toDestinationURL:options:completionHandler:]_block_invoke.102 : 416 -> 428
~ ___115-[PAVideoConversionServiceClient extractStillImageFromVideoAtSourceURL:toDestinationURL:options:completionHandler:]_block_invoke.103 : 352 -> 364
~ ___115-[PAVideoConversionServiceClient extractStillImageFromVideoAtSourceURL:toDestinationURL:options:completionHandler:]_block_invoke.104 : 488 -> 496
~ -[PAVideoConversionServiceClient modifyRequestWithIdentifier:modifications:] : 248 -> 252
~ -[PAVideoConversionServiceClient markPendingRequestAsOptionalForProgress:] : 316 -> 328
~ ___74-[PAVideoConversionServiceClient markPendingRequestAsOptionalForProgress:]_block_invoke : 440 -> 452
~ -[PAVideoConversionServiceClient canMarkPendingRequestAsOptionalForProgress:] : 84 -> 92
~ -[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:] : 2728 -> 2712
~ ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke : 332 -> 328
~ ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.86 : 332 -> 340
~ ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.90 : 392 -> 400
~ ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.92 : 364 -> 368
~ ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.95 : 384 -> 396
~ ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke_2 : 348 -> 352
~ ___121-[PAVideoConversionServiceClient convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke.93 : 208 -> 212
~ -[PAVideoConversionServiceClient convertVideoAtSourceURL:toDestinationURL:options:completionHandler:] : 320 -> 324
~ -[PAVideoConversionServiceClient setupServiceConnection] : 280 -> 304
~ -[PAVideoConversionServiceClient init] : 200 -> 208
~ -[PAVideoConversionServiceClient(UnitTestSupport) ut_invalidateServiceConnection] : 64 -> 68
~ _PAMediaConversionIsCancellationError : 108 -> 116
~ _PAMediaConversionJobPriorityIsBackground : 24 -> 16
~ -[PAImageConversionServiceClient requestStatusWithCompletionHandler:] : 200 -> 204
~ -[PAImageConversionServiceClient sendRequestWithOptions:sourceURLCollection:destinationURLCollection:jobIdentifier:attemptCount:completionHandler:] : 1112 -> 1020
~ ___147-[PAImageConversionServiceClient sendRequestWithOptions:sourceURLCollection:destinationURLCollection:jobIdentifier:attemptCount:completionHandler:]_block_invoke : 544 -> 552
~ ___147-[PAImageConversionServiceClient sendRequestWithOptions:sourceURLCollection:destinationURLCollection:jobIdentifier:attemptCount:completionHandler:]_block_invoke.96 : 884 -> 900
~ -[PAImageConversionServiceClient convertImageAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:] : 1768 -> 1836
~ ___121-[PAImageConversionServiceClient convertImageAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:]_block_invoke : 332 -> 328
~ -[PAImageConversionServiceClient convertImageAtSourceURL:options:completionHandler:] : 256 -> 260
~ -[PAImageConversionServiceClient setupServiceConnection] : 268 -> 284
~ -[PAImageConversionServiceClient dealloc] : 88 -> 92
~ -[PAMediaConversionServiceResourceURLReference dictionaryRepresentationWithError:] : 192 -> 200
~ -[PAMediaConversionServiceResourceURLReference dealloc] : 468 -> 480
~ -[PAMediaConversionServiceResourceURLReference hash] : 60 -> 64
~ -[PAMediaConversionServiceResourceURLReference isEqual:] : 116 -> 128
~ -[PAMediaConversionServiceResourceURLReference getPathHash:lastPathComponent:] : 216 -> 228
~ +[PAMediaConversionServiceResourceURLReference getPathHash:lastPathComponent:forDictionaryRepresentation:] : 444 -> 460
~ +[PAMediaConversionServiceResourceURLReference referenceWithDictionaryRepresentation:error:] : 424 -> 436
~ +[PAMediaConversionServiceResourceURLReference referenceWithURL:] : 184 -> 188
~ -[PAMediaConversionServiceResourceURLCollection copyURL:forRole:toDirectory:error:] : 320 -> 332
~ -[PAMediaConversionServiceResourceURLCollection urlForDebugDumpWithDirectoryName:inExistingParentDirectory:error:] : 1064 -> 1096
~ ___114-[PAMediaConversionServiceResourceURLCollection urlForDebugDumpWithDirectoryName:inExistingParentDirectory:error:]_block_invoke : 200 -> 208
~ ___71-[PAMediaConversionServiceResourceURLCollection enumerateResourceURLs:]_block_invoke : 132 -> 136
~ -[PAMediaConversionServiceResourceURLCollection enumerateResourceURLReferences:] : 360 -> 372
~ -[PAMediaConversionServiceResourceURLCollection fileSizeSummary] : 276 -> 288
~ ___64-[PAMediaConversionServiceResourceURLCollection fileSizeSummary]_block_invoke : 384 -> 396
~ -[PAMediaConversionServiceResourceURLCollection logMessageSummaryWithFullPath:] : 280 -> 292
~ ___79-[PAMediaConversionServiceResourceURLCollection logMessageSummaryWithFullPath:]_block_invoke : 268 -> 288
~ -[PAMediaConversionServiceResourceURLCollection allURLsAreReadable] : 236 -> 248
~ ___67-[PAMediaConversionServiceResourceURLCollection allURLsAreReadable]_block_invoke : 112 -> 116
~ -[PAMediaConversionServiceResourceURLCollection removeExistingEmptyFilesWithError:] : 376 -> 380
~ ___83-[PAMediaConversionServiceResourceURLCollection removeExistingEmptyFilesWithError:]_block_invoke : 544 -> 572
~ -[PAMediaConversionServiceResourceURLCollection ensureFilesExistWithError:] : 376 -> 380
~ ___75-[PAMediaConversionServiceResourceURLCollection ensureFilesExistWithError:]_block_invoke : 856 -> 900
~ -[PAMediaConversionServiceResourceURLCollection filenameExtensionAndPathHashForRole:] : 188 -> 200
~ -[PAMediaConversionServiceResourceURLCollection bookmarkDataDictionaryRepresentationWithError:] : 424 -> 428
~ ___95-[PAMediaConversionServiceResourceURLCollection bookmarkDataDictionaryRepresentationWithError:]_block_invoke : 332 -> 344
~ -[PAMediaConversionServiceResourceURLCollection typeIdentifierForResourceURLWithRole:] : 848 -> 884
~ -[PAMediaConversionServiceResourceURLCollection containsAnyRole:] : 376 -> 388
~ -[PAMediaConversionServiceResourceURLCollection containsAllRoles:] : 376 -> 388
~ -[PAMediaConversionServiceResourceURLCollection setShouldDeleteURLOnDeallocation:forRole:] : 204 -> 216
~ -[PAMediaConversionServiceResourceURLCollection resourceURLForRole:] : 268 -> 292
~ -[PAMediaConversionServiceResourceURLCollection setResourceURL:forRole:deleteOnDeallocation:] : 116 -> 120
~ -[PAMediaConversionServiceResourceURLCollection setResourceURL:forRole:] : 388 -> 408
~ -[PAMediaConversionServiceResourceURLCollection isEqual:] : 72 -> 76
~ -[PAMediaConversionServiceResourceURLCollection init] : 104 -> 108
~ +[PAMediaConversionServiceResourceURLCollection filenameSummaryStringForDictionaryRepresentation:] : 120 -> 132
~ +[PAMediaConversionServiceResourceURLCollection getSignatureString:filenameSummary:forDictionaryRepresentation:] : 652 -> 676
~ ___120+[PAMediaConversionServiceResourceURLCollection collectionForBookmarkDataDictionaryRepresentation:accessProvider:error:]_block_invoke : 344 -> 356
~ -[PAMediaConversionServiceResourceURLCollection(ResourceAccessControl) blastDoorError] : 76 -> 84
~ -[PAMediaConversionServiceResourceURLCollection(ResourceAccessControl) blastDoorSourceURL] : 76 -> 84
~ -[PAMediaConversionServiceResourceURLCollection(ResourceAccessControl) blastDoorVideoComplementProperties] : 140 -> 156
~ -[PAMediaConversionServiceResourceURLCollection(ResourceAccessControl) blastDoorMainSourceProperties] : 76 -> 84
~ -[PAMediaConversionServiceResourceURLCollection(ResourceAccessControl) isBlastDoorAccessRequired] : 56 -> 60
~ -[PHMediaFormatConversionContent description] : 172 -> 188
~ -[PHMediaFormatConversionContent fileSignature] : 464 -> 472
~ -[PHMediaFormatConversionContent fileType] : 80 -> 88
~ -[PHMediaFormatConversionContent typeFromFileExtensionWithError:] : 468 -> 488
~ -[PHMediaFormatConversionContent length] : 172 -> 188
~ -[PHMediaFormatConversionSource .cxx_destruct] : 124 -> 92
~ -[PHMediaFormatConversionSource setDidCheckForIsHDR:] : 16 -> 8
~ -[PHMediaFormatConversionSource didCheckForIsHDR] : 16 -> 8
~ -[PHMediaFormatConversionSource setIsHDR:] : 16 -> 8
~ -[PHMediaFormatConversionSource isHDR] : 16 -> 8
~ -[PHMediaFormatConversionSource transcodingEligibleVideoTrackFormatDescription] : 16 -> 8
~ -[PHMediaFormatConversionSource setAccessibilityDescriptionMetadataStatus:] : 16 -> 8
~ -[PHMediaFormatConversionSource accessibilityDescriptionMetadataStatus] : 16 -> 8
~ -[PHMediaFormatConversionSource setCaptionMetadataStatus:] : 16 -> 8
~ -[PHMediaFormatConversionSource captionMetadataStatus] : 16 -> 8
~ -[PHMediaFormatConversionSource setLocationMetadataStatus:] : 16 -> 8
~ -[PHMediaFormatConversionSource locationMetadataStatus] : 16 -> 8
~ -[PHMediaFormatConversionSource setDidCheckForVideoWithFormatEligibleForTranscoding:] : 16 -> 8
~ -[PHMediaFormatConversionSource didCheckForVideoWithFormatEligibleForTranscoding] : 20 -> 12
~ -[PHMediaFormatConversionSource setDidCheckForLivePhotoPairingIdentifier:] : 16 -> 8
~ -[PHMediaFormatConversionSource didCheckForLivePhotoPairingIdentifier] : 20 -> 12
~ -[PHMediaFormatConversionSource setLivePhotoPairingIdentifier:] : 20 -> 64
~ -[PHMediaFormatConversionSource containsHEIFImage] : 16 -> 8
~ -[PHMediaFormatConversionSource containsImageWithFormatEligibleForTranscoding] : 16 -> 8
~ -[PHMediaFormatConversionSource containsProResVideoWithFormatEligibleForTranscoding] : 16 -> 8
~ -[PHMediaFormatConversionSource setContainsVideoWithFormatEligibleForTranscoding:] : 16 -> 8
~ -[PHMediaFormatConversionSource containsVideoWithFormatEligibleForTranscoding] : 16 -> 8
~ -[PHMediaFormatConversionSource setFirstVideoTrackCodec:] : 16 -> 8
~ -[PHMediaFormatConversionSource firstVideoTrackCodec] : 16 -> 8
~ -[PHMediaFormatConversionSource setPreflighted:] : 16 -> 8
~ -[PHMediaFormatConversionSource preflighted] : 20 -> 12
~ -[PHMediaFormatConversionSource setImageDimensions:] : 64 -> 56
~ -[PHMediaFormatConversionSource imageDimensions] : 68 -> 60
~ -[PHMediaFormatConversionSource setRenderOriginatingSignature:] : 12 -> 8
~ -[PHMediaFormatConversionSource renderOriginatingSignature] : 16 -> 12
~ -[PHMediaFormatConversionSource setMetadata:] : 20 -> 64
~ -[PHMediaFormatConversionSource livePhotoPairingIdentifier] : 176 -> 184
~ -[PHMediaFormatConversionSource markAccessibilityDescriptionMetadataAsCheckedWithStatus:] : 16 -> 8
~ -[PHMediaFormatConversionSource sourceAccessibilityDescriptionMetadataStatus] : 88 -> 96
~ -[PHMediaFormatConversionSource checkForAccessibilityDescriptionData] : 240 -> 236
~ -[PHMediaFormatConversionSource markCaptionMetadataAsCheckedWithStatus:] : 16 -> 8
~ -[PHMediaFormatConversionSource sourceCaptionMetadataStatus] : 88 -> 96
~ -[PHMediaFormatConversionSource checkForCaptionData] : 240 -> 236
~ -[PHMediaFormatConversionSource markLocationMetadataAsCheckedWithStatus:] : 16 -> 8
~ -[PHMediaFormatConversionSource sourceLocationMetadataStatus] : 88 -> 96
~ -[PHMediaFormatConversionSource checkForLocationData] : 240 -> 236
~ -[PHMediaFormatConversionSource metadata] : 148 -> 152
~ -[PHMediaFormatConversionSource checkForLivePhotoPairingIdentifier] : 372 -> 388
~ -[PHMediaFormatConversionSource markLivePhotoPairingIdentifierAsCheckedWithValue:] : 92 -> 96
~ -[PHMediaFormatConversionSource preflightWithError:] : 252 -> 256
~ -[PHMediaFormatConversionSource checkForImageEligibleForTranscoding] : 504 -> 500
~ -[PHMediaFormatConversionSource markIsHDRAsCheckedWithValue:] : 32 -> 16
~ -[PHMediaFormatConversionSource checkForIsHDR] : 292 -> 252
~ -[PHMediaFormatConversionSource containsHEVCVideo] : 124 -> 120
~ -[PHMediaFormatConversionSource markContainsVideoEligibleForTranscodingAsCheckedWithValue:codec:isProRes:] : 56 -> 24
~ -[PHMediaFormatConversionSource checkForVideoEligibleForTranscoding] : 372 -> 344
~ -[PHMediaFormatConversionSource determineMediaTypeFromPathExtensionWithError:] : 436 -> 452
~ -[PHMediaFormatConversionRequest updateSinglePassVideoConversionStatus:addedRange:error:] : 420 -> 428
~ -[PHMediaFormatConversionRequest enableSinglePassVideoEncodingWithUpdateHandler:] : 196 -> 200
~ -[PHMediaFormatConversionRequest didFinishProcessing] : 204 -> 216
~ -[PHMediaFormatConversionRequest padOutputFileToEstimatedLength] : 492 -> 520
~ -[PHMediaFormatConversionRequest formatConversionExpansionFactor] : 588 -> 616
~ -[PHMediaFormatConversionRequest estimatedOutputFileLength] : 160 -> 168
~ -[PHMediaFormatConversionRequest outputFileType] : 628 -> 680
~ -[PHMediaFormatConversionRequest outputPathExtension] : 580 -> 624
~ -[PHMediaFormatConversionRequest _isKnownUTTypeForPathExtension:] : 64 -> 68
~ -[PHMediaFormatConversionRequest setAccessibilityDescriptionMetadataBehavior:withAccessibilityDescription:] : 228 -> 224
~ -[PHMediaFormatConversionRequest setCaptionMetadataBehavior:withCaption:] : 228 -> 224
~ -[PHMediaFormatConversionRequest setCreationDateMetadataBehavior:withCreationDate:inTimeZone:] : 340 -> 352
~ -[PHMediaFormatConversionRequest setLocationMetadataBehavior:withLocation:] : 228 -> 232
~ -[PHMediaFormatConversionRequest destinationCapabilitiesHintsIndicateSupportForSource] : 720 -> 748
~ -[PHMediaFormatConversionRequest _calculateRequiresFormatConversion] : 1152 -> 1216
~ -[PHMediaFormatConversionRequest requiresAccessibilityDescriptionMetadataChange] : 148 -> 156
~ -[PHMediaFormatConversionRequest requiresCaptionMetadataChange] : 148 -> 156
~ -[PHMediaFormatConversionRequest requiresCreationDateMetadataChange] : 80 -> 84
~ -[PHMediaFormatConversionRequest requiresLocationMetadataChange] : 148 -> 156
~ -[PHMediaFormatConversionRequest requiresLivePhotoPairingIdentifierChange] : 308 -> 328
~ -[PHMediaFormatConversionRequest requiresMetadataChanges] : 148 -> 156
~ -[PHMediaFormatConversionRequest sourceSupportsPassthroughConversion] : 404 -> 420
~ -[PHMediaFormatConversionRequest backwardsCompatibilityStatus] : 88 -> 92
~ -[PHMediaFormatConversionRequest preflightWithConversionManager:] : 1064 -> 1124
~ -[PHMediaFormatConversionRequest markAsCancelled] : 116 -> 120
~ -[PHMediaFormatConversionRequest setupProgress] : 76 -> 80
~ -[PHMediaFormatConversionRequest description] : 276 -> 308
~ -[PHMediaFormatConversionRequest setDestination:] : 148 -> 152
~ -[PHMediaFormatConversionRequest init] : 304 -> 316
~ +[PHMediaFormatConversionRequest requestForSource:destinationCapabilities:error:] : 288 -> 296
~ +[PHMediaFormatConversionSource sourceForFileURL:] : 216 -> 236
~ -[PHMediaFormatAssetBundleConversionRequest .cxx_destruct] : 20 -> 12
~ -[PHMediaFormatAssetBundleConversionRequest setSubrequests:] : 12 -> 8
~ -[PHMediaFormatAssetBundleConversionRequest subrequests] : 16 -> 12
~ -[PHMediaFormatAssetBundleConversionRequest outputFileType] : 248 -> 268
~ -[PHMediaFormatAssetBundleConversionRequest outputPathExtension] : 264 -> 288
~ -[PHMediaFormatAssetBundleConversionRequest requiresFormatConversion] : 116 -> 120
~ -[PHMediaFormatAssetBundleConversionRequest enumerateSubrequests:] : 276 -> 280
~ -[PHMediaFormatAssetBundleConversionRequest enqueueSubrequestsOnConversionManager:] : 368 -> 372
~ -[PHMediaFormatAssetBundleConversionRequest prepareWithError:] : 312 -> 328
~ -[PHMediaFormatConversionCompositeRequest setupProgress] : 176 -> 180
~ ___56-[PHMediaFormatConversionCompositeRequest setupProgress]_block_invoke : 140 -> 144
~ -[PHMediaFormatConversionCompositeRequest didFinishProcessing] : 300 -> 304
~ ___62-[PHMediaFormatConversionCompositeRequest didFinishProcessing]_block_invoke : 340 -> 356
~ ___79-[PHMediaFormatConversionCompositeRequest propagateRequestOptionsToSubrequests]_block_invoke : 416 -> 448
~ -[PHMediaFormatConversionCompositeRequest enumerateSubrequests:] : 112 -> 116
~ -[PHMediaFormatConversionCompositeRequest enqueueSubrequestsOnConversionManager:] : 112 -> 116
~ -[PHMediaFormatConversionCompositeRequest compositeRequestCommonInitWithError:] : 76 -> 80
~ -[PHMediaFormatConversionCompositeRequest preflightWithConversionManager:] : 376 -> 384
~ ___74-[PHMediaFormatConversionCompositeRequest preflightWithConversionManager:]_block_invoke : 88 -> 96
~ +[PHMediaFormatConversionAssetBundleSource sourceForFileURL:] : 260 -> 280
~ +[PHMediaFormatConversionSource sourceForFileURL:mediaType:imageDimensions:] : 236 -> 240
~ -[PHMediaFormatLivePhotoBundleConversionRequest .cxx_destruct] : 20 -> 12
~ -[PHMediaFormatLivePhotoBundleConversionRequest setLivePhotoConversionRequest:] : 12 -> 8
~ -[PHMediaFormatLivePhotoBundleConversionRequest livePhotoConversionRequest] : 16 -> 12
~ -[PHMediaFormatLivePhotoBundleConversionRequest postProcessSuccessfulCompositeRequest] : 1032 -> 1092
~ ___86-[PHMediaFormatLivePhotoBundleConversionRequest postProcessSuccessfulCompositeRequest]_block_invoke : 232 -> 240
~ -[PHMediaFormatConversionDestination .cxx_destruct] : 144 -> 104
~ -[PHMediaFormatConversionDestination setSinglePassVideoConversionTargetLength:] : 16 -> 8
~ -[PHMediaFormatConversionDestination singlePassVideoConversionTargetLength] : 16 -> 8
~ -[PHMediaFormatConversionDestination setOutputPathExtension:] : 12 -> 8
~ -[PHMediaFormatConversionDestination outputPathExtension] : 16 -> 12
~ -[PHMediaFormatConversionDestination setSinglePassVideoExportRangeCoordinator:] : 12 -> 8
~ -[PHMediaFormatConversionDestination singlePassVideoExportRangeCoordinator] : 16 -> 12
~ -[PHMediaFormatConversionDestination errorForSinglePassVideoConversionError:] : 308 -> 320
~ -[PHMediaFormatConversionDestination waitForAvailabilityOfRange:timeout:error:] : 244 -> 240
~ -[PHMediaFormatConversionDestination addAvailableRange:] : 188 -> 180
~ -[PHMediaFormatConversionDestination usesSinglePassVideoConversion] : 24 -> 16
~ -[PHMediaFormatConversionDestination enableSinglePassVideoConversionWithTargetLength:] : 88 -> 72
~ -[PHMediaFormatConversionDestination padImageToLength:fileHandle:error:] : 216 -> 224
~ -[PHMediaFormatConversionDestination padVideoToLength:fileHandle:error:] : 336 -> 344
~ -[PHMediaFormatConversionDestination padToLength:error:] : 512 -> 524
~ -[PHMediaFormatConversionDestination dealloc] : 96 -> 88
~ -[PHMediaFormatConversionDestination removeTemporaryFiles] : 780 -> 788
~ -[PHMediaFormatConversionDestination createTemporaryOutputDirectoryWithError:] : 504 -> 512
~ -[PHMediaFormatConversionDestination generateTemporaryOutputFileURLForRequest:] : 752 -> 804
~ +[PHMediaFormatConversionDestination sharedCleanupQueue] : 84 -> 100
~ +[PHMediaFormatConversionDestination destinationForConversionReturningUnchangedSource:] : 132 -> 136
~ -[PHMediaFormatLivePhotoBundleConversionRequest enumerateSubrequests:] : 116 -> 112
~ -[PHMediaFormatLivePhotoBundleConversionRequest enqueueSubrequestsOnConversionManager:] : 176 -> 180
~ ___87-[PHMediaFormatLivePhotoBundleConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke : 180 -> 184
~ -[PHMediaFormatLivePhotoBundleConversionRequest prepareWithError:] : 1164 -> 1232
~ -[PHMediaFormatLivePhotoConversionRequest .cxx_destruct] : 84 -> 68
~ -[PHMediaFormatLivePhotoConversionRequest setVideoConversionRequest:] : 12 -> 8
~ -[PHMediaFormatLivePhotoConversionRequest videoConversionRequest] : 16 -> 12
~ -[PHMediaFormatLivePhotoConversionRequest setImageConversionRequest:] : 12 -> 8
~ -[PHMediaFormatLivePhotoConversionRequest imageConversionRequest] : 16 -> 12
~ -[PHMediaFormatLivePhotoConversionRequest didPreflightSubrequest:] : 308 -> 324
~ -[PHMediaFormatLivePhotoConversionRequest enumerateSubrequests:] : 152 -> 160
~ -[PHMediaFormatLivePhotoConversionRequest enqueueSubrequestsOnConversionManager:] : 276 -> 284
~ ___81-[PHMediaFormatLivePhotoConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke : 180 -> 184
~ ___81-[PHMediaFormatLivePhotoConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke.749 : 180 -> 184
~ +[PHMediaFormatLivePhotoConversionRequest requestForImageConversionRequest:videoConversionRequest:error:] : 552 -> 572
~ +[PHMediaFormatLivePhotoConversionRequest requestForSource:destinationCapabilities:error:] : 140 -> 148
~ +[PHMediaFormatConversionLivePhotoBundleSource sourceForFileURL:] : 260 -> 280
~ -[PHMediaFormatConversionPlaceholderSource .cxx_destruct] : 20 -> 12
~ -[PHMediaFormatConversionPlaceholderSource setFileType:] : 12 -> 8
~ -[PHMediaFormatConversionPlaceholderSource fileType] : 16 -> 8
~ -[PHMediaFormatConversionPlaceholderSource imageDimensions] : 144 -> 152
~ -[PHMediaFormatConversionPlaceholderSource length] : 136 -> 144
~ -[PHMediaFormatConversionPlaceholderSource fileURL] : 236 -> 264
~ -[PHMediaFormatConversionPlaceholderSource initWithFileType:mediaType:] : 216 -> 220
~ +[PHMediaFormatChainedConversionRequest chainedRequestForAdjustmentRenderRequest:dependingOnRequest:error:] : 236 -> 228
~ ___107+[PHMediaFormatChainedConversionRequest chainedRequestForAdjustmentRenderRequest:dependingOnRequest:error:]_block_invoke : 244 -> 256
~ +[PHMediaFormatChainedConversionRequest chainedRequestForRequest:dependingOnRequest:error:successUpdateHandler:] : 456 -> 464
~ +[PHMediaFormatChainedConversionRequest requestForSource:destinationCapabilities:error:] : 140 -> 148
~ -[PHMediaFormatChainedConversionRequest .cxx_destruct] : 104 -> 80
~ -[PHMediaFormatChainedConversionRequest setSuccessUpdateHandler:] : 12 -> 8
~ -[PHMediaFormatChainedConversionRequest successUpdateHandler] : 16 -> 12
~ -[PHMediaFormatChainedConversionRequest setDependentRequest:] : 12 -> 8
~ -[PHMediaFormatChainedConversionRequest dependentRequest] : 16 -> 12
~ -[PHMediaFormatChainedConversionRequest setIndependentRequest:] : 12 -> 8
~ -[PHMediaFormatChainedConversionRequest independentRequest] : 16 -> 12
~ -[PHMediaFormatChainedConversionRequest postProcessSuccessfulCompositeRequest] : 100 -> 108
~ -[PHMediaFormatChainedConversionRequest enumerateSubrequests:] : 152 -> 160
~ -[PHMediaFormatChainedConversionRequest enqueueSubrequestsOnConversionManager:] : 268 -> 276
~ ___79-[PHMediaFormatChainedConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke : 388 -> 408
~ ___79-[PHMediaFormatChainedConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke.805 : 180 -> 184
~ -[PHMediaFormatConversionJob description] : 172 -> 188
~ -[PHMediaFormatConversionManager ut_objectsToBeDeallocatedWithReceiver] : 136 -> 148
~ -[PHMediaFormatConversionManager invalidate] : 148 -> 152
~ ___44-[PHMediaFormatConversionManager invalidate]_block_invoke : 456 -> 480
~ ___62-[PHMediaFormatConversionManager cancellationRequestedForJob:]_block_invoke : 308 -> 328
~ -[PHMediaFormatConversionManager jobForConversionRequest:completionHandler:] : 424 -> 420
~ -[PHMediaFormatConversionManager rootAncestorRequestForRequest:] : 128 -> 140
~ -[PHMediaFormatConversionManager preflightAllRelatedRequestsForCurrentJob] : 240 -> 244
~ ___74-[PHMediaFormatConversionManager preflightAllRelatedRequestsForCurrentJob]_block_invoke : 196 -> 208
~ ___74-[PHMediaFormatConversionManager preflightAllRelatedRequestsForCurrentJob]_block_invoke_2 : 492 -> 528
~ -[PHMediaFormatConversionManager validateLivePhotoPairingIdentifierConfigurationForRequest:] : 180 -> 196
~ -[PHMediaFormatConversionManager performConversionRequest:completionHandler:] : 760 -> 800
~ -[PHMediaFormatConversionManager processQueuedJobs] : 876 -> 928
~ ___51-[PHMediaFormatConversionManager processQueuedJobs]_block_invoke : 500 -> 520
~ ___51-[PHMediaFormatConversionManager processQueuedJobs]_block_invoke.871 : 216 -> 224
~ ___51-[PHMediaFormatConversionManager processQueuedJobs]_block_invoke_2 : 220 -> 232
~ -[PHMediaFormatConversionManager setDirectoryForTemporaryFiles:] : 408 -> 364
~ -[PHMediaFormatConversionManager configureTransferBehaviorUserPreferenceForRequest:] : 268 -> 272
~ -[PHMediaFormatConversionManager preflightConversionRequest:completionHandler:] : 216 -> 208
~ ___79-[PHMediaFormatConversionManager preflightConversionRequest:completionHandler:]_block_invoke : 96 -> 100
~ -[PHMediaFormatConversionManager preflightConversionRequest:] : 104 -> 108
~ -[PHMediaFormatConversionManager enqueueConversionRequest:completionHandler:] : 756 -> 768
~ ___77-[PHMediaFormatConversionManager enqueueConversionRequest:completionHandler:]_block_invoke : 448 -> 472
~ -[PHMediaFormatConversionManager init] : 268 -> 280
~ -[PHMediaFormatConversionImplementation_MediaConversionService performImageConversionRequest:completionHandler:] : 2392 -> 2588
~ ___112-[PHMediaFormatConversionImplementation_MediaConversionService performImageConversionRequest:completionHandler:]_block_invoke : 272 -> 268
~ -[PHMediaFormatConversionImplementation_MediaConversionService applyCommonOptionsFromVideoRequest:toOptions:] : 1328 -> 1428
~ -[PHMediaFormatConversionImplementation_MediaConversionService submitSinglePassVideoConversionRequest:destination:completionHandler:] : 720 -> 744
~ ___133-[PHMediaFormatConversionImplementation_MediaConversionService submitSinglePassVideoConversionRequest:destination:completionHandler:]_block_invoke : 396 -> 404
~ -[PHMediaFormatConversionImplementation_MediaConversionService submitNonSinglePassVideoConversionRequest:destination:completionHandler:] : 648 -> 660
~ ___136-[PHMediaFormatConversionImplementation_MediaConversionService submitNonSinglePassVideoConversionRequest:destination:completionHandler:]_block_invoke : 400 -> 408
~ -[PHMediaFormatConversionImplementation_MediaConversionService performVideoConversionRequest:completionHandler:] : 544 -> 552
~ -[PHMediaFormatConversionImplementation_MediaConversionService performConversionRequest:completionHandler:] : 404 -> 420
~ -[PHMediaFormatConversionImplementation_MediaConversionService transferBehaviorUserPreference] : 276 -> 280
~ -[PHMediaFormatConversionSinglePassVideoProgressObserver observeValueForKeyPath:ofObject:change:context:] : 628 -> 644
~ -[PHMediaFormatConversionSinglePassVideoProgressObserver startObservingProgress:forRequest:] : 564 -> 600
~ +[PAMediaConversionServiceImagingUtilities _generatePosterFrameExportForVideoURL:imageDestinationToAddToAndFinalize:maximumSize:error:] : 508 -> 524
~ +[PAMediaConversionServiceImagingUtilities generatePosterFrameExportForVideoURL:outputData:maximumSize:outputFileType:error:] : 460 -> 468
~ +[PAMediaConversionServiceImagingUtilities primaryImagePropertiesForFileAtURL:] : 340 -> 344
~ +[PAMediaConversionServiceImagingUtilities logMissingPropertiesInCMPhotoOutputData:comparedToProcessedSourceImagePropertiesByIndex:] : 836 -> 848
~ +[PAMediaConversionServiceImagingUtilities dataForSingleImageJPEGPassthroughConversionForImageSource:primaryImageProperties:] : 392 -> 400
~ +[PAMediaConversionServiceImagingUtilities imageDataForPassthroughConversionForSourceURL:metadataPolicy:outResultImageSize:] : 1016 -> 1028
~ ___124+[PAMediaConversionServiceImagingUtilities imageDataForPassthroughConversionForSourceURL:metadataPolicy:outResultImageSize:]_block_invoke : 172 -> 180
~ +[PAMediaConversionServiceImagingUtilities imagePropertiesByImageIndexInImageSource:processedWithMetadataPolicy:] : 252 -> 264
~ -[ConversionOptionSet photosAdjustmentsDictionaryForAdjustmentsFileAtPath:] : 468 -> 488
~ -[MediaConversionServiceCommandLineDriver waitForSigInt] : 368 -> 372
~ -[MediaConversionServiceCommandLineDriver observeValueForKeyPath:ofObject:change:context:] : 172 -> 164
~ -[MediaConversionServiceCommandLineDriver runVideoStillExtractionConversionWithConversionOptionSet:] : 576 -> 596
~ ___100-[MediaConversionServiceCommandLineDriver runVideoStillExtractionConversionWithConversionOptionSet:]_block_invoke : 240 -> 236
~ -[MediaConversionServiceCommandLineDriver runVideoConversionWithConversionOptionSet:] : 816 -> 848
~ ___85-[MediaConversionServiceCommandLineDriver runVideoConversionWithConversionOptionSet:]_block_invoke : 240 -> 236
~ -[MediaConversionServiceCommandLineDriver runImageConversionWithConversionOptionSet:] : 660 -> 712
~ ___69-[MediaConversionServiceCommandLineDriver sendMessageToLaunchService]_block_invoke : 160 -> 164
~ ___69-[MediaConversionServiceCommandLineDriver sendMessageToLaunchService]_block_invoke_2 : 160 -> 164
~ -[MediaConversionServiceCommandLineDriver run] : 624 -> 632
~ -[MediaConversionServiceCommandLineDriver hasConversionOfType:] : 300 -> 304
~ -[MediaConversionServiceCommandLineDriver processOption:arg:] : 636 -> 644
~ -[MediaConversionServiceCommandLineDriver init] : 188 -> 192
~ +[MediaConversionServiceCommandLineDriver outputConversionError:status:] : 284 -> 292
~ +[MediaConversionServiceCommandLineDriver replacementObjectForObject:valueConversionHandler:] : 776 -> 784
~ ___93+[MediaConversionServiceCommandLineDriver replacementObjectForObject:valueConversionHandler:]_block_invoke : 136 -> 140
~ +[MediaConversionServiceCommandLineDriver outputJSONDataForConversionOutputInformation:] : 328 -> 336
~ ___88+[MediaConversionServiceCommandLineDriver outputJSONDataForConversionOutputInformation:]_block_invoke : 160 -> 168
~ +[MediaConversionServiceCommandLineDriver usagesummary] : 136 -> 148
~ +[MediaConversionServiceCommandLineDriver usage] : 120 -> 128
~ -[ConversionOptionSet pfVideoAdjustmentsDictionaryForString:] : 544 -> 580
~ -[ConversionOptionSet photosAdjustmentsDictionaryForString:] : 496 -> 532
~ -[ConversionOptionSet cmTimeRangeDictionaryForString:] : 544 -> 572
~ -[ConversionOptionSet metadataPolicyForString:] : 368 -> 400
~ -[ConversionOptionSet arrayOfStringsForString:] : 248 -> 268
~ -[ConversionOptionSet conversionOptionValueForString:valueType:] : 504 -> 460
~ -[ConversionOptionSet scaleFactorForInputSize:sharedStreamsSizeSpecificationString:] : 320 -> 340
~ -[ConversionOptionSet processConversionOptionKey:valueString:] : 696 -> 712
~ ___62-[ConversionOptionSet processConversionOptionKey:valueString:]_block_invoke : 20 -> 68
~ -[ConversionOptionSet presetNameToOptionsMappingForVideoTranscoding] : 1400 -> 1492
~ -[ConversionOptionSet presetListForMapping:] : 88 -> 96
~ -[ConversionOptionSet checkDestinationExists] : 536 -> 544
~ -[ConversionOptionSet validateAndProcess] : 1132 -> 1180
~ -[ConversionOptionSet init] : 112 -> 116
~ +[ConversionOptionSet sizeForImageAtPath:] : 180 -> 196
~ +[ConversionOptionSet knownConversionTypes] : 144 -> 148

```
