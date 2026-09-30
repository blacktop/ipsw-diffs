## MediaConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService`

```diff

-912.0.234.0.0
-  __TEXT.__text: 0x1b520
-  __TEXT.__objc_methlist: 0x1c3c
+912.0.235.0.0
+  __TEXT.__text: 0x1e05c
+  __TEXT.__objc_methlist: 0x1eec
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x58c
-  __TEXT.__cstring: 0x4c8c
-  __TEXT.__oslogstring: 0x2564
-  __TEXT.__unwind_info: 0x710
+  __TEXT.__gcc_except_tab: 0x5a0
+  __TEXT.__cstring: 0x5970
+  __TEXT.__oslogstring: 0x28ca
+  __TEXT.__unwind_info: 0x778
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xae0
-  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__const: 0xcd8
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14b0
+  __DATA_CONST.__objc_selrefs: 0x1638
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_arraydata: 0x4c8
-  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_arraydata: 0x578
+  __DATA_CONST.__got: 0x3b8
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x2da0
-  __AUTH_CONST.__objc_const: 0x2a78
+  __AUTH_CONST.__cfstring: 0x3460
+  __AUTH_CONST.__objc_const: 0x2f88
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x200
-  __DATA.__data: 0x488
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x250
+  __DATA.__data: 0x4a8
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 640
-  Symbols:   1897
-  CStrings:  553
+  Functions: 708
+  Symbols:   2066
+  CStrings:  623
 
Symbols:
+ -[ConversionOptionSet setSourcePathProvenanceUnprocessedImage:]
+ -[ConversionOptionSet sourcePathProvenanceUnprocessedImage]
+ -[PAImageConversionServiceClient(ContentProvenance) embedProcessedProvenanceFromRegularImageAtURL:intoRegularImageAtURL:destinationURL:options:completionHandler:]
+ -[PAImageConversionServiceClient(ContentProvenance) embedUnprocessedProvenanceImageAtURL:intoRegularImageAtURL:destinationURL:options:completionHandler:]
+ -[PAImageConversionServiceClient(ContentProvenance) processContentProvenanceForSourceURLCollection:destinationURL:options:completionHandler:]
+ -[PAImageConversionServiceClient(ContentProvenance) stripProvenanceMetadataFromOriginalProvenanceImageAtURL:destinationURL:options:completionHandler:]
+ -[PAImageConversionServiceClient(ContentProvenance) validateContentProvenanceForProcessedImageAtURL:options:completionHandler:]
+ -[PAMediaConversionServiceContentProvenanceProcessingResult .cxx_destruct]
+ -[PAMediaConversionServiceContentProvenanceProcessingResult diagnosticsRequested]
+ -[PAMediaConversionServiceContentProvenanceProcessingResult setDiagnosticsRequested:]
+ -[PAMediaConversionServiceContentProvenanceProcessingResult setUtcLowerBoundTimestamp:]
+ -[PAMediaConversionServiceContentProvenanceProcessingResult setUtcProcessingTimestamp:]
+ -[PAMediaConversionServiceContentProvenanceProcessingResult setUtcUpperBoundTimestamp:]
+ -[PAMediaConversionServiceContentProvenanceProcessingResult utcLowerBoundTimestamp]
+ -[PAMediaConversionServiceContentProvenanceProcessingResult utcProcessingTimestamp]
+ -[PAMediaConversionServiceContentProvenanceProcessingResult utcUpperBoundTimestamp]
+ -[PAMediaConversionServiceContentProvenanceValidationResult .cxx_destruct]
+ -[PAMediaConversionServiceContentProvenanceValidationResult certificateVerificationStatus]
+ -[PAMediaConversionServiceContentProvenanceValidationResult init]
+ -[PAMediaConversionServiceContentProvenanceValidationResult processedJPEGImageData]
+ -[PAMediaConversionServiceContentProvenanceValidationResult revocationCheckIdentifier]
+ -[PAMediaConversionServiceContentProvenanceValidationResult revocationStatus]
+ -[PAMediaConversionServiceContentProvenanceValidationResult setCertificateVerificationStatus:]
+ -[PAMediaConversionServiceContentProvenanceValidationResult setProcessedJPEGImageData:]
+ -[PAMediaConversionServiceContentProvenanceValidationResult setRevocationCheckIdentifier:]
+ -[PAMediaConversionServiceContentProvenanceValidationResult setRevocationStatus:]
+ -[PAMediaConversionServiceContentProvenanceValidationResult setSignatureVerificationStatus:]
+ -[PAMediaConversionServiceContentProvenanceValidationResult setUtcLowerBoundTimestamp:]
+ -[PAMediaConversionServiceContentProvenanceValidationResult setUtcProcessingTimestamp:]
+ -[PAMediaConversionServiceContentProvenanceValidationResult setUtcUpperBoundTimestamp:]
+ -[PAMediaConversionServiceContentProvenanceValidationResult signatureVerificationStatus]
+ -[PAMediaConversionServiceContentProvenanceValidationResult utcLowerBoundTimestamp]
+ -[PAMediaConversionServiceContentProvenanceValidationResult utcProcessingTimestamp]
+ -[PAMediaConversionServiceContentProvenanceValidationResult utcUpperBoundTimestamp]
+ -[PAMediaConversionServiceContentProvenanceValidationResult validationStatus]
+ -[PHMediaFormatConversionCompositeRequest requiresProvenanceMetadataChange]
+ -[PHMediaFormatConversionImplementation_MediaConversionService _submitAdjustedProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:]
+ -[PHMediaFormatConversionImplementation_MediaConversionService _submitProvenanceProcessedEmbedRequest:destination:options:completionHandler:]
+ -[PHMediaFormatConversionRequest _requiresNonProvenanceMetadataChange]
+ -[PHMediaFormatConversionRequest provenanceAdjustedRenderSourceURL]
+ -[PHMediaFormatConversionRequest provenanceMetadataBehavior]
+ -[PHMediaFormatConversionRequest provenanceProcessedOriginalDestinationURL]
+ -[PHMediaFormatConversionRequest provenanceProcessedSourceImageURL]
+ -[PHMediaFormatConversionRequest provenanceSidecarURL]
+ -[PHMediaFormatConversionRequest requiresProvenanceMetadataChange]
+ -[PHMediaFormatConversionRequest setProvenanceMetadataBehavior:withProcessedSourceImageURL:]
+ -[PHMediaFormatConversionRequest setProvenanceMetadataBehavior:withProvenanceSidecarURL:]
+ -[PHMediaFormatConversionRequest setProvenanceMetadataBehavior:withUnprocessedSourceAdjustedRenderURL:processedOriginalDestinationURL:sidecarURL:]
+ -[PHMediaFormatConversionRequest setShouldPreserveProvenance:]
+ -[PHMediaFormatConversionRequest shouldPreserveProvenance]
+ -[PHMediaFormatConversionSource checkForProvenanceData]
+ -[PHMediaFormatConversionSource markProvenanceMetadataAsCheckedWithStatus:]
+ -[PHMediaFormatConversionSource provenanceMetadataStatus]
+ -[PHMediaFormatConversionSource setProvenanceMetadataStatus:]
+ -[PHMediaFormatConversionSource sourceProvenanceMetadataStatus]
+ GCC_except_table137
+ GCC_except_table152
+ GCC_except_table154
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table169
+ GCC_except_table175
+ GCC_except_table404
+ GCC_except_table406
+ GCC_except_table408
+ GCC_except_table410
+ GCC_except_table412
+ GCC_except_table414
+ GCC_except_table416
+ GCC_except_table418
+ GCC_except_table533
+ GCC_except_table541
+ GCC_except_table571
+ GCC_except_table573
+ GCC_except_table661
+ GCC_except_table663
+ GCC_except_table666
+ GCC_except_table668
+ GCC_except_table681
+ GCC_except_table92
+ GCC_except_table94
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_PAMediaConversionServiceContentProvenanceProcessingResult
+ _OBJC_CLASS_$_PAMediaConversionServiceContentProvenanceValidationResult
+ _OBJC_IVAR_$_ConversionOptionSet._sourcePathProvenanceUnprocessedImage
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceProcessingResult._diagnosticsRequested
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceProcessingResult._utcLowerBoundTimestamp
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceProcessingResult._utcProcessingTimestamp
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceProcessingResult._utcUpperBoundTimestamp
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceValidationResult._certificateVerificationStatus
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceValidationResult._processedJPEGImageData
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceValidationResult._revocationCheckIdentifier
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceValidationResult._revocationStatus
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceValidationResult._signatureVerificationStatus
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceValidationResult._utcLowerBoundTimestamp
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceValidationResult._utcProcessingTimestamp
+ _OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceValidationResult._utcUpperBoundTimestamp
+ _OBJC_IVAR_$_PHMediaFormatConversionRequest._provenanceAdjustedRenderSourceURL
+ _OBJC_IVAR_$_PHMediaFormatConversionRequest._provenanceMetadataBehavior
+ _OBJC_IVAR_$_PHMediaFormatConversionRequest._provenanceProcessedOriginalDestinationURL
+ _OBJC_IVAR_$_PHMediaFormatConversionRequest._provenanceProcessedSourceImageURL
+ _OBJC_IVAR_$_PHMediaFormatConversionRequest._provenanceSidecarURL
+ _OBJC_IVAR_$_PHMediaFormatConversionRequest._shouldPreserveProvenance
+ _OBJC_IVAR_$_PHMediaFormatConversionSource._provenanceMetadataStatus
+ _OBJC_METACLASS_$_PAMediaConversionServiceContentProvenanceProcessingResult
+ _OBJC_METACLASS_$_PAMediaConversionServiceContentProvenanceValidationResult
+ _PAMediaConversionIsProvenanceEligibilityError
+ _PAMediaConversionIsProvenanceProcessingTimeoutError
+ _PAMediaConversionResourceRoleProvenanceProcessedSourceImage
+ _PAMediaConversionResourceRoleProvenanceUnprocessed
+ _PAMediaConversionServiceOptionClientProcessNameKey
+ _PAMediaConversionServiceOptionIsContentProvenanceDryRunKey
+ _PAMediaConversionServiceOptionIsContentProvenanceMetadataStrippingConversionKey
+ _PAMediaConversionServiceOptionIsContentProvenanceProcessedEmbeddingConversionKey
+ _PAMediaConversionServiceOptionIsContentProvenanceProcessingConversionKey
+ _PAMediaConversionServiceOptionIsContentProvenanceUnprocessedEmbeddingConversionKey
+ _PAMediaConversionServiceOptionIsContentProvenanceValidationKey
+ _PAMediaConversionServiceOptionIsContentProvenanceValidationUnwrappedImageKey
+ _PAMediaConversionServiceOptionPreserveProvenanceKey
+ _PAMediaConversionServiceOptionProvenanceOriginalAssetLocalIdentifierKey
+ _PAMediaConversionServiceOptionUnitTestSupportUseMockProvenanceProcessingKey
+ _PAMediaConversionServiceProvenanceCertificateVerificationStatusKey
+ _PAMediaConversionServiceProvenanceCloudAppErrorDomain
+ _PAMediaConversionServiceProvenanceDiagnosticsRequestedKey
+ _PAMediaConversionServiceProvenanceProcessingDateAgeTimeIntervalKey
+ _PAMediaConversionServiceProvenanceProcessingResultMetadataKey
+ _PAMediaConversionServiceProvenanceRevocationCheckIdentifierKey
+ _PAMediaConversionServiceProvenanceRevocationStatusKey
+ _PAMediaConversionServiceProvenanceRoundTripDurationKey
+ _PAMediaConversionServiceProvenanceSignatureVerificationStatusKey
+ _PAMediaConversionServiceProvenanceUTCLowerBoundTimestampKey
+ _PAMediaConversionServiceProvenanceUTCProcessingTimestampKey
+ _PAMediaConversionServiceProvenanceUTCUpperBoundTimestampKey
+ _PAMediaConversionServiceProvenanceUploadDurationKey
+ _PAMediaConversionServiceProvenanceValidationResultMetadataKey
+ _UTTypeDNG
+ __OBJC_$_INSTANCE_METHODS_PAImageConversionServiceClient(ContentProvenance)
+ __OBJC_$_INSTANCE_METHODS_PAMediaConversionServiceContentProvenanceProcessingResult
+ __OBJC_$_INSTANCE_METHODS_PAMediaConversionServiceContentProvenanceValidationResult
+ __OBJC_$_INSTANCE_VARIABLES_PAMediaConversionServiceContentProvenanceProcessingResult
+ __OBJC_$_INSTANCE_VARIABLES_PAMediaConversionServiceContentProvenanceValidationResult
+ __OBJC_$_PROP_LIST_PAMediaConversionServiceContentProvenanceProcessingResult
+ __OBJC_$_PROP_LIST_PAMediaConversionServiceContentProvenanceValidationResult
+ __OBJC_CLASS_RO_$_PAMediaConversionServiceContentProvenanceProcessingResult
+ __OBJC_CLASS_RO_$_PAMediaConversionServiceContentProvenanceValidationResult
+ __OBJC_METACLASS_RO_$_PAMediaConversionServiceContentProvenanceProcessingResult
+ __OBJC_METACLASS_RO_$_PAMediaConversionServiceContentProvenanceValidationResult
+ ___127-[PAImageConversionServiceClient(ContentProvenance) validateContentProvenanceForProcessedImageAtURL:options:completionHandler:]_block_invoke
+ ___141-[PAImageConversionServiceClient(ContentProvenance) processContentProvenanceForSourceURLCollection:destinationURL:options:completionHandler:]_block_invoke
+ ___141-[PHMediaFormatConversionImplementation_MediaConversionService _submitProvenanceProcessedEmbedRequest:destination:options:completionHandler:]_block_invoke
+ ___150-[PAImageConversionServiceClient(ContentProvenance) stripProvenanceMetadataFromOriginalProvenanceImageAtURL:destinationURL:options:completionHandler:]_block_invoke
+ ___153-[PAImageConversionServiceClient(ContentProvenance) embedUnprocessedProvenanceImageAtURL:intoRegularImageAtURL:destinationURL:options:completionHandler:]_block_invoke
+ ___162-[PAImageConversionServiceClient(ContentProvenance) embedProcessedProvenanceFromRegularImageAtURL:intoRegularImageAtURL:destinationURL:options:completionHandler:]_block_invoke
+ ___165-[PHMediaFormatConversionImplementation_MediaConversionService _submitAdjustedProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:]_block_invoke
+ ___75-[PHMediaFormatConversionCompositeRequest requiresProvenanceMetadataChange]_block_invoke
+ ___block_descriptor_40_e8_32bs_e37_v32?0q8"NSDictionary"16"NSError"24ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?0q8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v24?0q8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e37_v32?0q8"NSDictionary"16"NSError"24ls32l8s40l8s48l8s56l8s64l8s72l8
+ _getprogname
+ _objc_msgSend$_requiresNonProvenanceMetadataChange
+ _objc_msgSend$_submitAdjustedProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:
+ _objc_msgSend$_submitProvenanceProcessedEmbedRequest:destination:options:completionHandler:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$checkForProvenanceData
+ _objc_msgSend$embedProcessedProvenanceFromRegularImageAtURL:intoRegularImageAtURL:destinationURL:options:completionHandler:
+ _objc_msgSend$hasProvenanceMetadata
+ _objc_msgSend$mainBundle
+ _objc_msgSend$markProvenanceMetadataAsCheckedWithStatus:
+ _objc_msgSend$provenanceAdjustedRenderSourceURL
+ _objc_msgSend$provenanceMetadataBehavior
+ _objc_msgSend$provenanceMetadataStatus
+ _objc_msgSend$provenanceProcessedOriginalDestinationURL
+ _objc_msgSend$provenanceProcessedSourceImageURL
+ _objc_msgSend$provenanceSidecarURL
+ _objc_msgSend$requiresProvenanceMetadataChange
+ _objc_msgSend$setCertificateVerificationStatus:
+ _objc_msgSend$setDiagnosticsRequested:
+ _objc_msgSend$setProcessedJPEGImageData:
+ _objc_msgSend$setProvenanceMetadataBehavior:withProcessedSourceImageURL:
+ _objc_msgSend$setProvenanceMetadataBehavior:withProvenanceSidecarURL:
+ _objc_msgSend$setProvenanceMetadataBehavior:withUnprocessedSourceAdjustedRenderURL:processedOriginalDestinationURL:sidecarURL:
+ _objc_msgSend$setRevocationCheckIdentifier:
+ _objc_msgSend$setRevocationStatus:
+ _objc_msgSend$setShouldPreserveProvenance:
+ _objc_msgSend$setSignatureVerificationStatus:
+ _objc_msgSend$setSourcePathProvenanceUnprocessedImage:
+ _objc_msgSend$setUtcLowerBoundTimestamp:
+ _objc_msgSend$setUtcProcessingTimestamp:
+ _objc_msgSend$setUtcUpperBoundTimestamp:
+ _objc_msgSend$shouldPreserveProvenance
+ _objc_msgSend$sourcePathProvenanceUnprocessedImage
+ _objc_msgSend$sourceProvenanceMetadataStatus
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$stripProvenanceMetadataFromOriginalProvenanceImageAtURL:destinationURL:options:completionHandler:
- GCC_except_table112
- GCC_except_table114
- GCC_except_table116
- GCC_except_table119
- GCC_except_table129
- GCC_except_table135
- GCC_except_table347
- GCC_except_table349
- GCC_except_table351
- GCC_except_table353
- GCC_except_table355
- GCC_except_table357
- GCC_except_table359
- GCC_except_table474
- GCC_except_table482
- GCC_except_table506
- GCC_except_table508
- GCC_except_table594
- GCC_except_table596
- GCC_except_table599
- GCC_except_table601
- GCC_except_table614
- GCC_except_table62
- GCC_except_table64
- GCC_except_table97
- __OBJC_$_INSTANCE_METHODS_PAImageConversionServiceClient
CStrings:
+ "#Q"
+ "--source-provenance-unprocessed-image is only valid for image conversions\n"
+ "-t|--type [%@] -s|--source <input media path> -d|--destination <output media path> [--source-video-complement <input media path>] [--destination-video-complement <output media path>] [--source-provenance-unprocessed-image <input provenance image path>] [--partial-results-cache-directory <cache directory path>] [--replace] [[-o|--option <key>=<value>], ...] [-r|--preset <preset>] [-c|--count <count>] [-v|--verbose] [--wait] [-p|--progress] [--pause] [--launch] [--launch-and-pause] [--next]"
+ "Invalid request using single pass encoding option and metadata changes (like location stripping, custom location, custom creation date, custom description, custom provenance) for video source %@"
+ "Network.NWError"
+ "PAMediaConversionResourceRoleProvenanceProcessedSourceImage"
+ "PAMediaConversionResourceRoleProvenanceUnprocessed"
+ "PAMediaConversionServiceErrorCodeMissingProvenanceProcessedMetadata"
+ "PAMediaConversionServiceErrorCodeMissingProvenanceUnprocessedMetadata"
+ "PAMediaConversionServiceErrorCodeProvenanceCloudAppInternalError"
+ "PAMediaConversionServiceErrorCodeProvenanceCloudAppManifestCertificateVerificationFailed"
+ "PAMediaConversionServiceErrorCodeProvenanceCloudAppSEPSignatureVerificationFailed"
+ "PAMediaConversionServiceErrorCodeProvenanceCloudAppSensorSignatureVerificationFailed"
+ "PAMediaConversionServiceErrorCodeProvenanceCloudAppUnknown"
+ "PAMediaConversionServiceErrorCodeProvenanceIneligible"
+ "PAMediaConversionServiceErrorCodeProvenanceMalformedResponse"
+ "PAMediaConversionServiceErrorCodeProvenanceMissingPayload"
+ "PAMediaConversionServiceErrorCodeProvenanceProcessedValidationFailure"
+ "PAMediaConversionServiceErrorCodeProvenanceProcessingDateExpired"
+ "PAMediaConversionServiceErrorCodeProvenanceRevocationCheckFailure"
+ "PAMediaConversionServiceErrorCodeProvenanceSourceDNGUnavailable"
+ "PAMediaConversionServiceErrorCodeProvenanceTemporaryFileWriteFailure"
+ "PAMediaConversionServiceErrorCodeProvenanceTimeout"
+ "PAMediaConversionServiceOptionClientProcessNameKey"
+ "PAMediaConversionServiceOptionIsContentProvenanceDryRunKey"
+ "PAMediaConversionServiceOptionIsContentProvenanceMetadataStrippingConversionKey"
+ "PAMediaConversionServiceOptionIsContentProvenanceProcessedEmbeddingConversionKey"
+ "PAMediaConversionServiceOptionIsContentProvenanceProcessingConversionKey"
+ "PAMediaConversionServiceOptionIsContentProvenanceUnprocessedEmbeddingConversionKey"
+ "PAMediaConversionServiceOptionIsContentProvenanceValidationKey"
+ "PAMediaConversionServiceOptionIsContentProvenanceValidationUnwrappedImageKey"
+ "PAMediaConversionServiceOptionPreserveProvenanceKey"
+ "PAMediaConversionServiceOptionProvenanceOriginalAssetLocalIdentifierKey"
+ "PAMediaConversionServiceOptionUnitTestSupportUseMockProvenanceProcessingKey"
+ "PAMediaConversionServiceProvenanceCertificateVerificationStatusKey"
+ "PAMediaConversionServiceProvenanceCloudAppErrorDomain"
+ "PAMediaConversionServiceProvenanceDiagnosticsRequestedKey"
+ "PAMediaConversionServiceProvenanceProcessingDateAgeTimeIntervalKey"
+ "PAMediaConversionServiceProvenanceProcessingResultMetadataKey"
+ "PAMediaConversionServiceProvenanceRevocationCheckIdentifierKey"
+ "PAMediaConversionServiceProvenanceRevocationStatusKey"
+ "PAMediaConversionServiceProvenanceRoundTripDurationKey"
+ "PAMediaConversionServiceProvenanceSignatureVerificationStatusKey"
+ "PAMediaConversionServiceProvenanceUTCLowerBoundTimestampKey"
+ "PAMediaConversionServiceProvenanceUTCProcessingTimestampKey"
+ "PAMediaConversionServiceProvenanceUTCUpperBoundTimestampKey"
+ "PAMediaConversionServiceProvenanceUploadDurationKey"
+ "PAMediaConversionServiceProvenanceValidationResultMetadataKey"
+ "PrivateCloudComputeError"
+ "Provenance embed processed failed: %@. Original: %@, Carrier: %@"
+ "Provenance embed processed succeeded. Destination: %@"
+ "Provenance processing failed: %@. Source: %@"
+ "Provenance processing succeeded. Destination URL: %@"
+ "Provenance provenanceSidecarURL is nil."
+ "Provenance stripping failed: %@. Source: %@"
+ "Provenance stripping succeeded. Destination: %@"
+ "Read provenance metadata status: %ld from file: %@"
+ "Requesting Provenance embed processed metadata from original: %@ into carrier: %@, destination: %@."
+ "Requesting Provenance processing with source: %@, destination: %@."
+ "Requesting Provenance strip metadata at URL: %@, destination: %@."
+ "Requesting single-pass Provenance processing with adjusted render. Source: %@, destination: %@."
+ "Single-pass Provenance processing failed: %@. Source: %@"
+ "Single-pass Provenance processing succeeded. Destination URL: %@"
+ "[sourceURLCollection resourceURLForRole:PAMediaConversionResourceRoleMainResource]"
+ "destinationURL"
+ "imageURL"
+ "originalProvenanceImageURL"
+ "processedProvenanceImageURL"
+ "regularImageURL"
+ "request.provenanceProcessedOriginalDestinationURL"
+ "source-provenance-unprocessed-image"
+ "unprocessedProvenanceImageURL"
+ "v24@?0q8@\"NSError\"16"
- "#A"
- "-t|--type [%@] -s|--source <input media path> -d|--destination <output media path> [--source-video-complement <input media path>] [--destination-video-complement <output media path>] [--partial-results-cache-directory <cache directory path>] [--replace] [[-o|--option <key>=<value>], ...] [-r|--preset <preset>] [-c|--count <count>] [-v|--verbose] [--wait] [-p|--progress] [--pause] [--launch] [--launch-and-pause] [--next]"
- "Invalid request using single pass encoding option and metadata changes (like location stripping, custom location, custom creation date, custom description) for video source %@"
```
