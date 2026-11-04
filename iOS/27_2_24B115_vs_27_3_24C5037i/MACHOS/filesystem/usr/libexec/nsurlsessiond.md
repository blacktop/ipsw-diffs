## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3896.200.61.0.0
-  __TEXT.__text: 0x82acc
-  __TEXT.__auth_stubs: 0x11e0
+3896.300.31.0.0
+  __TEXT.__text: 0x84020
+  __TEXT.__auth_stubs: 0x1210
   __TEXT.__lazy_helpers: 0xfc
-  __TEXT.__objc_stubs: 0xab60
-  __TEXT.__objc_methlist: 0x633c
+  __TEXT.__objc_stubs: 0xaca0
+  __TEXT.__objc_methlist: 0x63b4
   __TEXT.__const: 0x270
-  __TEXT.__gcc_except_tab: 0xe8f0
-  __TEXT.__cstring: 0x3d4d
-  __TEXT.__objc_methname: 0xf534
+  __TEXT.__gcc_except_tab: 0xea5c
+  __TEXT.__cstring: 0x3fab
+  __TEXT.__objc_methname: 0xf717
   __TEXT.__objc_classname: 0xbd1
-  __TEXT.__objc_methtype: 0x2f81
-  __TEXT.__oslogstring: 0xf9cf
-  __TEXT.__unwind_info: 0x3160
-  __DATA_CONST.__const: 0x15e8
-  __DATA_CONST.__cfstring: 0x1e60
+  __TEXT.__objc_methtype: 0x2fbd
+  __TEXT.__oslogstring: 0xfeb5
+  __TEXT.__unwind_info: 0x31d0
+  __DATA_CONST.__const: 0x1660
+  __DATA_CONST.__cfstring: 0x1ee0
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x138

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x908
+  __DATA_CONST.__auth_got: 0x920
   __DATA_CONST.__got: 0x7b0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x9000
-  __DATA.__objc_selrefs: 0x37d0
+  __DATA.__objc_selrefs: 0x3820
   __DATA.__objc_ivar: 0x6f0
   __DATA.__objc_data: 0x1680
   __DATA.__lazy_load_got: 0x18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2103
-  Symbols:   519
-  CStrings:  3906
+  Functions: 2118
+  Symbols:   522
+  CStrings:  3949
 
Symbols:
+ _AnalyticsSendEventLazy
+ _SecTaskGetCodeSignStatus
+ _SecTaskGetValidationCategory
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "B40@0:8@16^i24^B32"
+ "B60@0:8{?=[8I]}16@48B56"
+ "CREATE TABLE IF NOT EXISTS clients ( bundle_id text NOT NULL, identity_tier int NOT NULL, ls_tracked int NOT NULL, last_seen real, UNIQUE(bundle_id));"
+ "Client at identity tier %d took over bundle ID %{public}@ (previously tier %d), discarding inherited state"
+ "DELETE FROM clients"
+ "DELETE from session_tasks WHERE bundle_id = ?"
+ "Discarding background session state for bundle ID %{public}@"
+ "Failed to bind client identity params for bundleID (%{public}@) to the replace statement"
+ "Failed to create clients schema"
+ "Failed to create secure task to read identity tier. Treating client as unsigned"
+ "Failed to delete entries from clients table of DB: %s"
+ "Failed to execute task deletion for bundleID (%{public}@). Error = %s"
+ "Failed to init the _countStateStmt statement for bundleID: %{public}@"
+ "Failed to init the _deleteAllTasksForBundleIDStmt statement for bundleID: %{public}@"
+ "Failed to init the _replaceClientStmt statement for bundleID: %{public}@"
+ "Failed to init the _selectClientStmt statement for bundleID: %{public}@"
+ "Failed to migrate to version 5"
+ "Failed to read validation category, error: %d. Treating client as unsigned"
+ "Failed to record identity for bundleID (%{public}@). Error = %s"
+ "REPLACE INTO clients (bundle_id, identity_tier, ls_tracked, last_seen) VALUES (?, ?, ?, ?)"
+ "Refusing connection from client at identity tier %d claiming bundle ID %{public}@, which belongs to a client at tier %d"
+ "SELECT EXISTS (SELECT 1 FROM session_tasks WHERE bundle_id = ?) \t\tOR EXISTS (SELECT 1 FROM sessions WHERE bundle_id = ?)"
+ "SELECT identity_tier, ls_tracked from clients WHERE bundle_id = ? LIMIT 1"
+ "_deleteAllStateForBundleID:"
+ "_deleteAllTasksForBundleID: %{public}@"
+ "_getClientIdentityForBundleID: %{public}@"
+ "_getClientIdentityForBundleID:tier:trackedByLaunchServices:"
+ "_hasAnyStateForBundleID:"
+ "_hasAnyStateForBundleID: %{public}@"
+ "_onqueue_deleteAllTasksForBundleID:"
+ "_onqueue_getClientIdentityForBundleID:tier:trackedByLaunchServices:"
+ "_onqueue_hasAnyStateForBundleID:"
+ "_onqueue_updateClientIdentityForBundleID:tier:trackedByLaunchServices:"
+ "_updateClientIdentityForBundleID: %{public}@ tier: %d"
+ "_updateClientIdentityForBundleID:tier:trackedByLaunchServices:"
+ "com.apple.CFNetwork.nsurlsessiond-identity-tier-mismatch"
+ "discardStateForBundleID:"
+ "process"
+ "recordedTier"
+ "tier"
+ "v32@0:8@16i24B28"
+ "validateIdentityForClientWithAuditToken:bundleID:trackedByLaunchServices:"
```
