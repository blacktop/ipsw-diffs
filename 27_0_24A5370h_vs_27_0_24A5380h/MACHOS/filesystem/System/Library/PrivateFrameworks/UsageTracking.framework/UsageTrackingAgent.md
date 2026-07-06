## UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent`

```diff

-  __TEXT.__text: 0x72840
-  __TEXT.__auth_stubs: 0x2400
-  __TEXT.__objc_stubs: 0x4560
-  __TEXT.__objc_methlist: 0x11b8
+  __TEXT.__text: 0x73794
+  __TEXT.__auth_stubs: 0x2410
+  __TEXT.__objc_stubs: 0x47e0
+  __TEXT.__objc_methlist: 0x1290
   __TEXT.__const: 0x1ede
-  __TEXT.__cstring: 0x17c4
+  __TEXT.__cstring: 0x1864
   __TEXT.__objc_classname: 0x455
-  __TEXT.__objc_methname: 0x5b01
+  __TEXT.__objc_methname: 0x5eb1
   __TEXT.__objc_methtype: 0x138e
   __TEXT.__gcc_except_tab: 0x514
-  __TEXT.__oslogstring: 0x5726
-  __TEXT.__constg_swiftt: 0x1148
+  __TEXT.__oslogstring: 0x5a86
+  __TEXT.__constg_swiftt: 0x1150
   __TEXT.__swift5_typeref: 0x1de6
   __TEXT.__swift5_fieldmd: 0x568
   __TEXT.__swift5_builtin: 0x8c

   __TEXT.__swift_as_ret: 0x80
   __TEXT.__swift_as_cont: 0xcc
   __TEXT.__swift5_protos: 0x80
-  __TEXT.__unwind_info: 0x1048
+  __TEXT.__unwind_info: 0x1090
   __TEXT.__eh_frame: 0x1090
-  __DATA_CONST.__const: 0x2838
-  __DATA_CONST.__cfstring: 0xd80
+  __DATA_CONST.__const: 0x2840
+  __DATA_CONST.__cfstring: 0xdc0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x1210
-  __DATA_CONST.__got: 0x810
+  __DATA_CONST.__auth_got: 0x1218
+  __DATA_CONST.__got: 0x860
   __DATA_CONST.__auth_ptr: 0x4d8
-  __DATA.__objc_const: 0x3070
-  __DATA.__objc_selrefs: 0x1448
-  __DATA.__objc_ivar: 0x84
+  __DATA.__objc_const: 0x3140
+  __DATA.__objc_selrefs: 0x14e8
+  __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0xd40
   __DATA.__data: 0x12e8
   __DATA.__bss: 0x15c0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1484
-  Symbols:   952
-  CStrings:  1574
+  Functions: 1512
+  Symbols:   954
+  CStrings:  1617
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_protos : content changed
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
