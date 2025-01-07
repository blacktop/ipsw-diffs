## TrackingAvoidance

> `/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance`

```diff

-104.0.12.0.0
-  __TEXT.__text: 0x47af4
+107.0.1.0.0
+  __TEXT.__text: 0x47b18
   __TEXT.__auth_stubs: 0x580
   __TEXT.__objc_methlist: 0x4200
-  __TEXT.__const: 0x328
-  __TEXT.__oslogstring: 0x6934
+  __TEXT.__const: 0x340
+  __TEXT.__oslogstring: 0x69c9
   __TEXT.__cstring: 0x2d80
   __TEXT.__gcc_except_tab: 0x5ac
   __TEXT.__unwind_info: 0xd80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1505
-  Symbols:   1883
-  CStrings:  2933
+  Functions: 1506
+  Symbols:   1884
+  CStrings:  2934
 
CStrings:
+ "#TASingleDeviceRecord removing staged detection:%{sensitive}@"
+ "#TASingleDeviceRecord staging detection:%{sensitive}@"
+ "#TAStore adding:%{sensitive}s"
+ "#TAStore inserting OOO event:%{sensitive}s"
+ "#TAStore not adding %{public}s due to %{private}s:%{sensitive}s"
+ "#TAStore not adding %{public}s due to %{public}s:%{sensitive}s"
+ "#TAStore unreacheable state; in-order TAEvent should be added already: %{sensitive}s"
+ "#TATrackingAvoidanceService detection location associated with %{private}@:%{sensitive}@"
+ "#TATrackingAvoidanceService found:%{sensitive}@"
+ "#TATrackingAvoidanceService requesting:%{sensitive}@"
+ "#TATrackingAvoidanceService update location associated with %{private}@:%{sensitive}@"
+ "#TATrackingAvoidanceService update:%{sensitive}@"
+ "#TAVisitSnapshot _setRepresentativeVisit with input %{sensitive}@ and adjusted representativeVisit to %{sensitive}@"
+ "#TAVisitSnapshot departure POI populated already; drop TACLVisit %{sensitive}@"
+ "#TAVisitSnapshot dropping departure POI b/c there is no departure date: %{sensitive}@"
+ "#TAVisitState Visit snapshot quality is bad. Performing operations to remove bad visit: %{sensitive}@"
+ "#TAVisitState not adding %{public}s due to %{public}s:%{sensitive}s"
+ "#TAVisitState not considering %{public}s due to %{public}s:%{sensitive}s"
+ "%{sensitive}@"
+ "Updating %{sensitive}s to snapshot"
+ "{\"msg%{public}.0s\":\"#TAFilterKnownDevices dropping detection due to Issued state\", \"detection\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#TAFilterKnownDevices got TANotificationImmediacyTypeNever device\", \"detection\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#TAFilterKnownDevices got background immediate type. This is unexpected\", \"detection\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#TASingleDeviceRecord adding background detection to record\", \"detection\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#TASingleDeviceRecord setting first background detection date\", \"detection\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#TASingleDeviceRecord updating first background detection date\", \"detection\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#TATrackingAvoidanceService location too stale to update\", \"advertisement\":\"%{private}@\", \"latestLocation\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#TAVisitState adding PLOI\", \"PLOI\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#TAVisitState merging with other TAVisitState\", \"numVisitSnapshotsAttemptedToAdd\":%{private}llu, \"numInterVisitSnapshotsAttemptedToAdded\":%{private}llu, \"self.numVisitSnapshot\":%{private}lu, \"self.numInterVisitSnapshot\":%{private}lu, \"self.importantLois\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#TAVisitState recovered intervisit snapshot\", \"interval\":\"%{private}@\", \"arrivalVisit\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#manager:nextPLOI got nextPLOI\", \"nextPLOI\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#manager:nextPLOI ignoring low confidence PLOI\", \"nextPLOI\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#manager:nextPLOI missing required info to query\", \"latestVisit\":\"%{sensitive}@\", \"startDate\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#manager:visit got last visit\", \"visits\":\"%{sensitive}@\"}"
- "#TASingleDeviceRecord removing staged detection:%{private}@"
- "#TASingleDeviceRecord staging detection:%{private}@"
- "#TAStore adding:%{private}s"
- "#TAStore inserting OOO event:%{private}s"
- "#TAStore not adding %{public}s due to %{private}s:%{private}s"
- "#TAStore unreacheable state; in-order TAEvent should be added already: %{private}s"
- "#TATrackingAvoidanceService detection location associated with %{private}@:%{private}@"
- "#TATrackingAvoidanceService found:%{private}@"
- "#TATrackingAvoidanceService requesting:%{private}@"
- "#TATrackingAvoidanceService update location associated with %{private}@:%{private}@"
- "#TATrackingAvoidanceService update:%{private}@"
- "#TAVisitSnapshot _setRepresentativeVisit with input %@ and adjusted representativeVisit to %@"
- "#TAVisitSnapshot departure POI populated already; drop TACLVisit %{private}@"
- "#TAVisitSnapshot dropping departure POI b/c there is no departure date: %{private}@"
- "#TAVisitState Visit snapshot quality is bad. Performing operations to remove bad visit: %{private}@"
- "#TAVisitState not adding %{public}s due to %{public}s:%{private}s"
- "#TAVisitState not considering %{public}s due to %{public}s:%{private}s"
- "%{private}@"
- "Updating %{private}s to snapshot"
- "{\"msg%{public}.0s\":\"#TAFilterKnownDevices dropping detection due to Issued state\", \"detection\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#TAFilterKnownDevices got TANotificationImmediacyTypeNever device\", \"detection\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#TAFilterKnownDevices got background immediate type. This is unexpected\", \"detection\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#TASingleDeviceRecord adding background detection to record\", \"detection\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#TASingleDeviceRecord setting first background detection date\", \"detection\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#TASingleDeviceRecord updating first background detection date\", \"detection\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#TATrackingAvoidanceService location too stale to update\", \"advertisement\":\"%{private}@\", \"latestLocation\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#TAVisitState adding PLOI\", \"PLOI\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#TAVisitState merging with other TAVisitState\", \"numVisitSnapshotsAttemptedToAdd\":%{private}llu, \"numInterVisitSnapshotsAttemptedToAdded\":%{private}llu, \"self.numVisitSnapshot\":%{private}lu, \"self.numInterVisitSnapshot\":%{private}lu, \"self.importantLois\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#TAVisitState recovered intervisit snapshot\", \"interval\":\"%{private}@\", \"arrivalVisit\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#manager:nextPLOI got nextPLOI\", \"nextPLOI\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#manager:nextPLOI ignoring low confidence PLOI\", \"nextPLOI\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#manager:nextPLOI missing required info to query\", \"latestVisit\":\"%{private}@\", \"startDate\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#manager:visit got last visit\", \"visits\":\"%{private}@\"}"

```
