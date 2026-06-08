## AppC3D

> `/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D`

```diff

-1.20.0.0.0
-  __TEXT.__text: 0x878380
-  __TEXT.__auth_stubs: 0x26e0
-  __TEXT.__const: 0x6604c
-  __TEXT.__cstring: 0x17ef2
-  __TEXT.__gcc_except_tab: 0x52a7c
+1.21.0.0.0
+  __TEXT.__text: 0x89553c
+  __TEXT.__const: 0x660e0
+  __TEXT.__cstring: 0x180e6
+  __TEXT.__gcc_except_tab: 0x53ac0
   __TEXT.__oslogstring: 0xa14
-  __TEXT.__unwind_info: 0x162b8
-  __TEXT.__eh_frame: 0x1780
-  __TEXT.__objc_methname: 0x9f
-  __TEXT.__objc_stubs: 0x140
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x1d90
+  __TEXT.__unwind_info: 0x171a8
+  __TEXT.__eh_frame: 0x1788
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x1da8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x28
   __DATA_CONST.__objc_selrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x1380
-  __AUTH_CONST.__const: 0x27180
+  __DATA_CONST.__got: 0x3e8
+  __AUTH_CONST.__const: 0x273a0
   __AUTH_CONST.__cfstring: 0x340
+  __AUTH_CONST.__weak_auth_got: 0x40
+  __AUTH_CONST.__auth_got: 0x1350
   __AUTH.__data: 0x10
-  __DATA.__data: 0x1c80
+  __DATA.__data: 0x1c70
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x40
   __DATA.__common: 0x238
-  __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0xdf8
+  __DATA_DIRTY.__data: 0xa0
+  __DATA_DIRTY.__bss: 0xd78
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B6CE7283-E0C1-3328-9BB1-9478D7A44F0B
-  Functions: 16026
-  Symbols:   797
-  CStrings:  2414
+  UUID: B1B421A8-1CE9-3055-A4FD-060B09E0F34D
+  Functions: 16258
+  Symbols:   800
+  CStrings:  2410
 
Symbols:
+ _CVBufferPropagateAttachments
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
+ _kCFNull
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x24
+ _objc_retain
+ _objc_retain_x24
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x23
- _objc_retain_x26
CStrings:
+ "  #"
+ " Unable to bind surface object to input port. Port name:"
+ " as array of type with size "
+ " bytes"
+ " for format with properties:\n"
+ " getting tensor shape for buffer for output port:"
+ " size "
+ "(mesh.colors.empty() || mesh.colors.size() == mesh.vertices.size())"
+ "-inf"
+ ". If using espresso.net model. Please try setting \"experimental.aot.enable_surface_desc\" : \"1\"  in model.espresso.net properties"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppC3D/library/ODT/Util/src/PoseBucketFilter.cpp"
+ "; caused by:\n"
+ "An error occurred while loading the image"
+ "Cannot reinterpret memory region of byte size "
+ "Failed to allocate buffer for FP32 output: "
+ "Failed to create "
+ "Failed to deserialize JSON file "
+ "Failed to parse JSON file "
+ "HasAppleNeuralEngine"
+ "IOSurface"
+ "Return value != E5RT_ERROR_CODE_OK. "
+ "child_surface.Format() == Format(plane_index)"
+ "cvr == kCVReturnSuccess"
+ "enable_tensor_interface is set to true, but .net models do not support tensor interface (buffer objects). They require surface interface. Either use a .mil/.mlmodel model or set enable_tensor_interface to false."
+ "ext::expected<std::vector<bool>, Error> cv3d::appcode::codec::DecodeArcBits(const std::bitset<kColorBits> &, const std::bitset<kColorBits> &, const std::vector<bool> &, const std::vector<bool> &, const std::optional<Format>)"
+ "given "
+ "odt::imgproc::CreateLookUpTableData<>( lookup_table_data, width, height, cva::MatrixRef<const double, 3, 3, 3>{cam_intrinsics.data()}, distortion_coefficients, scale, use_rajan)"
- "(mesh.colors.size() == 0 || mesh.colors.size() == mesh.vertices.size())"
- "+N9mZUAHooNvMiQnjeTJ8g"
- ", used properties:\n"
- "- "
- ". "
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppC3D/library/ODT/ImageDetectionAndTracking/src/PoseBucketFilter.cpp"
- "DecodeArcBits"
- "Failed to create IOSurface for format "
- "UTF8String"
- "Unable to bind surface object to input port.Please set \"experimental.aot.enable_surface_desc\" : \"1\"  in model.espresso.net properties"
- "Unable to load program function: "
- "\\\""
- "\\'"
- "\\n"
- "\\r"
- "\\t"
- "aneSubType"
- "bitset set argument out of range"
- "bundlePath"
- "bundleWithIdentifier:"
- "cg_image.IsValid()"
- "child_surface.Format() == surface.Format(plane_index)"
- "dictionaryRepresentation"
- "given IOSurface size "
- "initWithSuiteName:"
- "mem_ret == E5RT_ERROR_CODE_OK"
- "objectForKey:"
- "odt::image_detection_and_tracking::CreateLookUpTableData<>( lookup_table_data, width, height, cva::MatrixRef<const double, 3, 3, 3>{cam_intrinsics.data()}, distortion_coefficients, scale, use_rajan)"
- "processInfo"
- "processName"
- "stringWithUTF8String:"

```
