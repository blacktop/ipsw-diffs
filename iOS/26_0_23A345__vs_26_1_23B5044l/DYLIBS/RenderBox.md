## RenderBox

> `/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox`

```diff

-7.0.84.1.108
-  __TEXT.__text: 0x14eff0
-  __TEXT.__auth_stubs: 0x2920
+7.1.4.1.103
+  __TEXT.__text: 0x14f394
+  __TEXT.__auth_stubs: 0x2930
   __TEXT.__objc_methlist: 0x2a90
-  __TEXT.__const: 0x5f88
+  __TEXT.__const: 0x5fa8
   __TEXT.__gcc_except_tab: 0x74dc
-  __TEXT.__cstring: 0x5d29
+  __TEXT.__cstring: 0x5d5a
   __TEXT.__oslogstring: 0xf7d
-  __TEXT.__unwind_info: 0x6200
+  __TEXT.__unwind_info: 0x61f0
   __TEXT.__eh_frame: 0x60
   __TEXT.__objc_classname: 0x41a
   __TEXT.__objc_methname: 0x6340

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e10
   __DATA_CONST.__objc_superrefs: 0xe0
-  __AUTH_CONST.__auth_got: 0x14a0
+  __AUTH_CONST.__auth_got: 0x14a8
   __AUTH_CONST.__const: 0x8ab8
-  __AUTH_CONST.__cfstring: 0x3000
+  __AUTH_CONST.__cfstring: 0x3040
   __AUTH_CONST.__objc_const: 0x4588
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x18

   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x10
   __DATA.__objc_ivar: 0x2b4
-  __DATA.__data: 0x934
+  __DATA.__data: 0x944
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x288
+  __DATA.__bss: 0x2a0
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__common: 0x50
-  __DATA_DIRTY.__bss: 0x550
+  __DATA_DIRTY.__bss: 0x538
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5BBA335D-7200-3B8F-936C-BC3F2BCB7393
-  Functions: 6873
-  Symbols:   18084
-  CStrings:  3633
+  UUID: A58259E6-26D7-3B7E-8F69-B876F2D52256
+  Functions: 6875
+  Symbols:   18088
+  CStrings:  3637
 
Symbols:
+ -[RBLayer displayWithBounds:flags:callback:]
+ -[RBLayer displayWithBounds:flags:callback:].cold.1
+ -[RBLayer displayWithBounds:flags:callback:].cold.2
+ -[RBLayer displayWithBounds:flags:callback:].cold.3
+ -[RBLayer displayWithBounds:flags:callback:].cold.4
+ -[RBLayer displayWithBounds:flags:callback:].cold.5
+ -[RBLayer displayWithBounds:flags:callback:].cold.6
+ -[RBLayer displayWithBounds:flags:callback:].cold.7
+ -[RBLayer displayWithBounds:flags:callback:].cold.8
+ -[RBLayer displayWithBounds:flags:callback:].cold.9
+ GCC_except_table113
+ GCC_except_table149
+ GCC_except_table68
+ GCC_except_table72
+ GCC_except_table83
+ GCC_except_table89
+ _RBImageRendererPreferNativeFloatComponents
+ _RBImageRendererSynchronousRendering
+ __ZGVZ44-[RBLayer displayWithBounds:flags:callback:]E19disable_subsurfaces
+ __ZGVZZZ44-[RBLayer displayWithBounds:flags:callback:]EUb_ENK3$_0clIPNSt3__14pairIPN2RB7SurfaceEP13_CAImageQueueEEEEDajyT_E9log_stats
+ __ZGVZZZ44-[RBLayer displayWithBounds:flags:callback:]EUb_ENK3$_0clIPvEEDajyT_E9log_stats
+ __ZN2RB11SurfacePool7collectEb
+ __ZN2RB11SurfacePool7collectEb.cold.1
+ __ZN2RB13ImageProvider15start_renderingEb
+ __ZN2RB13ImageProvider22start_rendering_lockedEbRNSt3__111unique_lockINS1_5mutexEEE
+ __ZN2RB13ImageProvider22start_rendering_lockedEbRNSt3__111unique_lockINS1_5mutexEEE.cold.1
+ __ZN2RB13ImageProvider22start_rendering_lockedEbRNSt3__111unique_lockINS1_5mutexEEE.cold.2
+ __ZN2RB13ImageProvider22start_rendering_lockedEbRNSt3__111unique_lockINS1_5mutexEEE.cold.3
+ __ZN2RB18SharedSurfaceGroup20wait_for_allocationsERNS_19SharedSurfaceClientEb
+ __ZN2RB18SharedSurfaceGroup20wait_for_allocationsERNS_19SharedSurfaceClientEb.cold.1
+ __ZN2RB18SharedSurfaceGroup20wait_for_allocationsERNS_19SharedSurfaceClientEb.cold.2
+ __ZN2RB18Typed_vImageBufferIDv4_DF16_E18apply_pixel_valuesIZNS_9CGContext21apply_distance_filterEDv2_fS5_jE3$_9EEvRKT_
+ __ZN2RB6Device19RenderPipelineEntry14function_tableEjjRKNS_13shared_vectorIPKNS_8FunctionEE8snapshotEj
+ __ZN2RB6Device19RenderPipelineEntry14function_tableEjjRKNS_13shared_vectorIPKNS_8FunctionEE8snapshotEj.cold.1
+ __ZN2RB6Device19RenderPipelineEntry8mark_useEjj
+ __ZN2RB6Device21render_pipeline_stateENS_20FormattedRenderStateERKNS_13shared_vectorIPKNS_8FunctionEE8snapshotEjj
+ __ZN2RB6vectorINS_6cf_ptrIP13_CAImageQueueEELm8EmED1Ev
+ __ZN2RB6vectorINSt3__14pairIP13_CAImageQueueyEELm2EmE12reserve_slowEm
+ __ZNSt3__111unique_lockINS_5mutexEE4lockB8nn200100Ev
+ __ZNSt3__111unique_lockINS_5mutexEE6unlockB8nn200100Ev
+ __ZZ44-[RBLayer displayWithBounds:flags:callback:]E19disable_subsurfaces
+ __ZZ44-[RBLayer displayWithBounds:flags:callback:]E8inverses
+ __ZZN2RB11SurfacePool15AsyncCollectionD1EvEN3$_08__invokeEPv
+ __ZZN2RB13ImageProvider22start_rendering_lockedEbRNSt3__111unique_lockINS1_5mutexEEEEN3$_08__invokeEPv
+ __ZZN2RB13ImageProvider22start_rendering_lockedEbRNSt3__111unique_lockINS1_5mutexEEEEN3$_08__invokeEPv.cold.1
+ __ZZN2RB13ImageProvider22start_rendering_lockedEbRNSt3__111unique_lockINS1_5mutexEEEEN3$_08__invokeEPv.cold.2
+ __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferIDv4_DF16_E17apply_quad_valuesIZNS_9CGContext21apply_glass_highlightERKNS_20GlassHighlightEffectEE3$_3EEvRKT_EUlmmmmE_EEvmmSC_ENUlPvmE_8__invokeESE_m
+ __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferIDv4_DF16_E17apply_quad_valuesIZNS_9CGContext25apply_component_thresholdEhDv2_fRKNS_4Fill5ColorEE3$_3EEvRKT_EUlmmmmE_EEvmmSE_ENUlPvmE_8__invokeESG_m
+ __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferIDv4_DF16_E18apply_pixel_valuesIZNS_9CGContext18apply_color_matrixERKNS_11ColorMatrixEbE3$_1EEvRKT_EUlmmmmE_EEvmmSC_ENUlPvmE_8__invokeESE_m
+ __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferIDv4_DF16_E18apply_pixel_valuesIZNS_9CGContext19apply_component_lutEhPKjE3$_0EEvRKT_EUlmmmmE_EEvmmSB_ENUlPvmE_8__invokeESD_m
+ __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferIDv4_DF16_E18apply_pixel_valuesIZNS_9CGContext21apply_distance_filterEDv2_fS6_jE3$_9EEvRKT_EUlmmmmE_EEvmmSA_ENUlPvmE_8__invokeESC_m
+ __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferIDv4_DF16_E18apply_pixel_valuesIZNS_9CGContext21apply_luminance_curveEDv4_fRKNS_4Fill5ColorEE3$_1EEvRKT_EUlmmmmE_EEvmmSE_ENUlPvmE_8__invokeESG_m
+ __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferIDv4_DF16_E18apply_pixel_valuesIZNS_9CGContext22apply_color_conversionERKNS_10ColorSpace10ConversionEE3$_1EEvRKT_EUlmmmmE_EEvmmSD_ENUlPvmE_8__invokeESF_m
+ __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferIDv4_DF16_E29apply_pixel_coords_and_valuesIZNS_9CGContext22apply_ovalize_gradientEDv2_fffS6_RKNS_15AffineTransformEE3$_2EEvRKT_EUlmmmmE_EEvmmSD_ENUlPvmE_8__invokeESF_m
+ __ZZZ44-[RBLayer displayWithBounds:flags:callback:]EUb_EN3$_08__invokeIPvEEDajyT_
+ __ZZZZ44-[RBLayer displayWithBounds:flags:callback:]EUb_ENK3$_0clIPvEEDajyT_E9log_stats
+ ___44-[RBLayer displayWithBounds:flags:callback:]_block_invoke
+ ___44-[RBLayer displayWithBounds:flags:callback:]_block_invoke.28
+ ___44-[RBLayer displayWithBounds:flags:callback:]_block_invoke.30
+ ___44-[RBLayer displayWithBounds:flags:callback:]_block_invoke.36
+ ___44-[RBLayer displayWithBounds:flags:callback:]_block_invoke_2
+ ___44-[RBLayer displayWithBounds:flags:callback:]_block_invoke_2.39
+ ___44-[RBLayer displayWithBounds:flags:callback:]_block_invoke_2.cold.1
+ ____ZN2RB11SurfacePool7collectEb_block_invoke
+ _dispatch_after
- -[RBLayer displayWithBounds:callback:].cold.1
- -[RBLayer displayWithBounds:callback:].cold.10
- -[RBLayer displayWithBounds:callback:].cold.2
- -[RBLayer displayWithBounds:callback:].cold.3
- -[RBLayer displayWithBounds:callback:].cold.4
- -[RBLayer displayWithBounds:callback:].cold.5
- -[RBLayer displayWithBounds:callback:].cold.6
- -[RBLayer displayWithBounds:callback:].cold.7
- -[RBLayer displayWithBounds:callback:].cold.8
- -[RBLayer displayWithBounds:callback:].cold.9
- GCC_except_table80
- GCC_except_table82
- GCC_except_table85
- GCC_except_table90
- __ZGVZ38-[RBLayer displayWithBounds:callback:]E19disable_subsurfaces
- __ZGVZZZ38-[RBLayer displayWithBounds:callback:]EUb_ENK3$_0clIPNSt3__14pairIPN2RB7SurfaceEP13_CAImageQueueEEEEDajyT_E9log_stats
- __ZGVZZZ38-[RBLayer displayWithBounds:callback:]EUb_ENK3$_0clIPvEEDajyT_E9log_stats
- __ZN2RB11SurfacePool14collect_queuesEdRd
- __ZN2RB11SurfacePool5clearEv
- __ZN2RB11SurfacePool7collectEjd
- __ZN2RB11SurfacePool7collectEjd.cold.1
- __ZN2RB13ImageProvider15start_renderingEv
- __ZN2RB13ImageProvider22start_rendering_lockedEv
- __ZN2RB13ImageProvider22start_rendering_lockedEv.cold.1
- __ZN2RB18SharedSurfaceGroup20wait_for_allocationsERNS_19SharedSurfaceClientE
- __ZN2RB18SharedSurfaceGroup20wait_for_allocationsERNS_19SharedSurfaceClientE.cold.1
- __ZN2RB18SharedSurfaceGroup20wait_for_allocationsERNS_19SharedSurfaceClientE.cold.2
- __ZN2RB18SharedSurfaceGroupC2EPNS_6DeviceE
- __ZN2RB18SharedSurfaceGroupD2Ev.cold.3
- __ZN2RB18Typed_vImageBufferINS_12packed_half4EE18apply_pixel_valuesIZNS_9CGContext21apply_distance_filterEDv2_fS5_jE3$_9EEvRKT_
- __ZN2RB6Device19RenderPipelineEntry14function_tableEjRKNS_13shared_vectorIPKNS_8FunctionEE8snapshotEj
- __ZN2RB6Device19RenderPipelineEntry14function_tableEjRKNS_13shared_vectorIPKNS_8FunctionEE8snapshotEj.cold.1
- __ZN2RB6Device21render_pipeline_stateENS_20FormattedRenderStateERKNS_13shared_vectorIPKNS_8FunctionEE8snapshotE
- __ZN2RB6vectorINS_6cf_ptrIP13_CAImageQueueEELm8EmED2Ev
- __ZN2RB6vectorINSt3__14pairIP13_CAImageQueueyEELm0EjE12reserve_slowEj
- __ZZ38-[RBLayer displayWithBounds:callback:]E19disable_subsurfaces
- __ZZ38-[RBLayer displayWithBounds:callback:]E8inverses
- __ZZN2RB11SurfacePool13collect_asyncEvEN3$_08__invokeEPv
- __ZZN2RB11SurfacePool7collectEjdEN3$_28__invokeEPv
- __ZZN2RB13ImageProvider22start_rendering_lockedEvEN3$_08__invokeEPv
- __ZZN2RB13ImageProvider22start_rendering_lockedEvEN3$_08__invokeEPv.cold.1
- __ZZN2RB13ImageProvider22start_rendering_lockedEvEN3$_08__invokeEPv.cold.2
- __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferINS_12packed_half4EE17apply_quad_valuesIZNS_9CGContext21apply_glass_highlightERKNS_20GlassHighlightEffectEE3$_3EEvRKT_EUlmmmmE_EEvmmSC_ENUlPvmE_8__invokeESE_m
- __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferINS_12packed_half4EE17apply_quad_valuesIZNS_9CGContext25apply_component_thresholdEhDv2_fRKNS_4Fill5ColorEE3$_3EEvRKT_EUlmmmmE_EEvmmSE_ENUlPvmE_8__invokeESG_m
- __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferINS_12packed_half4EE18apply_pixel_valuesIZNS_9CGContext18apply_color_matrixERKNS_11ColorMatrixEbE3$_1EEvRKT_EUlmmmmE_EEvmmSC_ENUlPvmE_8__invokeESE_m
- __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferINS_12packed_half4EE18apply_pixel_valuesIZNS_9CGContext19apply_component_lutEhPKjE3$_0EEvRKT_EUlmmmmE_EEvmmSB_ENUlPvmE_8__invokeESD_m
- __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferINS_12packed_half4EE18apply_pixel_valuesIZNS_9CGContext21apply_distance_filterEDv2_fS6_jE3$_9EEvRKT_EUlmmmmE_EEvmmSA_ENUlPvmE_8__invokeESC_m
- __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferINS_12packed_half4EE18apply_pixel_valuesIZNS_9CGContext21apply_luminance_curveEDv4_fRKNS_4Fill5ColorEE3$_1EEvRKT_EUlmmmmE_EEvmmSE_ENUlPvmE_8__invokeESG_m
- __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferINS_12packed_half4EE18apply_pixel_valuesIZNS_9CGContext22apply_color_conversionERKNS_10ColorSpace10ConversionEE3$_1EEvRKT_EUlmmmmE_EEvmmSD_ENUlPvmE_8__invokeESF_m
- __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferINS_12packed_half4EE29apply_pixel_coords_and_valuesIZNS_9CGContext22apply_ovalize_gradientEDv2_fffS6_RKNS_15AffineTransformEE3$_2EEvRKT_EUlmmmmE_EEvmmSD_ENUlPvmE_8__invokeESF_m
- __ZZZ38-[RBLayer displayWithBounds:callback:]EUb_EN3$_08__invokeIPvEEDajyT_
- __ZZZZ38-[RBLayer displayWithBounds:callback:]EUb_ENK3$_0clIPvEEDajyT_E9log_stats
- ___38-[RBLayer displayWithBounds:callback:]_block_invoke
- ___38-[RBLayer displayWithBounds:callback:]_block_invoke.28
- ___38-[RBLayer displayWithBounds:callback:]_block_invoke.30
- ___38-[RBLayer displayWithBounds:callback:]_block_invoke.36
- ___38-[RBLayer displayWithBounds:callback:]_block_invoke_2
- ___38-[RBLayer displayWithBounds:callback:]_block_invoke_2.39
- ___38-[RBLayer displayWithBounds:callback:]_block_invoke_2.cold.1
CStrings:
+ "  Surface %p; [%d %d]; IOSurface %lx%s; owner %p; last used %f\n"
+ "7.1.4.1.103"
+ "preferNativeFloatComponents"
+ "synchronousRendering"
- "  Surface %p; [%d %d]; IOSurface %x%s; owner %p; last used %f\n"
- "7.0.84.1.108"

```
