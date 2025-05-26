## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-981.20.0.0.0
-  __TEXT.__text: 0x26a744
-  __TEXT.__auth_stubs: 0x22f0
-  __TEXT.__objc_methlist: 0x618
-  __TEXT.__objc_methname: 0x3cdd
+981.23.0.0.0
+  __TEXT.__text: 0x272f98
+  __TEXT.__auth_stubs: 0x2300
+  __TEXT.__objc_methlist: 0x620
+  __TEXT.__objc_methname: 0x3cfb
   __TEXT.__objc_classname: 0x1e0
-  __TEXT.__objc_methtype: 0x123a
-  __TEXT.__cstring: 0x1bd34
-  __TEXT.__swift5_typeref: 0x5a2d
+  __TEXT.__objc_methtype: 0x1261
+  __TEXT.__cstring: 0x1c074
+  __TEXT.__swift5_typeref: 0x5a09
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xb7c0
-  __TEXT.__constg_swiftt: 0x8eb0
-  __TEXT.__swift5_reflstr: 0x4894
-  __TEXT.__swift5_fieldmd: 0x4b68
+  __TEXT.__const: 0xb6c0
+  __TEXT.__constg_swiftt: 0x8f24
+  __TEXT.__swift5_reflstr: 0x4914
+  __TEXT.__swift5_fieldmd: 0x4b88
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_assocty: 0x5a8
-  __TEXT.__swift5_proto: 0x928
-  __TEXT.__swift5_types: 0x490
+  __TEXT.__swift5_proto: 0x924
+  __TEXT.__swift5_types: 0x48c
   __TEXT.__swift5_protos: 0x1b8
-  __TEXT.__swift5_capture: 0x4b94
+  __TEXT.__swift5_capture: 0x4c4c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x57e4
-  __TEXT.__eh_frame: 0x5440
-  __DATA_CONST.__auth_got: 0x1178
-  __DATA_CONST.__got: 0x720
-  __DATA_CONST.__auth_ptr: 0x428
-  __DATA_CONST.__const: 0x13480
+  __TEXT.__unwind_info: 0x5a80
+  __TEXT.__eh_frame: 0x5688
+  __DATA_CONST.__auth_got: 0x1180
+  __DATA_CONST.__got: 0x730
+  __DATA_CONST.__auth_ptr: 0x430
+  __DATA_CONST.__const: 0x13490
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_classrefs: 0x418
+  __DATA_CONST.__objc_classrefs: 0x410
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xbfa8
-  __DATA.__objc_selrefs: 0x10c8
+  __DATA.__objc_const: 0xc270
+  __DATA.__objc_selrefs: 0x10d8
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x2498
-  __DATA.__data: 0xe8d8
-  __DATA.__objc_stublist: 0x78
-  __DATA.__bss: 0xe280
-  __DATA.__common: 0x3a8
+  __DATA.__objc_data: 0x2418
+  __DATA.__data: 0xe958
+  __DATA.__objc_stublist: 0x70
+  __DATA.__bss: 0xe180
+  __DATA.__common: 0x398
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8202
-  Symbols:   1079
-  CStrings:  2992
+  Functions: 8206
+  Symbols:   1080
+  CStrings:  3017
 
Symbols:
+ _$s18AAAFoundationSwift22AAFTimedAnalyticsEventCMa
+ _$sSo7NSErrorCs5Error10FoundationMc
+ _$ss24_getErrorEmbeddedNSErroryyXlSgxs0B0RzlF
+ _kAACustodianInviteEvent
- _$sSD6ValuesVMn
- _$sSo17OS_dispatch_groupC8DispatchE4waityyF
- _OBJC_CLASS_$_AAURLConfiguration
CStrings:
+ "    %s - escrow record check failed with error     %@"
+ "    %s - unrecoverable escrow record,     incremented failure count to: %ld"
+ "    %s - unrecoverable escrow record, number of previous     failures: %@"
+ "%s - isError31WithUnderlyingError9: %{bool}d"
+ "%s - isError31WithUnderlyingError9: false"
+ "%s - isMissingCRK: %{bool}d"
+ "%s - isUntrustedCRK: %{bool}d"
+ "%s - unrecoverable escrow record and failure count is missing... default to 1"
+ "%s - unrecoverable escrow record detected more than once for ADP user, proceeding to verify passcode scenario"
+ "%s recordID:%s one-off record fetch"
+ "%s recordID:%s one-off record fetch failed %@"
+ "%s recordID:%s one-off record fetch success newRecordID: %s"
+ "CKError Unknown Item while removing custodian. Continuing to update local record."
+ "Conflict while saving BenefactorInfoRecord : %s"
+ "Continuing to Remove CRK on OT"
+ "Custodian %s Calling setup finalization"
+ "Custodian %s IdMS status is unknown, Investigate."
+ "Custodian %s Setup finalization finished Successfully"
+ "Custodian %s Setup finalization finished with error: %@"
+ "Custodian %s is already known to IdMS and accepted"
+ "Custodian successfully fetched!. Updating status as %ld"
+ "Delete error is CK Unknown Item"
+ "Deleted Custodianship records for %s"
+ "Deleting Custodianship records for %s"
+ "Error cleaning up declined custodians %@"
+ "Error deleting %s from LocalCache: %@"
+ "Error deleting custodianship records for %s %@"
+ "Error deleting record at %s from LocalCache: %@"
+ "Error fetching records from %s: %@"
+ "Error removing CRK for custodianID: %s %@"
+ "Error removing CRK for otPeerID:%s for custodian:%s %@"
+ "Fetching User Information finished successfully."
+ "Fetching stored BenefactorInfoRecord with beneficiaryID: %s handle: %s recordID: %s status: %ld"
+ "LCInvite: Feature flag is enabled. Checking if handle:%s is a family member."
+ "LCInvite: Feature flag not enabled"
+ "LCInvite: The invitation was not pending. Must have been accepted or declined already. Returning without accepting."
+ "Local record update failed with error %@. Continuing to process decline status."
+ "Local record updated. Continuing to process decline status."
+ "Preflight error other than repairable errors: %@"
+ "Removing CRK for custodianID: %s"
+ "Removing CRK for otPeerID:%s for custodian:%s"
+ "RepairCustodians: 1/2 Finished repairing custodians: %s with error: %@"
+ "RepairCustodians: 1/2 Repairing custodians %s"
+ "RepairCustodians: 2/2 Finished preflight"
+ "RepairCustodians: 2/2 Starting preflight"
+ "RepairCustodians: Nothing to repair"
+ "Revoke from IdMS %s"
+ "Saving BenefactorInfoRecord %s in manatee? %{bool}d isFamilyMember? %{bool}d with status %ld"
+ "Saving BenefactorInfoRecord %s in manatee? %{bool}d with status %ld"
+ "Skipping Custodian Preflight TTR: hasAtLeastOneNewInvalidCRK:%{bool}d,\nhasOctagonMissingKeysError:%{bool}d,\nhasOctagonUntrustedKeysError:%{bool}d"
+ "Success removing CRK for custodianID: %s"
+ "Success removing CRK for otPeerID:%s for custodian:%s"
+ "Successfully fetched BenefactorInfoRecord with beneficiaryID: %s handle: %s recordID: %s status: %ld"
+ "TrustedPeersHelper.RecoveryKey.Error"
+ "Trying to fetch BenefactorInfoRecord from Server"
+ "Trying to grab Server Record from returned Error"
+ "User information did not return any custodian statuses"
+ "_TtC13appleaccountd17DaemonMessageUtil"
+ "_TtC13appleaccountd7CAEvent"
+ "aafTimedAnalyticsEvent"
+ "com.apple.aa.custodian.remove"
+ "eventName"
+ "informCustodianOfRemoval success"
+ "initWithBenefactorInfo:"
+ "initialData"
+ "inviteAction"
+ "isLCInviteAcceptanceEnabled"
+ "messageUtil"
+ "numOfRelation"
+ "pendingError"
+ "pendingIneligible"
+ "pendingNoManatee"
+ "pendingNonFamily"
+ "repairCustodians:completion:"
+ "ttr-cfgs isCustodianPreflightTTREnabledForUnusableCRK %{bool}d"
+ "ttr-cfgs normalized ttrFrequencyForCustodianUnusableCRK: %ld RandomNumber: %ld"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "version"
- "    %s - escrow record check failed,     incremented failure count to: %ld"
- "    %s - escrow record check failed, number of previous     failures: %@"
- "%s - escrow record check failed and failure count is missing... default to 1"
- "%s - escrow record check failed more than once for ADP user, proceeding to verify passcode scenario"
- "Asked to terminate an ineligible device CFU session that was already terminated or not found: %s"
- "Calling setup finalization"
- "Custodian IdMS status is unknown, Investigate."
- "Custodian is already known to IdMS and accepted"
- "Custodian successfully fetched!"
- "Custodianship records for %s deleted"
- "Dismissing any active CFU for: %s"
- "Error deleting custodianship records %@"
- "Error deleting record from LocalCache: %@"
- "Error fetching custodians for cleanup: %@"
- "Error fetching records from LocalCache: %@"
- "Failed to post Legacy Contact Invitation sent to Ineligible Device CFU. Error: %@"
- "Found existing ineligible device CFU session for ID: %s"
- "Generating new ineligible device CFU session for ID: %s, durationToPost: %ld"
- "Ineligible device replied auto-reject, and we intercepted, but will not post CFU because duration=0"
- "Invitation To Ineligible Device CFU Transaction already terminated, cannot terminate again"
- "Posting Legacy Contact Invitation sent to Ineligible Device CFU..."
- "Preflight error other than error 34 or error 32: %@"
- "RepairCustodians: 1/3 Removed unwanted custodians"
- "RepairCustodians: 1/3 Removing unwanted custodians"
- "RepairCustodians: 2/3 Finished repairing custodians: %s with error: %@"
- "RepairCustodians: 2/3 No custodians to repair"
- "RepairCustodians: 2/3 Repairing custodians %s"
- "RepairCustodians: 3/3 Finished preflight"
- "RepairCustodians: 3/3 Starting preflight"
- "RepairCustodians: Failed to Remove custodian:%s"
- "RepairCustodians: Found custodian(s) in both retain as well as remove arrays. %s"
- "RepairCustodians: Nothing to repair or remove"
- "RepairCustodians: Removed custodian:%s"
- "RepairCustodians: Removing custodian:%s"
- "Saving BenefactorInfoRecord %s in manatee? %{bool}d"
- "Setup finalization finished Successfully"
- "Setup finalization finished with error: %@"
- "Skipping Custodian Preflight TTR: hasAtLeastOneNewInvalidCRK:%{bool}d,\nhasError34:%{bool}d,\nhasError32:%{bool}d"
- "Successfully posted Legacy Contact Invitation sent to Ineligible Device CFU."
- "Terminating ineligible device CFU session with ID: %s"
- "User information fetching failed with error %@"
- "_TtC13appleaccountd29CustodianInviteAnalyticsEvent"
- "_TtC13appleaccountd35InvitationToIneligibleDeviceSession"
- "_TtC13appleaccountd42InvitationToIneligibleDeviceSessionManager"
- "appleaccountd.CustodianInviteAnalyticsEvent"
- "beneficiaryDurationBeforeNotSetupCFU"
- "cleanupDispatchGroup"
- "com.apple.aa.ineligible-device-invitation-"
- "com.apple.aa.ineligibledeviceinvitation-sessionmanager"
- "com.apple.appleaccount.CustodianInviteEvent"
- "initWithBenefactorName:handle:"
- "recipientHandle"
- "ttr-cfgs isCustodianPreflightTTREnabledForError34 %{bool}d"
- "ttr-cfgs normalized ttrFrequencyForCustodianError34: %ld RandomNumber: %ld"

```
