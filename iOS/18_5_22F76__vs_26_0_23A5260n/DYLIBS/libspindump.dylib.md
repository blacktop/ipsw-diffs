## libspindump.dylib

> `/usr/lib/libspindump.dylib`

```diff

-383.14.0.0.0
-  __TEXT.__text: 0x3a20
-  __TEXT.__auth_stubs: 0x3d0
+404.0.0.0.0
+  __TEXT.__text: 0x3b0c
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0xbb1
-  __TEXT.__cstring: 0x45f
-  __TEXT.__unwind_info: 0x128
+  __TEXT.__oslogstring: 0xca8
+  __TEXT.__cstring: 0x4a4
+  __TEXT.__unwind_info: 0x140
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x66
   __TEXT.__objc_stubs: 0xe0

   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x40
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA.__bss: 0xf8
   __DATA_DIRTY.__bss: 0x238
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 11A8DE55-ECF2-3256-B4AF-F7F25B76831B
-  Functions: 74
-  Symbols:   360
-  CStrings:  117
+  UUID: 63EA183C-B692-3794-8EB2-5224BD6FB3CA
+  Functions: 78
+  Symbols:   293
+  CStrings:  126
 
Symbols:
+ _SPReportPowerException
+ _SPReportPowerException.cold.1
+ _SPReportPowerException.cold.2
+ _SPReportPowerException.cold.3
+ _SPReportPowerException.cold.4
+ ___block_descriptor_40_e8_32bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_descriptor_44_e8_32bs_e5_v8?0ls32l8
+ ___block_literal_global.40
+ ___block_literal_global.42
+ ___block_literal_global.46
+ ___block_literal_global.78
+ ___block_literal_global.80
+ _libspindump_log
+ _libspindump_log.cold.1
+ _objc_claimAutoreleasedReturnValue
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x8
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x8
+ _objc_unsafeClaimAutoreleasedReturnValue
- _SPCheckHIDResponseTime2.cold.10
- _SPCheckHIDResponseTime2.cold.11
- _SPCheckHIDResponseTime2.cold.12
- _SPCheckHIDResponseTime2.cold.13
- _SPCheckHIDResponseTime2.cold.14
- _SPCheckHIDResponseTime2.cold.15
- _SPCheckHIDResponseTime2.cold.16
- _SPCheckHIDResponseTime2.cold.17
- _SPCheckHIDResponseTime2.cold.18
- _SPCheckHIDResponseTime2.cold.19
- _SPCheckHIDResponseTime2.cold.20
- _SPCheckHIDResponseTime2.cold.21
- _SPCheckHIDResponseTime2.cold.8
- _SPCheckHIDResponseTime2.cold.9
- _SPExpectedHIDResponseDelayUntil.cold.5
- _SPExpectedHIDResponseDelayUntil.cold.6
- _SPExpectedHIDResponseDelayUntil.cold.7
- _SPExpectedHIDResponseDelayUntil.cold.8
- _SPGenerateSpindump.cold.2
- _SPGenerateSpindump.cold.3
- _SPPauseMonitoringHIDResponsiveness.cold.2
- _SPReportCPUUsageResource.cold.3
- _SPReportCPUUsageResource.cold.4
- _SPReportCPUUsageResource.cold.5
- _SPReportDiskWritesResource.cold.3
- _SPReportDiskWritesResource.cold.4
- _SPReportDiskWritesResource.cold.5
- _SPReportWorkflowResponsivenessDelay.cold.4
- _SPReportWorkflowResponsivenessDelay.cold.5
- _SPReportWorkflowResponsivenessDelay.cold.6
- _SPResumeMonitoringHIDResponsiveness.cold.6
- _SPResumeMonitoringHIDResponsiveness.cold.7
- _SPResumeMonitoringHIDResponsiveness.cold.8
- __Block_copy
- __Block_release
- __SPReportFileDescriptorExhaustion.cold.3
- __SPReportFileDescriptorExhaustion.cold.4
- __SPReportFileDescriptorExhaustion.cold.5
- __SPReportKQWorkLoopExhaustion.cold.3
- __SPReportKQWorkLoopExhaustion.cold.4
- __SPReportKQWorkLoopExhaustion.cold.5
- __SPReportPortExhaustion.cold.3
- __SPReportPortExhaustion.cold.4
- __SPReportPortExhaustion.cold.5
- ___SPAddToHIDTelemetry_block_invoke.cold.1
- ___block_descriptor_40_e8_32b_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
- ___block_descriptor_44_e8_32b_e5_v8?0ls32l8
- ___block_literal_global.35
- ___block_literal_global.37
- ___block_literal_global.41
- ___block_literal_global.70
- ___block_literal_global.73
- ___procname_btd_block_invoke.cold.2
- ___spindump_connection_block_invoke_2.cold.2
- _objc_retain_x21
- _objc_retain_x22
- _spindump_connection.cold.3
- _xpc_release
CStrings:
+ "Reporting %{public}spower exception for %{public}s for the last %.0f seconds"
+ "Reporting power exception that is both fatal and background qos"
+ "Reporting power exception that is neither fatal nor background qos"
+ "Reporting power exception with no path"
+ "detector"
+ "event_duration"
+ "issue_type"
+ "mitigation_reason"
+ "report_duration"

```
