## libETLDMCDynamic.dylib

> `/usr/lib/libETLDMCDynamic.dylib`

```diff

 1418.1.0.0.0
-  __TEXT.__text: 0x1de38
+  __TEXT.__text: 0x1ddf0
   __TEXT.__auth_stubs: 0x500
   __TEXT.__const: 0xdb0
-  __TEXT.__cstring: 0x1185
+  __TEXT.__cstring: 0x138c
   __TEXT.__gcc_except_tab: 0x200
-  __TEXT.__unwind_info: 0x328
+  __TEXT.__unwind_info: 0x330
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0xd0
   __AUTH_CONST.__auth_got: 0x288

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: C75DB28F-3469-3579-B1B4-5686ECF934FC
+  UUID: 4B63F180-5B4A-3E65-8061-3B1D28C6215B
   Functions: 254
   Symbols:   412
-  CStrings:  186
+  CStrings:  200
 
Functions:
~ _ETLLOGParseLogHeader : 88 -> 148
~ _ETLLOGParseLog : 440 -> 476
~ _ETLEVENTProcessEvent : 696 -> 464
~ _ETLEVENTProcessEventItem : 296 -> 8
~ _ETLEVENTProcessEventItemTSLength : 304 -> 500
~ _ETLEVENTProcessHeader : 60 -> 152
~ _ETLEVENTParseReport : 208 -> 328
~ _ETLEVENTParseEventReport : 464 -> 376
~ _ETLEVENTReportFree : 132 -> 164
CStrings:
+ "Buffer Length %u for payload not enough for, need %zu\n"
+ "Buffer Length %u not enough, need %zu for full timestamp\n"
+ "Buffer Length %u not enough, need %zu for truncated timestamp\n"
+ "ETLEVENTParseReport"
+ "ETLEVENTProcessEventItemTSLength"
+ "ETLEVENTProcessHeader"
+ "ETLEVENTReportFree"
+ "ETLLOGParseLogHeader"
+ "Failed to process header\n"
+ "Freed %u, count was %u\n"
+ "Length %u\n"
+ "Length %u is greater than buffer size %u\n"
+ "Reading Event %u, length flag %u, timeLength %u, bufferLength %u\n"
+ "Warning: Buffer Length %u is greater than field length %u\n"

```
