## ISPExclaveKitServices

> `/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/ISPExclaveKitServices`

```diff

-6.103.0.0.0
-  __TEXT.__text: 0x27c78
-  __TEXT.__const: 0x290
-  __TEXT.__gcc_except_tab: 0x774
-  __TEXT.__oslogstring: 0x30b9
-  __TEXT.__cstring: 0x6dd2
-  __TEXT.__unwind_info: 0xfd8
+6.104.0.0.0
+  __TEXT.__text: 0x2c3dc
+  __TEXT.__const: 0x308
+  __TEXT.__gcc_except_tab: 0x7f4
+  __TEXT.__oslogstring: 0x3470
+  __TEXT.__cstring: 0x7e49
+  __TEXT.__unwind_info: 0x1180
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0xf00
+  __DATA_CONST.__const: 0x10d0
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x4c0
+  __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__auth_got: 0x390
   __DATA.__data: 0x5c90
   __DATA.__common: 0x8
-  __DATA_DIRTY.__data: 0x110ad0
+  __DATA_DIRTY.__data: 0x110ba0
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1000
-  Symbols:   627
-  CStrings:  665
+  Functions: 1103
+  Symbols:   674
+  CStrings:  730
 
Symbols:
+ _OUTLINED_FUNCTION_19
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
+ ____Z35ispExclaveKitCommandChRunPerceptionP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z42_ispExclaveKitCommandChPerceptionConfigSetj_block_invoke
+ ____Z46ispExclaveKitCommandChRunLightSourceEstimationP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z47ispExclaveKitCommandChRunPerceptionWithObjectIDP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z49ispExclaveKitCommandChRunDeviceProximityDetectionP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z56_ispExclaveKitCommandChDeviceProximityDetectionConfigSetj_block_invoke
+ ____Z58ispExclaveKitCommandChLightSourceEstimationConfigSetFinishj_block_invoke
+ ___perceptionmodule_perceptioncroptypes__v_raw_encode_block_invoke
+ ___perceptionmodule_perceptioncroptypes__v_visit_block_invoke
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
