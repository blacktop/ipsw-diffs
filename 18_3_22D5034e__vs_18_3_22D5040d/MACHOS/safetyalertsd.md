## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-64.0.4.0.0
-  __TEXT.__text: 0xaae34
+64.0.4.0.1
+  __TEXT.__text: 0xaae78
   __TEXT.__auth_stubs: 0xe90
   __TEXT.__objc_stubs: 0x2340
   __TEXT.__init_offsets: 0x4

   __TEXT.__const: 0x842f
   __TEXT.__gcc_except_tab: 0xa2e4
   __TEXT.__cstring: 0x4346
-  __TEXT.__oslogstring: 0x2518d
+  __TEXT.__oslogstring: 0x251d9
   __TEXT.__objc_classname: 0x1b7
   __TEXT.__objc_methname: 0x28b0
   __TEXT.__objc_methtype: 0x111e
CStrings:
+ "{\"msg%{public}.0s\":\"#bletransport,updateBleDataToAlertData\", \"source\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"bleAlertUID\":%{private, location:escape_only}s, \"regionCode\":%{private, location:escape_only}s, \"ingress_to_server_ts\":\"%{private}0.3f\", \"egress_from_source_ts\":\"%{private}0.3f\", \"event_origin_ts\":\"%{private}0.3f\", \"effective\":\"%{private}0.3f\", \"expires\":\"%{private}0.3f\", \"event_update_number\":\"%{private}0.3f\", \"epi_latitude\":\"%{private}0.3f\", \"epi_longitude\":\"%{private}0.3f\", \"magnitude\":\"%{private}0.3f\", \"depth\":\"%{private}0.3f\", \"mmiLat\":\"%{sensitive}0.3f\", \"mmiLon\":\"%{sensitive}0.3f\", \"mmiLevel\":\"%{private}0.3f\", \"bleAdvertiseTime\":\"%{private}0.3f\", \"effectiveDistance\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#chmgr,onLocationChanged\", \"lat\":\"%{sensitive}0.6f\", \"lon\":\"%{sensitive}0.6f\", \"unc\":\"%{private}0.2f\"}"
+ "{\"msg%{public}.0s\":\"#chsel,onLocationChanged\", \"lat\":\"%{sensitive}0.6f\", \"lon\":\"%{sensitive}0.6f\", \"unc\":\"%{private}0.2f\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onLocationChanged\", \"lat\":\"%{sensitive}0.6f\", \"lon\":\"%{sensitive}0.6f\", \"unc\":\"%{private}0.2f\"}"
+ "{\"msg%{public}.0s\":\"#geometry,isCircleInGeometry\", \"lat\":\"%{sensitive}0.6f\", \"lon\":\"%{sensitive}0.6f\", \"radiusMeters\":\"%{private}0.6f\"}"
+ "{\"msg%{public}.0s\":\"#geometry,isCircleInPolygonResult\", \"lat\":\"%{sensitive}0.6f\", \"lon\":\"%{sensitive}0.6f\", \"inside\":%{private}hhd, \"distance\":\"%{private}0.6f\"}"
+ "{\"msg%{public}.0s\":\"#gi,#generateGlobalTileIdFromLatLonAndGridSizeInDegrees\", \"totalGridsInEachRow\":%{private}lu, \"totalGridsInEachCol\":%{private}lu, \"gridSizeInDegrees\":\"%{private}0.3f\", \"swXIndex\":%{private}lu, \"swYIndex\":%{private}lu, \"curGlobalIndex\":%{private}lu, \"multiplier\":%{private}lu, \"lat\":\"%{sensitive}0.3f\", \"lon\":\"%{sensitive}0.3f\", \"gridLatOffset\":\"%{private}0.3f\", \"gridLonOffset\":\"%{private}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#gi,#generateGlobalTileIdFromLatLonAndGridSizeInDegrees,invalidLoc\", \"lat\":\"%{sensitive}0.3f\", \"lon\":\"%{sensitive}0.3f\", \"gridLatOffset\":\"%{private}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#gm,prepareGridTransitionMetric\", \"Time\":\"%{private}0.3f\", \"Lat\":\"%{sensitive}0.3f\", \"Lon\":\"%{sensitive}0.3f\", \"hAcc\":\"%{private}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#iap,doesIgneousAlertPassPrecheck\", \"source\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"ingress_to_server_ts\":\"%{private}0.3f\", \"egress_from_source_ts\":\"%{private}0.3f\", \"event_origin_ts\":\"%{private}0.3f\", \"effective\":\"%{private}0.3f\", \"expires\":\"%{private}0.3f\", \"event_update_number\":\"%{private}0.3f\", \"epi_latitude\":\"%{private}0.3f\", \"epi_longitude\":\"%{private}0.3f\", \"magnitude\":\"%{private}0.3f\", \"depth\":\"%{private}0.3f\", \"mmiLat\":\"%{sensitive}0.3f\", \"mmiLon\":\"%{sensitive}0.3f\", \"mmiLevel\":\"%{private}0.3f\", \"Magnitude\":\"%{private}0.3f\", \"FollowUpMessageValidTime\":\"%{private}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#iap,doesIgneousLivabilityAlertPassPrecheck\", \"source\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"ingress_to_server_ts\":\"%{private}0.3f\", \"egress_from_source_ts\":\"%{private}0.3f\", \"event_origin_ts\":\"%{private}0.3f\", \"effective\":\"%{private}0.3f\", \"expires\":\"%{private}0.3f\", \"event_update_number\":\"%{private}0.3f\", \"epi_latitude\":\"%{private}0.3f\", \"epi_longitude\":\"%{private}0.3f\", \"magnitude\":\"%{private}0.3f\", \"depth\":\"%{private}0.3f\", \"mmiLat\":\"%{sensitive}0.3f\", \"mmiLon\":\"%{sensitive}0.3f\", \"mmiLevel\":\"%{private}0.3f\", \"Magnitude\":\"%{private}0.3f\", \"FollowUpMessageValidTime\":\"%{private}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#iap,parseIgneousAlert\", \"source\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"alertSignature\":%{private, location:escape_only}s, \"bleAlertData\":%{private, location:escape_only}s, \"bleAlertUID\":%{private, location:escape_only}s, \"ingress_to_server_ts\":\"%{private}0.3f\", \"egress_from_source_ts\":\"%{private}0.3f\", \"event_origin_ts\":\"%{private}0.3f\", \"effective\":\"%{private}0.3f\", \"expires\":\"%{private}0.3f\", \"event_update_number\":\"%{private}0.3f\", \"epi_latitude\":\"%{private}0.3f\", \"epi_longitude\":\"%{private}0.3f\", \"magnitude\":\"%{private}0.3f\", \"depth\":\"%{private}0.3f\", \"mmiSize\":%{private}llu, \"mmiLat\":\"%{sensitive}0.3f\", \"mmiLon\":\"%{sensitive}0.3f\", \"mmiLevel\":\"%{private}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#iap,parseIgneousAlert,MMI\", \"objAtIndex\":%{sensitive, location:escape_only}@, \"lat\":\"%{sensitive}0.3f\", \"lon\":\"%{sensitive}0.3f\", \"mmi\":\"%{private}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#lm,didUpdateLocations\", \"locations\":%{sensitive, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#lm,processLocation,#warning,sameLocation\", \"lat\":\"%{sensitive}f\", \"lon\":\"%{sensitive}f\", \"alt\":\"%{sensitive}f\", \"unc\":\"%{private}f\", \"isLastKnownLocation\":%{public}hhd, \"ts\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"#lm,processLocation,usingLocation\", \"lat\":\"%{sensitive}f\", \"lon\":\"%{sensitive}f\", \"alt\":\"%{sensitive}f\", \"unc\":\"%{private}f\", \"isLastKnownLocation\":%{public}hhd, \"ts\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"#lmTest,InvalidTestInputs\", \"lat\":\"%{sensitive}0.1f\", \"lon\":\"%{sensitive}0.1f\", \"hunc\":\"%{private}0.1f\"}"
+ "{\"msg%{public}.0s\":\"#saanalytics,onLocationChanged\", \"lat\":\"%{sensitive}0.6f\", \"lon\":\"%{sensitive}0.6f\", \"unc\":\"%{private}0.2f\"}"
- "{\"msg%{public}.0s\":\"#bletransport,updateBleDataToAlertData\", \"source\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"bleAlertUID\":%{private, location:escape_only}s, \"regionCode\":%{private, location:escape_only}s, \"ingress_to_server_ts\":\"%{private}0.3f\", \"egress_from_source_ts\":\"%{private}0.3f\", \"event_origin_ts\":\"%{private}0.3f\", \"effective\":\"%{private}0.3f\", \"expires\":\"%{private}0.3f\", \"event_update_number\":\"%{private}0.3f\", \"epi_latitude\":\"%{private}0.3f\", \"epi_longitude\":\"%{private}0.3f\", \"magnitude\":\"%{private}0.3f\", \"depth\":\"%{private}0.3f\", \"mmiLat\":\"%{private}0.3f\", \"mmiLon\":\"%{private}0.3f\", \"mmiLevel\":\"%{private}0.3f\", \"bleAdvertiseTime\":\"%{private}0.3f\", \"effectiveDistance\":%{private}d}"
- "{\"msg%{public}.0s\":\"#chmgr,onLocationChanged\", \"lat\":\"%{private}0.6f\", \"lon\":\"%{private}0.6f\", \"unc\":\"%{private}0.2f\"}"
- "{\"msg%{public}.0s\":\"#chsel,onLocationChanged\", \"lat\":\"%{private}0.6f\", \"lon\":\"%{private}0.6f\", \"unc\":\"%{private}0.2f\"}"
- "{\"msg%{public}.0s\":\"#daemon,onLocationChanged\", \"lat\":\"%{private}0.6f\", \"lon\":\"%{private}0.6f\", \"unc\":\"%{private}0.2f\"}"
- "{\"msg%{public}.0s\":\"#geometry,isCircleInGeometry\", \"lat\":\"%{private}0.6f\", \"lon\":\"%{private}0.6f\", \"radiusMeters\":\"%{private}0.6f\"}"
- "{\"msg%{public}.0s\":\"#geometry,isCircleInPolygonResult\", \"lat\":\"%{private}0.6f\", \"lat\":\"%{private}0.6f\", \"inside\":%{private}hhd, \"distance\":\"%{private}0.6f\"}"
- "{\"msg%{public}.0s\":\"#gi,#generateGlobalTileIdFromLatLonAndGridSizeInDegrees\", \"totalGridsInEachRow\":%{private}lu, \"totalGridsInEachCol\":%{private}lu, \"gridSizeInDegrees\":\"%{private}0.3f\", \"swXIndex\":%{private}lu, \"swYIndex\":%{private}lu, \"curGlobalIndex\":%{private}lu, \"multiplier\":%{private}lu, \"lat\":\"%{private}0.3f\", \"lon\":\"%{private}0.3f\", \"gridLatOffset\":\"%{private}0.3f\", \"gridLonOffset\":\"%{private}0.3f\"}"
- "{\"msg%{public}.0s\":\"#gi,#generateGlobalTileIdFromLatLonAndGridSizeInDegrees,invalidLoc\", \"lat\":\"%{private}0.3f\", \"lon\":\"%{private}0.3f\", \"gridLatOffset\":\"%{private}0.3f\"}"
- "{\"msg%{public}.0s\":\"#gm,prepareGridTransitionMetric\", \"Time\":\"%{private}0.3f\", \"Lat\":\"%{private}0.3f\", \"Lon\":\"%{private}0.3f\", \"hAcc\":\"%{private}0.3f\"}"
- "{\"msg%{public}.0s\":\"#iap,doesIgneousAlertPassPrecheck\", \"source\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"ingress_to_server_ts\":\"%{private}0.3f\", \"egress_from_source_ts\":\"%{private}0.3f\", \"event_origin_ts\":\"%{private}0.3f\", \"effective\":\"%{private}0.3f\", \"expires\":\"%{private}0.3f\", \"event_update_number\":\"%{private}0.3f\", \"epi_latitude\":\"%{private}0.3f\", \"epi_longitude\":\"%{private}0.3f\", \"magnitude\":\"%{private}0.3f\", \"depth\":\"%{private}0.3f\", \"mmiLat\":\"%{private}0.3f\", \"mmiLon\":\"%{private}0.3f\", \"mmiLevel\":\"%{private}0.3f\", \"Magnitude\":\"%{private}0.3f\", \"FollowUpMessageValidTime\":\"%{private}0.3f\"}"
- "{\"msg%{public}.0s\":\"#iap,doesIgneousLivabilityAlertPassPrecheck\", \"source\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"ingress_to_server_ts\":\"%{private}0.3f\", \"egress_from_source_ts\":\"%{private}0.3f\", \"event_origin_ts\":\"%{private}0.3f\", \"effective\":\"%{private}0.3f\", \"expires\":\"%{private}0.3f\", \"event_update_number\":\"%{private}0.3f\", \"epi_latitude\":\"%{private}0.3f\", \"epi_longitude\":\"%{private}0.3f\", \"magnitude\":\"%{private}0.3f\", \"depth\":\"%{private}0.3f\", \"mmiLat\":\"%{private}0.3f\", \"mmiLon\":\"%{private}0.3f\", \"mmiLevel\":\"%{private}0.3f\", \"Magnitude\":\"%{private}0.3f\", \"FollowUpMessageValidTime\":\"%{private}0.3f\"}"
- "{\"msg%{public}.0s\":\"#iap,parseIgneousAlert\", \"source\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"alertSignature\":%{private, location:escape_only}s, \"bleAlertData\":%{private, location:escape_only}s, \"bleAlertUID\":%{private, location:escape_only}s, \"ingress_to_server_ts\":\"%{private}0.3f\", \"egress_from_source_ts\":\"%{private}0.3f\", \"event_origin_ts\":\"%{private}0.3f\", \"effective\":\"%{private}0.3f\", \"expires\":\"%{private}0.3f\", \"event_update_number\":\"%{private}0.3f\", \"epi_latitude\":\"%{private}0.3f\", \"epi_longitude\":\"%{private}0.3f\", \"magnitude\":\"%{private}0.3f\", \"depth\":\"%{private}0.3f\", \"mmiSize\":%{private}llu, \"mmiLat\":\"%{private}0.3f\", \"mmiLon\":\"%{private}0.3f\", \"mmiLevel\":\"%{private}0.3f\"}"
- "{\"msg%{public}.0s\":\"#iap,parseIgneousAlert,MMI\", \"objAtIndex\":%{private, location:escape_only}@, \"lat\":\"%{private}0.3f\", \"lon\":\"%{private}0.3f\", \"mmi\":\"%{private}0.3f\"}"
- "{\"msg%{public}.0s\":\"#lm,didUpdateLocations\", \"locations\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#lm,processLocation,#warning,sameLocation\", \"lat\":\"%{private}f\", \"lon\":\"%{private}f\", \"alt\":\"%{private}f\", \"unc\":\"%{private}f\", \"isLastKnownLocation\":%{public}hhd, \"ts\":\"%{public}f\"}"
- "{\"msg%{public}.0s\":\"#lm,processLocation,usingLocation\", \"lat\":\"%{private}f\", \"lon\":\"%{private}f\", \"alt\":\"%{private}f\", \"unc\":\"%{private}f\", \"isLastKnownLocation\":%{public}hhd, \"ts\":\"%{public}f\"}"
- "{\"msg%{public}.0s\":\"#lmTest,InvalidTestInputs\", \"lat\":\"%{private}0.1f\", \"lon\":\"%{private}0.1f\", \"hunc\":\"%{private}0.1f\"}"
- "{\"msg%{public}.0s\":\"#saanalytics,onLocationChanged\", \"lat\":\"%{private}0.6f\", \"lon\":\"%{private}0.6f\", \"unc\":\"%{private}0.2f\"}"

```
