## itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

-4025.200.18.0.0
-  __TEXT.__text: 0x145f68
+4025.300.10.0.0
+  __TEXT.__text: 0x14b148
   __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__objc_stubs: 0x15700
-  __TEXT.__objc_methlist: 0xb484
+  __TEXT.__objc_stubs: 0x15880
+  __TEXT.__objc_methlist: 0xb79c
   __TEXT.__dlopen_cstrs: 0x705
   __TEXT.__const: 0x4f0
-  __TEXT.__oslogstring: 0x297fe
-  __TEXT.__cstring: 0x10b5b
-  __TEXT.__objc_methname: 0x21bdc
+  __TEXT.__oslogstring: 0x2a510
+  __TEXT.__cstring: 0x10e19
+  __TEXT.__objc_methname: 0x221f9
   __TEXT.__constg_swiftt: 0x98
   __TEXT.__swift5_typeref: 0x9c
   __TEXT.__swift5_reflstr: 0x27

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__gcc_except_tab: 0x59d4
-  __TEXT.__objc_classname: 0x2668
-  __TEXT.__objc_methtype: 0x4695
-  __TEXT.__unwind_info: 0x3b20
+  __TEXT.__gcc_except_tab: 0x5a08
+  __TEXT.__objc_classname: 0x26f0
+  __TEXT.__objc_methtype: 0x4703
+  __TEXT.__unwind_info: 0x3c08
   __TEXT.__eh_frame: 0x3e0
   __DATA_CONST.__auth_got: 0xae8
-  __DATA_CONST.__got: 0x1048
+  __DATA_CONST.__got: 0x1050
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x60b0
-  __DATA_CONST.__cfstring: 0xc300
-  __DATA_CONST.__objc_classlist: 0x840
+  __DATA_CONST.__const: 0x60a8
+  __DATA_CONST.__cfstring: 0xc420
+  __DATA_CONST.__objc_classlist: 0x860
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x5f0
-  __DATA_CONST.__objc_intobj: 0xf18
-  __DATA_CONST.__objc_arraydata: 0x2b8
-  __DATA_CONST.__objc_arrayobj: 0x2a0
+  __DATA_CONST.__objc_superrefs: 0x600
+  __DATA_CONST.__objc_intobj: 0xf48
+  __DATA_CONST.__objc_arraydata: 0x2e0
+  __DATA_CONST.__objc_arrayobj: 0x2b8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x16040
-  __DATA.__objc_selrefs: 0x65e8
-  __DATA.__objc_ivar: 0xe2c
-  __DATA.__objc_data: 0x52f8
+  __DATA.__objc_const: 0x16460
+  __DATA.__objc_selrefs: 0x6698
+  __DATA.__objc_ivar: 0xe48
+  __DATA.__objc_data: 0x5438
   __DATA.__data: 0x1228
   __DATA.__bss: 0x560
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C8892000-87B8-329D-86E2-3BA4A442E799
-  Functions: 5090
-  Symbols:   923
-  CStrings:  10896
+  UUID: 1390CE76-CEB3-3CF0-A400-7290C59162C5
+  Functions: 5172
+  Symbols:   924
+  CStrings:  10974
 
Symbols:
+ _ML3AlbumPropertyStoreID
CStrings:
+ "%{public}@ - Got load artwork info request for album persistent ID=: %lld"
+ "%{public}@ - No active account, skipping import album artwork for persistentID: %lld"
+ "%{public}@ - No active locker account, skipping import container artwork for persistentID: %lld"
+ "%{public}@ - Updating availability finished with error %{public}@. update required = %{BOOL}u"
+ "%{public}@ - Updating item availability for saga IDs: [%{public}@}]"
+ "%{public}@ - ignoring deprioritizeAlbumArtworkForPersistentID as we don't have a valid SagaRequestHandler"
+ "%{public}@ - ignoring deprioritizePurchaseHistoryAlbumArtworkForPersistentID as we don't have a valid JaliscoRequestHandler"
+ "%{public}@ - ignoring deprioritizeSubscriptionAlbumArtworkForPersistentID as we don't have a valid SubscriptionRequestHandler"
+ "%{public}@ - ignoring importCloudAlbumArtworkForPersistentID for persistentID %lld as we don't have a valid SagaRequestHandler"
+ "%{public}@ - ignoring importPurchaseHistoryAlbumArtworkForPersistentID as we don't have a valid JaliscoRequestHandler"
+ "%{public}@ - ignoring importSubscriptionAlbumArtworkForPersistentID as we don't have a valid SubscriptionRequestHandler"
+ "%{public}@ - ignoring loadArtworkInfoForAlbumPersistentID as we don't have a valid SagaRequestHandler"
+ "%{public}@ - ignoring loadArtworkInfoForPurchaseHistoryAlbumPersistentID as we don't have a valid JaliscoRequestHandler"
+ "%{public}@ - ignoring loadArtworkInfoForSubscriptionAlbumPersistentID as we don't have a valid SubscriptionRequestHandler"
+ "%{public}@ - ignoring reconcileAvailabilityForItemSagaIDs as we don't have a valid SagaRequestHandler"
+ "%{public}@ Finished reconcile request"
+ "%{public}@ Finished reconcile request error=%{public}@"
+ "%{public}@ Removing old key '%{public}@' with renewalDate %{public}@"
+ "%{public}@ Skipping artwork info operation because the connection has not been set up"
+ "<%@: %p [cloud_id=%llu, artworkType=%lld, sourceType=%lld, variantType=%d]>"
+ "@\"ICReconcileAvailabilityResponse\""
+ "CloudService %p -  Unable to service deprioritizeSubscriptionAlbumArtworkForPersistentID request - error=%{public}@"
+ "CloudService %p -  Unable to service importSubscriptionAlbumArtworkForPersistentID request - error=%{public}@"
+ "CloudService %p -  Unable to service loadArtworkInfoForSubscriptionAlbumPersistentID request - error=%{public}@"
+ "CloudService %p - deprioritizeCloudAlbumArtworkForPersistentID (%llu) - Unable to service cloud library request - error=%{public}@"
+ "CloudService %p - deprioritizePurchaseHistoryAlbumArtworkForPersistentID(%llu) - Unable to service purchase request - error=%{public}@"
+ "CloudService %p - importCloudAlbumArtworkForPersistentID (persistentID=%lld) - Unable to service request - error=%{public}@"
+ "CloudService %p - importPurchaseHistoryAlbumArtworkForPersistentID (persistentID=%lld) - Unable to service request - error=%{public}@"
+ "CloudService %p - loadArtworkInfoForAlbumPersistentID (%lld) - Unable to service cloud library request - error=%{public}@"
+ "CloudService %p - loadArtworkInfoForCloudAlbumPersistentID: - Sending saga album artwork info: %{public}@ - error=%{public}@"
+ "CloudService %p - loadArtworkInfoForPurchaseHistoryAlbumPersistentID (%lld) Unable to service request for purchases - error=%{public}@"
+ "CloudService %p - loadArtworkInfoForPurchaseHistoryAlbumPersistentID: - Sending purchase history screenshot artwork info: %{public}@ - error=%{public}@"
+ "CloudService %p - loadArtworkInfoForSubscriptionAlbumPersistentID: - Sending subscription album artwork info: %{public}@ - error=%{public}@"
+ "CloudService %p - reconcileAvailabilityForItemSagaIDs: Unable to service request - error=%{public}@"
+ "ICReconcileAlbumRespongParserDelegate"
+ "ICReconcileAvailabilityRequest"
+ "ICReconcileAvailabilityResponse"
+ "Migrating to version 720000"
+ "No artwork token for album persistentID = %lld"
+ "No cloud_artwork_token for album persistent id = %llu, variantType = %ld"
+ "No sagaID for album representativeItem persistent id = %lld, variantType = %ld"
+ "SELECT DISTINCT (fetchable_artwork_token), entity_pid FROM best_artwork_token LEFT OUTER JOIN artwork ON fetchable_artwork_token = artwork_token WHERE artwork_token IS NULL AND best_artwork_token.artwork_type = ? AND fetchable_artwork_source_type = ? AND best_artwork_token.artwork_variant_type = ? GROUP BY fetchable_artwork_token"
+ "SELECT DISTINCT (fetchable_artwork_token), store_cloud_id FROM best_artwork_token LEFT OUTER JOIN artwork ON fetchable_artwork_token = artwork_token JOIN container ON entity_pid = container_pid AND entity_type = ? WHERE artwork_token IS NULL AND best_artwork_token.artwork_type = ? AND fetchable_artwork_source_type = ? AND best_artwork_token.artwork_variant_type = ? GROUP BY fetchable_artwork_token"
+ "SELECT DISTINCT (fetchable_artwork_token), store_saga_id, media_type FROM best_artwork_token LEFT OUTER JOIN artwork ON fetchable_artwork_token = artwork_token JOIN item_store ON entity_pid = item_store.item_pid AND entity_type = ? JOIN item USING (item_pid) WHERE artwork_token IS NULL AND best_artwork_token.artwork_type = ? AND fetchable_artwork_source_type = ? AND best_artwork_token.artwork_variant_type = ? GROUP BY fetchable_artwork_token"
+ "SagaReconcileAvailabilityOperation"
+ "SagaReconcileAvailabilityOperationSagaIDListKey"
+ "Skipping library update because we have custom playlist cover artwork"
+ "_reconcileAvailabilityResponse"
+ "album cloud"
+ "album cloud (subscription)"
+ "com.apple.itunescloudd.SagaRequestHandler.reconcileAlbumAvailabilityOperation"
+ "databases/%u/process"
+ "deprioritizeAlbumArtworkForPersistentID:"
+ "deprioritizeCloudAlbumArtworkForPersistentID:"
+ "deprioritizeCloudAlbumArtworkForPersistentID:configuration:"
+ "deprioritizePurchaseHistoryAlbumArtworkForPersistentID:"
+ "deprioritizePurchaseHistoryAlbumArtworkForPersistentID:configuration:"
+ "deprioritizeSubscriptionAlbumArtworkForPersistentID:"
+ "deprioritizeSubscriptionAlbumArtworkForPersistentID:configuration:"
+ "importAlbumArtworkForPersistentID:artworkVariantType:clientIdentity:completionHandler:"
+ "importAlbumArtworkForPersistentID:variantType:clientIdentity:completionHandler:"
+ "importCloudAlbumArtworkForPersistentID:artworkVariantType:clientIdentity:completionHandler:"
+ "importCloudAlbumArtworkForPersistentID:artworkVariantType:configuration:completion:"
+ "importContainerArtworkForPersistentID:artworkVariantType:clientIdentity:completionHandler:"
+ "importPurchaseHistoryAlbumArtworkForPersistentID:artworkVariantType:configuration:completion:"
+ "importPurchaseHistoryAlbumArtworkForPersistentID:variantType:clientIdentity:completionHandler:"
+ "importSubscriptionAlbumArtworkForPersistentID:artworkVariantType:clientIdentity:completionHandler:"
+ "importSubscriptionAlbumArtworkForPersistentID:artworkVariantType:configuration:completion:"
+ "importSubscriptionContainerArtworkForPersistentID:artworkVariantType:configuration:completion:"
+ "initWithDatabaseID:sagaIDs:"
+ "loadArtworkInfoForAlbumPersistentID:clientIdentity:completionHandler:"
+ "loadArtworkInfoForCloudAlbumPersistentID:configuration:completion:"
+ "loadArtworkInfoForPurchaseHistoryAlbumPersistentID:clientIdentity:completionHandler:"
+ "loadArtworkInfoForPurchaseHistoryAlbumPersistentID:configuration:completion:"
+ "loadArtworkInfoForSubscriptionAlbumPersistentID:clientIdentity:completionHandler:"
+ "loadArtworkInfoForSubscriptionAlbumPersistentID:configuration:completion:"
+ "reconcileAvailabilityForItemSagaIDs:clientIdentity:completion:"
+ "reconcileAvailabilityForItemSagaIDs:configuration:completion:"
+ "representativeArtworkItemForAlbumPersistentID:artworkSourceType:"
+ "v40@0:8q16@\"ICConnectionConfiguration\"24@?<v@?@\"NSError\"@\"NSDictionary\">32"
+ "{\"version\":\"0.0\"}"
- "%{public}@ Adding 3x4 variant entry for artwork token '%{public}@"
- "%{public}@ Artwork info does not contain any variants - skipping adding to db"
- "%{public}@ No existing entries for token '%{public}@' - not adding variants"
- "<%@: %p [cloud_id=%llu, artworkType=%lld, sourceType=%lld]>"
- "SELECT DISTINCT (fetchable_artwork_token), store_cloud_id FROM best_artwork_token LEFT OUTER JOIN artwork ON fetchable_artwork_token = artwork_token JOIN container ON entity_pid = container_pid AND entity_type = ? WHERE artwork_token IS NULL AND best_artwork_token.artwork_type = ? AND fetchable_artwork_source_type = ? GROUP BY fetchable_artwork_token"
- "SELECT DISTINCT (fetchable_artwork_token), store_saga_id, media_type FROM best_artwork_token LEFT OUTER JOIN artwork ON fetchable_artwork_token = artwork_token JOIN item_store ON entity_pid = item_store.item_pid AND entity_type = ? JOIN item USING (item_pid) WHERE artwork_token IS NULL AND best_artwork_token.artwork_type = ? AND fetchable_artwork_source_type = ? GROUP BY fetchable_artwork_token"
- "SELECT entity_pid, entity_type, artwork_variant_type from artwork_token WHERE artwork_token = ? AND artwork_source_type = ? AND artwork_type = ?"
- "_populateAvailableVariantsIfNeeded"
- "importArtworkTokenForEntityPersistentID:entityType:artworkToken:artworkType:sourceType:variantType:usingConnection:"
- "importContainerArtworkForPersistentID:clientIdentity:completionHandler:"
- "importSubscriptionContainerArtworkForPersistentID:configuration:completion:"
- "updateBestArtworkTokenForEntityPersistentID:entityType:artworkType:variantType:retrievalTime:preserveExistingAvailableToken:usingConnection:"

```
