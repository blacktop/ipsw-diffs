## WPDaemon

> `/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon`

```diff

-2700.51.1.3.0
-  __TEXT.__text: 0x5d634
-  __TEXT.__objc_methlist: 0x45a4
-  __TEXT.__cstring: 0x4a6d
+2701.3.0.0.0
+  __TEXT.__text: 0x5ee0c
+  __TEXT.__objc_methlist: 0x4654
+  __TEXT.__cstring: 0x4b73
   __TEXT.__const: 0x290
-  __TEXT.__oslogstring: 0xaf97
-  __TEXT.__gcc_except_tab: 0x1294
-  __TEXT.__unwind_info: 0x27b8
+  __TEXT.__oslogstring: 0xafe0
+  __TEXT.__gcc_except_tab: 0x12cc
+  __TEXT.__unwind_info: 0x2838
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x12f8
+  __DATA_CONST.__const: 0x1320
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28b0
+  __DATA_CONST.__objc_selrefs: 0x2938
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x2d0
-  __DATA_CONST.__got: 0x4b8
-  __AUTH_CONST.__const: 0x6e08
-  __AUTH_CONST.__cfstring: 0x3860
-  __AUTH_CONST.__objc_const: 0x8a88
+  __DATA_CONST.__got: 0x4c8
+  __AUTH_CONST.__const: 0x6f08
+  __AUTH_CONST.__cfstring: 0x3a00
+  __AUTH_CONST.__objc_const: 0x8b98
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x180
+  __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x510
-  __DATA.__objc_ivar: 0x578
+  __AUTH_CONST.__auth_got: 0x540
+  __DATA.__objc_ivar: 0x598
   __DATA.__data: 0x600
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__bss: 0x108

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3595
-  Symbols:   4028
-  CStrings:  1559
+  Functions: 3636
+  Symbols:   4075
+  CStrings:  1576
 
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
+ GCC_except_table43
+ _CBAdvReportMetricHeySiri
+ _OBJC_IVAR_$_LeAdvertisingMetric.daemonXPCSendAt
+ _OBJC_IVAR_$_LeAdvertisingMetric.gapRxAt
+ _OBJC_IVAR_$_LeAdvertisingMetric.hciRxAt
+ _OBJC_IVAR_$_LeAdvertisingMetric.observerRxAt
+ _OBJC_IVAR_$_LeAdvertisingMetric.preNotifyAt
+ _OBJC_IVAR_$_LeAdvertisingMetric.scanMgrRxAt
+ _OBJC_IVAR_$_LeAdvertisingMetric.wpdClientAt
+ _OBJC_IVAR_$_WPDClient._advReportMetricSet
+ ___32-[WPDStatsManager reportPLStats]_block_invoke_3
+ ___45-[LeAdvertisingMetric getAdvReportMetricCBv1]_block_invoke
+ ___47+[LeAdvertisingMetric getAdvReportDictFromXPC:]_block_invoke
+ ___50-[WPDStatsManager sendStatsToCoreAnalytics:stats:]_block_invoke
+ ___50-[WPDStatsManager sendStatsToCoreAnalytics:stats:]_block_invoke_2
+ ___block_descriptor_56_e8_32r_e37_B24?0r*8"NSObject<OS_xpc_object>"16lr32l8
+ __xpc_type_dictionary
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
+ _objc_release_x10
+ _reportPLStats.onceToken
+ _xpc_dictionary_apply
+ _xpc_dictionary_get_count
+ _xpc_dictionary_set_uint64
+ _xpc_get_type
+ _xpc_uint64_get_value
- GCC_except_table33
- GCC_except_table35
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
+ "WPDaemon iOS 27.2 (24B5083s) (WirelessProximity-2701.3) (Release) built on 2026-09-05 05:41:45"
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
- "WPDaemon iOS 27.0 (24A425) (WirelessProximity-2700.51.1.3) (Release) built on 2026-08-21 20:41:23"
- "com.apple.Bluetooth."
```
