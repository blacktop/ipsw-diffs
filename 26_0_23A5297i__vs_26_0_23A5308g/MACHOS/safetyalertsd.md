## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-64.0.21.0.0
-  __TEXT.__text: 0xd1b7c
+64.0.24.0.0
+  __TEXT.__text: 0xd1d40
   __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_stubs: 0x2dc0
+  __TEXT.__objc_stubs: 0x2d80
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xa84
-  __TEXT.__const: 0x9bd8
-  __TEXT.__gcc_except_tab: 0xc548
-  __TEXT.__cstring: 0x5009
-  __TEXT.__oslogstring: 0x340aa
+  __TEXT.__const: 0x9bf8
+  __TEXT.__gcc_except_tab: 0xc4f0
+  __TEXT.__cstring: 0x4fc0
+  __TEXT.__oslogstring: 0x340d3
   __TEXT.__objc_classname: 0x1ea
-  __TEXT.__objc_methname: 0x369c
+  __TEXT.__objc_methname: 0x366e
   __TEXT.__objc_methtype: 0x1939
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x3c88
+  __TEXT.__unwind_info: 0x3ca0
   __DATA_CONST.__auth_got: 0x7f8
-  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__got: 0x4d8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x8118
-  __DATA_CONST.__cfstring: 0x5660
+  __DATA_CONST.__cfstring: 0x5620
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x1160
-  __DATA.__objc_selrefs: 0xfd8
+  __DATA.__objc_selrefs: 0xfc8
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x430

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C462E975-42C1-3F9A-91BA-00C7781C7302
-  Functions: 3241
-  Symbols:   428
-  CStrings:  4353
+  UUID: A395DE2F-AA4A-3C61-B7BA-F84B14595A9A
+  Functions: 3244
+  Symbols:   426
+  CStrings:  4350
 
Symbols:
- _OBJC_CLASS_$_NSBundle
- _OBJC_CLASS_$_NSConstantArray
CStrings:
+ "Actualización de la alerta sísmica"
+ "Alerta sísmica"
+ "Earthquake Alert Update"
+ "Earthquake Detected Nearby"
+ "Sismo detectado cerca"
+ "integerValue"
+ "sender_id"
+ "{\"msg%{public}.0s\":\"#chsel,getIgneousStateParameters,state\", \"isEnabled\":%{private}hhd, \"inSupportedCountry\":%{private}hhd, \"isInMagnetMode\":%{private}hhd, \"isUserOptedIn\":%{private}hhd, \"inCoverageRegion\":%{private}hhd, \"isInCountry\":%{private}hhd, \"emergencyAlert\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref\", \"toggle\":%{private, location:escape_only}@, \"didSucceed\":%{public}d, \"enabled\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref\", \"toggle\":%{private, location:escape_only}@, \"errorCode\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref,none of the toggles exists\"}"
+ "{\"msg%{public}.0s\":\"#daemon,updateMotionHarvestStatus\", \"improveSafety\":%{private}hhd, \"motionHarvestPref\":%{private}hhd, \"motionHarvestOnlyInCountry\":%{private}hhd, \"motionHarvestAvailable\":%{private}hhd, \"motionHarvestAllowed\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#iap,parse\", \"uid\":%{private, location:escape_only}s, \"alertSignature\":%{private, location:escape_only}s, \"bleAlertData\":%{private, location:escape_only}s, \"bleAlertUID\":%{private, location:escape_only}s, \"ingress_to_server_ts\":\"%{private}0.3f\", \"egress_from_source_ts\":\"%{private}0.3f\", \"event_origin_ts\":\"%{private}0.3f\", \"effective\":\"%{private}0.3f\", \"expires\":\"%{private}0.3f\", \"event_update_number\":\"%{private}0.3f\", \"epi_latitude\":\"%{private}0.3f\", \"epi_longitude\":\"%{private}0.3f\", \"magnitude\":\"%{private}0.3f\", \"depth\":\"%{private}0.3f\", \"mmiLat\":\"%{sensitive}0.3f\", \"mmiLon\":\"%{sensitive}0.3f\", \"mmiLevel\":\"%{private}0.3f\", \"SenderId\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,cleanUpOldAlerts\", \"curTime\":\"%{public}0.3f\", \"ThresholdTimeBetweenAlerts\":\"%{public}0.3f\", \"FollowUpMessageValidTime\":\"%{public}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,isFollowUpReceived\", \"uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,isFollowUpReceived,actual alert not received\", \"uid\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,isIgneousReceived\", \"uid\":%{private, location:escape_only}s, \"bleUid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#igbv,validateAlertSignature,APNS\", \"isAuthenticated\":%{private}hhd}"
- ""
- "/System/Library/UserNotifications/Bundles/com.apple.safetyalerts.bundle"
- "Quake"
- "SAFETY_ALERTS_EARTHQUAKE_ALERT_NEARBY"
- "SAFETY_ALERTS_EARTHQUAKE_ALERT_TITLE"
- "SAFETY_ALERTS_EARTHQUAKE_ALERT_UPDATE"
- "bundleWithPath:"
- "cString"
- "earthquake_alerts"
- "localizedStringForKey:value:table:"
- "{\"msg%{public}.0s\":\"#chsel,getIgneousStateParameters,state\", \"isEnabled\":%{private}hhd, \"inSupportedCountry\":%{private}hhd, \"isInMagnetMode\":%{private}hhd, \"isUserOptedIn\":%{private}hhd, \"inCoverageRegion\":%{private}hhd, \"isInCountry\":%{private}hhd, \"emergencyAlert\":%{private}hhd, \"motionHarvestPref\":%{private}hhd, \"motionHarvestOnlyInCountry\":%{private}hhd, \"motionHarvestAvailable\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref error\"}"
- "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref\", \"opt out\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#daemon,updateCountrySupport\", \"motionHarvestAvailable\":%{private}hhd, \"motionHarvestAllowed\":%{private}hhd, \"improveSafety\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#iap,parse\", \"uid\":%{private, location:escape_only}s, \"alertSignature\":%{private, location:escape_only}s, \"bleAlertData\":%{private, location:escape_only}s, \"bleAlertUID\":%{private, location:escape_only}s, \"ingress_to_server_ts\":\"%{private}0.3f\", \"egress_from_source_ts\":\"%{private}0.3f\", \"event_origin_ts\":\"%{private}0.3f\", \"effective\":\"%{private}0.3f\", \"expires\":\"%{private}0.3f\", \"event_update_number\":\"%{private}0.3f\", \"epi_latitude\":\"%{private}0.3f\", \"epi_longitude\":\"%{private}0.3f\", \"magnitude\":\"%{private}0.3f\", \"depth\":\"%{private}0.3f\", \"mmiLat\":\"%{sensitive}0.3f\", \"mmiLon\":\"%{sensitive}0.3f\", \"mmiLevel\":\"%{private}0.3f\"}"
- "{\"msg%{public}.0s\":\"#igEventTracker,isDupBleReceived,dup apns alert\", \"lastAPNSReceivedTs\":\"%{public}0.3f\"}"
- "{\"msg%{public}.0s\":\"#igEventTracker,isDuplicateAlert,igneous NOT received for followUp\"}"
- "{\"msg%{public}.0s\":\"#igEventTracker,isDuplicateAlert,igneous received for followUp\"}"
- "{\"msg%{public}.0s\":\"#igEventTracker,isFollowUpReceived\", \"uid\":%{private, location:escape_only}s, \"curTime\":\"%{public}0.3f\", \"ThresholdTimeBetweenAlerts\":\"%{public}0.3f\", \"FollowUpMessageValidTime\":\"%{public}0.3f\"}"
- "{\"msg%{public}.0s\":\"#igEventTracker,isIgneousReceived\", \"uid\":%{private, location:escape_only}s, \"bleUid\":%{private, location:escape_only}s, \"curTime\":\"%{public}0.3f\", \"ThresholdTimeBetweenAlerts\":\"%{public}0.3f\", \"FollowUpMessageValidTime\":\"%{public}0.3f\"}"

```
