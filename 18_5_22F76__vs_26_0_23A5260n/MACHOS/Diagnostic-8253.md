## Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

-53.0.0.0.0
-  __TEXT.__text: 0x125c8
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_stubs: 0x740
+54.0.0.0.0
+  __TEXT.__text: 0x127b8
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_stubs: 0x780
   __TEXT.__objc_methlist: 0xe0
-  __TEXT.__gcc_except_tab: 0x2088
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x39ad
+  __TEXT.__gcc_except_tab: 0x2070
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x39f5
   __TEXT.__objc_classname: 0x20
-  __TEXT.__objc_methname: 0x585
-  __TEXT.__objc_methtype: 0x992
-  __TEXT.__unwind_info: 0x588
-  __DATA_CONST.__auth_got: 0x370
-  __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0x4d8
-  __DATA_CONST.__cfstring: 0x2ea0
+  __TEXT.__objc_methname: 0x5a1
+  __TEXT.__objc_methtype: 0x7bd
+  __TEXT.__unwind_info: 0x5a8
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__const: 0x4f8
+  __DATA_CONST.__cfstring: 0x2f60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA.__objc_const: 0x258
-  __DATA.__objc_selrefs: 0x1f8
+  __DATA.__objc_selrefs: 0x208
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 45F24345-0004-32B8-8321-3AD2BCDD1304
-  Functions: 198
-  Symbols:   346
-  CStrings:  903
+  UUID: 016A0BA4-7241-3F83-9E0D-D98C1F8D7387
+  Functions: 204
+  Symbols:   351
+  CStrings:  917
 
Symbols:
+ __Z18ecPearlStatusCheckv
+ __Z21stringForSensorStatusj
+ __Z38ecDiagnosticStatusCodeFromStatusStringP8NSString
+ _exclaves_sensor_create
+ _exclaves_sensor_status
+ _mach_port_deallocate
+ _mach_task_self_
- __Znwm
- _memcpy
CStrings:
+ "UTF8String"
+ "allowed"
+ "com.apple.sensors.cam_alt_faceid"
+ "control"
+ "denied"
+ "isEqualToString:"
+ "pending"
+ "unknown"
+ "{JasDiagnosticInteractor=\"_vptr$StreamingClient\"^^?\"m_jasperFramesCount\"i\"m_jasperPointsCount\"i\"m_rgbSuperWideFrameCount\"i\"m_isJasperFramesArrived\"B\"m_isRgbSuperWideFramesArrived\"B\"m_timer\"{DiagnosticTimer=\"sTimebaseInfo\"{mach_timebase_info=\"numer\"I\"denom\"I}\"beginTime\"Q}\"m_deviceName\"@\"NSString\"\"m_maxBanksNumberForFrame\"i\"m_minAveragePointsNumberThreshold\"d\"m_banksIdDictionary\"{map<int, int, std::less<int>, std::allocator<std::pair<const int, int>>>=\"__tree_\"{__tree<std::__value_type<int, int>, std::__map_value_compare<int, std::__value_type<int, int>, std::less<int>>, std::allocator<std::__value_type<int, int>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}\"m_goodPointsCount\"i\"m_currentSubframeCount\"i\"m_subframeCount\"i}"
+ "{vector<JasperConfiguration, std::allocator<JasperConfiguration>>=\"__begin_\"^{JasperConfiguration}\"__end_\"^{JasperConfiguration}\"__cap_\"^{JasperConfiguration}}"
+ "{vector<JasperValidationStatus, std::allocator<JasperValidationStatus>>=\"__begin_\"^{JasperValidationStatus}\"__end_\"^{JasperValidationStatus}\"__cap_\"^{JasperValidationStatus}}"
- "{JasDiagnosticInteractor=\"_vptr$StreamingClient\"^^?\"m_jasperFramesCount\"i\"m_jasperPointsCount\"i\"m_rgbSuperWideFrameCount\"i\"m_isJasperFramesArrived\"B\"m_isRgbSuperWideFramesArrived\"B\"m_timer\"{DiagnosticTimer=\"sTimebaseInfo\"{mach_timebase_info=\"numer\"I\"denom\"I}\"beginTime\"Q}\"m_deviceName\"@\"NSString\"\"m_maxBanksNumberForFrame\"i\"m_minAveragePointsNumberThreshold\"d\"m_banksIdDictionary\"{map<int, int, std::less<int>, std::allocator<std::pair<const int, int>>>=\"__tree_\"{__tree<std::__value_type<int, int>, std::__map_value_compare<int, std::__value_type<int, int>, std::less<int>>, std::allocator<std::__value_type<int, int>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<int, int>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<int, std::__value_type<int, int>, std::less<int>>>=\"__value_\"Q}}}\"m_goodPointsCount\"i\"m_currentSubframeCount\"i\"m_subframeCount\"i}"
- "{vector<JasperConfiguration, std::allocator<JasperConfiguration>>=\"__begin_\"^{JasperConfiguration}\"__end_\"^{JasperConfiguration}\"__end_cap_\"{__compressed_pair<JasperConfiguration *, std::allocator<JasperConfiguration>>=\"__value_\"^{JasperConfiguration}}}"
- "{vector<JasperValidationStatus, std::allocator<JasperValidationStatus>>=\"__begin_\"^{JasperValidationStatus}\"__end_\"^{JasperValidationStatus}\"__end_cap_\"{__compressed_pair<JasperValidationStatus *, std::allocator<JasperValidationStatus>>=\"__value_\"^{JasperValidationStatus}}}"

```
