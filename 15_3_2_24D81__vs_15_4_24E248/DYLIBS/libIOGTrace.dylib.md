## libIOGTrace.dylib

> `/usr/lib/libIOGTrace.dylib`

```diff

-598.0.0.0.0
-  __TEXT.__text: 0x12f4
+599.0.0.0.0
+  __TEXT.__text: 0x12dc
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__const: 0x34
   __TEXT.__gcc_except_tab: 0x124

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: C43AE437-3CD0-32BB-9478-70C0005C4A38
+  UUID: 34D5AF43-7336-3D82-A5CE-D29711E861BE
   Functions: 32
   Symbols:   88
   CStrings:  20
Symbols:
+ __ZNKSt3__16vectorI11GTraceEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrI8IOGTraceNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI11GTraceEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorI11GTraceEntryNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI11GTraceEntryNS_9allocatorIS1_EEEC2B8ne190102Em
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZNKSt3__16vectorI11GTraceEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110unique_ptrI8IOGTraceNS_14default_deleteIS1_EEE5resetB8ne180100EPS1_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI11GTraceEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorI11GTraceEntryNS_9allocatorIS1_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorI11GTraceEntryNS_9allocatorIS1_EEEC2Em
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
Functions:
~ __ZN8IOGTraceD2Ev : 284 -> 272
~ __ZN8IOGTrace11formatTokenEttytytytyy : 200 -> 196
~ _getBreadcrumbBase : 28 -> 32
~ _formatToken : 200 -> 196
~ _recordTokenNow : 240 -> 236
~ __ZNSt3__110unique_ptrI8IOGTraceNS_14default_deleteIS1_EEE5resetB8ne180100EPS1_ -> __ZNSt3__110unique_ptrI8IOGTraceNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_ : 80 -> 76

```
