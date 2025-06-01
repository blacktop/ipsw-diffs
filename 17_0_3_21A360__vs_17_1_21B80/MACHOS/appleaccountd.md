## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-973.1.1.3.0
-  __TEXT.__text: 0x211b74
-  __TEXT.__auth_stubs: 0x2110
-  __TEXT.__objc_methlist: 0x5e4
-  __TEXT.__objc_methname: 0x3a66
+981.1.1.0.0
+  __TEXT.__text: 0x22bb20
+  __TEXT.__auth_stubs: 0x2180
+  __TEXT.__objc_methlist: 0x5f0
+  __TEXT.__objc_methname: 0x3c5d
   __TEXT.__objc_classname: 0x1e0
-  __TEXT.__objc_methtype: 0x11c6
-  __TEXT.__cstring: 0x18884
+  __TEXT.__objc_methtype: 0x1207
+  __TEXT.__swift5_typeref: 0x55e7
+  __TEXT.__cstring: 0x1a294
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xafd0
-  __TEXT.__constg_swiftt: 0x782c
-  __TEXT.__swift5_typeref: 0x54b3
+  __TEXT.__const: 0xb260
+  __TEXT.__constg_swiftt: 0x80b8
+  __TEXT.__swift5_reflstr: 0x4114
+  __TEXT.__swift5_fieldmd: 0x4650
   __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_reflstr: 0x3d64
-  __TEXT.__swift5_fieldmd: 0x43d4
   __TEXT.__swift5_assocty: 0x5a8
-  __TEXT.__swift5_proto: 0x8cc
-  __TEXT.__swift5_types: 0x45c
-  __TEXT.__swift5_protos: 0x188
-  __TEXT.__swift5_capture: 0x4650
+  __TEXT.__swift5_proto: 0x8ec
+  __TEXT.__swift5_types: 0x478
+  __TEXT.__swift5_protos: 0x190
+  __TEXT.__swift5_capture: 0x49c4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5200
-  __TEXT.__eh_frame: 0x4418
-  __DATA_CONST.__auth_got: 0x1088
-  __DATA_CONST.__got: 0x608
-  __DATA_CONST.__auth_ptr: 0x3f8
-  __DATA_CONST.__const: 0x123d8
-  __DATA_CONST.__objc_classlist: 0x468
+  __TEXT.__unwind_info: 0x5ba8
+  __TEXT.__eh_frame: 0x49e8
+  __DATA_CONST.__auth_got: 0x10c0
+  __DATA_CONST.__got: 0x650
+  __DATA_CONST.__auth_ptr: 0x420
+  __DATA_CONST.__const: 0x12e88
+  __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xac48
-  __DATA.__objc_selrefs: 0x1040
+  __DATA.__objc_const: 0xb280
+  __DATA.__objc_selrefs: 0x10b0
   __DATA.__objc_protorefs: 0xa0
-  __DATA.__objc_classrefs: 0x418
+  __DATA.__objc_classrefs: 0x420
   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x2250
-  __DATA.__data: 0xce30
+  __DATA.__objc_data: 0x2450
+  __DATA.__data: 0xda68
   __DATA.__objc_stublist: 0x78
-  __DATA.__bss: 0xe000
-  __DATA.__common: 0x368
+  __DATA.__bss: 0xe100
+  __DATA.__common: 0x398
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreML.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4CB839F9-8E02-30C6-AE49-90AAE6710062
-  Functions: 7697
-  Symbols:   1004
-  CStrings:  2712
+  UUID: 1348913B-3C73-3D77-8AD6-5CB5527BDBE1
+  Functions: 7967
+  Symbols:   1021
+  CStrings:  2836
 
Symbols:
+ _$sSu10FoundationE19_bridgeToObjectiveCSo8NSNumberCyF
+ _$ss5Int32V10FoundationE19_bridgeToObjectiveCSo8NSNumberCyF
+ _$syycWV
+ _AAFollowUpIdentifierADPUserMissingHealthyCustodian
+ _OBJC_CLASS_$_AAAnalyticsRTCReporter
+ _OBJC_CLASS_$_AAFAnalyticsEvent
+ __swift_FORCE_LOAD_$_swiftCoreML
+ _kAAAnalyticsAdvancedDataProtectionState
+ _kAAAnalyticsCdpStatus
+ _kAAAnalyticsCircleSyncingStatus
+ _kAAAnalyticsCliqueStatus
+ _kAAAnalyticsSecurityLevel
+ _kAAFDidSucceed
+ _kAppleIDHealthCheckEventName
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_stdlib_isStackAllocationSafe
+ _swift_stdlib_random
- _OBJC_CLASS_$_AASignOutManager
CStrings:
+ "%s %s Apple ID Availability activity completed."
+ "%s %s Apple ID Availability activity failed with error %@"
+ "%s %s Trusted Contacts Preflight activity completed."
+ "%s %s Trusted Contacts Preflight activity failed with error %@"
+ "%s - AutoHeal: But, Recovery Info Record has an RKC. Aborting KeyRepair."
+ "%s - AutoHeal: CRK does not exists on Octagon"
+ "%s - AutoHeal: CRK exists on Octagon"
+ "%s - AutoHeal: CRK never existed. Recovery Info Record is missing RKC. Attempting to create CRK on Octagon"
+ "%s - AutoHeal: Check CRK presence on Octagon returned exists: %{bool}d with error: %@"
+ "%s - AutoHeal: RKC mpt present in CK. KeyRepair is needed. But, cannot delete keys from Octagon. Aborting KeyRepair."
+ "%s - AutoHeal: RKC present in CK. KeyRepair not needed. Aborting KeyRepair."
+ "%s - AutoHeal: Self is nil. Abort Custodian Key Repair"
+ "%s - AutoHeal: error creating recovery keys, unable to repair: %@"
+ "%s - Could not get Continuation Key, Apple ID is NOT available."
+ "%s - Ending preflight."
+ "%s - Error creating InheritanceAccessKeyRecord"
+ "%s - Failed to attach Octagon Status: %@"
+ "%s - Failed to attach SOS Status: %@"
+ "%s - Failed to attach Walrus Status: %@"
+ "%s - Octagon trust is not healthy, Apple ID is NOT available."
+ "%s - Owner is an ADP user, with only one custodian failing preflight."
+ "%s - Owner is an ADP user, with only one custodian with missing CRK and attempt to repair failed. Attempting to mark custodian as not reachable."
+ "%s - Preflight Inheritance Recovery failed for inheritance %s with error: %@\""
+ "%s - Preflight Inheritance Recovery successful for beneficiary %s"
+ "%s - Renew Credentials CFU is posted, Apple ID is NOT available."
+ "%s - Reporting AppleID Availability Healthcheck event %@"
+ "%s - Starting Inheritance Preflight Activity for %s."
+ "%s - Starting to Preflight Inheritance Recovery"
+ "%s - Warning: Custodian records count %ld does not match unique custodian UUIDs count %ld"
+ "%s - custodian %s check recovery key exists: %{bool}d. Ending with success"
+ "%s - custodian %s check recovery key missing: %{bool}d. Ending with failure"
+ "%s - custodian %s is being marked as Not reachable."
+ "%s - custodian %s status is not unreachable, bailing."
+ "%s - error fetching inheritance records: %@"
+ "%s - error repairing recovery keys for %s: %@."
+ "%s - failed to fetch healthy recovery contact status: %s"
+ "%s - failed: successfull."
+ "%s - marking custodian %s as Not reachable."
+ "%s - no manatee available, stopping custodian key repair."
+ "%s - recovery key repair was successful for %s."
+ "%s Starting repair keys"
+ "Adding Custodian ID: %s\nisAcceptedAndShared: %{bool}d\nisIdMSConfirmed: %{bool}d\ncrkExists: %{bool}d\npreflightFailed: %{bool}d"
+ "CRK exists in Octagon? %{bool}d error: %@"
+ "CRK repair successful. Proceeding to refetch records to preflight"
+ "Completed pulling all cloud data before %s Trusted Contacts Preflight activity: %{bool}d"
+ "ConnectionManager: Sending %@ to reporter"
+ "Current Key: %s Bool: %{bool}d"
+ "Custodian Preflight Silent TTR launched successfully."
+ "Did dismiss previously posted custodian invitation CFUs? %{bool}d"
+ "Error Preflighting Inheritance recovery: %@ for %s"
+ "Error repairing CRK."
+ "Inheritance Preflight successful for beneficiaryID: %s"
+ "Lost reference to self. Aborting AppleID Availability XPC activity"
+ "Lost reference to self. Aborting Trusted Contacts Preflight XPC activity"
+ "Mark as not reachable after failed CRK repair resulted in error %@. Ending preflight."
+ "Missing context, reporting CliqueStatus.error"
+ "Missing context, reporting SOSCCStatus.error"
+ "No account signed in. Skipping AppleID Availability activity."
+ "No old Preflight results for uuid: %s exist"
+ "Not logged in to AppleAccount, unable to fetch. Preflight Inheritance Recovery aborted."
+ "Not proceeding with IdMS Setup without recovery keys."
+ "Overall %s Apple ID Availability activities finished with errors: %s"
+ "Overall %s Trusted Contacts Preflight activities finished with errors: %s"
+ "Overall AppleID Availability activity failed: %s"
+ "Overall Custodian Preflight activity successful."
+ "Overall on-demand Apple ID Availability activity completed."
+ "Overall on-demand Apple ID Availability activity failed: %@"
+ "Overall on-demand Trusted Contacts preflight activity completed successfully."
+ "Overall on-demand Trusted Contacts preflight activity failed: %@"
+ "Past Key: %s Bool: %{bool}d"
+ "Preflight result for uuid: %s,\npreviously successful? %{bool}d,\ncurrently successful? %{bool}d"
+ "Preflight result for uuid: %s, are bad. This could possibly be the first bad preflight result."
+ "Preflight result for uuid: %s, transitioning from bad to good"
+ "Preflight result for uuid: %s, transitioning from good to bad"
+ "Preflight results are being fetched from UserDefaults"
+ "Preflight results are set in UserDefaults %s"
+ "Preflight results fetched from UserDefaults %s"
+ "Preflight results for uuid: %s not present"
+ "Preflight results for uuid: %s, is same as before"
+ "Preflight results for uuid: %s, transitioning from bad to bad. Not triggering TTR."
+ "Preflight results not found in UserDefaults"
+ "Preflighting Inheritance Recovery for beneficiaryID: %s"
+ "Recovery Contact Preflight Failed"
+ "Scheduling Apple ID Availability activity"
+ "Scheduling Trusted Contacts preflight activity"
+ "Self is nil. Failed to build custodianship record. Abandoning custodian setup."
+ "Skipping Custodian Preflight TTR: hasAtLeastOneNewInvalidCRK:%{bool}d,\nhasError34:%{bool}d,\nhasError32:%{bool}d"
+ "Skipping Custodian Preflight TTR: isWithInTTRFrequency:%{bool}d"
+ "Starting %s Apple ID Availability activities."
+ "Starting %s Apple ID Availability activity - %s"
+ "Starting %s Trusted Contacts Preflight activities."
+ "Starting %s Trusted Contacts Preflight activity - %s"
+ "Starting Cloud Sync"
+ "Starting on-demand Apple ID Availability activity"
+ "Starting on-demand Trusted Contacts preflight activity"
+ "Starting to pull all cloud data before %s Trusted Contacts Preflight activity"
+ "Successfully marked custodian as not reachable after failed CRK repair. Stopping preflight."
+ "Sync delegate is nil"
+ "Sync delegate is not nil. Saving/deleting records on disk."
+ "Time interval for AppleID Availability activity is being overridden."
+ "Trusted Contact: %s\nisSharedAndAccepted: %{bool}d\nconfirmedWithIdMS: %{bool}d\ninManateeContainer:%{bool}d"
+ "Unable to launch Silent TTR due to error: %@"
+ "[CustodianDaemonService buildRecords] was called."
+ "_TtC13appleaccountd14UrlBagProvider"
+ "_TtC13appleaccountd22DaemonCustodianFetcher"
+ "_TtC13appleaccountd28AppleIDAvailabilityScheduler"
+ "_TtC13appleaccountd30AppleIDAvailabilityHealthCheck"
+ "_TtC13appleaccountd31InheritancePreflightHealthCheck"
+ "_TtC13appleaccountd33TrustedContactsPreflightScheduler"
+ "_TtC13appleaccountd35AppleIDAvailabilityActivityProvider"
+ "_TtC13appleaccountd40TrustedContactsPreflightActivityProvider"
+ "_akAccountManager"
+ "_custodianFetcher"
+ "_followUpController"
+ "_trustedContactsPreflightScheduler"
+ "_urlBagProvider"
+ "activityProvider"
+ "analyticsEventWithName:altDSID:flowID:"
+ "appleIDAvailabilityScheduler"
+ "authKitAccountWithAltDSID:"
+ "com.apple.appleaccount.appleid.availability.serialQueue"
+ "com.apple.appleaccount.custodian.preflight.results.serial.queue"
+ "com.apple.appleaccount.trustedContacts.preflight.serialQueue"
+ "com.apple.appleaccountd.appleid.availability"
+ "com.apple.appleaccountd.trustedContacts.preflight"
+ "configurationAtKey:"
+ "contextForAccountWithAltDSID:"
+ "continuationTokenForAccount:"
+ "custodianError34"
+ "custodianPreflight"
+ "customAppleIDAvailabilityHealthCheckIntervalMinutes"
+ "didRepair"
+ "dismissFollowUpsStartingWithIdentifierPrefix:account:completion:"
+ "failedToFetchRecords"
+ "getCustodianInfo"
+ "hasAtLeastOneNewInvalidCRK was called."
+ "hasAtLeastOneNewInvalidCRK: Intersection set between old / new Preflight results is empty. Returning true."
+ "hasAtLeastOneNewInvalidCRK: Returning %{bool}d."
+ "inheritancePreflight"
+ "initWithID:status:handle:firstName:lastName:displayName:isAcceptedAndShared:isIdMSConfirmed:preflightStatus:"
+ "isCustomAppleIDAvailabilityHealthCheckIntervalEnabled"
+ "isOTEnabledForContext:"
+ "missingRKCinCKRecords"
+ "octagonStatusForContext:withCompletion:"
+ "populateUnderlyingErrorsStartingWithRootError:"
+ "preflightInheritanceRecoveryForBeneficiaryID:accessKey:completion:"
+ "preflightResults"
+ "previousPreflightError"
+ "previousPreflightResults"
+ "reportEvent"
+ "reporter"
+ "requestNewURLBagIfNecessaryWithCompletion:"
+ "sendEvent:"
+ "setCustodianInfo:"
+ "setFullDiagnostic:"
+ "sharedBag"
+ "shouldStartCloudSubscription is true. Creating subscriptions. Database: %@"
+ "simulate2FAFA"
+ "sosStatusForContext:withCompletion:"
+ "trustedContactsPreflightScheduler"
+ "ttr-cfgs isCustodianPreflightTTREnabledForError34 %{bool}d"
+ "ttr-cfgs normalized ttrFrequencyForCustodianError34: %ld RandomNumber: %ld"
+ "ttr-cfgs not found"
+ "ttr-cfgs ttrFrequency from IdMS: %ld"
+ "ttr-cfgs ttrFrequency not found"
+ "ttr-cfgs url bag requested? %{bool}d error: %@"
+ "ttr-cfgs: %s"
+ "uniqueCustodianCount"
+ "v20@?0i8@\"NSError\"12"
+ "v24@?0q8@\"NSError\"16"
+ "v40@0:8@\"NSUUID\"16@\"AKInheritanceAccessKey\"24@?<v@?@\"NSError\">32"
+ "validateAccessKey:withContext:completion:"
- "%s %s Custodian Preflight activity completed."
- "%s %s Custodian Preflight activity failed with error %@"
- "%s - Custodian preflight is enabled. Scheduling."
- "%s - Custodian preflight not enabled. Bailing"
- "%s - Custodian preflight not enabled. Skipping for %s"
- "%s - error creating recovery keys: %@"
- "%s - error regenerating recovery keys, unable to repair: %@"
- "%s - failed to fetch health recovery contact status: %s"
- "Benefactor manatee migrator listening for CKAccountChanged"
- "Beneficiary manatee migrator listening for CKAccountChanged"
- "Completed pulling all cloud data before %s Custodian Preflight activity: %{bool}d"
- "CustodianHealthCheckTTR"
- "Did not sign out with error: %s"
- "Error regenerating recovery key: %@ for %s"
- "Health check for custodian - %s failed. Not updating the health check record."
- "Lost reference to self. Aborting Custodian Preflight XPC activity"
- "No change token found for DB. Likely new Apple ID just signed in. Creating subscriptions. Database: %@"
- "Overall %s Custodian Preflight activities finished with errors: %s"
- "Overall on-demand Custodian preflight activity completed successfully."
- "Overall on-demand Custodian preflight activity failed: %@"
- "Proceeding to IdMS Setup without recovery keys."
- "Scheduling Custodian preflight activity"
- "Starting %s Custodian Preflight activities."
- "Starting %s Custodian Preflight activity - %s"
- "Starting on-demand Custodian preflight activity"
- "Starting to pull all cloud data before %s Custodian Preflight activity"
- "Successfully signed out of the account"
- "Trusted Contact: %s isSharedAndAccepted: %{bool}d confirmedWithIdMS: %{bool}d inManateeContainer:%{bool}d"
- "Trying to delete partially saved custodianship records"
- "_TtC13appleaccountd27CustodianPreflightScheduler"
- "_TtC13appleaccountd34CustodianPreflightActivityProvider"
- "_custodianPreflightScheduler"
- "appleaccountd to run sign out"
- "benefactorManateeMigrator"
- "beneficiaryManateeMigrator"
- "com.apple.appleaccount.custodian.preflight.serialQueue"
- "com.apple.appleaccount.healthcheck.serialQueue"
- "com.apple.appleaccountd.custodian.preflight"
- "custodianPreflightScheduler"
- "handleMarkedForSignOutForAccount:completion:"
- "initWithID:status:handle:firstName:lastName:displayName:isAcceptedAndShared:isIdMSConfirmed:"
- "isCustodianPreflightDisabled"
- "isCustodianPreflightTTREnabled"
- "setAlertOtherButtonAction:"
- "setAlertOtherButtonText:"
- "setHealthCheckTTREnabled:"
- "setKeywords:"
- "signOutOfAccount:completion:"

```
