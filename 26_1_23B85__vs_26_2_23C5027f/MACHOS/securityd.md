## securityd

> `/usr/libexec/securityd`

```diff

-61901.40.77.0.0
-  __TEXT.__text: 0x25bdf4
+61901.60.29.0.0
+  __TEXT.__text: 0x25cd6c
   __TEXT.__auth_stubs: 0x42b0
-  __TEXT.__objc_stubs: 0x1c7c0
-  __TEXT.__objc_methlist: 0x15348
+  __TEXT.__objc_stubs: 0x1c800
+  __TEXT.__objc_methlist: 0x15368
   __TEXT.__const: 0x919
-  __TEXT.__objc_methname: 0x2c64d
-  __TEXT.__cstring: 0x20fe0
-  __TEXT.__oslogstring: 0x2d520
+  __TEXT.__objc_methname: 0x2c6d3
+  __TEXT.__cstring: 0x21130
+  __TEXT.__oslogstring: 0x2d547
   __TEXT.__swift5_typeref: 0x37a
   __TEXT.__swift5_fieldmd: 0x120
   __TEXT.__constg_swiftt: 0x274

   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__gcc_except_tab: 0xb630
+  __TEXT.__gcc_except_tab: 0xb654
   __TEXT.__objc_classname: 0x238d
-  __TEXT.__objc_methtype: 0xa586
+  __TEXT.__objc_methtype: 0xa5b6
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x67b8
+  __TEXT.__unwind_info: 0x67e8
   __TEXT.__eh_frame: 0xa58
   __DATA_CONST.__auth_got: 0x2168
-  __DATA_CONST.__got: 0x1350
+  __DATA_CONST.__got: 0x1360
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x14180
-  __DATA_CONST.__cfstring: 0x1b300
+  __DATA_CONST.__const: 0x141d0
+  __DATA_CONST.__cfstring: 0x1b520
   __DATA_CONST.__objc_classlist: 0x8c0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x250

   __DATA_CONST.__objc_arraydata: 0x3f8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA.__objc_const: 0x22a30
-  __DATA.__objc_selrefs: 0x9360
+  __DATA.__objc_const: 0x22a38
+  __DATA.__objc_selrefs: 0x9378
   __DATA.__objc_ivar: 0x1a10
   __DATA.__objc_data: 0x5a78
   __DATA.__data: 0x2380

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E2ED4542-4761-3C8E-9921-D99FB9687126
-  Functions: 9635
-  Symbols:   1776
-  CStrings:  19595
+  UUID: D77E6C6B-77DF-31A3-A49E-D0BFAA571EC9
+  Functions: 9639
+  Symbols:   1778
+  CStrings:  19634
 
Symbols:
+ _kSecureBackupAlliCDPRecordsKey
+ _kSecureBackupRecordIDKey
CStrings:
+ "(%@,%ld)"
+ "@\"NSDictionary\"32@0:8@16^@24"
+ "B40@0:8^@16@24^@32"
+ "Failed to fetch remote changes"
+ "Returning force-fetch because engines aren't loaded with error: %{public}@"
+ "Sync Engines are not available"
+ "[%@]"
+ "com.apple.security.keychain.sharing.dbUpdateOperation"
+ "com.apple.security.keychain.sharing.initialFetchMetrics"
+ "com.apple.security.keychain.sharing.miscellaneousOperation"
+ "counts"
+ "creates"
+ "deletes"
+ "enableWithPasscodeStashSecret:existingRecord:account:error:"
+ "escrow-repair-get-account-info"
+ "failed to get existing record: %@"
+ "getAccountInfoWithError:"
+ "getAccountInfoWithSecureBackup:error:"
+ "getExistingRecord:peerID:error:"
+ "maintenance"
+ "maintenanceXPC"
+ "preflight"
+ "processDatabaseModificationsWithCompletion:"
+ "resyncXPC"
+ "setDaysLeftOnRateLimit:"
+ "setMetadataHash:"
+ "setRateLimitState:"
+ "verifyGroupsInSyncAndResyncMissingGroupsXPC"
+ "verifyGroupsInSyncXPC"
+ "{%@:%@}"
+ "{%@:{}}"
+ "{Success:{}}"
- "Error: %@ (Domain: %@, Code: %ld)"
- "com.apple.security.keychain.sharing.initialFetch"
- "deleteRecord:"
- "disableWithError:"
- "enableWithPasscodeStashSecret:account:error:"
- "escrow-repair-disable"
- "failed to delete escrow record: %@"
- "processDatabaseModifications"
- "stringWithCString:"
- "successfully deleted escrow record"

```
