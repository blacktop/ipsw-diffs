## libETLDMCDynamic.dylib

> `/usr/lib/libETLDMCDynamic.dylib`

```diff

-1390.0.0.0.0
-  __TEXT.__text: 0x1de68
+1391.0.0.0.0
+  __TEXT.__text: 0x1dea8
   __TEXT.__auth_stubs: 0x500
   __TEXT.__const: 0xdb8
-  __TEXT.__cstring: 0x138c
+  __TEXT.__cstring: 0x1185
   __TEXT.__gcc_except_tab: 0x200
   __TEXT.__unwind_info: 0x338
   __DATA_CONST.__got: 0x50

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 17688AAC-34C9-3F82-93A4-4886D3211E92
+  UUID: B5BA884D-7BD0-3378-8254-3FD117A08A19
   Functions: 254
   Symbols:   412
-  CStrings:  200
+  CStrings:  186
 
Functions:
~ _ETLLOGParseLogHeader : 148 -> 88
~ _ETLLOGParseLog : 476 -> 440
~ _ETLEVENTProcessEvent : 468 -> 696
~ _ETLEVENTProcessEventItem : 8 -> 296
~ _ETLEVENTProcessEventItemTSLength : 500 -> 304
~ _ETLEVENTProcessHeader : 152 -> 60
~ _ETLEVENTParseReport : 336 -> 216
~ _ETLEVENTParseEventReport : 384 -> 468
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
