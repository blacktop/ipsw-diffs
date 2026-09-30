## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-3.324.0.0.0
-  __TEXT.__text: 0x1bdec4
-  __TEXT.__auth_stubs: 0x3320
+3.407.0.0.0
+  __TEXT.__text: 0x1c96dc
+  __TEXT.__auth_stubs: 0x33e0
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__const: 0x229bc
-  __TEXT.__oslogstring: 0x1c07b
-  __TEXT.__cstring: 0x1961f
-  __TEXT.__gcc_except_tab: 0x5cd0
-  __TEXT.__unwind_info: 0x3c28
+  __TEXT.__const: 0x22cec
+  __TEXT.__oslogstring: 0x1bc3c
+  __TEXT.__cstring: 0x19d01
+  __TEXT.__gcc_except_tab: 0x6450
+  __TEXT.__unwind_info: 0x3fe8
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0x1c61
-  __TEXT.__objc_methtype: 0x11fa
+  __TEXT.__objc_methtype: 0x124e
   __TEXT.__objc_stubs: 0x1f60
   __DATA_CONST.__got: 0x3210
-  __DATA_CONST.__const: 0x84e8
+  __DATA_CONST.__const: 0x8700
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x808
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x19a0
+  __AUTH_CONST.__auth_got: 0x1a00
   __AUTH_CONST.__auth_ptr: 0x98
-  __AUTH_CONST.__const: 0x2828
-  __AUTH_CONST.__cfstring: 0x98c0
-  __AUTH_CONST.__objc_const: 0x808
+  __AUTH_CONST.__const: 0x2740
+  __AUTH_CONST.__cfstring: 0x9c20
+  __AUTH_CONST.__objc_const: 0xae0
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x2195f8
+  __DATA.__data: 0x26a640
   __DATA.__bss: 0xf9
   __DATA.__common: 0x54
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x110
-  __DATA_DIRTY.__bss: 0x924
-  __DATA_DIRTY.__common: 0x54d0
+  __DATA_DIRTY.__bss: 0x934
+  __DATA_DIRTY.__common: 0x5528
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5739
-  Symbols:   9264
-  CStrings:  6385
+  Functions: 6024
+  Symbols:   9831
+  CStrings:  6449
 
Symbols:
+ _AMFDRSealingMapCopyLocalDict
+ _AMFDRSealingMapCopyMultiInstanceForClass
+ __Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr
+ __ZN25H16ISPExclaveDebugService16StopDebugServiceEv
+ __ZN25H16ISPExclaveDebugService17StartDebugServiceEj
+ __ZN25H16ISPExclaveDebugServiceC1Ev
+ __ZN25H16ISPExclaveDebugServiceC2Ev
+ __ZN6H16ISP12H16ISPDevice20GetExclaveDeviceTypeEv
+ __ZN6H16ISP12H16ISPDevice27ISP_DCS_SetAudioAccelConfigEhbhh
+ __ZN6H16ISP12H16ISPDevice32ConfigureExclaveKitDebugServicesEj
+ __ZN6H16ISP23H16ISPPhotometerManager16GetFlickerResultEP13flickerResult
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNode14updateTestModeEb
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNode17updateObjectDictsEPNS_24H16ISPFilterGraphMessageE22PerceptionReturnStatus
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNode19asyncUpdateTestModeEb
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNodeC1EPNS_12H16ISPDeviceEjb
+ __ZN6H16ISP32H16ISPGraphExclavePerceptionNodeC2EPNS_12H16ISPDeviceEjb
+ __ZN6H16ISP37H16ISPGraphExclaveMotionDetectionNode18runMotionDetectionEPNS_24H16ISPFilterGraphMessageEb
+ __ZN6H16ISP37H16ISPGraphExclaveMotionDetectionNodeC1EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP37H16ISPGraphExclaveMotionDetectionNodeC2EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP37H16ISPGraphExclaveObjectDetectionNode20updateEnabledObjectsEPKj
+ __ZN6H16ISP37H16ISPGraphExclaveObjectDetectionNode25asyncUpdateEnabledObjectsEPKj
+ __ZN6H16ISP39H16ISPGraphExclaveIRObjectDetectionNode14InvokeEKRunKitEPNS_24H16ISPFilterGraphMessageEb
+ __ZN6H16ISP40H16ISPGraphExclaveAttentionDetectionNode29AddAttentionDetectionMetadataEPNS_24H16ISPFilterGraphMessageEP28ISPExclaveCoreChRunKitADRsltyb
+ __ZN6H16ISP40H16ISPGraphExclaveRGBObjectDetectionNode14InvokeEKRunKitEPNS_24H16ISPFilterGraphMessageEb
+ __ZN6H16ISP40H16ISPGraphExclaveRGBObjectDetectionNode27GenerateRGBObjectDictionaryEPNS_24H16ISPFilterGraphMessageERKNS_30ISPExclaveCoreChRunKitAnstRsltE
+ __ZNK6H16ISP12H16ISPDevice16getSensorChannelE25camera_module_descriptionS1_
+ __ZNK6H16ISP22H16ISPExclaveGraphNode11MustRunNodeEv
+ __ZNK6H16ISP22H16ISPExclaveGraphNode17GetExclaveKitTypeEv
+ __ZNK6H16ISP22H16ISPExclaveGraphNode7ChannelEv
+ __ZNK6H16ISP22H16ISPExclaveGraphNode7VerboseEv
+ __os_log_fault_impl
+ _abort
+ _dispatch_assert_queue$V2
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchalgoframerate
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitdeviceproximitydetection
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdrunkitdeviceproximitydetectionsetdevicemodels
+ _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_TestMode
+ _strtoull
+ _tb_message_configure_received
+ _tb_message_construct
+ _tb_message_decode_s64
+ _tb_message_destruct
+ _tb_message_encode_s64
+ _tb_transport_message_buffer_wrap_buffer
- _CFStringHasPrefix
- __ZN6H16ISP22H16ISPExclaveGraphNode7ChannelEv
- __ZN6H16ISP22H16ISPExclaveGraphNode7VerboseEv
- __ZN6H16ISP32H16ISPGraphExclavePerceptionNode17updateObjectDictsEPNS_24H16ISPFilterGraphMessageE45isprgbexclavekitmodule_perceptionreturnstatus
- __ZN6H16ISP32H16ISPGraphExclavePerceptionNodeC1EPNS_12H16ISPDeviceEj
- __ZN6H16ISP32H16ISPGraphExclavePerceptionNodeC2EPNS_12H16ISPDeviceEj
- __ZN6H16ISP37H16ISPGraphExclaveMotionDetectionNodeC2EPNS_12H16ISPDeviceEj14ExclaveKitType
- __ZN6H16ISP39H16ISPGraphExclaveIRMotionDetectionNode18runMotionDetectionEPNS_24H16ISPFilterGraphMessageE
- __ZN6H16ISP39H16ISPGraphExclaveIRMotionDetectionNodeC1EPNS_12H16ISPDeviceEj
- __ZN6H16ISP39H16ISPGraphExclaveIRMotionDetectionNodeC2EPNS_12H16ISPDeviceEj
- __ZN6H16ISP39H16ISPGraphExclaveIRObjectDetectionNode14InvokeEKRunKitEPNS_24H16ISPFilterGraphMessageE
- __ZN6H16ISP40H16ISPGraphExclaveAttentionDetectionNode29AddAttentionDetectionMetadataEPNS_24H16ISPFilterGraphMessageEP50ispirexclavekitmodule_ispexclavecorechrunkitadrsltyb
- __ZN6H16ISP40H16ISPGraphExclaveRGBMotionDetectionNode18runMotionDetectionEPNS_24H16ISPFilterGraphMessageE
- __ZN6H16ISP40H16ISPGraphExclaveRGBMotionDetectionNodeC1EPNS_12H16ISPDeviceEj
- __ZN6H16ISP40H16ISPGraphExclaveRGBMotionDetectionNodeC2EPNS_12H16ISPDeviceEj
- __ZN6H16ISP40H16ISPGraphExclaveRGBObjectDetectionNode14InvokeEKRunKitEPNS_24H16ISPFilterGraphMessageE
- __ZNK6H16ISP12H16ISPDevice16getSensorChannelE25camera_module_description
- __ZTIN6H16ISP39H16ISPGraphExclaveIRMotionDetectionNodeE
- __ZTIN6H16ISP40H16ISPGraphExclaveRGBMotionDetectionNodeE
- __ZTSN6H16ISP39H16ISPGraphExclaveIRMotionDetectionNodeE
- __ZTSN6H16ISP40H16ISPGraphExclaveRGBMotionDetectionNodeE
- __ZTVN6H16ISP39H16ISPGraphExclaveIRMotionDetectionNodeE
- __ZTVN6H16ISP40H16ISPGraphExclaveRGBMotionDetectionNodeE
- _kFigCaptureStreamProperty_DeskViewEnabled
CStrings:
+ "%01d%01d:%01d%01d:%01d%01d:%01d%01d"
+ "%s - All ExclaveKits are successfully setup. Conclave is now fully enabled!\n"
+ "%s - Attempting to async update the exclave graph node!\n"
+ "%s - Attempting to enable exclaves on a platform that isn't marked as supported!\n"
+ "%s - AttentionRequired = %{bool}d\n"
+ "%s - Camera Config Set Failed, ret %d \n"
+ "%s - Cannot enable exclave algorithms! error=%d\n"
+ "%s - Cannot get initial AE settings, resultStatus %d ret %d ch %d\n"
+ "%s - Cannot send channel info! channel=%u, ret=%d\n"
+ "%s - Cannot set attention settings! result=%u\n"
+ "%s - Cannot set face kit settings! result=%u\n"
+ "%s - Conclave not running for EKType: %s\n"
+ "%s - Could not setup Conclave on channel=%d\n"
+ "%s - Could not start exclave channel:%d, failure=%d\n"
+ "%s - Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading FDR CmCl calibration data\n"
+ "%s - Creating epipe graph node message! requestID=0x%08X, frameID=%U\n"
+ "%s - EK Framework algorithm enable returned failure=%d\n"
+ "%s - EK Framework enabled algorithms is NULL! Cannot start EK Framework!\n"
+ "%s - EK Framwework device enum type not found! platformID=0x%02X\n"
+ "%s - Enabled algorithms=0x%08x\n"
+ "%s - Exclave algos are enabled but no conclaves are running!\n"
+ "%s - Exiting filtration debug service thread, ch %d filtration type %d\n"
+ "%s - Failed to allocate graph message for requestID=0x%08X frameID=%u!\n"
+ "%s - Failed to configure exclave AE on channel=%d\n"
+ "%s - Failed to configure exclave PDP on channel=%d\n"
+ "%s - Failed to configure exclave streams, result=0x%08X\n\n"
+ "%s - Failed to create exclave graph manager, res=0x%08X\n\n"
+ "%s - Failed to get Exclave camera config for channel %d\n"
+ "%s - Failed to get Exclave camera config for channel=%d\n"
+ "%s - Failed to get camera config for channel %d, res=0x%08X\n"
+ "%s - Failed to get camera config for channel=%d, res=0x%08X\n\n"
+ "%s - Failed to get pearl camera calibration info!\n"
+ "%s - Failed to get sensor info for preset index=%d, channel=%d!\n"
+ "%s - Failed to power on Exclave Kit! result=0x%08X\n"
+ "%s - Failed to set target frame rate ret=0x%08x\n"
+ "%s - Failed to set up ExclaveKit error: 0x%08x\n\n"
+ "%s - Failed to set up conclave end point error: 0x%08x\n\n"
+ "%s - Failure in setting initial AE setting for channel %d, res=0x%08X\n"
+ "%s - Front camera not supported on this device\n"
+ "%s - ISP_EXCLAVEKIT_CMD_CH_DEBUG_CAPABILITY is failure Err: %d\n"
+ "%s - ISP_EXCLAVEKIT_CMD_CH_EXFILTRATION is failure Err: %d\n"
+ "%s - ISP_EXCLAVEKIT_CMD_CH_INFILTRATION is failure Err: %d\n"
+ "%s - ISP_EXCLAVEKIT_CMD_CH_OFF is failure Err: %d\n"
+ "%s - ISP_EXCLAVEKIT_CMD_CH_ON is failure Err: %d\n"
+ "%s - ISP_EXCLAVEKIT_CMD_CH_PDP_SET failed with ret: %d\n"
+ "%s - ISP_EXCLAVEKIT_CMD_CH_STOP is failure Err: %d\n"
+ "%s - ISP_EXCLAVEKIT_CMD_RGB_CH_CONCURRENT_FLAG_SET is failure Err: %d\n"
+ "%s - In concurrent streaming mode - Skip configuring Exclave AE\n"
+ "%s - Initializing EK Framework returned an error! result=%d\n\n"
+ "%s - Invalid Filtration Type %d\n"
+ "%s - LTC metadata %s (err=%d)\n\n"
+ "%s - Max Frame Rate call failed\n"
+ "%s - Min Frame Rate call failed ret %d\n"
+ "%s - PeriocularEnabled = %{bool}d\n"
+ "%s - Rear camera not supported on this device\n"
+ "%s - Sending EK info returned a failure=%d!\n"
+ "%s - Skipping configuring Exclave graph, Exclave Algorithms are not enabled!\n"
+ "%s - Skipping configuring Exclave graph, Exclave Kit is not configured!\n"
+ "%s - Successfully Stopped EK Channel=%d\n"
+ "%s - Successfully started EK channel=%d \n"
+ "%s - Successfully stopped EK Channel:%d\n"
+ "%s - Unable to power off EK Channel:%d, result=0x%08X\n"
+ "%s - Unable to start Debug Services, debug capabilities %d\n"
+ "%s - Unable to start exclave streams, res=0x%08X, channel=%d \n\n"
+ "%s - Unable to stop exclave streams, ret=0x%08X, channel=%d \n\n"
+ "%s - Updating the enabled objects array!\n"
+ "%s - [Exclaves]: Could not allocate cat body dictionary! Skipping!\n"
+ "%s - [Exclaves]: Could not allocate cat head dictionary! Skipping!\n"
+ "%s - [Exclaves]: Could not allocate dog body dictionary! Skipping!\n"
+ "%s - [Exclaves]: Could not allocate dog head dictionary! Skipping!\n"
+ "%s - [Exclaves]: RGB Object Detection Framework Success: channel=%u, numfaces=%u, numobjects=%u, valid=%u\n"
+ "%s - [Exclaves]: Runkit Object Detection channel=%d, reqID=0x%08X, pts=%llu, publishResult=%{bool}d\n"
+ "%s - [Exclaves]: face tracking secondary process failed! idl error=%u\n"
+ "%s - [Exclaves]: perception failed to run idl error=%u\n"
+ "%s - baseline streaming frameRate=%f\n"
+ "%s - channel=%u frameRate=%f\n"
+ "%s - channel=%u frameRate=%f algorithms=0x%08x\n"
+ "%s - failed to create flicker timer source\n"
+ "%s - failed to create flicker update queue\n"
+ "%s - failed to extract %s target frame rate\n"
+ "%s - failed to get flicker result ret=0x%08x\n"
+ "%s - failed to initialize flicker timer channel=%u ret=0x%08x\n"
+ "%s - failed to read property 0x%08x for channel %u\n"
+ "%s - failed to send frame rate %f to firmware ret=0x%08x\n"
+ "%s - failed to send frame rate ch=%u frameRate=%f err=%u success=%{bool}d\n"
+ "%s - failed to send frame rate to service ch=%u frameRate=%f ret=0x%08x\n"
+ "%s - failed to set flicker frequency channel=%u err=%u\n"
+ "%s - failed to update target frame rate ret=0x%08x\n"
+ "%s - failed to write property=0x%08x channel=%u err=%u\n"
+ "%s - invalid %s target frame rate value\n"
+ "%s - invalid attempt to set negative %s target frame rate\n"
+ "%s - invalid channel %u\n"
+ "%s - invalid flicker queue\n"
+ "%s - invalid remote connection\n"
+ "%s: invalid params - could not parse ISP property/value\n"
+ "%s:%s exists, length of the string = %ld.\n\n"
+ ".plist"
+ "/usr/local/share/firmware/isp/3525_01XX.dat"
+ "/usr/local/share/firmware/isp/7425_01XX.dat"
+ "2 "
+ "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
+ "AE init settings aeCounter %llu Exp %u ExpTime %d ReqID %llu SensorAG %d SensorDG %d IspDG %d VFrameSize %d VFrameTime %d Channel=%u\n"
+ "AE max framerate: channel=%u, maxfps=%u\n"
+ "AE min framerate: channel=%u, minfps=%u\n"
+ "APS_afRes_Private"
+ "APS_coilTemp_Private"
+ "APS_e_Private"
+ "APS_oisX_Private"
+ "APS_oisY_Private"
+ "APS_oisZEst_Private"
+ "APS_oisZGCOL_Private"
+ "APS_sensorTemp_Private"
+ "APS_w_Private"
+ "APS_zOffset_Private"
+ "APS_zPosGCOL_Private"
+ "APS_zPosLin_Private"
+ "APS_zPosition_Private"
+ "APS_zTarget_Private"
+ "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
+ "BackTeleCameraSNUM"
+ "C "
+ "ConfigureExclaveKitDebugServices"
+ "ConfigureFrameworkAlgorithmSettings"
+ "ConfigureFrameworkChannelSettings"
+ "ConfigureFrameworkPDPSettings"
+ "Couldn't read %s. Sensor is hosed/disconnected.\n"
+ "D "
+ "DCSAudioAccelConfig_Private"
+ "DCSAudioAccelConfig_dataRate_Private"
+ "DCSAudioAccelConfig_isFilterBypass_Private"
+ "DCSAudioAccelConfig_lowPwrMode_Private"
+ "DCSAudioAccelConfig_range_Private"
+ "DCSLTCEnabled"
+ "EK ANDK RunKit Command failed, ret=%d\n"
+ "Exclave Graph does not have object detection node! skipping update!\n"
+ "Exclave Graph not created! skipping update!\n"
+ "ExclaveHandleFlickerTimerEvent"
+ "ExclaveInitFlickerTimer"
+ "ExclaveSendFrameRateToFirmware"
+ "ExclaveSendFrameRateToService"
+ "ExclaveSendFrameRateToServiceInternal"
+ "ExclaveSetANDKFrameRateBucket"
+ "ExclaveSetTargetFrameRate"
+ "F "
+ "GetAPSPosition failed: channel=%u, ret=0x%08x\n\n"
+ "HITH "
+ "ISPExclaveExfiltrationThread"
+ "ISPExclaveFiltrationThreadMain"
+ "ISPExclaveInfiltrationThread"
+ "ISPPropertyValue_Private"
+ "KPD "
+ "LTC"
+ "LTCError"
+ "M "
+ "No module or No CmPM data (perhaps cuz the device does not support CmPM). Skip loading FDR CmPM calibration data\n"
+ "O "
+ "Projector Settings : ProbeMode %d StrobeMode %d StrobePulseWidth %f StrobeCurrentPercentage %f\n"
+ "Property_Private"
+ "R "
+ "RGB"
+ "RemoteAssistantGetFlickerResult"
+ "S "
+ "SFTM "
+ "SMVH "
+ "SMVP "
+ "SMVS "
+ "SMVSK "
+ "SPD "
+ "SR+ "
+ "STR "
+ "SecureAlgorithmSetTargetFrameRate"
+ "Sent FaceKit config! channel=%u, numtrackedfaces=%u\n"
+ "SetISPDCSDataLtcEnabled"
+ "SetISPProperty"
+ "SetMaximumFrameRateNow"
+ "SetupConclave"
+ "Shared LTC Data"
+ "Skip configuring initial AE settings, resultStatus %d ch %d\n"
+ "TB_ASSERT: (server->sendcmdchalgoframerate != NULL) && \"implementation for sendCmdChAlgoFrameRate is not present\""
+ "TB_ASSERT: (server->sendcmdchrunkitdeviceproximitydetection != NULL) && \"implementation for sendCmdChRunKitDeviceProximityDetection is not present\""
+ "TB_ASSERT: (server->sendcmdrunkitdeviceproximitydetectionsetdevicemodels != NULL) && \"implementation for sendCmdRunKitDeviceProximityDetectionSetDeviceModels is not present\""
+ "UpdateExclaveGraphNodeConfig"
+ "Value_Private"
+ "VdspSpecialization.hpp"
+ "[Exclaves] H16ISPGraphAttentionDetectionNode::%s AD RunKit failed, ret=%d\n"
+ "[Exclaves] H16ISPGraphExclaveEyeReliefNode::%s EK Runkit ER Runkit failed for reqid 0x%08X ret %d\n"
+ "[Exclaves]: H16ISPGraphAutoExposureNode::%s Debug AE results: reqID %llu aeCounter %llu exp %d ET %d Sensor AG %d Sensor DG %d ISP DG %d resultstatus=%d\n"
+ "[Exclaves]: H16ISPGraphExclaveAutoExposureNode::%s EK AE RunKit Failed for reqID 0x%08X resultStatus %d\n"
+ "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%s EK RGB ISP Manager RunKit failed, ret=%d\n"
+ "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%s EK RGB ISP Manager RunKit skipped reqid=0x%08x\n"
+ "[Exclaves]: running perception ch=%u publishResult=%{bool}d reqid=0x%08x\n"
+ "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"
+ "camChannel: %d, cmpmInstance: %s\n"
+ "com.apple.isp.flicker-update.queue"
+ "failed to run motion detection reqid=0x%08x err=%u hasValidResult=%{bool}d\n"
+ "failed to send IR sensor metadata ret=%d frameid=%u\n"
+ "failed to send rgb sensor metadata ret=%d frameid=%u\n"
+ "nCols2%2 == 1"
+ "nRows2%2 == 1"
+ "object detection"
+ "perception"
+ "runkit motion detection ch=%u publishResult=%{bool}d reqid=0x%08x\n"
+ "updateEnabledObjects"
+ "vDSPImgfir"
- "%s -  In concurrent streaming mode - Skip configuring Exclave AE\n"
- "%s - Camera Channel not supported for EK\n"
- "%s - Cannot configure Exclave PDP tberr=%d\n"
- "%s - Conclave IR Client Handle Invalid!\n"
- "%s - Conclave RGB Client Handle Invalid!\n"
- "%s - Failed to power on Exclave Kit, fatal\n"
- "%s - IR Max Frame Rate call failed\n"
- "%s - IR Min Frame Rate call failed\n"
- "%s - IR read IDL call failed\n"
- "%s - IR write IDL call failed\n"
- "%s - Invalid IR EK Client Handle\n"
- "%s - Invalid RGB EK Client Handle\n"
- "%s - Power ON EK Success\n"
- "%s - RGB Max Frame Rate call failed\n"
- "%s - RGB Min Frame Rate call failed\n"
- "%s - RGB read IDL call failed\n"
- "%s - RGB write IDL call failed\n"
- "%s - [Exclaves] Conclave not running for EKType: %d\n"
- "%s - [Exclaves] Set Flicker Freq call failed\n"
- "%s - [Exclaves] Skipping configuring Exclave graph, Exclave Algorithms are not enabled!\n"
- "%s - [Exclaves] Skipping configuring Exclave graph, Exclave Kit is not configured!\n"
- "%s - [Exclaves]: Camera Config Set Failed, result %d \n"
- "%s - [Exclaves]: Cannot get initial AE settings, ipcRet %d\n"
- "%s - [Exclaves]: Cannot get initial AE settings, ipcRet %d tberr %d ch %d\n"
- "%s - [Exclaves]: Cannot send channel info! channel=%u, result=%d\n"
- "%s - [Exclaves]: Cannot set FaceID AttentionDetection Periocular support to %{bool}d\n"
- "%s - [Exclaves]: Cannot set FaceID AttentionDetection attention requirement to true\n"
- "%s - [Exclaves]: Creating epipe graph node message! requestID=0x%08X, frameID=%U\n"
- "%s - [Exclaves]: EK IR CMD off failed, tberr=%d\n"
- "%s - [Exclaves]: EK IR CMD on failed, tberr=%d\n"
- "%s - [Exclaves]: EK IR Channel stop failed %d \n"
- "%s - [Exclaves]: EK RGB CMD off failed %d\n"
- "%s - [Exclaves]: EK RGB CMD on failed, tberr=%d\n"
- "%s - [Exclaves]: Enabling Exclave algo bitmask: %d\n"
- "%s - [Exclaves]: Exclave algos are enabled but no Conclaves are running! (treat as fatal)\n"
- "%s - [Exclaves]: Failed to allocate graph message for requestID=0x%08X frameID=%u!\n"
- "%s - [Exclaves]: Failed to create exclave graph manager, res=0x%08X\n\n"
- "%s - [Exclaves]: Failed to get Exclave camera config for channel %d\n"
- "%s - [Exclaves]: Failed to get camera config for channel %d, res=0x%08X\n"
- "%s - [Exclaves]: Failed to get camera config for channel %d, res=0x%08X\n\n"
- "%s - [Exclaves]: ISP Mgr IR CH Start Failed, result=%d \n"
- "%s - [Exclaves]: ISP Mgr RGB CH Start Failed, result %d\n"
- "%s - [Exclaves]: Invalid IR Client Handle!\n"
- "%s - [Exclaves]: Invalid RGB Client Handle!\n"
- "%s - [Exclaves]: RGB EK Object Detection RunKit failed, tberr=%d EK result=%{bool}d\n"
- "%s - [Exclaves]: RGB ISP Mgr Algo Enable Failed\n"
- "%s - [Exclaves]: RGB Object Detection IDL Success: channel=%u, numfaces=%u, numobjects=%u, valid=%u\n"
- "%s - [Exclaves]: RGB concurrent cmd Failed\n"
- "%s - [Exclaves]: Runkit Object Detection channel=%d, reqID=0x%08X, pts=%llu\n"
- "%s - [Exclaves]: Send RGB Perception Framerate failed!, result=%d, channel=%d\n"
- "%s - [Exclaves]: Skipping perception transfer!\n"
- "%s - [Exclaves]: Streaming Channel not supported on exclaves, ch=%d\n"
- "%s - [Exclaves]: Successfully started EK channel %d \n"
- "%s - [Exclaves]: Unable to power off Exclave Kit\n"
- "%s - [Exclaves]: Unable to stop EK RGB Channel, tberr=%d\n"
- "%s - [Exclaves]: Unable to stop exclave streams, ret=0x%08X, channel=%d \n\n"
- "%s - [Exclaves]: cannot configure face kit\n"
- "%s - [Exclaves]: failed to configure exclave AE\n"
- "%s - [Exclaves]: failed to configure exclave PDP\n"
- "%s - [Exclaves]: failed to configure exclave streams, treat as fatal 0x%08X\n\n"
- "%s - [Exclaves]: failed to get channel distortion info! Extrinsics info for this channel will not be correct!\n"
- "%s - [Exclaves]: failed to get pearl camera calibration info!\n"
- "%s - [Exclaves]: failed to get sensor info!\n"
- "%s - [Exclaves]: failure in setting initial AE setting for channel %d, res=0x%08X\n"
- "%s - [Exclaves]: send to perception IDL failed, tberr=%u ipcret=%{bool}d\n"
- "%s - [Exclaves]: sending algo enable cmd to EK failed!\n"
- "%s - [Exclaves]: unable to start exclave streams, res=0x%08X, channel=%d \n\n"
- "%s - [Exclaves]:%s Successfully stopped EK channel %d \n"
- "%s - error: 0x%08X\n"
- "%s - failed to set target frame rate channel=%u framerate=%f ret=0x%08x\n"
- "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
- "ANDK algorithm did not run for reqid: 0x%08x\n"
- "ANDK algorithm ran for reqid: 0x%08x\n"
- "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
- "BackCameraSNUM/BackSuperWideCameraSNUM exists - load FDR CmPM calibration data\n\n"
- "ConfigureExclavePDP"
- "Couldn't read BackCameraSNUM and BackSuperWideCameraSNUM. Sensor is hosed/disconnected. Skip loading FDR CmPM calibration data\n"
- "Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading FDR CmCl calibration data\n"
- "Failed ANDK runkit IDL\n"
- "H16ISPGraphExclaveObjectDetectionNode"
- "IR AE max framerate: channel=%u, maxfps=%u\n"
- "IR AE min framerate: channel=%u, minfps=%u\n"
- "IR property read: channel=%u, property=%u\n"
- "IRMotionDetectionResultCreateDictionaryRepresentation"
- "Invalid RGB Conclave Handle\n"
- "RGB AE max framerate: channel=%u, maxfps=%u\n"
- "RGB AE min framerate: channel=%u, minfps=%u\n"
- "RGB property read: channel=%u, property=%u\n"
- "RGB property write: channel=%u, property=%u, value=%u\n"
- "RGBMotionDetectionResultCreateDictionaryRepresentation"
- "SetDeskViewEnabled"
- "SetFlickerFrequency"
- "[Conclave] All ExclaveKits are successfully setup. Conclave is now fully enabled\n"
- "[Conclave] failed to set up ExclaveKit error: 0x%08x\n\n"
- "[Conclave] failed to set up end point error: 0x%08x\n\n"
- "[Exclaves] H16ISPGraphAttentionDetectionNode::%s AD RunKit failed, tberr=%d ipcret=%d\n"
- "[Exclaves] H16ISPGraphAttentionDetectionNode::%s Invalid IR Client Handle\n"
- "[Exclaves] H16ISPGraphExclaveEyeReliefNode::%s EK Runkit ER Runkit failed for reqid 0x%08X ipcRet %d\n"
- "[Exclaves] H16ISPGraphExclaveEyeReliefNode::%s Invalid IR Client Handle\n"
- "[Exclaves]: AE Configuration Set: channel=%u, totalH=%u, totalvmin=%u, max framerate=%u, min framerate=%u\n"
- "[Exclaves]: AE init settings aeCounter %llu Exp %u ExpTime %d ReqID %llu SensorAG %d SensorDG %d IspDG %d VFrameSize %d VFrameTime %d Channel=%u\n"
- "[Exclaves]: H16ISPGraphAutoExposureNode::%s Debug AE results: reqID %llu aeCounter %llu exp %d ET %d Sensor AG %d Sensor DG %d ISP DG %d\n"
- "[Exclaves]: H16ISPGraphAutoExposureNode::%s Debug AE results: reqID %llu aeCounter %llu exp %d ET %d Sensor AG %d Sensor DG %d ISP DG %d ipcresult=%{bool}d\n"
- "[Exclaves]: H16ISPGraphExclaveAutoExposureNode::%s EK AE RunKit Failed for reqID 0x%08X ipcret %d\n"
- "[Exclaves]: H16ISPGraphExclaveAutoExposureNode::%s EK RunKit AE Failed for reqID 0x%08X ipcret %d\n"
- "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%s EK IR ISP Manager RunKit failed, tberr=%d ipcret=%{bool}d\n"
- "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%s EK RGB ISP Manager RunKit failed, tberr=%d ipcret=%{bool}d\n"
- "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%s EK RGB ISP Manager RunKit requestid=0x%08X\n"
- "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%s Invalid IR Client Handle\n"
- "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%s Invalid RGB Client Handle\n"
- "[Exclaves]: IR ISP Manager IDL Success: channel=%u, requestid=%u\n"
- "[Exclaves]: IR property write: property=%u, value=%u\n"
- "[Exclaves]: Projector Settings : ProbeMode %d StrobeMode %d StrobePulseWidth %f StrobeCurrentPercentage %f\n"
- "[Exclaves]: Sending ANST results to perception!\n"
- "[Exclaves]: Sent IR Algorithm enable cmd!\n"
- "[Exclaves]: Sent IR ISP Mgr start! channel=%u, width=%u, height=%u\n"
- "[Exclaves]: Sent IR channel stop!\n"
- "[Exclaves]: Sent IR cmd off!\n"
- "[Exclaves]: Sent IR cmd on!\n"
- "[Exclaves]: Sent RGB FaceKit config! channel=%u, numtrackedfaces=%u\n"
- "[Exclaves]: Sent RGB Perception Framerate=%d channel=%d\n"
- "[Exclaves]: Sent RGB cmd off!\n"
- "[Exclaves]: Sent RGB cmd on!\n"
- "[Exclaves]: Sent RGB cmd start! channel=%u, width=%u, height=%u\n"
- "[Exclaves]: Sent RGB stop!\n"
- "[Exclaves]: Skip configuring initial AE settings, ipcRet %d\n"
- "[Exclaves]: Skip configuring initial AE settings, ipcRet %d ch %d\n"
- "[Exclaves]: face tracking secondary process failed: tberr=%u result=%{bool}d\n"
- "[Exclaves][%s:%d] Invalid camChannel (%u / max:%u)\n\n"
- "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"
- "failed to run ir motion detection reqid=0x%08x tberr=%u ipcret=%{bool}d hasvalidresult=%{bool}d\n"
- "failed to run rgb motion detection reqid=0x%08x tberr=%u ipcret=%{bool}d hasvalidresult=%{bool}d\n"
- "failed to send IR sensor metadata tberr=%u result=%{bool}d frameid=%u\n"
- "failed to send rgb sensor metadata tberr=%u result=%{bool}d frameid=%u\n"
- "invalid IR conclave client handle\n"
- "invalid RGB conclave client handle\n"
- "invalid ir conclave client handle\n"
- "invalid rgb conclave client handle\n"
- "ir runkit motion detection ch=%u reqid=0x%08x\n"
- "rgb runkit motion detection ch=%u reqid=0x%08x\n"

```
