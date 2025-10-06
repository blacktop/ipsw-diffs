## nearbyd

> `/usr/libexec/nearbyd`

```diff

-505.0.17.0.0
-  __TEXT.__text: 0x4cf0f4
-  __TEXT.__auth_stubs: 0x2950
+507.0.1.0.0
+  __TEXT.__text: 0x4cf60c
+  __TEXT.__auth_stubs: 0x28f0
   __TEXT.__objc_stubs: 0x13380
   __TEXT.__init_offsets: 0x6c8
-  __TEXT.__objc_methlist: 0xd40c
-  __TEXT.__gcc_except_tab: 0x52be0
-  __TEXT.__const: 0x355720
-  __TEXT.__cstring: 0x3622a
-  __TEXT.__objc_methname: 0x1d8fb
-  __TEXT.__oslogstring: 0x57902
-  __TEXT.__objc_classname: 0x1ac5
-  __TEXT.__objc_methtype: 0x1ecd5
+  __TEXT.__objc_methlist: 0xd424
+  __TEXT.__gcc_except_tab: 0x52c0c
+  __TEXT.__const: 0x355730
+  __TEXT.__cstring: 0x3621a
+  __TEXT.__objc_methname: 0x1d931
+  __TEXT.__oslogstring: 0x57a02
+  __TEXT.__objc_classname: 0x1ac6
+  __TEXT.__objc_methtype: 0x1ecf0
   __TEXT.__swift5_typeref: 0x9b
   __TEXT.__swift5_capture: 0x20
   __TEXT.__constg_swiftt: 0x9c
   __TEXT.__swift5_reflstr: 0x1a
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1a520
+  __TEXT.__unwind_info: 0x1a5e8
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x14c0
-  __DATA_CONST.__got: 0xa98
+  __DATA_CONST.__auth_got: 0x1490
+  __DATA_CONST.__got: 0xa48
   __DATA_CONST.__auth_ptr: 0xc0
-  __DATA_CONST.__const: 0x23b88
-  __DATA_CONST.__cfstring: 0x15020
+  __DATA_CONST.__const: 0x23b78
+  __DATA_CONST.__cfstring: 0x14fe0
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x268

   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_intobj: 0x678
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x16aa8
+  __DATA.__objc_const: 0x16ae8
   __DATA.__objc_selrefs: 0x5db0
-  __DATA.__objc_ivar: 0x1620
+  __DATA.__objc_ivar: 0x1628
   __DATA.__objc_data: 0x34b0
   __DATA.__data: 0x318c
-  __DATA.__bss: 0xd328
+  __DATA.__bss: 0xd320
   __DATA.__common: 0xd98
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 234460B5-A720-3448-8942-C4837B8367EA
-  Functions: 21001
-  Symbols:   1029
-  CStrings:  21242
+  UUID: 83AE99CE-87CC-33A4-A5F6-A7A5C18AF33E
+  Functions: 21009
+  Symbols:   1013
+  CStrings:  21230
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _xpc_bool_create
+ _xpc_connection_cancel
- _OBJC_CLASS_$_NSBackgroundActivityScheduler
- _XPC_ACTIVITY_CHECK_IN
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_INTERVAL
- _XPC_ACTIVITY_INTERVAL_15_MIN
- _XPC_ACTIVITY_INTERVAL_1_MIN
- _XPC_ACTIVITY_INTERVAL_30_MIN
- _XPC_ACTIVITY_INTERVAL_5_MIN
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _XPC_ACTIVITY_REPEATING
- _xpc_activity_copy_criteria
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_activity_set_criteria
- _xpc_activity_set_state
- _xpc_activity_unregister
- _xpc_dictionary_set_int64
- _xpc_dictionary_set_string
CStrings:
+ "#ils,not enough measurements for cluster %hu"
+ "#rlm,deregister %d in destructor"
+ "#rlm,failed to submit task with error: %@"
+ "#rlm,ranging limit manager update periodic reset"
+ "#rlm,ranging limit manager update periodic reset task complete"
+ "#rlm,ranging limit manager update periodic reset task expiring"
+ "#rlm,submitted ranging limit manager update task successfully"
+ "#rlm,task already submitted, return"
+ "#roseprovider,\t\t\t\t\t      coordinates: [lat: %.11f deg, lon: %.11f deg, alt: %.11f m]"
+ "#roseprovider,\t\t\t\t\t      coordinates:[x: %.3f m, y: %.3f m, z: %.3f m]"
+ "#roseprovider,\t\t\t\tresp %d: [rx_status: 0x%0x, address: 0x%04x, dtm_block_idx: %d, soi_rssi: %.1f, local_ts_sec: %.10f, dtm_ts_sec: %.10f]"
+ "#roseprovider,\t\t                   initator coordinates: [lat: %.11f deg, lon: %.11f deg, alt: %.11f m]"
+ "#roseprovider,\t\t                   initator coordinates: [x: %.3f m, y: %.3f m, z: %.3f m]"
+ "#roseprovider, GOT DTM from [0x%04x]: { [status: %hu, block_idx: %u, round_idx: %u, nRes: %hu, nS: %hu, nF: %hu]. POLL: [rx_status: 0x%0x, addr: 0x%04x, rssi: %.4f, local_ts: %.10f, dtm_ts: %.10f, cfo_ppt: %d]. FINAL: [rx_status: 0x%0x, rssi_dbm: %.1f, local_ts: %.10f, dtm_ts: %.10f, cfo_ppt: %d]. }"
+ "#ses-item-loc,Connection to wireless Coex manager fails"
+ "#ses-item-loc,Ignore any incoming message from WCM"
+ "#ses-item-loc,_processXPCEvent: Coex Event: XPC_ERROR_CONNECTION_INTERRUPTED"
+ "#ses-item-loc,_processXPCEvent: Unexpected XPC connection event: %{public}s"
+ "#ses-item-loc,_processXPCEvent: XPC connection error: %{public}s"
+ "#ses-item-loc,_sendRangingStartOrEndXPCmessageToWRM, WCMR1NBRangingActive = %s"
+ "#ses-item-loc,sending registration msg to WCM"
+ "#system-health,deregister %d in destructor"
+ "#system-health,failed to submit task with error: %@"
+ "#system-health,submitted task successfully"
+ "#system-health,task already submitted, return"
+ "/AppleInternal/Library/BuildRoots/4~B_FvugCO2TTg8P8vOtl-Io6aWHo3Q1_snY6Ct9A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/4~B_FvugCO2TTg8P8vOtl-Io6aWHo3Q1_snY6Ct9A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "0_W"
+ "@\"NSObject<OS_xpc_object>\""
+ "@\"PRBSTActivityManager\""
+ "FALSE"
+ "NIAlishaSignpost_GetKeyCompleteEvent_Process"
+ "NIAlishaSignpost_GetKeyCompleteEvent_Receive"
+ "NIAlishaSignpost_KeyCommandResponseElapse"
+ "NIDLTDOADisableVIO"
+ "PRBSTActivityManager"
+ "TRUE"
+ "_bstActivityGracePeriod"
+ "_bstActivityInterval"
+ "_bstActivityManager"
+ "_coexConnection"
+ "_nbRangingRunning"
+ "_processXPCEvent:"
+ "_sendRangingStartOrEndXPCmessageToWRM:"
+ "_sendRegistrationMessageToWRM"
+ "com.apple.nearbyd.rangingBudget.task"
+ "com.apple.nearbyd.regdownload.queue"
+ "com.apple.nearbyd.regdownload.task"
+ "deregister %d in destructor"
+ "failed to submit task %@ with error: %@"
+ "failed to submit task with error: %@"
+ "regulatory,download,task complete"
+ "regulatory,download,task expiring"
+ "regulatory,download,triggerUpdate"
+ "setScheduleAfter:"
+ "setTrySchedulingBefore:"
+ "submitted regulatory download task successfully"
+ "submitted task %@ successfully"
+ "task already submitted, return"
+ "task with identifier: %@ already submitted, return"
+ "v16@?0@\"BGNonRepeatingSystemTask\"8"
- "#ils,not enough measurmeents for cluster %hu"
- "#roseprovider,\t\taddress: 0x%04x"
- "#roseprovider,\t\tdtm_block_idx: %d"
- "#roseprovider,\t\tdtm_tof_sec: %f"
- "#roseprovider,\t\tdtm_ts_sec: %.10f"
- "#roseprovider,\t\tlocal_ts_sec: %.10f"
- "#roseprovider,\t\tresp_alt: %.11f m"
- "#roseprovider,\t\tresp_lat: %.11f deg"
- "#roseprovider,\t\tresp_lon: %.11f deg"
- "#roseprovider,\t\tresp_x: %.3f m"
- "#roseprovider,\t\tresp_y: %.3f m"
- "#roseprovider,\t\tresp_z: %.3f m"
- "#roseprovider,\t\trx_status: 0x%0x"
- "#roseprovider,\t\tsoi_rssi: %f"
- "#roseprovider,\tblock_idx: %u"
- "#roseprovider,\tfinal_cfo_ppt: %d"
- "#roseprovider,\tfinal_dtm_ts: %.10f"
- "#roseprovider,\tfinal_local_ts: %.10f"
- "#roseprovider,\tfinal_rssi_dbm: %f"
- "#roseprovider,\tfinal_rx_status: 0x%0x"
- "#roseprovider,\tinit_alt: %.3f m"
- "#roseprovider,\tinit_lat: %.11f deg"
- "#roseprovider,\tinit_lon: %.11f deg"
- "#roseprovider,\tinit_x: %.3f m"
- "#roseprovider,\tinit_y: %.3f m"
- "#roseprovider,\tinit_z: %.3f m"
- "#roseprovider,\tnfailures: %hu"
- "#roseprovider,\tnresponders: %hu"
- "#roseprovider,\tnsuccesses: %hu"
- "#roseprovider,\tpoll_address: 0x%04x"
- "#roseprovider,\tpoll_cfo_ppt: %d"
- "#roseprovider,\tpoll_dtm_ts: %.10f"
- "#roseprovider,\tpoll_local_ts: %.10f"
- "#roseprovider,\tpoll_rssi: %f"
- "#roseprovider,\tpoll_rx_status: 0x%0x"
- "#roseprovider,\tresp: %d"
- "#roseprovider,\tround_idx: %u"
- "#roseprovider,\tround_sts_index: 0x%0x"
- "#roseprovider,\tstatus: %hu"
- "#roseprovider,Received dt_tag_rb_cmp_evt cluster: [0x%04x], total resps: [%d], succeed resps: [%d], poll: %d, final: %d: "
- "#ses-loc,Enable Lifecycle timeout case: NoMeasurement after duration %f s to simulate not able to measurement case"
- "#ses-loc,Enable Lifecycle timeout case: NotDiscover to simulate not able to discover case"
- "#ses-loc,anchors coordinates overriden from OOB coordinates"
- "#ses-loc,current block index: %hu, expected address size is %zu"
- "#system-health,scheduleSendingOfSystemHealthReport: Background activity dispatch after destruct"
- "/AppleInternal/Library/BuildRoots/4~B9_QugDcjoNDgC5YX3SjwMTlYaFCh_WBfThTJDo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/4~B9_QugDcjoNDgC5YX3SjwMTlYaFCh_WBfThTJDo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "?8"
- "@\"PRXPCActivityManager\""
- "NIDLTDOALifeCycleNoMeasureAfterDurection"
- "NIDLTDOALifeCycleTimeoutCase"
- "NoMeasurement"
- "NotDiscover"
- "PRXPCActivityManager"
- "PRXPCActivityManager state: %ld"
- "Unexpected activity state %ld"
- "_xpcActivityGracePeriod"
- "_xpcActivityInterval"
- "_xpcActivityManager"
- "checkInForActivityWithCriteria:identifier:"
- "com.apple.nearbyd.rangingBudget.xpcActivity"
- "com.apple.nearbyd.regdownload"
- "regulatory,download,Unexpected activity state %ld"
- "regulatory,download,state,%ld"
- "regulatory,download,unable to set state, %u"
- "regulatory,download,xpc,triggerUpdate"
- "scheduleWithBlock:"
- "setQualityOfService:"
- "setRepeats:"
- "setTolerance:"
- "v16@?0@?<v@?q>8"

```
