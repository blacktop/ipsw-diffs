## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-3.324.0.0.0
-  __TEXT.__text: 0x78d30
-  __TEXT.__auth_stubs: 0x1e70
+3.407.0.0.0
+  __TEXT.__text: 0x79408
+  __TEXT.__auth_stubs: 0x1dd0
   __TEXT.__objc_stubs: 0x1360
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__gcc_except_tab: 0x2244
+  __TEXT.__gcc_except_tab: 0x220c
   __TEXT.__const: 0x2cf0
-  __TEXT.__cstring: 0x81b8
+  __TEXT.__cstring: 0x81f4
   __TEXT.__objc_classname: 0x89
-  __TEXT.__oslogstring: 0x52df
+  __TEXT.__oslogstring: 0x5335
   __TEXT.__objc_methname: 0x14ef
-  __TEXT.__objc_methtype: 0x11fa
-  __TEXT.__unwind_info: 0x14b0
+  __TEXT.__objc_methtype: 0x124e
+  __TEXT.__unwind_info: 0x14d8
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0xf48
+  __DATA_CONST.__auth_got: 0xef8
   __DATA_CONST.__got: 0xad0
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0x7ea8
-  __DATA_CONST.__cfstring: 0x3180
+  __DATA_CONST.__const: 0x8068
+  __DATA_CONST.__cfstring: 0x3200
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x558
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x216d68
+  __DATA.__data: 0x267d60
   __DATA.__bss: 0x101
   __DATA.__common: 0x5c
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1541
-  Symbols:   857
-  CStrings:  1899
+  Functions: 1551
+  Symbols:   847
+  CStrings:  1904
 
Symbols:
+ _AMFDRSealingMapCopyLocalDict
+ _AMFDRSealingMapCopyMultiInstanceForClass
+ _abort
- _FigHostTimeToNanoseconds
- __ZNSt3__18ios_base33__set_badbit_and_consider_rethrowEv
- ___cxa_end_catch
- _tb_client_connection_message_construct
- _tb_client_connection_message_destruct
- _tb_connection_send_query
- _tb_message_complete
- _tb_message_decode_bool
- _tb_message_encode_f32
- _tb_message_encode_u16
- _tb_message_encode_u32
- _tb_message_encode_u64
- _tb_message_encode_u8
CStrings:
+ "%s - Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading FDR CmCl calibration data\n"
+ "%s - Front camera not supported on this device\n"
+ "%s - Rear camera not supported on this device\n"
+ "%s:%s exists, length of the string = %ld.\n\n"
+ "/usr/local/share/firmware/isp/3525_01XX.dat"
+ "/usr/local/share/firmware/isp/7425_01XX.dat"
+ "3.407"
+ "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
+ "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
+ "BackTeleCameraSNUM"
+ "Couldn't read %s. Sensor is hosed/disconnected.\n"
+ "LTC"
+ "LTCError"
+ "No module or No CmPM data (perhaps cuz the device does not support CmPM). Skip loading FDR CmPM calibration data\n"
+ "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}^{H16ISPExclaveDebugService}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"
+ "camChannel: %d, cmpmInstance: %s\n"
- "%s - [Exclaves] Set Flicker Freq call failed\n"
- "3.324"
- "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
- "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
- "BackCameraSNUM/BackSuperWideCameraSNUM exists - load FDR CmPM calibration data\n\n"
- "Couldn't read BackCameraSNUM and BackSuperWideCameraSNUM. Sensor is hosed/disconnected. Skip loading FDR CmPM calibration data\n"
- "Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading FDR CmCl calibration data\n"
- "ISP_GetExclaveEnablementStatus"
- "SetFlickerFrequency"
- "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"
- "exclaves"

```
