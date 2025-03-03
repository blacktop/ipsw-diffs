## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1007.456.0.0.0
-  __TEXT.__text: 0x286650
-  __TEXT.__auth_stubs: 0x2740
-  __TEXT.__objc_methlist: 0xe00
-  __TEXT.__objc_methname: 0x4410
+1007.457.0.0.0
+  __TEXT.__text: 0x2d557c
+  __TEXT.__auth_stubs: 0x2730
+  __TEXT.__objc_methlist: 0xe10
+  __TEXT.__objc_methname: 0x4485
   __TEXT.__objc_classname: 0x20a
   __TEXT.__objc_methtype: 0x1525
-  __TEXT.__cstring: 0x82c4
-  __TEXT.__swift5_typeref: 0x5fc3
+  __TEXT.__cstring: 0x8494
+  __TEXT.__swift5_typeref: 0x612d
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xc55c
-  __TEXT.__constg_swiftt: 0xa2f8
-  __TEXT.__swift5_reflstr: 0x52d4
-  __TEXT.__swift5_fieldmd: 0x51c4
+  __TEXT.__const: 0xc70c
+  __TEXT.__constg_swiftt: 0xa630
+  __TEXT.__swift5_reflstr: 0x5404
+  __TEXT.__swift5_fieldmd: 0x52c4
   __TEXT.__swift5_builtin: 0x1e0
   __TEXT.__swift5_assocty: 0x698
-  __TEXT.__swift5_proto: 0x988
-  __TEXT.__swift5_types: 0x4cc
-  __TEXT.__oslogstring: 0x16e46
-  __TEXT.__swift_as_entry: 0x228
-  __TEXT.__swift_as_ret: 0x2a4
-  __TEXT.__swift5_protos: 0x1d4
-  __TEXT.__swift5_capture: 0x58e0
+  __TEXT.__swift5_proto: 0x998
+  __TEXT.__swift5_types: 0x4dc
+  __TEXT.__oslogstring: 0x172e6
+  __TEXT.__swift_as_entry: 0x254
+  __TEXT.__swift_as_ret: 0x2dc
+  __TEXT.__swift5_protos: 0x1e0
+  __TEXT.__swift5_capture: 0x5964
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5868
-  __TEXT.__eh_frame: 0x8530
-  __DATA_CONST.__auth_got: 0x13a0
-  __DATA_CONST.__got: 0xe58
-  __DATA_CONST.__auth_ptr: 0x12a8
-  __DATA_CONST.__const: 0x10c10
-  __DATA_CONST.__objc_classlist: 0x4e0
+  __TEXT.__unwind_info: 0x5928
+  __TEXT.__eh_frame: 0x8ed8
+  __DATA_CONST.__auth_got: 0x1398
+  __DATA_CONST.__got: 0xe68
+  __DATA_CONST.__auth_ptr: 0x1f00
+  __DATA_CONST.__const: 0x10d80
+  __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x184f8
-  __DATA.__objc_selrefs: 0x13c8
+  __DATA.__objc_const: 0x187c0
+  __DATA.__objc_selrefs: 0x13e8
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x29e8
-  __DATA.__data: 0x107c0
+  __DATA.__objc_data: 0x2ba8
+  __DATA.__data: 0x10d50
   __DATA.__objc_stublist: 0x68
   __DATA.__bss: 0xe800
-  __DATA.__common: 0x398
+  __DATA.__common: 0x3b0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7763
-  Symbols:   1275
-  CStrings:  3338
+  Functions: 7860
+  Symbols:   1276
+  CStrings:  3372
 
Symbols:
+ _$sScG8IteratorV4next9isolationxSgScA_pSgYi_tYaF
+ _$sScG8IteratorV4next9isolationxSgScA_pSgYi_tYaFTu
+ _AAFollowUpIdentifierChildProtoConnect
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
- _objc_retain_x1
- _objc_retain_x3
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
CStrings:
+ "Cleared follow up for child connect with success: %{bool}d"
+ "Custodian Preflight Silent TTR launched successfully."
+ "Encountered error while clearing follow up: %@"
+ "Failed fetch proto account type"
+ "Failed to fetch proto account: %@"
+ "Failed to remove proto account: %@"
+ "Finished all Maintenance Activities."
+ "Lost reference to self. Aborting XPC activity for Maintenance Activities"
+ "Maintenance Activity - %s failed %@"
+ "Maintenance Activity - %s succeeded."
+ "Maintenance Activity - Starting grouped tasks"
+ "MaintenanceActivityProvider - Maintenance succeeded."
+ "MaintenanceActivityProvider - Overall Maintenance Activities failed: %s"
+ "MaintenanceActivityProvider - Performing maintenance..."
+ "No primary Apple Account account found, skipping cleanup."
+ "ProtoAccountCleanupController - Found a protoaccount. Removing it."
+ "ProtoAccountCleanupController - No proto account found. Checking for followups"
+ "ProtoAccountCleanupController - Proto account removal failed: %@, trying again."
+ "Recovery Contact Preflight Failed"
+ "Removed proto account with success: %{bool}d"
+ "Unable to launch Silent TTR due to error: %@"
+ "_TtC13appleaccountd19ProtoAccountManager"
+ "_TtC13appleaccountd27MaintenanceActivityProvider"
+ "_TtC13appleaccountd27ProtoAccountCleanupActivity"
+ "_TtC13appleaccountd28MaintenanceActivityScheduler"
+ "_protoAccountManager"
+ "accountsWithAccountTypeIdentifiers:completion:"
+ "com.apple.appleaccountd.maintenance"
+ "identifier"
+ "maintenanceActivityScheduler"
+ "protoAccountManager"
+ "protoAccountType"
+ "removeChildConnectFollowUp()"
+ "removeChildConnectFollowUpWithCompletion:"

```
