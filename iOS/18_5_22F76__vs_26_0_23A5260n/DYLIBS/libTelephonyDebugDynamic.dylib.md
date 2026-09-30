## libTelephonyDebugDynamic.dylib

> `/usr/lib/libTelephonyDebugDynamic.dylib`

```diff

-6161.0.0.0.0
-  __TEXT.__text: 0x1bc4
+6318.0.0.0.0
+  __TEXT.__text: 0x1c68
   __TEXT.__auth_stubs: 0x360
   __TEXT.__gcc_except_tab: 0x228
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0x15c
   __TEXT.__oslogstring: 0x1e
   __TEXT.__unwind_info: 0x1a0
-  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0xc0
   __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0x110

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 3C5DDA73-F099-3A2C-89D9-709DF1A6FF84
+  UUID: 1E12EF52-054C-3CF9-A01C-F8B6E775F5FC
   Functions: 42
-  Symbols:   170
+  Symbols:   173
   CStrings:  20
 
Symbols:
+ GCC_except_table18
+ GCC_except_table21
+ GCC_except_table37
+ __ZNKRSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne200100Ev
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__16localeC1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
- GCC_except_table17
- GCC_except_table19
- GCC_except_table36
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne190102IS4_EENS_12basic_stringIcS2_T_EERKS8_
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
Functions:
~ ____ZN20TelephonySystemTrace13watchdogStartEjNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN8dispatch5blockIU13block_pointerFvvEEESB__block_invoke_3 : 1212 -> 1336
~ __ZNK20TelephonySystemTrace16writeTraceBufferEv -> __ZNKRSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne200100Ev : 372 -> 208
~ ____ZN20TelephonySystemTrace13watchdogStartEjNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN8dispatch5blockIU13block_pointerFvvEEESB__block_invoke_4 -> __ZNK20TelephonySystemTrace16writeTraceBufferEv : 16 -> 372
~ ___copy_helper_block_e8_32c43_ZTSN8dispatch5blockIU13block_pointerFvvEEE -> ____ZN20TelephonySystemTrace13watchdogStartEjNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN8dispatch5blockIU13block_pointerFvvEEESB__block_invoke_4 : 52 -> 16
~ ___destroy_helper_block_e8_32c43_ZTSN8dispatch5blockIU13block_pointerFvvEEE -> ___copy_helper_block_e8_32c43_ZTSN8dispatch5blockIU13block_pointerFvvEEE : 36 -> 52
~ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev -> ___destroy_helper_block_e8_32c43_ZTSN8dispatch5blockIU13block_pointerFvvEEE : 260 -> 36
~ __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m -> __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev : 812 -> 288
~ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne190102IS4_EENS_12basic_stringIcS2_T_EERKS8_ -> __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m : 208 -> 812
~ ___TelephonyBasebandWatchdogStartWithStackshot_block_invoke : 256 -> 268

```
