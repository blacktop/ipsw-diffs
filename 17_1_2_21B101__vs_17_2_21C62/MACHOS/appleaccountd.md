## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-981.1.1.0.0
-  __TEXT.__text: 0x22bb20
+981.5.1.0.0
+  __TEXT.__text: 0x22bd58
   __TEXT.__auth_stubs: 0x2180
-  __TEXT.__objc_methlist: 0x5f0
-  __TEXT.__objc_methname: 0x3c5d
+  __TEXT.__objc_methlist: 0x5dc
+  __TEXT.__objc_methname: 0x3b83
   __TEXT.__objc_classname: 0x1e0
-  __TEXT.__objc_methtype: 0x1207
-  __TEXT.__swift5_typeref: 0x55e7
-  __TEXT.__cstring: 0x1a294
+  __TEXT.__objc_methtype: 0x11c6
+  __TEXT.__cstring: 0x1a4e4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xb260
-  __TEXT.__constg_swiftt: 0x80b8
-  __TEXT.__swift5_reflstr: 0x4114
-  __TEXT.__swift5_fieldmd: 0x4650
+  __TEXT.__const: 0xb3e0
+  __TEXT.__constg_swiftt: 0x82cc
+  __TEXT.__swift5_typeref: 0x5697
   __TEXT.__swift5_builtin: 0x17c
+  __TEXT.__swift5_reflstr: 0x4324
+  __TEXT.__swift5_fieldmd: 0x474c
   __TEXT.__swift5_assocty: 0x5a8
-  __TEXT.__swift5_proto: 0x8ec
-  __TEXT.__swift5_types: 0x478
-  __TEXT.__swift5_protos: 0x190
-  __TEXT.__swift5_capture: 0x49c4
+  __TEXT.__swift5_proto: 0x8fc
+  __TEXT.__swift5_types: 0x480
+  __TEXT.__swift5_protos: 0x194
+  __TEXT.__swift5_capture: 0x48f8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5ba8
-  __TEXT.__eh_frame: 0x49e8
+  __TEXT.__unwind_info: 0x5b28
+  __TEXT.__eh_frame: 0x4980
   __DATA_CONST.__auth_got: 0x10c0
-  __DATA_CONST.__got: 0x650
+  __DATA_CONST.__got: 0x658
   __DATA_CONST.__auth_ptr: 0x420
-  __DATA_CONST.__const: 0x12e88
+  __DATA_CONST.__const: 0x12e10
   __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xb280
-  __DATA.__objc_selrefs: 0x10b0
+  __DATA.__objc_const: 0xb748
+  __DATA.__objc_selrefs: 0x1090
   __DATA.__objc_protorefs: 0xa0
   __DATA.__objc_classrefs: 0x420
   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x2450
-  __DATA.__data: 0xda68
+  __DATA.__objc_data: 0x23a0
+  __DATA.__data: 0xda18
   __DATA.__objc_stublist: 0x78
-  __DATA.__bss: 0xe100
-  __DATA.__common: 0x398
+  __DATA.__bss: 0xe280
+  __DATA.__common: 0x380
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage
   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1348913B-3C73-3D77-8AD6-5CB5527BDBE1
-  Functions: 7967
-  Symbols:   1021
-  CStrings:  2836
+  UUID: B14275D8-A236-39A1-AB8B-85DFDDFF809B
+  Functions: 7965
+  Symbols:   1026
+  CStrings:  2856
 
Symbols:
+ _$s12FeatureFlags02isA7EnabledySbAA0aB3Key_pF
+ _$s12FeatureFlags0aB3KeyMp
+ _$s12FeatureFlags0aB3KeyP6domains12StaticStringVvgTq
+ _$s12FeatureFlags0aB3KeyP7features12StaticStringVvgTq
+ _AAFollowUpUserInfoHasMultipleRecoveryContacts
CStrings:
+ "%s %s Custodian Preflight activity completed."
+ "%s %s Custodian Preflight activity failed with error %@"
+ "%s - Self is nil. Aborting."
+ "%s completed."
+ "%s: appending claimCodeVerificationError to the event %@"
+ "AppleAccount"
+ "Beneficiary UUID: %s"
+ "BeneficiaryInfo: %@"
+ "Claim code hash: %s "
+ "Completed pulling all cloud data before %s Custodian Preflight activity: %{bool}d"
+ "DecoupleOTPeerID"
+ "Fetching beneficiaries error: %s. Aborting %s"
+ "Handle is nil. BeneficiaryID:%s does not require health check"
+ "InheritanceHealthCheckAnalyticsEvent: reporting claimCode error %@"
+ "LockAssertion not supported. Not locking"
+ "LockAssertion not supported. Not unlocking."
+ "Lost reference to self. Aborting Custodian Preflight XPC activity"
+ "Overall %s Custodian Preflight activities finished with errors: %s"
+ "Overall on-demand Custodian preflight activity completed successfully."
+ "Overall on-demand Custodian preflight activity failed: %@"
+ "OverrideAppleIDHealthCheckInterval"
+ "RunAppleAccountdOntvOS"
+ "Scheduling Custodian preflight activity"
+ "Starting %s Custodian Preflight activities."
+ "Starting %s Custodian Preflight activity - %s"
+ "Starting on-demand Custodian preflight activity"
+ "Starting to pull all cloud data before %s Custodian Preflight activity"
+ "Wrapped Key Hash: %s"
+ "beneficiaryInfoForAccount:"
+ "claimCodeVerificationError"
+ "com.apple.appleaccount.custodian.preflight.serialQueue"
+ "com.apple.appleaccountd.custodian.preflight"
+ "countDelta"
+ "didClaimCodeMatch"
+ "didWrappedKeyMatch"
+ "healthRecordNotFound"
+ "idMS ClaimCode Hash: %s"
+ "idMS has EQUAL number of beneficiaries registered."
+ "idMS has LESS number of beneficiaries registered."
+ "idMS has MORE number of beneficiaries registered."
+ "idMSBeneficiaryCryptoData"
+ "invitationNotFound"
+ "isSharedAndAccepted"
+ "localClaimCodeHash: %s"
+ "shouldOverrideInterval"
+ "totalViableEscrowRecords"
+ "underlyingErrors"
+ "🌈🌈🌈 Claim code matches!"
+ "🌧️🌧️🌧️ Claim code does not match."
+ "💥💥💥 Claim code hash missing on idMS."
+ "💥💥💥 Claim code hash was not found in local CK record."
+ "💥💥💥 Failure to fetch beneficiaryInfo."
+ "💥💥💥 Failure to parse beneficiaryInfo."
+ "🛠️🛠️🛠️ Finished parsing beneficiaryInfo..."
+ "🛠️🛠️🛠️ Parsing beneficiaryInfo..."
- "%s %s Trusted Contacts Preflight activity completed."
- "%s %s Trusted Contacts Preflight activity failed with error %@"
- "%s - Error creating InheritanceAccessKeyRecord"
- "%s - Preflight Inheritance Recovery failed for inheritance %s with error: %@\""
- "%s - Preflight Inheritance Recovery successful for beneficiary %s"
- "%s - Starting Inheritance Preflight Activity for %s."
- "%s - Starting to Preflight Inheritance Recovery"
- "%s - beneficiary handle is nil. This beneficiary does not require a health check. BeneficiaryID - %s"
- "%s - error fetching inheritance records: %@"
- "%s - failed to start health check. An error occurred while fetching beneficiaries. Error :- %s"
- "%s - failed: successfull."
- "Completed pulling all cloud data before %s Trusted Contacts Preflight activity: %{bool}d"
- "Error Preflighting Inheritance recovery: %@ for %s"
- "Inheritance Preflight successful for beneficiaryID: %s"
- "Lost reference to self. Aborting Trusted Contacts Preflight XPC activity"
- "Not logged in to AppleAccount, unable to fetch. Preflight Inheritance Recovery aborted."
- "Overall %s Trusted Contacts Preflight activities finished with errors: %s"
- "Overall on-demand Trusted Contacts preflight activity completed successfully."
- "Overall on-demand Trusted Contacts preflight activity failed: %@"
- "Preflighting Inheritance Recovery for beneficiaryID: %s"
- "Scheduling Trusted Contacts preflight activity"
- "Starting %s Trusted Contacts Preflight activities."
- "Starting %s Trusted Contacts Preflight activity - %s"
- "Starting on-demand Trusted Contacts preflight activity"
- "Starting to pull all cloud data before %s Trusted Contacts Preflight activity"
- "appleaccountd.ConnectionManager"
- "com.apple.appleaccount.trustedContacts.preflight.serialQueue"
- "com.apple.appleaccountd.trustedContacts.preflight"
- "contextForAccountWithAltDSID:"
- "customAppleIDAvailabilityHealthCheckIntervalMinutes"
- "inheritancePreflight"
- "isCustomAppleIDAvailabilityHealthCheckIntervalEnabled"
- "preflightInheritanceRecoveryForBeneficiaryID:accessKey:completion:"
- "v40@0:8@\"NSUUID\"16@\"AKInheritanceAccessKey\"24@?<v@?@\"NSError\">32"
- "validateAccessKey:withContext:completion:"

```
