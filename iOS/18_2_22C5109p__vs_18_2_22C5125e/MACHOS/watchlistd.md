## watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

```diff

-850.20.28.0.0
-  __TEXT.__text: 0x27bfc
+850.20.30.0.0
+  __TEXT.__text: 0x279c8
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0x5140
-  __TEXT.__objc_methlist: 0x2250
-  __TEXT.__cstring: 0x4785
-  __TEXT.__oslogstring: 0x24fc
-  __TEXT.__objc_classname: 0x498
-  __TEXT.__objc_methtype: 0xf63
-  __TEXT.__objc_methname: 0x5ee1
-  __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0xee8
+  __TEXT.__objc_stubs: 0x5100
+  __TEXT.__objc_methlist: 0x2238
+  __TEXT.__cstring: 0x46e4
+  __TEXT.__oslogstring: 0x2497
+  __TEXT.__objc_classname: 0x497
+  __TEXT.__objc_methtype: 0xf43
+  __TEXT.__objc_methname: 0x5e4c
+  __TEXT.__const: 0x128
+  __TEXT.__gcc_except_tab: 0xedc
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0xb70
+  __TEXT.__unwind_info: 0xb60
   __DATA_CONST.__auth_got: 0x4b0
-  __DATA_CONST.__got: 0x558
-  __DATA_CONST.__const: 0x13b8
-  __DATA_CONST.__cfstring: 0x3c00
+  __DATA_CONST.__got: 0x550
+  __DATA_CONST.__const: 0x1378
+  __DATA_CONST.__cfstring: 0x3bc0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x5580
-  __DATA.__objc_selrefs: 0x1ae0
-  __DATA.__objc_ivar: 0x284
+  __DATA.__objc_const: 0x5530
+  __DATA.__objc_selrefs: 0x1ac8
+  __DATA.__objc_ivar: 0x27c
   __DATA.__objc_data: 0xb40
   __DATA.__data: 0x510
   __DATA.__bss: 0xf8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 897
-  Symbols:   2687
-  CStrings:  1995
+  Functions: 892
+  Symbols:   2675
+  CStrings:  1984
 
Symbols:
+ GCC_except_table16
+ GCC_except_table47
+ GCC_except_table58
+ GCC_except_table60
+ __56-[WLDFederatedPunchoutReporter _configureTimerWithDate:]_block_invoke.49
+ __block_literal_global.104
+ __block_literal_global.278
+ __block_literal_global.316
+ __block_literal_global.80
- -[WLDFederatedPunchoutReporter analyticsConnection]
- -[WLDFederatedPunchoutReporter setAnalyticsConnection:]
- GCC_except_table59
- GCC_except_table61
- OBJC_IVAR_$_WLDFederatedPunchoutReporter._analyticsConnection
- OBJC_IVAR_$_WLDPlaybackManager._analyticsConnection
- _OBJC_CLASS_$_VSAnalyticsServiceConnection
- __56-[WLDFederatedPunchoutReporter _configureTimerWithDate:]_block_invoke.55
- __73-[WLDFederatedPunchoutReporter _reportPunchoutEvent:withPlaybackSummary:]_block_invoke.cold.1
- ___73-[WLDFederatedPunchoutReporter _reportPunchoutEvent:withPlaybackSummary:]_block_invoke
- ___73-[WLDPlaybackManager _handleReporting:summary:sessionIDKey:isFirstParty:]_block_invoke_2
- __block_literal_global.105
- __block_literal_global.169
- __block_literal_global.290
- __block_literal_global.328
- __block_literal_global.53
- __block_literal_global.81
- _objc_msgSend$analyticsConnection
- _objc_msgSend$serviceWithErrorHandler:
CStrings:
+ "\x05\x121"
+ "WLDFederatedPunchoutReporter - Recording punchout with error %!@(MISSING)"
- "\x05\x12\x11!"
- "@\"VSAnalyticsServiceConnection\""
- "MetricsRefactor"
- "T@\"VSAnalyticsServiceConnection\",&,N,V_analyticsConnection"
- "VSA"
- "WLDFederatedPunchoutReporter - Failed to connect to analytics service: %!@(MISSING)"
- "WLDFederatedPunchoutReporter - Recording punchout to analytics connection %!p(MISSING) with error %!@(MISSING)"
- "WLDPlaybackManager: error with federated analytics service connection: %!@(MISSING)"
- "WLDPlaybackManager: reported summary from inactive player path: %!@(MISSING)"
- "_analyticsConnection"
- "analyticsConnection"
- "serviceWithErrorHandler:"
- "setAnalyticsConnection:"

```
