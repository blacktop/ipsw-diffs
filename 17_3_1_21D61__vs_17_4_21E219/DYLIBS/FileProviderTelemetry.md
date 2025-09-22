## FileProviderTelemetry

> `/System/Library/PrivateFrameworks/FileProviderTelemetry.framework/FileProviderTelemetry`

```diff

-1703.80.16.0.0
-  __TEXT.__text: 0x19d0
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x108
-  __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x30
+1835.102.2.0.0
+  __TEXT.__text: 0x1e00
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_methlist: 0x120
+  __TEXT.__const: 0x18
+  __TEXT.__gcc_except_tab: 0x50
   __TEXT.__cstring: 0x10c
-  __TEXT.__oslogstring: 0xc4
-  __TEXT.__unwind_info: 0xd4
+  __TEXT.__oslogstring: 0xec
+  __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_classname: 0x37
-  __TEXT.__objc_methname: 0x5c1
-  __TEXT.__objc_methtype: 0x188
-  __TEXT.__objc_stubs: 0x4a0
+  __TEXT.__objc_methname: 0x63f
+  __TEXT.__objc_methtype: 0x185
+  __TEXT.__objc_stubs: 0x4e0
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x150
-  __DATA_CONST.__objc_selrefs: 0x170
-  __AUTH_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_const: 0x170
+  __DATA_CONST.__objc_selrefs: 0x188
+  __DATA_CONST.__objc_classrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_const: 0xd8
-  __AUTH_CONST.__auth_got: 0x1f0
-  __DATA.__objc_classrefs: 0x40
-  __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x1c
+  __AUTH_CONST.__auth_got: 0x1f8
+  __DATA.__objc_ivar: 0x20
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 41D67E8B-71CD-3354-B152-DE108E0DCE87
-  Functions: 36
-  Symbols:   231
-  CStrings:  111
+  UUID: 31406C44-6894-371C-BDB2-E8BA1172E589
+  Functions: 40
+  Symbols:   247
+  CStrings:  116
 
Symbols:
+ -[FPRTCReportingSession initWithWithCommonProperties:manager:]
+ -[FPRTCReportingSession initWithWithCommonProperties:manager:].cold.1
+ -[FPRTCReportingSessionManager sessionWithCommonProperties:]
+ -[FPRTCReportingSessionManager waitUntilTelemetrySessionIsAvailable:retryDuration:]
+ GCC_except_table10
+ GCC_except_table19
+ GCC_except_table26
+ _FPTelemetrySessionPropertyProviderIDKey
+ _FPTelemetrySessionPropertyProviderVersionKey
+ _OBJC_IVAR_$_FPRTCReportingSession._commonProperties
+ ___83-[FPRTCReportingSessionManager postMultipleReports:type:userinfo:session:observer:]_block_invoke.16
+ ___83-[FPRTCReportingSessionManager postMultipleReports:type:userinfo:session:observer:]_block_invoke.16.cold.1
+ ___83-[FPRTCReportingSessionManager postMultipleReports:type:userinfo:session:observer:]_block_invoke.17
+ ___83-[FPRTCReportingSessionManager postMultipleReports:type:userinfo:session:observer:]_block_invoke.17.cold.1
+ ___83-[FPRTCReportingSessionManager waitUntilTelemetrySessionIsAvailable:retryDuration:]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSArray"8lr40l8s32l8
+ ___block_literal_global.27
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$initWithWithCommonProperties:manager:
+ _objc_msgSend$sessionWithCommonProperties:
+ _sleep
- -[FPRTCReportingSession initWithProviderID:version:manager:]
- -[FPRTCReportingSession initWithProviderID:version:manager:].cold.1
- GCC_except_table23
- GCC_except_table9
- ___83-[FPRTCReportingSessionManager postMultipleReports:type:userinfo:session:observer:]_block_invoke.10
- ___83-[FPRTCReportingSessionManager postMultipleReports:type:userinfo:session:observer:]_block_invoke.11
- ___83-[FPRTCReportingSessionManager postMultipleReports:type:userinfo:session:observer:]_block_invoke.11.cold.1
- ___block_literal_global.21
- _objc_msgSend$initWithProviderID:version:manager:
CStrings:
+ "\x06"
+ "[ERROR] Failed to configure RTC session"
+ "_commonProperties"
+ "addEntriesFromDictionary:"
+ "initWithWithCommonProperties:manager:"
+ "sessionWithCommonProperties:"
+ "v32@0:8Q16Q24"
+ "waitUntilTelemetrySessionIsAvailable:retryDuration:"
- "\x05"
- "@40@0:8@16@24@32"
- "initWithProviderID:version:manager:"

```
