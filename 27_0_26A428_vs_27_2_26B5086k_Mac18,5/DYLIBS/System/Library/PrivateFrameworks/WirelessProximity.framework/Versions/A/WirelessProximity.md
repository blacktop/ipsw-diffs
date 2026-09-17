## WirelessProximity

> `/System/Library/PrivateFrameworks/WirelessProximity.framework/Versions/A/WirelessProximity`

```diff

-2700.51.0.0.0
-  __TEXT.__text: 0x35e48
-  __TEXT.__objc_methlist: 0x2bdc
+2701.3.0.0.0
+  __TEXT.__text: 0x37400
+  __TEXT.__objc_methlist: 0x2c6c
   __TEXT.__const: 0x350
-  __TEXT.__cstring: 0x3c34
-  __TEXT.__oslogstring: 0x48f0
-  __TEXT.__gcc_except_tab: 0x718
-  __TEXT.__unwind_info: 0x1980
+  __TEXT.__cstring: 0x3d21
+  __TEXT.__oslogstring: 0x493c
+  __TEXT.__gcc_except_tab: 0x750
+  __TEXT.__unwind_info: 0x19f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16f0
+  __DATA_CONST.__objc_selrefs: 0x1758
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc8
-  __DATA_CONST.__got: 0x1a8
-  __AUTH_CONST.__const: 0x3ec0
-  __AUTH_CONST.__cfstring: 0x2fe0
-  __AUTH_CONST.__objc_const: 0x3138
+  __DATA_CONST.__got: 0x1b0
+  __AUTH_CONST.__const: 0x3ff0
+  __AUTH_CONST.__cfstring: 0x3180
+  __AUTH_CONST.__objc_const: 0x3218
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x1e0
-  __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x218
+  __AUTH_CONST.__objc_intobj: 0x1f8
+  __AUTH_CONST.__auth_got: 0x2e8
+  __DATA.__objc_ivar: 0x234
   __DATA.__data: 0x2a8
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2033
-  Symbols:   2571
-  CStrings:  969
+  Functions: 2069
+  Symbols:   2607
+  CStrings:  986
 
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
+ GCC_except_table30
+ OBJC_IVAR_$_LeAdvertisingMetric.daemonXPCSendAt
+ OBJC_IVAR_$_LeAdvertisingMetric.gapRxAt
+ OBJC_IVAR_$_LeAdvertisingMetric.hciRxAt
+ OBJC_IVAR_$_LeAdvertisingMetric.observerRxAt
+ OBJC_IVAR_$_LeAdvertisingMetric.preNotifyAt
+ OBJC_IVAR_$_LeAdvertisingMetric.scanMgrRxAt
+ OBJC_IVAR_$_LeAdvertisingMetric.wpdClientAt
+ __45-[LeAdvertisingMetric getAdvReportMetricCBv1]_block_invoke
+ __47+[LeAdvertisingMetric getAdvReportDictFromXPC:]_block_invoke
+ ___45-[LeAdvertisingMetric getAdvReportMetricCBv1]_block_invoke
+ ___47+[LeAdvertisingMetric getAdvReportDictFromXPC:]_block_invoke
+ ___block_descriptor_56_e8_32r_e37_B24?0r*8"NSObject<OS_xpc_object>"16l
+ ___chkstk_darwin
+ __xpc_type_dictionary
+ _bzero
+ _objc_msgSend$getAdvReportTimestamps
+ _objc_msgSend$initWithObjects:forKeys:count:
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
