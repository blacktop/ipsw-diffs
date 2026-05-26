## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0x15ffe0
-  __TEXT.__auth_stubs: 0x3890
+960.4.3.0.0
+  __TEXT.__text: 0x160e0c
+  __TEXT.__auth_stubs: 0x3930
   __TEXT.__objc_methlist: 0xae4
   __TEXT.__const: 0x326d5
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__gcc_except_tab: 0x7e4
-  __TEXT.__cstring: 0x2fb5d
-  __TEXT.__unwind_info: 0x1498
+  __TEXT.__cstring: 0x300bd
+  __TEXT.__unwind_info: 0x14b8
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x144
   __TEXT.__objc_methname: 0x2819
   __TEXT.__objc_methtype: 0x1645
   __TEXT.__objc_stubs: 0x2960
   __DATA_CONST.__got: 0x890
-  __DATA_CONST.__const: 0x1dd8
+  __DATA_CONST.__const: 0x1e48
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1c58
-  __AUTH_CONST.__const: 0x90f8
-  __AUTH_CONST.__cfstring: 0xb080
+  __AUTH_CONST.__auth_got: 0x1ca8
+  __AUTH_CONST.__const: 0x9158
+  __AUTH_CONST.__cfstring: 0xb120
   __AUTH_CONST.__objc_const: 0x1530
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x170
-  __DATA.__data: 0x17af0
-  __DATA.__bss: 0x5c8
+  __DATA.__data: 0x17b60
+  __DATA.__bss: 0x5d8
   __DATA.__common: 0xa84
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x310

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 596A41A9-3852-32D4-973C-6AFC5C8F24AE
-  Functions: 1597
-  Symbols:   5128
-  CStrings:  6909
+  UUID: 40800DDF-8663-3959-93DC-201BEF47982C
+  Functions: 1609
+  Symbols:   5166
+  CStrings:  6946
 
Symbols:
+ GCC_except_table1064
+ GCC_except_table1083
+ GCC_except_table1134
+ GCC_except_table1138
+ GCC_except_table1191
+ GCC_except_table1201
+ _APNetworkPathMonitorCopyProperty
+ _APNetworkPathMonitorCreate
+ _APNetworkPathMonitorGetTypeID
+ _APNetworkPathMonitorStart
+ _APNetworkPathMonitorStop
+ _APReceiverRequestProcessorCopyProperty.3980
+ _APReceiverRequestProcessorCopyProperty.7093
+ _APReceiverRequestProcessorCopyProperty.7613
+ _APReceiverRequestProcessorSetProperty.4543
+ _APSRoundToSignificantFigures
+ __APNetworkPathMonitorFinalize
+ __APNetworkPathMonitorGetTypeID
+ __Finalize.6376
+ __GetTypeID.6373
+ __UpdateAVAudioSessionAudioMode.5475
+ ___APNetworkPathMonitorCreate_block_invoke
+ ___APNetworkPathMonitorCreate_block_invoke_2
+ ___APNetworkPathMonitorStop_block_invoke
+ ___block_descriptor_tmp.11
+ ___block_descriptor_tmp.143.5347
+ ___block_descriptor_tmp.171.6256
+ ___block_descriptor_tmp.172.6257
+ ___block_descriptor_tmp.18
+ ___block_descriptor_tmp.42.7166
+ ___block_descriptor_tmp.52.7538
+ ___block_descriptor_tmp.5372
+ ___block_descriptor_tmp.5938
+ ___block_descriptor_tmp.6128
+ ___block_descriptor_tmp.7073
+ ___block_descriptor_tmp.7169
+ ___block_descriptor_tmp.7501
+ ___block_descriptor_tmp.7531
+ ___block_literal_global.5657
+ ___block_literal_global.5879
+ ___block_literal_global.5936
+ ___block_literal_global.7152
+ ___block_literal_global.7529
+ _airplayReqProcessor_reportSessionDurationMetricsIfNeeded
+ _airplayReqProcessor_stopCopyStatsAndDestroyNetworkPathMonitor
+ _audioSession_audioDecoderDecodeCallback.6218
+ _audioSession_audioDecoderDecodeFrame.6205
+ _audioSession_handleMediaDataControlRequest.6095
+ _audioSession_log.6229
+ _audioSession_networkThread.6239
+ _audioSession_performPeriodicTasks.6234
+ _audioSession_sessionLock.6132
+ _audioSession_sessionUnlock.6134
+ _gAPNetworkPathMonitorInitOnce
+ _gAPNetworkPathMonitorTypeID
+ _gAirTunesRelativeTimeOffset.6260
+ _gLogCategory_APNetworkPathMonitor
+ _if_indextoname
+ _kAPNetworkPathMonitorClass
+ _kAPNetworkPathMonitorProperty_MonitoredInterfaceDuration
+ _kAPNetworkPathMonitorProperty_MonitoredInterfaceOnCount
+ _nw_path_get_interface_index
+ _nw_path_monitor_cancel
+ _nw_path_monitor_create
+ _nw_path_monitor_set_cancel_handler
+ _nw_path_monitor_set_queue
+ _nw_path_monitor_set_update_handler
+ _nw_path_monitor_start
+ _strncmp
- GCC_except_table1062
- GCC_except_table1081
- GCC_except_table1132
- GCC_except_table1136
- GCC_except_table1189
- GCC_except_table1197
- _APReceiverRequestProcessorCopyProperty.3979
- _APReceiverRequestProcessorCopyProperty.7082
- _APReceiverRequestProcessorCopyProperty.7570
- _APReceiverRequestProcessorSetProperty.4529
- __Finalize.6359
- __GetTypeID.6356
- __UpdateAVAudioSessionAudioMode.5458
- ___block_descriptor_tmp.143.5330
- ___block_descriptor_tmp.171.6239
- ___block_descriptor_tmp.172.6240
- ___block_descriptor_tmp.42.7155
- ___block_descriptor_tmp.52.7495
- ___block_descriptor_tmp.5355
- ___block_descriptor_tmp.5921
- ___block_descriptor_tmp.6111
- ___block_descriptor_tmp.7062
- ___block_descriptor_tmp.7158
- ___block_descriptor_tmp.7488
- ___block_literal_global.5640
- ___block_literal_global.5862
- ___block_literal_global.5919
- ___block_literal_global.7141
- ___block_literal_global.7486
- _audioSession_audioDecoderDecodeCallback.6201
- _audioSession_audioDecoderDecodeFrame.6188
- _audioSession_handleMediaDataControlRequest.6078
- _audioSession_log.6212
- _audioSession_networkThread.6222
- _audioSession_performPeriodicTasks.6217
- _audioSession_sessionLock.6115
- _audioSession_sessionUnlock.6117
- _gAirTunesRelativeTimeOffset.6243
CStrings:
+ "960.4.3"
+ "APNetworkPathMonitor"
+ "APNetworkPathMonitor.%{ptr}.queue"
+ "APNetworkPathMonitorCopyProperty"
+ "APNetworkPathMonitorCreate"
+ "OSStatus APNetworkPathMonitorCopyProperty(APNetworkPathMonitorRef, CFStringRef, void *)"
+ "OSStatus APNetworkPathMonitorCreate(APNetworkPathMonitorRef *, char *)"
+ "OSStatus APNetworkPathMonitorCreate(APNetworkPathMonitorRef *, char *)_block_invoke"
+ "OSStatus APNetworkPathMonitorStart(APNetworkPathMonitorRef)"
+ "OSStatus APNetworkPathMonitorStop(APNetworkPathMonitorRef)"
+ "OSStatus airplayReqProcessor_reportSessionDurationMetricsIfNeeded(APReceiverRequestProcessorRef)"
+ "[%{ptr}] %@ Copy property error %#m"
+ "[%{ptr}] Create failed %#m"
+ "[%{ptr}] Created [%{ptr}]"
+ "[%{ptr}] Finalize"
+ "[%{ptr}] Receiver session metrics : Duration = %llu sec, type = %d%?{end}, IR duration = %llu sec"
+ "[%{ptr}] Started [%{ptr}]"
+ "[%{ptr}] Starting [%{ptr}]"
+ "[%{ptr}] Stopped [%{ptr}]"
+ "[%{ptr}] Stopping [%{ptr}]"
+ "[%{ptr}] Update handler [%{ptr}], %s starting now"
+ "[%{ptr}] Update handler [%{ptr}], interface now is %s, %s started %llu ms ago"
+ "airplayReqProcessor_createAndStartNetworkPathMonitor"
+ "airplayReqProcessor_reportSessionDurationMetricsIfNeeded"
+ "airplayReqProcessor_stopCopyStatsAndDestroyNetworkPathMonitor"
+ "currentSessionType"
+ "infraRelayDurationSecs"
+ "ir0"
+ "monitoredInterfaceDurationMs"
+ "monitoredInterfaceOnCount"
+ "sessionTotalDurationSecs"
+ "v16@?0^{nw_path=}8"
+ "void _APNetworkPathMonitorFinalize(CFTypeRef)"
- "950.7.1"

```
