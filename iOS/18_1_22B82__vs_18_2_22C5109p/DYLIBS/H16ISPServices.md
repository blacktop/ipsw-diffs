## H16ISPServices

> `/System/Library/PrivateFrameworks/H16ISPServices.framework/H16ISPServices`

```diff

-3.114.0.0.0
-  __TEXT.__text: 0x20254
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x829f
+3.316.903.0.0
+  __TEXT.__text: 0x1e0ac
+  __TEXT.__auth_stubs: 0x680
   __TEXT.__gcc_except_tab: 0x594
-  __TEXT.__unwind_info: 0x460
+  __TEXT.__cstring: 0x8e3f
+  __TEXT.__const: 0x58
+  __TEXT.__unwind_info: 0x2a8
   __DATA_CONST.__got: 0x168
   __DATA_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__cfstring: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libIOAccessoryManager.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 433
-  Symbols:   830
-  CStrings:  1473
+  Functions: 351
+  Symbols:   628
+  CStrings:  1500
 
Symbols:
+ _ispirexclavekitmodule_ispirexclavekit__destruct
+ _ispirexclavekitmodule_ispirexclavekit__server_start_owned
+ _ispirexclavekitmodule_ispirexclavekit__server_stop
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdadsettings
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeinitsettinggetv2
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchaeintegrationgainsetv2
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchdpcset
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchisconcurrent
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchrunkitaev2
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchrunkitmdv2
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchsensormetadatav3
+ _ispirexclavekitmodule_ispirexclavekit_sendcmddebugcapability
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdexfiltration
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdinfiltration
+ _isprgbexclavekitmodule_isprgbexclavekit__destruct
+ _isprgbexclavekitmodule_isprgbexclavekit__server_start_owned
+ _isprgbexclavekitmodule_isprgbexclavekit__server_stop
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeinitsettinggetv2
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchaeintegrationgainsetv2
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchdpcset
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchisconcurrent
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchpdpset
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitaev2
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitandk
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitmd
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitmdv2
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitperception
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchsensormetadatav3
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchsetperceptionframerate
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmddebugcapability
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdexfiltration
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdinfiltration
+ _memmove
+ _tb_client_connection_destruct
+ _tb_endpoint_set_interface_identifier
+ _tb_service_connection_destruct
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- _tb_message_configure_recieved
- _tb_message_construct
- _tb_message_destruct
- _tb_transport_message_buffer_wrap_buffer
CStrings:
+ "Shared Depth to Position Debug"
+ "TB_ASSERT: (ispirexclavekitmodule_ispexclavecoreadsettings__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreAdSettings\""
+ "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechdpcset__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChDPCSet\""
+ "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechsensormetadatav3__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChSensorMetadataV3\""
+ "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorefiltration__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreFiltration\""
+ "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechdpcset__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChDPCSet\""
+ "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechsensormetadatav3__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChSensorMetadataV3\""
+ "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorefiltration__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreFiltration\""
+ "TB_ASSERT: (server->sendcmdadsettings != NULL) && \"implementation for sendCmdAdSettings is not present\""
+ "TB_ASSERT: (server->sendcmdchaeinitsettinggetv2 != NULL) && \"implementation for sendCmdChAEInitSettingGetV2 is not present\""
+ "TB_ASSERT: (server->sendcmdchaeintegrationgainsetv2 != NULL) && \"implementation for sendCmdChAEIntegrationGainSetV2 is not present\""
+ "TB_ASSERT: (server->sendcmdchdpcset != NULL) && \"implementation for sendCmdChDPCSet is not present\""
+ "TB_ASSERT: (server->sendcmdchisconcurrent != NULL) && \"implementation for sendCmdChIsConcurrent is not present\""
+ "TB_ASSERT: (server->sendcmdchrunkitaev2 != NULL) && \"implementation for sendCmdChRunKitAEV2 is not present\""
+ "TB_ASSERT: (server->sendcmdchrunkitandk != NULL) && \"implementation for sendCmdChRunKitANDK is not present\""
+ "TB_ASSERT: (server->sendcmdchrunkitmdv2 != NULL) && \"implementation for sendCmdChRunKitMDV2 is not present\""
+ "TB_ASSERT: (server->sendcmdchrunkitperception != NULL) && \"implementation for sendCmdChRunKitPerception is not present\""
+ "TB_ASSERT: (server->sendcmdchsensormetadatav3 != NULL) && \"implementation for sendCmdChSensorMetadataV3 is not present\""
+ "TB_ASSERT: (server->sendcmdchsetperceptionframerate != NULL) && \"implementation for sendCmdChSetPerceptionFrameRate is not present\""
+ "TB_ASSERT: (server->sendcmddebugcapability != NULL) && \"implementation for sendCmdDebugCapability is not present\""
+ "TB_ASSERT: (server->sendcmdexfiltration != NULL) && \"implementation for sendCmdExfiltration is not present\""
+ "TB_ASSERT: (server->sendcmdinfiltration != NULL) && \"implementation for sendCmdInfiltration is not present\""
+ "isSifrFrameDecimated"
+ "sensorSifrBayerBinFactor"
+ "sensorSifrQuadraBinFactor"
+ "sifrBinHeight"
+ "sifrBinWidth"

```
