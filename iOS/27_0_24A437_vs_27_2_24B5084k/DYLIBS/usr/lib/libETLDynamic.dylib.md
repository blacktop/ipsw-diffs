## libETLDynamic.dylib

> `/usr/lib/libETLDynamic.dylib`

```diff

-1585.0.0.0.0
-  __TEXT.__text: 0x47120
+1594.0.0.0.0
+  __TEXT.__text: 0x474c4
   __TEXT.__const: 0x1350
-  __TEXT.__cstring: 0x5069
-  __TEXT.__gcc_except_tab: 0x2a8
-  __TEXT.__unwind_info: 0xb10
+  __TEXT.__cstring: 0x5374
+  __TEXT.__gcc_except_tab: 0x2dc
+  __TEXT.__unwind_info: 0xb38
   __TEXT.__eh_frame: 0x50
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xf8

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x218
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__auth_got: 0x258
+  __AUTH_CONST.__auth_got: 0x288
   __DATA.__data: 0x2c
   __DATA.__common: 0x2
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 715
-  Symbols:   881
-  CStrings:  613
+  Functions: 716
+  Symbols:   892
+  CStrings:  640
 
Symbols:
+ GCC_except_table10
+ _TelephonyUtilGetSystemTime
+ __ZL17_ETLDebugOpenFilev
+ __ZL17gETLDebugStdoutFD
+ __ZN3ctu2fs16create_directoryENS_4llvm9StringRefEtb
+ __ZN3ctu6assignERNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEPKhjbb
+ ___FUNCTION__.ETLEVENTProcessHeader
+ ___stdoutp
+ _fflush
+ _fopen
+ _vfprintf
Functions:
~ _ETLGSDIParseGetFeatureResponse : 260 -> 288
~ _ETLGSDIParseGetECCResponse : 168 -> 192
~ _ETLGSDIPerformGetECC : 796 -> 824
~ __ZL20_ETLDebugPrintStdoutPKcS0_Pc : 4 -> 176
~ __ZL26_ETLDebugPrintBinaryStdoutPKc23ETLDebugPrintBinaryTypePKvj : 4 -> 300
+ __ZL17_ETLDebugOpenFilev
~ _ETLMaverickParseSetGPIOResponse : 348 -> 404
~ _ETLEVENTProcessEvent : 688 -> 456
~ _ETLEVENTProcessEventItem : 296 -> 8
~ _ETLEVENTProcessEventItemTSLength : 304 -> 500
~ _ETLEVENTProcessHeader : 60 -> 152
~ _ETLEVENTParseReport : 208 -> 328
~ _ETLEVENTParseEventReport : 464 -> 376
~ _ETLEVENTReportFree : 132 -> 164
~ _ETLEFS2ParseStatResponse : 384 -> 416
~ _ETLLOGParseLogHeader : 88 -> 148
~ _ETLLOGParseLog : 440 -> 476
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
