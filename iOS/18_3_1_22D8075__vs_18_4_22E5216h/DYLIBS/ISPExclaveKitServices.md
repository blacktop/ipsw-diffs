## ISPExclaveKitServices

> `/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/ISPExclaveKitServices`

```diff

-3.411.0.0.0
-  __TEXT.__text: 0x19a08
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x62c
-  __TEXT.__oslogstring: 0x906
-  __TEXT.__cstring: 0x16ef
-  __TEXT.__unwind_info: 0x470
-  __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0xde8
-  __AUTH_CONST.__auth_got: 0x150
-  __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__cfstring: 0x120
-  __DATA.__data: 0x5e50
-  __DATA.__common: 0xd007d
+3.509.0.0.0
+  __TEXT.__text: 0x32190
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__const: 0x140
+  __TEXT.__gcc_except_tab: 0xa3c
+  __TEXT.__oslogstring: 0x21a5
+  __TEXT.__cstring: 0x3b10
+  __TEXT.__unwind_info: 0x7f0
+  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__const: 0x1300
+  __AUTH_CONST.__auth_got: 0x230
+  __AUTH_CONST.__auth_ptr: 0x18
+  __AUTH_CONST.__cfstring: 0x200
+  __DATA.__data: 0xd67fd
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 527
-  Symbols:   624
-  CStrings:  158
+  Functions: 1043
+  Symbols:   1216
+  CStrings:  368
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFEqual
+ _CFGetTypeID
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _CFPreferencesCopyValue
+ _CFStringCompare
+ _CFStringGetCStringPtr
+ _CFStringGetIntValue
+ _CFStringGetSystemEncoding
+ _CFStringGetTypeID
+ __Z15channelStateGetj
+ __Z17channelStateResetv
+ __Z18channelStateUpdatej22eIspExclaveKitChSignal
+ __Z20exclaveKitDefaultGetP21ISPExclaveKitDefaults19eExclaveKitDefaults
+ __Z20getConfigurationType27ISPExclaveConfigurationType
+ __Z21exclaveKitReadDefaultPK10__CFStringS1_i
+ __Z22exclaveKitDefaultsInitP21ISPExclaveKitDefaults
+ __Z23exclaveKitDefaultsResetP21ISPExclaveKitDefaults
+ __Z28_generateIdlAlgoEnableBitMapPb
+ __Z34_ispExclaveKitCommandChAdConfigSetj
+ __Z35searApprovedInterfaceSwitcherUpdateb
+ __Z36ispExclaveKitCommandChOnSearApprovedP20sExclaveKitIspCmdHdr
+ __Z37ispExclaveKitCommandChOffSearApprovedP20sExclaveKitIspCmdHdr
+ __Z38ispExclaveKitCommandChStopSearApprovedP20sExclaveKitIspCmdHdr
+ __Z39_ispExclaveKitCommandChFacekitConfigSetj
+ __Z39ispExclaveKitCommandChRunAdSearApprovedP20sExclaveKitIspCmdHdr
+ __Z39ispExclaveKitCommandChRunAeSearApprovedP20sExclaveKitIspCmdHdr
+ __Z39ispExclaveKitCommandChRunFdSearApprovedP20sExclaveKitIspCmdHdr
+ __Z39ispExclaveKitCommandChRunMdSearApprovedP20sExclaveKitIspCmdHdr
+ __Z39ispExclaveKitCommandChStartSearApprovedP20sExclaveKitIspCmdHdr
+ __Z40ispExclaveKitCommandChFacekitConfigSetV2P20sExclaveKitIspCmdHdr
+ __Z40ispExclaveKitCommandChLscSetSearApprovedP20sExclaveKitIspCmdHdr
+ __Z40ispExclaveKitCommandChPdpSetSearApprovedP20sExclaveKitIspCmdHdr
+ __Z40ispExclaveKitCommandChRunIspSearApprovedP20sExclaveKitIspCmdHdr
+ __Z41_ispExclaveKitCommandChFacekitConfigSetV2j
+ __Z41ispExclaveKitCommandChInfoSetSearApprovedP20sExclaveKitIspCmdHdr
+ __Z41ispExclaveKitCommandChRunAndkSearApprovedP20sExclaveKitIspCmdHdr
+ __Z41ispExclaveKitCommandChRunAnstSearApprovedP20sExclaveKitIspCmdHdr
+ __Z42_ispExclaveKitCommandChPerceptionConfigSetj
+ __Z43_ispExclaveKitCommandAlgoEnableSearApprovedj
+ __Z43ispExclaveKitCommandChRunFacekitFirstPassV2P20sExclaveKitIspCmdHdr
+ __Z44ispExclaveKitCommandChRunFacekitSecondPassV2P20sExclaveKitIspCmdHdr
+ __Z45ispExclaveKitCommandChAdConfigSetSearApprovedP20sExclaveKitIspCmdHdr
+ __Z46ispExclaveKitCommandChExfiltrationSearApprovedP20sExclaveKitIspCmdHdr
+ __Z46ispExclaveKitCommandChInfiltrationSearApprovedP20sExclaveKitIspCmdHdr
+ __Z46ispExclaveKitCommandChPropertyReadSearApprovedP20sExclaveKitIspCmdHdr
+ __Z46ispExclaveKitCommandChSendMetadataSearApprovedP20sExclaveKitIspCmdHdr
+ __Z47ispExclaveKitCommandChPropertyWriteSearApprovedP20sExclaveKitIspCmdHdr
+ __Z47ispExclaveKitCommandChRunPerceptionSearApprovedP20sExclaveKitIspCmdHdr
+ __Z49ispExclaveKitCommandChCameraConfigSetSearApprovedP20sExclaveKitIspCmdHdr
+ __Z49ispExclaveKitCommandChDebugCapabilitySearApprovedP20sExclaveKitIspCmdHdr
+ __Z50ispExclaveKitCommandChAeFlickerFreqSetSearApprovedP20sExclaveKitIspCmdHdr
+ __Z50ispExclaveKitCommandChAeInitSettingGetSearApprovedP20sExclaveKitIspCmdHdr
+ __Z50ispExclaveKitCommandChFrameRateControlSearApprovedP20sExclaveKitIspCmdHdr
+ __Z51ispExclaveKitCommandChAeFrameRateMaxGetSearApprovedP20sExclaveKitIspCmdHdr
+ __Z51ispExclaveKitCommandChAeFrameRateMaxSetSearApprovedP20sExclaveKitIspCmdHdr
+ __Z51ispExclaveKitCommandChAeFrameRateMinGetSearApprovedP20sExclaveKitIspCmdHdr
+ __Z51ispExclaveKitCommandChAeFrameRateMinSetSearApprovedP20sExclaveKitIspCmdHdr
+ __Z51ispExclaveKitCommandChConcurrentFlagSetSearApprovedP20sExclaveKitIspCmdHdr
+ __Z54_ispExclaveKitCommandChPerceptionConfigSetSearApprovedj
+ __Z57ispExclaveKitCommandChConfigurationStatusReadSearApprovedP20sExclaveKitIspCmdHdr
+ _exclaveKitDefaultsNameList
+ _kCFBooleanTrue
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _memset
+ _strtol
+ _tb_message_configure_received
+ _tb_message_construct
+ _tb_message_measure_subrange
+ _tb_message_precheck_decoding
+ _tb_message_precheck_encoding
+ _tb_message_raw_decode_bool
+ _tb_message_raw_decode_f32
+ _tb_message_raw_decode_f64
+ _tb_message_raw_decode_s32
+ _tb_message_raw_decode_s8
+ _tb_message_raw_decode_u16
+ _tb_message_raw_decode_u32
+ _tb_message_raw_decode_u64
+ _tb_message_raw_decode_u8
+ _tb_message_raw_encode_bool
+ _tb_message_raw_encode_f32
+ _tb_message_raw_encode_s16
+ _tb_message_raw_encode_s32
+ _tb_message_raw_encode_s8
+ _tb_message_raw_encode_u16
+ _tb_message_raw_encode_u32
+ _tb_message_raw_encode_u64
+ _tb_message_raw_encode_u8
+ _tb_message_subrange
+ _tb_transport_message_buffer_wrap_buffer
- _ISPExclaveKitCmdChAEInitSettingGet
- _ISPExclaveKitCmdChRunKitAE
- _ISPExclaveKitCmdChRunKitER
- _ISPExclaveKitCmdChRunKitISP
- _ISPExclaveKitCmdChSensorMetadata
- _ISPExclaveKitCmdChStart
- _ISPExclaveKitCmdChStop
- _ISPExclaveKitCmdExclaveChCameraConfigSet
- _ISPExclaveKitCmdOff
- _ISPExclaveKitCmdOn
- _ISPExclaveKitServicesInit
- __Z34_ispExclaveKitCommandChAdConfigSetv
- __Z39_ispExclaveKitCommandChFacekitConfigSetv
- __Z42_ispExclaveKitCommandChPerceptionConfigSetv
- _conclaveServiceNames
- _session
- _tb_message_decode_s32
- _tb_message_encode_bool
- _tb_message_encode_f32
- _tb_message_encode_s16
- _tb_message_encode_s32
- _tb_message_encode_s8
- _tb_message_encode_u16
- _tb_message_encode_u32
- _tb_message_encode_u64
- _tb_message_encode_u8
CStrings:
+ "%s:%d - CMD_CH_DEBUG_CAPABILITY legacy path\n"
+ "%s:%d - CMD_CH_DEBUG_CAPABILITY new path\n"
+ "%s:%d - CMD_CH_EXFILTRATION legacy path\n"
+ "%s:%d - CMD_CH_EXFILTRATION new path\n"
+ "%s:%d - CMD_CH_INFILTRATION legacy path\n"
+ "%s:%d - CMD_CH_INFILTRATION new path\n"
+ "%s:%d - CMD_CH_PROPERTY_READ legacy path\n"
+ "%s:%d - CMD_CH_PROPERTY_READ new path\n"
+ "%s:%d - CMD_CH_PROPERTY_WRITE legacy path\n"
+ "%s:%d - CMD_CH_PROPERTY_WRITE new path\n"
+ "%s:%d - Channel OFF legacy path\n"
+ "%s:%d - Channel OFF new path\n"
+ "%s:%d - Channel ON legacy path\n"
+ "%s:%d - Channel ON new path\n"
+ "%s:%d - Channel camera config set legacy path\n"
+ "%s:%d - Channel camera config set new path\n"
+ "%s:%d - Channel concurrent flag set legacy path\n"
+ "%s:%d - Channel concurrent flag set new path\n"
+ "%s:%d - Channel fps control legacy path\n"
+ "%s:%d - Channel fps control new path\n"
+ "%s:%d - Channel info set legacy path\n"
+ "%s:%d - Channel info set new path\n"
+ "%s:%d - Channel run ISP legacy path\n"
+ "%s:%d - Channel run ISP new path\n"
+ "%s:%d - Channel start legacy path\n"
+ "%s:%d - Channel start new path\n"
+ "%s:%d - Channel stop legacy path\n"
+ "%s:%d - Channel stop new path\n"
+ "%s:%d - Configuration status read legacy path\n"
+ "%s:%d - Configuration status read new path\n"
+ "%s:%d - EK isReleaseVariant=%d\n"
+ "%s:%d - ERROR: Channel camera configuration being set doesn't match with the data received from EK\n"
+ "%s:%d - ERROR: Expected VCP index in Ch info: %d\n"
+ "%s:%d - ERROR: Expected extrinsicsrotation in Ch info: [%f %f %f %f %f %f %f %f %f]\n"
+ "%s:%d - ERROR: Expected extrinsicstranslation in Ch info: [%f %f %f] \n"
+ "%s:%d - ERROR: Expected firstPixelColor in Ch info: %d\n"
+ "%s:%d - ERROR: Expected isIRSensor in Ch info: %u\n"
+ "%s:%d - ERROR: Expected lenslimitedocshift in Ch info: %d %d\n"
+ "%s:%d - ERROR: Expected window percentage in Ch info: %u %u\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_INPUT intrinsic[%d]=%f > %f\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_OUTPUT\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_STATE: chIdx=%d\n"
+ "%s:%d - ERROR: Invalid VCP index in Ch info: %d\n"
+ "%s:%d - ERROR: Invalid config number received\n"
+ "%s:%d - ERROR: Invalid extrinsicsrotation in Ch info: [%f %f %f %f %f %f %f %f %f]\n"
+ "%s:%d - ERROR: Invalid extrinsicstranslation in Ch info: [%f %f %f] \n"
+ "%s:%d - ERROR: Invalid firstPixelColor in Ch info: %d\n"
+ "%s:%d - ERROR: Invalid isIRSensor in Ch info: %u\n"
+ "%s:%d - ERROR: Invalid lenslimitedocshift in Ch info: %d %d\n"
+ "%s:%d - ERROR: Invalid window percentage in Ch info: %u %u\n"
+ "%s:%d - ERROR: cachedCmdRes=%d\n"
+ "%s:%d - ERROR: face number exceed max %zu in iteration\n"
+ "%s:%d - ERROR: object number exceed max %zu in iteration\n"
+ "%s:%d - ERROR: unkonw perception return code %llx\n"
+ "%s:%d - Expected values: %u %u %u %u %u %u %u %u %u %u %u %u\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_ANDK handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_ANST handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_ATTENTION_AWARENESS handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_AUTO_EXPOSURE handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_CHANNEL_STREAMING_CONTROL handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_DEBUG handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_FACEKIT handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_HARDWARE_DEFAULT_CONFIG handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_ISP_MANAGER handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_MOTION_TO_WAKE handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_PERCEPTION handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_STREAMING_CONTROL handler is created\n"
+ "%s:%d - Invalid Configuration type: %d\n"
+ "%s:%d - Received values: %u %u %u %u %u %u %u %u %u %u %u %u\n"
+ "%s:%d - SearApprovedPathFlag=%d\n"
+ "%s:%d - Skip downstream node\n"
+ "%s:%d - WARN: minFps is not equal to minFps. received: %u, expected : %u\n"
+ "%s:%d - [Conclave] (EKType:%d) Failed to setup AA client\n\n"
+ "%s:%d - [Conclave] (EKType:%d) Failed to setup ANDK client\n\n"
+ "%s:%d - [Conclave] (EKType:%d) Failed to setup ANST client\n\n"
+ "%s:%d - [Conclave] (EKType:%d) Failed to setup channel HW default config client\n\n"
+ "%s:%d - [Conclave] (EKType:%d) Failed to setup channel streaming control client\n\n"
+ "%s:%d - [Conclave] (EKType:%d) Failed to setup client\n\n"
+ "%s:%d - [Conclave] (EKType:%d) Failed to setup facekit client\n\n"
+ "%s:%d - [Conclave] (EKType:%d) Failed to setup streaming control client\n\n"
+ "%s:%d - after calling IDL\n"
+ "%s:%d - before calling IDL\n"
+ "%s:%d - before calling new IDL %d %d\n"
+ "%s:%d - channel state: !ISP_EXCLAVEKIT_CHANNEL_STATE_OFF, issue the request, res=%d\n"
+ "%s:%d - channel state: ISP_EXCLAVEKIT_CHANNEL_STATE_OFF, cache the request\n"
+ "%s:%d - facekit: debug 0\n"
+ "%s:%d - illegal chIdx=%d\n"
+ "%s:%d - illegal transition signal=%d, currentState=%d\n"
+ "%s:%d - in release mode, ispExclaveKitCommandChDebugCapabilitySearApproved is not available\n"
+ "%s:%d - in release mode, ispExclaveKitCommandChExfiltrationSearApproved is not available\n"
+ "%s:%d - in release mode, ispExclaveKitCommandChInfiltrationSearApproved is not available\n"
+ "%s:%d - in release mode, ispExclaveKitCommandChPropertyReadSearApproved is not available\n"
+ "%s:%d - in release mode, ispExclaveKitCommandChPropertyWriteSearApproved is not available\n"
+ "%s:%d - isUsingSearApprovedPath=%d\n"
+ "%s:%d - ispExclaveKitCommandChRunAndk\n"
+ "%s:%d - ispExclaveKitCommandChRunAndkSearApproved\n"
+ "%s:%d - run AD SearApproved\n"
+ "%s:%d - run AD legacy path\n"
+ "%s:%d - run ANDK SearApproved\n"
+ "%s:%d - run ANDK legacy path\n"
+ "%s:%d - run ANST SearApproved\n"
+ "%s:%d - run ANST legacy path\n"
+ "%s:%d - run FD SearApproved\n"
+ "%s:%d - run FD legacy path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_AE_FLICKER_FREQ_SET legacy path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_AE_FLICKER_FREQ_SET new path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_AE_FRAME_RATE_MAX_GET legacy path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_AE_FRAME_RATE_MAX_GET new path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_AE_FRAME_RATE_MAX_SET legacy path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_AE_FRAME_RATE_MAX_SET new path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_AE_FRAME_RATE_MIN_GET legacy path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_AE_FRAME_RATE_MIN_GET new path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_AE_FRAME_RATE_MIN_SET legacy path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_AE_FRAME_RATE_MIN_SET new path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_AE_INIT_SETTING_GET legacy path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_AE_INIT_SETTING_GET new path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_RUN_AE legacy path\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_RUN_AE new path\n"
+ "%s:%d - run LSC SET legacy path\n"
+ "%s:%d - run LSC SET new path\n"
+ "%s:%d - run PDP SET legacy path\n"
+ "%s:%d - run PDP SET new path\n"
+ "%s:%d - run facekit SearApproved\n"
+ "%s:%d - run motionToWake SearApproved\n"
+ "%s:%d - run motionToWake legacy path\n"
+ "%s:%d - run perception SearApproved\n"
+ "%s:%d - run perception legacy path\n"
+ "%s:%d - signal=%d, state=%d\n"
+ "%s:%d - trackedFaceValid %d confidence %u\n"
+ "%s:%d - wrong channel state\n"
+ "/Library/Caches/com.apple.xbs/Sources/ExclaveSISP_XNU_products/XNU/EKServiceFramework/ISPExclaveKitServices_C.c"
+ "0"
+ "I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8"
+ "I8@?0"
+ "TB_ASSERT: (anstmodule_anstfacev1502__decode(msg, &item) == TB_ERROR_SUCCESS) && \"failed to decode type: AnstModule.ANSTFaceV1502\""
+ "TB_ASSERT: (anstmodule_anstobjectv1502__decode(msg, &item) == TB_ERROR_SUCCESS) && \"failed to decode type: AnstModule.ANSTObjectV1502\""
+ "TB_ASSERT: (err == TB_ERROR_SUCCESS) && \"failed to wrap packed buffer\""
+ "TB_ASSERT: (vErr == TB_ERROR_SUCCESS) && \"tb_message_subrange failed\""
+ "TB_FATAL: invalid tag in array metadata: 0x%x"
+ "TB_FATAL: invalid tag in array metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: invalid value: unexpected bits, 0x%llx"
+ "TB_FATAL: invalid value: unexpected bits, 0x%llx (%s:%d)\n"
+ "_ispExclaveKitCommandAlgoEnableSearApproved"
+ "_ispExclaveKitCommandChFacekitConfigSetV2"
+ "_ispExclaveKitCommandChPerceptionConfigSetSearApproved"
+ "channelStateGet"
+ "channelStateUpdate"
+ "com.apple.coremedia"
+ "decodeAnstResultSearApproved"
+ "exclaveKitDefaultsInit"
+ "false"
+ "getAdSetField"
+ "getConfigurationType"
+ "ispExclaveKitCommandChAdConfigSetSearApproved"
+ "ispExclaveKitCommandChAeFlickerFreqSetSearApproved"
+ "ispExclaveKitCommandChAeFrameRateMaxGetSearApproved"
+ "ispExclaveKitCommandChAeFrameRateMaxSetSearApproved"
+ "ispExclaveKitCommandChAeFrameRateMinGetSearApproved"
+ "ispExclaveKitCommandChAeFrameRateMinSetSearApproved"
+ "ispExclaveKitCommandChAeInitSettingGetSearApproved"
+ "ispExclaveKitCommandChCameraConfigSetSearApproved"
+ "ispExclaveKitCommandChConcurrentFlagSetSearApproved"
+ "ispExclaveKitCommandChConfigurationStatusReadSearApproved"
+ "ispExclaveKitCommandChDebugCapabilitySearApproved"
+ "ispExclaveKitCommandChExfiltrationSearApproved"
+ "ispExclaveKitCommandChFacekitConfigSetV2"
+ "ispExclaveKitCommandChFrameRateControlSearApproved"
+ "ispExclaveKitCommandChInfiltrationSearApproved"
+ "ispExclaveKitCommandChInfoSetSearApproved"
+ "ispExclaveKitCommandChLscSetSearApproved"
+ "ispExclaveKitCommandChOffSearApproved"
+ "ispExclaveKitCommandChOnSearApproved"
+ "ispExclaveKitCommandChPdpSetSearApproved"
+ "ispExclaveKitCommandChPropertyReadSearApproved"
+ "ispExclaveKitCommandChPropertyWriteSearApproved"
+ "ispExclaveKitCommandChRunAdSearApproved"
+ "ispExclaveKitCommandChRunAeSearApproved"
+ "ispExclaveKitCommandChRunAndkSearApproved"
+ "ispExclaveKitCommandChRunAnstSearApproved"
+ "ispExclaveKitCommandChRunFacekitFirstPassV2"
+ "ispExclaveKitCommandChRunFacekitSecondPassV2"
+ "ispExclaveKitCommandChRunFdSearApproved"
+ "ispExclaveKitCommandChRunIspSearApproved"
+ "ispExclaveKitCommandChRunMdSearApproved"
+ "ispExclaveKitCommandChRunPerceptionSearApproved"
+ "ispExclaveKitCommandChRunPerceptionSearApproved_block_invoke"
+ "ispExclaveKitCommandChSendMetadataSearApproved"
+ "ispExclaveKitCommandChStartSearApproved"
+ "ispExclaveKitCommandChStopSearApproved"
+ "no"
+ "searApprovedInterfaceSwitcherUpdate"
+ "searApprovedPathFlag"
+ "true"
+ "v120@?0{ispexclavekitshared_ekispmanager_channelinformationget__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitshared_ekchannelinformation_s=BIIIiic[3f][3f][9f][3f]I})}8"
+ "v144@?0{perceptionmodule_ekperception_runperception__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{perceptionmodule_perceptionresult_s={perceptionmodule_perceptionreturninfo_s=Q}[30i]})}8"
+ "v24@?0Q8r^{anstmodule_anstfacev1502_s=II{anstmodule_anstcategory2_s=Q}{anstmodule_anstrect2_s=ffff}{anstmodule_anstfaceposedegree_s=Q(?={?=I})}{anstmodule_anstfaceposedegree_s=Q(?={?=I})}{anstmodule_anstfaceposedegree_s=Q(?={?=I})}{anstmodule_anstfaceposedegree_s=Q(?={?=I})}{anstmodule_anstfaceposedegree_s=Q(?={?=I})}BfB}16"
+ "v24@?0Q8r^{anstmodule_anstobjectv1502_s=II{anstmodule_anstcategory2_s=Q}{anstmodule_anstrect2_s=ffff}f}16"
+ "v24@?0{andkmodule_ekandk_runandk__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{attentionawarenessmodule_ekattentionawareness_channelrunfacedetect__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}B)}8"
+ "v24@?0{autoexposuremodule_ekautoexposure_channelautoexposureflickerfreqset__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{autoexposuremodule_ekautoexposure_channelautoexposureframeratemaxget__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}I)}8"
+ "v24@?0{autoexposuremodule_ekautoexposure_channelautoexposureframeratemaxset__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{autoexposuremodule_ekautoexposure_channelautoexposureframerateminget__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}I)}8"
+ "v24@?0{autoexposuremodule_ekautoexposure_channelautoexposureframerateminset__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{facekitmodule_ekfacekit_channelfaceconfigset__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{facekitmodule_ekfacekit_channelrunkitfacesecondaryprocess__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{ispexclavekitdebugmodule_ekdebug_channeldebugcapability__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitdebugmodule_ekchanneldebugcapabilityrslt_s=I})}8"
+ "v24@?0{ispexclavekitdebugmodule_ekdebug_channelexfiltration__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitdebugmodule_ekchannelfiltrationrslt_s=I})}8"
+ "v24@?0{ispexclavekitdebugmodule_ekdebug_channelinfiltration__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitdebugmodule_ekchannelfiltrationrslt_s=I})}8"
+ "v24@?0{ispexclavekitdebugmodule_ekdebug_channelpropertywrite__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{ispexclavekithardwaredefaultconfig_ekhardwaredefaultconfig_channellscset__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{ispexclavekithardwaredefaultconfig_ekhardwaredefaultconfig_channelpdpset__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{ispexclavekitshared_ekchannelstreamingcontrol_channelalgorithmenable__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitshared_ekchannelalgorithmenablereturn_s=I})}8"
+ "v24@?0{ispexclavekitshared_ekchannelstreamingcontrol_channelconcurrentflagset__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{ispexclavekitshared_ekchannelstreamingcontrol_channelconfigurationstatusread__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}B)}8"
+ "v24@?0{ispexclavekitshared_ekchannelstreamingcontrol_channelsetalgoframerate__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}f)}8"
+ "v24@?0{ispexclavekitshared_ekchannelstreamingcontrol_channelstart__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{ispexclavekitshared_ekchannelstreamingcontrol_channelstop__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{ispexclavekitshared_ekispmanager_channelrunispmanager__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{ispexclavekitshared_ekispmanager_channelsensormetadataset__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{ispexclavekitshared_ekstreamingcontrol_off__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{ispexclavekitshared_ekstreamingcontrol_on__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitshared_ekonreturn_s=B})}8"
+ "v24@?0{motiontowakemodule_ekmotiontowake_channelrunmotiondetect__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{motiontowakemodule_ekmotiondetectresult_s=Q})}8"
+ "v24@?0{perceptionmodule_ekperception_setperceptionframerate__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v256@?0{facekitmodule_ekfacekit_channelrunkitfaceprocess__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{facekitmodule_ekfacekitprocessresult_s=d{facekitmodule_facekitcameraparameters_s={facekitmodule_facekittransformation3d_s=[9f][3f]}[9f]}{facekitmodule_facekitdatafailure_s={bool__opt_s=BB}{bool__opt_s=BB}B}{facekitmodule_facekittrackedface__opt_s=B{facekitmodule_facekittrackedface_s=ii{facekitmodule_facekittransformation3d_s=[9f][3f]}{facekitmodule_facekittransformation3d_s=[9f][3f]}BB}}{facekitmodule_facekitclientdata_s={facekitmodule_facekitaccessibilitydata__opt_s=B{facekitmodule_facekitaccessibilitydata_s={facekitmodule_facekitexpressions_s=CCCCCCCCC}[2f]}}}B})}8"
+ "v32@?0{ispexclavekitdebugmodule_ekdebug_channelpropertyread__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitdebugmodule_ekchannelpropertyreadreturn_s=III})}8"
+ "v64@?0{ispirexclavekitmodule_ispexclavecorechrunkitadrslt_s=[1{ispirexclavekitmodule_attentioninfo_s=BBf{ispirexclavekitmodule_facerect_s=fffff}{ispirexclavekitmodule_faceangle_s=ffff}I}]IB}8"
+ "v80@?0{autoexposuremodule_ekautoexposure_channelautoexposureinitsettingget__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{autoexposuremodule_ekautoexposureresult_s=IQIIIIIIIffIIB})}8"
+ "v80@?0{autoexposuremodule_ekautoexposure_channelrunautoexposure__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{autoexposuremodule_ekautoexposureresult_s=IQIIIIIIIffIIB})}8"
+ "v88@?0{attentionawarenessmodule_ekattentionawareness_channelrunattentiondetect__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{attentionawarenessmodule_attentiondetectresult_s={attentionawarenessmodule_attentioninfo2_s=BB{attentionawarenessmodule_facerect2_s=ffff{attentionawarenessmodule_faceconfidence_s=Q}}{attentionawarenessmodule_faceangle2_s=fff{attentionawarenessmodule_facedistance_s=Q}}{attentionawarenessmodule_faceorientation2_s=Q}}II})}8"
+ "v88@?0{ispexclavekitshared_ekispmanager_channelcameraconfigurationget__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitshared_ekchannelcameraconfiguration_s=ISSSSIISICSIIISSIIIII})}8"
+ "v96@?0{anstmodule_ekanst_channelrunkitanstv150__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{anstmodule_ispexclavecorechrunkitanstresultv150_s={anstmodule_anstresultipcv1502_s={anstmodule_anstfacev1502_v_s=C(?={?=^{anstmodule_anstfacev1502_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}{anstmodule_anstobjectv1502_v_s=C(?={?=^{anstmodule_anstobjectv1502_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}})}8"
+ "yes"
- "ISPExclaveKitCmdChAEInitSettingGet"
- "ISPExclaveKitCmdChRunKitAE"
- "ISPExclaveKitCmdChRunKitER"
- "ISPExclaveKitCmdChRunKitISP"
- "ISPExclaveKitCmdChSensorMetadata"
- "ISPExclaveKitCmdChStart"
- "ISPExclaveKitCmdChStop"
- "ISPExclaveKitCmdExclaveChCameraConfigSet"
- "ISPExclaveKitCmdOff"
- "ISPExclaveKitCmdOn"
- "[Conclave] (EKType:%d) Failed to setup ER client\n"
- "[Conclave] (EKType:%d) Failed to setup IR client\n"
- "[Conclave] (EKType:%d) Failed to setup RGB client\n"
- "[Conclave] Conclave launch is success"
- "[Conclave] Invalid EK Type!"
- "[Conclave] tb_conclave_endpoint_for_service failed (EKType:%d / tberr:%u / mConclaveEndpoint:%lu)\n"
- "[Conclave] tb_conclave_endpoint_for_service is success (EKType:%d / tberr:%u / mConclaveEndpoint:%lu)\n"
- "cmd: %s failed"
- "cmd: %s is success"
- "cmd: %s to ek failed"
- "cmd: %s to ek success"
- "v64@?0{ispirexclavekitmodule_ispexclavecorechrunkitadrslt_s=[1{ispirexclavekitmodule_attentioninfo_s=Bf{ispirexclavekitmodule_facerect_s=fffff}{ispirexclavekitmodule_faceangle_s=ffff}I}]IB}8"
- "v72@?0{ispirexclavekitmodule_ispexclavecorechrunkitaerslt_s=IQIIIIIIffIIB}8"

```
