## cameraispd

> `/usr/libexec/cameraispd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-20.70.0.0.0
-  __TEXT.__text: 0x8b758
+20.107.1.0.0
+  __TEXT.__text: 0x8c0e4
   __TEXT.__auth_stubs: 0x18f0
-  __TEXT.__objc_stubs: 0x980
+  __TEXT.__objc_stubs: 0x9c0
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x6586
-  __TEXT.__const: 0x1fe20
-  __TEXT.__gcc_except_tab: 0xed0
-  __TEXT.__oslogstring: 0x4922
-  __TEXT.__objc_methname: 0x9dd
+  __TEXT.__cstring: 0x670e
+  __TEXT.__const: 0x20160
+  __TEXT.__gcc_except_tab: 0xecc
+  __TEXT.__oslogstring: 0x4a2b
+  __TEXT.__objc_methname: 0xa0c
   __TEXT.__objc_classname: 0xa0
-  __TEXT.__objc_methtype: 0x5f9
-  __TEXT.__info_plist: 0x65a
-  __TEXT.__unwind_info: 0x1810
-  __DATA_CONST.__const: 0x8b38
-  __DATA_CONST.__cfstring: 0x28c0
+  __TEXT.__objc_methtype: 0x60d
+  __TEXT.__info_plist: 0x660
+  __TEXT.__unwind_info: 0x1830
+  __DATA_CONST.__const: 0x8b18
+  __DATA_CONST.__cfstring: 0x28a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0xc88
-  __DATA_CONST.__got: 0x1400
+  __DATA_CONST.__got: 0x1438
   __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_const: 0x5c8
-  __DATA.__objc_selrefs: 0x390
+  __DATA.__objc_selrefs: 0x3a0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x3be330
-  __DATA.__bss: 0x528
+  __DATA.__data: 0x5ad3c0
+  __DATA.__bss: 0x510
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1380
-  Symbols:   1060
-  CStrings:  1545
+  Functions: 1388
+  Symbols:   1067
+  CStrings:  1562
 
Symbols:
+ __DefaultRuneLocale
+ _kFigCaptureStreamMetadata_SmartTapAlgorithmMetadata
+ _kFigCaptureStreamSegmentFocusTrackingDataKey_FocusBias
+ _kFigCaptureStreamSegmentFocusTrackingDataKey_MaskConfidence
+ _kFigCaptureStreamSegmentFocusTrackingDataKey_ObjectID
+ _kFigCaptureStreamSegmentFocusTrackingDataKey_TotalPoints
+ _kFigCaptureStreamSegmentFocusTrackingDataKey_ValidCoverage
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _dlopen
- _dlsym
CStrings:
+ "%08X-%04X-%04X-%04X-%012X"
+ "%s - CopyBuiltInCameraDeviceUID returned NULL on macOS — falling back to \"0\"; privacy indicator may not engage.\n"
+ "%s - CopyBuiltInCameraDeviceUID: unexpected kMGQProductType=%{public}@\n"
+ "%s - Error reading kernel config cache - chan: %d, res: 0x%08X\n"
+ "%s - channel configs not valid - exiting\n"
+ "%s - kernel config count %d != firmware %d - chan: %d\n"
+ ","
+ "/usr/local/share/firmware/isp/2027_01XX.dat"
+ "/usr/local/share/firmware/isp/2327_01XX.dat"
+ "/usr/local/share/firmware/isp/2327_02XX.dat"
+ "/usr/local/share/firmware/isp/2727_01XX.dat"
+ "/usr/local/share/firmware/isp/3527_02XX.dat"
+ "/usr/local/share/firmware/isp/3527_03XX.dat"
+ "/usr/local/share/firmware/isp/4227_01XX.dat"
+ "/usr/local/share/firmware/isp/4427_01XX.dat"
+ "/usr/local/share/firmware/isp/7127_02XX.dat"
+ "/usr/local/share/firmware/isp/7327_01XX.dat"
+ "/usr/local/share/firmware/isp/7327_02XX.dat"
+ "20.107.1"
+ "@36@0:8^{ISPExtensionProvider=}16^{ISPDevice={ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{ISPDeviceCachedConfigChannel}^{ISPModuleParams}}^{ISPDeviceController}I^{__CFDictionary}^{ISPServicesRemote}^{SystemStatus}I[4096c]{?=[8I]}^{ISPFirmwareWorkProcessor}I^{ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[7{ISPNotification=*Bi}][7{ISPNotification=*Bi}]{ISPNotification=*Bi}{ISPNotification=*Bi}{ISPNotification=*Bi}II{os_unfair_lock_s=I}^?^v^{__CFDictionary}{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}24I32"
+ "CacheChannelConfigs"
+ "CopyBuiltInCameraDeviceUID"
+ "Could not find %s as %s (errno: %d)"
+ "Found %s at %s."
+ "ProductType"
+ "Unexpected client Get data length=%zu expected=%zu (pid %{private}d)\n"
+ "Unexpected client Set data length=%zu expected=%zu (pid %{private}d)\n"
+ "Will use ISP references"
+ "Will use SEP references"
+ "characterAtIndex:"
+ "componentsSeparatedByString:"
+ "sparse reference plist"
+ "sparseLP reference plist"
- "%s - CopyCMIODeviceUID returned NULL on macOS — falling back to \"0\". Privacy indicator may not engage.\n"
- "%s - Error getting LSC polynomial - chan: %d, res: 0x%08X\n"
- "%s - Error getting camera config - chan: %d, res: 0x%08X\n"
- "/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO"
- "20.70"
- "@36@0:8^{ISPExtensionProvider=}16^{ISPDevice={ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{ISPDeviceCachedConfigChannel}^{ISPModuleParams}}^?^v^{ISPDeviceController}I^{__CFDictionary}^{ISPServicesRemote}^{SystemStatus}I[4096c]{?=[8I]}^{ISPFirmwareWorkProcessor}I^{ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[7{ISPNotification=*Bi}][7{ISPNotification=*Bi}]{ISPNotification=*Bi}{ISPNotification=*Bi}{ISPNotification=*Bi}II^{__CFDictionary}{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}24I32"
- "CMIOObjectGetPropertyData"
- "CMIOObjectGetPropertyDataSize"
- "Could not find reference plist at %s (errno: %d). Will use ISP references"
- "FocusBias"
- "Found reference plist at %s. Will use SEP references"
- "MaskConfidence"
- "ObjectID"
- "SmartTapAlgorithmMetadata"
- "TotalPoints"
- "ValidCoverage"
```
