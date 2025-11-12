## libETLDynamic.dylib

> `/usr/lib/libETLDynamic.dylib`

```diff

-1399.2.0.0.0
-  __TEXT.__text: 0x46fc8
-  __TEXT.__auth_stubs: 0x530
+1399.4.0.0.0
+  __TEXT.__text: 0x46b98
+  __TEXT.__auth_stubs: 0x4c0
   __TEXT.__const: 0x1360
-  __TEXT.__cstring: 0x5335
-  __TEXT.__gcc_except_tab: 0x2b4
-  __TEXT.__unwind_info: 0x800
-  __DATA_CONST.__got: 0x58
+  __TEXT.__cstring: 0x502a
+  __TEXT.__gcc_except_tab: 0x280
+  __TEXT.__unwind_info: 0x7e0
+  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0xf8
-  __AUTH_CONST.__auth_got: 0x2a0
+  __AUTH_CONST.__auth_got: 0x268
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
-  UUID: F1B6F6AF-C89E-33C7-8447-CF116E173246
-  Functions: 725
-  Symbols:   1054
-  CStrings:  640
+  UUID: DB110D90-BB18-390F-B105-6D49437C41B2
+  Functions: 724
+  Symbols:   1035
+  CStrings:  613
 
Symbols:
+ _.str.29
+ _.str.35
+ _.str.46
- GCC_except_table10
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
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev : 24 -> 16
~ __ZNSt3__120__throw_length_errorB8ne200100EPKc : 92 -> 84
~ __ZNSt12length_errorC1B8ne200100EPKc : 52 -> 60
~ __ZL20_ETLDebugPrintStdoutPKcS0_Pc : 188 -> 4
~ __ZL26_ETLDebugPrintBinaryStdoutPKc23ETLDebugPrintBinaryTypePKvj : 300 -> 4
- __ZL17_ETLDebugOpenFilev
~ _ETLMaverickParseSetGPIOResponse : 396 -> 340
~ _ETLEVENTProcessEvent : 468 -> 696
~ _ETLEVENTProcessEventItem : 8 -> 296
~ _ETLEVENTProcessEventItemTSLength : 500 -> 304
~ _ETLEVENTProcessHeader : 152 -> 60
~ _ETLEVENTParseReport : 336 -> 216
~ _ETLEVENTParseEventReport : 384 -> 468
~ _ETLEVENTReportFree : 164 -> 132
~ _ETLEFS2ParseStatResponse : 416 -> 384
~ _ETLLOGParseLogHeader : 148 -> 88
~ _ETLLOGParseLog : 476 -> 440
~ _LZ4_compress_limitedOutput_withState : 1740 -> 1728
~ _LZ4_compress_limitedOutput_continue : 1232 -> 1220
CStrings:
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
