## libETLDMCDynamic.dylib

> `/usr/lib/libETLDMCDynamic.dylib`

```diff

 1585.0.0.0.0
-  __TEXT.__text: 0x1e134
+  __TEXT.__text: 0x1e17c
   __TEXT.__const: 0xda8
-  __TEXT.__cstring: 0x138c
+  __TEXT.__cstring: 0x1185
   __TEXT.__gcc_except_tab: 0x200
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__unwind_info: 0x328
   __TEXT.__eh_frame: 0x48
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xd0

   - /usr/lib/libxml2.2.dylib
   Functions: 254
   Symbols:   378
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
