## libETLDMCDynamic.dylib

> `/usr/lib/libETLDMCDynamic.dylib`

```diff

-1391.0.0.0.0
-  __TEXT.__text: 0x1dea8
+1397.0.0.0.0
+  __TEXT.__text: 0x1de68
   __TEXT.__auth_stubs: 0x500
   __TEXT.__const: 0xdb8
-  __TEXT.__cstring: 0x1185
+  __TEXT.__cstring: 0x138c
   __TEXT.__gcc_except_tab: 0x200
   __TEXT.__unwind_info: 0x338
   __DATA_CONST.__got: 0x50

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: B5BA884D-7BD0-3378-8254-3FD117A08A19
+  UUID: 271D12B5-89C5-3A08-9CE4-F14E969493BA
   Functions: 254
   Symbols:   412
-  CStrings:  186
+  CStrings:  200
 
Functions:
~ _ETLLOGParseLogHeader : 88 -> 148
~ _ETLLOGParseLog : 440 -> 476
~ _ETLEVENTProcessEvent : 696 -> 468
~ _ETLEVENTProcessEventItem : 296 -> 8
~ _ETLEVENTProcessEventItemTSLength : 304 -> 500
~ _ETLEVENTProcessHeader : 60 -> 152
~ _ETLEVENTParseReport : 216 -> 336
~ _ETLEVENTParseEventReport : 468 -> 384
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
