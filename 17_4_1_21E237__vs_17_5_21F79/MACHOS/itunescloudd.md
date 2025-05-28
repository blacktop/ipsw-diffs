## itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

-4023.510.1.0.0
-  __TEXT.__text: 0x1282ec
-  __TEXT.__auth_stubs: 0x1290
-  __TEXT.__objc_stubs: 0x146a0
-  __TEXT.__objc_methlist: 0x9548
+4023.610.4.0.0
+  __TEXT.__text: 0x128c34
+  __TEXT.__auth_stubs: 0x12a0
+  __TEXT.__objc_stubs: 0x14760
+  __TEXT.__objc_methlist: 0x9678
   __TEXT.__const: 0x1e8
-  __TEXT.__gcc_except_tab: 0x30dc
-  __TEXT.__oslogstring: 0x25d4f
-  __TEXT.__objc_classname: 0x249c
-  __TEXT.__objc_methname: 0x1f48d
+  __TEXT.__gcc_except_tab: 0x3108
+  __TEXT.__oslogstring: 0x25f56
+  __TEXT.__objc_classname: 0x249e
+  __TEXT.__objc_methname: 0x1f85d
   __TEXT.__objc_methtype: 0x4098
-  __TEXT.__cstring: 0xef51
+  __TEXT.__cstring: 0xefb7
   __TEXT.__dlopen_cstrs: 0x6b8
-  __TEXT.__unwind_info: 0x3640
+  __TEXT.__unwind_info: 0x3678
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x958
+  __DATA_CONST.__auth_got: 0x960
   __DATA_CONST.__got: 0xa08
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x56d8
-  __DATA_CONST.__cfstring: 0xb660
+  __DATA_CONST.__const: 0x57a8
+  __DATA_CONST.__cfstring: 0xb640
   __DATA_CONST.__objc_classlist: 0x7d8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_classrefs: 0xd70
+  __DATA_CONST.__objc_classrefs: 0xd80
   __DATA_CONST.__objc_superrefs: 0x588
-  __DATA_CONST.__objc_intobj: 0xd98
+  __DATA_CONST.__objc_intobj: 0xde0
   __DATA_CONST.__objc_arraydata: 0x288
   __DATA_CONST.__objc_arrayobj: 0x258
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x162a0
-  __DATA.__objc_selrefs: 0x5da8
-  __DATA.__objc_ivar: 0xca4
+  __DATA.__objc_const: 0x16428
+  __DATA.__objc_selrefs: 0x5e58
+  __DATA.__objc_ivar: 0xcc4
   __DATA.__objc_data: 0x4e70
   __DATA.__data: 0xfd0
   __DATA.__bss: 0x3a0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4564
-  Symbols:   834
-  CStrings:  8725
+  Functions: 4590
+  Symbols:   837
+  CStrings:  8775
 
Symbols:
+ _OBJC_CLASS_$_AMSAccountCachedServerData
+ _OBJC_CLASS_$_AMSAccountIdentity
+ _div
CStrings:
+ "\x02\x19"
+ "%{public}@ - _updateAccountServerCachedData caching isU18 value of %{BOOL}u for account %{public}@"
+ "%{public}@ - _updateAccountServerCachedData failed to load active account. err=%{public}@"
+ "%{public}@ Fetched last batch of items - performing import"
+ "%{public}@ Import completed"
+ "%{public}@ Import completed error=%{public}@"
+ "%{public}@ Import was cancelled - returning"
+ "%{public}@ Importing tracks up to revision %u. onDiskRevision=%u, supportsPagination=%{BOOL}u"
+ "%{public}@ Sending items request %{public}@ on connection %{public}@"
+ "%{public}@ Server requested restart. restartCount=%u"
+ "%{public}@ received response: %{public}@"
+ "%{public}@ received response: %{public}@ error=%{public}@"
+ "7"
+ "<%@ %p [identity=%@, revision %u --> %u]>"
+ "@16@?0@8"
+ "Failed to load U18 account value from account %{public}@ error=%{public}@"
+ "Failed to load properties for identity %{public}@ error=%{public}@"
+ "JaliscoPagination"
+ "T@\"NSMutableArray\",&,N,V_itemsFiles"
+ "T@\"NSObject<OS_tcc_identity>\",&,N,V_clientIdentity"
+ "T@\"NSString\",&,N,V_currentPaginationToken"
+ "T@\"NSString\",&,N,V_updateBaseDirectory"
+ "TB,N,V_shouldRestart"
+ "TI,N,V_currentPageNumber"
+ "TI,N,V_restartCount"
+ "TI,N,V_updateFromRevision"
+ "TI,N,V_updateToRevision"
+ "Update complete"
+ "Update complete error=%{public}@"
+ "_currentPageNumber"
+ "_importTracksFromRevision:toRevision:withItemsResponse:clientIdentity:itemsFiles:"
+ "_itemsFiles"
+ "_performNextItemsPageRequestWithCompletion:"
+ "_processItemsPageResponse:withCompletion:"
+ "_restartCount"
+ "_updateAccountServerCachedData"
+ "_updateBaseDirectory"
+ "_updateFromRevision"
+ "_updateToRevision"
+ "activeStoreAccountWithError:"
+ "boolForKey:accountID:updateBlock:"
+ "cancelUpdatesForToken:"
+ "com.apple.itunescloudd.artworkimporter.artworkColorAnalysisAccessQueue"
+ "currentPageNumber"
+ "getPlayActivityEvents:storeAccountID:limit:returningError:"
+ "ic_altDSID"
+ "initWithDSID:altDSID:"
+ "itemsFiles"
+ "requestWithDatabaseID:metadataFilter:queryFilter:purchaseTokens:includeHiddenItems:includePreorders:paginationToken:"
+ "restartCount"
+ "resultWithTimeout:completion:"
+ "setCachedU18MinorAccountStatus:"
+ "setCurrentPageNumber:"
+ "setCurrentPaginationToken:"
+ "setItemsFiles:"
+ "setRestartCount:"
+ "setShouldRestart:"
+ "setUpdateBaseDirectory:"
+ "setUpdateFromRevision:"
+ "setUpdateToRevision:"
+ "updateBaseDirectory"
+ "updateFromRevision"
+ "updateLibraryFromRevision:toRevision:withResponse:clientIdentity:itemsFiles:"
+ "updateToRevision"
+ "v24@?0@\"<AMSAccountCachedServerBool>\"8@\"NSError\"16"
- "\x02\x1a"
- "%{public}@ Could not set store_saga_id for track with adamID=%lld as cloudid=%{public}@ is not a number"
- "%{public}@ Could not set store_saga_id=%lld for track with persistentID=%lld. Error=%{public}@"
- "Fetching tracks failed with error: %{public}@"
- "Sending items request <%{public}@: %p method=%{public}@ action=%{public}@> on connection: <%{public}@ %p>"
- "T@\"NSMutableArray\",&,N,V_artworkAssets"
- "UPDATE item_store SET store_saga_id=?, cloud_in_my_library=? WHERE item_pid=?"
- "_artworkAssets"
- "_importTracksFromRevision:toRevision:withItemsResponse:clientIdentity:"
- "_trackPidsMatchingRequestStoreID"
- "artworkAssets"
- "getPlayActivityEvents:storeAccountID:returningError:"
- "items.daap"
- "setArtworkAssets:"
- "updateLibraryFromRevision:toRevision:withResponse:clientIdentity:"

```
