## ImageIOXPCService

> `/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService`

```diff

-2488.0.1.6.0
-  __TEXT.__text: 0x412ec0
+2488.1.11.0.0
+  __TEXT.__text: 0x415220
   __TEXT.__auth_stubs: 0x41f0
   __TEXT.__objc_stubs: 0xf60
   __TEXT.__objc_methlist: 0x310
-  __TEXT.__gcc_except_tab: 0x1f3ac
-  __TEXT.__const: 0x2a720
-  __TEXT.__cstring: 0x76660
+  __TEXT.__gcc_except_tab: 0x1f52c
+  __TEXT.__const: 0x2a760
+  __TEXT.__cstring: 0x76f5e
   __TEXT.__objc_methname: 0x1242
   __TEXT.__objc_classname: 0x3f
   __TEXT.__objc_methtype: 0x5f1
   __TEXT.__oslogstring: 0x1ef
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xec64
+  __TEXT.__unwind_info: 0xec44
   __TEXT.__eh_frame: 0x1068
   __DATA_CONST.__auth_got: 0x2110
-  __DATA_CONST.__got: 0x628
+  __DATA_CONST.__got: 0x5c0
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x714e8
-  __DATA_CONST.__cfstring: 0xbe80
+  __DATA_CONST.__const: 0x71560
+  __DATA_CONST.__cfstring: 0xbea0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x950
   __DATA.__objc_selrefs: 0x460
   __DATA.__objc_classrefs: 0x78
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x31f8
+  __DATA.__data: 0x3200
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x116f8
-  __DATA.__common: 0x2f8c
+  __DATA.__bss: 0x11708
+  __DATA.__common: 0x29bc
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 829A1455-3E2C-35A1-A5CD-C0D2A9AA29FF
-  Functions: 16081
-  Symbols:   10731
-  CStrings:  13970
+  UUID: 1480CFA5-720C-3879-BEFE-862DCA4C4E5A
+  Functions: 16073
+  Symbols:   10704
+  CStrings:  14011
 
Symbols:
+ _CFBundleGetValueForInfoDictionaryKey
+ _CGColorSpaceCreateLinearized
+ _CGCreatePNGDataFromSVGData
+ _CGGetImageIOVersion
+ _IIOXPCLog
+ _IIOXPCUpdateAllowedTypes
+ _IIOXPCUpdatePermissions
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ __Z15IIOSkipMetadataP13IIODictionary
+ __Z19IIOSkipXMP_and_IPTCP13IIODictionary
+ __Z38IIOMetadataFlagsFromImageSourceOptionsP13IIODictionary
+ __ZN12IIOXPCClient17oopFeatureEnabledEv
+ __ZN12IIOXPCClient23debugSendingMessageDoneEPv
+ __ZN14IIOImageSource18getTypeIfAvailableEv
+ __ZN14IIOImageSource33imageDataDidNotMatchRequestedHintEv
+ __ZN17IIO_ReaderHandler14readerForBytesEPKhmPK10__CFStringmbb10IIORequestPi
+ __ZN17IIO_ReaderHandler17readerForBytesImpEPKhmPK10__CFStringmbb10IIORequestPi
+ __ZN17LibJPEGReadPlugin14decodeImageImpEP18IIODecodeParameter12IIOImageTypePP11__IOSurfacePP10__CVBufferPP15CGImageBlockSet
+ __ZN17LibJPEGReadPlugin20copyImageBlockSetImpEP7InfoRecP15CGImageProvider6CGRect6CGSizePK14__CFDictionary
+ __cg_TIFFNumberOfDirectories
+ __cg_TIFFOpen
+ _kCFBundleVersionKey
+ _kCGFallbackHDRGain
+ _kCGImagePropertyOpenEXRChromaticities
+ _xpc_dictionary_get_array
- _TIFFNumberOfDirectories
- _TIFFOpen
- __Z27FlagsFromImageSourceOptionsP13IIODictionary
- __ZN13IIO_Reader_AI12canDecodeOOPEj
- __ZN13IIO_Reader_BC12canDecodeOOPEj
- __ZN14IIO_Reader_ATX12canDecodeOOPEj
- __ZN14IIO_Reader_BMP12canDecodeOOPEj
- __ZN14IIO_Reader_CUR12canDecodeOOPEj
- __ZN14IIO_Reader_DDS12canDecodeOOPEj
- __ZN14IIO_Reader_ETC12canDecodeOOPEj
- __ZN14IIO_Reader_GIF12canDecodeOOPEj
- __ZN14IIO_Reader_ICO12canDecodeOOPEj
- __ZN14IIO_Reader_JP212canDecodeOOPEj
- __ZN14IIO_Reader_KTX12canDecodeOOPEj
- __ZN14IIO_Reader_MPO12canDecodeOOPEj
- __ZN14IIO_Reader_PBM12canDecodeOOPEj
- __ZN14IIO_Reader_PDF12canDecodeOOPEj
- __ZN14IIO_Reader_PNG12canDecodeOOPEj
- __ZN14IIO_Reader_PSD12canDecodeOOPEj
- __ZN14IIO_Reader_PVR12canDecodeOOPEj
- __ZN14IIO_Reader_RAD12canDecodeOOPEj
- __ZN14IIO_Reader_TGA12canDecodeOOPEj
- __ZN14IIO_Reader_XBM12canDecodeOOPEj
- __ZN15IIO_Reader_ASTC12canDecodeOOPEj
- __ZN15IIO_Reader_HEIF12canDecodeOOPEj
- __ZN15IIO_Reader_ICNS12canDecodeOOPEj
- __ZN15IIO_Reader_KTX212canDecodeOOPEj
- __ZN15IIO_Reader_TIFF12canDecodeOOPEj
- __ZN15IIO_Reader_WebP12canDecodeOOPEj
- __ZN17IIO_ReaderHandler14readerForBytesEPKhmPK10__CFStringmb10IIORequest
- __ZN17LibJPEGReadPlugin17copyImageBlockSetEP7InfoRecP15CGImageProvider6CGRect6CGSizePK14__CFDictionary
- __ZN18IIO_Reader_LibJPEG12canDecodeOOPEj
- __ZN18IIO_Reader_OpenEXR12canDecodeOOPEj
- __ZN20IIO_Reader_AppleJPEG12canDecodeOOPEj
- __os_log_fault_impl
- __xpc_type_array
- __xpc_type_bool
- __xpc_type_connection
- __xpc_type_data
- __xpc_type_date
- __xpc_type_double
- __xpc_type_endpoint
- __xpc_type_fd
- __xpc_type_int64
- __xpc_type_null
- __xpc_type_shmem
- __xpc_type_string
- __xpc_type_uint64
- __xpc_type_uuid
- _xpcLog
- _xpc_dictionary_apply
- _xpc_dictionary_get_double
CStrings:
+ "(branch_min[index] >= -work_L) && (branch_max[index] <= work_L)"
+ "(last + 1) % num_colors == first"
+ "*** ERROR: CGCreatePNGDataFromSVGData - pngData is NULL\n"
+ "*** ERROR: CGCreatePNGDataFromSVGData - svgData is NULL\n"
+ "*** ERROR: Invalid dfdLength (%d)."
+ "*** ERROR: Invalid dfdOffset (%d)."
+ "*** ERROR: Invalid kvdLength (%d)."
+ "*** ERROR: Invalid kvdOffset (%d)."
+ "*** ERROR: Invalid numberOfArrayElements (%d)."
+ "*** ERROR: Invalid scgdLength (%d)."
+ "*** ERROR: Invalid scgdOffset (%d)."
+ "*** ERROR: Invalid typeSize (%d). typeSize must be 1 for block-compressed or supercompressed formats."
+ "*** ERROR: hint ('%s') does not match image data - kCGImageSourceFailForDataNotMatchingHint was specified --> failing\n"
+ "*** ERROR: invalid CGImageSourceRef (non-matching hint)\n"
+ "*** ERROR: tileHeight %d is not a multiple of 16\n"
+ "*c1 != *c2"
+ "Alpha decoder initialization failed."
+ "CGCreatePNGDataFromSVGData"
+ "CGGetImageIOVersion"
+ "CoOccurrenceFindMax"
+ "GetColorPalette"
+ "IIO_LogRestrictions"
+ "ImageIOXPCAllowedTypesArray"
+ "ImageIOXPCFailIfNotMatchingHint"
+ "ImageIOXPCPermissionData"
+ "Malformed JEPG2000 - overflow."
+ "PaletteCompareColorsForQsort"
+ "PaletteSort"
+ "PaletteSortModifiedZeng"
+ "ReadHuffmanCode"
+ "Unexpected rowsperstrip: %lu"
+ "WebPUnfilters[WEBP_FILTER_NONE] != NULL"
+ "XPC_READPLUGIN_CREATE_PNG_FROM_SVG"
+ "XPC_READPLUGIN_UPDATE_ALLOWED_TYPES"
+ "XPC_READPLUGIN_UPDATE_PERMISSIONS"
+ "a != b"
+ "create xpc service connection (_connection: %p)\n"
+ "createImageFromSource"
+ "doBindToReader"
+ "getEnableRestrictedDecodingFlag"
+ "kCGFallbackHDRGain"
+ "num_codes <= NUM_CODE_LENGTH_CODES"
+ "palette.c"
+ "readerForBytesImp"
+ "unexpected tileHeight: %d\n"
+ "unexpected tileSize: %ll  d\n"
+ "unexpected tileWidth: %d\n"
+ "virtual OSStatus LibJPEGReadPlugin::decodeImageImp(IIODecodeParameter *, IIOImageType, IOSurfaceRef *, CVPixelBufferRef *, CGImageBlockSetRef *)"
+ "xdr::convert_HLG_YCC_to_EDR_RGB"
+ "••• %s EnableRestrictedDecoding  | %s:%d\n"
+ "••• %s UseHardwareAcceleration  | %s:%d\n"
+ "••• CGImageSourceDisableCaching - caching is disabled for this process\n"
+ "••• CGImageSourceDisableHardwareDecoding - JPEG/HEIF hardware decoder will no longer be used in this process\n"
+ "••• CGImageSourceDisableRAWDecoding - RAW formats will no longer be handled in this process\n"
+ "••• CGImageSourceEnableRestrictedDecoding - restricted decoding (no IOSurface,...) is enabled for this process\n"
+ "••• CGImageSourceSetAllowableTypes: limiting to %ld types\n"
+ "••• Ⓜ️  CGImageSourceDisableMetadataParsing - image metadata will no longer be handled in this process\n"
+ "••• Ⓜ️  kCGImageSourceSkipMetadata --> handle minimum metadata only\n"
+ "••• Ⓜ️  kCGImageSourceSkipXMPMetadata --> skipping XMP+IPTC\n"
+ "••• Ⓜ️  skipping metdata for thumbnail creation\n"
+ "••• ✅ EnableRestrictedDecoding  | %s:%d\n"
+ "••• ✅ Process-EnableRestrictedDecoding  | %s:%d\n"
+ "••• ✅ UseHardwareAcceleration  | %s:%d\n"
+ "••• ❌ EnableRestrictedDecoding  | %s:%d\n"
+ "••• ❌ Process-UseHardwareAcceleration  | %s:%d\n"
+ "••• ❌ UseHardwareAcceleration  | %s:%d\n"
+ "••• ❓ EnableRestrictedDecoding  | %s:%d\n"
+ "••• ❓ UseHardwareAcceleration  | %s:%d\n"
+ "☀️  Invalid Meteor+ makernote data (hdrGain=%s, gainMapValue=%s)"
+ "☀️  Metor+ headroom: %f (hdrGain=%f, gainMapValue=%f)"
+ "☀️  Missing makernote data, using fallback hdrGain=%f\n"
+ "☀️  Missing makernote data: %s, no fallback provided"
+ "✅"
+ "❌"
+ "➡️ XPC_READPLUGIN_UPDATE_ALLOWED_TYPES [%lld]\n"
+ "➡️ XPC_READPLUGIN_UPDATE_PERMISSIONS [%lld]\n"
+ "⬅️ XPC_READPLUGIN_UPDATE_ALLOWED_TYPES [%lld]\n"
+ "⬅️ XPC_READPLUGIN_UPDATE_PERMISSIONS [%lld]\n"
- "    %s : %p [???]\n"
- "    %s : %p [array]\n"
- "    %s : %p [connection]\n"
- "    %s : %p [data]\n"
- "    %s : %p [date]\n"
- "    %s : %p [dictionary]\n"
- "    %s : %p [endpoint]\n"
- "    %s : %p [error]\n"
- "    %s : %p [fd]\n"
- "    %s : %p [null]\n"
- "    %s : %p [shmem]\n"
- "    %s : %p [uuid]\n"
- "    %s : '%d' [bool]\n"
- "    %s : '%g' [double]\n"
- "    %s : '%lld' [int64]\n"
- "    %s : '%lld' [uint64]\n"
- "    %s : '%s' [string]\n"
- "(branch_min[1-step_parity] >= -work_L) && (branch_max[1-step_parity] <= work_L)"
- "*** ImageIO: HW decoding disabled for this process\n"
- "*** ImageIO: RAW decoding disabled for this process\n"
- "*** ImageIO: Restricted decoding enabled for this process\n"
- "*** ImageIO: image caching disabled for this process\n"
- "+[_IIOXPCXDRImage getGainMapHeadroom:fromProperties:]"
- "B24@?0r*8^v16"
- "IIODisableCaching_block_invoke"
- "IIODisableHardwareDecoding_block_invoke"
- "IIODisableRAWDecoding_block_invoke"
- "IIOEnableRestrictedDecoding_block_invoke"
- "Invalid Meteor+ makernote data (hdrGain=%s, gainMapValue=%s)"
- "Metor+ headroom: %f (hdrGain=%f, gainMapValue=%f)"
- "Missing makernote data: %s"
- "WebPGetColorPalette"
- "create xpc service connection\n"
- "setupGeometry"
- "unexpected bitsPerPixel\n"
- "xdr::convert_HLG_420_to_EDR_RGB"
- "➡️ XPC_READPLUGIN_DECODE_FRAMES [%lld]\n"
- "➡️ unknown-messageID: %lld [%lld]\n"

```
