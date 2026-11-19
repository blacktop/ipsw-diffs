## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO`

```diff

-2851.0.0.0.0
-  __TEXT.__text: 0x3d3aa0
-  __TEXT.__objc_methlist: 0xd58
-  __TEXT.__const: 0x2b480
-  __TEXT.__gcc_except_tab: 0x1d648
-  __TEXT.__cstring: 0x77765
+2851.1.8.0.0
+  __TEXT.__text: 0x3d94a0
+  __TEXT.__objc_methlist: 0xd68
+  __TEXT.__const: 0x2b620
+  __TEXT.__gcc_except_tab: 0x1d860
+  __TEXT.__cstring: 0x78385
   __TEXT.__oslogstring: 0x17
   __TEXT.__constg_swiftt: 0x26a4
   __TEXT.__swift5_typeref: 0x3d88

   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x112f0
-  __TEXT.__eh_frame: 0x8fec
+  __TEXT.__unwind_info: 0x113a0
+  __TEXT.__eh_frame: 0x902c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x47808
+  __DATA_CONST.__const: 0x47880
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_selrefs: 0xb08
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__got: 0xa88
-  __AUTH_CONST.__const: 0x4ed98
-  __AUTH_CONST.__cfstring: 0x35f60
+  __DATA_CONST.__got: 0xaf8
+  __AUTH_CONST.__const: 0x4efc0
+  __AUTH_CONST.__cfstring: 0x36060
   __AUTH_CONST.__objc_const: 0x11d0
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x3278
+  __AUTH_CONST.__auth_got: 0x32c0
   __AUTH_CONST.__auth_ptr: 0x1270
   __AUTH.__objc_data: 0x370
   __AUTH.__data: 0x15c8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
   __DATA.__objc_ivar: 0xa4
-  __DATA.__data: 0x62b0
-  __DATA.__bss: 0x30c78
-  __DATA.__common: 0xaf8
+  __DATA.__data: 0x6440
+  __DATA.__bss: 0x30888
+  __DATA.__common: 0xaf0
   __DATA_DIRTY.__data: 0x38c
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0xbd0
-  __DATA_DIRTY.__common: 0xfd9
+  __DATA_DIRTY.__bss: 0x1050
+  __DATA_DIRTY.__common: 0xfe0
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 19796
-  Symbols:   23002
-  CStrings:  15190
+  Functions: 19865
+  Symbols:   23084
+  CStrings:  15253
 
Symbols:
+ -[IIO_CXMLParser dealloc]
+ GCC_except_table179
+ GCC_except_table188
+ IIO_CreateMergedISO5Metadata
+ _CGColorSpaceContainsISO5Metadata
+ _CGColorSpaceCreateWithCopyOfDataAndMetadata
+ _CGImageCopyColorSyncISO5Metadata
+ _CGImageGetContentAverageLightLevelNits
+ _ColorSyncProfileCopyISO5Metadata
+ _ColorSyncProfileCreateCopyWithISO5Metadata
+ _ColorSyncProfileGetContentHeadroom
+ _ColorSyncProfileGetISO5AverageLightLevel
+ _IIOImageIsHDR
+ _IIO_ColorSpaceCreateWithICCDataAndISO5Metadata
+ _IIO_CreateColorSpaceCopyWithColorSyncISO5Metadata
+ _IIO_CreateISO5MetadataInfo
+ _IIO_CreateImageCopyWithColorSyncISO5Metadata
+ _IIO_CreateMergedISO5Metadata
+ _IIO_FloatsMatch
+ _IIO_GetCLLFromISO5Dict
+ _IIO_GetMDCVLuminanceFromISO5Dict
+ _ZN12BCReadPlugin16decodeDXTCtoRGBXEP19IIOImageReadSessionP13vImage_Buffer16CGImageAlphaInfob
+ _ZN15KTX2WritePlugin8writeOneEP25IIOImagePixelDataProviderP13IIODictionaryS3_j
+ _ZN7GPSCopy11processDataEv
+ _ZN7GPSCopy13checkCapacityEPhm
+ _ZN7GPSCopy15pointerToOffsetEm
+ _ZN7GPSCopy22checkInitializedLengthEPhm
+ _ZN7GPSCopy26copyFileWithGPSInformationEv
+ __Z21CreateReader_DDS_ASTCv
+ __Z22CreateReader_RawCameraP13IIODictionary
+ __ZL18IIO_GetFloatForKeyPK14__CFDictionaryPK10__CFString
+ __ZL19DDSDXGIFormatIsASTCj
+ __ZL21IIO_ApplyCheckNonZeroPKvS0_Pv
+ __ZL24IIO_CreateNeutralISO5KeyPK10__CFString
+ __ZL25IIO_ApplyNeutralISO5EntryPKvS0_Pv
+ __ZL26IIO_ISO5CategoryDictsMatchPK14__CFDictionaryS1_PKPK10__CFStringj
+ __ZL29HEIFCopyColorSyncISO5MetadataP7CGImage
+ __ZL29IIO_ApplyNeutralISO5KeyRenamePKvS0_Pv
+ __ZL31dds_dx9_packed_format_for_masksjjjjj
+ __ZN10IIO_Reader19updateImageAVLLNitsEP7CGImageP19IIOImageReadSessionP12CGColorSpace20CGImageComponentTypej
+ __ZN11OFDDocument5closeEv
+ __ZN11OFDTemplate5closeEv
+ __ZN11OutOfBoundsD0Ev
+ __ZN11OutOfBoundsD1Ev
+ __ZN12BCReadPlugin21decode1010102toRGBA16EP19IIOImageReadSessionP13vImage_Buffer
+ __ZN12BCReadPlugin22decodePacked16toRGBA16EP19IIOImageReadSessionP13vImage_Bufferj
+ __ZN12BCReadPlugin24decodeUncompressedToRGBAEP19IIOImageReadSessionP13vImage_Buffer
+ __ZN13HEIFMainImage23getMaxContentLightLevelEv
+ __ZN13HEIFMainImage28hasISO5ContentLightLevelInfoEv
+ __ZN13HEIFMainImage34getISO5MasteringDisplayColorVolumeEv
+ __ZN13HEIFMainImage34hasISO5MasteringDisplayColorVolumeEv
+ __ZN13IIOReadPlugin29willApplyOrientationTransformEv
+ __ZN14ASTCTextureImp24MetalFormatForDXGIFormatEj
+ __ZN14HEIFReadPlugin29willApplyOrientationTransformEv
+ __ZN14IIO_Reader_RAD27hasCustomCompareOptionsProcEv
+ __ZN15IIO_Reader_HEIF19updateImageAVLLNitsEP7CGImageP19IIOImageReadSessionP12CGColorSpace20CGImageComponentTypej
+ __ZN20IIOPixelConverterRGBC1E13IIO_PixelTypehhhhhS0_hhPKcbb
+ __ZN20IIOPixelConverterRGBC2E13IIO_PixelTypehhhhhS0_hhPKcbb
+ __ZN7GPSCopy13checkCapacityEPhm
+ __ZN7GPSCopy15pointerToOffsetEm
+ __ZN7GPSCopy15read32UncheckedEPh
+ __ZN7GPSCopy22checkInitializedLengthEPhm
+ __ZNKSt9exception4whatEv
+ __ZNSt9exceptionD2Ev
+ __ZTI11OutOfBounds
+ __ZTS11OutOfBounds
+ __ZTV11OutOfBounds
+ __ZZL16DDSASTCBlockDimsjPhS_E4dims
+ __ZZN14ASTCTextureImp24MetalFormatForDXGIFormatEjE3hdr
+ __ZZN14ASTCTextureImp24MetalFormatForDXGIFormatEjE3ldr
+ __ZZN14ASTCTextureImp24MetalFormatForDXGIFormatEjE4srgb
+ _iptc_AIPromptInformation
+ _iptc_AIPromptWriterName
+ _kCGColorSpaceExtendedRange
+ _kCGImagePropertyIPTCExtAIPromptInformation
+ _kCGImagePropertyIPTCExtAIPromptWriterName
+ _kColorSyncAverageLightLevel
+ _kColorSyncAverageLuminance
+ _kColorSyncCCVInfo
+ _kColorSyncCLLInfo
+ _kColorSyncCRWLInfo
+ _kColorSyncDerivedISO5Metadata
+ _kColorSyncMDCVInfo
+ _kColorSyncMaxLightLevel
+ _kColorSyncMaxLuminance
+ _kColorSyncMinLuminance
+ _kColorSyncPrimaries
+ _kColorSyncReferenceWhite
+ _kIIOICCISO5MetadataPropertyKey
+ _sniffDDS
+ _unzClose
+ _vImageConvert_RGBFFFtoRGBAFFFF
- GCC_except_table180
- GCC_except_table185
- GCC_except_table214
- _ZN12IIOImagePlus11setGeometryEPv19CGImagePlusGeometry
- __ZN19IIOReader_RawCameraC1EP13IIODictionary
- __ZN20IIOPixelConverterRGBC1E13IIO_PixelTypehhhhhS0_hhPKc
- __ZN20IIOPixelConverterRGBC2E13IIO_PixelTypehhhhhS0_hhPKc
- __ZN7GPSCopy6read32EPh
- _sniffBC
- _sniffOlympusRaw
CStrings:
+ "       : opacity=%d flags=0x%02x%s\n"
+ " (hidden)"
+ "*** BC - no compressed data for level %d\n"
+ "*** BMP - writePrefix failed, not writing pixel data\n"
+ "*** CMPhotoDecompressionContainerCopyXMPForIndexWithOptions returned noErr with no XMP data\n"
+ "*** DDS/ASTC: image dimensions overflow\n"
+ "*** ERROR: BC (KTX) no complete miplevel in file\n"
+ "*** ERROR: CFURLCreateWithFileSystemPath returned nil.\n"
+ "*** ERROR: CGImagePluginInitThumbJPEGAtOffsetWithOptions offset (%ld) + size (%ld) out of range (%zu)\n"
+ "*** ERROR: CGImageReadCreateWithURL returned nil.\n"
+ "*** ERROR: TIFFSetDirectory failed\n"
+ "*** ERROR: could not create the image reader for the given path.\n"
+ "*** ERROR: decodeStripPlanar destination row is %u bytes, the scatter needs %llu\n"
+ "*** ERROR: decodeTilePlanar destination row is %u bytes, the scatter needs %llu\n"
+ "*** ERROR: extractImageInfo: thumbnail offset (%llu) + length (%llu) out of range (%zu)\n"
+ "*** ERROR: failed to allocte temp (%zu bytes)\n"
+ "*** ERROR: failed to read %zu bytes of pixel data for 420f\n"
+ "*** ERROR: iio_vImageBuffer_InitWithCGImage failed: %ld\n"
+ "*** ERROR: initThumbnail: thumbnail offset (%zu) + length (%zu) out of range (%zu)\n"
+ "*** ERROR: marker 0x%04X is out of bounds (offset %llu, length %u, size %zd) - skipping\n"
+ "*** ERROR: markerLength too big: %u  max: %zd\n"
+ "*** ERROR: no XMP could be reassembled from the extended XMP blocks\n"
+ "*** ERROR: short read for tag %d, count: %d\n"
+ "*** ERROR: updateTiffStruct failed after the codec data format was set\n"
+ "*** ERRROR: could not allocate rlebuf - size=%llu\n"
+ "*** ERRROR: unsupported height (%llu)\n"
+ "*** ERRROR: unsupported width (%llu)\n"
+ "*** NOTE: layer#%u has %u channels; cannot apply opacity %u\n"
+ "*** NOTE: skipping hidden layer#%u\n"
+ "*** RGBX coverage?  bitMask: %08X\n"
+ "*** TIFFReadEncodedStrip(%d) failed - strip %d is zero-filled\n"
+ "*** _bitsPerPixel %d is too small for 4 channels of %d bits [%d-%d-%d-%d]\n"
+ "*** bad 'fcTL' chunk size at offset %ld: %u - expected frames: %ld  found: %ld\n"
+ "*** bad DDS/ASTC data: expected %llu bytes\n"
+ "*** bad DDS/ASTC height %u\n"
+ "*** bad DDS/ASTC width %u\n"
+ "*** bad KTX: [%ldx%ld]  srcBpp: %lld  fileSize: %d\n"
+ "*** bad packed KTX: [%ldx%ld] fileSize: %d\n"
+ "*** can't write KTX - failed to read %zu bytes of pixel data\n"
+ "*** can't write KTX - unsupported image size (%u x %u, rowBytes %zu)\n"
+ "*** can't write KTX2 - bad image size (%zu x %zu)\n"
+ "*** can't write KTX2 - failed to read %zu bytes of pixel data\n"
+ "*** could not create ASTC encoder\n"
+ "*** decode buffer is too small for the SDR conversion\n"
+ "*** decode buffer too small: need %zu bytes (%zu x %zu), have %zu\n"
+ "*** failed to read %zu bytes of pixel data\n"
+ "*** frame[%ld] rect {%d, %d, %d, %d} does not fit the %d x %d destination\n"
+ "*** truncated 'fcTL' chunk at offset %ld - expected frames: %ld  found: %ld\n"
+ "*** truncated chunk header at offset %ld - expected frames: %ld  found: %ld\n"
+ "8BIMiOpa"
+ "AIPromptInformation"
+ "AIPromptWriterName"
+ "AverageLightLevelNits"
+ "ColorPrimaries"
+ "MetadataDisplayName"
+ "Primaries"
+ "com.apple.cmm."
+ "decodeStripChunky"
+ "decodeStripPlanar"
+ "ico image %zu: %zu bytes is too small for a BITMAPINFOHEADER\n"
+ "ico image %zu: header %u + pixels %zu + mask %zu exceeds %zu bytes\n"
+ "loadTIFFStructure"
+ "updateImageAVLLNits"
+ "write420fData"
+ "{ICC ISO-5}"
+ "☀️  %s - failed to update image avll: %d  [colorspace: '%s']\n"
+ "☀️  %s - not setting image avll: %d for SDR [colorspace: '%s']\n"
+ "☀️  %s - updating image AVLL: %d [colorspace: '%s']\n"
- "*** ERROR: failed to allocte temp (%d bytes)\n"
- "*** ERRROR: could not allocate rlebuf - size=%d\n"
- "*** WARNING: check markerLength: %d - expected max: %zd\n"
- "*** bad KTX: [%ldx%ld]  channels: %ld  fileSize: %d\n"
- "CGImageReadCreateWithURL returned nil.\n"
```
