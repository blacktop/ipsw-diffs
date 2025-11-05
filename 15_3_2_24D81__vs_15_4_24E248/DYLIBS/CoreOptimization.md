## CoreOptimization

> `/System/Library/PrivateFrameworks/CoreOptimization.framework/Versions/A/CoreOptimization`

```diff

 117.0.0.0.0
-  __TEXT.__text: 0x3d34
+  __TEXT.__text: 0x3d88
   __TEXT.__auth_stubs: 0x230
   __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x4c0
+  __TEXT.__gcc_except_tab: 0x4d8
   __TEXT.__cstring: 0x2cf
   __TEXT.__unwind_info: 0x180
   __DATA_CONST.__got: 0x40

   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 25691492-0C8C-346B-9402-70B75D25888A
+  UUID: 5B2CDD2B-2F4A-3302-B704-98010BEED2F8
   Functions: 30
   Symbols:   101
   CStrings:  45
Symbols:
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
+ __ZNSt3__116__pad_and_outputB8ne190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__14endlB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_
+ __ZNSt3__1lsB8ne190102INS_11char_traitsIcEEEERNS_13basic_ostreamIcT_EES6_PKc
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100Emc
- __ZNSt3__116__pad_and_outputB8ne180100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__124__put_character_sequenceB8ne180100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__14endlB8ne180100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_
- __ZNSt3__1lsB8ne180100INS_11char_traitsIcEEEERNS_13basic_ostreamIcT_EES6_PKc
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
Functions:
~ __ZN16CoreOptimization4BFGS13UpdateHessianERNS_9hessian_tERKNSt3__18valarrayIdEES7_ : 1012 -> 1008
~ __ZN16CoreOptimization4BFGS16UpdateHessianInvERNS_9hessian_tERKNSt3__18valarrayIdEES7_ : 1256 -> 1252
~ __ZN16CoreOptimization4BFGS8OptimizeEv : 2172 -> 2120
~ __ZN16CoreOptimization4BFGS19GoldenSectionSearchERKNSt3__18valarrayIdEES5_b : 720 -> 772
~ __ZN16CoreOptimization4BFGS9Optimize0Ev : 1932 -> 1908
~ __ZN16CoreOptimization4BFGS21GoldenSectionSearch_rEddddRKNSt3__18valarrayIdEES5_ : 1184 -> 1300
~ __ZN16CoreOptimization4BFGS20GoldenSectionSearch0ERKNSt3__18valarrayIdEES5_b : 1256 -> 1260
~ __ZNSt3__124__put_character_sequenceB8ne180100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m -> __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m : 420 -> 424
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100Emc -> __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc : 172 -> 164

```
