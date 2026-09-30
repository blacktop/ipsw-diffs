## com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0x22c34
+800.14.111.0.0
+  __TEXT.__text: 0x20160
   __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_stubs: 0x6100
-  __TEXT.__objc_methlist: 0x20c4
+  __TEXT.__objc_stubs: 0x5c00
+  __TEXT.__objc_methlist: 0x1bdc
   __TEXT.__dlopen_cstrs: 0xbe
-  __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0xbdc
-  __TEXT.__cstring: 0x2f9a
-  __TEXT.__objc_classname: 0x5a7
-  __TEXT.__objc_methname: 0x7deb
-  __TEXT.__objc_methtype: 0xd67
-  __TEXT.__oslogstring: 0x2d4e
-  __TEXT.__unwind_info: 0x840
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0xbf4
+  __TEXT.__objc_methname: 0x781d
+  __TEXT.__oslogstring: 0x2d37
+  __TEXT.__cstring: 0x2f2a
+  __TEXT.__objc_classname: 0x365
+  __TEXT.__objc_methtype: 0xcf5
+  __TEXT.__unwind_info: 0x740
   __DATA_CONST.__auth_got: 0x548
-  __DATA_CONST.__got: 0x878
-  __DATA_CONST.__const: 0xad0
-  __DATA_CONST.__cfstring: 0x2460
-  __DATA_CONST.__objc_classlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__got: 0x758
+  __DATA_CONST.__const: 0xa48
+  __DATA_CONST.__cfstring: 0x2320
+  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x3130
-  __DATA.__objc_selrefs: 0x1ce8
-  __DATA.__objc_ivar: 0x238
-  __DATA.__objc_data: 0x910
-  __DATA.__data: 0x360
-  __DATA.__bss: 0x88
+  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA.__objc_const: 0x28c8
+  __DATA.__objc_selrefs: 0x1b60
+  __DATA.__objc_ivar: 0x210
+  __DATA.__objc_data: 0x5f0
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x58
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore
   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation
   - /System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 694F8928-CDCF-3193-B3CB-DC9DD56460E9
-  Functions: 704
-  Symbols:   448
-  CStrings:  2184
+  UUID: 52AC5976-8DE7-39EE-9992-F4EFF99F2B74
+  Functions: 616
+  Symbols:   411
+  CStrings:  2073
 
Symbols:
+ _OBJC_CLASS_$_PFImageIOOptionsBuilder
+ _OBJC_CLASS_$_PFImageMetadataChangePolicy
+ _OBJC_CLASS_$_PFImageMetadataChangePolicyDefault
- _AVAppleMakerNote_MeteorHeadroom
- _AVAppleMakerNote_MeteorPlusGainMap
- _OBJC_CLASS_$_NSConstantFloatNumber
- _OBJC_CLASS_$_PFImageMetadataBuilder
- _OBJC_CLASS_$_PFSharingUtilities
- _kCGImageDestinationCreateHDRGainMap
- _kCGImageDestinationImageMaxPixelSize
- _kCGImageDestinationLossyCompressionQuality
- _kCGImageDestinationOptimizeColorForSharing
- _kCGImagePropertyExifAuxDictionary
- _kCGImagePropertyExifDateTimeDigitized
- _kCGImagePropertyExifDateTimeOriginal
- _kCGImagePropertyExifDictionary
- _kCGImagePropertyExifOffsetTime
- _kCGImagePropertyExifOffsetTimeDigitized
- _kCGImagePropertyExifOffsetTimeOriginal
- _kCGImagePropertyExifSubsecTime
- _kCGImagePropertyExifSubsecTimeDigitized
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
- _kCGImagePropertyTIFFOrientation
- _kCGImageSourceCreateThumbnailWithTransform
- _kCGImageSourceDecodeRequest
- _kCGImageSourceDecodeToSDR
- _kCGImageSourceRasterizationDPI
CStrings:
+ "@\"PFImageMetadataChangePolicy\""
+ "B32@0:8@16@?24"
+ "Invalid request identifier format"
+ "T@\"PFImageMetadataChangePolicy\",&,V_metadataPolicy"
+ "Unable to perform passthrough conversion for %@: %d"
+ "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
+ "setApplyTransform:"
+ "setColorBehavior:"
+ "setIncludeHDRGainMaps:"
+ "setMaximumLongSideLength:"
+ "typeRequiresRasterization:"
+ "validateRequestIdentifier:replyHandler:"
- "@"
- "@\"CLLocation\""
- "@\"NSArray\""
- "@\"NSTimeZone\""
- "@\"PAMediaConversionServiceImageMetadataPolicy\""
- "@20@0:8f16"
- "@24@0:8@\"NSCoder\"16"
- "NSCoding"
- "NSSecureCoding"
- "PAMediaConversionServiceAddPFMetadataPolicy"
- "PAMediaConversionServiceCompositeImageMetadataPolicy"
- "PAMediaConversionServiceDefaultImageMetadataPolicy"
- "PAMediaConversionServiceImageMetadataPolicy"
- "PAMediaConversionServiceImageMetadataPolicy.m"
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
- "T@\"PAMediaConversionServiceImageMetadataPolicy\",&,V_metadataPolicy"
- "T@,&,V_value"
- "Tf,V_lossyCompressionQuality"
- "Tq,V_rasterizationDPI"
- "Unable to add metadata: %@"
- "Unable to perform passthrough conversion for %@"
- "_accessibilityDescription"
- "_caption"
- "_creationDate"
- "_filterImageProperties:metadataWithKey:preserveProperties:"
- "_key"
- "_location"
- "_lossyCompressionQuality"
- "_policies"
- "_rasterizationDPI"
- "_timeZone"
- "_value"
- "accessibilityDescription"
- "addMakerApplePropertyWithKey:value:toProperties:"
- "arrayWithObjects:"
- "caption"
- "containsValueForKey:"
- "creationDate"
- "creationDateTimeZone"
- "decodeFloatForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultRasterizationDPI"
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
- "livePhotoPairingIdentifier"
- "livePhotoPairingIdentifierMetadataKey"
- "location"
- "lossyCompressionQuality"
- "mediaMetadataType"
- "mediaMetadataValue"
- "metadataNeedsProcessing:"
- "numberWithFloat:"
- "policies"
- "policyList"
- "policyWithAccessibilityDescription:"
- "policyWithAllowLocation:"
- "policyWithCaption:"
- "policyWithCreationDate:inTimeZone:"
- "policyWithKey:value:"
- "policyWithLocation:"
- "policyWithLossyCompressionQuality:"
- "policyWithPolicies:"
- "rasterizationDPI"
- "sRGB"
- "setAccessibilityDescription:"
- "setCaption:"
- "setCreationDate:"
- "setCreationDate:timeZone:"
- "setLocation:"
- "setLossyCompressionQuality:"
- "setPolicies:"
- "setRasterizationDPI:"
- "supportsSecureCoding"
- "tiffDictionary"
- "timeZone"
- "typeRequiresRasterizationDPI:"
- "v20@0:8f16"
- "v24@0:8@\"NSCoder\"16"

```
