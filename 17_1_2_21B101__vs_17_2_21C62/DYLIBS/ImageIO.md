## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2488.1.11.0.0
-  __TEXT.__text: 0x3b6818
+2488.4.15.0.0
+  __TEXT.__text: 0x3b6be4
   __TEXT.__auth_stubs: 0x3bd0
   __TEXT.__objc_methlist: 0x310
-  __TEXT.__gcc_except_tab: 0x1bc34
-  __TEXT.__const: 0x28968
-  __TEXT.__cstring: 0x6c539
-  __TEXT.__oslogstring: 0xc
+  __TEXT.__gcc_except_tab: 0x1bbd0
+  __TEXT.__const: 0x28978
+  __TEXT.__cstring: 0x6cbdc
+  __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xcdcc
+  __TEXT.__unwind_info: 0xce84
   __TEXT.__eh_frame: 0x460
   __TEXT.__objc_classname: 0x3c
-  __TEXT.__objc_methname: 0x1242
+  __TEXT.__objc_methname: 0x1260
   __TEXT.__objc_methtype: 0x5f1
-  __TEXT.__objc_stubs: 0xf60
-  __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x10be0
+  __TEXT.__objc_stubs: 0xfc0
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0x10c68
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x830
-  __DATA_CONST.__objc_selrefs: 0x460
-  __AUTH_CONST.__cfstring: 0xbbe0
+  __DATA_CONST.__objc_selrefs: 0x478
+  __AUTH_CONST.__cfstring: 0xbc60
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__const: 0x3d2e8
+  __AUTH_CONST.__const: 0x3d328
   __AUTH_CONST.__objc_const: 0x120
   __AUTH_CONST.__auth_ptr: 0x78
   __AUTH_CONST.__auth_got: 0x1e00
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x1d0
-  __DATA.__objc_classrefs: 0x78
+  __DATA.__objc_classrefs: 0x80
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x33b0
-  __DATA.__bss: 0x1020
-  __DATA.__common: 0x1a54
+  __DATA.__bss: 0x1030
+  __DATA.__common: 0x1a5c
   __DATA_DIRTY.__data: 0x1b8
   __DATA_DIRTY.__crash_info: 0x40
   __DATA_DIRTY.__common: 0xa78

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12959
-  Symbols:   32520
-  CStrings:  11159
+  Functions: 12991
+  Symbols:   32598
+  CStrings:  11216
 
Symbols:
+ _CGImageMetadataCreateFromXPCObj
+ _DecodeImageStream.cold.4
+ _DecodeImageStream.cold.5
+ _NSLog
+ _OBJC_CLASS_$_NSURL
+ _ReadHuffmanCodesHelper
+ _VP8LHuffmanTablesAllocate
+ _VP8LHuffmanTablesDeallocate
+ _VP8SetError.cold.1
+ __ImageIO_AccreditMemory
+ __ZN10IIO_Reader10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN12HEIFAuxImage25auxiliaryAlphaPixelFormatEv
+ __ZN12HEIFAuxImageC2EP14__CFReadStream
+ __ZN12IIOImagePlus11createImageEP13CGImageSourcePi
+ __ZN12IIOXPCClient12replyIsValidEPv
+ __ZN12IIOXPCClient16useServerForCallEP10IIO_Reader10IIORequest10IIO_XPC_IDb
+ __ZN13IIOReadPlugin22validateReadPluginDataEv
+ __ZN13IIO_Reader_AI10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN13IIO_Reader_BC10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN13PSDReadPluginD2Ev
+ __ZN14IIOImageSource18createImageAtIndexEmP13IIODictionaryPi
+ __ZN14IIOImageSource22createThumbnailAtIndexEmP13IIODictionaryPi
+ __ZN14IIO_Reader_ATX10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_BMP10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN14IIO_Reader_CUR10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
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
+ __ZN17IIO_ReaderHandler17readerForBytesImpEPKhmPK10__CFStringm16IIOHeaderOptions10IIORequestPi
+ __ZN17IIO_ReaderHandler18typeFromDataAtPathEPK10__CFStringS2_16IIOHeaderOptions
+ __ZN17IIO_ReaderHandler19typeForDataProviderEP14CGDataProviderPK10__CFString16IIOHeaderOptionsPb
+ __ZN18HEIFThumbnailImageC2EP14__CFReadStream
+ __ZN18IIO_Reader_LibJPEG10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN18IIO_Reader_OpenEXR10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN19IIOReader_RawCamera10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN20IIO_Reader_AppleJPEG10testHeaderEPKhmPK10__CFString16IIOHeaderOptions
+ __ZN7HEIFXMPC2EP14__CFReadStream
+ __ZN8HEIFExifC2EP14__CFReadStream
+ __ZN8HEIFItemC2EP14__CFReadStream
+ __ZN8_MPEntryC2EP14__CFReadStream
+ __ZNSt3__16vectorIP12HEIFAuxImageNS_9allocatorIS2_EEE7reserveEm
+ __ZNSt3__16vectorIP13HEIFMainImageNS_9allocatorIS2_EEE7reserveEm
+ __ZNSt3__16vectorIP18HEIFThumbnailImageNS_9allocatorIS2_EEE7reserveEm
+ __ZNSt3__16vectorIP7HEIFXMPNS_9allocatorIS2_EEE7reserveEm
+ __ZNSt3__16vectorIP8HEIFExifNS_9allocatorIS2_EEE7reserveEm
+ __ZNSt3__16vectorIP8HEIFItemNS_9allocatorIS2_EEE7reserveEm
+ __ZNSt3__16vectorIP8_MPEntryNS_9allocatorIS2_EEE7reserveEm
+ __ZZ9IIOXPCLogE6logXPC
+ __ZZ9IIOXPCLogE9onceToken
+ __ZZN12IIOImagePlus11createImageEP13CGImageSourcePiE6invert
+ ___IIOXPCLog_block_invoke
+ ____ZN12IIOXPCClient12replyIsValidEPv_block_invoke
+ ____ZN12IIOXPCClientC2Ev_block_invoke_2
+ ___block_descriptor_tmp.112
+ ___block_descriptor_tmp.115
+ ___block_descriptor_tmp.124
+ ___block_descriptor_tmp.125
+ ___block_descriptor_tmp.127
+ ___block_descriptor_tmp.130
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.135
+ ___block_descriptor_tmp.139
+ ___block_descriptor_tmp.143
+ ___block_descriptor_tmp.147
+ ___block_descriptor_tmp.152
+ ___block_descriptor_tmp.153
+ ___block_descriptor_tmp.156
+ ___block_descriptor_tmp.162
+ ___block_descriptor_tmp.165
+ ___block_descriptor_tmp.181
+ ___block_descriptor_tmp.189
+ ___block_descriptor_tmp.195
+ ___block_descriptor_tmp.200
+ ___block_descriptor_tmp.204
+ ___block_descriptor_tmp.210
+ ___block_descriptor_tmp.216
+ ___block_descriptor_tmp.221
+ ___block_descriptor_tmp.226
+ ___block_descriptor_tmp.239
+ ___block_descriptor_tmp.245
+ ___block_descriptor_tmp.252
+ ___block_descriptor_tmp.259
+ ___block_descriptor_tmp.266
+ ___block_descriptor_tmp.273
+ ___block_descriptor_tmp.278
+ ___block_descriptor_tmp.283
+ ___block_descriptor_tmp.288
+ ___block_descriptor_tmp.295
+ ___block_descriptor_tmp.299
+ ___block_descriptor_tmp.303
+ ___block_descriptor_tmp.321
+ ___block_descriptor_tmp.323
+ ___block_descriptor_tmp.325
+ ___block_descriptor_tmp.329
+ ___block_descriptor_tmp.332
+ ___block_descriptor_tmp.335
+ ___block_descriptor_tmp.338
+ ___block_descriptor_tmp.341
+ ___block_descriptor_tmp.344
+ ___block_descriptor_tmp.426
+ ___block_descriptor_tmp.80
+ ___block_descriptor_tmp.92
+ ___block_descriptor_tmp.94
+ ___block_literal_global.114
+ ___block_literal_global.117
+ ___block_literal_global.126
+ ___block_literal_global.129
+ ___block_literal_global.132
+ ___block_literal_global.135
+ ___block_literal_global.137
+ ___block_literal_global.141
+ ___block_literal_global.145
+ ___block_literal_global.149
+ ___block_literal_global.151
+ ___block_literal_global.154
+ ___block_literal_global.158
+ ___block_literal_global.160
+ ___block_literal_global.167
+ ___block_literal_global.172
+ ___block_literal_global.183
+ ___block_literal_global.191
+ ___block_literal_global.197
+ ___block_literal_global.202
+ ___block_literal_global.206
+ ___block_literal_global.212
+ ___block_literal_global.218
+ ___block_literal_global.223
+ ___block_literal_global.228
+ ___block_literal_global.241
+ ___block_literal_global.247
+ ___block_literal_global.254
+ ___block_literal_global.261
+ ___block_literal_global.268
+ ___block_literal_global.275
+ ___block_literal_global.280
+ ___block_literal_global.285
+ ___block_literal_global.290
+ ___block_literal_global.297
+ ___block_literal_global.301
+ ___block_literal_global.305
+ ___block_literal_global.323
+ ___block_literal_global.327
+ ___block_literal_global.331
+ ___block_literal_global.334
+ ___block_literal_global.337
+ ___block_literal_global.340
+ ___block_literal_global.343
+ ___block_literal_global.346
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
+ _iio_xpc_dictionary_get_GlobalInfo
+ _iio_xpc_dictionary_get_error_code
+ _iio_xpc_get_CGRect_from_xpcObj
+ _iio_xpc_get_callback_dict
+ _iio_xpc_get_message_dict
+ _iio_xpc_get_plugin_dict
+ _iio_xpc_get_source_dict
+ _kCFPreferencesCurrentHost
+ _kIIONewPluginDataOffset
+ _kIIONewPluginDataSize
+ _kIIONewPluginExpectedHeight
+ _kIIONewPluginExpectedWidth
+ _kIIONewPluginOSType
+ _objc_msgSend$isFileReferenceURL
+ _objc_msgSend$isFileURL
+ _objc_msgSend$isProxy
+ _strspn
+ _xpc_dictionary_apply
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_count
+ _xpc_dictionary_get_double
+ _xpc_dictionary_set_double
+ _xpc_dictionary_set_int64
- _CGContextSelectFont
- _CGContextSetBlendMode
- _CGContextSetTextDrawingMode
- _CGContextShowTextAtPoint
- _CGImageBlockGetBitmapInfo
- _ERROR_ImageIO_DataBufferIsNotBigEnough
- __ZN10IIO_Reader10testHeaderEPKhmPK10__CFString
- __ZN12IIOImagePlus11createImageEP13CGImageSource
- __ZN12IIOXPCClient33useServerForDecodeFramesAtIndexesEP10IIO_Reader10IIORequest
- __ZN13GIFReadPlugin28CallDecodeIndexedColorFramesEP10IIO_ReaderP12IIOImageReadP13GlobalGIFInfo14ReadPluginData13GIFPluginDataRNSt3__16vectorI20IIODecodeFrameParamsNS8_9allocatorISA_EEEE
- __ZN13IIO_Reader_AI10testHeaderEPKhmPK10__CFString
- __ZN13IIO_Reader_BC10testHeaderEPKhmPK10__CFString
- __ZN13PNGReadPlugin26CallDecodeUncomposedFramesEP12IIOImageReadP13GlobalPNGInfoRK14ReadPluginDataRK13PNGPluginDataRNSt3__16vectorI20IIODecodeFrameParamsNSA_9allocatorISC_EEEE
- __ZN13PSDPluginData22initWithSerializedDataEPK8__CFData
- __ZN14IIOImageSource18createImageAtIndexEmP13IIODictionary
- __ZN14IIOImageSource22createThumbnailAtIndexEmP13IIODictionary
- __ZN14IIO_Reader_ATX10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_BMP10testHeaderEPKhmPK10__CFString
- __ZN14IIO_Reader_CUR10testHeaderEPKhmPK10__CFString
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
- __ZN17IIO_ReaderHandler17readerForBytesImpEPKhmPK10__CFStringmbb10IIORequestPi
- __ZN17IIO_ReaderHandler18typeFromDataAtPathEPK10__CFStringS2_bb
- __ZN17IIO_ReaderHandler19typeForDataProviderEP14CGDataProviderPK10__CFStringbPb
- __ZN18IIO_Reader_LibJPEG10testHeaderEPKhmPK10__CFString
- __ZN18IIO_Reader_OpenEXR10testHeaderEPKhmPK10__CFString
- __ZN19IIOReader_RawCamera10testHeaderEPKhmPK10__CFString
- __ZN20IIO_Reader_AppleJPEG10testHeaderEPKhmPK10__CFString
- __ZNK13PSDPluginData20createSerializedDataEv
- __ZNSt3__16vectorIP12HEIFAuxImageNS_9allocatorIS2_EEE6resizeEm
- __ZNSt3__16vectorIP12HEIFAuxImageNS_9allocatorIS2_EEE8__appendEm
- __ZNSt3__16vectorIP18HEIFThumbnailImageNS_9allocatorIS2_EEE6resizeEm
- __ZNSt3__16vectorIP18HEIFThumbnailImageNS_9allocatorIS2_EEE8__appendEm
- __ZNSt3__16vectorIP7HEIFXMPNS_9allocatorIS2_EEE6resizeEm
- __ZNSt3__16vectorIP7HEIFXMPNS_9allocatorIS2_EEE8__appendEm
- __ZNSt3__16vectorIP8HEIFExifNS_9allocatorIS2_EEE6resizeEm
- __ZNSt3__16vectorIP8HEIFExifNS_9allocatorIS2_EEE8__appendEm
- __ZNSt3__16vectorIP8HEIFItemNS_9allocatorIS2_EEE6resizeEm
- __ZNSt3__16vectorIP8HEIFItemNS_9allocatorIS2_EEE8__appendEm
- __ZZN12IIOImagePlus11createImageEP13CGImageSourceE6invert
- ____ZN13GIFReadPlugin28CallDecodeIndexedColorFramesEP10IIO_ReaderP12IIOImageReadP13GlobalGIFInfo14ReadPluginData13GIFPluginDataRNSt3__16vectorI20IIODecodeFrameParamsNS8_9allocatorISA_EEEE_block_invoke
- ____ZN13JP2ReadPlugin19saveDataToXPCObjectEPv_block_invoke
- ____ZN13PNGReadPlugin26CallDecodeUncomposedFramesEP12IIOImageReadP13GlobalPNGInfoRK14ReadPluginDataRK13PNGPluginDataRNSt3__16vectorI20IIODecodeFrameParamsNSA_9allocatorISC_EEEE_block_invoke
- ___block_descriptor_tmp.111
- ___block_descriptor_tmp.118
- ___block_descriptor_tmp.123
- ___block_descriptor_tmp.126
- ___block_descriptor_tmp.129
- ___block_descriptor_tmp.132
- ___block_descriptor_tmp.134
- ___block_descriptor_tmp.138
- ___block_descriptor_tmp.140
- ___block_descriptor_tmp.144
- ___block_descriptor_tmp.146
- ___block_descriptor_tmp.148
- ___block_descriptor_tmp.154
- ___block_descriptor_tmp.160
- ___block_descriptor_tmp.163
- ___block_descriptor_tmp.173
- ___block_descriptor_tmp.180
- ___block_descriptor_tmp.184
- ___block_descriptor_tmp.188
- ___block_descriptor_tmp.194
- ___block_descriptor_tmp.199
- ___block_descriptor_tmp.203
- ___block_descriptor_tmp.209
- ___block_descriptor_tmp.215
- ___block_descriptor_tmp.220
- ___block_descriptor_tmp.225
- ___block_descriptor_tmp.229
- ___block_descriptor_tmp.238
- ___block_descriptor_tmp.244
- ___block_descriptor_tmp.251
- ___block_descriptor_tmp.258
- ___block_descriptor_tmp.272
- ___block_descriptor_tmp.277
- ___block_descriptor_tmp.282
- ___block_descriptor_tmp.287
- ___block_descriptor_tmp.294
- ___block_descriptor_tmp.298
- ___block_descriptor_tmp.302
- ___block_descriptor_tmp.315
- ___block_descriptor_tmp.320
- ___block_descriptor_tmp.324
- ___block_descriptor_tmp.328
- ___block_descriptor_tmp.331
- ___block_descriptor_tmp.334
- ___block_descriptor_tmp.337
- ___block_descriptor_tmp.340
- ___block_descriptor_tmp.343
- ___block_descriptor_tmp.423
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.81
- ___block_descriptor_tmp.91
- ___block_literal_global.113
- ___block_literal_global.120
- ___block_literal_global.125
- ___block_literal_global.128
- ___block_literal_global.131
- ___block_literal_global.134
- ___block_literal_global.140
- ___block_literal_global.142
- ___block_literal_global.146
- ___block_literal_global.148
- ___block_literal_global.150
- ___block_literal_global.156
- ___block_literal_global.159
- ___block_literal_global.162
- ___block_literal_global.165
- ___block_literal_global.171
- ___block_literal_global.175
- ___block_literal_global.182
- ___block_literal_global.190
- ___block_literal_global.196
- ___block_literal_global.201
- ___block_literal_global.205
- ___block_literal_global.211
- ___block_literal_global.217
- ___block_literal_global.222
- ___block_literal_global.227
- ___block_literal_global.231
- ___block_literal_global.240
- ___block_literal_global.246
- ___block_literal_global.253
- ___block_literal_global.260
- ___block_literal_global.274
- ___block_literal_global.279
- ___block_literal_global.284
- ___block_literal_global.289
- ___block_literal_global.296
- ___block_literal_global.300
- ___block_literal_global.304
- ___block_literal_global.322
- ___block_literal_global.326
- ___block_literal_global.330
- ___block_literal_global.333
- ___block_literal_global.336
- ___block_literal_global.339
- ___block_literal_global.342
- ___block_literal_global.345
- _addDataToDictionary
- _xpc_array_append_value
- _xpc_array_apply
- _xpc_array_create
- _xpc_dictionary_set_bool
CStrings:
+ "               isProxy: %d"
+ "             isFileURL: %d"
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
+ "*** running on server - [%s will run in-process]\n"
+ "*** updateTiffStruct failed (%d)\n"
+ ":   bad APP2 MPEntry offset: '%ld'   fileSize: '%ld'\n"
+ ":   bad APP2 entry count: '%ld'   APP2 length: '%ld'\n"
+ ":   bad APP2 offset: '%ld'   APP2 length: '%ld'    fileSize: '%ld'\n"
+ "B24@?0r*8^v16"
+ "IIOColorMap"
+ "ImageIOXPCService"
+ "NEW_PLUGIN_dataOffset"
+ "NEW_PLUGIN_dataSize"
+ "NEW_PLUGIN_expectedHeight"
+ "NEW_PLUGIN_expectedWidth"
+ "NEW_PLUGIN_ostype"
+ "ReadHuffmanCodes"
+ "Unexpected kdu_resolution."
+ "VP8SetError"
+ "XPC_READPLUGIN_COPYBLOCKSET"
+ "XPC_READPLUGIN_COPYIOSURFACE"
+ "XPC_READPLUGIN_CREATE_PNG_FROM_SVG"
+ "XPC_READPLUGIN_IDENTIFY"
+ "XPC_READPLUGIN_IMAGECOUNT"
+ "XPC_READPLUGIN_INITIMAGE"
+ "XPC_READPLUGIN_SOURCEPROPERTIES"
+ "XPC_READPLUGIN_UPDATE_ALLOWED_TYPES"
+ "XPC_READPLUGIN_UPDATE_PERMISSIONS"
+ "abcdefghijklmnopqrstuvwxyz0123456789_"
+ "createImageBlockSetFromXPCObject"
+ "dec->hdr_.huffman_tables_.root.start != NULL"
+ "dec->incremental_ || error != VP8_STATUS_SUSPENDED"
+ "decodeImageDataPVR"
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
+ "iio_xpc_msg_call_options"
+ "iio_xpc_msg_error"
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
+ "messageID ???"
+ "origin_x"
+ "origin_y"
+ "setImageMedadataAtIndex index (%d) larger than arrayCount (%d) and image count (%d)\n"
+ "setImagePlusAtIndex index (%d) larger than arrayCount (%d) and image count (%d)\n"
+ "size_height"
+ "size_width"
+ "testHeader"
+ "xpc_shmem_map"
+ "••• Ⓜ️  skipping metadata for thumbnail creation\n"
+ "☀️  Meteor+ headroom: %f (hdrGain=%f, gainMapValue=%f)"
+ "✅ ImageIOXPC: XPC_READPLUGIN_UPDATE_ALLOWED_TYPES\n"
+ "✅ ImageIOXPC: XPC_READPLUGIN_UPDATE_PERMISSIONS\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_COPYBLOCKSET corrupt XPC reply: %d\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_COPYIOSURFACE corrupt XPC reply: %d\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_DECODE_IMAGE corrupt XPC reply: %d\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_DECODE_IMAGE error: %d\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_IMAGECOUNT corrupt XPC reply: %d\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_INITIMAGE corrupt XPC reply: %d\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_INITIMAGE error: %d  (IMAGEIO_PLUGIN_REPLY: %p)\n"
+ "❌ ImageIOXPC [%c%c%c%c]: XPC_READPLUGIN_SOURCEPROPERTIES corrupt XPC reply: %d\n"
+ "❌ ImageIOXPC: IIO_OOP_UPDATE_ALLOWED_TYPES error null-reply\n"
+ "❌ ImageIOXPC: IIO_OOP_UPDATE_PERMISSIONS error null-reply\n"
+ "❌ ImageIOXPC: XPC_READPLUGIN_IDENTIFY '%c%c%c%c' failed to get plugin\n"
+ "❌ ImageIOXPC: XPC_READPLUGIN_IDENTIFY corrupt XPC reply: %d\n"
+ "❌ ImageIOXPC: XPC_READPLUGIN_IDENTIFY error null-reply\n"
+ "❌ ImageIOXPC: XPC_READPLUGIN_IDENTIFY error: %d\n"
+ "❌ ImageIOXPC: XPC_READPLUGIN_IMAGECOUNT error null-reply\n"
+ "❌ ImageIOXPC: XPC_READPLUGIN_INITIMAGE error null-reply\n"
+ "❌ ImageIOXPC: XPC_READPLUGIN_SOURCEPROPERTIES error null-reply\n"
+ "🔺 bad width/height:  w: %d   h: %d\n"
- "    '%c%c%c%c' BLOCK (%d/%d) *** %p {%g, %g, %g, %g} rb: %ld  [%ld bytes]\n"
- "    '%c%c%c%c' BLOCK *** blockSet:%p   count: %d\n"
- "*** ERROR: CGImageSourceCreateImageAtIndex[%ld] - '%c%c%c%c' - failed to create image\n"
- "*** ERROR: CGImageSourceCreateThumbnailAtIndex[%ld] - '%c%c%c%c' - failed to create thumbnail\n"
- "*** ERROR: CGImageSourceCreateThumbnailAtIndex[%ld] - '%c%c%c%c' - failed to create thumbnail (no options)\n"
- "*** ERROR: MPEntry out of bounds\n"
- "*** ERROR: PNG decode  %dx%d  bpc: %d  cs: %d"
- "*** ERROR: blockSet-pixelSize: %d  block-pixelSize: %d\n"
- "*** ERROR: rowBytes <= 0 - skipping layer decoding\n"
- "*** dDebugBlockSet - cannot add text to imageBlockSet\n"
- ": _mpEntryCount > _markerLength (%ld > %ld)\n"
- "B24@?0Q8^v16"
- "Helvetica"
- "ImageIOXPCAllowedTypesArray"
- "ImageIOXPCBlockRect"
- "ImageIOXPCBlockRowBytes"
- "ImageIOXPCBlockSet"
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
- "callUpdateSourceProperties"
- "dec->br_.eos_"
- "dec->hdr_.huffman_tables_ != NULL"
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
- "❌ ImageIOXPC: XPC_READPLUGIN_IDENTIFY error - no reply\n"
- "❌ ImageIOXPC: XPC_READPLUGIN_IDENTIFY error: %lld\n"
- "❌ ImageIOXPC: XPC_READPLUGIN_INITIMAGE error (null-reply)\n"
- "❌ ImageIOXPC:: XPC_READPLUGIN_DECODE_FRAMES error\n"
- "❌ ImageIOXPC:: XPC_READPLUGIN_DECODE_FRAMES malformed reply\n"
- "⭕️ ImageIOXPC: OOP-request was made, but we're decoding in-process (GIF-XPC_READPLUGIN_DECODE_FRAMES)...\n"
- "⭕️ ImageIOXPC: OOP-request was made, but we're decoding in-process (PNG-XPC_READPLUGIN_DECODE_FRAMES)...\n"

```
