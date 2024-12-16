## BasebandTraceHelper

> `/System/Library/PrivateFrameworks/BasebandTraceHelper.framework/BasebandTraceHelper`

```diff

-1211.0.0.0.0
-  __TEXT.__text: 0x46eb4
-  __TEXT.__auth_stubs: 0x1230
+1218.0.0.0.0
+  __TEXT.__text: 0x48da8
+  __TEXT.__auth_stubs: 0x1270
   __TEXT.__init_offsets: 0x30
-  __TEXT.__gcc_except_tab: 0x3458
-  __TEXT.__const: 0x260c
-  __TEXT.__cstring: 0x197a
-  __TEXT.__oslogstring: 0x23dc
-  __TEXT.__unwind_info: 0x14c8
+  __TEXT.__gcc_except_tab: 0x3964
+  __TEXT.__const: 0x276c
+  __TEXT.__cstring: 0x19d8
+  __TEXT.__oslogstring: 0x2508
+  __TEXT.__unwind_info: 0x15b0
   __TEXT.__objc_methname: 0x119
   __TEXT.__objc_stubs: 0x1a0
   __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x7c8
+  __DATA_CONST.__const: 0x7f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x928
-  __AUTH_CONST.__const: 0x20e0
+  __AUTH_CONST.__auth_got: 0x948
+  __AUTH_CONST.__const: 0x2288
   __AUTH_CONST.__cfstring: 0x20
   __DATA.__data: 0x370
   __DATA.__bss: 0x68

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 964
-  Symbols:   1461
-  CStrings:  545
+  Functions: 993
+  Symbols:   1496
+  CStrings:  556
 
Symbols:
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZN21TraceDataRateObserver10feedSampleEj
+ __ZN21TraceDataRateObserver20updateTraceBandwidthEj
+ __ZN21TraceDataRateObserver4initERKNS_10ParametersE
+ __ZN21TraceDataRateObserver6createENSt3__110shared_ptrIN3ctu9LogServerEEERKNS_10ParametersE
+ __ZN21TraceDataRateObserver8snapshotENSt3__110shared_ptrIN3abm5trace9TraceInfoEEE
+ __ZN21TraceDataRateObserverC1ENSt3__110shared_ptrIN3ctu9LogServerEEE
+ __ZN21TraceDataRateObserverC2ENSt3__110shared_ptrIN3ctu9LogServerEEE
+ __ZN3abm5trace11TraceReader20updateTraceBandwidthEj
+ __ZN3abm5trace11TraceReader6createENSt3__110shared_ptrIN3ctu9LogServerEEERKN8dispatch5queueEPKcRKN19TraceFileCollection10ParametersESG_N5trace17LiveFilterSettingEN21TraceDataRateObserver10ParametersE
+ __ZN3abm5trace11TraceReaderC1ENSt3__110shared_ptrIN3ctu9LogServerEEERKN8dispatch5queueEPKcRKN19TraceFileCollection10ParametersESG_N5trace17LiveFilterSettingEN21TraceDataRateObserver10ParametersE
+ __ZN3abm5trace11TraceReaderC2ENSt3__110shared_ptrIN3ctu9LogServerEEERKN8dispatch5queueEPKcRKN19TraceFileCollection10ParametersESG_N5trace17LiveFilterSettingEN21TraceDataRateObserver10ParametersE
+ __ZN3abm5trace9TraceInfo4pushERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEN3xpc5arrayE
+ __ZNK21TraceDataRateObserver7getNameEv
+ __ZNSt3__16chrono12steady_clock3nowEv
+ _xpc_double_create
- __ZN3abm5trace11TraceReader6createENSt3__110shared_ptrIN3ctu9LogServerEEERKN8dispatch5queueEPKcRKN19TraceFileCollection10ParametersESG_N5trace17LiveFilterSettingE
- __ZN3abm5trace11TraceReaderC1ENSt3__110shared_ptrIN3ctu9LogServerEEERKN8dispatch5queueEPKcRKN19TraceFileCollection10ParametersESG_N5trace17LiveFilterSettingE
- __ZN3abm5trace11TraceReaderC2ENSt3__110shared_ptrIN3ctu9LogServerEEERKN8dispatch5queueEPKcRKN19TraceFileCollection10ParametersESG_N5trace17LiveFilterSettingE
CStrings:
+ "#D duration: %llu milliseconds, bandwidth: %lf Mbps, start: %s, end: %s"
+ "#N baseband trace data rate %lf Mbps is higher than %llu Mbps"
+ "BandwidthMbps"
+ "EndTime"
+ "PeakBandwidth"
+ "StartTime"
+ "Watchdog timed out"
+ "error: [client] Failed to set read source for local socket"
+ "failed to create entry array"
+ "failed to create entry dictionary"
+ "trace.dataRateObserver"
+ "warning: data handler required for setting up async local socket read source"
- "error: close local socket failed"

```
