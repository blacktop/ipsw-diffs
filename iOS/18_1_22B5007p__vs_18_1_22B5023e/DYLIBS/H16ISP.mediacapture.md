## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-3.32.0.0.0
-  __TEXT.__text: 0x1a90e4
-  __TEXT.__auth_stubs: 0x32c0
+3.44.0.0.0
+  __TEXT.__text: 0x1a7708
+  __TEXT.__auth_stubs: 0x31e0
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__gcc_except_tab: 0x5e04
-  __TEXT.__const: 0x216bc
-  __TEXT.__cstring: 0x19367
-  __TEXT.__oslogstring: 0x1ab03
-  __TEXT.__unwind_info: 0x3bd0
+  __TEXT.__gcc_except_tab: 0x5ca0
+  __TEXT.__const: 0x215fc
+  __TEXT.__cstring: 0x1935a
+  __TEXT.__oslogstring: 0x1a8f6
+  __TEXT.__unwind_info: 0x3ae8
   __TEXT.__eh_frame: 0x110
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0x1ca1
   __TEXT.__objc_methtype: 0x11e8
   __TEXT.__objc_stubs: 0x1fa0
-  __DATA_CONST.__got: 0x31a8
-  __DATA_CONST.__const: 0x7670
+  __DATA_CONST.__got: 0x3110
+  __DATA_CONST.__const: 0x69b0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x818
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1970
-  __AUTH_CONST.__auth_ptr: 0xa0
-  __AUTH_CONST.__const: 0x20f0
-  __AUTH_CONST.__cfstring: 0x92e0
+  __AUTH_CONST.__auth_got: 0x1900
+  __AUTH_CONST.__auth_ptr: 0x98
+  __AUTH_CONST.__const: 0x2040
+  __AUTH_CONST.__cfstring: 0x93c0
   __AUTH_CONST.__objc_const: 0xae0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x2083e0
-  __DATA.__bss: 0x101
+  __DATA.__data: 0x208370
+  __DATA.__bss: 0xe1
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x968
-  __DATA_DIRTY.__common: 0x52f8
+  __DATA_DIRTY.__data: 0x118
+  __DATA_DIRTY.__bss: 0x988
+  __DATA_DIRTY.__common: 0x5358
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5538
-  Symbols:   9115
-  CStrings:  6216
+  Functions: 5513
+  Symbols:   9047
+  CStrings:  6221
 
Symbols:
+ __ZN6H16ISP12H16ISPDevice14ISP_SavageAuthEjPKhyj
+ __ZN6H16ISP12H16ISPDevice20EnableVibeMitigationEjb
+ __ZN6H16ISP12H16ISPDevice21EnableHighStrengthTNREjb
+ __ZN6H16ISP29H16ISPFrameReceiverBufferPoolC1EPNS_12H16ISPDeviceENS_33H16ISPFrameReceiverBufferPoolTypeEjjjjj17H16ISPFrameFormatNS_33H16ISPFrameReceiverBufferPoolTagsEbjjjjjjjPK10__CFStringP19__CVPixelBufferPoolj
+ __ZN6H16ISP29H16ISPFrameReceiverBufferPoolC2EPNS_12H16ISPDeviceENS_33H16ISPFrameReceiverBufferPoolTypeEjjjjj17H16ISPFrameFormatNS_33H16ISPFrameReceiverBufferPoolTagsEbjjjjjjjPK10__CFStringP19__CVPixelBufferPoolj
+ __os_log_unreliable_impl
+ _kFigCaptureStreamProperty_CameraControlsCacheExpiryDuration
+ _kFigCaptureStreamProperty_VibeMitigationEnabled
+ _kFigCaptureStreamTemporalNoiseReductionConfigurationKey_StrengthHighEnabled
+ _pthread_cond_timedwait_relative_np
- _CVAFaceTrackingLiteCopyDecodedOutput
- __ZN6H16ISP19H16ISPFrameReceiver13waitforBGsendEv
- __ZN6H16ISP29H16ISPFrameReceiverBufferPoolC1EPNS_12H16ISPDeviceENS_33H16ISPFrameReceiverBufferPoolTypeEjjjjj17H16ISPFrameFormatNS_33H16ISPFrameReceiverBufferPoolTagsEbjjjjjjjPK10__CFStringP19__CVPixelBufferPooljj
- __ZN6H16ISP29H16ISPFrameReceiverBufferPoolC2EPNS_12H16ISPDeviceENS_33H16ISPFrameReceiverBufferPoolTypeEjjjjj17H16ISPFrameFormatNS_33H16ISPFrameReceiverBufferPoolTagsEbjjjjjjjPK10__CFStringP19__CVPixelBufferPooljj
- __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNode29AddSecureTrackedFacesMetadataEPNS_24H16ISPFilterGraphMessageE60isprgbexclavekitmodule_ispexclavecorechrunkitfaceprocessrsltb
- __ZNSt11logic_errorC2ERKS_
- __ZNSt13exception_ptrC1ERKS_
- __ZNSt13exception_ptrD1Ev
- __ZNSt3__112future_errorC1ENS_10error_codeE
- __ZNSt3__112future_errorD1Ev
- __ZNSt3__114__shared_countD2Ev
- __ZNSt3__115future_categoryEv
- __ZNSt3__117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE
- __ZNSt3__117__assoc_sub_state13set_exceptionESt13exception_ptr
- __ZNSt3__117__assoc_sub_state9__executeEv
- __ZNSt3__118condition_variable10notify_allEv
- __ZNSt3__118condition_variable15__do_timed_waitERNS_11unique_lockINS_5mutexEEENS_6chrono10time_pointINS5_12system_clockENS5_8durationIxNS_5ratioILl1ELl1000000000EEEEEEE
- __ZNSt3__118condition_variableD1Ev
- __ZNSt3__16thread6detachEv
- __ZSt17current_exceptionv
- __ZSt17rethrow_exceptionSt13exception_ptr
- __ZTINSt3__112future_errorE
- __ZTINSt3__117__assoc_sub_stateE
- __ZTVNSt3__112future_errorE
- __ZTVNSt3__117__assoc_sub_stateE
- _kFigCaptureStreamFaceTrackingConfigurationKey_NetworkFailureThresholdMultiplier
- _kFigCaptureStreamFaceTrackingConfigurationKey_NumTrackedFaces
- _kFigCaptureStreamLMAConfigurationKey_EdgeDetectionEnabled
- _kFigCaptureStreamMetadataOutputConfigurationKey_LMAConfiguration
- _kFigCaptureStreamMetadataOutputConfigurationKey_LMAEnabled
- _kFigCaptureStreamMetadataOutputConfigurationKey_StreamingFaceTrackingConfiguration
- _kFigCaptureStreamMetadataOutputConfigurationKey_StreamingFaceTrackingEnabled
- _kFigCaptureStreamMetadataOutputKey_FaceFound
- _kFigCaptureStreamMetadataOutputKey_StreamingTrackedFaces
- _kFigCaptureStreamStreamingFaceKey_FaceIndex
- _kFigCaptureStreamStreamingFaceKey_Found
- _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_FaceOcclusionDetectionEnabled
- _kFigCaptureStreamVibeMitigationDeviceOrientationInfoKey_MaxGravityZ
- _kFigCaptureStreamVibeMitigationDeviceOrientationInfoKey_MinGravityZ
- _kFigCaptureStreamVibeMitigationInfoKey_CameraChannelIndex
- _kFigCaptureStreamVibeMitigationInfoKey_DeviceOrientationInfo
- _kFigCaptureStreamVibeMitigationInfoKey_RestingLensPosition
- _kFigCaptureStreamVibeMitigationInfoKey_VibeSafeLensPosition
CStrings:
+ " Unable to stop vibe mitigation\n"
+ "%!s(MISSING) - EnableHighStrengthTNR failed: 0x%!X(MISSING)\n"
+ "%!s(MISSING) - Sending %!d(MISSING) buffers to firmware (poolID=%!d(MISSING), poolSize=%!d(MISSING), poolType=%!d(MISSING)) result=0x%!X(MISSING)\n\n"
+ "%!s(MISSING): Data file load failed, status = 0x%!x(MISSING)\n"
+ "%!s(MISSING): Invalid connection\n"
+ "%!s(MISSING): Invalid data file arguments\n"
+ "%!s(MISSING): Savage Auth failed, status = 0x%!x(MISSING)\n"
+ "%!s(MISSING): Savage Pre Auth failed, status = 0x%!x(MISSING)\n"
+ "Armed"
+ "ChipState"
+ "EnableVibeMitigation error: 0x%!X(MISSING)\n"
+ "Error sending sCIspCmdChCropSet command: 0x%!X(MISSING)"
+ "Error sending sCIspCmdChOutputConfigSet command: 0x%!X(MISSING)"
+ "Expiry duration cannot be negative (%!f(MISSING))\n"
+ "FaultDT0"
+ "FaultDT01ST"
+ "FaultDT1"
+ "FaultDT11ST"
+ "FaultState"
+ "ISP_SavageAuth"
+ "Received frame drop request: channel=%!d(MISSING) frameDropRequestEnabled=%!d(MISSING) frameCount=%!d(MISSING)"
+ "SPD:ERR: #%!d(MISSING) SPD(%!d(MISSING),%!d(MISSING)) stride=%!d(MISSING) scaleXY(%!d(MISSING),%!d(MISSING)) totSize=%!d(MISSING)\n"
+ "SPD:ERR: CSPD::SPD pContext->meta.geom.sizeX is not expected as an odd number!!!\n"
+ "Sending data buffer failed, result=0x%!X(MISSING)"
+ "Sending shared buffer failed, result=0x%!X(MISSING)"
+ "SetCameraControlsCacheExpiryDuration error: 0x%!X(MISSING)\n"
+ "Unable to allocate a replacement buffer (poolID = CHAN_%!d(MISSING)_%!s(MISSING), actual poolID = %!d(MISSING), buffer pool pointer = %!p(MISSING))"
+ "Unable to locate surface ID %!d(MISSING)"
+ "camera is streaming, vibe mitigation cannot be performed\n"
+ "pH16ISPDevice->ISP_SendBuffers failed, result=0x%!X(MISSING)"
- "%!s(MISSING) - Error sending sCIspCmdChCropSet command: 0x%!X(MISSING)\n"
- "%!s(MISSING) - Error sending sCIspCmdChOutputConfigSet command: 0x%!X(MISSING)\n"
- "%!s(MISSING) - FW Buffer Background send error: 0x%!X(MISSING)\n\n"
- "%!s(MISSING) - FW Buffer Background timeout for 1s!\n"
- "%!s(MISSING) - H16ISPFrameReceiver - std::future is invalid! Async background task in unknown state!\n\n"
- "%!s(MISSING) - Received frame drop request: channel=%!d(MISSING) frameDropRequestEnabled=%!d(MISSING) frameCount=%!d(MISSING)\n"
- "%!s(MISSING) - Sending %!d(MISSING) initial buffers to firmware (async buffer count: %!d(MISSING)) (poolID=%!d(MISSING), poolSize=%!d(MISSING), poolType=%!d(MISSING)) result=0x%!X(MISSING)\n\n"
- "%!s(MISSING) - Sending data buffer failed, result=0x%!X(MISSING)\n"
- "%!s(MISSING) - Sending shared buffer failed, result=0x%!X(MISSING)\n"
- "%!s(MISSING) - Unable to allocate a replacement buffer (poolID = CHAN_%!d(MISSING)_%!s(MISSING), actual poolID = %!d(MISSING), buffer pool pointer = %!p(MISSING))\n"
- "%!s(MISSING) - [Exclaves]: Face ID PreCheck uxFeedback=0x%!X(MISSING) readiness=%!s(MISSING)\n"
- "%!s(MISSING) - [Exclaves]: H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) index: %!z(MISSING)u AngleInfoRoll: %!f(MISSING) Rect[%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)] Confidence %!f(MISSING) \n"
- "AddFaceIDMetadata"
- "AddSecureTrackedFacesMetadata"
- "H16ISPFrameReceiver [Async]: Done sending FW remaining %!d(MISSING) buffers: (poolID=%!d(MISSING), poolType=%!d(MISSING)) result=0x%!X(MISSING)\n\n"
- "H16ISPFrameReceiver [Async]: Started sending FW remaining %!d(MISSING) buffers: (poolID=%!d(MISSING), poolType=%!d(MISSING))\n"
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) CVAFaceTrackingLiteCopyDecodedOutput failed, err=0x%!X(MISSING) \n"
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) RunKit FT reqID:0x%!x(MISSING) channel %!d(MISSING)\n"
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) Skipped processing secure face tracking algorithm\n"
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::onActivate\n"
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::onDeactivate\n"
- "[Exclaves]: H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) EK Face Kit Runkit failed, tberr %!d(MISSING) ipcRet %!d(MISSING)\n"
- "[Exclaves]: RGB Face Tracking: channel=%!u(MISSING)\n"
- "pContext->meta.geom.sizeX %! (MISSING)== 0"
- "waitforBGsend"

```
