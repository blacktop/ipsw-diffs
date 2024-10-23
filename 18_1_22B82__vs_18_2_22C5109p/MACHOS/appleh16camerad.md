## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-3.114.0.0.0
-  __TEXT.__text: 0x78448
+3.316.903.0.0
+  __TEXT.__text: 0x78c98
   __TEXT.__auth_stubs: 0x1e70
-  __TEXT.__objc_stubs: 0x13c0
+  __TEXT.__objc_stubs: 0x1360
   __TEXT.__init_offsets: 0x14
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__gcc_except_tab: 0x226c
-  __TEXT.__const: 0x2d00
-  __TEXT.__cstring: 0x80e8
-  __TEXT.__oslogstring: 0x50b9
+  __TEXT.__gcc_except_tab: 0x2244
+  __TEXT.__const: 0x2cf0
+  __TEXT.__cstring: 0x818b
   __TEXT.__objc_classname: 0x89
-  __TEXT.__objc_methname: 0x153f
-  __TEXT.__objc_methtype: 0x11e8
-  __TEXT.__unwind_info: 0x1490
+  __TEXT.__oslogstring: 0x52af
+  __TEXT.__objc_methname: 0x14ef
+  __TEXT.__objc_methtype: 0x11fa
+  __TEXT.__unwind_info: 0x14a8
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__auth_got: 0xf48
-  __DATA_CONST.__got: 0xad8
+  __DATA_CONST.__got: 0xad0
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0x6440
-  __DATA_CONST.__cfstring: 0x3160
+  __DATA_CONST.__const: 0x7e90
+  __DATA_CONST.__cfstring: 0x3180
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x808
-  __DATA.__objc_selrefs: 0x570
+  __DATA.__objc_selrefs: 0x558
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x206c10
-  __DATA.__bss: 0x184
-  __DATA.__common: 0x60
+  __DATA.__data: 0x216d68
+  __DATA.__bss: 0x101
+  __DATA.__common: 0x5c
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1535
-  Symbols:   858
-  CStrings:  1890
+  Functions: 1541
+  Symbols:   857
+  CStrings:  1897
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ _strerror
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc
- _matrix_identity_float3x3
CStrings:
+ "\tDefault calibration from NVM: deice is not ready or no ToF channel found"
+ "\tSerial nubmers size mismatch"
+ "\tValidting SN (registry vs cache)"
+ "%!s(MISSING) - Failed to open file: %!s(MISSING) %!s(MISSING)\n"
+ "%!s(MISSING) : Load override %!s(MISSING) cal data: Size = %!l(MISSING)d (== %!l(MISSING)d ?); Status = %!x(MISSING)\n"
+ "%!s(MISSING) : Status = %!x(MISSING); OCCl (%!s(MISSING)) data - %!s(MISSING) \n"
+ "%!s(MISSING) OCCl is not a dict (FDR2.0?), Unauthorized swap or No OCCl data (perhaps cuz the device does not support OCCl) [error]: %!s(MISSING) \n"
+ "/usr/local/share/firmware/isp/2325_01XX.dat"
+ "/usr/local/share/firmware/isp/OCCl-cmca.DAT"
+ "/usr/local/share/firmware/isp/OCCl-cmcd.DAT"
+ "3.316"
+ "903"
+ "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
+ "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
+ "BackTeleCameraModuleSerialNumString"
+ "Couldn't read back camera module serial number. Sensor is hosed/disconnected. Skip loading OCCl calibration data\n"
+ "FrontCameraModuleSerialNumString exists - load OCCl calibration data\n\n"
+ "LoadOCClCalDataFile"
+ "OCCl"
+ "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"
+ "backTeleCameraModuleSerialNumString exists - load OCCl calibration data\n\n"
+ "cmca"
+ "cmcd"
- "\tDefault calibration from NVM: device is not ready or no ToF channel found"
- "\tSerial numbers sized mismatch"
- "\tValidating SN (registry vs cache)"
- "%!s(MISSING) - Failed to open file: %!s(MISSING)\n"
- ".bin"
- ".plist"
- "3.114"
- "@36@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?}^{DCSAudioAccelManager}}16I24^{H16ISPServicesRemote=@@^?^v*}28"
- "B24@0:8^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?}^{DCSAudioAccelManager}}16"
- "^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}I^{H16ISPMotionManager}^{H16ISPServicesRemote}[2{H16ISPConclaveService=^{tb_endpoint_s}i^vB{ispirexclavekitmodule_ispirexclavekit=^{tb_connection_s}}{isprgbexclavekitmodule_isprgbexclavekit=^{tb_connection_s}}}]^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}BBII^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?}^{DCSAudioAccelManager}}"
- "adjustForImageRotation:"
- "calibration"
- "reference"
- "setCameraToPlatformTransform:"
- "setWmcamToMcamExtrinsics:"
- "spotDB"

```
