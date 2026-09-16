## WirelessProximity

> `/System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity`

```diff

-2700.51.1.3.0
-  __TEXT.__text: 0x325c8
-  __TEXT.__objc_methlist: 0x2c0c
+2701.3.0.0.0
+  __TEXT.__text: 0x33ae8
+  __TEXT.__objc_methlist: 0x2c9c
   __TEXT.__const: 0x380
-  __TEXT.__cstring: 0x3bcb
-  __TEXT.__oslogstring: 0x478f
-  __TEXT.__gcc_except_tab: 0x698
-  __TEXT.__unwind_info: 0x1880
+  __TEXT.__cstring: 0x3cb8
+  __TEXT.__oslogstring: 0x47db
+  __TEXT.__gcc_except_tab: 0x6d0
+  __TEXT.__unwind_info: 0x18f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7a8
+  __DATA_CONST.__const: 0x7d0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1720
+  __DATA_CONST.__objc_selrefs: 0x1788
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc8
-  __DATA_CONST.__got: 0x1b0
-  __AUTH_CONST.__const: 0x3728
-  __AUTH_CONST.__cfstring: 0x2f80
-  __AUTH_CONST.__objc_const: 0x3198
+  __DATA_CONST.__got: 0x1b8
+  __AUTH_CONST.__const: 0x3828
+  __AUTH_CONST.__cfstring: 0x3120
+  __AUTH_CONST.__objc_const: 0x3278
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x1e0
-  __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x220
+  __AUTH_CONST.__objc_intobj: 0x1f8
+  __AUTH_CONST.__auth_got: 0x3d8
+  __DATA.__objc_ivar: 0x23c
   __DATA.__data: 0x2a8
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1969
-  Symbols:   2436
-  CStrings:  957
+  Functions: 2005
+  Symbols:   2470
+  CStrings:  974
 
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
+ _OBJC_IVAR_$_LeAdvertisingMetric.daemonXPCSendAt
+ _OBJC_IVAR_$_LeAdvertisingMetric.gapRxAt
+ _OBJC_IVAR_$_LeAdvertisingMetric.hciRxAt
+ _OBJC_IVAR_$_LeAdvertisingMetric.observerRxAt
+ _OBJC_IVAR_$_LeAdvertisingMetric.preNotifyAt
+ _OBJC_IVAR_$_LeAdvertisingMetric.scanMgrRxAt
+ _OBJC_IVAR_$_LeAdvertisingMetric.wpdClientAt
+ ___45-[LeAdvertisingMetric getAdvReportMetricCBv1]_block_invoke
+ ___47+[LeAdvertisingMetric getAdvReportDictFromXPC:]_block_invoke
+ ___block_descriptor_56_e8_32r_e37_B24?0r*8"NSObject<OS_xpc_object>"16lr32l8
+ ___chkstk_darwin
+ __xpc_type_dictionary
+ _bzero
+ _objc_msgSend$getAdvReportTimestamps
+ _objc_msgSend$initWithObjects:forKeys:count:
+ _objc_release_x10
+ _xpc_dictionary_apply
+ _xpc_dictionary_create
+ _xpc_dictionary_get_count
+ _xpc_dictionary_set_uint64
+ _xpc_get_type
+ _xpc_uint64_get_value
CStrings:
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "DaemonXPCToScanMgr"
+ "GapRxToObserver"
+ "GapToObserver"
+ "HCIToGap"
+ "ObserverToPreNotify"
+ "PreNotifyToDaemonXPC"
+ "ScanMgrToWPDClient"
+ "[LeAdvMetric] getAdvReportMetricCBv1 (ms) %@"
+ "[LeAdvMetric] inXPC not a dict"
+ "daemonXPCSendAt"
+ "gapRxAt"
+ "hciRxAt"
+ "observerRxAt"
+ "preNotifyAt"
+ "scanMgrRxAt"
+ "wpdClientAt"
```
