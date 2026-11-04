## appleaccountd

> `/usr/libexec/appleaccountd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_stublist`

```diff

-1069.125.7.0.0
-  __TEXT.__text: 0x3cf880
-  __TEXT.__auth_stubs: 0x3800
+1069.250.3.0.0
+  __TEXT.__text: 0x3e474c
+  __TEXT.__auth_stubs: 0x3820
   __TEXT.__objc_stubs: 0x4de0
-  __TEXT.__objc_methlist: 0xf80
-  __TEXT.__objc_methname: 0x78b5
-  __TEXT.__objc_classname: 0x2e9d
-  __TEXT.__cstring: 0x46a9
-  __TEXT.__objc_methtype: 0x2044
+  __TEXT.__objc_methlist: 0xfc8
+  __TEXT.__objc_methname: 0x7a85
+  __TEXT.__objc_classname: 0x2ecd
+  __TEXT.__cstring: 0x47a9
+  __TEXT.__objc_methtype: 0x2184
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x133b0
-  __TEXT.__constg_swiftt: 0xc680
-  __TEXT.__swift5_typeref: 0x79eb
+  __TEXT.__const: 0x135f0
+  __TEXT.__constg_swiftt: 0xc7e0
+  __TEXT.__swift5_typeref: 0x7ae5
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_reflstr: 0x66d5
-  __TEXT.__swift5_fieldmd: 0x66a0
+  __TEXT.__swift5_reflstr: 0x6867
+  __TEXT.__swift5_fieldmd: 0x67a0
   __TEXT.__swift5_assocty: 0x938
-  __TEXT.__swift5_proto: 0xc68
-  __TEXT.__swift5_types: 0x63c
-  __TEXT.__swift5_capture: 0x66a4
-  __TEXT.__oslogstring: 0x212dd
-  __TEXT.__swift5_protos: 0x22c
-  __TEXT.__swift_as_entry: 0x680
-  __TEXT.__swift_as_ret: 0x88c
-  __TEXT.__swift_as_cont: 0x11d8
+  __TEXT.__swift5_proto: 0xc74
+  __TEXT.__swift5_types: 0x644
+  __TEXT.__swift5_capture: 0x6818
+  __TEXT.__oslogstring: 0x218bd
+  __TEXT.__swift5_protos: 0x234
+  __TEXT.__swift_as_entry: 0x6bc
+  __TEXT.__swift_as_ret: 0x8f0
+  __TEXT.__swift_as_cont: 0x12cc
   __TEXT.__swift5_acfuncs: 0xb4
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xa320
-  __TEXT.__eh_frame: 0x1488c
-  __DATA_CONST.__const: 0x14048
-  __DATA_CONST.__objc_classlist: 0x600
+  __TEXT.__unwind_info: 0xa698
+  __TEXT.__eh_frame: 0x155b0
+  __DATA_CONST.__const: 0x14308
+  __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x1c08
-  __DATA_CONST.__got: 0x1568
-  __DATA_CONST.__auth_ptr: 0x16a0
-  __DATA.__objc_const: 0x1e170
-  __DATA.__objc_selrefs: 0x1748
+  __DATA_CONST.__auth_got: 0x1c18
+  __DATA_CONST.__got: 0x1578
+  __DATA_CONST.__auth_ptr: 0x16d0
+  __DATA.__objc_const: 0x1e8d0
+  __DATA.__objc_selrefs: 0x1758
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x3360
-  __DATA.__data: 0x144a0
+  __DATA.__objc_data: 0x33c0
+  __DATA.__data: 0x145d0
   __DATA.__objc_stublist: 0x68
   __DATA.__common: 0x4e0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10282
-  Symbols:   1818
-  CStrings:  4214
+  Functions: 10453
+  Symbols:   1824
+  CStrings:  4253
 
Symbols:
+ _$s2os21OSAllocatedUnfairLockVMn
+ _$s8Dispatch0A3QoSV0B6SClassO7utilityyA2EmFWC
+ _$sSayxG8CloudKit21CKRecordValueProtocolA2bCRzlMc
+ _$sShMa
+ _$ss13ManagedBufferCMn
+ _$ss8DurationV7secondsyABSdFZ
CStrings:
+ "%s %s save returned no decodable record"
+ "%s recordID:%s one-off record fetch returned no decodable record"
+ "@\"NSUUID\"80@0:8@\"NSData\"16@\"NSArray\"24@\"NSString\"32@\"NSString\"40B48@\"NSSet\"52@\"NSSet\"60B68^@72"
+ "@80@0:8@16@24@32@40B48@52@60B68^@72"
+ "Check if expected states: %s contain local record state: %ld for recordID: %s"
+ "Error saving invitation after conflict: %@"
+ "Expected states: %s, but local record state: %ld for recordID: %s, shouldRefresh: %{bool}d"
+ "Failed to fetch custodians for delivered message %s, error: %@"
+ "Failed to save invitation delivery for custodianID: %s, error: %@"
+ "Invitation %s was delivered before its identifier was saved, custodianID: %s"
+ "Invitation %s was delivered, custodianID: %s"
+ "Invitation conflict: keeping server status %ld, local status was %ld"
+ "Invitation conflict: upgrading server status pending to accepted after family auto-accept"
+ "Message with description %s and identifier %s sent successfully to %@!"
+ "No custodian invitation found for delivered message %s, keeping it for a later invitationSent"
+ "No custodian record to update invitation delivery, custodianID: %s"
+ "Owner finalize before verdict failed for custodianID: %s, error: %@"
+ "Owner invitation was not delivered to any contact device, custodianID: %s"
+ "Owner setup is invited on server past grace period, finalizing before verdict, custodianID: %s"
+ "Owner setup is still invited on server after finalize, deferring verdict, custodianID: %s"
+ "Record state(%ld) is not in expected states(%s) after refreshing for recordID: %s"
+ "RemoteUITermsMigration"
+ "Repair-count config read from URL bag failed: %@. Continuing with the compiled default."
+ "Unrecognized IdMS custodian status: %{public}s, custodianID: %s"
+ "UrlBagProvider - maxRepairCountV2 absent from urlbag; defaulting to %ld."
+ "UrlBagProvider - maxRepairCountV2 has unexpected type %s; defaulting to %ld."
+ "_TtC13appleaccountd25InvitationDeliveryTracker"
+ "beginTransaction"
+ "com.apple.aa.custodian.invitation-sent"
+ "com.apple.appleaccountd.custodian.invitation-delivered"
+ "com.apple.appleaccountd.custodian.message."
+ "containerStore"
+ "earlyDeliveries"
+ "invitationDeliveredDate"
+ "invitationDeliveryTracker"
+ "invitationMessageIDs"
+ "maxRepairCountV2"
+ "messageService:didDeliverMessageWithIdentifier:"
+ "messageService:didReceiveMessage:fromID:sentToHandleUri:completion:"
+ "process(_:from:completion:)"
+ "save-invitation: retry %ld in %f s after transient error: %@"
+ "sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:wantsDeliveryAcknowledgement:error:"
+ "telemetryRecorder"
+ "unsavedInvitations"
+ "v32@0:8@\"<AAIDSMessagingService>\"16@\"NSUUID\"24"
+ "v56@0:8@\"<AAIDSMessagingService>\"16@\"NSData\"24@\"NSString\"32@\"NSString\"40@?<v@?>48"
+ "v56@0:8@16@24@32@40@?48"
- "Check if expected state: %s == local record state: %ld for recordID: %s"
- "DecoupleOTPeerID"
- "Expected state: %ld, but local record state: %ld for recordID: %s, shouldRefresh: %{bool}d"
- "Message with description %s sent successfully to %@!"
- "Record state(%ld) does not matches expected state(%ld) after refreshing for recordID: %s"
- "Using Health Check interval - One Week"
- "maxRepairCount"
- "process(_:from:)"
```
