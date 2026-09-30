## PhotosFormats

> `/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats`

```diff

-912.0.234.0.0
-  __TEXT.__text: 0xd706c
-  __TEXT.__objc_methlist: 0xc8e8
-  __TEXT.__const: 0x2db0
+912.0.235.0.0
+  __TEXT.__text: 0xde05c
+  __TEXT.__objc_methlist: 0xcfc0
+  __TEXT.__const: 0x33a0
   __TEXT.__dlopen_cstrs: 0x1b7
-  __TEXT.__gcc_except_tab: 0x2d8c
-  __TEXT.__cstring: 0xdc55
-  __TEXT.__oslogstring: 0x762c
+  __TEXT.__cstring: 0xe147
+  __TEXT.__constg_swiftt: 0xa0
+  __TEXT.__swift5_typeref: 0xeb
+  __TEXT.__swift5_reflstr: 0x162
+  __TEXT.__swift5_fieldmd: 0xf4
+  __TEXT.__swift5_proto: 0x2c
+  __TEXT.__swift5_types: 0x10
+  __TEXT.__gcc_except_tab: 0x2da4
+  __TEXT.__oslogstring: 0x7954
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x3350
+  __TEXT.__unwind_info: 0x3580
+  __TEXT.__eh_frame: 0x380
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2ae8
-  __DATA_CONST.__objc_classlist: 0x550
+  __DATA_CONST.__const: 0x2b18
+  __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x6248
+  __DATA_CONST.__objc_selrefs: 0x64f0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x390
+  __DATA_CONST.__objc_superrefs: 0x3c0
   __DATA_CONST.__objc_arraydata: 0x800
-  __DATA_CONST.__got: 0x1608
-  __AUTH_CONST.__const: 0x1c10
-  __AUTH_CONST.__cfstring: 0xc920
-  __AUTH_CONST.__objc_const: 0x14628
+  __DATA_CONST.__got: 0x17a0
+  __AUTH_CONST.__const: 0x1da8
+  __AUTH_CONST.__cfstring: 0xcc80
+  __AUTH_CONST.__objc_const: 0x15380
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x208
-  __AUTH_CONST.__auth_got: 0xe98
-  __AUTH.__objc_data: 0x500
-  __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0xd10
-  __DATA.__data: 0xdd8
+  __AUTH_CONST.__auth_got: 0x10e8
+  __AUTH.__objc_data: 0x7a0
+  __AUTH.__data: 0xd0
+  __DATA.__objc_ivar: 0xd8c
+  __DATA.__data: 0xe58
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3020
   __DATA_DIRTY.__bss: 0x858

   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation
   - /System/Library/PrivateFrameworks/Portrait.framework/Portrait
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SwiftASN1Internal.framework/SwiftASN1Internal
   - /usr/lib/libAppleArchive.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4826
-  Symbols:   11622
-  CStrings:  2562
+  Functions: 5090
+  Symbols:   12022
+  CStrings:  2616
 
Symbols:
+ +[PFContentProvenanceDNGHelper dngFileContainsEmbeddedProvenanceImage:checkUnprocessed:]
+ +[PFContentProvenanceResourceInfo dataContainsNonZeroBytes:]
+ +[PFContentProvenanceResourceInfo reconciledProvenanceState:forMetadata:hasUnprocessedEmbeddedProvenanceContent:assetContainsProvenanceResource:utiConformsToDNGType:]
+ +[PFImageMetadataChangePolicySetProvenanceFlags supportsSecureCoding]
+ +[PFMetadataIdentifier quickTimeMetadataCoreMediaCaptureMode]
+ -[PFAssetBundle initWithOriginalPhotoURL:alternatePhotoURL:fullSizePhotoURL:adjustmentBaseFullSizePhotoURL:spatialOvercapturePhotoURL:originalPairedVideoURL:fullSizePairedVideoURL:adjustmentBaseFullSizePairedVideoURL:spatialOvercapturePairedVideoURL:fullSizeVideoURL:adjustmentsURL:originalAdjustmentsURL:adjustmentsSecondaryDataURL:originalProvenanceURL:mediaSubtypes:playbackStyle:playbackVariation:videoComplementVisibilityState:]
+ -[PFAssetBundle originalProvenanceURL]
+ -[PFContentProvenanceDNGHelper .cxx_destruct]
+ -[PFContentProvenanceDNGHelper containsNonZeroUpperBoundTimestampData]
+ -[PFContentProvenanceDNGHelper initWithDNGFileURL:error:]
+ -[PFContentProvenanceDNGHelper nonceDataForModification]
+ -[PFContentProvenanceDNGHelper nonceReservedLength]
+ -[PFContentProvenanceDNGHelper sensorSignature]
+ -[PFContentProvenanceDNGHelper sepSignature]
+ -[PFContentProvenanceDNGHelper setNonceDataForModification:]
+ -[PFContentProvenanceDNGHelper setUpperBoundTimestampDataForModification:]
+ -[PFContentProvenanceDNGHelper upperBoundTimestampDataForModification]
+ -[PFContentProvenanceDNGHelper upperBoundTimestampReservedLength]
+ -[PFContentProvenanceDNGHelper writeModificationsToURL:error:]
+ -[PFContentProvenanceEmbeddedImageWriter .cxx_destruct]
+ -[PFContentProvenanceEmbeddedImageWriter _provenanceStateForMode]
+ -[PFContentProvenanceEmbeddedImageWriter _writeCombinedProvenanceImageToURL:error:]
+ -[PFContentProvenanceEmbeddedImageWriter initWithMode:regularImageURL:payloadToEmbed:]
+ -[PFContentProvenanceEmbeddedImageWriter validateConfiguration]
+ -[PFContentProvenanceEmbeddedImageWriter writeCombinedImageToURL:error:]
+ -[PFContentProvenanceProcessedImageInfo .cxx_destruct]
+ -[PFContentProvenanceProcessedImageInfo certificateVerificationStatus]
+ -[PFContentProvenanceProcessedImageInfo fileContentPartialDigest]
+ -[PFContentProvenanceProcessedImageInfo processedImageJPEGData]
+ -[PFContentProvenanceProcessedImageInfo setCertificateVerificationStatus:]
+ -[PFContentProvenanceProcessedImageInfo setFileContentPartialDigest:]
+ -[PFContentProvenanceProcessedImageInfo setProcessedImageJPEGData:]
+ -[PFContentProvenanceProcessedImageInfo setSignatureVerificationStatus:]
+ -[PFContentProvenanceProcessedImageInfo setUtcLowerBoundTimestamp:]
+ -[PFContentProvenanceProcessedImageInfo setUtcProcessingTimestamp:]
+ -[PFContentProvenanceProcessedImageInfo setUtcUpperBoundTimestamp:]
+ -[PFContentProvenanceProcessedImageInfo signatureVerificationStatus]
+ -[PFContentProvenanceProcessedImageInfo utcLowerBoundTimestamp]
+ -[PFContentProvenanceProcessedImageInfo utcProcessingTimestamp]
+ -[PFContentProvenanceProcessedImageInfo utcUpperBoundTimestamp]
+ -[PFContentProvenanceProcessedImageReader .cxx_destruct]
+ -[PFContentProvenanceProcessedImageReader initWithProcessedProvenanceImageURL:]
+ -[PFContentProvenanceProcessedImageReader initWithRegularImageWithProcessedProvenanceImageURL:]
+ -[PFContentProvenanceProcessedImageReader readProcessedImageWithError:]
+ -[PFContentProvenanceResourceInfo .cxx_destruct]
+ -[PFContentProvenanceResourceInfo baaCertificateChainData]
+ -[PFContentProvenanceResourceInfo configureWithMetadata:]
+ -[PFContentProvenanceResourceInfo containsNonZeroUpperBoundTimestampData]
+ -[PFContentProvenanceResourceInfo developmentStatus]
+ -[PFContentProvenanceResourceInfo dngProperties]
+ -[PFContentProvenanceResourceInfo fileType]
+ -[PFContentProvenanceResourceInfo initWithMetadata:]
+ -[PFContentProvenanceResourceInfo lowerBoundTimestampData]
+ -[PFContentProvenanceResourceInfo sealingManifestData]
+ -[PFContentProvenanceResourceInfo secureBootManifestData]
+ -[PFContentProvenanceResourceInfo sensorSignatureData]
+ -[PFContentProvenanceResourceInfo sepSignatureData]
+ -[PFContentProvenanceResourceInfo timestampStatus]
+ -[PFContentProvenanceResourceInfo upperBoundTimestampData]
+ -[PFContentProvenanceUnprocessedEmbeddedImageReader .cxx_destruct]
+ -[PFContentProvenanceUnprocessedEmbeddedImageReader dataForEmbeddedUnprocessedProvenanceImageWithError:]
+ -[PFContentProvenanceUnprocessedEmbeddedImageReader initWithRegularImageWithUnprocessedProvenanceImageURL:]
+ -[PFContentProvenanceUnprocessedEmbeddedImageReader writeEmbeddedUnprocessedProvenanceImageToURL:error:]
+ -[PFImageIODestinationOptionsBuilder setShouldPreserveProvenance:]
+ -[PFImageIODestinationOptionsBuilder shouldPreserveProvenance]
+ -[PFImageMetadataChangePolicySetProvenanceFlags _flagForProvenanceState:]
+ -[PFImageMetadataChangePolicySetProvenanceFlags encodeWithCoder:]
+ -[PFImageMetadataChangePolicySetProvenanceFlags initWithCoder:]
+ -[PFImageMetadataChangePolicySetProvenanceFlags initWithProvenanceState:]
+ -[PFImageMetadataChangePolicySetProvenanceFlags metadataNeedsProcessing:]
+ -[PFImageMetadataChangePolicySetProvenanceFlags processMetadata:]
+ -[PFImageMetadataChangePolicySetProvenanceFlags provenanceState]
+ -[PFImageMetadataChangePolicySetProvenanceFlags setProvenanceState:]
+ -[PFMetadata cinematicRenderingVersion]
+ -[PFMetadata coreMediaCaptureMode]
+ -[PFMetadata hasProcessedProvenanceAuxiliaryMetadata]
+ -[PFMetadata hasProcessedProvenanceDNGMetadata]
+ -[PFMetadata hasProvenanceMetadata]
+ -[PFMetadata hasTextureStyle]
+ -[PFMetadata hasUnprocessedProvenanceAuxiliaryMetadata]
+ -[PFMetadata hasUnprocessedProvenanceDNGMetadata]
+ -[PFMetadata isCinematicCapableVideo]
+ -[PFMetadata isTimelapseAutoAdjust]
+ -[PFMetadata isTimelapseClassic]
+ -[PFMetadata metadataIndicatesDevelopedProvenanceImage]
+ -[PFMetadata metadataIndicatesUndevelopedProvenanceImage]
+ -[PFMetadata provenanceFlags]
+ -[PFMetadata provenanceState]
+ -[PFMetadata textureStyleGrainIntensity]
+ -[PFMetadata textureStyleIntensity]
+ -[PFMetadata textureStyleIsReversible]
+ -[PFMetadata textureStylePreset]
+ -[PFMetadataImage hasProcessedProvenanceAuxiliaryMetadata]
+ -[PFMetadataImage hasProcessedProvenanceDNGMetadata]
+ -[PFMetadataImage hasProvenanceMetadata]
+ -[PFMetadataImage hasTextureStyle]
+ -[PFMetadataImage hasUnprocessedProvenanceAuxiliaryMetadata]
+ -[PFMetadataImage hasUnprocessedProvenanceDNGMetadata]
+ -[PFMetadataImage metadataIndicatesDevelopedProvenanceImage]
+ -[PFMetadataImage metadataIndicatesUndevelopedProvenanceImage]
+ -[PFMetadataImage provenanceFlags]
+ -[PFMetadataImage provenanceState]
+ -[PFMetadataImage textureStyleGrainIntensity]
+ -[PFMetadataImage textureStyleIntensity]
+ -[PFMetadataImage textureStyleIsReversible]
+ -[PFMetadataImage textureStylePreset]
+ -[PFMetadataMovie cinematicRenderingVersion]
+ -[PFMetadataMovie coreMediaCaptureMode]
+ -[PFMetadataMovie isCinematicCapableVideo]
+ -[PFMetadataMovie isTimelapseAutoAdjust]
+ -[PFMetadataMovie isTimelapseClassic]
+ GCC_except_table1142
+ GCC_except_table1520
+ GCC_except_table1527
+ GCC_except_table1530
+ GCC_except_table1565
+ GCC_except_table1579
+ GCC_except_table1685
+ GCC_except_table1738
+ GCC_except_table1759
+ GCC_except_table1761
+ GCC_except_table1837
+ GCC_except_table1841
+ GCC_except_table1852
+ GCC_except_table1893
+ GCC_except_table1919
+ GCC_except_table1930
+ GCC_except_table1956
+ GCC_except_table1964
+ GCC_except_table1967
+ GCC_except_table1982
+ GCC_except_table2007
+ GCC_except_table2012
+ GCC_except_table2017
+ GCC_except_table2028
+ GCC_except_table2131
+ GCC_except_table2162
+ GCC_except_table2169
+ GCC_except_table2172
+ GCC_except_table2178
+ GCC_except_table2182
+ GCC_except_table2196
+ GCC_except_table2260
+ GCC_except_table2269
+ GCC_except_table2289
+ GCC_except_table2357
+ GCC_except_table2360
+ GCC_except_table2367
+ GCC_except_table2471
+ GCC_except_table2487
+ GCC_except_table2583
+ GCC_except_table2584
+ GCC_except_table2591
+ GCC_except_table2593
+ GCC_except_table2594
+ GCC_except_table2596
+ GCC_except_table2599
+ GCC_except_table2643
+ GCC_except_table2666
+ GCC_except_table2668
+ GCC_except_table2796
+ GCC_except_table285
+ GCC_except_table3076
+ GCC_except_table3142
+ GCC_except_table3146
+ GCC_except_table3148
+ GCC_except_table3149
+ GCC_except_table3153
+ GCC_except_table3155
+ GCC_except_table3157
+ GCC_except_table3158
+ GCC_except_table3159
+ GCC_except_table3161
+ GCC_except_table3162
+ GCC_except_table3169
+ GCC_except_table3170
+ GCC_except_table3171
+ GCC_except_table3172
+ GCC_except_table3175
+ GCC_except_table3178
+ GCC_except_table3188
+ GCC_except_table3191
+ GCC_except_table3194
+ GCC_except_table3201
+ GCC_except_table3202
+ GCC_except_table3203
+ GCC_except_table3225
+ GCC_except_table3227
+ GCC_except_table3228
+ GCC_except_table3234
+ GCC_except_table3235
+ GCC_except_table3236
+ GCC_except_table3237
+ GCC_except_table3238
+ GCC_except_table3244
+ GCC_except_table3247
+ GCC_except_table3304
+ GCC_except_table3451
+ GCC_except_table3454
+ GCC_except_table3455
+ GCC_except_table3457
+ GCC_except_table3458
+ GCC_except_table3460
+ GCC_except_table3461
+ GCC_except_table3462
+ GCC_except_table3466
+ GCC_except_table3472
+ GCC_except_table3479
+ GCC_except_table3482
+ GCC_except_table3483
+ GCC_except_table3485
+ GCC_except_table3490
+ GCC_except_table3491
+ GCC_except_table3492
+ GCC_except_table3498
+ GCC_except_table3505
+ GCC_except_table3506
+ GCC_except_table3569
+ GCC_except_table3573
+ GCC_except_table3576
+ GCC_except_table3577
+ GCC_except_table3627
+ GCC_except_table3636
+ GCC_except_table3711
+ GCC_except_table3779
+ GCC_except_table3781
+ GCC_except_table3798
+ GCC_except_table3808
+ GCC_except_table3823
+ GCC_except_table3825
+ GCC_except_table3914
+ GCC_except_table4149
+ GCC_except_table4153
+ GCC_except_table4165
+ GCC_except_table4246
+ GCC_except_table4247
+ GCC_except_table4248
+ GCC_except_table4252
+ GCC_except_table4254
+ GCC_except_table4261
+ GCC_except_table4265
+ GCC_except_table4272
+ GCC_except_table4286
+ GCC_except_table4287
+ GCC_except_table4289
+ GCC_except_table4294
+ GCC_except_table4295
+ GCC_except_table4297
+ GCC_except_table4298
+ GCC_except_table4301
+ GCC_except_table4314
+ GCC_except_table4321
+ GCC_except_table4326
+ GCC_except_table4327
+ GCC_except_table4331
+ GCC_except_table4336
+ GCC_except_table4365
+ GCC_except_table4370
+ GCC_except_table4371
+ GCC_except_table4372
+ GCC_except_table4373
+ GCC_except_table4374
+ GCC_except_table4376
+ GCC_except_table4381
+ GCC_except_table4382
+ GCC_except_table4384
+ GCC_except_table4385
+ GCC_except_table4387
+ GCC_except_table4388
+ GCC_except_table4389
+ GCC_except_table4390
+ GCC_except_table4391
+ GCC_except_table4392
+ GCC_except_table4394
+ GCC_except_table4396
+ GCC_except_table4397
+ GCC_except_table4398
+ GCC_except_table4399
+ GCC_except_table4402
+ GCC_except_table4474
+ GCC_except_table4541
+ GCC_except_table4616
+ GCC_except_table4620
+ GCC_except_table4622
+ GCC_except_table4625
+ GCC_except_table4626
+ GCC_except_table4644
+ GCC_except_table4660
+ GCC_except_table4661
+ GCC_except_table4662
+ GCC_except_table4664
+ GCC_except_table4666
+ GCC_except_table4930
+ GCC_except_table4937
+ GCC_except_table4939
+ GCC_except_table633
+ GCC_except_table649
+ GCC_except_table652
+ GCC_except_table710
+ GCC_except_table717
+ GCC_except_table756
+ GCC_except_table760
+ GCC_except_table770
+ GCC_except_table773
+ GCC_except_table774
+ GCC_except_table785
+ GCC_except_table788
+ GCC_except_table789
+ GCC_except_table790
+ GCC_except_table795
+ GCC_except_table796
+ GCC_except_table801
+ GCC_except_table802
+ GCC_except_table814
+ GCC_except_table815
+ GCC_except_table822
+ GCC_except_table827
+ GCC_except_table828
+ GCC_except_table829
+ GCC_except_table834
+ GCC_except_table839
+ GCC_except_table853
+ GCC_except_table855
+ GCC_except_table856
+ GCC_except_table857
+ _AVAppleMakerNote_ProvenanceFlags
+ _AVAppleMakerNote_TextureStyleKey_Grain
+ _AVAppleMakerNote_TextureStyleKey_Intensity
+ _AVAppleMakerNote_TextureStyleKey_OriginalInsteadOfReversibility
+ _AVAppleMakerNote_TextureStyleKey_Preset
+ _CMPhotoDNGCopyProperties
+ _CMPhotoDNGReplaceTagsInPlace
+ _CMPhotoDecompressionContainerCopyCustomMetadataForIndexWithOptions
+ _CMPhotoDecompressionContainerGetCustomMetadataCountForIndexWithOptions
+ _CMPhotoEncodeLengthPrefixedData
+ _CMPhotoProvenanceInsertProvenanceImage
+ _CMPhotoVerifyProvenanceSignatureAndCertificates
+ _NSOSStatusErrorDomain
+ _OBJC_CLASS_$_PFContentProvenanceDNGHelper
+ _OBJC_CLASS_$_PFContentProvenanceEmbeddedImageWriter
+ _OBJC_CLASS_$_PFContentProvenanceProcessedImageInfo
+ _OBJC_CLASS_$_PFContentProvenanceProcessedImageReader
+ _OBJC_CLASS_$_PFContentProvenanceResourceInfo
+ _OBJC_CLASS_$_PFContentProvenanceUnprocessedEmbeddedImageReader
+ _OBJC_CLASS_$_PFContentProvenanceUpperBoundTimestampDigestBuilder
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetProvenanceFlags
+ _OBJC_CLASS_$_PTGlobalRenderingMetadata
+ _OBJC_CLASS_$_PTGlobalVideoMetadata
+ _OBJC_CLASS_$_PTRenderPipeline
+ _OBJC_IVAR_$_PFAssetBundle._originalProvenanceURL
+ _OBJC_IVAR_$_PFContentProvenanceDNGHelper._dngData
+ _OBJC_IVAR_$_PFContentProvenanceDNGHelper._dngDict
+ _OBJC_IVAR_$_PFContentProvenanceDNGHelper._dngFileURL
+ _OBJC_IVAR_$_PFContentProvenanceDNGHelper._dngProperties
+ _OBJC_IVAR_$_PFContentProvenanceDNGHelper._nonceDataForModification
+ _OBJC_IVAR_$_PFContentProvenanceDNGHelper._upperBoundTimestampDataForModification
+ _OBJC_IVAR_$_PFContentProvenanceEmbeddedImageWriter._mode
+ _OBJC_IVAR_$_PFContentProvenanceEmbeddedImageWriter._outputContentType
+ _OBJC_IVAR_$_PFContentProvenanceEmbeddedImageWriter._payloadToEmbed
+ _OBJC_IVAR_$_PFContentProvenanceEmbeddedImageWriter._regularImageURL
+ _OBJC_IVAR_$_PFContentProvenanceProcessedImageInfo._certificateVerificationStatus
+ _OBJC_IVAR_$_PFContentProvenanceProcessedImageInfo._fileContentPartialDigest
+ _OBJC_IVAR_$_PFContentProvenanceProcessedImageInfo._processedImageJPEGData
+ _OBJC_IVAR_$_PFContentProvenanceProcessedImageInfo._signatureVerificationStatus
+ _OBJC_IVAR_$_PFContentProvenanceProcessedImageInfo._utcLowerBoundTimestamp
+ _OBJC_IVAR_$_PFContentProvenanceProcessedImageInfo._utcProcessingTimestamp
+ _OBJC_IVAR_$_PFContentProvenanceProcessedImageInfo._utcUpperBoundTimestamp
+ _OBJC_IVAR_$_PFContentProvenanceProcessedImageReader._processedProvenanceImageURL
+ _OBJC_IVAR_$_PFContentProvenanceProcessedImageReader._regularImageWithProcessedProvenanceImageURL
+ _OBJC_IVAR_$_PFContentProvenanceResourceInfo._contentType
+ _OBJC_IVAR_$_PFContentProvenanceResourceInfo._developmentStatus
+ _OBJC_IVAR_$_PFContentProvenanceResourceInfo._dngProperties
+ _OBJC_IVAR_$_PFContentProvenanceResourceInfo._fileType
+ _OBJC_IVAR_$_PFContentProvenanceResourceInfo._fileURLFromMetadata
+ _OBJC_IVAR_$_PFContentProvenanceResourceInfo._timestampStatus
+ _OBJC_IVAR_$_PFContentProvenanceUnprocessedEmbeddedImageReader._regularImageWithUnprocessedProvenanceImageURL
+ _OBJC_IVAR_$_PFImageIODestinationOptionsBuilder._shouldPreserveProvenance
+ _OBJC_IVAR_$_PFImageMetadataChangePolicySetProvenanceFlags._provenanceState
+ _OBJC_IVAR_$_PFMetadataImage._hasProcessedProvenanceDNGMetadataValue
+ _OBJC_IVAR_$_PFMetadataImage._hasUnprocessedProvenanceDNGMetadataValue
+ _OBJC_METACLASS_$_PFContentProvenanceDNGHelper
+ _OBJC_METACLASS_$_PFContentProvenanceEmbeddedImageWriter
+ _OBJC_METACLASS_$_PFContentProvenanceProcessedImageInfo
+ _OBJC_METACLASS_$_PFContentProvenanceProcessedImageReader
+ _OBJC_METACLASS_$_PFContentProvenanceResourceInfo
+ _OBJC_METACLASS_$_PFContentProvenanceUnprocessedEmbeddedImageReader
+ _OBJC_METACLASS_$_PFContentProvenanceUpperBoundTimestampDigestBuilder
+ _OBJC_METACLASS_$_PFImageMetadataChangePolicySetProvenanceFlags
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _PFAssetBundlePathOriginalProvenanceKey
+ _PFReadEmbeddedImageDataFromImageURLForCustomMetadataURI
+ _UTTypeHEIF
+ __DATA_PFContentProvenanceUpperBoundTimestampDigestBuilder
+ __INSTANCE_METHODS_PFContentProvenanceUpperBoundTimestampDigestBuilder
+ __IVARS_PFContentProvenanceUpperBoundTimestampDigestBuilder
+ __METACLASS_DATA_PFContentProvenanceUpperBoundTimestampDigestBuilder
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_PFContentProvenanceDNGHelper
+ __OBJC_$_CLASS_METHODS_PFContentProvenanceResourceInfo
+ __OBJC_$_CLASS_METHODS_PFImageMetadataChangePolicySetProvenanceFlags
+ __OBJC_$_INSTANCE_METHODS_PFContentProvenanceDNGHelper
+ __OBJC_$_INSTANCE_METHODS_PFContentProvenanceEmbeddedImageWriter
+ __OBJC_$_INSTANCE_METHODS_PFContentProvenanceProcessedImageInfo
+ __OBJC_$_INSTANCE_METHODS_PFContentProvenanceProcessedImageReader
+ __OBJC_$_INSTANCE_METHODS_PFContentProvenanceResourceInfo
+ __OBJC_$_INSTANCE_METHODS_PFContentProvenanceUnprocessedEmbeddedImageReader
+ __OBJC_$_INSTANCE_METHODS_PFImageMetadataChangePolicySetProvenanceFlags
+ __OBJC_$_INSTANCE_VARIABLES_PFContentProvenanceDNGHelper
+ __OBJC_$_INSTANCE_VARIABLES_PFContentProvenanceEmbeddedImageWriter
+ __OBJC_$_INSTANCE_VARIABLES_PFContentProvenanceProcessedImageInfo
+ __OBJC_$_INSTANCE_VARIABLES_PFContentProvenanceProcessedImageReader
+ __OBJC_$_INSTANCE_VARIABLES_PFContentProvenanceResourceInfo
+ __OBJC_$_INSTANCE_VARIABLES_PFContentProvenanceUnprocessedEmbeddedImageReader
+ __OBJC_$_INSTANCE_VARIABLES_PFImageMetadataChangePolicySetProvenanceFlags
+ __OBJC_$_PROP_LIST_PFContentProvenanceDNGHelper
+ __OBJC_$_PROP_LIST_PFContentProvenanceProcessedImageInfo
+ __OBJC_$_PROP_LIST_PFContentProvenanceResourceInfo
+ __OBJC_$_PROP_LIST_PFImageMetadataChangePolicySetProvenanceFlags
+ __OBJC_CLASS_RO_$_PFContentProvenanceDNGHelper
+ __OBJC_CLASS_RO_$_PFContentProvenanceEmbeddedImageWriter
+ __OBJC_CLASS_RO_$_PFContentProvenanceProcessedImageInfo
+ __OBJC_CLASS_RO_$_PFContentProvenanceProcessedImageReader
+ __OBJC_CLASS_RO_$_PFContentProvenanceResourceInfo
+ __OBJC_CLASS_RO_$_PFContentProvenanceUnprocessedEmbeddedImageReader
+ __OBJC_CLASS_RO_$_PFImageMetadataChangePolicySetProvenanceFlags
+ __OBJC_METACLASS_RO_$_PFContentProvenanceDNGHelper
+ __OBJC_METACLASS_RO_$_PFContentProvenanceEmbeddedImageWriter
+ __OBJC_METACLASS_RO_$_PFContentProvenanceProcessedImageInfo
+ __OBJC_METACLASS_RO_$_PFContentProvenanceProcessedImageReader
+ __OBJC_METACLASS_RO_$_PFContentProvenanceResourceInfo
+ __OBJC_METACLASS_RO_$_PFContentProvenanceUnprocessedEmbeddedImageReader
+ __OBJC_METACLASS_RO_$_PFImageMetadataChangePolicySetProvenanceFlags
+ __PROPERTIES_PFContentProvenanceUpperBoundTimestampDigestBuilder
+ ___39-[PFMetadataMovie coreMediaCaptureMode]_block_invoke
+ ___42-[PFMetadataMovie isCinematicCapableVideo]_block_invoke
+ ___42-[PFMetadataMovie isCinematicCapableVideo]_block_invoke_2
+ ___44-[PFMetadataMovie cinematicRenderingVersion]_block_invoke
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_getEnumTagSinglePayload
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy24_8
+ ___swift_memcpy32_8
+ ___swift_memcpy72_8
+ ___swift_storeEnumTagSinglePayload
+ __readEmbeddedImageDataFromDNGForCustomMetadataURI
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_PhotosFormats
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 13PhotosFormats25UpperBoundTimestampDigest33_DBB759D668E779954A02FCD0FA8D210FLLV17SwiftASN1Internal21DERImplicitlyTaggableAaE12DERParseable
+ _associated conformance 13PhotosFormats25UpperBoundTimestampDigest33_DBB759D668E779954A02FCD0FA8D210FLLV17SwiftASN1Internal21DERImplicitlyTaggableAaE15DERSerializable
+ _associated conformance 13PhotosFormats26UpperBoundTimestampWrapper33_DBB759D668E779954A02FCD0FA8D210FLLV17SwiftASN1Internal21DERImplicitlyTaggableAaE12DERParseable
+ _associated conformance 13PhotosFormats26UpperBoundTimestampWrapper33_DBB759D668E779954A02FCD0FA8D210FLLV17SwiftASN1Internal21DERImplicitlyTaggableAaE15DERSerializable
+ _associated conformance 13PhotosFormats31UpperBoundTimestampNonceWrapper33_DBB759D668E779954A02FCD0FA8D210FLLV17SwiftASN1Internal21DERImplicitlyTaggableAaE12DERParseable
+ _associated conformance 13PhotosFormats31UpperBoundTimestampNonceWrapper33_DBB759D668E779954A02FCD0FA8D210FLLV17SwiftASN1Internal21DERImplicitlyTaggableAaE15DERSerializable
+ _associated conformance 13PhotosFormats37UpperBoundTimestampDigestBuilderErrorO10Foundation13CustomNSErrorAAs0H0
+ _get_enum_tag_for_layout_string 10Foundation4DataV15_RepresentationO
+ _kCGImageDestinationPreserveProvenance
+ _kCGImagePropertyDNGDictionary
+ _kCMPhotoCustomMetadataTypeURN_Provenance_ProcessedImage
+ _kCMPhotoCustomMetadataTypeURN_Provenance_UnprocessedImage
+ _kCMPhotoCustomMetadata_Data
+ _kCMPhotoCustomMetadata_URI
+ _kCMPhotoMetadata_Provenance_TimingInformation_LowerBoundCaptureTime
+ _kCMPhotoMetadata_Provenance_TimingInformation_ProcessingTime
+ _kCMPhotoMetadata_Provenance_TimingInformation_UpperBoundCaptureTime
+ _kCMPhotoProvenanceResult_CertificateSecTrustVerified
+ _kCMPhotoProvenanceResult_FileContentsPartialDigestData
+ _kCMPhotoProvenanceResult_PQSignatureVerified
+ _kCMPhotoProvenanceResult_TimingInformation
+ _kCMPhoto_CGImagePropertyDNGProvenanceBAACertificateChain
+ _kCMPhoto_CGImagePropertyDNGProvenanceLowerTimeBound
+ _kCMPhoto_CGImagePropertyDNGProvenanceNonce
+ _kCMPhoto_CGImagePropertyDNGProvenanceProcessedImage
+ _kCMPhoto_CGImagePropertyDNGProvenanceSEPSignature
+ _kCMPhoto_CGImagePropertyDNGProvenanceSealingManifest
+ _kCMPhoto_CGImagePropertyDNGProvenanceSecureBootManifest
+ _kCMPhoto_CGImagePropertyDNGProvenanceSensorSignature
+ _kCMPhoto_CGImagePropertyDNGProvenanceUnprocessedImage
+ _kCMPhoto_CGImagePropertyDNGProvenanceUpperTimeBound
+ _kDCIMImageWriterProvenanceMetadataPathExtension
+ _kPFVideoPropertyCaptureModeTimelapseAutoAdjust
+ _kPFVideoPropertyCaptureModeTimelapseClassic
+ _kPFVideoPropertyCoreMediaCaptureMode
+ _kSecRandomDefault
+ _malloc_size
+ _objc_allocWithZone
+ _objc_msgSend$_flagForProvenanceState:
+ _objc_msgSend$_writeCombinedProvenanceImageToURL:error:
+ _objc_msgSend$certificateVerificationStatus
+ _objc_msgSend$cinematicRenderingVersion
+ _objc_msgSend$configureWithMetadata:
+ _objc_msgSend$containsNonZeroUpperBoundTimestampData
+ _objc_msgSend$coreMediaCaptureMode
+ _objc_msgSend$dataContainsNonZeroBytes:
+ _objc_msgSend$dataForEmbeddedUnprocessedProvenanceImageWithError:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$deserializeMetadataWithType:fromGlobalMetadata:error:
+ _objc_msgSend$dngFileContainsEmbeddedProvenanceImage:checkUnprocessed:
+ _objc_msgSend$dngProperties
+ _objc_msgSend$fileContentPartialDigest
+ _objc_msgSend$hasProcessedProvenanceAuxiliaryMetadata
+ _objc_msgSend$hasProcessedProvenanceDNGMetadata
+ _objc_msgSend$hasUnprocessedProvenanceAuxiliaryMetadata
+ _objc_msgSend$hasUnprocessedProvenanceDNGMetadata
+ _objc_msgSend$initWithSensorSignature:sepSignature:error:
+ _objc_msgSend$isRenderVersionSupported:
+ _objc_msgSend$metadataIndicatesDevelopedProvenanceImage
+ _objc_msgSend$metadataIndicatesUndevelopedProvenanceImage
+ _objc_msgSend$nonceReservedLength
+ _objc_msgSend$provenanceFlags
+ _objc_msgSend$quickTimeMetadataCoreMediaCaptureMode
+ _objc_msgSend$reconciledProvenanceState:forMetadata:hasUnprocessedEmbeddedProvenanceContent:assetContainsProvenanceResource:utiConformsToDNGType:
+ _objc_msgSend$renderingVersion
+ _objc_msgSend$setCertificateVerificationStatus:
+ _objc_msgSend$setFileContentPartialDigest:
+ _objc_msgSend$setProcessedImageJPEGData:
+ _objc_msgSend$setSignatureVerificationStatus:
+ _objc_msgSend$setUtcLowerBoundTimestamp:
+ _objc_msgSend$setUtcProcessingTimestamp:
+ _objc_msgSend$setUtcUpperBoundTimestamp:
+ _objc_msgSend$signatureVerificationStatus
+ _objc_msgSend$upperBoundTimestampData
+ _objc_msgSend$upperBoundTimestampReservedLength
+ _objc_msgSend$utcLowerBoundTimestamp
+ _objc_msgSend$utcProcessingTimestamp
+ _objc_msgSend$utcUpperBoundTimestamp
+ _objc_msgSend$validateConfiguration
+ _swift_allocBox
+ _swift_allocError
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_deallocPartialClassInstance
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getEnumCaseMultiPayload
+ _swift_getErrorValue
+ _swift_getExistentialTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getSingletonMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_retain
+ _swift_storeEnumTagMultiPayload
+ _swift_willThrow
+ _symbolic SS
+ _symbolic Si
+ _symbolic Si8expected_Si6actualt
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 13PhotosFormats25UpperBoundTimestampDigest33_DBB759D668E779954A02FCD0FA8D210FLLV
+ _symbolic _____ 13PhotosFormats26UpperBoundTimestampWrapper33_DBB759D668E779954A02FCD0FA8D210FLLV
+ _symbolic _____ 13PhotosFormats31UpperBoundTimestampNonceWrapper33_DBB759D668E779954A02FCD0FA8D210FLLV
+ _symbolic _____ 13PhotosFormats37UpperBoundTimestampDigestBuilderErrorO
+ _symbolic _____6status_t s5Int32V
+ _symbolic ____________pSg10underlyingt 10Foundation3URLV s5ErrorP
+ _symbolic ______p10underlying_t s5ErrorP
+ _symbolic ______pSg s5ErrorP
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s17_NativeDictionaryV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _type_layout_string 13PhotosFormats25UpperBoundTimestampDigest33_DBB759D668E779954A02FCD0FA8D210FLLV
+ _type_layout_string 13PhotosFormats26UpperBoundTimestampWrapper33_DBB759D668E779954A02FCD0FA8D210FLLV
+ _type_layout_string 13PhotosFormats31UpperBoundTimestampNonceWrapper33_DBB759D668E779954A02FCD0FA8D210FLLV
- -[PFAssetBundle initWithOriginalPhotoURL:alternatePhotoURL:fullSizePhotoURL:adjustmentBaseFullSizePhotoURL:spatialOvercapturePhotoURL:originalPairedVideoURL:fullSizePairedVideoURL:adjustmentBaseFullSizePairedVideoURL:spatialOvercapturePairedVideoURL:fullSizeVideoURL:adjustmentsURL:originalAdjustmentsURL:adjustmentsSecondaryDataURL:mediaSubtypes:playbackStyle:playbackVariation:videoComplementVisibilityState:]
- GCC_except_table1133
- GCC_except_table1492
- GCC_except_table1499
- GCC_except_table1502
- GCC_except_table1537
- GCC_except_table1551
- GCC_except_table1657
- GCC_except_table1710
- GCC_except_table1731
- GCC_except_table1733
- GCC_except_table1809
- GCC_except_table1813
- GCC_except_table1824
- GCC_except_table1863
- GCC_except_table1865
- GCC_except_table1902
- GCC_except_table1928
- GCC_except_table1936
- GCC_except_table1939
- GCC_except_table1954
- GCC_except_table1975
- GCC_except_table1980
- GCC_except_table1991
- GCC_except_table2094
- GCC_except_table2125
- GCC_except_table2132
- GCC_except_table2135
- GCC_except_table2141
- GCC_except_table2145
- GCC_except_table2159
- GCC_except_table2223
- GCC_except_table2232
- GCC_except_table2252
- GCC_except_table2320
- GCC_except_table2323
- GCC_except_table2330
- GCC_except_table2434
- GCC_except_table2450
- GCC_except_table2546
- GCC_except_table2547
- GCC_except_table2554
- GCC_except_table2556
- GCC_except_table2557
- GCC_except_table2559
- GCC_except_table2562
- GCC_except_table2606
- GCC_except_table2629
- GCC_except_table2631
- GCC_except_table2746
- GCC_except_table276
- GCC_except_table3025
- GCC_except_table3091
- GCC_except_table3092
- GCC_except_table3095
- GCC_except_table3097
- GCC_except_table3098
- GCC_except_table3102
- GCC_except_table3104
- GCC_except_table3106
- GCC_except_table3107
- GCC_except_table3108
- GCC_except_table3110
- GCC_except_table3111
- GCC_except_table3118
- GCC_except_table3119
- GCC_except_table3120
- GCC_except_table3121
- GCC_except_table3123
- GCC_except_table3124
- GCC_except_table3125
- GCC_except_table3127
- GCC_except_table3135
- GCC_except_table3137
- GCC_except_table3140
- GCC_except_table3150
- GCC_except_table3151
- GCC_except_table3152
- GCC_except_table3177
- GCC_except_table3183
- GCC_except_table3184
- GCC_except_table3185
- GCC_except_table3187
- GCC_except_table3193
- GCC_except_table3196
- GCC_except_table3253
- GCC_except_table3398
- GCC_except_table3400
- GCC_except_table3401
- GCC_except_table3402
- GCC_except_table3404
- GCC_except_table3405
- GCC_except_table3407
- GCC_except_table3408
- GCC_except_table3409
- GCC_except_table3413
- GCC_except_table3419
- GCC_except_table3426
- GCC_except_table3429
- GCC_except_table3430
- GCC_except_table3432
- GCC_except_table3437
- GCC_except_table3438
- GCC_except_table3439
- GCC_except_table3445
- GCC_except_table3452
- GCC_except_table3470
- GCC_except_table3516
- GCC_except_table3520
- GCC_except_table3524
- GCC_except_table3574
- GCC_except_table3583
- GCC_except_table3658
- GCC_except_table3726
- GCC_except_table3728
- GCC_except_table3745
- GCC_except_table3755
- GCC_except_table3770
- GCC_except_table3772
- GCC_except_table3861
- GCC_except_table4096
- GCC_except_table4098
- GCC_except_table4100
- GCC_except_table4107
- GCC_except_table4112
- GCC_except_table4122
- GCC_except_table4132
- GCC_except_table4133
- GCC_except_table4134
- GCC_except_table4138
- GCC_except_table4140
- GCC_except_table4147
- GCC_except_table4148
- GCC_except_table4158
- GCC_except_table4162
- GCC_except_table4163
- GCC_except_table4164
- GCC_except_table4171
- GCC_except_table4172
- GCC_except_table4173
- GCC_except_table4180
- GCC_except_table4181
- GCC_except_table4183
- GCC_except_table4184
- GCC_except_table4187
- GCC_except_table4200
- GCC_except_table4207
- GCC_except_table4212
- GCC_except_table4213
- GCC_except_table4217
- GCC_except_table4222
- GCC_except_table4251
- GCC_except_table4256
- GCC_except_table4257
- GCC_except_table4258
- GCC_except_table4259
- GCC_except_table4260
- GCC_except_table4267
- GCC_except_table4268
- GCC_except_table4270
- GCC_except_table4271
- GCC_except_table4273
- GCC_except_table4275
- GCC_except_table4280
- GCC_except_table4282
- GCC_except_table4283
- GCC_except_table4284
- GCC_except_table4288
- GCC_except_table4359
- GCC_except_table4426
- GCC_except_table4432
- GCC_except_table4501
- GCC_except_table4505
- GCC_except_table4507
- GCC_except_table4510
- GCC_except_table4511
- GCC_except_table4529
- GCC_except_table4545
- GCC_except_table4546
- GCC_except_table4549
- GCC_except_table4551
- GCC_except_table4814
- GCC_except_table4821
- GCC_except_table4823
- GCC_except_table624
- GCC_except_table640
- GCC_except_table643
- GCC_except_table701
- GCC_except_table708
- GCC_except_table747
- GCC_except_table751
- GCC_except_table752
- GCC_except_table764
- GCC_except_table765
- GCC_except_table767
- GCC_except_table768
- GCC_except_table769
- GCC_except_table772
- GCC_except_table779
- GCC_except_table780
- GCC_except_table792
- GCC_except_table793
- GCC_except_table797
- GCC_except_table803
- GCC_except_table804
- GCC_except_table805
- GCC_except_table807
- GCC_except_table809
- GCC_except_table810
- GCC_except_table811
- GCC_except_table844
- GCC_except_table846
- GCC_except_table847
- GCC_except_table848
CStrings:
+ " underlying "
+ ".%@"
+ "ASN.1 encoding failed"
+ "CMPhotoVerifyProvenanceSignatureAndCertificates: certStatus=%d sigStatus=%d hasDigest=%d lowerBound=%{public}@ upperBound=%{public}@ processingTime=%{public}@"
+ "Could not get DNG data from dng file %@ with error: %@"
+ "Decoding not implemented"
+ "Failed to copy DNG regular image to temporary location: %@"
+ "Failed to deserialize cinematic global rendering metadata: %{public}@"
+ "Failed to insert provenance image: %d"
+ "Failed to patch DNG: OSStatus %d"
+ "Failed to read DNG properties for %@: %d"
+ "Failed to read DNG properties via CMPhotoDNGCopyProperties"
+ "Failed to read source file: %@"
+ "Failed to remove partial output file at url: %@ error: %@"
+ "Failed to remove temporary provenance original at url: %@ error: %@"
+ "Failed to write final file: %@"
+ "Failed to write modified DNG to %@"
+ "Fatal error"
+ "Invalid sensor signature length: expected "
+ "Missing sensor signature in DNG file"
+ "No DNG provenance data for URI %@ in %@"
+ "No custom metadata with URI %@ found in %@"
+ "No modifications queued"
+ "No reserved space for nonce in DNG"
+ "No reserved space for upper bound timestamp in DNG"
+ "Output content type %@ is unsupported"
+ "PFAssetBundlePathOriginalProvenanceKey"
+ "PhotosFormats.PFContentProvenanceUpperBoundTimestampDigestBuilder"
+ "PhotosFormats/PFContentProvenance.swift"
+ "Provenance UpperBound Timestamp"
+ "Random generation failed with status: "
+ "SubIFD"
+ "Time-lapse-Auto-adjust"
+ "Time-lapse-Classic"
+ "Unable to create content type for %@"
+ "Unable to create decompression session for %@: %d"
+ "Unable to get content type identifier for %@"
+ "Unable to length-prefix nonce data: %d"
+ "Unable to length-prefix upper bound timestamp data: %d"
+ "Unable to open container for %@: %d"
+ "Unable to read DNG file: "
+ "Unknown provenance embedding mode %td"
+ "cinematicRenderingVersion"
+ "com.apple.coremedia.captureMode"
+ "com.apple.quicktime.cinematic-video"
+ "expected actual "
+ "heic"
+ "init()"
+ "isCinematicCapableVideo"
+ "provenance"
+ "provenanceFlags"
+ "provenanceFlags metadata indicates embedded provenance data when none is present"
+ "temp_regular_%@.%@"
+ "{DNG}"
```
