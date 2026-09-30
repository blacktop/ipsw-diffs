## ISPExclaveKitServices

> `/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/ISPExclaveKitServices`

```diff

-3.515.0.0.0
-  __TEXT.__text: 0x32190
+3.605.0.0.0
+  __TEXT.__text: 0x32d20
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0xa3c
-  __TEXT.__oslogstring: 0x21a5
-  __TEXT.__cstring: 0x3b10
-  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__const: 0x160
+  __TEXT.__gcc_except_tab: 0xa60
+  __TEXT.__oslogstring: 0x23c1
+  __TEXT.__cstring: 0x432e
+  __TEXT.__unwind_info: 0x808
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x1300
+  __DATA_CONST.__const: 0x1648
   __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__cfstring: 0x200
-  __DATA.__data: 0xd67fd
+  __DATA.__data: 0xd6815
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1043
-  Symbols:   1216
-  CStrings:  368
+  Functions: 1054
+  Symbols:   1227
+  CStrings:  431
 
Symbols:
+ __Z12cmdStringGetj
+ __Z29GetString_eIspExclaveKitCmdIdm
+ __Z46_ispExclaveKitCommandChAdConfigSetSearApprovedj
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
+ "/Library/Caches/com.apple.xbs/Binaries/ExclaveSISP_XNU_products/install/TempContent/Objects/ExclaveSISP.build/ISPExclaveKitServices.build/DerivedSources/ISPExclaveKitServices_C.c"
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
- "/Library/Caches/com.apple.xbs/Sources/ExclaveSISP_XNU_products/XNU/EKServiceFramework/ISPExclaveKitServices_C.c"
- "getAdSetField"

```
