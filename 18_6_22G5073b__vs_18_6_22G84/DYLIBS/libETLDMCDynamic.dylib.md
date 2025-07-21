## libETLDMCDynamic.dylib

> `/usr/lib/libETLDMCDynamic.dylib`

```diff

 1249.1.0.0.0
-  __TEXT.__text: 0x1b1d0
+  __TEXT.__text: 0x1b0f0
   __TEXT.__auth_stubs: 0x500
   __TEXT.__const: 0xdb8
-  __TEXT.__cstring: 0x1388
+  __TEXT.__cstring: 0x1181
   __TEXT.__gcc_except_tab: 0x200
   __TEXT.__unwind_info: 0x310
   __DATA_CONST.__got: 0x48

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: E6E6781B-4B7E-3A09-8D49-906B51607E74
+  UUID: D7187543-E7BA-36C9-9BF0-5AEC23C21039
   Functions: 254
   Symbols:   411
-  CStrings:  199
+  CStrings:  185
 
Functions:
~ _ETLLOGParseLogHeader : 148 -> 88
~ _ETLLOGParseLog : 476 -> 440
~ _ETLEVENTProcessEvent : 468 -> 696
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
