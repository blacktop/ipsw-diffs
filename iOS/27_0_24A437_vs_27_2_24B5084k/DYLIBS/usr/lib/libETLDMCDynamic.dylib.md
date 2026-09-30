## libETLDMCDynamic.dylib

> `/usr/lib/libETLDMCDynamic.dylib`

```diff

-1585.0.0.0.0
-  __TEXT.__text: 0x1dfd4
+1594.0.0.0.0
+  __TEXT.__text: 0x1df8c
   __TEXT.__const: 0xda8
-  __TEXT.__cstring: 0x1185
+  __TEXT.__cstring: 0x138c
   __TEXT.__gcc_except_tab: 0x200
-  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__unwind_info: 0x4b0
   __TEXT.__eh_frame: 0x50
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xd0

   - /usr/lib/libxml2.2.dylib
   Functions: 254
   Symbols:   378
-  CStrings:  186
+  CStrings:  200
 
Functions:
~ _ETLLOGParseLogHeader : 88 -> 148
~ _ETLLOGParseLog : 440 -> 476
~ _ETLEVENTProcessEvent : 688 -> 456
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
