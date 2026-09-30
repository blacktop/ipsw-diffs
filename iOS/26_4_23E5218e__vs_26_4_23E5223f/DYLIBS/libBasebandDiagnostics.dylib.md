## libBasebandDiagnostics.dylib

> `/usr/lib/libBasebandDiagnostics.dylib`

```diff

-1417.0.0.0.0
-  __TEXT.__text: 0xd3b4
-  __TEXT.__auth_stubs: 0x900
+1418.1.0.0.0
+  __TEXT.__text: 0xd3b8
+  __TEXT.__auth_stubs: 0x8f0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x338
   __TEXT.__gcc_except_tab: 0x154c
-  __TEXT.__cstring: 0x1396
+  __TEXT.__cstring: 0x1233
   __TEXT.__oslogstring: 0x95f
   __TEXT.__unwind_info: 0x480
   __TEXT.__objc_classname: 0x1

   __DATA_CONST.__const: 0x650
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__auth_got: 0x488
   __AUTH_CONST.__const: 0x230
   __AUTH_CONST.__cfstring: 0x12c0
   __DATA.__data: 0x50

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1340F820-00B2-36B5-8DA8-E1AF9570D364
+  UUID: C249F684-FEE7-3CF6-B6A9-793D6EDC4CA7
   Functions: 150
-  Symbols:   681
-  CStrings:  475
+  Symbols:   680
+  CStrings:  474
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__110shared_ptrI19BasebandDiagnosticsED2B9nqe210106Ev
+ __ZNSt3__110shared_ptrIN3abm6client7ManagerEED1B9nqe210106Ev
+ __ZNSt3__110shared_ptrIN3ctu7GestaltEED1B9nqe210106Ev
+ __ZNSt3__110shared_ptrIN5radio6OpModeEED2B9nqe210106Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9nqe210106Ev
+ __ZNSt3__116__pad_and_outputB9nqe210106IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106Ev
+ __ZNSt3__120__throw_bad_weak_ptrB9nqe210106Ev
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__124__put_character_sequenceB9nqe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB9nqe210106INS_11__wrap_iterIPhEES7_EES7_NS5_IPKhEET_T0_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__110shared_ptrI19BasebandDiagnosticsED2B9foe210106Ev
- __ZNSt3__110shared_ptrIN3abm6client7ManagerEED1B9foe210106Ev
- __ZNSt3__110shared_ptrIN3ctu7GestaltEED1B9foe210106Ev
- __ZNSt3__110shared_ptrIN5radio6OpModeEED2B9foe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9foe210106Ev
- __ZNSt3__116__pad_and_outputB9foe210106IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106Ev
- __ZNSt3__120__throw_bad_weak_ptrB9foe210106Ev
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__124__put_character_sequenceB9foe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB9foe210106INS_11__wrap_iterIPhEES7_EES7_NS5_IPKhEET_T0_l
- __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB9foe210106Ev
Functions:
~ __ZNK12TelephonyXPC6Result8describeEv : 1280 -> 1284
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJRnugBJQVh_0UvyFSAukEw4XJM6nZ8AmFIwcoA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
