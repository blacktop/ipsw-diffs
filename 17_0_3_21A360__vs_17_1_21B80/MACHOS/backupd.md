## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-1996.2.3.0.0
-  __TEXT.__text: 0x2177c4
+2008.42.2.0.0
+  __TEXT.__text: 0x218268
   __TEXT.__auth_stubs: 0x2d30
-  __TEXT.__objc_stubs: 0x25b60
-  __TEXT.__objc_methlist: 0x14d50
+  __TEXT.__objc_stubs: 0x25bc0
+  __TEXT.__objc_methlist: 0x14d78
   __TEXT.__const: 0xa10
-  __TEXT.__cstring: 0x63d64
+  __TEXT.__cstring: 0x64048
   __TEXT.__constg_swiftt: 0x6d4
   __TEXT.__swift5_typeref: 0x53b
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift5_fieldmd: 0x320
   __TEXT.__swift5_types: 0x34
   __TEXT.__objc_classname: 0x1aed
-  __TEXT.__objc_methname: 0x2f47f
-  __TEXT.__objc_methtype: 0x5954
+  __TEXT.__objc_methname: 0x2f573
+  __TEXT.__objc_methtype: 0x5962
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__oslogstring: 0x26d4e
-  __TEXT.__gcc_except_tab: 0x7c2c
-  __TEXT.__unwind_info: 0x5d54
+  __TEXT.__oslogstring: 0x26e44
+  __TEXT.__gcc_except_tab: 0x7cc4
+  __TEXT.__unwind_info: 0x5d7c
   __TEXT.__eh_frame: 0x3a8
   __DATA_CONST.__auth_got: 0x16a8
   __DATA_CONST.__got: 0x750
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x6370
-  __DATA_CONST.__cfstring: 0x1ae80
+  __DATA_CONST.__const: 0x6398
+  __DATA_CONST.__cfstring: 0x1aea0
   __DATA_CONST.__objc_classlist: 0x8d0
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x188

   __DATA_CONST.__objc_arraydata: 0xc80
   __DATA_CONST.__objc_dictobj: 0x1e0
   __DATA_CONST.__objc_arrayobj: 0x438
-  __DATA.__objc_const: 0x22778
-  __DATA.__objc_selrefs: 0xabd8
+  __DATA.__objc_const: 0x227a8
+  __DATA.__objc_selrefs: 0xabf8
   __DATA.__objc_protorefs: 0x50
-  __DATA.__objc_classrefs: 0xda8
+  __DATA.__objc_classrefs: 0xdb0
   __DATA.__objc_superrefs: 0x6f0
-  __DATA.__objc_ivar: 0x195c
+  __DATA.__objc_ivar: 0x1960
   __DATA.__objc_data: 0x5f20
   __DATA.__data: 0x15a0
   __DATA.__bss: 0xdf0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6B774173-CFEE-3B29-BA6B-61FD2635816E
-  Functions: 8308
-  Symbols:   1241
-  CStrings:  25289
+  UUID: EC37D11E-E447-3CFA-8CCD-B5E5AF081CE4
+  Functions: 8312
+  Symbols:   1242
+  CStrings:  25302
 
Symbols:
+ _OBJC_CLASS_$_ICQOfferManager
CStrings:
+ "\x05\x97G"
+ "-[MBBackupScheduler _determineInternalNotificationActionForErrors:dateOfLastUnlock:]"
+ "-[MBFollowUpManager postFollowUpForRestoreFinishedForAccount:skipiCloudQuotaOffer:]"
+ "-[MBFollowUpManager postFollowUpForRestoreFinishedForAccount:skipiCloudQuotaOffer:]_block_invoke"
+ "=ttr= Error deleting backup: %@"
+ "=ttr= Found %lu failures 1 day ago and %lu failures between 1 day and %lu days ago. dateOfLastUnlock:%{private}@ action:%ld"
+ "=ttr= Not posting internal notification, %p is in-flight"
+ "=ttr= Posted internal notification %p"
+ "=ttr= Received response (%lu) from internal notification %p"
+ "Finished queueing %llu files (%llu) and %llu deletes for %lu domains in %.2fs"
+ "Finished uploading %llu files (%llu) and %llu deletes for %lu domains"
+ "Finished uploading %llu files (%llu) and %llu deletes for %lu domains: %@"
+ "Going to upload %lu domains(%llu) files:%d deletes:%llu"
+ "Not posting restore finished follow up because of ICQ offer"
+ "Queued %llu files (%llu) and %llu deletes for %{public}@"
+ "Queued a total of %llu files (%llu) and %llu deletes for %{public}@"
+ "SELECT COUNT(*) FROM FileChanges WHERE changeType = %lu"
+ "SELECT relativePath, size, changeType, shouldCopy FROM FileChanges WHERE domain = %@ AND (changeType = %lu OR changeType = %lu OR (changeType = %lu AND NOT EXISTS (SELECT 1 FROM Files WHERE SUBSTR(manifestID, 0, 36) == (SELECT SUBSTR(value, 3 , 36) FROM Properties WHERE key == %@) AND Files.domain = FileChanges.domain AND Files.relativePath = FileChanges.relativePath AND Files.deleted = 1)))"
+ "T@\"NSDate\",&,N,V_dateOfLastUnlockSeenByDaemon"
+ "_dateOfLastUnlockSeenByDaemon"
+ "_determineInternalNotificationActionForErrors:dateOfLastUnlock:"
+ "_restoreFinishedFollowUpItemForAccount:"
+ "dateOfLastUnlockSeenByDaemon"
+ "postBackupRestoredOffer:"
+ "postFollowUpForRestoreFinishedForAccount:skipiCloudQuotaOffer:"
+ "q32@0:8@16@24"
+ "setDateOfLastUnlockSeenByDaemon:"
+ "v24@?0I8I12Q16"
- "\x05\x97F"
- "-[MBBackupScheduler _determineInternalNotificationActionForErrors:]"
- "-[MBFollowUpManager postFollowUpForRestoreFinishedForAccount:]"
- "Error deleting backup: %@"
- "Finished queueing %llu files (%llu) for %lu domains in %.2fs"
- "Finished uploading %llu files (%llu) for %lu domains"
- "Finished uploading %llu files (%llu) for %lu domains: %@"
- "Found %lu failures 1 day ago and %lu failures between 1 day and %lu days ago"
- "Not posting internal notification, %p is in-flight"
- "Posted internal notification %p"
- "Queued %llu files (%llu) for %{public}@"
- "Queued a total of %llu files (%llu) for %{public}@"
- "Received response (%lu) from internal notification %p"
- "SELECT relativePath, size, changeType, shouldCopy FROM FileChanges WHERE domain = %@ AND changeType != %lu"
- "Uploading %lu domains: %@"
- "_determineInternalNotificationActionForErrors:"
- "postFollowUpForRestoreFinishedForAccount:"

```
