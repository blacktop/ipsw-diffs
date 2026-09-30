## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-3.415.0.0.0
-  __TEXT.__text: 0x79408
-  __TEXT.__auth_stubs: 0x1dd0
+3.504.14.0.0
+  __TEXT.__text: 0x78f7c
+  __TEXT.__auth_stubs: 0x1de0
   __TEXT.__objc_stubs: 0x1360
   __TEXT.__init_offsets: 0x14
-  __TEXT.__objc_methlist: 0x11c
-  __TEXT.__gcc_except_tab: 0x220c
-  __TEXT.__const: 0x2cf0
-  __TEXT.__cstring: 0x81f4
+  __TEXT.__objc_methlist: 0x268
+  __TEXT.__gcc_except_tab: 0x21f8
+  __TEXT.__const: 0x2ce0
+  __TEXT.__cstring: 0x8378
   __TEXT.__objc_classname: 0x89
   __TEXT.__oslogstring: 0x5335
   __TEXT.__objc_methname: 0x14ef
-  __TEXT.__objc_methtype: 0x124e
-  __TEXT.__unwind_info: 0x14d8
-  __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0xef8
+  __TEXT.__objc_methtype: 0x105f
+  __TEXT.__unwind_info: 0x1428
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__auth_got: 0xf00
   __DATA_CONST.__got: 0xad0
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0x8068
+  __DATA_CONST.__const: 0x8070
   __DATA_CONST.__cfstring: 0x3200
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x808
-  __DATA.__objc_selrefs: 0x558
+  __DATA.__objc_const: 0x5a8
+  __DATA.__objc_selrefs: 0x5f0
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x267d60
+  __DATA.__data: 0x331d60
   __DATA.__bss: 0x101
   __DATA.__common: 0x5c
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1551
-  Symbols:   847
-  CStrings:  1904
+  Functions: 1509
+  Symbols:   848
+  CStrings:  1907
 
Symbols:
+ _objc_retainAutoreleaseReturnValue
CStrings:
+ "/usr/local/share/firmware/isp/3525_02XX.dat"
+ "/usr/local/share/firmware/isp/7525_01XX.dat"
+ "14"
+ "3.504"
+ "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
+ "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
+ "LSC_GET_BASE_U32_PT(chInfo1[ch]) % (chInfo1[ch]->gridCountX * chInfo1[ch]->gridCountY) == 0"
+ "LSC_GET_BASE_U32_PT(chInfo2[ch]) % (chInfo2[ch]->gridCountX * chInfo2[ch]->gridCountY) == 0"
+ "Savage/SavagePatch%s.DAT"
+ "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"
+ "chInfo1[ch]->gridCountX == chInfo1[0]->gridCountX"
+ "chInfo1[ch]->gridCountY == chInfo1[0]->gridCountY"
+ "chInfo2[ch]->gridCountX == chInfo2[0]->gridCountX"
+ "chInfo2[ch]->gridCountY == chInfo2[0]->gridCountY"
- "3.415"
- "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
- "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
- "B3"
- "BA"
- "FlowAccumulate"
- "FlowAccumulateNeon64"
- "FlowAccumulateScalar"
- "FlowEstimateGainError"
- "Savage/SavagePatch%s%s.DAT"
- "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"

```
