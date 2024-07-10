## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/Versions/A/AVFCapture`

```diff

-558.2.22.1.0
-  __TEXT.__text: 0x1c50c0
+563.1.0.0.0
+  __TEXT.__text: 0x1c6114
   __TEXT.__auth_stubs: 0x22b0
-  __TEXT.__objc_methlist: 0x12658
-  __TEXT.__cstring: 0x300db
+  __TEXT.__objc_methlist: 0x126a8
+  __TEXT.__cstring: 0x302c1
   __TEXT.__const: 0x10f0
-  __TEXT.__oslogstring: 0x26cf9
-  __TEXT.__gcc_except_tab: 0x33cc
+  __TEXT.__oslogstring: 0x26ffb
+  __TEXT.__gcc_except_tab: 0x3438
   __TEXT.__dlopen_cstrs: 0x1d1
   __TEXT.__ustring: 0xbe
-  __TEXT.__unwind_info: 0x5668
+  __TEXT.__unwind_info: 0x56a8
   __TEXT.__objc_classname: 0x2486
-  __TEXT.__objc_methname: 0x29498
+  __TEXT.__objc_methname: 0x29532
   __TEXT.__objc_methtype: 0x4968
-  __TEXT.__objc_stubs: 0x17400
-  __DATA_CONST.__got: 0x24e8
-  __DATA_CONST.__const: 0x1240
+  __TEXT.__objc_stubs: 0x17480
+  __DATA_CONST.__got: 0x24f0
+  __DATA_CONST.__const: 0x1248
   __DATA_CONST.__objc_classlist: 0x808
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x73f0
+  __DATA_CONST.__objc_selrefs: 0x7408
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x668
   __DATA_CONST.__objc_arraydata: 0x280
   __AUTH_CONST.__auth_got: 0x1168
-  __AUTH_CONST.__const: 0x2650
-  __AUTH_CONST.__cfstring: 0x11c20
-  __AUTH_CONST.__objc_const: 0x1dfe0
+  __AUTH_CONST.__const: 0x26b0
+  __AUTH_CONST.__cfstring: 0x11c80
+  __AUTH_CONST.__objc_const: 0x1e040
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x1dc0
+  __DATA.__objc_ivar: 0x1dcc
   __DATA.__data: 0xd38
   __DATA.__common: 0x5c0
   __DATA.__bss: 0xba8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7362
-  Symbols:   17445
-  CStrings:  4195
+  Functions: 7371
+  Symbols:   17468
+  CStrings:  4206
 
Symbols:
+ +[AVCaptureProprietaryDefaultsSingleton objectsForWildcardKey:]
+ +[AVCaptureProprietaryDefaultsSingleton setObject:forWildcardKey:]
+ -[AVCaptureDeviceInput_Tundra _refreshDALDeviceSuppressVideoEffects]
+ -[AVCaptureDeviceInput_Tundra graphWillStopForSession:error:]
+ -[AVCaptureProprietaryDefaultsSingleton objectsForWildcardKey:]
+ -[AVCaptureProprietaryDefaultsSingleton setObject:forWildcardKey:]
+ -[AVCaptureSession liveSessionConnectedVideoCaptureDevices]
+ -[CMIOProprietaryDefaultsSource objectsForWildcardKey:]
+ -[CMIOProprietaryDefaultsSource setObject:forWildcardKey:]
+ GCC_except_table125
+ GCC_except_table126
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table147
+ GCC_except_table151
+ GCC_except_table250
+ GCC_except_table251
+ GCC_except_table380
+ GCC_except_table78
+ GCC_except_table82
+ GCC_except_table88
+ OBJC_IVAR_$_AVCaptureConnectionInternal.clientUsesVideoRotationAngleAPI
+ OBJC_IVAR_$_AVCaptureDeviceInputInternal_Tundra.observingSuppressVideoEffects
+ OBJC_IVAR_$_AVCaptureSessionInternal.clientIsVOIP
+ _AVCapturePrewarmReasonCameraLaunchLockScreenButton
+ _AVCapturePrewarmReasonCameraLaunchLockScreenSwipe
+ __102-[AVCaptureProprietaryDefaultsSingleton setObserveFrameSenderServerEndpoints:endpointsChangedHandler:]_block_invoke.165
+ __132-[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:handlersForKeyObservers:callHandlersAsync:]_block_invoke.154
+ __29+[AVCaptureSession dotString]_block_invoke.239
+ __29+[AVCaptureSession dotString]_block_invoke.359
+ __29+[AVCaptureSession dotString]_block_invoke.372
+ __66-[AVCaptureProprietaryDefaultsSingleton setObject:forWildcardKey:]_block_invoke.117
+ __74-[AVCaptureProprietaryDefaultsSingleton _updateProprietaryDefaultsSource:]_block_invoke.136
+ __74-[AVCaptureProprietaryDefaultsSingleton _updateProprietaryDefaultsSource:]_block_invoke.140
+ __74-[AVCaptureProprietaryDefaultsSingleton _updateProprietaryDefaultsSource:]_block_invoke_2.141
+ ___59-[AVCaptureSession liveSessionConnectedVideoCaptureDevices]_block_invoke
+ ___63-[AVCaptureProprietaryDefaultsSingleton objectsForWildcardKey:]_block_invoke
+ ___66-[AVCaptureProprietaryDefaultsSingleton setObject:forWildcardKey:]_block_invoke
+ ___block_descriptor_40_e8_32o_e32_B32?0"AVCaptureDevice"8Q16^B24l
+ ___block_descriptor_48_e8_32o40o_e37_v32?0"NSString"8"NSMapTable"16^B24l
+ __block_literal_global.158
+ __block_literal_global.242
+ __block_literal_global.251
+ __block_literal_global.270
+ __block_literal_global.335
+ __block_literal_global.341
+ __block_literal_global.343
+ __block_literal_global.356
+ __block_literal_global.364
+ __block_literal_global.366
+ __block_literal_global.368
+ __block_literal_global.856
+ _kFigCaptureSessionIrisStillImageSinkNotification_DidFinishRecordingMomentCaptureMovie
+ _objc_msgSend$_refreshDALDeviceSuppressVideoEffects
+ _objc_msgSend$objectsForWildcardKey:
+ _objc_msgSend$setObject:forWildcardKey:
+ _objc_msgSend$suppressVideoEffects
- +[AVCaptureDevice observeSuppressVideoEffectsForDeviceID:handler:]
- +[AVCaptureDevice_Tundra observeSuppressVideoEffectsForDeviceID:handler:]
- GCC_except_table123
- GCC_except_table131
- GCC_except_table132
- GCC_except_table137
- GCC_except_table138
- GCC_except_table149
- GCC_except_table252
- GCC_except_table253
- GCC_except_table29
- GCC_except_table382
- GCC_except_table54
- GCC_except_table73
- GCC_except_table77
- GCC_except_table92
- _AVAppleMakerNote_GenAIImageType
- _AVCaptureSuppressVideoEffectsPreferenceKey
- _AVCaptureWarnBackgroundReplacementIsUnreleasedFeatureAndConfirmOptIn
- __102-[AVCaptureProprietaryDefaultsSingleton setObserveFrameSenderServerEndpoints:endpointsChangedHandler:]_block_invoke.155
- __132-[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:handlersForKeyObservers:callHandlersAsync:]_block_invoke.144
- __29+[AVCaptureSession dotString]_block_invoke.232
- __29+[AVCaptureSession dotString]_block_invoke.352
- __29+[AVCaptureSession dotString]_block_invoke.365
- __74-[AVCaptureProprietaryDefaultsSingleton _updateProprietaryDefaultsSource:]_block_invoke.128
- __74-[AVCaptureProprietaryDefaultsSingleton _updateProprietaryDefaultsSource:]_block_invoke.132
- __74-[AVCaptureProprietaryDefaultsSingleton _updateProprietaryDefaultsSource:]_block_invoke_2.133
- ___73+[AVCaptureDevice_Tundra observeSuppressVideoEffectsForDeviceID:handler:]_block_invoke
- __block_literal_global.148
- __block_literal_global.235
- __block_literal_global.254
- __block_literal_global.276
- __block_literal_global.328
- __block_literal_global.344
- __block_literal_global.346
- __block_literal_global.362
- __block_literal_global.367
- __block_literal_global.369
- __block_literal_global.371
- __block_literal_global.842
CStrings:
+ "-[AVCaptureDeviceInput_Tundra _refreshDALDeviceSuppressVideoEffects]"
+ "-[AVCaptureProprietaryDefaultsSingleton setObject:forWildcardKey:]_block_invoke"
+ "-[CMIOProprietaryDefaultsSource objectsForWildcardKey:]"
+ "-[CMIOProprietaryDefaultsSource setObject:forWildcardKey:]"
+ "LockScreenButton"
+ "LockScreenSwipe"
+ "MaximumRealTimeFrameRate"
+ "description=CameraCapture_AVF-563.1"
+ "get-wildcard-preference-value"
+ "kAVCaptureDeviceInputSuppressVideoEffectsChangedContext"
+ "maxFrameRate <= formatMaxFrameRate"
+ "set-wildcard-preference-value"
+ "suppressVideoEffects"
+ "v32@?0@\"NSString\"8@\"NSMapTable\"16^B24"
- "%!@(MISSING)suppress-video-effects-for-deviceid"
- "86"
- "description=CameraCapture_AVF-558.2.22.1"

```
