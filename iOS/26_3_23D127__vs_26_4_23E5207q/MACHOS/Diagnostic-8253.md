## Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

 57.0.0.0.0
-  __TEXT.__text: 0x12f8c
-  __TEXT.__auth_stubs: 0x700
+  __TEXT.__text: 0x13bd8
+  __TEXT.__auth_stubs: 0x740
   __TEXT.__objc_stubs: 0x820
   __TEXT.__objc_methlist: 0xf8
-  __TEXT.__gcc_except_tab: 0x2220
+  __TEXT.__gcc_except_tab: 0x222c
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x3baf
+  __TEXT.__cstring: 0x3dde
   __TEXT.__objc_classname: 0x20
   __TEXT.__objc_methname: 0x60a
-  __TEXT.__objc_methtype: 0x7d5
-  __TEXT.__unwind_info: 0x5c8
-  __DATA_CONST.__auth_got: 0x390
+  __TEXT.__objc_methtype: 0x7d1
+  __TEXT.__unwind_info: 0x5d0
+  __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0x320
   __DATA_CONST.__const: 0x4f8
   __DATA_CONST.__cfstring: 0x3220

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 33AD43E7-BED3-346F-956E-E680C5D328EC
+  UUID: 5F27B1EC-906A-32D2-8BF7-1AF5DC829D07
   Functions: 207
-  Symbols:   355
-  CStrings:  967
+  Symbols:   359
+  CStrings:  968
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIVHugA-cBTIxKkO3sPQ2yf9upAS1yjcAr_VL1E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/Library/Caches/com.apple.xbs/CD9A0A60-C977-4AC9-B6FF-517EF032205A/TemporaryDirectory.QiI78Y/Sources/DepthDiagnostics/Common/DeviceCMInterface.mm"
+ "/Library/Caches/com.apple.xbs/CD9A0A60-C977-4AC9-B6FF-517EF032205A/TemporaryDirectory.QiI78Y/Sources/DepthDiagnostics/Common/DiagnosticUtils.mm"
+ "/Library/Caches/com.apple.xbs/CD9A0A60-C977-4AC9-B6FF-517EF032205A/TemporaryDirectory.QiI78Y/Sources/DepthDiagnostics/Diagnostic-8253/JasDiagnosticInteractor.mm"
+ "/Library/Caches/com.apple.xbs/CD9A0A60-C977-4AC9-B6FF-517EF032205A/TemporaryDirectory.QiI78Y/Sources/DepthDiagnostics/Diagnostic-8253/Jas_FW_Status_iOSController.mm"
+ "{JasDiagnosticInteractor=\"_vptr$StreamingClient\"^^?\"m_jasperFramesCount\"i\"m_jasperPointsCount\"i\"m_rgbSuperWideFrameCount\"i\"m_isJasperFramesArrived\"B\"m_isRgbSuperWideFramesArrived\"B\"m_timer\"{DiagnosticTimer=\"sTimebaseInfo\"{mach_timebase_info=\"numer\"I\"denom\"I}\"beginTime\"Q}\"m_deviceName\"@\"NSString\"\"m_maxBanksNumberForFrame\"i\"m_minAveragePointsNumberThreshold\"d\"m_banksIdDictionary\"{map<int, int, std::less<int>, std::allocator<std::pair<const int, int>>>=\"__tree_\"{__tree<std::__value_type<int, int>, std::__map_value_compare<int, std::pair<const int, int>, std::less<int>>, std::allocator<std::pair<const int, int>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}\"m_goodPointsCount\"i\"m_currentSubframeCount\"i\"m_subframeCount\"i}"
- "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Common/DeviceCMInterface.mm"
- "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Common/DiagnosticUtils.mm"
- "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Diagnostic-8253/JasDiagnosticInteractor.mm"
- "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Diagnostic-8253/Jas_FW_Status_iOSController.mm"
- "{JasDiagnosticInteractor=\"_vptr$StreamingClient\"^^?\"m_jasperFramesCount\"i\"m_jasperPointsCount\"i\"m_rgbSuperWideFrameCount\"i\"m_isJasperFramesArrived\"B\"m_isRgbSuperWideFramesArrived\"B\"m_timer\"{DiagnosticTimer=\"sTimebaseInfo\"{mach_timebase_info=\"numer\"I\"denom\"I}\"beginTime\"Q}\"m_deviceName\"@\"NSString\"\"m_maxBanksNumberForFrame\"i\"m_minAveragePointsNumberThreshold\"d\"m_banksIdDictionary\"{map<int, int, std::less<int>, std::allocator<std::pair<const int, int>>>=\"__tree_\"{__tree<std::__value_type<int, int>, std::__map_value_compare<int, std::__value_type<int, int>, std::less<int>>, std::allocator<std::__value_type<int, int>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}\"m_goodPointsCount\"i\"m_currentSubframeCount\"i\"m_subframeCount\"i}"

```
