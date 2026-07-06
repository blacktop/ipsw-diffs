## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

```diff

-  __TEXT.__text: 0xb18c0
+  __TEXT.__text: 0xb19bc
   __TEXT.__objc_methlist: 0x262c
-  __TEXT.__cstring: 0x21a55
+  __TEXT.__cstring: 0x21a59
   __TEXT.__const: 0xc1db
   __TEXT.__gcc_except_tab: 0x3a78
   __TEXT.__dlopen_cstrs: 0x63
   __TEXT.__oslogstring: 0xad5
-  __TEXT.__unwind_info: 0x2900
+  __TEXT.__unwind_info: 0x2910
   __TEXT.__eh_frame: 0x7c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__cfstring: 0xf120
   __AUTH_CONST.__objc_const: 0x4908
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__auth_got: 0xda8
+  __AUTH_CONST.__auth_got: 0xd98
   __AUTH.__objc_data: 0x13b0
   __AUTH.__data: 0x20
   __AUTH.__thread_vars: 0x18

   - /usr/lib/updaters/libAppleTconUARPUpdater.dylib
   - /usr/lib/updaters/libT200Updater.dylib
   Functions: 3814
-  Symbols:   6857
+  Symbols:   6855
   CStrings:  6788
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__objc_classrefs : content changed
~ __DATA.__objc_superrefs : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_opt_class
Functions:
~ __AMAuthInstallApFtabCopyFtabFromFile : 312 -> 188
~ _AMAuthInstallApImg4GetTypeForEntryName : 120 -> 128
~ _AMAuthInstallMonetMeasureDbl : 428 -> 420
~ _AMAuthInstallMonetMeasureMav20ElfMBN : 944 -> 932
~ _AMAuthInstallMonetMeasureElfMBN : 972 -> 960
~ _OUTLINED_FUNCTION_9 : 28 -> 12
~ _OUTLINED_FUNCTION_10 : 12 -> 28
~ __AMAuthInstallUpdaterInitLocalSigning : 184 -> 188
~ _b64_ntop : 364 -> 352
~ _SoCUpdaterExecCommandDynamic : 472 -> 480
~ _Ace3RestoreInfoCopyFirmware : 268 -> 272
~ -[Ace3SoCRestoreInfoFirmwareCopierOS parseOptions:] : 912 -> 960
~ -[Ace3SoCRestoreInfoFirmwareCopierOS copyFirmwareToDestinationBundleWithError:] : 892 -> 948
~ -[Ace3SoCRestoreInfoFirmwareCopierOS readFirmwareFileDataWithError:] : 264 -> 272
~ -[NSError(FileExistsCheck) isFileExistsError] : 100 -> 104
~ -[Ace3SoCRestoreInfoHelperOS initWithOptions:logFunction:logContext:] : 244 -> 256
~ -[Ace3RestoreInfoFirmwareCopierOS firmwareKeyFromBuildIdentityDict:deviceInfo:] : 224 -> 232
~ -[FTABFileOS parseFileData] : 844 -> 832
~ __ZN19CentauriRestoreHost13createRequestENSt3__110shared_ptrI12ACFUFirmwareEERKN15ACFURestoreHost8DemotionE : 916 -> 920
~ __ZN19CentauriRestoreHost4initEPK14__CFDictionaryPK10__CFString : 1112 -> 1120
~ __ZN19CentauriRestoreHost19copyFirmwareUpdaterEPK14__CFDictionaryN15ACFURestoreHost24CopyFirmwareFileDictTypeE : 3804 -> 3852
~ __ZN19CentauriRestoreHost15isFirmwareValidEP12ACFUFTABFile : 548 -> 552
~ _CentauriUpdaterGetTags : 1264 -> 1284
~ _CentauriUpdaterCopyFirmware : 1248 -> 1268
~ _CentauriUpdaterCreateRequest : 2596 -> 2632
~ __ZNSt3__134__uninitialized_allocator_relocateB9nqe220106INS_9allocatorI18ACFUErrorContainerEEPS2_EEvRT_T0_S7_S7_ : 200 -> 192
~ __ZN13SERestoreInfo11UpdateTableC2ERK7DERItem : 2000 -> 2012
~ __ZNSt3__16vectorIN13SERestoreInfo4BLOBENS_9allocatorIS2_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS2_RS4_EE : 268 -> 248
~ __ZNSt3__16vectorIN13SERestoreInfo4BLOBENS_9allocatorIS2_EEE16__init_with_sizeB9nqe220106IPS2_S7_EEvT_T0_m : 196 -> 188
~ __ZNSt3__16vectorIN13SERestoreInfo4BLOBENS_9allocatorIS2_EEE16__destroy_vectorclB9nqe220106Ev : 172 -> 152
~ __ZNSt3__134__uninitialized_allocator_relocateB9nqe220106INS_9allocatorIN13SERestoreInfo8ApduBLOBEEEPS3_EEvRT_T0_S8_S8_ : 252 -> 244
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
+ "Helsinki_Restore_Host-58.0.42"
+ "libauthinstall-1155.0.3"
- "Helsinki_Restore_Host-58.0.41"
- "libauthinstall-1155"

```
