## MultitouchHID

> `/System/Library/Extensions/AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin/MultitouchHID`

```diff

-9130.1.0.0.0
-  __TEXT.__text: 0x52680
-  __TEXT.__auth_stubs: 0x1760
+9130.2.0.0.0
+  __TEXT.__text: 0x53754
+  __TEXT.__auth_stubs: 0x1770
   __TEXT.__objc_methlist: 0x1e4
-  __TEXT.__const: 0x1881
-  __TEXT.__cstring: 0x536b
-  __TEXT.__gcc_except_tab: 0xc58
-  __TEXT.__oslogstring: 0x3423
-  __TEXT.__unwind_info: 0x14d8
+  __TEXT.__const: 0x1971
+  __TEXT.__cstring: 0x53b0
+  __TEXT.__gcc_except_tab: 0xc90
+  __TEXT.__oslogstring: 0x3619
+  __TEXT.__unwind_info: 0x1540
   __TEXT.__objc_classname: 0x3e
   __TEXT.__objc_methname: 0x809
   __TEXT.__objc_methtype: 0xe6
   __TEXT.__objc_stubs: 0x9c0
-  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x760
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_selrefs: 0x2f8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xbc0
-  __AUTH_CONST.__const: 0x2a48
-  __AUTH_CONST.__cfstring: 0x5ce0
+  __AUTH_CONST.__auth_got: 0xbc8
+  __AUTH_CONST.__const: 0x2ad8
+  __AUTH_CONST.__cfstring: 0x5d40
   __AUTH_CONST.__objc_const: 0x2e0
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__data: 0xa8
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x150

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF573A14-7316-3A61-ABD0-83A56E56CBFE
-  Functions: 1572
-  Symbols:   2892
-  CStrings:  2146
+  UUID: A8E779DC-D2C5-36E1-95E9-4D4E475AC1F0
+  Functions: 1596
+  Symbols:   2952
+  CStrings:  2161
 
Symbols:
+ GCC_except_table15
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ __ZN23MultitouchReportTrackerC2Ev
+ __ZN28MTTelemetryAnalyticsReporter13trackReportIDEh
+ __ZN28MTTelemetryAnalyticsReporter14logPathReportsEv
+ __ZN28MTTelemetryAnalyticsReporter23scheduleOnDispatchQueueEP16dispatch_queue_s
+ __ZN28MTTelemetryAnalyticsReporter27unscheduleFromDispatchQueueEP16dispatch_queue_s
+ __ZNK23MultitouchReportTracker22iterateReceivedReportsENSt3__18functionIFvhEEE
+ __ZNKSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0NS_9allocatorIS3_EEFvhEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0NS_9allocatorIS3_EEFvhEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0NS_9allocatorIS3_EEFvhEE7__cloneEPNS0_6__baseIS6_EE
+ __ZNKSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0NS_9allocatorIS3_EEFvhEE7__cloneEv
+ __ZNKSt3__18functionIFvhEEclEh
+ __ZNSt3__110__function12__value_funcIFvhEED2B8ne200100Ev
+ __ZNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0NS_9allocatorIS3_EEFvhEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0NS_9allocatorIS3_EEFvhEE7destroyEv
+ __ZNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0NS_9allocatorIS3_EEFvhEED0Ev
+ __ZNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0NS_9allocatorIS3_EEFvhEED1Ev
+ __ZNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0NS_9allocatorIS3_EEFvhEEclEOh
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhS2_NS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhS2_NS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIhJRKNS_21piecewise_construct_tENS_5tupleIJRKhEEENSI_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhS2_NS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE4findIhEENS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhS2_NS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhS2_NS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS2_S7_S5_Lb1EEENS_9allocatorIS2_EEED2Ev
+ __ZNSt3__112__next_primeEm
+ __ZNSt3__117bad_function_callD1Ev
+ __ZNSt3__125__throw_bad_function_callB8ne200100Ev
+ __ZTINSt3__110__function6__baseIFvhEEE
+ __ZTINSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0NS_9allocatorIS3_EEFvhEEE
+ __ZTINSt3__117bad_function_callE
+ __ZTIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0
+ __ZTSNSt3__110__function6__baseIFvhEEE
+ __ZTSNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0NS_9allocatorIS3_EEFvhEEE
+ __ZTSZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0
+ __ZTVNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0NS_9allocatorIS3_EEFvhEEE
+ __ZTVNSt3__117bad_function_callE
+ __ZZN23MultitouchReportTrackerC1EvE9reportIds
+ ____ZN28MTTelemetryAnalyticsReporter23scheduleOnDispatchQueueEP16dispatch_queue_s_block_invoke
CStrings:
+ "Deallocating telemetry reporter (deviceID 0x%llX)"
+ "Sending analytics event for reportID %d: %{public}@ (deviceID 0x%llX)"
+ "Telemetry reporter failed to register frame callback (deviceID 0x%llX)"
+ "Telemetry reporter logging found report IDs (deviceID 0x%llX)"
+ "Telemetry reporter scheduling periodic 24h logging on dispatch queue (deviceID 0x%llX)"
+ "Telemetry reporter starting (deviceID 0x%llX)"
+ "Telemetry reporter stopping (deviceID 0x%llX)"
+ "Telemetry reporter unscheduling from dispatch queue (deviceID 0x%llX)"
+ "com.apple.HID.multitouchPathsReportIDUsage"
+ "i"
+ "reportID"
+ "reportID_value"

```
