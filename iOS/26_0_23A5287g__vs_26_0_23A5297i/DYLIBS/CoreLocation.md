## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-3056.0.6.0.2
-  __TEXT.__text: 0x1fd0cc
-  __TEXT.__auth_stubs: 0x1af0
-  __TEXT.__objc_methlist: 0xa554
-  __TEXT.__const: 0x4948
-  __TEXT.__gcc_except_tab: 0xf060
-  __TEXT.__oslogstring: 0x3a8ad
-  __TEXT.__cstring: 0x257aa
+3056.0.14.0.0
+  __TEXT.__text: 0x1fd458
+  __TEXT.__auth_stubs: 0x1b00
+  __TEXT.__objc_methlist: 0xa594
+  __TEXT.__const: 0x4938
+  __TEXT.__gcc_except_tab: 0xefe4
+  __TEXT.__oslogstring: 0x3a8f3
+  __TEXT.__cstring: 0x259bb
   __TEXT.__ustring: 0x70a
-  __TEXT.__unwind_info: 0x5910
+  __TEXT.__unwind_info: 0x5878
   __TEXT.__objc_classname: 0x1395
-  __TEXT.__objc_methname: 0x1cf9d
-  __TEXT.__objc_methtype: 0x5dc7
-  __TEXT.__objc_stubs: 0xeb00
+  __TEXT.__objc_methname: 0x1d101
+  __TEXT.__objc_methtype: 0x5da4
+  __TEXT.__objc_stubs: 0xeac0
   __DATA_CONST.__got: 0x748
-  __DATA_CONST.__const: 0x2198
+  __DATA_CONST.__const: 0x2170
   __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5540
+  __DATA_CONST.__objc_selrefs: 0x5568
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0xd90
+  __AUTH_CONST.__auth_got: 0xd98
   __AUTH_CONST.__const: 0x3b98
-  __AUTH_CONST.__cfstring: 0xbde0
-  __AUTH_CONST.__objc_const: 0x11838
+  __AUTH_CONST.__cfstring: 0xbec0
+  __AUTH_CONST.__objc_const: 0x11950
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x2ee0
-  __DATA.__objc_ivar: 0xb38
+  __DATA.__objc_ivar: 0xb50
   __DATA.__data: 0xf20
   __DATA.__bss: 0xae0
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_ivar: 0xa8
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0xd60
+  __DATA_DIRTY.__bss: 0xd30
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E9E528FE-0A12-3A59-9FBC-2E5E7DE80B1B
-  Functions: 5322
+  UUID: 1F737E56-F0E3-309B-9AEE-864235635B20
+  Functions: 5307
   Symbols:   1115
-  CStrings:  12022
+  CStrings:  12056
 
Symbols:
+ _objc_release_x28
- _CLCopyMicroLocationInternalVersion
CStrings:
+ "#EED2FWK,%{public}s, invalid value received for key:%{public}@"
+ "#EED2FWK,%{public}s, invalid value received for key:%{public}@ value:%{public}ld"
+ "-[CLEEDFeedbackRequest getBooleanAsNumberFromDictionary:key:]"
+ "-[CLEEDFeedbackRequest getIntegerAsNumberFromDictionary:key:]"
+ "00:48:43"
+ "@344@0:8Q16Q24Q32Q40Q48Q56Q64Q72Q80Q88Q96Q104Q112Q120Q128Q136Q144Q152Q160Q168Q176Q184Q192Q200Q208Q216Q224q232Q240Q248Q256Q264Q272Q280Q288Q296Q304Q312Q320Q328Q336"
+ "CoreLocation MiLo DonateMicroLocationTruthTag API Deprecated"
+ "CoreLocation MiLo DonateMicroLocationTruthTagBetweenDates API Deprecated"
+ "CoreLocation MiLo ExportMicroLocationDataForMigration API Deprecated"
+ "CoreLocation MiLo ExportMicroLocationDatabaseTables API Deprecated"
+ "CoreLocation MiLo RequestMicroLocationLearning API Deprecated"
+ "CoreLocation MiLo RequestMicroLocationStaticSourcesStatistics API Deprecated"
+ "CoreLocation MiLo RequestRecordingOrLocalization API Deprecated"
+ "Invalid call to CLClientDonateMicroLocationTruthTag"
+ "Invalid call to CLClientDonateMicroLocationTruthTagBetweenDates"
+ "Invalid call to CLClientPurgeMicroLocationData"
+ "Invalid call to CLClientPurgeMicroLocationSemiSupervisedData"
+ "Invalid call to CLClientRequestMicroLocationLearning"
+ "Invalid call to CLClientRequestMicroLocationStaticSourcesStatistics"
+ "Invalid call to CLClientRequestRecordingOrLocalization"
+ "Invalid call to CLExportMicroLocationDataForMigration"
+ "Invalid call to CLExportMicroLocationDatabaseTables"
+ "Jul 15 2025"
+ "TQ,R,V_nbmmsRangingCount"
+ "TQ,R,V_tempHighCount"
+ "TQ,R,V_tempLastPIn"
+ "TQ,R,V_tempLowCount"
+ "TQ,R,V_tempOkCount"
+ "TQ,R,V_tempVeryLowCount"
+ "Unspecified_Or_Invalid"
+ "_nbmmsRangingCount"
+ "_tempHighCount"
+ "_tempLastPIn"
+ "_tempLowCount"
+ "_tempOkCount"
+ "_tempVeryLowCount"
+ "bool CLLocationOutlierRejector::runRejector(NSArray<CLTripSegmentLocation *> * _Nonnull, NSArray<CLBackgroundInertialOdometrySample *> * _Nullable, NSMutableIndexSet * _Nullable, std::unordered_map<size_t, double> &, std::unordered_map<size_t, double> &, const bool)"
+ "bool CLLocationOutlierRejector::selectInliers(NSArray<CLTripSegmentLocation *> * _Nonnull, NSArray<CLBackgroundInertialOdometrySample *> * _Nonnull, NSMutableIndexSet * _Nonnull, double &, double &)"
+ "bool CLTrajectorySmoother::runPedestrianTrajectorySmoothing(NSArray<CLTripSegmentLocation *> * _Nonnull, NSArray<CLBackgroundInertialOdometrySample *> * _Nullable, NSMutableArray<CLTripSegmentLocation *> * _Nonnull, double &, const bool, const bool, std::unordered_map<size_t, double> &, std::unordered_map<size_t, double> &)"
+ "getBooleanAsNumberFromDictionary:key:"
+ "getIntegerAsNumberFromDictionary:key:"
+ "initWithOverflowFlag:crashCount:multiTime:nearOwnerTime:wildTime:soundCount:soundTime:rangingCount:rangingTime:multiLeashTime:multiConnectionTime:nearOwnerTimeV2:singleLeashTime:singleConnectionTime:dualConnectionTime:dualLeashTime:utAccelCount:lastClear:roseOnTime:ownerLongSoundCount:ownerShortSoundCount:utLongSoundCount:utShortSoundCount:bomSoundCount:fc1ndRangingCount:fc1ndRangingTime:lastPIn:batteryState:nbmmsRangingTime:abandonedFwUpdateCount:abandonedFwUpdateTime:roseInitCount:pairingAttemptsCount:tempVeryLowCount:tempLowCount:tempOkCount:tempHighCount:proxPairingTime:tempLastPIn:nbmmsRangingCount:version:"
+ "lastPInTemperature"
+ "nbmmsRangingCount"
+ "tempHighCount"
+ "tempLastPIn"
+ "tempLowCount"
+ "tempOkCount"
+ "tempVeryLowCount"
+ "void CLClientDonateMicroLocationTruthTag(CLClientRef, CFStringRef, CFStringRef, void (^)(NSError *))"
+ "void CLClientDonateMicroLocationTruthTagBetweenDates(CLClientRef, CFStringRef, CFDateRef, CFDateRef, void (^)(NSError *))"
+ "void CLClientPurgeMicroLocationData(CLClientRef)"
+ "void CLClientPurgeMicroLocationSemiSupervisedData(CLClientRef)"
+ "void CLClientRequestMicroLocationLearning(CLClientRef, void (^)(bool, NSError *))"
+ "void CLClientRequestMicroLocationStaticSourcesStatistics(CLClientRef, void (^)(NSError *, CFDictionaryRef))"
+ "void CLClientRequestRecordingOrLocalization(CLClientRef, const char *const, CFDictionaryRef, void (^)(bool, NSError *))"
+ "void CLExportMicroLocationDataForMigration(CLClientRef, void (^)(NSError *, CFDictionaryRef))"
+ "void CLExportMicroLocationDatabaseTables(CLClientRef, void (^)(NSError *, CFDictionaryRef))"
+ "{\"msg%{public}.0s\":\"#durian #userstats\", \"type\":%{public, location:escape_only}s, \"typeByte\":%{public}d, \"length\":%{public}d, \"valueHex\":%{public, location:escape_only}@, \"value\":%{public}lu}"
- "-[CLMiLoConnectionInternal initWithInfo:delegate:delegateQueue:]_block_invoke"
- "21:28:14"
- "@296@0:8Q16Q24Q32Q40Q48Q56Q64Q72Q80Q88Q96Q104Q112Q120Q128Q136Q144Q152Q160Q168Q176Q184Q192Q200Q208Q216Q224q232Q240Q248Q256Q264Q272Q280Q288"
- "CL: CLCopyMicroLocationInternalVersion"
- "CLMiLoConnection, connection to locationd interrupted"
- "DefaultMessageHandler, received null response"
- "Jul  1 2025"
- "^{__CFString=}16@0:8"
- "bool CLLocationOutlierRejector::runRejector(NSArray<CLTripSegmentLocation *> * _Nonnull, NSArray<CLBackgroundInertialOdometrySample *> * _Nullable, NSMutableIndexSet * _Nullable, std::unordered_map<size_t, double> &, const bool)"
- "bool CLLocationOutlierRejector::selectInliers(NSArray<CLTripSegmentLocation *> * _Nonnull, NSArray<CLBackgroundInertialOdometrySample *> * _Nonnull, NSMutableIndexSet * _Nonnull, double &)"
- "bool CLTrajectorySmoother::runPedestrianTrajectorySmoothing(NSArray<CLTripSegmentLocation *> * _Nonnull, NSArray<CLBackgroundInertialOdometrySample *> * _Nullable, NSMutableArray<CLTripSegmentLocation *> * _Nonnull, double &, const bool, const bool, std::unordered_map<size_t, double> &)"
- "copyMicroLocationInternalVersion"
- "getMicroLocationInternalVersion"
- "getMicroLocationInternalVersionWithReplyBlock:"
- "initWithOverflowFlag:crashCount:multiTime:nearOwnerTime:wildTime:soundCount:soundTime:rangingCount:rangingTime:multiLeashTime:multiConnectionTime:nearOwnerTimeV2:singleLeashTime:singleConnectionTime:dualConnectionTime:dualLeashTime:utAccelCount:lastClear:roseOnTime:ownerLongSoundCount:ownerShortSoundCount:utLongSoundCount:utShortSoundCount:bomSoundCount:fc1ndRangingCount:fc1ndRangingTime:lastPIn:batteryState:nbmmsRangingTime:abandonedFwUpdateCount:abandonedFwUpdateTime:roseInitCount:pairingAttemptsCount:proxPairingTime:version:"
- "kCLConnectionMessageMicroLocationDonateTruthLabelBetweenDatesEvent"
- "kCLConnectionMessageMicroLocationDonateTruthLabelEvent"
- "kCLConnectionMessageMicroLocationExportDataForMigration"
- "kCLConnectionMessageMicroLocationExportDataForMigrationInfoKey"
- "kCLConnectionMessageMicroLocationExportDatabaseTables"
- "kCLConnectionMessageMicroLocationExportDatabaseTablesInfoKey"
- "kCLConnectionMessageMicroLocationRecordingTriggerUuidKey"
- "kCLConnectionMessageMicroLocationRequestLearning"
- "kCLConnectionMessageMicroLocationRequestStaticSourcesStatistics"
- "kCLConnectionMessageMicroLocationRequestStaticSourcesStatisticsInfoKey"
- "kCLConnectionMessageMicroLocationTruthLabelEndDateKey"
- "kCLConnectionMessageMicroLocationTruthLabelKey"
- "kCLConnectionMessageMicroLocationTruthLabelStartDateKey"
- "kCLConnectionMessagePurgeMicroLocationData"
- "kCLConnectionMessagePurgeMicroLocationSemiSupervisedData"
- "kCLConnectionMessageRequestMicroLocation"
- "kCLConnectionMessageRequestMicroLocationRecordingScan"
- "v24@0:8@?<v@?@\"NSError\"@\"NSString\">16"
- "{\"msg%{public}.0s\":\"#durian #userstats\", \"type\":%{public, location:escape_only}s, \"typeByte\":%{public}d, \"length\":%{public}d, \"valueHex\":%{public, location:escape_only}@, \"value\":%{public}u}"
- "{\"msg%{public}.0s\":\"CLCopyMicroLocationInternalVersion\", \"event\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"DefaultMessageHandler, known non-actionable message\", \"MessageName\":%{public, location:escape_only}s, \"DictionaryKeys\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"DefaultMessageHandler, message received\", \"MessageName\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"received internal version get request\"}"

```
