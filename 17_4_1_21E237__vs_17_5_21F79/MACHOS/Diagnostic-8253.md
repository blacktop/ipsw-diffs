## Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

-32.0.0.0.0
-  __TEXT.__text: 0x11674
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_stubs: 0x6c0
+38.0.0.0.0
+  __TEXT.__text: 0x12298
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_stubs: 0x740
   __TEXT.__objc_methlist: 0xe0
-  __TEXT.__gcc_except_tab: 0x1cc8
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x3730
-  __TEXT.__objc_classname: 0x1f
-  __TEXT.__objc_methname: 0x54b
-  __TEXT.__objc_methtype: 0x661
-  __TEXT.__unwind_info: 0x580
+  __TEXT.__gcc_except_tab: 0x1e00
+  __TEXT.__const: 0x48
+  __TEXT.__cstring: 0x3930
+  __TEXT.__objc_classname: 0x20
+  __TEXT.__objc_methname: 0x59d
+  __TEXT.__objc_methtype: 0x992
+  __TEXT.__unwind_info: 0x5a4
   __TEXT.__eh_frame: 0x60
-  __DATA_CONST.__auth_got: 0x338
-  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x4d8
-  __DATA_CONST.__cfstring: 0x2c80
+  __DATA_CONST.__cfstring: 0x2e00
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x48
   __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x238
-  __DATA.__objc_selrefs: 0x1d8
-  __DATA.__objc_ivar: 0x34
+  __DATA.__objc_const: 0x258
+  __DATA.__objc_selrefs: 0x1f8
+  __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12FD8216-2126-345C-B871-452D028D4952
-  Functions: 205
-  Symbols:   338
-  CStrings:  861
+  UUID: B614BD05-4BF3-3E4F-838A-5020628DF9FA
+  Functions: 208
+  Symbols:   340
+  CStrings:  892
 
Symbols:
+ __ZN17DeviceCMInterface23requestControlOfStreamsEbj
+ __ZN23JasDiagnosticInteractor23setIsJasperFrameArrivedEbii
+ __ZN28HxISPCaptureDeviceController14RequestStreamsEPK9__CFArrayPK14__CFDictionary
+ _kFigCaptureDeviceRequestControlOfStreamsOptionsKey_ClientPriority
+ _objc_release_x9
- __ZN17DeviceCMInterface23requestControlOfStreamsEv
- __ZN23JasDiagnosticInteractor23setIsJasperFrameArrivedEbi
- __ZN28HxISPCaptureDeviceController14RequestStreamsEPK9__CFArray
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Diagnostic-8253/JasDiagnosticInteractor.mm"
+ "BankDict size %zu point count %d frame %d"
+ "FW VALIDATION FAIL INFO"
+ "bankIds"
+ "cmsetcurrentformat 2 %d, setPearlFormatIndex(m_streamIdsInfo.rgbPearlStreamId, %d) ret = %d"
+ "config pearl device failed to read projector version"
+ "d"
+ "d8"
+ "d9"
+ "dictionary"
+ "done waiting"
+ "hasPrefix:"
+ "j7"
+ "lowercaseString"
+ "m_minAveragePointsNumberThreshold"
+ "projector version %d"
+ "request control on high priority"
+ "requestControlOfStreamscontrol - controlled by another client. %d/%d"
+ "waiting for preempted client to terminate for %.2f sec..."
+ "{DeviceCMInterface=\"m_hVersion\"i\"m_delegate\"^{StreamingClient}\"m_captureDeviceController\"^{HxISPCaptureDeviceController}\"m_streamIdsInfo\"{StreamIdsInfo=\"rgbTeleStreamId\"i\"rgbWideStreamId\"i\"rgbPearlStreamId\"i\"irPearlStreamId\"i\"rgbSuperWideStreamId\"i\"jasperStreamId\"i}\"m_currentPearlConfiguration\"{PearlConfiguration=\"isIrOn\"B\"isDepthOn\"B\"isRgbOn\"B\"irType\"i\"bitMaskID\"i\"deviceName\"@\"NSString\"}\"m_currentJasperConfiguration\"{JasperConfiguration=\"isJasperOn\"B\"isSuperWideOn\"B\"isWideOn\"B\"isSyncModeOn\"B\"bitMaskID\"i}\"m_primarySyncModeStreamID\"i\"m_isPearlRgbConfigured\"B\"m_isPearlIrConfigured\"B\"m_isJasperSuperWideConfigured\"B\"m_isJasperConfigured\"B}"
+ "{JasDiagnosticInteractor=\"_vptr$StreamingClient\"^^?\"m_jasperFramesCount\"i\"m_jasperPointsCount\"i\"m_rgbSuperWideFrameCount\"i\"m_isJasperFramesArrived\"B\"m_isRgbSuperWideFramesArrived\"B\"m_timer\"{DiagnosticTimer=\"sTimebaseInfo\"{mach_timebase_info=\"numer\"I\"denom\"I}\"beginTime\"Q}\"m_deviceName\"@\"NSString\"\"m_maxBanksNumberForFrame\"i\"m_minAveragePointsNumberThreshold\"d\"m_banksIdDictionary\"{map<int, int, std::less<int>, std::allocator<std::pair<const int, int>>>=\"__tree_\"{__tree<std::__value_type<int, int>, std::__map_value_compare<int, std::__value_type<int, int>, std::less<int>>, std::allocator<std::__value_type<int, int>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<int, int>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<int, std::__value_type<int, int>, std::less<int>>>=\"__value_\"Q}}}\"m_goodPointsCount\"i\"m_currentSubframeCount\"i\"m_subframeCount\"i}"
+ "\xb1qa"
- "{DeviceCMInterface=\"m_hVersion\"i\"m_delegate\"^{StreamingClient}\"m_captureDeviceController\"^{HxISPCaptureDeviceController}\"m_streamIdsInfo\"{StreamIdsInfo=\"rgbTeleStreamId\"i\"rgbWideStreamId\"i\"rgbPearlStreamId\"i\"irPearlStreamId\"i\"rgbSuperWideStreamId\"i\"jasperStreamId\"i}\"m_currentPearlConfiguration\"{PearlConfiguration=\"isIrOn\"B\"isDepthOn\"B\"isRgbOn\"B\"irType\"i\"bitMaskID\"i}\"m_currentJasperConfiguration\"{JasperConfiguration=\"isJasperOn\"B\"isSuperWideOn\"B\"isWideOn\"B\"isSyncModeOn\"B\"bitMaskID\"i}\"m_primarySyncModeStreamID\"i\"m_isPearlRgbConfigured\"B\"m_isPearlIrConfigured\"B\"m_isJasperSuperWideConfigured\"B\"m_isJasperConfigured\"B}"
- "{JasDiagnosticInteractor=\"_vptr$StreamingClient\"^^?\"m_jasperFramesCount\"i\"m_jasperPointsCount\"i\"m_rgbSuperWideFrameCount\"i\"m_isJasperFramesArrived\"B\"m_isRgbSuperWideFramesArrived\"B\"m_timer\"{DiagnosticTimer=\"sTimebaseInfo\"{mach_timebase_info=\"numer\"I\"denom\"I}\"beginTime\"Q}}"
- "\xf01"

```
