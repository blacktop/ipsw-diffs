## NLPLearner

> `/System/Library/PrivateFrameworks/NLPLearner.framework/NLPLearner`

```diff

 69.0.0.0.0
-  __TEXT.__text: 0xee44
+  __TEXT.__text: 0xeda8
   __TEXT.__auth_stubs: 0x8a0
   __TEXT.__objc_methlist: 0xb9c
   __TEXT.__const: 0xb8
   __TEXT.__cstring: 0x1147
   __TEXT.__oslogstring: 0xd46
   __TEXT.__ustring: 0x58
-  __TEXT.__gcc_except_tab: 0xe9c
-  __TEXT.__unwind_info: 0x590
+  __TEXT.__gcc_except_tab: 0xea4
+  __TEXT.__unwind_info: 0x588
   __TEXT.__objc_classname: 0x253
   __TEXT.__objc_methname: 0x211b
   __TEXT.__objc_methtype: 0x3c2

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C1D9D56F-5650-332A-AC23-7BA1BD374F5C
+  UUID: 4753E942-454F-318F-AE04-8B1F3CEA1310
   Functions: 339
-  Symbols:   1534
+  Symbols:   1533
   CStrings:  887
 
Symbols:
+ __ZN10applesauce2CF8ArrayRefD2Ev
+ __ZN10applesauce2CF9ObjectRefIPK9__CFArrayED2Ev
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100EmRKf
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE9push_backB8ne200100ERKj
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZnwmSt19__type_descriptor_t
- __ZN10applesauce2CF8ArrayRef8from_getEPK9__CFArray
- __ZN10applesauce2CF8ArrayRefD1Ev
- __ZN10applesauce2CF9ObjectRefIPK9__CFArrayED1Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102EmRKf
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
Functions:
~ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em -> __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em : 68 -> 60
~ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m -> __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m : 56 -> 72
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE7reserveEm : 164 -> 160
~ ___66-[NLPLearnerLanguageModelingData loadFromCoreDuet:limitSamplesTo:]_block_invoke : 1056 -> 708
~ -[NLPLearnerLanguageModelingData nextTrainingDataBatch:] -> __ZNSt3__16vectorIjNS_9allocatorIjEEE9push_backB8ne200100ERKj : 580 -> 224
~ -[NLPLearnerLanguageModelingData nextEvaluationDataPoint] -> -[NLPLearnerLanguageModelingData nextTrainingDataBatch:] : 668 -> 580
~ __ZN10applesauce2CF8ArrayRefD1Ev -> -[NLPLearnerLanguageModelingData nextEvaluationDataPoint] : 52 -> 824
~ __ZN10applesauce2CF8ArrayRef8from_getEPK9__CFArray -> __ZN10applesauce2CF9ObjectRefIPK9__CFArrayED2Ev : 188 -> 52
~ __ZN10applesauce2CF7details20CFArray_get_value_toINSt3__16vectorIfNS3_9allocatorIfEEEEEET_PK9__CFArray : 368 -> 364

```
