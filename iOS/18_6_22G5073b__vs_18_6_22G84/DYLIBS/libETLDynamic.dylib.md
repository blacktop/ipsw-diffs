## libETLDynamic.dylib

> `/usr/lib/libETLDynamic.dylib`

```diff

 1249.1.0.0.0
-  __TEXT.__text: 0x43e9c
-  __TEXT.__auth_stubs: 0x570
+  __TEXT.__text: 0x43a64
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__const: 0x1350
-  __TEXT.__cstring: 0x535a
-  __TEXT.__gcc_except_tab: 0x2a8
-  __TEXT.__unwind_info: 0x7f0
-  __DATA_CONST.__got: 0x50
+  __TEXT.__cstring: 0x504c
+  __TEXT.__gcc_except_tab: 0x280
+  __TEXT.__unwind_info: 0x7d0
+  __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0xf8
-  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH_CONST.__auth_got: 0x288
   __AUTH_CONST.__const: 0x218
   __DATA.__data: 0x2c
   __DATA.__common: 0x8020
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__data: 0x10
   - /usr/lib/libHDLCDynamic.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 99B3C92D-E02E-387C-8434-0BB0F6328534
-  Functions: 728
-  Symbols:   1064
-  CStrings:  640
+  UUID: CD51634E-CC42-36B3-9BB0-70DF5775171D
+  Functions: 727
+  Symbols:   1045
+  CStrings:  612
 
Symbols:
+ _.str.29
+ _.str.35
+ _.str.46
- GCC_except_table8
- GCC_except_table9
- _.str.30
- _.str.40
- _.str.48
- _TelephonyUtilGetSystemTime
- __ZL17_ETLDebugOpenFilev
- __ZL17gETLDebugStdoutFD
- __ZN3ctu2fs16create_directoryENS_4llvm9StringRefEtb
- __ZN3ctu6assignERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEPKhjbb
- __ZNSt12out_of_rangeD0Ev
- __ZNSt12out_of_rangeD1Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
- __ZTISt12out_of_range
- __ZTVSt12out_of_range
- ___FUNCTION__.ETLEVENTProcessHeader
- ___stdoutp
- _fflush
- _fopen
- _vfprintf
Functions:
~ _ETLGSDIParseGetFeatureResponse : 288 -> 260
~ _ETLGSDIParseGetECCResponse : 192 -> 168
~ _ETLGSDIPerformGetECC : 824 -> 796
~ __ZN18ETLFirmwareVersion21initWithVersionStringERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 948 -> 936
~ __ZN18ETLFirmwareVersion18initWithFolderNameERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 308 -> 304
~ __ZNK18ETLFirmwareVersion11getAsStringEv : 2528 -> 2812
~ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev : 24 -> 16
~ __ZNSt3__120__throw_length_errorB8ne190102EPKc : 92 -> 84
~ __ZNSt12length_errorC1B8ne190102EPKc : 52 -> 60
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_no_aliasILb1EEERS5_PKcm : 196 -> 192
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_no_aliasILb0EEERS5_PKcm : 284 -> 280
~ __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m : 852 -> 848
~ __ZL20_ETLDebugPrintStdoutPKcS0_Pc : 188 -> 4
~ __ZL26_ETLDebugPrintBinaryStdoutPKc23ETLDebugPrintBinaryTypePKvj : 300 -> 4
- __ZL17_ETLDebugOpenFilev
~ _ETLMaverickParseSetGPIOResponse : 396 -> 340
~ _ETLEVENTProcessEvent : 468 -> 696
~ _ETLEVENTProcessEventItemTSLength : 500 -> 304
~ _ETLEVENTProcessHeader : 152 -> 60
~ _ETLEVENTParseReport : 336 -> 216
~ _ETLEVENTParseEventReport : 384 -> 468
~ _ETLEVENTReportFree : 164 -> 132
~ _ETLEFS2ParseStatResponse : 416 -> 384
~ _ETLLOGParseLogHeader : 148 -> 88
~ _ETLLOGParseLog : 476 -> 440
CStrings:
- " )"
- "%u.%03u %s:"
- "%u.%03u [%s] %s\n%s"
- "/private/var/wireless/Library/Logs/CrashReporter/Baseband/"
- "Buffer Length %u for payload not enough for, need %zu\n"
- "Buffer Length %u not enough, need %zu for full timestamp\n"
- "Buffer Length %u not enough, need %zu for truncated timestamp\n"
- "EFS File Mode: %u\n"
- "ETLEVENTParseReport"
- "ETLEVENTProcessEventItemTSLength"
- "ETLEVENTProcessHeader"
- "ETLEVENTReportFree"
- "ETLLOGParseLogHeader"
- "Failed to process header\n"
- "Freed %u, count was %u\n"
- "GPIO State: %u, GPIO, Number of GPIOs: %u\n"
- "Length %u\n"
- "Length %u is greater than buffer size %u\n"
- "Reading Event %u, length flag %u, timeLength %u, bufferLength %u\n"
- "Received %u bytes\n"
- "Received %u records\n"
- "Warning: Buffer Length %u is greater than field length %u\n"
- "Warning: Failed to open %s for writing\n"
- "libETL.log"
- "misc"
- "recv"
- "send"
- "w"

```
