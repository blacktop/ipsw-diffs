## libVinylNonUpdater.dylib

> `/usr/lib/libVinylNonUpdater.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0x52298
-  __TEXT.__auth_stubs: 0x1c90
+  __TEXT.__text: 0x517b0
+  __TEXT.__auth_stubs: 0x1c50
   __TEXT.__init_offsets: 0x44
-  __TEXT.__const: 0x6d7c
-  __TEXT.__gcc_except_tab: 0x4288
-  __TEXT.__cstring: 0xa7de
+  __TEXT.__const: 0x6d5c
+  __TEXT.__gcc_except_tab: 0x426c
+  __TEXT.__cstring: 0x9a8f
   __TEXT.__oslogstring: 0x7c
-  __TEXT.__unwind_info: 0x1d70
+  __TEXT.__unwind_info: 0x1d50
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__const: 0x1e38
-  __AUTH_CONST.__auth_got: 0xe50
+  __AUTH_CONST.__auth_got: 0xe30
   __AUTH_CONST.__const: 0x1cb8
   __AUTH_CONST.__cfstring: 0xb00
   __DATA.__data: 0xc10

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1627
-  Symbols:   3031
-  CStrings:  1341
+  Functions: 1622
+  Symbols:   3021
+  CStrings:  1220
 
Symbols:
+ GCC_except_table63
+ GCC_except_table64
- GCC_except_table70
- __ZN15BBUpdaterCommon17BBUPrintBackTraceEv
- __ZN15BBUpdaterCommon23BBURegisterDebugSignalsEv
- __ZN15BBUpdaterCommonL18handleDebugSignalsEiP9__siginfoPv
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEEC2B9nqe210106Em
- _backtrace
- _backtrace_symbols_fd
- _getchar
- _sigaction
CStrings:
+ "0x<< SNUM >>"
- "        %s '%s' - Press [c] to continue ; [q] to quit: "
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/CommandDrivers/eUICCVinylICEValve.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/Communication/Eureka/VinylETLEUICC.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/NonUpdate/VinylClearMetadata.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProv.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProvSessionData.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProvUtil.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/Support/BBUPurpleReverseProxy.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/Update/Perso/eUICCPerso.cpp"
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
- "GetData_EoS"
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
- "VinyleUICCPerformOperationWithLinkAndLogSync"
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
- "operator()"
- "performNonUpdateOperation"
- "processAlderResponse"
- "startRouterServer"
- "statusCallback"
- "stopRouterServer"
- "supportsVinylUpdate"
- "verifyPairing"
- "waitForeSIMBoot"
```
