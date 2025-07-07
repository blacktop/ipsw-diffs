## postersyncd

> `/System/Library/Frameworks/Contacts.framework/Support/postersyncd`

```diff

-10.100.1.0.0
-  __TEXT.__text: 0x10e10
-  __TEXT.__auth_stubs: 0xc30
+14.100.2.0.0
+  __TEXT.__text: 0x13b24
+  __TEXT.__auth_stubs: 0xcd0
   __TEXT.__objc_stubs: 0x20
   __TEXT.__objc_methlist: 0x254
-  __TEXT.__const: 0x92e
-  __TEXT.__cstring: 0x62f
-  __TEXT.__oslogstring: 0x975
+  __TEXT.__oslogstring: 0x1098
   __TEXT.__objc_classname: 0x80
-  __TEXT.__objc_methname: 0x6d6
+  __TEXT.__objc_methname: 0x766
   __TEXT.__objc_methtype: 0x246
-  __TEXT.__constg_swiftt: 0x360
-  __TEXT.__swift5_typeref: 0x40e
+  __TEXT.__const: 0x9b2
+  __TEXT.__cstring: 0x747
+  __TEXT.__constg_swiftt: 0x3ac
+  __TEXT.__swift5_typeref: 0x4ab
   __TEXT.__swift5_fieldmd: 0x258
-  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift5_types: 0x40
+  __TEXT.__swift5_reflstr: 0x1f5
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_reflstr: 0x1ed
-  __TEXT.__swift5_capture: 0xc0
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_proto: 0x58
+  __TEXT.__swift5_capture: 0x130
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_proto: 0x54
-  __TEXT.__unwind_info: 0x428
+  __TEXT.__unwind_info: 0x458
   __TEXT.__eh_frame: 0x528
-  __DATA_CONST.__auth_got: 0x620
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__auth_ptr: 0x1a8
-  __DATA_CONST.__const: 0x7c0
+  __DATA_CONST.__auth_got: 0x670
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__auth_ptr: 0x1b8
+  __DATA_CONST.__const: 0x8d0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA.__objc_const: 0x5b8
-  __DATA.__objc_selrefs: 0x298
-  __DATA.__objc_data: 0x360
-  __DATA.__data: 0x9d8
+  __DATA.__objc_selrefs: 0x2d8
+  __DATA.__objc_data: 0x380
+  __DATA.__data: 0xa30
   __DATA.__common: 0x38
-  __DATA.__bss: 0xa80
+  __DATA.__bss: 0xb00
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 537215A7-D5E3-39F4-9E8F-2CE8B1807D2D
-  Functions: 343
-  Symbols:   332
-  CStrings:  222
+  UUID: 22B7F657-5E6B-36DE-AE6F-099451E609CF
+  Functions: 376
+  Symbols:   353
+  CStrings:  260
 
Symbols:
+ _$s10Foundation12NotificationV19_bridgeToObjectiveCSo14NSNotificationCyF
+ _$s10Foundation12NotificationV4name6object8userInfoACSo18NSNotificationNamea_ypSgSDys11AnyHashableVypGSgtcfC
+ _$s10Foundation3URLV13DirectoryHintO13inferFromPathyA2EmFWC
+ _$s10Foundation3URLV13DirectoryHintOMa
+ _$s10Foundation3URLV9appending9component13directoryHintACx_AC09DirectoryF0OtSyRzlF
+ _$s10Foundation3URLVMn
+ _$s10Foundation3URLVs23CustomStringConvertibleAAMc
+ _$s8Contacts21BackupRestoreMigratorV16attemptMigration9directionSbAC0F9DirectionO_tKF
+ _$s8Contacts21BackupRestoreMigratorV9container7tempURL9modelName13recoveryLimitACSo21NSPersistentContainerC_10Foundation0G0VSSSitcfC
+ _$s8Contacts21BackupRestoreMigratorVMa
+ _$s8Contacts22ContactPosterContainerV04makeD015disableCloudKit8inMemory15customStorePathSo012NSPersistentD0CSb_Sb10Foundation3URLVSgtKFZ
+ _$sBi64_WV
+ _$sSS10describingSSx_tclufC
+ _$sSSSysMc
+ _NSCloudKitMirroringDelegateDidResetSyncNotificationName
+ _NSCloudKitMirroringDelegateResetSyncReasonKey
+ _NSCloudKitMirroringDelegateWillResetSyncNotificationName
+ _OBJC_CLASS_$_CNEnvironment
+ _OBJC_CLASS_$_CNInhibitor
+ _OBJC_CLASS_$_NSNumber
+ _objc_retain_x9
+ _swift_getForeignTypeMetadata
- _$s8Contacts22ContactPosterContainerV04makeD015disableCloudKit8inMemorySo012NSPersistentD0CSb_SbtKFZ
CStrings:
+ "Attempted to back up poster data, but there was no readable data to backup, so no temp database was created."
+ "Attempted to restore backed up poster data, but there was no data to restore."
+ "CNContactMetadata"
+ "CloudKit mirroring did reset due to account login. Attempting to restore from backup."
+ "CloudKit mirroring will reset due to account login. Starting backup"
+ "CloudKit reset for reason: %s."
+ "CloudKit reset notification didn't map to a known ResetSyncReason: %s."
+ "Created backup-before-signin transaction"
+ "Created poster cleanup transaction"
+ "Created restore-after-signin transaction"
+ "Failed to migrate poster data into %s with error: %@"
+ "Failed to restore poster data from %s with error: %@"
+ "In response to testing notification, broadcasting fake CoreData+CloudKit sign-in didReset notification"
+ "In response to testing notification, broadcasting fake CoreData+CloudKit sign-in willReset notification"
+ "In response to testing notification, sent fake CoreData+CloudKit sign-in didReset notification"
+ "In response to testing notification, sent fake CoreData+CloudKit sign-in willReset notification"
+ "No migration needed for a non-login CloudKit reset."
+ "No restore needed for a non-login CloudKit reset."
+ "Received CloudKit didReset for login, but unexpectedly couldn't construct URL for the poster store. Giving up with potentially abandoned backup."
+ "Received CloudKit reset for login, but unexpectedly couldn't construct URL for the poster store. Abandoning ship."
+ "Stopped backup-before-signin transaction"
+ "Stopped poster cleanup transaction"
+ "Stopped restore-after-signin transaction"
+ "Successfully backed up poster data to %s"
+ "Successfully restored poster data from %s"
+ "TempBackupDuringSignin.db"
+ "com.apple.contacts.posters.backup-before-signin"
+ "com.apple.contacts.posters.restore-after-signin"
+ "com.apple.private.contacts.test.icloud-signin.finish"
+ "com.apple.private.contacts.test.icloud-signin.start"
+ "currentEnvironment"
+ "initWithUnsignedInteger:"
+ "isInternalBuild"
+ "os_transactionInhibitorWithLabel:"
+ "postNotification:"
+ "start"
+ "stop"
+ "unsignedIntegerValue"

```
