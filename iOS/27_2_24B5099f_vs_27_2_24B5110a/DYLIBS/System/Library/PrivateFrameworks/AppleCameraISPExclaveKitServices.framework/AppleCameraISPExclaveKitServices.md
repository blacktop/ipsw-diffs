## AppleCameraISPExclaveKitServices

> `/System/Library/PrivateFrameworks/AppleCameraISPExclaveKitServices.framework/AppleCameraISPExclaveKitServices`

```diff

-20.106.4.0.0
-  __TEXT.__text: 0x32a94
-  __TEXT.__const: 0x2fa
-  __TEXT.__gcc_except_tab: 0x934
-  __TEXT.__oslogstring: 0x44fe
-  __TEXT.__cstring: 0x8d16
+20.109.0.0.0
+  __TEXT.__text: 0x37698
+  __TEXT.__const: 0x37a
+  __TEXT.__gcc_except_tab: 0x9a4
+  __TEXT.__oslogstring: 0x4a2e
+  __TEXT.__cstring: 0x9f36
   __TEXT.__swift5_typeref: 0x2e
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x12d8
+  __TEXT.__unwind_info: 0x14b0
   __TEXT.__eh_frame: 0x70
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
-  __DATA_CONST.__const: 0x1210
+  __DATA_CONST.__const: 0x13e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x48
-  __AUTH_CONST.__cfstring: 0x5e0
+  __AUTH_CONST.__cfstring: 0x620
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__auth_got: 0x590
+  __AUTH_CONST.__auth_got: 0x598
   __AUTH.__data: 0x98
-  __DATA.__data: 0x118bd0
+  __DATA.__data: 0x118cd8
   __DATA.__common: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1197
-  Symbols:   783
-  CStrings:  828
+  Functions: 1310
+  Symbols:   831
+  CStrings:  898
 
Symbols:
+ __Z35ispExclaveKitCommandChRunPerceptionP20sExclaveKitIspCmdHdr
+ __Z40isNewSharedMemoryReplayBufferDumpSkipRawP21ISPExclaveKitDefaults
+ __Z40isNewSharedMemoryReplayBufferDumpSkipYuvP21ISPExclaveKitDefaults
+ __Z41ispExclaveKitCommandChPerceptionConfigSetP20sExclaveKitIspCmdHdr
+ __Z42_ispExclaveKitCommandChPerceptionConfigSetj
+ __Z46ispExclaveKitCommandChRunLightSourceEstimationP20sExclaveKitIspCmdHdr
+ __Z47ispExclaveKitCommandChRunPerceptionWithObjectIDP20sExclaveKitIspCmdHdr
+ __Z49ispExclaveKitCommandChRunDeviceProximityDetectionP20sExclaveKitIspCmdHdr
+ __Z52ispExclaveKitCommandChLightSourceEstimationConfigSetP20sExclaveKitIspCmdHdr
+ __Z55ispExclaveKitCommandChDeviceProximityDetectionConfigSetP20sExclaveKitIspCmdHdr
+ __Z56_ispExclaveKitCommandChDeviceProximityDetectionConfigSetj
+ __Z58ispExclaveKitCommandChLightSourceEstimationConfigSetFinishj
+ __ZN28ISPExclaveKitFileServiceBase24_allocateLocalTempBufferEm
+ ____Z35ispExclaveKitCommandChRunPerceptionP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z42_ispExclaveKitCommandChPerceptionConfigSetj_block_invoke
+ ____Z46ispExclaveKitCommandChRunLightSourceEstimationP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z47ispExclaveKitCommandChRunPerceptionWithObjectIDP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z49ispExclaveKitCommandChRunDeviceProximityDetectionP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z56_ispExclaveKitCommandChDeviceProximityDetectionConfigSetj_block_invoke
+ ____Z58ispExclaveKitCommandChLightSourceEstimationConfigSetFinishj_block_invoke
+ ___applecamera_perceptionmodule_perceptioncroptypes__v_raw_encode_block_invoke
+ ___applecamera_perceptionmodule_perceptioncroptypes__v_visit_block_invoke
+ _applecamera_deviceproximitydetectionmodule_detecteddevicev2__raw_decode
+ _applecamera_deviceproximitydetectionmodule_ekdeviceproximitydetection__init
+ _applecamera_deviceproximitydetectionmodule_ekdeviceproximitydetection_run
+ _applecamera_deviceproximitydetectionmodule_ekdeviceproximitydetection_run__result_get_success
+ _applecamera_deviceproximitydetectionmodule_ekdeviceproximitydetection_setconfiguration
+ _applecamera_deviceproximitydetectionmodule_ekdeviceproximitydetection_setconfiguration__result_get_success
+ _applecamera_ntkeklightsourceestimationmodule_ispexclavecorechrunkitlightsourceestimationresult__decode
+ _applecamera_ntkeklightsourceestimationmodule_ntkeklightsourceestimation__init
+ _applecamera_ntkeklightsourceestimationmodule_ntkeklightsourceestimation_channelrunlightsourceestimation
+ _applecamera_ntkeklightsourceestimationmodule_ntkeklightsourceestimation_channelrunlightsourceestimation__result_get_success
+ _applecamera_ntkeklightsourceestimationmodule_ntkeklightsourceestimation_channelsetlightsourceestimationals
+ _applecamera_perceptionmodule_ekperception__init
+ _applecamera_perceptionmodule_ekperception_runperception
+ _applecamera_perceptionmodule_ekperception_runperception__result_get_success
+ _applecamera_perceptionmodule_ekperception_setperceptioncroptypes
+ _applecamera_perceptionmodule_ekperception_setperceptioncroptypes__result_get_success
+ _applecamera_perceptionmodule_perceptioncroptypes__v_assign_unowned
+ _applecamera_perceptionmodule_perceptioncroptypes__v_count
+ _applecamera_perceptionmodule_perceptioncroptypes__v_visit
+ _applecamera_perceptionmodule_perceptionreturninfo_detectionserror__get
+ _applecamera_perceptionmodule_perceptionreturninfo_frameskipped__get
+ _applecamera_perceptionmodule_perceptionreturninfo_frameskippedbydecimation__get
+ _applecamera_perceptionmodule_perceptionreturninfo_queuefull__get
+ _applecamera_perceptionmodule_perceptionreturninfo_queueingfailed__get
+ _applecamera_perceptionmodule_perceptionreturninfo_sharedmemorymappingissue__get
+ _applecamera_perceptionmodule_perceptionreturninfo_success__get
+ _memset_pattern16
- GCC_except_table17
CStrings:
+ "%s:%d - ERROR: Device Proximity Detection service not initialized for channel %u\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_IDL_CALL_FAIL set cropTypes failed\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_INPUT, type count %u\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_INPUT, unknow type %u\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_INPUT, unknown crop type %u\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_INPUT, wrong model: %d\n"
+ "%s:%d - ERROR: Perception service not initialized for channel %u\n"
+ "%s:%d - ERROR: unkonw perception return code %llx\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_DEVICE_PROXIMITY_DETECTION handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_LIGHT_SOURCE_ESTIMATION handler is created\n"
+ "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_PERCEPTION handler is created\n"
+ "%s:%d - [EK] CH: %d frameId: 0x%x bufferTypeIndex = %d dropped: copy out failed (err %d)\n"
+ "%s:%d - _isMemoryPortCreated is false for region: %s\n"
+ "%s:%d - call idl after\n"
+ "%s:%d - call idl before\n"
+ "%s:%d - call idl middle\n"
+ "%s:%d - config %u %u %u\n"
+ "%s:%d - create lightSourceEstimationHandler done!\n"
+ "%s:%d - creating shared memory region: %s failed with err: %d, region unavailable on this platform\n"
+ "%s:%d - exclaves_outbound_buffer_copyout failed with err: %d - region %s offset 0x%lx + size %ld %s mapped view of %zu bytes; destination buffer left unwritten\n"
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
+ "TB_ASSERT: (applecamera_perceptionmodule_perceptioncroptypes__decode(msg, &item) == TB_ERROR_SUCCESS) && \"failed to decode type: AppleCamera_PerceptionModule.PerceptionCropTypes\""
+ "TB_ASSERT: (applecamera_perceptionmodule_perceptioncroptypes__v_raw_encode(&msg, types) == TB_ERROR_SUCCESS) && \"failed to encode type: AppleCamera_PerceptionModule.PerceptionCropTypes\""
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
+ "TB_FATAL: invalid tag in `[AppleCamera_PerceptionModule.PerceptionCropTypes]` metadata: 0x%x"
+ "TB_FATAL: invalid tag in `[AppleCamera_PerceptionModule.PerceptionCropTypes]` metadata: 0x%x (%s:%d)\n"
+ "TB_FATAL: overflow detected when adding"
+ "TB_FATAL: overflow detected when adding (%s:%d)\n"
+ "TB_FATAL: overflow detected when multiplying"
+ "TB_FATAL: overflow detected when multiplying (%s:%d)\n"
+ "_ispExclaveKitCommandChDeviceProximityDetectionConfigSet"
+ "_ispExclaveKitCommandChPerceptionConfigSet"
+ "exceeds"
+ "is within"
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
+ "v160@?0{applecamera_perceptionmodule_ekperception_runperception__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q}{applecamera_perceptionmodule_perceptionresult_s={applecamera_exclavesispshared_exclavesispresultcommon_s=QB}{applecamera_perceptionmodule_perceptionreturninfo_s=Q}[30i]})}8"
+ "v24@?0Q8r^{applecamera_perceptionmodule_perceptioncroptypes_s=Q}16"
+ "v24@?0{applecamera_deviceproximitydetectionmodule_ekdeviceproximitydetection_setconfiguration__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q}B)}8"
+ "v24@?0{applecamera_perceptionmodule_ekperception_setperceptioncroptypes__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q})}8"
+ "v424@?0{applecamera_deviceproximitydetectionmodule_ekdeviceproximitydetection_run__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q}{applecamera_deviceproximitydetectionmodule_ispexclavecorechrunkitdeviceproximitydetectionresult_s={applecamera_exclavesispshared_exclavesispresultcommon_s=QB}{applecamera_deviceproximitydetectionmodule_deviceproximitydetectionresultipcv2_s=BC[4{applecamera_deviceproximitydetectionmodule_detecteddevicev2_s=QQ{applecamera_deviceproximitydetectionmodule_devicefamily_s=Q}[16f]C}]}})}8"
+ "v512@?0{applecamera_ntkeklightsourceestimationmodule_ntkeklightsourceestimation_channelrunlightsourceestimation__result_s=C(?={applecamera_exclavesispshared_exclavesisperror_s=Q}{applecamera_ntkeklightsourceestimationmodule_ispexclavecorechrunkitlightsourceestimationresult_s={applecamera_exclavesispshared_exclavesispresultcommon_s=QB}[17{applecamera_ntkeklightsourceestimationmodule_ntkeklightsourceestimationunifiedlightinggaussian_s={applecamera_ntkeklightsourceestimationmodule_ntkeklightsourceestimationposition_s=fff}f{applecamera_ntkeklightsourceestimationmodule_ntkeklightsourceestimationrgb_s=fff}}]})}8"
- "%s:%d - _isMemoryPortCreated is false\n"
- "%s:%d - creating shared memory region: %s failed with err: %d\n"
- "%s:%d - exclaves_outbound_buffer_copyout failed with err: %d\n"
```
