## libVinylNonUpdater.dylib

> `/usr/lib/libVinylNonUpdater.dylib`

```diff

 144.0.0.0.0
-  __TEXT.__text: 0x467f0
-  __TEXT.__auth_stubs: 0x1660
+  __TEXT.__text: 0x45e70
+  __TEXT.__auth_stubs: 0x1620
   __TEXT.__init_offsets: 0x38
-  __TEXT.__const: 0x5394
-  __TEXT.__gcc_except_tab: 0x3468
-  __TEXT.__cstring: 0x803f
+  __TEXT.__const: 0x5384
+  __TEXT.__gcc_except_tab: 0x344c
+  __TEXT.__cstring: 0x755f
   __TEXT.__oslogstring: 0x7c
-  __TEXT.__unwind_info: 0x18a0
+  __TEXT.__unwind_info: 0x1880
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x1d68
-  __AUTH_CONST.__auth_got: 0xb38
+  __AUTH_CONST.__auth_got: 0xb18
   __AUTH_CONST.__const: 0x10e8
   __AUTH_CONST.__cfstring: 0xb00
-  __DATA.__data: 0xbc8
+  __DATA.__data: 0xbd0
   __DATA.__bss: 0x4d8
   __DATA.__common: 0x48
   __DATA_DIRTY.__data: 0x20

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 03071923-55AF-3C27-ABE7-EF09DB44A248
-  Functions: 1308
-  Symbols:   4360
-  CStrings:  1236
+  UUID: E1AD8DE2-71D2-3BFB-BA7B-A91D8A25E5C9
+  Functions: 1304
+  Symbols:   4342
+  CStrings:  1121
 
Symbols:
+ GCC_except_table63
+ GCC_except_table64
+ ___block_descriptor_tmp.110
+ ___block_descriptor_tmp.12
+ ___block_descriptor_tmp.16
+ ___block_descriptor_tmp.18
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.8
+ ___block_literal_global.112
+ ___cxx_global_var_init.126
+ ___cxx_global_var_init.21
+ ___cxx_global_var_init.23
+ ___der_key_platform_config_hidden_key_pka_keep_entropy
+ _der_key_platform_config_hidden_key_pka_keep_entropy
- GCC_except_table68
- __ZN15BBUpdaterCommon17BBUPrintBackTraceEv
- __ZN15BBUpdaterCommon23BBURegisterDebugSignalsEv
- __ZN15BBUpdaterCommonL18handleDebugSignalsEiP9__siginfoPv
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEEC2B8ne200100Em
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.109
- ___block_descriptor_tmp.15
- ___block_descriptor_tmp.17
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.7
- ___block_literal_global.111
- ___cxx_global_var_init.125
- ___cxx_global_var_init.20
- ___cxx_global_var_init.22
- _backtrace
- _backtrace_symbols_fd
- _getchar
- _sigaction
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B66tugDUThjrDcxdZIdqsNC5udlczY-xoy5oqMk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "0x<< SNUM >>"
- "        %s '%s' - Press [c] to continue ; [q] to quit: "
- "/AppleInternal/Library/BuildRoots/4~B6HEugB3eWo3wSOE-pqZbI-DwPXlukJJ9BaJmfs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/CommandDrivers/eUICCVinylICEValve.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/Communication/Eureka/VinylETLEUICC.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/NonUpdate/VinylClearMetadata.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProv.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProvSessionData.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProvUtil.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/Support/BBUPurpleReverseProxy.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/Update/Perso/eUICCPerso.cpp"
- "AuthPerso"
- "AuthenticatePersoDevice"
- "BBUCreateCFError"
- "BBUFDRLogHandler"
- "BBULogPrintBinaryDelegate"
- "BBUReadNVRAM"
- "BBUReadNVRAM_block_invoke"
- "ClearMetadataForIccids"
- "ComposeDeleteReq"
- "ComposeDisableReq"
- "ComposeGps"
- "ComposeNsr"
- "ComposeRnl"
- "ConvertGpsToGbpp"
- "ConvertPirToHir"
- "CreateDictionaryFromPlistData"
- "CreateValidatePersoPayload"
- "CreateValidationBlob"
- "DeleteProfile"
- "DisableProfile"
- "ExtractDataFromPbiRsp"
- "ExtractNotificationListSeqNumbers"
- "ExtractProfileInfo"
- "ExtractResult"
- "FinalizePerso"
- "FinalizePersoDevice"
- "ForcePerso"
- "GetData"
- "GetListOfIccids"
- "GetNextBppSegment"
- "GetNonceServer"
- "GetParameters"
- "GetParametersDummy"
- "GetProfilesInfoList"
- "GetProvisioningSessions"
- "GetSIMSKUString"
- "GetVinylType"
- "GetWrapKeyServer"
- "HandleNotifications"
- "HandleRefurbishProfileReference"
- "HardwareHasESIM_block_invoke"
- "InitPerso"
- "InitPersoDevice"
- "InitPersoServer"
- "InstallPairingMSM"
- "IsNotificationForTwoPhase"
- "IsNotificationSentRspSuccess"
- "IsProvTxIdAvailable"
- "LETOEnableEUICC"
- "ListInstallationNotifications"
- "LoadBPP"
- "ManagePairingAuthenticate"
- "ManagePairingGetNonce"
- "NotificationSent"
- "Perform"
- "PostDataSync"
- "PowerDownSE"
- "PowerUpSE"
- "PrepareBPPInstallation"
- "Refurb"
- "ResetCard"
- "RetrieveNotificationListForSeqNum"
- "ReverseProxyGetSettings"
- "ReverseProxyGetSettings_block_invoke"
- "SendReceiptServer"
- "SerializeDictIntoPlistData"
- "SerializeKeyValuePairsIntoPlistData"
- "SetCardMode"
- "StoreData"
- "ValidatePerso"
- "ValidatePersoDevice"
- "VinylControllerObjDestroy"
- "VinyleUICCPerformOperationWithTransportAndLogSync"
- "bbupdater_log"
- "bootstrapProvisioning"
- "caught signal %d\n"
- "checkEOSDev"
- "collectCoreDump"
- "convertGbppToPbiBpp"
- "create"
- "createTransport"
- "createTransportNoEvents"
- "createTransport_block_invoke_2"
- "extractDataFromPbiReq"
- "extractDataFromPbiRsp"
- "extractDataFromPir"
- "freeTransport"
- "freeTransportSync"
- "freeTransportSync_block_invoke"
- "freeTransportSync_block_invoke_2"
- "getECID_block_invoke"
- "getEID"
- "getPairingIdentifier"
- "getPairingParameters"
- "get_info"
- "inRestoreOS_block_invoke"
- "inRestoreOS_block_invoke_2"
- "isAbsentOkay"
- "isNVRAMKeyPresent"
- "logEUICCData"
- "managePairingInstallMSM"
- "openChannel"
- "performNonUpdateOperation"
- "processAlderResponse"
- "statusCallback"
- "supportsVinylUpdate"
- "verifyPairing"

```
