## STF

> `/System/Library/VideoProcessors/STF.bundle/STF`

```diff

 587.122.6.0.2
-  __TEXT.__text: 0xb9010
-  __TEXT.__auth_stubs: 0x710
+  __TEXT.__text: 0x1012b0
+  __TEXT.__auth_stubs: 0x720
   __TEXT.__objc_methlist: 0x1654
-  __TEXT.__const: 0x300
-  __TEXT.__cstring: 0x407e
-  __TEXT.__gcc_except_tab: 0x7c
+  __TEXT.__const: 0x540
+  __TEXT.__cstring: 0x4084
+  __TEXT.__gcc_except_tab: 0x154
   __TEXT.__oslogstring: 0x53
-  __TEXT.__unwind_info: 0xac8
-  __TEXT.__eh_frame: 0x1e8
+  __TEXT.__unwind_info: 0xe30
+  __TEXT.__eh_frame: 0xb38
   __TEXT.__objc_classname: 0x254
   __TEXT.__objc_methname: 0x4809
   __TEXT.__objc_methtype: 0x10a9

   __DATA_CONST.__objc_selrefs: 0xc60
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__auth_got: 0x3a0
   __AUTH_CONST.__const: 0x388
   __AUTH_CONST.__cfstring: 0x1100
   __AUTH_CONST.__objc_const: 0x3ba0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1687
-  Symbols:   4394
-  CStrings:  1659
+  Functions: 1980
+  Symbols:   4986
+  CStrings:  1660
 
Symbols:
+ __Z19sgetf2_sme_internalPKiS0_PfS0_PiS2_
+ __Z19sgetrf_sme_internalPKiS0_PfS0_PiS1_S2_S2_
+ __Z20get_sgemm_sme_kernelN3sme4blas8SCALARFPES1_
+ __Z20get_ssyrk_sme_kernelN3sme4blas8SCALARFPES1_
+ __Z20sgetrf2_sme_internalPKiS0_PfS0_PiS1_S2_S2_
+ __Z27get_sgemm_sme_packed_kernelN3sme4blas8SCALARFPES1_
+ __Z27get_ssyrk_sme_packed_kernelN3sme4blas8SCALARFPES1_
+ __Z27get_strsm_sme_packed_kernelN3sme4blas8SCALARFPE
+ __Z8sme_gemvbllfPKflS0_lfPff
+ __ZN12_GLOBAL__N_112syrkT_kernelIfEEvmmmN3sme4blas8SCALARFPES3_bllT_PKS4_lS4_PS4_lS7_S7_
+ __ZN12_GLOBAL__N_120syrkN_incache_kernelIfEEvN3sme4blas8SCALARFPES3_bllT_PKS4_lS4_PS4_l
+ __ZN12_GLOBAL__N_121sme_transpose_alignedIfLb0EEEvllPKT_lPS1_l
+ __ZN12_GLOBAL__N_121sme_transpose_alignedIfLb1EEEvllPKT_lPS1_l
+ __ZN12_GLOBAL__N_122gemm_nn_incache_kernelIfEEvN3sme4blas8SCALARFPES3_lllT_PKS4_lS6_lS4_PS4_lS7_
+ __ZN12_GLOBAL__N_122gemm_nt_incache_kernelIfEEvN3sme4blas8SCALARFPES3_lllT_PKS4_lS6_lS4_PS4_l
+ __ZN12_GLOBAL__N_122gemm_tn_incache_kernelIfEEvN3sme4blas8SCALARFPES3_mmmlllT_PKS4_lS6_lS4_PS4_lS7_S7_
+ __ZN12_GLOBAL__N_122gemm_tt_incache_kernelIfEEvN3sme4blas8SCALARFPES3_mlllT_PKS4_lS6_lS4_PS4_lS7_
+ __ZN12_GLOBAL__N_124repack_unaligned_alignedIfLb0EEEvllPKT_lPS1_l
+ __ZN12_GLOBAL__N_124trsm_blocked_left_kernelIfEEvN3sme4blas8SCALARFPEbbbllT_PKS4_lPS4_lllS7_S7_S7_S7_
+ __ZN12_GLOBAL__N_125syrkN_outsidecache_kernelIfEEvmmmN3sme4blas8SCALARFPES3_bllT_PKS4_lS4_PS4_lS7_S7_
+ __ZN12_GLOBAL__N_125trsm_blocked_right_kernelIfEEvN3sme4blas8SCALARFPEbbbllT_PKS4_lPS4_lllS7_S7_S7_S7_
+ __ZN12_GLOBAL__N_127gemm_nn_outsidecache_kernelIfEEvbmmmN3sme4blas8SCALARFPES3_lllT_PKS4_lS6_lS4_PS4_lS7_S7_
+ __ZN12_GLOBAL__N_127gemm_nt_outsidecache_kernelIfEEvbmmmN3sme4blas8SCALARFPES3_lllT_PKS4_lS6_lS4_PS4_lS7_S7_
+ __ZN12_GLOBAL__N_127gemm_tn_outsidecache_kernelIfEEvbN3sme4blas8SCALARFPES3_mmmlllT_PKS4_lS6_lS4_PS4_lS7_S7_
+ __ZN12_GLOBAL__N_127gemm_tt_outsidecache_kernelIfEEvbmmmN3sme4blas8SCALARFPES3_lllT_PKS4_lS6_lS4_PS4_lS7_S7_
+ __ZN3sme10production10apply_betaIfLy0EEEvllT_PS2_l
+ __ZN3sme10production10apply_betaIfLy1EEEvllT_PS2_l
+ __ZN3sme10production10apply_betaIfLy2EEEvllT_PS2_l
+ __ZN3sme10production10apply_betaIfLy3EEEvllT_PS2_l
+ __ZN3sme10production13gemm_internalIfLb0ELi0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production13gemm_internalIfLb0ELi1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production13gemm_internalIfLb0ELi2EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production13gemm_internalIfLb0ELi3EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production13gemm_internalIfLb0ELi4EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production13gemm_internalIfLb1ELi0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production13gemm_internalIfLb1ELi1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production13gemm_internalIfLb1ELi2EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production13gemm_internalIfLb1ELi3EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production13gemm_internalIfLb1ELi4EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production13syrk_internalIfLb0ELi0EEEvbllT_PKS2_lS2_PS2_l
+ __ZN3sme10production13syrk_internalIfLb0ELi1EEEvbllT_PKS2_lS2_PS2_l
+ __ZN3sme10production13syrk_internalIfLb0ELi2EEEvbllT_PKS2_lS2_PS2_l
+ __ZN3sme10production13syrk_internalIfLb0ELi3EEEvbllT_PKS2_lS2_PS2_l
+ __ZN3sme10production13syrk_internalIfLb0ELi4EEEvbllT_PKS2_lS2_PS2_l
+ __ZN3sme10production13syrk_internalIfLb1ELi0EEEvbllT_PKS2_lS2_PS2_l
+ __ZN3sme10production13syrk_internalIfLb1ELi1EEEvbllT_PKS2_lS2_PS2_l
+ __ZN3sme10production13syrk_internalIfLb1ELi2EEEvbllT_PKS2_lS2_PS2_l
+ __ZN3sme10production13syrk_internalIfLb1ELi3EEEvbllT_PKS2_lS2_PS2_l
+ __ZN3sme10production13syrk_internalIfLb1ELi4EEEvbllT_PKS2_lS2_PS2_l
+ __ZN3sme10production15load_apply_betaIfLy0EEEvllT_PS2_l
+ __ZN3sme10production19load_apply_beta_1x2IfLb1ELy0EEEvllT_PS2_l
+ __ZN3sme10production19load_apply_beta_1x4IfLb0ELy0EEEvllT_PS2_l
+ __ZN3sme10production19load_apply_beta_1x4IfLb1ELy0EEEvllT_PS2_l
+ __ZN3sme10production19syrk_lower_dispatchIfLb0EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production19syrk_upper_dispatchIfLb0EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production20gemm_worker_dispatchIfLb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production20gemm_worker_dispatchIfLb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production20gemm_worker_dispatchIfLb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production21sme_trans_pack_singleEllPKflPf
+ __ZN3sme10production21sme_transpose_alignedEllPKflPfl
+ __ZN3sme10production23trsm_left_lower_fms_1x2IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x2IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x2IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x2IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x2IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x2IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x2IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x2IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x4IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x4IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x4IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x4IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x4IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x4IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x4IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_lower_fms_1x4IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x2IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x2IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x2IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x2IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x2IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x2IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x2IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x2IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x4IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x4IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x4IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x4IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x4IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x4IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x4IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production23trsm_left_upper_fms_1x4IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production24blocked_left_trsm_packedIfLb0ELi1EEEvbbllT_PKS2_PS2_lS5_
+ __ZN3sme10production24blocked_left_trsm_packedIfLb0ELi3EEEvbbllT_PKS2_PS2_lS5_
+ __ZN3sme10production24blocked_left_trsm_packedIfLb1ELi1EEEvbbllT_PKS2_PS2_lS5_
+ __ZN3sme10production24blocked_left_trsm_packedIfLb1ELi3EEEvbbllT_PKS2_PS2_lS5_
+ __ZN3sme10production24gemm_worker_1xN_dispatchIfLb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production24gemm_worker_1xN_dispatchIfLb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production24gemm_worker_Mx1_dispatchIfLb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production24gemm_worker_Mx1_dispatchIfLb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production24sme_no_trans_pack_singleEllPKflPf
+ __ZN3sme10production24trsm_left_lower_dispatchIfLb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production24trsm_left_lower_dispatchIfLb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production24trsm_left_lower_dispatchIfLb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production24trsm_left_lower_dispatchIfLb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production24trsm_left_upper_dispatchIfLb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production24trsm_left_upper_dispatchIfLb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production24trsm_left_upper_dispatchIfLb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production24trsm_left_upper_dispatchIfLb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
+ __ZN3sme10production24trsm_right_lower_fms_2x1IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_2x1IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_2x1IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_2x1IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_2x1IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_2x1IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_2x1IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_2x1IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_4x1IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_4x1IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_4x1IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_4x1IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_4x1IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_4x1IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_4x1IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_lower_fms_4x1IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_2x1IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_2x1IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_2x1IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_2x1IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_2x1IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_2x1IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_2x1IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_2x1IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_4x1IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_4x1IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_4x1IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_4x1IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_4x1IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_4x1IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_4x1IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production24trsm_right_upper_fms_4x1IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production25blocked_right_trsm_packedIfLb0ELi1EEEvbbllT_PKS2_PS2_lS5_
+ __ZN3sme10production25blocked_right_trsm_packedIfLb0ELi3EEEvbbllT_PKS2_PS2_lS5_
+ __ZN3sme10production25blocked_right_trsm_packedIfLb1ELi1EEEvbbllT_PKS2_PS2_lS5_
+ __ZN3sme10production25blocked_right_trsm_packedIfLb1ELi3EEEvbbllT_PKS2_PS2_lS5_
+ __ZN3sme10production25gemm_alpha_beta_writebackIfLb0ELb0EEEvllT_S2_PS2_l
+ __ZN3sme10production25gemm_alpha_beta_writebackIfLb0ELb1EEEvllT_S2_PS2_l
+ __ZN3sme10production25gemm_alpha_beta_writebackIfLb1ELb0EEEvllT_S2_PS2_l
+ __ZN3sme10production25gemm_alpha_beta_writebackIfLb1ELb1EEEvllT_S2_PS2_l
+ __ZN3sme10production25syrk_alpha_beta_writebackIfLb0EEEvblT_S2_PS2_l
+ __ZN3sme10production25syrk_alpha_beta_writebackIfLb1EEEvblT_S2_PS2_l
+ __ZN3sme10production25trsm_right_lower_dispatchIfLb0ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production25trsm_right_lower_dispatchIfLb0ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production25trsm_right_lower_dispatchIfLb1ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production25trsm_right_lower_dispatchIfLb1ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production25trsm_right_upper_dispatchIfLb0ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production25trsm_right_upper_dispatchIfLb0ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production25trsm_right_upper_dispatchIfLb1ELb0EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production25trsm_right_upper_dispatchIfLb1ELb1EEEvllPKT_S4_lS2_PS2_l
+ __ZN3sme10production28syrk_lower_dispatch_fastpathIfLb0ELb0ELb0EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production28syrk_lower_dispatch_fastpathIfLb0ELb0ELb1EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production28syrk_lower_dispatch_fastpathIfLb0ELb1ELb0EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production28syrk_lower_dispatch_fastpathIfLb0ELb1ELb1EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production28syrk_lower_dispatch_fastpathIfLb1ELb0ELb1EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production28syrk_lower_dispatch_fastpathIfLb1ELb1ELb1EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production28syrk_upper_dispatch_fastpathIfLb0ELb0ELb0EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production28syrk_upper_dispatch_fastpathIfLb0ELb0ELb1EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production28syrk_upper_dispatch_fastpathIfLb0ELb1ELb0EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production28syrk_upper_dispatch_fastpathIfLb0ELb1ELb1EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production28syrk_upper_dispatch_fastpathIfLb1ELb0ELb1EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production28syrk_upper_dispatch_fastpathIfLb1ELb1ELb1EEEvllT_PKS2_lS2_PS2_l
+ __ZN3sme10production29gemm_1xN_alpha_beta_writebackIfLb0EEEvllT_S2_PS2_l
+ __ZN3sme10production29gemm_1xN_alpha_beta_writebackIfLb1EEEvllT_S2_PS2_l
+ __ZN3sme10production29gemm_Mx1_alpha_beta_writebackIfLb0EEEvllT_S2_PS2_l
+ __ZN3sme10production29gemm_Mx1_alpha_beta_writebackIfLb1EEEvllT_S2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb0ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb0ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb0ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb0ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb1ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb1ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb1ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb1ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb1ELb0ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb1ELb0ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb1ELb0ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb1ELb0ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb1ELb1ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb1ELb1ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb0ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb0ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb0ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb0ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb1ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb1ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb1ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb1ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb0ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb0ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb0ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb0ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb1ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb1ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb1ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb1ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb0ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb0ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb0ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb0ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb1ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb1ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb1ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb1ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb1ELb0ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb1ELb0ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
+ __ZN3sme10production4trsmIfLi1EEEvbbbbllT_PKS2_PS2_lS5_
+ __ZN3sme10production4trsmIfLi3EEEvbbbbllT_PKS2_PS2_lS5_
+ __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvmllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
+ __ZN4blas6memory13aligned_allocIfEENSt3__110unique_ptrIT_NS0_11custom_freeIS4_EEEEmm
+ __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
+ __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
+ __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
+ __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
+ __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
+ __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
+ __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
+ __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
+ __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
+ ___arm_tpidr2_restore
+ ___arm_tpidr2_save
+ _abort
+ _do_abort
+ _saxpby_internal
+ _sme_sgemm
+ _sme_ssyrk
+ _sme_strsm
CStrings:
+ "GETF2"

```
