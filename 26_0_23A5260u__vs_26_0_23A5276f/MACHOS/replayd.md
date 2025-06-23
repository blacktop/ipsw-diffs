## replayd

> `/usr/libexec/replayd`

```diff

-650.38.1.0.0
-  __TEXT.__text: 0x602fc
+650.42.1.0.0
+  __TEXT.__text: 0x60f7c
   __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_stubs: 0x85a0
-  __TEXT.__objc_methlist: 0x43bc
-  __TEXT.__const: 0x1bc
-  __TEXT.__objc_methname: 0xc7c6
-  __TEXT.__cstring: 0xc7bd
-  __TEXT.__oslogstring: 0x9186
+  __TEXT.__objc_stubs: 0x8680
+  __TEXT.__objc_methlist: 0x43fc
+  __TEXT.__const: 0x1b4
+  __TEXT.__objc_methname: 0xc958
+  __TEXT.__cstring: 0xc776
+  __TEXT.__oslogstring: 0x93f9
   __TEXT.__objc_classname: 0x69b
-  __TEXT.__objc_methtype: 0x227d
-  __TEXT.__gcc_except_tab: 0x7c8
-  __TEXT.__unwind_info: 0x12b0
+  __TEXT.__objc_methtype: 0x22b1
+  __TEXT.__gcc_except_tab: 0x7b4
+  __TEXT.__unwind_info: 0x12b8
   __DATA_CONST.__auth_got: 0x850
-  __DATA_CONST.__got: 0x710
+  __DATA_CONST.__got: 0x718
   __DATA_CONST.__const: 0x1900
-  __DATA_CONST.__cfstring: 0x3b00
+  __DATA_CONST.__cfstring: 0x3a00
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xe0

   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_doubleobj: 0x30
-  __DATA.__objc_const: 0x95d0
-  __DATA.__objc_selrefs: 0x2a30
-  __DATA.__objc_ivar: 0x5ac
+  __DATA.__objc_const: 0x9610
+  __DATA.__objc_selrefs: 0x2a68
+  __DATA.__objc_ivar: 0x5b4
   __DATA.__objc_data: 0xe60
   __DATA.__data: 0xa98
   __DATA.__bss: 0x1d0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C548601-C685-35F9-9654-7983F6A4C7B2
-  Functions: 1956
-  Symbols:   503
-  CStrings:  4489
+  UUID: 9E997E13-046C-38C6-9C2C-8ADF9FD1C0D5
+  Functions: 1966
+  Symbols:   504
+  CStrings:  4498
 
Symbols:
+ _OBJC_CLASS_$_AVAudioChannelLayout
CStrings:
+ " [DEBUG] %{public}s:%d %s calling clientApplicationDidEnterBackground"
+ " [DEBUG] %{public}s:%d %s calling clientApplicationDidEnterForeground"
+ " [DEBUG] %{public}s:%d %s processIdentifer %@ observer nonnil %i"
+ " [DEBUG] %{public}s:%d %s processIdentifier %i BKSApplicationStateKey %@ previousState %@"
+ " [DEBUG] %{public}s:%d %s processIdentifier %i userInfo %@ previousState %@"
+ " [DEBUG] %{public}s:%d %s state %i previousState %@"
+ " [DEBUG] %{public}s:%d %s state %i previousState %i"
+ " [DEBUG] %{public}s:%d %s userInfo %@ previousState %@"
+ " [INFO] %{public}s:%d HQLR camera capture manager did start"
+ " [INFO] %{public}s:%d usingCamera=%@"
+ "-[RPCameraCaptureManager startWithAppUsingCamera:startHandler:outputHandler:]_block_invoke"
+ "-[RPCaptureManager startCameraCaptureWithDispatchGroup:usingCamera:]_block_invoke"
+ "-[RPHighQualityLocalRecordingSession handleMemoryWarning]"
+ "-[RPHighQualityLocalRecordingSession handleMemoryWarning]_block_invoke"
+ "-[RPMicAudioCaptureManager startMicrophoneCaptureWithOutput:didStartHandler:useRemoteIOFormat:]"
+ "-[RPMicAudioCaptureManager startMicrophoneCaptureWithOutput:didStartHandler:useRemoteIOFormat:]_block_invoke"
+ "_isAppUsingCameraWhenStarting"
+ "_startHandler"
+ "hasSufficientFreeSpaceForRecording"
+ "hasSufficientSpaceForCurrentRecording"
+ "initWithCommonFormat:sampleRate:interleaved:channelLayout:"
+ "layoutWithLayoutTag:"
+ "setRemoteIOOutputFormat:"
+ "startCameraCaptureWithDispatchGroup:usingCamera:"
+ "startHQLRMicrophoneCaptureWithOutput:didStartHandler:"
+ "startMicrophoneCaptureWithOutput:didStartHandler:useRemoteIOFormat:"
+ "startWithAppUsingCamera:startHandler:outputHandler:"
+ "v28@0:8@16B24"
+ "v36@0:8@?16@?24B32"
+ "v36@0:8B16@?20@?28"
- "%s calling clientApplicationDidEnterBackground"
- "%s calling clientApplicationDidEnterForeground"
- "%s processIdentifer %@ observer nonnil %i"
- "%s processIdentifier %i BKSApplicationStateKey %@ previousState %@"
- "%s processIdentifier %i userInfo %@ previousState %@"
- "%s state %i previousState %@"
- "%s state %i previousState %i"
- "%s userInfo %@ previousState %@"
- "-[RPCameraCaptureManager startWithOutputHandler:]_block_invoke"
- "-[RPMicAudioCaptureManager startMicrophoneCaptureWithOutput:didStartHandler:]"
- "-[RPMicAudioCaptureManager startMicrophoneCaptureWithOutput:didStartHandler:]_block_invoke"
- "startCameraCapture"
- "startWithOutputHandler:"

```
