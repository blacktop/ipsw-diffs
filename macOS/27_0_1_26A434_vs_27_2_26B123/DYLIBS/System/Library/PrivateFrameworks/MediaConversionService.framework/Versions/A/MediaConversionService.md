## MediaConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/Versions/A/MediaConversionService`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x200e0
-  __TEXT.__objc_methlist: 0x1eec
+916.58.114.0.0
+  __TEXT.__text: 0x2133c
+  __TEXT.__objc_methlist: 0x2004
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x55c
-  __TEXT.__cstring: 0x5931
-  __TEXT.__oslogstring: 0x2885
-  __TEXT.__unwind_info: 0x7c8
+  __TEXT.__gcc_except_tab: 0x57c
+  __TEXT.__cstring: 0x5bfe
+  __TEXT.__oslogstring: 0x2940
+  __TEXT.__unwind_info: 0x810
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x648
+  __DATA_CONST.__const: 0x690
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1630
+  __DATA_CONST.__objc_selrefs: 0x16f0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x578
-  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__objc_arraydata: 0x5b8
+  __DATA_CONST.__got: 0x3c8
   __AUTH_CONST.__const: 0x920
-  __AUTH_CONST.__cfstring: 0x3400
-  __AUTH_CONST.__objc_const: 0x2f88
-  __AUTH_CONST.__objc_intobj: 0x198
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__cfstring: 0x3560
+  __AUTH_CONST.__objc_const: 0x30d8
+  __AUTH_CONST.__objc_intobj: 0x1c8
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x250
-  __DATA.__data: 0x4a8
+  __DATA.__objc_ivar: 0x26c
   __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0x730
+  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__data: 0x4a8
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/Versions/A/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 741
-  Symbols:   2081
-  CStrings:  619
+  Functions: 769
+  Symbols:   2151
+  CStrings:  633
 
Symbols:
+ -[PAMediaConversionServiceContentProvenanceValidationResult certificateChainDERData]
+ -[PAMediaConversionServiceContentProvenanceValidationResult setCertificateChainDERData:]
+ -[PHMediaFormatConversionCompositeRequest requiresStarRatingMetadataChange]
+ -[PHMediaFormatConversionCompositeRequest requiresTitleMetadataChange]
+ -[PHMediaFormatConversionImplementation_MediaConversionService _submitProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:]
+ -[PHMediaFormatConversionRequest _provenanceRenderOutputType]
+ -[PHMediaFormatConversionRequest provenanceRenderSourceURL]
+ -[PHMediaFormatConversionRequest requiresStarRatingMetadataChange]
+ -[PHMediaFormatConversionRequest requiresTitleMetadataChange]
+ -[PHMediaFormatConversionRequest setProvenanceMetadataBehavior:withUnprocessedSourceRenderURL:processedOriginalDestinationURL:sidecarURL:]
+ -[PHMediaFormatConversionRequest setStarRatingMetadataBehavior:withStarRating:]
+ -[PHMediaFormatConversionRequest setTitleMetadataBehavior:withTitle:]
+ -[PHMediaFormatConversionRequest starRatingMetadataBehavior]
+ -[PHMediaFormatConversionRequest starRating]
+ -[PHMediaFormatConversionRequest titleMetadataBehavior]
+ -[PHMediaFormatConversionRequest title]
+ -[PHMediaFormatConversionSource checkForStarRatingData]
+ -[PHMediaFormatConversionSource checkForTitleData]
+ -[PHMediaFormatConversionSource markStarRatingMetadataAsCheckedWithStatus:]
+ -[PHMediaFormatConversionSource markTitleMetadataAsCheckedWithStatus:]
+ -[PHMediaFormatConversionSource setStarRatingMetadataStatus:]
+ -[PHMediaFormatConversionSource setTitleMetadataStatus:]
+ -[PHMediaFormatConversionSource sourceStarRatingMetadataStatus]
+ -[PHMediaFormatConversionSource sourceTitleMetadataStatus]
+ -[PHMediaFormatConversionSource starRatingMetadataStatus]
+ -[PHMediaFormatConversionSource titleMetadataStatus]
+ GCC_except_table112
+ GCC_except_table118
+ GCC_except_table161
+ GCC_except_table178
+ GCC_except_table182
+ GCC_except_table186
+ GCC_except_table189
+ GCC_except_table199
+ GCC_except_table207
+ GCC_except_table455
+ GCC_except_table457
+ GCC_except_table459
+ GCC_except_table461
+ GCC_except_table463
+ GCC_except_table465
+ GCC_except_table467
+ GCC_except_table469
+ GCC_except_table471
+ GCC_except_table473
+ GCC_except_table588
+ GCC_except_table598
+ GCC_except_table630
+ GCC_except_table634
+ GCC_except_table722
+ GCC_except_table724
+ GCC_except_table727
+ GCC_except_table729
+ GCC_except_table742
+ OBJC_IVAR_$_PAMediaConversionServiceContentProvenanceValidationResult._certificateChainDERData
+ OBJC_IVAR_$_PHMediaFormatConversionRequest._provenanceRenderSourceURL
+ OBJC_IVAR_$_PHMediaFormatConversionRequest._starRating
+ OBJC_IVAR_$_PHMediaFormatConversionRequest._starRatingMetadataBehavior
+ OBJC_IVAR_$_PHMediaFormatConversionRequest._title
+ OBJC_IVAR_$_PHMediaFormatConversionRequest._titleMetadataBehavior
+ OBJC_IVAR_$_PHMediaFormatConversionSource._starRatingMetadataStatus
+ OBJC_IVAR_$_PHMediaFormatConversionSource._titleMetadataStatus
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetKeywords
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetStarRating
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetTitle
+ _PAMediaConversionErrorIsProvenanceProcessingError
+ _PAMediaConversionIsProvenanceClientUpgradeRequiredError
+ _PAMediaConversionServiceOptionAVMetadataIncludeRatingKey
+ _PAMediaConversionServiceOptionAVMetadataIncludeTitleKey
+ _PAMediaConversionServiceOptionAVMetadataRatingKey
+ _PAMediaConversionServiceProvenanceCertificateChainDataKey
+ _PAMediaConversionServiceProvenanceRetryableKey
+ _PAProvenanceCloudAppErrorIsTransient
+ _PFErrorOrUnderlyingErrorMatchesCodesByDomain
+ ___157-[PHMediaFormatConversionImplementation_MediaConversionService _submitProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:]_block_invoke
+ ___70-[PHMediaFormatConversionCompositeRequest requiresTitleMetadataChange]_block_invoke
+ ___75-[PHMediaFormatConversionCompositeRequest requiresStarRatingMetadataChange]_block_invoke
+ _objc_msgSend$_provenanceRenderOutputType
+ _objc_msgSend$_submitProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:
+ _objc_msgSend$checkForKeywordsData
+ _objc_msgSend$checkForStarRatingData
+ _objc_msgSend$checkForTitleData
+ _objc_msgSend$markStarRatingMetadataAsCheckedWithStatus:
+ _objc_msgSend$markTitleMetadataAsCheckedWithStatus:
+ _objc_msgSend$outputFileType
+ _objc_msgSend$policyWithKeywords:
+ _objc_msgSend$policyWithStarRating:
+ _objc_msgSend$policyWithTitle:
+ _objc_msgSend$provenanceRenderSourceURL
+ _objc_msgSend$requiresStarRatingMetadataChange
+ _objc_msgSend$requiresTitleMetadataChange
+ _objc_msgSend$setCertificateChainDERData:
+ _objc_msgSend$setProvenanceMetadataBehavior:withUnprocessedSourceRenderURL:processedOriginalDestinationURL:sidecarURL:
+ _objc_msgSend$setStarRatingMetadataBehavior:withStarRating:
+ _objc_msgSend$setTitleMetadataBehavior:withTitle:
+ _objc_msgSend$sourceKeywordsMetadataStatus
+ _objc_msgSend$sourceStarRatingMetadataStatus
+ _objc_msgSend$sourceTitleMetadataStatus
+ _objc_msgSend$starRating
+ _objc_msgSend$starRatingMetadataBehavior
+ _objc_msgSend$starRatingMetadataStatus
+ _objc_msgSend$title
+ _objc_msgSend$titleMetadataBehavior
+ _objc_msgSend$titleMetadataStatus
- -[PHMediaFormatConversionImplementation_MediaConversionService _submitAdjustedProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:]
- -[PHMediaFormatConversionRequest provenanceAdjustedRenderSourceURL]
- -[PHMediaFormatConversionRequest setProvenanceMetadataBehavior:withUnprocessedSourceAdjustedRenderURL:processedOriginalDestinationURL:sidecarURL:]
- GCC_except_table107
- GCC_except_table113
- GCC_except_table156
- GCC_except_table173
- GCC_except_table177
- GCC_except_table181
- GCC_except_table184
- GCC_except_table194
- GCC_except_table202
- GCC_except_table431
- GCC_except_table433
- GCC_except_table435
- GCC_except_table437
- GCC_except_table439
- GCC_except_table441
- GCC_except_table443
- GCC_except_table445
- GCC_except_table560
- GCC_except_table570
- GCC_except_table602
- GCC_except_table606
- GCC_except_table694
- GCC_except_table696
- GCC_except_table699
- GCC_except_table701
- GCC_except_table714
- OBJC_IVAR_$_PHMediaFormatConversionRequest._provenanceAdjustedRenderSourceURL
- ___165-[PHMediaFormatConversionImplementation_MediaConversionService _submitAdjustedProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:]_block_invoke
- _objc_msgSend$_submitAdjustedProvenanceProcessingRequest:destination:sourceURLCollection:options:completionHandler:
- _objc_msgSend$provenanceAdjustedRenderSourceURL
- _objc_msgSend$setProvenanceMetadataBehavior:withUnprocessedSourceAdjustedRenderURL:processedOriginalDestinationURL:sidecarURL:
CStrings:
+ "#q"
+ "PAMediaConversionServiceErrorCodeProvenanceCloudAppCaptureUnsupported"
+ "PAMediaConversionServiceErrorCodeProvenanceCloudAppClientVersionUnsupported"
+ "PAMediaConversionServiceErrorCodeProvenanceDestinationFormatUnsupported"
+ "PAMediaConversionServiceErrorCodeProvenanceRevocationCheckClientUpgradeRequired"
+ "PAMediaConversionServiceOptionAVMetadataIncludeRatingKey"
+ "PAMediaConversionServiceOptionAVMetadataIncludeTitleKey"
+ "PAMediaConversionServiceOptionAVMetadataRatingKey"
+ "PAMediaConversionServiceProvenanceCertificateChainDataKey"
+ "PAMediaConversionServiceProvenanceRetryableKey"
+ "Read star rating metadata status: %ld from file: %@"
+ "Read title metadata status: %ld from file: %@"
+ "Render path extension (%@) is not a known UTType. Falling back to the conversion source's format."
+ "Requesting single-pass Provenance processing with render. Source: %@, destination: %@."
+ "starRating must not be nil if behavior is PHMediaFormatMetadataBehaviorApply"
+ "title must not be nil if behavior is PHMediaFormatMetadataBehaviorApply"
- "#Q"
- "Requesting single-pass Provenance processing with adjusted render. Source: %@, destination: %@."
```
