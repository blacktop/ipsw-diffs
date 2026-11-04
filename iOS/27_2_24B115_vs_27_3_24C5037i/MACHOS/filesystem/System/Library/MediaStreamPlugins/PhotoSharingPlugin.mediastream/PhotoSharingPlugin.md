## PhotoSharingPlugin

> `/System/Library/MediaStreamPlugins/PhotoSharingPlugin.mediastream/PhotoSharingPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-916.57.153.0.0
-  __TEXT.__text: 0x4008
-  __TEXT.__auth_stubs: 0x290
+920.7.110.0.0
+  __TEXT.__text: 0x4458
+  __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_stubs: 0xae0
   __TEXT.__objc_methlist: 0x82c
   __TEXT.__const: 0x38
   __TEXT.__objc_methname: 0x2035
-  __TEXT.__oslogstring: 0xcd8
+  __TEXT.__oslogstring: 0xeea
   __TEXT.__cstring: 0x25
   __TEXT.__objc_classname: 0x3b
   __TEXT.__objc_methtype: 0xdb3

   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__auth_got: 0x160
   __DATA_CONST.__got: 0xd0
   __DATA.__objc_const: 0x5f0
   __DATA.__objc_selrefs: 0x698

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 53
-  Symbols:   75
+  Symbols:   77
   CStrings:  361
 
Symbols:
+ _PLCurrentLibraryLogTag
+ _objc_retain_x26
CStrings:
+ "%{public}s calling PLCloudSharedAssetSaveJob processMetadataFromClientProcessForAssetCollections:%@ inAlbum:%@ personID:%@"
+ "%{public}s%@ %@"
+ "%{public}s%@ %@ %@"
+ "%{public}s%@ %@ %@ album %@"
+ "%{public}s%@ %@ %@ album %@ info %@"
+ "%{public}s%@ %@ %@ error:%@"
+ "%{public}s%@ : MSASPersonIDForPollingTriggeredByPushNotification returning %@"
+ "%{public}s%@ Failed to add asset collection %@ toAlbum:%@ error:%@"
+ "%{public}s%@ MSASModel:didFindNewAssetCollections:%@ inAlbum:%@ info:%@"
+ "%{public}s%@ MSASModel:didFinishRetrievingAsset:(collectionGUID:%@)%@ inAlbum:%@ error:%@"
+ "%{public}s%@ deleting album with GUID %@ inviterAddress %@"
+ "%{public}s%@(Last-viewed management): currentLastViewedCommentDate %@ didFindLastViewedCommentDate %@ forAssetCollection:%@ inAlbum:%@"
+ "%{public}s%@(Last-viewed management): didMarkAlbum %@ asHavingUnreadContent:%i"
+ "%{public}s%@(Last-viewed management): didMarkAssetCollection %@ asHavingUnreadComments:%i inAlbum:%@"
+ "%{public}s%@(Last-viewed management): didUpdateUnviewedAssetCollectionCount %i forAlbum:%@"
+ "%{public}s%@: didFindGlobalResetSyncInfo %@"
+ "%{public}s%@: didFinishCheckingForChangesInfo %@ Error %@"
+ "%{public}s(server-configuration) MSASModelDidReceiveNewServerSideConfiguration %@"
+ "%{public}s===== IMPLEMENT ME ====="
+ "%{public}sERROR : couldn't copy MMCS transient file %@ to inflight file %@: %@"
+ "%{public}sERROR : couldn't create a path to store inflight file for %@"
+ "%{public}sERROR: asset path is nil"
+ "%{public}sERROR: can't proceed because we don't have an assetCollection for collectionGUID %@"
+ "%{public}sERROR: unable to find asset collection for GUID %@, skipping saving"
+ "%{public}sIgnoring new album because shared streams has been explicitly disabled by user"
+ "%{public}sInflight file already exists at %@. We have re-downloaded the same asset."
+ "%{public}sMSASModel:didFindAccessControlChange:%@ inAlbum:%@ with infoDict:%@"
+ "%{public}sMSASModel:didFindDeletedAccessControl:%@ inAlbum:%@ with infoDict:%@"
+ "%{public}sMSASModel:didFindDeletedInvitation:%@ with infoDict:%@"
+ "%{public}sMSASModel:didFindInvitationChange:%@ with infoDict:%@"
+ "%{public}sMSASModel:didFindNewAccessControls:%@ inAlbum:%@ with infoDict:%@"
+ "%{public}sMSASModel:didFindNewInvitation:%@ with infoDict:%@"
+ "%{public}sMSASModel:didFinishAddingAssetCollection:%@ toAlbum:%@ error:%@"
+ "%{public}sMSASModel:didFinishSendingInvitationByPhone:%@ inAlbum:%@ info:%@ error:%@"
+ "%{public}sMSASModel:didRequestDerivativesForAssetCollections:%@ \n specifications:%@ \n info %@"
+ "%{public}sMSASModelWillBeForgotten personID %@"
+ "%{public}sMaster asset at path %@ no longer exists, skipping"
+ "%{public}sUnknown derivative specification: %@"
+ "%{public}sWarning: got an MSASCollection with more than one asset, will select last one"
+ "%{public}sabout to PLCloudSharedAssetSaveJob deleteCloudSharedAssetsWithCloudGUIDs %@ inAlbum:%@"
+ "%{public}sabout to PLCloudSharedAssetSaveJob saveCloudSharedAssetAtPath %@ collectionGUID %@  guidOfCurrentAssetInCollection %@ albumGUID %@"
+ "%{public}sabout to PLCloudSharedCommentsJob locallyProcessDeletedComments %@"
+ "%{public}sabout to call completionBlock with computedAssetCollections %@ rejectedAssetCollections %@ info %@ elapsed time %f"
+ "%{public}sdelegatePluginForPersonID invoked with nil personID"
+ "%{public}sdelegatePluginForPersonID returning plugin %@ for personID %@"
+ "%{public}sdidDeleteAllCommentsForAssetCollection %@ inAlbum: %@"
+ "%{public}sdidFindCommentChange %@ inAssetCollection:%@ inAlbum: %@"
+ "%{public}sdidFindDeletedComments %@ forAssetCollection:%@ inAlbum: %@ info:%@"
+ "%{public}sdidFindNewComments %@ forAssetCollection:%@ inAlbum: %@ info:%@"
+ "%{public}sfailed to open library: %@"
+ "%{public}snotify_cancel() failed for kMSASFileTransferPushTimerDidEndNotification. (%d)"
+ "%{public}snotify_cancel() failed for kMSASFileTransferPushTimerDidStartNotification. (%d)"
+ "%{public}swe just enqueued collection GUID %@, skipping"
- " calling PLCloudSharedAssetSaveJob processMetadataFromClientProcessForAssetCollections:%@ inAlbum:%@ personID:%@"
- "%@ %@"
- "%@ %@ %@"
- "%@ %@ %@ album %@"
- "%@ %@ %@ album %@ info %@"
- "%@ %@ %@ error:%@"
- "%@ : MSASPersonIDForPollingTriggeredByPushNotification returning %@"
- "%@ Failed to add asset collection %@ toAlbum:%@ error:%@"
- "%@ MSASModel:didFindNewAssetCollections:%@ inAlbum:%@ info:%@"
- "%@ MSASModel:didFinishRetrievingAsset:(collectionGUID:%@)%@ inAlbum:%@ error:%@"
- "%@ deleting album with GUID %@ inviterAddress %@"
- "%@(Last-viewed management): currentLastViewedCommentDate %@ didFindLastViewedCommentDate %@ forAssetCollection:%@ inAlbum:%@"
- "%@(Last-viewed management): didMarkAlbum %@ asHavingUnreadContent:%i"
- "%@(Last-viewed management): didMarkAssetCollection %@ asHavingUnreadComments:%i inAlbum:%@"
- "%@(Last-viewed management): didUpdateUnviewedAssetCollectionCount %i forAlbum:%@"
- "%@: didFindGlobalResetSyncInfo %@"
- "%@: didFinishCheckingForChangesInfo %@ Error %@"
- "(server-configuration) MSASModelDidReceiveNewServerSideConfiguration %@"
- "===== IMPLEMENT ME ====="
- "ERROR : couldn't copy MMCS transient file %@ to inflight file %@: %@"
- "ERROR : couldn't create a path to store inflight file for %@"
- "ERROR: asset path is nil"
- "ERROR: can't proceed because we don't have an assetCollection for collectionGUID %@"
- "ERROR: unable to find asset collection for GUID %@, skipping saving"
- "Ignoring new album because shared streams has been explicitly disabled by user"
- "Inflight file already exists at %@. We have re-downloaded the same asset."
- "MSASModel:didFindAccessControlChange:%@ inAlbum:%@ with infoDict:%@"
- "MSASModel:didFindDeletedAccessControl:%@ inAlbum:%@ with infoDict:%@"
- "MSASModel:didFindDeletedInvitation:%@ with infoDict:%@"
- "MSASModel:didFindInvitationChange:%@ with infoDict:%@"
- "MSASModel:didFindNewAccessControls:%@ inAlbum:%@ with infoDict:%@"
- "MSASModel:didFindNewInvitation:%@ with infoDict:%@"
- "MSASModel:didFinishAddingAssetCollection:%@ toAlbum:%@ error:%@"
- "MSASModel:didFinishSendingInvitationByPhone:%@ inAlbum:%@ info:%@ error:%@"
- "MSASModel:didRequestDerivativesForAssetCollections:%@ \n specifications:%@ \n info %@"
- "MSASModelWillBeForgotten personID %@"
- "Master asset at path %@ no longer exists, skipping"
- "Unknown derivative specification: %@"
- "Warning: got an MSASCollection with more than one asset, will select last one"
- "about to PLCloudSharedAssetSaveJob deleteCloudSharedAssetsWithCloudGUIDs %@ inAlbum:%@"
- "about to PLCloudSharedAssetSaveJob saveCloudSharedAssetAtPath %@ collectionGUID %@  guidOfCurrentAssetInCollection %@ albumGUID %@"
- "about to PLCloudSharedCommentsJob locallyProcessDeletedComments %@"
- "about to call completionBlock with computedAssetCollections %@ rejectedAssetCollections %@ info %@ elapsed time %f"
- "delegatePluginForPersonID invoked with nil personID"
- "delegatePluginForPersonID returning plugin %@ for personID %@"
- "didDeleteAllCommentsForAssetCollection %@ inAlbum: %@"
- "didFindCommentChange %@ inAssetCollection:%@ inAlbum: %@"
- "didFindDeletedComments %@ forAssetCollection:%@ inAlbum: %@ info:%@"
- "didFindNewComments %@ forAssetCollection:%@ inAlbum: %@ info:%@"
- "failed to open library: %@"
- "notify_cancel() failed for kMSASFileTransferPushTimerDidEndNotification. (%d)"
- "notify_cancel() failed for kMSASFileTransferPushTimerDidStartNotification. (%d)"
- "we just enqueued collection GUID %@, skipping"
```
