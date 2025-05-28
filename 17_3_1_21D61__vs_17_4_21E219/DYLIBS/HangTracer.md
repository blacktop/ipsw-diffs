## HangTracer

> `/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`

```diff

-281.2.0.0.0
-  __TEXT.__text: 0xcf74
-  __TEXT.__auth_stubs: 0x810
+288.0.0.0.0
+  __TEXT.__text: 0xd230
+  __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_methlist: 0x788
-  __TEXT.__const: 0x94
-  __TEXT.__cstring: 0x2ad0
+  __TEXT.__const: 0x84
+  __TEXT.__cstring: 0x2b9b
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__oslogstring: 0x1d4b
-  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__oslogstring: 0x1d91
+  __TEXT.__unwind_info: 0x2b4
   __TEXT.__objc_classname: 0x37
-  __TEXT.__objc_methname: 0x2f06
+  __TEXT.__objc_methname: 0x2f3e
   __TEXT.__objc_methtype: 0x669
-  __TEXT.__objc_stubs: 0xbe0
+  __TEXT.__objc_stubs: 0xc20
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0xf80
+  __DATA_CONST.__const: 0xfa8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x13a0
-  __DATA_CONST.__objc_selrefs: 0x6e8
-  __AUTH_CONST.__cfstring: 0x3780
-  __AUTH_CONST.__const: 0x280
+  __DATA_CONST.__objc_selrefs: 0x6f8
+  __DATA_CONST.__objc_classrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0x18
+  __AUTH_CONST.__cfstring: 0x3840
+  __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_const: 0x168
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x418
-  __DATA.__objc_classrefs: 0xb8
-  __DATA.__objc_superrefs: 0x18
+  __AUTH_CONST.__auth_got: 0x438
   __DATA.__objc_ivar: 0x198
-  __DATA.__data: 0x1a8
-  __DATA.__bss: 0x28
+  __DATA.__data: 0x1d8
+  __DATA.__bss: 0x48
   __DATA.__common: 0x0
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0xb8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 331
-  Symbols:   1307
-  CStrings:  1091
+  Functions: 335
+  Symbols:   1332
+  CStrings:  1102
 
Symbols:
+ _HTCAQueue
+ _HTCAQueue.caQueue
+ _HTCAQueue.onceToken
+ _HTCreateAnalyticsEventForAlwaysOnHang
+ _HTGatherHomeVolumeSpaceInfo.homeURL
+ _HTGatherHomeVolumeSpaceInfo.onceToken
+ _HTGetHomeDirectoryURL
+ _NSHomeDirectoryForUser
+ ___HTCAQueue_block_invoke
+ ___HTCreateAnalyticsEventForAlwaysOnHang_block_invoke
+ ___HTCreateAnalyticsEventForAlwaysOnHang_block_invoke_2
+ ___HTGatherHomeVolumeSpaceInfo_block_invoke
+ ___HTHangEventCreateWithBundleID_block_invoke.33
+ ___StartMonitoringWatchdogDisablement_block_invoke.117
+ ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.111
+ ___block_literal_global.121
+ ___block_literal_global.127
+ ___block_literal_global.131
+ ___block_literal_global.177
+ ___block_literal_global.32
+ ___block_literal_global.35
+ ___block_literal_global.86
+ ___block_literal_global.92
+ ___checkForHangWithUserMovedAwayAndRecentAssertions_block_invoke.162
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _kHTCoreAnalyticsDiskAvailableBytes
+ _kHTCoreAnalyticsDiskAvailablePercent
+ _kHTCoreAnalyticsHaveNonDefaultFeatureFlags
+ _kHTCoreAnalyticsHaveSerialLoggingEnabled
+ _kHTCoreAnalyticsNandIndirectionTableAvailablePercent
+ _kHTCoreAnalyticsNumOSCryptexFileExtents
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_retain_x9
+ _statfs
- ___HTHangEventCreateWithBundleID_block_invoke.25
- ___StartMonitoringWatchdogDisablement_block_invoke.110
- ___block_literal_global.104
- ___block_literal_global.114
- ___block_literal_global.117
- ___block_literal_global.120
- ___block_literal_global.28
- ___block_literal_global.79
- ___block_literal_global.85
- ___checkForHangWithUserMovedAwayAndRecentAssertions_block_invoke.155
- ___checkForHangWithUserMovedAwayAndRecentAssertions_block_invoke_2
- ___createAnalyticsEventForHang_block_invoke
- _createAnalyticsEventForHang
CStrings:
+ "HTUserSwitchedAwayFromApp for pid %d reason %@"
+ "Logging always-on telemetry: %@"
+ "Successfully created directory at path %@"
+ "Unable to get home dir URL"
+ "com.apple.hangtracer.coreanalytics"
+ "disk_available_bytes"
+ "disk_available_percent"
+ "fileSystemRepresentation"
+ "fileURLWithPath:isDirectory:"
+ "have_non_default_feature_flags"
+ "have_serial_logging_enabled"
+ "nand_indirection_table_available_percent"
+ "os_cryptex_file_extents"
- "HTUserSwitchedAwayFromApp for pid %d"
- "Sucessfully created directory at path %@"

```
