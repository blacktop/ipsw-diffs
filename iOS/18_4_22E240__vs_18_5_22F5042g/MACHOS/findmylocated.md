## findmylocated

> `/usr/libexec/findmylocated`

```diff

-93.34.7.11.37
-  __TEXT.__text: 0x4eda70
-  __TEXT.__auth_stubs: 0x5100
+93.35.2.11.8
+  __TEXT.__text: 0x4f66e0
+  __TEXT.__auth_stubs: 0x5160
   __TEXT.__objc_methlist: 0xc0c
-  __TEXT.__const: 0x15930
-  __TEXT.__cstring: 0xe09b
-  __TEXT.__swift5_typeref: 0x60d6
-  __TEXT.__constg_swiftt: 0x62b8
+  __TEXT.__const: 0x15a00
+  __TEXT.__cstring: 0xe1eb
+  __TEXT.__swift5_typeref: 0x60f8
+  __TEXT.__constg_swiftt: 0x6314
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0x67a3
-  __TEXT.__swift5_fieldmd: 0x78a0
+  __TEXT.__swift5_reflstr: 0x67d3
+  __TEXT.__swift5_fieldmd: 0x78d4
   __TEXT.__swift5_assocty: 0x848
-  __TEXT.__objc_methname: 0x295b
-  __TEXT.__swift5_proto: 0x1418
-  __TEXT.__swift5_types: 0x664
+  __TEXT.__objc_methname: 0x2968
+  __TEXT.__swift5_proto: 0x1424
+  __TEXT.__swift5_types: 0x668
   __TEXT.__objc_classname: 0x110
   __TEXT.__objc_methtype: 0x8bd
   __TEXT.__swift5_protos: 0x48
-  __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x177d6
-  __TEXT.__swift_as_entry: 0x11fc
-  __TEXT.__swift_as_ret: 0x1f20
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift5_capture: 0x4594
-  __TEXT.__unwind_info: 0x12f68
-  __TEXT.__eh_frame: 0x3cde4
-  __DATA_CONST.__auth_got: 0x2880
-  __DATA_CONST.__got: 0x1b88
-  __DATA_CONST.__auth_ptr: 0x1be0
-  __DATA_CONST.__const: 0x14998
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __TEXT.__oslogstring: 0x17a26
+  __TEXT.__swift_as_entry: 0x1230
+  __TEXT.__swift_as_ret: 0x1f68
+  __TEXT.__swift5_capture: 0x468c
+  __TEXT.__swift5_entry: 0x8
+  __TEXT.__unwind_info: 0x13090
+  __TEXT.__eh_frame: 0x3d54c
+  __DATA_CONST.__auth_got: 0x28b0
+  __DATA_CONST.__got: 0x1ba8
+  __DATA_CONST.__auth_ptr: 0x1b88
+  __DATA_CONST.__const: 0x14bf0
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__linkguard: 0x33
-  __DATA.__objc_const: 0x5478
-  __DATA.__objc_selrefs: 0xbe8
+  __DATA.__objc_const: 0x5570
+  __DATA.__objc_selrefs: 0xbf0
   __DATA.__objc_data: 0x1028
-  __DATA.__data: 0xff40
-  __DATA.__bss: 0x26f80
-  __DATA.__common: 0x13a8
+  __DATA.__data: 0x100b8
+  __DATA.__bss: 0x27100
+  __DATA.__common: 0x13b0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 15257
-  Symbols:   2618
-  CStrings:  3598
+  Functions: 15356
+  Symbols:   2628
+  CStrings:  3614
 
Symbols:
+ _$s10FindMyBase13WorkItemQueueC21enqueueAndAwaitResultyxxyYaYbKcYaKlFTjTu
+ _$s12FindMyLocate5FenceV13MonitorRegionV12updateRadiusyySdF
+ _$s12FindMyLocate5FenceV13MonitorRegionV13maximumRadiusSdvgZ
+ _$s12FindMyLocate5FenceV13MonitorRegionV13minimumRadiusSdvgZ
+ _$s12FindMyLocate5FenceV16AcceptanceStatusOs23CustomStringConvertibleAAMc
+ _$s12FindMyLocate5FenceV6regionAC13MonitorRegionVvM
+ _$ss15ContinuousClockV7InstantV3nowADvgZ
+ _$ss5Int64VSEsWP
+ _$ss5Int64VSesWP
+ _$ss8DurationV10FindMyBaseE11nanosecondss5Int64Vvg
CStrings:
+ "    Fence radius %{public}f for %{public}s capped to max"
+ "    Fence radius %{public}f for %{public}s capped to min"
+ "Couldn't retrieve MessagingSession while stopping live: No outgoing session (already disconnected)"
+ "Failed to monitor to account state: %@"
+ "Failed to parse server context: %s"
+ "Fence %{public}s will not be triggered as its current acceptance status (%{public}s) does not match the required status (%{public}s)"
+ "FenceService.triggerWorkItemQueue"
+ "Invite date for %{public}s is in the past (%{public}s). Triggering the fence invitation."
+ "MyPersonID set to nil"
+ "Start processing accountStateStream"
+ "_TtC13findmylocated16MigrationService"
+ "analytics: logged location reliability to CA"
+ "com.apple.findmy.findmylocate.secureLocations.locationReliability"
+ "defaultSound"
+ "publishingReason"
+ "triggerFence(id:position:requiredAcceptanceStatus:)"
+ "triggerWorkItemQueue"
- "Error retrieving MessagingSession while stopping live: No outgoing session"
- "triggerFence(id:position:)"

```
