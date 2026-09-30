## Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

 57.0.0.0.0
-  __TEXT.__text: 0x12f88
+  __TEXT.__text: 0x12f8c
   __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_stubs: 0x820
   __TEXT.__objc_methlist: 0xf8

   __TEXT.__cstring: 0x3baf
   __TEXT.__objc_classname: 0x20
   __TEXT.__objc_methname: 0x60a
-  __TEXT.__objc_methtype: 0x7bd
+  __TEXT.__objc_methtype: 0x7d5
   __TEXT.__unwind_info: 0x5c8
   __DATA_CONST.__auth_got: 0x390
   __DATA_CONST.__got: 0x320

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A822FF5-BD46-3E54-BF54-9D104F3E6EDD
+  UUID: 48D13208-ACD0-345C-8969-CE76FCD56C9E
   Functions: 207
   Symbols:   355
   CStrings:  967
Functions:
~ sub_100005b5c : 60 -> 64
~ sub_100005c18 -> sub_100005c1c : 288 -> 284
~ sub_100005e64 : 316 -> 320
CStrings:
+ "{JasDiagnosticInteractor=\"_vptr$StreamingClient\"^^?\"m_jasperFramesCount\"i\"m_jasperPointsCount\"i\"m_rgbSuperWideFrameCount\"i\"m_isJasperFramesArrived\"B\"m_isRgbSuperWideFramesArrived\"B\"m_timer\"{DiagnosticTimer=\"sTimebaseInfo\"{mach_timebase_info=\"numer\"I\"denom\"I}\"beginTime\"Q}\"m_deviceName\"@\"NSString\"\"m_maxBanksNumberForFrame\"i\"m_minAveragePointsNumberThreshold\"d\"m_banksIdDictionary\"{map<int, int, std::less<int>, std::allocator<std::pair<const int, int>>>=\"__tree_\"{__tree<std::__value_type<int, int>, std::__map_value_compare<int, std::__value_type<int, int>, std::less<int>>, std::allocator<std::__value_type<int, int>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}\"m_goodPointsCount\"i\"m_currentSubframeCount\"i\"m_subframeCount\"i}"
+ "{vector<JasperConfiguration, std::allocator<JasperConfiguration>>=\"__begin_\"^{JasperConfiguration}\"__end_\"^{JasperConfiguration}\"\"{?=\"__cap_\"^{JasperConfiguration}}}"
+ "{vector<JasperValidationStatus, std::allocator<JasperValidationStatus>>=\"__begin_\"^{JasperValidationStatus}\"__end_\"^{JasperValidationStatus}\"\"{?=\"__cap_\"^{JasperValidationStatus}}}"
- "{JasDiagnosticInteractor=\"_vptr$StreamingClient\"^^?\"m_jasperFramesCount\"i\"m_jasperPointsCount\"i\"m_rgbSuperWideFrameCount\"i\"m_isJasperFramesArrived\"B\"m_isRgbSuperWideFramesArrived\"B\"m_timer\"{DiagnosticTimer=\"sTimebaseInfo\"{mach_timebase_info=\"numer\"I\"denom\"I}\"beginTime\"Q}\"m_deviceName\"@\"NSString\"\"m_maxBanksNumberForFrame\"i\"m_minAveragePointsNumberThreshold\"d\"m_banksIdDictionary\"{map<int, int, std::less<int>, std::allocator<std::pair<const int, int>>>=\"__tree_\"{__tree<std::__value_type<int, int>, std::__map_value_compare<int, std::__value_type<int, int>, std::less<int>>, std::allocator<std::__value_type<int, int>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}\"m_goodPointsCount\"i\"m_currentSubframeCount\"i\"m_subframeCount\"i}"
- "{vector<JasperConfiguration, std::allocator<JasperConfiguration>>=\"__begin_\"^{JasperConfiguration}\"__end_\"^{JasperConfiguration}\"__cap_\"^{JasperConfiguration}}"
- "{vector<JasperValidationStatus, std::allocator<JasperValidationStatus>>=\"__begin_\"^{JasperValidationStatus}\"__end_\"^{JasperValidationStatus}\"__cap_\"^{JasperValidationStatus}}"

```
