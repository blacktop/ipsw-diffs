## JournalDataclassOwner

> `/System/Library/Accounts/DataclassOwners/JournalDataclassOwner.bundle/JournalDataclassOwner`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0x149fc
-  __TEXT.__auth_stubs: 0xdb0
+39.0.0.0.1
+  __TEXT.__text: 0xf5a0
+  __TEXT.__auth_stubs: 0xca0
   __TEXT.__objc_methlist: 0x25c
-  __TEXT.__const: 0x690
+  __TEXT.__const: 0x678
   __TEXT.__constg_swiftt: 0x1b0
-  __TEXT.__swift5_typeref: 0x316
+  __TEXT.__swift5_typeref: 0x294
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x9c
   __TEXT.__swift5_fieldmd: 0xd0
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x20
-  __TEXT.__cstring: 0x483
-  __TEXT.__objc_methname: 0x960
-  __TEXT.__oslogstring: 0x1cb4
-  __TEXT.__swift5_capture: 0x280
+  __TEXT.__cstring: 0x3e9
+  __TEXT.__objc_methname: 0x796
+  __TEXT.__oslogstring: 0x1484
+  __TEXT.__swift5_capture: 0x11c
   __TEXT.__objc_classname: 0x23
   __TEXT.__objc_methtype: 0x1f4
-  __TEXT.__unwind_info: 0x338
-  __TEXT.__eh_frame: 0x200
-  __DATA_CONST.__auth_got: 0x6d8
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__auth_ptr: 0x1a8
-  __DATA_CONST.__const: 0x7c8
+  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__eh_frame: 0x1c8
+  __DATA_CONST.__auth_got: 0x650
+  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__auth_ptr: 0x198
+  __DATA_CONST.__const: 0x4f8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA.__objc_const: 0x348
-  __DATA.__objc_selrefs: 0x3b0
+  __DATA.__objc_selrefs: 0x2d0
   __DATA.__objc_data: 0x330
-  __DATA.__data: 0x530
-  __DATA.__common: 0xd8
+  __DATA.__data: 0x498
+  __DATA.__common: 0xc8
   __DATA.__bss: 0x980
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 97C6B559-DB5B-3D62-965D-4DAC08BE0F67
-  Functions: 295
+  UUID: 1859CD91-6EC1-3ED5-AEB5-EB61426B7057
+  Functions: 232
   Symbols:   135
-  CStrings:  283
+  CStrings:  229
 
Symbols:
+ _swift_endAccess
- _objc_retain_x24
CStrings:
+ "Database is not open"
+ "Deleted all local data"
+ "Deleting all local data"
+ "Device is locked"
+ "Error trying to mark all records as not uploaded %@, %s"
+ "Failed to delete all local data %@, %s"
+ "Failed to get record from systemfields for the asset: %s"
+ "Failed to get record from systemfields for the attachment: %@"
+ "Failed writing assetMetadata to file %s: %@"
+ "File attachment file does not exist: %s"
+ "Found  %ld local %s objects that need to be uploaded.  Created %ld corresponding records."
+ "Ignoring action %s"
+ "Marked all records as not uploaded"
+ "Marking all records as not uploaded"
+ "Missing assetMetadata for asset id %s"
+ "Need to create recordSystemFields for %s with %s"
+ "Saving assetMetadata to url: %s"
+ "Unable to get attachment url: %s"
+ "will upload asset records: %ld"
+ "will upload attachments records: %ld"
- "%{public}s (Delete All) Unabled to delete all journal entries: %@"
- "%{public}s (Delete All) journal entries"
- "%{public}s (Delete All) journal entries asset attachments"
- "%{public}s (Delete All) journal entries assets"
- "%{public}s (getEntriesNotUploaded) Unable to get un-uploaded entries: %@"
- "%{public}s (getEntriesNotUploaded) fetched un-uploaded entries:%ld"
- "%{public}s (getEntriesNotUploaded) started"
- "%{public}s (getRecordsFromJournalEntryAssetFileAttachments) will upload attachments records:%ld"
- "%{public}s (getRecordsFromJournalEntryAssets) will upload asset records:%ld"
- "%{public}s Unable to fetch sync data: %@"
- "%{public}s Unable to get sync data"
- "%{public}s Unabled to fetch all journal entries to make all not uploaded: %@"
- "%{public}s Unabled to fetch all not uploaded assets: %@"
- "%{public}s Unabled to fetch all not uploaded file attachments: %@"
- "%{public}s [REMOVED] Sync state data "
- "(actionDeleteAllLocalData) Unable to remove all journal entries"
- "(actionDeleteAllLocalData) Unable to remove sync metadata"
- "(actionDeleteAllLocalData) Unresolved error %@, %s"
- "(actionDeleteAllLocalData) complete success"
- "(actionDeleteAllLocalData) started"
- "(actionMakeAllDataNotUploaded) %s Database is not open"
- "(actionMakeAllDataNotUploaded) %s complete success"
- "(actionMakeAllDataNotUploaded) %s, device is locked"
- "(actionMakeAllDataNotUploaded) Unable to mark all assets as not uploaded"
- "(actionMakeAllDataNotUploaded) Unable to mark all entries as not uploaded"
- "(actionMakeAllDataNotUploaded) Unable to mark all file attachments as not uploaded"
- "(actionMakeAllDataNotUploaded) Unable to remove sync metadata"
- "(actionMakeAllDataNotUploaded) Unresolved error with %s %@, %s"
- "(actionMakeAllDataNotUploaded) started"
- "(actionUploadChanges) un-uploaded entries count:%ld"
- "(actionUploadChanges) will upload entry records:%ld"
- "(getRecordFromJournalEntry) Failed to get record from systemfields for the entry: %s"
- "(getRecordFromJournalEntryAsset) An asset doesn't have assetMetadata: %s"
- "(getRecordFromJournalEntryAsset) CKRecord Recreated from asset:\n%s"
- "(getRecordFromJournalEntryAsset) Failed to get record from systemfields for the asset: %s"
- "(getRecordFromJournalEntryAsset) Saving assetMetadata to url: %s"
- "(getRecordFromJournalEntryAsset) Unable to create an assetMetadataAsset, reason:%@"
- "(getRecordFromJournalEntryAssetFileAttachment) CKRecord Recreated from fileAttachment:\n%s"
- "(getRecordFromJournalEntryAssetFileAttachment) Failed to get record from systemfields for the attachment: %s"
- "(getRecordFromJournalEntryAssetFileAttachment) File attachment file does not exist: %s"
- "(getRecordFromJournalEntryAssetFileAttachment) Unable to get attachment url: %s"
- "CKRecord Recreated from entry %s"
- "Error serializing mergeable attributes for entry %s: %@"
- "assetOrdering"
- "bundleDate"
- "bundleEndDate"
- "bundleId"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "dateSource"
- "deleteObject:"
- "entryDate"
- "entryType"
- "flagged"
- "isRemovedFromCloud"
- "markAllJournalEntriesNotUploaded"
- "markAllJournalEntryAssetFileAttachmentsNotUploaded"
- "markAllJournalEntryAssetsNotUploaded"
- "mergeableAttributes"
- "minimumSupportedAppVersionMode"
- "prompt"
- "reflectionIcon"
- "reflectionPrompt"
- "reflectionType"
- "removeItemAtURL:error:"
- "setIsUploadedToCloud:"
- "setMetadata:"
- "setRecordSystemFields:"
- "setStatedata:"
- "setUserId:"
- "showPhotoMemoryBanner"
- "showTitle"
- "text"
- "textLength"
- "updatedDate"

```
