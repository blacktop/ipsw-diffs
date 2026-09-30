## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-950.2.0.0.0
-  __TEXT.__text: 0xb4b08
-  __TEXT.__auth_stubs: 0x15c0
-  __TEXT.__objc_methlist: 0xffc8
-  __TEXT.__const: 0x648
-  __TEXT.__cstring: 0x1b4d4
-  __TEXT.__oslogstring: 0x39e8
-  __TEXT.__gcc_except_tab: 0x18e8
+980.33.0.0.0
+  __TEXT.__text: 0xb8564
+  __TEXT.__auth_stubs: 0x15f0
+  __TEXT.__objc_methlist: 0x10fa0
+  __TEXT.__const: 0x638
+  __TEXT.__cstring: 0x1bc9f
+  __TEXT.__oslogstring: 0x3a15
+  __TEXT.__gcc_except_tab: 0x1904
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x20d8
-  __TEXT.__objc_classname: 0x135b
-  __TEXT.__objc_methname: 0x306dc
-  __TEXT.__objc_methtype: 0x39f2
-  __TEXT.__objc_stubs: 0x17500
-  __DATA_CONST.__got: 0xa58
-  __DATA_CONST.__const: 0x2170
-  __DATA_CONST.__objc_classlist: 0x508
+  __TEXT.__unwind_info: 0x21a8
+  __TEXT.__objc_classname: 0x1379
+  __TEXT.__objc_methname: 0x31518
+  __TEXT.__objc_methtype: 0x3a1a
+  __TEXT.__objc_stubs: 0x17e80
+  __DATA_CONST.__got: 0xa40
+  __DATA_CONST.__const: 0x21d8
+  __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9170
+  __DATA_CONST.__objc_selrefs: 0x9690
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x428
+  __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0xa58
-  __AUTH_CONST.__auth_got: 0xaf8
+  __AUTH_CONST.__auth_got: 0xb10
+  __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x17e60
-  __AUTH_CONST.__objc_const: 0x21650
-  __AUTH_CONST.__objc_intobj: 0x16e0
+  __AUTH_CONST.__cfstring: 0x185c0
+  __AUTH_CONST.__objc_const: 0x20868
+  __AUTH_CONST.__objc_intobj: 0x1740
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0x1fa8
+  __AUTH.__objc_data: 0x820
+  __DATA.__objc_ivar: 0x2060
   __DATA.__data: 0x1bc0
   __DATA.__bss: 0x22
   __DATA_DIRTY.__objc_data: 0x2a80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5816
-  Symbols:   6788
-  CStrings:  12935
+  Functions: 5987
+  Symbols:   6991
+  CStrings:  13149
 
Symbols:
+ _Apple80211ReturnToString
+ _CNCRC
+ _OBJC_CLASS_$_WADeviceAnalyticsClient
+ _OBJC_CLASS_$_WiFiUsageWatchdogDetails
+ _OBJC_METACLASS_$_WiFiUsageWatchdogDetails
+ _convertLinkChangeReasonToString
- _OBJC_CLASS_$_AnalyticsProcessor
CStrings:
+ "\x03\xd1\x13\x12#EQ"
+ "\ncolocatedMLD_2G:%@ colocatedMLD_5G:%@ colocatedMLD_6G:%@"
+ "#\x12"
+ "%lu(%@/%lu)"
+ "%s HighImpactTime %lu (afterFirstTDConfirmed: %lu)"
+ "%s LowModHighImpactTime %lu (afterFirstTDConfirmed: %lu)"
+ "%s ModHighImpactTime %lu (afterFirstTDConfirmed: %lu)"
+ "%s RTAppAtSessionEnd %d (atFirstTDConfirmed: %d) , FGAppAtSessionEnd %d (atFirstTDConfirmed: %d)"
+ "%s Session (started: %@, ended: %@)"
+ "%s TDAlerted due to BadRssi"
+ "%s TotalSessionTime %lu (afterFirstTDConfirmed: %lu)"
+ "%s: (GoodRssiTimer expired) calling sessionDidEnd:%@"
+ "%s: (LinkDownNotTDTimer expired) calling sessionDidEnd:%@"
+ "%s: (TDTimer expired) calling sessionDidEnd:%@"
+ "%s: (Timer expired) w/ no reason"
+ "%s: BadLink session started due to highCCA for 2.4G "
+ "%s: BadLink session will end due to rssi (%lddBm) crossing GoodLink Threshold (%@dBm) or tdRecommended(%@) %d sec GoodRssiTimer up"
+ "%s: Element %u_%u is invalid:%@"
+ "%s: Link changed while in GoodRssi Timer active session ended"
+ "%s: Sending linkTest to DeviceStore: %@"
+ "%s: Session will end due to goodRssi %d sec timer is up"
+ "%s: _toBeClosedAfterLQM: YES, should not happen %@"
+ "%s: null interface name"
+ "%s: start timer (%@) wait up to %lu secs"
+ "%s:%d available:%d interface:%@ flags:0x%x reason:%@(0x%x) subreason:0x%x"
+ "-[WiFiUsageParsedBeacon parseSSID:length:endOfBuffer:]"
+ "-[WiFiUsagePoorLinkSession initializeTimer]_block_invoke"
+ "-[WiFiUsagePoorLinkSession startTimerWithTimeout:reason:]"
+ "-[WiFiUsageSession processDriverAvailability:available:version:flags:eventID:reason:subReason:minorReason:reasonString:]"
+ "-[WiFiUsageWatchdogDetails initWithInterfaceName:andConnectedBss:]"
+ "@\"WiFiUsageAccessPointProfile\""
+ "B40@0:8q16q24@32"
+ "B;\x1d\x14/\x03\x11"
+ "Driver Booted"
+ "FGAppAtFirstTDConfirmed"
+ "FGAppAtSessionEnd"
+ "FaultReasonMTBFEventCount"
+ "GoodRSSITimer"
+ "GoodRssiThenBadSession"
+ "GoodRssiThenLinkChange"
+ "HND"
+ "HighCca2Ghz"
+ "HighImpactTime"
+ "HighImpactTimeAfterFirstTDConfirmed"
+ "HotspotConnectionInactive"
+ "LinkDownNotTDThenLinkUp"
+ "LinkDownNotTDTimer"
+ "LinkDownTDTimer"
+ "Locale from authorized client: <%@>"
+ "LowModHighImpactTime"
+ "LowModHighImpactTimeAfterFirstTDConfirmed"
+ "ModHighImpactTime"
+ "ModHighImpactTimeAfterFirstTDConfirmed"
+ "NetworkCarrierPayloadIdentifier"
+ "NetworkCarrierPayloadIdentifierIsAllowed"
+ "NoTimer"
+ "RTAppAtFirstTDConfirmed"
+ "RTAppAtSessionEnd"
+ "T@\"NSDate\",&,N,V_createdAt"
+ "T@\"NSDate\",C,N,V_settledDate"
+ "T@\"NSMutableArray\",&,N,V_pendingWatchdogs"
+ "T@\"NSString\",&,N,V_availableReasonString"
+ "T@\"NSString\",&,N,V_unavailableReasonString"
+ "T@\"NSString\",N,V_carrierPayloadIdentifier"
+ "T@\"WiFiUsageAccessPointProfile\",&,V_lastApProfile"
+ "T@\"WiFiUsageBssDetails\",&,N,V_connectedBss"
+ "TB,N,V_fgAppAtFirstTDConfirmed"
+ "TB,N,V_fgAppAtSessionEnd"
+ "TB,N,V_hasColocatedMLOs"
+ "TB,N,V_isCarrierPayloadIdentifierTelemetryApproved"
+ "TB,N,V_rtAppAtFirstTDConfirmed"
+ "TB,N,V_rtAppAtSessionEnd"
+ "TC,N,V_ap6gPowerMode"
+ "TI,N,V_shortSSID"
+ "TQ,N,V_highImpactTime"
+ "TQ,N,V_highImpactTimeAfterFirstTDConfirmed"
+ "TQ,N,V_lastWiFiSARState"
+ "TQ,N,V_lowModHighImpactTime"
+ "TQ,N,V_lowModHighImpactTimeAfterFirstTDConfirmed"
+ "TQ,N,V_modHighImpactTime"
+ "TQ,N,V_modHighImpactTimeAfterFirstTDConfirmed"
+ "TQ,N,V_totalSessionTime"
+ "TQ,N,V_totalSessionTimeAfterFirstTDConfirmed"
+ "Ti,N,V_availableReason"
+ "Ti,N,V_availableSubreason"
+ "Ti,N,V_unavailableReason"
+ "Ti,N,V_unavailableSubreason"
+ "Ti,R,N,V_currentBand"
+ "TotalSessionTime"
+ "TotalSessionTimeAfterFirstTDConfirmed"
+ "Unknown=0x%x:0x%x"
+ "WiFiUsageWatchdogDetails"
+ "WiFiUsageWatchdogDetailsSubmitToCA"
+ "[1035Q]"
+ "[35Q]"
+ "_ap6gPowerMode"
+ "_availableReason"
+ "_availableReasonString"
+ "_availableSubreason"
+ "_bcnPerThresholdForPerCoreUse"
+ "_carrierPayloadIdentifier"
+ "_ccaThresholdFor2GHz"
+ "_createdAt"
+ "_fgAppAtFirstTDConfirmed"
+ "_fgAppAtSessionEnd"
+ "_firstLQMForSessionReceived"
+ "_hasColocatedMLOs"
+ "_highImpactTime"
+ "_highImpactTimeAfterFirstTDConfirmed"
+ "_isCarrierPayloadIdentifierTelemetryApproved"
+ "_isFirstTDConfirmed"
+ "_lastApProfile"
+ "_lastIsAnyAppinFG"
+ "_lastIsTimeSensitiveAppRunning"
+ "_lastWiFiSARState"
+ "_lowModHighImpactTime"
+ "_lowModHighImpactTimeAfterFirstTDConfirmed"
+ "_maxPerCoreRssiHist"
+ "_modHighImpactTime"
+ "_modHighImpactTimeAfterFirstTDConfirmed"
+ "_pendingWatchdogs"
+ "_rssiCore0Array"
+ "_rssiCore1Array"
+ "_rssiThresholdFor2GHz"
+ "_rssiThresholdForPerCoreUse"
+ "_rtAppAtFirstTDConfirmed"
+ "_rtAppAtSessionEnd"
+ "_shortSSID"
+ "_timerActive"
+ "_timerReason"
+ "_totalSessionTime"
+ "_totalSessionTimeAfterFirstTDConfirmed"
+ "_txPerThresholdHigh"
+ "_txPerThresholdLow"
+ "_txPerThresholdModerate"
+ "_unavailableReason"
+ "_unavailableReasonString"
+ "_unavailableSubreason"
+ "ap6gPowerMode"
+ "appendSARStatsToDict:"
+ "associated"
+ "associationState"
+ "availableReason"
+ "availableReasonString"
+ "availableSubreason"
+ "avgValidRssiInArray:"
+ "carrierPayloadIdentifier"
+ "checkGoodRssiThenBadSession"
+ "com.apple.wifi.WatchdogEvent"
+ "createdAt"
+ "disassociated"
+ "fgAppAtFirstTDConfirmed"
+ "fgAppAtSessionEnd"
+ "foregroundActivity"
+ "getLocaleFromRemoteClient"
+ "getRemoteClientCountryCode"
+ "highImpactTime"
+ "highImpactTimeAfterFirstTDConfirmed"
+ "initWithCString:"
+ "initWithInterfaceName:andConnectedBss:"
+ "initializeTimer"
+ "isCarrierPayloadIdentifierTelemetryApproved"
+ "isDriverAvailabilityNonFatal"
+ "isDriverUnavailabilityReasonVoluntary:subReason:orReasonString:"
+ "isHighCcaFor2Ghz:"
+ "kWiFiUsageFaultReasonMTBFEvent"
+ "lastApProfile"
+ "lastWiFiSARState"
+ "lowModHighImpactTime"
+ "lowModHighImpactTimeAfterFirstTDConfirmed"
+ "modHighImpactTime"
+ "modHighImpactTimeAfterFirstTDConfirmed"
+ "parseSSID:length:endOfBuffer:"
+ "pendingWatchdogs"
+ "reasonString"
+ "recoveryLatency"
+ "releaseBackgroundProcessingMOC"
+ "reportedReason"
+ "reportedReasonString"
+ "reportedSubreason"
+ "reportedSubreasonString"
+ "rtAppAtFirstTDConfirmed"
+ "rtAppAtSessionEnd"
+ "setAp6gPowerMode:"
+ "setAvailableReason:"
+ "setAvailableReasonString:"
+ "setAvailableSubreason:"
+ "setCarrierPayloadIdentifier:"
+ "setCreatedAt:"
+ "setFgAppAtFirstTDConfirmed:"
+ "setFgAppAtSessionEnd:"
+ "setHasColocatedMLOs:"
+ "setHighImpactTime:"
+ "setHighImpactTimeAfterFirstTDConfirmed:"
+ "setIsCarrierPayloadIdentifierTelemetryApproved:"
+ "setLastApProfile:"
+ "setLastWiFiSARState:"
+ "setLowModHighImpactTime:"
+ "setLowModHighImpactTimeAfterFirstTDConfirmed:"
+ "setModHighImpactTime:"
+ "setModHighImpactTimeAfterFirstTDConfirmed:"
+ "setPendingWatchdogs:"
+ "setRtAppAtFirstTDConfirmed:"
+ "setRtAppAtSessionEnd:"
+ "setSARState:builtInReceiverOn:"
+ "setShortSSID:"
+ "setTotalSessionTime:"
+ "setTotalSessionTimeAfterFirstTDConfirmed:"
+ "setUnavailableReason:"
+ "setUnavailableReasonString:"
+ "setUnavailableSubreason:"
+ "sharedDeviceAnalyticsClient"
+ "shortSSID"
+ "shouldFilterSession:"
+ "startTimerWithTimeout:reason:"
+ "stopTimer"
+ "stringWithCString:"
+ "subreason"
+ "subreasonString"
+ "suspendTimer"
+ "timeBetweenFailure"
+ "timerReason:"
+ "totalSessionTime"
+ "totalSessionTimeAfterFirstTDConfirmed"
+ "unavailableReason"
+ "unavailableReasonString"
+ "unavailableSubreason"
+ "v28@0:8Q16i24"
+ "v32@?0@\"NSNumber\"8Q16^B24"
+ "v84@0:8@16B24Q28Q36Q44q52q60q68@76"
+ "wifiSARState"
+ "wpsManufacturerElement"
+ "wpsModelName"
+ "wpsModelNumber"
+ "\x84\x15"
+ "\x912\x113"
+ "\xf0\xf0\xd1\x11:\xf0\xf01\x81\xb9"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0!\x93\x11$\x11\x8f\x0f\x03\xf0\xf0\xf0\x91s\xf0\xf0\xf0\x91\xb2t\xb2S'\x11\x11\x91\xf0\xa1\x11\xf0\xb4"
- "\x03Q\x11\x15EQ"
- "%s (%@): %@"
- "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"
- "%s on %@ - Unexpected ifDown due to %@ while session is inactive"
- "%s: BadLink session ended due to linkUp"
- "%s: BadLink session ended due to rssi (%lddBm) crossing GoodLink Threshold (%@dBm) or tdRecommended(%@)"
- "%s: BadLink session will end due to linkUp (waiting on LQM update)"
- "%s: Link went down due to %@, ending session"
- "%s: Link went down, waiting on linkUp for up to %ds"
- "-[WiFiUsageParsedBeacon parseNormalIE:from:length:endOfBuffer:]"
- "2\x12"
- "@\"AnalyticsProcessor\""
- "B;\x1d\x15/\x03"
- "HND_AnalyticsProcessor"
- "T@\"AnalyticsProcessor\",&,V_analyticsProcessor"
- "T@\"NSDate\",N,V_settledDate"
- "[1034Q]"
- "[34Q]"
- "_analyticsProcessor"
- "_waitingOnLinkUp"
- "analyticsProcessor"
- "setAnalyticsProcessor:"
- "sharedAnalyticsProcessor"
- "t\x14"
- "v88@0:8@16Q24Q32Q40Q48Q56Q64Q72@80"
- "\x812\x113"
- "\xf0\xf0\xc1\x11:\xf0\xf01\x81\xb9"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf1\x93\x11#\x11\x8f\x0f\x03\xf0\xf0\xf0\x91s\xf0\xf0\xf0\x91\xb2t\xb2S'\x11\x11\x91\xf0\xa1\x11\xf0\xb4"

```
