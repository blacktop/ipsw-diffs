## wirelessinsightsd

> `/System/Library/Frameworks/WirelessInsights.framework/Support/wirelessinsightsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 350.1.0.0.0
-  __TEXT.__text: 0x34a9c4
+  __TEXT.__text: 0x34ce54
   __TEXT.__auth_stubs: 0x5000
-  __TEXT.__objc_stubs: 0xfae0
+  __TEXT.__objc_stubs: 0xfc60
   __TEXT.__init_offsets: 0x2b8
-  __TEXT.__objc_methlist: 0x78a4
-  __TEXT.__gcc_except_tab: 0x2a448
-  __TEXT.__const: 0x17ea3
-  __TEXT.__cstring: 0x15ecb
-  __TEXT.__oslogstring: 0x2ed42
-  __TEXT.__objc_methname: 0x1892c
+  __TEXT.__objc_methlist: 0x7924
+  __TEXT.__gcc_except_tab: 0x2a88c
+  __TEXT.__const: 0x18113
+  __TEXT.__cstring: 0x1602b
+  __TEXT.__oslogstring: 0x2eef2
+  __TEXT.__objc_methname: 0x18b2c
   __TEXT.__objc_classname: 0x1c4e
   __TEXT.__objc_methtype: 0x45ea
   __TEXT.__swift5_typeref: 0x2662

   __TEXT.__swift_as_cont: 0x848
   __TEXT.__swift5_protos: 0x74
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x10470
+  __TEXT.__unwind_info: 0x10548
   __TEXT.__eh_frame: 0x6b00
-  __DATA_CONST.__const: 0x173a8
-  __DATA_CONST.__cfstring: 0x7320
+  __DATA_CONST.__const: 0x17528
+  __DATA_CONST.__cfstring: 0x74e0
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_doubleobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__auth_got: 0x2818
-  __DATA_CONST.__got: 0x13e8
+  __DATA_CONST.__got: 0x1410
   __DATA_CONST.__auth_ptr: 0x768
-  __DATA.__objc_const: 0x145b0
-  __DATA.__objc_selrefs: 0x4528
-  __DATA.__objc_ivar: 0xa1c
+  __DATA.__objc_const: 0x14670
+  __DATA.__objc_selrefs: 0x4588
+  __DATA.__objc_ivar: 0xa2c
   __DATA.__objc_data: 0x5568
   __DATA.__data: 0x67a8
   __DATA.__common: 0x610

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14426
-  Symbols:   2058
-  CStrings:  10385
+  Functions: 14476
+  Symbols:   2063
+  CStrings:  10427
 
Symbols:
+ __ZN3abm15kRFSensingValueE
+ __ZN3abm15kTunerModeStateE
+ __ZN3abm17kRFSensingCommandE
+ __ZN3abm27kEventRFSensingStateChangedE
+ __ZN3abm34kRFSensingSubCommandQueryTunerModeE
CStrings:
+ "350.1~193"
+ "C20@0:8C16"
+ "DailyWirelessUsageMetric:No valid tuner mode state, skipping"
+ "DailyWirelessUsageMetric:Received RF sensing state dict %@"
+ "DailyWirelessUsageMetric:Received tuner mode state update: %u"
+ "DailyWirelessUsageMetric:handleDeviceStateChangedTo: numDeviceStateChanges %lu, numDeviceStateChangesConnected %lu"
+ "Failed to fetch initial RF sensing state, unsupported"
+ "Incorrect key for RF sensing in response, fixing"
+ "Received RF sensing state: %s"
+ "TB,N,V_isDeviceStateAvailable"
+ "TC,N,V_deviceState"
+ "TQ,N,V_numDeviceStateChanges"
+ "TQ,N,V_numDeviceStateChangesConnected"
+ "_deviceState"
+ "_isDeviceStateAvailable"
+ "_numDeviceStateChanges"
+ "_numDeviceStateChangesConnected"
+ "deviceState"
+ "deviceStateA"
+ "deviceStateAConnected"
+ "deviceStateB"
+ "deviceStateBConnected"
+ "deviceStateUnknown"
+ "deviceStateUnknownConnected"
+ "duration_device_state_a"
+ "duration_device_state_a_connected"
+ "duration_device_state_b"
+ "duration_device_state_b_connected"
+ "duration_device_usage_unknown"
+ "duration_device_usage_unknown_connected"
+ "handleABMRFSensingStateChangedWithState:"
+ "isDeviceStateAvailable"
+ "numDeviceStateChanges"
+ "numDeviceStateChangesConnected"
+ "num_device_usage_switches"
+ "num_device_usage_switches_connected"
+ "sarStateToWISDeviceUsageState:"
+ "setDeviceState:"
+ "setIsDeviceStateAvailable:"
+ "setNumDeviceStateChanges:"
+ "setNumDeviceStateChangesConnected:"
+ "unsignedShortValue"
+ "updateDeviceStateDurationTrackers"
- "350.1~198"
```
