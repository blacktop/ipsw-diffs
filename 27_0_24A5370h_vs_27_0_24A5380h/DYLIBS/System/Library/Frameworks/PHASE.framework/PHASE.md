## PHASE

> `/System/Library/Frameworks/PHASE.framework/PHASE`

```diff

-  __TEXT.__text: 0x252438
-  __TEXT.__realtime: 0x17114
+  __TEXT.__text: 0x252a58
+  __TEXT.__realtime: 0x17198
   __TEXT.__objc_methlist: 0x5084
-  __TEXT.__const: 0x47b0c
+  __TEXT.__const: 0x47b2c
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__gcc_except_tab: 0x26820
-  __TEXT.__oslogstring: 0x21c4d
-  __TEXT.__cstring: 0x16384
-  __TEXT.__unwind_info: 0xc480
+  __TEXT.__gcc_except_tab: 0x268b8
+  __TEXT.__oslogstring: 0x21da3
+  __TEXT.__cstring: 0x163a9
+  __TEXT.__unwind_info: 0xc4a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3c0
   __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__got: 0x6b8
+  __DATA_CONST.__got: 0x6d0
   __AUTH_CONST.__const: 0xe310
-  __AUTH_CONST.__cfstring: 0x5e20
+  __AUTH_CONST.__cfstring: 0x5e40
   __AUTH_CONST.__objc_const: 0xa510
   __AUTH_CONST.__weak_auth_got: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9884
-  Symbols:   27058
-  CStrings:  5344
+  Functions: 9894
+  Symbols:   27084
+  CStrings:  5350
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table126
+ __ZN5Phase14SpatialModeler12ERClusteringL30GenerateFadingSourceERMetadataEyRKNS0_20SourceListenerResultERKNS0_14RayTracerStateEdmRNS0_25DirectionalMetadataOutputIfEERNS_6VectorIfLm2EEE
+ __ZN5Phase14SpatialModeler30BroadBandScaleMetadataSubbandsIfEEvRNS0_25DirectionalMetadataOutputIT_EERKf
+ __ZNSt3__110__function12__value_funcIFbRKN2CA13ChannelLayoutEbNS_4spanIfLm18446744073709551615EEEEEaSB9nqe220106EDn
+ __ZNSt3__110__function12__value_funcIFbRKN2CA13ChannelLayoutEbNS_4spanIfLm18446744073709551615EEEEEaSB9nqe220106EOS9_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN5Phase14SpatialModeler25DirectionalMetadataOutputIfEEEEE9constructB9nqe220106IS5_JS5_ELi0EEEvRS6_PT_DpOT0_
+ __ZNSt3__134__uninitialized_allocator_relocateB9nqe220106INS_9allocatorIN5Phase14SpatialModeler25DirectionalMetadataOutputIfEEEEPS5_EEvRT_T0_SA_SA_
+ __ZNSt3__16vectorIN5Phase14SpatialModeler20SourcePreProcessData13PerSourceDataENS_9allocatorIS4_EEE20__throw_length_errorB9nqe220106Ev
+ __ZNSt3__16vectorIN5Phase14SpatialModeler25DirectionalMetadataOutputIfEENS_9allocatorIS4_EEE20__throw_length_errorB9nqe220106Ev
+ __ZNSt3__16vectorIN5Phase14SpatialModeler25DirectionalMetadataOutputIfEENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJS4_EEEPS4_DpOT_
+ __ZNSt3__16vectorIN5Phase14SpatialModeler25DirectionalMetadataOutputIfEENS_9allocatorIS4_EEE9push_backB9nqe220106EOS4_
+ __ZNSt3__19allocatorIN5Phase14SpatialModeler20SourcePreProcessData13PerSourceDataEE17allocate_at_leastB9nqe220106Em
+ __ZNSt3__19allocatorIN5Phase14SpatialModeler25DirectionalMetadataOutputIfEEE17allocate_at_leastB9nqe220106Em
- GCC_except_table127
CStrings:
+ "%25s:%-5d [ER_ENERGY_DEBUG] AggregateER src=%llu NAR=%.1f coeffs: b0=%.4f a1=%.4f (minPseudo=%.1f)"
+ "%25s:%-5d [ER_ENERGY_DEBUG] FindERClusters active=%zu fading=%zu numClusters=%u"
+ "%25s:%-5d [ER_ENERGY_DEBUG] HandleResultsER clusterKey=%llu found=%d numClusters=%zu"
+ "%25s:%-5d [ER_ENERGY_DEBUG] ProcessSourcesForClustering active=%zu fading=%zu"
+ "phase_enable_er_energy_debug_logging"

```
