## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-3.414.0.0.0
-  __TEXT.__text: 0x6a3c4
-  __TEXT.__auth_stubs: 0x16f0
-  __TEXT.__objc_stubs: 0xa80
+3.512.0.0.0
+  __TEXT.__text: 0x67144
+  __TEXT.__auth_stubs: 0x16a0
+  __TEXT.__objc_stubs: 0x9c0
   __TEXT.__init_offsets: 0x24
-  __TEXT.__objc_methlist: 0x154
-  __TEXT.__cstring: 0x5853
-  __TEXT.__const: 0x145d8
+  __TEXT.__objc_methlist: 0x334
+  __TEXT.__cstring: 0x58c4
+  __TEXT.__const: 0x14e30
   __TEXT.__gcc_except_tab: 0xfd8
-  __TEXT.__oslogstring: 0x48eb
-  __TEXT.__objc_methname: 0xaa3
+  __TEXT.__oslogstring: 0x42ce
+  __TEXT.__objc_methname: 0x9f4
   __TEXT.__objc_classname: 0xaa
-  __TEXT.__objc_methtype: 0x6ef
-  __TEXT.__unwind_info: 0xf40
-  __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0xb88
-  __DATA_CONST.__got: 0x1158
+  __TEXT.__objc_methtype: 0x62a
+  __TEXT.__unwind_info: 0xea0
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__auth_got: 0xb60
+  __DATA_CONST.__got: 0x1138
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x78a0
+  __DATA_CONST.__const: 0x8868
   __DATA_CONST.__cfstring: 0x21e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x938
-  __DATA.__objc_selrefs: 0x330
+  __DATA.__objc_const: 0x5c8
+  __DATA.__objc_selrefs: 0x3a0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x268298
-  __DATA.__bss: 0x840
+  __DATA.__data: 0x332288
+  __DATA.__bss: 0x940
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 18AF350B-071D-31BA-B34F-86B9180A25B4
-  Functions: 1270
-  Symbols:   941
-  CStrings:  1722
+  UUID: F452AFB2-7FFD-31DB-B7F8-08B94EC1D50B
+  Functions: 1177
+  Symbols:   932
+  CStrings:  1680
 
Symbols:
+ _os_variant_allows_internal_security_policies
+ _os_variant_has_internal_content
- _OBJC_CLASS_$_STActivityAttribution
- _OBJC_CLASS_$_STMediaStatusDomainCameraCaptureAttribution
- _OBJC_CLASS_$_STMediaStatusDomainCameraDescriptor
- _kFigCaptureStreamMetadata_InvalidDueToNoSensorAccess
- _tb_client_connection_message_construct
- _tb_client_connection_message_destruct
- _tb_connection_send_query
- _tb_message_complete
- _tb_message_decode_bool
- _tb_message_encode_u32
- _tb_message_encode_u64
CStrings:
+ "%s - Assistant Version %s\n"
+ "%s - illegal RPC access\n"
+ "%s-Ch%d.DAT"
+ "/usr/local/share/firmware/isp/3525_02XX.dat"
+ "/usr/local/share/firmware/isp/7525_01XX.dat"
+ "/usr/local/share/firmware/isp/CmPM-CALm"
+ "/usr/local/share/firmware/isp/CmPM-DPCd"
+ "/usr/local/share/firmware/isp/CmPM-DPCm"
+ "/usr/local/share/firmware/isp/CmPM-brcl"
+ "/usr/local/share/firmware/isp/CmPM-brgd"
+ "/usr/local/share/firmware/isp/CmPM-dcnu"
+ "3.512"
+ "@36@0:8^{H16ISPExtensionProvider=}16^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}^{H16ISPServicesRemote}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}I^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}24I32"
+ "EnableV5LTMMetadata"
+ "LSC_GET_BASE_U32_PT(chInfo1[ch]) % (chInfo1[ch]->gridCountX * chInfo1[ch]->gridCountY) == 0"
+ "LSC_GET_BASE_U32_PT(chInfo2[ch]) % (chInfo2[ch]->gridCountX * chInfo2[ch]->gridCountY) == 0"
+ "Savage/SavagePatch%s.DAT"
+ "chInfo1[ch]->gridCountX == chInfo1[0]->gridCountX"
+ "chInfo1[ch]->gridCountY == chInfo1[0]->gridCountY"
+ "chInfo2[ch]->gridCountX == chInfo2[0]->gridCountX"
+ "chInfo2[ch]->gridCountY == chInfo2[0]->gridCountY"
- "%s - Assistant Version %s.%s\n"
- "%s - CIL off request\n"
- "%s - CIL on request\n"
- "%s - Calling ISP_CILRequestPerChannel error: 0x%08X (%u/false)\n"
- "%s - Calling ISP_CILRequestPerChannel(Line:%d) error: 0x%08X (%u/%u)\n"
- "%s - Cannot unregister epipedone callback, invalid channel = %d numChannels = %d\n"
- "%s - Conclave IR Client Handle Invalid!\n"
- "%s - Conclave RGB Client Handle Invalid!\n"
- "%s - Failed enabling exclave streaming mode res=0x%08x\n"
- "%s - Failed to unregister epipe done callback in kernel , error: 0x%08X\n"
- "%s - IOConnect Failed, status = 0x%08x\n"
- "%s - IR Max Frame Rate call failed\n"
- "%s - IR Min Frame Rate call failed\n"
- "%s - RGB Max Frame Rate call failed\n"
- "%s - RGB Min Frame Rate call failed\n"
- "%s - SetBufferPoolConfiguration for exclave meta pool error: res=0x%08X\n"
- "%s - Unable to register epipe done callback, res=0x%08X\n"
- "%s - [%d] [CIL] Call ISP_CILRequestPerChannel (%u/%u)\n"
- "%s - [%d] [CIL] Call ISP_CILRequestPerChannel (%u/false)\n"
- "%s - [Exclaves] H16ISPFrameReceiver - Exclave buffer ready notification received, requestID 0x%08X, epipe status: %d\n"
- "%s - [Exclaves] H16ISPFrameReceiver - Invalid number of epipe done arguments, numArgs=%d, bail \n\n"
- "%s - [Exclaves] H16ISPFrameReceiver - epipe plugin callback not registered!\n"
- "%s - process name is mediaserverd or cameracaptured, so skip calling SystemsStatus\n"
- "%s - systemStatus is NULL\n"
- "/usr/local/share/firmware/isp/CmPM-CALm.DAT"
- "/usr/local/share/firmware/isp/CmPM-DPCd.DAT"
- "/usr/local/share/firmware/isp/CmPM-DPCm.DAT"
- "/usr/local/share/firmware/isp/CmPM-brcl.DAT"
- "/usr/local/share/firmware/isp/CmPM-brgd.DAT"
- "/usr/local/share/firmware/isp/CmPM-dcnu.DAT"
- "3.414"
- "@36@0:8^{H16ISPExtensionProvider=}16^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}24I32"
- "B3"
- "BA"
- "EPipeDone"
- "EnableExclaveDebug"
- "FlowAccumulate"
- "FlowAccumulateNeon64"
- "FlowAccumulateScalar"
- "FlowEstimateGainError"
- "IR AE max framerate: channel=%u, maxfps=%u\n"
- "IR AE min framerate: channel=%u, minfps=%u\n"
- "ISP_CILRequestPerChannel"
- "ISP_GetExclavePlatformStatus"
- "ISP_SetExclaveMaximumFrameRate"
- "ISP_SetExclaveMinimumFrameRate"
- "ISP_UnregisterEPipeDoneCallback"
- "NotifySystemStatusForCIL"
- "RGB AE max framerate: channel=%u, maxfps=%u\n"
- "RGB AE min framerate: channel=%u, minfps=%u\n"
- "Savage/SavagePatch%s%s.DAT"
- "[%s:%d] Invalid camChannel (%u / max:%u)\n\n"
- "[%s:%d] [CIL] ISP_CILRequestPerChannel calls kernel (%u/%u)\n\n"
- "addCameraAttribution:"
- "attributionWithAuditToken:"
- "cameracaptured"
- "exclaves"
- "initWithCameraDescriptor:activityAttribution:"
- "initWithCameraIdentifier:"
- "mediaserverd"
- "removeCameraAttribution:"
- "updateVolatileDataWithBlock:"
- "v16@?0@\"STMutableMediaStatusDomainData\"8"

```
