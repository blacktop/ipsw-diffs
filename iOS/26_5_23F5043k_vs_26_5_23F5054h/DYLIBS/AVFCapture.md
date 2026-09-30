## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-665.120.3.0.0
-  __TEXT.__text: 0x171d7c
+665.120.6.0.0
+  __TEXT.__text: 0x17228c
   __TEXT.__auth_stubs: 0x2030
-  __TEXT.__objc_methlist: 0xf0ec
+  __TEXT.__objc_methlist: 0xf114
   __TEXT.__const: 0xba2
-  __TEXT.__gcc_except_tab: 0x2c98
-  __TEXT.__cstring: 0x2ba49
-  __TEXT.__oslogstring: 0x22b0b
+  __TEXT.__gcc_except_tab: 0x2c6c
+  __TEXT.__cstring: 0x2bba9
+  __TEXT.__oslogstring: 0x22b89
   __TEXT.__dlopen_cstrs: 0x274
   __TEXT.__ustring: 0x54
   __TEXT.__swift5_typeref: 0xf7

   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x4f70
-  __TEXT.__objc_classname: 0x19d1
-  __TEXT.__objc_methname: 0x2abfd
+  __TEXT.__objc_classname: 0x1a21
+  __TEXT.__objc_methname: 0x2ac87
   __TEXT.__objc_methtype: 0x4081
-  __TEXT.__objc_stubs: 0x18f40
-  __DATA_CONST.__got: 0x2aa0
-  __DATA_CONST.__const: 0x81c8
+  __TEXT.__objc_stubs: 0x18f60
+  __DATA_CONST.__got: 0x2ac8
+  __DATA_CONST.__const: 0x8208
   __DATA_CONST.__objc_classlist: 0x5e0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7c10
+  __DATA_CONST.__objc_selrefs: 0x7c20
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x510
   __DATA_CONST.__objc_arraydata: 0x498
   __AUTH_CONST.__auth_got: 0x1028
   __AUTH_CONST.__const: 0xd10
-  __AUTH_CONST.__cfstring: 0x150a0
-  __AUTH_CONST.__objc_const: 0x189c8
+  __AUTH_CONST.__cfstring: 0x151a0
+  __AUTH_CONST.__objc_const: 0x18a28
   __AUTH_CONST.__objc_intobj: 0xa50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0xb10
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x1a64
+  __DATA.__objc_ivar: 0x1a70
   __DATA.__data: 0xd78
   __DATA.__common: 0x300
   __DATA.__bss: 0x980

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9A7A9C21-8627-3CAC-93FA-C0F93A0160A0
-  Functions: 6643
-  Symbols:   23228
-  CStrings:  14638
+  UUID: 99B458C5-EDA9-3EC5-8F7B-FBD3A57BE670
+  Functions: 6646
+  Symbols:   23249
+  CStrings:  14661
 
Symbols:
+ -[AVCaptureSession _handleDidBeginGraphBuildNotificationWithPayload:]
+ -[AVCaptureSession _notifySessionStoppedWithNotificationPayload:]
+ -[AVCaptureSession(AVCaptureSessionCameraLaunchTelemetry) enableLaunchTelemetry]
+ -[AVCaptureVideoPreviewLayer(AVCaptureVideoPreviewLayerCameraLaunchTelemetry) enableLaunchTelemetry]
+ GCC_except_table181
+ GCC_except_table185
+ GCC_except_table187
+ GCC_except_table191
+ GCC_except_table199
+ GCC_except_table204
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table213
+ GCC_except_table221
+ GCC_except_table223
+ GCC_except_table225
+ _AVCaptureClientBackgroundedKey
+ _AVCaptureHostTimeUsKey
+ _AVCaptureMemoryStatusLevelKey
+ _AVCaptureSessionDidBeginGraphBuildNotification
+ _AVCaptureThermalLevelKey
+ _AVCaptureVideoPreviewLayerDidDisplayFirstPreviewFrameNotification
+ _AVCaptureVideoPreviewLayerDisplayedHostTimeUsKey
+ _AVCaptureVideoPreviewLayerPreviewingHostTimeUsKey
+ _OBJC_IVAR_$_AVCaptureInputPortInternal.internalLock
+ _OBJC_IVAR_$_AVCaptureSessionInternal.clientLaunchTelemetryEnabled
+ _OBJC_IVAR_$_AVCaptureVideoPreviewLayerInternal.clientLaunchTelemetryEnabled
+ __OBJC_$_INSTANCE_METHODS_AVCaptureSession(AVContinuityCapturePrivateState|AVCaptureSessionCameraLaunchTelemetry)
+ __OBJC_$_INSTANCE_METHODS_AVCaptureVideoPreviewLayer(AVCaptureVideoPreviewLayerCameraLaunchTelemetry)
+ ___block_literal_global.1149
+ ___block_literal_global.1151
+ ___block_literal_global.1156
+ ___block_literal_global.299
+ ___block_literal_global.392
+ _kFigCaptureSessionNotificationPayloadKey_ClientBackgrounded
+ _kFigCaptureSessionNotificationPayloadKey_HostTimeUs
+ _kFigCaptureSessionNotificationPayloadKey_MemoryStatusLevel
+ _kFigCaptureSessionNotificationPayloadKey_ThermalLevel
+ _kFigCaptureSessionNotification_DidBeginGraphBuild
+ _objc_msgSend$_handleDidBeginGraphBuildNotificationWithPayload:
+ _objc_msgSend$_notifySessionStoppedWithNotificationPayload:
- -[AVCaptureSession _notifySessionStopped]
- GCC_except_table14
- GCC_except_table15
- GCC_except_table180
- GCC_except_table186
- GCC_except_table193
- GCC_except_table203
- GCC_except_table205
- GCC_except_table207
- GCC_except_table209
- GCC_except_table212
- GCC_except_table218
- GCC_except_table222
- GCC_except_table224
- __OBJC_$_INSTANCE_METHODS_AVCaptureSession(AVContinuityCapturePrivateState)
- __OBJC_$_INSTANCE_METHODS_AVCaptureVideoPreviewLayer
- ___block_literal_global.1130
- ___block_literal_global.1132
- ___block_literal_global.1137
- ___block_literal_global.283
- ___block_literal_global.376
- _objc_msgSend$_notifySessionStopped
CStrings:
+ "-[AVCaptureSession _notifySessionStoppedWithNotificationPayload:]"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %{public}@: posted AVCaptureVideoPreviewLayerDidDisplayFirstPreviewFrameNotification"
+ "AVCaptureClientBackgroundedKey"
+ "AVCaptureHostTimeUsKey"
+ "AVCaptureMemoryStatusLevelKey"
+ "AVCaptureSessionCameraLaunchTelemetry"
+ "AVCaptureSessionDidBeginGraphBuildNotification"
+ "AVCaptureThermalLevelKey"
+ "AVCaptureVideoPreviewLayerCameraLaunchTelemetry"
+ "AVCaptureVideoPreviewLayerDidDisplayFirstPreviewFrameNotification"
+ "AVCaptureVideoPreviewLayerDisplayedHostTimeUsKey"
+ "AVCaptureVideoPreviewLayerPreviewingHostTimeUsKey"
+ "LastShownBuild:AVCaptureVideoPreviewLayer.m:2037"
+ "LastShownDate:AVCaptureVideoPreviewLayer.m:2037"
+ "_handleDidBeginGraphBuildNotificationWithPayload:"
+ "_notifySessionStoppedWithNotificationPayload:"
+ "clientLaunchTelemetryEnabled"
+ "description=CameraCapture_AVF-665.120.6"
+ "enableLaunchTelemetry"
+ "internalLock"
- "-[AVCaptureSession _notifySessionStopped]"
- "LastShownBuild:AVCaptureVideoPreviewLayer.m:2030"
- "LastShownDate:AVCaptureVideoPreviewLayer.m:2030"
- "_notifySessionStopped"
- "description=CameraCapture_AVF-665.120.3"

```
