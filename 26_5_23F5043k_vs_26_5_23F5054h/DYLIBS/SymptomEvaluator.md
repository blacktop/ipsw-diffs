## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-2169.120.2.0.0
-  __TEXT.__text: 0x28ca1c
+2169.120.6.0.0
+  __TEXT.__text: 0x28ce18
   __TEXT.__auth_stubs: 0x2c30
-  __TEXT.__objc_methlist: 0x17a90
+  __TEXT.__objc_methlist: 0x17ab8
   __TEXT.__cstring: 0x25369
   __TEXT.__const: 0x1050
   __TEXT.__oslogstring: 0x43b6f

   __TEXT.bb_MAV_clp: 0x89e0
   __TEXT.bb_INT_clp: 0x6a10
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x7570
+  __TEXT.__unwind_info: 0x7578
   __TEXT.__eh_frame: 0x6c8
   __TEXT.__objc_classname: 0x1d95
-  __TEXT.__objc_methname: 0x3d2f9
-  __TEXT.__objc_methtype: 0x6dd8
-  __TEXT.__objc_stubs: 0x25c20
+  __TEXT.__objc_methname: 0x3d519
+  __TEXT.__objc_methtype: 0x6eb8
+  __TEXT.__objc_stubs: 0x25c60
   __DATA_CONST.__got: 0xf68
   __DATA_CONST.__const: 0x67c8
   __DATA_CONST.__objc_classlist: 0x870
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcb78
+  __DATA_CONST.__objc_selrefs: 0xcb90
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x598
   __DATA_CONST.__objc_arraydata: 0x8c0
   __AUTH_CONST.__auth_got: 0x1630
   __AUTH_CONST.__const: 0x2c30
   __AUTH_CONST.__cfstring: 0x1d4a0
-  __AUTH_CONST.__objc_const: 0x3cbb0
+  __AUTH_CONST.__objc_const: 0x3cd70
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x938
   __AUTH_CONST.__objc_intobj: 0x870

   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x1560
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x2e20
+  __DATA.__objc_ivar: 0x2e58
   __DATA.__data: 0x1d78
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xf58
-  __DATA.__common: 0x18098
+  __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x3f20
   __DATA_DIRTY.__data: 0x1e8
   __DATA_DIRTY.__bss: 0x16c8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 141B38F0-1BC3-3731-9156-B4A4F16D27B7
-  Functions: 11555
-  Symbols:   37145
-  CStrings:  26815
+  UUID: 2A4F3AC3-784B-36EE-AB42-C6259B5B21AF
+  Functions: 11559
+  Symbols:   37169
+  CStrings:  26833
 
Symbols:
+ -[NetworkAnalyticsEngine _resetLoadedLqmEventDedupState]
+ -[NetworkAnalyticsEngine _shouldSubmitLoadedLqmAnalyticsEvent]
+ -[TCPProgressProbe _setProbeConnectivity:socket:request:]
+ GCC_except_table210
+ GCC_except_table246
+ GCC_except_table251
+ GCC_except_table255
+ GCC_except_table263
+ GCC_except_table284
+ GCC_except_table291
+ GCC_except_table299
+ GCC_except_table343
+ GCC_except_table380
+ GCC_except_table394
+ GCC_except_table405
+ GCC_except_table67
+ GCC_except_table74
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._cellLoadedLqmLastDepressBothLQM
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._cellLoadedLqmLastDepressBothLQMOld
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._cellLoadedLqmLastIsLowInternetDL
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._cellLoadedLqmLastIsLowInternetUL
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._cellLoadedLqmLastLoadedLQM
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._cellLoadedLqmLastNewLQM
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._cellLoadedLqmLastOldLQM
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._loadedLqmEventQuota
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._loadedLqmEventQuotaLastUpdated
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._wifiLoadedLqmLastIsLowInternetDL
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._wifiLoadedLqmLastIsLowInternetUL
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._wifiLoadedLqmLastLoadedLQM
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._wifiLoadedLqmLastNewLQM
+ _OBJC_IVAR_$_NetworkAnalyticsEngine._wifiLoadedLqmLastOldLQM
+ _machContinuousTime_timeIntervals
+ _machContinuousTime_timeIntervals.cold.1
+ _objc_msgSend$_setProbeConnectivity:socket:request:
+ _objc_msgSend$_shouldSubmitLoadedLqmAnalyticsEvent
- GCC_except_table161
- GCC_except_table244
- GCC_except_table249
- GCC_except_table254
- GCC_except_table259
- GCC_except_table287
- GCC_except_table296
- GCC_except_table297
- GCC_except_table341
- GCC_except_table378
- GCC_except_table392
- GCC_except_table403
- GCC_except_table66
- GCC_except_table73
- _bpf_buffer
Functions:
~ -[NetworkAnalyticsEngine _computeLoadedLQMFrom:oldLqm:isLowInternetDL:isLowInternetUL:stallMetric:onInterfaceType:] : 3268 -> 3816
+ -[NetworkAnalyticsEngine _shouldSubmitLoadedLqmAnalyticsEvent]
+ -[NetworkAnalyticsEngine _resetLoadedLqmEventDedupState]
+ -[TCPProgressProbe _setProbeConnectivity:socket:request:]
~ ___36-[TCPProgressProbe manage:outValue:]_block_invoke : 1832 -> 1824
+ _machContinuousTime_timeIntervals
CStrings:
+ "_cellLoadedLqmLastDepressBothLQM"
+ "_cellLoadedLqmLastDepressBothLQMOld"
+ "_cellLoadedLqmLastIsLowInternetDL"
+ "_cellLoadedLqmLastIsLowInternetUL"
+ "_cellLoadedLqmLastLoadedLQM"
+ "_cellLoadedLqmLastNewLQM"
+ "_cellLoadedLqmLastOldLQM"
+ "_loadedLqmEventQuota"
+ "_loadedLqmEventQuotaLastUpdated"
+ "_resetLoadedLqmEventDedupState"
+ "_setProbeConnectivity:socket:request:"
+ "_shouldSubmitLoadedLqmAnalyticsEvent"
+ "_wifiLoadedLqmLastIsLowInternetDL"
+ "_wifiLoadedLqmLastIsLowInternetUL"
+ "_wifiLoadedLqmLastLoadedLQM"
+ "_wifiLoadedLqmLastNewLQM"
+ "_wifiLoadedLqmLastOldLQM"
+ "i32@0:8i16i20^{ifreq=[16c](?={sockaddr=CC[14c]}{sockaddr=CC[14c]}{sockaddr=CC[14c]}siiiii*{ifdevmtu=iii}{ifkpi=II(?=^vi)}IIi[2i]{?=II}QQ{?=iIii}I{?=III}IIIII{?=II}{if_interface_state=CCcC}IIIIIIiIiIiI{?=CC}{?=CC}QCCIC)}24"

```
