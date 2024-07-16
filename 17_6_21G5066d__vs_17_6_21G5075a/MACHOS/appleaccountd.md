## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-981.21.0.0.0
-  __TEXT.__text: 0x26f840
+981.23.0.0.0
+  __TEXT.__text: 0x272ee0
   __TEXT.__auth_stubs: 0x2300
   __TEXT.__objc_methlist: 0x620
-  __TEXT.__objc_methname: 0x3d0b
+  __TEXT.__objc_methname: 0x3cfb
   __TEXT.__objc_classname: 0x1e0
   __TEXT.__objc_methtype: 0x1261
-  __TEXT.__cstring: 0x1c0d4
-  __TEXT.__swift5_typeref: 0x5a83
+  __TEXT.__cstring: 0x1c044
+  __TEXT.__swift5_typeref: 0x5a09
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xb810
-  __TEXT.__constg_swiftt: 0x9034
-  __TEXT.__swift5_reflstr: 0x4944
-  __TEXT.__swift5_fieldmd: 0x4c00
+  __TEXT.__const: 0xb6c0
+  __TEXT.__constg_swiftt: 0x8f24
+  __TEXT.__swift5_reflstr: 0x4914
+  __TEXT.__swift5_fieldmd: 0x4b88
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_assocty: 0x5a8
-  __TEXT.__swift5_proto: 0x930
-  __TEXT.__swift5_types: 0x490
-  __TEXT.__swift5_protos: 0x1c0
-  __TEXT.__swift5_capture: 0x4ba4
+  __TEXT.__swift5_proto: 0x924
+  __TEXT.__swift5_types: 0x48c
+  __TEXT.__swift5_protos: 0x1b8
+  __TEXT.__swift5_capture: 0x4c4c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__info_plist: 0x814
-  __TEXT.__unwind_info: 0x57ec
-  __TEXT.__eh_frame: 0x5428
+  __TEXT.__unwind_info: 0x5a80
+  __TEXT.__eh_frame: 0x5688
   __DATA_CONST.__auth_got: 0x1180
   __DATA_CONST.__got: 0x730
-  __DATA_CONST.__auth_ptr: 0x440
-  __DATA_CONST.__const: 0x13480
-  __DATA_CONST.__objc_classlist: 0x4c0
+  __DATA_CONST.__auth_ptr: 0x430
+  __DATA_CONST.__const: 0x13490
+  __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_classrefs: 0x418
+  __DATA_CONST.__objc_classrefs: 0x410
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xc388
+  __DATA.__objc_const: 0xc270
   __DATA.__objc_selrefs: 0x10d8
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x2468
-  __DATA.__data: 0xea78
+  __DATA.__objc_data: 0x2418
+  __DATA.__data: 0xe958
   __DATA.__objc_stublist: 0x70
-  __DATA.__bss: 0xe280
-  __DATA.__common: 0x3b8
+  __DATA.__bss: 0xe180
+  __DATA.__common: 0x398
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8201
-  Symbols:   1081
-  CStrings:  3017
+  Functions: 8206
+  Symbols:   1080
+  CStrings:  3016
 
Symbols:
- _OBJC_CLASS_$_AAURLConfiguration
CStrings:
+ "%!s(MISSING) recordID:%!s(MISSING) one-off record fetch"
+ "%!s(MISSING) recordID:%!s(MISSING) one-off record fetch failed %!@(MISSING)"
+ "%!s(MISSING) recordID:%!s(MISSING) one-off record fetch success newRecordID: %!s(MISSING)"
+ "Conflict while saving BenefactorInfoRecord : %!s(MISSING)"
+ "Fetching stored BenefactorInfoRecord with beneficiaryID: %!s(MISSING) handle: %!s(MISSING) recordID: %!s(MISSING) status: %!l(MISSING)d"
+ "LCInvite: Feature flag is enabled. Checking if handle:%!s(MISSING) is a family member."
+ "LCInvite: Feature flag not enabled"
+ "LCInvite: The invitation was not pending. Must have been accepted or declined already. Returning without accepting."
+ "Saving BenefactorInfoRecord %!s(MISSING) in manatee? %!{(MISSING)bool}d isFamilyMember? %!{(MISSING)bool}d with status %!l(MISSING)d"
+ "Saving BenefactorInfoRecord %!s(MISSING) in manatee? %!{(MISSING)bool}d with status %!l(MISSING)d"
+ "Successfully fetched BenefactorInfoRecord with beneficiaryID: %!s(MISSING) handle: %!s(MISSING) recordID: %!s(MISSING) status: %!l(MISSING)d"
+ "Trying to fetch BenefactorInfoRecord from Server"
+ "Trying to grab Server Record from returned Error"
+ "_TtC13appleaccountd17DaemonMessageUtil"
+ "initWithBenefactorInfo:"
+ "isLCInviteAcceptanceEnabled"
+ "messageUtil"
- "Asked to terminate an ineligible device CFU session that was already terminated or not found: %!s(MISSING)"
- "Dismissing any active CFU for: %!s(MISSING)"
- "Failed to post Legacy Contact Invitation sent to Ineligible Device CFU. Error: %!@(MISSING)"
- "Found existing ineligible device CFU session for ID: %!s(MISSING)"
- "Generating new ineligible device CFU session for ID: %!s(MISSING), durationToPost: %!l(MISSING)d"
- "Ineligible device replied auto-reject, and we intercepted, but will not post CFU because duration=0"
- "Invitation To Ineligible Device CFU Transaction already terminated, cannot terminate again"
- "Posting Legacy Contact Invitation sent to Ineligible Device CFU..."
- "Saving BenefactorInfoRecord %!s(MISSING) in manatee? %!{(MISSING)bool}d"
- "Successfully posted Legacy Contact Invitation sent to Ineligible Device CFU."
- "Terminating ineligible device CFU session with ID: %!s(MISSING)"
- "_TtC13appleaccountd35InvitationToIneligibleDeviceSession"
- "_TtC13appleaccountd42InvitationToIneligibleDeviceSessionManager"
- "beneficiaryDurationBeforeNotSetupCFU"
- "com.apple.aa.ineligible-device-invitation-"
- "com.apple.aa.ineligibledeviceinvitation-sessionmanager"
- "initWithBenefactorName:handle:"
- "recipientHandle"

```
