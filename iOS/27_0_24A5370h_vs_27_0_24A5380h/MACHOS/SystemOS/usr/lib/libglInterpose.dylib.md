## libglInterpose.dylib

> `/usr/lib/libglInterpose.dylib`

```diff

-  __TEXT.__text: 0x1ea7dc
+  __TEXT.__text: 0x1ea79c
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_stubs: 0xee0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x140
-  __TEXT.__gcc_except_tab: 0x1694c
+  __TEXT.__gcc_except_tab: 0x16944
   __TEXT.__cstring: 0x23f8
   __TEXT.__const: 0x1c8
   __TEXT.__objc_methname: 0xd3c
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ __Z22copyout_vertex_arrays2P11ContextInfolllb : 3704 -> 3816
~ _unapply_draw_overrides : 608 -> 600
~ __ZN16ContextHarvester24harvestLegacyARBProgramsEv : 188 -> 180
~ __ZN16ContextHarvester15harvestTexturesEb : 324 -> 308
~ __ZN16ContextHarvester19harvestQueryObjectsEv : 224 -> 200
~ __ZN16ContextHarvester24encodeProgramXfbVaryingsEjRK10ProgramXfb : 492 -> 480
~ __ZN16ContextHarvester19harvestGroupMarkersEv : 260 -> 252
~ _get_all_per_function_profiling_data : 524 -> 512
~ __ZN11ContextInfo19ExecuteAfterPresentEv : 296 -> 284
~ __ZNSt3__16vectorINS_8functionIFvP11ContextInfoEEENS_9allocatorIS5_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS5_RS7_EE : 368 -> 340
~ __ZN8GPUTools15ResourceUpdater30_GetCombinedLinkedShaderSourceERKNSt3__16vectorI17ProgramShaderInfoNS1_9allocatorIS3_EEEE : 312 -> 296
~ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9fqe220106EPKvm : 532 -> 520
~ __ZNSt3__116__insertion_sortB9fqe220106INS_17_ClassicAlgPolicyERU13block_pointerFbRKN8GPUTools15NameTargetTupleES5_ENS2_14array_iteratorIS3_EEEEvT1_SB_T0_ : 236 -> 220
~ __ZNSt3__126__insertion_sort_unguardedB9fqe220106INS_17_ClassicAlgPolicyERU13block_pointerFbRKN8GPUTools15NameTargetTupleES5_ENS2_14array_iteratorIS3_EEEEvT1_SB_T0_ : 272 -> 260
~ __ZNSt3__127__insertion_sort_incompleteB9fqe220106INS_17_ClassicAlgPolicyERU13block_pointerFbRKN8GPUTools15NameTargetTupleES5_ENS2_14array_iteratorIS3_EEEEbT1_SB_T0_ : 1016 -> 1024

```
