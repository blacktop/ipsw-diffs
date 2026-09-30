## remindd

> `/usr/libexec/remindd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_catlist2`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA.__objc_data`
- `__DATA.__objc_stublist`

```diff

-4076.0.0.0.0
-  __TEXT.__text: 0x7f4284
+4077.0.0.0.0
+  __TEXT.__text: 0x7f7b38
   __TEXT.__auth_stubs: 0x8ce0
-  __TEXT.__objc_stubs: 0x1bc40
-  __TEXT.__objc_methlist: 0xabc8
-  __TEXT.__const: 0x29518
-  __TEXT.__objc_methname: 0x28501
+  __TEXT.__objc_stubs: 0x1bc80
+  __TEXT.__objc_methlist: 0xac28
+  __TEXT.__const: 0x295b8
+  __TEXT.__objc_methname: 0x28611
   __TEXT.__objc_classname: 0x6406
-  __TEXT.__cstring: 0x18c97
+  __TEXT.__cstring: 0x18d97
   __TEXT.__objc_methtype: 0x43f7
   __TEXT.__gcc_except_tab: 0x20f0
-  __TEXT.__oslogstring: 0x61cd0
+  __TEXT.__oslogstring: 0x621f0
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x1453e
+  __TEXT.__swift5_typeref: 0x145d0
   __TEXT.__swift5_fieldmd: 0xa8a4
   __TEXT.__constg_swiftt: 0xd240
   __TEXT.__swift5_builtin: 0x3c0
   __TEXT.__swift5_reflstr: 0xc225
   __TEXT.__swift5_assocty: 0x1ee8
-  __TEXT.__swift5_capture: 0x63d0
+  __TEXT.__swift5_capture: 0x6458
   __TEXT.__swift5_protos: 0x2e4
   __TEXT.__swift5_proto: 0x192c
   __TEXT.__swift5_types: 0xb58

   __TEXT.__swift_as_ret: 0x22c
   __TEXT.__swift_as_cont: 0x46c
   __TEXT.__swift5_mpenum: 0xe0
-  __TEXT.__unwind_info: 0x14098
-  __TEXT.__eh_frame: 0x1fd38
-  __DATA_CONST.__const: 0x26530
+  __TEXT.__unwind_info: 0x140d8
+  __TEXT.__eh_frame: 0x1fdb0
+  __DATA_CONST.__const: 0x266c0
   __DATA_CONST.__cfstring: 0x5220
   __DATA_CONST.__objc_classlist: 0xc60
   __DATA_CONST.__objc_catlist: 0x110

   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__auth_got: 0x4680
-  __DATA_CONST.__got: 0x3598
-  __DATA_CONST.__auth_ptr: 0x28e0
-  __DATA.__objc_const: 0x1dfb0
-  __DATA.__objc_selrefs: 0x7cd8
+  __DATA_CONST.__got: 0x35a0
+  __DATA_CONST.__auth_ptr: 0x28e8
+  __DATA.__objc_const: 0x1dfc8
+  __DATA.__objc_selrefs: 0x7d00
   __DATA.__objc_ivar: 0x490
   __DATA.__objc_data: 0x87e8
-  __DATA.__data: 0x1f5a0
+  __DATA.__data: 0x1f5d0
   __DATA.__objc_stublist: 0x38
   __DATA.__common: 0xa00
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 22812
-  Symbols:   4299
-  CStrings:  11829
+  Functions: 22842
+  Symbols:   4300
+  CStrings:  11855
 
Symbols:
+ _$s19ReminderKitInternal15REMFeatureFlagsO27ckDeleteZoneAccountRecoveryyA2CmFWC
CStrings:
+ "No CK account persistent store found"
+ "Primary CK store has no URL"
+ "RDGroceryCategorizer: maximumResponseTokens: %ld"
+ "REMReminderStorageCDIngestor:applyDueDateDeltaAlertChanges: Collapsed duplicate existing early alerts {before: %ld, after: %ld, ids: %{public}s}"
+ "ckDeleteZone recovery: account re-initialized successfully"
+ "ckDeleteZone recovery: accountUtils is nil, cannot re-initialize accounts"
+ "ckDeleteZone recovery: cloudContext is nil, skipping server change token reset — data may not re-appear"
+ "ckDeleteZone recovery: resetting all CK server change tokens <rdar://181242487>"
+ "ckDeleteZone recovery: scheduling updateAccountsAndFetchMigrationState <rdar://181242487>"
+ "ckDeleteZone recovery: updateAccountsAndFetchMigrationState failed: %{public}@"
+ "com.apple.RDStoreController.ckDeleteZone.simulate"
+ "recoverAfterSimulatedZoneDeletion:"
+ "recoverAfterSimulatedZoneDeletion: triggerAccountsUpdateAfterZoneDeletion dispatched"
+ "setMetadata:forPersistentStoreOfType:URL:options:error:"
+ "simulateAccountStoreMarkedForDeletion:"
+ "simulateAccountStoreMarkedForDeletion: Marked store at %s — kill remindd to reproduce rdar://181242487"
+ "simulateLocalZoneDeletion"
+ "simulateLocalZoneDeletion: could not fetch primary CK account in simulation context"
+ "simulateLocalZoneDeletion: deleted %ld objects, triggerAccountsUpdateAfterZoneDeletion dispatched"
+ "simulateLocalZoneDeletion: deleting %ld child objects"
+ "simulateLocalZoneDeletion: failed: %@"
+ "simulateLocalZoneDeletion: failed: %s"
+ "simulateLocalZoneDeletion: no primary active CK account found"
+ "simulateLocalZoneDeletionAndRecover:"
+ "triggerAccountsUpdateAfterZoneDeletion"
+ "v24@0:8@?<v@?q@\"NSError\">16"
```
