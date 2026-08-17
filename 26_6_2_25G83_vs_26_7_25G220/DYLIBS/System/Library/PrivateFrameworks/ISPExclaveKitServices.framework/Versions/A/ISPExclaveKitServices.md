## ISPExclaveKitServices

> `/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/Versions/A/ISPExclaveKitServices`

```diff

 5.605.0.0.0
-  __TEXT.__text: 0x28668
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__const: 0x2d0
-  __TEXT.__gcc_except_tab: 0x7d0
-  __TEXT.__oslogstring: 0x3092
-  __TEXT.__cstring: 0x6a1b
-  __TEXT.__unwind_info: 0x800
+  __TEXT.__text: 0x2d1b4
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__const: 0x348
+  __TEXT.__gcc_except_tab: 0x85c
+  __TEXT.__oslogstring: 0x3449
+  __TEXT.__cstring: 0x7adf
+  __TEXT.__unwind_info: 0x8e0
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x5a0
-  __AUTH_CONST.__auth_got: 0x3a8
-  __AUTH_CONST.__const: 0xb30
-  __AUTH_CONST.__cfstring: 0x4c0
-  __DATA.__data: 0x116750
+  __DATA_CONST.__const: 0x630
+  __AUTH_CONST.__auth_got: 0x3b0
+  __AUTH_CONST.__const: 0xcb0
+  __AUTH_CONST.__cfstring: 0x6e0
+  __DATA.__data: 0x116988
   __DATA.__common: 0x20
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 996
-  Symbols:   788
-  CStrings:  658
+  Functions: 1100
+  Symbols:   859
+  CStrings:  738
 
Symbols:
+ _Z35ispExclaveKitCommandChRunPerceptionP20sExclaveKitIspCmdHdr
+ _Z41ispExclaveKitCommandChPerceptionConfigSetP20sExclaveKitIspCmdHdr
+ _Z42_ispExclaveKitCommandChPerceptionConfigSetj
+ _Z46ispExclaveKitCommandChRunLightSourceEstimationP20sExclaveKitIspCmdHdr
+ _Z47ispExclaveKitCommandChRunPerceptionWithObjectIDP20sExclaveKitIspCmdHdr
+ _Z49ispExclaveKitCommandChRunDeviceProximityDetectionP20sExclaveKitIspCmdHdr
+ _Z52ispExclaveKitCommandChLightSourceEstimationConfigSetP20sExclaveKitIspCmdHdr
+ _Z55ispExclaveKitCommandChDeviceProximityDetectionConfigSetP20sExclaveKitIspCmdHdr
+ _Z56_ispExclaveKitCommandChDeviceProximityDetectionConfigSetj
+ _Z58ispExclaveKitCommandChLightSourceEstimationConfigSetFinishj
+ __Z35ispExclaveKitCommandChRunPerceptionP20sExclaveKitIspCmdHdr
+ __Z41ispExclaveKitCommandChPerceptionConfigSetP20sExclaveKitIspCmdHdr
+ __Z42_ispExclaveKitCommandChPerceptionConfigSetj
+ __Z46ispExclaveKitCommandChRunLightSourceEstimationP20sExclaveKitIspCmdHdr
+ __Z47ispExclaveKitCommandChRunPerceptionWithObjectIDP20sExclaveKitIspCmdHdr
+ __Z49ispExclaveKitCommandChRunDeviceProximityDetectionP20sExclaveKitIspCmdHdr
+ __Z52ispExclaveKitCommandChLightSourceEstimationConfigSetP20sExclaveKitIspCmdHdr
+ __Z55ispExclaveKitCommandChDeviceProximityDetectionConfigSetP20sExclaveKitIspCmdHdr
+ __Z56_ispExclaveKitCommandChDeviceProximityDetectionConfigSetj
+ __Z58ispExclaveKitCommandChLightSourceEstimationConfigSetFinishj
+ ___Z35ispExclaveKitCommandChRunPerceptionP20sExclaveKitIspCmdHdr_block_invoke
+ ___Z47ispExclaveKitCommandChRunPerceptionWithObjectIDP20sExclaveKitIspCmdHdr_block_invoke
+ ___Z58ispExclaveKitCommandChLightSourceEstimationConfigSetFinishj_block_invoke
+ ____Z35ispExclaveKitCommandChRunPerceptionP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z42_ispExclaveKitCommandChPerceptionConfigSetj_block_invoke
+ ____Z46ispExclaveKitCommandChRunLightSourceEstimationP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z47ispExclaveKitCommandChRunPerceptionWithObjectIDP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z49ispExclaveKitCommandChRunDeviceProximityDetectionP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z56_ispExclaveKitCommandChDeviceProximityDetectionConfigSetj_block_invoke
+ ____Z58ispExclaveKitCommandChLightSourceEstimationConfigSetFinishj_block_invoke
+ ___copy_helper_block_8_32r
+ ___destroy_helper_block_8_32r
+ ___perceptionmodule_perceptioncroptypes__v_raw_encode_block_invoke
+ ___perceptionmodule_perceptioncroptypes__v_visit_block_invoke
+ __perceptionmodule_perceptioncroptypes__v_raw_encode_block_invoke
+ __perceptionmodule_perceptioncroptypes__v_visit_block_invoke
+ _deviceproximitydetectionmodule_detecteddevicev2__raw_decode
+ _deviceproximitydetectionmodule_ekdeviceproximitydetection__init
+ _deviceproximitydetectionmodule_ekdeviceproximitydetection_run
+ _deviceproximitydetectionmodule_ekdeviceproximitydetection_run__result_get_success
+ _deviceproximitydetectionmodule_ekdeviceproximitydetection_setconfiguration
+ _deviceproximitydetectionmodule_ekdeviceproximitydetection_setconfiguration__result_get_success
+ _memset_pattern16
+ _ntkeklightsourceestimationmodule_ispexclavecorechrunkitlightsourceestimationresult__decode
+ _ntkeklightsourceestimationmodule_ntkeklightsourceestimation__init
+ _ntkeklightsourceestimationmodule_ntkeklightsourceestimation_channelrunlightsourceestimation
+ _ntkeklightsourceestimationmodule_ntkeklightsourceestimation_channelrunlightsourceestimation__result_get_success
+ _ntkeklightsourceestimationmodule_ntkeklightsourceestimation_channelsetlightsourceestimationals
+ _perceptionmodule_ekperception__init
+ _perceptionmodule_ekperception_runperception
+ _perceptionmodule_ekperception_runperception__result_get_success
+ _perceptionmodule_ekperception_setperceptioncroptypes
+ _perceptionmodule_ekperception_setperceptioncroptypes__result_get_success
+ _perceptionmodule_perceptioncroptypes__v_assign_unowned
+ _perceptionmodule_perceptioncroptypes__v_count
+ _perceptionmodule_perceptioncroptypes__v_visit
+ _perceptionmodule_perceptionreturninfo_detectionserror__get
+ _perceptionmodule_perceptionreturninfo_frameskipped__get
+ _perceptionmodule_perceptionreturninfo_frameskippedbydecimation__get
+ _perceptionmodule_perceptionreturninfo_queuefull__get
+ _perceptionmodule_perceptionreturninfo_queueingfailed__get
+ _perceptionmodule_perceptionreturninfo_sharedmemorymappingissue__get
+ _perceptionmodule_perceptionreturninfo_success__get
+ deviceproximitydetectionmodule_detecteddevicev2__raw_decode
+ deviceproximitydetectionmodule_ekdeviceproximitydetection_run
+ deviceproximitydetectionmodule_ekdeviceproximitydetection_setconfiguration
+ ntkeklightsourceestimationmodule_ntkeklightsourceestimation_channelrunlightsourceestimation
+ perceptionmodule_ekperception_runperception
+ perceptionmodule_ekperception_setperceptioncroptypes
+ perceptionmodule_perceptioncroptypes__v_count
+ perceptionmodule_perceptioncroptypes__v_visit
CStrings:
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_IDL_CALL_FAIL set cropTypes failed\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_INPUT, type count %u\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_INPUT, unknow type %u\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_INPUT, unknown crop type %u\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_INPUT, wrong model: %d\n"
+ "%s:%d - ERROR: unkonw perception return code %llx\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_DEVICE_PROXIMITY_DETECTION handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_LIGHT_SOURCE_ESTIMATION handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_PERCEPTION handler is created\n"
+ "%s:%d - call idl after\n"
+ "%s:%d - call idl before\n"
+ "%s:%d - call idl middle\n"
+ "%s:%d - config %u %u %u\n"
+ "%s:%d - create lightSourceEstimationHandler done!\n"
+ "%s:%d - lightSourceEstimationHandler %p\n"
+ "%s:%d - run perception \n"
+ "%s:%d - run perception with Object ID\n"
+ "%s:%d - run proximity \n"
+ "ISP_EXCLAVEKIT_CMD_CH_DEVICE_PROXIMITY_DETECTION_CONFIG_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_LIGHT_SOURCE_ESTIMATION_CONFIG_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_PERCEPTION_CONFIG_SET"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_DEVICE_PROXIMITY_DETECTION"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_LIGHT_SOURCE_ESTIMATION"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_PERCEPTION"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_PERCEPTION_WITH_OBJECTID"
+ "J490"
+ "J491"
+ "J510"
+ "J511"
+ "J804"
+ "J833"
+ "J834"
+ "K114c"
+ "K114s"
+ "K116c"
+ "K116s"
+ "T5950"
+ "T8160"
+ "TB_ASSERT: (perceptionmodule_perceptioncroptypes__decode(msg, &item) == TB_ERROR_SUCCESS) && \"failed to decode type: PerceptionModule.PerceptionCropTypes\""
+ "TB_ASSERT: (perceptionmodule_perceptioncroptypes__v_raw_encode(&msg, types) == TB_ERROR_SUCCESS) && \"failed to encode type: PerceptionModule.PerceptionCropTypes\""
+ "TB_FATAL: invalid result returned from channelRunLightSourceEstimation"
+ "TB_FATAL: invalid result returned from channelRunLightSourceEstimation (%s:%d)\n"
+ "TB_FATAL: invalid result returned from run"
+ "TB_FATAL: invalid result returned from run (%s:%d)\n"
+ "TB_FATAL: invalid result returned from runPerception"
+ "TB_FATAL: invalid result returned from runPerception (%s:%d)\n"
+ "TB_FATAL: invalid result returned from setConfiguration"
+ "TB_FATAL: invalid result returned from setConfiguration (%s:%d)\n"
+ "TB_FATAL: invalid result returned from setPerceptionCropTypes"
+ "TB_FATAL: invalid result returned from setPerceptionCropTypes (%s:%d)\n"
+ "TB_FATAL: invalid tag in `[PerceptionModule.PerceptionCropTypes]` metadata: 0x%x"
+ "TB_FATAL: invalid tag in `[PerceptionModule.PerceptionCropTypes]` metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: overflow detected when adding"
+ "TB_FATAL: overflow detected when adding (%s:%d)\n"
+ "TB_FATAL: overflow detected when multiplying"
+ "TB_FATAL: overflow detected when multiplying (%s:%d)\n"
+ "V62"
+ "V63"
+ "V64"
+ "V68"
+ "_ispExclaveKitCommandChDeviceProximityDetectionConfigSet"
+ "_ispExclaveKitCommandChPerceptionConfigSet"
+ "ispExclaveKitCommandChDeviceProximityDetectionConfigSet"
+ "ispExclaveKitCommandChLightSourceEstimationConfigSet"
+ "ispExclaveKitCommandChLightSourceEstimationConfigSetFinish"
+ "ispExclaveKitCommandChLightSourceEstimationConfigSetFinish_block_invoke"
+ "ispExclaveKitCommandChPerceptionConfigSet"
+ "ispExclaveKitCommandChRunDeviceProximityDetection"
+ "ispExclaveKitCommandChRunLightSourceEstimation"
+ "ispExclaveKitCommandChRunPerception"
+ "ispExclaveKitCommandChRunPerceptionWithObjectID"
+ "ispExclaveKitCommandChRunPerceptionWithObjectID_block_invoke"
+ "ispExclaveKitCommandChRunPerception_block_invoke"
+ "v12@?0B8"
+ "v160@?0{perceptionmodule_ekperception_runperception__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{perceptionmodule_perceptionresult_s={exclavesispshared_exclavesispresultcommon_s=QB}{perceptionmodule_perceptionreturninfo_s=Q}[30i]})}8"
+ "v24@?0Q8r^{perceptionmodule_perceptioncroptypes_s=Q}16"
+ "v24@?0{deviceproximitydetectionmodule_ekdeviceproximitydetection_setconfiguration__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}B)}8"
+ "v24@?0{perceptionmodule_ekperception_setperceptioncroptypes__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v424@?0{deviceproximitydetectionmodule_ekdeviceproximitydetection_run__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{deviceproximitydetectionmodule_ispexclavecorechrunkitdeviceproximitydetectionresult_s={exclavesispshared_exclavesispresultcommon_s=QB}{deviceproximitydetectionmodule_deviceproximitydetectionresultipcv2_s=BC[4{deviceproximitydetectionmodule_detecteddevicev2_s=QQ{deviceproximitydetectionmodule_devicefamily_s=Q}[16f]C}]}})}8"
+ "v512@?0{ntkeklightsourceestimationmodule_ntkeklightsourceestimation_channelrunlightsourceestimation__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ntkeklightsourceestimationmodule_ispexclavecorechrunkitlightsourceestimationresult_s={exclavesispshared_exclavesispresultcommon_s=QB}[17{ntkeklightsourceestimationmodule_ntkeklightsourceestimationunifiedlightinggaussian_s={ntkeklightsourceestimationmodule_ntkeklightsourceestimationposition_s=fff}f{ntkeklightsourceestimationmodule_ntkeklightsourceestimationrgb_s=fff}}]})}8"
```
