## MediaAnalysisServices

> `/System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices`

```diff

-405.3.1.0.0
-  __TEXT.__text: 0x3d088
-  __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x4c9c
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x366c
-  __TEXT.__gcc_except_tab: 0x4834
-  __TEXT.__oslogstring: 0x2349
+435.60.2.11.2
+  __TEXT.__text: 0x3deb0
+  __TEXT.__objc_methlist: 0x4f78
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x3c78
+  __TEXT.__gcc_except_tab: 0x4578
+  __TEXT.__oslogstring: 0x2326
   __TEXT.__dlopen_cstrs: 0x417
-  __TEXT.__unwind_info: 0x1c08
-  __TEXT.__objc_classname: 0xea5
-  __TEXT.__objc_methname: 0x8416
-  __TEXT.__objc_methtype: 0x2404
-  __TEXT.__objc_stubs: 0x2720
-  __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__const: 0xae0
-  __DATA_CONST.__objc_classlist: 0x410
+  __TEXT.__unwind_info: 0x1c58
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xa70
+  __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1818
+  __DATA_CONST.__objc_selrefs: 0x1988
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x3d8
-  __AUTH_CONST.__auth_got: 0x488
+  __DATA_CONST.__objc_superrefs: 0x3f0
+  __DATA_CONST.__got: 0x518
   __AUTH_CONST.__const: 0x318
-  __AUTH_CONST.__cfstring: 0x4b40
-  __AUTH_CONST.__objc_const: 0x9c98
+  __AUTH_CONST.__cfstring: 0x4e40
+  __AUTH_CONST.__objc_const: 0xa210
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x12c0
-  __DATA.__objc_ivar: 0x564
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x1360
+  __DATA.__objc_ivar: 0x5a0
   __DATA.__data: 0x420
   __DATA.__bss: 0x90
-  __DATA_DIRTY.__objc_data: 0x15e0
+  __DATA_DIRTY.__objc_data: 0x1680
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
+  - /System/Library/PrivateFrameworks/EmbeddingCore.framework/EmbeddingCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 018C2F4C-704B-310B-83FF-474D3742AEFF
-  Functions: 1649
-  Symbols:   5950
-  CStrings:  3134
+  UUID: A9B13D2F-9965-38B8-8F71-9A9A6356066A
+  Functions: 1732
+  Symbols:   6178
+  CStrings:  1506
 
Symbols:
+ +[MADCrossEncoderSimilarityRequest supportsSecureCoding]
+ +[MADCrossEncoderSimilarityResult supportsSecureCoding]
+ +[MADVideoSessionHomeVisionRequest supportsSecureCoding]
+ -[MADCoreMLResult initWithVisionResults:].cold.1
+ -[MADCrossEncoderSimilarityRequest .cxx_destruct]
+ -[MADCrossEncoderSimilarityRequest chunkOverlap]
+ -[MADCrossEncoderSimilarityRequest description]
+ -[MADCrossEncoderSimilarityRequest documents]
+ -[MADCrossEncoderSimilarityRequest encodeWithCoder:]
+ -[MADCrossEncoderSimilarityRequest extendedContextLength]
+ -[MADCrossEncoderSimilarityRequest initWithCoder:]
+ -[MADCrossEncoderSimilarityRequest initWithDocuments:]
+ -[MADCrossEncoderSimilarityRequest init]
+ -[MADCrossEncoderSimilarityRequest maxNumChunks]
+ -[MADCrossEncoderSimilarityRequest requireWeights]
+ -[MADCrossEncoderSimilarityRequest setChunkOverlap:]
+ -[MADCrossEncoderSimilarityRequest setExtendedContextLength:]
+ -[MADCrossEncoderSimilarityRequest setMaxNumChunks:]
+ -[MADCrossEncoderSimilarityRequest setRequireWeights:]
+ -[MADCrossEncoderSimilarityRequest similarityResults]
+ -[MADCrossEncoderSimilarityResult .cxx_destruct]
+ -[MADCrossEncoderSimilarityResult crossEncoderOutputs]
+ -[MADCrossEncoderSimilarityResult description]
+ -[MADCrossEncoderSimilarityResult encodeWithCoder:]
+ -[MADCrossEncoderSimilarityResult error]
+ -[MADCrossEncoderSimilarityResult initWithCoder:]
+ -[MADCrossEncoderSimilarityResult initWithCrossEncoderOutputs:error:]
+ -[MADImageCaptionRequest .cxx_destruct]
+ -[MADImageCaptionRequest customizedPrompt]
+ -[MADImageCaptionRequest setCustomizedPrompt:]
+ -[MADImageEmbeddingRequest .cxx_destruct]
+ -[MADImageEmbeddingRequest embeddingSpaceDescriptor]
+ -[MADImageEmbeddingRequest setEmbeddingSpaceDescriptor:]
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.10
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.11
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.12
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.13
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.14
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.15
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.16
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.17
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.18
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.19
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.2
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.20
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.21
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.22
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.23
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.24
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.25
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.26
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.3
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.4
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.5
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.6
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.7
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.8
+ -[MADPixelBufferProcesser _configurePixelRotationSessionWithOrientation:].cold.9
+ -[MADPixelBufferProcesser _createPixelBuffer:width:height:format:].cold.1
+ -[MADPixelBufferProcesser _createPixelBuffer:width:height:format:].cold.2
+ -[MADService(Text) activeCrossEncoderVersionStrings:]
+ -[MADService(Text) activeTextEmbeddingVersions:]
+ -[MADTextEmbeddingRequest .cxx_destruct]
+ -[MADTextEmbeddingRequest allowPCC]
+ -[MADTextEmbeddingRequest computeLexiconSafety]
+ -[MADTextEmbeddingRequest embeddingSpaceDescriptor]
+ -[MADTextEmbeddingRequest independent]
+ -[MADTextEmbeddingRequest locale]
+ -[MADTextEmbeddingRequest setAllowPCC:]
+ -[MADTextEmbeddingRequest setComputeLexiconSafety:]
+ -[MADTextEmbeddingRequest setEmbeddingSpaceDescriptor:]
+ -[MADTextEmbeddingRequest setIndependent:]
+ -[MADTextEmbeddingRequest setLocale:]
+ -[MADTextEmbeddingResult error]
+ -[MADTextEmbeddingResult initWithEmbedding:calibrationVersion:bias:scale:threshold:]
+ -[MADTextEmbeddingResult initWithError:]
+ -[MADTextEmbeddingResult isLexiconSafe]
+ -[MADTextEmbeddingResult setIsLexiconSafe:]
+ -[MADTextEmbeddingResult textEmbedding]
+ -[MADVideoSessionFrameProperties displayFrameSize]
+ -[MADVideoSessionFrameProperties setDisplayFrameSize:]
+ -[MADVideoSessionHomeVisionRequest description]
+ -[MADVideoSessionHomeVisionRequest encodeWithCoder:]
+ -[MADVideoSessionHomeVisionRequest initWithCoder:]
+ -[MADVideoSessionHomeVisionRequest setStreamToken:]
+ -[MADVideoSessionHomeVisionRequest streamToken]
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.1
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.2
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.3
+ -[MADVideoSessionPixelBufferPool copyPixelBuffer:toPixelBuffer:].cold.4
+ GCC_except_table18
+ GCC_except_table180
+ GCC_except_table181
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table189
+ GCC_except_table71
+ GCC_except_table74
+ GCC_except_table80
+ GCC_except_table81
+ _CGSizeZero
+ _MADIsModelDownloadSupportedForEmbeddingVersion
+ _OBJC_CLASS_$_MADCrossEncoderOutput
+ _OBJC_CLASS_$_MADCrossEncoderSimilarityRequest
+ _OBJC_CLASS_$_MADCrossEncoderSimilarityResult
+ _OBJC_CLASS_$_MADEmbeddingSpaceDescriptor
+ _OBJC_CLASS_$_MADTextEncoder
+ _OBJC_CLASS_$_MADVideoSessionHomeVisionRequest
+ _OBJC_CLASS_$_MADVideoSessionHomeVisionResult
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_IVAR_$_MADCrossEncoderSimilarityRequest._chunkOverlap
+ _OBJC_IVAR_$_MADCrossEncoderSimilarityRequest._documents
+ _OBJC_IVAR_$_MADCrossEncoderSimilarityRequest._extendedContextLength
+ _OBJC_IVAR_$_MADCrossEncoderSimilarityRequest._maxNumChunks
+ _OBJC_IVAR_$_MADCrossEncoderSimilarityRequest._requireWeights
+ _OBJC_IVAR_$_MADCrossEncoderSimilarityResult._crossEncoderOutputs
+ _OBJC_IVAR_$_MADCrossEncoderSimilarityResult._error
+ _OBJC_IVAR_$_MADImageCaptionRequest._customizedPrompt
+ _OBJC_IVAR_$_MADImageEmbeddingRequest._embeddingSpaceDescriptor
+ _OBJC_IVAR_$_MADTextEmbeddingRequest._allowPCC
+ _OBJC_IVAR_$_MADTextEmbeddingRequest._computeLexiconSafety
+ _OBJC_IVAR_$_MADTextEmbeddingRequest._embeddingSpaceDescriptor
+ _OBJC_IVAR_$_MADTextEmbeddingRequest._independent
+ _OBJC_IVAR_$_MADTextEmbeddingRequest._locale
+ _OBJC_IVAR_$_MADTextEmbeddingResult._error
+ _OBJC_IVAR_$_MADTextEmbeddingResult._isLexiconSafe
+ _OBJC_IVAR_$_MADVideoSessionFrameProperties._displayFrameSize
+ _OBJC_IVAR_$_MADVideoSessionHomeVisionRequest._streamToken
+ _OBJC_METACLASS_$_MADCrossEncoderSimilarityRequest
+ _OBJC_METACLASS_$_MADCrossEncoderSimilarityResult
+ _OBJC_METACLASS_$_MADVideoSessionHomeVisionRequest
+ _OBJC_METACLASS_$_MADVideoSessionHomeVisionResult
+ __OBJC_$_CLASS_METHODS_MADCrossEncoderSimilarityRequest
+ __OBJC_$_CLASS_METHODS_MADCrossEncoderSimilarityResult
+ __OBJC_$_CLASS_METHODS_MADVideoSessionHomeVisionRequest
+ __OBJC_$_INSTANCE_METHODS_MADCrossEncoderSimilarityRequest
+ __OBJC_$_INSTANCE_METHODS_MADCrossEncoderSimilarityResult
+ __OBJC_$_INSTANCE_METHODS_MADVideoSessionHomeVisionRequest
+ __OBJC_$_INSTANCE_VARIABLES_MADCrossEncoderSimilarityRequest
+ __OBJC_$_INSTANCE_VARIABLES_MADCrossEncoderSimilarityResult
+ __OBJC_$_INSTANCE_VARIABLES_MADVideoSessionHomeVisionRequest
+ __OBJC_$_PROP_LIST_MADCrossEncoderSimilarityRequest
+ __OBJC_$_PROP_LIST_MADCrossEncoderSimilarityResult
+ __OBJC_$_PROP_LIST_MADVideoSessionHomeVisionRequest
+ __OBJC_CLASS_RO_$_MADCrossEncoderSimilarityRequest
+ __OBJC_CLASS_RO_$_MADCrossEncoderSimilarityResult
+ __OBJC_CLASS_RO_$_MADVideoSessionHomeVisionRequest
+ __OBJC_CLASS_RO_$_MADVideoSessionHomeVisionResult
+ __OBJC_METACLASS_RO_$_MADCrossEncoderSimilarityRequest
+ __OBJC_METACLASS_RO_$_MADCrossEncoderSimilarityResult
+ __OBJC_METACLASS_RO_$_MADVideoSessionHomeVisionRequest
+ __OBJC_METACLASS_RO_$_MADVideoSessionHomeVisionResult
+ __ZL40CGImage_CreateCVPixelBufferWithTransformP7CGImagePP10__CVBufferj26CGImagePropertyOrientationd.cold.6
+ __ZL40CGImage_CreateCVPixelBufferWithTransformP7CGImagePP10__CVBufferj26CGImagePropertyOrientationd.cold.7
+ ___100-[MADService performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:completionHandler:]_block_invoke.100
+ ___100-[MADService(Photos) requestApplicationDataFolderIdentifierVisionServiceWithPhotosLibraryURL:error:]_block_invoke.227
+ ___100-[MADService(Photos) requestApplicationDataFolderIdentifierVisionServiceWithPhotosLibraryURL:error:]_block_invoke.227.cold.1
+ ___101-[MADService(Spotlight) submitSpotlightAssetURL:uniqueIdentifier:bundleIdentifier:completionHandler:]_block_invoke.405
+ ___104-[MADComputeService performRequests:assetURLs:options:progressHandler:resultsHandler:completionHandler:]_block_invoke.76
+ ___105-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:error:]_block_invoke.184
+ ___105-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:error:]_block_invoke.184.cold.1
+ ___109-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:completionHandler:]_block_invoke.197
+ ___122-[MADService(Photos) _performRequests:onIOSurface:withOrientation:assetLocalIdentifier:photoLibraryURL:completionHandler:]_block_invoke.185
+ ___123-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:resultHandler:completionHandler:]_block_invoke.198
+ ___123-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:resultHandler:completionHandler:]_block_invoke.198.cold.1
+ ___133-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:]_block_invoke.182
+ ___133-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:]_block_invoke.182.cold.1
+ ___24-[MADService connection]_block_invoke.62
+ ___24-[MADService connection]_block_invoke.62.cold.1
+ ___29-[MADVideoSession connection]_block_invoke.215
+ ___29-[MADVideoSession connection]_block_invoke.215.cold.1
+ ___29-[MADVideoSession connection]_block_invoke.216
+ ___31-[MADComputeService connection]_block_invoke.60
+ ___31-[MADComputeService connection]_block_invoke.60.cold.1
+ ___33-[MADVideoSession removeRequest:]_block_invoke.230
+ ___36-[MADVideoSession addRequest:error:]_block_invoke.226
+ ___36-[MADVideoSession removeAllRequests]_block_invoke.238
+ ___37-[MADService currentOutstandingTasks]_block_invoke.109
+ ___41-[MADComputeService removeRequest:error:]_block_invoke.162
+ ___44-[MADService(UserSafety) userSafetyEnabled:]_block_invoke.304
+ ___52-[MADVideoSession _addBackRequestsAfterReconnection]_block_invoke.221
+ ___55-[MADService(Performance) queryPerformanceMeasurements]_block_invoke.268
+ ___58-[MADService(Text) prewarmTextRequests:completionHandler:]_block_invoke.337
+ ___62-[MADComputeService scheduleRequests:assetURLs:options:error:]_block_invoke.92
+ ___62-[MADService performRequests:onImageURL:withIdentifier:error:]_block_invoke.99
+ ___62-[MADService performRequests:onImageURL:withIdentifier:error:]_block_invoke.99.cold.1
+ ___64-[MADService(Photos) requestVUIndexURLForPhotoLibraryURL:error:]_block_invoke.208
+ ___64-[MADService(Photos) requestVUIndexURLForPhotoLibraryURL:error:]_block_invoke.208.cold.1
+ ___64-[MADService(Photos) requestVUIndexURLForPhotoLibraryURL:error:]_block_invoke.208.cold.2
+ ___65-[MADService(Text) performRequests:textInputs:completionHandler:]_block_invoke.341
+ ___68-[MADVideoSession processPixelBuffer:frameProperties:resultHandler:]_block_invoke.248
+ ___70-[MADService(MultiModal) prewarmMultiModalRequests:completionHandler:]_block_invoke.411
+ ___70-[MADService(UserSafety) registerUserSafetyPolicyUpdateHandler:error:]_block_invoke.306
+ ___74-[MADService performRequests:onImageURL:withIdentifier:completionHandler:]_block_invoke.98
+ ___74-[MADService(Photos) queryVUIndexAssetCountForType:photoLibraryURL:error:]_block_invoke.220
+ ___74-[MADService(Photos) queryVUIndexAssetCountForType:photoLibraryURL:error:]_block_invoke.220.cold.1
+ ___76-[MADService performRequests:onCGImage:withOrientation:andIdentifier:error:]_block_invoke.89
+ ___76-[MADService performRequests:onCGImage:withOrientation:andIdentifier:error:]_block_invoke.89.cold.1
+ ___76-[MADService(Photos) performRequestsWithCloudIdentifiers:completionHandler:]_block_invoke.190
+ ___76-[MADService(Photos) queryImagePriority1MCEnableDate:photoLibraryURL:error:]_block_invoke.226
+ ___76-[MADService(Photos) queryImagePriority1MCEnableDate:photoLibraryURL:error:]_block_invoke.226.cold.1
+ ___77-[MADService(MultiModal) performRequests:multiModalInputs:completionHandler:]_block_invoke.412
+ ___80-[MADService(Photos) queryVUIndexLastFullModeClusterDate:photoLibraryURL:error:]_block_invoke.223
+ ___80-[MADService(Photos) queryVUIndexLastFullModeClusterDate:photoLibraryURL:error:]_block_invoke.223.cold.1
+ ___83-[MADService(Photos) performRequests:onAssetWithCloudIdentifier:completionHandler:]_block_invoke.189
+ ___84-[MADService performRequests:videoURL:identifier:progressHandler:completionHandler:]_block_invoke.102
+ ___86-[MADService(Photos) queryVUIndexAssetCountForType:photoLibraryURL:completionHandler:]_block_invoke.222
+ ___88-[MADService performRequests:onCGImage:withOrientation:andIdentifier:completionHandler:]_block_invoke.82
+ ___88-[MADService performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:error:]_block_invoke.101
+ ___88-[MADService performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:error:]_block_invoke.101.cold.1
+ ___90-[MADComputeService resumeWithRequestID:progressHandler:resultsHandler:completionHandler:]_block_invoke.106
+ ___92-[MADService performRequests:onPixelBuffer:withOrientation:andIdentifier:completionHandler:]_block_invoke.80
+ ___95-[MADService(Photos) queryVUIndexLastFullModeClusterDateWithPhotoLibraryURL:completionHandler:]_block_invoke.225
+ ___95-[MADVideoSession(UserSafety) requestTTRNotificationWithVideoFrames:options:completionHandler:]_block_invoke.294
+ ___Block_byref_object_copy_.114
+ ___Block_byref_object_copy_.245
+ ___Block_byref_object_copy_.71
+ ___Block_byref_object_dispose_.115
+ ___Block_byref_object_dispose_.246
+ ___Block_byref_object_dispose_.72
+ ___block_literal_global.104
+ ___block_literal_global.106
+ ___block_literal_global.108
+ ___block_literal_global.111
+ ___block_literal_global.113
+ ___block_literal_global.201
+ ___block_literal_global.267
+ ___block_literal_global.271
+ ___block_literal_global.303
+ ___block_literal_global.316
+ ___block_literal_global.318
+ ___block_literal_global.320
+ ___block_literal_global.322
+ ___block_literal_global.324
+ ___block_literal_global.61
+ ___block_literal_global.66
+ ___block_literal_global.70
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$URLByAppendingPathExtension:
+ _objc_msgSend$URLWithString:relativeToURL:
+ _objc_msgSend$bundleWithIdentifier:
+ _objc_msgSend$customizedPrompt
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$decodeSizeForKey:
+ _objc_msgSend$encodeSize:forKey:
+ _objc_msgSend$family
+ _objc_msgSend$isModelDownloaded:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$revisionForAppleEmbeddingVersion:
+ _objc_msgSend$set
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$version
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_retain_x9
- +[MADTextInput csuTokenizerRevisionForEmbeddingVersion:].cold.1
- -[MADTextEmbeddingRequest calibrate]
- -[MADTextEmbeddingRequest setCalibrate:]
- -[MADTextEmbeddingResult initWithEmbedding:calibrationVersion:mean:standardDeviation:bias:scale:threshold:]
- -[MADTextEmbeddingResult mean]
- -[MADTextEmbeddingResult standardDeviation]
- GCC_except_table183
- GCC_except_table184
- GCC_except_table187
- GCC_except_table69
- GCC_except_table82
- GCC_except_table86
- _MADComputeUnitsToString
- _MADUnifiedEmbeddingVersionToString
- _OBJC_IVAR_$_MADTextEmbeddingRequest._calibrate
- _OBJC_IVAR_$_MADTextEmbeddingResult._mean
- _OBJC_IVAR_$_MADTextEmbeddingResult._standardDeviation
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- ___100-[MADService performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:completionHandler:]_block_invoke.101
- ___100-[MADService(Photos) requestApplicationDataFolderIdentifierVisionServiceWithPhotosLibraryURL:error:]_block_invoke.228
- ___100-[MADService(Photos) requestApplicationDataFolderIdentifierVisionServiceWithPhotosLibraryURL:error:]_block_invoke.228.cold.1
- ___101-[MADService(Spotlight) submitSpotlightAssetURL:uniqueIdentifier:bundleIdentifier:completionHandler:]_block_invoke.354
- ___104-[MADComputeService performRequests:assetURLs:options:progressHandler:resultsHandler:completionHandler:]_block_invoke.77
- ___105-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:error:]_block_invoke.185
- ___105-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:error:]_block_invoke.185.cold.1
- ___109-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:completionHandler:]_block_invoke.198
- ___122-[MADService(Photos) _performRequests:onIOSurface:withOrientation:assetLocalIdentifier:photoLibraryURL:completionHandler:]_block_invoke.186
- ___123-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:resultHandler:completionHandler:]_block_invoke.199.cold.1
- ___123-[MADService(Photos) performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:resultHandler:completionHandler:]_block_invoke.200
- ___133-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:]_block_invoke.183.cold.1
- ___133-[MADService(Photos) performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:]_block_invoke.184
- ___24-[MADService connection]_block_invoke.63.cold.1
- ___24-[MADService connection]_block_invoke.64
- ___29-[MADVideoSession connection]_block_invoke.201
- ___29-[MADVideoSession connection]_block_invoke.201.cold.1
- ___29-[MADVideoSession connection]_block_invoke.202
- ___31-[MADComputeService connection]_block_invoke.61.cold.1
- ___31-[MADComputeService connection]_block_invoke.62
- ___33-[MADVideoSession removeRequest:]_block_invoke.216
- ___36-[MADVideoSession addRequest:error:]_block_invoke.212
- ___36-[MADVideoSession removeAllRequests]_block_invoke.224
- ___37-[MADService currentOutstandingTasks]_block_invoke.110
- ___41-[MADComputeService removeRequest:error:]_block_invoke.163
- ___44-[MADService(UserSafety) userSafetyEnabled:]_block_invoke.305
- ___52-[MADVideoSession _addBackRequestsAfterReconnection]_block_invoke.207
- ___55-[MADService(Performance) queryPerformanceMeasurements]_block_invoke.269
- ___58-[MADService(Text) prewarmTextRequests:completionHandler:]_block_invoke.338
- ___62-[MADComputeService scheduleRequests:assetURLs:options:error:]_block_invoke.93
- ___62-[MADService performRequests:onImageURL:withIdentifier:error:]_block_invoke.100
- ___62-[MADService performRequests:onImageURL:withIdentifier:error:]_block_invoke.100.cold.1
- ___64-[MADService(Photos) requestVUIndexURLForPhotoLibraryURL:error:]_block_invoke.209
- ___64-[MADService(Photos) requestVUIndexURLForPhotoLibraryURL:error:]_block_invoke.209.cold.1
- ___64-[MADService(Photos) requestVUIndexURLForPhotoLibraryURL:error:]_block_invoke.209.cold.2
- ___65-[MADService(Text) performRequests:textInputs:completionHandler:]_block_invoke.342
- ___68-[MADVideoSession processPixelBuffer:frameProperties:resultHandler:]_block_invoke.234
- ___70-[MADService(MultiModal) prewarmMultiModalRequests:completionHandler:]_block_invoke.360
- ___70-[MADService(UserSafety) registerUserSafetyPolicyUpdateHandler:error:]_block_invoke.307
- ___74-[MADService performRequests:onImageURL:withIdentifier:completionHandler:]_block_invoke.99
- ___74-[MADService(Photos) queryVUIndexAssetCountForType:photoLibraryURL:error:]_block_invoke.221
- ___74-[MADService(Photos) queryVUIndexAssetCountForType:photoLibraryURL:error:]_block_invoke.221.cold.1
- ___76-[MADService performRequests:onCGImage:withOrientation:andIdentifier:error:]_block_invoke.90
- ___76-[MADService performRequests:onCGImage:withOrientation:andIdentifier:error:]_block_invoke.90.cold.1
- ___76-[MADService(Photos) performRequestsWithCloudIdentifiers:completionHandler:]_block_invoke.192
- ___76-[MADService(Photos) queryImagePriority1MCEnableDate:photoLibraryURL:error:]_block_invoke.227
- ___76-[MADService(Photos) queryImagePriority1MCEnableDate:photoLibraryURL:error:]_block_invoke.227.cold.1
- ___77-[MADService(MultiModal) performRequests:multiModalInputs:completionHandler:]_block_invoke.361
- ___80-[MADService(Photos) queryVUIndexLastFullModeClusterDate:photoLibraryURL:error:]_block_invoke.224
- ___80-[MADService(Photos) queryVUIndexLastFullModeClusterDate:photoLibraryURL:error:]_block_invoke.224.cold.1
- ___83-[MADService(Photos) performRequests:onAssetWithCloudIdentifier:completionHandler:]_block_invoke.190
- ___84-[MADService performRequests:videoURL:identifier:progressHandler:completionHandler:]_block_invoke.103
- ___86-[MADService(Photos) queryVUIndexAssetCountForType:photoLibraryURL:completionHandler:]_block_invoke.223
- ___88-[MADService performRequests:onCGImage:withOrientation:andIdentifier:completionHandler:]_block_invoke.83
- ___88-[MADService performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:error:]_block_invoke.102
- ___88-[MADService performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:error:]_block_invoke.102.cold.1
- ___90-[MADComputeService resumeWithRequestID:progressHandler:resultsHandler:completionHandler:]_block_invoke.107
- ___92-[MADService performRequests:onPixelBuffer:withOrientation:andIdentifier:completionHandler:]_block_invoke.81
- ___95-[MADService(Photos) queryVUIndexLastFullModeClusterDateWithPhotoLibraryURL:completionHandler:]_block_invoke.226
- ___95-[MADVideoSession(UserSafety) requestTTRNotificationWithVideoFrames:options:completionHandler:]_block_invoke.280
- ___Block_byref_object_copy_.115
- ___Block_byref_object_copy_.231
- ___Block_byref_object_copy_.72
- ___Block_byref_object_dispose_.116
- ___Block_byref_object_dispose_.232
- ___Block_byref_object_dispose_.73
- ___block_literal_global.105
- ___block_literal_global.107
- ___block_literal_global.109
- ___block_literal_global.112
- ___block_literal_global.114
- ___block_literal_global.202
- ___block_literal_global.268
- ___block_literal_global.272
- ___block_literal_global.304
- ___block_literal_global.317
- ___block_literal_global.319
- ___block_literal_global.321
- ___block_literal_global.323
- ___block_literal_global.325
- ___block_literal_global.62
- ___block_literal_global.67
- ___block_literal_global.71
- _objc_retainAutoreleasedReturnValue
CStrings:
+ ", embedding: %@"
+ ", error: %@"
+ ", isLexiconSafe: %@"
+ "./Utilities/CGUtilities.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/MediaAnalysisServices/ComputeService/MADCoreMLResult.mm"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/MADVideoSession.mm"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MediaAnalysis/MediaAnalysisServices/MADVideoSession/Utilities/MADPixelBufferProcesser.mm"
+ "AllowPCC"
+ "ChunkOverlap"
+ "ComputeLexiconSafety"
+ "CrossEncoderOutputs"
+ "DisplayFrameSize"
+ "Documents"
+ "EmbeddingCore bundle not found"
+ "EmbeddingCore bundle resourceURL is nil"
+ "EmbeddingMigration"
+ "EmbeddingSpaceDescriptor"
+ "Failed to parse cross encoder metadata JSON (%@)"
+ "Failed to read cross encoder metadata (%@)"
+ "ImageCustomizedPrompt"
+ "Independent"
+ "IsLexiconSafe"
+ "Locale"
+ "MD4 tokenization not supported through MADSystemSearchTextEncoderV1"
+ "MaxNumChunks"
+ "RequireWeights"
+ "SafetyTypeGV"
+ "SafetyTypeGVVideo"
+ "SearchUnifiedEmbeddingMD8"
+ "StreamToken"
+ "StreamToken: %d, "
+ "Unexpected cross encoder metadata JSON item type"
+ "Unexpected cross encoder metadata JSON shape"
+ "VersionString"
+ "[LOG_ERROR] %s[%d]: code %d\n"
+ "allowPCC: %d, "
+ "chunkOverlap: %@, "
+ "com.apple.EmbeddingCore"
+ "computeLexiconSafety: %d, "
+ "cross encoder metadata missing VersionString"
+ "cross encoder metadata missing userDefinedMetadata"
+ "crossEncoderOutputs: %@,"
+ "cross_encoder_v120_ane_8bit_combined"
+ "customizedPrompt %@, "
+ "displayFrameSize: width %.4f, height %.4f"
+ "documents: %@, "
+ "embeddingSpaceDescriptor: (%@), "
+ "embeddingSpaceDescriptor: (family=%lu version=%lu), "
+ "independent: %d, "
+ "locale: %@, "
+ "maxNumChunks: %@, "
+ "metadata.json"
+ "mlmodelc"
+ "requireWeights: %d, "
+ "userDefinedMetadata"
- ", mean: %@"
- ", standardDeviation: %@"
- ".cxx_construct"
- ".cxx_destruct"
- "@\"CIBarcodeDescriptor\""
- "@\"CLLocation\""
- "@\"IOSurface\""
- "@\"MADComputeService\""
- "@\"MADEmbeddingResult\""
- "@\"MADPixelBufferProcesser\""
- "@\"MADService\""
- "@\"MADVIVisualSearchThirdPartyObject\""
- "@\"MADVideoSafetyFrameSampling\""
- "@\"MADVideoSession\""
- "@\"MADVideoSessionPixelBufferPool\""
- "@\"MLFeatureValue\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSIndexSet\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSSet\""
- "@\"NSSet\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSValue\""
- "@\"NSXPCConnection\""
- "@\"Protocol\"16@0:8"
- "@\"SCSensitivityAnalysis\""
- "@\"UTType\""
- "@\"VNFaceprint\""
- "@\"VNRequest\""
- "@\"VUWGalleryPersonalizationOptions\""
- "@104@0:8{?={?=qiIq}{?=qiIq}}16@64{CGRect={CGPoint=dd}{CGSize=dd}}72"
- "@104@0:8{?={?=qiIq}{?=qiIq}}16d64{CGRect={CGPoint=dd}{CGSize=dd}}72"
- "@104@0:8{CGPoint=dd}16{CGPoint=dd}32{CGPoint=dd}48{CGPoint=dd}64@80@88@96"
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@24@0:8q16"
- "@28@0:8Q16B24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8@16q24"
- "@32@0:8Q16@24"
- "@32@0:8Q16Q24"
- "@32@0:8Q16^@24"
- "@32@0:8^@16^@24"
- "@32@0:8q16q24"
- "@36@0:8Q16B24@?28"
- "@36@0:8Q16Q24B32"
- "@40@0:8@16@24@32"
- "@40@0:8Q16@24Q32"
- "@40@0:8Q16Q24q32"
- "@44@0:8@16@24@32B40"
- "@44@0:8@16f24B28B32@36"
- "@44@0:8Q16Q24B32@?36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32^@40"
- "@48@0:8@16Q24Q32@40"
- "@48@0:8Q16@24Q32@40"
- "@48@0:8{?=qiIq}16@40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@52@0:8^{__CVBuffer=}16{?=qiIq}24I48"
- "@56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
- "@60@0:8i16d20{CGRect={CGPoint=dd}{CGSize=dd}}28"
- "@64@0:8@16@24@32@?40@?48@?56"
- "@64@0:8@16^{__CVBuffer=}24@32@?40@?48@?56"
- "@64@0:8@16d24{CGRect={CGPoint=dd}{CGSize=dd}}32"
- "@64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56"
- "@68@0:8i16d20{CGRect={CGPoint=dd}{CGSize=dd}}28@60"
- "@72@0:8@16@24@32@40@48@56@64"
- "@72@0:8@16d24{CGRect={CGPoint=dd}{CGSize=dd}}32@64"
- "@72@0:8{?={?=qiIq}{?=qiIq}}16d64"
- "@76@0:8@16@24@32B40{CGPoint=dd}44@60@68"
- "@80@0:8{?={?=qiIq}{?=qiIq}}16d64@72"
- "@84@0:8@16@24@32@40f48@52@60@68@76"
- "@84@0:8@16@24@32s40B44{CGRect={CGPoint=dd}{CGSize=dd}}48f80"
- "@84@0:8@16@24@32{CGRect={CGPoint=dd}{CGSize=dd}}40f72@76"
- "@?"
- "AB"
- "ANE"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8@?16^@24"
- "B32@0:8^{__CVBuffer=}16^@24"
- "B40@0:8@16@24^@32"
- "B40@0:8@16Q24^@32"
- "B40@0:8^{__CVBuffer=}16@24@?32"
- "B40@0:8^{__CVBuffer=}16@24^@32"
- "B40@0:8^{__CVBuffer=}16Q24^@32"
- "B48@0:8@16@24@32^@40"
- "B52@0:8@16^{CGImage=}24I32@36^@44"
- "B56@0:8@16@24@32@40^@48"
- "B56@0:8@16@24Q32@40^@48"
- "B56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16i48i52"
- "B60@0:8^{__CVBuffer=}16{?=qiIq}24I48@?52"
- "CPU"
- "Calibrate"
- "GPU"
- "I"
- "I16@0:8"
- "MADCaptionResult"
- "MADComputeService"
- "MADComputeServiceClientProtocol"
- "MADComputeServiceProxy"
- "MADComputeServiceServerProtocol"
- "MADCoreMLObservation"
- "MADCoreMLRequest"
- "MADCoreMLResult"
- "MADDetectedFace"
- "MADDetectedFaceVideoEntry"
- "MADEmbeddingResult"
- "MADExposureImageRequest"
- "MADExposureResult"
- "MADFaceDetectionImageRequest"
- "MADFaceDetectionResult"
- "MADFaceDetectionVideoRequest"
- "MADImageCaptionRequest"
- "MADImageCoreMLRequest"
- "MADImageEmbeddingRequest"
- "MADImageEmbeddingResult"
- "MADImagePersonalizationFace"
- "MADImagePersonalizationGatingRequest"
- "MADImagePersonalizationGatingResult"
- "MADImageSafetyClassificationRequest"
- "MADImageSafetyClassificationResult"
- "MADImageVisionRequest"
- "MADMLEnhancementRequest"
- "MADMLEnhancementResult"
- "MADMLScalingRequest"
- "MADMLScalingResult"
- "MADMovieCurationRequest"
- "MADMovieCurationResult"
- "MADMovieCurationScoreEntry"
- "MADMovieHighlightEntry"
- "MADMultiModalInput"
- "MADMultiModalInputDescriptionSegment"
- "MADMultiModalInputFaceprintSegment"
- "MADMultiModalInputImageSegment"
- "MADMultiModalInputSegment"
- "MADMultiModalInputTextSegment"
- "MADMultiModalReply"
- "MADMultiModalRequest"
- "MADMultiModalResult"
- "MADOptions"
- "MADPersonIdentificationRequest"
- "MADPersonIdentificationResult"
- "MADPersonIdentificationResultItem"
- "MADPersonalizedEmbeddingRequest"
- "MADPersonalizedEmbeddingResult"
- "MADPixelBufferProcesser"
- "MADRemoveBackgroundMaskRequest"
- "MADRemoveBackgroundMaskResult"
- "MADRemoveBackgroundMatteRequest"
- "MADRemoveBackgroundMatteResult"
- "MADRequest"
- "MADResult"
- "MADRichLabelClassificationRequest"
- "MADRichLabelClassificationResult"
- "MADRichLabelClassificationResultItem"
- "MADSceneClassification"
- "MADSceneClassificationImageRequest"
- "MADSceneClassificationResult"
- "MADSceneClassificationVideoEntry"
- "MADSceneClassificationVideoRequest"
- "MADService"
- "MADServicePrivate"
- "MADServiceProtocol"
- "MADServiceProxy"
- "MADServicePublic"
- "MADSharpnessImageRequest"
- "MADSharpnessResult"
- "MADTextEmbeddingRequest"
- "MADTextEmbeddingResult"
- "MADTextInput"
- "MADTextInputSegment"
- "MADTextInputTextSegment"
- "MADTextInputTokenSegment"
- "MADTextRequest"
- "MADTextResult"
- "MADTextResultsPayload"
- "MADTextTokenizationRequest"
- "MADTextTokenizationResult"
- "MADTimer"
- "MADUserSafetyPolicy"
- "MADVIDocumentRecognitionRequest"
- "MADVIDocumentRecognitionResult"
- "MADVIFaceRequest"
- "MADVIFaceResult"
- "MADVIMachineReadableCodeDetectionRequest"
- "MADVIMachineReadableCodeDetectionResult"
- "MADVIMachineReadableCodeDetectionResultItem"
- "MADVIRectangleDetectionRequest"
- "MADVIRectangleDetectionResult"
- "MADVISceneClassificationRequest"
- "MADVISceneClassificationResult"
- "MADVITextLookupRequest"
- "MADVITextLookupResult"
- "MADVIUserFeedbackRequest"
- "MADVIUserFeedbackResult"
- "MADVIVisualSearchGatingDomainInfo"
- "MADVIVisualSearchGatingRequest"
- "MADVIVisualSearchGatingResult"
- "MADVIVisualSearchGatingResultItem"
- "MADVIVisualSearchRegionAttributes"
- "MADVIVisualSearchRequest"
- "MADVIVisualSearchResult"
- "MADVIVisualSearchResultItem"
- "MADVIVisualSearchThirdPartyObject"
- "MADVideoCoreMLRequest"
- "MADVideoRemoveBackgroundPreviewFrame"
- "MADVideoRemoveBackgroundPreviewRequest"
- "MADVideoRemoveBackgroundPreviewResult"
- "MADVideoRemoveBackgroundRequest"
- "MADVideoRemoveBackgroundResult"
- "MADVideoRequest"
- "MADVideoResult"
- "MADVideoResultsPayload"
- "MADVideoSafetyClassificationRequest"
- "MADVideoSafetyClassificationResult"
- "MADVideoSafetyFrameSampling"
- "MADVideoSession"
- "MADVideoSessionClientProtocol"
- "MADVideoSessionFrameProperties"
- "MADVideoSessionPixelBufferPool"
- "MADVideoSessionProxy"
- "MADVideoSessionRequest"
- "MADVideoSessionResult"
- "MADVideoSessionSafetyRequest"
- "MADVideoSessionSafetyResult"
- "MADVideoSessionServerProtocol"
- "MADVideoSessionTTRFrame"
- "MADVideoSessionTTROptions"
- "MADVideoVisionRequest"
- "MADVisionRequest"
- "MADVisionResult"
- "MD1"
- "MD2"
- "MD3"
- "MD4"
- "MD4 tokenization not supported through CSUSystemSearchTextEncoderV1"
- "MD5"
- "MD6"
- "MD6'"
- "MD7"
- "MD7v2"
- "Mean"
- "MultiModal"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "Performance"
- "Photos"
- "ProtocolDefaults"
- "Q"
- "Q16@0:8"
- "SearchUnifiedEmbeddingMD7"
- "Spotlight"
- "StandardDeviation"
- "T@\"CIBarcodeDescriptor\",R,N,V_descriptor"
- "T@\"CLLocation\",C,N,V_location"
- "T@\"IOSurface\",R,N,V_surface"
- "T@\"MADEmbeddingResult\",R,N,V_embedding"
- "T@\"MADEmbeddingResult\",R,N,V_hiddenLayer"
- "T@\"MADEmbeddingResult\",R,N,V_pooledEmbedding"
- "T@\"MADImagePersonalizationGatingResult\",R,N"
- "T@\"MADRemoveBackgroundMaskResult\",R,N"
- "T@\"MADRemoveBackgroundMatteResult\",R,N"
- "T@\"MADRichLabelClassificationResult\",R,N"
- "T@\"MADVIVisualSearchThirdPartyObject\",R,N,V_thirdPartyObject"
- "T@\"MADVideoRemoveBackgroundPreviewResult\",R,N"
- "T@\"MADVideoRemoveBackgroundResult\",R,N"
- "T@\"MADVideoSafetyFrameSampling\",C,N,V_sampling"
- "T@\"MLFeatureValue\",R,N,V_featureValue"
- "T@\"NSArray\",&,N,V_results"
- "T@\"NSArray\",C,N,V_catalogIDs"
- "T@\"NSArray\",C,N,V_domains"
- "T@\"NSArray\",C,N,V_languages"
- "T@\"NSArray\",C,N,V_normalizedBoundingBoxes"
- "T@\"NSArray\",C,N,V_stickerIdentifiers"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_classificationIdentifiers"
- "T@\"NSArray\",R,N,V_classificationObservations"
- "T@\"NSArray\",R,N,V_curationScoreEntries"
- "T@\"NSArray\",R,N,V_domains"
- "T@\"NSArray\",R,N,V_faceAttributesObservations"
- "T@\"NSArray\",R,N,V_faceExpressionsObservations"
- "T@\"NSArray\",R,N,V_faceLandmarksObservations"
- "T@\"NSArray\",R,N,V_faceRectanglesObservations"
- "T@\"NSArray\",R,N,V_faceprintObservations"
- "T@\"NSArray\",R,N,V_faces"
- "T@\"NSArray\",R,N,V_frames"
- "T@\"NSArray\",R,N,V_highlightEntries"
- "T@\"NSArray\",R,N,V_nsfwObservations"
- "T@\"NSArray\",R,N,V_observations"
- "T@\"NSArray\",R,N,V_recognizedObjectObservations"
- "T@\"NSArray\",R,N,V_regionAttributes"
- "T@\"NSArray\",R,N,V_resultItems"
- "T@\"NSArray\",R,N,V_results"
- "T@\"NSArray\",R,N,V_saliencyObservations"
- "T@\"NSArray\",R,N,V_searchSections"
- "T@\"NSArray\",R,N,V_shape"
- "T@\"NSArray\",R,N,V_significantEventObservations"
- "T@\"NSArray\",R,N,V_summaryEntries"
- "T@\"NSArray\",R,N,V_symbologies"
- "T@\"NSArray\",R,N,V_tokenIDs"
- "T@\"NSArray\",R,N,V_videoEntries"
- "T@\"NSArray\",R,N,V_visionResults"
- "T@\"NSData\",R,N"
- "T@\"NSData\",R,N,V_data"
- "T@\"NSData\",R,N,V_metadata"
- "T@\"NSData\",R,N,V_payload"
- "T@\"NSData\",R,N,V_sfReportData"
- "T@\"NSData\",R,N,V_userFeedbackPayload"
- "T@\"NSDate\",&,N,V_eventDate"
- "T@\"NSDate\",&,N,V_startDate"
- "T@\"NSDictionary\",R,N,V_attributes"
- "T@\"NSDictionary\",R,N,V_knowledgeProperties"
- "T@\"NSDictionary\",R,N,V_scoresForLabels"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSIndexSet\",&,N,V_domains"
- "T@\"NSIndexSet\",C,N,V_instances"
- "T@\"NSIndexSet\",R,N,V_allInstances"
- "T@\"NSNumber\",&,N,V_sensitiveFrameCountThreshold"
- "T@\"NSNumber\",C,N,V_imageType"
- "T@\"NSNumber\",C,N,V_maxDimension"
- "T@\"NSNumber\",C,N,V_maxFileSize"
- "T@\"NSNumber\",C,N,V_minDimension"
- "T@\"NSNumber\",C,N,V_queryID"
- "T@\"NSNumber\",C,N,V_uiScale"
- "T@\"NSNumber\",R,N,V_animatedStickerScore"
- "T@\"NSNumber\",R,N,V_bias"
- "T@\"NSNumber\",R,N,V_calibrationVersion"
- "T@\"NSNumber\",R,N,V_confidenceTypeN"
- "T@\"NSNumber\",R,N,V_isSafe"
- "T@\"NSNumber\",R,N,V_isSensitiveGoreViolence"
- "T@\"NSNumber\",R,N,V_isSensitiveNudity"
- "T@\"NSNumber\",R,N,V_mean"
- "T@\"NSNumber\",R,N,V_safetyScore"
- "T@\"NSNumber\",R,N,V_scale"
- "T@\"NSNumber\",R,N,V_seed"
- "T@\"NSNumber\",R,N,V_standardDeviation"
- "T@\"NSNumber\",R,N,V_threshold"
- "T@\"NSNumber\",R,N,V_truncated"
- "T@\"NSSet\",R,N"
- "T@\"NSSet\",R,N,V_classifications"
- "T@\"NSSet\",R,N,V_faces"
- "T@\"NSString\",&,N,V_streamID"
- "T@\"NSString\",&,N,V_uuid"
- "T@\"NSString\",C,N,V_conversationIdentifier"
- "T@\"NSString\",C,N,V_engagementSuggestionType"
- "T@\"NSString\",C,N,V_featureIdentifier"
- "T@\"NSString\",C,N,V_hintDomain"
- "T@\"NSString\",C,N,V_stagedText"
- "T@\"NSString\",C,N,V_surroundingText"
- "T@\"NSString\",R,C,N,V_queryTerm"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_caption"
- "T@\"NSString\",R,N,V_detailedDescription"
- "T@\"NSString\",R,N,V_displayLabel"
- "T@\"NSString\",R,N,V_displayMessage"
- "T@\"NSString\",R,N,V_domain"
- "T@\"NSString\",R,N,V_featureName"
- "T@\"NSString\",R,N,V_glyphName"
- "T@\"NSString\",R,N,V_imageURL"
- "T@\"NSString\",R,N,V_knowledgeGraphID"
- "T@\"NSString\",R,N,V_label"
- "T@\"NSString\",R,N,V_mdID"
- "T@\"NSString\",R,N,V_objectIdentifier"
- "T@\"NSString\",R,N,V_payload"
- "T@\"NSString\",R,N,V_personIdentifier"
- "T@\"NSString\",R,N,V_personName"
- "T@\"NSString\",R,N,V_reportIdentifier"
- "T@\"NSString\",R,N,V_requestID"
- "T@\"NSString\",R,N,V_shortDescription"
- "T@\"NSString\",R,N,V_symbology"
- "T@\"NSString\",R,N,V_text"
- "T@\"NSString\",R,N,V_thumbnailURL"
- "T@\"NSString\",R,N,V_title"
- "T@\"NSURL\",C,N,V_imageURL"
- "T@\"NSURL\",C,N,V_referralURL"
- "T@\"NSURL\",R,N,V_modelURL"
- "T@\"NSURL\",R,N,V_thumbnailURL"
- "T@\"NSURL\",R,N,V_webURL"
- "T@\"NSValue\",C,N,V_instancePoint"
- "T@\"Protocol\",R,N"
- "T@\"SCSensitivityAnalysis\",R,N,V_analysisResult"
- "T@\"UTType\",C,N,V_outputType"
- "T@\"UTType\",R,N,V_uniformTypeIdentifier"
- "T@\"VNFaceprint\",R,N,V_faceprint"
- "T@\"VNRequest\",R,N,V_visionRequest"
- "T@\"VUWGalleryPersonalizationOptions\",&,N,V_personalizationOptions"
- "TB,N,V_allowOnDemand"
- "TB,N,V_allowTruncation"
- "TB,N,V_allowUnverifiedIdentity"
- "TB,N,V_appliesPreferredTrackTransform"
- "TB,N,V_bypassFaceDetection"
- "TB,N,V_bypassNormalizaton"
- "TB,N,V_calibrate"
- "TB,N,V_computeSafety"
- "TB,N,V_computeThreshold"
- "TB,N,V_cropResult"
- "TB,N,V_enableDetectionTypeGV"
- "TB,N,V_enableDetectionTypeN"
- "TB,N,V_enableGoreViolenceDetection"
- "TB,N,V_enableNudityDetection"
- "TB,N,V_extendedContextLength"
- "TB,N,V_inPlace"
- "TB,N,V_includePets"
- "TB,N,V_modelPreparationOnly"
- "TB,N,V_requiresBlastdoor"
- "TB,N,V_requiresScoresAndLabels"
- "TB,N,V_useLowResolutionPicture"
- "TB,N,V_useVIPModel"
- "TB,N,V_usesFormFieldDetection"
- "TB,N,V_usesLanguageCorrection"
- "TB,N,V_usesLanguageDetection"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_containsUnsafeContent"
- "TB,R,N,V_hasFocalPoint"
- "TB,R,N,V_isLowConfidence"
- "TB,R,N,V_personalized"
- "TB,R,N,V_uniformSampling"
- "TB,R,N,V_verified"
- "TI,N,V_orientation"
- "TI,R,N,V_orientation"
- "TQ,N,V_computeUnits"
- "TQ,N,V_faceDetectorVisionRevision"
- "TQ,N,V_maximumCandidateCount"
- "TQ,N,V_maximumFaceCount"
- "TQ,N,V_maximumObservations"
- "TQ,N,V_version"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_classificationRevision"
- "TQ,R,N,V_domain"
- "TQ,R,N,V_frameLimit"
- "TQ,R,N,V_framesPerSync"
- "TQ,R,N,V_height"
- "TQ,R,N,V_maximumHierarchicalObservations"
- "TQ,R,N,V_maximumLeafObservations"
- "TQ,R,N,V_nsfwRevision"
- "TQ,R,N,V_recognizeObjectsRevision"
- "TQ,R,N,V_saliencyRevision"
- "TQ,R,N,V_scaledImageHeight"
- "TQ,R,N,V_scaledImageWidth"
- "TQ,R,N,V_significantEventRevision"
- "TQ,R,N,V_type"
- "TQ,R,N,V_version"
- "TQ,R,N,V_width"
- "T^{CGImage=},R,N"
- "T^{__CVBuffer=},R,N"
- "Td,R"
- "Td,R,N,V_confidence"
- "Td,R,N,V_exposureScore"
- "Td,R,N,V_score"
- "Td,R,N,V_sharpnessScore"
- "Tf,N,V_maximumAspectRatio"
- "Tf,N,V_minimumAspectRatio"
- "Tf,N,V_minimumConfidence"
- "Tf,N,V_minimumSize"
- "Tf,N,V_minimumTextHeight"
- "Tf,N,V_quadratureTolerance"
- "Tf,R,N,V_confidence"
- "Tf,R,N,V_score"
- "Tf,R,N,V_thumbnailAspectRatio"
- "Ti,R,N,V_faceID"
- "Tokenizer revision unknown for specified embedding version (%d)"
- "Tq,N"
- "Tq,N,V_embeddingRequestType"
- "Tq,N,V_recognitionLevel"
- "Tq,N,V_revision"
- "Tq,R,N"
- "Tq,R,N,V_frontCameraCaptureState"
- "Tq,R,N,V_modelType"
- "Tq,R,N,V_policyType"
- "Tq,R,N,V_safetyType"
- "Tq,R,N,V_scalingModelIndex"
- "Ts,R,N,V_detectionType"
- "T{?=qiIq},N,V_maskTime"
- "T{?=qiIq},N,V_timestamp"
- "T{?=qiIq},R,N,V_presentationTimeStamp"
- "T{?=qiIq},R,N,V_timestamp"
- "T{?={?=qiIq}{?=qiIq}},R,N,V_timeRange"
- "T{?={?=qiIq}{?=qiIq}},R,N,V_timerange"
- "T{CGPoint=dd},R,N,V_bottomLeft"
- "T{CGPoint=dd},R,N,V_bottomRight"
- "T{CGPoint=dd},R,N,V_focalPoint"
- "T{CGPoint=dd},R,N,V_topLeft"
- "T{CGPoint=dd},R,N,V_topRight"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_regionOfInterest"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_targetBounds"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_boundingBox"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_cropRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_normalizedBoundingBox"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_normalizedCropRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_sourceRegionOfInterest"
- "URLByAppendingPathComponent:"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "UTF8String"
- "UUIDString"
- "Unexpected value (%lu)"
- "Unknown"
- "UserSafety"
- "VCPMADServicePublicServerProtocol"
- "VCPMediaAnalysisClientProtocol"
- "VCPMediaAnalysisServerProtocol"
- "VIAnalytics"
- "^{CGImage=}16@0:8"
- "^{__CVBuffer=}16@0:8"
- "_active"
- "_addBackRequestsAfterReconnection"
- "_addPixelBuffer:seed:error:"
- "_allInstances"
- "_allowOnDemand"
- "_allowTruncation"
- "_allowUnverifiedIdentity"
- "_analysisResult"
- "_animatedStickerScore"
- "_appliesPreferredTrackTransform"
- "_attributes"
- "_bias"
- "_block"
- "_bottomLeft"
- "_bottomRight"
- "_boundingBox"
- "_bufferHeight"
- "_bufferWidth"
- "_bypassFaceDetection"
- "_bypassNormalizaton"
- "_calibrate"
- "_calibrationVersion"
- "_caption"
- "_catalogIDs"
- "_classificationIdentifiers"
- "_classificationObservations"
- "_classificationRevision"
- "_classifications"
- "_computeSafety"
- "_computeThreshold"
- "_computeUnits"
- "_confidence"
- "_confidenceTypeN"
- "_configurePixelRotationSessionWithOrientation:"
- "_connection"
- "_connectionQueue"
- "_containsUnsafeContent"
- "_conversationIdentifier"
- "_coordinator"
- "_createPixelBuffer:width:height:format:"
- "_cropRect"
- "_cropResult"
- "_curationScoreEntries"
- "_data"
- "_descriptor"
- "_detailedDescription"
- "_detectionType"
- "_displayLabel"
- "_displayMessage"
- "_documentObservations"
- "_domain"
- "_domains"
- "_embedding"
- "_embeddingRequestType"
- "_enableDetectionTypeGV"
- "_enableDetectionTypeN"
- "_enableGoreViolenceDetection"
- "_enableNudityDetection"
- "_engagementSuggestionType"
- "_error"
- "_eventDate"
- "_executionNanoseconds"
- "_exposureScore"
- "_extendedContextLength"
- "_extensionData"
- "_faceAttributesObservations"
- "_faceDetectorVisionRevision"
- "_faceExpressionsObservations"
- "_faceID"
- "_faceLandmarksObservations"
- "_faceRectanglesObservations"
- "_faceprint"
- "_faceprintObservations"
- "_faces"
- "_featureIdentifier"
- "_featureName"
- "_featureValue"
- "_focalPoint"
- "_frameLimit"
- "_frames"
- "_framesPerSync"
- "_frontCameraCaptureState"
- "_gatingPayload"
- "_gatingResultItems"
- "_glyphName"
- "_hasFocalPoint"
- "_height"
- "_hiddenLayer"
- "_highlightEntries"
- "_hintDomain"
- "_image"
- "_imageType"
- "_imageURL"
- "_inPlace"
- "_includePets"
- "_instanceMaskImage"
- "_instanceMaskPixelBuffer"
- "_instanceMaskSurface"
- "_instancePoint"
- "_instances"
- "_isEntitledForVUIndexAccess"
- "_isLowConfidence"
- "_isOneShot"
- "_isSafe"
- "_isSensitiveGoreViolence"
- "_isSensitiveNudity"
- "_knowledgeGraphID"
- "_knowledgeProperties"
- "_label"
- "_languages"
- "_location"
- "_maskTime"
- "_maxDimension"
- "_maxFileSize"
- "_maximumAspectRatio"
- "_maximumCandidateCount"
- "_maximumFaceCount"
- "_maximumHierarchicalObservations"
- "_maximumLeafObservations"
- "_maximumObservations"
- "_mdID"
- "_mean"
- "_metadata"
- "_minDimension"
- "_minimumAspectRatio"
- "_minimumConfidence"
- "_minimumSize"
- "_minimumTextHeight"
- "_modelPreparationOnly"
- "_modelType"
- "_modelURL"
- "_normalizedBoundingBox"
- "_normalizedBoundingBoxes"
- "_normalizedCropRect"
- "_nsfwObservations"
- "_nsfwRevision"
- "_objectIdentifier"
- "_observations"
- "_orientation"
- "_outputType"
- "_packageCoreMLObservations"
- "_payload"
- "_perInstanceMaskSurfaces"
- "_performRequests:onIOSurface:withOrientation:assetLocalIdentifier:photoLibraryURL:completionHandler:"
- "_personIdentifier"
- "_personName"
- "_personalizationOptions"
- "_personalized"
- "_pixelBuffer"
- "_pixelBufferPool"
- "_pixelBufferProcessor"
- "_pixelFormat"
- "_policyType"
- "_pool"
- "_pooledEmbedding"
- "_presentationTimeStamp"
- "_progressHandlerQueue"
- "_progressHandlers"
- "_quadratureTolerance"
- "_queryID"
- "_queryTerm"
- "_queue"
- "_recognitionLevel"
- "_recognizeObjectsRevision"
- "_recognizedObjectObservations"
- "_referralURL"
- "_regionAttributes"
- "_regionOfInterest"
- "_removeLocalRequest:"
- "_reportIdentifier"
- "_requestID"
- "_requests"
- "_requestsManagementQueue"
- "_requiresBlastdoor"
- "_requiresScoresAndLabels"
- "_resultHandlerQueue"
- "_resultHandlers"
- "_resultItems"
- "_results"
- "_resultsHandlerQueue"
- "_resultsHandlers"
- "_revision"
- "_rotationSession"
- "_safetyScore"
- "_safetyType"
- "_saliencyObservations"
- "_saliencyRevision"
- "_sampling"
- "_scale"
- "_scaledImageHeight"
- "_scaledImageWidth"
- "_scalingModelIndex"
- "_score"
- "_scoresForLabels"
- "_searchSections"
- "_seed"
- "_segments"
- "_sensitiveFrameCountThreshold"
- "_service"
- "_session"
- "_sfReportData"
- "_shape"
- "_sharpnessScore"
- "_shortDescription"
- "_significantEventObservations"
- "_significantEventRevision"
- "_source"
- "_sourceRegionOfInterest"
- "_stagedText"
- "_standardDeviation"
- "_startDate"
- "_stickerIdentifiers"
- "_streamID"
- "_summaryEntries"
- "_surface"
- "_surroundingText"
- "_symbologies"
- "_symbology"
- "_targetBounds"
- "_text"
- "_thirdPartyObject"
- "_threshold"
- "_thumbnailAspectRatio"
- "_thumbnailURL"
- "_timeRange"
- "_timerange"
- "_timestamp"
- "_title"
- "_tokenIDs"
- "_topLeft"
- "_topRight"
- "_transferSession"
- "_truncated"
- "_type"
- "_uiScale"
- "_uniformSampling"
- "_uniformTypeIdentifier"
- "_useLowResolutionPicture"
- "_useVIPModel"
- "_userFeedbackPayload"
- "_userSafetyHandler"
- "_usesFormFieldDetection"
- "_usesLanguageCorrection"
- "_usesLanguageDetection"
- "_uuid"
- "_validFileURL:toRequestID:"
- "_verified"
- "_version"
- "_videoEntries"
- "_visionRequest"
- "_visionResults"
- "_webURL"
- "_width"
- "addEntityUUID:"
- "addEntityUUID:error:"
- "addEntityUUID:seed:error:"
- "addFaceprint:error:"
- "addObject:"
- "addPersonDescription:error:"
- "addPixelBuffer:error:"
- "addPixelBuffer:seed:error:"
- "addProgressHandler:forRequestID:"
- "addRequest:error:"
- "addRequest:reply:"
- "addResultHandler:forRequestID:"
- "addText:"
- "addText:error:"
- "addTokenIDs:"
- "allInstances"
- "allocWithZone:"
- "allowOnDemand"
- "allowTruncation"
- "allowUnverifiedIdentity"
- "allowedClasses"
- "allowedMultiModalInputClasses"
- "allowedMultiModalRequestClasses"
- "allowedMultiModalResultClasses"
- "allowedRequestTTRNotificationClasses"
- "allowedResultClasses"
- "allowedTextRequestClasses"
- "allowedTextResultClasses"
- "allowedVideoRequestClasses"
- "allowedVideoResultClasses"
- "analysisResult"
- "animatedStickerScore"
- "appendFormat:"
- "appendString:"
- "appliesPreferredTrackTransform"
- "array"
- "arrayWithObjects:count:"
- "attributeSet"
- "attributes"
- "barcodeDescriptor"
- "bias"
- "boolValue"
- "bottomLeft"
- "bottomRight"
- "boundingBox"
- "bundleID"
- "bundleIdentifier"
- "button"
- "bypassFaceDetection"
- "bytesPerRow"
- "cacheHitWithQueryID:cachedResultQueryID:"
- "cacheHitWithQueryID:cachedResultQueryID:engagementSuggestionType:"
- "calibrate"
- "calibrate: %d, "
- "calibrationVersion"
- "cancelAllRequests"
- "cancelBackgroundActivityWithReply:"
- "cancelRequest:"
- "cancelRequestID:"
- "cancelWithRequestID:"
- "caption"
- "catalogIDs"
- "classificationIdentifiers"
- "classificationObservations"
- "classificationRevision"
- "classifications"
- "code"
- "colorSpace"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "componentsSeparatedByString:"
- "computeSafety"
- "computeThreshold"
- "computeUnits"
- "confidence"
- "confidenceTypeN"
- "configureClientInterface:"
- "configureServerInterface:"
- "conformsToProtocol:"
- "connection"
- "consumeSandboxExtension"
- "containsUnsafeContent"
- "contentURL"
- "context"
- "conversationIdentifier"
- "copy"
- "copyPixelBuffer:toPixelBuffer:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "cropRect"
- "cropResult"
- "csuTokenizerRevision"
- "csuTokenizerRevisionForEmbeddingVersion:"
- "curationScoreEntries"
- "currentOutstandingTasks"
- "currentOutstandingTasksWithReply:"
- "d"
- "d16@0:8"
- "data"
- "dataWithBytes:length:"
- "dataWithContentsOfURL:"
- "date"
- "dealloc"
- "decodeBoolForKey:"
- "decodeCMTimeForKey:"
- "decodeCMTimeRangeForKey:"
- "decodeDoubleForKey:"
- "decodeFloatForKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodePointForKey:"
- "decodeRectForKey:"
- "defaultManager"
- "deregisterProgressHandlerForRequestID:"
- "deregisterResultsHandlerForRequestID:"
- "description"
- "descriptor"
- "destroy"
- "detailedDescription"
- "detectionType"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "displayLabel"
- "displayMessage"
- "documentObservations"
- "domain"
- "domains"
- "downloadVideoEncoderIfNeededWithReply:"
- "elementCount"
- "elementType"
- "embedding: %@"
- "embeddingData"
- "embeddingResults"
- "enableDetectionTypeGV"
- "enableDetectionTypeN"
- "enableGoreViolenceDetection"
- "enableNudityDetection"
- "enabledQRCodeDetection"
- "enabledVideoSessionXPC"
- "encodeBool:forKey:"
- "encodeCMTime:forKey:"
- "encodeCMTimeRange:forKey:"
- "encodeDouble:forKey:"
- "encodeFloat:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodePoint:forKey:"
- "encodeRect:forKey:"
- "encodeWithCoder:"
- "endEntryPoint"
- "engagementSuggestionType"
- "entryWithFaceID:confidence:boundingBox:"
- "entryWithFaceID:confidence:boundingBox:videoEntries:"
- "entryWithFeatureName:featureValue:"
- "entryWithLabel:confidence:boundingBox:"
- "entryWithLabel:confidence:boundingBox:videoEntries:"
- "entryWithTimeRange:confidence:boundingBox:"
- "entryWithTimeRange:score:"
- "entryWithTimeRange:score:attributes:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "error"
- "errorWithDomain:code:userInfo:"
- "eventDate"
- "executionNanoseconds"
- "executionTimeInterval"
- "exportedInterface"
- "exposureScore"
- "extendedContextLength"
- "extensionDataForResultDirectoryURL:error:"
- "extensionDataFromAssetURLs:error:"
- "extent"
- "f"
- "f16@0:8"
- "faceAttributesObservations"
- "faceDetectorVisionRevision"
- "faceExpressionsObservations"
- "faceID"
- "faceLandmarksObservations"
- "faceRectanglesObservations"
- "faceprint"
- "faceprintObservations"
- "faces"
- "featureIdentifier"
- "featureName"
- "featureValue"
- "fetchResultsWithRequestID:"
- "fileExistsAtPath:"
- "fileURLWithPath:"
- "firstIndex"
- "firstObject"
- "focalPoint"
- "frameLimit"
- "frames"
- "framesPerSync"
- "frontCameraCaptureState"
- "gatingPayload"
- "gatingResult"
- "gatingResultItems"
- "getResourceValue:forKey:error:"
- "getTranscript"
- "glyphName"
- "handleResult:atRequestIdx:forRequestID:"
- "handleResults:assetRepresentation:requestID:error:acknowledgement:"
- "handleTimerEvent"
- "hasFocalPoint"
- "hasOnlyOneSafetyRquest"
- "hash"
- "height"
- "hiddenLayer"
- "highlightEntries"
- "hintDomain"
- "i16@0:8"
- "i20@0:8I16"
- "i24@0:8@16"
- "i32@0:8@16@?24"
- "i32@0:8@?16@24"
- "i32@0:8^{__CVBuffer=}16^^{__CVBuffer}24"
- "i40@0:8@16@24@?32"
- "i40@0:8^@16@24^@32"
- "i40@0:8q16@24@?32"
- "i44@0:8@16^{__CVBuffer=}24I32@?36"
- "i44@0:8^^{__CVBuffer}16Q24Q32I40"
- "i48@0:8@16@24@32@?40"
- "i52@0:8@16@24I32@36@?44"
- "i52@0:8@16^{CGImage=}24I32@36@?44"
- "i52@0:8@16^{__CVBuffer=}24I32@36@?44"
- "i56@0:8@16@24@32@40@?48"
- "i56@0:8@16@24@32@?40@?48"
- "i56@0:8@16@24@32d40@?48"
- "i56@0:8@16@24Q32@40@?48"
- "i60@0:8@16@24I32@36@44@?52"
- "i60@0:8@16^{CGImage=}24I32@36@44@?52"
- "i60@0:8@16^{__CVBuffer=}24I32@36@44@?52"
- "i64@0:8@16@24@32@?40@?48@?56"
- "i64@0:8@16@24Q32@40d48@?56"
- "i76@0:8^{__CVBuffer=}16I24{CGRect={CGPoint=dd}{CGSize=dd}}28^^{__CVBuffer}60^B68"
- "i88@0:8^{__CVBuffer=}16I24{CGRect={CGPoint=dd}{CGSize=dd}}28Q60Q68I76^^{__CVBuffer}80"
- "identifier"
- "image"
- "imageType"
- "imageURL"
- "inPlace"
- "includePets"
- "indexGreaterThanIndex:"
- "indexSet"
- "init"
- "initInternal"
- "initWithCaption:score:containsUnsafeContent:isLowConfidence:classificationIdentifiers:"
- "initWithClassifications:"
- "initWithCoder:"
- "initWithCoordinator:"
- "initWithDetectedFaces:"
- "initWithDomain:displayLabel:"
- "initWithDomain:knowledgeGraphID:title:thumbnailURL:thumbnailAspectRatio:shortDescription:detailedDescription:webURL:knowledgeProperties:"
- "initWithDomain:label:glyphName:hasFocalPoint:focalPoint:displayLabel:displayMessage:"
- "initWithEmbedding:calibrationVersion:mean:standardDeviation:bias:scale:threshold:"
- "initWithEmbedding:hiddenLayer:pooledEmbedding:personalized:"
- "initWithExposureScore:"
- "initWithFaceID:confidence:boundingBox:videoEntries:"
- "initWithFaceprint:"
- "initWithFaces:"
- "initWithFeatureName:featureValue:"
- "initWithFrameLimit:uniformSampling:"
- "initWithFramesPerSync:frameLimit:uniformSampling:"
- "initWithGatingResultItems:andPayload:"
- "initWithGatingResultItems:payload:documentObservations:"
- "initWithInstances:instanceMaskSurface:perInstanceMaskSurfaces:sourceRegionOfInterest:confidence:animatedStickerScore:"
- "initWithIntervalNanoseconds:isOneShot:andBlock:"
- "initWithIsSensitiveNudity:isSensitiveGoreViolence:"
- "initWithIsSensitiveNudity:isSensitiveGoreViolence:scoresForLabels:"
- "initWithLabel:confidence:boundingBox:videoEntries:"
- "initWithLanguages:"
- "initWithMachServiceName:options:"
- "initWithModelType:safetyType:"
- "initWithModelURL:error:"
- "initWithNormalizedBoundingBox:andDomains:"
- "initWithNormalizedBoundingBox:regionAttributes:andSearchSections:"
- "initWithNormalizedCropRect:"
- "initWithObjectIdentifier:imageURL:thumbnailURL:metadata:"
- "initWithObservations:"
- "initWithPayload:andReportIdentifier:"
- "initWithPersonIdentifier:personName:mdID:detectionType:verified:boundingBox:andConfidence:"
- "initWithPixelBuffer:timestamp:orientation:"
- "initWithPixelBufferClassificationDictionary:error:"
- "initWithPolicyType:"
- "initWithPresentationTimeStamp:surface:"
- "initWithQueryTerm:"
- "initWithQueryTerm:domain:textContext:"
- "initWithRequestID:"
- "initWithResultItems:"
- "initWithResultItems:andPayload:"
- "initWithResultItems:andUserFeedbackPayload:"
- "initWithResultItems:frontCameraCaptureState:"
- "initWithScaledImageWidth:scaledImageHeight:"
- "initWithScaledImageWidth:scaledImageHeight:scalingModel:"
- "initWithSearchSections:"
- "initWithSensitivityAttributes:requestID:"
- "initWithService:"
- "initWithSession:"
- "initWithSharpnessScore:"
- "initWithSuiteName:"
- "initWithSummaryEntries:highlightEntries:curationScoreEntries:"
- "initWithSurface:"
- "initWithSurface:cropRect:"
- "initWithSurface:seed:"
- "initWithSymbologies:"
- "initWithText:"
- "initWithTimeRange:confidence:boundingBox:"
- "initWithTimeRange:frames:normalizedCropRect:"
- "initWithTimeRange:score:"
- "initWithTimeRange:score:attributes:"
- "initWithTokenIDs:"
- "initWithTokenIDs:error:"
- "initWithTopLeft:topRight:bottomLeft:bottomRight:symbology:payload:andDescriptor:"
- "initWithUniformTypeIdentifier:width:height:data:"
- "initWithUserFeedbackPayload:sfReportData:reportIdentifier:"
- "initWithVersion:data:type:"
- "initWithVersion:data:type:shape:"
- "initWithVisionRequest:error:"
- "initWithVisionResults:"
- "instanceMaskImage"
- "instanceMaskPixelBuffer"
- "instancePoint"
- "instances"
- "interfaceWithProtocol:"
- "invalidate"
- "isEntitled"
- "isEqualToString:"
- "isInitiallyHidden"
- "isLowConfidence"
- "isMemberOfClass:"
- "isSafe"
- "isSensitive"
- "isSensitiveGoreViolence"
- "isSensitiveNudity"
- "isValidRegionOfInterest:frameWidth:frameHeight:"
- "knowledgeGraphID"
- "knowledgeProperties"
- "label"
- "labels"
- "languages"
- "lastPathComponent"
- "length"
- "location"
- "mainBundle"
- "maskImagesForInstances:error:"
- "maskPixelBuffersForInstances:error:"
- "maskTime"
- "maxDimension"
- "maxFileSize"
- "maxInitiallyVisibleResults"
- "maxTokenSize"
- "maxTokenSizeForVersion:error:"
- "maximumAspectRatio"
- "maximumCandidateCount"
- "maximumFaceCount"
- "maximumHierarchicalObservations"
- "maximumLeafObservations"
- "maximumObservations"
- "mdID"
- "mean"
- "metadata"
- "minDimension"
- "minimumAspectRatio"
- "minimumConfidence"
- "minimumSize"
- "minimumTextHeight"
- "modelPreparationOnly"
- "modelType"
- "modelURL"
- "moreText"
- "mutableCopy"
- "newlineCharacterSet"
- "normalizedBoundingBox"
- "normalizedBoundingBoxes"
- "normalizedCropRect"
- "notifyLibraryAvailableAtURL:"
- "now"
- "nsfwObservations"
- "nsfwRevision"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectIdentifier"
- "observations"
- "orientation"
- "outputType"
- "passedGating"
- "path"
- "pauseWithRequestID:error:"
- "payload"
- "payloadStringValue"
- "performRequests:assetLocalIdentifier:photoLibraryURL:error:"
- "performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:completionHandler:"
- "performRequests:assetLocalIdentifier:photoLibraryURL:progressHandler:resultHandler:completionHandler:"
- "performRequests:assetURLs:options:progressHandler:resultsHandler:completionHandler:"
- "performRequests:multiModalInputs:completionHandler:"
- "performRequests:onAssetWithCloudIdentifier:completionHandler:"
- "performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:completionHandler:"
- "performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:error:"
- "performRequests:onAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:"
- "performRequests:onAssetWithLocalIdentifier:fromPhotoLibraryWithURL:completionHandler:"
- "performRequests:onAssetWithLocalIdentifier:fromPhotoLibraryWithURL:timeoutInterval:completionHandler:"
- "performRequests:onAssetWithSyndicationIdentifier:error:"
- "performRequests:onCGImage:withOrientation:andIdentifier:completionHandler:"
- "performRequests:onCGImage:withOrientation:andIdentifier:error:"
- "performRequests:onCGImage:withOrientation:assetLocalIdentifier:photoLibraryURL:completionHandler:"
- "performRequests:onCIImage:withOrientation:andIdentifier:completionHandler:"
- "performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:completionHandler:"
- "performRequests:onImageData:withUniformTypeIdentifier:andIdentifier:error:"
- "performRequests:onImageURL:completionHandler:"
- "performRequests:onImageURL:withIdentifier:completionHandler:"
- "performRequests:onImageURL:withIdentifier:error:"
- "performRequests:onPixelBuffer:withOrientation:andIdentifier:completionHandler:"
- "performRequests:onPixelBuffer:withOrientation:assetLocalIdentifier:photoLibraryURL:completionHandler:"
- "performRequests:onPixelBuffer:withOrientation:completionHandler:"
- "performRequests:pixelBuffer:options:progressHandler:resultsHandler:completionHandler:"
- "performRequests:text:identifier:completionHandler:"
- "performRequests:textInputs:completionHandler:"
- "performRequests:videoURL:identifier:progressHandler:completionHandler:"
- "performRequestsWithCloudIdentifiers:completionHandler:"
- "personIdentifier"
- "personName"
- "personalizationOptions"
- "personalized"
- "pixelBuffer"
- "pixelFormat"
- "pointValue"
- "policyType"
- "pooledEmbedding"
- "preprocessPixelBuffer:orientation:regionOfInterest:output:isProcessed:"
- "presentationTimeStamp"
- "prewarmMultiModalRequests:completionHandler:"
- "prewarmTextRequests:completionHandler:"
- "processFrameWithIOSurface:frameProperties:reply:"
- "processPixelBuffer:frameProperties:resultHandler:"
- "processPixelBuffer:orientation:regionOfInterest:scaledWidth:scaledHeight:pixelFormat:output:"
- "processPixelBuffer:timestamp:orientation:resultHandler:"
- "purgeResultsWithRequestID:error:"
- "q"
- "q16@0:8"
- "q24@0:8Q16"
- "q40@0:8q16@24^@32"
- "quadratureTolerance"
- "queryAssetsPendingDeferredProcessingWithPhotoLibraryURL:andReply:"
- "queryAutoCounterOptInStatus:withPhotoLibraryURL:personLocalIdentifiers:andReply:"
- "queryID"
- "queryImagePriority1MCEnableDate:photoLibraryURL:error:"
- "queryImagePriority1MCEnableDateWithPhotoLibraryURL:reply:"
- "queryPerformanceMeasurements"
- "queryPerformanceMeasurementsWithReply:"
- "queryTerm"
- "queryUserSafetyEnablement:"
- "queryVUIndexAssetCountForType:photoLibraryURL:completionHandler:"
- "queryVUIndexAssetCountForType:photoLibraryURL:error:"
- "queryVUIndexAssetCountForType:photoLibraryURL:reply:"
- "queryVUIndexLastFullModeClusterDate:photoLibraryURL:error:"
- "queryVUIndexLastFullModeClusterDateWithPhotoLibraryURL:completionHandler:"
- "queryVUIndexLastFullModeClusterDateWithPhotoLibraryURL:reply:"
- "rankingScore"
- "recognitionLevel"
- "recognizeObjectsRevision"
- "recognizedObjectObservations"
- "referralURL"
- "regionAttributes"
- "regionOfInterest"
- "registerProgressHandler:requestID:"
- "registerResultsHandler:requestID:"
- "registerUserSafetyPolicyUpdateHandler:error:"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeAllRequests"
- "removeItemAtURL:error:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "removeProgressHandlerForRequestID:"
- "removeRequest:"
- "removeRequest:error:"
- "removeRequest:reply:"
- "removeResultHandlerForRequestID:"
- "removeWithRequestID:reply:"
- "render:toCVPixelBuffer:"
- "reportIdentifier"
- "reportMADUserSafetyPolicy:error:"
- "reportProgress:forRequest:"
- "reportProgress:requestID:"
- "requestAnalysisXPCStoreListenerEndpointWithPhotoLibraryURL:reply:"
- "requestApplicationDataFolderIdentifierVisionServiceWithPhotosLibraryURL:error:"
- "requestAssetAnalysis:forLocalIdentifiers:fromPhotoLibraryWithURL:withOptions:analysisTypes:withReply:"
- "requestAssetAnalysis:forPhotoLibraryURL:withLocalIdentifiers:realTime:withReply:"
- "requestAssetProcessing:withTaskID:forLocalIdentifiers:fromPhotoLibraryWithURL:withOptions:andReply:"
- "requestAutoCounterAccuracyCalculation:withPhotoLibraryURL:andReply:"
- "requestAutoCounterAccuracyCalculation:withPhotoLibraryURL:clusterStateURL:groundTruthURL:andReply:"
- "requestAutoCounterSIMLValidation:withPhotoLibraryURL:simlGroundTruthURL:andReply:"
- "requestClusterCacheValidation:withPhotoLibraryURL:andReply:"
- "requestCollectionTheme:forLocalIdentifiers:fromPhotoLibraryWithURL:withOptions:andReply:"
- "requestCollectionThemeVersion:withOptions:andReply:"
- "requestDatabaseRestoreFastPassProcessing:reply:"
- "requestDeferredProcessingTypes:forAssetsWithLocalIdentifiers:withPhotoLibraryURL:andReply:"
- "requestDumpAutoCounter:withPhotoLibraryURL:andReply:"
- "requestFaceCandidatesforKeyFace:withPersonsWithLocalIdentifiers:andPhotoLibraryURL:andReply:"
- "requestForceDeferredProcessing:andReply:"
- "requestID"
- "requestIdentificationOfFacesWithLocalIdentifiers:fromPhotoLibraryWithURL:withRequestID:andReply:"
- "requestImageProcessing:forAssetURL:withSandboxToken:identifier:requestID:andReply:"
- "requestImageProcessing:forAssetWithCloudIdentifier:requestID:andReply:"
- "requestImageProcessing:forAssetWithIdentifier:identifierType:fromPhotoLibraryWithURL:requestID:andReply:"
- "requestImageProcessing:forIOSurface:withOrientation:assetLocalIdentifier:photoLibraryURL:requestID:andReply:"
- "requestImageProcessing:forIOSurface:withOrientation:identifier:requestID:andReply:"
- "requestImageProcessing:forImageData:withUniformTypeIdentifier:identifier:requestID:andReply:"
- "requestImageProcessingWithCloudIdentifierRequests:requestID:andReply:"
- "requestLibraryProcessing:withTaskID:forPhotoLibraryURL:withOptions:andReply:"
- "requestMediaAnalysisDatabaseAccessSandboxExtensionWithPhotoLibraryURL:andReply:"
- "requestMultiModalPrewarming:requestID:reply:"
- "requestOTAMaintenance:options:reply:"
- "requestOptInAutoCounter:withPhotoLibraryURL:persons:andReply:"
- "requestPersonPreferenceForPhotoLibraryURL:andReply:"
- "requestPersonPromoterStatus:withAdvancedFlag:andPhotoLibraryURL:andReply:"
- "requestPhotosDeferredProcessing:reply:"
- "requestPhotosFaceFastPassProcessing:withPhotoLibraryURL:andReply:"
- "requestPhotosSceneFastPassProcessing:withPhotoLibraryURL:andReply:"
- "requestProcessing:assetURLs:extensionData:resultDirectoryURL:resultExtensionData:requestID:reply:"
- "requestProcessing:localIdentifiers:photoLibraryURL:resultDirectoryURL:resultExtensionData:requestID:reply:"
- "requestProcessing:multiModalInputs:requestID:reply:"
- "requestProcessingTypes:forAssetsWithLocalIdentifiers:fromPhotoLibraryWithURL:withRequestID:andReply:"
- "requestProgressReport:reply:"
- "requestRebuildPersons:withLocalIdentifiers:andPhotoLibraryURL:andReply:"
- "requestRecentsProcessing:withTaskID:photoLibraryWithURL:reply:"
- "requestReclusterFaces:withPhotoLibraryURL:andReply:"
- "requestResetFaceClassificationModel:withPhotoLibraryURL:andReply:"
- "requestResetFaceClusteringState:withPhotoLibraryURL:andReply:"
- "requestResetPersons:withPhotoLibraryURL:andReply:"
- "requestResetPetClassificationModel:withPhotoLibraryURL:andReply:"
- "requestResetProcessingStatus:taskID:photoLibraryURL:options:reply:"
- "requestStaticStickerScoring:photoLibraryURL:options:reply:"
- "requestSuggestedMePersonIdentifier:withContext:andPhotoLibraryURL:andReply:"
- "requestSuggestedPersons:withPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:andPhotoLibraryURL:andReply:"
- "requestSystemXPCStoreListenerEndpoint:"
- "requestTTRNotificationWithVideoFrames:options:completionHandler:"
- "requestTTRNotificationWithVideoFrames:options:reply:"
- "requestTextPrewarming:requestID:reply:"
- "requestTextProcessing:textInputs:requestID:reply:"
- "requestURLAssetAnalysis:forAssetWithResourcePaths:withOptions:analysisTypes:sandboxTokens:withReply:"
- "requestUpdateKeyFacesOfPersons:withLocalIdentifiers:andForceUpdate:andPhotoLibraryURL:andReply:"
- "requestVIPModelStorageFilepathForPhotoLibraryURL:forModelType:andReply:"
- "requestVUIndexURLForPhotoLibraryURL:error:"
- "requestVUIndexURLForSystemPhotosLibraryWithError:"
- "requestVideoFramesProcessing:withTaskID:frames:options:andReply:"
- "requestVideoProcessing:assetIdentifier:identifierType:photoLibraryURL:requestID:isIncremental:reply:"
- "requestVideoProcessing:assetURL:sandboxToken:identifier:requestID:reply:"
- "requestVisionCacheStorageDirectoryURLForPhotoLibraryURL:reply:"
- "requestWallpaperUpgrade:atSourceURL:toDestinationURL:withOptions:sandboxTokens:andReply:"
- "requestWithModelURL:error:"
- "requestWithVisionRequest:error:"
- "requiresBlastdoor"
- "requiresScoresAndLabels"
- "resetPerformanceMeasurements"
- "resourceURL"
- "result"
- "resultDirectoryURL"
- "resultItems"
- "resultWithClassifications:"
- "resultWithDetectedFaces:"
- "resultWithExposureScore:"
- "resultWithSharpnessScore:"
- "resultWithSummaryEntries:highlightEntries:curationScoreEntries:"
- "resultWithVisionResults:"
- "results"
- "resume"
- "resumeWithRequestID:progressHandler:resultsHandler:completionHandler:"
- "resumeWithRequestID:reply:"
- "revision"
- "richLabelResult"
- "s"
- "s16@0:8"
- "safetyScore"
- "safetyType"
- "saliencyObservations"
- "saliencyRevision"
- "salientObjects"
- "sampling"
- "sandboxExtensionForURL:error:"
- "scale"
- "scaledImageHeight"
- "scaledImageWidth"
- "scalingModelIndex"
- "scheduleProcessing:assetURLs:extensionData:resultDirectoryURL:resultExtensionData:requestID:reply:"
- "scheduleProcessing:localIdentifiers:photoLibraryURL:resultDirectoryURL:resultExtensionData:requestID:reply:"
- "scheduleRequests:assetURLs:options:error:"
- "score"
- "scoresForLabels"
- "searchSections"
- "seed"
- "segments"
- "sensitiveFrameCountThreshold"
- "serverProtocol"
- "service"
- "serviceName"
- "session"
- "setAllowOnDemand:"
- "setAllowTruncation:"
- "setAllowUnverifiedIdentity:"
- "setAppliesPreferredTrackTransform:"
- "setBypassFaceDetection:"
- "setBypassNormalizaton:"
- "setCalibrate:"
- "setCatalogIDs:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClassificationObservations:"
- "setComputeSafety:"
- "setComputeThreshold:"
- "setComputeUnits:"
- "setConversationIdentifier:"
- "setCropResult:"
- "setDateFormat:"
- "setDomains:"
- "setEmbeddingRequestType:"
- "setEnableDetectionTypeGV:"
- "setEnableDetectionTypeN:"
- "setEnableGoreViolenceDetection:"
- "setEnableNudityDetection:"
- "setEngagementSuggestionType:"
- "setError:"
- "setEventDate:"
- "setExecutionNanoseconds:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExtendedContextLength:"
- "setFaceAttributesObservations:"
- "setFaceDetectorVisionRevision:"
- "setFaceExpressionsObservations:"
- "setFaceLandmarksObservations:"
- "setFaceRectanglesObservations:"
- "setFaceprintObservations:"
- "setFeatureIdentifier:"
- "setHintDomain:"
- "setImageType:"
- "setImageURL:"
- "setInPlace:"
- "setIncludePets:"
- "setInstancePoint:"
- "setInstances:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLanguages:"
- "setLocation:"
- "setMaskTime:"
- "setMaxDimension:"
- "setMaxFileSize:"
- "setMaximumAspectRatio:"
- "setMaximumCandidateCount:"
- "setMaximumFaceCount:"
- "setMaximumObservations:"
- "setMinDimension:"
- "setMinimumAspectRatio:"
- "setMinimumConfidence:"
- "setMinimumSize:"
- "setMinimumTextHeight:"
- "setModelPreparationOnly:"
- "setNSFWObservations:"
- "setNormalizedBoundingBoxes:"
- "setObject:forKeyedSubscript:"
- "setOrientation:"
- "setOutputType:"
- "setPersonalizationOptions:"
- "setQuadratureTolerance:"
- "setQueryID:"
- "setRecognitionLevel:"
- "setRecognizedObjectObservations:"
- "setReferralURL:"
- "setRegionOfInterest:"
- "setRemoteObjectInterface:"
- "setRequiresBlastdoor:"
- "setRequiresScoresAndLabels:"
- "setResults:"
- "setRevision:"
- "setSafetyScore:isSafe:"
- "setSaliencyObservations:"
- "setSampling:"
- "setSensitiveFrameCountThreshold:"
- "setSignificantEventObservations:"
- "setStagedText:"
- "setStartDate:"
- "setStickerIdentifiers:"
- "setStreamID:"
- "setSurroundingText:"
- "setTargetBounds:"
- "setThirdPartyObject:"
- "setTimestamp:"
- "setTruncated:"
- "setType:"
- "setUiScale:"
- "setUseLowResolutionPicture:"
- "setUseVIPModel:"
- "setUsesFormFieldDetection:"
- "setUsesLanguageCorrection:"
- "setUsesLanguageDetection:"
- "setUuid:"
- "setVersion:"
- "setWithArray:"
- "sfReportData"
- "shape"
- "sharpnessScore"
- "shortDescription"
- "significantEventObservations"
- "significantEventRevision"
- "sourceRegionOfInterest"
- "stagedText"
- "standardDeviation"
- "startAccessingSecurityScopedResource"
- "startDate"
- "startEntryPointWithQueryID:"
- "startEntryPointWithQueryID:andEvent:"
- "stickerIdentifiers"
- "stopAccessingSecurityScopedResource"
- "streamID"
- "string"
- "stringFromDate:"
- "stringValue"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "submitSearchableItem:completionHandler:"
- "submitSpotlightAssetURL:uniqueIdentifier:bundleIdentifier:completionHandler:"
- "submitSpotlightAssetURL:uniqueIdentifier:bundleIdentifier:typeIdentifier:sandboxToken:reply:"
- "subscribeUserSafety:"
- "summaryEntries"
- "supportsSecureCoding"
- "surface"
- "surroundingText"
- "symbologies"
- "symbology"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "targetBounds"
- "targetResolution"
- "text"
- "thirdPartyObject"
- "threshold"
- "thumbnailAspectRatio"
- "thumbnailURL"
- "timeRange"
- "timerWithInterval:unit:oneShot:andBlock:"
- "timerWithIntervalSeconds:isOneShot:andBlock:"
- "timerange"
- "timestamp"
- "title"
- "tokenIDs"
- "tokenizationResults"
- "tokenizerRevision"
- "topLeft"
- "topRight"
- "truncated"
- "type"
- "typeWithIdentifier:"
- "uiScale"
- "unarchivedObjectOfClass:fromData:error:"
- "uniformSampling"
- "uniformTypeIdentifier"
- "uniqueIdentifier"
- "unsignedIntegerValue"
- "useLowResolutionPicture"
- "useVIPModel"
- "userFeedbackPayload"
- "userInfo"
- "userSafetyEnabled:"
- "usesFormFieldDetection"
- "usesLanguageCorrection"
- "usesLanguageDetection"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"NSURL\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?Q>16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v28@0:8@?16i24"
- "v28@0:8d16i24"
- "v28@0:8i16@?20"
- "v28@0:8i16@?<v@?@\"NSError\">20"
- "v32@0:8@\"MADUserSafetyPolicy\"16@\"NSError\"24"
- "v32@0:8@\"MADVideoSessionRequest\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSDate\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSString\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSURL\"@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16Q24"
- "v32@0:8d16@\"NSString\"24"
- "v32@0:8d16@24"
- "v36@0:8@\"MADVideoResultsPayload\"16Q24i32"
- "v36@0:8@\"NSArray\"16i24@?<v@?@\"NSError\">28"
- "v36@0:8@\"NSDictionary\"16i24@?<v@?@\"NSDictionary\"@\"NSError\">28"
- "v36@0:8@16Q24i32"
- "v36@0:8@16i24@?28"
- "v36@0:8i16@\"NSDictionary\"20@?<v@?@\"NSError\">28"
- "v36@0:8i16@\"NSDictionary\"20@?<v@?@\"NSNumber\"@\"NSError\">28"
- "v36@0:8i16@\"NSURL\"20@?<v@?@\"NSDictionary\"@\"NSError\">28"
- "v36@0:8i16@\"NSURL\"20@?<v@?@\"NSError\">28"
- "v36@0:8i16@\"NSURL\"20@?<v@?B@\"NSError\">28"
- "v36@0:8i16@20@?28"
- "v40@0:8@\"IOSurface\"16@\"MADVideoSessionFrameProperties\"24@?<v@?@\"NSArray\"{?=qiIq}@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"MADVideoSessionTTROptions\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSURL\"16Q24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8Q16Q24@\"NSString\"32"
- "v40@0:8Q16Q24@32"
- "v40@0:8i16B20@\"NSURL\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8i16B20@24@?32"
- "v40@0:8q16@\"NSURL\"24@?<v@?q@\"NSError\">32"
- "v40@0:8q16@24@?32"
- "v40@0:8{?=qiIq}16"
- "v44@0:8@\"NSArray\"16@\"NSArray\"24i32@?<v@?@\"NSArray\"@\"NSError\">36"
- "v44@0:8@\"NSArray\"16@\"NSString\"24i32@?<v@?@\"NSArray\"@\"NSError\">36"
- "v44@0:8@\"NSArray\"16@\"NSURL\"24i32@?<v@?@\"NSDictionary\"@\"NSError\">36"
- "v44@0:8@16@24i32@?36"
- "v44@0:8i16@\"NSArray\"20@\"NSURL\"28@?<v@?@\"NSArray\"@\"NSError\">36"
- "v44@0:8i16@\"NSArray\"20@\"NSURL\"28@?<v@?B@\"NSError\">36"
- "v44@0:8i16@\"NSDictionary\"20@\"NSURL\"28@?<v@?@\"NSString\"@\"NSError\">36"
- "v44@0:8i16@\"NSURL\"20@\"NSArray\"28@?<v@?@\"NSDictionary\"@\"NSError\">36"
- "v44@0:8i16@\"NSURL\"20@\"NSDictionary\"28@?<v@?@\"NSError\">36"
- "v44@0:8i16@\"NSURL\"20@\"NSURL\"28@?<v@?@\"NSDictionary\"@\"NSError\">36"
- "v44@0:8i16@20@28@?36"
- "v44@0:8i16Q20@\"NSURL\"28@?<v@?@\"NSError\">36"
- "v44@0:8i16Q20@28@?36"
- "v48@0:8@\"NSIndexSet\"16@\"NSArray\"24@\"NSURL\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@?24@?32@?40"
- "v48@0:8i16@\"NSArray\"20B28@\"NSURL\"32@?<v@?B@\"NSError\">40"
- "v48@0:8i16@\"NSURL\"20@\"NSArray\"28B36@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8i16@20@28B36@?40"
- "v48@0:8i16@20B28@32@?40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v52@0:8Q16@\"NSArray\"24@\"NSURL\"32i40@?<v@?@\"NSError\">44"
- "v52@0:8Q16@24@32i40@?44"
- "v52@0:8i16@\"NSArray\"20@\"NSURL\"28@\"NSDictionary\"36@?<v@?@\"NSDictionary\"@\"NSError\">44"
- "v52@0:8i16@\"NSURL\"20@\"NSURL\"28@\"NSURL\"36@?<v@?@\"NSDictionary\"@\"NSError\">44"
- "v52@0:8i16@20@28@36@?44"
- "v52@0:8i16Q20@\"NSArray\"28@\"NSDictionary\"36@?<v@?@\"NSDictionary\"@\"NSError\">44"
- "v52@0:8i16Q20@\"NSURL\"28@\"NSDictionary\"36@?<v@?@\"NSError\">44"
- "v52@0:8i16Q20@28@36@?44"
- "v56@0:8@\"NSArray\"16@\"IOSurface\"24I32@\"NSString\"36i44@?<v@?@\"NSArray\"@\"NSError\">48"
- "v56@0:8@\"NSArray\"16@24@\"NSString\"32@\"NSError\"40@?<v@?B>48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24I32@36i44@?48"
- "v60@0:8@\"NSArray\"16@\"NSData\"24@\"UTType\"32@\"NSString\"40i48@?<v@?@\"NSArray\"@\"NSError\">52"
- "v60@0:8@\"NSArray\"16@\"NSString\"24Q32@\"NSURL\"40i48@?<v@?@\"NSArray\"@\"NSError\">52"
- "v60@0:8@\"NSArray\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40i48@?<v@?@\"NSArray\"@\"NSError\">52"
- "v60@0:8@16@24@32@40i48@?52"
- "v60@0:8@16@24Q32@40i48@?52"
- "v60@0:8i16@\"NSArray\"20@\"NSDictionary\"28Q36@\"NSArray\"44@?<v@?@\"NSDictionary\"@\"NSError\">52"
- "v60@0:8i16@\"NSArray\"20@\"NSURL\"28@\"NSDictionary\"36Q44@?<v@?@\"NSDictionary\"@\"NSError\">52"
- "v60@0:8i16@\"NSString\"20@\"NSArray\"28@\"NSArray\"36@\"NSURL\"44@?<v@?@\"NSArray\"@\"NSError\">52"
- "v60@0:8i16@\"NSURL\"20@\"NSURL\"28@\"NSDictionary\"36@\"NSArray\"44@?<v@?@\"NSDictionary\"@\"NSError\">52"
- "v60@0:8i16@20@28@36@44@?52"
- "v60@0:8i16@20@28@36Q44@?52"
- "v60@0:8i16@20@28Q36@44@?52"
- "v60@0:8i16Q20@\"NSArray\"28@\"NSURL\"36@\"NSDictionary\"44@?<v@?@\"NSDictionary\"@\"NSError\">52"
- "v60@0:8i16Q20@28@36@44@?52"
- "v64@0:8@\"NSArray\"16@\"IOSurface\"24I32@\"NSString\"36@\"NSURL\"44i52@?<v@?@\"NSArray\"@\"NSError\">56"
- "v64@0:8@\"NSArray\"16@\"NSString\"24Q32@\"NSURL\"40i48B52@?<v@?@\"NSArray\"@\"NSError\">56"
- "v64@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "v64@0:8@16@24I32@36@44i52@?56"
- "v64@0:8@16@24Q32@40i48B52@?56"
- "v72@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@\"NSURL\"40@\"NSData\"48@\"NSString\"56@?<v@?@\"NSError\">64"
- "v72@0:8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@\"NSURL\"40@\"NSData\"48@\"NSString\"56@?<v@?B@\"NSError\">64"
- "v72@0:8@\"NSArray\"16@\"NSArray\"24@\"NSURL\"32@\"NSURL\"40@\"NSData\"48@\"NSString\"56@?<v@?@\"NSError\">64"
- "v72@0:8@\"NSArray\"16@\"NSArray\"24@\"NSURL\"32@\"NSURL\"40@\"NSData\"48@\"NSString\"56@?<v@?B@\"NSError\">64"
- "v72@0:8@16@24@32@40@48@56@?64"
- "version"
- "videoEntries"
- "visionRequest"
- "visionResults"
- "webURL"
- "width"
- "{?=\"start\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"duration\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}}"
- "{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}"
- "{?=qiIq}16@0:8"
- "{?={?=qiIq}{?=qiIq}}16@0:8"
- "{CF<CGImage *>=\"value_\"^{CGImage}}"
- "{CF<OpaqueVTPixelRotationSession *>=\"value_\"^{OpaqueVTPixelRotationSession}}"
- "{CF<OpaqueVTPixelTransferSession *>=\"value_\"^{OpaqueVTPixelTransferSession}}"
- "{CF<__CVBuffer *>=\"value_\"^{__CVBuffer}}"
- "{CF<__CVPixelBufferPool *>=\"value_\"^{__CVPixelBufferPool}}"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{atomic<int>=\"__a_\"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>=\"__a_value\"Ai}}"

```
