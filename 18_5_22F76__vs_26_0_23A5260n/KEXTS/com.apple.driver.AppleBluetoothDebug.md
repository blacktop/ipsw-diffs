## com.apple.driver.AppleBluetoothDebug

> `com.apple.driver.AppleBluetoothDebug`

```diff

 45.0.0.0.0
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x17e3
-  __TEXT_EXEC.__text: 0xb5a4
+  __TEXT_EXEC.__text: 0xb654
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xf8
   __DATA.__common: 0x90

   __DATA_CONST.__const: 0xf88
   __DATA_CONST.__kalloc_type: 0x680
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: FE3DA18B-4ADF-329F-9B11-858C43D5179C
+  UUID: 13CF88C2-5FC0-366E-BB50-861F002A9F9A
   Functions: 163
   Symbols:   0
   CStrings:  206
Functions:
~ __ZN7BTDebug5startEP9IOService : 2312 -> 2324
~ sub_fffffff008d81cf0 -> sub_fffffff008f923bc : 1320 -> 1312
~ __ZN7BTDebug26initCoreCaptureForLogFlowsEv : 1648 -> 1716
~ __ZN7BTDebug17enqueueAsyncEventENS_14AsyncEventTypeEPNS_10AsyncEvent7PayloadE : 904 -> 900
~ __ZN7BTDebug17asyncEventHandlerEv : 2584 -> 2580
~ __ZN7BTDebug14queueLogBufferEPNS_9LogBufferE : 884 -> 876
~ __ZN7BTDebug18mapCrashInfoBufferEv : 1148 -> 1144
~ __ZN7BTDebug8coreDumpEyPKcPN14BTDebugService18CoreDumpCompletionE : 948 -> 944
~ __ZN7BTDebug13coreDumpGatedEPNS_15CoreDumpContextE : 2884 -> 2876
~ __ZN7BTDebug13enableLoggingEjjPK13LogFlowParamsj : 540 -> 536
~ __ZN7BTDebug18enableLoggingGatedEjjPK13LogFlowParamsj : 1828 -> 1848
~ __ZN7BTDebug21enableLoggingInternalEv : 1996 -> 1984
~ sub_fffffff008d87888 -> sub_fffffff008f97f74 : 272 -> 268
~ __ZN7BTDebug22disableLoggingInternalEv : 648 -> 644
~ sub_fffffff008d87de8 -> sub_fffffff008f984cc : 276 -> 272
~ __ZN7BTDebug13dumpLogsGatedEPKc : 992 -> 988
~ __ZN7BTDebug16readLogsCompleteEPviPN14BTDebugService7LogDataEj : 1820 -> 1876
~ __ZN7BTDebug15configureReportEP19IOReportChannelListjPvS2_ : 456 -> 452
~ __ZN7BTDebug12updateReportEP19IOReportChannelListjPvS2_ : 456 -> 452
~ sub_fffffff008d8a774 -> sub_fffffff008f9ae80 : 148 -> 188
~ sub_fffffff008d8a880 -> sub_fffffff008f9afb4 : 220 -> 268
~ __ZN17BTDebugUserClient11clientCloseEv : 424 -> 420
~ sub_fffffff008d8b728 -> sub_fffffff008f9be88 : 80 -> 96

```
