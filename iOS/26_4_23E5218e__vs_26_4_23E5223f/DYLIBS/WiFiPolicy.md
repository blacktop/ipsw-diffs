## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-1041.24.0.0.0
-  __TEXT.__text: 0xd584c
+1041.25.0.0.0
+  __TEXT.__text: 0xd7be4
   __TEXT.__auth_stubs: 0x1730
-  __TEXT.__objc_methlist: 0x12190
+  __TEXT.__objc_methlist: 0x12450
   __TEXT.__const: 0x6e8
-  __TEXT.__cstring: 0x1fe2e
+  __TEXT.__cstring: 0x2028d
   __TEXT.__oslogstring: 0x4862
   __TEXT.__gcc_except_tab: 0x1920
   __TEXT.__dlopen_cstrs: 0xf3
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0x2f50
-  __TEXT.__objc_classname: 0x149e
-  __TEXT.__objc_methname: 0x3466a
+  __TEXT.__unwind_info: 0x2fd0
+  __TEXT.__objc_classname: 0x14ba
+  __TEXT.__objc_methname: 0x34e6c
   __TEXT.__objc_methtype: 0x3f90
-  __TEXT.__objc_stubs: 0x19e20
-  __DATA_CONST.__got: 0xaa8
-  __DATA_CONST.__const: 0x23c8
-  __DATA_CONST.__objc_classlist: 0x568
+  __TEXT.__objc_stubs: 0x1a200
+  __DATA_CONST.__got: 0xab0
+  __DATA_CONST.__const: 0x23d0
+  __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa018
+  __DATA_CONST.__objc_selrefs: 0xa198
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x480
+  __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0xb50
   __AUTH_CONST.__auth_got: 0xbb0
   __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x1ac80
-  __AUTH_CONST.__objc_const: 0x229d0
-  __AUTH_CONST.__objc_intobj: 0x19e0
+  __AUTH_CONST.__cfstring: 0x1b260
+  __AUTH_CONST.__objc_const: 0x22e00
+  __AUTH_CONST.__objc_intobj: 0x19f8
   __AUTH_CONST.__objc_arrayobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x7a8
-  __DATA.__objc_ivar: 0x2264
+  __AUTH.__objc_data: 0x7f8
+  __DATA.__objc_ivar: 0x22b0
   __DATA.__data: 0x1c20
   __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x2e68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9EF7C9FB-559B-3472-85C6-1FA4BAA80082
-  Functions: 6501
-  Symbols:   21229
-  CStrings:  17517
+  UUID: 219826C7-29AC-307C-8725-6AE67E9721E4
+  Functions: 6559
+  Symbols:   21402
+  CStrings:  17701
 
Symbols:
+ -[WiFiUsageRoamingSession .cxx_destruct]
+ -[WiFiUsageRoamingSession bandsInDeployment]
+ -[WiFiUsageRoamingSession calculatePercentage:denominator:]
+ -[WiFiUsageRoamingSession copyWithZone:]
+ -[WiFiUsageRoamingSession eventDictionary:]
+ -[WiFiUsageRoamingSession faultEventDetected:event:]
+ -[WiFiUsageRoamingSession getMostCommonMotionStatus]
+ -[WiFiUsageRoamingSession getMostCommonRoamProfile]
+ -[WiFiUsageRoamingSession getMostCommonRoamReason]
+ -[WiFiUsageRoamingSession getUsedRoamProfilesBitmask]
+ -[WiFiUsageRoamingSession inWiFi1BarDuration]
+ -[WiFiUsageRoamingSession inWiFi1BarEntryTime]
+ -[WiFiUsageRoamingSession inWiFi2BarDuration]
+ -[WiFiUsageRoamingSession inWiFi2BarEntryTime]
+ -[WiFiUsageRoamingSession inWiFi3BarDuration]
+ -[WiFiUsageRoamingSession inWiFi3BarEntryTime]
+ -[WiFiUsageRoamingSession inWiFiPrimaryDuration]
+ -[WiFiUsageRoamingSession inWiFiPrimaryEntryTime]
+ -[WiFiUsageRoamingSession initWithInterfaceName:andCapabilities:]
+ -[WiFiUsageRoamingSession interfaceRankingDidChange:]
+ -[WiFiUsageRoamingSession lastRoamStartTime]
+ -[WiFiUsageRoamingSession lastSuccessfulRoamTime]
+ -[WiFiUsageRoamingSession linkQualityDidChange:]
+ -[WiFiUsageRoamingSession linkStateDidChange:isInvoluntary:linkChangeReason:linkChangeSubreason:withNetworkDetails:]
+ -[WiFiUsageRoamingSession metricName]
+ -[WiFiUsageRoamingSession numChannelsScanned]
+ -[WiFiUsageRoamingSession numRoamsNoARP]
+ -[WiFiUsageRoamingSession numRoamsToLowerRSSI]
+ -[WiFiUsageRoamingSession numRoamsWithWiFiPrimary]
+ -[WiFiUsageRoamingSession numVeryLowRssiAttempts]
+ -[WiFiUsageRoamingSession populateBandsInDeployment]
+ -[WiFiUsageRoamingSession roamProfileCounts]
+ -[WiFiUsageRoamingSession roamScanDurationInMs]
+ -[WiFiUsageRoamingSession roamingStateDidChange:reason:andStatus:andLatency:andRoamData:andPingPongStats:]
+ -[WiFiUsageRoamingSession sessionDidEnd]
+ -[WiFiUsageRoamingSession sessionDidStart]
+ -[WiFiUsageRoamingSession setBandsInDeployment:]
+ -[WiFiUsageRoamingSession setInWiFi1BarDuration:]
+ -[WiFiUsageRoamingSession setInWiFi1BarEntryTime:]
+ -[WiFiUsageRoamingSession setInWiFi2BarDuration:]
+ -[WiFiUsageRoamingSession setInWiFi2BarEntryTime:]
+ -[WiFiUsageRoamingSession setInWiFi3BarDuration:]
+ -[WiFiUsageRoamingSession setInWiFi3BarEntryTime:]
+ -[WiFiUsageRoamingSession setInWiFiPrimaryDuration:]
+ -[WiFiUsageRoamingSession setInWiFiPrimaryEntryTime:]
+ -[WiFiUsageRoamingSession setLastRoamStartTime:]
+ -[WiFiUsageRoamingSession setLastSuccessfulRoamTime:]
+ -[WiFiUsageRoamingSession setNumChannelsScanned:]
+ -[WiFiUsageRoamingSession setNumRoamsNoARP:]
+ -[WiFiUsageRoamingSession setNumRoamsToLowerRSSI:]
+ -[WiFiUsageRoamingSession setNumRoamsWithWiFiPrimary:]
+ -[WiFiUsageRoamingSession setNumVeryLowRssiAttempts:]
+ -[WiFiUsageRoamingSession setRoamProfileCounts:]
+ -[WiFiUsageRoamingSession setRoamScanDurationInMs:]
+ -[WiFiUsageRoamingSession summarizeSession]
+ -[WiFiUsageRoamingSession systemWakeStateDidChange:wokenByWiFi:]
+ -[WiFiUsageSession roamReasonDeauthCount]
+ -[WiFiUsageSession setRoamReasonDeauthCount:]
+ _OBJC_CLASS_$_WiFiUsageRoamingSession
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._bandsInDeployment
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._inWiFi1BarDuration
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._inWiFi1BarEntryTime
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._inWiFi2BarDuration
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._inWiFi2BarEntryTime
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._inWiFi3BarDuration
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._inWiFi3BarEntryTime
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._inWiFiPrimaryDuration
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._inWiFiPrimaryEntryTime
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._lastRoamStartTime
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._lastSuccessfulRoamTime
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._numChannelsScanned
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._numRoamsNoARP
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._numRoamsToLowerRSSI
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._numRoamsWithWiFiPrimary
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._numVeryLowRssiAttempts
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._roamProfileCounts
+ _OBJC_IVAR_$_WiFiUsageRoamingSession._roamScanDurationInMs
+ _OBJC_IVAR_$_WiFiUsageSession._roamReasonDeauthCount
+ _OBJC_METACLASS_$_WiFiUsageRoamingSession
+ __OBJC_$_INSTANCE_METHODS_WiFiUsageRoamingSession
+ __OBJC_$_INSTANCE_VARIABLES_WiFiUsageRoamingSession
+ __OBJC_$_PROP_LIST_WiFiUsageRoamingSession
+ __OBJC_CLASS_RO_$_WiFiUsageRoamingSession
+ __OBJC_METACLASS_RO_$_WiFiUsageRoamingSession
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9nqe210106Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9nqe210106Ej
+ __ZNSt3__116__pad_and_outputB9nqe210106IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIN6gloria6TileIdEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106Ev
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__124__put_character_sequenceB9nqe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__127__tree_balance_after_insertB9nqe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16vectorIN6gloria6TileIdENS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
+ ___36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.784
+ ___69-[WiFiUsageMonitor startMonitoringWiFiInterface:withLinkSessionOnly:]_block_invoke.320
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.844
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.852
+ ___block_literal_global.847
+ ___block_literal_global.857
+ ___block_literal_global.859
+ _apple80211_roam_profile_typetoStr
+ _objc_msgSend$bandsInNetwork:withError:
+ _objc_msgSend$calculatePercentage:denominator:
+ _objc_msgSend$getMostCommonMotionStatus
+ _objc_msgSend$getMostCommonRoamProfile
+ _objc_msgSend$getMostCommonRoamReason
+ _objc_msgSend$getUsedRoamProfilesBitmask
+ _objc_msgSend$has2GHz
+ _objc_msgSend$has5GHz
+ _objc_msgSend$has6GHz
+ _objc_msgSend$inMotionDuration
+ _objc_msgSend$inRoamEventCount
+ _objc_msgSend$inVehicleDuration
+ _objc_msgSend$inWalkingDuration
+ _objc_msgSend$lastInterfacePrimaryState
+ _objc_msgSend$populateBandsInDeployment
+ _objc_msgSend$roamReasonBeaconLostCount
+ _objc_msgSend$roamReasonBetterCandidateCount
+ _objc_msgSend$roamReasonDeauthCount
+ _objc_msgSend$roamReasonDeauthDisassocCount
+ _objc_msgSend$roamReasonHostTriggeredCount
+ _objc_msgSend$roamReasonInitialAssociationCount
+ _objc_msgSend$roamReasonLowRssiCount
+ _objc_msgSend$roamReasonReassocRequestedCount
+ _objc_msgSend$roamReasonSteeredByBtmCount
+ _objc_msgSend$roamReasonSteeredByCsaCount
+ _objc_msgSend$roamStatusSucceededCount
+ _objc_msgSend$setInWiFi1BarEntryTime:
+ _objc_msgSend$setInWiFi2BarEntryTime:
+ _objc_msgSend$setInWiFi3BarEntryTime:
+ _objc_msgSend$setInWiFiPrimaryEntryTime:
+ _objc_msgSend$setRoamReasonDeauthCount:
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9foe210106Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9foe210106Ej
- __ZNSt3__116__pad_and_outputB9foe210106IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIN6gloria6TileIdEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106Ev
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__124__put_character_sequenceB9foe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__127__tree_balance_after_insertB9foe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIN6gloria6TileIdENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
- ___36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.783
- ___69-[WiFiUsageMonitor startMonitoringWiFiInterface:withLinkSessionOnly:]_block_invoke.319
- ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.840
- ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.848
- ___block_literal_global.843
- ___block_literal_global.851
- ___block_literal_global.853
CStrings:
+ "%s: WiFiUsageRoamingSession: Ending session due to 60s roaming inactivity"
+ "%s: WiFiUsageRoamingSession: Ending session due to link down"
+ "%s: WiFiUsageRoamingSession: Ending session due to system sleep"
+ "%s: WiFiUsageRoamingSession: Starting roam session"
+ "-[WiFiUsageRoamingSession linkQualityDidChange:]"
+ "-[WiFiUsageRoamingSession linkStateDidChange:isInvoluntary:linkChangeReason:linkChangeSubreason:withNetworkDetails:]"
+ "-[WiFiUsageRoamingSession roamingStateDidChange:reason:andStatus:andLatency:andRoamData:andPingPongStats:]"
+ "-[WiFiUsageRoamingSession systemWakeStateDidChange:wokenByWiFi:]"
+ "BTM"
+ "BeaconsLost"
+ "CSA"
+ "DeauthIndication"
+ "DisassocIndication"
+ "FoundBetterAP"
+ "HostTriggered"
+ "InOtherMotion"
+ "InitialAssociation"
+ "LowRSSI"
+ "ROAMEDEVENT_PROFILE_TYPE"
+ "ROAMEDEVENT_TIME_ENDED"
+ "ROAMEDEVENT_TIME_STARTED"
+ "Reassoc"
+ "T@\"NSDate\",&,N,V_inWiFi1BarEntryTime"
+ "T@\"NSDate\",&,N,V_inWiFi2BarEntryTime"
+ "T@\"NSDate\",&,N,V_inWiFi3BarEntryTime"
+ "T@\"NSDate\",&,N,V_inWiFiPrimaryEntryTime"
+ "T@\"NSDate\",&,N,V_lastRoamStartTime"
+ "T@\"NSDate\",&,N,V_lastSuccessfulRoamTime"
+ "T@\"NSMutableDictionary\",&,N,V_roamProfileCounts"
+ "TQ,N,V_bandsInDeployment"
+ "TQ,N,V_numChannelsScanned"
+ "TQ,N,V_numRoamsNoARP"
+ "TQ,N,V_numRoamsToLowerRSSI"
+ "TQ,N,V_numRoamsWithWiFiPrimary"
+ "TQ,N,V_numVeryLowRssiAttempts"
+ "TQ,N,V_roamReasonDeauthCount"
+ "TQ,N,V_roamScanDurationInMs"
+ "Td,N,V_inWiFi1BarDuration"
+ "Td,N,V_inWiFi2BarDuration"
+ "Td,N,V_inWiFi3BarDuration"
+ "Td,N,V_inWiFiPrimaryDuration"
+ "WiFi1barDuration"
+ "WiFi2barsDuration"
+ "WiFi3barsDuration"
+ "WiFiPrimaryDuration"
+ "WiFiUsageRoamingSession"
+ "[1041Q]"
+ "_bandsInDeployment"
+ "_inWiFi1BarDuration"
+ "_inWiFi1BarEntryTime"
+ "_inWiFi2BarDuration"
+ "_inWiFi2BarEntryTime"
+ "_inWiFi3BarDuration"
+ "_inWiFi3BarEntryTime"
+ "_inWiFiPrimaryDuration"
+ "_inWiFiPrimaryEntryTime"
+ "_lastRoamStartTime"
+ "_lastSuccessfulRoamTime"
+ "_numChannelsScanned"
+ "_numRoamsNoARP"
+ "_numRoamsToLowerRSSI"
+ "_numRoamsWithWiFiPrimary"
+ "_numVeryLowRssiAttempts"
+ "_roamProfileCounts"
+ "_roamReasonDeauthCount"
+ "_roamScanDurationInMs"
+ "bandsInDeployment"
+ "bandsInNetwork:withError:"
+ "calculatePercentage:denominator:"
+ "channelScanRate"
+ "com.apple.wifi.roamsession"
+ "getMostCommonMotionStatus"
+ "getMostCommonRoamProfile"
+ "getMostCommonRoamReason"
+ "getUsedRoamProfilesBitmask"
+ "has2GHz"
+ "has5GHz"
+ "has6GHz"
+ "inRoamSession"
+ "inWiFi1BarDuration"
+ "inWiFi1BarEntryTime"
+ "inWiFi2BarDuration"
+ "inWiFi2BarEntryTime"
+ "inWiFi3BarDuration"
+ "inWiFi3BarEntryTime"
+ "inWiFiPrimaryDuration"
+ "inWiFiPrimaryEntryTime"
+ "lastRoamStartTime"
+ "lastSuccessfulRoamTime"
+ "mostCommonMotionStatus"
+ "mostCommonRoamReason"
+ "mostUsedRoamProfile"
+ "numChannelsScanned"
+ "numRoamsNoARP"
+ "numRoamsToLowerRSSI"
+ "numRoamsWithWiFiPrimary"
+ "numVeryLowRssiAttempts"
+ "populateBandsInDeployment"
+ "roamProfileCounts"
+ "roamReasonAssocPercentage"
+ "roamReasonBTMPercentage"
+ "roamReasonBeaconsLostPercentage"
+ "roamReasonCSAPercentage"
+ "roamReasonDeauthCount"
+ "roamReasonDeauthPercentage"
+ "roamReasonDisassocPercentage"
+ "roamReasonFoundBetterAPPercentage"
+ "roamReasonHostPercentage"
+ "roamReasonLowRSSIPercentage"
+ "roamReasonReassocPercentage"
+ "roamScanDurationInMs"
+ "roamWiFiPrimary"
+ "roamingProfilesCount"
+ "roamingRate"
+ "roamsNoARP"
+ "roamsToLowerRSSI"
+ "setBandsInDeployment:"
+ "setInWiFi1BarDuration:"
+ "setInWiFi1BarEntryTime:"
+ "setInWiFi2BarDuration:"
+ "setInWiFi2BarEntryTime:"
+ "setInWiFi3BarDuration:"
+ "setInWiFi3BarEntryTime:"
+ "setInWiFiPrimaryDuration:"
+ "setInWiFiPrimaryEntryTime:"
+ "setLastRoamStartTime:"
+ "setLastSuccessfulRoamTime:"
+ "setNumChannelsScanned:"
+ "setNumRoamsNoARP:"
+ "setNumRoamsToLowerRSSI:"
+ "setNumRoamsWithWiFiPrimary:"
+ "setNumVeryLowRssiAttempts:"
+ "setRoamProfileCounts:"
+ "setRoamReasonDeauthCount:"
+ "setRoamScanDurationInMs:"
+ "successfulRoamPercentage"
+ "usedRoamProfiles"
+ "veryLowRssiRoamAttempts"
- "/AppleInternal/Library/BuildRoots/4~CJRgugAKKq0kCjKnNgmx_Gop-soc5PorRhXJ_nA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "[1040Q]"

```
