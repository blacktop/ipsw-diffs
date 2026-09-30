## ISPExclaveKitServices

> `/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/Versions/A/ISPExclaveKitServices`

```diff

-3.512.0.0.0
-  __TEXT.__text: 0x321c8
+3.604.0.0.0
+  __TEXT.__text: 0x32d54
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0xa3c
-  __TEXT.__oslogstring: 0x21a5
-  __TEXT.__cstring: 0x3be2
-  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__const: 0x168
+  __TEXT.__gcc_except_tab: 0xa60
+  __TEXT.__oslogstring: 0x23c1
+  __TEXT.__cstring: 0x4400
+  __TEXT.__unwind_info: 0x810
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__const: 0x360
   __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x1680
+  __AUTH_CONST.__const: 0x16b0
   __AUTH_CONST.__cfstring: 0x200
-  __DATA.__data: 0xd67fd
+  __DATA.__data: 0xd6815
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Versions/A/Tightbeam
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1047
-  Symbols:   1426
-  CStrings:  368
+  Functions: 1058
+  Symbols:   1441
+  CStrings:  431
 
Symbols:
+ _Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.75
+ _Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.76
+ _Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.77
+ _Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.78
+ _Z32ispExclaveKitCommandChAlgoEnableP20sExclaveKitIspCmdHdr.cold.38
+ _Z32ispExclaveKitCommandChAlgoEnableP20sExclaveKitIspCmdHdr.cold.39
+ _Z39ispExclaveKitCommandChRunAdSearApprovedP20sExclaveKitIspCmdHdr.cold.3
+ _Z46_ispExclaveKitCommandChAdConfigSetSearApprovedj.cold.1
+ __Z12cmdStringGetj
+ __Z29GetString_eIspExclaveKitCmdIdm
+ __Z46_ispExclaveKitCommandChAdConfigSetSearApprovedj
+ __ZL12invalidCmdId
+ __ZL22gs_eIspExclaveKitCmdId
+ ____Z46_ispExclaveKitCommandChAdConfigSetSearApprovedj_block_invoke
+ _attentionawarenessmodule_ekattentionawareness_channelupdateattentionconfig
+ _attentionawarenessmodule_ekattentionawareness_channelupdateattentionconfig__result_get_success
+ attentionawarenessmodule_ekattentionawareness_channelupdateattentionconfig.cold.1
- GCC_except_table10
- _Z39ispExclaveKitCommandChRunFdSearApprovedP20sExclaveKitIspCmdHdr.cold.3
- _Z40ispExclaveKitCommandChRunIspSearApprovedP20sExclaveKitIspCmdHdr.cold.4
- _Z40ispExclaveKitCommandChRunIspSearApprovedP20sExclaveKitIspCmdHdr.cold.5
CStrings:
+ "%s:%d - [EK] ISP Manager Done\n"
+ "%s:%d - [EK] Run ISP Manager\n"
+ "%s:%d - [IR-EK] Attention Detection Finished\n"
+ "%s:%d - [IR-EK] Face Detection Finished\n"
+ "%s:%d - [IR-EK] Run Attention Detection\n"
+ "%s:%d - [IR-EK] Run Face Detection\n"
+ "%s:%d - cmd: %s[0x%x]\n"
+ "%s:%d - in release mode, ispExclaveKitCommandChLscSetSearApproved is not available\n"
+ "%s:%d - in release mode, ispExclaveKitCommandChPdpSetSearApproved is not available\n"
+ "%s:%d - run AD Config SearApproved\n"
+ "%s:%d - run AD Config legacy path\n"
+ "%s:%d - run AlgoEnable SearApproved\n"
+ "%s:%d - run AlgoEnable legacy path\n"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/ExclaveSISP_XNU_products/install/TempContent/Objects/ExclaveSISP.build/ISPExclaveKitServices.build/DerivedSources/ISPExclaveKitServices_C.c"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/ExclaveSISP_XNU_products/install/TempContent/Objects/ExclaveSISP.build/ISPExclaveKitServices.build/DerivedSources/ISPIRExclaveKitModule_tightbeam_C.c"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Binaries/ExclaveSISP_XNU_products/install/TempContent/Objects/ExclaveSISP.build/ISPExclaveKitServices.build/DerivedSources/ISPRGBExclaveKitModule_tightbeam_C.c"
+ "ISP_EXCLAVEKIT_CMD_CH_AD_CONFIG_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_AE_FLICKER_FREQ_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_AE_FRAME_RATE_MAX_GET"
+ "ISP_EXCLAVEKIT_CMD_CH_AE_FRAME_RATE_MAX_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_AE_FRAME_RATE_MIN_GET"
+ "ISP_EXCLAVEKIT_CMD_CH_AE_FRAME_RATE_MIN_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_AE_GAIN_CAP_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_AE_INIT_SETTING_GET"
+ "ISP_EXCLAVEKIT_CMD_CH_AE_INTEGRATION_GAIN_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_AE_INTEGRATION_TIME_MAX_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_AE_UPDATE_RESUME"
+ "ISP_EXCLAVEKIT_CMD_CH_AE_UPDATE_SUSPEND"
+ "ISP_EXCLAVEKIT_CMD_CH_ALGO_ENABLE"
+ "ISP_EXCLAVEKIT_CMD_CH_CAMERA_CONFIG_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_CONCURRENT_FLAG_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_CONFIGURATION_STATUS_GET"
+ "ISP_EXCLAVEKIT_CMD_CH_DEBUG_CAPABILITY"
+ "ISP_EXCLAVEKIT_CMD_CH_DPC_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_EXFILTRATION"
+ "ISP_EXCLAVEKIT_CMD_CH_FACEKIT_CONFIG_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_FACEKIT_CONFIG_SET_V2"
+ "ISP_EXCLAVEKIT_CMD_CH_FPS_CONTROL"
+ "ISP_EXCLAVEKIT_CMD_CH_INFILTRATION"
+ "ISP_EXCLAVEKIT_CMD_CH_INFO_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_LSC_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_OFF"
+ "ISP_EXCLAVEKIT_CMD_CH_ON"
+ "ISP_EXCLAVEKIT_CMD_CH_PDP_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_PERCEPTION_CONFIG_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_PROPERTY_READ"
+ "ISP_EXCLAVEKIT_CMD_CH_PROPERTY_WRITE"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_AD"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_AE"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_ANDK"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_ANST"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_ER"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_FACEKIT_FIRST_PASS"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_FACEKIT_FIRST_PASS_V2"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_FACEKIT_SECOND_PASS"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_FACEKIT_SECOND_PASS_V2"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_FD"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_ISP"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_MD"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_PERCEPTION"
+ "ISP_EXCLAVEKIT_CMD_CH_SEND_METADATA"
+ "ISP_EXCLAVEKIT_CMD_CH_START"
+ "ISP_EXCLAVEKIT_CMD_CH_STOP"
+ "ISP_EXCLAVEKIT_CMD_DEVICE_INFO_GET"
+ "ISP_EXCLAVEKIT_CMD_FRAMEWORK_INIT"
+ "_ispExclaveKitCommandChAdConfigSetSearApproved"
+ "getAdSetFieldSearApproved"
+ "v24@?0{attentionawarenessmodule_ekattentionawareness_channelupdateattentionconfig__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}B)}8"
- "%s:%d - cmdId=0x%x\n"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/ExclaveSISP_XNU_products/install/TempContent/Objects/ExclaveSISP.build/ISPExclaveKitServices.build/DerivedSources/ISPIRExclaveKitModule_tightbeam_C.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/ExclaveSISP_XNU_products/install/TempContent/Objects/ExclaveSISP.build/ISPExclaveKitServices.build/DerivedSources/ISPRGBExclaveKitModule_tightbeam_C.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ExclaveSISP_XNU_products/XNU/EKServiceFramework/ISPExclaveKitServices_C.c"
- "getAdSetField"

```
