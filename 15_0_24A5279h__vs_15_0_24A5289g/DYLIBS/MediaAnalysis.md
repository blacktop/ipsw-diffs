## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/Versions/A/MediaAnalysis`

```diff

-255.62.1.15.1
-  __TEXT.__text: 0x3fe774
-  __TEXT.__auth_stubs: 0x3000
-  __TEXT.__objc_methlist: 0x18754
-  __TEXT.__const: 0x13f38
-  __TEXT.__gcc_except_tab: 0x4e580
-  __TEXT.__cstring: 0x22969
-  __TEXT.__oslogstring: 0x21c0b
+255.67.2.0.0
+  __TEXT.__text: 0x404648
+  __TEXT.__auth_stubs: 0x3160
+  __TEXT.__objc_methlist: 0x188fc
+  __TEXT.__const: 0x13f58
+  __TEXT.__gcc_except_tab: 0x4eee8
+  __TEXT.__cstring: 0x23167
+  __TEXT.__oslogstring: 0x224ab
   __TEXT.__dlopen_cstrs: 0x3e7
   __TEXT.__ustring: 0x40
   __TEXT.__swift5_typeref: 0x9c

   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0xf268
+  __TEXT.__unwind_info: 0xf360
   __TEXT.__eh_frame: 0x1e0
-  __TEXT.__objc_classname: 0x392d
-  __TEXT.__objc_methname: 0x36364
-  __TEXT.__objc_methtype: 0xc278
-  __TEXT.__objc_stubs: 0x249e0
-  __DATA_CONST.__got: 0x17a0
-  __DATA_CONST.__const: 0x25f8
-  __DATA_CONST.__objc_classlist: 0x1000
+  __TEXT.__objc_classname: 0x3994
+  __TEXT.__objc_methname: 0x36aa7
+  __TEXT.__objc_methtype: 0xc499
+  __TEXT.__objc_stubs: 0x24e60
+  __DATA_CONST.__got: 0x17e0
+  __DATA_CONST.__const: 0x2640
+  __DATA_CONST.__objc_classlist: 0x1020
   __DATA_CONST.__objc_catlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaff8
+  __DATA_CONST.__objc_selrefs: 0xb128
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0xd70
-  __DATA_CONST.__objc_arraydata: 0xaa0
-  __AUTH_CONST.__auth_got: 0x1818
+  __DATA_CONST.__objc_superrefs: 0xd78
+  __DATA_CONST.__objc_arraydata: 0xa80
+  __AUTH_CONST.__auth_got: 0x18c8
   __AUTH_CONST.__auth_ptr: 0x108
-  __AUTH_CONST.__const: 0x8840
-  __AUTH_CONST.__cfstring: 0x130e0
-  __AUTH_CONST.__objc_const: 0x33448
+  __AUTH_CONST.__const: 0x8850
+  __AUTH_CONST.__cfstring: 0x13660
+  __AUTH_CONST.__objc_const: 0x339c0
   __AUTH_CONST.__objc_floatobj: 0x260
   __AUTH_CONST.__objc_doubleobj: 0x1d0
-  __AUTH_CONST.__objc_intobj: 0x26d0
-  __AUTH_CONST.__objc_arrayobj: 0x8b8
+  __AUTH_CONST.__objc_intobj: 0x26e8
+  __AUTH_CONST.__objc_arrayobj: 0x8a0
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0xa100
+  __AUTH.__objc_data: 0xa240
   __AUTH.__data: 0x168
   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_data: 0x40
   __AUTH.__thread_bss: 0x9c9
-  __DATA.__objc_ivar: 0x2d3c
+  __DATA.__objc_ivar: 0x2d94
   __DATA.__data: 0x1728
-  __DATA.__bss: 0x1041
+  __DATA.__bss: 0x1021
   __DATA.__common: 0x3b9
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/Stickers.framework/Versions/A/Stickers
   - /System/Library/PrivateFrameworks/VectorSearch.framework/Versions/A/VectorSearch
+  - /System/Library/PrivateFrameworks/VisionCore.framework/Versions/A/VisionCore
   - /System/Library/PrivateFrameworks/VisualIntelligence.framework/Versions/A/VisualIntelligence
   - /System/Library/PrivateFrameworks/VisualUnderstanding.framework/Versions/A/VisualUnderstanding
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 14699
-  Symbols:   35211
-  CStrings:  3583
+  Functions: 14750
+  Symbols:   35395
+  CStrings:  3629
 
Symbols:
+ +[MADEmbedding prewarmSearchWithConcurrencyLimit:photoLibraryURL:error:]
+ +[MADEmbeddingStore prewarmSearchWithConcurrencyLimit:photoLibraryURL:error:]
+ +[PHAsset(MediaAnalysis) vcp_shortMovieDurationThreshold]
+ +[VCPANSTHandsDetector anstHandsDetectorWithExtendRatio:options:]
+ -[Container buffer]
+ -[Container setBuffer:]
+ -[MADEmbeddingStoreService prewarmSearchWithConcurrencyLimit:photoLibraryURL:error:]
+ -[MADGenerativePlaygroundsMD1TextEncoderResource additionalLayerNames]
+ -[MADGenerativePlaygroundsMD1TextEncoderResource revision]
+ -[MADGenerativePlaygroundsMD1TextEncoderResource tokenEmbeddingType]
+ -[MADGenerativePlaygroundsMD1TextEncoderResource version]
+ -[MADGenerativePlaygroundsMD4TextEncoderResource additionalLayerNames]
+ -[MADGenerativePlaygroundsMD4TextEncoderResource revision]
+ -[MADGenerativePlaygroundsMD4TextEncoderResource tokenEmbeddingType]
+ -[MADGenerativePlaygroundsMD4TextEncoderResource version]
+ -[MADVSKClient .cxx_destruct]
+ -[MADVSKClient cooldown]
+ -[MADVSKClient countWithError:]
+ -[MADVSKClient dealloc]
+ -[MADVSKClient deleteStringIdentifiers:error:]
+ -[MADVSKClient embeddingCountWithError:]
+ -[MADVSKClient initWithConfig:error:]
+ -[MADVSKClient insertAssets:error:]
+ -[MADVSKClient isPrewarmed]
+ -[MADVSKClient rebuildWithError:]
+ -[MADVSKClient searchByBatch:stringIdentifiers:attributeFilters:limit:fullScan:includePayload:numberOfProbes:batchSize:numConcurrentReaders:error:]
+ -[MADVSKClient stringIdentifiedAssetsWithIdentifiers:attributeFilters:pagination:error:]
+ -[MADVSKClient warmup]
+ -[MADVectorDatabase prewarmSearchWithConcurrencyLimit:]
+ -[PHPhotoLibrary(MediaAnalysis) mad_calculateProgressPercentage:progressPercentageWithFailure:taskID:phTaskID:priority:failedAssetCount:error:]
+ -[VCPANSTHandsBodyDetector anstDetection:rotationInDegrees:detectingFullbody:detectingHands:handsRegions:personRegions:cancel:].cold.3
+ -[VCPANSTHandsBodyDetector anstDetection:rotationInDegrees:detectingFullbody:detectingHands:handsRegions:personRegions:cancel:].cold.4
+ -[VCPANSTHandsDetector handsDetection:rotationInDegrees:handsRegions:cancel:].cold.3
+ -[VCPANSTHandsDetector initWithExtendRatio:options:]
+ -[VCPANSTHandsDetector initWithExtendRatio:options:].cold.1
+ -[VCPAsset(Movie) isShortMovie]
+ -[VCPCNNModelEspressoV2 createPrecompiledOp:isPrecompiled:functionName:]
+ -[VCPCNNVisionCoreDetector .cxx_construct]
+ -[VCPCNNVisionCoreDetector .cxx_destruct]
+ -[VCPCNNVisionCoreDetector UpdateInputBuffersAndBindPixelBuffer:]
+ -[VCPCNNVisionCoreDetector allocatePostProcessingBuffers:error:]
+ -[VCPCNNVisionCoreDetector dealloc]
+ -[VCPCNNVisionCoreDetector downscaleBuffer:scaledImage:]
+ -[VCPCNNVisionCoreDetector downscaleBuffer:scaledImage:].cold.1
+ -[VCPCNNVisionCoreDetector downscaleBuffer:scaledImage:].cold.2
+ -[VCPCNNVisionCoreDetector getBodyRegions:fromVisionCorePostProcessingOutput:imageWidth:imageHeight:extendRatio:portrait_mode:]
+ -[VCPCNNVisionCoreDetector getHandsRegions:fromVisionCorePostProcessingOutput:imageWidth:imageHeight:extendRatio:portrait_mode:]
+ -[VCPCNNVisionCoreDetector initWithOptions:]
+ -[VCPCNNVisionCoreDetector initWithOptions:].cold.1
+ -[VCPCNNVisionCoreDetector loadModel:withOptions:]
+ -[VCPCNNVisionCoreDetector planExecutionandOutput:descriptor:]
+ -[VCPCNNVisionCoreDetector resultForPixelBuffer:orientation:Error:]
+ -[VCPMediaAnalyzer searchForQuery:forAssets:withOptions:matchingScoreOnly:isURLAsset:analyses:]
+ -[VCPPhotosAsset(Movie) isShortMovie]
+ GCC_except_table209
+ GCC_except_table217
+ GCC_except_table236
+ GCC_except_table267
+ GCC_except_table282
+ GCC_except_table289
+ GCC_except_table294
+ GCC_except_table298
+ GCC_except_table312
+ OBJC_IVAR_$_Container._buffer
+ OBJC_IVAR_$_MADVSKClient._client
+ OBJC_IVAR_$_MADVSKClient._isPrewarmed
+ OBJC_IVAR_$_VCPANSTHandsBodyDetector._useVisionCore
+ OBJC_IVAR_$_VCPANSTHandsBodyDetector._visionCoreDetector
+ OBJC_IVAR_$_VCPANSTHandsDetector._useVisionCore
+ OBJC_IVAR_$_VCPANSTHandsDetector._visionCoreDetector
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._descriptor
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._espressoContext
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._espressoNetwork
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._frameCount
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._hairBuffer
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._inferenceOutputNamedObjects
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._inputBufferMapping
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._inputMasksNames
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._outputBufferMapping
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._outputEspressoBuffers
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._personBuffer
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._postProcessingObjects
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._salientBuffer
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._scaler
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._skinBuffer
+ OBJC_IVAR_$_VCPCNNVisionCoreDetector._skyBuffer
+ _OBJC_CLASS_$_Container
+ _OBJC_CLASS_$_MADGenerativePlaygroundsMD1TextEncoderResource
+ _OBJC_CLASS_$_MADGenerativePlaygroundsMD4TextEncoderResource
+ _OBJC_CLASS_$_MADVSKClient
+ _OBJC_CLASS_$_VCPCNNVisionCoreDetector
+ _OBJC_CLASS_$_VisionCoreISPInferenceNetworkDescriptor
+ _OBJC_CLASS_$_VisionCoreISPInferenceNetworkPostProcessingInput
+ _OBJC_CLASS_$_VisionCoreISPInferenceNetworkPostProcessingOutput
+ _OBJC_CLASS_$_VisionCoreImageTensorDescriptor
+ _OBJC_CLASS_$_VisionCoreMutableNamedObjects
+ _OBJC_CLASS_$_VisionCoreResourceVersion
+ _OBJC_CLASS_$_VisionCoreTensorDescriptor
+ _OBJC_METACLASS_$_Container
+ _OBJC_METACLASS_$_MADGenerativePlaygroundsMD1TextEncoderResource
+ _OBJC_METACLASS_$_MADGenerativePlaygroundsMD4TextEncoderResource
+ _OBJC_METACLASS_$_MADVSKClient
+ _OBJC_METACLASS_$_VCPCNNVisionCoreDetector
+ _VCPKeyValueMediaAnalysisImageCheckpointWithFailureReportedTimestamp
+ _VCPKeyValueMediaAnalysisImagePriority1CheckpointWithFailureReportedTimestamp
+ _VCPKeyValueMediaAnalysisImagePriority1ProgressPercentageWithFailure
+ _VCPKeyValuePrioritizedFaceAnalysisCompleteWithFailureTimestamp
+ _VCPKeyValuePrioritizedFaceAnalysisProgressPercentageWithFailure
+ _VCPKeyValuePrioritizedFaceCheckpointWithFailureReportedTimestamp
+ _VisionCoreEspressoStorageTypeForTensorDataType
+ _VisionCoreISPInferenceNetworkIdentifier512x384
+ __103-[VCPFaceProcessingServiceWorker faceCandidatesforKeyFaceForPersonsWithLocalIdentifiers:context:reply:]_block_invoke.448
+ __103-[VCPPhotosPersistenceDelegate _processNewlyClusteredFaceCropsInFaceGroups:cancelOrExtendTimeoutBlock:]_block_invoke.665
+ __103-[VCPPhotosPersistenceDelegate _processNewlyClusteredFaceCropsInFaceGroups:cancelOrExtendTimeoutBlock:]_block_invoke.669
+ __104-[VCPPhotosQuickFaceIdentificationManager processAsset:onDemandDetection:detectedFaces:detectedPersons:]_block_invoke.287
+ __108-[VCPPhotosPersistenceDelegate _adjustConfirmingAndRejectionWithFaces:faceCrops:cancelOrExtendTimeoutBlock:]_block_invoke.627
+ __108-[VCPPhotosPersistenceDelegate _adjustConfirmingAndRejectionWithFaces:faceCrops:cancelOrExtendTimeoutBlock:]_block_invoke.633
+ __108-[VCPPhotosPersistenceDelegate _adjustConfirmingAndRejectionWithFaces:faceCrops:cancelOrExtendTimeoutBlock:]_block_invoke.642
+ __108-[VCPPhotosPersistenceDelegate _adjustConfirmingAndRejectionWithFaces:faceCrops:cancelOrExtendTimeoutBlock:]_block_invoke.644
+ __108-[VCPPhotosPersistenceDelegate _adjustConfirmingAndRejectionWithFaces:faceCrops:cancelOrExtendTimeoutBlock:]_block_invoke_2.643
+ __113-[VCPClusterer _processingQueueSyncClustererWithPhotoLibraryUsingFacesInClusterCache:cancelOrExtendTimeoutBlock:]_block_invoke.381
+ __113-[VCPClusterer _processingQueueSyncClustererWithPhotoLibraryUsingFacesInClusterCache:cancelOrExtendTimeoutBlock:]_block_invoke.385
+ __113-[VCPClusterer _processingQueueSyncClustererWithPhotoLibraryUsingFacesInClusterCache:cancelOrExtendTimeoutBlock:]_block_invoke.386
+ __113-[VCPClusterer _processingQueueSyncClustererWithPhotoLibraryUsingFacesInClusterCache:cancelOrExtendTimeoutBlock:]_block_invoke.388
+ __113-[VCPClusterer _processingQueueSyncClustererWithPhotoLibraryUsingFacesInClusterCache:cancelOrExtendTimeoutBlock:]_block_invoke.389
+ __116-[VCPClusterer differencesBetweenClusterCacheAndLibrary:excludedL0ClustersByL1ClusterId:cancelOrExtendTimeoutBlock:]_block_invoke.506
+ __116-[VCPClusterer differencesBetweenClusterCacheAndLibrary:excludedL0ClustersByL1ClusterId:cancelOrExtendTimeoutBlock:]_block_invoke.512
+ __119-[VCPClusterer _resolveConflictingL0ClustersFromVNClusters:excludedL0ClustersByL1ClusterId:cancelOrExtendTimeoutBlock:]_block_invoke.500
+ __121-[VCPPhotosPersistenceDelegate updateKeyFacesOfPersonsWithLocalIdentifiers:forceUpdate:cancelOrExtendTimeoutBlock:error:]_block_invoke.516
+ __121-[VCPPhotosQuickFaceIdentificationManager personIdentificationForSyndicationPhotoLibrary:withCancelOrExtendTimeoutBlock:]_block_invoke.320
+ __121-[VCPPhotosQuickFaceIdentificationManager personIdentificationForSyndicationPhotoLibrary:withCancelOrExtendTimeoutBlock:]_block_invoke.325
+ __128-[VCPPhotosPersistenceDelegate _cleanupMergeCandidatesForVerifiedPersons:minimumFaceGroupSize:cancelOrExtendTimeoutBlock:error:]_block_invoke.580
+ __128-[VCPPhotosPersistenceDelegate _cleanupMergeCandidatesForVerifiedPersons:minimumFaceGroupSize:cancelOrExtendTimeoutBlock:error:]_block_invoke.583
+ __131-[VCPPhotosQuickFaceIdentificationManager _generatePersonsModelWithExtendTimeoutBlock:cancel:evaluationMode:allowUnverifiedPerson:]_block_invoke.385
+ __131-[VCPPhotosQuickFaceIdentificationManager _generatePersonsModelWithExtendTimeoutBlock:cancel:evaluationMode:allowUnverifiedPerson:]_block_invoke.389
+ __135-[VCPPhotosPersistenceDelegate _buildPersonsFromUpdatedFaceGroups:faceClusterer:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:]_block_invoke.671
+ __135-[VCPPhotosPersistenceDelegate _buildPersonsFromUpdatedFaceGroups:faceClusterer:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:]_block_invoke.685
+ __135-[VCPPhotosPersistenceDelegate _buildPersonsFromUpdatedFaceGroups:faceClusterer:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:]_block_invoke.699
+ __135-[VCPPhotosPersistenceDelegate _buildPersonsFromUpdatedFaceGroups:faceClusterer:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:]_block_invoke.738
+ __137-[VCPPhotosAutoCounterWorker _reportCoreAnalyticsWithVisionClusterMeasure:personClusterMeasure:personClusters:andGroundTruthInformation:]_block_invoke.598
+ __137-[VCPPhotosAutoCounterWorker _reportCoreAnalyticsWithVisionClusterMeasure:personClusterMeasure:personClusters:andGroundTruthInformation:]_block_invoke.599
+ __137-[VCPPhotosAutoCounterWorker _reportCoreAnalyticsWithVisionClusterMeasure:personClusterMeasure:personClusters:andGroundTruthInformation:]_block_invoke.602
+ __137-[VCPPhotosAutoCounterWorker _reportCoreAnalyticsWithVisionClusterMeasure:personClusterMeasure:personClusters:andGroundTruthInformation:]_block_invoke.630
+ __137-[VCPPhotosAutoCounterWorker _reportCoreAnalyticsWithVisionClusterMeasure:personClusterMeasure:personClusters:andGroundTruthInformation:]_block_invoke.631
+ __147-[VCPPhotosPersistenceDelegate identifyConflictingL0Clusters:csnToRejectedPersonForNewlyClusteredFaces:csnToConfirmedPersonForNewlyClusteredFaces:]_block_invoke.414
+ __147-[VCPPhotosPersistenceDelegate identifyConflictingL0Clusters:csnToRejectedPersonForNewlyClusteredFaces:csnToConfirmedPersonForNewlyClusteredFaces:]_block_invoke.432
+ __147-[VCPPhotosPersistenceDelegate identifyConflictingL0Clusters:csnToRejectedPersonForNewlyClusteredFaces:csnToConfirmedPersonForNewlyClusteredFaces:]_block_invoke.440
+ __147-[VCPPhotosPersistenceDelegate identifyConflictingL0Clusters:csnToRejectedPersonForNewlyClusteredFaces:csnToConfirmedPersonForNewlyClusteredFaces:]_block_invoke.445
+ __147-[VCPPhotosPersistenceDelegate identifyConflictingL0Clusters:csnToRejectedPersonForNewlyClusteredFaces:csnToConfirmedPersonForNewlyClusteredFaces:]_block_invoke.447
+ __147-[VCPPhotosPersistenceDelegate identifyConflictingL0Clusters:csnToRejectedPersonForNewlyClusteredFaces:csnToConfirmedPersonForNewlyClusteredFaces:]_block_invoke_2.433
+ __149-[VCPPhotosAutoCounterWorker _parseGroundTruthWithURL:faceCountPerPerson:personInformation:faceToPerson:assetToFaces:extendTimeoutBlock:cancelBlock:]_block_invoke.463
+ __162-[VCPClusterer _performAndPersistClustersWithFaceTorsoprintsToAdd:groupingIdentifiersToAdd:faceTorsoprintsToRemove:updatedFaces:cancelOrExtendTimeoutBlock:error:]_block_invoke.367
+ __162-[VCPClusterer _performAndPersistClustersWithFaceTorsoprintsToAdd:groupingIdentifiersToAdd:faceTorsoprintsToRemove:updatedFaces:cancelOrExtendTimeoutBlock:error:]_block_invoke.374
+ __167-[VCPPhotosPersistenceDelegate _detectDuplicationInExistingFaceCrops:withFetchedFaces:faceCropFaceIdentifiersToEvaluate:duplicationResults:cancelOrExtendTimeoutBlock:]_block_invoke.654
+ __167-[VCPPhotosPersistenceDelegate _detectDuplicationInExistingFaceCrops:withFetchedFaces:faceCropFaceIdentifiersToEvaluate:duplicationResults:cancelOrExtendTimeoutBlock:]_block_invoke.657
+ __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.395
+ __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.399
+ __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.403
+ __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.406
+ __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.412
+ __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.427
+ __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.431
+ __202-[VCPPhotosAutoCounterWorker _measurePNPersonClusters:groundTruthFaceCountPerPerson:groundTruthPersonInformation:groundTruthFaceToPerson:groundTruthAssetToFaces:measures:extendTimeoutBlock:cancelBlock:]_block_invoke.509
+ __202-[VCPPhotosAutoCounterWorker _measurePNPersonClusters:groundTruthFaceCountPerPerson:groundTruthPersonInformation:groundTruthFaceToPerson:groundTruthAssetToFaces:measures:extendTimeoutBlock:cancelBlock:]_block_invoke.512
+ __202-[VCPPhotosAutoCounterWorker _measurePNPersonClusters:groundTruthFaceCountPerPerson:groundTruthPersonInformation:groundTruthFaceToPerson:groundTruthAssetToFaces:measures:extendTimeoutBlock:cancelBlock:]_block_invoke_2.513
+ __212-[VCPPhotosAutoCounterWorker _measureClusterWithClusterStateURL:groundTruthFaceCountPerPerson:groundTruthPersonInformation:groundTruthFaceToPerson:groundTruthAssetToFaces:measures:extendTimeoutBlock:cancelBlock:]_block_invoke.480
+ __212-[VCPPhotosAutoCounterWorker _measureClusterWithClusterStateURL:groundTruthFaceCountPerPerson:groundTruthPersonInformation:groundTruthFaceToPerson:groundTruthAssetToFaces:measures:extendTimeoutBlock:cancelBlock:]_block_invoke.481
+ __212-[VCPPhotosAutoCounterWorker _measureClusterWithClusterStateURL:groundTruthFaceCountPerPerson:groundTruthPersonInformation:groundTruthFaceToPerson:groundTruthAssetToFaces:measures:extendTimeoutBlock:cancelBlock:]_block_invoke.505
+ __278-[VCPPhotosPersistenceDelegate _completePersonBuildingWithPersonsToUpdate:facesToRemoveByPerson:facesToAddByPerson:updateFaceGroup:newMergeCandidatePairs:newInvalidMergeCandidatePairs:faceInFaceGroupByCSN:personCache:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:error:]_block_invoke.602
+ __278-[VCPPhotosPersistenceDelegate _completePersonBuildingWithPersonsToUpdate:facesToRemoveByPerson:facesToAddByPerson:updateFaceGroup:newMergeCandidatePairs:newInvalidMergeCandidatePairs:faceInFaceGroupByCSN:personCache:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:error:]_block_invoke.603
+ __278-[VCPPhotosPersistenceDelegate _completePersonBuildingWithPersonsToUpdate:facesToRemoveByPerson:facesToAddByPerson:updateFaceGroup:newMergeCandidatePairs:newInvalidMergeCandidatePairs:faceInFaceGroupByCSN:personCache:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:error:]_block_invoke.607
+ __278-[VCPPhotosPersistenceDelegate _completePersonBuildingWithPersonsToUpdate:facesToRemoveByPerson:facesToAddByPerson:updateFaceGroup:newMergeCandidatePairs:newInvalidMergeCandidatePairs:faceInFaceGroupByCSN:personCache:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:error:]_block_invoke.611
+ __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.459
+ __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.462
+ __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.464
+ __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.465
+ __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.472
+ __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.486
+ __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.490
+ __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.491
+ __38-[MADEmbeddingStoreService connection]_block_invoke.234
+ __38-[MADEmbeddingStoreService connection]_block_invoke.234.cold.1
+ __38-[MADEmbeddingStoreService connection]_block_invoke.235
+ __42-[VCPMobileAssetManager queryMobileAssets]_block_invoke.577
+ __42-[VCPMobileAssetManager queryMobileAssets]_block_invoke.579
+ __48-[VCPMobileAssetManager purgeAllInstalledAssets]_block_invoke.593
+ __51-[VCPVideoFullFaceDetector updateWithExistingFaces]_block_invoke.273
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.552
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.552.cold.1
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.555
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.555.cold.1
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.560
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.560.cold.1
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.566
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.566.cold.1
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.574
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.574.cold.1
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.574.cold.2
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.578
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.578.cold.1
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.578.cold.2
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.583
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.583.cold.1
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.583.cold.2
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.586
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.586.cold.1
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.586.cold.2
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.597
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.597.cold.1
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.600
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.600.cold.1
+ __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.600.cold.2
+ __58-[VCPPhotosQuickFaceIdentificationManager classifyVIPPets]_block_invoke.302
+ __58-[VCPPhotosQuickFaceIdentificationManager classifyVIPPets]_block_invoke.306
+ __64-[VCPPreAnalyzer _extractAndSortBoundingBoxFromDetectedObjects:]_block_invoke.381
+ __65-[VCPMobileAssetManager downloadMobileAssetIfNeeded:petWatchDog:]_block_invoke.584
+ __65-[VCPMobileAssetManager downloadMobileAssetIfNeeded:petWatchDog:]_block_invoke.586
+ __74-[MADEmbeddingStoreService checkSandboxExtensionForPhotoLibraryURL:error:]_block_invoke.244
+ __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.583
+ __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.583.cold.1
+ __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.583.cold.2
+ __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.590
+ __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.590.cold.1
+ __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.590.cold.2
+ __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.590.cold.3
+ __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.590.cold.4
+ __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.590.cold.5
+ __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.590.cold.6
+ __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.590.cold.7
+ __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.590.cold.8
+ __76-[VCPFaceProcessingServiceWorker resetFaceClusteringStateWithContext:reply:]_block_invoke.462
+ __79-[MADEmbeddingStoreService searchWithEmbeddings:photoLibraryURL:options:error:]_block_invoke.260
+ __82-[VCPPhotosPersistenceDelegate dedupeGraphVerifiedPersonsInFaceGroup:personCache:]_block_invoke.597
+ __82-[VCPPhotosPersistenceDelegate dedupeGraphVerifiedPersonsInFaceGroup:personCache:]_block_invoke.598
+ __84-[MADEmbeddingStoreService prewarmSearchWithConcurrencyLimit:photoLibraryURL:error:]_block_invoke.266
+ __88-[MADEmbeddingStoreService fetchEmbeddingsWithAssetUUIDs:photoLibraryURL:options:error:]_block_invoke.254
+ __88-[VCPPreAnalyzer _performSceneAnalysis:image:mediaType:mediaSubtypes:abnormalDimension:]_block_invoke.403
+ __90-[VCPVideoFullFaceDetector detectTrackFacesInFrame:withTimestamp:faces:torsos:frameStats:]_block_invoke.249
+ __91-[VCPPhotosQuickFaceIdentificationManager _generatePetsModelWithExtendTimeoutBlock:cancel:]_block_invoke.371
+ __99-[VCPFaceProcessingServiceWorker validateClusterCacheWithContext:cancelOrExtendTimeoutBlock:reply:]_block_invoke.455
+ __Block_byref_object_copy_.550
+ __Block_byref_object_dispose_.551
+ __OBJC_$_INSTANCE_METHODS_Container
+ __OBJC_$_INSTANCE_METHODS_MADGenerativePlaygroundsMD1TextEncoderResource
+ __OBJC_$_INSTANCE_METHODS_MADGenerativePlaygroundsMD4TextEncoderResource
+ __OBJC_$_INSTANCE_METHODS_MADVSKClient
+ __OBJC_$_INSTANCE_METHODS_VCPCNNVisionCoreDetector
+ __OBJC_$_INSTANCE_VARIABLES_Container
+ __OBJC_$_INSTANCE_VARIABLES_MADVSKClient
+ __OBJC_$_INSTANCE_VARIABLES_VCPCNNVisionCoreDetector
+ __OBJC_$_PROP_LIST_Container
+ __OBJC_$_PROP_LIST_MADVSKClient
+ __OBJC_CLASS_RO_$_Container
+ __OBJC_CLASS_RO_$_MADGenerativePlaygroundsMD1TextEncoderResource
+ __OBJC_CLASS_RO_$_MADGenerativePlaygroundsMD4TextEncoderResource
+ __OBJC_CLASS_RO_$_MADVSKClient
+ __OBJC_CLASS_RO_$_VCPCNNVisionCoreDetector
+ __OBJC_METACLASS_RO_$_Container
+ __OBJC_METACLASS_RO_$_MADGenerativePlaygroundsMD1TextEncoderResource
+ __OBJC_METACLASS_RO_$_MADGenerativePlaygroundsMD4TextEncoderResource
+ __OBJC_METACLASS_RO_$_MADVSKClient
+ __OBJC_METACLASS_RO_$_VCPCNNVisionCoreDetector
+ __ZL25_espressoPlanErrorMessagePv
+ __ZN13sentencepiece22SentencePieceProcessor17MMapAuthenticatedENSt3__117basic_string_viewIcNS1_11char_traitsIcEEEE
+ __ZN13sentencepiece4MmapIcE4openERKNSt3__14__fs10filesystem4pathEb
+ __ZNKSt3__14__fs10filesystem4path10__filenameEv
+ __ZNKSt3__14__fs10filesystem4path11parent_pathB8ne180100Ev
+ __ZNKSt3__14__fs10filesystem4path13__parent_pathEv
+ __ZNKSt3__14__fs10filesystem4path8filenameB8ne180100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16__init_with_sizeB8ne180100IPKcS8_EEvT_T0_m
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendB8ne180100IPKcLi0EEERS5_T_SA_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
+ __ZNSt3__115__quoted_outputB8ne180100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_S9_S4_S4_
+ __ZNSt3__14__fs10filesystem4pathC2B8ne180100IPKcvEERKT_NS2_6formatE
+ __ZNSt3__14__fs10filesystem8__statusERKNS1_4pathEPNS_10error_codeE
+ ___84-[MADEmbeddingStoreService prewarmSearchWithConcurrencyLimit:photoLibraryURL:error:]_block_invoke
+ ___95-[VCPMediaAnalyzer searchForQuery:forAssets:withOptions:matchingScoreOnly:isURLAsset:analyses:]_block_invoke
+ ___block_descriptor_40_ea8_32s_e19_"MADVSKClient"8?0l
+ __block_literal_global.1138
+ __block_literal_global.1224
+ __block_literal_global.1779
+ __block_literal_global.2072
+ __block_literal_global.2154
+ __block_literal_global.2246
+ __block_literal_global.2348
+ __block_literal_global.2355
+ __block_literal_global.237
+ __block_literal_global.254
+ __block_literal_global.255
+ __block_literal_global.259
+ __block_literal_global.260
+ __block_literal_global.264
+ __block_literal_global.265
+ __block_literal_global.284
+ __block_literal_global.301
+ __block_literal_global.306
+ __block_literal_global.311
+ __block_literal_global.316
+ __block_literal_global.316
+ __block_literal_global.321
+ __block_literal_global.334
+ __block_literal_global.353
+ __block_literal_global.354
+ __block_literal_global.362
+ __block_literal_global.369
+ __block_literal_global.378
+ __block_literal_global.379
+ __block_literal_global.383
+ __block_literal_global.383
+ __block_literal_global.384
+ __block_literal_global.385
+ __block_literal_global.398
+ __block_literal_global.398
+ __block_literal_global.399
+ __block_literal_global.400
+ __block_literal_global.401
+ __block_literal_global.401
+ __block_literal_global.403
+ __block_literal_global.408
+ __block_literal_global.425
+ __block_literal_global.430
+ __block_literal_global.450
+ __block_literal_global.464
+ __block_literal_global.468
+ __block_literal_global.473
+ __block_literal_global.474
+ __block_literal_global.478
+ __block_literal_global.509
+ __block_literal_global.520
+ __block_literal_global.549
+ __block_literal_global.567
+ __block_literal_global.575
+ __block_literal_global.612
+ __block_literal_global.613
+ __block_literal_global.646
+ __block_literal_global.660
+ __block_literal_global.667
+ _e5rt_e5_compiler_compile
+ _e5rt_e5_compiler_create
+ _e5rt_e5_compiler_options_create
+ _e5rt_e5_compiler_options_get_compute_device_types_mask
+ _e5rt_e5_compiler_options_release
+ _e5rt_e5_compiler_options_retain_mil_entry_points
+ _e5rt_e5_compiler_options_set_mil_entry_points
+ _e5rt_e5_compiler_release
+ _e5rt_execution_stream_operation_create_precompiled_compute_operation_with_options
+ _e5rt_precompiled_compute_op_create_options_create_with_program_function
+ _e5rt_precompiled_compute_op_create_options_release
+ _e5rt_program_function_release
+ _e5rt_program_library_retain_program_function
+ _espresso_buffer_pack_tensor_shape
+ _espresso_context_set_low_precision_accumulation
+ _espresso_plan_get_error_info
+ _objc_msgSend$UpdateInputBuffersAndBindPixelBuffer:
+ _objc_msgSend$allInputNames
+ _objc_msgSend$allOutputNames
+ _objc_msgSend$allocatePostProcessingBuffers:error:
+ _objc_msgSend$anstHandsDetectorWithExtendRatio:options:
+ _objc_msgSend$assignData:toName:error:
+ _objc_msgSend$assignPixelBuffer:toName:error:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$buffer
+ _objc_msgSend$createPrecompiledOp:isPrecompiled:functionName:
+ _objc_msgSend$descriptorForIdentifier:version:objectTrackingEnabled:segmentationEnabled:lowFrameRate:error:
+ _objc_msgSend$downscaleBuffer:scaledImage:
+ _objc_msgSend$fullBodyResults
+ _objc_msgSend$getBodyRegions:fromVisionCorePostProcessingOutput:imageWidth:imageHeight:extendRatio:portrait_mode:
+ _objc_msgSend$getHandsRegions:fromVisionCorePostProcessingOutput:imageWidth:imageHeight:extendRatio:portrait_mode:
+ _objc_msgSend$hands
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$initWithExtendRatio:options:
+ _objc_msgSend$initWithInputImageBuffer:inputImageOrientation:inferenceOutputNamedObjects:
+ _objc_msgSend$initWithMajor:
+ _objc_msgSend$initWithPostProcessedPersonImageBuffer:personImageOrientation:salientPersonImageBuffer:salientPersonImageBufferOrientation:skinImageBuffer:skinImageBufferOrientation:hairImageBuffer:hairImageBufferOrientation:skyImageBuffer:skyImageBufferOrientation:
+ _objc_msgSend$inputNamed:error:
+ _objc_msgSend$loadModel:withOptions:
+ _objc_msgSend$outputNamed:error:
+ _objc_msgSend$performPostProcessingForInput:postProcessingOutput:error:
+ _objc_msgSend$pixelBufferForName:error:
+ _objc_msgSend$planExecutionandOutput:descriptor:
+ _objc_msgSend$postProcessingOutputDescriptors
+ _objc_msgSend$prewarmSearchWithConcurrencyLimit:
+ _objc_msgSend$prewarmSearchWithConcurrencyLimit:photoLibraryURL:error:
+ _objc_msgSend$prewarmSearchWithConcurrencyLimit:photoLibraryURL:reply:
+ _objc_msgSend$rank
+ _objc_msgSend$requiresPostProcessing
+ _objc_msgSend$resultForPixelBuffer:orientation:Error:
+ _objc_msgSend$searchForQuery:forAssets:withOptions:matchingScoreOnly:isURLAsset:analyses:
+ _objc_msgSend$setBuffer:
+ _objc_msgSend$sizes
+ _objc_msgSend$storageByteCount
+ _objc_msgSend$vcp_shortMovieDurationThreshold
+ _openat_authenticated_np
- +[VCPANSTHandsDetector anstHandsDetectorWithExtendRatio:]
- -[MADGenerativePlaygroundsTextEncoderResource additionalLayerNames]
- -[MADGenerativePlaygroundsTextEncoderResource revision]
- -[MADGenerativePlaygroundsTextEncoderResource tokenEmbeddingType]
- -[MADGenerativePlaygroundsTextEncoderResource version]
- -[MADVectorDatabase dealloc]
- -[PHPhotoLibrary(MediaAnalysis) mad_progressPercentageForTaskID:withPHTaskID:priority:error:]
- -[VCPANSTHandsDetector initWithExtendRatio:]
- -[VCPANSTHandsDetector initWithExtendRatio:].cold.1
- -[VCPFaceAnalyzer dealloc]
- -[VCPImageFaceQualityAnalyzer dealloc]
- -[VCPMediaAnalyzer searchForQuery:forAssets:withOptions:matchingScoreOnly:analyses:]
- -[VCPPreAnalyzer dealloc]
- -[VCPVideoFullFaceDetector dealloc]
- -[VCPVideoLightFaceDetector dealloc]
- -[VCPVideoSceneClassifier dealloc]
- GCC_except_table214
- GCC_except_table232
- GCC_except_table270
- GCC_except_table276
- GCC_except_table280
- GCC_except_table288
- GCC_except_table300
- OBJC_IVAR_$_VCPFreeFormSearch._textEmbeddingThresholdMD3
- _OBJC_CLASS_$_MADGenerativePlaygroundsTextEncoderResource
- _OBJC_METACLASS_$_MADGenerativePlaygroundsTextEncoderResource
- __103-[VCPFaceProcessingServiceWorker faceCandidatesforKeyFaceForPersonsWithLocalIdentifiers:context:reply:]_block_invoke.460
- __103-[VCPPhotosPersistenceDelegate _processNewlyClusteredFaceCropsInFaceGroups:cancelOrExtendTimeoutBlock:]_block_invoke.677
- __103-[VCPPhotosPersistenceDelegate _processNewlyClusteredFaceCropsInFaceGroups:cancelOrExtendTimeoutBlock:]_block_invoke.681
- __104-[VCPPhotosQuickFaceIdentificationManager processAsset:onDemandDetection:detectedFaces:detectedPersons:]_block_invoke.299
- __108-[VCPPhotosPersistenceDelegate _adjustConfirmingAndRejectionWithFaces:faceCrops:cancelOrExtendTimeoutBlock:]_block_invoke.639
- __108-[VCPPhotosPersistenceDelegate _adjustConfirmingAndRejectionWithFaces:faceCrops:cancelOrExtendTimeoutBlock:]_block_invoke.645
- __108-[VCPPhotosPersistenceDelegate _adjustConfirmingAndRejectionWithFaces:faceCrops:cancelOrExtendTimeoutBlock:]_block_invoke.654
- __108-[VCPPhotosPersistenceDelegate _adjustConfirmingAndRejectionWithFaces:faceCrops:cancelOrExtendTimeoutBlock:]_block_invoke.656
- __108-[VCPPhotosPersistenceDelegate _adjustConfirmingAndRejectionWithFaces:faceCrops:cancelOrExtendTimeoutBlock:]_block_invoke_2.655
- __113-[VCPClusterer _processingQueueSyncClustererWithPhotoLibraryUsingFacesInClusterCache:cancelOrExtendTimeoutBlock:]_block_invoke.393
- __113-[VCPClusterer _processingQueueSyncClustererWithPhotoLibraryUsingFacesInClusterCache:cancelOrExtendTimeoutBlock:]_block_invoke.397
- __113-[VCPClusterer _processingQueueSyncClustererWithPhotoLibraryUsingFacesInClusterCache:cancelOrExtendTimeoutBlock:]_block_invoke.398
- __113-[VCPClusterer _processingQueueSyncClustererWithPhotoLibraryUsingFacesInClusterCache:cancelOrExtendTimeoutBlock:]_block_invoke.400
- __113-[VCPClusterer _processingQueueSyncClustererWithPhotoLibraryUsingFacesInClusterCache:cancelOrExtendTimeoutBlock:]_block_invoke.401
- __116-[VCPClusterer differencesBetweenClusterCacheAndLibrary:excludedL0ClustersByL1ClusterId:cancelOrExtendTimeoutBlock:]_block_invoke.518
- __116-[VCPClusterer differencesBetweenClusterCacheAndLibrary:excludedL0ClustersByL1ClusterId:cancelOrExtendTimeoutBlock:]_block_invoke.524
- __119-[VCPClusterer _resolveConflictingL0ClustersFromVNClusters:excludedL0ClustersByL1ClusterId:cancelOrExtendTimeoutBlock:]_block_invoke.512
- __121-[VCPPhotosPersistenceDelegate updateKeyFacesOfPersonsWithLocalIdentifiers:forceUpdate:cancelOrExtendTimeoutBlock:error:]_block_invoke.528
- __121-[VCPPhotosQuickFaceIdentificationManager personIdentificationForSyndicationPhotoLibrary:withCancelOrExtendTimeoutBlock:]_block_invoke.332
- __121-[VCPPhotosQuickFaceIdentificationManager personIdentificationForSyndicationPhotoLibrary:withCancelOrExtendTimeoutBlock:]_block_invoke.337
- __128-[VCPPhotosPersistenceDelegate _cleanupMergeCandidatesForVerifiedPersons:minimumFaceGroupSize:cancelOrExtendTimeoutBlock:error:]_block_invoke.592
- __128-[VCPPhotosPersistenceDelegate _cleanupMergeCandidatesForVerifiedPersons:minimumFaceGroupSize:cancelOrExtendTimeoutBlock:error:]_block_invoke.595
- __131-[VCPPhotosQuickFaceIdentificationManager _generatePersonsModelWithExtendTimeoutBlock:cancel:evaluationMode:allowUnverifiedPerson:]_block_invoke.397
- __131-[VCPPhotosQuickFaceIdentificationManager _generatePersonsModelWithExtendTimeoutBlock:cancel:evaluationMode:allowUnverifiedPerson:]_block_invoke.401
- __135-[VCPPhotosPersistenceDelegate _buildPersonsFromUpdatedFaceGroups:faceClusterer:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:]_block_invoke.683
- __135-[VCPPhotosPersistenceDelegate _buildPersonsFromUpdatedFaceGroups:faceClusterer:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:]_block_invoke.697
- __135-[VCPPhotosPersistenceDelegate _buildPersonsFromUpdatedFaceGroups:faceClusterer:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:]_block_invoke.711
- __135-[VCPPhotosPersistenceDelegate _buildPersonsFromUpdatedFaceGroups:faceClusterer:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:]_block_invoke.750
- __137-[VCPPhotosAutoCounterWorker _reportCoreAnalyticsWithVisionClusterMeasure:personClusterMeasure:personClusters:andGroundTruthInformation:]_block_invoke.610
- __137-[VCPPhotosAutoCounterWorker _reportCoreAnalyticsWithVisionClusterMeasure:personClusterMeasure:personClusters:andGroundTruthInformation:]_block_invoke.611
- __137-[VCPPhotosAutoCounterWorker _reportCoreAnalyticsWithVisionClusterMeasure:personClusterMeasure:personClusters:andGroundTruthInformation:]_block_invoke.614
- __137-[VCPPhotosAutoCounterWorker _reportCoreAnalyticsWithVisionClusterMeasure:personClusterMeasure:personClusters:andGroundTruthInformation:]_block_invoke.642
- __137-[VCPPhotosAutoCounterWorker _reportCoreAnalyticsWithVisionClusterMeasure:personClusterMeasure:personClusters:andGroundTruthInformation:]_block_invoke.643
- __147-[VCPPhotosPersistenceDelegate identifyConflictingL0Clusters:csnToRejectedPersonForNewlyClusteredFaces:csnToConfirmedPersonForNewlyClusteredFaces:]_block_invoke.438
- __147-[VCPPhotosPersistenceDelegate identifyConflictingL0Clusters:csnToRejectedPersonForNewlyClusteredFaces:csnToConfirmedPersonForNewlyClusteredFaces:]_block_invoke.452
- __147-[VCPPhotosPersistenceDelegate identifyConflictingL0Clusters:csnToRejectedPersonForNewlyClusteredFaces:csnToConfirmedPersonForNewlyClusteredFaces:]_block_invoke.456
- __147-[VCPPhotosPersistenceDelegate identifyConflictingL0Clusters:csnToRejectedPersonForNewlyClusteredFaces:csnToConfirmedPersonForNewlyClusteredFaces:]_block_invoke.457
- __147-[VCPPhotosPersistenceDelegate identifyConflictingL0Clusters:csnToRejectedPersonForNewlyClusteredFaces:csnToConfirmedPersonForNewlyClusteredFaces:]_block_invoke.459
- __147-[VCPPhotosPersistenceDelegate identifyConflictingL0Clusters:csnToRejectedPersonForNewlyClusteredFaces:csnToConfirmedPersonForNewlyClusteredFaces:]_block_invoke_2.445
- __149-[VCPPhotosAutoCounterWorker _parseGroundTruthWithURL:faceCountPerPerson:personInformation:faceToPerson:assetToFaces:extendTimeoutBlock:cancelBlock:]_block_invoke.475
- __162-[VCPClusterer _performAndPersistClustersWithFaceTorsoprintsToAdd:groupingIdentifiersToAdd:faceTorsoprintsToRemove:updatedFaces:cancelOrExtendTimeoutBlock:error:]_block_invoke.379
- __162-[VCPClusterer _performAndPersistClustersWithFaceTorsoprintsToAdd:groupingIdentifiersToAdd:faceTorsoprintsToRemove:updatedFaces:cancelOrExtendTimeoutBlock:error:]_block_invoke.386
- __167-[VCPPhotosPersistenceDelegate _detectDuplicationInExistingFaceCrops:withFetchedFaces:faceCropFaceIdentifiersToEvaluate:duplicationResults:cancelOrExtendTimeoutBlock:]_block_invoke.666
- __167-[VCPPhotosPersistenceDelegate _detectDuplicationInExistingFaceCrops:withFetchedFaces:faceCropFaceIdentifiersToEvaluate:duplicationResults:cancelOrExtendTimeoutBlock:]_block_invoke.669
- __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.407
- __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.411
- __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.415
- __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.418
- __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.424
- __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.439
- __169-[VCPFaceProcessingServiceWorker _suggestionsForPersonWithLocalIdentifier:toBeConfirmedPersonSuggestions:toBeRejectedPersonSuggestions:cancelOrExtendTimeoutBlock:error:]_block_invoke.443
- __202-[VCPPhotosAutoCounterWorker _measurePNPersonClusters:groundTruthFaceCountPerPerson:groundTruthPersonInformation:groundTruthFaceToPerson:groundTruthAssetToFaces:measures:extendTimeoutBlock:cancelBlock:]_block_invoke.521
- __202-[VCPPhotosAutoCounterWorker _measurePNPersonClusters:groundTruthFaceCountPerPerson:groundTruthPersonInformation:groundTruthFaceToPerson:groundTruthAssetToFaces:measures:extendTimeoutBlock:cancelBlock:]_block_invoke.524
- __202-[VCPPhotosAutoCounterWorker _measurePNPersonClusters:groundTruthFaceCountPerPerson:groundTruthPersonInformation:groundTruthFaceToPerson:groundTruthAssetToFaces:measures:extendTimeoutBlock:cancelBlock:]_block_invoke_2.525
- __212-[VCPPhotosAutoCounterWorker _measureClusterWithClusterStateURL:groundTruthFaceCountPerPerson:groundTruthPersonInformation:groundTruthFaceToPerson:groundTruthAssetToFaces:measures:extendTimeoutBlock:cancelBlock:]_block_invoke.492
- __212-[VCPPhotosAutoCounterWorker _measureClusterWithClusterStateURL:groundTruthFaceCountPerPerson:groundTruthPersonInformation:groundTruthFaceToPerson:groundTruthAssetToFaces:measures:extendTimeoutBlock:cancelBlock:]_block_invoke.493
- __212-[VCPPhotosAutoCounterWorker _measureClusterWithClusterStateURL:groundTruthFaceCountPerPerson:groundTruthPersonInformation:groundTruthFaceToPerson:groundTruthAssetToFaces:measures:extendTimeoutBlock:cancelBlock:]_block_invoke.517
- __278-[VCPPhotosPersistenceDelegate _completePersonBuildingWithPersonsToUpdate:facesToRemoveByPerson:facesToAddByPerson:updateFaceGroup:newMergeCandidatePairs:newInvalidMergeCandidatePairs:faceInFaceGroupByCSN:personCache:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:error:]_block_invoke.614
- __278-[VCPPhotosPersistenceDelegate _completePersonBuildingWithPersonsToUpdate:facesToRemoveByPerson:facesToAddByPerson:updateFaceGroup:newMergeCandidatePairs:newInvalidMergeCandidatePairs:faceInFaceGroupByCSN:personCache:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:error:]_block_invoke.615
- __278-[VCPPhotosPersistenceDelegate _completePersonBuildingWithPersonsToUpdate:facesToRemoveByPerson:facesToAddByPerson:updateFaceGroup:newMergeCandidatePairs:newInvalidMergeCandidatePairs:faceInFaceGroupByCSN:personCache:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:error:]_block_invoke.619
- __278-[VCPPhotosPersistenceDelegate _completePersonBuildingWithPersonsToUpdate:facesToRemoveByPerson:facesToAddByPerson:updateFaceGroup:newMergeCandidatePairs:newInvalidMergeCandidatePairs:faceInFaceGroupByCSN:personCache:keyFaceUpdateBlock:cancelOrExtendTimeoutBlock:context:error:]_block_invoke.623
- __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.474
- __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.477
- __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.483
- __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.484
- __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.488
- __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.498
- __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.502
- __321-[VCPPhotosPersistenceDelegate persistChangesToAlgorithmicFaceGroups:l1ClustersByFaceCSNRepresentingFaceGroup:l0ClustersByFaceCSNRepresentingFaceGroup:faceCSNByLocalIdentifierForNewlyClusteredFaces:faceCSNsOfUnclusteredFaces:localIdentifiersOfUnclusteredFaces:persistenceCompletionBlock:cancelOrExtendTimeoutBlock:error:]_block_invoke.503
- __38-[MADEmbeddingStoreService connection]_block_invoke.231
- __38-[MADEmbeddingStoreService connection]_block_invoke.231.cold.1
- __38-[MADEmbeddingStoreService connection]_block_invoke.232
- __42-[VCPMobileAssetManager queryMobileAssets]_block_invoke.589
- __42-[VCPMobileAssetManager queryMobileAssets]_block_invoke.591
- __48-[VCPMobileAssetManager purgeAllInstalledAssets]_block_invoke.605
- __51-[VCPVideoFullFaceDetector updateWithExistingFaces]_block_invoke.276
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.553
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.553.cold.1
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.556
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.556.cold.1
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.561
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.561.cold.1
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.567
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.567.cold.1
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.575
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.575.cold.1
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.575.cold.2
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.579
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.579.cold.1
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.579.cold.2
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.585
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.585.cold.1
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.585.cold.2
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.587
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.587.cold.1
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.587.cold.2
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.598
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.598.cold.1
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.601
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.601.cold.1
- __58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.601.cold.2
- __58-[VCPPhotosQuickFaceIdentificationManager classifyVIPPets]_block_invoke.314
- __58-[VCPPhotosQuickFaceIdentificationManager classifyVIPPets]_block_invoke.318
- __64-[VCPPreAnalyzer _extractAndSortBoundingBoxFromDetectedObjects:]_block_invoke.384
- __65-[VCPMobileAssetManager downloadMobileAssetIfNeeded:petWatchDog:]_block_invoke.596
- __65-[VCPMobileAssetManager downloadMobileAssetIfNeeded:petWatchDog:]_block_invoke.598
- __74-[MADEmbeddingStoreService checkSandboxExtensionForPhotoLibraryURL:error:]_block_invoke.241
- __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.585
- __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.585.cold.1
- __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.585.cold.2
- __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.592
- __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.592.cold.1
- __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.592.cold.2
- __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.592.cold.3
- __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.592.cold.4
- __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.592.cold.5
- __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.592.cold.6
- __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.592.cold.7
- __74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.592.cold.8
- __76-[VCPFaceProcessingServiceWorker resetFaceClusteringStateWithContext:reply:]_block_invoke.474
- __79-[MADEmbeddingStoreService searchWithEmbeddings:photoLibraryURL:options:error:]_block_invoke.257
- __82-[VCPPhotosPersistenceDelegate dedupeGraphVerifiedPersonsInFaceGroup:personCache:]_block_invoke.609
- __82-[VCPPhotosPersistenceDelegate dedupeGraphVerifiedPersonsInFaceGroup:personCache:]_block_invoke.610
- __88-[MADEmbeddingStoreService fetchEmbeddingsWithAssetUUIDs:photoLibraryURL:options:error:]_block_invoke.251
- __88-[VCPPreAnalyzer _performSceneAnalysis:image:mediaType:mediaSubtypes:abnormalDimension:]_block_invoke.406
- __90-[VCPVideoFullFaceDetector detectTrackFacesInFrame:withTimestamp:faces:torsos:frameStats:]_block_invoke.252
- __91-[VCPPhotosQuickFaceIdentificationManager _generatePetsModelWithExtendTimeoutBlock:cancel:]_block_invoke.383
- __99-[VCPFaceProcessingServiceWorker validateClusterCacheWithContext:cancelOrExtendTimeoutBlock:reply:]_block_invoke.467
- __Block_byref_object_copy_.551
- __Block_byref_object_dispose_.552
- __OBJC_$_INSTANCE_METHODS_MADGenerativePlaygroundsTextEncoderResource
- __OBJC_CLASS_RO_$_MADGenerativePlaygroundsTextEncoderResource
- __OBJC_METACLASS_RO_$_MADGenerativePlaygroundsTextEncoderResource
- __ZGVZ43+[MADVectorDatabase _vectorDatabaseVersion]E27kVectorDatabaseMajorVersion
- __ZN13sentencepiece4MmapIcE4openEPKcS3_
- __ZZ39+[VCPVideoTransformerBackbone revision]E8revision
- __ZZ43+[MADVectorDatabase _vectorDatabaseVersion]E27kVectorDatabaseMajorVersion
- ___84-[VCPMediaAnalyzer searchForQuery:forAssets:withOptions:matchingScoreOnly:analyses:]_block_invoke
- ___block_descriptor_40_ea8_32s_e16_"VSKClient"8?0l
- __block_literal_global.1150
- __block_literal_global.1236
- __block_literal_global.1791
- __block_literal_global.2084
- __block_literal_global.2166
- __block_literal_global.2258
- __block_literal_global.230
- __block_literal_global.2360
- __block_literal_global.2367
- __block_literal_global.263
- __block_literal_global.281
- __block_literal_global.286
- __block_literal_global.308
- __block_literal_global.313
- __block_literal_global.318
- __block_literal_global.323
- __block_literal_global.328
- __block_literal_global.333
- __block_literal_global.346
- __block_literal_global.365
- __block_literal_global.380
- __block_literal_global.380
- __block_literal_global.386
- __block_literal_global.390
- __block_literal_global.391
- __block_literal_global.396
- __block_literal_global.410
- __block_literal_global.410
- __block_literal_global.412
- __block_literal_global.413
- __block_literal_global.413
- __block_literal_global.414
- __block_literal_global.417
- __block_literal_global.418
- __block_literal_global.421
- __block_literal_global.421
- __block_literal_global.427
- __block_literal_global.428
- __block_literal_global.442
- __block_literal_global.462
- __block_literal_global.476
- __block_literal_global.480
- __block_literal_global.486
- __block_literal_global.532
- __block_literal_global.539
- __block_literal_global.548
- __block_literal_global.579
- __block_literal_global.587
- __block_literal_global.611
- __block_literal_global.624
- __block_literal_global.658
- __block_literal_global.672
- __block_literal_global.679
- __block_literal_global.692
- _objc_msgSend$anstHandsDetectorWithExtendRatio:
- _objc_msgSend$fetchPropertySets
- _objc_msgSend$initWithExtendRatio:
- _objc_msgSend$searchForQuery:forAssets:withOptions:matchingScoreOnly:analyses:
CStrings:
+ "$postprocessed$Hair"
+ "$postprocessed$Person"
+ "$postprocessed$SalientPerson"
+ "$postprocessed$Skin"
+ "$postprocessed$Sky"
+ "%!s(MISSING) (%!@(MISSING))"
+ "(fd = ::open(filename.string().data(), mode)) >= 0"
+ "(p = reinterpret_cast<char*>( ::mmap(0, length, PROT_READ, MAP_SHARED, fd, 0))) != MAP_FAILED"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/bpe_model.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/filesystem.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/mmap.h"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_factory.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_interface.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_interface.h"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/normalizer.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/sentencepiece_processor.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/unigram_model.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/util.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/util.h"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1106: exception: failed to insert key: negative value"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1108: exception: failed to insert key: zero-length key"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1122: exception: failed to insert key: invalid null character"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: wrong key order"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1339: exception: failed to modify unit: too large offset"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1675: exception: failed to build double-array: invalid null character"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1677: exception: failed to build double-array: negative value"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1692: exception: failed to build double-array: wrong key order"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:743: exception: failed to resize pool: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:859: exception: failed to build rank index: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
+ "/AppleInternal/Library/BuildRoots/72033bc0-34d0-11ef-b006-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/AdaptiveSegmentAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/AudioAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/AudioClassifier.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/AudioVideoEmbeddingFuser.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/BlurAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNANSTHandsBodyDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNANSTHandsDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNBlurAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNBlurAnalyzerEspresso.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNBlurAnalyzerMPS.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlock.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockBinary.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockGPU.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockScalar.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockVector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNData.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNDataGPU.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFaceLandmarkDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFaceLandmarkDetectorEspresso.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFaceLandmarkDetectorMPS.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFastGestureRecognition.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFlattenBlock.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFullConnectionBlock.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFullConnectionBlockGPU.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFullConnectionBlockScalar.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNGazeAnalysis.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNHandKeypointsDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNHandKeypointsDetectorEspresso.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNHandsDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNMLEnhancerEspresso.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNMLScalerEspresso.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNModel.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspresso.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspresso.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspressoV2.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspressoV2Data.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPersonDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPersonKeypointsDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPetsDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPetsDetectorEspresso.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPetsDetectorV2.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPetsKeypointsDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPoolingBlock.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPoolingBlockGPU.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPoolingBlockVector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPoseEstimator.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPoseEstimatorEspresso.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPoseEstimatorMPS.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNSmileDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNSmileDetectorEspresso.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNSmileDetectorMPS.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNVisionCore.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CVUtilities.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CameraMotionAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CameraMotionSegment.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CommSafety/VCPMADImageSafetyClassificationTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Convexhull.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/DatabaseReader.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/DescriptorAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/DescriptorSegment.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EdgeDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EmbeddingSummarizationAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EncodeAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EncodeStats.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsAVE1.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsAVE2.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsHW.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsSW.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ExifAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/FineSubjectMotionAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/FineSubjectMotionSegment.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Frame.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/FreeFormSearch.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/FullVideoAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/GaborFilter.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Histogram.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/HomeKitMotionAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/HoughTransform.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Human.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageBackboneAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageBlurAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageCaptionAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageCompositionAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageConverter.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageDescriptor.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageDescriptorWrapper.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageExposureAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageExposurePreAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageFaceDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageFaceExpressionAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageFaceQualityAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageHandsAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageHumanActionAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzer.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzerHolistic.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzerTopDown.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageLivePhotoBlurAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageManager.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageMotionFlowAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImagePetsAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImagePetsKeypointsAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageQualityAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzerBinary.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzerFull.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzerFullEspresso.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/InterAssetAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/InterestingnessAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/IrisAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/JunkAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/LandmarkDetector.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/LandmarkValidator.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/LightMotionAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/LightVideoAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/LivePhotoKeyFrameAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/LoudnessAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MADImageASTCFormatReader.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MADMovieBlastDoorAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MatrixOperationsForFace.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MediaAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MetaTrackDecoder.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFieldAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPBackwarp.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPCorrelation.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPFlowDecoder.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPFlowFeatureExtractor.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPFlowUtils.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPMoFlowSingleEspresso.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPModelR2D2.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlowAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlowSubtleMotionAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionSearch.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MovieAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MovieCurationAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MovieHighlightAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MovingObjectAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MovingObjectSegment.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/NSDictionary+MediaAnalysis.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Object.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ObjectDetection.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ObjectTracking.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ObstructionAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/PHAssetResourceManager+MediaAnalysis.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/PhotoAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/Face/VCPMADPersonIdentificationTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceCropManager.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceProcessingVersionManager.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceUtils.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFullAnalysisAssetProcessingTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFullAnalysisURLProcessingTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosAutoCounterWorker.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosFace.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosQuickFaceDetectionManager.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosQuickFaceIdentificationManager.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosSceneprintAssetProcessingTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPSceneProcessingImageManager.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPVideoStabilizationAssetProcessingTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/PnPSolver.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/PreEncodeAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/QualityAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/RotationAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/RotationSegment.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Rotator.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Scaler.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SceneAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SceneChangeAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Segment.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Service/MADPersonalizedEmbeddingTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Service/VCPMADServiceImageAsset.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ShapeModel.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SlowMotionAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SongDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/StillImageMetaAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SubjectMotionAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SubjectMotionSegment.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SubtleMotionAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SubtleMotionSegment.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/TensorModel.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Text/MADTextEmbeddingCalibration.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Text/MADTextEmbeddingThreshold.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Text/MADTextEmbeddingThresholdMD4.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/TextEncoder.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/TrackSegment.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/TrackingAnalysis.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Transforms.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPAnalysisProgressQuery.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPColorNormalizationAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPContentAnalysis.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPDownloadManager.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPFrameAnalysisStats.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPInternetReachability.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPPoolBasedPixelBufferCreator.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPPreAnalysisImage.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPPreAnalysisImageLoader.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPPreAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPPriorityAnalysis.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPRTLandmarkDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPSceneprintDescriptor.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPSceneprintDescriptorWrapper.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPTimeMeasurement.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPURLAsset.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPVideoEmbeddings.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPWallpaperAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VanishingPointDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoActivityAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoActivityDescriptor.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoAnalysisCommon.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNActionClassifier.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNAutoplay.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNBackbone.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNCameraMotion.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNHighlight.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNQuality.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCaptionAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCaptionEncoder.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoFaceMeshAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoFacePoseAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoFacePoseFilter.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoFullFaceDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoGlobalAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoGyroStabilizer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoHumanActionAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoKeyFrame.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoKeyFrameAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoLightFaceDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoMetaFaceAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoMetaFocusAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoMetaLivePhotoMetaAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoMetaMotionAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoMetaOrientationAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoMetaSegmentAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoObjectTracker.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoPersonDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoPetsActionAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoPetsAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoPixelStabilizer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoRanker.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoSafetyClassifier.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoSaliencyAnalyzer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoSceneClassifier.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoStabilizer.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoTrackStandardDecoder.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoTrackSubsamplingDecoder.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoTrackSyncDecoder.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoTransformerBackbone.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADHEICSAlphaSequenceTranscoder.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADHEICSAlphaSequenceWriter.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADHEVCAlphaSequenceWriter.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADPNGAlphaSequenceWriter.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADVideoRemoveBackgroundCropTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADImageCaptionTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADImageEmbeddingTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADMLEnhancementTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADMLScalingTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIDocumentRecognitionTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIFaceTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIMachineReadableCodeDetectionTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIRectangleDetectionTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVISceneClassificationTask.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VoiceDetector.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VoiceDetectorV2.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/MovieCurationResults.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPCaptureAnalysisSession.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPCoreMLFeatureProviderGestureVideo.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureClassifier.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureImageRequest.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureMitigator.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureVideoRequest.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHandPoseImageRequest.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHandPoseVideoRequest.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHumanPoseEspressoSession.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHumanPoseImageRequest.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHumanPoseVideoRequest.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPMotionFlowRequest.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPPetsPoseImageRequest.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPVideoProcessor.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPVideoProcessorSession.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPVideoSyncFrameDecoder.mm"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/iCloud/MediaAnalysis/Image/MAImageAnalysisRequest.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/iCloud/MediaAnalysis/MAComputeRequest.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/iCloud/MediaAnalysis/Movie/MAAssetByteStream.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/iCloud/MediaAnalysis/Movie/MAMovieAnalysisRequest.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/iCloud/Proto/MAImageComputeResult+CFDictionary.cpp"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/iCloud/Proto/VCPProtoImageHumanPoseResult+CFDictionary.cpp"
+ "@\"MADVSKClient\"8@?0"
+ "BUILT"
+ "DESIGN"
+ "FAILURE"
+ "FaceAnalysisCheckpointWithFailureReportedTimestamp"
+ "FaceAnalysisCompleteWithFailureTimestamp"
+ "FaceAnalysisProgressPercentageWithFailure"
+ "IPXDefaultEnhancedVisualSearchEnabled"
+ "MediaAnalysisCheckpointWithFailureReportedTimestamp"
+ "MediaAnalysisCompleteWithFailureTimestamp"
+ "MediaAnalysisImageCheckpointWithFailureReportedTimestamp"
+ "MediaAnalysisImagePriority1CheckpointWithFailureReportedTimestamp"
+ "MediaAnalysisImagePriority1ProgressPercentageWithFailure"
+ "MediaAnalysisProgressPercentageWithFailure"
+ "OCRAnalysisCheckpointWithFailureReportedTimestamp"
+ "OCRAnalysisCompleteWithFailureTimestamp"
+ "OCRAnalysisProgressPercentageWithFailure"
+ "PECAnalysisCheckpointWithFailureReportedTimestamp"
+ "PECAnalysisCompleteWithFailureTimestamp"
+ "PECAnalysisProgressPercentageWithFailure"
+ "PrioritizedFaceAnalysisCheckpointWithFailureReportedTimestamp"
+ "PrioritizedFaceAnalysisCompleteWithFailureTimestamp"
+ "PrioritizedFaceAnalysisProgressPercentageWithFailure"
+ "SceneAnalysisCheckpointWithFailureReportedTimestamp"
+ "SceneAnalysisCompleteWithFailureTimestamp"
+ "SceneAnalysisProgressPercentageWithFailure"
+ "Trie blob is wrongly formatted."
+ "Trie data size exceeds the input blob size."
+ "VCPCNNVisionCoreDetector - Descriptor requires post processing - but no postProcessingDescriptors returned"
+ "VCPCNNVisionCoreDetector - ISP post processing failure"
+ "VCPCNNVisionCoreDetector - downscaling buffer failed"
+ "VCPCNNVisionCoreDetector - update input buffers and binding buffer failed"
+ "VCPCNNVisionCoreDetectorDownscale"
+ "VCPCNNVisionCoreDetectorExecution"
+ "VCPCNNVisionCoreDetectorPostProcessing"
+ "VisionCore"
+ "VisualSearchAnalysisCheckpointWithFailureReportedTimestamp"
+ "VisualSearchAnalysisCompleteWithFailureTimestamp"
+ "VisualSearchAnalysisProgressPercentageWithFailure"
+ "com.apple.photos.shareddefaults"
+ "fd >= 0"
+ "input_image"
+ "isShortMovie"
+ "last_mask"
+ "last_salient_mask"
+ "model.mil"
+ "mubb_md4"
+ "plan phase %!u(MISSING)"
+ "prior_mask"
+ "salient_person_prior_mask"
+ "std::filesystem::is_directory(dir) && (dirfd = ::open(dir.string().data(), mode)) >= 0"
- "(fd = ::open(filename, flag | O_BINARY)) >= 0"
- "(p = reinterpret_cast<char*>(::mmap( 0, length, prot, MAP_SHARED, fd, 0))) != MAP_FAILED"
- "(trie_blob.size() %!t(MISSING)rie_->unit_size()) == (0)"
- "(trie_blob.size()) > (0)"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/bpe_model.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/filesystem.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/mmap.h"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_factory.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_interface.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/model_interface.h"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/normalizer.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/sentencepiece_processor.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/unigram_model.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/util.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/src/util.h"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1106: exception: failed to insert key: negative value"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1108: exception: failed to insert key: zero-length key"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1122: exception: failed to insert key: invalid null character"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: wrong key order"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1339: exception: failed to modify unit: too large offset"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1675: exception: failed to build double-array: invalid null character"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1677: exception: failed to build double-array: negative value"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:1692: exception: failed to build double-array: wrong key order"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:743: exception: failed to resize pool: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/darts_clone/darts.h:859: exception: failed to build rank index: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/AdaptiveSegmentAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/AudioAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/AudioClassifier.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/AudioVideoEmbeddingFuser.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/BlurAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNANSTHandsBodyDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNANSTHandsDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNBlurAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNBlurAnalyzerEspresso.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNBlurAnalyzerMPS.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlock.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockBinary.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockGPU.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockScalar.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockVector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNData.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNDataGPU.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFaceLandmarkDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFaceLandmarkDetectorEspresso.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFaceLandmarkDetectorMPS.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFastGestureRecognition.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFlattenBlock.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFullConnectionBlock.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFullConnectionBlockGPU.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNFullConnectionBlockScalar.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNGazeAnalysis.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNHandKeypointsDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNHandKeypointsDetectorEspresso.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNHandsDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNMLEnhancerEspresso.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNMLScalerEspresso.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNModel.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspresso.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspresso.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspressoV2.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspressoV2Data.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPersonDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPersonKeypointsDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPetsDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPetsDetectorEspresso.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPetsDetectorV2.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPetsKeypointsDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPoolingBlock.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPoolingBlockGPU.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPoolingBlockVector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPoseEstimator.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPoseEstimatorEspresso.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNPoseEstimatorMPS.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNSmileDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNSmileDetectorEspresso.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CNNSmileDetectorMPS.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CVUtilities.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CameraMotionAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CameraMotionSegment.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/CommSafety/VCPMADImageSafetyClassificationTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Convexhull.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/DatabaseReader.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/DescriptorAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/DescriptorSegment.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EdgeDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EmbeddingSummarizationAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EncodeAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EncodeStats.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsAVE1.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsAVE2.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsHW.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsSW.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ExifAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/FineSubjectMotionAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/FineSubjectMotionSegment.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Frame.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/FreeFormSearch.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/FullVideoAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/GaborFilter.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Histogram.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/HomeKitMotionAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/HoughTransform.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Human.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageBackboneAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageBlurAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageCaptionAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageCompositionAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageConverter.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageDescriptor.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageDescriptorWrapper.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageExposureAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageExposurePreAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageFaceDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageFaceExpressionAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageFaceQualityAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageHandsAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageHumanActionAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzer.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzerHolistic.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzerTopDown.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageLivePhotoBlurAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageManager.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageMotionFlowAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImagePetsAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImagePetsKeypointsAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageQualityAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzerBinary.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzerFull.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzerFullEspresso.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/InterAssetAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/InterestingnessAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/IrisAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/JunkAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/LandmarkDetector.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/LandmarkValidator.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/LightMotionAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/LightVideoAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/LivePhotoKeyFrameAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/LoudnessAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MADImageASTCFormatReader.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MADMovieBlastDoorAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MatrixOperationsForFace.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MediaAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MetaTrackDecoder.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFieldAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPBackwarp.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPCorrelation.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPFlowDecoder.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPFlowFeatureExtractor.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPFlowUtils.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPMoFlowSingleEspresso.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPModelR2D2.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlowAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionFlowSubtleMotionAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MotionSearch.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MovieAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MovieCurationAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MovieHighlightAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MovingObjectAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/MovingObjectSegment.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/NSDictionary+MediaAnalysis.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Object.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ObjectDetection.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ObjectTracking.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ObstructionAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/PHAssetResourceManager+MediaAnalysis.m"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/PhotoAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/Face/VCPMADPersonIdentificationTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceCropManager.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceProcessingVersionManager.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceUtils.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFullAnalysisAssetProcessingTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFullAnalysisURLProcessingTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosAutoCounterWorker.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosFace.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosQuickFaceDetectionManager.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosQuickFaceIdentificationManager.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosSceneprintAssetProcessingTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPSceneProcessingImageManager.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPVideoStabilizationAssetProcessingTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/PnPSolver.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/PreEncodeAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/QualityAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/RotationAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/RotationSegment.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Rotator.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Scaler.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SceneAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SceneChangeAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Segment.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Service/MADPersonalizedEmbeddingTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Service/VCPMADServiceImageAsset.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/ShapeModel.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SlowMotionAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SongDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/StillImageMetaAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SubjectMotionAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SubjectMotionSegment.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SubtleMotionAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/SubtleMotionSegment.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/TensorModel.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Text/MADTextEmbeddingCalibration.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Text/MADTextEmbeddingThreshold.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Text/MADTextEmbeddingThresholdMD4.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/TextEncoder.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/TrackSegment.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/TrackingAnalysis.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/Transforms.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPAnalysisProgressQuery.m"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPColorNormalizationAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPContentAnalysis.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPDownloadManager.m"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPFrameAnalysisStats.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPInternetReachability.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPPoolBasedPixelBufferCreator.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPPreAnalysisImage.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPPreAnalysisImageLoader.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPPreAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPPriorityAnalysis.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPRTLandmarkDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPSceneprintDescriptor.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPSceneprintDescriptorWrapper.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPTimeMeasurement.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPURLAsset.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPVideoEmbeddings.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VCPWallpaperAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VanishingPointDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoActivityAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoActivityDescriptor.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoAnalysisCommon.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNActionClassifier.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNAutoplay.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNBackbone.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNCameraMotion.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNHighlight.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCNNQuality.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCaptionAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoCaptionEncoder.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoFaceMeshAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoFacePoseAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoFacePoseFilter.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoFullFaceDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoGlobalAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoGyroStabilizer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoHumanActionAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoKeyFrame.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoKeyFrameAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoLightFaceDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoMetaFaceAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoMetaFocusAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoMetaLivePhotoMetaAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoMetaMotionAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoMetaOrientationAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoMetaSegmentAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoObjectTracker.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoPersonDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoPetsActionAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoPetsAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoPixelStabilizer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoRanker.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoSafetyClassifier.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoSaliencyAnalyzer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoSceneClassifier.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoStabilizer.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoTrackStandardDecoder.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoTrackSubsamplingDecoder.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoTrackSyncDecoder.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VideoTransformerBackbone.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADHEICSAlphaSequenceTranscoder.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADHEICSAlphaSequenceWriter.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADHEVCAlphaSequenceWriter.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADPNGAlphaSequenceWriter.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADVideoRemoveBackgroundCropTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADImageCaptionTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADImageEmbeddingTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADMLEnhancementTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADMLScalingTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIDocumentRecognitionTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIFaceTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIMachineReadableCodeDetectionTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIRectangleDetectionTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVISceneClassificationTask.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VoiceDetector.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/MediaAnalysis/VoiceDetectorV2.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/MovieCurationResults.m"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPCaptureAnalysisSession.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPCoreMLFeatureProviderGestureVideo.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureClassifier.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureImageRequest.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureMitigator.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureVideoRequest.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHandPoseImageRequest.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHandPoseVideoRequest.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHumanPoseEspressoSession.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHumanPoseImageRequest.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPHumanPoseVideoRequest.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPMotionFlowRequest.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPPetsPoseImageRequest.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPVideoProcessor.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPVideoProcessorSession.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/VideoProcessing/VCPVideoSyncFrameDecoder.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/iCloud/MediaAnalysis/Image/MAImageAnalysisRequest.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/iCloud/MediaAnalysis/MAComputeRequest.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/iCloud/MediaAnalysis/Movie/MAAssetByteStream.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/iCloud/MediaAnalysis/Movie/MAMovieAnalysisRequest.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/iCloud/Proto/MAImageComputeResult+CFDictionary.cpp"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MediaAnalysis/iCloud/Proto/VCPProtoImageHumanPoseResult+CFDictionary.cpp"
- "@\"VSKClient\"8@?0"
- "SearchUnifiedEmbeddingMD4"
- "hiddenEmbedding"
- "model_->status().ok()"
- "mubb_md3.bundle"
- "mubb_md4.bundle"
- "r"
- "r+"
- "spatialEmbedding"
- "unknown open mode: "

```
