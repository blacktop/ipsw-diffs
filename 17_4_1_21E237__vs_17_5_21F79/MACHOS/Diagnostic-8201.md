## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

-32.0.0.0.0
-  __TEXT.__text: 0x13b20
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_stubs: 0x760
+38.0.0.0.0
+  __TEXT.__text: 0x15124
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_stubs: 0x820
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x16c
-  __TEXT.__gcc_except_tab: 0x1fb8
-  __TEXT.__cstring: 0x45ac
-  __TEXT.__const: 0x88
-  __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x870
-  __TEXT.__objc_methtype: 0x681
-  __TEXT.__unwind_info: 0x590
+  __TEXT.__objc_methlist: 0x1cc
+  __TEXT.__gcc_except_tab: 0x22c4
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x4a39
+  __TEXT.__objc_classname: 0x55
+  __TEXT.__objc_methname: 0xa1e
+  __TEXT.__objc_methtype: 0x6b3
+  __TEXT.__unwind_info: 0x5c0
   __TEXT.__eh_frame: 0x4c
-  __DATA_CONST.__auth_got: 0x358
-  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__auth_got: 0x360
+  __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x4d8
-  __DATA_CONST.__cfstring: 0x3420
+  __DATA_CONST.__cfstring: 0x3760
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x728
-  __DATA.__objc_selrefs: 0x230
-  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_const: 0x858
+  __DATA.__objc_selrefs: 0x278
+  __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x18

   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/H10ISPServices.framework/H10ISPServices
   - /System/Library/PrivateFrameworks/JasperDepth.framework/JasperDepth
+  - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 32C7DDF1-1756-3E8D-9551-8723D82820ED
-  Functions: 213
-  Symbols:   346
-  CStrings:  1090
+  UUID: E44DD54F-D502-33F0-ABEF-1BFF99031F76
+  Functions: 223
+  Symbols:   348
+  CStrings:  1163
 
Symbols:
+ __AXSAttentionAwarenessFeaturesEnabled
+ __AXSSetAttentionAwarenessFeaturesEnabled
+ __ZN17DeviceCMInterface23requestControlOfStreamsEbj
+ __ZN28HxISPCaptureDeviceController14RequestStreamsEPK9__CFArrayPK14__CFDictionary
+ _kFigCaptureDeviceRequestControlOfStreamsOptionsKey_ClientPriority
+ _objc_retain_x20
- __ZN17DeviceCMInterface23requestControlOfStreamsEv
- __ZN28HxISPCaptureDeviceController14RequestStreamsEPK9__CFArray
- _objc_retain_x26
- _objc_retain_x4
CStrings:
+ "%@ = %d"
+ "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Diagnostic-8201/Pearl_Fw_StatusInputs.mm"
+ "FAIL, (%d passed out of %d) cannot achieve control on streams"
+ "FW VALIDATION FAIL INFO"
+ "NURI projector version detected"
+ "Ti,N,V_preemtingWaitInMicroSec"
+ "Ti,N,V_useADControl"
+ "Ti,N,V_useHighPriority"
+ "_preemtingWaitInMicroSec"
+ "_useADControl"
+ "_useHighPriority"
+ "attention detection already as require"
+ "attention detection already disabled"
+ "attention detection current status is %d after restoring"
+ "cancel triggered, verify attention detection status before bailing out"
+ "cmsetcurrentformat 2 %d, setPearlFormatIndex(m_streamIdsInfo.rgbPearlStreamId, %d) ret = %d"
+ "config pearl device failed to read projector version"
+ "current attention detection status %d"
+ "dictionary"
+ "disable attention detection, current status is %d"
+ "disableAttentionDetection"
+ "disableAttentionDetection if needed"
+ "done waiting"
+ "i28@0:8i16^{PearlConfiguration=BBBii@}20"
+ "i40@0:8{PearlConfiguration=BBBii@}16"
+ "input value: isUseADControl = %d"
+ "input value: preemtionWaitingTimeInMicroSec = %d"
+ "input value: useHighPriority = %d"
+ "m_attentionDetectionSetting"
+ "m_isNuri"
+ "m_isUseADControl"
+ "m_preemtionWaitingTimeInMicroSec"
+ "m_useHighPriorityControlRequest"
+ "preemtingWaitInMicroSec"
+ "projector version %d"
+ "request control on high priority"
+ "requestControlOfStreamscontrol - controlled by another client. %d/%d"
+ "restore attention detection if needed"
+ "restore attention detection to its prevues status of %d"
+ "restoreAttentionDetection"
+ "setPreemtingWaitInMicroSec:"
+ "setUseADControl:"
+ "setUseHighPriority:"
+ "tear down triggered, verify attention detection status before bailing out"
+ "useADControl"
+ "useHighPriority"
+ "v40@0:8{PearlConfiguration=BBBii@}16"
+ "v48@0:8{PearlConfiguration=BBBii@}16@40"
+ "waiting for preempted client to terminate for %.2f sec..."
+ "{DeviceCMInterface=\"m_hVersion\"i\"m_delegate\"^{StreamingClient}\"m_captureDeviceController\"^{HxISPCaptureDeviceController}\"m_streamIdsInfo\"{StreamIdsInfo=\"rgbTeleStreamId\"i\"rgbWideStreamId\"i\"rgbPearlStreamId\"i\"irPearlStreamId\"i\"rgbSuperWideStreamId\"i\"jasperStreamId\"i}\"m_currentPearlConfiguration\"{PearlConfiguration=\"isIrOn\"B\"isDepthOn\"B\"isRgbOn\"B\"irType\"i\"bitMaskID\"i\"deviceName\"@\"NSString\"}\"m_currentJasperConfiguration\"{JasperConfiguration=\"isJasperOn\"B\"isSuperWideOn\"B\"isWideOn\"B\"isSyncModeOn\"B\"bitMaskID\"i}\"m_primarySyncModeStreamID\"i\"m_isPearlRgbConfigured\"B\"m_isPearlIrConfigured\"B\"m_isJasperSuperWideConfigured\"B\"m_isJasperConfigured\"B}"
+ "{PearlDiagnosticInteractor=\"_vptr$StreamingClient\"^^?\"m_gmcResult\"@\"NSNumber\"\"m_gmcPointCount\"@\"NSNumber\"\"m_currentPearlConfiguration\"{PearlConfiguration=\"isIrOn\"B\"isDepthOn\"B\"isRgbOn\"B\"irType\"i\"bitMaskID\"i\"deviceName\"@\"NSString\"}\"m_rgbPearlFramesCount\"i\"m_isPearlRgbFramesArrived\"B\"m_isPearlIrFramesArrived\"B\"m_irPearlFramesCount\"i}"
+ "\x81!\x82!"
- "FAIL, (%d passed out of %d) cannot achive control on streams"
- "i28@0:8i16^{PearlConfiguration=BBBii}20"
- "i28@0:8{PearlConfiguration=BBBii}16"
- "v28@0:8{PearlConfiguration=BBBii}16"
- "v36@0:8{PearlConfiguration=BBBii}16@28"
- "{DeviceCMInterface=\"m_hVersion\"i\"m_delegate\"^{StreamingClient}\"m_captureDeviceController\"^{HxISPCaptureDeviceController}\"m_streamIdsInfo\"{StreamIdsInfo=\"rgbTeleStreamId\"i\"rgbWideStreamId\"i\"rgbPearlStreamId\"i\"irPearlStreamId\"i\"rgbSuperWideStreamId\"i\"jasperStreamId\"i}\"m_currentPearlConfiguration\"{PearlConfiguration=\"isIrOn\"B\"isDepthOn\"B\"isRgbOn\"B\"irType\"i\"bitMaskID\"i}\"m_currentJasperConfiguration\"{JasperConfiguration=\"isJasperOn\"B\"isSuperWideOn\"B\"isWideOn\"B\"isSyncModeOn\"B\"bitMaskID\"i}\"m_primarySyncModeStreamID\"i\"m_isPearlRgbConfigured\"B\"m_isPearlIrConfigured\"B\"m_isJasperSuperWideConfigured\"B\"m_isJasperConfigured\"B}"
- "{PearlDiagnosticInteractor=\"_vptr$StreamingClient\"^^?\"m_gmcResult\"@\"NSNumber\"\"m_gmcPointCount\"@\"NSNumber\"\"m_currentPearlConfiguration\"{PearlConfiguration=\"isIrOn\"B\"isDepthOn\"B\"isRgbOn\"B\"irType\"i\"bitMaskID\"i}\"m_rgbPearlFramesCount\"i\"m_isPearlRgbFramesArrived\"B\"m_isPearlIrFramesArrived\"B\"m_irPearlFramesCount\"i}"
- "\xa1\x82"

```
