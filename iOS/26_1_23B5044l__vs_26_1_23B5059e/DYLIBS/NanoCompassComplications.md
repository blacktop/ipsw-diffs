## NanoCompassComplications

> `/System/Library/NanoTimeKit/ComplicationBundles/NanoCompassComplications.bundle/NanoCompassComplications`

```diff

-676.2.4.0.0
-  __TEXT.__text: 0x3e8e8
-  __TEXT.__auth_stubs: 0xa80
+676.2.12.0.0
+  __TEXT.__text: 0x3f9d8
+  __TEXT.__auth_stubs: 0xa90
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x3b44
+  __TEXT.__objc_methlist: 0x3be4
   __TEXT.__const: 0x544
-  __TEXT.__cstring: 0x3b4e
+  __TEXT.__cstring: 0x3cee
   __TEXT.__ustring: 0xd6
-  __TEXT.__oslogstring: 0x3cd1
-  __TEXT.__gcc_except_tab: 0xcf0
+  __TEXT.__oslogstring: 0x3da0
+  __TEXT.__gcc_except_tab: 0xb40
   __TEXT.__constg_swiftt: 0x18c
   __TEXT.__swift5_typeref: 0x58
   __TEXT.__swift5_fieldmd: 0x90
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_reflstr: 0x25
-  __TEXT.__unwind_info: 0x1088
-  __TEXT.__objc_classname: 0x9b2
-  __TEXT.__objc_methname: 0x8ba9
-  __TEXT.__objc_methtype: 0x132f
-  __TEXT.__objc_stubs: 0x71e0
-  __DATA_CONST.__got: 0x668
-  __DATA_CONST.__const: 0xca0
-  __DATA_CONST.__objc_classlist: 0x290
-  __DATA_CONST.__objc_catlist: 0x18
+  __TEXT.__unwind_info: 0x10e0
+  __TEXT.__objc_classname: 0xa0d
+  __TEXT.__objc_methname: 0x8c91
+  __TEXT.__objc_methtype: 0x137c
+  __TEXT.__objc_stubs: 0x7300
+  __DATA_CONST.__got: 0x678
+  __DATA_CONST.__const: 0xdb0
+  __DATA_CONST.__objc_classlist: 0x298
+  __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2378
+  __DATA_CONST.__objc_selrefs: 0x23c8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1b8
-  __DATA_CONST.__objc_arraydata: 0x1120
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__const: 0x9e0
-  __AUTH_CONST.__cfstring: 0x2ee0
-  __AUTH_CONST.__objc_const: 0x6d78
+  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_arraydata: 0x1140
+  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__const: 0xa00
+  __AUTH_CONST.__cfstring: 0x2f60
+  __AUTH_CONST.__objc_const: 0x6ec0
   __AUTH_CONST.__objc_doubleobj: 0x4d0
-  __AUTH_CONST.__objc_intobj: 0x4b0
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__objc_intobj: 0x4c8
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x3e8
-  __AUTH.__objc_data: 0x1b98
+  __AUTH.__objc_data: 0x1be8
   __AUTH.__data: 0x160
-  __DATA.__objc_ivar: 0x51c
+  __DATA.__objc_ivar: 0x52c
   __DATA.__data: 0x3cc
-  __DATA.__bss: 0x928
+  __DATA.__bss: 0x948
   __DATA.__common: 0x38
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 95454033-FCC5-3856-9E04-0510DC72F916
-  Functions: 1578
-  Symbols:   676
-  CStrings:  3042
+  UUID: BD86FAF8-BE56-30AF-B7E8-A7626D689CE1
+  Functions: 1608
+  Symbols:   680
+  CStrings:  3078
 
Symbols:
+ _GlobalGuideTypeEnabledStatesKey
+ _OBJC_CLASS_$_NCGuidesEnabledState
+ _OBJC_CLASS_$_NSThread
+ _OBJC_METACLASS_$_NCGuidesEnabledState
+ _dispatch_sync
- _GlobalGuideTypeToggleStatesKey
CStrings:
+ "%s: Initialized guide enabled states: %@"
+ "%s: No change needed. Global enabled state for type %ld is already %d."
+ "%s: Setting global enabled state for guide type %ld to %d"
+ "%s: Updating parked car waypoint. Posting ParkedCarWaypointChangedNotification."
+ "%{public}s: Encountered unexpected guide type. %ld"
+ "%{public}s: Error fetching waypoints for user guides: %{public}@"
+ "%{public}s: Maximum priority compass waypoints is %lu"
+ "-[NCGuidesEnabledState NSStringFromNCGuideType:]"
+ "-[NCGuidesEnabledState init]"
+ "-[NCGuidesManager _fetchEnabledWaypointsForUserGuidesRestrictedToRadius:around:maximumCount:handler:]"
+ "-[NCGuidesManager _fetchEnabledWaypointsForUserGuidesRestrictedToRadius:around:maximumCount:handler:]_block_invoke"
+ "-[NCGuidesManager maxPriorityCompassWaypoints]_block_invoke"
+ "-[NCGuidesManager setGlobalEnabledState:forGuideType:]"
+ "-[NSArray(NCWaypointWithDistanceMergeSorted) mergeWithSortedWaypoints:maximumCount:]"
+ "@\"NCGuidesEnabledState\""
+ "@\"NSArray\"8@?0"
+ "@32@0:8@16Q24"
+ "B24@0:8q16"
+ "CompassGuideType"
+ "GlobalGuideTypeEnabledStates"
+ "MapUserGuideType"
+ "MapsDatabaseGuideType"
+ "MaxPriorityCompassWaypoints"
+ "NCGuidesEnabledState"
+ "NCWaypointWithDistanceDeduplication"
+ "NCWaypointWithDistanceMergeSorted"
+ "NSStringFromNCGuideType:"
+ "NearbyPOIGuideType"
+ "_backupDisabledGuides"
+ "_backupEnabledStates"
+ "_currentlyDisabledGuides"
+ "_disabledGuidesQueue"
+ "_fetchEnabledWaypointsForUserGuidesRestrictedToRadius:around:maximumCount:handler:"
+ "_globalGuideTypeEnabledStates"
+ "_guideTypeName"
+ "_guidesEnabledState"
+ "_lock"
+ "_lock_saveGuideEnabledStatesToDefaults"
+ "_withLock:"
+ "arrayWithCapacity:"
+ "com.apple.nanocompass.corelocation-fetch-queue"
+ "com.apple.nanocompass.guidesmanager.disabledguides"
+ "dedupedWaypointsWithVisitedMUIDs:"
+ "getGlobalEnabledState:"
+ "isEnabledForGuideType:"
+ "isMainThread"
+ "maxPriorityCompassWaypoints"
+ "mergeWithSortedWaypoints:maximumCount:"
+ "setEnabled:forGuideType:"
+ "setGlobalEnabledState:forGuideType:"
+ "setWithArray:"
+ "subarrayWithRange:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "%s: Fetching MSCollections failed with %{public}@"
- "%s: Loaded global toggle states: %@"
- "%s: No change needed. Global toggle state for type %ld is already %d."
- "%s: Setting global toggle state for guide type %ld to %d"
- "-[NCGuidesManager _fetchEnabledWaypointsForUserGuidesRestrictingTo:ofLocation:maxCount:]"
- "-[NCGuidesManager _mergeSortedWaypoints:withOtherSortedWaypoints:maxCount:]"
- "-[NCGuidesManager setGlobalToggleState:forGuideType:]"
- "@40@0:8@16@24Q32"
- "GlobalGuideTypeToggleStates"
- "T@\"NSDictionary\",R,C,N"
- "_defaultGlobalGuideTypeToggleStates"
- "_fetchEnabledWaypointsForUserGuidesRestrictingTo:ofLocation:maxCount:"
- "_filterWaypoints:updatingSeenMUIDs:"
- "_globalGuideTypeToggleStates"
- "_mergeSortedWaypoints:withOtherSortedWaypoints:maxCount:"
- "com.apple.NanoCompass.corelocation-fetch-queue"
- "didChangeValueForKey:"
- "globalGuideTypeToggleStates"
- "setGlobalToggleState:forGuideType:"
- "willChangeValueForKey:"

```
