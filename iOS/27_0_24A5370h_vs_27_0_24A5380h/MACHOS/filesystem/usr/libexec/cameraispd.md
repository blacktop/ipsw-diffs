## cameraispd

> `/usr/libexec/cameraispd`

```diff

-  __TEXT.__text: 0x7c5e8
-  __TEXT.__auth_stubs: 0x1ee0
+  __TEXT.__text: 0x7cb80
+  __TEXT.__auth_stubs: 0x1f20
   __TEXT.__objc_stubs: 0xf80
   __TEXT.__objc_methlist: 0x270
   __TEXT.__gcc_except_tab: 0x18c8
-  __TEXT.__const: 0x2c08
-  __TEXT.__cstring: 0x75df
-  __TEXT.__oslogstring: 0x5ecb
+  __TEXT.__const: 0x2c18
+  __TEXT.__cstring: 0x7754
+  __TEXT.__oslogstring: 0x5f4b
   __TEXT.__objc_methname: 0x1295
   __TEXT.__objc_classname: 0x88
-  __TEXT.__objc_methtype: 0x1034
-  __TEXT.__unwind_info: 0x1238
-  __DATA_CONST.__const: 0x92a8
-  __DATA_CONST.__cfstring: 0x2a60
+  __TEXT.__objc_methtype: 0x1067
+  __TEXT.__unwind_info: 0x1248
+  __DATA_CONST.__const: 0x9a28
+  __DATA_CONST.__cfstring: 0x2bc0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0xf80
-  __DATA_CONST.__got: 0xc80
+  __DATA_CONST.__auth_got: 0xfa0
+  __DATA_CONST.__got: 0xc90
   __DATA_CONST.__auth_ptr: 0x50
   __DATA.__objc_const: 0x5c8
   __DATA.__objc_selrefs: 0x4f8

   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x3aede0
   __DATA.__common: 0xf
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x8c
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1550
-  Symbols:   911
-  CStrings:  2172
+  Functions: 1556
+  Symbols:   917
+  CStrings:  2194
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _AMFDRSealingMapCopyLocalData
+ _CFPreferencesGetAppBooleanValue
+ _kFigCaptureStreamMetadata_AH
+ _kFigCaptureStreamMetadata_IREnabled
+ _unlink
+ _xpc_connection_copy_entitlement_value
CStrings:
+ "%s: Failed to create file \"%s\" because of permissions. Deleting it (in case it exists) and trying again"
+ "%s: Failed to create file %s: %s"
+ "/usr/local/share/firmware/isp/dcs_isp_fw.bin"
+ "20.55.3"
+ "<UNKNOWN>"
+ "@36@0:8^{ISPDevice={ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{ISPDeviceCachedConfigChannel}^{ISPModuleParams}}^?^v^{ISPDeviceController}I^{__CFDictionary}I^{ISPMotionManager}^{ISPDeviceImpactManager}^{ISPServicesRemote}^{ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{ISPFirmwareWorkProcessor}BBII^{ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[7{ISPNotification=*Bi}][7{ISPNotification=*Bi}]{ISPNotification=*Bi}{ISPNotification=*Bi}{ISPNotification=*Bi}II^{__CFDictionary}{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{ISPServicesRemote=@@^?^v*}28"
+ "Audit: XPC peer missing %{public}s (pid %{private}d) — would reject\n"
+ "B24@0:8^{ISPDevice={ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{ISPDeviceCachedConfigChannel}^{ISPModuleParams}}^?^v^{ISPDeviceController}I^{__CFDictionary}I^{ISPMotionManager}^{ISPDeviceImpactManager}^{ISPServicesRemote}^{ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{ISPFirmwareWorkProcessor}BBII^{ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[7{ISPNotification=*Bi}][7{ISPNotification=*Bi}]{ISPNotification=*Bi}{ISPNotification=*Bi}{ISPNotification=*Bi}II^{__CFDictionary}{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
+ "EnforceClientEntitlement"
+ "ISPServicesRemoteFDRCalDataKey"
+ "PRF1: %s-%s: Unexpected references size (Expected %ld, Got %d)\n"
+ "PRF1: %s-%s: Unexpected references size after compression (Expected %ld, Got %ld)\n"
+ "PRF1: %s-%s: Unknown format %d"
+ "PRF1: Couldn't create reference file %s to write\n"
+ "PRF1: Failed to save plist %@\n"
+ "Rejecting XPC peer missing %{public}s (pid %{private}d)\n"
+ "^{ISPDevice={ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{ISPDeviceCachedConfigChannel}^{ISPModuleParams}}^?^v^{ISPDeviceController}I^{__CFDictionary}I^{ISPMotionManager}^{ISPDeviceImpactManager}^{ISPServicesRemote}^{ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{ISPFirmwareWorkProcessor}BBII^{ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[7{ISPNotification=*Bi}][7{ISPNotification=*Bi}]{ISPNotification=*Bi}{ISPNotification=*Bi}{ISPNotification=*Bi}II^{__CFDictionary}{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"
+ "com.apple.private.cameraispd.client"
+ "fopen_protected"
- "20.50.6"
- "@36@0:8^{ISPDevice={ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{ISPDeviceCachedConfigChannel}^{ISPModuleParams}}^?^v^{ISPDeviceController}I^{__CFDictionary}I^{ISPMotionManager}^{ISPDeviceImpactManager}^{ISPServicesRemote}^{ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{ISPFirmwareWorkProcessor}BBII^{ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[7{ISPNotification=*Bi}][7{ISPNotification=*Bi}]{ISPNotification=*Bi}{ISPNotification=*Bi}{ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16I24^{ISPServicesRemote=@@^?^v*}28"
- "B24@0:8^{ISPDevice={ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{ISPDeviceCachedConfigChannel}^{ISPModuleParams}}^?^v^{ISPDeviceController}I^{__CFDictionary}I^{ISPMotionManager}^{ISPDeviceImpactManager}^{ISPServicesRemote}^{ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{ISPFirmwareWorkProcessor}BBII^{ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[7{ISPNotification=*Bi}][7{ISPNotification=*Bi}]{ISPNotification=*Bi}{ISPNotification=*Bi}{ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}16"
- "Couldn't create reference file %s to write\n"
- "Failed to save plist"
- "Unexpected references size (Expected %ld, Got %d)\n"
- "Unexpected references size after compression (Expected %ld, Got %ld)\n"
- "^{ISPDevice={ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{ISPDeviceCachedConfigChannel}^{ISPModuleParams}}^?^v^{ISPDeviceController}I^{__CFDictionary}I^{ISPMotionManager}^{ISPDeviceImpactManager}^{ISPServicesRemote}^{ISPExclaveDebugService}^{SystemStatus}I[4096c]{?=[8I]}^{ISPFirmwareWorkProcessor}BBII^{ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[7{ISPNotification=*Bi}][7{ISPNotification=*Bi}]{ISPNotification=*Bi}{ISPNotification=*Bi}{ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}"

```
