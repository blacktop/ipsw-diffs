## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/TrustedPeersHelper.xpc/Contents/MacOS/TrustedPeersHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_stublist`

```diff

-62460.0.55.0.1
-  __TEXT.__text: 0x2b77e8
-  __TEXT.__auth_stubs: 0x2070
-  __TEXT.__objc_stubs: 0x6060
-  __TEXT.__objc_methlist: 0x2934
-  __TEXT.__const: 0xd4f0
-  __TEXT.__cstring: 0x17bd9
-  __TEXT.__swift5_typeref: 0x3fee
-  __TEXT.__oslogstring: 0xd591
+62460.1.2.0.0
+  __TEXT.__text: 0x2c0868
+  __TEXT.__auth_stubs: 0x2250
+  __TEXT.__objc_stubs: 0x61a0
+  __TEXT.__objc_methlist: 0x2944
+  __TEXT.__const: 0xd770
+  __TEXT.__cstring: 0x17e69
+  __TEXT.__swift5_typeref: 0x40b2
+  __TEXT.__oslogstring: 0xe151
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_classname: 0x147b
-  __TEXT.__objc_methname: 0x9131
-  __TEXT.__objc_methtype: 0x29f0
-  __TEXT.__constg_swiftt: 0x3c1c
-  __TEXT.__swift5_fieldmd: 0x2b8c
-  __TEXT.__swift5_reflstr: 0x2677
-  __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_assocty: 0x420
-  __TEXT.__swift5_proto: 0x98c
-  __TEXT.__swift5_types: 0x2c8
+  __TEXT.__objc_classname: 0x14bb
+  __TEXT.__objc_methname: 0x92b1
+  __TEXT.__objc_methtype: 0x2a00
+  __TEXT.__constg_swiftt: 0x3cc8
+  __TEXT.__swift5_fieldmd: 0x2bf8
+  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_reflstr: 0x26d7
+  __TEXT.__swift5_assocty: 0x450
+  __TEXT.__swift5_proto: 0x9a8
+  __TEXT.__swift5_types: 0x2d0
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__gcc_except_tab: 0x178
-  __TEXT.__swift5_capture: 0x51f4
+  __TEXT.__swift5_capture: 0x5268
   __TEXT.__dlopen_cstrs: 0x1c2
-  __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x50b8
-  __TEXT.__eh_frame: 0x7ea8
-  __DATA_CONST.__const: 0x14f28
+  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__unwind_info: 0x5120
+  __TEXT.__eh_frame: 0x7fa8
+  __DATA_CONST.__const: 0x15078
   __DATA_CONST.__cfstring: 0x18e0
-  __DATA_CONST.__objc_classlist: 0x268
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__auth_got: 0x1048
-  __DATA_CONST.__got: 0xa28
-  __DATA_CONST.__auth_ptr: 0x6f8
-  __DATA.__objc_const: 0x6e78
-  __DATA.__objc_selrefs: 0x1ec0
+  __DATA_CONST.__auth_got: 0x1138
+  __DATA_CONST.__got: 0xaa0
+  __DATA_CONST.__auth_ptr: 0x770
+  __DATA.__objc_const: 0x6f90
+  __DATA.__objc_selrefs: 0x1f10
   __DATA.__objc_ivar: 0x1fc
-  __DATA.__objc_data: 0x2c90
-  __DATA.__data: 0x84d0
+  __DATA.__objc_data: 0x2c98
+  __DATA.__data: 0x85f0
   __DATA.__objc_stublist: 0xa8
-  __DATA.__bss: 0x12e40
+  __DATA.__bss: 0x13140
   __DATA.__common: 0xa28
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libsqlite3.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8926
-  Symbols:   536
-  CStrings:  3210
+  Functions: 8967
+  Symbols:   549
+  CStrings:  3274
 
Symbols:
+ _NSFileSize
+ _NSSQLiteStoreType
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSPersistentStoreCoordinator
+ _getegid
+ _geteuid
+ _kSecurityRTCEventNameRecoverRKTLKSharesResult
+ _sqlite3_close
+ _sqlite3_exec
+ _sqlite3_free
+ _sqlite3_open_v2
+ _sqlite3_wal_checkpoint_v2
CStrings:
+ ". TrustedPeersHelper cannot operate without the DataVault-backed store."
+ "Container.init: about to loadPersistentStores name=%{public}s path=%{public}s existsPre=%{bool,public}d sizePre=%{public}ld"
+ "Container.init: loadPersistentStores returned err=%{public}s existsPost=%{bool,public}d sizePost=%{public}ld"
+ "Container.init: retry loadPersistentStores succeeded"
+ "Container.init: store flagged as corrupt; destroying and retrying. domain=%{public}s code=%{public}ld"
+ "Could not find RK TLK for %s, skipping evaluation"
+ "PRAGMA journal_mode=DELETE;"
+ "PRAGMA journal_mode=WAL;"
+ "Protected System container has no resolved path"
+ "Protected System container resolution failed for "
+ "Sponsor (%s doesn't have any TLK Shares to prove ownership, skipping"
+ "StorageContainersPrivate.Container.Owned symbol not resolved: StorageContainersPrivate framework is weak-linked but was not found at runtime. TrustedPeersHelper cannot operate without the container manager library."
+ "StorageContainersProvider: constructed Container.Owned identifier=%{public}s"
+ "StorageContainersProvider: grantAccess failed: %{public}s"
+ "StorageContainersProvider: grantAccess succeeded for identifier=%{public}s"
+ "StorageContainersProvider: revokeAccess for identifier=%{public}s"
+ "TrustedPeersHelper/ContainerMap.swift"
+ "WAL checkpoint failed"
+ "_TtC18TrustedPeersHelper25StorageContainersProvider"
+ "accessGranted"
+ "attributesOfItemAtPath:error:"
+ "categoriesByView"
+ "closeAndReturnError:"
+ "errored while trying to get full peer only views"
+ "fileExistsAtPath:"
+ "fileHandleForReadingFromURL:error:"
+ "findOrCreate: opening store for container=%{public}s context=%{public}s persona=%{public}s"
+ "findOrCreate: persistent store URL=%{public}s"
+ "grantAccess failed: "
+ "initWithManagedObjectModel:"
+ "migrateLegacyStoreIfNeeded: %{public}s -> %{public}s"
+ "migrateLegacyStoreIfNeeded: %{public}s — quarantining and starting fresh"
+ "migrateLegacyStoreIfNeeded: %{public}s — starting fresh"
+ "migrateLegacyStoreIfNeeded: WAL checkpoint rc=%{public}d for %{public}s"
+ "migrateLegacyStoreIfNeeded: checkpoint open failed for %{public}s"
+ "migrateLegacyStoreIfNeeded: copy complete (atomic rename)"
+ "migrateLegacyStoreIfNeeded: destination already exists; skipping"
+ "migrateLegacyStoreIfNeeded: journal_mode=DELETE failed: %{public}s for %{public}s"
+ "migrateLegacyStoreIfNeeded: journal_mode=WAL failed: %{public}s for %{public}s"
+ "migrateLegacyStoreIfNeeded: legacy file still present (not removed): %{public}s"
+ "migrateLegacyStoreIfNeeded: migration complete"
+ "migrateLegacyStoreIfNeeded: restoreWALMode open failed for %{public}s"
+ "migrateLegacyStoreIfNeeded: source does not exist; nothing to migrate"
+ "migrateLegacyStoreIfNeeded: unexpected %{public}s sibling remains after checkpoint at %{public}s"
+ "moveItemAtURL:toURL:error:"
+ "owned"
+ "protectedSystemProviderFactory"
+ "quarantineCorruptStore: failed to move %{public}s aside: %{public}s"
+ "quarantineCorruptStore: quarantined %{public}s → %{public}s"
+ "readDataOfLength:"
+ "removeItemAtURL:error:"
+ "replacePersistentStore failed: "
+ "replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:"
+ "source is not a SQLite database"
+ "storageOwner"
+ "urlForPersistentStore: Protected System container URL=%{public}s"
+ "urlForPersistentStore: db at %{public}s exists=%{bool,public}d"
+ "urlForPersistentStore: db does not exist yet; checking legacy for migration"
+ "urlForPersistentStore: destination already existed; using it as-is"
+ "urlForPersistentStore: migration failed (%{public}s); CoreData will create fresh schema"
+ "urlForPersistentStore: migration succeeded"
+ "urlForPersistentStore: no legacy URL resolvable for %{public}s; skipping migration"
+ "urlForPersistentStore: no legacy store; CoreData will create fresh schema"
+ "urlForPersistentStore: resolving for filename=%{public}s persona=%{public}s"
+ "urlForPersistentStore: returning Protected System URL %{public}s"
- "Potential sponsor %s does not have a self-TLKShare for this view, skipping"
```
