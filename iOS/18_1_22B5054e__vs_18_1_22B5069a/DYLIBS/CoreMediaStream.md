## CoreMediaStream

> `/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream`

```diff

-710.22.200.0.0
-  __TEXT.__text: 0xbdf60
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x63b8
-  __TEXT.__const: 0x22b
-  __TEXT.__gcc_except_tab: 0x2738
-  __TEXT.__cstring: 0x9e24
-  __TEXT.__oslogstring: 0xe564
+712.0.160.0.0
+  __TEXT.__text: 0xc0c0c
+  __TEXT.__auth_stubs: 0xfb0
+  __TEXT.__objc_methlist: 0x6478
+  __TEXT.__const: 0x223
+  __TEXT.__gcc_except_tab: 0x2a14
+  __TEXT.__cstring: 0x9f79
+  __TEXT.__oslogstring: 0xe8dd
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x2828
+  __TEXT.__unwind_info: 0x28b0
   __TEXT.__objc_classname: 0x813
-  __TEXT.__objc_methname: 0x12475
-  __TEXT.__objc_methtype: 0x41e4
-  __TEXT.__objc_stubs: 0xc3c0
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__const: 0x20d8
+  __TEXT.__objc_methname: 0x12977
+  __TEXT.__objc_methtype: 0x4265
+  __TEXT.__objc_stubs: 0xc860
+  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__const: 0x2278
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3be8
+  __DATA_CONST.__objc_selrefs: 0x3d10
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1c0
-  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH_CONST.__auth_got: 0x7e8
   __AUTH_CONST.__const: 0x890
-  __AUTH_CONST.__cfstring: 0x7e60
-  __AUTH_CONST.__objc_const: 0xa5e8
+  __AUTH_CONST.__cfstring: 0x8040
+  __AUTH_CONST.__objc_const: 0xa648
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x650

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3257
-  Symbols:   4066
-  CStrings:  5199
+  Functions: 3284
+  Symbols:   4104
+  CStrings:  5269
 
Symbols:
+ _CKErrorDomain
+ _OBJC_CLASS_$_CKContainer
+ _OBJC_CLASS_$_CKContainerID
+ _OBJC_CLASS_$_CKContainerOptions
+ _OBJC_CLASS_$_CKFetchRecordsOperation
+ _OBJC_CLASS_$_CKOperationConfiguration
+ _OBJC_CLASS_$_CKRecordID
+ _OBJC_CLASS_$_CKRecordZoneID
+ __os_feature_enabled_impl
+ _kMSASModelSetMigrationMarkerFn
+ _kMSASPVMigrationMarkerKey
CStrings:
+ "%!{(MISSING)public}@: Album %!{(MISSING)public}@ publicURLString needs to be refetched through another albumsummary request now that we have a clientOrgKey for the album."
+ "%!{(MISSING)public}@: Encountered invalid/missing clientOrgKey error. Fetching new clientOrgKey for album: %!{(MISSING)public}@. Not retrying. Error: %!{(MISSING)public}@"
+ "%!{(MISSING)public}@: Fetched migrationCtag: %!{(MISSING)public}@"
+ "%!{(MISSING)public}@: Finished retrieving album summary for album %!{(MISSING)public}@. Error: %!{(MISSING)public}@ Response: %!{(MISSING)private}@"
+ "%!{(MISSING)public}@: Finished retrieving clientOrgKey for zoneName %!{(MISSING)public}@. Account is in DBR. Error: %!{(MISSING)public}@"
+ "%!{(MISSING)public}@: Invalid/missing clientOrgKey in request. Client must fetch new clientOrgKey for album."
+ "%!{(MISSING)public}@: Missing one of zoneName: %!{(MISSING)public}@ recordId: %!{(MISSING)public}@ fieldName:%!{(MISSING)public}@. Account may not be in DBR."
+ "@40@0:8@16@24#32"
+ "DBRMetadata"
+ "ERROR_MSAS_PROT_INVALID_CLIENTORGKEY"
+ "Failed to fetch userRecord: %!@(MISSING)"
+ "Fetched userRecord: %!@(MISSING)"
+ "Invalid zoneID for zoneName: %!@(MISSING)"
+ "No valid userRecord for recordID: %!@(MISSING)"
+ "Photos"
+ "SharedAlbumsDBR"
+ "SharedAlbumsInfo"
+ "Unexpected object instead of encrypted data for %!{(MISSING)public}@.%!{(MISSING)public}@: %!{(MISSING)public}@"
+ "_actionDidFinishWithError:album:"
+ "_decryptedObjectForRecord:forKey:validateClass:"
+ "_fetchClientOrgKeyAndPersistLocallyForResponseDict:isOwned:completionHandler:"
+ "_fetchRecordWithRecordID:zoneName:fieldName:ownerUserID:isOwned:completionHandler:"
+ "_setClientOrgKeyForRequestBody:clientOrgKey:"
+ "addOperation:"
+ "base64EncodedStringWithOptions:"
+ "clientOrgKeyForRecordID:zoneName:ownerUserID:personID:"
+ "com.apple.icloud-photos.fdb"
+ "com.apple.sharedstreams"
+ "dbrMetadataInfo"
+ "encryptedValues"
+ "fetchClientOrgKeyForRecordID:zoneName:fieldName:ownerUserID:isOwned:completionHandler:"
+ "fetchMigrationCtag"
+ "fieldName"
+ "getChangesRootCtag:migrationCtag:completionBlock:"
+ "initWithContainerID:options:"
+ "initWithContainerIdentifier:environment:"
+ "initWithRecordIDs:"
+ "initWithRecordName:zoneID:"
+ "initWithZoneName:ownerName:"
+ "isSubclassOfClass:"
+ "migrationCtag"
+ "migrationCtagToCheckForChanges"
+ "migrationMarker"
+ "migrationctag"
+ "modelSetMigrationMarkerFn"
+ "ownerCkUserId"
+ "pendingMigration"
+ "privateCloudDatabase"
+ "recordId"
+ "recordName"
+ "recordType"
+ "requiresretrywithclientorgkey"
+ "setApplicationBundleIdentifierOverrideForContainerAccess:"
+ "setApplicationBundleIdentifierOverrideForNetworkAttribution:"
+ "setApplicationBundleIdentifierOverrideForPushTopicGeneration:"
+ "setClientOrgKey:forAlbumWithGUID:"
+ "setClientOrgKey:forAlbumWithGUID:info:"
+ "setClientOrgKey:forAlbumWithGUID:personID:"
+ "setClientOrgKey:forAlbumWithGUID:personID:info:"
+ "setConfiguration:"
+ "setContainer:"
+ "setDesiredKeys:"
+ "setFetchRecordsCompletionBlock:"
+ "setMigrationMarker:"
+ "setMigrationMarker:personID:"
+ "sharedCloudDatabase"
+ "v24@?0@\"CKRecord\"8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32"
+ "v52@?0@\"NSError\"8B16@\"NSArray\"20B28@\"MSASAlbum\"32@\"NSString\"40B48"
+ "v60@0:8@16@24@32@40B48@?52"
+ "waitUntilFinished"
- "%!{(MISSING)public}@: Finished retrieving album summary for album %!{(MISSING)public}@. Error: %!{(MISSING)public}@"
- "getChangesRootCtag:completionBlock:"
- "v48@?0@\"NSError\"8B16@\"NSArray\"20B28@\"MSASAlbum\"32@\"NSString\"40"

```
