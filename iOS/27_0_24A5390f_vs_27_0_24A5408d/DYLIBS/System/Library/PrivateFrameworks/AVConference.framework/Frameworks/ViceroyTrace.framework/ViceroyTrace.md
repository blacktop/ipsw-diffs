## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2235.57.1.0.0
-  __TEXT.__text: 0xb9250
+2235.63.1.1.0
+  __TEXT.__text: 0xb9378
   __TEXT.__objc_methlist: 0x9338
   __TEXT.__const: 0x27f0
-  __TEXT.__cstring: 0xf45c
-  __TEXT.__oslogstring: 0xf2dd
+  __TEXT.__cstring: 0xf46e
+  __TEXT.__oslogstring: 0xf32a
   __TEXT.__gcc_except_tab: 0x38c
   __TEXT.__dlopen_cstrs: 0xa0
   __TEXT.__unwind_info: 0x1870

   __DATA_CONST.__objc_arraydata: 0x220
   __DATA_CONST.__got: 0x298
   __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0xede0
-  __AUTH_CONST.__objc_const: 0x178f8
+  __AUTH_CONST.__cfstring: 0xee00
+  __AUTH_CONST.__objc_const: 0x17918
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0x480
+  __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__auth_got: 0x6d8
   __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0x21f8
+  __DATA.__objc_ivar: 0x21fc
   __DATA.__data: 0x750
   __DATA.__bss: 0x78
   __DATA.__common: 0x1

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4248
-  Symbols:   8764
-  CStrings:  3350
+  Functions: 4249
+  Symbols:   8766
+  CStrings:  3352
 
Symbols:
+ _CFPropertyListCreateDeepCopy
+ _OBJC_IVAR_$_VCAggregatorAirPlay._reportedMediaStreamType
Functions:
~ -[VCAggregatorAirPlay initWithDelegate:options:] : 1388 -> 1408
~ -[VCAggregatorAirPlay composeSegmentReport:] : 904 -> 956
~ -[VCAggregatorAirPlay updateSenderVideoStreamConfiguration:] : 448 -> 488
~ -[RTCReportingAgent reportPeriodicTelemetryWithCategory:type:payload:lock:] : 368 -> 420
~ -[VCPersistentDataStore finalizeInternal] : 144 -> 128
~ -[VCPersistentDataStore closeDatabase] : 100 -> 104
~ ___VCPersistentDataStore_DumpMessage_block_invoke_2 : 296 -> 288
~ -[VCAggregatorHomeKitAudio dispatchedAggregatedSessionReport] : 324 -> 348
~ -[RTCReportingAgent reportPeriodicTelemetryWithCategory:type:payload:lock:].cold.1 : 124 -> 128
+ -[RTCReportingAgent reportPeriodicTelemetryWithCategory:type:payload:lock:].cold.3
CStrings:
+ "ReportingVC [%s] %s:%d Failed to populate payload snapshot for Periodic Task"
+ "VCMediaStreamType"
```
