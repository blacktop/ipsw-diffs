## wirelessinsightsd

> `/System/Library/PrivateFrameworks/WirelessInsights.framework/Support/wirelessinsightsd`

```diff

-26.0.0.0.0
-  __TEXT.__text: 0xdc550
-  __TEXT.__auth_stubs: 0x20c0
-  __TEXT.__objc_stubs: 0x18e0
-  __TEXT.__init_offsets: 0x12c
-  __TEXT.__objc_methlist: 0x98c
-  __TEXT.__gcc_except_tab: 0xd8c4
+31.0.0.0.0
+  __TEXT.__text: 0xe1070
+  __TEXT.__auth_stubs: 0x20f0
+  __TEXT.__objc_stubs: 0x1ca0
+  __TEXT.__init_offsets: 0x130
+  __TEXT.__objc_methlist: 0xcf4
+  __TEXT.__gcc_except_tab: 0xe0f8
   __TEXT.__const: 0x6d63
-  __TEXT.__cstring: 0x58ab
-  __TEXT.__oslogstring: 0x7aca
-  __TEXT.__objc_methname: 0x255c
-  __TEXT.__objc_classname: 0x1ee
-  __TEXT.__objc_methtype: 0x10d9
-  __TEXT.__unwind_info: 0x5f30
+  __TEXT.__cstring: 0x5bff
+  __TEXT.__oslogstring: 0x8591
+  __TEXT.__objc_methname: 0x2aaa
+  __TEXT.__objc_classname: 0x268
+  __TEXT.__objc_methtype: 0x1143
+  __TEXT.__unwind_info: 0x6108
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x1070
-  __DATA_CONST.__got: 0x3c0
-  __DATA_CONST.__const: 0x76f0
-  __DATA_CONST.__cfstring: 0xa00
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__auth_got: 0x1088
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x77e0
+  __DATA_CONST.__cfstring: 0xd20
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x150
+  __DATA_CONST.__objc_intobj: 0x198
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x1ed0
-  __DATA.__objc_selrefs: 0x6c0
-  __DATA.__objc_classrefs: 0xd8
-  __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0xd8
-  __DATA.__objc_data: 0x320
+  __DATA.__objc_const: 0x25c8
+  __DATA.__objc_selrefs: 0x7c0
+  __DATA.__objc_classrefs: 0x108
+  __DATA.__objc_superrefs: 0x68
+  __DATA.__objc_ivar: 0x12c
+  __DATA.__objc_data: 0x4b0
   __DATA.__data: 0xfc8
-  __DATA.__bss: 0x1b0
+  __DATA.__bss: 0x1c0
   __DATA.__common: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4C7B47DA-2BE8-37F7-B101-B14B688EF6AE
-  Functions: 4591
-  Symbols:   692
-  CStrings:  2112
+  UUID: 25B36DD9-71EC-31AF-8172-9DB5F1EE676D
+  Functions: 4705
+  Symbols:   703
+  CStrings:  2268
 
Symbols:
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _clock_gettime_nsec_np
+ _kCTCellMonitorARFCN
+ _kCTCellMonitorPCI
+ _kCTRegistrationStatusDenied
+ _kCTRegistrationStatusRegisteredHome
+ _kCTRegistrationStatusRegisteredRoaming
+ _kCTRegistrationStatusSearching
+ _kCTRegistrationStatusUnknown
+ _objc_release_x9
+ _objc_retain_x6
+ _objc_retain_x9
- _OBJC_CLASS_$_NSDate
- _objc_retain_x5
CStrings:
+ "\x11!"
+ "\x14"
+ "\x15"
+ "31"
+ "31~71"
+ "@\"NSMutableOrderedSet\""
+ "@\"OOSRecoveryMetricCellInfo\""
+ "@\"OOSRecoveryMetricOOSStartState\""
+ "@124@0:8Q16@24@32@40@48@56@64@72@80@88@96@104B112@116"
+ "@36@0:8B16@20@28"
+ "@40@0:8Q16@24@32"
+ "@56@0:8Q16@24@32@40@48"
+ "@60@0:8Q16q24q32B40@44@52"
+ "B40@0:8@16@24Q32"
+ "Can only extract ARFCN for GSM, UMTS, LTE and NR cells"
+ "Cannot extract PCI: RAT is neither LTE nor NR"
+ "Denied"
+ "NO"
+ "NotRegistered"
+ "OOSRecoveryMetric:#D Airplane mode status switched to %@"
+ "OOSRecoveryMetric:#D Cell info extraction failed. Error %@, servingCellInfo %p, rat %p, band %p, tacOrLac %p, gci %p"
+ "OOSRecoveryMetric:#D Current data context changed to %@"
+ "OOSRecoveryMetric:#D Display status of context %@ changed. New display status: %@"
+ "OOSRecoveryMetric:#D Initializing data for new context %@"
+ "OOSRecoveryMetric:#D Received Cell Monitor update for context %@"
+ "OOSRecoveryMetric:#D Received callback for airplane mode, but its value did not change"
+ "OOSRecoveryMetric:#D Received cell monitor update for unknown context: %@"
+ "OOSRecoveryMetric:#D Received display status change callback for context %@, but display status did not change"
+ "OOSRecoveryMetric:#D Received display status change callback for unknown context: %@"
+ "OOSRecoveryMetric:#D Registration state for context %@ indicates in service, but cell info not up to date"
+ "OOSRecoveryMetric:#D Removing state for %lu contexts, %lu subscriptions in use"
+ "OOSRecoveryMetric:#D Sending OOS event for context %@"
+ "OOSRecoveryMetric:#D Sent CA event for state %@"
+ "OOSRecoveryMetric:#D Skipping initialization for existing context %@"
+ "OOSRecoveryMetric:#D Starting OOS tracking for context %@"
+ "OOSRecoveryMetric:#D Subscription info changed"
+ "OOSRecoveryMetric:#D Successfully initialized state for context %@: %@"
+ "OOSRecoveryMetric:#D Successfully received initial cell info for context %@"
+ "OOSRecoveryMetric:#D Suppressing event since cellInfo or oosStart.cellInfo is default or start is before current time"
+ "OOSRecoveryMetric:#I Current data context changed to %@, but we did not successfully initialize. Running initialization"
+ "OOSRecoveryMetric:#N Error while extracting data from cell for context %@: %@"
+ "OOSRecoveryMetric:Cell info is null for context %@"
+ "OOSRecoveryMetric:Could not allocate state for context %@"
+ "OOSRecoveryMetric:Could not extract cell information for context %@: %@"
+ "OOSRecoveryMetric:Error while fetching cell info for context %@: %@"
+ "OOSRecoveryMetric:Error while fetching registration display status: %@"
+ "OOSRecoveryMetric:Received null display status for context %@"
+ "OOSRecoveryMetric:Subscriptions in use is null"
+ "OOSRecoveryMetric:Unable to fetch current data subscription context: %@"
+ "OOSRecoveryMetric:Unable to fetch subscription info: %@"
+ "OOSRecoveryMetricCellInfo"
+ "OOSRecoveryMetricOOSStartState"
+ "OOSRecoveryMetricState"
+ "RatRetentionMetric:#D Not submitting CA event because current time is before start time"
+ "RatRetentionMetric:#D Not submitting CA event because duration is shorter than threshold: %llu"
+ "RegisteredHome"
+ "RegisteredRoaming"
+ "Reported PCI is less than zero"
+ "Returned value for airplane mode status is of unexpected type"
+ "Searching"
+ "SignalBarMetric:#D Current data context changed to %@"
+ "SignalBarMetric:#D Current data context changed to %@, but we did not successfully initialize. Running initialization"
+ "SignalBarMetric:#D Display status of context %@ changed. Status: %@"
+ "SignalBarMetric:#D Ignoring non-SIM context %@"
+ "SignalBarMetric:#D Initializing data for context %@"
+ "SignalBarMetric:#D Received PLMN change callback for unknown context: %@"
+ "SignalBarMetric:#D Received display status change callback for unknown context: %@"
+ "SignalBarMetric:#D Received signal strength callback for context %@ but signal strength did not change"
+ "SignalBarMetric:#D Received signal strength change callback for unknown context: %@"
+ "SignalBarMetric:#D Removing state for contexts: %@"
+ "SignalBarMetric:#D Signal strength of context %@ changed: %@ bars"
+ "SignalBarMetric:#D Skipping initialization for existing context %@"
+ "SignalBarMetric:#D Subscription info changed"
+ "SignalBarMetric:#D Successfully initialized state for context %@: startTime %llu, MNC %ld, MCC %ld, dataPreferred %@, signalBarState %@, registrationState %@"
+ "SignalBarMetric:Aborting PLMN change update due to error while converting MCC: %@"
+ "SignalBarMetric:Aborting PLMN change update due to error while converting MNC: %@"
+ "SignalBarMetric:Context and/or plmn info is null"
+ "SignalBarMetric:Could not allocate state for context %@"
+ "SignalBarMetric:Error while fetching registration display status: %@"
+ "SignalBarMetric:Invalid subscription context or signal strength info"
+ "SignalBarMetric:PLMN part <= 0: %ld"
+ "SignalBarMetric:Received invalid context for data SIM change"
+ "SignalBarMetric:TelephonyStateRelay coreTelephonyClient is nil"
+ "SignalBarMetric:Unable to convert MCC for context %@: %@"
+ "SignalBarMetric:Unable to convert MNC for context %@: %@"
+ "SignalBarMetric:Unable to fetch MCC for context %@: %@"
+ "SignalBarMetric:Unable to fetch MNC for context %@: %@"
+ "SignalBarMetric:Unable to fetch current data subscription context: %@"
+ "SignalBarMetric:Unable to fetch signal strength for context %@: %@"
+ "SignalBarMetric:Unable to fetch the subscription info: %@"
+ "SignalBarMetric:Unable to find any subscriptions that are in use"
+ "T@\"NSMutableOrderedSet\",&,V_knownOosGcis"
+ "T@\"NSMutableOrderedSet\",&,V_knownOosTacs"
+ "T@\"NSNumber\",R,V_tacOrLac"
+ "T@\"NSString\",R,V_registrationState"
+ "T@\"OOSRecoveryMetricCellInfo\",&,V_cellInfo"
+ "T@\"OOSRecoveryMetricCellInfo\",R,V_cellInfo"
+ "T@\"OOSRecoveryMetricOOSStartState\",&,V_oosStart"
+ "TB,V_isAirplaneModeActive"
+ "TB,V_isContextMapInitialized"
+ "TB,V_isDataContext"
+ "TB,V_knownOosGcisSizeLimited"
+ "TB,V_knownOosTacsSizeLimited"
+ "TQ,R,V_timestamp"
+ "TQ,V_startTime"
+ "TelephonyStateRelay:#N Unable to fetch airplane mode status: %@"
+ "TelephonyStateRelay:Creating preferences for airplane mode updates failed"
+ "TelephonyStateRelay:Error while fetching airplane mode status after callback: %@"
+ "TelephonyStateRelay:Error while setting airplane mode change callback"
+ "TelephonyStateRelay:Error while setting dispatch queue for airplane mode change callback"
+ "TelephonyStateRelay:Unable to allocate preferences name for airplane mode updates"
+ "TelephonyStateRelay:Unable to allocate process name for airplane mode updates"
+ "WISOOSRecoveryMetric"
+ "WISTelephonyUtils"
+ "YES"
+ "_cellInfo"
+ "_isAirplaneModeActive"
+ "_isContextMapInitialized"
+ "_isDataContext"
+ "_knownOosGcis"
+ "_knownOosGcisSizeLimited"
+ "_knownOosTacs"
+ "_knownOosTacsSizeLimited"
+ "_oosStart"
+ "_tacOrLac"
+ "_timestamp"
+ "airplaneModeStatusChanged:"
+ "bandAfter"
+ "bandBefore"
+ "cellInfo"
+ "com.apple.Telephony.cellularOutOfService"
+ "com.apple.wirelessinsightsd.OOSRecoveryMetric"
+ "com.apple.wirelessinsightsd.TelephonyStateRelayPrefs"
+ "dataContext"
+ "duration"
+ "findDelegateEntryByDelegate:"
+ "getAirplaneModeStatus:"
+ "getMAVNRNSANeighborCellInfo:"
+ "getPciFromCellInfo:error:"
+ "getServingCellInfoFromArray:"
+ "getShortenedRegistrationStateString:"
+ "handleCompletedOutOfServiceEventWithState:atTime:"
+ "indexOfObject:"
+ "indexSetWithIndex:"
+ "initWithIsDataContext:registrationState:cellInfo:"
+ "initWithTimestamp:rat:tacOrLac:gci:band:"
+ "initWithTimestamp:registrationState:cellInfo:"
+ "initializeStateForContext:isDataContext:"
+ "insertOrMoveObject:InMutableOrderedSet:WithSizeLimit:"
+ "isAirplaneModeActive"
+ "isContextMapInitialized"
+ "isDataContext"
+ "isDataContext %@, registrationState %@, cellInfo %@, oosStart %@, knownOosTacsSizeLimited %@, knownGcisSizeLimited %@, knownOosTacs %lu, knownOosGcis %lu"
+ "isGSMRat:"
+ "isRegistrationDisplayStatusInService:"
+ "isUMTSRat:"
+ "isValidContext:"
+ "knownOOSCell"
+ "knownOOSTAC"
+ "knownOosGcis"
+ "knownOosGcisSizeLimited"
+ "knownOosTacs"
+ "knownOosTacsSizeLimited"
+ "moveObjectsAtIndexes:toIndex:"
+ "off"
+ "on"
+ "oosCellCacheFull"
+ "oosStart"
+ "oosTACCacheFull"
+ "ratAfter"
+ "ratBefore"
+ "registerAirplaneModeCallbacks"
+ "registrationStateAfter"
+ "registrationStateBefore"
+ "removeObjectAtIndex:"
+ "sameCell"
+ "sameRAT"
+ "sameTAC"
+ "setCellInfo:"
+ "setIsAirplaneModeActive:"
+ "setIsContextMapInitialized:"
+ "setIsDataContext:"
+ "setKnownOosGcis:"
+ "setKnownOosGcisSizeLimited:"
+ "setKnownOosTacs:"
+ "setKnownOosTacsSizeLimited:"
+ "setLastKnownGCI:forPayload:"
+ "setOosStart:"
+ "startTime %llu, displayStatus %@, rat %@, dataBearerTechnology %@, band %@, arfcn %@, nrnsaArfcn %@, bandwidth %@, nrnsaBandwidth %@, frequencyRange %@, nrnsaFrequencyRange %@, dataPreferred %@, subsId %@"
+ "tacOrLac"
+ "timestamp %llu, rat %@, band %@"
+ "timestamp %llu, registrationState %@, cellInfo %@"
+ "updateTimestampTo:"
+ "v24@0:8Q16"
+ "v32@0:8@16Q24"
+ "v32@?0@\"NSUUID\"8@\"OOSRecoveryMetricState\"16^B24"
+ "v36@0:8@16B24Q28"
+ "v40@0:8@16Q24@32"
- "\x11\x11\x11"
- "#D Current data context changed to %@"
- "#D Current data context changed to %@, but we did not successfully initialize. Running initialization"
- "#D Display status of context %@ changed. Status: %@"
- "#D Ignoring non-SIM context %@"
- "#D Initializing data for context %@"
- "#D Received PLMN change callback for unknown context: %@"
- "#D Received display status change callback for unknown context: %@"
- "#D Received signal strength callback for context %@ but signal strength did not change"
- "#D Received signal strength change callback for unknown context: %@"
- "#D Removing state for contexts: %@"
- "#D Signal strength of context %@ changed: %@ bars"
- "#D Skipping initialization for existing context %@"
- "#D Subscription info changed"
- "#D Successfully initialized state for context %@: startTime %.3f, MNC %ld, MCC %ld, dataPreferred %@, signalBarState %@, registrationState %@"
- "26"
- "26~536"
- "@\"NSDictionary\""
- "@124@0:8d16@24@32@40@48@56@64@72@80@88@96@104B112@116"
- "@60@0:8d16q24q32B40@44@52"
- "Aborting PLMN change update due to error while converting MCC: %@"
- "Aborting PLMN change update due to error while converting MNC: %@"
- "Can only extract ARFCN for UMTS, LTE and NR cells"
- "Context and/or plmn info is null"
- "Could not allocate state for context %@"
- "Error while fetching registration display status: %@"
- "Invalid subscription context or signal strength info"
- "PLMN part <= 0: %ld"
- "RatRetentionMetric:#D Not submitting CA event because duration is shorter than threshold: %lld"
- "RatRetentionMetric:#N Unable to fetch airplane mode status: %@"
- "RatRetentionMetric:Creating preferences for airplane mode updates failed"
- "RatRetentionMetric:Error while setting airplane mode change callback"
- "RatRetentionMetric:Error while setting dispatch queue for airplane mode change callback"
- "RatRetentionMetric:Received notification that the airplane mode status changed, but could not fetch the new status: %@"
- "RatRetentionMetric:Unable to allocate preferences name for airplane mode updates"
- "RatRetentionMetric:Unable to allocate process name for airplane mode updates"
- "Received invalid context for data SIM change"
- "Signal bar event duration is less than zero, not submitting: %lld"
- "T@\"NSDictionary\",&,V_lteRBToBWMap"
- "T^{__SCPreferences=},V_airplaneModePrefs"
- "Td,V_startTime"
- "TelephonyStateRelay coreTelephonyClient is nil"
- "Unable to convert MCC for context %@: %@"
- "Unable to convert MNC for context %@: %@"
- "Unable to fetch MCC for context %@: %@"
- "Unable to fetch MNC for context %@: %@"
- "Unable to fetch current data subscription context: %@"
- "Unable to fetch signal strength for context %@: %@"
- "Unable to fetch the subscription info: %@"
- "Unable to find any subscriptions that are in use"
- "^{__SCPreferences=}16@0:8"
- "_lteRBToBWMap"
- "airplaneModePrefs"
- "contextIsValid:"
- "d16@0:8"
- "deriveShortenedRegistrationStateString:"
- "getNRNSANeighborCellInfo:"
- "hasPrefix:"
- "kCTRegistrationStatus"
- "length"
- "lteRBToBWMap"
- "numberWithLongLong:"
- "setAirplaneModePrefs:"
- "setLteRBToBWMap:"
- "startTime %.3f, displayStatus %@, rat %@, dataBearerTechnology %@, band %@, arfcn %@, nrnsaArfcn %@, bandwidth %@, nrnsaBandwidth %@, frequencyRange %@, nrnsaFrequencyRange %@, dataPreferred %@, subsId %@"
- "substringFromIndex:"
- "timeIntervalSinceReferenceDate"
- "v24@0:8^{__SCPreferences=}16"
- "v36@0:8@16B24d28"
- "v40@0:8@16d24@32"

```
