## IntelligentRoutingDaemon

> `/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon`

```diff

-66.0.1.0.0
-  __TEXT.__text: 0x66f2c
+66.0.3.0.0
+  __TEXT.__text: 0x67514
   __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0x6578
-  __TEXT.__oslogstring: 0x5eab
-  __TEXT.__cstring: 0x8810
+  __TEXT.__objc_methlist: 0x65c8
+  __TEXT.__oslogstring: 0x5ed8
+  __TEXT.__cstring: 0x886d
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x120c
-  __TEXT.__unwind_info: 0x1730
-  __TEXT.__objc_classname: 0xe98
-  __TEXT.__objc_methname: 0x14dc7
-  __TEXT.__objc_methtype: 0x1e31
-  __TEXT.__objc_stubs: 0xce00
+  __TEXT.__unwind_info: 0x1770
+  __TEXT.__objc_classname: 0xead
+  __TEXT.__objc_methname: 0x14f4d
+  __TEXT.__objc_methtype: 0x1e4a
+  __TEXT.__objc_stubs: 0xcf00
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x1b48
-  __DATA_CONST.__objc_classlist: 0x418
+  __DATA_CONST.__const: 0x1b90
+  __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa7e8
-  __DATA_CONST.__objc_selrefs: 0x3910
+  __DATA_CONST.__objc_const: 0xa8c8
+  __DATA_CONST.__objc_selrefs: 0x3958
+  __DATA_CONST.__objc_classrefs: 0x670
+  __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x4c8
   __AUTH_CONST.__objc_const: 0x3780
-  __AUTH_CONST.__cfstring: 0x6da0
+  __AUTH_CONST.__cfstring: 0x6e20
   __AUTH_CONST.__objc_intobj: 0x2e8
-  __AUTH_CONST.__const: 0x5c0
+  __AUTH_CONST.__const: 0x5e0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0x438
-  __AUTH.__objc_data: 0x910
-  __DATA.__objc_classrefs: 0x668
-  __DATA.__objc_superrefs: 0x2d0
-  __DATA.__objc_ivar: 0x884
+  __AUTH.__objc_data: 0x960
+  __DATA.__objc_ivar: 0x888
   __DATA.__data: 0xb40
-  __DATA.__bss: 0x3c
+  __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x1fe0
-  __DATA_DIRTY.__bss: 0x98
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2437
-  Symbols:   8858
-  CStrings:  4623
+  Functions: 2450
+  Symbols:   8899
+  CStrings:  4642
 
Symbols:
+ +[IRAnalyticsUtilities _temporaryListOfAllowedApps]
+ +[IRAnalyticsUtilities getRedactedBundleID:]
+ +[IRAnalyticsUtilities isMediaEligibleApp:]
+ -[IRCandidateClassificationDetectorSameSpace _isSameSpaceBrokeredDeviceForCandidate:basedOnSystemState:andHistoryEventsAsc:andDate:]
+ -[IRCandidateDO(Extensions) containsNonAirplayTarget]
+ -[IRCandidatesContainerDO(Extension) airplayOrUnknownCandidates]
+ -[IRNodeDO(Extension) deviceTypeExistsAirplay]
+ -[IRNodeDO(Extension) deviceTypeExistsNotAirplay]
+ -[IRPolicyEngine shouldAskForLowLatencyMiLo:historyEventsContainer:]
+ -[IRPolicyEngine shouldRejectEvent:withHistoryEventsContainer:forCandidateIdentifier:]
+ -[IRPreferences AVODOverrideIsAirplayForCandidateIDArray]
+ -[IRPreferences candidateSelectorAllowSelectByPDRFence]
+ -[IRPreferences deleteAndNotifyKey:]
+ -[IRProximityProvider didLocationDCrashProxy]
+ -[IRServicePackageAdapterAppleTVControl shouldAskForLowLatencyMiLo:historyEventsAsc:]
+ -[IRServicePackageAdapterAppleTVControl shouldRejectEvent:withHistoryEventsContainer:forCandidateIdentifier:]
+ -[IRServicePackageAdapterMedia shouldAskForLowLatencyMiLo:historyEventsAsc:]
+ -[IRServicePackageAdapterMedia shouldRejectEvent:withHistoryEventsContainer:forCandidateIdentifier:]
+ -[IRServiceStore _cleanupNotAirplayCandidates]
+ -[IRSystemStateDO(Extension) isMiLoSupportedLocation]
+ -[IRSystemStateManager didLocationDCrashProxy]
+ _OBJC_CLASS_$_IRAnalyticsUtilities
+ _OBJC_IVAR_$_IRPreferences._AVODOverrideIsAirplayForCandidateIDArray
+ _OBJC_IVAR_$_IRPreferences._candidateSelectorAllowSelectByPDRFence
+ _OBJC_METACLASS_$_IRAnalyticsUtilities
+ __OBJC_$_CLASS_METHODS_IRAnalyticsUtilities
+ __OBJC_CLASS_RO_$_IRAnalyticsUtilities
+ __OBJC_METACLASS_RO_$_IRAnalyticsUtilities
+ ___132-[IRCandidateClassificationDetectorSameSpace _isSameSpaceBrokeredDeviceForCandidate:basedOnSystemState:andHistoryEventsAsc:andDate:]_block_invoke
+ ___166-[IRClassificatonGenerator generateClassificationsWithCandiatesContainer:systemState:historyEventsContainer:miloPrediction:nearbyDeviceContainer:fillInspection:date:]_block_invoke.38
+ ___166-[IRClassificatonGenerator generateClassificationsWithCandiatesContainer:systemState:historyEventsContainer:miloPrediction:nearbyDeviceContainer:fillInspection:date:]_block_invoke_2.42
+ ___45-[IRProximityProvider didLocationDCrashProxy]_block_invoke
+ ___46-[IRServiceStore _cleanupNotAirplayCandidates]_block_invoke
+ ___53-[IRCandidateDO(Extensions) containsNonAirplayTarget]_block_invoke
+ ___55-[IRProximityProvider didBridgeSuspendStartedWithName:]_block_invoke.55
+ ___64-[IRCandidatesContainerDO(Extension) airplayOrUnknownCandidates]_block_invoke
+ ___76-[IRServicePackageAdapterMedia shouldAskForLowLatencyMiLo:historyEventsAsc:]_block_invoke
+ ___76-[IRServicePackageAdapterMedia shouldAskForLowLatencyMiLo:historyEventsAsc:]_block_invoke_2
+ ___85-[IRServicePackageAdapterAppleTVControl shouldAskForLowLatencyMiLo:historyEventsAsc:]_block_invoke
+ ___85-[IRServicePackageAdapterAppleTVControl shouldAskForLowLatencyMiLo:historyEventsAsc:]_block_invoke_2
+ ___block_descriptor_32_e8_v16?08l
+ ___block_descriptor_40_e8_32s_e28_16?0"IRCandidateWrapper"8ls32l8
+ ___block_descriptor_40_e8_32s_e33_v32?0"IRHistoryEventDO"8Q16^B24ls32l8
+ ___block_descriptor_80_e8_32s40r48r56r64r72r_e33_v32?0"IRHistoryEventDO"8Q16^B24ls32l8r40l8r48l8r56l8r64l8r72l8
+ ___block_literal_global.133
+ ___block_literal_global.236
+ ___block_literal_global.37
+ ___block_literal_global.57
+ _objc_msgSend$AVODOverrideIsAirplayForCandidateIDArray
+ _objc_msgSend$_cleanupNotAirplayCandidates
+ _objc_msgSend$_isSameSpaceBrokeredDeviceForCandidate:basedOnSystemState:andHistoryEventsAsc:andDate:
+ _objc_msgSend$airplayOrUnknownCandidates
+ _objc_msgSend$candidateSelectorAllowSelectByPDRFence
+ _objc_msgSend$containsNonAirplayTarget
+ _objc_msgSend$deviceTypeExistsAirplay
+ _objc_msgSend$deviceTypeExistsNotAirplay
+ _objc_msgSend$didLocationDCrashProxy
+ _objc_msgSend$getRedactedBundleID:
+ _objc_msgSend$isMediaEligibleApp:
+ _objc_msgSend$isMiLoSupportedLocation
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$shouldAskForLowLatencyMiLo:historyEventsAsc:
+ _objc_msgSend$shouldAskForLowLatencyMiLo:historyEventsContainer:
+ _objc_msgSend$shouldRejectEvent:withHistoryEventsContainer:forCandidateIdentifier:
- +[IRServicePackageAdapterMedia(IRAnalytics) _temporaryListOfAllowedApps]
- -[IRCandidateClassificationDetectorSameSpace _isSameSpaceBrokeredDeviceForCandidate:basedOnLoi:andHistoryEventsAsc:andDate:]
- -[IRCandidateDO(Extensions) isValidForPrediction]
- -[IRCandidatesContainerDO(Extension) validForPredictionCandidates]
- -[IRNodeDO(Extension) isAirplayTarget]
- -[IRPolicyEngine shouldAskForLowLatencyMiLo:]
- -[IRPolicyEngine shouldRejectEvent:withHistoryEventsContainer:]
- -[IRPreferences pdrFenceCandidateSelectorAllowSelectByFence]
- -[IRServicePackageAdapterAppleTVControl _oneTapClassificationPositiveRulesForCandidate:forClassificationEvaluated:]
- -[IRServicePackageAdapterAppleTVControl shouldAskForLowLatencyMiLo:]
- -[IRServicePackageAdapterAppleTVControl shouldRejectEvent:withHistoryEventsContainer:]
- -[IRServicePackageAdapterMedia shouldAskForLowLatencyMiLo:]
- -[IRServicePackageAdapterMedia shouldRejectEvent:withHistoryEventsContainer:]
- -[IRServiceStore _cleanupNotValidForPredictionCandidates]
- GCC_except_table31
- _OBJC_IVAR_$_IRPreferences._pdrFenceCandidateSelectorAllowSelectByFence
- __OBJC_$_CLASS_METHODS_IRServicePackageAdapterMedia(IRAnalytics)
- ___124-[IRCandidateClassificationDetectorSameSpace _isSameSpaceBrokeredDeviceForCandidate:basedOnLoi:andHistoryEventsAsc:andDate:]_block_invoke
- ___166-[IRClassificatonGenerator generateClassificationsWithCandiatesContainer:systemState:historyEventsContainer:miloPrediction:nearbyDeviceContainer:fillInspection:date:]_block_invoke.36
- ___55-[IRProximityProvider didBridgeSuspendStartedWithName:]_block_invoke.53
- ___57-[IRServiceStore _cleanupNotValidForPredictionCandidates]_block_invoke
- ___66-[IRCandidatesContainerDO(Extension) validForPredictionCandidates]_block_invoke
- ___88-[IRCandidateSelector selectFromCandidates:withSystemState:andHistoryEventsAsc:andDate:]_block_invoke
- ___block_descriptor_32_e28_B16?0"IRCandidateWrapper"8l
- ___block_descriptor_88_e8_32s40s48r56r64r72r80r_e33_v32?0"IRHistoryEventDO"8Q16^B24ls32l8r48l8s40l8r56l8r64l8r72l8r80l8
- ___block_literal_global.123
- ___block_literal_global.135
- ___block_literal_global.232
- _kRuleAppleTVControlLongTermPatternAtLOIKey
- _objc_msgSend$_cleanupNotValidForPredictionCandidates
- _objc_msgSend$_isSameSpaceBrokeredDeviceForCandidate:basedOnLoi:andHistoryEventsAsc:andDate:
- _objc_msgSend$isAirplayTarget
- _objc_msgSend$isValidForPrediction
- _objc_msgSend$pdrFenceCandidateSelectorAllowSelectByFence
- _objc_msgSend$shouldAskForLowLatencyMiLo:
- _objc_msgSend$shouldRejectEvent:withHistoryEventsContainer:
- _objc_msgSend$validForPredictionCandidates
CStrings:
+ "\x1f\x0f\x0f\x0f\x0f\x0f\x05"
+ "%s[%@], SameSpaceCandidate: name: %@, identifier: %@, MiLo: %@, BrokeredDeviceInLOI: %@, PDRFence: %@, uwbRange: %@, bleRange: %@"
+ "%s[%@], didLocationDCrashProxy"
+ "AVODOverrideIsAirplayForCandidateIDArray"
+ "B32@0:8@\"IRCandidatesContainerDO\"16@\"NSArray\"24"
+ "B40@0:8@\"IREventDO\"16@\"IRHistoryEventsContainerDO\"24@\"NSString\"32"
+ "IRAVODOverrideIsAirplayForCandidateIDArray"
+ "IRAnalyticsUtilities"
+ "IRcandidateSelectorAllowSelectByPDRFence"
+ "T@\"NSArray\",R,N,V_AVODOverrideIsAirplayForCandidateIDArray"
+ "T@\"NSNumber\",R,N,V_candidateSelectorAllowSelectByPDRFence"
+ "T@\"NSString\",?,R,C"
+ "UI_Event_Current_LOI_Enum"
+ "UI_Event_Internal_App_Name_Enum"
+ "UI_Event_Is_Eligible_App"
+ "_AVODOverrideIsAirplayForCandidateIDArray"
+ "_candidateSelectorAllowSelectByPDRFence"
+ "_cleanupNotAirplayCandidates"
+ "_isSameSpaceBrokeredDeviceForCandidate:basedOnSystemState:andHistoryEventsAsc:andDate:"
+ "airplayOrUnknownCandidates"
+ "candidateSelectorAllowSelectByPDRFence"
+ "com.apple."
+ "com.apple.mobilesafari"
+ "containsNonAirplayTarget"
+ "deleteAndNotifyKey:"
+ "deviceTypeExistsAirplay"
+ "deviceTypeExistsNotAirplay"
+ "didLocationDCrashProxy"
+ "getRedactedBundleID:"
+ "isMediaEligibleApp:"
+ "isMiLoSupportedLocation"
+ "setWithObjects:"
+ "shouldAskForLowLatencyMiLo:historyEventsAsc:"
+ "shouldAskForLowLatencyMiLo:historyEventsContainer:"
+ "shouldRejectEvent:withHistoryEventsContainer:forCandidateIdentifier:"
+ "speaker"
+ "v16@?0@8"
- "\x1f\x0f\x0f\x0f\x0f\x0f\x04"
- "%s[%@], SameSpaceCandidate: name: %@, identifier: %@, MiLo: %@, BrokeredDeviceInLOI: %@, uwbRange: %@, bleRange: %@"
- "AppleTVControl_Long_term_pattern_at_LOI"
- "B24@0:8@\"IRCandidatesContainerDO\"16"
- "B32@0:8@\"IREventDO\"16@\"IRHistoryEventsContainerDO\"24"
- "IRpdrFenceCandidateSelectorAllowSelectByFence"
- "T@\"NSNumber\",R,N,V_pdrFenceCandidateSelectorAllowSelectByFence"
- "UI_Event_App_Type"
- "UI_Event_Current_LOI"
- "_cleanupNotValidForPredictionCandidates"
- "_isSameSpaceBrokeredDeviceForCandidate:basedOnLoi:andHistoryEventsAsc:andDate:"
- "_pdrFenceCandidateSelectorAllowSelectByFence"
- "isAirplayTarget"
- "isValidForPrediction"
- "pdrFenceCandidateSelectorAllowSelectByFence"
- "shouldAskForLowLatencyMiLo:"
- "shouldRejectEvent:withHistoryEventsContainer:"
- "validForPredictionCandidates"

```
