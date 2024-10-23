## libBKDM2.dylib

> `/usr/lib/libBKDM2.dylib`

```diff

-733.40.2.0.0
-  __TEXT.__text: 0x708dc
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_methlist: 0x5c1c
-  __TEXT.__cstring: 0x52ca
-  __TEXT.__const: 0x6954
-  __TEXT.__gcc_except_tab: 0x7c0
-  __TEXT.__oslogstring: 0x3419
+737.60.22.0.0
+  __TEXT.__text: 0x752dc
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_methlist: 0x5cd4
+  __TEXT.__cstring: 0x5657
+  __TEXT.__const: 0x697c
+  __TEXT.__gcc_except_tab: 0x908
+  __TEXT.__oslogstring: 0x38b1
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__ustring: 0x11c
-  __TEXT.__unwind_info: 0x8d0
+  __TEXT.__unwind_info: 0x940
   __TEXT.__eh_frame: 0xf0
-  __TEXT.__objc_classname: 0x308
-  __TEXT.__objc_methname: 0x11a39
-  __TEXT.__objc_methtype: 0x29b7
-  __TEXT.__objc_stubs: 0x64e0
-  __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0x1000
+  __TEXT.__objc_classname: 0x332
+  __TEXT.__objc_methname: 0x12079
+  __TEXT.__objc_methtype: 0x2adc
+  __TEXT.__objc_stubs: 0x6ba0
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__const: 0x1098
   __DATA_CONST.__objc_classlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3440
+  __DATA_CONST.__objc_selrefs: 0x35f0
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x358
-  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__auth_got: 0x6c8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x6a8
-  __AUTH_CONST.__cfstring: 0x50a0
-  __AUTH_CONST.__objc_const: 0x8cd8
+  __AUTH_CONST.__const: 0x728
+  __AUTH_CONST.__cfstring: 0x5420
+  __AUTH_CONST.__objc_const: 0x9030
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__objc_intobj: 0x2a0
+  __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x8e4
-  __DATA.__data: 0x830
+  __DATA.__objc_ivar: 0x944
+  __DATA.__data: 0x890
   __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__common: 0x30
   __DATA_DIRTY.__bss: 0x50
+  - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 2223
-  Symbols:   3237
-  CStrings:  3940
+  Functions: 2246
+  Symbols:   3277
+  CStrings:  4107
 
Symbols:
+ _AVCaptureDeviceTypeBuiltInInfraredMetadataCamera
+ _AVCaptureSessionDidStartRunningNotification
+ _AVCaptureSessionDidStopRunningNotification
+ _AVCaptureSessionInterruptionEndedNotification
+ _AVCaptureSessionRuntimeErrorNotification
+ _AVCaptureSessionWasInterruptedNotification
+ _AVMediaTypeMetadataObject
+ _AVMetadataObjectTypeEyeReliefStatus
+ _AVMetadataObjectTypeFace
+ _MGGetSInt32Answer
+ _OBJC_CLASS_$_AVCaptureDevice
+ _OBJC_CLASS_$_AVCaptureDeviceInput
+ _OBJC_CLASS_$_AVCaptureMetadataOutput
+ _OBJC_CLASS_$_AVCaptureSession
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSRecursiveLock
+ _kdebug_trace
CStrings:
+ "\x11A\x12\x16!\x91\x11Q\x17a"
+ "\x12\x18#\x12\""
+ "!_avcSessionInitialized"
+ "@\"AVCaptureDevice\""
+ "@\"AVCaptureDeviceInput\""
+ "@\"AVCaptureMetadataOutput\""
+ "@\"AVCaptureSession\""
+ "@\"NSRecursiveLock\""
+ "AVC delegate: captureOutput:%!@(MISSING) didOutputMetadataObjects:%!@(MISSING) fromConnection:%!@(MISSING)\n"
+ "AVCaptureMetadataOutputObjectsDelegate"
+ "AVF notification: AVCaptureSessionDidStartRunningNotification\n"
+ "AVF notification: AVCaptureSessionDidStopRunningNotification\n"
+ "AVF notification: AVCaptureSessionInterruptionEndedNotification\n"
+ "AVF notification: AVCaptureSessionRuntimeErrorNotification\n"
+ "AVF notification: AVCaptureSessionWasInterruptedNotification\n"
+ "BKOptionMatchOperationTrigger"
+ "BKStatusDetailMotionDetectMatrix"
+ "BKStatusDetailMotionDetectState"
+ "FrontCameraRotationForISP"
+ "Secure face detect succeeded\n"
+ "TC,N,V_trigger"
+ "Unexpected value of kMGQFrontCameraRotationForISP: %!f(MISSING)\n"
+ "[_avcSession canAddInput:_avcInput]"
+ "[_avcSession canAddOutput:_avcOutput]"
+ "[msgData length] >= sizeof(message_secure_fd_request_v1_t)"
+ "_avcDevice"
+ "_avcInput"
+ "_avcLock"
+ "_avcObservers"
+ "_avcOutput"
+ "_avcQueue"
+ "_avcSession"
+ "_avcSession.running"
+ "_avcSessionInitialized"
+ "_collectedMetadataObjects"
+ "_collectedMetadataObjectsTimestamp"
+ "_dispatchQueueWriting"
+ "_frontCameraRotationForISP"
+ "_lastProcessedNoMetadataObjects"
+ "_secureFaceDetectDict"
+ "_secureFaceDetectLastFeedback"
+ "_secureFaceDetectLastOcclusionState"
+ "_secureFaceDetectLastWUPE"
+ "_secureFaceDetectPreCheckDone"
+ "_secureFaceDetectRequest"
+ "_secureFaceDetectRequestFlags"
+ "_secureFaceDetectSessionID"
+ "_secureSequenceId"
+ "_synchronizeMetadataObjects"
+ "_trigger"
+ "addInput:"
+ "addObserverForName:object:queue:usingBlock:"
+ "addOutput:"
+ "beginConfiguration"
+ "bounds"
+ "canAddInput:"
+ "canAddOutput:"
+ "captureOutput:didOutputMetadataObjects:fromConnection:"
+ "clearSecureFaceDetectContext"
+ "com.apple.BioLog.writing"
+ "com.apple.pearld.avc"
+ "commitConfiguration"
+ "confidence"
+ "currentRequest:%!u(MISSING) currentFlags:0x%!x(MISSING) -> can reuse current AVC session\n"
+ "d"
+ "defaultCenter"
+ "defaultDeviceWithDeviceType:mediaType:position:"
+ "deinitSecureFaceDetect"
+ "deinitSecureFaceDetect\n"
+ "deinitSecureFaceDetect: -> void\n"
+ "eyeReliefStatus"
+ "eye_relief_status"
+ "face"
+ "faceDetectMessage:info:fromSecureFD:"
+ "final_state"
+ "frameDict"
+ "frameDict[@\"eye_relief_status\"] == ((void *)0)"
+ "frameDict[@\"face\"] == ((void *)0)"
+ "frame_array"
+ "hasConfidence"
+ "hasDistance"
+ "hasOrientation"
+ "hasPayingAttention"
+ "hasPayingAttentionConfidence"
+ "hasPitchAngle"
+ "hasRollAngle"
+ "hasYawAngle"
+ "height"
+ "i24@0:8i16I20"
+ "initSecureFaceDetect"
+ "initSecureFaceDetect\n"
+ "initSecureFaceDetect: -> %!d(MISSING)\n"
+ "initWithDevice:error:"
+ "isInterrupted"
+ "isRunning"
+ "logSecureFaceDetectInfo"
+ "logSecureFaceDetectInfo [%!u(MISSING):*]\n"
+ "logSecureFaceDetectInfo: %!l(MISSING)u > %!@(MISSING)\n"
+ "logSecureFaceDetectStart <- [%!u(MISSING):*]\n"
+ "logSecureFaceDetectStart:"
+ "logSecureFaceDetectState:"
+ "logSecureFaceDetectStop"
+ "logSecureFrameMeta:timestamp:"
+ "match_flags"
+ "match_trigger"
+ "message"
+ "message->sessionID != 0"
+ "metadataObjectTypes"
+ "metadataObjects"
+ "motionDetectMessage:info:state:"
+ "note.object == strongSelf->_avcSession"
+ "object"
+ "payingAttention"
+ "payingAttentionConfidence"
+ "paying_attention"
+ "paying_attention_confidence"
+ "pitch=%!d(MISSING), yaw=%!d(MISSING), roll=%!d(MISSING), distance=%!d(MISSING), faceRectW=%!d(MISSING), faceRectH=%!d(MISSING) --> wuPoseEligible: %!u(MISSING)\n"
+ "pitchAngle"
+ "pitch_angle"
+ "processMetadataObjects:"
+ "processMetadataObjects:%!@(MISSING)\n"
+ "removeAllObjects"
+ "removeObserver:"
+ "request"
+ "rollAngle"
+ "roll_angle"
+ "sec-%!d(MISSING)-%!l(MISSING)d%!@(MISSING)%!@(MISSING)"
+ "secureFaceDetectRequestMessage:"
+ "secureFaceDetectRequestMessage: request=%!u(MISSING), flags:0x%!x(MISSING), sessionID=%!u(MISSING)\n"
+ "secureFaceDetectSequence"
+ "secure_face_detect_mode"
+ "sessionID"
+ "setMetadataObjectTypes:"
+ "setMetadataObjectsDelegate:queue:"
+ "setSecureFaceDetectState:sessionID:"
+ "setTrigger:"
+ "startRunning"
+ "startSecureFaceDetect"
+ "startSecureFaceDetect\n"
+ "startSecureFaceDetect: -> %!d(MISSING)\n"
+ "startSecureFaceDetect: startRunning (dt = %!f(MISSING) ms), running:%!u(MISSING), interrupted:%!u(MISSING)\n"
+ "stopRunning"
+ "stopSecureFaceDetect"
+ "stopSecureFaceDetect\n"
+ "stopSecureFaceDetect: -> void\n"
+ "stopSecureFaceDetect: stopRunning (dt = %!f(MISSING) ms)\n"
+ "stopped"
+ "time"
+ "timestamp_av"
+ "trigger"
+ "v16@?0@\"NSNotification\"8"
+ "v24@0:8^{?=III{?=QSC}}16"
+ "v32@0:8I16^{?=CSSSSIfffIffBf}20B28"
+ "v32@0:8I16^{?=[16f]}20i28"
+ "v39@0:8{?=III{?=QSC}}16"
+ "v40@0:8@\"AVCaptureOutput\"16@\"NSArray\"24@\"AVCaptureConnection\"32"
+ "v40@0:8@16@24@32"
+ "width"
+ "x"
+ "y"
+ "yawAngle"
+ "yaw_angle"
+ "{?=\"nanotime\"Q\"number\"S\"type\"C}"
- "\x11A\x12\x16!\x91\x11Q"
- "\x12\x18#\x12"
- "BKStatusDetailMotionDetectStatus"
- "faceDetectMessage:info:"
- "motionDetectInfo"
- "motionDetectMessage:info:"
- "v28@0:8I16^{?=CSSSSIfffIffBf}20"
- "v28@0:8I16^{?=[16f]}20"

```
