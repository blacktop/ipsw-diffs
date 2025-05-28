## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-981.12.0.0.0
-  __TEXT.__text: 0x2658c4
-  __TEXT.__auth_stubs: 0x22b0
+981.20.0.0.0
+  __TEXT.__text: 0x26a744
+  __TEXT.__auth_stubs: 0x22f0
   __TEXT.__objc_methlist: 0x618
-  __TEXT.__objc_methname: 0x3c7e
+  __TEXT.__objc_methname: 0x3cdd
   __TEXT.__objc_classname: 0x1e0
   __TEXT.__objc_methtype: 0x123a
-  __TEXT.__cstring: 0x1bb24
-  __TEXT.__swift5_typeref: 0x59f7
+  __TEXT.__cstring: 0x1bd34
+  __TEXT.__swift5_typeref: 0x5a2d
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xb770
-  __TEXT.__constg_swiftt: 0x8e48
-  __TEXT.__swift5_reflstr: 0x47e4
-  __TEXT.__swift5_fieldmd: 0x4ad4
+  __TEXT.__const: 0xb7c0
+  __TEXT.__constg_swiftt: 0x8eb0
+  __TEXT.__swift5_reflstr: 0x4894
+  __TEXT.__swift5_fieldmd: 0x4b68
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_assocty: 0x5a8
-  __TEXT.__swift5_proto: 0x924
+  __TEXT.__swift5_proto: 0x928
   __TEXT.__swift5_types: 0x490
-  __TEXT.__swift5_protos: 0x1b4
-  __TEXT.__swift5_capture: 0x4aec
+  __TEXT.__swift5_protos: 0x1b8
+  __TEXT.__swift5_capture: 0x4b94
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x56d0
-  __TEXT.__eh_frame: 0x5290
-  __DATA_CONST.__auth_got: 0x1158
-  __DATA_CONST.__got: 0x710
-  __DATA_CONST.__auth_ptr: 0x420
-  __DATA_CONST.__const: 0x13310
+  __TEXT.__unwind_info: 0x57e4
+  __TEXT.__eh_frame: 0x5440
+  __DATA_CONST.__auth_got: 0x1178
+  __DATA_CONST.__got: 0x720
+  __DATA_CONST.__auth_ptr: 0x428
+  __DATA_CONST.__const: 0x13480
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_classrefs: 0x410
+  __DATA_CONST.__objc_classrefs: 0x418
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xbf48
-  __DATA.__objc_selrefs: 0x10a0
+  __DATA.__objc_const: 0xbfa8
+  __DATA.__objc_selrefs: 0x10c8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x2498
-  __DATA.__data: 0xe830
+  __DATA.__data: 0xe8d8
   __DATA.__objc_stublist: 0x78
   __DATA.__bss: 0xe280
-  __DATA.__common: 0x3a0
+  __DATA.__common: 0x3a8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage
   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreML.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftVision.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8177
-  Symbols:   1066
-  CStrings:  2976
+  Functions: 8202
+  Symbols:   1079
+  CStrings:  2992
 
Symbols:
+ _$s10Foundation12CharacterSetV12charactersInACSSh_tcfC
+ _$sSo8NSStringC10FoundationE13stringLiteralABs12StaticStringV_tcfC
+ _$sSy10FoundationE10components11separatedBySaySSGAA12CharacterSetV_tF
+ _AAPrefsDomain
+ _CFPreferencesCopyAppValue
+ _OBJC_CLASS_$_AAFKeybagLockAssertion
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftVision
+ _kAAAnalyticsADPCohortType
CStrings:
+ "\n recordBuildVersion: "
+ "%s - Checking if pending custodian review follow up needs to be dismissed for custodians: %s"
+ "%s - Failed to attach ADP cohort type, account nil"
+ "%s - Failed to attach ADP cohort type, cohort nil"
+ "%s - custodian %s recordBuildVersion could not be updated. %@"
+ "%s - custodian %s recordBuildVersion updated."
+ "%s Account is nil. Not reporting Post Repair CFU Event."
+ "%s CRK exists on OT? %{bool}d error: %@"
+ "%s CRK repair successful. Proceeding to refetch records to preflight"
+ "%s Current Key: %s Bool: %{bool}d"
+ "%s Error repairing CRK."
+ "%s Event creation failed. Not reporting Post Repair CFU Event."
+ "%s Mark as not reachable after failed CRK repair resulted in error %@. Ending preflight."
+ "%s Past Key: %s Bool: %{bool}d"
+ "%s Reporting Post Repair CFU Event %@"
+ "%s Successfully marked custodian as not reachable after failed CRK repair. Stopping preflight."
+ "%s hasAtLeastOneNewInvalidCRK: Returning %{bool}d."
+ "Beneficiary id %s is pending. Resending CK share..."
+ "Comparing handles from BenefactorInfoRecord: %s and IDS message: %s are same and not empty."
+ "Completed processing accepted status change. Error: %@"
+ "Completed processing declined status change. Error: %@"
+ "DismissCustodianReviewCFU"
+ "Dismissing"
+ "Finished sharing health record. Error: %@"
+ "No existing BenefactorInfoRecord found."
+ "Not Accepting CKShare from sender %s due to %@"
+ "Not dismissing"
+ "Reported Preflight Event successfully %@"
+ "Sent IDS Message for Inheritance Invitation successfully."
+ "Sent the IDS message for Inheritance Invitation successfully."
+ "Should Dismiss Custodian Review CFU: %s"
+ "adpCohortForAccount:"
+ "checkName"
+ "dictionary"
+ "encryptedValues"
+ "initWithWrappedRKC:wrappingKey:custodianUUID:recordBuildVersion:"
+ "invitation %s"
+ "invitationMessage %s"
+ "member-appleID-aliases"
+ "member-phone-numbers"
+ "recordBuildVersion"
+ "setRecordBuildVersion:"
+ "unlock"
+ "⛔️ Cannot proceed. Beneficiary handle does not match incoming message from: handle"
- "%s - Defaults repairWithoutTransparencyCFU is enabled. Repairing..."
- "%s - Dismissing pending custodian review follow up posted for custodians: %s"
- "Account is nil. Not reporting Post Repair CFU Event."
- "CRK repair successful. Proceeding to refetch records to preflight"
- "Can repair FeatureFlag (client+IdMS): %{bool}d"
- "Checking if Custodian %s is approved for repair "
- "Current Key: %s Bool: %{bool}d"
- "Custodian repair approval list is being set in UserDefaults: %s"
- "Custodian repair approval list is being updated in UserDefaults"
- "Defaults repairWithoutTransparencyCFU enabled: %{bool}d"
- "Error code is 32/34: %{bool}d"
- "Error repairing CRK."
- "Event creation failed. Not reporting Post Repair CFU Event."
- "Is custodian already approved for repair: %{bool}d"
- "LockAssertion not supported. Not locking"
- "LockAssertion not supported. Not unlocking."
- "Mark as not reachable after failed CRK repair resulted in error %@. Ending preflight."
- "Past Key: %s Bool: %{bool}d"
- "RepairCustodians: LockAssertion not supported. Not locking"
- "RepairCustodians: LockAssertion not supported. Not unlocking."
- "Reporting Post Repair CFU Event %@"
- "Successfully marked custodian as not reachable after failed CRK repair. Stopping preflight."
- "UUIDs to repair: %s"
- "approvedForRepair"
- "hasAtLeastOneNewInvalidCRK: Returning %{bool}d."
- "initWithCapabilityType:"
- "repairWithoutTransparencyCFU"
- "✅Repaired: %s"
- "❌Pending: %s"

```
