## CoreOptimization

> `/System/Library/PrivateFrameworks/CoreOptimization.framework/CoreOptimization`

```diff

 117.0.0.0.0
-  __TEXT.__text: 0x3e50
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x4e8
-  __TEXT.__cstring: 0x2cf
-  __TEXT.__unwind_info: 0x178
+  __TEXT.__text: 0x4828
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0x4fc
+  __TEXT.__cstring: 0x66e
+  __TEXT.__unwind_info: 0x190
   __DATA_CONST.__got: 0x40
-  __AUTH_CONST.__auth_got: 0x120
+  __AUTH_CONST.__auth_got: 0x128
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 25B4CCAB-9225-3CE0-B75D-9D5295DBCA7C
-  Functions: 29
-  Symbols:   116
-  CStrings:  45
+  UUID: 612C209F-E5A5-3430-B323-FC5E7B076336
+  Functions: 33
+  Symbols:   125
+  CStrings:  48
 
Symbols:
+ __ZN16CoreOptimization4BFGS13UpdateHessianERNS_9hessian_tERKNSt3__18valarrayIdEES7_.cold.1
+ __ZNKSt3__19_BinaryOpINS_10multipliesIdEENS_8valarrayIdEENS_13__scalar_exprIdEEEixB9foe210106Em
+ __ZNKSt3__19_BinaryOpINS_4plusIdEENS_8valarrayIdEENS_10__val_exprINS0_INS_10multipliesIdEES4_NS_13__scalar_exprIdEEEEEEEixB9foe210106Em
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__116__pad_and_outputB9foe210106IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__124__put_character_sequenceB9foe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__14endlB9foe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_
+ __ZNSt3__1lsB9foe210106INS_11char_traitsIcEEEERNS_13basic_ostreamIcT_EES6_PKc
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ __ZlsRNSt3__113basic_ostreamIcNS_11char_traitsIcEEEERKN16CoreOptimization9hessian_tE.cold.1
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__116__pad_and_outputB8ne200100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__14endlB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_
- __ZNSt3__1lsB8ne200100INS_11char_traitsIcEEEERNS_13basic_ostreamIcT_EES6_PKc
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBZPXDgY3YPpe1EgoXrx0pqESX7xaTdMtE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBZPXDgY3YPpe1EgoXrx0pqESX7xaTdMtE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/valarray:825: libc++ Hardening assertion __i < size() failed: valarray::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoJugBZPXDgY3YPpe1EgoXrx0pqESX7xaTdMtE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/valarray:830: libc++ Hardening assertion __i < size() failed: valarray::operator[] index out of bounds\n"

```
