## libETLDynamic.dylib

> `/usr/lib/libETLDynamic.dylib`

```diff

-1418.1.0.0.0
-  __TEXT.__text: 0x469dc
-  __TEXT.__auth_stubs: 0x4c0
+1563.0.0.0.0
+  __TEXT.__text: 0x4895c
   __TEXT.__const: 0x1350
-  __TEXT.__cstring: 0x5069
-  __TEXT.__gcc_except_tab: 0x27c
-  __TEXT.__unwind_info: 0x7d0
-  __DATA_CONST.__got: 0x50
+  __TEXT.__cstring: 0x5374
+  __TEXT.__gcc_except_tab: 0x2dc
+  __TEXT.__unwind_info: 0x7f8
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xf8
-  __AUTH_CONST.__auth_got: 0x268
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x218
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__auth_got: 0x288
   __DATA.__data: 0x2c
-  __DATA.__common: 0x8020
+  __DATA.__common: 0x2
   __DATA.__bss: 0x8
   __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x8
+  __DATA_DIRTY.__common: 0x8018
   - /usr/lib/libHDLCDynamic.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: C9448EFA-3252-39B6-8255-656AFF38E493
-  Functions: 724
-  Symbols:   1035
-  CStrings:  613
+  UUID: 0911F2FA-14C4-365C-9738-A7F6FE7338CC
+  Functions: 721
+  Symbols:   1041
+  CStrings:  640
 
Symbols:
+ GCC_except_table10
+ _.str.30
+ _.str.40
+ _.str.48
+ _TelephonyUtilGetSystemTime
+ __ZL17_ETLDebugOpenFilev
+ __ZL17gETLDebugStdoutFD
+ __ZN3ctu2fs16create_directoryENS_4llvm9StringRefEtb
+ __ZN3ctu6assignERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEPKhjbb
+ __ZNSt12length_errorC1B9noe220100EPKc
+ __ZNSt3__110shared_ptrIN5eUICC13ValidatePerso8ResponseEED2B9noe220100Ev
+ __ZNSt3__110shared_ptrIN5eUICC16AuthPersoSession8ResponseEED2B9noe220100Ev
+ __ZNSt3__110shared_ptrIN5eUICC16InitPersoSession8ResponseEED2B9noe220100Ev
+ __ZNSt3__110shared_ptrIN5eUICC20FinalizePersoSession8ResponseEED2B9noe220100Ev
+ __ZNSt3__110shared_ptrIN5eUICC6GetCSN8ResponseEED2B9noe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9noe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ __ZNSt3__120__throw_length_errorB9noe220100EPKc
+ __ZNSt3__124__put_character_sequenceB9noe220100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEED1B9noe220100Ev
+ ___FUNCTION__.ETLEVENTProcessHeader
+ ___stdoutp
+ _fflush
+ _fopen
+ _vfprintf
- _.str.29
- _.str.35
- _.str.46
- _OUTLINED_FUNCTION_39
- _OUTLINED_FUNCTION_40
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_42
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__110shared_ptrIN5eUICC13ValidatePerso8ResponseEED2B9nqe210106Ev
- __ZNSt3__110shared_ptrIN5eUICC16AuthPersoSession8ResponseEED2B9nqe210106Ev
- __ZNSt3__110shared_ptrIN5eUICC16InitPersoSession8ResponseEED2B9nqe210106Ev
- __ZNSt3__110shared_ptrIN5eUICC20FinalizePersoSession8ResponseEED2B9nqe210106Ev
- __ZNSt3__110shared_ptrIN5eUICC6GetCSN8ResponseEED2B9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__124__put_character_sequenceB9nqe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEED1B9nqe210106Ev
CStrings:
+ "%u.%03u %s:"
+ "%u.%03u [%s] %s\n%s"
+ "/private/var/wireless/Library/Logs/CrashReporter/Baseband/"
+ "Buffer Length %u for payload not enough for, need %zu\n"
+ "Buffer Length %u not enough, need %zu for full timestamp\n"
+ "Buffer Length %u not enough, need %zu for truncated timestamp\n"
+ "EFS File Mode: %u\n"
+ "ETLEVENTParseReport"
+ "ETLEVENTProcessEventItemTSLength"
+ "ETLEVENTProcessHeader"
+ "ETLEVENTReportFree"
+ "ETLLOGParseLogHeader"
+ "Failed to process header\n"
+ "Freed %u, count was %u\n"
+ "GPIO State: %u, GPIO, Number of GPIOs: %u\n"
+ "Length %u\n"
+ "Length %u is greater than buffer size %u\n"
+ "Reading Event %u, length flag %u, timeLength %u, bufferLength %u\n"
+ "Received %u bytes\n"
+ "Received %u records\n"
+ "Warning: Buffer Length %u is greater than field length %u\n"
+ "Warning: Failed to open %s for writing\n"
+ "libETL.log"
+ "misc"
+ "recv"
+ "send"
+ "w"

```
