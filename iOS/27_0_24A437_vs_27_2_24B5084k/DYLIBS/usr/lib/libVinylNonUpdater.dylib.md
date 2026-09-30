## libVinylNonUpdater.dylib

> `/usr/lib/libVinylNonUpdater.dylib`

```diff

 178.0.0.0.0
-  __TEXT.__text: 0x58558
+  __TEXT.__text: 0x590a0
   __TEXT.__init_offsets: 0x54
-  __TEXT.__const: 0x7424
-  __TEXT.__gcc_except_tab: 0x4e90
-  __TEXT.__cstring: 0xba3f
+  __TEXT.__const: 0x7484
+  __TEXT.__gcc_except_tab: 0x4e94
+  __TEXT.__cstring: 0xca08
   __TEXT.__oslogstring: 0x7c
   __TEXT.__unwind_info: 0x22e8
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__cfstring: 0xcc0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0xe88
-  __DATA.__data: 0xc98
+  __DATA.__data: 0xcc0
   __DATA.__common: 0x48
   __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__common: 0x18

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 1700
-  Symbols:   3148
-  CStrings:  1411
+  Symbols:   3158
+  CStrings:  1555
 
Symbols:
+ ___der_key_state_abs_last_mesa_auth
+ ___der_key_state_abs_last_mesa_unlock
+ ___der_key_state_abs_last_passcode_auth
+ ___der_key_state_abs_last_passcode_unlock
+ ___der_key_state_abs_lock_time
+ _der_key_state_abs_last_mesa_auth
+ _der_key_state_abs_last_mesa_unlock
+ _der_key_state_abs_last_passcode_auth
+ _der_key_state_abs_last_passcode_unlock
+ _der_key_state_abs_lock_time
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/CommandDrivers/eUICCVinylICEValve.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/CommandDrivers/eUICCVinylValve.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/Communication/Eureka/VinylETLEUICC.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/NonUpdate/VinylClearMetadata.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProv.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProvSessionData.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/NonUpdate/VinylTwoPhaseProvUtil.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/Support/BBUPurpleReverseProxy.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/Update/Perso/eUICCPerso.cpp"
+ "AuthPerso"
+ "AuthenticatePersoDevice"
+ "BBUFDRLogHandler"
+ "BBULogPrintBinaryDelegate"
+ "BBUReadNVRAM"
+ "BBUReadNVRAM_block_invoke"
+ "CheckIftheIccidIsPresent"
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
+ "GetProfilesInfoListOnlyIccid"
+ "GetProvisioningSessions"
+ "GetSIMSKUString"
+ "GetSimMuxCfg"
+ "GetValve"
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
+ "ListInstallationNotifications"
+ "LoadBPP"
+ "LpaSigningRequest"
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
+ "SwitchSimMuxCfgPolled"
+ "ValidatePerso"
+ "ValidatePersoDevice"
+ "VinylControllerObjDestroy"
+ "VinyleUICCPerformOperationWithLinkAndLogSync"
+ "VinyleUICCPerformOperationWithTransportAndLogSync"
+ "bbupdater_log"
+ "bootstrapProvisioning"
+ "checkBCOMDeleteNotifications"
+ "checkEOSDev"
+ "collectCoreDump"
+ "configIdProvisioning"
+ "convertGbppToPbiBpp"
+ "create"
+ "createLPASigningRequest"
+ "createMapMetaDataPayLoad"
+ "createTransport"
+ "createTransportNoEvents"
+ "createTransport_block_invoke_2"
+ "decodeConfigIdFromResponse"
+ "decodeEuuidFromResponse"
+ "deleteNotification"
+ "extractDataFromPbiReq"
+ "extractDataFromPbiRsp"
+ "extractDataFromPir"
+ "freeTransport"
+ "freeTransportSync"
+ "freeTransportSync_block_invoke"
+ "freeTransportSync_block_invoke_2"
+ "getConfigIdBootstrapV2"
+ "getECID_block_invoke"
+ "getEID"
+ "getPairingIdentifier"
+ "getPairingParameters"
+ "get_info"
+ "geteUUIDBootstrapV2"
+ "inRestoreOS_block_invoke"
+ "inRestoreOS_block_invoke_2"
+ "isAbsentOkay"
+ "isLETOCapable"
+ "isNVRAMKeyPresent"
+ "listDeleteNotifications"
+ "logEUICCData"
+ "managePairingInstallMSM"
+ "openChannel"
+ "operator()"
+ "parseLPASignedData"
+ "perform"
+ "performNonUpdateOperation"
+ "postDataAndGetServerResponse"
+ "processAlderResponse"
+ "retrieveNotificationListForSeqNum"
+ "sendCommandNonceToMarinaServer"
+ "sendEUICCdataFeedToMarinaServer"
+ "sendLPASigningRequestToEUICC"
+ "startRouterServer"
+ "statusCallback"
+ "stopRouterServer"
+ "supportsVinylUpdate"
+ "validateDeleteBCOMNotification"
+ "verifyPairing"
+ "waitForeSIMBoot"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
```
