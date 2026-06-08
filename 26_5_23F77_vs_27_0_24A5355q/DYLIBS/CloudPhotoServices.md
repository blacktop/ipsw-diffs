## CloudPhotoServices

> `/System/Library/PrivateFrameworks/CloudPhotoServices.framework/CloudPhotoServices`

```diff

-852.0.102.0.0
-  __TEXT.__text: 0x7618
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0x208
-  __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__cstring: 0x8a5
-  __TEXT.__oslogstring: 0x9fa
-  __TEXT.__unwind_info: 0x1a8
-  __TEXT.__objc_classname: 0x46
-  __TEXT.__objc_methname: 0x164f
-  __TEXT.__objc_methtype: 0x2e6
-  __TEXT.__objc_stubs: 0x1400
-  __DATA_CONST.__got: 0x2c8
+910.14.107.0.0
+  __TEXT.__text: 0x7b78
+  __TEXT.__objc_methlist: 0x220
+  __TEXT.__const: 0xb8
+  __TEXT.__gcc_except_tab: 0x200
+  __TEXT.__cstring: 0x900
+  __TEXT.__oslogstring: 0xbd2
+  __TEXT.__unwind_info: 0x188
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x540
+  __DATA_CONST.__objc_selrefs: 0x578
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x218
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x560
+  __DATA_CONST.__got: 0x2e8
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0x5e0
   __AUTH_CONST.__objc_const: 0x198
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x60
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__common: 0x1
+  __DATA_DIRTY.__common: 0x2
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0C7B5389-4404-3406-8695-AE2726621853
-  Functions: 70
-  Symbols:   546
-  CStrings:  345
+  UUID: 625A0B32-8871-3016-8F78-9B53D511C2AA
+  Functions: 74
+  Symbols:   575
+  CStrings:  162
 
Symbols:
+ +[CloudPhotoServices _createPartialResultsDirectoryForResourceFilename:destinationDirectory:error:]
+ +[CloudPhotoServices _createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:outPartialResultsURL:error:]
+ +[CloudPhotoServices convertVideoAtSourceURL:toDestinationURL:withPartialResultsURL:options:completionHandler:]
+ +[CloudPhotoServices transcodeVideoAtURL:withAdjustments:destinationURL:partialResultsURL:options:reason:isCancellable:completionHandler:]
+ GCC_except_table16
+ GCC_except_table25
+ _OBJC_CLASS_$_CPLPartialDerivativesGenerationResult
+ _OBJC_CLASS_$_PAMediaConversionServiceResourceURLCollection
+ _PAMediaConversionResourceRolePartialResultsTemporaryStorage
+ _UTTypePNG
+ ___138+[CloudPhotoServices transcodeVideoAtURL:withAdjustments:destinationURL:partialResultsURL:options:reason:isCancellable:completionHandler:]_block_invoke
+ ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke.100
+ ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke.76
+ ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke.82
+ ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke_2.85
+ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.145
+ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.152
+ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.153
+ ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.154
+ ___218+[CloudPhotoServices _createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:outPartialResultsURL:error:]_block_invoke
+ ___CPLResumableDerivativeGenerationOSLogDomain
+ ___CPLResumableDerivativeGenerationOSLogDomain.onceToken
+ ___CPLResumableDerivativeGenerationOSLogDomain.result
+ _____CPLResumableDerivativeGenerationOSLogDomain_block_invoke
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88r96r_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8s48l8r88l8s56l8s64l8s72l8r96l8s80l8
+ ___block_descriptor_129_e8_32s40s48s56s64s72s80s88r96r104r_e5_v8?0lr88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8r96l8r104l8
+ ___block_literal_global.132
+ ___block_literal_global.147
+ ___block_literal_global.158
+ ___block_literal_global.178
+ ___block_literal_global.181
+ ___block_literal_global.247
+ ___block_literal_global.250
+ ___block_literal_global.253
+ ___block_literal_global.57
+ ___block_literal_global.84
+ ___block_literal_global.87
+ __logResumableDerivativeGeneration
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_createPartialResultsDirectoryForResourceFilename:destinationDirectory:error:
+ _objc_msgSend$_createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:outPartialResultsURL:error:
+ _objc_msgSend$collectionWithMainResourceURL:
+ _objc_msgSend$convertVideoAtSourceURL:toDestinationURL:withPartialResultsURL:options:completionHandler:
+ _objc_msgSend$convertVideoAtSourceURLCollection:toDestinationURLCollection:options:completionHandler:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$initWithResources:partialResultsURL:
+ _objc_msgSend$setResourceURL:forRole:
+ _objc_msgSend$transcodeVideoAtURL:withAdjustments:destinationURL:partialResultsURL:options:reason:isCancellable:completionHandler:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_storeStrong
- +[CloudPhotoServices _createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:error:]
- +[CloudPhotoServices transcodeVideoAtURL:withAdjustments:destinationURL:options:reason:isCancellable:completionHandler:]
- GCC_except_table14
- GCC_except_table23
- ___120+[CloudPhotoServices transcodeVideoAtURL:withAdjustments:destinationURL:options:reason:isCancellable:completionHandler:]_block_invoke
- ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke.69
- ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke.75
- ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke.93
- ___176+[CloudPhotoServices _generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:]_block_invoke_2.78
- ___197+[CloudPhotoServices _createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:error:]_block_invoke
- ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.132
- ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.139
- ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.140
- ___203+[CloudPhotoServices _generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:]_block_invoke.141
- ___block_descriptor_112_e8_32s40s48s56s64s72s80r88r_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8s48l8r80l8s56l8s64l8r88l8s72l8
- ___block_descriptor_121_e8_32s40s48s56s64s72s80s88r96r_e5_v8?0lr88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8r96l8
- ___block_literal_global.119
- ___block_literal_global.134
- ___block_literal_global.144
- ___block_literal_global.164
- ___block_literal_global.167
- ___block_literal_global.229
- ___block_literal_global.232
- ___block_literal_global.53
- ___block_literal_global.77
- ___block_literal_global.80
- _objc_msgSend$_createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:error:
- _objc_msgSend$transcodeVideoAtURL:withAdjustments:destinationURL:options:reason:isCancellable:completionHandler:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%@-partialResults"
+ "CPLLogResumableDerivativeGeneration"
+ "Created partial results directory at %@"
+ "FAILED"
+ "Finished image derivative: %{public}@ %{public}@"
+ "Finished video derivative: %{public}@ %{public}@"
+ "Found existing partial results at %@"
+ "Found previously generated derivative, skipping generation for %@"
+ "SUCCESS"
+ "Starting image derivative: %{public}@"
+ "Starting video derivative: %{public}@ (preset: %{public}@)"
+ "Unable to create partial results directory at %@"
+ "Unable to delete partial results at %@: %@"
+ "Video transcode was cancelled: %{public}@"
+ "derivatives.resumable"
- "@\"NSArray\"16@0:8"
- "@16@0:8"
- "@24@0:8Q16"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16Q24@32"
- "@56@0:8@16Q24@32@40@48"
- "@68@0:8@16@24@32@40@48B56@?60"
- "B16@0:8"
- "B24@0:8@\"NSError\"16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@16"
- "B36@0:8@16Q24B32"
- "B92@0:8@16@24@32Q40B48@52@60@68q76^@84"
- "CPLDerivativeGenerator"
- "CloudPhotoServices"
- "CloudPhotoServicesUtilities"
- "Q24@0:8q16"
- "T@\"NSArray\",R,N"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathExtension:"
- "UUID"
- "UUIDString"
- "^{CGImageSource=}24@0:8@16"
- "_bestImageResourceTypeForPixelCount:"
- "_createCPLResourceFromURL:withResourceType:uniformType:itemScopedIdentifier:fingerprintScheme:"
- "_createDerivativeResourcesFromInputURL:resourceTypes:withItemScopedIdentifier:destinationDirectory:fingerprintScheme:outputResources:convertToSRGB:"
- "_createPosterFrameResourcesFromInputURL:withItemScopedIdentifier:includeDerivative:destinationDirectory:fingerprintScheme:outputResources:"
- "_createVideoResourcesFromInputURL:withItemScopedIdentifier:videoAdjustments:resourceType:forIris:destinationDirectory:fingerprintScheme:outputResources:weightInProgress:error:"
- "_extractVideoMetadataResourceFrom:destinationDirectory:fingerprintScheme:"
- "_filenameForResourceWithItemScopedIdentifier:resourceType:extension:"
- "_generateImageDerivativeResourcesFromInputResource:destinationDirectory:fingerprintScheme:isAdjusted:derivativesFilter:recordChangeType:completionHandler:"
- "_generateVideoDerivativeResourcesFromInputResource:withCPLAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrame:completionHandler:"
- "_imageServiceClient"
- "_shouldGenerateHDRMediumVideoDerivative"
- "_shouldGenerateLargeVideoDerivativeForAVAsset:"
- "_videoServiceClient"
- "addChild:withPendingUnitCount:"
- "addObject:"
- "adjustmentCompoundVersion"
- "adjustmentSourceType"
- "adjustmentTimestamp"
- "adjustmentType"
- "appendFormat:"
- "array"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "assetWithURL:"
- "attributesOfItemAtPath:error:"
- "boolForKey:"
- "boolValue"
- "canGenerateImageDerivativesFromType:"
- "canGenerateImageDerivativesFromUTI:"
- "code"
- "compare:"
- "conformsToType:"
- "convertImageAtSourceURL:options:completionHandler:"
- "convertVideoAtSourceURL:toDestinationURL:options:completionHandler:"
- "copyItemAtURL:toURL:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "creationDate"
- "currentDeviceHEVCCapabilities"
- "currentHandler"
- "currentProgress"
- "data"
- "date"
- "defaultManager"
- "derivativeGenerationThreshold"
- "derivativeImageResourceUniformTypeForResourceType:"
- "descriptionForResourceType:"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "dimensionsForAVAsset:"
- "discreteProgressWithTotalUnitCount:"
- "domain"
- "errorWithDomain:code:userInfo:"
- "extractStillImageFromVideoAtSourceURL:toDestinationURL:options:completionHandler:"
- "fileExistsAtPath:"
- "fileSize"
- "fileURL"
- "fileUTI"
- "fingerPrintForFileAtURL:error:"
- "firstVideoTrackCodec"
- "generateDerivativeResourcesFromInputResource:withAdjustments:destinationDirectory:fingerprintScheme:derivativesFilter:recordChangeType:includePosterFrameForVideo:completionHandler:"
- "generateDerivativeResourcesFromInputResource:withAdjustments:destinationDirectory:fingerprintScheme:includePosterFrameForVideo:completionHandler:"
- "generateFullSizeJPEGIfNecessaryFromInputResource:destinationDirectory:fingerprintScheme:completionHandler:"
- "generateGIFForVideoAtURL:destinationURL:completionHandler:"
- "generatePosterFrameForVideoAtURL:maximumPixelCount:destinationURL:reason:completionHandler:"
- "getDimensionsFromImageProperties:orientationOut:widthOut:heightOut:"
- "getResourceValue:forKey:error:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasEmbeddedJPEGSuitableForDerivativesInImageAtURL:metadata:error:"
- "identifier"
- "identity"
- "indexesOfObjectsPassingTest:"
- "initWithAVAsset:timeZoneLookup:"
- "initWithAVURL:timeZoneLookup:"
- "initWithCapacity:"
- "initWithFileURL:"
- "initWithFormatIdentifier:formatVersion:data:baseVersion:editorBundleID:renderTypes:"
- "initWithImageURL:contentType:timeZoneLookup:"
- "initWithResourceIdentity:itemScopedIdentifier:resourceType:"
- "initWithSourceResourceType:uti:changeType:droppingDerivativeTypes:"
- "initWithTimeIntervalSinceReferenceDate:"
- "initWithUnsignedInteger:"
- "initialize"
- "intValue"
- "integerValue"
- "involvedProcesses"
- "isCancelled"
- "isCompatibleWithPhotosTranscodingServiceWithOptions:"
- "isEmpty"
- "isEqual:"
- "isEqualToString:"
- "isHDR"
- "isMovieUTI:"
- "isTransientDerivativeGenerationError:"
- "isUnsupportedOriginalFormatError:"
- "itemScopedIdentifier"
- "lastPathComponent"
- "length"
- "livePhotoPairingIdentifierMetadataKey"
- "maxPixelSizeForResourceType:"
- "mightDropSomeDerivativesForSourceType:forChangeType:"
- "mutableCopy"
- "naturalSize"
- "newImageSourceFromImageAtURL:"
- "null"
- "numberWithBool:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectsAtIndexes:"
- "operationCancelledError"
- "orientedPixelSize"
- "originatingAssetIdentifierMetadataKey"
- "paMediaConversionColorSpaceForCloudPhotoDerivativeColorOutput:"
- "path"
- "pathExtension"
- "performAsCurrentWithPendingUnitCount:usingBlock:"
- "policyWithKey:value:"
- "policyWithPolicies:"
- "preferredFilenameExtension"
- "preferredTransform"
- "progressWithTotalUnitCount:"
- "propertyListDictionary"
- "q24@0:8q16"
- "removeAllCachedResourceValues"
- "removeItemAtURL:error:"
- "removeObject:"
- "resizeImageAtURL:destinationURL:maximumPixelCount:bakeInOrientation:colorOutput:reason:completionHandler:"
- "resizeImageAtURL:destinationURL:options:completionHandler:"
- "resourceType"
- "scopeIdentifier"
- "setAdjustmentTimestamp:"
- "setAttributes:ofItemAtPath:error:"
- "setAvailable:"
- "setCompletedUnitCount:"
- "setFileSize:"
- "setFileUTI:"
- "setFingerPrint:"
- "setImageDimensions:"
- "setObject:forKeyedSubscript:"
- "setTotalUnitCount:"
- "shortDescriptionForResourceType:"
- "shouldDropDerivativeWithDropDerivativeRecipe:"
- "shouldGenerateVideoDerivativeForAVAsset:forResourceType:adjusted:"
- "simpleAdjustmentData"
- "sizeOfImageAtURL:orientationOut:"
- "standardPolicy"
- "standardUserDefaults"
- "string"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "timeIntervalSinceDate:"
- "totalUnitCount"
- "tracksWithMediaType:forAsset:"
- "transcodeVideoAtURL:withAdjustments:destinationURL:options:reason:isCancellable:completionHandler:"
- "typeWithFilenameExtension:conformingToType:"
- "typeWithIdentifier:"
- "unsignedIntegerValue"
- "uppercaseString"
- "v16@0:8"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16^i24^i32^i40"
- "v56@0:8@16q24@32@40@?48"
- "v60@0:8@16@24@32@40B48@?52"
- "v64@0:8@16@24@?32@40@48@56"
- "v68@0:8@16@24@32@40@48@56B64"
- "v68@0:8@16@24@32B40@44Q52@?60"
- "v68@0:8@16@24q32B40q44@52@?60"
- "v76@0:8@\"CPLResource\"16@\"CPLAdjustments\"24@\"NSURL\"32@\"CPLFingerprintScheme\"40@\"CPLDerivativesFilter\"48Q56B64@?<v@?@\"NSArray\"@\"NSError\">68"
- "v76@0:8@16@24@32@40@48Q56B64@?68"
- "workQueue"
- "writeToURL:options:error:"
- "{CGSize=dd}24@0:8@16"
- "{CGSize=dd}32@0:8@16^i24"

```
