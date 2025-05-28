## VisualLocalization

> `/System/Library/PrivateFrameworks/VisualLocalization.framework/VisualLocalization`

```diff

-49.31.8.9.3
-  __TEXT.__text: 0x109b70
-  __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_methlist: 0x694
-  __TEXT.__cstring: 0x8320
+49.32.9.28.4
+  __TEXT.__text: 0x10d298
+  __TEXT.__auth_stubs: 0x1300
+  __TEXT.__objc_methlist: 0x7fc
+  __TEXT.__cstring: 0x88b6
   __TEXT.__oslogstring: 0x1280
-  __TEXT.__const: 0x3030
-  __TEXT.__gcc_except_tab: 0x934
+  __TEXT.__const: 0x2fd0
+  __TEXT.__gcc_except_tab: 0x96c
   __TEXT.__dlopen_cstrs: 0xe1
-  __TEXT.__unwind_info: 0x106c
+  __TEXT.__unwind_info: 0x1154
   __TEXT.__eh_frame: 0xd8
-  __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methname: 0x26e3
-  __TEXT.__objc_methtype: 0x3d6a
-  __TEXT.__objc_stubs: 0x1e20
+  __TEXT.__objc_classname: 0x16d
+  __TEXT.__objc_methname: 0x2ad1
+  __TEXT.__objc_methtype: 0x3d7e
+  __TEXT.__objc_stubs: 0x2380
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0x648
-  __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1a80
-  __DATA_CONST.__objc_selrefs: 0x928
-  __AUTH_CONST.__cfstring: 0x1060
-  __AUTH_CONST.__objc_const: 0x428
+  __DATA_CONST.__objc_const: 0x1d30
+  __DATA_CONST.__objc_selrefs: 0xa80
+  __AUTH_CONST.__cfstring: 0x10a0
+  __AUTH_CONST.__objc_const: 0x4f8
   __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_ptr: 0xd8
-  __AUTH_CONST.__auth_got: 0x9c0
-  __AUTH.__objc_data: 0x190
+  __AUTH_CONST.__auth_ptr: 0xe8
+  __AUTH_CONST.__auth_got: 0x998
+  __AUTH.__objc_data: 0x1e0
   __AUTH.__data: 0x10
-  __DATA.__objc_classrefs: 0x148
-  __DATA.__objc_superrefs: 0x40
-  __DATA.__objc_ivar: 0x118
+  __DATA.__objc_classrefs: 0x170
+  __DATA.__objc_superrefs: 0x48
+  __DATA.__objc_ivar: 0x128
   __DATA.__data: 0x324
   __DATA.__thread_vars: 0x18
   __DATA.__thread_data: 0x8
   __DATA.__common: 0x288
-  __DATA.__bss: 0x121d60
+  __DATA.__bss: 0x802241
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x108
+  __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1416
-  Symbols:   3856
-  CStrings:  1632
+  Functions: 1514
+  Symbols:   4120
+  CStrings:  1834
 
Symbols:
+ +[GEOVLFCrowdsourcingDetails(VisualLocalizationExtras) _vl_createWithVLCrowdsourcingDetails:]
+ +[VLLocalizationCrowdsourcingDetails supportsSecureCoding]
+ -[VLLocalizationCrowdsourcingDetails .cxx_destruct]
+ -[VLLocalizationCrowdsourcingDetails descriptorDimension]
+ -[VLLocalizationCrowdsourcingDetails encodeWithCoder:]
+ -[VLLocalizationCrowdsourcingDetails frameCount]
+ -[VLLocalizationCrowdsourcingDetails initWithCoder:]
+ -[VLLocalizationCrowdsourcingDetails initWithStats:resultTransform:]
+ -[VLLocalizationCrowdsourcingDetails inlierIndices]
+ -[VLLocalizationCrowdsourcingDetails inliersCount]
+ -[VLLocalizationCrowdsourcingDetails perFrameCalibrationMatrices]
+ -[VLLocalizationCrowdsourcingDetails perFrameDistortion]
+ -[VLLocalizationCrowdsourcingDetails perFrameVioPoses]
+ -[VLLocalizationCrowdsourcingDetails perFrameVioStatusCodes]
+ -[VLLocalizationCrowdsourcingDetails points2D]
+ -[VLLocalizationCrowdsourcingDetails points3D]
+ -[VLLocalizationCrowdsourcingDetails resultPoseRotation]
+ -[VLLocalizationCrowdsourcingDetails resultPoseTranslation]
+ -[VLLocalizationCrowdsourcingDetails slamOrigin]
+ -[VLLocalizationCrowdsourcingDetails slamTrackDescriptors]
+ -[VLLocalizationCrowdsourcingDetails slamTrackImageIndices]
+ -[VLLocalizationCrowdsourcingDetails slamTrackObservations]
+ -[VLLocalizationCrowdsourcingDetails slamTracks2D]
+ -[VLLocalizationCrowdsourcingDetails slamTracksCount]
+ -[VLLocalizationCrowdsourcingDetails slamTracks]
+ -[VLLocalizationCrowdsourcingDetails statistics]
+ -[VLLocalizationDebugInfo crowdsourcingDetails]
+ _.str.25
+ _.str.33
+ _.str.40
+ _.str.41
+ _.str.42
+ _.str.43
+ _.str.45
+ _.str.51
+ _.str.53
+ _.str.56
+ _.str.90
+ _OBJC_CLASS_$_GEOVLFCrowdsourcingDetails
+ _OBJC_CLASS_$_GEOVLFFrameDetails
+ _OBJC_CLASS_$_GEOVLFImagePosition
+ _OBJC_CLASS_$_GEOVLFPoint3D
+ _OBJC_CLASS_$_GEOVLFSLAMTrack
+ _OBJC_CLASS_$_VLLocalizationCrowdsourcingDetails
+ _OBJC_IVAR_$_VLLocalizationCrowdsourcingDetails._resultPoseRotation
+ _OBJC_IVAR_$_VLLocalizationCrowdsourcingDetails._resultPoseTranslation
+ _OBJC_IVAR_$_VLLocalizationCrowdsourcingDetails._statistics
+ _OBJC_IVAR_$_VLLocalizationDebugInfo._crowdsourcingDetails
+ _OBJC_METACLASS_$_VLLocalizationCrowdsourcingDetails
+ __OBJC_$_CATEGORY_GEOVLFCrowdsourcingDetails_$_VisualLocalizationExtras
+ __OBJC_$_CLASS_METHODS_GEOVLFCrowdsourcingDetails(VisualLocalizationExtras)
+ __OBJC_$_CLASS_METHODS_VLLocalizationCrowdsourcingDetails
+ __OBJC_$_CLASS_PROP_LIST_VLLocalizationCrowdsourcingDetails
+ __OBJC_$_INSTANCE_METHODS_VLLocalizationCrowdsourcingDetails
+ __OBJC_$_INSTANCE_VARIABLES_VLLocalizationCrowdsourcingDetails
+ __OBJC_$_PROP_LIST_VLLocalizationCrowdsourcingDetails
+ __OBJC_CLASS_PROTOCOLS_$_VLLocalizationCrowdsourcingDetails
+ __OBJC_CLASS_RO_$_VLLocalizationCrowdsourcingDetails
+ __OBJC_METACLASS_RO_$_VLLocalizationCrowdsourcingDetails
+ ___FUNCTION__.p_scale16_bilinear_ex
+ ___block_descriptor_32_e3911_i40?0^{vl_t={?={?=ii{?=iiifffi}{?=fiiifififfifi}{?=iiifi}ffi}{?=ffi{?=iff}ii}{?=i{?=i}fi}{?=ii}{?=i{?=ifffifiiiiiifi}{?=iffffffiffffiiifiifii[8f]iiiifffifii}{?={?=fffiiiiffffffiQ{?=fff}}fff}{?=i}iffff{?=iffffifi}{?=ii}{?=iii}{?=iii}f}{?=iiiiiiffdffff}{?=iiiii{?=idiifffffff{?=if}{?=ffffff}{?=ii}iii{?=ffffff}{?=iiiiiifffff{?=ffffff}{?=fff}{?=ffffff}ffii{?=fff}}iff{?=ffff}ffii}}{?=iiii}{?=iiii}}i^{?}{?={?=*iiq}{?=idddddddd(?={?=ddd}{?=dddd}{?=ddddd}{?=[12d]}{?=[12d]}{?=[7d]})ii}{g_pos3_t=ddd}ff{?=fff}fff{?=[3[3f]][3f]}{?=[3[3d]][3d]}}[512c]{?=q^{?}q{float_list_t=q^fq}}{vl_kpt3_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{?={?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dog_octave_list_t=q^{?}q}{?={int_pair_list_t=q^{int_pair_t}q}}{?=[3^{lbl_feature2d_t}][512c]ii}^?^vi}{?=ii{g_pos3_t=ddd}f^{?}i[512c]^v^?^{?}{vl_tile_t=iiii}{vl_gnd_t={?=[3[3d]][3d]}dd}^v^{_opaque_pthread_t}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_image_meta_list_t=q^{?}q}{vl_inliers_list_t=q^{?}q}{vl_tile_list_t=q^{vl_tile_t}q}{vl_gnd_list_t=q^{vl_gnd_t}q}{vl_pose_list_t=q^{?}q}{int_list_t=q^iq}iiii}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={int_list_t=q^iq}{?=q^{?}q{float_list_t=q^fq}}}{?={vl_gnd_t={?=[3[3d]][3d]}dd}i{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=ddQ}{?={?=[3[3d]][3d]}^v}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]{?=i{?=[3[3d]][3d]}d[512c]}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_ps_hyp_list_t=q^{?}q}{float_list_t=q^fq}{float_list_t=q^fq}^{vl_pose_fuse_t}{?={?=[3[3d]][3d]}}}{?={_opaque_pthread_mutex_t=q[56c]}ii{vl_context_history_frame_list_t=q^{?}q}}{?={?=[3[3d]][3d]}ii}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=ii^{_opaque_pthread_t}{timespec=qq}i[512c][512c]{_opaque_pthread_mutex_t=q[56c]}{vl_dump_update_data_list_t=q^{?}q}{vl_dump_locate_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dump_kpts_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dump_result_ptr_list_t=q^^{?}q}{?=d{vl_dump_hash_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?=q^{?}q{float_list_t=q^fq}}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{?=[3[3d]][3d]}f{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{vl_gnd_t={?=[3[3d]][3d]}dd}*i}{vl_dump_detail_ptr_list_t=q^^{?}q}{vl_dump_stats_ptr_list_t=q^^{?}q}}^{?}^{?}{?=[3[3d]][3d]f[36f]}{?=di}{?=iiii}}8r^{?=*iii}16r^{?={?=[9f][2f]}{?=[3d]fii}d{?=ff[3f]}{?=[12f]i}}24^{?=[3[3d]][3d]f[36f]}32l
+ ___func__.g_proj_bspline_cnt
+ ___func__.log_to_other_targets_lf
+ ___func__.vl_fio_mkdir2
+ __malloc
+ __realloc
+ _acc
+ _counter_auto_grow
+ _counter_create
+ _counter_free
+ _counter_increment
+ _dash_create
+ _dash_find
+ _dash_find_or_insert
+ _dash_free
+ _dash_insert
+ _dashv_bin_size
+ _dashv_capacity
+ _dashv_create
+ _dashv_find
+ _dashv_find_or_insert
+ _dashv_free
+ _dashv_insert
+ _dashv_n_bins
+ _dashv_resize
+ _dashv_size
+ _double_cmp
+ _fisheye_kannala_inv
+ _g_frame_from_geoc
+ _g_imcam_to_imcam
+ _g_interp_acc_wa
+ _g_interp_bspline3_mix2
+ _g_interp_get_a
+ _g_isect_plane_rayf
+ _g_mat_rot_trans_inv
+ _g_pca3
+ _g_pinhole_to_pixel_jac
+ _g_proj_bspline_cnt
+ _g_proj_bspline_f0f1
+ _g_proj_is_bspline
+ _g_quat_conj
+ _g_quat_from_axisangle
+ _g_quat_mul
+ _g_quat_to_axisangle
+ _int_cmp
+ _levenshtein_distance
+ _log_args_buf
+ _log_console_fmt
+ _log_is_printable
+ _log_to_other_targets_lf
+ _lsq_cholesky_cov
+ _lsq_cholesky_create
+ _lsq_cholesky_free
+ _lsq_cholesky_jac
+ _lsq_cholesky_jac_multi
+ _lsq_cholesky_normcols
+ _lsq_cholesky_solve
+ _mx_chol_create
+ _mx_chol_fact_d
+ _mx_chol_solve
+ _mx_cholesky_solve
+ _mx_dtrtri
+ _mx_lu_create
+ _mx_lu_fact
+ _mx_lu_solve
+ _objc_msgSend$addCalibrationMatrix:
+ _objc_msgSend$addDescriptors:
+ _objc_msgSend$addFrameDetails:
+ _objc_msgSend$addImagePositions:
+ _objc_msgSend$addInlierPoints2D:
+ _objc_msgSend$addInlierPoints3D:
+ _objc_msgSend$addObservationImageIndices:
+ _objc_msgSend$addResultPoseRotation:
+ _objc_msgSend$addSlamOrigin:
+ _objc_msgSend$addSlamPose:
+ _objc_msgSend$addSlamPtsInlierIdx:
+ _objc_msgSend$addSlamTracks:
+ _objc_msgSend$addVioPose:
+ _objc_msgSend$descriptorDimension
+ _objc_msgSend$frameCount
+ _objc_msgSend$initWithStats:resultTransform:
+ _objc_msgSend$inliersCount
+ _objc_msgSend$perFrameCalibrationMatrices
+ _objc_msgSend$perFrameDistortion
+ _objc_msgSend$perFrameVioPoses
+ _objc_msgSend$perFrameVioStatusCodes
+ _objc_msgSend$points2D
+ _objc_msgSend$points3D
+ _objc_msgSend$resultPoseRotation
+ _objc_msgSend$resultPoseTranslation
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setRadialDistortion1:
+ _objc_msgSend$setRadialDistortion2:
+ _objc_msgSend$setResultStatus:
+ _objc_msgSend$setResultTranslationX:
+ _objc_msgSend$setResultTranslationY:
+ _objc_msgSend$setResultTranslationZ:
+ _objc_msgSend$setStartFrameIdx:
+ _objc_msgSend$setTimestamp:
+ _objc_msgSend$setVioStatus:
+ _objc_msgSend$slamOrigin
+ _objc_msgSend$slamTrackDescriptors
+ _objc_msgSend$slamTrackImageIndices
+ _objc_msgSend$slamTrackObservations
+ _objc_msgSend$slamTracks
+ _objc_msgSend$slamTracks2D
+ _objc_msgSend$slamTracksCount
+ _objc_msgSend$statistics
+ _p_clonereff
+ _pf_chsum
+ _pf_chsum16
+ _pf_chsumyv12
+ _pf_resize_rgb
+ _pf_unpack_10to16_s
+ _pp_yv12_to_xrgb_s
+ _pthread_mutex_destroy
+ _ref_count_init
+ _rkd_inside
+ _slam_depth_range_free
+ _store_vkey
+ _stretch2x
+ _string_list_add2
+ _update_history
+ _vDSP_vsadd
+ _vl_context_clear
+ _vl_context_history_add_frame
+ _vl_context_history_clear
+ _vl_context_history_trim
+ _vl_desc_cluster_centroids
+ _vl_desc_cluster_similar
+ _vl_desc_dist_sqr_basic
+ _vl_desc_dist_sqr_k16
+ _vl_dog_clear_octave_list
+ _vl_dump_detail_pose_result
+ _vl_dump_detail_vl_debug
+ _vl_fio_mkdir2
+ _vl_inliers_clone
+ _vl_par_ver_46434
+ _vl_par_ver_46435
+ _vl_par_ver_46436
+ _vl_par_ver_4731
+ _vl_par_ver_4732
+ _vl_par_ver_4733
+ _vl_par_ver_475
+ _vl_par_ver_4751
+ _vl_par_ver_4752
+ _vl_par_ver_480
+ _vl_pose_irefine
+ _vl_printf
+ _vl_t_print
+ _wstr_from_utf8
+ _wstr_is_ascii
+ _wstr_len
+ _wstr_to_utf8
- _.str.22
- _.str.23
- _.str.28
- _.str.30
- _.str.37
- _.str.38
- _.str.44
- _.str.49
- _.str.87
- _IOSurfaceGetBaseAddress
- _IOSurfaceGetBytesPerElement
- _IOSurfaceGetBytesPerRow
- _IOSurfaceLock
- _IOSurfaceUnlock
- ___FUNCTION__.g_ins_get_gravity
- ___FUNCTION__.log_to_other_targets
- ___block_descriptor_32_e3955_i40?0^{vl_t={?={?=ii{?=iiifffi}{?=fiiifififfifi}{?=iiifi}ffi}{?=ffi{?=iff}ii}{?=i{?=i}fi}{?=ii}{?=i{?=ifffifiiiiiifi}{?=iffffffiffffiiifiifii[8f]iiiifffifii}{?={?=fffiiiiffffffiQ{?=fff}}fff}{?=i}iffff{?=iffffi}{?=ii}{?=iii}{?=iii}f}{?=iiiiiiffdffff}{?=iiiii{?=idiifffffff{?=if}{?=ffffff}{?=ii}iii{?=ffffff}{?=iiiiiifffff{?=ffffff}{?=fff}{?=ffffff}ffii{?=iiiff}{?=fff}}iff{?=ffff}ffii}}{?=iiii}}i^{?}{?={?=*iiq}{?=iddddd(?=dd)ddd(?=dd)(?=dd)ii}{g_pos3_t=ddd}ff{?=fff}fff{?=[3[3f]][3f]}{?=[3[3d]][3d]}}[512c]{?=q^{?}q{float_list_t=q^fq}}{vl_kpt3_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{?={?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dog_octave_list_t=q^{?}q}{?={int_pair_list_t=q^{int_pair_t}q}}{?=[3^{lbl_feature2d_t}][512c]ii}^?^vi}{?=ii{g_pos3_t=ddd}f^{?}i[512c]^v^?^{?}{vl_tile_t=iiii}{vl_gnd_t={?=[3[3d]][3d]}dd}^v^{_opaque_pthread_t}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_image_meta_list_t=q^{?}q}{vl_inliers_list_t=q^{?}q}{vl_tile_list_t=q^{vl_tile_t}q}{vl_gnd_list_t=q^{vl_gnd_t}q}{vl_pose_list_t=q^{?}q}{int_list_t=q^iq}iiii}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={int_list_t=q^iq}{?=q^{?}q{float_list_t=q^fq}}}{?={vl_gnd_t={?=[3[3d]][3d]}dd}i{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=ddQ}{?={?=[3[3d]][3d]}^v}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]{?=i{?=[3[3d]][3d]}d[512c]}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_ps_hyp_list_t=q^{?}q}{float_list_t=q^fq}{float_list_t=q^fq}^{vl_pose_fuse_t}{?={?=[3[3d]][3d]}}}{?={?=[3[3d]][3d]}ii}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=ii^{_opaque_pthread_t}{timespec=qq}i[512c][512c]iC{vl_dump_update_data_list_t=q^{?}q}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_locate_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_kpts_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_result_ptr_list_t=q^^{?}q}{_opaque_pthread_mutex_t=q[56c]}{?=d{vl_dump_hash_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?=q^{?}q{float_list_t=q^fq}}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{?=[3[3d]][3d]}f{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{vl_gnd_t={?=[3[3d]][3d]}dd}}{vl_dump_detail_ptr_list_t=q^^{?}q}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_stats_ptr_list_t=q^^{?}q}{_opaque_pthread_mutex_t=q[56c]}}^{?}^{?}{?=[3[3d]][3d]f[36f]}{?=di}{?=iiii}}8r^{?=*iii}16r^{?={?=[9f][2f]}{?=[3d]fii}{?=ff[3f]}{?=[12f]i}}24^{?=[3[3d]][3d]f[36f]}32l
- ___const.p_scale16_bilinear.bbox
- ___func__.g_jac_apply_rotation
- ___func__.g_proj2_to_g_proj
- _bias_prior
- _bon_eval_ins
- _bon_upd_vec
- _dtime_normalize
- _dump_detail_single
- _dump_kpts_single
- _dump_locate_single
- _dump_result_single
- _dump_update_single
- _g_imgnd_z_to_xyz
- _g_ins_get_imu_ypr
- _g_ins_imu_data_find
- _g_ins_integrate
- _g_ins_intg_predict
- _g_ins_predict
- _g_ins_predict_R
- _g_ins_predict_rk4
- _g_ins_trajectory_predict_exact
- _g_ins_trajectory_predict_internal
- _g_rot_trans_mat
- _gen_depth_ranges_isect
- _log10
- _log_msg_every
- _log_to_other_targets
- _lsq_bs_info
- _lsq_jacobian_dense
- _p_scale16_bilinear_ex
- _pf_scale_rgb
- _pthread_mutex_trylock
- _sss_cnt_node
- _sss_hotspots
- _sss_nn
- _tracker_bundle_bon.log_every
- _upd_bias
- _vl_dictionary_compress_delta
- _vl_dictionary_decompress_delta
- _vl_dictionary_free
- _vl_dictionary_load
- _vl_dictionary_read
- _vl_par_ver_46433
CStrings:
+ "\x02\xf0\xf0!\xf0\xf0\xd2"
+ "\n"
+ "    "
+ "      "
+ "        "
+ "          "
+ " {\n"
+ "%s%s %s ="
+ "%s%s %s = %d\n"
+ "%s%s %s = %f\n"
+ "%s%s %s = %u\n"
+ "%s%s %s = *%p\n"
+ "%s: NaN\n"
+ "%sAccepted%s: conf = %s%.04f%s."
+ "%sRejected%s: conf = %s%.04f%s."
+ "%s}\n"
+ "(npar == 8 || npar == 10) && \"A projection must have 0,8, or 10 parameters\""
+ "(pblock->n_par <= 75) && \"eval_jac_col_numerically with n_par > 75\""
+ "*16@0:8"
+ "/Library/Caches/com.apple.xbs/Sources/VisualLocalization/argo/pwin/core/base/g_euclid.c"
+ "/Library/Caches/com.apple.xbs/Sources/VisualLocalization/argo/pwin/core/base/p_geom.c"
+ "/t/"
+ "0 && \"Hash map full\""
+ "0 && \"Not a spline based camera model.\""
+ "0 && \"compile with PWIN_LAPACK to access mx_cholesky_solve\""
+ "0 && \"compile with PWIN_LAPACK to access mx_dgetri\""
+ "@\"VLLocalizationCrowdsourcingDetails\""
+ "@152@0:8@16{?=[4]}24"
+ "@24@0:8r^{?=^d^f^i^s^s[3f]ii^f^fiiiiii^{vl_tile_t}*^{?}^ii[6d]^f*i^f^s^s^f^d^i^f^f^fiiidddddddddddddddddddddddqi}16"
+ "@300@0:8^{__CVBuffer=}16d24d32d40{?=[3d]fii}48@88{?=dd}96112{?=[4]}144{?=[3]}208256d264r^{?=^d^f^i^s^s[3f]ii^f^fiiiiii^{vl_tile_t}*^{?}^ii[6d]^f*i^f^s^s^f^d^i^f^f^fiiidddddddddddddddddddddddqi}272Q280r^{?=[3[3d]][3d]f[36f]}288B296"
+ "ARR_SIZE(J_tmp) >= n_par * 2"
+ "Averaging kernel is taller than image height."
+ "Averaging kernel is wider than image width."
+ "Clustered descriptors: %d => %d (%.1f%%)\n"
+ "Could not open %s to print!"
+ "DDEB"
+ "Dump thread is already running"
+ "Failed to create dir %s"
+ "File %s does not exist"
+ "INPUT inlier  = %s%d%s"
+ "Lens type %d is not implemented!"
+ "Loading model at: %s"
+ "Lt has NaN. C non-invertible or numerical problems?"
+ "Not implemented"
+ "P_SAME_SIZE((im_src), (im_dst)) && \"pf_average only accepts images of same size\""
+ "Sparsified slam tracks: %d => %d (%.1f%%)"
+ "T*,R,N"
+ "T@\"VLLocalizationCrowdsourcingDetails\",R,N,V_crowdsourcingDetails"
+ "T@\"_VLStatistics\",R,N,V_statistics"
+ "T^i,R,N"
+ "T^s,R,N"
+ "T^{?=^d^f^i^s^s[3f]ii^f^fiiiiii^{vl_tile_t}*^{?}^ii[6d]^f*i^f^s^s^f^d^i^f^f^fiiidddddddddddddddddddddddqi},R,N"
+ "There are still %d detail to dump."
+ "There are still %d kpts to dump."
+ "There are still %d locates to dump."
+ "There are still %d result to dump."
+ "There are still %d stats to dump."
+ "There are still %d update to dump."
+ "Unexpected stats file ver: %d, %s"
+ "Updated dump path to: %s"
+ "VLLocalizationCrowdsourcingDetails"
+ "[3[3d]]"
+ "[3d]"
+ "^s16@0:8"
+ "^{?=^d^f^i^s^s[3f]ii^f^fiiiiii^{vl_tile_t}*^{?}^ii[6d]^f*i^f^s^s^f^d^i^f^f^fiiidddddddddddddddddddddddqi}16@0:8"
+ "^{vl_t={?={?=ii{?=iiifffi}{?=fiiifififfifi}{?=iiifi}ffi}{?=ffi{?=iff}ii}{?=i{?=i}fi}{?=ii}{?=i{?=ifffifiiiiiifi}{?=iffffffiffffiiifiifii[8f]iiiifffifii}{?={?=fffiiiiffffffiQ{?=fff}}fff}{?=i}iffff{?=iffffifi}{?=ii}{?=iii}{?=iii}f}{?=iiiiiiffdffff}{?=iiiii{?=idiifffffff{?=if}{?=ffffff}{?=ii}iii{?=ffffff}{?=iiiiiifffff{?=ffffff}{?=fff}{?=ffffff}ffii{?=fff}}iff{?=ffff}ffii}}{?=iiii}{?=iiii}}i^{?}{?={?=*iiq}{?=idddddddd(?={?=ddd}{?=dddd}{?=ddddd}{?=[12d]}{?=[12d]}{?=[7d]})ii}{g_pos3_t=ddd}ff{?=fff}fff{?=[3[3f]][3f]}{?=[3[3d]][3d]}}[512c]{?=q^{?}q{float_list_t=q^fq}}{vl_kpt3_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{?={?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dog_octave_list_t=q^{?}q}{?={int_pair_list_t=q^{int_pair_t}q}}{?=[3^{lbl_feature2d_t}][512c]ii}^?^vi}{?=ii{g_pos3_t=ddd}f^{?}i[512c]^v^?^{?}{vl_tile_t=iiii}{vl_gnd_t={?=[3[3d]][3d]}dd}^v^{_opaque_pthread_t}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_image_meta_list_t=q^{?}q}{vl_inliers_list_t=q^{?}q}{vl_tile_list_t=q^{vl_tile_t}q}{vl_gnd_list_t=q^{vl_gnd_t}q}{vl_pose_list_t=q^{?}q}{int_list_t=q^iq}iiii}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={int_list_t=q^iq}{?=q^{?}q{float_list_t=q^fq}}}{?={vl_gnd_t={?=[3[3d]][3d]}dd}i{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=ddQ}{?={?=[3[3d]][3d]}^v}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]{?=i{?=[3[3d]][3d]}d[512c]}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_ps_hyp_list_t=q^{?}q}{float_list_t=q^fq}{float_list_t=q^fq}^{vl_pose_fuse_t}{?={?=[3[3d]][3d]}}}{?={_opaque_pthread_mutex_t=q[56c]}ii{vl_context_history_frame_list_t=q^{?}q}}{?={?=[3[3d]][3d]}ii}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=ii^{_opaque_pthread_t}{timespec=qq}i[512c][512c]{_opaque_pthread_mutex_t=q[56c]}{vl_dump_update_data_list_t=q^{?}q}{vl_dump_locate_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dump_kpts_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dump_result_ptr_list_t=q^^{?}q}{?=d{vl_dump_hash_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?=q^{?}q{float_list_t=q^fq}}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{?=[3[3d]][3d]}f{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{vl_gnd_t={?=[3[3d]][3d]}dd}*i}{vl_dump_detail_ptr_list_t=q^^{?}q}{vl_dump_stats_ptr_list_t=q^^{?}q}}^{?}^{?}{?=[3[3d]][3d]f[36f]}{?=di}{?=iiii}}"
+ "^{vl_t={?={?=ii{?=iiifffi}{?=fiiifififfifi}{?=iiifi}ffi}{?=ffi{?=iff}ii}{?=i{?=i}fi}{?=ii}{?=i{?=ifffifiiiiiifi}{?=iffffffiffffiiifiifii[8f]iiiifffifii}{?={?=fffiiiiffffffiQ{?=fff}}fff}{?=i}iffff{?=iffffifi}{?=ii}{?=iii}{?=iii}f}{?=iiiiiiffdffff}{?=iiiii{?=idiifffffff{?=if}{?=ffffff}{?=ii}iii{?=ffffff}{?=iiiiiifffff{?=ffffff}{?=fff}{?=ffffff}ffii{?=fff}}iff{?=ffff}ffii}}{?=iiii}{?=iiii}}i^{?}{?={?=*iiq}{?=idddddddd(?={?=ddd}{?=dddd}{?=ddddd}{?=[12d]}{?=[12d]}{?=[7d]})ii}{g_pos3_t=ddd}ff{?=fff}fff{?=[3[3f]][3f]}{?=[3[3d]][3d]}}[512c]{?=q^{?}q{float_list_t=q^fq}}{vl_kpt3_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{?={?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dog_octave_list_t=q^{?}q}{?={int_pair_list_t=q^{int_pair_t}q}}{?=[3^{lbl_feature2d_t}][512c]ii}^?^vi}{?=ii{g_pos3_t=ddd}f^{?}i[512c]^v^?^{?}{vl_tile_t=iiii}{vl_gnd_t={?=[3[3d]][3d]}dd}^v^{_opaque_pthread_t}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_image_meta_list_t=q^{?}q}{vl_inliers_list_t=q^{?}q}{vl_tile_list_t=q^{vl_tile_t}q}{vl_gnd_list_t=q^{vl_gnd_t}q}{vl_pose_list_t=q^{?}q}{int_list_t=q^iq}iiii}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={int_list_t=q^iq}{?=q^{?}q{float_list_t=q^fq}}}{?={vl_gnd_t={?=[3[3d]][3d]}dd}i{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=ddQ}{?={?=[3[3d]][3d]}^v}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]{?=i{?=[3[3d]][3d]}d[512c]}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_ps_hyp_list_t=q^{?}q}{float_list_t=q^fq}{float_list_t=q^fq}^{vl_pose_fuse_t}{?={?=[3[3d]][3d]}}}{?={_opaque_pthread_mutex_t=q[56c]}ii{vl_context_history_frame_list_t=q^{?}q}}{?={?=[3[3d]][3d]}ii}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=ii^{_opaque_pthread_t}{timespec=qq}i[512c][512c]{_opaque_pthread_mutex_t=q[56c]}{vl_dump_update_data_list_t=q^{?}q}{vl_dump_locate_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dump_kpts_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dump_result_ptr_list_t=q^^{?}q}{?=d{vl_dump_hash_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?=q^{?}q{float_list_t=q^fq}}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{?=[3[3d]][3d]}f{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{vl_gnd_t={?=[3[3d]][3d]}dd}*i}{vl_dump_detail_ptr_list_t=q^^{?}q}{vl_dump_stats_ptr_list_t=q^^{?}q}}^{?}^{?}{?=[3[3d]][3d]f[36f]}{?=di}{?=iiii}}16@0:8"
+ "_crowdsourcingDetails"
+ "_malloc_page"
+ "_resultPoseRotation"
+ "_resultPoseTranslation"
+ "_vl_createWithVLCrowdsourcingDetails:"
+ "addCalibrationMatrix:"
+ "addDescriptors:"
+ "addFrameDetails:"
+ "addImagePositions:"
+ "addInlierPoints2D:"
+ "addInlierPoints3D:"
+ "addObservationImageIndices:"
+ "addResultPoseRotation:"
+ "addSlamOrigin:"
+ "addSlamPose:"
+ "addSlamPtsInlierIdx:"
+ "addSlamTracks:"
+ "addVioPose:"
+ "base_path[0] != 0"
+ "best_frame >= 0"
+ "cell_size_xy"
+ "cell_size_z"
+ "cell_split_factor_xy"
+ "cell_split_factor_z"
+ "contrast_threshold"
+ "counter.c"
+ "counter_increment"
+ "crowdsourcingDetails"
+ "da_size(&frames) <= vl->par.history.stats_max_frames"
+ "dash.c"
+ "dash_find_or_insert"
+ "dash_insert"
+ "dashv_find"
+ "dashv_find_or_insert"
+ "dashv_insert"
+ "data_version"
+ "debug_print_level"
+ "desc_method"
+ "descriptorDimension"
+ "det_thr"
+ "detect_method"
+ "early_out_th"
+ "edge_threshold"
+ "enabled"
+ "err == 0 && \"Could not acquire lock of targets variable. Has log been initialized?\""
+ "err == 0 && \"Could not release log lock\""
+ "espressos/lbl2d_v5.mlmodelc"
+ "eval_jac_col_numerically"
+ "fix this case if needed"
+ "flg"
+ "float"
+ "float[8]"
+ "frameCount"
+ "g_interp.c"
+ "g_interp_acc_wa"
+ "g_interp_get_a"
+ "g_pca3"
+ "g_pinhole_to_pixel_jac"
+ "g_proj_bspline_cnt"
+ "g_ps"
+ "g_ps_par"
+ "g_ps_par_t"
+ "grav_thr"
+ "grav_uncertainty"
+ "height_th"
+ "human_offset"
+ "i != i_initial && \"Counter hash table is full.\""
+ "i40@?0^{vl_t={?={?=ii{?=iiifffi}{?=fiiifififfifi}{?=iiifi}ffi}{?=ffi{?=iff}ii}{?=i{?=i}fi}{?=ii}{?=i{?=ifffifiiiiiifi}{?=iffffffiffffiiifiifii[8f]iiiifffifii}{?={?=fffiiiiffffffiQ{?=fff}}fff}{?=i}iffff{?=iffffifi}{?=ii}{?=iii}{?=iii}f}{?=iiiiiiffdffff}{?=iiiii{?=idiifffffff{?=if}{?=ffffff}{?=ii}iii{?=ffffff}{?=iiiiiifffff{?=ffffff}{?=fff}{?=ffffff}ffii{?=fff}}iff{?=ffff}ffii}}{?=iiii}{?=iiii}}i^{?}{?={?=*iiq}{?=idddddddd(?={?=ddd}{?=dddd}{?=ddddd}{?=[12d]}{?=[12d]}{?=[7d]})ii}{g_pos3_t=ddd}ff{?=fff}fff{?=[3[3f]][3f]}{?=[3[3d]][3d]}}[512c]{?=q^{?}q{float_list_t=q^fq}}{vl_kpt3_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{?={?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dog_octave_list_t=q^{?}q}{?={int_pair_list_t=q^{int_pair_t}q}}{?=[3^{lbl_feature2d_t}][512c]ii}^?^vi}{?=ii{g_pos3_t=ddd}f^{?}i[512c]^v^?^{?}{vl_tile_t=iiii}{vl_gnd_t={?=[3[3d]][3d]}dd}^v^{_opaque_pthread_t}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_image_meta_list_t=q^{?}q}{vl_inliers_list_t=q^{?}q}{vl_tile_list_t=q^{vl_tile_t}q}{vl_gnd_list_t=q^{vl_gnd_t}q}{vl_pose_list_t=q^{?}q}{int_list_t=q^iq}iiii}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={int_list_t=q^iq}{?=q^{?}q{float_list_t=q^fq}}}{?={vl_gnd_t={?=[3[3d]][3d]}dd}i{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=ddQ}{?={?=[3[3d]][3d]}^v}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]{?=i{?=[3[3d]][3d]}d[512c]}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_ps_hyp_list_t=q^{?}q}{float_list_t=q^fq}{float_list_t=q^fq}^{vl_pose_fuse_t}{?={?=[3[3d]][3d]}}}{?={_opaque_pthread_mutex_t=q[56c]}ii{vl_context_history_frame_list_t=q^{?}q}}{?={?=[3[3d]][3d]}ii}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=ii^{_opaque_pthread_t}{timespec=qq}i[512c][512c]{_opaque_pthread_mutex_t=q[56c]}{vl_dump_update_data_list_t=q^{?}q}{vl_dump_locate_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dump_kpts_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dump_result_ptr_list_t=q^^{?}q}{?=d{vl_dump_hash_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?=q^{?}q{float_list_t=q^fq}}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{?=[3[3d]][3d]}f{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{vl_gnd_t={?=[3[3d]][3d]}dd}*i}{vl_dump_detail_ptr_list_t=q^^{?}q}{vl_dump_stats_ptr_list_t=q^^{?}q}}^{?}^{?}{?=[3[3d]][3d]f[36f]}{?=di}{?=iiii}}8r^{?=*iii}16r^{?={?=[9f][2f]}{?=[3d]fii}d{?=ff[3f]}{?=[12f]i}}24^{?=[3[3d]][3d]f[36f]}32"
+ "idx >= 0 && \"No negative indexes allowed\""
+ "image_boundary"
+ "initWithStats:resultTransform:"
+ "inlier_thr"
+ "int"
+ "isfinite(slam_pt3s[i])"
+ "isfinite(slam_tracks[i*2+0])"
+ "k < (1U << 31) && \"Too many/long keys\""
+ "key != COUNTER_UNUSED_KEY"
+ "knn_prior"
+ "kpt"
+ "lbl_filter_ddist"
+ "lbl_filter_dist"
+ "lbl_par"
+ "lbl_version"
+ "len > 0 && len < 256 && \"Invalid key length\""
+ "load_ddir"
+ "log_to_other_targets_lf"
+ "lowe_lt_th"
+ "lowe_prio"
+ "lowe_th"
+ "map"
+ "match"
+ "matches_lim"
+ "max_hyps"
+ "max_kpts_octave"
+ "max_n_kpts"
+ "max_time_ms"
+ "method"
+ "min_inlier"
+ "min_inliers"
+ "mkdir %s"
+ "mn"
+ "multi_img"
+ "mx"
+ "mx_chol_fact_d"
+ "mx_cholesky_solve"
+ "mx_dtrtri"
+ "mx_lapack.c"
+ "n_i == slam_tracks_len[i]"
+ "n_iter"
+ "n_keep_refine"
+ "n_kpts"
+ "n_lev_refine"
+ "n_model"
+ "n_model_brute"
+ "n_octave_layers"
+ "n_octaves"
+ "n_octaves_layers"
+ "n_par == k_size + 6 && \"par size wrong\""
+ "n_regions"
+ "n_sol_refine"
+ "n_split_steps"
+ "n_test"
+ "n_test_sub"
+ "n_tracks == vl_stats->num_slam_pt3s"
+ "nms_radius"
+ "nn"
+ "ori_sigma_fac"
+ "ori_th"
+ "orientation_nbins"
+ "orientation_radius"
+ "orientation_threshold"
+ "orientation_weight"
+ "p_scale16_bilinear_ex"
+ "p_th"
+ "par"
+ "par_dog"
+ "par_sift"
+ "par_sss"
+ "perFrameCalibrationMatrices"
+ "perFrameDistortion"
+ "perFrameVioPoses"
+ "perFrameVioStatusCodes"
+ "pf_average16"
+ "pf_averagef"
+ "post_filter_radius"
+ "quantize"
+ "radius_init"
+ "ransac"
+ "rebuild_dist_thr"
+ "refine"
+ "refine_comp"
+ "region_r"
+ "reproj_th"
+ "res_xy"
+ "res_z"
+ "resultPoseRotation"
+ "resultPoseTranslation"
+ "retrieval"
+ "run_simplified"
+ "s_test_sub"
+ "scaled_width"
+ "score"
+ "setPosition:"
+ "setRadialDistortion1:"
+ "setRadialDistortion2:"
+ "setResultStatus:"
+ "setResultTranslationX:"
+ "setResultTranslationY:"
+ "setResultTranslationZ:"
+ "setStartFrameIdx:"
+ "setTimestamp:"
+ "setVioStatus:"
+ "sigma"
+ "size_th"
+ "sizeof(page_t) == 3 * sizeof(dash_ki_t) && !((uint64_t)mem & 1)"
+ "slamOrigin"
+ "slamTrackDescriptors"
+ "slamTrackImageIndices"
+ "slamTrackObservations"
+ "slamTracks"
+ "slamTracks2D"
+ "slamTracksCount"
+ "slam_tracks_img_idx[i] >= 0 && slam_tracks_img_idx[i] < stats->num_frames"
+ "slam_tracks_len[i] > 0"
+ "split_comp"
+ "stats->slam_tracks_img_idx[i] < stats->num_frames"
+ "stats->slam_tracks_img_idx[i] >= 0"
+ "step_brute"
+ "store_vkey"
+ "struct (unnamed)"
+ "struct vl_t"
+ "thr"
+ "topk"
+ "track dedupe: %.1f ms"
+ "txt"
+ "upscale"
+ "use_learned_confidence"
+ "use_ori_prior"
+ "use_pose_refine"
+ "use_vote_prio"
+ "validate_dist_thr"
+ "ver"
+ "view_angle_th"
+ "vl_dog_par_t"
+ "vl_dump_update_path"
+ "vl_fio_mkdir2"
+ "vl_kpts_desc_method_t"
+ "vl_kpts_detect_method_t"
+ "vl_match_method_t"
+ "vl_par_kpt_lbl_t"
+ "vl_par_kpt_ocv_sift_t"
+ "vl_par_kpt_t"
+ "vl_par_map_t"
+ "vl_par_match_sss_t"
+ "vl_par_match_t"
+ "vl_par_pose_g_ps_par_t"
+ "vl_par_pose_ransac_t"
+ "vl_par_pose_score_t"
+ "vl_par_pose_t"
+ "vl_par_retrieval_t"
+ "vl_par_t"
+ "vl_pose output"
+ "vl_pose_method_t"
+ "vl_stats_get_from_history"
+ "vl_stats_get_from_history_frames"
+ "vl_stats_pick_frames"
+ "vl_stats_rebuild_slam_tracks"
+ "{?=\"points3d\"^d\"points2d\"^f\"inlier_indices\"^i\"inlier_number\"^s\"slam_pt3s_inlier_idx\"^s\"gravity\"[3f]\"localized\"i\"status_ps\"i\"solver_conf\"^f\"fused_conf\"^f\"num_confs\"i\"num_inliers_gt\"i\"num_inliers\"i\"num_keypoints\"i\"num_tracks\"i\"num_matches\"i\"tile\"^{vl_tile_t}\"uuid\"*\"result_poses\"^{?}\"result_status\"^i\"num_frames\"i\"slam_origin\"[6d]\"slam_pt3s\"^f\"slam_pt3_desc\"*\"desc_dim\"i\"slam_tracks\"^f\"slam_tracks_img_idx\"^s\"slam_tracks_len\"^s\"slam_poses\"^f\"slam_time_stamps\"^d\"vio_status\"^i\"vio_poses\"^f\"K\"^f\"distortion\"^f\"slam_keyframe\"i\"num_slam_pt3s\"i\"start_frame\"i\"t_kpts\"d\"t_kpts_pyr\"d\"t_kpts_det\"d\"t_kpts_model\"d\"t_kpts_desc\"d\"t_load\"d\"t_index\"d\"t_pca\"d\"t_match\"d\"t_match_sss\"d\"t_match_filter\"d\"t_slam_tracker\"d\"t_pose\"d\"t_pose_score_filter\"d\"t_pose_score_vote\"d\"t_pose_score_find_peak\"d\"t_pose_score_refine\"d\"t_pose_score_other\"d\"t_pose_score\"d\"t_pose_ransac\"d\"t_pose_referee\"d\"t_pose_fuse\"d\"t_total\"d\"tracks_file_size\"q\"peak_mem_usage\"i}"
- "\x02\xf0\xf0!\xf0\xf0\xd1"
- " (%lld lines skipped since last log)"
- "%d points and %d matches removed"
- "%d. Computed step dx didn't decrease error (new: %f, old: %f). dx = dx/2.\n"
- "%d. Interval search has failed - current rms(%.8f) is still greater than previous rms(%.8f)"
- "%d. Max damping reached: %f\n. Exiting."
- "%d. RMS error: %.8f, |g|: %.10f \n"
- "%d. RMS error: %f -> %f, |g|: %f, damping: %f\n"
- "%d/%d(%.2f%%) imu intervals has a larger diff of 1e-5s, max is %f"
- "%s : "
- "%s: Jacobian of inverse is not implemented"
- "%s: No terms in optimization, skipping"
- "%s: No tracks to optimize"
- "%s: failed"
- "%s:%u: %s: Assertion `%s' failed.\n"
- "%sRejected%s: conf = %s%.02f%s."
- "(n_par <=6 ) && \"jac_apply euclidean for now only works with jacobians that have not more than 6 columns\""
- "--------- \n"
- "/Library/Caches/com.apple.xbs/Sources/VisualLocalization/argo/pwin/core/containers/ccs.c"
- "/Library/Caches/com.apple.xbs/Sources/VisualLocalization/argo/pwin/core/util/huff_coder.c"
- "@24@0:8r^{?=^d^f^i^s^s[3f]ii^f^fiiiii^{vl_tile_t}*^{?}^ii[6d]^f*i^f^s^s^f^d^i^f^f^fiiidddddddddddddddddddddddqi}16"
- "@300@0:8^{__CVBuffer=}16d24d32d40{?=[3d]fii}48@88{?=dd}96112{?=[4]}144{?=[3]}208256d264r^{?=^d^f^i^s^s[3f]ii^f^fiiiii^{vl_tile_t}*^{?}^ii[6d]^f*i^f^s^s^f^d^i^f^f^fiiidddddddddddddddddddddddqi}272Q280r^{?=[3[3d]][3d]f[36f]}288B296"
- "BON: RMSE {%6.4f for %d tracks, %6.4f for %d constraints}"
- "Could not acquire lock of targets variable. Has log been initialized?"
- "Could not release log lock"
- "Error: SSS cannot find k-nearest neighboors"
- "Failed IMU at %f"
- "Failed to lerp imu at time %fs in [%f, %f], using closest one"
- "Final statistics after completion"
- "Finished due hitting maxiter. Iteration %i/%i"
- "Finished due to being below tolerance. (%f < %f). Iteration %i/%i"
- "Finished due to zero length gradient in iteration: %i/%i"
- "Has converged because current gradient norm(%.8f) is less than tolerance(%.8f)"
- "Initialising lsq problem"
- "M x N = %10d x %10d"
- "Normalizing rotation matrices"
- "Number of iterations(%d) has equaled max iterations(%d). Will not optimize further"
- "P"
- "Pos not given, predicted: %f %f %f  %f %f %f"
- "Ran BON solver with rmse:%f (%f) "
- "Something wrong with timestamp"
- "T^{?=^d^f^i^s^s[3f]ii^f^fiiiii^{vl_tile_t}*^{?}^ii[6d]^f*i^f^s^s^f^d^i^f^f^fiiidddddddddddddddddddddddqi},R,N"
- "Tot time: %f ms Tot time linearize: %f ms Tot time solve: %f ms\n"
- "Tot time: %f ms Tot time linearize: %f ms Tot time solve: %f ms Tot time rms: %f ms Time other: %f ms\n"
- "U"
- "Unexpect stats file ver: %d, %s"
- "V"
- "VLDC"
- "W"
- "^{?=^d^f^i^s^s[3f]ii^f^fiiiii^{vl_tile_t}*^{?}^ii[6d]^f*i^f^s^s^f^d^i^f^f^fiiidddddddddddddddddddddddqi}16@0:8"
- "^{vl_t={?={?=ii{?=iiifffi}{?=fiiifififfifi}{?=iiifi}ffi}{?=ffi{?=iff}ii}{?=i{?=i}fi}{?=ii}{?=i{?=ifffifiiiiiifi}{?=iffffffiffffiiifiifii[8f]iiiifffifii}{?={?=fffiiiiffffffiQ{?=fff}}fff}{?=i}iffff{?=iffffi}{?=ii}{?=iii}{?=iii}f}{?=iiiiiiffdffff}{?=iiiii{?=idiifffffff{?=if}{?=ffffff}{?=ii}iii{?=ffffff}{?=iiiiiifffff{?=ffffff}{?=fff}{?=ffffff}ffii{?=iiiff}{?=fff}}iff{?=ffff}ffii}}{?=iiii}}i^{?}{?={?=*iiq}{?=iddddd(?=dd)ddd(?=dd)(?=dd)ii}{g_pos3_t=ddd}ff{?=fff}fff{?=[3[3f]][3f]}{?=[3[3d]][3d]}}[512c]{?=q^{?}q{float_list_t=q^fq}}{vl_kpt3_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{?={?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dog_octave_list_t=q^{?}q}{?={int_pair_list_t=q^{int_pair_t}q}}{?=[3^{lbl_feature2d_t}][512c]ii}^?^vi}{?=ii{g_pos3_t=ddd}f^{?}i[512c]^v^?^{?}{vl_tile_t=iiii}{vl_gnd_t={?=[3[3d]][3d]}dd}^v^{_opaque_pthread_t}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_image_meta_list_t=q^{?}q}{vl_inliers_list_t=q^{?}q}{vl_tile_list_t=q^{vl_tile_t}q}{vl_gnd_list_t=q^{vl_gnd_t}q}{vl_pose_list_t=q^{?}q}{int_list_t=q^iq}iiii}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={int_list_t=q^iq}{?=q^{?}q{float_list_t=q^fq}}}{?={vl_gnd_t={?=[3[3d]][3d]}dd}i{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=ddQ}{?={?=[3[3d]][3d]}^v}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]{?=i{?=[3[3d]][3d]}d[512c]}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_ps_hyp_list_t=q^{?}q}{float_list_t=q^fq}{float_list_t=q^fq}^{vl_pose_fuse_t}{?={?=[3[3d]][3d]}}}{?={?=[3[3d]][3d]}ii}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=ii^{_opaque_pthread_t}{timespec=qq}i[512c][512c]iC{vl_dump_update_data_list_t=q^{?}q}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_locate_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_kpts_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_result_ptr_list_t=q^^{?}q}{_opaque_pthread_mutex_t=q[56c]}{?=d{vl_dump_hash_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?=q^{?}q{float_list_t=q^fq}}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{?=[3[3d]][3d]}f{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{vl_gnd_t={?=[3[3d]][3d]}dd}}{vl_dump_detail_ptr_list_t=q^^{?}q}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_stats_ptr_list_t=q^^{?}q}{_opaque_pthread_mutex_t=q[56c]}}^{?}^{?}{?=[3[3d]][3d]f[36f]}{?=di}{?=iiii}}"
- "^{vl_t={?={?=ii{?=iiifffi}{?=fiiifififfifi}{?=iiifi}ffi}{?=ffi{?=iff}ii}{?=i{?=i}fi}{?=ii}{?=i{?=ifffifiiiiiifi}{?=iffffffiffffiiifiifii[8f]iiiifffifii}{?={?=fffiiiiffffffiQ{?=fff}}fff}{?=i}iffff{?=iffffi}{?=ii}{?=iii}{?=iii}f}{?=iiiiiiffdffff}{?=iiiii{?=idiifffffff{?=if}{?=ffffff}{?=ii}iii{?=ffffff}{?=iiiiiifffff{?=ffffff}{?=fff}{?=ffffff}ffii{?=iiiff}{?=fff}}iff{?=ffff}ffii}}{?=iiii}}i^{?}{?={?=*iiq}{?=iddddd(?=dd)ddd(?=dd)(?=dd)ii}{g_pos3_t=ddd}ff{?=fff}fff{?=[3[3f]][3f]}{?=[3[3d]][3d]}}[512c]{?=q^{?}q{float_list_t=q^fq}}{vl_kpt3_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{?={?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dog_octave_list_t=q^{?}q}{?={int_pair_list_t=q^{int_pair_t}q}}{?=[3^{lbl_feature2d_t}][512c]ii}^?^vi}{?=ii{g_pos3_t=ddd}f^{?}i[512c]^v^?^{?}{vl_tile_t=iiii}{vl_gnd_t={?=[3[3d]][3d]}dd}^v^{_opaque_pthread_t}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_image_meta_list_t=q^{?}q}{vl_inliers_list_t=q^{?}q}{vl_tile_list_t=q^{vl_tile_t}q}{vl_gnd_list_t=q^{vl_gnd_t}q}{vl_pose_list_t=q^{?}q}{int_list_t=q^iq}iiii}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={int_list_t=q^iq}{?=q^{?}q{float_list_t=q^fq}}}{?={vl_gnd_t={?=[3[3d]][3d]}dd}i{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=ddQ}{?={?=[3[3d]][3d]}^v}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]{?=i{?=[3[3d]][3d]}d[512c]}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_ps_hyp_list_t=q^{?}q}{float_list_t=q^fq}{float_list_t=q^fq}^{vl_pose_fuse_t}{?={?=[3[3d]][3d]}}}{?={?=[3[3d]][3d]}ii}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=ii^{_opaque_pthread_t}{timespec=qq}i[512c][512c]iC{vl_dump_update_data_list_t=q^{?}q}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_locate_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_kpts_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_result_ptr_list_t=q^^{?}q}{_opaque_pthread_mutex_t=q[56c]}{?=d{vl_dump_hash_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?=q^{?}q{float_list_t=q^fq}}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{?=[3[3d]][3d]}f{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{vl_gnd_t={?=[3[3d]][3d]}dd}}{vl_dump_detail_ptr_list_t=q^^{?}q}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_stats_ptr_list_t=q^^{?}q}{_opaque_pthread_mutex_t=q[56c]}}^{?}^{?}{?=[3[3d]][3d]f[36f]}{?=di}{?=iiii}}16@0:8"
- "add_imu_term"
- "bs_cgls"
- "cgls iterations: %d\n"
- "data_i.dt >= 0"
- "g_ins_get_imu_ypr"
- "g_ins_imu_data_set_interval"
- "g_ins_integrate"
- "g_ins_state_apply_lever_arm"
- "g_ins_trajectory_predict_exact"
- "g_ins_trajectory_predict_internal"
- "g_jac_apply_inverse_rotation"
- "g_jac_apply_rotation"
- "g_len3(&ya) > 1e-5 && \"fix this case if needed\""
- "get_basis_from_z"
- "huff_dp_cost: cost: %f, max_bits: %d\n"
- "huff_length_limited"
- "i40@?0^{vl_t={?={?=ii{?=iiifffi}{?=fiiifififfifi}{?=iiifi}ffi}{?=ffi{?=iff}ii}{?=i{?=i}fi}{?=ii}{?=i{?=ifffifiiiiiifi}{?=iffffffiffffiiifiifii[8f]iiiifffifii}{?={?=fffiiiiffffffiQ{?=fff}}fff}{?=i}iffff{?=iffffi}{?=ii}{?=iii}{?=iii}f}{?=iiiiiiffdffff}{?=iiiii{?=idiifffffff{?=if}{?=ffffff}{?=ii}iii{?=ffffff}{?=iiiiiifffff{?=ffffff}{?=fff}{?=ffffff}ffii{?=iiiff}{?=fff}}iff{?=ffff}ffii}}{?=iiii}}i^{?}{?={?=*iiq}{?=iddddd(?=dd)ddd(?=dd)(?=dd)ii}{g_pos3_t=ddd}ff{?=fff}fff{?=[3[3f]][3f]}{?=[3[3d]][3d]}}[512c]{?=q^{?}q{float_list_t=q^fq}}{vl_kpt3_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{?={?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_dog_octave_list_t=q^{?}q}{?={int_pair_list_t=q^{int_pair_t}q}}{?=[3^{lbl_feature2d_t}][512c]ii}^?^vi}{?=ii{g_pos3_t=ddd}f^{?}i[512c]^v^?^{?}{vl_tile_t=iiii}{vl_gnd_t={?=[3[3d]][3d]}dd}^v^{_opaque_pthread_t}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_image_meta_list_t=q^{?}q}{vl_inliers_list_t=q^{?}q}{vl_tile_list_t=q^{vl_tile_t}q}{vl_gnd_list_t=q^{vl_gnd_t}q}{vl_pose_list_t=q^{?}q}{int_list_t=q^iq}iiii}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={int_list_t=q^iq}{?=q^{?}q{float_list_t=q^fq}}}{?={vl_gnd_t={?=[3[3d]][3d]}dd}i{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{?=ddQ}{?={?=[3[3d]][3d]}^v}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}[512c]{?=i{?=[3[3d]][3d]}d[512c]}}{?={?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{vl_ps_hyp_list_t=q^{?}q}{float_list_t=q^fq}{float_list_t=q^fq}^{vl_pose_fuse_t}{?={?=[3[3d]][3d]}}}{?={?=[3[3d]][3d]}ii}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}}{?=ii^{_opaque_pthread_t}{timespec=qq}i[512c][512c]iC{vl_dump_update_data_list_t=q^{?}q}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_locate_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_kpts_ptr_list_t=q^^{?}q}{?=[3{timespec=qq}][3{timespec=qq}][3q][3q]i[64c]i}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_result_ptr_list_t=q^^{?}q}{_opaque_pthread_mutex_t=q[56c]}{?=d{vl_dump_hash_list_t=q^{?}q}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{?=q^{?}q{float_list_t=q^fq}}{?={int_nn_list_t=q^[2i]q}{float_nn_list_t=q^[2f]q}}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{g_coords_list_t=q^{?}q}{float_list_t=q^fq}{?=[3[3d]][3d]}f{?={g_pos2f_list_t=q^{?}q}{g_pos3f_list_t=q^{?}q}{int_pair_list_t=q^{int_pair_t}q}i}{vl_gnd_t={?=[3[3d]][3d]}dd}}{vl_dump_detail_ptr_list_t=q^^{?}q}{_opaque_pthread_mutex_t=q[56c]}{vl_dump_stats_ptr_list_t=q^^{?}q}{_opaque_pthread_mutex_t=q[56c]}}^{?}^{?}{?=[3[3d]][3d]f[36f]}{?=di}{?=iiii}}8r^{?=*iii}16r^{?={?=[9f][2f]}{?=[3d]fii}{?=ff[3f]}{?=[12f]i}}24^{?=[3[3d]][3d]f[36f]}32"
- "idx0 < n_samples"
- "idx1 < n_samples"
- "idx1 >= idx0"
- "imu_i.dt > 0"
- "intg->delta_time > 0"
- "iteration %d, relative residual %f, log rel ne-residual %f"
- "log_to_other_targets"
- "lsq_bs_info"
- "lsq_bsolve_add_damping: %f ms \n"
- "lsq_bsolve_cg %3d: rel err = %f"
- "lsq_bsolve_cg finished after %d iterations: r = %f -> %f (rsmin = %f) \n"
- "lsq_bsolve_cg: %f ms \n"
- "lsq_bsolve_invert_V: %f ms \n"
- "lsq_bsolve_ne"
- "lsq_solve: nblocks = %d nterms = %d jac = %d x %d nnz = %d"
- "lsq_solve_levenberg_marquardt"
- "lsq_solve_linear: rmse = %f \n"
- "m x n = %10d x %10d"
- "mem: %f MB \n"
- "nnz / (m x n) = %f"
- "nnz = %zu \n"
- "predict_imu"
- "s0 not covered by imu"
- "s1 not covered by imu"
- "term_index > n_imu"
- "vl_dump already running"
- "{?=\"points3d\"^d\"points2d\"^f\"inlier_indices\"^i\"inlier_number\"^s\"slam_pt3s_inlier_idx\"^s\"gravity\"[3f]\"localized\"i\"status_ps\"i\"solver_conf\"^f\"fused_conf\"^f\"num_confs\"i\"num_inliers\"i\"num_keypoints\"i\"num_tracks\"i\"num_matches\"i\"tile\"^{vl_tile_t}\"uuid\"*\"result_poses\"^{?}\"result_status\"^i\"num_frame\"i\"slam_origin\"[6d]\"slam_pt3s\"^f\"slam_pt3_desc\"*\"desc_dim\"i\"slam_tracks\"^f\"slam_tracks_img_idx\"^s\"slam_tracks_len\"^s\"slam_poses\"^f\"slam_time_stamps\"^d\"vio_status\"^i\"vio_poses\"^f\"K\"^f\"distortion\"^f\"slam_keyframe\"i\"num_slam_pt3s\"i\"start_frame\"i\"t_kpts\"d\"t_kpts_pyr\"d\"t_kpts_det\"d\"t_kpts_model\"d\"t_kpts_desc\"d\"t_load\"d\"t_index\"d\"t_pca\"d\"t_match\"d\"t_match_sss\"d\"t_match_filter\"d\"t_slam_tracker\"d\"t_pose\"d\"t_pose_score_filter\"d\"t_pose_score_vote\"d\"t_pose_score_find_peak\"d\"t_pose_score_refine\"d\"t_pose_score_other\"d\"t_pose_score\"d\"t_pose_ransac\"d\"t_pose_referee\"d\"t_pose_fuse\"d\"t_total\"d\"tracks_file_size\"q\"peak_mem_usage\"i}"

```
