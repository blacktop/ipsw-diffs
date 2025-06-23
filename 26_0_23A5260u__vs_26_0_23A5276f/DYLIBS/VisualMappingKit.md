## VisualMappingKit

> `/System/Library/PrivateFrameworks/VisualMappingKit.framework/VisualMappingKit`

```diff

-8.25.5.7.1
-  __TEXT.__text: 0x636bdc
-  __TEXT.__auth_stubs: 0x1d50
-  __TEXT.__const: 0x44cb0
-  __TEXT.__cstring: 0x10824
-  __TEXT.__oslogstring: 0x2ac
-  __TEXT.__gcc_except_tab: 0x41ce0
-  __TEXT.__unwind_info: 0x11ec8
+8.25.5.28.1
+  __TEXT.__text: 0x63ad04
+  __TEXT.__auth_stubs: 0x1db0
+  __TEXT.__const: 0x44cc0
+  __TEXT.__cstring: 0x1076a
+  __TEXT.__oslogstring: 0x2d6
+  __TEXT.__gcc_except_tab: 0x421b0
+  __TEXT.__unwind_info: 0x11f00
   __TEXT.__eh_frame: 0xcd4
   __TEXT.__objc_methname: 0x23
   __TEXT.__objc_stubs: 0x60
   __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x1338
+  __DATA_CONST.__const: 0x1340
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xeb8
-  __AUTH_CONST.__const: 0x1e640
+  __AUTH_CONST.__auth_got: 0xee8
+  __AUTH_CONST.__const: 0x1e738
   __AUTH_CONST.__cfstring: 0x280
   __AUTH.__data: 0x18
-  __DATA.__data: 0x1e90
+  __DATA.__data: 0x1ec8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xa58
-  __DATA.__common: 0x298
+  __DATA.__bss: 0xa88
+  __DATA.__common: 0x2e8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23A12F2F-3059-3FD7-9A2A-E6D50ACEC7FF
-  Functions: 11798
-  Symbols:   674
-  CStrings:  1721
+  UUID: FF826F08-3983-34FF-AFC4-117768772126
+  Functions: 11803
+  Symbols:   681
+  CStrings:  1728
 
Symbols:
+ _VMKVisualLogFrame
+ __ZdlPvSt11align_val_t
+ __ZdlPvSt11align_val_tRKSt9nothrow_t
+ __ZnwmSt11align_val_t
+ __ZnwmSt11align_val_tRKSt9nothrow_t
+ __os_signpost_emit_unreliably_with_name_impl
+ _os_signpost_enabled
+ _pthread_threadid_np
+ _timespec_get
- __os_log_pack_fill
- __os_log_pack_size
CStrings:
+ " is processing only the first encountered timestamp, which was '"
+ "Database"
+ "System"
+ "T_anchor_to_global_R"
+ "T_anchor_to_global_t"
+ "T_keyframe_to_global_R"
+ "T_keyframe_to_global_t"
+ "VMKSessionProcessOdometry"
+ "Vuelta"
+ "anchors"
+ "constraints"
+ "exporter"
+ "id"
+ "image_retrieval"
+ "inlier_mask"
+ "keyframes"
+ "keypoints"
+ "kf1.has_value() && kf2.has_value()"
+ "matches"
+ "neighbor"
+ "passed_inlier_check"
+ "query_desc.Dimension() == DIMS && ref_desc.Dimension() == DIMS"
+ "query_desc.Type() == lf::DescriptorDataType::Float32 && ref_desc.Type() == lf::DescriptorDataType::Float32"
+ "query_frame_id"
+ "ref_desc.Size() == 1u && query_desc.Size() == 1u"
+ "reference_frame_id"
+ "relocalization"
+ "retrieved"
+ "source"
+ "tracing"
+ "trajectory"
- "    with tolerance: "
- "   with tolerance: "
- "  actual R^T*R:\n"
- "  actual last row: "
- "; exporter is exporting only the first encountered timestamp, which was '"
- "Invalid argument for SE3: "
- "actual determinant: "
- "cv3dapi.kit.viz.SE3"
- "expected last row: "
- "keyframe_id"
- "keyframe_info"
- "num_features"
- "query_desc.Dimension() == 128u && train_desc.Dimension() == 128u"
- "query_desc.Type() == lf::DescriptorDataType::Float32 && train_desc.Type() == lf::DescriptorDataType::Float32"
- "ret != vio::AddPoseGraphEdgeReturn::kFailDueToInvalidEdge"
- "se3 group matrix must be an affine 3x4 transform:\n"
- "se3 group matrix must have determinant 1\n"
- "se3 group rotation must be orthogonal (expecting identity R^T*R)\n"
- "train_desc.Size() == 1u && query_desc.Size() == 1u"
- "unknown file"
- "unknown function"
- "vuelta.anchor"
- "vuelta.keyframe"
- "vuelta.relocalization"
- "vuelta.trajectory"
- "with tolerance: "

```
