## ISP.mediacapture

> `/System/Library/MediaCapture/ISP.mediacapture`

```diff

-20.57.4.0.0
-  __TEXT.__text: 0x1a6d68
+20.70.0.0.0
+  __TEXT.__text: 0x1a70c4
   __TEXT.__init_offsets: 0xc
-  __TEXT.__gcc_except_tab: 0x4a1c
-  __TEXT.__const: 0x27835
-  __TEXT.__oslogstring: 0x1b807
-  __TEXT.__cstring: 0x163b7
-  __TEXT.__unwind_info: 0x3138
+  __TEXT.__gcc_except_tab: 0x49f4
+  __TEXT.__const: 0x278c5
+  __TEXT.__oslogstring: 0x1b96c
+  __TEXT.__cstring: 0x16484
+  __TEXT.__unwind_info: 0x3130
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1ef0
+  __AUTH_CONST.__const: 0x1f10
   __AUTH_CONST.__cfstring: 0x7fa0
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1340
-  __DATA.__data: 0x3b1df8
-  __DATA.__bss: 0xaa8
+  __AUTH_CONST.__auth_got: 0x1350
+  __DATA.__data: 0x3c0e00
+  __DATA.__bss: 0xac0
   __DATA.__common: 0x54e8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5053
-  Symbols:   7139
-  CStrings:  5788
+  Functions: 5054
+  Symbols:   7147
+  CStrings:  5796
 
Symbols:
+ GCC_except_table665
+ _ZN3ISP12SystemStatus17CopyCMIODeviceUIDEv
+ _ZN3ISP9ISPDevice16ISP_EnableABDNetEjb
+ __ZN3ISP12SystemStatus17CopyCMIODeviceUIDEv
+ __ZN3ISP9ISPDevice16ISP_EnableABDNetEjb
+ __ZN3ISPL24IMX958_setfile_2226_01XXE
+ __ZN3ISPL24VD56G8_setfile_0227_01XXE
+ __ZZN3ISP12SystemStatus17CopyCMIODeviceUIDEvE9fnGetData
+ __ZZN3ISP12SystemStatus17CopyCMIODeviceUIDEvE9fnGetSize
+ __ZZN3ISP12SystemStatus17CopyCMIODeviceUIDEvE9onceToken
+ ____ZN3ISP12SystemStatus17CopyCMIODeviceUIDEv_block_invoke
+ _dlopen
+ _dlsym
+ _kFigCaptureDeviceMultiCamConfigurationKey_BuiltInMicrophoneIsRecording
- GCC_except_table664
- __ZN3ISP12_GLOBAL__N_124FindFaceIDMetadataBufferEPNS_21ISPFilterGraphMessageE
- __ZN3ISP15ISPFaceIDTracer15RecordExitFrameEPNS_9ISPDeviceEjPNS_21ISPFilterGraphMessageE
- __ZN3ISP15ISPFaceIDTracer17RecordSessionModeEjNS0_11SessionModeE
- __ZN3ISP15ISPFaceIDTracer17RecordStreamFrameEPNS_9ISPDeviceEjPNS_21ISPFilterGraphMessageE
- __ZN3ISP15ISPFaceIDTracer20RecordBracketRequestEjjjj
CStrings:
+ "%s - %s: Failed to enable ABDNet in FW\n"
+ "%s - CopyCMIODeviceUID returned NULL on macOS — falling back to \"0\". Privacy indicator may not engage.\n"
+ "%s - focalLength=%f exceeds 2000px! focalLengthPinhole=%f, isValid=%hhu, binFactorW=%hhu, binFactorH=%hhu, lensPSF=%f, pixelSize_um=%f, quadraBinFactor=%hhu, cropX=%u, cropY=%u, cropWidth=%u, cropHeight=%u\n"
+ "/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO"
+ "/usr/local/share/firmware/isp/0227_01XX.dat"
+ "/usr/local/share/firmware/isp/2226_01XX.dat"
+ "CMIOObjectGetPropertyData"
+ "CMIOObjectGetPropertyDataSize"
+ "SetABDNetConfiguration - CISP_CMD_CH_UDC_MULTI_PASS_ENABLE(%d) error: 0x%08X\n\n"
- "SetABDNetConfiguration - CISP_CMD_CH_UDC_MULTI_PASS_ENABLE error: 0x%08X\n\n"
```
