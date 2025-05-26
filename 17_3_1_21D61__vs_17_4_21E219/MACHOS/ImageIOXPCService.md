## ImageIOXPCService

> `/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService`

```diff

-2488.3.8.0.0
-  __TEXT.__text: 0x4165cc
-  __TEXT.__auth_stubs: 0x4300
-  __TEXT.__objc_stubs: 0xfe0
+2488.4.29.0.0
+  __TEXT.__text: 0x41c8c0
+  __TEXT.__auth_stubs: 0x4250
+  __TEXT.__objc_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x310
-  __TEXT.__gcc_except_tab: 0x1f540
+  __TEXT.__gcc_except_tab: 0x1f6d0
   __TEXT.__const: 0x2a770
-  __TEXT.__cstring: 0x777f1
-  __TEXT.__objc_methname: 0x1272
+  __TEXT.__cstring: 0x78c01
+  __TEXT.__objc_methname: 0x1282
   __TEXT.__objc_classname: 0x3f
   __TEXT.__objc_methtype: 0x5f1
   __TEXT.__oslogstring: 0x1ee
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xecbc
-  __TEXT.__eh_frame: 0x1068
-  __DATA_CONST.__auth_got: 0x2198
-  __DATA_CONST.__got: 0x640
-  __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x71668
-  __DATA_CONST.__cfstring: 0xbf40
+  __TEXT.__unwind_info: 0xebbc
+  __TEXT.__eh_frame: 0x1018
+  __DATA_CONST.__auth_got: 0x2140
+  __DATA_CONST.__got: 0x630
+  __DATA_CONST.__auth_ptr: 0x90
+  __DATA_CONST.__const: 0x718c8
+  __DATA_CONST.__cfstring: 0xbee0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x950
-  __DATA.__objc_selrefs: 0x480
-  __DATA.__objc_classrefs: 0x80
-  __DATA.__objc_superrefs: 0x10
+  __DATA.__objc_selrefs: 0x478
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x3200
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x11738
-  __DATA.__common: 0x29bc
+  __DATA.__bss: 0x11728
+  __DATA.__common: 0x2ac4
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 16106
-  Symbols:   10768
-  CStrings:  12570
+  Functions: 16122
+  Symbols:   10801
+  CStrings:  12677
 
Symbols:
+ _IIO_UpdateIOSurfaceOwnershipIdentity
+ _IOSurfaceGetBulkAttachments
+ _IOSurfaceSetOwnershipIdentity
+ __ZN10IIO_Reader17callGetImageCountEP18CGImageReadSessionP13IIODictionaryP19CGImageSourceStatusPi
+ __ZN12HEIFAuxImage20auxiliaryPixelFormatEv
+ __ZN12IIOImageRead10trustedURLEv
+ __ZN12IIOImageReadC1EPK8__CFData15CGImageReadTypebbb
+ __ZN12IIOImageReadC1EiPhmbb
+ __ZN12IIOImageReadC2EPK8__CFData15CGImageReadTypebbb
+ __ZN12IIOImageReadC2EiPhmbb
+ __ZN12IIOXPCClient16useServerForCallEP12IIOImageReadP10IIO_Reader10IIORequest10IIO_XPC_IDb
+ __ZN12IIOXPCClient18ProcessSupportsOOPEv
+ __ZN12IIOXPCClient21useServerForInitImageEP12IIOImageReadP10IIO_Reader10IIORequest
+ __ZN12IIOXPCClient22useServerForDecodeDataEP12IIOImageReadP10IIO_Reader10IIORequest
+ __ZN12IIOXPCClient22useServerForImageCountEP12IIOImageReadP10IIO_Reader10IIORequest
+ __ZN12IIOXPCClient23useServerForDecodeImageEP12IIOImageReadP10IIO_Reader10IIORequest
+ __ZN12IIOXPCClient24useServerForCopyBlockSetEP12IIOImageReadP10IIO_Reader10IIORequest
+ __ZN12IIOXPCClient25useServerForCopyIOSurfaceEP12IIOImageReadP10IIO_Reader10IIORequest
+ __ZN12IIOXPCClient26useServerForIdentificationEP12IIOImageRead10IIORequest
+ __ZN12IIOXPCClient28useServerForSourcePropertiesEP12IIOImageReadP10IIO_Reader10IIORequest
+ __ZN13JP2ReadPlugin21checkImageTileSizeBoxEP10IIOScanner
+ __ZN13JP2ReadPlugin26checkCodingStyleDefaultBoxEP10IIOScanner
+ __ZN14GlobalHEIFInfo12setLoopCountEj
+ __ZN14GlobalHEIFInfo9loopCountEv
+ __ZN14IIOImageSource19updateThumbnailInfoEP13IIODictionaryPjS2_
+ __ZN14IIOImageSource23getThumbnailInfoAtIndexEmjP16IIOThumbnailInfo
+ __ZN17IIO_ReaderHandler14readerForBytesEPKhmPK10__CFStringP12IIOImageReadm16IIOHeaderOptions10IIORequestPi
+ __ZN18HEIFAlternateImage13writeToStreamEP15__CFWriteStream
+ __ZN18HEIFAlternateImage14readFromStreamEP14__CFReadStream
+ __ZN18HEIFAlternateImageC1EP14__CFReadStream
+ __ZN18HEIFAlternateImageC1EPK14__CFDictionaryS2_ji
+ __ZN18HEIFAlternateImageC2EP14__CFReadStream
+ __ZN18HEIFAlternateImageC2EPK14__CFDictionaryS2_ji
+ __ZN18HEIFAlternateImageD0Ev
+ __ZN18HEIFAlternateImageD1Ev
+ __ZN18HEIFAlternateImageD2Ev
+ __ZN19AppleJPEGReadPlugin19decodeIntoIOSurfaceEP18IIODecodeParameterP11__IOSurface
+ __ZN19AppleJPEGReadPlugin22copyImageBlockSetTilesEP7InfoRecP15CGImageProvider6CGRect6CGSizemPi
+ __ZN19AppleJPEGReadPlugin37createImageBlockSetWithHardwareDecodeEP7InfoRecP15CGImageProvider6CGSizePK14__CFDictionaryPi
+ __ZN19IIOReader_RawCamera17callGetImageCountEP18CGImageReadSessionP13IIODictionaryP19CGImageSourceStatusPi
+ __ZN9_JPEGFile15removeAppMarkerEP5_APPx
+ __ZNK14ASTCTextureImp17textureBaseOffsetEv
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
+ __ZTI18HEIFAlternateImage
+ __ZTS18HEIFAlternateImage
+ __ZTV18HEIFAlternateImage
+ _gFunc_CMPhotoDecompressionContainerCopyAuxiliaryImageMetadataForIndex
+ _gFunc_CVColorPrimariesGetStringForIntegerCodePoint
+ _gFunc_CVPixelBufferGetBaseAddressOfPlane
+ _gFunc_CVPixelBufferGetBytesPerRowOfPlane
+ _gFunc_CVTransferFunctionGetStringForIntegerCodePoint
+ _gFunc_CVYCbCrMatrixGetStringForIntegerCodePoint
+ _gIIO_kCMPhotoCompressionOption_BitDepth
+ _gIIO_kCMPhotoDecompressionContainerDescription_LoopCount
+ _gIIO_kCVImageBufferChromaLocationBottomFieldKey
+ _gIIO_kCVImageBufferChromaLocationTopFieldKey
+ _gIIO_kCVImageBufferChromaLocation_Bottom
+ _gIIO_kCVImageBufferChromaLocation_BottomLeft
+ _gIIO_kCVImageBufferChromaLocation_Center
+ _gIIO_kCVImageBufferChromaLocation_DV420
+ _gIIO_kCVImageBufferChromaLocation_Left
+ _gIIO_kCVImageBufferChromaLocation_Top
+ _gIIO_kCVImageBufferChromaLocation_TopLeft
+ _gIIO_kCVImageBufferChromaSubsamplingKey
+ _gIIO_kCVImageBufferChromaSubsampling_411
+ _gIIO_kCVImageBufferChromaSubsampling_420
+ _gIIO_kCVImageBufferChromaSubsampling_422
+ _gIIO_kCVImageBufferColorPrimariesKey
+ _gIIO_kCVImageBufferContentLightLevelInfoKey
+ _gIIO_kCVImageBufferGammaLevelKey
+ _gIIO_kCVImageBufferMasteringDisplayColorVolumeKey
+ _gIIO_kCVImageBufferTransferFunctionKey
+ _gIIO_kCVImageBufferTransferFunction_UseGamma
+ _gIIO_kCVPixelFormatBitsPerComponent
+ _gIIO_kCVPixelFormatComponentRange
+ _gIIO_kCVPixelFormatComponentRange_FullRange
+ _gIIO_kCVPixelFormatComponentRange_VideoRange
+ _gIIO_kCVPixelFormatContainsGrayscale
+ _gIIO_kCVPixelFormatContainsRGB
+ _kCGImagePropertyTIFFXPosition
+ _kCGImagePropertyTIFFYPosition
+ _kCGImageWrappingIOSurfacePixelFormat
+ _rootless_trusted_by_self_token
+ _rootless_verify_trusted_by_self_token
+ _tiff_xPosition
+ _tiff_yPosition
+ _vImageConverter_CreateWithCGColorConversionInfo
- _CFBundleCreate
- _CFBundleIsExecutableLoaded
- _CGImageBlockSetGetSize
- _ColorSyncTransformCopyProperty
- _ColorSyncTransformCreate
- _ColorSyncTransformCreateWithName
- _IIO_CreateColorConverter
- _OBJC_CLASS_$_NSURL
- __ZN10IIO_Reader17callGetImageCountEP18CGImageReadSessionP13IIODictionaryP19CGImageSourceStatus
- __ZN12HEIFAuxImage25auxiliaryAlphaPixelFormatEv
- __ZN12IIOImageReadC1EPK8__CFData15CGImageReadTypebb
- __ZN12IIOImageReadC1EiPhmb
- __ZN12IIOImageReadC2EPK8__CFData15CGImageReadTypebb
- __ZN12IIOImageReadC2EiPhmb
- __ZN12IIOXPCClient16useServerForCallEP10IIO_Reader10IIORequest10IIO_XPC_IDb
- __ZN12IIOXPCClient21useServerForInitImageEP10IIO_Reader10IIORequest
- __ZN12IIOXPCClient22useServerForDecodeDataEP10IIO_Reader10IIORequest
- __ZN12IIOXPCClient22useServerForImageCountEP10IIO_Reader10IIORequest
- __ZN12IIOXPCClient23useServerForDecodeImageEP10IIO_Reader10IIORequest
- __ZN12IIOXPCClient24useServerForCopyBlockSetEP10IIO_Reader10IIORequest
- __ZN12IIOXPCClient25useServerForCopyIOSurfaceEP10IIO_Reader10IIORequest
- __ZN12IIOXPCClient26useServerForIdentificationE10IIORequest
- __ZN12IIOXPCClient28useServerForSourcePropertiesEP10IIO_Reader10IIORequest
- __ZN12IIOXPCClient33useServerForDecodeFramesAtIndexesEP10IIO_Reader10IIORequest
- __ZN12IIOXPCClient34useServerForIdentificationAndCountE10IIORequest
- __ZN14IIOImageSource19updateThumbnailInfoEP13IIODictionary
- __ZN14IIOImageSource23getThumbnailInfoAtIndexEmj
- __ZN17IIOColorConverter27createConverterWithProfilesEP20vImage_CGImageFormatS1_PK16ColorSyncProfileS4_
- __ZN17IIOColorConverter31createWithColorSyncCodeFragmentEP20vImage_CGImageFormatS1_P12CGColorSpaceS3_
- __ZN17IIOColorConverterC1EP20vImage_CGImageFormatS1_PK16ColorSyncProfileS4_
- __ZN17IIOColorConverterC2EP20vImage_CGImageFormatS1_PK16ColorSyncProfileS4_
- __ZN17IIO_ReaderHandler14readerForBytesEPKhmPK10__CFStringm16IIOHeaderOptions10IIORequestPi
- __ZN19AppleJPEGReadPlugin15createConverterEPKvj
- __ZN19AppleJPEGReadPlugin22copyImageBlockSetTilesEP7InfoRecP15CGImageProvider6CGRect6CGSizePK14__CFDictionaryPi
- __ZN19AppleJPEGReadPlugin26createMatchedIOSurfaceCopyEP11__IOSurfacePKvj
- __ZN19AppleJPEGReadPlugin30copy_BGR8_to_CIF10_surfacedataEP11__IOSurfaceS1_
- __ZN19AppleJPEGReadPlugin37createImageBlockSetWithHardwareDecodeEP7InfoRecP15CGImageProvider6CGSizePK14__CFDictionary
- __ZN19IIOReader_RawCamera17callGetImageCountEP18CGImageReadSessionP13IIODictionaryP19CGImageSourceStatus
- __ZN20IIOImageProviderInfo20colorConvertIfNeededEP15CGImageBlockSetP15CGImageProvider6CGRect6CGSizePK14__CFDictionaryb
- __ZN8_TAGList10indexOfTagEP4_TAG
- __ZN9_JPEGFile22removeAppMarkerAtIndexEt
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
- _calloc
- _kColorSyncDisplayP3Profile
- _kColorSyncTransformFullConversionData
- _malloc
- _realloc
- _task_create_identity_token
- _vImageConvert_ARGB8888ToXRGB2101010
- _vImageConverter_CreateWithColorSyncCodeFragment
- _vm_purgable_control
- _xpc_connection_create_mach_service
- _xpc_dictionary_set_mach_send
CStrings:
+ "                 error: %@"
+ "    decoding multi tiles [%d]: {%g,%g,%g,%g} {%g,%g}\n"
+ "#️⃣ hash {%g,%g,%g,%g} rb: %d   ptr: %p   size: %ld  '%016x'\n"
+ "%s retrying 'copyIOSurface'  err: %d\n"
+ "%s retrying 'copyImageBlockSet'  err: %d\n"
+ "%s retrying 'decodeImage'  err: %d\n"
+ "%s retrying 'getImageCount'  err: %d\n"
+ "%s retrying 'initializeImageAtOffset'  err: %d\n"
+ "%s retrying 'readerForBytes'  err: %d\n"
+ "%s retrying 'updateSourceProperties'  err: %d\n"
+ "(CFDataRef) %p @\"%ld bytes\""
+ "*** ERROR - check the _surfacePixelFormat case '%c%c%c%c'\n"
+ "*** ERROR: CGBitmapContextCreateImage returned NULL\n"
+ "*** ERROR: CGImageBlockSetCreate returned NULL - called with NULL provider\n"
+ "*** ERROR: CGImageCreateCopyWithParametersNew returned NULL\n"
+ "*** ERROR: CGImageSourceCreateThumbnailAtIndex[%ld] - '%c%c%c%c' - failed to create thumbnail [%d] {alw:%d, abs: %d tra:%d max:%d}\n"
+ "*** ERROR: CGImageSourceGetSource returned NULL\n"
+ "*** ERROR: CVPixelBufferCreateWithBytes err = %s [%d]  '%c%c%c%c'\n"
+ "*** ERROR: IOSurface '%s' [%c%c%c%c] has no kIOSurfaceColorSpace/kIOSurfaceICCProfile - using %s\n"
+ "*** ERROR: IOSurfaceSetOwnershipIdentity failed: %d"
+ "*** ERROR: _blockArray: %p    _blockArray[%d]: %p\n"
+ "*** ERROR: _blockCount is 0   (_blockArray: %p)\n"
+ "*** ERROR: _tga._tgaHeader.hasPalette: %d\n"
+ "*** ERROR: alpha dimension (%dxd%d) does not match image dimension (%dxd%d) - ignoring alpha\n"
+ "*** ERROR: at_block_get_features issue (size=0)  #channels:%d  blockSize: %dx%d\n"
+ "*** ERROR: bad 'COD NumDecompositionLevels' (%d)\n"
+ "*** ERROR: bad 'COD NumberOfLayers' (%d)\n"
+ "*** ERROR: bad bitsPerComponent '%d'\n"
+ "*** ERROR: bad bpc:%d bpp:%d alpha:%d\n"
+ "*** ERROR: bad bytesPerRow %d for width: %d bpc: %d\n"
+ "*** ERROR: bad dimension: %dx%d\n"
+ "*** ERROR: bad image size (%ld x %ld) rb: %ld\n"
+ "*** ERROR: bad targetColorSpaceType %d\n"
+ "*** ERROR: bitsPerPixel: %d alphaInfo:%d\n"
+ "*** ERROR: bpp: %d   minPixelSize: %d"
+ "*** ERROR: callInitializeImageAtOffset err:%d\n"
+ "*** ERROR: cannot save %d-bitPerComoponent alpha\n"
+ "*** ERROR: color conversion fp16_xsRGB to fp16_P3 failed: %d\n"
+ "*** ERROR: context is NULL\n"
+ "*** ERROR: conversion from CIF10 to FP16 failed: %d\n"
+ "*** ERROR: copyIOSurfaceImp returned: %d\n"
+ "*** ERROR: copyImageBlockSetWithOptions10Bit err = %d\n"
+ "*** ERROR: copyImageBlockSetWithOptions16Bit err = %d\n"
+ "*** ERROR: copyImageBlockSetWithOptions8Bit err = %d\n"
+ "*** ERROR: copy_2C0h_16bit returned: %d\n"
+ "*** ERROR: copy_BGRA_16bit returned: %d\n"
+ "*** ERROR: copy_L008_16bit returned: %d\n"
+ "*** ERROR: copy_LA08_16bit returned: %d\n"
+ "*** ERROR: copy_RGBA_16bit returned: %d\n"
+ "*** ERROR: copy_RGhA_16bit returned: %d\n"
+ "*** ERROR: copy_and_colormatch_CIF10_to_P3_CA returned: %d\n"
+ "*** ERROR: copy_and_colormatch_CIF10_to_P3_MSR returned: %d\n"
+ "*** ERROR: copy_and_colormatch_CIF10_to_P3_vImage returned: %d\n"
+ "*** ERROR: copy_to_CIF10_FP16_xsRGB returned: %d\n"
+ "*** ERROR: could not find plugin for image source - imageRead is NULL\n"
+ "*** ERROR: createImage err:%d\n"
+ "*** ERROR: createImageAtIndex %d could not find plugin for image source [%ld bytes] %02X %02X %02X %02X %02X %02X %02X %02X... '%c%c%c%c%c%c%c%c'\n"
+ "*** ERROR: createImageAtIndex[%ld] - '%c%c%c%c' - failed to create image [%d]\n"
+ "*** ERROR: dstImage is NULL\n"
+ "*** ERROR: duplicate _APPX? '%p' (markerID: 0x%04X) already exists\n"
+ "*** ERROR: duplicate _TAG? '%p' (markerID: 0x%04X) already exists\n"
+ "*** ERROR: iio_vImageConvert_16Fto16U returned: %d\n"
+ "*** ERROR: iio_vImageConvert_ARGB8888ToARGB16U returned: %d\n"
+ "*** ERROR: iio_vImageConvert_Planar8To16U returned: %d\n"
+ "*** ERROR: invalid JP2: CodestreamBox missing SOC\n"
+ "*** ERROR: marker '%c%c%c%c' length (%d) at offset (%d [0x%04X]) larger than fileSize(%d)\n"
+ "*** ERROR: offset (%ld) out of range (%ld)\n"
+ "*** ERROR: pixelFormat was not set for:  bpc:%d   bpp:%d\n"
+ "*** ERROR: sanityCheck failed\n"
+ "*** ERROR: setupGeometry failed\n"
+ "*** ERROR: targetColorSpace is NULL\n"
+ "*** ERROR: unexpected 'Progression order for the SGcod, SPcoc, and Ppoc parameters' (%d)\n"
+ "*** ERROR: unexpected image type (%d) with color palette\n"
+ "*** ERROR: unexpected numberOfChannels: %d\n"
+ "*** ERROR: vImageConvert_16Fto16U err: %d\n"
+ "*** ERROR: vImageConvert_Planar16FtoPlanar8 err: %d\n"
+ "*** Error: CGImageReadSessionCreate returned NULL\n"
+ "*** Error: imageReadRef returned NULL\n"
+ "*** Error: ipRef is NULL\n"
+ "*** NOTE: no kCGImageSourceThumbnailMaxPixelSize specified using 'full image size'\n"
+ "*** copyImageBlockSet_10bit '%c%c%c%c' failed: err=%d\n"
+ "*** copyImageBlockSet_16bit '%c%c%c%c' failed: err=%d\n"
+ "*** imageProperties-bitDepth: %d    bpc: %d  -- using: %d bit/component\n"
+ "*** invalid JPEG2000 file ***\n"
+ "CGImageDestinationCopyImageSource: source is corrupt\n"
+ "CMPhotoDecompressionContainerCopyAuxiliaryImageMetadataForIndex"
+ "CVColorPrimariesGetStringForIntegerCodePoint"
+ "CVPixelBufferGetBaseAddressOfPlane"
+ "CVPixelBufferGetBytesPerRowOfPlane"
+ "CVTransferFunctionGetStringForIntegerCodePoint"
+ "CVYCbCrMatrixGetStringForIntegerCodePoint"
+ "ExtendedLinearGray"
+ "ExtendedLinearSRGB"
+ "GenericGrayGamma2_2"
+ "IIO_UpdateIOSurfaceOwnershipIdentity"
+ "S   CopyImageBlockSetWithOptions: {%g, %g, %g, %g} {%g, %g} '%c%c%c%c' %s\n"
+ "SRGB"
+ "T@\"NSString\",?,R,C"
+ "[%p] {%ld,%ld}  rb:%ld  bpc:%ld  (%s) %c%c%c%c"
+ "addImageBlocksToXPCObject"
+ "checkCodingStyleDefaultBox"
+ "checkContinousCodestreamBox"
+ "copyImageBlockSetWithOptions10Bit"
+ "copyImageBlockSetWithOptions16Bit"
+ "copyImageBlockSetWithOptions8Bit"
+ "initWithContentsOfURL:options:error:"
+ "insertAppMarker"
+ "insertTag"
+ "kCGImageWrappingIOSurfacePixelFormat"
+ "kCMPhotoCompressionOption_BitDepth"
+ "kCMPhotoDecompressionContainerDescription_LoopCount"
+ "kCVImageBufferChromaLocationBottomFieldKey"
+ "kCVImageBufferChromaLocationTopFieldKey"
+ "kCVImageBufferChromaLocation_Bottom"
+ "kCVImageBufferChromaLocation_BottomLeft"
+ "kCVImageBufferChromaLocation_Center"
+ "kCVImageBufferChromaLocation_DV420"
+ "kCVImageBufferChromaLocation_Left"
+ "kCVImageBufferChromaLocation_Top"
+ "kCVImageBufferChromaLocation_TopLeft"
+ "kCVImageBufferChromaSubsamplingKey"
+ "kCVImageBufferChromaSubsampling_411"
+ "kCVImageBufferChromaSubsampling_420"
+ "kCVImageBufferChromaSubsampling_422"
+ "kCVImageBufferColorPrimariesKey"
+ "kCVImageBufferContentLightLevelInfoKey"
+ "kCVImageBufferGammaLevelKey"
+ "kCVImageBufferMasteringDisplayColorVolumeKey"
+ "kCVImageBufferTransferFunctionKey"
+ "kCVImageBufferTransferFunction_UseGamma"
+ "kCVPixelFormatBitsPerComponent"
+ "kCVPixelFormatComponentRange"
+ "kCVPixelFormatComponentRange_FullRange"
+ "kCVPixelFormatComponentRange_VideoRange"
+ "kCVPixelFormatContainsGrayscale"
+ "kCVPixelFormatContainsRGB"
+ "send_message_with_reply"
+ "v4.0.0-76-g16d3b6b4-dirty"
+ "write_P1_ASCII"
+ "write_P2_ASCII"
+ "write_P3_ASCII"
+ "write_P4_Binary"
+ "write_P5_Binary"
+ "write_P6_Binary"
+ "write_PF_Binary"
+ "write_Pf_Binary"
+ "‼️ retrying 'copyIOSurface' (ImageIOXPCService crashed?)\n"
+ "‼️ retrying 'copyImageBlockSet' (ImageIOXPCService crashed?)\n"
+ "‼️ retrying 'decodeImage' (ImageIOXPCService crashed?)\n"
+ "‼️ retrying 'getImageCount' (ImageIOXPCService crashed?)\n"
+ "‼️ retrying 'initializeImageAtOffset' (ImageIOXPCService crashed?)\n"
+ "‼️ retrying 'readerForBytes' (ImageIOXPCService crashed?)\n"
+ "‼️ retrying 'updateSourceProperties' (ImageIOXPCService crashed?)\n"
+ "☀️  ***ERROR: cannot applyGainMap / applyToneMap into a caller-provided IOSurface\n"
+ "❌ Error: ImageIOXPCService send message error: %s\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_COPYBLOCKSET XPC connection interrupted\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_COPYIOSURFACE XPC connection interrupted\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_DECODE_IMAGE XPC connection interrupted\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_IMAGECOUNT XPC connection interrupted\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_INITIMAGE XPC connection interrupted\n"
+ "❌ copy_RGBA_10bit not handled\n"
- "    ImageIO_make_non_purgeable: %14p\n"
- "    ImageIO_make_purgeable:     %14p\n"
- "    decoding multi tiles: {%g,%g,%g,%g} {%g,%g}\n"
- "    vm_purgable_control-SET_STATE-VM_PURGABLE_NONVOLATILE : %ld\n"
- "    vm_purgable_control-SET_STATE-VM_PURGABLE_VOLATILE : %ld\n"
- "*** ERROR: CGImageSourceCreateThumbnailAtIndex[%ld] - '%c%c%c%c' - failed to create thumbnail [%d]\n"
- "*** ERROR: CVPixelBufferCreateWithBytes err = %s [%d]\n"
- "*** ERROR: offset (%d) out of range (%d)\n"
- "*** ERROR: task_create_identity_token: %s"
- "*** ERROR: vImageConverter_CreateWithColorSyncCodeFragment - %d - '%s'\n"
- "*** Error: createThumbnailAtIndex - max not specified -- failing...\n"
- "*** bpp: %d   minPixelSize: %d"
- "*** could not find plugin for image source - imageRead is NULL\n"
- "*** invalid JPEG2000 file\n"
- "*** sourceType: %d could not find plugin for image source [%ld bytes] %02X %02X %02X %02X %02X %02X %02X %02X... '%c%c%c%c%c%c%c%c'\n"
- "/System/Library/Frameworks/UIKit.framework"
- "CGImagePlus.cpp"
- "Failed to create vImageConverter, error: %d\n"
- "Failed to extract code fragment from ColorSyncTransform\n"
- "IIO_CreateColorConverter"
- "IIO_ImageBlockSetCreate returned NULL\n"
- "S   CopyImageBlockSetWithOptions: {%g, %g, %g, %g} {%g, %g} %s\n"
- "[%p] {%ld,%ld}  rb:%ld  bpc:%ld  (%s)"
- "blockSet"
- "colorConvert err: %d\n"
- "colorConvertIfNeeded"
- "com.apple.MessagesAirlockService"
- "com.apple.MessagesBlastDoorService"
- "com.apple.WebKit.WebContent"
- "com.apple.WebKit.WebContent.CaptivePortal"
- "com.apple.WebKit.WebContent.Crashy"
- "com.apple.WebKit.WebContent.Development"
- "com.apple.iiod"
- "com.apple.imageio.useragent.queue"
- "copy_BGR8_to_CIF10_surfacedata"
- "create user agent connection\n"
- "create user agent queue\n"
- "createConverterWithProfiles"
- "createMatchedIOSurfaceCopy"
- "createWithColorSyncCodeFragment"
- "fileURLWithPath:"
- "hash {%g,%g,%g,%g} ptr: %p   size: %ld  '%016x'\n"
- "image size error (%ld x %ld) rb: %ld\n"
- "initWithContentsOfURL:"
- "saveDataToXPCObject_block_invoke"
- "vImageConvert_16Fto16U err: %d\n"
- "vImageConvert_ARGB8888ToXRGB2101010 err: %d\n"
- "vImageConvert_Planar16FtoPlanar8 err: %d\n"
- "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_COPYBLOCKSET corrupt XPC reply: %d\n"
- "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_COPYIOSURFACE corrupt XPC reply: %d\n"
- "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_DECODE_IMAGE corrupt XPC reply: %d\n"
- "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_IMAGECOUNT corrupt XPC reply: %d\n"
- "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_INITIMAGE corrupt XPC reply: %d\n"

```
