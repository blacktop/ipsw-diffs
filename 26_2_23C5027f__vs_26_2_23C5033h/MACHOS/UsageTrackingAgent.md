## UsageTrackingAgent

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTrackingAgent`

```diff

-392.2.2.0.0
-  __TEXT.__text: 0x645dc
+392.2.3.0.0
+  __TEXT.__text: 0x65130
   __TEXT.__auth_stubs: 0x20b0
-  __TEXT.__objc_stubs: 0x3820
-  __TEXT.__objc_methlist: 0xfe8
+  __TEXT.__objc_stubs: 0x3a80
+  __TEXT.__objc_methlist: 0x10c8
   __TEXT.__const: 0x1aae
-  __TEXT.__cstring: 0x1fee
-  __TEXT.__objc_classname: 0x1da
-  __TEXT.__objc_methname: 0x4c75
-  __TEXT.__objc_methtype: 0x105c
+  __TEXT.__cstring: 0x1f8e
+  __TEXT.__objc_classname: 0x1db
+  __TEXT.__objc_methname: 0x51dc
+  __TEXT.__objc_methtype: 0x10bb
   __TEXT.__gcc_except_tab: 0x780
-  __TEXT.__oslogstring: 0x5636
+  __TEXT.__oslogstring: 0x56d6
   __TEXT.__constg_swiftt: 0x1094
   __TEXT.__swift5_typeref: 0x1c0e
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift5_protos: 0x80
   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x6c
-  __TEXT.__unwind_info: 0xf60
+  __TEXT.__unwind_info: 0xf80
   __TEXT.__eh_frame: 0xeb8
   __DATA_CONST.__auth_got: 0x1068
   __DATA_CONST.__got: 0x760
   __DATA_CONST.__auth_ptr: 0x480
-  __DATA_CONST.__const: 0x23f8
-  __DATA_CONST.__cfstring: 0xcc0
+  __DATA_CONST.__const: 0x2420
+  __DATA_CONST.__cfstring: 0xd40
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2c90
-  __DATA.__objc_selrefs: 0x1338
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_const: 0x2e18
+  __DATA.__objc_selrefs: 0x13d8
+  __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0xb58
   __DATA.__data: 0x10a8
   __DATA.__bss: 0x1140

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: FDE340D9-0B45-3E38-8F49-A0A87496414C
-  Functions: 1315
+  UUID: D311EFBC-ECC1-30B7-AF0A-A5E723C6A170
+  Functions: 1343
   Symbols:   870
-  CStrings:  1503
+  CStrings:  1552
 
CStrings:
+ "@\"BPSDrivableSink\""
+ "Application tombstone event did fire"
+ "B16@?0@\"BMStoreEvent\"8"
+ "Finished refreshing local device activity after tombstone event."
+ "Now playing tombstone event did fire"
+ "Resetting all data and budgets after tombstone event."
+ "Resetting all data and caching time remaining for budgets after tombstone event."
+ "T@\"BMBiomeScheduler\",R,V_applicationTombstoneScheduler"
+ "T@\"BMBiomeScheduler\",R,V_nowPlayingTombstoneScheduler"
+ "T@\"BMBiomeScheduler\",R,V_videoTombstoneScheduler"
+ "T@\"BMBiomeScheduler\",R,V_webDomainTombstoneScheduler"
+ "T@\"BPSDrivableSink\",&,V_applicationTombstoneSubscription"
+ "T@\"BPSDrivableSink\",&,V_nowPlayingTombstoneSubscription"
+ "T@\"BPSDrivableSink\",&,V_videoTombstoneSubscription"
+ "T@\"BPSDrivableSink\",&,V_webDomainTombstoneSubscription"
+ "Video tombstone event did fire"
+ "Web domain tombstone event did fire"
+ "_applicationTombstoneEventDidFire"
+ "_applicationTombstoneScheduler"
+ "_applicationTombstoneSubscription"
+ "_nowPlayingTombstoneEventDidFire"
+ "_nowPlayingTombstoneScheduler"
+ "_nowPlayingTombstoneSubscription"
+ "_resetAllDataAndCacheTimeRemainingForBudgetsAfterTombstone"
+ "_resetAllDataAndResetBudgetsAfterTombstone"
+ "_videoTombstoneEventDidFire"
+ "_videoTombstoneScheduler"
+ "_videoTombstoneSubscription"
+ "_webDomainTombstoneEventDidFire"
+ "_webDomainTombstoneScheduler"
+ "_webDomainTombstoneSubscription"
+ "applicationTombstoneScheduler"
+ "applicationTombstoneSubscription"
+ "com.apple.UsageTrackingAgent.application-tombstone-scheduler"
+ "com.apple.UsageTrackingAgent.now-playing-tombstone-scheduler"
+ "com.apple.UsageTrackingAgent.video-tombstone-scheduler"
+ "com.apple.UsageTrackingAgent.web-domain-tombstone-scheduler"
+ "nowPlayingTombstoneScheduler"
+ "nowPlayingTombstoneSubscription"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "setApplicationTombstoneSubscription:"
+ "setNowPlayingTombstoneSubscription:"
+ "setVideoTombstoneSubscription:"
+ "setWebDomainTombstoneSubscription:"
+ "sinkWithCompletion:shouldContinue:"
+ "tombstoneDSLPublisherWithUseCase:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"
+ "videoTombstoneScheduler"
+ "videoTombstoneSubscription"
+ "webDomainTombstoneScheduler"
+ "webDomainTombstoneSubscription"
- "Finished refreshing local device activity due to Duet tombstone event."
- "Received Duet tombstone event %{public}s; clearing eligible posted notifications, reseting alarms and checking all budgets for current usage"
- "_tombstoneEventDidFire:"
- "com.apple.UsageTrackingAgent.distributed-notification.duet-application-usage-did-tombstone"
- "com.apple.UsageTrackingAgent.distributed-notification.duet-now-playing-usage-did-tombstone"
- "com.apple.UsageTrackingAgent.distributed-notification.duet-video-usage-did-tombstone"
- "com.apple.UsageTrackingAgent.distributed-notification.duet-web-domain-usage-did-tombstone"
- "v24@0:8r*16"

```
