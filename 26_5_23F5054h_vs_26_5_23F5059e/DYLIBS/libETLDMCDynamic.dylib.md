## libETLDMCDynamic.dylib

> `/usr/lib/libETLDMCDynamic.dylib`

```diff

 1418.1.0.0.0
-  __TEXT.__text: 0x1ddf0
+  __TEXT.__text: 0x1de38
   __TEXT.__auth_stubs: 0x500
   __TEXT.__const: 0xdb0
-  __TEXT.__cstring: 0x138c
+  __TEXT.__cstring: 0x1185
   __TEXT.__gcc_except_tab: 0x200
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__unwind_info: 0x328
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0xd0
   __AUTH_CONST.__auth_got: 0x288

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: A69951A5-287D-369F-8C62-07AA1C99ADF7
+  UUID: D124EB10-5739-3BFC-87A0-4BCB394A4E64
   Functions: 254
   Symbols:   412
-  CStrings:  200
+  CStrings:  186
 
Functions:
~ _ETLLOGParseLogHeader : 148 -> 88
~ _ETLLOGParseLog : 476 -> 440
~ _ETLEVENTProcessEvent : 464 -> 696
~ _ETLEVENTProcessEventItem : 8 -> 296
~ _ETLEVENTProcessEventItemTSLength : 500 -> 304
~ _ETLEVENTProcessHeader : 152 -> 60
~ _ETLEVENTParseReport : 328 -> 208
~ _ETLEVENTParseEventReport : 376 -> 464
~ _ETLEVENTReportFree : 164 -> 132
CStrings:
- "Buffer Length %u for payload not enough for, need %zu\n"
- "Buffer Length %u not enough, need %zu for full timestamp\n"
- "Buffer Length %u not enough, need %zu for truncated timestamp\n"
- "ETLEVENTParseReport"
- "ETLEVENTProcessEventItemTSLength"
- "ETLEVENTProcessHeader"
- "ETLEVENTReportFree"
- "ETLLOGParseLogHeader"
- "Failed to process header\n"
- "Freed %u, count was %u\n"
- "Length %u\n"
- "Length %u is greater than buffer size %u\n"
- "Reading Event %u, length flag %u, timeLength %u, bufferLength %u\n"
- "Warning: Buffer Length %u is greater than field length %u\n"

```
