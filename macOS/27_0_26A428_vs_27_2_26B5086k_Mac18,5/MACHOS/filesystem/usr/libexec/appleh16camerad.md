## appleh16camerad

> `/usr/libexec/appleh16camerad`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-6.20.0.0.0
-  __TEXT.__text: 0x86784
+6.103.0.0.0
+  __TEXT.__text: 0x87fa8
   __TEXT.__auth_stubs: 0x1740
-  __TEXT.__objc_stubs: 0x9c0
+  __TEXT.__objc_stubs: 0xac0
   __TEXT.__init_offsets: 0x1c
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x6463
-  __TEXT.__const: 0x19b80
-  __TEXT.__gcc_except_tab: 0xfd0
-  __TEXT.__oslogstring: 0x4467
-  __TEXT.__objc_methname: 0x9f4
+  __TEXT.__cstring: 0x65da
+  __TEXT.__const: 0x19b70
+  __TEXT.__gcc_except_tab: 0x108c
+  __TEXT.__oslogstring: 0x4713
+  __TEXT.__objc_methname: 0xad2
   __TEXT.__objc_classname: 0xa9
-  __TEXT.__objc_methtype: 0x62a
-  __TEXT.__unwind_info: 0x1788
-  __DATA_CONST.__const: 0xa3c0
-  __DATA_CONST.__cfstring: 0x2360
+  __TEXT.__objc_methtype: 0x63d
+  __TEXT.__unwind_info: 0x17c0
+  __DATA_CONST.__const: 0xa3d0
+  __DATA_CONST.__cfstring: 0x23c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0xbb0
-  __DATA_CONST.__got: 0x1260
+  __DATA_CONST.__got: 0x1280
   __DATA_CONST.__auth_ptr: 0x38
   __DATA.__objc_const: 0x5c8
-  __DATA.__objc_selrefs: 0x3a0
+  __DATA.__objc_selrefs: 0x3e0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x3812a8
+  __DATA.__data: 0x3812b0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1348
-  Symbols:   981
-  CStrings:  1491
+  Functions: 1364
+  Symbols:   985
+  CStrings:  1526
 
Symbols:
+ _OBJC_CLASS_$_STActivityAttribution
+ _OBJC_CLASS_$_STMediaStatusDomainCameraCaptureAttribution
+ _OBJC_CLASS_$_STMediaStatusDomainCameraDescriptor
+ __DefaultRuneLocale
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _dlopen
- _dlsym
CStrings:
+ "%08X-%04X-%04X-%04X-%012X"
+ "%s - CIL off request\n"
+ "%s - CIL on request\n"
+ "%s - Calling ISP_CILRequestPerChannel error: 0x%08X (%u/false)\n"
+ "%s - Calling ISP_CILRequestPerChannel(Line:%d) error: 0x%08X (%u/%u)\n"
+ "%s - CopyBuiltInCameraDeviceUID returned NULL on macOS — falling back to \"0\"; privacy indicator may not engage.\n"
+ "%s - CopyBuiltInCameraDeviceUID: unexpected kMGQProductType=%{public}@\n"
+ "%s - [%d] [CIL] Call ISP_CILRequestPerChannel (%u/%u)\n"
+ "%s - [%d] [CIL] Call ISP_CILRequestPerChannel (%u/false)\n"
+ "%s - process name is mediaserverd or cameracaptured, so skip calling SystemsStatus\n"
+ "%s - systemStatus is NULL\n"
+ ","
+ "6.103"
+ "73E5DA24-0C5C-4582-A32D-51C316922115"
+ "7F8975D2-5993-4D0A-A835-1BCD65497A2E"
+ "82F52358-2D92-45AA-9482-39D9FE44052F"
+ "@32@0:8^{H16ISPExtensionDevice=}16r^{H16ISPStreamInfoStruct=B*}24"
+ "@36@0:8^{H16ISPExtensionProvider=}16^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^{H16ISPDeviceController}I^{__CFDictionary}^{H16ISPServicesRemote}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}I^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{os_unfair_lock_s=I}^?^v{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}24I32"
+ "A06D2852-7127-44C8-ACC0-330C5D61AC5C"
+ "CEFDBF0A-CE56-4F92-B429-465EE8311EB5"
+ "CopyBuiltInCameraDeviceUID"
+ "D9824D83-563F-49B5-8D3F-92E51E5A2C71"
+ "FDB7767D-C40C-4AE5-9A6C-3A26FDE822CB"
+ "FE92254C-7034-4F4C-91D2-DDCA5BD09EE3"
+ "ISP_CILRequestPerChannel"
+ "NotifySystemStatusForCIL"
+ "ProductType"
+ "Unexpected client Get data length=%zu expected=%zu (pid %{private}d)\n"
+ "Unexpected client Set data length=%zu expected=%zu (pid %{private}d)\n"
+ "[%s:%d] [CIL] ISP_CILRequestPerChannel calls kernel (%u/%u)\n\n"
+ "addCameraAttribution:"
+ "attributionWithAuditToken:"
+ "cameracaptured"
+ "characterAtIndex:"
+ "componentsSeparatedByString:"
+ "initWithCameraDescriptor:activityAttribution:"
+ "initWithCameraIdentifier:"
+ "mediaserverd"
+ "removeCameraAttribution:"
+ "services"
+ "updateVolatileDataWithBlock:"
+ "v16@?0@\"STMutableMediaStatusDomainData\"8"
- "%s - CopyCMIODeviceUID returned NULL on macOS — falling back to \"0\". Privacy indicator may not engage.\n"
- "/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO"
- "6.20"
- "@32@0:8^{H16ISPExtensionDevice=}16r^{H16ISPStreamInfoStruct=iB*}24"
- "@36@0:8^{H16ISPExtensionProvider=}16^{H16ISPDevice={H16ISPDeviceCachedConfigs=IB{sCIspCmdConfigGet=ISSIIIII}^{H16ISPDeviceCachedConfigChannel}^{H16ISPModuleParams}}^?^v^{H16ISPDeviceController}I^{__CFDictionary}^{H16ISPServicesRemote}^{SystemStatus}I[4096c]{?=[8I]}^{H16ISPFirmwareWorkProcessor}I^{H16ISPPlatformInfoStruct}i^v^{__CFRunLoopSource}III{_opaque_pthread_mutex_t=q[56c]}B[6{H16ISPNotification=*Bi}][6{H16ISPNotification=*Bi}]{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}{H16ISPNotification=*Bi}II{DCSAudioAccelClientConfigStruct=Q@?^?@?^?}^{DCSAudioAccelManager}}24I32"
- "CMIOObjectGetPropertyData"
- "CMIOObjectGetPropertyDataSize"
```
