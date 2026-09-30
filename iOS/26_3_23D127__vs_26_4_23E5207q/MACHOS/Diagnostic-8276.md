## Diagnostic-8276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276`

```diff

 57.0.0.0.0
-  __TEXT.__text: 0x1b280
-  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__text: 0x1c750
+  __TEXT.__auth_stubs: 0xb30
   __TEXT.__objc_stubs: 0x1bc0
   __TEXT.__objc_methlist: 0x8a4
-  __TEXT.__gcc_except_tab: 0x2d80
+  __TEXT.__gcc_except_tab: 0x2d1c
   __TEXT.__const: 0x128
   __TEXT.__objc_methname: 0x225d
-  __TEXT.__cstring: 0x42ee
+  __TEXT.__cstring: 0x449f
   __TEXT.__objc_classname: 0xca
-  __TEXT.__objc_methtype: 0xa16
+  __TEXT.__objc_methtype: 0xa12
   __TEXT.__oslogstring: 0x11d
-  __TEXT.__unwind_info: 0x7d0
-  __DATA_CONST.__auth_got: 0x5c0
+  __TEXT.__unwind_info: 0x878
+  __DATA_CONST.__auth_got: 0x5b0
   __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0x5e8
   __DATA_CONST.__cfstring: 0x3480

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7E1121AF-5994-3EDF-B63F-39232F2550D2
-  Functions: 346
-  Symbols:   464
-  CStrings:  1497
+  UUID: 510A09E4-9D50-3E0F-BD7F-F2946A3FEFA7
+  Functions: 347
+  Symbols:   462
+  CStrings:  1498
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retain_x23
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIVHugA-cBTIxKkO3sPQ2yf9upAS1yjcAr_VL1E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/Library/Caches/com.apple.xbs/CD9A0A60-C977-4AC9-B6FF-517EF032205A/TemporaryDirectory.QiI78Y/Sources/DepthDiagnostics/Common/DeviceCMInterface.mm"
+ "/Library/Caches/com.apple.xbs/CD9A0A60-C977-4AC9-B6FF-517EF032205A/TemporaryDirectory.QiI78Y/Sources/DepthDiagnostics/Common/DiagnosticUtils.mm"
+ "{map<int, std::vector<RgbJasperCalibrationInfo>, std::less<int>, std::allocator<std::pair<const int, std::vector<RgbJasperCalibrationInfo>>>>=\"__tree_\"{__tree<std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>, std::__map_value_compare<int, std::pair<const int, std::vector<RgbJasperCalibrationInfo>>, std::less<int>>, std::allocator<std::pair<const int, std::vector<RgbJasperCalibrationInfo>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Common/DeviceCMInterface.mm"
- "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Common/DiagnosticUtils.mm"
- "{map<int, std::vector<RgbJasperCalibrationInfo>, std::less<int>, std::allocator<std::pair<const int, std::vector<RgbJasperCalibrationInfo>>>>=\"__tree_\"{__tree<std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>, std::__map_value_compare<int, std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>, std::less<int>>, std::allocator<std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"

```
