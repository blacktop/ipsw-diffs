## Diagnostic-8276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276`

```diff

-53.0.0.0.0
-  __TEXT.__text: 0x1a66c
-  __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_stubs: 0x1a40
+54.0.0.0.0
+  __TEXT.__text: 0x1ace0
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_stubs: 0x1b60
   __TEXT.__objc_methlist: 0x8a4
-  __TEXT.__gcc_except_tab: 0x2b5c
+  __TEXT.__gcc_except_tab: 0x2c34
   __TEXT.__const: 0x128
-  __TEXT.__objc_methname: 0x21a0
-  __TEXT.__cstring: 0x400b
+  __TEXT.__objc_methname: 0x221f
+  __TEXT.__cstring: 0x4186
   __TEXT.__objc_classname: 0xca
-  __TEXT.__objc_methtype: 0xc41
+  __TEXT.__objc_methtype: 0x9fe
   __TEXT.__oslogstring: 0x11d
-  __TEXT.__unwind_info: 0x7a0
-  __DATA_CONST.__auth_got: 0x580
-  __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0x5c8
-  __DATA_CONST.__cfstring: 0x2fe0
+  __TEXT.__unwind_info: 0x7c0
+  __DATA_CONST.__auth_got: 0x5a8
+  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__const: 0x5e8
+  __DATA_CONST.__cfstring: 0x31c0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x1288
-  __DATA.__objc_selrefs: 0x968
+  __DATA.__objc_selrefs: 0x9b0
   __DATA.__objc_ivar: 0x15c
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x120

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CoreUI.framework/CoreUI
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/JasperDepth.framework/JasperDepth
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C31E5C8-AF06-3F5C-9854-DBD065A57790
-  Functions: 341
-  Symbols:   449
-  CStrings:  1411
+  UUID: A5AB8581-BAD0-3D00-8A33-2D4709DA0131
+  Functions: 345
+  Symbols:   460
+  CStrings:  1450
 
Symbols:
+ _NSClassFromString
+ _OBJC_CLASS_$_CUICatalog
+ _OBJC_CLASS_$_UIDevice
+ __Z18ecPearlStatusCheckv
+ __Z21stringForSensorStatusj
+ __Z38ecDiagnosticStatusCodeFromStatusStringP8NSString
+ _exclaves_sensor_create
+ _exclaves_sensor_status
+ _mach_port_deallocate
+ _mach_task_self_
+ _objc_opt_isKindOfClass
+ _objc_retain_x24
- __Znwm
CStrings:
+ "/System/Library/CoreServices/CoreGlyphsPrivate.bundle"
+ "Assets"
+ "CUINamedImage"
+ "Falling back to SF Symbol: checkmark.circle"
+ "Image name %@ not found in catalog."
+ "No suitable image found for %@"
+ "Selected image: %@ - Scale: %.1f, Size: {%.1f, %.1f}"
+ "allImageNames"
+ "allowed"
+ "bundleWithPath:"
+ "com.apple.sensors.cam_alt_faceid"
+ "control"
+ "currentDevice"
+ "denied"
+ "image"
+ "imagesWithName:"
+ "initWithName:fromBundle:error:"
+ "ipad.rear.camera.badge.checkmark"
+ "iphone.rear.camera.badge.checkmark"
+ "pending"
+ "scale"
+ "size"
+ "unknown"
+ "userInterfaceIdiom"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}"
+ "{map<int, std::vector<RgbJasperCalibrationInfo>, std::less<int>, std::allocator<std::pair<const int, std::vector<RgbJasperCalibrationInfo>>>>=\"__tree_\"{__tree<std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>, std::__map_value_compare<int, std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>, std::less<int>>, std::allocator<std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
- "{map<int, std::vector<RgbJasperCalibrationInfo>, std::less<int>, std::allocator<std::pair<const int, std::vector<RgbJasperCalibrationInfo>>>>=\"__tree_\"{__tree<std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>, std::__map_value_compare<int, std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>, std::less<int>>, std::allocator<std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<int, std::__value_type<int, std::vector<RgbJasperCalibrationInfo>>, std::less<int>>>=\"__value_\"Q}}}"
- "{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__begin_\"^\"__end_\"^\"__end_cap_\"{__compressed_pair<float * __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__value_\"^}}"

```
