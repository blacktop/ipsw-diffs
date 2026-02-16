## Diagnostic-6002

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002`

```diff

 57.0.0.0.0
-  __TEXT.__text: 0x1c084
-  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__text: 0x1d684
+  __TEXT.__auth_stubs: 0xb50
   __TEXT.__objc_stubs: 0x1d60
   __TEXT.__objc_methlist: 0x8e4
-  __TEXT.__gcc_except_tab: 0x3074
+  __TEXT.__gcc_except_tab: 0x3010
   __TEXT.__const: 0x128
   __TEXT.__objc_methname: 0x23bf
-  __TEXT.__cstring: 0x4568
+  __TEXT.__cstring: 0x4758
   __TEXT.__objc_classname: 0xc0
-  __TEXT.__objc_methtype: 0xa85
+  __TEXT.__objc_methtype: 0xa81
   __TEXT.__oslogstring: 0x26
-  __TEXT.__unwind_info: 0x7f8
-  __DATA_CONST.__auth_got: 0x5c8
+  __TEXT.__unwind_info: 0x8a8
+  __DATA_CONST.__auth_got: 0x5c0
   __DATA_CONST.__got: 0x428
   __DATA_CONST.__const: 0x5e8
   __DATA_CONST.__cfstring: 0x3600

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A90FF3C8-5974-3DCA-83AC-BEFD8061D210
-  Functions: 351
-  Symbols:   467
-  CStrings:  1536
+  UUID: DD115B23-B07D-3BC0-A15B-6B110D8E2B27
+  Functions: 352
+  Symbols:   466
+  CStrings:  1537
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retain_x23
+ _objc_retain_x27
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
+ "/Library/Caches/com.apple.xbs/CD9A0A60-C977-4AC9-B6FF-517EF032205A/TemporaryDirectory.QiI78Y/Sources/DepthDiagnostics/Diagnostic-6002/PeCoNetViewController.mm"
+ "{map<int, std::vector<RgbJasperCalibrationInfo>, std::less<int>, std::allocator<std::pair<const int, std::vector<RgbJasperCalibrationInfo>>>>=\"__tree_\"{__tree<std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>, std::__map_value_compare<int, std::pair<const int, std::vector<RgbJasperCalibrationInfo>>, std::less<int>>, std::allocator<std::pair<const int, std::vector<RgbJasperCalibrationInfo>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
- "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Common/DeviceCMInterface.mm"
- "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Common/DiagnosticUtils.mm"
- "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Diagnostic-6002/PeCoNetViewController.mm"
- "{map<int, std::vector<RgbJasperCalibrationInfo>, std::less<int>, std::allocator<std::pair<const int, std::vector<RgbJasperCalibrationInfo>>>>=\"__tree_\"{__tree<std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>, std::__map_value_compare<int, std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>, std::less<int>>, std::allocator<std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"

```
