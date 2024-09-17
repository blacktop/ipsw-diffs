## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1005.1.5.0.0
-  __TEXT.__text: 0x26f5d8
-  __TEXT.__auth_stubs: 0x24d0
-  __TEXT.__objc_methlist: 0x5f8
-  __TEXT.__objc_methname: 0x3ea1
+1007.100.1.1.0
+  __TEXT.__text: 0x282474
+  __TEXT.__auth_stubs: 0x24c0
+  __TEXT.__objc_methlist: 0x614
+  __TEXT.__objc_methname: 0x4009
   __TEXT.__objc_classname: 0x20e
-  __TEXT.__objc_methtype: 0x1368
-  __TEXT.__cstring: 0x7f34
-  __TEXT.__swift5_typeref: 0x5d1d
+  __TEXT.__objc_methtype: 0x1429
+  __TEXT.__cstring: 0x7f64
+  __TEXT.__swift5_typeref: 0x5d89
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xc040
-  __TEXT.__constg_swiftt: 0x95ec
-  __TEXT.__swift5_reflstr: 0x4df4
-  __TEXT.__swift5_fieldmd: 0x4f70
+  __TEXT.__const: 0xc0d0
+  __TEXT.__constg_swiftt: 0x977c
+  __TEXT.__swift5_reflstr: 0x4e84
+  __TEXT.__swift5_fieldmd: 0x4fbc
   __TEXT.__swift5_builtin: 0x1a4
   __TEXT.__swift5_assocty: 0x620
-  __TEXT.__swift5_proto: 0x988
-  __TEXT.__swift5_types: 0x4b8
-  __TEXT.__oslogstring: 0x152c6
+  __TEXT.__swift5_proto: 0x994
+  __TEXT.__swift5_types: 0x4bc
+  __TEXT.__oslogstring: 0x15cf6
   __TEXT.__swift5_protos: 0x1c8
-  __TEXT.__swift5_capture: 0x50ec
+  __TEXT.__swift5_capture: 0x547c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4f20
-  __TEXT.__eh_frame: 0x4ca8
-  __DATA_CONST.__auth_got: 0x1268
-  __DATA_CONST.__got: 0xba8
-  __DATA_CONST.__auth_ptr: 0x1b28
-  __DATA_CONST.__const: 0xfe00
-  __DATA_CONST.__objc_classlist: 0x4d0
+  __TEXT.__unwind_info: 0x50c0
+  __TEXT.__eh_frame: 0x4f10
+  __DATA_CONST.__auth_got: 0x1260
+  __DATA_CONST.__got: 0xbb0
+  __DATA_CONST.__auth_ptr: 0x1c78
+  __DATA_CONST.__const: 0x105d8
+  __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x13588
-  __DATA.__objc_selrefs: 0x1148
+  __DATA.__objc_const: 0x13878
+  __DATA.__objc_selrefs: 0x1178
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x2678
-  __DATA.__data: 0xf010
+  __DATA.__objc_data: 0x26d8
+  __DATA.__data: 0xf2b0
   __DATA.__objc_stublist: 0x70
   __DATA.__bss: 0xeb80
   __DATA.__common: 0x3c0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7407
+  Functions: 7580
   Symbols:   1129
-  CStrings:  3127
+  CStrings:  3180
 
Symbols:
+ _kAACustodianPreflightCRKStateChangedFromGoodToBadEvent
- _swift_stdlib_random
CStrings:
+ " %!s(MISSING) - failed to update and save BeneficiaryInfoRecord %!s(MISSING)     error: %!@(MISSING)"
+ "%!s(MISSING) listOfCRKStateChangedToBad was called."
+ "LCDeletionChangeCKStatusToDeclined feature is not enabled."
+ "%!s(MISSING) - Wrapping key in new inheritanceKey does not match existing wrapping key."
+ "Error while sending beneficiary removed IDS message %!@(MISSING)"
+ "Cannot proceed to remove beneficiary. Error fetching beneficiary -\n%!s(MISSING)"
+ "%!s(MISSING) listOfCRKStateChangedToBad: Returning %!s(MISSING)."
+ "Successfully fetched BenefactorRecord. Declining...."
+ "v32@0:8@\"AKInheritanceAccessKey\"16@?<v@?@\"AKInheritanceAccessKey\"@\"NSError\">24"
+ "  %!s(MISSING) - failed to verify and update BeneficiaryInfoRecord"
+ "@72@0:8@16@24@32@40@48Q56@64"
+ "Successfully declined beneficiary invitation record."
+ "Error declining invitation: %!s(MISSING)"
+ "_TtC13appleaccountd37CustodianPreflightHealthCheckSequoiaB"
+ "%!s(MISSING) - Wrapped key in new inheritanceKey does not match the existing wrapped key."
+ "claimTokenData"
+ "%!s(MISSING) - old accessKey properties do not match new accessKey properties. Error: %!@(MISSING)"
+ "Successfully declined benefactor record: %!s(MISSING)"
+ "One or more CKRs state change to bad: %!l(MISSING)d"
+ "Error creating accessKey. Error: %!@(MISSING)"
+ "LCDeletionChangeCKStatusToDeclined"
+ "Starting cleaning up benefactor..."
+ "Preflight TTR is not available after 18.1"
+ "Notifying beneficiary %!s(MISSING) to remove via IDS."
+ "Successfully to updated CKRecord record status!"
+ "Setting beneficiaryIdentifier to new otPeerID: %!s(MISSING)"
+ "otPeerID"
+ "%!s(MISSING) Preflight result for uuid: %!s(MISSING), transitioning from good to bad"
+ "Invalid Record! Failed to change CKRecord trusted contact status to declined."
+ "Success removing access key for beneficiaryID: %!s(MISSING)"
+ "LCDeletionChangeCKStatusToDeclined feature is enabled. Changing CK record status to declined..."
+ "Invalid container ID received %!s(MISSING)"
+ "CKRecord record updated with otPeerID. %!s(MISSING)!"
+ "earlierReleasePreflightHealthChecker"
+ "%!s(MISSING) Preflight result for uuid: %!s(MISSING), previous: %!{(MISSING)bool}d, current: %!{(MISSING)bool}d"
+ "Preflight error other than error 32 or error 34. Error: %!@(MISSING)"
+ "maxRepairCountForBeneficiaries"
+ "Starting cleaning up beneficiary..."
+ "Invitation record doesn't exist. Begin removal without declining status."
+ "Fetched InheritanceInvitationRecord. Declining record..."
+ "Successfully updated BeneficiaryInfoRecord for beneficiaryUUID: %!s(MISSING)"
+ "initWithBeneficiaryID:benefactorAltDSID:handle:otPeerID:repairDate:repairCount:recordBuildVersion:"
+ "%!s(MISSING) - successfully recreated inheritanceKey for beneficiaryID %!s(MISSING) and new OTPeerID %!s(MISSING)"
+ "Failed to fetch benefactor. Cannot remove benefactor. %!s(MISSING)"
+ "Adding OTPeerID to BeneficiaryInfoRecord with beneficiaryID - %!s(MISSING)..."
+ "Aborting deletion flow. Failed to decline fetched record. Error: %!@(MISSING)."
+ "Failed to update CKRecord record status to removed: %!@(MISSING)"
+ "CKRecord record was not updated with otPeerID %!@(MISSING)"
+ "Fetching beneficiary to delete..."
+ "CKRs state did not change from previous preflight run"
+ "%!s(MISSING) - successfully updated and saved inheritanceKey for beneficiaryID\n%!s(MISSING) and new OTPeerID %!s(MISSING)"
+ "Cannot recognize record type! Failed to change CKRecord trusted contact status to declined."
+ "Failed to update BeneficiaryInfoRecord for beneficiaryUUID: %!s(MISSING)"
+ "recreateInheritanceKeyWithContext:newOTPeerID:inheritanceKey:completion:"
+ "Feature flag turned off, not recreating new access key."
+ "Removing Beneficiary local records."
+ "Recreating PeerID due to preflight error: %!@(MISSING)"
+ "canRepairBeneficiary"
+ "Telemetry event creation failed"
+ "@72@0:8@\"NSUUID\"16@\"NSString\"24@\"NSString\"32@\"NSUUID\"40@\"NSString\"48Q56@\"NSString\"64"
+ "recreateInheritanceKeyWithAccessKey:completion:"
+ "Beneficiary Cleanup Complete!"
+ "Beneficiary repair count  %!l(MISSING)u < IdMS maxRepairCount %!l(MISSING)d. Can repair beneficiaries: %!{(MISSING)bool}d"
+ "Success removing access key for otPeerID: %!s(MISSING)"
+ "TQ,R,N"
+ "%!s(MISSING) - Claim code in new inheritanceKey does not match existing claim code."
+ "wrappedKeyData"
- "LegacyMarkCKRemovedBeforeDeletion"
- "Fetched BenefactorRecord. Declining..."
- "custodianError34"
- "ttr-cfgs ttrFrequency not found"
- "ttr-cfgs ttrFrequency from IdMS: %!l(MISSING)d"
- "Cannot proceed to remove benefactor. Error fetching benefactor - %!s(MISSING)"
- "checkInheritanceKey for beneficiaryID: %!s(MISSING)"
- "ttr-cfgs not found"
- "peerIDCreatedOnBuild"
- "ttr-cfgs url bag requested? %!{(MISSING)bool}d error: %!@(MISSING)"
- "ttr-cfgs: %!s(MISSING)"
- "ttr-cfgs normalized ttrFrequencyForCustodianUnusableCRK: %!l(MISSING)d RandomNumber: %!l(MISSING)d"
- "Error Preflighting Inheritance recovery: %!@(MISSING) for %!s(MISSING)"
- "Error declining invitation - %!s(MISSING)"
- "Removed Beneficiary from storage."
- "CleanupBeneficiary completed successfully. Notifying beneficiary (%!s(MISSING)) to remove via IDS."
- "ttr-cfgs isCustodianPreflightTTREnabledForUnusableCRK %!{(MISSING)bool}d"

```
