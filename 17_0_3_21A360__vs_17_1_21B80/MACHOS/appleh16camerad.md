## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-1.69.0.0.0
-  __TEXT.__text: 0x69c68
-  __TEXT.__auth_stubs: 0x1b70
+1.107.0.0.0
+  __TEXT.__text: 0x6a518
+  __TEXT.__auth_stubs: 0x1b80
   __TEXT.__objc_stubs: 0x1100
   __TEXT.__init_offsets: 0x10
   __TEXT.__objc_methlist: 0x11c
   __TEXT.__const: 0x2e70
-  __TEXT.__gcc_except_tab: 0x1d94
-  __TEXT.__cstring: 0x7a61
-  __TEXT.__oslogstring: 0x3e04
+  __TEXT.__gcc_except_tab: 0x1da0
+  __TEXT.__cstring: 0x7b77
+  __TEXT.__oslogstring: 0x3f3d
   __TEXT.__objc_classname: 0x89
-  __TEXT.__objc_methname: 0x11e3
+  __TEXT.__objc_methname: 0x11e5
   __TEXT.__objc_methtype: 0xf00
-  __TEXT.__unwind_info: 0x1290
+  __TEXT.__unwind_info: 0x129c
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xdc8
-  __DATA_CONST.__got: 0x998
+  __DATA_CONST.__auth_got: 0xdd0
+  __DATA_CONST.__got: 0x9a0
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA_CONST.__const: 0xe160
+  __DATA_CONST.__const: 0xe180
   __DATA_CONST.__cfstring: 0x2ba0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x808
   __DATA.__objc_selrefs: 0x4c0
-  __DATA.__objc_classrefs: 0x150
+  __DATA.__objc_classrefs: 0x158
   __DATA.__objc_superrefs: 0x18
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xf0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1555
-  Symbols:   797
-  CStrings:  1655
+  Functions: 1564
+  Symbols:   800
+  CStrings:  1671
 
Symbols:
+ _OBJC_CLASS_$_ADFigCameraCalibrationSource
+ _kFigCaptureStreamMetadata_AdaptiveLensShadingStrength
+ _xpc_string_get_length
CStrings:
+ "%s: client already has a registered device ID"
+ "1.107"
+ "<null>"
+ "Active client pid %{private}d deviceID %{private}s"
+ "CameraPowerOnDurationInMS"
+ "Failed to send report to analyticsd: %08X\n"
+ "Failed to send the %s event into the diagnostics system.\n"
+ "H16ISPServicesRemoteDeviceID"
+ "H16ISPServicesRemoteRGBJMetadataKey"
+ "PrepareGridCalculation"
+ "PrepareGridCalculation failed."
+ "RGB-IR: %s: rdar://112006283 Aborting texture creation rows: %d, cols: %d, buffer: %p"
+ "RGB-IR: %s: rdar://112006283 Error creating textures => Abortig Rgb-Ir run"
+ "RGB-IR: %s: rdar://112006283 numOfGoodPts is %d < 256 => Abortig Rgb-Ir run"
+ "SpmiInterface0ErrCount"
+ "SpmiInterface1ErrCount"
+ "com.apple.applecamerad.SpmiFaultStatus"
+ "createTexture"
+ "preprocessInputColorFrame:colorPose:jasperPointClouds:jasperPoses:jasperCameraCalibration:colorCameraCalibration:colorMetadata:"
+ "registerDeviceIDForClient"
- "1.69"
- "Failed to report the ISP Pearl statistics to analyticsd: %08X\n"
- "Failed to report the ISP Power status to analyticsd: %08X\n"
- "preprocessInputColorFrame:colorPose:jasperPointClouds:jasperPoses:jasperCameraCalibration:colorCameraCalibration:timestamp:"

```
