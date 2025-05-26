## ImageIOXPCService

> `/System/Library/Frameworks/ImageIO.framework/XPCServices/ImageIOXPCService.xpc/ImageIOXPCService`

```diff

-2488.1.11.0.0
-  __TEXT.__text: 0x415220
-  __TEXT.__auth_stubs: 0x41f0
-  __TEXT.__objc_stubs: 0xf60
+2488.4.15.0.0
+  __TEXT.__text: 0x416048
+  __TEXT.__auth_stubs: 0x4290
+  __TEXT.__objc_stubs: 0xfe0
   __TEXT.__objc_methlist: 0x310
-  __TEXT.__gcc_except_tab: 0x1f52c
-  __TEXT.__const: 0x2a760
-  __TEXT.__cstring: 0x76f5e
-  __TEXT.__objc_methname: 0x1242
+  __TEXT.__gcc_except_tab: 0x1f534
+  __TEXT.__const: 0x2a770
+  __TEXT.__cstring: 0x7769e
+  __TEXT.__objc_methname: 0x1272
   __TEXT.__objc_classname: 0x3f
   __TEXT.__objc_methtype: 0x5f1
-  __TEXT.__oslogstring: 0x1ef
+  __TEXT.__oslogstring: 0x1ee
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xec44
+  __TEXT.__unwind_info: 0xecb4
   __TEXT.__eh_frame: 0x1068
-  __DATA_CONST.__auth_got: 0x2110
-  __DATA_CONST.__got: 0x5c0
+  __DATA_CONST.__auth_got: 0x2160
+  __DATA_CONST.__got: 0x640
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x71560
-  __DATA_CONST.__cfstring: 0xbea0
+  __DATA_CONST.__const: 0x71628
+  __DATA_CONST.__cfstring: 0xbf40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x950
-  __DATA.__objc_selrefs: 0x460
-  __DATA.__objc_classrefs: 0x78
+  __DATA.__objc_selrefs: 0x480
+  __DATA.__objc_classrefs: 0x80
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x3200
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x11708
+  __DATA.__bss: 0x11728
   __DATA.__common: 0x29bc
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 16073
-  Symbols:   10704
-  CStrings:  12486
+  Functions: 16105
+  Symbols:   10761
+  CStrings:  12562
 
Symbols:
+ _CFBundleCreate
+ _CFBundleIsExecutableLoaded
+ _CGImageMetadataCreateFromXPCObj
+ _CGImageMetadataCreateXPCObj
+ _IIOAppIsUsingAppKitUIKit
+ _NSLog
+ _OBJC_CLASS_$_NSURL
+ __ImageIO_AccreditMemory
+ __Z15IIOImageTypeStr12IIOImageType
+ __ZN10IIO_Reader10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN12HEIFAuxImage25auxiliaryAlphaPixelFormatEv
+ __ZN12IIOImagePlus11createImageEP13CGImageSourcePi
+ __ZN12IIOXPCClient12debugMessageEPvPKci
+ __ZN12IIOXPCClient12replyIsValidEPv
+ __ZN12IIOXPCClient15runningOnServerEv
+ __ZN12IIOXPCClient18wakeup_xpc_serviceEv
+ __ZN13IIOReadPlugin13getPropertiesEv
+ __ZN13IIOReadPlugin22validateReadPluginDataEv
+ __ZN13IIO_Reader_AI10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN13IIO_Reader_BC10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIOImageSource18createImageAtIndexEmP13IIODictionaryPi
+ __ZN14IIOImageSource22createThumbnailAtIndexEmP13IIODictionaryPi
+ __ZN14IIO_Reader_ATX10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_BMP10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_CUR10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_DDS10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_ETC10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_GIF10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_ICO10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_JP210testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_KTX10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_MPO10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_PBM10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_PDF10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_PNG10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_PSD10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_PVR10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_RAD10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_TGA10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_XBM10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN15IIO_Reader_ASTC10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN15IIO_Reader_HEIF10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN15IIO_Reader_ICNS10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN15IIO_Reader_KTX210testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN15IIO_Reader_TIFF10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN15IIO_Reader_WebP10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN17IIO_ReaderHandler11typeForDataEPK8__CFDataPK10__CFString16IIOHeaderOptionsPb
+ __ZN17IIO_ReaderHandler11typeFromURLEPK7__CFURLPK10__CFString16IIOHeaderOptions
+ __ZN17IIO_ReaderHandler12typeForBytesEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN17IIO_ReaderHandler14readerForBytesEPKhmPK10__CFStringm16IIOHeaderOptions10IIORequestPi
+ __ZN17IIO_ReaderHandler16typeForImageReadEP12IIOImageReadPK10__CFString16IIOHeaderOptionsPb
+ __ZN17IIO_ReaderHandler17readerForBytesImpEPKhmPK10__CFStringm16IIOHeaderOptions10IIORequestPi
+ __ZN17IIO_ReaderHandler18typeFromDataAtPathEPK10__CFStringS2_16IIOHeaderOptions
+ __ZN17IIO_ReaderHandler19typeForDataProviderEP14CGDataProviderPK10__CFString16IIOHeaderOptionsPb
+ __ZN18IIO_Reader_LibJPEG10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN18IIO_Reader_OpenEXR10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN19IIOReader_RawCamera10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN20IIO_Reader_AppleJPEG10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZNSt3__19to_stringEm
+ ___cxa_guard_abort
+ __dispatch_queue_attr_concurrent
+ __xpc_type_array
+ __xpc_type_bool
+ __xpc_type_connection
+ __xpc_type_data
+ __xpc_type_date
+ __xpc_type_double
+ __xpc_type_endpoint
+ __xpc_type_fd
+ __xpc_type_int64
+ __xpc_type_mach_send
+ __xpc_type_null
+ __xpc_type_shmem
+ __xpc_type_string
+ __xpc_type_uint64
+ __xpc_type_uuid
+ _gIIO_kCMPhotoDecompressionContainerDescription_AuxiliaryNativePixelFormat
+ _iio_xpc_add_callback_dict
+ _iio_xpc_add_message_dict
+ _iio_xpc_add_permission_dict
+ _iio_xpc_add_plugin_dict
+ _iio_xpc_add_source_dict
+ _iio_xpc_add_xpcObj_from_CGRect
+ _iio_xpc_add_xpcObj_from_CGSize
+ _iio_xpc_dictionary_addCGRect
+ _iio_xpc_dictionary_addCGSize
+ _iio_xpc_dictionary_add_CFArray
+ _iio_xpc_dictionary_add_CFData
+ _iio_xpc_dictionary_add_CFDictionary
+ _iio_xpc_dictionary_add_GlobalInfo
+ _iio_xpc_dictionary_add_databuffer
+ _iio_xpc_dictionary_copy_CFDictionary
+ _iio_xpc_dictionary_get_CGRect
+ _iio_xpc_dictionary_get_CGSize
+ _iio_xpc_dictionary_get_GlobalInfo
+ _iio_xpc_dictionary_get_error_code
+ _iio_xpc_dictionary_set_error_code
+ _iio_xpc_get_CGRect_from_xpcObj
+ _iio_xpc_get_CGSize_from_xpcObj
+ _iio_xpc_get_callback_dict
+ _iio_xpc_get_message_dict
+ _iio_xpc_get_permission_dict
+ _iio_xpc_get_plugin_dict
+ _iio_xpc_get_source_dict
+ _kIIONewPluginDataOffset
+ _kIIONewPluginDataSize
+ _kIIONewPluginExpectedHeight
+ _kIIONewPluginExpectedWidth
+ _kIIONewPluginOSType
+ _xpc_bool_get_value
+ _xpc_connection_send_message_with_reply
+ _xpc_data_get_length
+ _xpc_dictionary_apply
+ _xpc_dictionary_get_count
+ _xpc_dictionary_get_double
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_double
+ _xpc_double_get_value
+ _xpc_int64_get_value
+ _xpc_string_get_string_ptr
+ _xpc_uint64_get_value
- _CGContextSelectFont
- _CGContextSetBlendMode
- _CGContextSetTextDrawingMode
- _CGContextShowTextAtPoint
- _CGImageBlockGetBitmapInfo
- __ZN10IIO_Reader10testHeaderEPKhmPK10__CFString
- __ZN12IIOImagePlus11createImageEP13CGImageSource
- __ZN13GIFReadPlugin28CallDecodeIndexedColorFramesEP10IIO_ReaderP12IIOImageReadP13GlobalGIFInfo14ReadPluginData13GIFPluginDataRNSt3__16vectorI20IIODecodeFrameParamsNS8_9allocatorISA_EEEE
- __ZN13IIO_Reader_AI10testHeaderEPKhmPK10__CFString
- __ZN13IIO_Reader_BC10testHeaderEPKhmPK10__CFString
- __ZN13PNGReadPlugin26CallDecodeUncomposedFramesEP12IIOImageReadP13GlobalPNGInfoRK14ReadPluginDataRK13PNGPluginDataRNSt3__16vectorI20IIODecodeFrameParamsNSA_9allocatorISC_EEEE
- __ZN13PSDPluginData22initWithSerializedDataEPK8__CFData
- __ZN13PSDPluginDataC1EPK8__CFData
- __ZN13PSDPluginDataC1ERKS_
- __ZN13PSDPluginDataC1Ev
- __ZN13PSDPluginDataC2EPK8__CFData
- __ZN13PSDPluginDataC2ERKS_
- __ZN13PSDPluginDataC2Ev
- __ZN13PSDPluginDataD1Ev
- __ZN13PSDPluginDataD2Ev
- __ZN13PSDPluginDataaSERKS_
- __ZN14IIOImageSource18createImageAtIndexEmP13IIODictionary
- __ZN14IIOImageSource22createThumbnailAtIndexEmP13IIODictionary
- __ZN14IIO_Reader_ATX10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_BMP10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_CUR10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_DDS10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_ETC10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_GIF10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_ICO10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_JP210testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_KTX10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_MPO10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_PBM10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_PDF10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_PNG10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_PSD10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_PVR10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_RAD10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_TGA10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_XBM10testHeaderEPKhmPK10__CFString
- __ZN15IIO_Reader_ASTC10testHeaderEPKhmPK10__CFString
- __ZN15IIO_Reader_HEIF10testHeaderEPKhmPK10__CFString
- __ZN15IIO_Reader_ICNS10testHeaderEPKhmPK10__CFString
- __ZN15IIO_Reader_KTX210testHeaderEPKhmPK10__CFString
- __ZN15IIO_Reader_TIFF10testHeaderEPKhmPK10__CFString
- __ZN15IIO_Reader_WebP10testHeaderEPKhmPK10__CFString
- __ZN17IIO_ReaderHandler11typeForDataEPK8__CFDataPK10__CFStringbPb
- __ZN17IIO_ReaderHandler11typeFromURLEPK7__CFURLPK10__CFStringb
- __ZN17IIO_ReaderHandler12typeForBytesEPKhmPK10__CFStringb
- __ZN17IIO_ReaderHandler14readerForBytesEPKhmPK10__CFStringmbb10IIORequestPi
- __ZN17IIO_ReaderHandler16typeForImageReadEP12IIOImageReadPK10__CFStringbPb
- __ZN17IIO_ReaderHandler17readerForBytesImpEPKhmPK10__CFStringmbb10IIORequestPi
- __ZN17IIO_ReaderHandler18typeFromDataAtPathEPK10__CFStringS2_bb
- __ZN17IIO_ReaderHandler19typeForDataProviderEP14CGDataProviderPK10__CFStringbPb
- __ZN18IIO_Reader_LibJPEG10testHeaderEPKhmPK10__CFString
- __ZN18IIO_Reader_OpenEXR10testHeaderEPKhmPK10__CFString
- __ZN19IIOReader_RawCamera10testHeaderEPKhmPK10__CFString
- __ZN20IIO_Reader_AppleJPEG10testHeaderEPKhmPK10__CFString
- __ZNK13PSDPluginData20createSerializedDataEv
- _addDataToDictionary
- _gLogXPC
- _xpc_array_create
- _xpc_data_create
CStrings:
+ "               isProxy: %d"
+ "             isFileURL: %d"
+ "    %*s%s : %d [bool]\n"
+ "    %*s%s : %g [double]\n"
+ "    %*s%s : %lld (%s) [uint64]\n"
+ "    %*s%s : %lld [int64]\n"
+ "    %*s%s : %lld [uint64]\n"
+ "    %*s%s : %p [???]\n"
+ "    %*s%s : %p [MACH]\n"
+ "    %*s%s : %p [array] - %d item(s)\n"
+ "    %*s%s : %p [connection]\n"
+ "    %*s%s : %p [data] - %ld bytes\n"
+ "    %*s%s : %p [date]\n"
+ "    %*s%s : %p [endpoint]\n"
+ "    %*s%s : %p [error]\n"
+ "    %*s%s : %p [fd]\n"
+ "    %*s%s : %p [null]\n"
+ "    %*s%s : %p [shmem]\n"
+ "    %*s%s : %p [uuid]\n"
+ "    %*s%s : '%c%c%c%c' [int64]\n"
+ "    %*s%s : '%c%c%c%c' [uint64]\n"
+ "    %*s%s : '%d' [int64]\n"
+ "    %*s%s : '%s' [string]\n"
+ "    %*s%s : [dictionary] - %d items\n"
+ "    %*s%s : [dictionary] - {%g,%g,%g,%g}\n"
+ "    %*s%s : [dictionary] - {%g,%g}\n"
+ "    changed pluin from '%c%c%c%c' to '%c%c%c%c'\n"
+ "    isFileReferenceURL: %d"
+ "!dec->incremental_ || (br->eos_ && src < src_last) || src >= src_last"
+ "%{public}s"
+ "*** ERROR: CGImageSourceCreateImageAtIndex[%ld] - '%c%c%c%c' - failed to create image [%d]\n"
+ "*** ERROR: CGImageSourceCreateThumbnailAtIndex[%ld] - '%c%c%c%c' - failed to create thumbnail (no options) [%d]\n"
+ "*** ERROR: CGImageSourceCreateThumbnailAtIndex[%ld] - '%c%c%c%c' - failed to create thumbnail [%d]\n"
+ "*** ERROR: IIOImageReadSession::getBytes: _iRead is NULL\n"
+ "*** ERROR: IIOImageReadSession::getBytesAtOffset: _iRead is NULL\n"
+ "*** ERROR: PNG decode  %dx%d  bpc: %d  cs: %d\n"
+ "*** ERROR: PNG decode failed ('png' is NULL)\n"
+ "*** ERROR: TIFFReadTileWithSize failed\n"
+ "*** ERROR: cannot get data from '%@'"
+ "*** ERROR: failed to load 'IMAGEIO_PLUGIN_DATA_TIFF'\n"
+ "*** ERROR: failed to read ColorMap - expected %d bytes, got %d\n"
+ "*** ERROR: handleColorSpace failed (%d)\n"
+ "*** ERROR: imageType '%d' not handled\n"
+ "*** ERROR: sanityCheck failed (%d)\n"
+ "*** JPEG with aux-image + 'fail-for-non-matching-hint are not compatible' - ignoring aux-image\n"
+ "*** _bc._ktxTexture is NULL\n"
+ "*** _pvr._ktxTexture is NULL\n"
+ "*** could not find a reader for: '%s'\n"
+ "*** data mismatch?\n"
+ "*** initDataSize: %8ld    sizeof(ReadPluginInitData): %8ld\n"
+ "*** running on server - [%s will run in-process]\n"
+ "*** updateTiffStruct failed (%d)\n"
+ "/System/Library/Frameworks/UIKit.framework"
+ ":   bad APP2 MPEntry offset: '%ld'   fileSize: '%ld'\n"
+ ":   bad APP2 entry count: '%ld'   APP2 length: '%ld'\n"
+ ":   bad APP2 offset: '%ld'   APP2 length: '%ld'    fileSize: '%ld'\n"
+ "B24@?0r*8^v16"
+ "IIOColorMap"
+ "ImageBlockSet"
+ "ImageIOXPCService"
+ "NEW_PLUGIN_dataOffset"
+ "NEW_PLUGIN_dataSize"
+ "NEW_PLUGIN_expectedHeight"
+ "NEW_PLUGIN_expectedWidth"
+ "NEW_PLUGIN_ostype"
+ "PixelBuffer"
+ "ReadHuffmanCodes"
+ "Unexpected kdu_resolution."
+ "VP8SetError"
+ "_cgrect"
+ "_cgsize"
+ "_ostype"
+ "abcdefghijklmnopqrstuvwxyz0123456789_"
+ "com.apple.iio.queue"
+ "createImageBlockSetFromXPCObject"
+ "dec->hdr_.huffman_tables_.root.start != NULL"
+ "dec->incremental_ || error != VP8_STATUS_SUSPENDED"
+ "decodeImageDataPVR"
+ "event_queue != NULL"
+ "fileURLWithPath:"
+ "huffman_tables->curr_segment == NULL"
+ "huffman_tables->root.start == NULL"
+ "iio_xpc_"
+ "iio_xpc_cb"
+ "iio_xpc_cb_block_cgrect"
+ "iio_xpc_cb_block_rowbytes"
+ "iio_xpc_cb_blockset"
+ "iio_xpc_cb_blockset_cgrect"
+ "iio_xpc_cb_blockset_dest_cgsize"
+ "iio_xpc_cb_blockset_options"
+ "iio_xpc_cb_decode_image_buffer"
+ "iio_xpc_cb_decode_image_buffer_size"
+ "iio_xpc_cb_decode_iosurface"
+ "iio_xpc_message_id"
+ "iio_xpc_metadata_maker"
+ "iio_xpc_metadata_mutable"
+ "iio_xpc_metadata_obj"
+ "iio_xpc_msg"
+ "iio_xpc_msg_call_counts"
+ "iio_xpc_msg_call_options"
+ "iio_xpc_msg_error"
+ "iio_xpc_msg_wakeup_time"
+ "iio_xpc_permission"
+ "iio_xpc_permission_allowed_types_array"
+ "iio_xpc_permission_data"
+ "iio_xpc_plugin"
+ "iio_xpc_plugin_data"
+ "iio_xpc_plugin_data_applejpeg"
+ "iio_xpc_plugin_data_astc"
+ "iio_xpc_plugin_data_astc_imp"
+ "iio_xpc_plugin_data_atx"
+ "iio_xpc_plugin_data_bc"
+ "iio_xpc_plugin_data_bc_imp"
+ "iio_xpc_plugin_data_bmp"
+ "iio_xpc_plugin_data_common_astc"
+ "iio_xpc_plugin_data_dds"
+ "iio_xpc_plugin_data_etc"
+ "iio_xpc_plugin_data_etc_imp"
+ "iio_xpc_plugin_data_exr"
+ "iio_xpc_plugin_data_gif"
+ "iio_xpc_plugin_data_heif"
+ "iio_xpc_plugin_data_icns"
+ "iio_xpc_plugin_data_ico"
+ "iio_xpc_plugin_data_jp2"
+ "iio_xpc_plugin_data_jpeg"
+ "iio_xpc_plugin_data_ktx"
+ "iio_xpc_plugin_data_libjpeg"
+ "iio_xpc_plugin_data_mpo"
+ "iio_xpc_plugin_data_pbm"
+ "iio_xpc_plugin_data_pdf"
+ "iio_xpc_plugin_data_png"
+ "iio_xpc_plugin_data_png_idot"
+ "iio_xpc_plugin_data_psd"
+ "iio_xpc_plugin_data_psd_layer"
+ "iio_xpc_plugin_data_pvr"
+ "iio_xpc_plugin_data_rad"
+ "iio_xpc_plugin_data_tga"
+ "iio_xpc_plugin_data_tiff"
+ "iio_xpc_plugin_data_webp"
+ "iio_xpc_plugin_data_xbm"
+ "iio_xpc_plugin_global_info"
+ "iio_xpc_plugin_global_info_data"
+ "iio_xpc_plugin_global_info_data_size"
+ "iio_xpc_plugin_global_info_ostype"
+ "iio_xpc_plugin_header_infoptr"
+ "iio_xpc_plugin_init_data"
+ "iio_xpc_plugin_init_metadata"
+ "iio_xpc_plugin_init_properties"
+ "iio_xpc_plugin_type_changed"
+ "iio_xpc_src"
+ "iio_xpc_src_data"
+ "iio_xpc_src_file_size"
+ "iio_xpc_src_header_data"
+ "iio_xpc_src_header_options"
+ "iio_xpc_src_hint_string"
+ "iio_xpc_src_image_count"
+ "iio_xpc_src_image_index"
+ "iio_xpc_src_image_type"
+ "iio_xpc_src_options"
+ "iio_xpc_src_ostype"
+ "iio_xpc_src_properties"
+ "iio_xpc_src_shmem"
+ "iio_xpc_src_shmem_size"
+ "iio_xpc_src_status"
+ "iio_xpc_src_utitype"
+ "iio_xpc_transacion_id"
+ "isFileReferenceURL"
+ "isFileURL"
+ "kCMPhotoDecompressionContainerDescription_AuxiliaryNativePixelFormat"
+ "loadDataFromXPCObject"
+ "origin_x"
+ "origin_y"
+ "setImageMedadataAtIndex index (%d) larger than arrayCount (%d) and image count (%d)\n"
+ "setImagePlusAtIndex index (%d) larger than arrayCount (%d) and image count (%d)\n"
+ "size_height"
+ "size_width"
+ "testHeader"
+ "wakeup_xpc_service_block_invoke"
+ "xpc_shmem_map"
+ "••• Ⓜ️  skipping metadata for thumbnail creation\n"
+ "☀️  Meteor+ headroom: %f (hdrGain=%f, gainMapValue=%f)"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_COPYBLOCKSET corrupt XPC reply: %d\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_COPYIOSURFACE corrupt XPC reply: %d\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_DECODE_IMAGE corrupt XPC reply: %d\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_DECODE_IMAGE error: %d\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_IMAGECOUNT corrupt XPC reply: %d\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_INITIMAGE corrupt XPC reply: %d\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_INITIMAGE error: %d  (IMAGEIO_PLUGIN_REPLY: %p)\n"
+ "❌ ImageIOXPC: XPC_READPLUGIN_IMAGECOUNT error null-reply\n"
+ "❌ ImageIOXPC: XPC_READPLUGIN_INITIMAGE error null-reply\n"
+ "➡️ XPC_READPLUGIN_WAKEUP [%lld]\n"
+ "⬅️ XPC_READPLUGIN_WAKEUP [%lld]\n"
+ "🔺 bad width/height:  w: %d   h: %d\n"
- "    '%c%c%c%c' BLOCK (%d/%d) *** %p {%g, %g, %g, %g} rb: %ld  [%ld bytes]\n"
- "    '%c%c%c%c' BLOCK *** blockSet:%p   count: %d\n"
- "%{public}s\n"
- "*** ERROR: CGImageSourceCreateImageAtIndex[%ld] - '%c%c%c%c' - failed to create image\n"
- "*** ERROR: CGImageSourceCreateThumbnailAtIndex[%ld] - '%c%c%c%c' - failed to create thumbnail\n"
- "*** ERROR: CGImageSourceCreateThumbnailAtIndex[%ld] - '%c%c%c%c' - failed to create thumbnail (no options)\n"
- "*** ERROR: MPEntry out of bounds\n"
- "*** ERROR: PNG decode  %dx%d  bpc: %d  cs: %d"
- "*** ERROR: blockSet-pixelSize: %d  block-pixelSize: %d\n"
- "*** ERROR: rowBytes <= 0 - skipping layer decoding\n"
- "*** dDebugBlockSet - cannot add text to imageBlockSet\n"
- ": _mpEntryCount > _markerLength (%ld > %ld)\n"
- "Helvetica"
- "ImageIOXPCAllowedTypesArray"
- "ImageIOXPCBlockRect"
- "ImageIOXPCBlockRowBytes"
- "ImageIOXPCBlockSet"
- "ImageIOXPCCallCounts"
- "ImageIOXPCCallOptions"
- "ImageIOXPCCopyBlockSetDestSize"
- "ImageIOXPCCopyBlockSetOptions"
- "ImageIOXPCCopyBlockSetRect"
- "ImageIOXPCDecodeFrames_FrameIndex"
- "ImageIOXPCDecodeFrames_FrameRect"
- "ImageIOXPCDecodeFrames_ParamsArray"
- "ImageIOXPCDecodedIOSurface"
- "ImageIOXPCDecodedImageBuffer"
- "ImageIOXPCDecodedImageBufferRowBytes"
- "ImageIOXPCDecodedImageBufferSize"
- "ImageIOXPCErrorCode"
- "ImageIOXPCFailIfNotMatchingHint"
- "ImageIOXPCFileSize"
- "ImageIOXPCHeaderData"
- "ImageIOXPCHintString"
- "ImageIOXPCImageCount"
- "ImageIOXPCImageIndex"
- "ImageIOXPCImageSourceOSType"
- "ImageIOXPCImageSourceUTIType"
- "ImageIOXPCImageType"
- "ImageIOXPCIncrementalLoading"
- "ImageIOXPCMessageID"
- "ImageIOXPCPermissionData"
- "ImageIOXPCReadPluginHeaderInfoPtr"
- "ImageIOXPCReadPluginInitMetadata"
- "ImageIOXPCReadPluginInitProperties"
- "ImageIOXPCReadPluginTypeChanged"
- "ImageIOXPCReadPlugin_Data"
- "ImageIOXPCReadPlugin_Data_ASTC"
- "ImageIOXPCReadPlugin_Data_ASTC_IMP"
- "ImageIOXPCReadPlugin_Data_ATX"
- "ImageIOXPCReadPlugin_Data_AppleJPEG"
- "ImageIOXPCReadPlugin_Data_BC"
- "ImageIOXPCReadPlugin_Data_BC_IMP"
- "ImageIOXPCReadPlugin_Data_BMP"
- "ImageIOXPCReadPlugin_Data_CommonASTC"
- "ImageIOXPCReadPlugin_Data_DDS"
- "ImageIOXPCReadPlugin_Data_ETC"
- "ImageIOXPCReadPlugin_Data_ETC_IMP"
- "ImageIOXPCReadPlugin_Data_EXR"
- "ImageIOXPCReadPlugin_Data_GIF"
- "ImageIOXPCReadPlugin_Data_GIF_colormap"
- "ImageIOXPCReadPlugin_Data_HEIF"
- "ImageIOXPCReadPlugin_Data_ICNS"
- "ImageIOXPCReadPlugin_Data_ICO"
- "ImageIOXPCReadPlugin_Data_JP2"
- "ImageIOXPCReadPlugin_Data_JPEG"
- "ImageIOXPCReadPlugin_Data_KTX"
- "ImageIOXPCReadPlugin_Data_LibJPEG"
- "ImageIOXPCReadPlugin_Data_MPO"
- "ImageIOXPCReadPlugin_Data_PBM"
- "ImageIOXPCReadPlugin_Data_PDF"
- "ImageIOXPCReadPlugin_Data_PNG"
- "ImageIOXPCReadPlugin_Data_PNG_iDOT"
- "ImageIOXPCReadPlugin_Data_PSD"
- "ImageIOXPCReadPlugin_Data_PVR"
- "ImageIOXPCReadPlugin_Data_RAD"
- "ImageIOXPCReadPlugin_Data_TGA"
- "ImageIOXPCReadPlugin_Data_TIFF"
- "ImageIOXPCReadPlugin_Data_WEBP"
- "ImageIOXPCReadPlugin_Data_XBM"
- "ImageIOXPCReadPlugin_GlobalInfo"
- "ImageIOXPCReadPlugin_InitData"
- "ImageIOXPCSourceData"
- "ImageIOXPCSourceOptions"
- "ImageIOXPCSourceProperties"
- "ImageIOXPCSourceShMem"
- "ImageIOXPCSourceShMemSize"
- "ImageIOXPCStatus"
- "ImageIOXPCTransacionID"
- "ImageOPXPCDecodeFrames_FrameRowsRead"
- "ImageOPXPCDecodeFrames_FrameStatus"
- "NEW_PLUGIN_EXPECTED_HEIGHT"
- "NEW_PLUGIN_EXPECTED_WIDTH"
- "NEW_PLUGIN_TYPE"
- "NEW_PLUGIN_TYPE_OFFSET"
- "NEW_PLUGIN_TYPE_SIZE"
- "RestoreState"
- "XPC_READPLUGIN_DECODE_FRAMES"
- "data mismatch?\n"
- "dec->br_.eos_"
- "dec->hdr_.huffman_tables_ != NULL"
- "initDataSize: %8ld    sizeof(ReadPluginInitData): %8ld\n"
- "setImageMedadataAtIndex index (%d) larger than arrayCount (%d) and image count (%d\n"
- "setImagePlusAtIndex index (%d) larger than arrayCount (%d) and image count (%d\n"
- "••• Ⓜ️  skipping metdata for thumbnail creation\n"
- "☀️  Metor+ headroom: %f (hdrGain=%f, gainMapValue=%f)"
- "✅ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_DECODE_FRAMES: OK\n"
- "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_DECODE_FRAMES error: %lld\n"
- "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_DECODE_IMAGE error: %lld\n"
- "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_INITIMAGE error: %lld\n"
- "❌ ImageIOXPC: XPC_READPLUGIN_DECODE_FRAMES error\n"
- "❌ ImageIOXPC: XPC_READPLUGIN_DECODE_FRAMES malformed reply\n"
- "❌ ImageIOXPC: XPC_READPLUGIN_INITIMAGE error (null-reply)\n"
- "❌ ImageIOXPC:: XPC_READPLUGIN_DECODE_FRAMES error\n"
- "❌ ImageIOXPC:: XPC_READPLUGIN_DECODE_FRAMES malformed reply\n"
- "⭕️ ImageIOXPC: OOP-request was made, but we're decoding in-process (GIF-XPC_READPLUGIN_DECODE_FRAMES)...\n"
- "⭕️ ImageIOXPC: OOP-request was made, but we're decoding in-process (PNG-XPC_READPLUGIN_DECODE_FRAMES)...\n"

```
