## libVinylNonUpdater.dylib

> `/usr/lib/libVinylNonUpdater.dylib`

```diff

 78.0.0.0.0
-  __TEXT.__text: 0x260c8
-  __TEXT.__auth_stubs: 0xf30
+  __TEXT.__text: 0x25a08
+  __TEXT.__auth_stubs: 0xed0
   __TEXT.__init_offsets: 0x2c
-  __TEXT.__const: 0x1259
-  __TEXT.__gcc_except_tab: 0x20c4
-  __TEXT.__cstring: 0x4de2
-  __TEXT.__unwind_info: 0xfd8
+  __TEXT.__const: 0x1239
+  __TEXT.__gcc_except_tab: 0x20a0
+  __TEXT.__cstring: 0x458d
+  __TEXT.__unwind_info: 0xfb8
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0x788
-  __AUTH_CONST.__auth_got: 0x7a0
+  __AUTH_CONST.__auth_got: 0x770
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0xce0
   __AUTH_CONST.__cfstring: 0x780

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 701
-  Symbols:   2367
-  CStrings:  689
+  Functions: 697
+  Symbols:   2345
+  CStrings:  602
 
Symbols:
+ GCC_except_table42
+ GCC_except_table59
+ ___block_descriptor_tmp.12
+ ___block_descriptor_tmp.16
+ ___block_descriptor_tmp.18
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.8
+ ___block_descriptor_tmp.97
+ ___block_literal_global.99
+ ___cxx_global_var_init.13
+ ___cxx_global_var_init.21
+ ___cxx_global_var_init.48
- GCC_except_table48
- GCC_except_table58
- GCC_except_table63
- GCC_except_table65
- GCC_except_table69
- __ZN15BBUpdaterCommon17BBUPrintBackTraceEv
- __ZN15BBUpdaterCommon23BBURegisterDebugSignalsEv
- __ZN15BBUpdaterCommonL18handleDebugSignalsEiP9__siginfoPv
- __ZNKSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEEC2B8ne190102Em
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.15
- ___block_descriptor_tmp.17
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.7
- ___block_descriptor_tmp.96
- ___block_literal_global.98
- ___cxx_global_var_init.12
- ___cxx_global_var_init.20
- ___cxx_global_var_init.47
- _backtrace
- _backtrace_symbols_fd
- _fprintf
- _getchar
- _printf
- _sigaction
CStrings:
+ "/AppleInternal/Library/BuildRoots/818328e5-1f5b-11f0-9b1c-f6a14c66e6eb/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "0x<< SNUM >>"
- "        %s '%s' - Press [c] to continue ; [q] to quit: "
- "/AppleInternal/Library/BuildRoots/52be8cca-1f60-11f0-b20f-6661e7117d4d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/CommandDrivers/eUICCVinylICEValve.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/NonUpdate/VinylClearMetadata.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProv.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProvSessionData.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProvUtil.cpp"
- "/Library/Caches/com.apple.xbs/Sources/VinylRestore/Support/BBUPurpleReverseProxy.cpp"
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
- "DeleteProfile"
- "DisableProfile"
- "ExtractDataFromPbiRsp"
- "ExtractNotificationListSeqNumbers"
- "ExtractProfileInfo"
- "ExtractResult"
- "GetData"
- "GetListOfIccids"
- "GetNextBppSegment"
- "GetParameters"
- "GetProfilesInfoList"
- "GetProvisioningSessions"
- "GetVinylType"
- "HandleNotifications"
- "HandleRefurbishProfileReference"
- "IsNotificationForTwoPhase"
- "IsNotificationSentRspSuccess"
- "IsProvTxIdAvailable"
- "ListInstallationNotifications"
- "LoadBPP"
- "NotificationSent"
- "Perform"
- "PostDataSync"
- "PowerDownSE"
- "PowerUpSE"
- "PrepareBPPInstallation"
- "Refurb"
- "RetrieveNotificationListForSeqNum"
- "ReverseProxyGetSettings"
- "ReverseProxyGetSettings_block_invoke"
- "SerializeDictIntoPlistData"
- "SetCardMode"
- "StoreData"
- "ValidatePerso"
- "VinylControllerObjDestroy"
- "VinyleUICCPerformOperationWithTransport"
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
- "getPairingParameters"
- "inRestoreOS_block_invoke"
- "inRestoreOS_block_invoke_2"
- "isAbsentOkay"
- "isNVRAMKeyPresent"
- "logEUICCData"
- "openChannel"
- "performNonUpdateOperation"
- "processAlderResponse"
- "statusCallback"
- "supportsVinylUpdate"

```
