## managedassetsd

> `/usr/libexec/managedassetsd`

```diff

-269.0.17.0.0
-  __TEXT.__text: 0xd2bc0
-  __TEXT.__auth_stubs: 0x1e60
-  __TEXT.__objc_stubs: 0x4d80
-  __TEXT.__objc_methlist: 0x2324
-  __TEXT.__const: 0x1df4
-  __TEXT.__cstring: 0xa066
+269.0.19.0.0
+  __TEXT.__text: 0xd3f90
+  __TEXT.__auth_stubs: 0x1e50
+  __TEXT.__objc_stubs: 0x4e40
+  __TEXT.__objc_methlist: 0x2344
+  __TEXT.__const: 0x1e64
+  __TEXT.__cstring: 0xa0e6
   __TEXT.__objc_classname: 0x3a3
-  __TEXT.__objc_methname: 0x686b
-  __TEXT.__oslogstring: 0xa6ff
-  __TEXT.__objc_methtype: 0x1f0e
-  __TEXT.__gcc_except_tab: 0x980
-  __TEXT.__swift5_typeref: 0x8cc
-  __TEXT.__constg_swiftt: 0x900
+  __TEXT.__objc_methname: 0x69bd
+  __TEXT.__oslogstring: 0xac8f
+  __TEXT.__objc_methtype: 0x1f4c
+  __TEXT.__gcc_except_tab: 0x954
+  __TEXT.__swift5_typeref: 0x8d8
+  __TEXT.__constg_swiftt: 0x910
   __TEXT.__swift5_fieldmd: 0xa7c
   __TEXT.__swift5_reflstr: 0xd6d
-  __TEXT.__swift5_proto: 0x118
+  __TEXT.__swift5_proto: 0x11c
   __TEXT.__swift5_types: 0x94
   __TEXT.__swift5_assocty: 0x168
-  __TEXT.__swift5_capture: 0x578
-  __TEXT.__swift_as_entry: 0x2bc
-  __TEXT.__swift_as_ret: 0x2bc
+  __TEXT.__swift5_capture: 0x5b8
+  __TEXT.__swift_as_entry: 0x2d0
+  __TEXT.__swift_as_ret: 0x2b4
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2868
-  __TEXT.__eh_frame: 0x5c38
-  __DATA_CONST.__auth_got: 0xf40
-  __DATA_CONST.__got: 0xa48
+  __TEXT.__unwind_info: 0x2850
+  __TEXT.__eh_frame: 0x5be8
+  __DATA_CONST.__auth_got: 0xf38
+  __DATA_CONST.__got: 0xa58
   __DATA_CONST.__auth_ptr: 0x308
-  __DATA_CONST.__const: 0x2b00
-  __DATA_CONST.__cfstring: 0x4a60
+  __DATA_CONST.__const: 0x2b58
+  __DATA_CONST.__cfstring: 0x4ba0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_intobj: 0x648
+  __DATA_CONST.__objc_intobj: 0x660
   __DATA_CONST.__objc_arraydata: 0x350
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x55e0
-  __DATA.__objc_selrefs: 0x18f8
-  __DATA.__objc_ivar: 0x274
+  __DATA.__objc_const: 0x5630
+  __DATA.__objc_selrefs: 0x1918
+  __DATA.__objc_ivar: 0x27c
   __DATA.__objc_data: 0x8d8
-  __DATA.__data: 0x17b0
-  __DATA.__bss: 0x2580
+  __DATA.__data: 0x1788
+  __DATA.__bss: 0x2600
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B9DA4FEF-1E7E-3933-B4BE-D8BC5CE2C193
-  Functions: 2686
-  Symbols:   919
-  CStrings:  3840
+  UUID: C106CF3A-5D77-359C-832B-815EA4819ADD
+  Functions: 2694
+  Symbols:   920
+  CStrings:  3894
 
Symbols:
+ _$s10Foundation4DateVSQAAMc
+ _$sSis23CustomStringConvertiblesWP
- _$s10Foundation4DateV21timeIntervalSince1970ACSd_tcfC
CStrings:
+ "\t%@ = "
+ " [\n"
+ " lastUpdatedTime:"
+ "%@ (%@)\n"
+ "%@,\n"
+ "%s db: %@ name:%@ auto append updatedDate: %@"
+ "-[MAKVStoreManager checkStoreForUploadWithOption:profile:completionHandler:]"
+ "-[MAKVStoreManager resetKVCloudStateWithProfile:error:]"
+ "-[MAServer processAccountChangedWithSigninUser:signoutUser:accountSwitch:]_block_invoke"
+ "@64@0:8@16@24Q32B40B44B48B52@56"
+ "Account is not available, will schedule upload when it becomes ready. record: %s"
+ "Adding new KVSRecord to be uploaded to local cache. record: %s"
+ "Adding to be deleted AssetRecord: %s to local cache"
+ "Aq"
+ "Asset with handle: %@ label: %@ size:%lu recordName %@ uploaded to cloud"
+ "B36@0:8Q16B24^@28"
+ "Continue propagating KVSRecord sync down to replace current KVSRecord. recordName: %s"
+ "Continue propagating KVSRecord sync down to replace previously downloaded KVSRecord. recordName: %s"
+ "Continue propagating KVSRecord sync down to replace previously uploaded KVSRecord. recordName: %s"
+ "Continue propagating asset sync down to replace current asset. recordName: %s"
+ "Continue propagating asset sync down to replace previously downloaded asset. recordName: %s"
+ "Continue propagating asset sync down to replace previously uploaded asset. recordName: %s"
+ "Date"
+ "Delegate failed to ack zone delete sync down with encryptedDataReset %s"
+ "Delegate notified zone delete sync down with encryptedDataReset %s"
+ "Error unsetting kMASDUploadedToCloudState for assets error=%@"
+ "Populate CKRecord, asset type: %s - %lu, assetData size = %ld"
+ "Saving asset to cloud %s"
+ "Skip KVSRecord sync down as a it was previously uploaded. recordName: %s"
+ "Skip KVSRecord sync down as a previous sync down was processed. recordName: %s"
+ "Skip KVSRecord sync down as cloud delete request is pending. recordName: %s"
+ "Skip KVSRecord sync up as it's not changed yet and already in cloud. recordName: %s"
+ "Skip asset sync down as a it was previously uploaded. recordName: %s"
+ "Skip asset sync down as a previous sync down was processed. recordName: %s"
+ "Skip asset sync down as cloud delete request is pending. recordName: %s"
+ "Skip asset sync up as it's not changed yet and already in cloud. recordName: %s"
+ "Skip forced cloud sync checkup as the last checkup was done in less than 30 min."
+ "TB,R,N,V_isCoreRXDataSharingStore"
+ "Unknown Record Name"
+ "Update to be deleted AssetRecord: %s in local cache"
+ "Update to be deleted KVSRecord: %s in local cache"
+ "Updating existing KVSRecord to be uploaded in local cache: %s"
+ "[%lu bytes],\n"
+ "]\n"
+ "_isCoreRXDataSharingStore"
+ "_lastCloudSyncCheckTimeInterval"
+ "account switch from = %s to %s"
+ "accountChangedWithSigninUser:signoutUser:accountSwitch:"
+ "checkStoreForUploadWithOption:profile:completionHandler:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "deleteData, key: %@"
+ "error: %@"
+ "existing localAsset: %s"
+ "existing localRecord: %s"
+ "existingRecord = %@"
+ "failed to reset syncState for: %@"
+ "initWithName:group:assetType:syncToCloud:hasStaging:hasAutoUpdateTime:isCoreRXDataSharingStore:recordHandleField:"
+ "isCoreRXDataSharingStore"
+ "nil"
+ "processAccountChangedWithSigninUser:signoutUser:accountSwitch:"
+ "putData: %@"
+ "queryData, key: %@ returns: %@"
+ "record SyncDown saved in local cache: %s"
+ "recordHandle is not present in serialized row %s"
+ "resetKVCloudStateWithProfile:error:"
+ "saveAssetFromCloud: %s"
+ "saveDataToCloud:records:updateSyncState:error:"
+ "saveKVSDataFromCloud: %s"
+ "sqlite3_bind Unknown type to string value=%@"
+ "updateData, key: %@ values: %@"
+ "upload KVStore records for ManateeIdentityRecovery"
+ "upload assets for ManateeIdentityRecovery"
+ "upload assets for account sign in .."
+ "uploadOldAssetsWithOption %lu includeKVStoreData:%u"
+ "uploadOldAssetsWithOption:includeKVStoreData:error:"
+ "v36@0:8@\"NSString\"16@\"NSString\"24B32"
+ "v36@0:8@16@24B32"
+ "v40@0:8Q16@24@?32"
- "-[MAKVStoreManager checkStoreForUploadWithOption:completionHandler:]"
- "-[MAKVStoreManager resetKVCloudStateWithError:]"
- "-[MAServer UpdateAsset:uuid:sessionToken:algorithmVersion:completion:]_block_invoke"
- "-[MAServer processAccountChangedWithSigninUser:signoutUser:]_block_invoke"
- "@60@0:8@16@24Q32B40B44B48@52"
- "Account is not available, will schedule upload when it becomes ready. recordName: %s recordHandle: %s"
- "Adding KVSRecord with updated recordName to local cache. recordName: %s"
- "Adding new KVSRecord to be uploaded to local cache. recordName: %s"
- "Asset with handle: %@ recordName %@ uploaded to cloud"
- "Call UpdateAsset by %@"
- "Forcily sync up KVSData without checking local cache. recordHandle: %s recordName: %s"
- "Forcily sync up asset without checking local cache. recordName: %s"
- "Ignore the down sync as record with updated recordName %s already exist"
- "No accountIdentifier found to re-upload local records"
- "No accountIdentifier found to re-upload local records for encryptedDataReset"
- "Populate CKRecord, asset type: %s - %lu"
- "Saving asset to cloud %@"
- "Skip KVSRecord sync up as it's not changed yet. recordName: %s"
- "Skip asset sync up as it's not changed yet. recordName: %s"
- "Updating existing KVSRecord to be uploaded in local cache. recordName: %s"
- "accountChangedWithSigninUser:signoutUser:"
- "existingRecords = %@"
- "fail to cleanup local asset store for asset handle:%@ record: %@, error: %@"
- "initWithName:group:assetType:syncToCloud:hasStaging:hasAutoUpdateTime:recordHandleField:"
- "old record with %s synced down, expected recordName is %s"
- "oldAccountIdentifier = %s"
- "processAccountChangedWithSigninUser:signoutUser:"
- "recordHandle is not present in serilazed row %s"
- "saveAssetFromCloud %s"
- "saveDataToCloud:records:error:"
- "sqlite3_bind unkown type to string value=%@"
- "upload assets belong to no account.."
- "uploadOldAssetsWithOption %lu"
- "uploadOldAssetsWithOption:error:"
- "v32@0:8@\"NSString\"16@\"NSString\"24"

```
