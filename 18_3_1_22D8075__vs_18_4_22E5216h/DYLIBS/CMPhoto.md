## CMPhoto

> `/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto`

```diff

-356.80.3.0.0
-  __TEXT.__text: 0xff48c
-  __TEXT.__auth_stubs: 0x3330
+356.100.9.0.1
+  __TEXT.__text: 0xf7324
+  __TEXT.__auth_stubs: 0x3340
   __TEXT.__objc_methlist: 0x3fc
-  __TEXT.__const: 0xc248
-  __TEXT.__cstring: 0x5cfc
-  __TEXT.__oslogstring: 0x790
-  __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__unwind_info: 0x1bc8
+  __TEXT.__const: 0xc2f0
+  __TEXT.__cstring: 0x6074
+  __TEXT.__oslogstring: 0x875
+  __TEXT.__gcc_except_tab: 0x16c
+  __TEXT.__unwind_info: 0x1da0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x54
-  __TEXT.__objc_methname: 0x1ca1
-  __TEXT.__objc_methtype: 0xb53
-  __TEXT.__objc_stubs: 0x1ba0
-  __DATA_CONST.__got: 0x1220
-  __DATA_CONST.__const: 0x26b8
+  __TEXT.__objc_methname: 0x1d97
+  __TEXT.__objc_methtype: 0xb8a
+  __TEXT.__objc_stubs: 0x1ca0
+  __DATA_CONST.__got: 0x1258
+  __DATA_CONST.__const: 0x2600
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x778
+  __DATA_CONST.__objc_selrefs: 0x7b8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x19b0
-  __AUTH_CONST.__auth_ptr: 0x68
-  __AUTH_CONST.__const: 0x1248
-  __AUTH_CONST.__cfstring: 0x5c20
+  __AUTH_CONST.__auth_got: 0x19b8
+  __AUTH_CONST.__auth_ptr: 0x78
+  __AUTH_CONST.__const: 0x12c8
+  __AUTH_CONST.__cfstring: 0x6040
   __AUTH_CONST.__objc_const: 0xcc8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x50
+  __AUTH.__data: 0xf0
   __DATA.__objc_ivar: 0x124
-  __DATA.__data: 0x808
-  __DATA.__bss: 0x4f8
+  __DATA.__data: 0x208
+  __DATA.__bss: 0x548
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x880
-  __DATA_DIRTY.__bss: 0x500
+  __DATA_DIRTY.__data: 0xec0
+  __DATA_DIRTY.__bss: 0x520
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2410
-  Symbols:   4257
-  CStrings:  1326
+  Functions: 3284
+  Symbols:   5755
+  CStrings:  1374
 
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
- _objc_retain_x25
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
+ "^{CMPhotoDecompressionContainer={__CFRuntimeBase=QAQ}^{CMPhotoDecompressionSession}CCCCC^{CMPhotoDecompressionContainerVTable}(?={?=^{__CFAllocator}^{OpaqueFigPictureCollection}^{OpaqueFigFormatReader}{?=@Cqq^{CGImageMetadata}^{__CFDictionary}i}{?=C^{__CFArray}}{?=Cqq}{?=CC}{?=CCC}{?=CC}}{?=^{__CFAllocator}{?=CCq}^{OpaqueFigFormatReader}^{__CFDictionary}^{?}^{__CFArray}^{__CFArray}@C}{?=^{__CFAllocator}{?=i(?=^v^{__CFURL}^{__IOSurface}^{__CFData}^{OpaqueCMBlockBuffer})^{OpaqueCMByteStream}}^{OpaqueFigSimpleMutex}{?={?=C^{__CFArray}}}^{CMPhotoUnifiedJPEGDecoder}{?=C{?=QQ}iCCi^{__CFData}}{?=CC{?={?=QQ}iI^{CGImageMetadata}^{__CFString}^{__CFDictionary}{?=qQ}Ci^{__CFData}^{CGColorSpace}^{__CFDictionary}}qQ^{?}}{?=CC{?=qQ}iC{?=C{?=QQ}i{?=qQ}i}}{?=CC{?=qQ}}{?=CC{?=qQ}^{__CFData}}{?=CC{?=qQ}^{__CFData}}{?=CC^{__CFData}}{?=CC^{__CFData}}}{?=^{__CFAllocator}{?=i(?=^v^{__CFURL}^{__IOSurface}^{__CFData}^{OpaqueCMBlockBuffer})^{OpaqueCMByteStream}^{__CFData}}{?=C{?=iIIIIffifiiiiIIIIi{?=II}{?=IIIi}II[100C]}^{CGColorSpace}^{__CFData}^{__CFString}^{__CFString}^{__CFArray}^{__CFArray}}})QQ{?=Cq}{?=Cq}i{?=^{__CFArray}^q^qqqq}{?=^{__CFDictionary}^{__CFDictionary}^{__CFDictionary}}}"
+ "_compressionPluginSequenceFrameEncodeCallback"
+ "_compressionPluginTileEncodeCallback"
+ "com.apple.private.cmphoto.decodeallowlist"
+ "http://ns.apple.com/HDRToneMap/1.0/"
+ "i40@?0^{CMPhotoDecompressionSession={__CFRuntimeBase=QAQ}{os_unfair_lock_s=I}Q^{__CFSet}@{?=C@@@^{__CFArray}i}{?=C@@@^{__CFArray}i}{?=C@@@^{__CFArray}i}{?=C@@@^{__CFArray}i}{?=Ci{os_unfair_lock_s=I}@^{__CFArray}}^{CMPhotoSurfacePool}^{CMPhotoScaleAndRotateSession}^{CMPhotoCodecSessionPool}^{CMPhotoCodecSessionPool}@?^vQ}8^{CMPhotoDecompressionContainer={__CFRuntimeBase=QAQ}^{CMPhotoDecompressionSession}CCCCC^{CMPhotoDecompressionContainerVTable}(?={?=^{__CFAllocator}^{OpaqueFigPictureCollection}^{OpaqueFigFormatReader}{?=@Cqq^{CGImageMetadata}^{__CFDictionary}i}{?=C^{__CFArray}}{?=Cqq}{?=CC}{?=CCC}{?=CC}}{?=^{__CFAllocator}{?=CCq}^{OpaqueFigFormatReader}^{__CFDictionary}^{?}^{__CFArray}^{__CFArray}@C}{?=^{__CFAllocator}{?=i(?=^v^{__CFURL}^{__IOSurface}^{__CFData}^{OpaqueCMBlockBuffer})^{OpaqueCMByteStream}}^{OpaqueFigSimpleMutex}{?={?=C^{__CFArray}}}^{CMPhotoUnifiedJPEGDecoder}{?=C{?=QQ}iCCi^{__CFData}}{?=CC{?={?=QQ}iI^{CGImageMetadata}^{__CFString}^{__CFDictionary}{?=qQ}Ci^{__CFData}^{CGColorSpace}^{__CFDictionary}}qQ^{?}}{?=CC{?=qQ}iC{?=C{?=QQ}i{?=qQ}i}}{?=CC{?=qQ}}{?=CC{?=qQ}^{__CFData}}{?=CC{?=qQ}^{__CFData}}{?=CC^{__CFData}}{?=CC^{__CFData}}}{?=^{__CFAllocator}{?=i(?=^v^{__CFURL}^{__IOSurface}^{__CFData}^{OpaqueCMBlockBuffer})^{OpaqueCMByteStream}^{__CFData}}{?=C{?=iIIIIffifiiiiIIIIi{?=II}{?=IIIi}II[100C]}^{CGColorSpace}^{__CFData}^{__CFString}^{__CFString}^{__CFArray}^{__CFArray}}})QQ{?=Cq}{?=Cq}i{?=^{__CFArray}^q^qqqq}{?=^{__CFDictionary}^{__CFDictionary}^{__CFDictionary}}}16Q24^v32"
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
+ "v40@?0^{CMPhotoDecompressionContainer={__CFRuntimeBase=QAQ}^{CMPhotoDecompressionSession}CCCCC^{CMPhotoDecompressionContainerVTable}(?={?=^{__CFAllocator}^{OpaqueFigPictureCollection}^{OpaqueFigFormatReader}{?=@Cqq^{CGImageMetadata}^{__CFDictionary}i}{?=C^{__CFArray}}{?=Cqq}{?=CC}{?=CCC}{?=CC}}{?=^{__CFAllocator}{?=CCq}^{OpaqueFigFormatReader}^{__CFDictionary}^{?}^{__CFArray}^{__CFArray}@C}{?=^{__CFAllocator}{?=i(?=^v^{__CFURL}^{__IOSurface}^{__CFData}^{OpaqueCMBlockBuffer})^{OpaqueCMByteStream}}^{OpaqueFigSimpleMutex}{?={?=C^{__CFArray}}}^{CMPhotoUnifiedJPEGDecoder}{?=C{?=QQ}iCCi^{__CFData}}{?=CC{?={?=QQ}iI^{CGImageMetadata}^{__CFString}^{__CFDictionary}{?=qQ}Ci^{__CFData}^{CGColorSpace}^{__CFDictionary}}qQ^{?}}{?=CC{?=qQ}iC{?=C{?=QQ}i{?=qQ}i}}{?=CC{?=qQ}}{?=CC{?=qQ}^{__CFData}}{?=CC{?=qQ}^{__CFData}}{?=CC^{__CFData}}{?=CC^{__CFData}}}{?=^{__CFAllocator}{?=i(?=^v^{__CFURL}^{__IOSurface}^{__CFData}^{OpaqueCMBlockBuffer})^{OpaqueCMByteStream}^{__CFData}}{?=C{?=iIIIIffifiiiiIIIIi{?=II}{?=IIIi}II[100C]}^{CGColorSpace}^{__CFData}^{__CFString}^{__CFString}^{__CFArray}^{__CFArray}}})QQ{?=Cq}{?=Cq}i{?=^{__CFArray}^q^qqqq}{?=^{__CFDictionary}^{__CFDictionary}^{__CFDictionary}}}8Q16i24i28^v32"
+ "workingColorSpace"
- "^{CMPhotoDecompressionContainer={__CFRuntimeBase=QAQ}^{CMPhotoDecompressionSession}CCCCC^{CMPhotoDecompressionContainerVTable}(?={?=^{__CFAllocator}^{OpaqueFigPictureCollection}^{OpaqueFigFormatReader}{?=@Cqq^{CGImageMetadata}^{__CFDictionary}i}{?=C^{__CFArray}}{?=Cqq}{?=CC}{?=CCC}{?=CC}}{?=^{__CFAllocator}{?=CCq}^{OpaqueFigFormatReader}^{__CFDictionary}^{?}^{__CFArray}^{__CFArray}@C}{?=^{__CFAllocator}{?=i(?=^v^{__CFURL}^{__IOSurface}^{__CFData}^{OpaqueCMBlockBuffer})^{OpaqueCMByteStream}}^{OpaqueFigSimpleMutex}{?={?=C^{__CFArray}}}^{CMPhotoUnifiedJPEGDecoder}{?=C{?=QQ}iCCi^{__CFData}}{?=CC{?={?=QQ}iI^{CGImageMetadata}^{__CFString}^{__CFDictionary}{?=qQ}Ci^{__CFData}^{CGColorSpace}^{__CFDictionary}}qQ^{?}}{?=CC{?=qQ}iC{?=C{?=QQ}i{?=qQ}i}}{?=CC{?=qQ}}{?=CC{?=qQ}^{__CFData}}{?=CC{?=qQ}^{__CFData}}{?=CC^{__CFData}}{?=CC^{__CFData}}}{?=^{__CFAllocator}{?=i(?=^v^{__CFURL}^{__IOSurface}^{__CFData}^{OpaqueCMBlockBuffer})^{OpaqueCMByteStream}^{__CFData}}{?=C{?=iIIIIffifiiiiIIIIi{?=II}{?=IIIi}II[100C]}^{CGColorSpace}^{__CFData}^{__CFString}^{__CFString}^{__CFArray}^{__CFArray}}})QQ{?=Cq}{?=Cq}i{?=^{__CFArray}^q^qqqq}}"
- "i40@?0^{CMPhotoDecompressionSession={__CFRuntimeBase=QAQ}{os_unfair_lock_s=I}Q^{__CFSet}@{?=C@@@^{__CFArray}i}{?=C@@@^{__CFArray}i}{?=C@@@^{__CFArray}i}{?=C@@@^{__CFArray}i}{?=Ci{os_unfair_lock_s=I}@^{__CFArray}}^{CMPhotoSurfacePool}^{CMPhotoScaleAndRotateSession}^{CMPhotoCodecSessionPool}^{CMPhotoCodecSessionPool}@?^vQ}8^{CMPhotoDecompressionContainer={__CFRuntimeBase=QAQ}^{CMPhotoDecompressionSession}CCCCC^{CMPhotoDecompressionContainerVTable}(?={?=^{__CFAllocator}^{OpaqueFigPictureCollection}^{OpaqueFigFormatReader}{?=@Cqq^{CGImageMetadata}^{__CFDictionary}i}{?=C^{__CFArray}}{?=Cqq}{?=CC}{?=CCC}{?=CC}}{?=^{__CFAllocator}{?=CCq}^{OpaqueFigFormatReader}^{__CFDictionary}^{?}^{__CFArray}^{__CFArray}@C}{?=^{__CFAllocator}{?=i(?=^v^{__CFURL}^{__IOSurface}^{__CFData}^{OpaqueCMBlockBuffer})^{OpaqueCMByteStream}}^{OpaqueFigSimpleMutex}{?={?=C^{__CFArray}}}^{CMPhotoUnifiedJPEGDecoder}{?=C{?=QQ}iCCi^{__CFData}}{?=CC{?={?=QQ}iI^{CGImageMetadata}^{__CFString}^{__CFDictionary}{?=qQ}Ci^{__CFData}^{CGColorSpace}^{__CFDictionary}}qQ^{?}}{?=CC{?=qQ}iC{?=C{?=QQ}i{?=qQ}i}}{?=CC{?=qQ}}{?=CC{?=qQ}^{__CFData}}{?=CC{?=qQ}^{__CFData}}{?=CC^{__CFData}}{?=CC^{__CFData}}}{?=^{__CFAllocator}{?=i(?=^v^{__CFURL}^{__IOSurface}^{__CFData}^{OpaqueCMBlockBuffer})^{OpaqueCMByteStream}^{__CFData}}{?=C{?=iIIIIffifiiiiIIIIi{?=II}{?=IIIi}II[100C]}^{CGColorSpace}^{__CFData}^{__CFString}^{__CFString}^{__CFArray}^{__CFArray}}})QQ{?=Cq}{?=Cq}i{?=^{__CFArray}^q^qqqq}}16Q24^v32"
- "v40@?0^{CMPhotoDecompressionContainer={__CFRuntimeBase=QAQ}^{CMPhotoDecompressionSession}CCCCC^{CMPhotoDecompressionContainerVTable}(?={?=^{__CFAllocator}^{OpaqueFigPictureCollection}^{OpaqueFigFormatReader}{?=@Cqq^{CGImageMetadata}^{__CFDictionary}i}{?=C^{__CFArray}}{?=Cqq}{?=CC}{?=CCC}{?=CC}}{?=^{__CFAllocator}{?=CCq}^{OpaqueFigFormatReader}^{__CFDictionary}^{?}^{__CFArray}^{__CFArray}@C}{?=^{__CFAllocator}{?=i(?=^v^{__CFURL}^{__IOSurface}^{__CFData}^{OpaqueCMBlockBuffer})^{OpaqueCMByteStream}}^{OpaqueFigSimpleMutex}{?={?=C^{__CFArray}}}^{CMPhotoUnifiedJPEGDecoder}{?=C{?=QQ}iCCi^{__CFData}}{?=CC{?={?=QQ}iI^{CGImageMetadata}^{__CFString}^{__CFDictionary}{?=qQ}Ci^{__CFData}^{CGColorSpace}^{__CFDictionary}}qQ^{?}}{?=CC{?=qQ}iC{?=C{?=QQ}i{?=qQ}i}}{?=CC{?=qQ}}{?=CC{?=qQ}^{__CFData}}{?=CC{?=qQ}^{__CFData}}{?=CC^{__CFData}}{?=CC^{__CFData}}}{?=^{__CFAllocator}{?=i(?=^v^{__CFURL}^{__IOSurface}^{__CFData}^{OpaqueCMBlockBuffer})^{OpaqueCMByteStream}^{__CFData}}{?=C{?=iIIIIffifiiiiIIIIi{?=II}{?=IIIi}II[100C]}^{CGColorSpace}^{__CFData}^{__CFString}^{__CFString}^{__CFArray}^{__CFArray}}})QQ{?=Cq}{?=Cq}i{?=^{__CFArray}^q^qqqq}}8Q16i24i28^v32"
- "{HEIF}"

```
