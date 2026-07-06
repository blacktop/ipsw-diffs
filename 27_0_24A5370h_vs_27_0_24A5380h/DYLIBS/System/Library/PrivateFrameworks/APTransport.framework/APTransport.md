## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-  __TEXT.__text: 0xb3f88
+  __TEXT.__text: 0xb5504
   __TEXT.__objc_methlist: 0x1cf4
   __TEXT.__const: 0x418
   __TEXT.__gcc_except_tab: 0x9d8
-  __TEXT.__cstring: 0x2f86d
+  __TEXT.__cstring: 0x3004f
   __TEXT.__dlopen_cstrs: 0x1f3
   __TEXT.__oslogstring: 0x31c
-  __TEXT.__unwind_info: 0x2cc8
+  __TEXT.__unwind_info: 0x2d10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3d10
+  __DATA_CONST.__const: 0x3d60
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b38
+  __DATA_CONST.__objc_selrefs: 0x1b90
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x3e8
-  __AUTH_CONST.__const: 0x2db8
-  __AUTH_CONST.__cfstring: 0x6520
+  __DATA_CONST.__got: 0x400
+  __AUTH_CONST.__const: 0x2dd8
+  __AUTH_CONST.__cfstring: 0x65c0
   __AUTH_CONST.__objc_const: 0x2498
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1e0
+  __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x2c0
   __DATA.__objc_ivar: 0x18c
-  __DATA.__data: 0x1580
-  __DATA.__bss: 0x148
-  __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__data: 0xbd0
-  __DATA_DIRTY.__bss: 0x2b8
+  __DATA.__data: 0x14a0
+  __DATA.__bss: 0x138
+  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA_DIRTY.__data: 0xcb0
+  __DATA_DIRTY.__bss: 0x2c8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5314
-  Symbols:   13651
-  CStrings:  5308
+  Functions: 5342
+  Symbols:   13736
+  CStrings:  5354
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__data : content changed
Symbols:
+ GCC_except_table40
+ _APCarPlayHelperGetTypeID
+ _APSGetNANPerformanceForecastThresholds
+ _APTNANDataSessionGetPerformanceForecast
+ _APTransportDeviceIsTransportRecommended
+ _APTransportTrafficCaptureFlushForSysdiagnose
+ _NSFileSize
+ ___APTransportTrafficCaptureFlushForSysdiagnose_block_invoke
+ ___block_descriptor_32_e39_q24?0"NSDictionary"8"NSDictionary"16l
+ ___block_descriptor_72_e8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
+ ___trafficCapture_enforceStorageLimits_block_invoke
+ _fflush
+ _fileno
+ _fsync
+ _kAPTransportTrafficCaptureCreationOption_CaptureDirectory
+ _localtime_r
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$localInfrastructureThroughputCapacityRatio
+ _objc_msgSend$localThroughputCapacityMbps
+ _objc_msgSend$performanceForecast
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$signalStrength
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$unavailabilityLatencyCeilingMs
+ _objc_msgSend$unsignedIntegerValue
+ _rename
+ _strerror
+ _strftime
+ _time
+ _trafficCapture_formatNow
+ _unlink
- GCC_except_table38
CStrings:
+ "%H-%M-%S"
+ "%Y.%m.%d"
+ "%s/airplaysnoop_%s__%s__%s.atslite"
+ "%s/airplaysnoop_%s__%s__live.atslite"
+ ".atslite"
+ "980.67.2"
+ "APTNANDataSessionGetPerformanceForecast"
+ "APTransportDeviceIsTransportRecommended"
+ "APTransportTrafficCaptureCreate: missing %@ option\n"
+ "Boolean transportDevice_isNANRecommended(APTransportDeviceRef, OSStatus *)"
+ "NANDS [%{ptr}] Failed to obtain NANEndpoint with error: %#m"
+ "NANDS [%{ptr}] perfForecast=%@"
+ "OSStatus APTNANDataSessionGetPerformanceForecast(APTNANDataSessionRef, APSTransportPerformanceInfo *)"
+ "OSStatus APTransportTrafficCaptureFlushForSysdiagnose(APTransportTrafficCaptureRef)_block_invoke"
+ "OSStatus APTransportTrafficCaptureStartSession(APTransportTrafficCaptureRef)_block_invoke"
+ "OSStatus trafficCapture_closeAndRenameToFinal(APTransportTrafficCaptureRef)"
+ "OSStatus trafficCapture_createCaptureDirectory(APTransportTrafficCaptureRef)"
+ "OSStatus trafficCapture_openSessionFile(APTransportTrafficCaptureRef)"
+ "Terminus_ExplicitNANControl"
+ "[%{ptr}] Created (directory: %@)\n"
+ "[%{ptr}] Created capture directory: %s\n"
+ "[%{ptr}] Deleted old capture file: %s\n"
+ "[%{ptr}] Failed to create capture directory %s: %s\n"
+ "[%{ptr}] Failed to delete old capture file (skipping cleanup): %s\n"
+ "[%{ptr}] Failed to list capture directory: %s\n"
+ "[%{ptr}] Failed to rename capture file %s → %s (errno: %d)\n"
+ "[%{ptr}] FlushForSysdiagnose completed: %s\n"
+ "[%{ptr}] FlushForSysdiagnose fflush failed: %s (errno: %d, %s)\n"
+ "[%{ptr}] FlushForSysdiagnose fsync failed: %s (errno: %d, %s)\n"
+ "[%{ptr}] FlushForSysdiagnose: no active capture file, nothing to flush\n"
+ "[%{ptr}] NAN [%{ptr}] not recommended due to NAN throughput of %f with threshold of %f"
+ "[%{ptr}] NAN [%{ptr}] not recommended due to infra throughput ratio of %f with threshold of %f"
+ "[%{ptr}] NAN [%{ptr}] not recommended due to latency of %f with threshold of %f"
+ "[%{ptr}] NAN [%{ptr}] not recommended due to signal strength of %f with threshold of %f"
+ "[%{ptr}] Opened capture file: %s\n"
+ "[%{ptr}] Renamed capture file to: %s\n"
+ "[%{ptr}] Session stop: no active capture session, nothing to do\n"
+ "[%{ptr}] Start session %s (err: %#m)\n"
+ "captureDirectory"
+ "path"
+ "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "size"
+ "trafficCapture_closeAndRenameToFinal"
+ "trafficCapture_openSessionFile"
+ "transportDevice_isNANRecommended"
+ "void trafficCapture_enforceStorageLimits(APTransportTrafficCaptureRef)"
- "980.63.2"
- "APTransportTrafficCaptureStartSession_block_invoke"
- "APTransportTrafficCaptureStopSession_block_invoke"
- "OSStatus APTransportTrafficCaptureStartSession(APTransportTrafficCaptureRef, const char *, CFDictionaryRef)_block_invoke"
- "[%{ptr}] Start session for %s %s (err: %#m)\n"

```
