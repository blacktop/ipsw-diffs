## GPUToolsDiagnostics

> `/System/Library/PrivateFrameworks/GPUToolsDiagnostics.framework/GPUToolsDiagnostics`

```diff

-314.10.0.0.0
-  __TEXT.__text: 0xaf74
-  __TEXT.__auth_stubs: 0x4a0
+314.12.0.0.0
+  __TEXT.__text: 0xaf04
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_stubs: 0xc00
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0x1d4
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x1440
-  __TEXT.__cstring: 0x247f
+  __TEXT.__cstring: 0x234c
   __TEXT.__objc_methname: 0x101f
   __TEXT.__objc_classname: 0x6c
   __TEXT.__objc_methtype: 0x1de
   __TEXT.__oslogstring: 0x79
   __TEXT.__unwind_info: 0x4e0
-  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x2c8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7FD35C80-E1FB-326B-B7EC-D32239E0950C
+  UUID: AD753FFD-FA75-3B40-A596-416239D54C73
   Functions: 111
-  Symbols:   465
-  CStrings:  454
+  Symbols:   464
+  CStrings:  453
 
Symbols:
+ __ZNSt3__119__allocate_at_leastB9nqn210106INS_9allocatorIPiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeImNS_6vectorImNS1_ImEEEEEEPvEEEEEclB9nqn210106EPS9_
+ __ZNSt3__16vectorIN8GPUTools4Diag9CallstackENS_9allocatorIS3_EEE20__throw_length_errorB9nqn210106Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9nqn210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9nqn210106v
- __ZNSt3__119__allocate_at_leastB9fon210106INS_9allocatorIPiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeImNS_6vectorImNS1_ImEEEEEEPvEEEEEclB9fon210106EPS9_
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIN8GPUTools4Diag9CallstackENS_9allocatorIS3_EEE20__throw_length_errorB9fon210106Ev
- __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9fon210106Ev
- __ZSt28__throw_bad_array_new_lengthB9fon210106v
Functions:
~ ____ZN8GPUTools4Diag14BacktraceStore15InsertBacktraceENS0_9CallstackEm_block_invoke : 1408 -> 1352
~ ____ZN8GPUTools4Diag14BacktraceStore15RemoveBacktraceEm_block_invoke : 1784 -> 1728
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJInugDz3Hivhcv6JwAyROPneKktez0TvG7LEXg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
