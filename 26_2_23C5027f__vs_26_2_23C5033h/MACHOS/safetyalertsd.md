## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-64.0.36.0.0
-  __TEXT.__text: 0xf0ce8
+64.0.38.0.0
+  __TEXT.__text: 0xf3094
   __TEXT.__auth_stubs: 0xfe0
   __TEXT.__objc_stubs: 0x30a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xacc
-  __TEXT.__const: 0x9da0
-  __TEXT.__gcc_except_tab: 0xeb00
-  __TEXT.__cstring: 0x5b20
-  __TEXT.__oslogstring: 0x3be28
+  __TEXT.__objc_methlist: 0xadc
+  __TEXT.__const: 0x9dde
+  __TEXT.__gcc_except_tab: 0xecbc
+  __TEXT.__cstring: 0x5b2e
+  __TEXT.__oslogstring: 0x3cbe3
   __TEXT.__objc_classname: 0x1ea
-  __TEXT.__objc_methname: 0x3946
-  __TEXT.__objc_methtype: 0x1a2c
+  __TEXT.__objc_methname: 0x39b7
+  __TEXT.__objc_methtype: 0x1a87
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x4188
+  __TEXT.__unwind_info: 0x41c8
   __DATA_CONST.__auth_got: 0x800
   __DATA_CONST.__got: 0x580
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x8560
-  __DATA_CONST.__cfstring: 0x60e0
+  __DATA_CONST.__cfstring: 0x6100
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0x1168
-  __DATA.__objc_selrefs: 0x1098
-  __DATA.__objc_ivar: 0x7c
+  __DATA.__objc_const: 0x1190
+  __DATA.__objc_selrefs: 0x10a0
+  __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x438
   __DATA.__bss: 0x508
-  __DATA.__common: 0x120
+  __DATA.__common: 0x128
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0805B8D8-EEDC-3BE4-BEFA-A6C4F14CF32C
-  Functions: 3450
+  UUID: 233E6295-9A5D-3B86-A347-7344800D2998
+  Functions: 3457
   Symbols:   448
-  CStrings:  4850
+  CStrings:  4880
 
CStrings:
+ "%s.notif_%@"
+ "@88@0:8@16r*24Q32Q40Q48r*56r*64{shared_ptr<SACoreAnalytics>=^{SACoreAnalytics}^{__shared_weak_count}}72"
+ "_silentInterruptionLevel"
+ "initWithQueue:bundleIdentifier:authorizationOption:interruptionLevel:silentInterruptionLevel:extension:categoryName:analyticsRef:"
+ "is_last_alert"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"
+ "{\"msg%{public}.0s\":\"#channel,alert_not_dict\", \"alert_index\":%{private}d, \"alert_class\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#channel,processing_alert\", \"alert_index\":%{private}d, \"is_last_alert\":%{public}hhd, \"alert_keys_count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#chsel,isSARegistrationAllowed,state\", \"isSaRegisterPreCheckPass\":%{public}hhd, \"isSaRegisterPreCheckPassForWatch\":%{public}hhd, \"isInCountry\":%{public}hhd, \"requiresTelephony\":%{public}hhd, \"isTelephonySupported\":%{public}hhd, \"isParticipating\":%{public}hhd, \"isCompanion\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#daemon,addDisplayedWeaMessage\", \"weaMessage\":%{private, location:escape_only}s, \"timestamp\":\"%{public}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#daemon,addDisplayedWeaMessage,complete\", \"totalTrackedMessages\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#daemon,addDisplayedWeaMessage,removedExpired\", \"removedCount\":%{public}lu, \"expiryThreshold\":\"%{public}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#daemon,addDisplayedWeaMessage,removingOldestBySize\", \"currentSize\":%{public}lu, \"maxSize\":%{public}lu, \"excessCount\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,forwarding to GeneralSafetyAlertDisplay\", \"isWeaReceived\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,weaAlreadyDisplayed\", \"matchedCmamLongText\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#daemon,pushSafetyAlertsSettingsToCompanion,fCompanionMessenger invalid\"}"
+ "{\"msg%{public}.0s\":\"#daemon,wasWeaDisplayedForContent,found\", \"content\":%{private, location:escape_only}s, \"matchedTimestamp\":\"%{public}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#daemon,wasWeaDisplayedForContent,notFound\", \"content\":%{private, location:escape_only}s, \"checkedMessages\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#fum,onFollowUpAlertReceived\", \"wasActualAlertReceived\":%{private}hhd, \"isIgneousAwarenessReceived\":%{private}hhd, \"isIgneousActionReceived\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#gap,parse,success\", \"uid\":%{private, location:escape_only}s, \"sessionId\":%{private, location:escape_only}s, \"status\":%{private}d, \"msgType\":%{private}d, \"urgency\":%{private}d, \"severity\":%{private}d, \"certainty\":%{private}d, \"infoEntriesCount\":%{private}d, \"cacheTTLSeconds\":%{private}d, \"hasGeometry\":%{private}hhd, \"isLastAlert\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#gsadisp,post,not last alert or WEA already received, setting silent\", \"isLastAlert\":%{private}hhd, \"isWeaReceived\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,isFollowUpReceivedAlready false\"}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,isFollowUpReceivedAlready for action\"}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,isFollowUpReceivedAlready for awareness\"}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,isFollowUpReceivedAlready\"}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,isIgneousReceivedAlready\", \"newUID\":%{private, location:escape_only}s, \"isActionAlertReceivedPreviously\":%{private}hhd, \"isAwarenessAlertReceivedPreviously\":%{private}hhd, \"isCurrentAlertIsAwareness\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,isIgneousReceivedAlready\", \"newUID\":%{private, location:escape_only}s, \"isActionAlertReceivedPreviously\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,isIgneousReceivedAlready,dup alert awareness already received with bleUid\"}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,isIgneousReceivedAlready,dup alert, action alert already received with bleUid\"}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,onAPNSReceived,done\", \"uidHash\":%{private, location:escape_only}s, \"timestamp\":\"%{private}0.1f\", \"metaValueStr\":%{private, location:escape_only}s, \"newUID\":%{private, location:escape_only}s, \"mmiBandConfig.level\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#igEventTracker,onBleReceived,done\", \"bleUID\":%{private, location:escape_only}s, \"Level\":%{private}d, \"bleUID\":%{private, location:escape_only}s, \"timestamp\":\"%{private}0.1f\"}"
+ "{\"msg%{public}.0s\":\"#igv,validateIntensity out of bound location\", \"result\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#igv,validateIntensity\", \"result\":%{private}hhd, \"isDistInActionRange\":%{private}hhd, \"isDistInAwarenessRange\":%{private}hhd, \"isActionBCMatched\":%{private}hhd, \"isAwarenessBCMatched\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#igv,validateIntensity,Mag not found\"}"
+ "{\"msg%{public}.0s\":\"#igv,validateIntensity,mmiBand\", \"igneousAlertInformation.magnitude\":\"%{private}.1f\", \"distanceToEpicenter\":\"%{private}.1f\", \"igneousAlertInformation.strongShakeRadius\":\"%{private}.1f\", \"igneousAlertInformation.effectiveDistance\":\"%{private}.1f\"}"
+ "{\"msg%{public}.0s\":\"#igv,validateIntensity,mmiBand\", \"minMagnitude\":\"%{private}.1f\", \"maxMagnitude\":\"%{private}.1f\", \"minIntensity\":\"%{private}.1f\", \"maxIntensity\":\"%{private}.1f\", \"mmiBand.level\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#notif,notificationIdentifier\", \"identifier\":%{public, location:escape_only}@, \"uid\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#notif,postGeneralAlertRichNotification,sound_control\", \"shouldBeSilent\":%{private}hhd, \"isSilentFromDisplay\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onMotionHarvestPref\", \"earthquake switch state\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onMotionHarvestPref,earthquake switch not visible\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onMotionHarvestPref,not phone\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,updateMotionHarvestStatus\", \"improveSafety\":%{private}hhd, \"motionHarvestPref\":%{private}hhd, \"motionHarvestOnlyInCountry\":%{private}hhd, \"motionHarvestAvailable\":%{private}hhd, \"motionHarvestAllowed\":%{private}hhd}"
- "%s.notif_%d"
- "@80@0:8@16r*24Q32Q40r*48r*56{shared_ptr<SACoreAnalytics>=^{SACoreAnalytics}^{__shared_weak_count}}64"
- "initWithQueue:bundleIdentifier:authorizationOption:interruptionLevel:extension:categoryName:analyticsRef:"
- "{\"msg%{public}.0s\":\"#channel,forwarding_last_alert\", \"last_alert_index\":%{private}d, \"total_alerts_skipped\":%{private}d, \"alert_keys_count\":%{private}d}"
- "{\"msg%{public}.0s\":\"#channel,last_alert_not_dict\", \"last_alert_index\":%{private}d, \"alert_class\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#chsel,isSARegistrationAllowed,state\", \"isSaRegisterPreCheckPass\":%{public}hhd, \"isInCountry\":%{public}hhd, \"requiresTelephony\":%{public}hhd, \"isTelephonySupported\":%{public}hhd, \"isParticipating\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,forwarding to GeneralSafetyAlertDisplay\"}"
- "{\"msg%{public}.0s\":\"#daemon,updateMotionHarvestStatus\", \"improveSafety\":%{private}hhd, \"motionHarvestPref\":%{private}hhd, \"motionHarvestOnlyInCountry\":%{private}hhd, \"motionHarvestAvailable\":%{private}hhd, \"motionHarvestAllowed\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#gap,parse,success\", \"uid\":%{private, location:escape_only}s, \"sessionId\":%{private, location:escape_only}s, \"status\":%{private}d, \"msgType\":%{private}d, \"urgency\":%{private}d, \"severity\":%{private}d, \"certainty\":%{private}d, \"infoEntriesCount\":%{private}d, \"cacheTTLSeconds\":%{private}d, \"hasGeometry\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#igEventTracker,onAPNSReceived,done\", \"uidHash\":%{private, location:escape_only}s, \"timestamp\":\"%{private}0.1f\", \"metaValueStr\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#igEventTracker,onBleReceived,done\", \"bleUID\":%{private, location:escape_only}s, \"timestamp\":\"%{private}0.1f\"}"
- "{\"msg%{public}.0s\":\"#ignalert,getNotificationContentInternal,mmiBandNotFound\"}"
- "{\"msg%{public}.0s\":\"#igv,validateIntensity\", \"result\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#igv,validateIntensity,mmiBand\", \"minMagnitude\":\"%{private}.1f\", \"maxMagnitude\":\"%{private}.1f\", \"minIntensity\":\"%{private}.1f\", \"maxIntensity\":\"%{private}.1f\"}"
- "{\"msg%{public}.0s\":\"#igv,validateIntensity,source Not found\", \"senderId\":%{private}d}"

```
