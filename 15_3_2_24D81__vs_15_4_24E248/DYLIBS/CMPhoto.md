## CMPhoto

> `/System/Library/PrivateFrameworks/CMPhoto.framework/Versions/A/CMPhoto`

```diff

-356.80.3.0.0
-  __TEXT.__text: 0xf90b8
-  __TEXT.__auth_stubs: 0x3080
+356.100.10.0.0
+  __TEXT.__text: 0xf1164
+  __TEXT.__auth_stubs: 0x30b0
   __TEXT.__objc_methlist: 0x10c
-  __TEXT.__const: 0xc27c
-  __TEXT.__cstring: 0x4e75
-  __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__oslogstring: 0x790
-  __TEXT.__unwind_info: 0x1aa0
+  __TEXT.__const: 0xc31c
+  __TEXT.__cstring: 0x517f
+  __TEXT.__gcc_except_tab: 0x110
+  __TEXT.__oslogstring: 0x875
+  __TEXT.__unwind_info: 0x1be0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x36
-  __TEXT.__objc_methname: 0xc27
+  __TEXT.__objc_methname: 0xd1d
   __TEXT.__objc_methtype: 0x148
-  __TEXT.__objc_stubs: 0xf20
-  __DATA_CONST.__got: 0x1138
-  __DATA_CONST.__const: 0x1cc0
+  __TEXT.__objc_stubs: 0x1020
+  __DATA_CONST.__got: 0x1170
+  __DATA_CONST.__const: 0x1b90
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f0
+  __DATA_CONST.__objc_selrefs: 0x430
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x1858
-  __AUTH_CONST.__const: 0x1af8
-  __AUTH_CONST.__cfstring: 0x5a00
+  __AUTH_CONST.__auth_got: 0x1870
+  __AUTH_CONST.__const: 0x1c08
+  __AUTH_CONST.__cfstring: 0x5e20
   __AUTH_CONST.__objc_const: 0x348
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x6c0
+  __AUTH.__data: 0x810
   __DATA.__objc_ivar: 0x44
-  __DATA.__data: 0x988
-  __DATA.__bss: 0x8e0
+  __DATA.__data: 0x968
+  __DATA.__bss: 0x950
   __DATA.__common: 0x40
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CAAE6290-9557-3618-A86C-D3345D3BF663
-  Functions: 2331
-  Symbols:   2303
-  CStrings:  1768
+  UUID: 67B50275-1F3A-3E1F-9525-3B0B777B0F5B
+  Functions: 3200
+  Symbols:   2350
+  CStrings:  1849
 
Symbols:
+ _CGImageConvertHDRGainMap
+ _CGImageCreatePixelBufferAttributesForHDRTarget
+ _CMPhotoColorTripletCreateDictionaryRepresentation
+ _CMPhotoColorTripletMakeWithDictionaryRepresentation
+ _CMPhotoCreateSDRAndGainMapFromImage
+ _CMPhotoCreateScaleAndRotateOptionsWithHWIfNeeded
+ _CMPhotoDetectCorruptionForSource
+ _CMPhotoEnableInformationCollectionActions
+ _CMPhotoEnableTTR
+ _CMPhotoFindCVPixelBufferHeadroomWithCI
+ _CMPhotoFindImageValueWithCI
+ _CMPhotoGetSlimPixelFormatAndFlavorFromFormatDescription
+ _CMPhotoScaleAndRotateSessionTransformImage
+ _CMPhotoTransferWithCI
+ _FigCFDictionaryCopyArrayOfKeys
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ _kCGColorSpaceDCIP3
+ _kCGFlexRangeBaseIsHDR
+ _kCGFlexRangeOptions
+ _kCGFlexRangeSubsample
+ _kCGFlexRangeUseAlternateColor
+ _kCGImagePropertyHEIFDictionary
+ _kCGTargetColorSpace
+ _kCGTargetPixelFormat
+ _kCGTargetYCCMatrix
+ _kCGToneMappingMode
+ _kCMPhotoCompressionContainerOption_EnableSoftwareHEVCEncoder
+ _kCMPhotoHDRGainMapOption_BufferPool
+ _kCMPhotoHDRGainMapOption_GainMapSubsample
+ _kCMPhotoHDRGainMapOption_Headroom
+ _kCMPhotoHDRGainMapOption_PreferMeteor
+ _kCMPhotoHDRGainMapOption_ToneMapping
+ _kCMPhotoHDRGainMap_Headroom
+ _kCMPhotoHDRGainMap_MeteorMetadata
+ _kCMPhotoHDRGainMap_TmapColorSpace
+ _kCMPhotoHDRGainMap_TmapMetadata
+ _kCMPhotoScaleAndRotateOption_AllowMaxPixelScaleUpscale
+ _kCMPhotoScaleAndRotateOption_DestinationBackedByIOSurface
+ _kCMPhotoScaleAndRotateOption_DestinationChromaLocation
+ _kCMPhotoScaleAndRotateOption_DestinationColorTripletDictionary
+ _kCMPhotoScaleAndRotateOption_DestinationCropRectDictionary
+ _kCMPhotoScaleAndRotateOption_DestinationEvenDimensions
+ _kCMPhotoScaleAndRotateOption_DestinationMaxSideLength
+ _kCMPhotoScaleAndRotateOption_DestinationPixelFormat
+ _kCMPhotoScaleAndRotateOption_DestinationSizeDictionary
+ _kCMPhotoScaleAndRotateOption_DisableGPUForTransfer
+ _kCMPhotoScaleAndRotateOption_DisableMSRForTransfer
+ _kCMPhotoScaleAndRotateOption_ExactDimensions
+ _kCMPhotoScaleAndRotateOption_HighSpeed
+ _kCMPhotoScaleAndRotateOption_RowAlignment
+ _kCMPhotoScaleAndRotateOption_SourceCropRectDictionary
+ _kCMPhotoScaleAndRotateOption_SourceExifOrientation
+ _kCMPhotoScaleAndRotateOption_UseExperimentalMSRAcceleratorForTransfer
+ _kCVImageBufferYCbCrMatrix_SMPTE_240M_1995
+ _vImagePermuteChannels_ARGB8888
- _CGColorSpaceCopyFlexGTCInfo
- _CGImageConvertHDRPixelBufferToSDR
- _CMPhotoScaleAndRotateSessionTransformForMaxSideLengthWithOptions
- _CMPhotoScaleAndRotateSessionTransformForSizeWithHW
- _CMPhotoScaleAndRotateSessionTransformForSizeWithOptions
- ___memmove_chk
- _cmpweak_exists_kCMFormatDescriptionExtension_ContentColorVolume
- _cmpweak_kCMFormatDescriptionExtension_ContentColorVolume
- _kCGFlexGTCInfo
CStrings:
+ "<<<< CMPhotoCompressionSession+HEICS >>>> %s: ERROR!!! There was an error (%d) in the compression plugin callback."
+ "<<<< CMPhotoCompressionSession+HEIF >>>> %s: ERROR!!! There was an error (%d) in the compression plugin callback."
+ "Adobe"
+ "AllowMaxPixelScaleUpscale"
+ "AlternateHeadroom"
+ "BaseColorIsWorkingColor"
+ "BaseHeadroom"
+ "BufferPool"
+ "CIAreaAverage"
+ "CIAreaMinimum"
+ "CIMaximumComponent"
+ "ChannelMetadata"
+ "DestinationBackedByIOSurface"
+ "DestinationChromaLocation"
+ "DestinationColorTripletDictionary"
+ "DestinationCropRectDictionary"
+ "DestinationEvenDimensions"
+ "DestinationMaxSideLength"
+ "DestinationPixelFormat"
+ "DestinationSizeDictionary"
+ "ExactDimensions"
+ "GainMapSubsample"
+ "Headroom"
+ "HighSpeed"
+ "MeteorMetadata"
+ "PreferMeteor"
+ "RowAlignment"
+ "SourceCropRectDictionary"
+ "SourceExifOrientation"
+ "TmapColorSpace"
+ "TmapMetadata"
+ "ToneMapping"
+ "_compressionPluginSequenceFrameEncodeCallback"
+ "_compressionPluginTileEncodeCallback"
+ "com.apple.private.cmphoto.decodeallowlist"
+ "http://ns.apple.com/HDRToneMap/1.0/"
+ "imageByApplyingFilter:"
+ "imageByClampingToExtent"
+ "imageByInsertingIntermediate:"
+ "imageWithCVPixelBuffer:"
+ "imageYCC444:matrix:fullRange:precision:colorSpace:"
+ "initWithBitmapData:width:height:bytesPerRow:format:"
+ "kCIFormatRf"
+ "kCIInputExtentKey"
+ "matrix"
+ "primaries"
+ "render:toCVPixelBuffer:"
+ "transferFunction"
+ "workingColorSpace"
- "{HEIF}"

```
