## QueryUnderstanding

> `/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding`

```diff

-  __TEXT.__text: 0x70a0
+  __TEXT.__text: 0x6fcc
   __TEXT.__objc_methlist: 0x754
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0xf55
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0xe22
   __TEXT.__oslogstring: 0x59a
   __TEXT.__gcc_except_tab: 0x94c
   __TEXT.__unwind_info: 0x2b0

   - /usr/lib/libobjc.A.dylib
   Functions: 143
   Symbols:   735
-  CStrings:  296
+  CStrings:  295
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ __ZNSt12length_errorC1B9fqe220106EPKc
+ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorIfEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__120__throw_length_errorB9fqe220106EPKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB9fqe220106Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB9fqe220106IPfS5_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9fqe220106Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9fqe220106Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9fqe220106EmRKf
+ __ZSt28__throw_bad_array_new_lengthB9fqe220106v
+ _objc_retain_x28
- __ZNSt12length_errorC1B9foe220106EPKc
- __ZNSt3__119__allocate_at_leastB9foe220106INS_9allocatorIfEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
- __ZNSt3__120__throw_length_errorB9foe220106EPKc
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB9foe220106Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB9foe220106IPfS5_EEvT_T0_m
- __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9foe220106Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9foe220106Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9foe220106EmRKf
- __ZSt28__throw_bad_array_new_lengthB9foe220106v
Functions:
~ -[U2HeadWrapper getTokenScoresfromScoreTensor:intentIndex:tokens:subtokenLenForTokens:subtokens:scoreFromSubtokenScores:] : 1388 -> 1284
~ -[U2HeadWrapper mapLogitsToLabels:queryString:queryID:intentHint:tokens:subtokenLenForTokens:subtokens:] : 2360 -> 2252
CStrings:
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:414: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
