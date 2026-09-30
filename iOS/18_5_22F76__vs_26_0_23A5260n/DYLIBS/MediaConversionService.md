## MediaConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/MediaConversionService`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0x1dce0
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x202c
-  __TEXT.__const: 0xc8
+800.14.111.0.0
+  __TEXT.__text: 0x1b534
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x1b74
+  __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x6ac
-  __TEXT.__cstring: 0x4aca
-  __TEXT.__oslogstring: 0x22ef
-  __TEXT.__unwind_info: 0x7d8
-  __TEXT.__objc_classname: 0x693
-  __TEXT.__objc_methname: 0x65ce
-  __TEXT.__objc_methtype: 0xa1c
-  __TEXT.__objc_stubs: 0x4600
-  __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0xaa0
-  __DATA_CONST.__objc_classlist: 0x108
-  __DATA_CONST.__objc_protolist: 0x40
+  __TEXT.__cstring: 0x49cd
+  __TEXT.__oslogstring: 0x23af
+  __TEXT.__unwind_info: 0x6e0
+  __TEXT.__objc_classname: 0x452
+  __TEXT.__objc_methname: 0x6194
+  __TEXT.__objc_methtype: 0x9b5
+  __TEXT.__objc_stubs: 0x4140
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__const: 0xa70
+  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1578
+  __DATA_CONST.__objc_selrefs: 0x1430
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__objc_arraydata: 0x4b8
-  __AUTH_CONST.__auth_got: 0x3e8
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x2e80
-  __AUTH_CONST.__objc_const: 0x3190
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_arraydata: 0x4a8
+  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x2d00
+  __AUTH_CONST.__objc_const: 0x2988
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_ivar: 0x20c
-  __DATA.__data: 0x528
-  __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0xa50
+  __DATA.__objc_ivar: 0x1ec
+  __DATA.__data: 0x468
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 047CA615-63F7-3EA0-AB1C-BABFAB1CF784
-  Functions: 694
-  Symbols:   2807
-  CStrings:  2031
+  UUID: 1DD877C1-AF68-3177-9D46-2D3AE2AD0A4A
+  Functions: 610
+  Symbols:   2465
+  CStrings:  1934
 
Symbols:
+ -[PHMediaFormatConversionRequest _isKnownUTTypeForPathExtension:]
+ -[PHMediaFormatConversionRequest forcedOutputPathExtension]
+ -[PHMediaFormatConversionRequest setForcedOutputPathExtension:]
+ GCC_except_table325
+ GCC_except_table327
+ GCC_except_table329
+ GCC_except_table331
+ GCC_except_table333
+ GCC_except_table335
+ GCC_except_table450
+ GCC_except_table458
+ GCC_except_table481
+ GCC_except_table483
+ GCC_except_table570
+ GCC_except_table572
+ GCC_except_table585
+ _OBJC_CLASS_$_PFImageMetadataChangePolicyAddPFMetadata
+ _OBJC_CLASS_$_PFImageMetadataChangePolicyComposite
+ _OBJC_CLASS_$_PFImageMetadataChangePolicyDefault
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetAccessibilityDescription
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetCaption
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetCreationDate
+ _OBJC_CLASS_$_PFImageMetadataChangePolicySetLocation
+ _OBJC_IVAR_$_PHMediaFormatConversionRequest._forcedOutputPathExtension
+ ___51-[PHMediaFormatConversionManager processQueuedJobs]_block_invoke.871
+ ___79-[PHMediaFormatChainedConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke.805
+ ___81-[PHMediaFormatLivePhotoConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke.749
+ ___block_literal_global.397
+ ___block_literal_global.430
+ ___block_literal_global.743
+ _objc_msgSend$_isKnownUTTypeForPathExtension:
+ _objc_msgSend$forcedOutputPathExtension
+ _objc_msgSend$isDynamic
- +[PAMediaConversionServiceAddPFMetadataPolicy policyWithKey:value:]
- +[PAMediaConversionServiceAddPFMetadataPolicy supportsSecureCoding]
- +[PAMediaConversionServiceCompositeImageMetadataPolicy policyWithPolicies:]
- +[PAMediaConversionServiceCompositeImageMetadataPolicy supportsSecureCoding]
- +[PAMediaConversionServiceDefaultImageMetadataPolicy policyWithLossyCompressionQuality:]
- +[PAMediaConversionServiceDefaultImageMetadataPolicy standardPolicy]
- +[PAMediaConversionServiceDefaultImageMetadataPolicy supportsSecureCoding]
- +[PAMediaConversionServiceImageMetadataPolicy standardPolicy]
- +[PAMediaConversionServiceImageMetadataPolicy supportsSecureCoding]
- +[PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy policyWithAccessibilityDescription:]
- +[PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy supportsSecureCoding]
- +[PAMediaConversionServiceSetCaptionImageMetadataPolicy policyWithCaption:]
- +[PAMediaConversionServiceSetCaptionImageMetadataPolicy supportsSecureCoding]
- +[PAMediaConversionServiceSetCreationDateImageMetadataPolicy policyWithCreationDate:inTimeZone:]
- +[PAMediaConversionServiceSetCreationDateImageMetadataPolicy supportsSecureCoding]
- +[PAMediaConversionServiceSetLocationImageMetadataPolicy policyWithLocation:]
- +[PAMediaConversionServiceSetLocationImageMetadataPolicy supportsSecureCoding]
- +[PAMediaConversionServiceSharedPhotoStreamImageMetadataPolicy _filterImageProperties:metadataWithKey:preserveProperties:]
- +[PAMediaConversionServiceSharedPhotoStreamImageMetadataPolicy policyWithAllowLocation:]
- +[PAMediaConversionServiceSharedPhotoStreamImageMetadataPolicy supportsSecureCoding]
- +[PAMediaConversionServiceiCloudPhotoLibraryImageMetadataPolicy standardPolicy]
- -[PAMediaConversionServiceAddPFMetadataPolicy .cxx_destruct]
- -[PAMediaConversionServiceAddPFMetadataPolicy encodeWithCoder:]
- -[PAMediaConversionServiceAddPFMetadataPolicy initWithCoder:]
- -[PAMediaConversionServiceAddPFMetadataPolicy key]
- -[PAMediaConversionServiceAddPFMetadataPolicy metadataNeedsProcessing:]
- -[PAMediaConversionServiceAddPFMetadataPolicy processMetadata:]
- -[PAMediaConversionServiceAddPFMetadataPolicy setKey:]
- -[PAMediaConversionServiceAddPFMetadataPolicy setValue:]
- -[PAMediaConversionServiceAddPFMetadataPolicy value]
- -[PAMediaConversionServiceCompositeImageMetadataPolicy .cxx_destruct]
- -[PAMediaConversionServiceCompositeImageMetadataPolicy encodeWithCoder:]
- -[PAMediaConversionServiceCompositeImageMetadataPolicy initWithCoder:]
- -[PAMediaConversionServiceCompositeImageMetadataPolicy metadataNeedsProcessing:]
- -[PAMediaConversionServiceCompositeImageMetadataPolicy policies]
- -[PAMediaConversionServiceCompositeImageMetadataPolicy processMetadata:]
- -[PAMediaConversionServiceCompositeImageMetadataPolicy setPolicies:]
- -[PAMediaConversionServiceDefaultImageMetadataPolicy encodeWithCoder:]
- -[PAMediaConversionServiceDefaultImageMetadataPolicy initWithCoder:]
- -[PAMediaConversionServiceDefaultImageMetadataPolicy initWithLossyCompressionQuality:]
- -[PAMediaConversionServiceDefaultImageMetadataPolicy init]
- -[PAMediaConversionServiceDefaultImageMetadataPolicy lossyCompressionQuality]
- -[PAMediaConversionServiceDefaultImageMetadataPolicy metadataNeedsProcessing:]
- -[PAMediaConversionServiceDefaultImageMetadataPolicy processMetadata:]
- -[PAMediaConversionServiceDefaultImageMetadataPolicy setLossyCompressionQuality:]
- -[PAMediaConversionServiceImageMetadataPolicy encodeWithCoder:]
- -[PAMediaConversionServiceImageMetadataPolicy initWithCoder:]
- -[PAMediaConversionServiceImageMetadataPolicy metadataNeedsProcessing:]
- -[PAMediaConversionServiceImageMetadataPolicy processMetadata:]
- -[PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy .cxx_destruct]
- -[PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy accessibilityDescription]
- -[PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy encodeWithCoder:]
- -[PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy initWithCoder:]
- -[PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy metadataNeedsProcessing:]
- -[PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy processMetadata:]
- -[PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy setAccessibilityDescription:]
- -[PAMediaConversionServiceSetCaptionImageMetadataPolicy .cxx_destruct]
- -[PAMediaConversionServiceSetCaptionImageMetadataPolicy caption]
- -[PAMediaConversionServiceSetCaptionImageMetadataPolicy encodeWithCoder:]
- -[PAMediaConversionServiceSetCaptionImageMetadataPolicy initWithCoder:]
- -[PAMediaConversionServiceSetCaptionImageMetadataPolicy metadataNeedsProcessing:]
- -[PAMediaConversionServiceSetCaptionImageMetadataPolicy processMetadata:]
- -[PAMediaConversionServiceSetCaptionImageMetadataPolicy setCaption:]
- -[PAMediaConversionServiceSetCreationDateImageMetadataPolicy .cxx_destruct]
- -[PAMediaConversionServiceSetCreationDateImageMetadataPolicy creationDate]
- -[PAMediaConversionServiceSetCreationDateImageMetadataPolicy encodeWithCoder:]
- -[PAMediaConversionServiceSetCreationDateImageMetadataPolicy initWithCoder:]
- -[PAMediaConversionServiceSetCreationDateImageMetadataPolicy metadataNeedsProcessing:]
- -[PAMediaConversionServiceSetCreationDateImageMetadataPolicy processMetadata:]
- -[PAMediaConversionServiceSetCreationDateImageMetadataPolicy setCreationDate:]
- -[PAMediaConversionServiceSetCreationDateImageMetadataPolicy setTimeZone:]
- -[PAMediaConversionServiceSetCreationDateImageMetadataPolicy timeZone]
- -[PAMediaConversionServiceSetLocationImageMetadataPolicy .cxx_destruct]
- -[PAMediaConversionServiceSetLocationImageMetadataPolicy encodeWithCoder:]
- -[PAMediaConversionServiceSetLocationImageMetadataPolicy initWithCoder:]
- -[PAMediaConversionServiceSetLocationImageMetadataPolicy location]
- -[PAMediaConversionServiceSetLocationImageMetadataPolicy metadataNeedsProcessing:]
- -[PAMediaConversionServiceSetLocationImageMetadataPolicy processMetadata:]
- -[PAMediaConversionServiceSetLocationImageMetadataPolicy setLocation:]
- -[PAMediaConversionServiceSharedPhotoStreamImageMetadataPolicy metadataNeedsProcessing:]
- -[PAMediaConversionServiceSharedPhotoStreamImageMetadataPolicy processMetadata:]
- -[PAMediaConversionServiceiCloudPhotoLibraryImageMetadataPolicy processMetadata:]
- GCC_except_table322
- GCC_except_table324
- GCC_except_table326
- GCC_except_table328
- GCC_except_table330
- GCC_except_table332
- GCC_except_table447
- GCC_except_table455
- GCC_except_table649
- GCC_except_table651
- GCC_except_table654
- GCC_except_table656
- GCC_except_table669
- _AVAppleMakerNote_MeteorHeadroom
- _AVAppleMakerNote_MeteorPlusGainMap
- _OBJC_CLASS_$_CLLocation
- _OBJC_CLASS_$_PAMediaConversionServiceAddPFMetadataPolicy
- _OBJC_CLASS_$_PAMediaConversionServiceCompositeImageMetadataPolicy
- _OBJC_CLASS_$_PAMediaConversionServiceDefaultImageMetadataPolicy
- _OBJC_CLASS_$_PAMediaConversionServiceImageMetadataPolicy
- _OBJC_CLASS_$_PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy
- _OBJC_CLASS_$_PAMediaConversionServiceSetCaptionImageMetadataPolicy
- _OBJC_CLASS_$_PAMediaConversionServiceSetCreationDateImageMetadataPolicy
- _OBJC_CLASS_$_PAMediaConversionServiceSetLocationImageMetadataPolicy
- _OBJC_CLASS_$_PAMediaConversionServiceSharedPhotoStreamImageMetadataPolicy
- _OBJC_CLASS_$_PAMediaConversionServiceiCloudPhotoLibraryImageMetadataPolicy
- _OBJC_CLASS_$_PFImageMetadataBuilder
- _OBJC_CLASS_$_PFMetadataUtilities
- _OBJC_CLASS_$_PFSharingUtilities
- _OBJC_IVAR_$_PAMediaConversionServiceAddPFMetadataPolicy._key
- _OBJC_IVAR_$_PAMediaConversionServiceAddPFMetadataPolicy._value
- _OBJC_IVAR_$_PAMediaConversionServiceCompositeImageMetadataPolicy._policies
- _OBJC_IVAR_$_PAMediaConversionServiceDefaultImageMetadataPolicy._lossyCompressionQuality
- _OBJC_IVAR_$_PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy._accessibilityDescription
- _OBJC_IVAR_$_PAMediaConversionServiceSetCaptionImageMetadataPolicy._caption
- _OBJC_IVAR_$_PAMediaConversionServiceSetCreationDateImageMetadataPolicy._creationDate
- _OBJC_IVAR_$_PAMediaConversionServiceSetCreationDateImageMetadataPolicy._timeZone
- _OBJC_IVAR_$_PAMediaConversionServiceSetLocationImageMetadataPolicy._location
- _OBJC_METACLASS_$_PAMediaConversionServiceAddPFMetadataPolicy
- _OBJC_METACLASS_$_PAMediaConversionServiceCompositeImageMetadataPolicy
- _OBJC_METACLASS_$_PAMediaConversionServiceDefaultImageMetadataPolicy
- _OBJC_METACLASS_$_PAMediaConversionServiceImageMetadataPolicy
- _OBJC_METACLASS_$_PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy
- _OBJC_METACLASS_$_PAMediaConversionServiceSetCaptionImageMetadataPolicy
- _OBJC_METACLASS_$_PAMediaConversionServiceSetCreationDateImageMetadataPolicy
- _OBJC_METACLASS_$_PAMediaConversionServiceSetLocationImageMetadataPolicy
- _OBJC_METACLASS_$_PAMediaConversionServiceSharedPhotoStreamImageMetadataPolicy
- _OBJC_METACLASS_$_PAMediaConversionServiceiCloudPhotoLibraryImageMetadataPolicy
- _PAMediaConversionServiceOptionRasterizationDPIKey
- __OBJC_$_CLASS_METHODS_PAMediaConversionServiceAddPFMetadataPolicy
- __OBJC_$_CLASS_METHODS_PAMediaConversionServiceCompositeImageMetadataPolicy
- __OBJC_$_CLASS_METHODS_PAMediaConversionServiceDefaultImageMetadataPolicy
- __OBJC_$_CLASS_METHODS_PAMediaConversionServiceImageMetadataPolicy
- __OBJC_$_CLASS_METHODS_PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy
- __OBJC_$_CLASS_METHODS_PAMediaConversionServiceSetCaptionImageMetadataPolicy
- __OBJC_$_CLASS_METHODS_PAMediaConversionServiceSetCreationDateImageMetadataPolicy
- __OBJC_$_CLASS_METHODS_PAMediaConversionServiceSetLocationImageMetadataPolicy
- __OBJC_$_CLASS_METHODS_PAMediaConversionServiceSharedPhotoStreamImageMetadataPolicy
- __OBJC_$_CLASS_METHODS_PAMediaConversionServiceiCloudPhotoLibraryImageMetadataPolicy
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
- __OBJC_$_CLASS_PROP_LIST_PAMediaConversionServiceImageMetadataPolicy
- __OBJC_$_INSTANCE_METHODS_PAMediaConversionServiceAddPFMetadataPolicy
- __OBJC_$_INSTANCE_METHODS_PAMediaConversionServiceCompositeImageMetadataPolicy
- __OBJC_$_INSTANCE_METHODS_PAMediaConversionServiceDefaultImageMetadataPolicy
- __OBJC_$_INSTANCE_METHODS_PAMediaConversionServiceImageMetadataPolicy
- __OBJC_$_INSTANCE_METHODS_PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy
- __OBJC_$_INSTANCE_METHODS_PAMediaConversionServiceSetCaptionImageMetadataPolicy
- __OBJC_$_INSTANCE_METHODS_PAMediaConversionServiceSetCreationDateImageMetadataPolicy
- __OBJC_$_INSTANCE_METHODS_PAMediaConversionServiceSetLocationImageMetadataPolicy
- __OBJC_$_INSTANCE_METHODS_PAMediaConversionServiceSharedPhotoStreamImageMetadataPolicy
- __OBJC_$_INSTANCE_METHODS_PAMediaConversionServiceiCloudPhotoLibraryImageMetadataPolicy
- __OBJC_$_INSTANCE_VARIABLES_PAMediaConversionServiceAddPFMetadataPolicy
- __OBJC_$_INSTANCE_VARIABLES_PAMediaConversionServiceCompositeImageMetadataPolicy
- __OBJC_$_INSTANCE_VARIABLES_PAMediaConversionServiceDefaultImageMetadataPolicy
- __OBJC_$_INSTANCE_VARIABLES_PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy
- __OBJC_$_INSTANCE_VARIABLES_PAMediaConversionServiceSetCaptionImageMetadataPolicy
- __OBJC_$_INSTANCE_VARIABLES_PAMediaConversionServiceSetCreationDateImageMetadataPolicy
- __OBJC_$_INSTANCE_VARIABLES_PAMediaConversionServiceSetLocationImageMetadataPolicy
- __OBJC_$_PROP_LIST_PAMediaConversionServiceAddPFMetadataPolicy
- __OBJC_$_PROP_LIST_PAMediaConversionServiceCompositeImageMetadataPolicy
- __OBJC_$_PROP_LIST_PAMediaConversionServiceDefaultImageMetadataPolicy
- __OBJC_$_PROP_LIST_PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy
- __OBJC_$_PROP_LIST_PAMediaConversionServiceSetCaptionImageMetadataPolicy
- __OBJC_$_PROP_LIST_PAMediaConversionServiceSetCreationDateImageMetadataPolicy
- __OBJC_$_PROP_LIST_PAMediaConversionServiceSetLocationImageMetadataPolicy
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding
- __OBJC_CLASS_PROTOCOLS_$_PAMediaConversionServiceImageMetadataPolicy
- __OBJC_CLASS_RO_$_PAMediaConversionServiceAddPFMetadataPolicy
- __OBJC_CLASS_RO_$_PAMediaConversionServiceCompositeImageMetadataPolicy
- __OBJC_CLASS_RO_$_PAMediaConversionServiceDefaultImageMetadataPolicy
- __OBJC_CLASS_RO_$_PAMediaConversionServiceImageMetadataPolicy
- __OBJC_CLASS_RO_$_PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy
- __OBJC_CLASS_RO_$_PAMediaConversionServiceSetCaptionImageMetadataPolicy
- __OBJC_CLASS_RO_$_PAMediaConversionServiceSetCreationDateImageMetadataPolicy
- __OBJC_CLASS_RO_$_PAMediaConversionServiceSetLocationImageMetadataPolicy
- __OBJC_CLASS_RO_$_PAMediaConversionServiceSharedPhotoStreamImageMetadataPolicy
- __OBJC_CLASS_RO_$_PAMediaConversionServiceiCloudPhotoLibraryImageMetadataPolicy
- __OBJC_LABEL_PROTOCOL_$_NSCoding
- __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
- __OBJC_METACLASS_RO_$_PAMediaConversionServiceAddPFMetadataPolicy
- __OBJC_METACLASS_RO_$_PAMediaConversionServiceCompositeImageMetadataPolicy
- __OBJC_METACLASS_RO_$_PAMediaConversionServiceDefaultImageMetadataPolicy
- __OBJC_METACLASS_RO_$_PAMediaConversionServiceImageMetadataPolicy
- __OBJC_METACLASS_RO_$_PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy
- __OBJC_METACLASS_RO_$_PAMediaConversionServiceSetCaptionImageMetadataPolicy
- __OBJC_METACLASS_RO_$_PAMediaConversionServiceSetCreationDateImageMetadataPolicy
- __OBJC_METACLASS_RO_$_PAMediaConversionServiceSetLocationImageMetadataPolicy
- __OBJC_METACLASS_RO_$_PAMediaConversionServiceSharedPhotoStreamImageMetadataPolicy
- __OBJC_METACLASS_RO_$_PAMediaConversionServiceiCloudPhotoLibraryImageMetadataPolicy
- __OBJC_PROTOCOL_$_NSCoding
- __OBJC_PROTOCOL_$_NSSecureCoding
- ___51-[PHMediaFormatConversionManager processQueuedJobs]_block_invoke.865
- ___61+[PAMediaConversionServiceImageMetadataPolicy standardPolicy]_block_invoke
- ___68+[PAMediaConversionServiceDefaultImageMetadataPolicy standardPolicy]_block_invoke
- ___78-[PAMediaConversionServiceSetCreationDateImageMetadataPolicy processMetadata:]_block_invoke
- ___79+[PAMediaConversionServiceiCloudPhotoLibraryImageMetadataPolicy standardPolicy]_block_invoke
- ___79-[PHMediaFormatChainedConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke.799
- ___81-[PHMediaFormatLivePhotoConversionRequest enqueueSubrequestsOnConversionManager:]_block_invoke.743
- ___86-[PAMediaConversionServiceSetCreationDateImageMetadataPolicy metadataNeedsProcessing:]_block_invoke
- ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
- ___block_literal_global.400
- ___block_literal_global.427
- ___block_literal_global.432
- ___block_literal_global.52
- ___block_literal_global.824
- ___block_literal_global.88
- _kCGImageDestinationLossyCompressionQuality
- _kCGImagePropertyExifAuxDictionary
- _kCGImagePropertyExifDateTimeDigitized
- _kCGImagePropertyExifDateTimeOriginal
- _kCGImagePropertyExifDictionary
- _kCGImagePropertyExifOffsetTime
- _kCGImagePropertyExifOffsetTimeDigitized
- _kCGImagePropertyExifOffsetTimeOriginal
- _kCGImagePropertyExifSubsecTime
- _kCGImagePropertyExifSubsecTimeDigitized
- _kCGImagePropertyExifSubsecTimeOriginal
- _kCGImagePropertyGPSDictionary
- _kCGImagePropertyIPTCCaptionAbstract
- _kCGImagePropertyIPTCDateCreated
- _kCGImagePropertyIPTCDictionary
- _kCGImagePropertyIPTCExtArtworkContentDescription
- _kCGImagePropertyIPTCImageOrientation
- _kCGImagePropertyIPTCTimeCreated
- _kCGImagePropertyMakerAppleDictionary
- _kCGImagePropertyMakerCanonDictionary
- _kCGImagePropertyMakerFujiDictionary
- _kCGImagePropertyMakerMinoltaDictionary
- _kCGImagePropertyMakerNikonDictionary
- _kCGImagePropertyMakerOlympusDictionary
- _kCGImagePropertyMakerPentaxDictionary
- _kCGImagePropertyTIFFCopyright
- _kCGImagePropertyTIFFDateTime
- _kCGImagePropertyTIFFDictionary
- _kCGImagePropertyTIFFMake
- _kCGImagePropertyTIFFModel
- _kCGImagePropertyTIFFOrientation
- _objc_alloc_init
- _objc_msgSend$_filterImageProperties:metadataWithKey:preserveProperties:
- _objc_msgSend$addEntriesFromDictionary:
- _objc_msgSend$addMakerApplePropertyWithKey:value:toProperties:
- _objc_msgSend$arrayWithObjects:
- _objc_msgSend$containsValueForKey:
- _objc_msgSend$decodeFloatForKey:
- _objc_msgSend$decodeObjectForKey:
- _objc_msgSend$decodeObjectOfClass:forKey:
- _objc_msgSend$defaultTimeZone
- _objc_msgSend$dictionaryWithCapacity:
- _objc_msgSend$dictionaryWithObjectsAndKeys:
- _objc_msgSend$encodeFloat:forKey:
- _objc_msgSend$encodeObject:forKey:
- _objc_msgSend$exifDictionary
- _objc_msgSend$gpsDictionaryForLocation:
- _objc_msgSend$init
- _objc_msgSend$initWithCapacity:
- _objc_msgSend$initWithImageProperties:contentType:timeZoneLookup:
- _objc_msgSend$initWithLossyCompressionQuality:
- _objc_msgSend$iptcDictionary
- _objc_msgSend$isEqualToDictionary:
- _objc_msgSend$key
- _objc_msgSend$lossyCompressionQuality
- _objc_msgSend$metadataNeedsProcessing:
- _objc_msgSend$numberWithFloat:
- _objc_msgSend$objectForKey:
- _objc_msgSend$policies
- _objc_msgSend$setAccessibilityDescription:
- _objc_msgSend$setCaption:
- _objc_msgSend$setCreationDate:
- _objc_msgSend$setCreationDate:timeZone:
- _objc_msgSend$setKey:
- _objc_msgSend$setLocation:
- _objc_msgSend$setLossyCompressionQuality:
- _objc_msgSend$setObject:forKey:
- _objc_msgSend$setPolicies:
- _objc_msgSend$setTimeZone:
- _objc_msgSend$setValue:
- _objc_msgSend$tiffDictionary
- _objc_msgSend$timeZone
- _objc_msgSend$value
- _standardPolicy.onceToken
- _standardPolicy.onceToken.50
- _standardPolicy.onceToken.86
- _standardPolicy.standardPolicy
- _standardPolicy.standardPolicy.49
- _standardPolicy.standardPolicy.85
CStrings:
+ "Forced path extension (%@) is not a known UTType. Falling back to %{public}@ as the output path extension."
+ "Forced path extension (%@) is not a known UTType. Falling back to %{public}@ as the output type identifier."
+ "T@\"NSString\",C,V_forcedOutputPathExtension"
+ "Unable to perform passthrough conversion for %@: %d"
+ "_forcedOutputPathExtension"
+ "_isKnownUTTypeForPathExtension:"
+ "forcedOutputPathExtension"
+ "isDynamic"
+ "setForcedOutputPathExtension:"
- "@20@0:8f16"
- "@24@0:8@\"NSCoder\"16"
- "@32@0:8@16@24"
- "NSCoding"
- "NSSecureCoding"
- "PAMediaConversionServiceAddPFMetadataPolicy"
- "PAMediaConversionServiceCompositeImageMetadataPolicy"
- "PAMediaConversionServiceDefaultImageMetadataPolicy"
- "PAMediaConversionServiceImageMetadataPolicy"
- "PAMediaConversionServiceImageMetadataPolicy.m"
- "PAMediaConversionServiceOptionRasterizationDPIKey"
- "PAMediaConversionServiceSetAccessibilityDescriptionImageMetadataPolicy"
- "PAMediaConversionServiceSetCaptionImageMetadataPolicy"
- "PAMediaConversionServiceSetCreationDateImageMetadataPolicy"
- "PAMediaConversionServiceSetLocationImageMetadataPolicy"
- "PAMediaConversionServiceSharedPhotoStreamImageMetadataPolicy"
- "PAMediaConversionServiceiCloudPhotoLibraryImageMetadataPolicy"
- "T@\"CLLocation\",&,V_location"
- "T@\"NSArray\",&,V_policies"
- "T@\"NSDate\",&,V_creationDate"
- "T@\"NSString\",&,V_key"
- "T@\"NSString\",C,V_accessibilityDescription"
- "T@\"NSString\",C,V_caption"
- "T@\"NSTimeZone\",&,V_timeZone"
- "T@,&,V_value"
- "Tf,V_lossyCompressionQuality"
- "Unable to add metadata: %@"
- "Unable to perform passthrough conversion for %@"
- "_filterImageProperties:metadataWithKey:preserveProperties:"
- "_key"
- "_lossyCompressionQuality"
- "_policies"
- "_timeZone"
- "_value"
- "addEntriesFromDictionary:"
- "addMakerApplePropertyWithKey:value:toProperties:"
- "arrayWithObjects:"
- "containsValueForKey:"
- "decodeFloatForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultTimeZone"
- "dictionaryWithCapacity:"
- "dictionaryWithObjectsAndKeys:"
- "encodeFloat:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "exifDictionary"
- "f"
- "f16@0:8"
- "gpsDictionaryForLocation:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithImageProperties:contentType:timeZoneLookup:"
- "initWithLossyCompressionQuality:"
- "iptcDictionary"
- "isEqualToDictionary:"
- "key"
- "lossyCompressionQuality"
- "mediaMetadataType"
- "mediaMetadataValue"
- "metadataNeedsProcessing:"
- "numberWithFloat:"
- "objectForKey:"
- "policies"
- "policyList"
- "policyWithAllowLocation:"
- "policyWithLossyCompressionQuality:"
- "setAccessibilityDescription:"
- "setCaption:"
- "setCreationDate:"
- "setCreationDate:timeZone:"
- "setKey:"
- "setLocation:"
- "setLossyCompressionQuality:"
- "setObject:forKey:"
- "setPolicies:"
- "setTimeZone:"
- "setValue:"
- "supportsSecureCoding"
- "tiffDictionary"
- "timeZone"
- "v20@0:8f16"
- "v24@0:8@\"NSCoder\"16"
- "v40@0:8@16@24@32"
- "value"
- "\xf1"

```
