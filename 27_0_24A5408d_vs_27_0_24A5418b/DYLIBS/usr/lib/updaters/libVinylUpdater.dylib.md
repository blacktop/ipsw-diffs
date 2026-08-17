## libVinylUpdater.dylib

> `/usr/lib/updaters/libVinylUpdater.dylib`

```diff

 178.0.0.0.0
-  __TEXT.__text: 0x4dc6c
+  __TEXT.__text: 0x4d594
   __TEXT.__init_offsets: 0x48
   __TEXT.__const: 0x53f1
-  __TEXT.__gcc_except_tab: 0x47bc
+  __TEXT.__gcc_except_tab: 0x47b4
   __TEXT.__oslogstring: 0x17c3
-  __TEXT.__cstring: 0xaf2d
-  __TEXT.__unwind_info: 0x1988
+  __TEXT.__cstring: 0xa6c3
+  __TEXT.__unwind_info: 0x1990
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x9a8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1296
+  Functions: 1295
   Symbols:   2145
-  CStrings:  1365
+  CStrings:  1279
 
Functions:
~ ____ZN15BBUpdaterCommon12BBUReadNVRAMEv_block_invoke : 588 -> 564
~ __ZN5eUICC5Perso19PersoImplementation7PerformERK7OptionsRKNSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEERNS5_10unique_ptrINS_15eUICCVinylValveENS5_14default_deleteISF_EEEE : 1244 -> 1204
~ __ZN5eUICC5Perso19PersoImplementation10ForcePersoERNSt3__16vectorIhNS2_9allocatorIhEEEERNS2_10unique_ptrINS_15eUICCVinylValveENS2_14default_deleteIS9_EEEE : 996 -> 964
~ __ZN5eUICC5Perso19PersoImplementation15InitPersoDeviceERNSt3__16vectorIhNS2_9allocatorIhEEEERNS2_10unique_ptrINS_15eUICCVinylValveENS2_14default_deleteIS9_EEEE : 888 -> 872
~ __ZN5eUICC5Perso19PersoImplementation15InitPersoServerERNSt3__16vectorIhNS2_9allocatorIhEEEERKNS2_12basic_stringIcNS2_11char_traitsIcEENS4_IcEEEERNS2_10unique_ptrINS_15eUICCVinylValveENS2_14default_deleteISG_EEEE : 2420 -> 2364
~ __ZN5eUICC5Perso19PersoImplementation23AuthenticatePersoDeviceERNSt3__16vectorIhNS2_9allocatorIhEEEERNS2_10unique_ptrINS_15eUICCVinylValveENS2_14default_deleteIS9_EEEE : 612 -> 604
~ __ZN5eUICC5Perso19PersoImplementation16GetWrapKeyServerERNSt3__16vectorIhNS2_9allocatorIhEEEE : 1620 -> 1588
~ __ZN5eUICC5Perso19PersoImplementation19FinalizePersoDeviceERNSt3__16vectorIhNS2_9allocatorIhEEEERNS2_10unique_ptrINS_15eUICCVinylValveENS2_14default_deleteIS9_EEEE : 428 -> 420
~ __ZN5eUICC5Perso19PersoImplementation14GetNonceServerERNSt3__16vectorIhNS2_9allocatorIhEEEERNS2_10unique_ptrINS_15eUICCVinylValveENS2_14default_deleteIS9_EEEE : 1688 -> 1640
~ __ZN5eUICC5Perso19PersoImplementation20CreateValidationBlobERNSt3__16vectorIhNS2_9allocatorIhEEEE : 1548 -> 1476
~ __ZN5eUICC5Perso19PersoImplementation19ValidatePersoDeviceERNSt3__16vectorIhNS2_9allocatorIhEEEERNS2_10unique_ptrINS_15eUICCVinylValveENS2_14default_deleteIS9_EEEE : 432 -> 424
~ __ZN5eUICC5Perso19PersoImplementation17SendReceiptServerERNSt3__16vectorIhNS2_9allocatorIhEEEE : 1152 -> 1136
~ __ZN5eUICC5Perso19PersoImplementation35SerializeKeyValuePairsIntoPlistDataEPPKvS4_lRNSt3__16vectorIhNS5_9allocatorIhEEEE : 784 -> 760
~ __ZN5eUICC5Perso19PersoImplementation29CreateDictionaryFromPlistDataEN3ctu2cf11CFSharedRefIK8__CFDataEERNS4_IK14__CFDictionaryEE : 820 -> 796
- _OUTLINED_FUNCTION_4
~ __ZN5eUICC18eUICCVinylICEValve12isAbsentOkayEv : 924 -> 908
~ __ZN5eUICC18eUICCVinylICEValve13DeleteProfileEh : 1168 -> 1152
~ __ZN5eUICC18eUICCVinylICEValve9StoreDataERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_Rt : 672 -> 656
~ __ZN5eUICC18eUICCVinylICEValve13InstallTicketEN3ctu2cf11CFSharedRefIK8__CFDataEE : 1288 -> 1256
~ __ZN5eUICC18eUICCVinylICEValve14StreamFirmwareEP8__CFData : 1776 -> 1728
~ __ZN5eUICC18eUICCVinylICEValve9InitPersoERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_ : 728 -> 712
~ __ZN5eUICC18eUICCVinylICEValve9AuthPersoERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_ : 728 -> 712
~ __ZN5eUICC18eUICCVinylICEValve13FinalizePersoERKNSt3__16vectorIhNS1_9allocatorIhEEEE : 672 -> 656
~ __ZN5eUICC18eUICCVinylICEValve13ValidatePersoERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_ : 732 -> 716
~ __ZN5eUICC18eUICCVinylICEValve17LpaSigningRequestERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_ : 784 -> 768
~ __ZN5eUICC18eUICCVinylICEValve17InstallPairingMSMERKNSt3__16vectorIhNS1_9allocatorIhEEEE : 668 -> 652
~ __ZN5eUICC18eUICCVinylICEValve21ManagePairingGetNonceERNSt3__16vectorIhNS1_9allocatorIhEEEE : 932 -> 916
~ __ZN5eUICC18eUICCVinylICEValve25ManagePairingAuthenticateERKNSt3__16vectorIhNS1_9allocatorIhEEEES7_ : 800 -> 784
~ __ZN5eUICC18eUICCVinylICEValve19geteUUIDBootstrapV2ERNSt3__16vectorIhNS1_9allocatorIhEEEE : 580 -> 564
~ __ZN5eUICC18eUICCVinylICEValve22getConfigIdBootstrapV2ERNSt3__16vectorIhNS1_9allocatorIhEEEE : 1084 -> 1044
~ __ZN5eUICC11GetSIMSKUID7PerformERKNS0_7RequestE : 468 -> 444
~ __ZN5eUICC13LETOMuxSwitch7PerformERKNS0_7RequestE : 1032 -> 976
~ __ZN5eUICC15VinylPollResultINS_13LETOMuxSwitch8Response8ContentsEEEiR13HDLCFrame_tagRT_P26TelephonyUtilTransport_tagjbjNSt3__18functionIFbRKS6_EEE : 428 -> 420
~ __ZN5eUICC18VinylManagePairing7PerformERKNS0_7RequestE : 496 -> 480
~ __ZN5eUICC15VinylPollResultINS_18VinylManagePairing8ResponseUt_EEEiR13HDLCFrame_tagRT_P26TelephonyUtilTransport_tagjbjNSt3__18functionIFbRKS6_EEE : 436 -> 428
~ __ZN5eUICC18VinylValidatePerso7PerformERKNS0_7RequestE : 572 -> 556
~ __ZN5eUICC15VinylPollResultINS_18VinylValidatePerso8Response8contentsEEEiR13HDLCFrame_tagRT_P26TelephonyUtilTransport_tagjbjNSt3__18functionIFbRKS6_EEE : 436 -> 428
~ __ZN5eUICC22VinylLPASigningRequest7PerformERKNS0_7RequestE : 960 -> 928
~ __ZN5eUICC15VinylPollResultINS_22VinylLPASigningRequest8Response8ContentsEEEiR13HDLCFrame_tagRT_P26TelephonyUtilTransport_tagjbjNSt3__18functionIFbRKS6_EEE : 436 -> 428
~ __ZN5eUICC26decodeConfigIdFromResponseEPKhmRNSt3__16vectorIhNS2_9allocatorIhEEEE : 824 -> 776
~ __ZN5eUICC23decodeEuuidFromResponseEPKhmRNSt3__16vectorIhNS2_9allocatorIhEEEE : 456 -> 424
~ __ZN5eUICC18eUICCVinylMAVValve11SetCardModeENS_11VinylOpModeEb : 488 -> 480
~ __ZN5eUICC18eUICCVinylMAVValve9StoreDataERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_Rt : 384 -> 376
~ __ZN5eUICC18eUICCVinylMAVValve13InstallTicketEN3ctu2cf11CFSharedRefIK8__CFDataEE : 424 -> 408
~ __ZN5eUICC18eUICCVinylMAVValve14StreamFirmwareEP8__CFData : 1176 -> 1140
~ __ZN5eUICC18eUICCVinylMAVValve9InitPersoERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_ : 520 -> 504
~ __ZN5eUICC18eUICCVinylMAVValve9AuthPersoERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_ : 504 -> 488
~ __ZN5eUICC18eUICCVinylMAVValve13FinalizePersoERKNSt3__16vectorIhNS1_9allocatorIhEEEE : 556 -> 540
~ __ZN5eUICC18eUICCVinylMAVValve13ValidatePersoERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_ : 556 -> 540
~ __ZN5eUICC18eUICCVinylMAVValve17LpaSigningRequestERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_ : 564 -> 548
~ __ZN5eUICC18eUICCVinylMAVValve17InstallPairingMSMERKNSt3__16vectorIhNS1_9allocatorIhEEEE : 380 -> 372
~ __ZN5eUICC18eUICCVinylMAVValve21ManagePairingGetNonceERNSt3__16vectorIhNS1_9allocatorIhEEEE : 412 -> 404
~ __ZN5eUICC18eUICCVinylMAVValve25ManagePairingAuthenticateERKNSt3__16vectorIhNS1_9allocatorIhEEEES7_ : 384 -> 376
~ __ZN17eUICCStateMachine8RecoveryEP13VinylFirmwareS1_RK7OptionsRNS_5StateERNSt3__110unique_ptrIN5eUICC15eUICCVinylValveENS7_14default_deleteISA_EEEE : 868 -> 844
~ __ZN17eUICCStateMachine10UpdateGoldEP13VinylFirmwareS1_RK7OptionsRNS_5StateERNSt3__110unique_ptrIN5eUICC15eUICCVinylValveENS7_14default_deleteISA_EEEE : 2048 -> 1992
~ __ZN17eUICCStateMachine10UpdateMainEP13VinylFirmwareS1_RK7OptionsRNS_5StateERNSt3__110unique_ptrIN5eUICC15eUICCVinylValveENS7_14default_deleteISA_EEEE : 3360 -> 3288
~ __Z8get_infoPPK14__CFDictionaryRN5eUICC14eUICCVinylData15vinylDataParamsE : 1660 -> 1652
~ _OUTLINED_FUNCTION_3 : 16 -> 20
+ _OUTLINED_FUNCTION_4
~ __Z23ReverseProxyGetSettingsRKNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE : 1520 -> 1488
~ __ZN5eUICC18eUICCVinylDALValveC2EPvibNSt3__110shared_ptrIvEE : 916 -> 920
~ __ZN5eUICC18eUICCVinylDALValve13InstallTicketEN3ctu2cf11CFSharedRefIK8__CFDataEE : 1364 -> 1340
~ __ZN5eUICC18eUICCVinylDALValve14StreamFirmwareEP8__CFData : 1972 -> 1948
~ _OUTLINED_FUNCTION_1 : 28 -> 36
~ _OUTLINED_FUNCTION_2 : 20 -> 28
- _OUTLINED_FUNCTION_5
~ ____Z14gBBULogMaskGetv_block_invoke : 44 -> 48
~ __Z13BBULogSetMaskm : 72 -> 76
~ __Z20BBULogParseDebugArgsN3ctu2cf11CFSharedRefIK14__CFDictionaryEE : 676 -> 672
~ __ZN22VinylDaleCommunication15createTransportEP26TelephonyUtilTransport_tag.cold.4 : 120 -> 112
~ __ZN22VinylDaleCommunication11openChannelEP26TelephonyUtilTransport_tag.cold.1 : 132 -> 124
~ __Z8get_infoPPK14__CFDictionaryRN5eUICC14eUICCVinylData15vinylDataParamsE.cold.1 : 160 -> 140
~ __ZN15VinylController23createTransportNoEventsEb.cold.1 : 160 -> 140
~ __ZN15VinylController13freeTransportEv.cold.1 : 156 -> 136
~ __ZN5eUICC18eUICCVinylDALValve15waitForeSIMBootEv.cold.1 : 104 -> 84
~ __ZN5eUICC18eUICCVinylDALValve7GetDataEv.cold.1 : 104 -> 84
~ __ZN5eUICC18eUICCVinylDALValve11SetCardModeENS_11VinylOpModeEb.cold.1 : 104 -> 84
~ __ZN5eUICC18eUICCVinylDALValve13DeleteProfileEh.cold.1 : 104 -> 84
~ __ZN5eUICC18eUICCVinylDALValve9StoreDataERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_Rt.cold.1 : 104 -> 84
~ __ZN5eUICC18eUICCVinylDALValve13InstallTicketEN3ctu2cf11CFSharedRefIK8__CFDataEE.cold.1 : 104 -> 84
~ __ZN5eUICC18eUICCVinylDALValve9InitPersoERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_.cold.1 : 104 -> 84
~ __ZN5eUICC18eUICCVinylDALValve9AuthPersoERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_.cold.1 : 104 -> 84
~ __ZN5eUICC18eUICCVinylDALValve13FinalizePersoERKNSt3__16vectorIhNS1_9allocatorIhEEEE.cold.1 : 104 -> 84
~ __ZN5eUICC18eUICCVinylDALValve17LpaSigningRequestERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_.cold.1 : 100 -> 80
~ __ZN5eUICC18eUICCVinylDALValve13ValidatePersoERKNSt3__16vectorIhNS1_9allocatorIhEEEERS5_.cold.1 : 104 -> 84
~ __ZN5eUICC18eUICCVinylDALValve17InstallPairingMSMERKNSt3__16vectorIhNS1_9allocatorIhEEEE.cold.1 : 104 -> 84
~ __ZN5eUICC18eUICCVinylDALValve21ManagePairingGetNonceERNSt3__16vectorIhNS1_9allocatorIhEEEE.cold.1 : 104 -> 84
~ __ZN5eUICC18eUICCVinylDALValve25ManagePairingAuthenticateERKNSt3__16vectorIhNS1_9allocatorIhEEEES7_.cold.1 : 104 -> 84
CStrings:
+ "VinylRestore-178~6921"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/CommandDrivers/eUICCVinylICEValve.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/CommandDrivers/eUICCVinylValve.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/Communication/Eureka/VinylETLEUICC.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/Support/BBUPurpleReverseProxy.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/Update/Perso/eUICCPerso.cpp"
- "AuthPerso"
- "AuthenticatePersoDevice"
- "BBUFDRLogHandler"
- "BBULogPrintBinaryDelegate"
- "BBUReadNVRAM"
- "BBUReadNVRAM_block_invoke"
- "CreateDictionaryFromPlistData"
- "CreateValidationBlob"
- "DeleteProfile"
- "FinalizePerso"
- "FinalizePersoDevice"
- "ForcePerso"
- "GetData"
- "GetData_EoS"
- "GetNonceServer"
- "GetSIMSKUString"
- "GetSimMuxCfg"
- "GetValve"
- "GetVinylType"
- "GetWrapKeyServer"
- "HardwareHasESIM_block_invoke"
- "HowToProceed"
- "InitPerso"
- "InitPersoDevice"
- "InitPersoServer"
- "InstallPairingMSM"
- "InstallTicket"
- "LpaSigningRequest"
- "ManagePairingAuthenticate"
- "ManagePairingGetNonce"
- "Perform"
- "PostDataSync"
- "PowerDownSE"
- "PowerUpSE"
- "Refurb"
- "ResetCard"
- "ReverseProxyGetSettings"
- "ReverseProxyGetSettings_block_invoke"
- "Run"
- "SendReceiptServer"
- "SerializeKeyValuePairsIntoPlistData"
- "SetCardMode"
- "Step"
- "StoreData"
- "StreamFirmware"
- "SwitchSimMuxCfgPolled"
- "ValidatePerso"
- "ValidatePersoDevice"
- "VinylControllerObjDestroy"
- "VinylRestore-178~6332"
- "bbupdater_log"
- "checkEOSDev"
- "collectCoreDump"
- "createTransportNoEvents"
- "createTransport_block_invoke_2"
- "decodeConfigIdFromResponse"
- "decodeEuuidFromResponse"
- "freeTransport"
- "freeTransportSync"
- "freeTransportSync_block_invoke"
- "freeTransportSync_block_invoke_2"
- "getConfigIdBootstrapV2"
- "getECID_block_invoke"
- "getEID"
- "getPairingIdentifier"
- "getParamUpdateOperation"
- "get_info"
- "geteUUIDBootstrapV2"
- "inRestoreOS_block_invoke"
- "inRestoreOS_block_invoke_2"
- "isAbsentOkay"
- "isLETOCapable"
- "isNVRAMKeyPresent"
- "logEUICCData"
- "openChannel"
- "operator()"
- "perform"
- "startRouterServer"
- "statusCallback"
- "stopRouterServer"
- "supportsVinylUpdate"
- "waitForeSIMBoot"
```
