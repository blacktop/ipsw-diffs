## OSAnalytics

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics`

```diff

-927.80.2.0.0
-  __TEXT.__text: 0x4a924
-  __TEXT.__auth_stubs: 0x1b50
-  __TEXT.__objc_methlist: 0x1c78
+934.100.27.0.0
+  __TEXT.__text: 0x4beb0
+  __TEXT.__auth_stubs: 0x1ae0
+  __TEXT.__objc_methlist: 0x1c70
   __TEXT.__const: 0x748
-  __TEXT.__oslogstring: 0x3d2c
-  __TEXT.__cstring: 0x933e
-  __TEXT.__gcc_except_tab: 0x125c
+  __TEXT.__oslogstring: 0x3c5c
+  __TEXT.__cstring: 0x91ba
+  __TEXT.__gcc_except_tab: 0x1180
   __TEXT.__dlopen_cstrs: 0x21f
-  __TEXT.__swift5_typeref: 0xea
-  __TEXT.__swift5_capture: 0x80
+  __TEXT.__swift5_typeref: 0xd6
+  __TEXT.__swift5_capture: 0x70
   __TEXT.__constg_swiftt: 0x130
   __TEXT.__swift5_fieldmd: 0x64
   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_reflstr: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xde0
-  __TEXT.__eh_frame: 0x348
-  __TEXT.__objc_classname: 0x318
-  __TEXT.__objc_methname: 0x5256
-  __TEXT.__objc_methtype: 0xc05
+  __TEXT.__unwind_info: 0xe10
+  __TEXT.__eh_frame: 0x210
+  __TEXT.__objc_classname: 0x39f
+  __TEXT.__objc_methname: 0x520a
+  __TEXT.__objc_methtype: 0xc6d
   __TEXT.__objc_stubs: 0x4a20
   __DATA_CONST.__got: 0x440
-  __DATA_CONST.__const: 0x12c8
+  __DATA_CONST.__const: 0x1310
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1698
+  __DATA_CONST.__objc_selrefs: 0x1680
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0x990
-  __AUTH_CONST.__auth_got: 0xdb8
-  __AUTH_CONST.__const: 0x660
-  __AUTH_CONST.__cfstring: 0xa160
-  __AUTH_CONST.__objc_const: 0x3900
+  __DATA_CONST.__objc_arraydata: 0x958
+  __AUTH_CONST.__auth_got: 0xd80
+  __AUTH_CONST.__const: 0x638
+  __AUTH_CONST.__cfstring: 0xa120
+  __AUTH_CONST.__objc_const: 0x38d0
   __AUTH_CONST.__objc_intobj: 0x4c8
-  __AUTH_CONST.__objc_dictobj: 0x5a0
+  __AUTH_CONST.__objc_dictobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0x3b0
   __AUTH.__data: 0x190
-  __DATA.__objc_ivar: 0x2cc
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0x218
-  __DATA.__bss: 0x178
+  __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x2b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 458C7517-3731-32C8-A369-FCADD56E07EB
-  Functions: 1234
-  Symbols:   4054
-  CStrings:  4370
+  UUID: C6D0191B-67C7-3C94-AAF0-EAB42E7D3C4A
+  Functions: 1240
+  Symbols:   4127
+  CStrings:  4350
 
Symbols:
+ +[OSADiagnosticsReporterSupport handleDiagnosticLog:logPath:patternMatchActions:completion:]
+ +[OSADiagnosticsReporterSupport handleDiagnosticLog:logPath:patternMatchActions:completion:].cold.1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.382
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.382.cold.1
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.382.cold.2
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.382.cold.3
+ ___37-[OSASystemConfiguration internalKey]_block_invoke.382.cold.4
+ ___61+[OSASystemConfiguration ensureUsablePath:component:options:]_block_invoke.466
+ ___92+[OSADiagnosticsReporterSupport handleDiagnosticLog:logPath:patternMatchActions:completion:]_block_invoke
+ ___92+[OSADiagnosticsReporterSupport handleDiagnosticLog:logPath:patternMatchActions:completion:]_block_invoke.cold.1
+ ___block_literal_global.39
+ ___block_literal_global.59
+ ___rtc_internal_block_invoke.62
+ ___rtc_internal_block_invoke.62.cold.1
+ ___rtc_internal_block_invoke.62.cold.2
+ ___rtc_internal_block_invoke.62.cold.3
+ ___rtc_internal_block_invoke.64
+ ___rtc_internal_block_invoke.65.cold.1
+ _block_copy_helper.19
+ _block_copy_helper.25
+ _block_descriptor.21
+ _block_descriptor.27
+ _block_destroy_helper.20
+ _block_destroy_helper.26
+ _handleDiagnosticLog:logPath:patternMatchActions:completion:.DiagnosticsReporterLaunchOptionsClass
+ _handleDiagnosticLog:logPath:patternMatchActions:completion:.OSADiagnosticsReporterClass
+ _objc_msgSend$getXattrWithName:at:
+ _objc_msgSend$handleDiagnosticLog:logPath:patternMatchActions:completion:
+ _objc_msgSend$init
+ _objc_msgSend$readXattrWithReader:errorContext:
+ _objc_msgSend$setActions:
- +[OSADiagnosticsReporterSupport handleDiagnosticLog:logPath:completion:]
- +[OSADiagnosticsReporterSupport handleDiagnosticLog:logPath:completion:].cold.1
- -[OSASystemConfiguration pathAWDTasking]
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFNotificationCenterPostNotification
- _OBJC_IVAR_$_OSASystemConfiguration._pathAWDTasking
- ___37-[OSASystemConfiguration internalKey]_block_invoke.370
- ___37-[OSASystemConfiguration internalKey]_block_invoke.370.cold.1
- ___37-[OSASystemConfiguration internalKey]_block_invoke.370.cold.2
- ___37-[OSASystemConfiguration internalKey]_block_invoke.370.cold.3
- ___37-[OSASystemConfiguration internalKey]_block_invoke.370.cold.4
- ___40-[OSASystemConfiguration pathAWDTasking]_block_invoke
- ___61+[OSASystemConfiguration ensureUsablePath:component:options:]_block_invoke.454
- ___72+[OSADiagnosticsReporterSupport handleDiagnosticLog:logPath:completion:]_block_invoke
- ___72+[OSADiagnosticsReporterSupport handleDiagnosticLog:logPath:completion:]_block_invoke.cold.1
- ___block_literal_global.40
- ___block_literal_global.60
- ___rtc_internal_block_invoke.63
- ___rtc_internal_block_invoke.63.cold.1
- ___rtc_internal_block_invoke.63.cold.2
- ___rtc_internal_block_invoke.63.cold.3
- ___rtc_internal_block_invoke.66
- ___rtc_internal_block_invoke.66.cold.1
- _block_copy_helper.22
- _block_copy_helper.28
- _block_descriptor.24
- _block_descriptor.30
- _block_destroy_helper.23
- _block_destroy_helper.29
- _handleDiagnosticLog:logPath:completion:.DiagnosticsReporterLaunchOptionsClass
- _handleDiagnosticLog:logPath:completion:.OSADiagnosticsReporterClass
- _installAwdTasking
- _isConfigValid
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$arrayWithContentsOfFile:
- _objc_msgSend$deletePreference:forUser:inDomain:
- _objc_msgSend$handleDiagnosticLog:logPath:completion:
- _objc_msgSend$pathAWDTasking
- _objc_msgSend$setPreference:forUser:inDomain:toValue:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x9
- _pathAWDTasking.onceToken
- _symbolic So8NSStringCIeyBa_
CStrings:
+ "%@-seed"
+ "Carrier"
+ "CarrierSeed"
+ "Seed"
+ "failed task_read_for_pid with %d"
+ "handleDiagnosticLog:logPath:patternMatchActions:completion:"
+ "seed"
+ "setActions:"
+ "task_read_for_pid(%d) for resampling UUIDs failed with %d"
+ "task_read_for_pid(%d) for resampling backtraces failed with %d"
+ "v48@0:8q16@24@32@?40"
- "/Library/AWD"
- "AWDTaskingID"
- "Applying awd task failed"
- "Could not delete preference for domain,key: %@, %@"
- "Could not write task blob to file: %@"
- "Couldn't delete file for awd task at %@: %@"
- "GM"
- "_pathAWDTasking"
- "arrayWithContentsOfFile:"
- "awd"
- "awd task successfully applied and saved as %@"
- "deletePreference:forUser:inDomain:"
- "failed task_read_for_pid"
- "failed to install awd tasking"
- "failed to uninstall previous awd tasking"
- "handleDiagnosticLog:logPath:completion:"
- "logging tasks have changed"
- "pathAWDTasking"
- "setPreference:forUser:inDomain:toValue:"
- "task_read_for_pid(%d) for resampling UUIDs failed"
- "task_read_for_pid(%d) for resampling backtraces failed"
- "v40@0:8q16@24@?32"
- "writing %@@%@:%@=%@"

```
