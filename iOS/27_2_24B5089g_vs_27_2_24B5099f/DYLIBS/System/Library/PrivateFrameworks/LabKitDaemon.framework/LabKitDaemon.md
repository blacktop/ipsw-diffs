## LabKitDaemon

> `/System/Library/PrivateFrameworks/LabKitDaemon.framework/LabKitDaemon`

```diff

-7027.1.45.2.4
-  __TEXT.__text: 0x57f2c
-  __TEXT.__objc_methlist: 0xb2c
-  __TEXT.__const: 0x1084
-  __TEXT.__constg_swiftt: 0x4f8
-  __TEXT.__swift5_typeref: 0x7aa
-  __TEXT.__swift5_reflstr: 0x514
-  __TEXT.__swift5_fieldmd: 0x57c
+7027.1.54.2.3
+  __TEXT.__text: 0x5ea5c
+  __TEXT.__objc_methlist: 0xbb4
+  __TEXT.__const: 0x1114
+  __TEXT.__constg_swiftt: 0x500
+  __TEXT.__swift5_typeref: 0x7e0
+  __TEXT.__swift5_reflstr: 0x5a4
+  __TEXT.__swift5_fieldmd: 0x5b8
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_proto: 0x90
   __TEXT.__swift5_types: 0x58
-  __TEXT.__cstring: 0x1ed6
-  __TEXT.__oslogstring: 0x1888
-  __TEXT.__swift5_capture: 0xaac
-  __TEXT.__swift_as_entry: 0xb4
-  __TEXT.__swift_as_ret: 0x80
-  __TEXT.__swift_as_cont: 0x1fc
+  __TEXT.__cstring: 0x1f76
+  __TEXT.__oslogstring: 0x1a98
+  __TEXT.__swift5_capture: 0xb78
+  __TEXT.__swift_as_entry: 0xc4
+  __TEXT.__swift_as_ret: 0x8c
+  __TEXT.__swift_as_cont: 0x214
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1418
-  __TEXT.__eh_frame: 0x27e8
+  __TEXT.__unwind_info: 0x1550
+  __TEXT.__eh_frame: 0x2b00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x960
-  __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__got: 0x410
-  __AUTH_CONST.__const: 0x2fa8
-  __AUTH_CONST.__objc_const: 0xfb0
-  __AUTH_CONST.__auth_got: 0xd98
-  __AUTH.__objc_data: 0x558
+  __DATA_CONST.__objc_selrefs: 0x9e8
+  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__got: 0x468
+  __AUTH_CONST.__const: 0x3200
+  __AUTH_CONST.__objc_const: 0x10b8
+  __AUTH_CONST.__auth_got: 0xdc8
+  __AUTH.__objc_data: 0x580
   __AUTH.__data: 0x268
-  __DATA.__data: 0xba8
+  __DATA.__data: 0xca8
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x398
   __DATA_DIRTY.__data: 0x1a0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1320
-  Symbols:   624
-  CStrings:  219
+  Functions: 1400
+  Symbols:   638
+  CStrings:  232
 
Symbols:
+ _HDClinicalAccountEntityPropertyIdentifier
+ _HDClinicalDeletedAccountEntityPropertySyncIdentifier
+ _OBJC_CLASS_$_HDClinicalDeletedAccountEntity
+ _OBJC_CLASS_$_HDNewMedicalRecordsCounts
+ _OBJC_CLASS_$_HKMedicalType
+ __OBJC_$_INSTANCE_METHODS__TtC12LabKitDaemon13LabSHLManager(LabKitDaemon|LabKitDaemon1|LabKitDaemon2)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDCloudSyncManagerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDCloudSyncManagerObserver
+ __OBJC_$_PROTOCOL_REFS_HDCloudSyncManagerObserver
+ __OBJC_CLASS_PROTOCOLS_$__TtC12LabKitDaemon13LabSHLManager(LabKitDaemon|LabKitDaemon1|LabKitDaemon2)
+ __OBJC_LABEL_PROTOCOL_$_HDCloudSyncManagerObserver
+ __OBJC_PROTOCOL_$_HDCloudSyncManagerObserver
+ ___swift_closure_destructor.14Tm
+ ___swift_closure_destructorTm
+ _symbolic Say_____G 10Foundation4UUIDV
+ _symbolic _____yShy_____GG 2os21OSAllocatedUnfairLockV 10Foundation4UUIDV
+ _symbolic _____yShy_____y_____SSGGG 2os21OSAllocatedUnfairLockV 15HealthUtilities15TypedIdentifierV 0E14RecordServices15LaboratoryOrderV
- __OBJC_$_INSTANCE_METHODS__TtC12LabKitDaemon13LabSHLManager(LabKitDaemon|LabKitDaemon1)
- __OBJC_CLASS_PROTOCOLS_$__TtC12LabKitDaemon13LabSHLManager(LabKitDaemon|LabKitDaemon1)
- ___swift_project_boxed_opaque_existential_0Tm
CStrings:
+ "AND sync_provenance = "
+ "Failed to fetch orders with unstored SHLs: %@"
+ "Failed to remove orders for deleted clinical accounts: %@"
+ "LabNotifyForNewMedicalRecords"
+ "LabRefreshOrdersMissingSHL"
+ "SELECT item_uuid FROM "
+ "Unable to find health records profile extension, skipping SHL storage for %ld unlinked order(s)"
+ "[%s]: Failed to fetch fulfilled orders missing an SHL: %@"
+ "[%s]: Failed to fetch lab orders for account %{public}s: %@"
+ "[%s]: Failed to post new medical records notification with error: %@"
+ "[%s]: Refreshing %{public}ld fulfilled order(s) missing an SHL"
+ "[%s]: Sending results ready notification"
+ "[%s]: account %{public}s is linked to lab order(s) %s"
+ "[%s]: didCreateNewMedicalRecordsFor account `%s` with %ld new and %ld updated record(s) across %ld medical record type(s)"
+ "[%s]: no lab order is linked to account %{public}s"
+ "com.apple.Health.Labs.ResultsReady"
- "[%s]: Failed to post new medical records notification for account %{public}s with error: %@"
- "[%s]: Sending notificaton for account %{public}s"
- "[%s]: didCreateNewMedicalRecordsForAccountIdentifier `%s` and healthLinkIdentifier `%s`"
```
