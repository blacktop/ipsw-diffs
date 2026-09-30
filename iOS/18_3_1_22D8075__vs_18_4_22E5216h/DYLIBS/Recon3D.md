## Recon3D

> `/System/Library/PrivateFrameworks/Recon3D.framework/Recon3D`

```diff

-7.23.0.0.0
-  __TEXT.__text: 0x151e25c
-  __TEXT.__auth_stubs: 0x2590
-  __TEXT.__cstring: 0x4142c
-  __TEXT.__const: 0x10dd0b
-  __TEXT.__oslogstring: 0x7327
-  __TEXT.__gcc_except_tab: 0xeaf20
-  __TEXT.__unwind_info: 0x342c0
-  __TEXT.__eh_frame: 0x218
+7.63.0.0.0
+  __TEXT.__text: 0x14b6dcc
+  __TEXT.__auth_stubs: 0x2530
+  __TEXT.__const: 0x10d94b
+  __TEXT.__cstring: 0x41aeb
+  __TEXT.__gcc_except_tab: 0xe2d40
+  __TEXT.__oslogstring: 0x75c3
+  __TEXT.__unwind_info: 0x339d8
+  __TEXT.__eh_frame: 0x2d8
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0xc19
   __TEXT.__objc_stubs: 0x1080
-  __DATA_CONST.__got: 0x468
-  __DATA_CONST.__const: 0x15d8
+  __DATA_CONST.__got: 0x480
+  __DATA_CONST.__const: 0x1d68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x420
-  __AUTH_CONST.__auth_got: 0x12d8
+  __AUTH_CONST.__auth_got: 0x12a8
   __AUTH_CONST.__auth_ptr: 0xa8
-  __AUTH_CONST.__const: 0x5b778
+  __AUTH_CONST.__const: 0x5b5c0
   __AUTH_CONST.__cfstring: 0x260
   __AUTH.__data: 0x8
   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_bss: 0x38
-  __DATA.__data: 0x9c38
+  __DATA.__data: 0x9c40
+  __DATA.__llvm_prf_cnts: 0x950
+  __DATA.__llvm_prf_data: 0x25c0
+  __DATA.__llvm_prf_names: 0x3955
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x2020
-  __DATA.__common: 0x4f8
+  __DATA.__bss: 0x2018
+  __DATA.__common: 0x4f0
   __DATA_DIRTY.__data: 0x70
   __DATA_DIRTY.__bss: 0x5c58
+  __LLVM_COV.__llvm_covfun: 0x18450
+  __LLVM_COV.__llvm_covmap: 0x448
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 35876
-  Symbols:   1664
-  CStrings:  6772
+  Functions: 35374
+  Symbols:   1660
+  CStrings:  6815
 
Symbols:
+ _CV3DReconSessionConfigurationEnableRoomPlan
+ _CV3DReconSessionConfigurationHasRoomPlanEnabled
+ __ZNSt13exception_ptr31__from_native_exception_pointerEPv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ ___cxa_init_primary_exception
+ _objc_retain_x26
- _CV3DReconMeshingConfigurationEnableReflectivityMapping
- _CV3DReconMeshingConfigurationHasReflectivityMapping
- _CV3DReconSessionConfigurationEnablePersonMasking
- __ZNSt3__18ios_base5imbueERKNS_6localeE
- ___invert_d2
- ___invert_d3
- ___invert_f2
- ___invert_f3
- ___invert_f4
- _fmodf
- _objc_autorelease
- _objc_retain_x25
CStrings:
+ "!flush_after_replay_received_"
+ "!kvi::ShouldHaveValidKeyframe(kvi::KeyVolEventFromUpdateState(kf.update_state))"
+ "&"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/add_rings.hpp"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/get_turn_info_la.hpp"
+ "/AppleInternal/Library/BuildRoots/67297523-efcb-11ef-9685-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/rational.hpp"
+ "/Library/Caches/com.apple.xbs/Sources/Recon3D/library/Essentials/Apple/src/Clock.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/Recon3D/library/Kit/CoreVideo/src/CVImage.cpp:55"
+ "/Library/Caches/com.apple.xbs/Sources/Recon3D/library/Reconstruction/Block/include/Reconstruction/Block/ChunkRecycler.hpp"
+ "/Library/Caches/com.apple.xbs/Sources/Recon3D/library/Reconstruction/Mapper/include/Reconstruction/Mapper/KeyframingAdaptor.h"
+ "0 == mach_timebase_info(&timebase)"
+ "Bundle voxel size not found"
+ "Candidate floor plane %.13s in floor selection is close to vertical."
+ "ColorMetadata"
+ "Deintegrating keyframe %s"
+ "Deintegrating keyframe %s - nothing to do"
+ "Expect invalid keyframes"
+ "Expect valid keyframes"
+ "Expected the existing voxel size to be equal to the given one!"
+ "GridExtent"
+ "Incrementing previous frame timestamp for flush event %.3fs"
+ "Indoor room %.13s does not have room boundary. Skip associating planes."
+ "KFE result has zero timestamp; interpreting this as a 'flush after replay' event."
+ "KFM:S"
+ "KFM:T"
+ "KFOS:BL O:%llu K:%llu NK:%lu"
+ "KFS %.13s was added (update timestamp: %.3fs, creation timestamp: %.3fs)"
+ "KFS %.13s was modified (pose: %d, content: %d, update timestamp: %.3fs)"
+ "KFS %.13s will be removed (update timestamp: %.3fs)"
+ "Mapper bundle container not initialized!"
+ "No valid voxel size for bundle!"
+ "Occupancy is enabled, but not yet support cluster-recon."
+ "Processing at %.3fs keyframe %.13s creation with timestamp %.3fs (Δ=%.3fs)"
+ "Processing at %.3fs keyframe %.13s relocalization with timestamp %.3fs (Δ=%.3fs)"
+ "Processing at %.3fs keyframe %.13s update with timestamp %.3fs (Δ=%.3fs)"
+ "Received KFE result for timestamp %.3fs with %zu keyframe updates, %zu updates pending updates, %zu integration candidates, %zu overlapping candidates."
+ "Received another update after 'flush after replay' event."
+ "Setting current frame timestamp %.3fs (Δ=%.3fs)"
+ "SingleShot.planes"
+ "SingleShot.segmentation_mask"
+ "Timestamp update %.3fs -> %.3fs is non-monotonic"
+ "VLM: Updated block %d erased before meshing"
+ "VLM:ME UPC:%d UPV:%d UPF:%d RMC:%d, GCHS:%ld, GCHC:%ld"
+ "VLM:UKF:PP HC:%lu DC:%lu MC:%lu"
+ "VLM:UKF:RC B:%d, OVS:%lf, NVS:%lf"
+ "VLM:UKF:Skip"
+ "VLM:UKF:Skip HCM:%lu DCM:%lu"
+ "Volumetric.Preprocessing"
+ "active_depth_dt"
+ "bundle_blocks != iter_chunk->second.end() && \"Can only erase an added block!\""
+ "chunk_pos == MapToCoarserVoxelPosition(chunk_pos, chunk_size_)"
+ "color_frame"
+ "com.apple.recon3d.kfplanes.polygon_extents"
+ "com.apple.recon3d.room_plan.enabled"
+ "common.room_plan.enabled"
+ "const "
+ "depth_conf"
+ "is_3dof"
+ "it != bundle_voxel_sizes.end()"
+ "it_size != chunk_block_bundle_index.bundle_voxel_sizes.end()"
+ "it_voxel_size != bundle_voxel_sizes.end()"
+ "kf.update_time <= CurrentFrameTime()"
+ "kvi::ShouldHaveValidKeyframe(kvi::KeyVolEventFromUpdateState(kf.update_state))"
+ "map_size"
+ "mapper_bundle_container_ != nullptr"
+ "max_voxel_size > 0"
+ "region_index == i->first"
+ "std::abs(voxel_size - it->second) < std::numeric_limits<float>::epsilon()"
+ "string_view::substr"
+ "voxel_size <= config_.max_voxel_size"
+ "voxel_size <= max_voxel_size_"
+ "voxel_size > 0"
+ "voxel_size > std::numeric_limits<float>::epsilon()"
+ "voxel_size_opt.has_value()"
- " -> "
- " is non-monotonic"
- "$1"
- "(cluster_sum_voxel.semantic_contribution.e() >= 0).all()"
- "(Δ="
- "/AppleInternal/Library/BuildRoots/849ea0ff-b99c-11ef-afc1-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
- "/AppleInternal/Library/BuildRoots/849ea0ff-b99c-11ef-afc1-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/add_rings.hpp"
- "/AppleInternal/Library/BuildRoots/849ea0ff-b99c-11ef-afc1-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/get_turn_info_la.hpp"
- "/AppleInternal/Library/BuildRoots/849ea0ff-b99c-11ef-afc1-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/boost/rational.hpp"
- "/Library/Caches/com.apple.xbs/Sources/Recon3D/library/Kit/CoreVideo/src/CVImage.cpp:51"
- "Backlogged %llu frames; Updated %llu frames."
- "Deintegrating keyframe %s\n"
- "Deintegrating keyframe %s - nothing to do\n"
- "Global keyframe polygon for plane %.13s is empty after filtering"
- "Indoor room  %.13s does not have room boundary. Skip associating planes."
- "KFM:Keyframing Disk IO loop started"
- "KFS %.13s was added"
- "KFS %.13s was modified (pose: %d, content: %d)"
- "KFS %.13s will be removed"
- "Keyframing Disk IO loop terminated"
- "No method to save given format"
- "Occuancy is enabled, but not yet support cluster-recon."
- "Processing %zu keyframe updates. %zu updates pending updates, %zu integration candidates, %zu overlapping candidates."
- "Processing frame with timestamp "
- "Timestamp update "
- "VLM:ME UPC:%d UPV:%d UPF:%d RMC:%d"
- "VLM:MEM GCHC:%ld GCHS:%ld"
- "VLM:PP:HC %lu"
- "Volumetric.Preprocesing"
- "cluster_sum_voxel.clutter >= voxel.clutter"
- "cluster_sum_voxel.free >= voxel.free"
- "cluster_sum_voxel.keyframes >= voxel.keyframes"
- "cluster_sum_voxel.occupied >= voxel.occupied"
- "count_observed_voxels_ > 0"
- "depth_std"
- "iter_bid != bundle_block_index.end()"
- "iter_bid_block != iter_bid->second.end()"
- "iter_chunk_block != iter_chunk->second.end() && \"Can only erase an added block!\""
- "kpseg.UpdateTimestamp() == kf_data.update_time"
- "ref->UpdateTimestamp() == kf.update_time"
- "uuid: "
- "voxel.clutter > 0 || voxel.point.norm2() < 1e-3f"

```
