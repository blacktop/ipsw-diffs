## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2851.0.0.0.0
-  __TEXT.__text: 0x4f620c
-  __TEXT.__objc_methlist: 0xd58
-  __TEXT.__const: 0x49ed0
-  __TEXT.__gcc_except_tab: 0x229c0
-  __TEXT.__cstring: 0xa6a6d
+2851.1.4.0.0
+  __TEXT.__text: 0x4faefc
+  __TEXT.__objc_methlist: 0xd68
+  __TEXT.__const: 0x4a070
+  __TEXT.__gcc_except_tab: 0x22b68
+  __TEXT.__cstring: 0xa709d
   __TEXT.__oslogstring: 0x17
   __TEXT.__constg_swiftt: 0x26a4
   __TEXT.__swift5_typeref: 0x3d88

   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x18268
-  __TEXT.__eh_frame: 0x92e4
+  __TEXT.__unwind_info: 0x18340
+  __TEXT.__eh_frame: 0x9314
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0xb48
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__got: 0xaa8
-  __AUTH_CONST.__const: 0x4f290
+  __DATA_CONST.__got: 0xb10
+  __AUTH_CONST.__const: 0x4f2d0
   __AUTH_CONST.__cfstring: 0x36000
   __AUTH_CONST.__objc_const: 0x11d0
   __AUTH_CONST.__weak_auth_got: 0x30

   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x2f78
+  __AUTH_CONST.__auth_got: 0x2fa0
   __AUTH.__objc_data: 0x370
   __AUTH.__data: 0x15d8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x1
   __DATA.__objc_ivar: 0xa4
-  __DATA.__data: 0x65f0
+  __DATA.__data: 0x6780
   __DATA.__common: 0x2270
   __DATA_DIRTY.__data: 0x3b0
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0xbe8
+  __DATA_DIRTY.__bss: 0xc58
   __DATA_DIRTY.__common: 0xff0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
-  Functions: 23176
-  Symbols:   24725
-  CStrings:  18247
+  Functions: 23225
+  Symbols:   24781
+  CStrings:  18283
 
Symbols:
+ -[IIO_CXMLParser dealloc]
+ GCC_except_table179
+ GCC_except_table217
+ _CGColorSpaceCreateWithCopyOfDataAndMetadata
+ _CGImageCopyColorSyncISO5Metadata
+ _ColorSyncProfileCopyISO5Metadata
+ _ColorSyncProfileCreateCopyWithISO5Metadata
+ _IIOImageIsHDR
+ _IIO_ColorSpaceCreateWithICCDataAndISO5Metadata
+ _IIO_CreateColorSpaceCopyWithColorSyncISO5Metadata
+ _IIO_CreateImageCopyWithColorSyncISO5Metadata
+ _IIO_CreateMergedISO5Metadata
+ _IIO_FloatsMatch
+ _IIO_GetCLLFromISO5Dict
+ _IIO_GetMDCVLuminanceFromISO5Dict
+ __Z21CreateReader_DDS_ASTCv
+ __Z22CreateReader_RawCameraP13IIODictionary
+ __ZL18IIO_GetFloatForKeyPK14__CFDictionaryPK10__CFString
+ __ZL19DDSDXGIFormatIsASTCj
+ __ZL26IIO_ISO5CategoryDictsMatchPK14__CFDictionaryS1_PKPK10__CFStringj
+ __ZL29HEIFCopyColorSyncISO5MetadataP7CGImage
+ __ZL31dds_dx9_packed_format_for_masksjjjjj
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
+ __ZN14ASTCTextureImp24MetalFormatForDXGIFormatEj
+ __ZN14IIO_Reader_RAD27hasCustomCompareOptionsProcEv
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
+ _kCGColorSpaceExtendedRange
+ _kColorSyncAverageLightLevel
+ _kColorSyncAverageLuminance
+ _kColorSyncCCVInfo
+ _kColorSyncCLLInfo
+ _kColorSyncCRWLInfo
+ _kColorSyncMDCVInfo
+ _kColorSyncMaxLightLevel
+ _kColorSyncMaxLuminance
+ _kColorSyncMinLuminance
+ _kColorSyncPrimaries
+ _kColorSyncReferenceWhite
+ _sniffDDS
+ _unzClose
+ _vImageConvert_RGBFFFtoRGBAFFFF
- GCC_except_table181
- GCC_except_table185
- GCC_except_table215
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
+ "*** CMPhotoDecompressionContainerCopyXMPForIndexWithOptions returned noErr with no XMP data\n"
+ "*** DDS/ASTC: image dimensions overflow\n"
+ "*** ERROR: BC (KTX) no complete miplevel in file\n"
+ "*** ERROR: TIFFSetDirectory failed\n"
+ "*** ERROR: iio_vImageBuffer_InitWithCGImage failed: %ld\n"
+ "*** ERROR: no XMP could be reassembled from the extended XMP blocks\n"
+ "*** ERRROR: could not allocate rlebuf - size=%llu\n"
+ "*** ERRROR: unsupported height (%llu)\n"
+ "*** ERRROR: unsupported width (%llu)\n"
+ "*** NOTE: layer#%u has %u channels; cannot apply opacity %u\n"
+ "*** NOTE: skipping hidden layer#%u\n"
+ "*** RGBX coverage?  bitMask: %08X\n"
+ "*** _bitsPerPixel %d is too small for 4 channels of %d bits [%d-%d-%d-%d]\n"
+ "*** bad 'fcTL' chunk size at offset %ld: %u - expected frames: %ld  found: %ld\n"
+ "*** bad DDS/ASTC data: expected %llu bytes\n"
+ "*** bad DDS/ASTC height %u\n"
+ "*** bad DDS/ASTC width %u\n"
+ "*** bad KTX: [%ldx%ld]  srcBpp: %lld  fileSize: %d\n"
+ "*** bad packed KTX: [%ldx%ld] fileSize: %d\n"
+ "*** could not create ASTC encoder\n"
+ "*** decode buffer is too small for the SDR conversion\n"
+ "*** decode buffer too small: need %zu bytes (%zu x %zu), have %zu\n"
+ "*** frame[%ld] rect {%d, %d, %d, %d} does not fit the %d x %d destination\n"
+ "*** truncated 'fcTL' chunk at offset %ld - expected frames: %ld  found: %ld\n"
+ "*** truncated chunk header at offset %ld - expected frames: %ld  found: %ld\n"
+ "8BIMiOpa"
+ "TIFFReadDirEntryFloatArray"
+ "TIFFReadDirEntryIfd8Array"
+ "TIFFReadDirEntryLong8ArrayWithLimit"
+ "TIFFReadDirEntryLongArray"
+ "TIFFReadDirEntryShortArray"
+ "TIFFReadDirEntrySlong8Array"
+ "TIFFReadDirEntrySlongArray"
+ "TIFFReadDirEntrySshortArray"
+ "loadTIFFStructure"
- "*** ERRROR: could not allocate rlebuf - size=%d\n"
- "*** bad KTX: [%ldx%ld]  channels: %ld  fileSize: %d\n"
```
