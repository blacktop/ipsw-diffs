## com.apple.driver.AppleSARService

> `com.apple.driver.AppleSARService`

```diff

 1585.0.0.0.0
-  __TEXT.__os_log: 0x24020
-  __TEXT.__const: 0x124e
-  __TEXT.__cstring: 0x1edbf
-  __TEXT_EXEC.__text: 0xf34d4
+  __TEXT.__os_log: 0x24f7a
+  __TEXT.__const: 0x1286
+  __TEXT.__cstring: 0x1fd60
+  __TEXT_EXEC.__text: 0xfb790
   __TEXT_EXEC.__auth_stubs: 0x730
   __DATA.__data: 0x133
   __DATA.__common: 0x11b8
   __DATA_CONST.__mod_init_func: 0xe8
   __DATA_CONST.__mod_term_func: 0xf0
-  __DATA_CONST.__const: 0xd730
-  __DATA_CONST.__kalloc_type: 0xcf80
+  __DATA_CONST.__const: 0xdd08
+  __DATA_CONST.__kalloc_type: 0xd640
   __DATA_CONST.__kalloc_var: 0x280
   __DATA_CONST.__auth_got: 0x398
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x18
-  Functions: 1826
+  Functions: 1866
   Symbols:   0
-  CStrings:  2347
+  CStrings:  2447
 
CStrings:
+ "#D: %s::%s:%d: Attached to CoreAnalytics service"
+ "#D: %s::%s:%d: SensingCAInfo: angle=%d, fdDist=%s, pitch=%s, roll=%s, facing=%s"
+ "#D: %s::%s:%d: Updating Sensing CA Info"
+ "#D: %s::%s:%d: Updating State Osiris"
+ "%s::%s:%d: CA snapshot (flushCount: %u) already submitted — skipping duplicate"
+ "%s::%s:%d: Enqueueing Sensing CA snapshot: flushCount: %u, reason: %s, tx: %s, device_state: %s, sensing_state: %s, orientation: %s, duration: %u"
+ "%s::%s:%d: Failed to allocate CoreAnalytics event objects"
+ "%s::%s:%d: Failed to create sensing CA flush interrupt"
+ "%s::%s:%d: Failed to create sensing CA snapshot queue"
+ "%s::%s:%d: Failed to setup CoreAnalytics service"
+ "%s::%s:%d: Failed to setup analytic modules"
+ "%s::%s:%d: Feature is not enabled on this device, skip reporting to CA"
+ "%s::%s:%d: Flush triggered due to %s"
+ "%s::%s:%d: Flushing Sensing CA:, reason: %s, duration: %u  tx: %s  device_state: %s, sensing_state: %s, orientation: %s, has_case: %s, angle(neg/0/45/57/92/135/177/180/183): %u/%u/%u/%u/%u/%u/%u/%u/%u, fd_delta(gt100c/0-100c/0-100f/gt100f): %u/%u/%u/%u, pitch_delta(lt10b/w10b/w10a/gt10a): %u/%u/%u/%u, roll_delta(lt10b/w10b/w10a/gt10a): %u/%u/%u/%u, ue_facing_down: %u"
+ "%s::%s:%d: No CA snapshot in queue"
+ "%s::%s:%d: Not attached to core analytics yet"
+ "%s::%s:%d: Required sensing input is null"
+ "%s::%s:%d: SAR RFSensing Decision: Tx indicator: %s, Audio Output: %s, Uplink Constraint Condition: %s, VSWR Occlusion Type1: %s, VSWR Occlusion Type2: %s, Screen On State: %s, Orientation: %s, Antenna on Top: %s, Face Detected: %s, Front Camera: %s, State AB (Tuner): %s, State AB (Osiris): %s, VSWR Learning: %s, VSWR Only Mode: %s, Use Case Detection: %s"
+ "%s::%s:%d: Sensing CA queue or interrupt not initialized"
+ "%s::%s:%d: SensingCAInfo data is null"
+ "%s::%s:%d: State Osiris: %s (Override: %s)"
+ "%s::%s:%d: aborting metric submission due to device just boot"
+ "%s::%s:%d: aborting metric submission due to invalid state combination"
+ "%s::%s:%d: osiris state / orientation is nullptr"
+ "%s::%s:%d: rfSensingCACurrentState only supports kGet"
+ "%s::%s:%d: rfSensingCACurrentState output size mismatch (%u vs %zu)"
+ "121111121222121212111121121121121121121121121122121111211211212112112112"
+ "1211111212221212121111211211211211211211211211221211112112112121121121122111112222222222222"
+ "Body Not In Mode 1/2/3"
+ "Body Prim Ant Not At Top"
+ "Body Screen Off"
+ "Body Type2 Occluded + FCam Off"
+ "Body Type2 Occluded + No Face Detected"
+ "Body Type2 Occluded + No UL Constraint"
+ "Body Type2 Occluded + Type1 Occluded"
+ "Body Use Case Not Supported"
+ "Current Write Index is out of the bound: %d\n"
+ "Not Occluded HiPwr"
+ "Not Occluded LoPwr FCam Off"
+ "Not Occluded LoPwr No Face Detected"
+ "Not Occluded LoPwr No UL Constraint"
+ "Not Occluded LoPwr Type1 Occluded"
+ "Not Occluded LoPwr UC Det Not Supp"
+ "R187"
+ "R188"
+ "State 1"
+ "State 2"
+ "State 3"
+ "State Changed"
+ "TX Turn To Off"
+ "angle_0_duration_s"
+ "angle_135_duration_s"
+ "angle_177_duration_s"
+ "angle_180_duration_s"
+ "angle_183_duration_s"
+ "angle_45_duration_s"
+ "angle_57_duration_s"
+ "angle_92_duration_s"
+ "angle_neg_duration_s"
+ "attachCoreAnalyticsService_block_invoke"
+ "com.apple.Telephony.hsarSensingDecisionVerdict"
+ "deriveSensingStateGated"
+ "device_state"
+ "duration_s"
+ "enqueueFlushSnapshotGated"
+ "fd_dist_closer_duration_s"
+ "fd_dist_farther_duration_s"
+ "fd_dist_nominally_closer_duration_s"
+ "fd_dist_nominally_farther_duration_s"
+ "has_case"
+ "incrementSensingCABucketsGated"
+ "orientation"
+ "pitch_closer_duration_s"
+ "pitch_farther_duration_s"
+ "pitch_nominally_closer_duration_s"
+ "pitch_nominally_farther_duration_s"
+ "rfSensingCACurrentState"
+ "rfSensingCAInfo"
+ "rfSensingCAInfo_block_invoke"
+ "rfSensingCAInfo_block_invoke_2"
+ "rfSensingCALastSubmit"
+ "rfSensingCALastSubmit_block_invoke"
+ "roll_closer_duration_s"
+ "roll_farther_duration_s"
+ "roll_nominally_closer_duration_s"
+ "roll_nominally_farther_duration_s"
+ "sensing_state"
+ "setupSensingCA"
+ "stateABOsiris"
+ "stateABOsiris_block_invoke"
+ "stateABOsiris_block_invoke_2"
+ "static IOReturn AppleSARServiceUserClient::extSARSensingCACurrentState(AppleSARService *, void *, IOExternalMethodArguments *)"
+ "static IOReturn AppleSARServiceUserClient::extSARSensingCAInfo(AppleSARService *, void *, IOExternalMethodArguments *)"
+ "static IOReturn AppleSARServiceUserClient::extSARSensingCALastSubmit(AppleSARService *, void *, IOExternalMethodArguments *)"
+ "static IOReturn AppleSARServiceUserClient::extStateABOsiris(AppleSARService *, void *, IOExternalMethodArguments *)"
+ "submitSensingCAEventGated"
+ "tickSensingCAGated"
+ "tryFlushOnTickStateChange"
+ "ue_facing_down_duration_s"
+ "updateSensingCAInfoGated"
+ "updateStateOsirisGated"
+ "|R187"
+ "|R188"
- "%s::%s:%d: SAR RFSensing Decision: Tx indicator: %s, Audio Output: %s, Uplink Constraint Condition: %s, VSWR Occlusion Type1: %s, VSWR Occlusion Type2: %s, Screen On State: %s, Orientation: %s, Antenna on Top: %s, Face Detected: %s, Front Camera: %s, State AB (Tuner): %s, VSWR Learning: %s, VSWR Only Mode: %s, Use Case Detection: %s"
- "121111121222121212111121121121121121121121121122121111211211212"
- "12111112122212121211112112112112112112112112112212111121121121221"
```
