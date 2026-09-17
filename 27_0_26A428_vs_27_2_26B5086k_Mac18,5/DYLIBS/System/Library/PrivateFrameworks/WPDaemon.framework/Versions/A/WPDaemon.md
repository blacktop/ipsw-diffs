## WPDaemon

> `/System/Library/PrivateFrameworks/WPDaemon.framework/Versions/A/WPDaemon`

```diff

-2700.51.0.0.0
-  __TEXT.__text: 0x5b340
-  __TEXT.__objc_methlist: 0x42f4
-  __TEXT.__cstring: 0x46e3
+2701.3.0.0.0
+  __TEXT.__text: 0x5cbb0
+  __TEXT.__objc_methlist: 0x43a4
+  __TEXT.__cstring: 0x47fa
   __TEXT.__const: 0x238
-  __TEXT.__oslogstring: 0x9de8
-  __TEXT.__gcc_except_tab: 0x1124
-  __TEXT.__unwind_info: 0x2538
+  __TEXT.__oslogstring: 0x9e35
+  __TEXT.__gcc_except_tab: 0x115c
+  __TEXT.__unwind_info: 0x25b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27a8
+  __DATA_CONST.__objc_selrefs: 0x2830
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x2d0
-  __DATA_CONST.__got: 0x478
-  __AUTH_CONST.__const: 0x7600
-  __AUTH_CONST.__cfstring: 0x36a0
-  __AUTH_CONST.__objc_const: 0x85f0
+  __DATA_CONST.__got: 0x488
+  __AUTH_CONST.__const: 0x7730
+  __AUTH_CONST.__cfstring: 0x3840
+  __AUTH_CONST.__objc_const: 0x8700
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x3f0
-  __DATA.__objc_ivar: 0x538
+  __AUTH_CONST.__auth_got: 0x420
+  __DATA.__objc_ivar: 0x558
   __DATA.__data: 0x5a0
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__bss: 0xda

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3363
-  Symbols:   4035
-  CStrings:  1443
+  Functions: 3403
+  Symbols:   4083
+  CStrings:  1461
 
Symbols:
+ +[LeAdvertisingMetric getAdvReportDictFromXPC:]
+ -[LeAdvertisingMetric getAdvReportMetricCBv1]
+ -[LeAdvertisingMetric getAdvReportTimestamps]
+ -[LeAdvertisingMetric getAdvReportXPCRepresentation]
+ -[LeAdvertisingMetric setAdvReportTimestamps:]
+ -[LeAdvertisingMetric setDaemonXPCSendAt]
+ -[LeAdvertisingMetric setGapRxAt:]
+ -[LeAdvertisingMetric setHciRxAt:]
+ -[LeAdvertisingMetric setObserverRxAt]
+ -[LeAdvertisingMetric setPreNotifyAt]
+ -[LeAdvertisingMetric setScanMgrRxAt]
+ -[LeAdvertisingMetric setWPDClientAt]
+ -[WPDClient advReportMetricSet]
+ -[WPDClient setAdvReportMetricSet:]
+ -[WPDStatsManager sendStatsToCoreAnalytics:stats:]
+ GCC_except_table30
+ GCC_except_table36
+ GCC_except_table40
+ GCC_except_table46
+ OBJC_IVAR_$_LeAdvertisingMetric.daemonXPCSendAt
+ OBJC_IVAR_$_LeAdvertisingMetric.gapRxAt
+ OBJC_IVAR_$_LeAdvertisingMetric.hciRxAt
+ OBJC_IVAR_$_LeAdvertisingMetric.observerRxAt
+ OBJC_IVAR_$_LeAdvertisingMetric.preNotifyAt
+ OBJC_IVAR_$_LeAdvertisingMetric.scanMgrRxAt
+ OBJC_IVAR_$_LeAdvertisingMetric.wpdClientAt
+ OBJC_IVAR_$_WPDClient._advReportMetricSet
+ _CBAdvReportMetricHeySiri
+ __45-[LeAdvertisingMetric getAdvReportMetricCBv1]_block_invoke
+ __47+[LeAdvertisingMetric getAdvReportDictFromXPC:]_block_invoke
+ ___45-[LeAdvertisingMetric getAdvReportMetricCBv1]_block_invoke
+ ___47+[LeAdvertisingMetric getAdvReportDictFromXPC:]_block_invoke
+ ___50-[WPDStatsManager sendStatsToCoreAnalytics:stats:]_block_invoke
+ ___50-[WPDStatsManager sendStatsToCoreAnalytics:stats:]_block_invoke_2
+ ___block_descriptor_56_e8_32r_e37_B24?0r*8"NSObject<OS_xpc_object>"16l
+ __xpc_type_dictionary
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_msgSend$advReportMetricSet
+ _objc_msgSend$getAdvReportMetricCBv1
+ _objc_msgSend$getAdvReportTimestamps
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithObjects:forKeys:count:
+ _objc_msgSend$reportQueue
+ _objc_msgSend$sendStatsToCoreAnalytics:stats:
+ _objc_msgSend$setAdvReportTimestamps:
+ _objc_msgSend$setScanMgrRxAt
+ _objc_msgSend$setWPDClientAt
+ _xpc_dictionary_apply
+ _xpc_dictionary_get_count
+ _xpc_dictionary_set_uint64
+ _xpc_get_type
+ _xpc_uint64_get_value
- GCC_except_table35
- GCC_except_table37
- GCC_except_table39
- ___sendWPStatsToCoreAnalytics_block_invoke
CStrings:
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "DaemonXPCToScanMgr"
+ "GapRxToObserver"
+ "GapToObserver"
+ "HCIToGap"
+ "HeySiriAdvReportDurationWiProx"
+ "ObserverToPreNotify"
+ "PreNotifyToDaemonXPC"
+ "ScanMgrToWPDClient"
+ "W!f$"
+ "WPDaemon macOS 27.2 (26B5085s) (WirelessProximity-2701.3) (Release) built on 2026-09-05 04:04:13"
+ "WPStatsQueue"
+ "[LeAdvMetric] getAdvReportMetricCBv1 (ms) %@"
+ "[LeAdvMetric] inXPC not a dict"
+ "com.apple.Bluetooth.%@"
+ "daemonXPCSendAt"
+ "gapRxAt"
+ "hciRxAt"
+ "observerRxAt"
+ "preNotifyAt"
+ "scanMgrRxAt"
+ "wpdClientAt"
- "%@%@"
- "W!f#"
- "WPDaemon macOS 27.0 (26A411) (WirelessProximity-2700.51) (Release) built on 2026-08-08 16:28:00"
- "com.apple.Bluetooth."
```
