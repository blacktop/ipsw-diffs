## MobileDevice

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/MobileDevice.framework/Versions/A/MobileDevice`

```diff

-  __TEXT.__text: 0x2b7f84
+  __TEXT.__text: 0x2b7b38
   __TEXT.__objc_methlist: 0x3fbc
-  __TEXT.__const: 0x10c098
-  __TEXT.__cstring: 0x7aa87
+  __TEXT.__const: 0x10c0a8
+  __TEXT.__cstring: 0x7aa8b
   __TEXT.__gcc_except_tab: 0x52b0
   __TEXT.__oslogstring: 0xf37
   __TEXT.__ustring: 0xb0

   __TEXT.__unwind_info: 0x6ef0
   __TEXT.__eh_frame: 0x66c
   __TEXT.__objc_stubs: 0x5e00
-  __TEXT.__auth_stubs: 0x41a0
+  __TEXT.__auth_stubs: 0x4190
   __TEXT.__objc_classname: 0xe2f
   __TEXT.__objc_methname: 0x7711
   __TEXT.__objc_methtype: 0x2782

   __AUTH_CONST.__cfstring: 0x40320
   __AUTH_CONST.__objc_const: 0x74e0
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__auth_got: 0x20c8
+  __AUTH_CONST.__auth_got: 0x20c0
   __AUTH.__objc_data: 0x1a40
   __AUTH.__data: 0x338
   __AUTH.__thread_vars: 0x18

   - /usr/lib/libssl.35.dylib
   - /usr/lib/libz.1.dylib
   Functions: 10384
-  Symbols:   17319
+  Symbols:   17318
   CStrings:  25220
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__dof_MobileDev : content changed
~ __TEXT.__dof_afc : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__objc_classrefs : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
~ __DATA.__common : content changed
Symbols:
+ _uarpProcessTLV2
- _objc_claimAutoreleasedReturnValue
- _uarpProcessTLV
Functions:
~ _ComputeShortestPathFromNodes : 128 -> 104
~ _lzvnStreamDecode : 592 -> 584
~ _adler32 : 316 -> 308
~ _BrotliDecoderHuffmanTreeGroupInit : 156 -> 132
~ _BrotliSplitBlock : 13984 -> 13952
~ _CreateBackwardReferencesNH35 : 3608 -> 3588
~ _CreateBackwardReferencesNH55 : 3632 -> 3600
~ _CreateBackwardReferencesNH65 : 5528 -> 5372
~ _BrotliHistogramCombineLiteral : 744 -> 748
~ _BrotliHistogramCombineCommand : 748 -> 752
~ _BrotliHistogramCombineDistance : 748 -> 752
~ _crc32 : 808 -> 828
~ _build_tree : 1168 -> 1184
~ _BrotliDecoderDecompressStream : 4016 -> 4004
~ _DecodeVarLenUint8 : 456 -> 444
~ _DecodeContextMap : 1108 -> 1084
~ _SafeProcessCommands : 2844 -> 2796
~ _SafeDecodeCommandBlockSwitch : 808 -> 784
~ _SafeDecodeLiteralBlockSwitch : 884 -> 860
~ _SafeDecodeDistanceBlockSwitch : 832 -> 808
~ _deflate_rle : 828 -> 832
~ _longest_match : 472 -> 484
~ _BrotliBuildHistogramsWithContext : 640 -> 632
~ _BrotliBuildAndStoreHuffmanTreeFast : 1792 -> 1784
~ _BrotliBuildHuffmanTable : 560 -> 568
~ sub_5dda0 -> sub_5dc00 : 96 -> 64
~ __base64_ntop : 424 -> 412
~ _ccaes_vng_ctr_crypt : 384 -> 296
~ _cckeccak_squeeze_internal : 932 -> 616
~ _ccmldsa_poly_bitunpack_eta2 : 160 -> 156
~ _ccmldsa_poly_bitunpack_t1 : 128 -> 124
~ _ccmldsa_poly_simplebitpack_w1 : 60 -> 52
~ _probeDeviceForRegistryEntry : 268 -> 252
~ _probeHubForVIDPID : 112 -> 100
~ _cfStringCompare : 324 -> 308
~ ___AFCConnectionDispatchReply : 244 -> 232
~ ___WaitForTimeoutOrEvent : 1136 -> 1144
~ __getDeviceMapEntryForHardwareFromDeviceMapTxt : 1024 -> 1028
~ __getDeviceMapEntryForHardwareFromPlistCache : 568 -> 576
~ __AMRUSBDeviceGetFirmwareInfo : 320 -> 328
~ __createDFUDataFromFile : 632 -> 628
~ _AMRAuthInstallUpdaterGetOptionName : 136 -> 144
~ _uarpPlatformEndpointStreamingRecvBytes : 280 -> 304
~ _uarpPlatformAssetResponseData : 436 -> 452
~ _uarpProcessTLV -> _uarpProcessTLV2 : 196 -> 228
~ _uarpPlatformAssetAllMetaDataWindowFilled : 304 -> 312
~ _uarpPlatformEndpointRecvMessage : 5452 -> 5460
~ _SoCUpdaterExecCommandDynamic : 472 -> 480
~ _Ace3RestoreInfoCopyFirmware : 268 -> 272
~ _Ace3RestoreInfoCreateRequest : 592 -> 624
~ -[Ace3SoCRestoreInfoFirmwareCopierBackDeploy parseOptions:] : 912 -> 960
~ -[Ace3SoCRestoreInfoFirmwareCopierBackDeploy copyFirmwareToDestinationBundleWithError:] : 892 -> 948
~ -[Ace3SoCRestoreInfoFirmwareCopierBackDeploy readFirmwareFileDataWithError:] : 264 -> 272
~ -[NSError(FileExistsCheck) isFileExistsError] : 100 -> 104
~ -[Ace3SoCRestoreInfoHelperBackDeploy initWithOptions:logFunction:logContext:] : 244 -> 256
~ -[Ace3RestoreInfoFirmwareCopierBackDeploy firmwareKeyFromBuildIdentityDict:deviceInfo:] : 224 -> 232
~ _CTCopyDeviceIdentifiers -> _CTConvertAsciiHexToUint64 : 292 -> 328
~ _CTConvertDashTerminatedHexstringTo64BitInteger -> _CTCopyDeviceIdentifiers : 252 -> 292
~ _CTFillBAAIdentity -> _CTConvertDashTerminatedHexstringTo64BitInteger : 164 -> 252
~ _CTEvaluateBAASystemTestRoot -> _CTFillBAAIdentity : 156 -> 164
~ _CTConvertAsciiHexToUint64 -> _CTEvaluateBAAUserTestRoot : 336 -> 156
~ _X509ChainCheckPathWithOptions : 1580 -> 1584
~ _apBoardForAceBoard : 68 -> 76
~ __AMAuthInstallApFtabCopyFtabFromFile : 312 -> 188
~ _AMAuthInstallApImg4GetTypeForEntryName : 120 -> 128
~ _AMAuthInstallMonetMeasureDbl : 428 -> 420
~ _AMAuthInstallMonetMeasureMav20ElfMBN : 944 -> 932
~ _AMAuthInstallMonetMeasureElfMBN : 972 -> 960
~ _OUTLINED_FUNCTION_9 : 28 -> 12
~ _OUTLINED_FUNCTION_10 : 12 -> 28
~ __AMAuthInstallUpdaterInitLocalSigning : 184 -> 188
~ _b64_ntop : 364 -> 352
~ _ComputeShortestPathFromNodes : 128 -> 104
~ _lzx_huffman_tree_read_code : 308 -> 276
~ _lzx_huffman_tree_update_tree_using_pre_tree_encoding : 796 -> 748
~ _lzx_huffman_create_pre_tree : 272 -> 256
~ _lzbitmap_decode : 2200 -> 2208
~ _LZFSEIBootBufferPushN : 224 -> 212
~ _BrotliSplitBlock : 13976 -> 13952
~ _lzx_decode_buffer : 2388 -> 2292
~ _smb_lz77_encode_buffer : 892 -> 900
~ _RavGetOptimal : 4816 -> 4860
~ _CreateBackwardReferencesNH35 : 3608 -> 3588
~ _CreateBackwardReferencesNH55 : 3632 -> 3600
~ _CreateBackwardReferencesNH65 : 5528 -> 5372
~ _BrotliHistogramCombineLiteral : 744 -> 748
~ _BrotliHistogramCombineCommand : 748 -> 752
~ _BrotliHistogramCombineDistance : 748 -> 752
~ _CountsCreateWithBuffer : 404 -> 396
~ _BrotliDecoderDecompressStream : 4016 -> 4004
~ _DecodeVarLenUint8 : 456 -> 444
~ _DecodeContextMap : 1108 -> 1084
~ _SafeProcessCommands : 2844 -> 2796
~ _SafeDecodeCommandBlockSwitch : 808 -> 784
~ _SafeDecodeLiteralBlockSwitch : 884 -> 860
~ _SafeDecodeDistanceBlockSwitch : 832 -> 808
~ _BrotliBuildAndStoreHuffmanTreeFast : 1792 -> 1784
~ _BrotliBuildHuffmanTable : 560 -> 568
~ __ZNSt3__134__uninitialized_allocator_relocateB9nqe220106INS_9allocatorI18ACFUErrorContainerEEPS2_EEvRT_T0_S7_S7_ : 200 -> 192
~ -[FTABFileBackDeploy parseFileData] : 844 -> 832
~ __ZN19CentauriRestoreHost13createRequestENSt3__110shared_ptrI12ACFUFirmwareEERKN15ACFURestoreHost8DemotionE : 916 -> 920
~ __ZN19CentauriRestoreHost4initEPK14__CFDictionaryPK10__CFString : 1112 -> 1120
~ __ZN19CentauriRestoreHost19copyFirmwareUpdaterEPK14__CFDictionaryN15ACFURestoreHost24CopyFirmwareFileDictTypeE : 3804 -> 3852
~ __ZN19CentauriRestoreHost15isFirmwareValidEP12ACFUFTABFile : 548 -> 552
~ _CentauriUpdaterGetTags : 1264 -> 1284
~ _CentauriUpdaterCopyFirmware : 1248 -> 1268
~ _CentauriUpdaterCreateRequest : 2596 -> 2632
~ __ZN13SERestoreInfo11UpdateTableC2ERK7DERItem : 2000 -> 2012
~ __ZNSt3__16vectorIN13SERestoreInfo4BLOBENS_9allocatorIS2_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS2_RS4_EE : 268 -> 248
~ __ZNSt3__16vectorIN13SERestoreInfo4BLOBENS_9allocatorIS2_EEE16__init_with_sizeB9nqe220106IPS2_S7_EEvT_T0_m : 196 -> 188
~ __ZNSt3__16vectorIN13SERestoreInfo4BLOBENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe220106Ev : 172 -> 152
~ __ZNSt3__134__uninitialized_allocator_relocateB9nqe220106INS_9allocatorIN13SERestoreInfo8ApduBLOBEEEPS3_EEvRT_T0_S8_S8_ : 252 -> 244
~ _externalBackendCreate : 1364 -> 1352
~ _USBCUpdateEndpointInitialize : 740 -> 744
~ _AMAuthInstallApFtabStitchTicketData : 388 -> 384
~ _AMAuthInstallApFtabCopyFtabFromFile.cold.1 : 44 -> 192
~ _AMAuthInstallMonetMeasureElf : 784 -> 772
~ _AMAuthInstallMonetMeasureBootSbl : 444 -> 436
~ _ZN14CentauriCommon11createErrorEPKcS1_S1_13ACFUErrorCode.cold.1 : 152 -> 156
~ _ZN14CentauriCommon11createErrorEPKcS1_S1_13ACFUErrorCode.cold.2 : 144 -> 148
~ _ZN14CentauriCommon11createErrorEPKcS1_S1_13ACFUErrorCode.cold.3 : 144 -> 148
~ _ZN19CentauriRestoreHost13createRequestENSt3__110shared_ptrI12ACFUFirmwareEERKN15ACFURestoreHost8DemotionE.cold.2 : 192 -> 196
~ _ZN19CentauriRestoreHost13createRequestENSt3__110shared_ptrI12ACFUFirmwareEERKN15ACFURestoreHost8DemotionE.cold.4 : 156 -> 160
~ _ZN19CentauriRestoreHost19copyFirmwareUpdaterEPK14__CFDictionaryN15ACFURestoreHost24CopyFirmwareFileDictTypeE.cold.1 : 156 -> 160
~ _ZN19CentauriRestoreHost19copyFirmwareUpdaterEPK14__CFDictionaryN15ACFURestoreHost24CopyFirmwareFileDictTypeE.cold.2 : 156 -> 160
~ _ZN19CentauriRestoreHost19copyFirmwareUpdaterEPK14__CFDictionaryN15ACFURestoreHost24CopyFirmwareFileDictTypeE.cold.3 : 156 -> 160
~ _ZN19CentauriRestoreHost19copyFirmwareUpdaterEPK14__CFDictionaryN15ACFURestoreHost24CopyFirmwareFileDictTypeE.cold.5 : 156 -> 160
~ _ZN19CentauriRestoreHost19copyFirmwareUpdaterEPK14__CFDictionaryN15ACFURestoreHost24CopyFirmwareFileDictTypeE.cold.7 : 156 -> 160
~ _ZN19CentauriRestoreHost19copyFirmwareUpdaterEPK14__CFDictionaryN15ACFURestoreHost24CopyFirmwareFileDictTypeE.cold.8 : 144 -> 148
~ _ZN19CentauriRestoreHost19copyFirmwareUpdaterEPK14__CFDictionaryN15ACFURestoreHost24CopyFirmwareFileDictTypeE.cold.9 : 156 -> 160
~ _ZN19CentauriRestoreHost15populateCFErrorEPKcS1_13ACFUErrorCode.cold.2 : 160 -> 164
~ CentauriUpdaterGetTags.cold.1 : 252 -> 256
~ CentauriUpdaterCopyFirmware.cold.1 : 252 -> 256
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CN4oW8/Sources/VeridianDylibs/T200RestoreInfo/T200RestoreInfo.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CN4oW8/Sources/VeridianDylibs/T200Updater/T200UpdaterPrivateHelper.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KCqARo/Sources/MobileInstallation_host/patch.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UMlVaw/Sources/PurpleReverseProxy_host/Common/RPSocket.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UMlVaw/Sources/PurpleReverseProxy_host/Common/Utilities.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UMlVaw/Sources/PurpleReverseProxy_host/ReverseProxyHost/ReverseProxyHost.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UMlVaw/Sources/PurpleReverseProxy_host/Socks5/Socks5Server.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/IOCompressedStreams.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/SharedArray.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/SharedBuffer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/ThreadPipeline.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/Threads.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/Utils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelCompression/Filter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XGGYNh/Sources/MobileDevice/Source/AMDevicePowerAssertion.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y29Bww/Sources/AppleFileConduit/afc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y29Bww/Sources/AppleFileConduit/client-async.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y29Bww/Sources/AppleFileConduit/client-sync.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y29Bww/Sources/AppleFileConduit/connection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y29Bww/Sources/AppleFileConduit/platform.c"
+ "Helsinki_Restore_Host-58.0.42"
+ "libauthinstall-1155.0.3"
+ "restore library built Jun 26 2026 at 19:26:41"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1yEuLg/Sources/MobileDevice/Source/AMDevicePowerAssertion.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5HLdNa/Sources/MobileInstallation_host/patch.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/IOCompressedStreams.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/SharedArray.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/SharedBuffer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/ThreadPipeline.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/Threads.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/Utils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelCompression/Filter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvZM97/Sources/AppleFileConduit/afc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvZM97/Sources/AppleFileConduit/client-async.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvZM97/Sources/AppleFileConduit/client-sync.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvZM97/Sources/AppleFileConduit/connection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WvZM97/Sources/AppleFileConduit/platform.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mlnI1F/Sources/PurpleReverseProxy_host/Common/RPSocket.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mlnI1F/Sources/PurpleReverseProxy_host/Common/Utilities.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mlnI1F/Sources/PurpleReverseProxy_host/ReverseProxyHost/ReverseProxyHost.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mlnI1F/Sources/PurpleReverseProxy_host/Socks5/Socks5Server.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rTYLtr/Sources/VeridianDylibs/T200RestoreInfo/T200RestoreInfo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rTYLtr/Sources/VeridianDylibs/T200Updater/T200UpdaterPrivateHelper.c"
- "Helsinki_Restore_Host-58.0.41"
- "libauthinstall-1155"
- "restore library built Jun 12 2026 at 07:05:49"

```
