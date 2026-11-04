## MobileSlideShow

> `/System/Library/DataClassMigrators/MobileSlideShow.migrator/MobileSlideShow`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__objc_classname`
- `__TEXT.__objc_methtype`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`

```diff

-916.57.153.0.0
-  __TEXT.__text: 0x284c
-  __TEXT.__auth_stubs: 0x290
+920.7.110.0.0
+  __TEXT.__text: 0x29d0
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_stubs: 0xb20
   __TEXT.__objc_methlist: 0x134
   __TEXT.__const: 0x20
   __TEXT.__objc_methname: 0xa21
   __TEXT.__cstring: 0xe6
-  __TEXT.__oslogstring: 0x664
+  __TEXT.__oslogstring: 0x754
   __TEXT.__objc_classname: 0x42
   __TEXT.__objc_methtype: 0xa0
   __TEXT.__unwind_info: 0xc0

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__auth_got: 0x158
   __DATA_CONST.__got: 0xf0
   __DATA.__objc_const: 0x290
   __DATA.__objc_selrefs: 0x2f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 23
-  Symbols:   82
+  Symbols:   83
   CStrings:  167
 
Symbols:
+ _PLCurrentLibraryLogTag
CStrings:
+ "%{public}sCould not remove the old large thumbnails directory %@. Error: %@"
+ "%{public}sCreated foreground restore from cloud backup complete token"
+ "%{public}sFailed to create %{public}@ [Migration will fail.] Error: %{public}@"
+ "%{public}sFailed to create %{public}@ to hold the video's metadata [Migration will fail.] Error: %{public}@"
+ "%{public}sFailed to create directory %{public}@ Error: %{public}@"
+ "%{public}sFailed to create foreground restore from cloud backup complete token: %{public}@"
+ "%{public}sFailed to delete existing %{public}@ [Migration will skip %{public}@.] Error: %{public}@"
+ "%{public}sFailed to enumerate %{public}@. Its files won't be moved to %{public}@. Error %{public}@"
+ "%{public}sFailed to enumerate %{public}@. No *APPLE or *IMPRT directories will be migrated."
+ "%{public}sFailed to enumerate old iTunes videos paths at %{public}@ [Migration will continue.] Error: %{public}@"
+ "%{public}sFailed to move %{public}@ to %{public}@ [Migration will continue.] Error: %{public}@"
+ "%{public}sFailed to move %{public}@ to %{public}@ [Migration will fail.] Error: %{public}@"
+ "%{public}sFailed to remove %{public}@ to replace it with the current version [Migration will fail.] Error: %{public}@"
+ "%{public}sFailed to remove empty %{public}@. Error: %{public}@"
+ "%{public}sLegacy migration %{public}@"
+ "%{public}sMigration complete"
+ "%{public}sRequires legacy migration"
+ "%{public}sSent cleanupModelForDataMigrationForRestoreType: %{public}@ at QoS: %{public}@"
+ "%{public}sSent dataMigrationWillFinish at %{public}@"
+ "%{public}sStarting assetsd migration service requests for restore type: %{public}@ at QoS: %{public}@"
+ "%{public}sStarting migration at QoS: %{public}@"
+ "%{public}sUnable to assign data protection to \"%{public}@\": %{public}@"
+ "%{public}sUnable to change owner of file at path: %{public}@, reason: %{public}@"
+ "%{public}sUnable to create directory: %{public}@, reason: %{public}@"
- "Could not remove the old large thumbnails directory %@. Error: %@"
- "Created foreground restore from cloud backup complete token"
- "Failed to create %{public}@ [Migration will fail.] Error: %{public}@"
- "Failed to create %{public}@ to hold the video's metadata [Migration will fail.] Error: %{public}@"
- "Failed to create directory %{public}@ Error: %{public}@"
- "Failed to create foreground restore from cloud backup complete token: %{public}@"
- "Failed to delete existing %{public}@ [Migration will skip %{public}@.] Error: %{public}@"
- "Failed to enumerate %{public}@. Its files won't be moved to %{public}@. Error %{public}@"
- "Failed to enumerate %{public}@. No *APPLE or *IMPRT directories will be migrated."
- "Failed to enumerate old iTunes videos paths at %{public}@ [Migration will continue.] Error: %{public}@"
- "Failed to move %{public}@ to %{public}@ [Migration will continue.] Error: %{public}@"
- "Failed to move %{public}@ to %{public}@ [Migration will fail.] Error: %{public}@"
- "Failed to remove %{public}@ to replace it with the current version [Migration will fail.] Error: %{public}@"
- "Failed to remove empty %{public}@. Error: %{public}@"
- "Legacy migration %{public}@"
- "Migration complete"
- "Requires legacy migration"
- "Sent cleanupModelForDataMigrationForRestoreType: %{public}@ at QoS: %{public}@"
- "Sent dataMigrationWillFinish at %{public}@"
- "Starting assetsd migration service requests for restore type: %{public}@ at QoS: %{public}@"
- "Starting migration at QoS: %{public}@"
- "Unable to assign data protection to \"%{public}@\": %{public}@"
- "Unable to change owner of file at path: %{public}@, reason: %{public}@"
- "Unable to create directory: %{public}@, reason: %{public}@"
```
