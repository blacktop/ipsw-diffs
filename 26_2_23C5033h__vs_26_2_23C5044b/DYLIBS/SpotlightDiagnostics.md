## SpotlightDiagnostics

> `/System/Library/PrivateFrameworks/SpotlightDiagnostics.framework/SpotlightDiagnostics`

```diff

-2400.17.1.0.0
-  __TEXT.__text: 0x20c4
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x118
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x302
-  __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__oslogstring: 0x51
-  __TEXT.__unwind_info: 0xf8
+2400.18.100.0.0
+  __TEXT.__text: 0x240c
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_methlist: 0x120
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x334
+  __TEXT.__gcc_except_tab: 0x188
+  __TEXT.__oslogstring: 0xcc
+  __TEXT.__unwind_info: 0x110
   __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0x617
-  __TEXT.__objc_methtype: 0xe3
-  __TEXT.__objc_stubs: 0x5e0
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__objc_methname: 0x69e
+  __TEXT.__objc_methtype: 0xf1
+  __TEXT.__objc_stubs: 0x680
+  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d0
+  __DATA_CONST.__objc_selrefs: 0x200
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x380
+  __AUTH_CONST.__cfstring: 0x3e0
   __AUTH_CONST.__objc_const: 0x2e0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x24

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 713080B5-92C6-325A-A1CE-9565BC62DFD1
-  Functions: 56
-  Symbols:   286
-  CStrings:  156
+  UUID: AE54DA4D-C977-30D3-9585-906438D4E6D4
+  Functions: 61
+  Symbols:   306
+  CStrings:  173
 
Symbols:
+ -[SDCoreSpotlightDiagnosticClient copySpotlightIndexDropsToDirectory:forDays:]
+ -[SDCoreSpotlightDiagnosticClient copySpotlightIndexDropsToDirectory:forDays:].cold.1
+ GCC_except_table23
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OUTLINED_FUNCTION_0
+ ___60-[SDCoreSpotlightDiagnosticClient getSpotlightHeartbeatData]_block_invoke.cold.1
+ ___78-[SDCoreSpotlightDiagnosticClient copySpotlightIndexDropsToDirectory:forDays:]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e28_v24?0"NSData"8"NSError"16lr40l8s32l8
+ __os_log_impl
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$date
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$stringFromDate:
+ _objc_release_x25
+ _objc_retain_x25
- _NSHomeDirectory
- ___block_descriptor_56_e8_32s40r48r_e28_v24?0"NSData"8"NSError"16lr40l8r48l8s32l8
CStrings:
+ ","
+ "/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/Search"
+ "@28@0:8@16I24"
+ "analytics:copyreports:%@:%@"
+ "completed index drop reports copy"
+ "componentsSeparatedByString:"
+ "copySpotlightIndexDropsToDirectory:forDays:"
+ "date"
+ "dateByAddingTimeInterval:"
+ "got heartbeat data"
+ "setDateFormat:"
+ "stringFromDate:"
+ "timed out copying index drop reports"
+ "timed out getting heartbeat data"
+ "yyyy-MM-dd"
- "%@/Library/Logs/CrashReporter/DiagnosticLogs/Search"

```
