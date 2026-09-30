## libVinylNonUpdater.dylib

> `/usr/lib/libVinylNonUpdater.dylib`

```diff

 144.0.0.0.0
-  __TEXT.__text: 0x5260c
-  __TEXT.__auth_stubs: 0x1c50
+  __TEXT.__text: 0x52fb4
+  __TEXT.__auth_stubs: 0x1c90
   __TEXT.__init_offsets: 0x44
-  __TEXT.__const: 0x6a54
-  __TEXT.__gcc_except_tab: 0x426c
-  __TEXT.__cstring: 0x93cd
+  __TEXT.__const: 0x6a74
+  __TEXT.__gcc_except_tab: 0x4288
+  __TEXT.__cstring: 0x9f24
   __TEXT.__oslogstring: 0x7c
-  __TEXT.__unwind_info: 0x1d68
+  __TEXT.__unwind_info: 0x1d88
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__const: 0x1e38
-  __AUTH_CONST.__auth_got: 0xe30
+  __AUTH_CONST.__auth_got: 0xe50
   __AUTH_CONST.__const: 0x1cb8
   __AUTH_CONST.__cfstring: 0xb00
   __DATA.__data: 0xbd8

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 4904FE53-2A3D-3222-B5A4-90AA1CBE2F62
-  Functions: 1579
-  Symbols:   5238
-  CStrings:  1290
+  UUID: A99E6B47-D1EA-33E6-AD98-4B8A4F3752E6
+  Functions: 1583
+  Symbols:   5258
+  CStrings:  1411
 
Symbols:
+ GCC_except_table68
+ __ZN15BBUpdaterCommon17BBUPrintBackTraceEv
+ __ZN15BBUpdaterCommon23BBURegisterDebugSignalsEv
+ __ZN15BBUpdaterCommonL18handleDebugSignalsEiP9__siginfoPv
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPvNS_9allocatorIS1_EEEC2B8ne200100Em
+ ___block_descriptor_tmp.10
+ ___block_descriptor_tmp.109
+ ___block_descriptor_tmp.15
+ ___block_descriptor_tmp.17
+ ___block_descriptor_tmp.19
+ ___block_descriptor_tmp.7
+ ___block_literal_global.111
+ ___cxx_global_var_init.125
+ ___cxx_global_var_init.20
+ ___cxx_global_var_init.22
+ ___cxx_global_var_init.60
+ _backtrace
+ _backtrace_symbols_fd
+ _getchar
+ _sigaction
- GCC_except_table63
- GCC_except_table64
- ___block_descriptor_tmp.110
- ___block_descriptor_tmp.12
- ___block_descriptor_tmp.16
- ___block_descriptor_tmp.18
- ___block_descriptor_tmp.20
- ___block_descriptor_tmp.8
- ___block_literal_global.112
- ___cxx_global_var_init.126
- ___cxx_global_var_init.21
- ___cxx_global_var_init.23
- ___cxx_global_var_init.61
CStrings:
+ "        %s '%s' - Press [c] to continue ; [q] to quit: "
+ "/AppleInternal/Library/BuildRoots/4~CBEKugDeL24n7wT0eQUIovFC1NSVNtUuB2OG56Y/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/Library/Caches/com.apple.xbs/Sources/VinylRestore/CommandDrivers/eUICCVinylICEValve.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/VinylRestore/Communication/Eureka/VinylETLEUICC.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/VinylRestore/NonUpdate/VinylClearMetadata.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProv.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProvSessionData.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProvUtil.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/VinylRestore/Support/BBUPurpleReverseProxy.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/VinylRestore/Update/Perso/eUICCPerso.cpp"
+ "AuthPerso"
+ "AuthenticatePersoDevice"
+ "BBUCreateCFError"
+ "BBUFDRLogHandler"
+ "BBULogPrintBinaryDelegate"
+ "BBUReadNVRAM"
+ "BBUReadNVRAM_block_invoke"
+ "ClearMetadataForIccids"
+ "ComposeDeleteReq"
+ "ComposeDisableReq"
+ "ComposeGps"
+ "ComposeNsr"
+ "ComposeRnl"
+ "ConvertGpsToGbpp"
+ "ConvertPirToHir"
+ "CreateDictionaryFromPlistData"
+ "CreateValidatePersoPayload"
+ "CreateValidationBlob"
+ "DeleteProfile"
+ "DisableProfile"
+ "ExtractDataFromPbiRsp"
+ "ExtractNotificationListSeqNumbers"
+ "ExtractProfileInfo"
+ "ExtractResult"
+ "FinalizePerso"
+ "FinalizePersoDevice"
+ "ForcePerso"
+ "GetData"
+ "GetData_EoS"
+ "GetListOfIccids"
+ "GetNextBppSegment"
+ "GetNonceServer"
+ "GetParameters"
+ "GetParametersDummy"
+ "GetProfilesInfoList"
+ "GetProvisioningSessions"
+ "GetSIMSKUString"
+ "GetVinylType"
+ "GetWrapKeyServer"
+ "HandleNotifications"
+ "HandleRefurbishProfileReference"
+ "HardwareHasESIM_block_invoke"
+ "InitPerso"
+ "InitPersoDevice"
+ "InitPersoServer"
+ "InstallPairingMSM"
+ "IsNotificationForTwoPhase"
+ "IsNotificationSentRspSuccess"
+ "IsProvTxIdAvailable"
+ "LETOEnableEUICC"
+ "ListInstallationNotifications"
+ "LoadBPP"
+ "ManagePairingAuthenticate"
+ "ManagePairingGetNonce"
+ "NotificationSent"
+ "Perform"
+ "PostDataSync"
+ "PowerDownSE"
+ "PowerUpSE"
+ "PrepareBPPInstallation"
+ "Refurb"
+ "ResetCard"
+ "RetrieveNotificationListForSeqNum"
+ "ReverseProxyGetSettings"
+ "ReverseProxyGetSettings_block_invoke"
+ "SendReceiptServer"
+ "SerializeDictIntoPlistData"
+ "SerializeKeyValuePairsIntoPlistData"
+ "SetCardMode"
+ "StoreData"
+ "ValidatePerso"
+ "ValidatePersoDevice"
+ "VinylControllerObjDestroy"
+ "VinyleUICCPerformOperationWithLinkAndLogSync"
+ "VinyleUICCPerformOperationWithTransportAndLogSync"
+ "bbupdater_log"
+ "bootstrapProvisioning"
+ "caught signal %d\n"
+ "checkEOSDev"
+ "collectCoreDump"
+ "convertGbppToPbiBpp"
+ "create"
+ "createTransport"
+ "createTransportNoEvents"
+ "createTransport_block_invoke_2"
+ "extractDataFromPbiReq"
+ "extractDataFromPbiRsp"
+ "extractDataFromPir"
+ "freeTransport"
+ "freeTransportSync"
+ "freeTransportSync_block_invoke"
+ "freeTransportSync_block_invoke_2"
+ "getECID_block_invoke"
+ "getEID"
+ "getPairingIdentifier"
+ "getPairingParameters"
+ "get_info"
+ "inRestoreOS_block_invoke"
+ "inRestoreOS_block_invoke_2"
+ "isAbsentOkay"
+ "isNVRAMKeyPresent"
+ "logEUICCData"
+ "managePairingInstallMSM"
+ "openChannel"
+ "operator()"
+ "performNonUpdateOperation"
+ "processAlderResponse"
+ "startRouterServer"
+ "statusCallback"
+ "stopRouterServer"
+ "supportsVinylUpdate"
+ "verifyPairing"
+ "waitForeSIMBoot"
- "/AppleInternal/Library/BuildRoots/4~CAp9ugAn917kH9XUndyMFQOIqUsu2rgjmZKHsog/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "0x<< SNUM >>"

```
