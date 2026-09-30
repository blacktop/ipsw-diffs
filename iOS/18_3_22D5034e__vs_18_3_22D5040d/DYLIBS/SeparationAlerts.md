## SeparationAlerts

> `/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`

```diff

-104.0.12.0.0
-  __TEXT.__text: 0x2d68c
+107.0.1.0.0
+  __TEXT.__text: 0x2d6a8
   __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_methlist: 0x2e50
-  __TEXT.__const: 0xf8
+  __TEXT.__const: 0x100
   __TEXT.__cstring: 0x14dd
-  __TEXT.__oslogstring: 0x664b
+  __TEXT.__oslogstring: 0x6688
   __TEXT.__gcc_except_tab: 0x238
   __TEXT.__unwind_info: 0x7e0
   __TEXT.__objc_classname: 0x592
CStrings:
+ "%{sensitive}@"
+ "{\"msg%{public}.0s\":\"#SADeviceRecord updateLocation updated\", \"lastLocation\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager checking if alert was triggered at home\", \"location\":\"%{sensitive}@\", \"isEarlyVehicularTrigger\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager handleGeofenceEvent geofenceEvent cannot be mapped to monitoring session\", \"geofence\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager handleGeofenceEvent ignored (recent crash?)\", \"geofence\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager handleGeofenceEvent invalid geofenceEvent\", \"geofence\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager handleGeofenceEvent received geofenceEvent\", \"geofence\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager removing currentVisitOrLOIEvent due to scenario change\", \"currentVisitOrLOIEvent\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager updateLocation update criteria not satisfied\", \"lastLocation\":\"%{sensitive}@\", \"newLocation\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager updateLocation updated\", \"lastLocation\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SAScenarioClassifier addSafeLocation replacing\", \"device\":\"%{private}@\", \"location\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SAScenarioClassifier removeSafeLocation not in set\", \"device\":\"%{private}@\", \"location\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#SATime received event with future date\", \"Event\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#manager:visit got last visit\", \"visits\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"#sa #loi error fetching LOI\", \"visit\":\"%{sensitive}@\", \"error\":\"%{public}@\"}"
+ "{\"msg%{public}.0s\":\"#sa #loi received LOI\", \"loi\":\"%{sensitive}@\", \"loiIdentifier\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa #loi received nil in return when fetching LOI\", \"visit\":\"%{sensitive}@\", \"loiIdentifier\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa ServiceMgr FetchSafe\", \"uuid\":\"%{private}@\", \"name\":\"%{private}@\", \"lat\":\"%{sensitive}f\", \"lon\":\"%{sensitive}f\", \"radius\":\"%{public}f\", \"refFrame\":%{private}lu}"
+ "{\"msg%{public}.0s\":\"#sa ServiceMgr FetchSafeForBeacon\", \"device\":\"%{private}@\", \"uuid\":\"%{private}@\", \"name\":\"%{private}@\", \"lat\":\"%{sensitive}f\", \"lon\":\"%{sensitive}f\", \"radius\":\"%{public}f\", \"refFrame\":%{private}lu}"
+ "{\"msg%{public}.0s\":\"Archiver error\", \"Error\":\"%{private}@\", \"String\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"Ingesting event\", \"Event\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"SADeviceRecord updateLocation update criteria not satisfied\", \"lastLocation\":\"%{sensitive}@\", \"newLocation\":\"%{sensitive}@\"}"
- "%@"
- "{\"msg%{public}.0s\":\"#SADeviceRecord updateLocation updated\", \"lastLocation\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager checking if alert was triggered at home\", \"location\":\"%{private}@\", \"isEarlyVehicularTrigger\":%{private}d}"
- "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager handleGeofenceEvent geofenceEvent cannot be mapped to monitoring session\", \"geofence\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager handleGeofenceEvent ignored (recent crash?)\", \"geofence\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager handleGeofenceEvent invalid geofenceEvent\", \"geofence\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager handleGeofenceEvent received geofenceEvent\", \"geofence\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager removing currentVisitOrLOIEvent due to scenario change\", \"currentVisitOrLOIEvent\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager updateLocation update criteria not satisfied\", \"lastLocation\":\"%{private}@\", \"newLocation\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#SAMonitoringSessionManager updateLocation updated\", \"lastLocation\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#SAScenarioClassifier addSafeLocation replacing\", \"device\":\"%{private}@\", \"location\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#SAScenarioClassifier removeSafeLocation not in set\", \"device\":\"%{private}@\", \"location\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#SATime received event with future date\", \"Event\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#manager:visit got last visit\", \"visits\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#sa #loi error fetching LOI\", \"visit\":\"%{private}@\", \"error\":\"%{public}@\"}"
- "{\"msg%{public}.0s\":\"#sa #loi received LOI\", \"loi\":\"%{private}@\", \"loiIdentifier\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#sa #loi received nil in return when fetching LOI\", \"visit\":\"%{private}@\", \"loiIdentifier\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"#sa ServiceMgr FetchSafe\", \"uuid\":\"%{private}@\", \"name\":\"%{private}@\", \"lat\":\"%{private}f\", \"lon\":\"%{private}f\", \"radius\":\"%{public}f\", \"refFrame\":%{private}lu}"
- "{\"msg%{public}.0s\":\"#sa ServiceMgr FetchSafeForBeacon\", \"device\":\"%{private}@\", \"uuid\":\"%{private}@\", \"name\":\"%{private}@\", \"lat\":\"%{private}f\", \"lon\":\"%{private}f\", \"radius\":\"%{public}f\", \"refFrame\":%{private}lu}"
- "{\"msg%{public}.0s\":\"Archiver error\", \"Error\":\"%{private}@\", \"String\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"Ingesting event\", \"Event\":\"%{private}@\"}"
- "{\"msg%{public}.0s\":\"SADeviceRecord updateLocation update criteria not satisfied\", \"lastLocation\":\"%{private}@\", \"newLocation\":\"%{private}@\"}"

```
