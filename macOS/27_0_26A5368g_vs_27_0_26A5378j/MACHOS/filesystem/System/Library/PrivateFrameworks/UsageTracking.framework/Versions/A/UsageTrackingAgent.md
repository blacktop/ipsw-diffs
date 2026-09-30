## UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/Versions/A/UsageTrackingAgent`

```diff

-  __TEXT.__text: 0x7167c
-  __TEXT.__auth_stubs: 0x1f20
-  __TEXT.__objc_stubs: 0x45c0
-  __TEXT.__objc_methlist: 0x11c8
+  __TEXT.__text: 0x726d0
+  __TEXT.__auth_stubs: 0x1f30
+  __TEXT.__objc_stubs: 0x4840
+  __TEXT.__objc_methlist: 0x12a0
   __TEXT.__const: 0x1bee
-  __TEXT.__cstring: 0x16b4
+  __TEXT.__cstring: 0x1754
   __TEXT.__objc_classname: 0x446
-  __TEXT.__objc_methname: 0x5aa1
+  __TEXT.__objc_methname: 0x5e51
   __TEXT.__objc_methtype: 0x136a
   __TEXT.__gcc_except_tab: 0x524
-  __TEXT.__oslogstring: 0x55b4
-  __TEXT.__constg_swiftt: 0x1144
+  __TEXT.__oslogstring: 0x5924
+  __TEXT.__constg_swiftt: 0x114c
   __TEXT.__swift5_typeref: 0x1ca6
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_reflstr: 0x455

   __TEXT.__swift_as_entry: 0x7c
   __TEXT.__swift_as_ret: 0x7c
   __TEXT.__swift_as_cont: 0xc0
-  __TEXT.__unwind_info: 0x1028
+  __TEXT.__unwind_info: 0x1070
   __TEXT.__eh_frame: 0xf20
-  __DATA_CONST.__const: 0x28b0
-  __DATA_CONST.__cfstring: 0xd20
+  __DATA_CONST.__const: 0x28b8
+  __DATA_CONST.__cfstring: 0xd60
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0xfa0
-  __DATA_CONST.__got: 0x7b8
+  __DATA_CONST.__auth_got: 0xfa8
+  __DATA_CONST.__got: 0x808
   __DATA_CONST.__auth_ptr: 0x4c0
-  __DATA.__objc_const: 0x30b0
-  __DATA.__objc_selrefs: 0x1458
-  __DATA.__objc_ivar: 0x84
+  __DATA.__objc_const: 0x3180
+  __DATA.__objc_selrefs: 0x14f8
+  __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0xd60
   __DATA.__data: 0x11a8
   __DATA.__bss: 0x1140

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1459
-  Symbols:   864
-  CStrings:  1559
+  Functions: 1487
+  Symbols:   866
+  CStrings:  1602
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _$s14DeviceActivity12EventStreamsV36currentIntelligenceBundleIdentifiersSo12NSOrderedSetCvgZ
+ _BMIntelligenceUsageIdentifier
CStrings:
+ "Checking budgets for current intelligence bundle identifiers"
+ "Could not start tracking budgeted intelligence usage because an error occurred while fetching applications: %{public}@"
+ "Could not start tracking budgeted intelligence usage because an error occurred while fetching categories: %{public}@"
+ "Error fetching budgets for intelligence bundle identifiers: %{public}@, %{public}@"
+ "Intelligence"
+ "Intelligence alarm fired, checking budgets for current intelligence bundle identifiers"
+ "Intelligence alarm fired, no intelligence in use so not checking budgets for current intelligence"
+ "Intelligence registration fired, checking budgets for current intelligence bundle identifiers"
+ "Intelligence registration fired, no intelligence in use so not checking budgets for current intelligence"
+ "Intelligence tombstone event did fire"
+ "No intelligence in use so not checking budgets for current intelligence"
+ "T@\"BMBiomeScheduler\",R,V_intelligenceScheduler"
+ "T@\"BMBiomeScheduler\",R,V_intelligenceTombstoneScheduler"
+ "T@\"BPSDrivableSink\",&,V_intelligenceTombstoneSubscription"
+ "T@\"BPSSink\",&,V_intelligenceSubscription"
+ "Usage"
+ "_checkBudgetStatusForIntelligenceBundleIdentifiers:"
+ "_didCollectLocalActivityForIntelligenceBundleIdentifiers:"
+ "_intelligenceAlarmDidFire"
+ "_intelligenceRegistrationDidFire"
+ "_intelligenceScheduler"
+ "_intelligenceSubscription"
+ "_intelligenceTombstoneEventDidFire"
+ "_intelligenceTombstoneScheduler"
+ "_intelligenceTombstoneSubscription"
+ "_subscribeForApplicationTombstones"
+ "_subscribeForIntelligenceTombstones"
+ "_subscribeForIntelligenceUsage"
+ "_subscribeForNowPlayingTombstones"
+ "_subscribeForVideoTombstones"
+ "_subscribeForWebDomainTombstones"
+ "com.apple.UsageTrackingAgent.alarm.intelligence"
+ "com.apple.UsageTrackingAgent.intelligence-scheduler"
+ "com.apple.UsageTrackingAgent.intelligence-tombstone-scheduler"
+ "currentIntelligenceBundleIdentifiers"
+ "intelligenceScheduler"
+ "intelligenceSubscription"
+ "intelligenceTombstoneScheduler"
+ "intelligenceTombstoneSubscription"
+ "setIntelligenceSubscription:"
+ "setIntelligenceTombstoneSubscription:"

```
