## ShazamInsights

> `/System/Library/PrivateFrameworks/ShazamInsights.framework/Versions/A/ShazamInsights`

```diff

-307.2.0.0.0
-  __TEXT.__text: 0xc5d4
+318.0.0.0.0
+  __TEXT.__text: 0xc604
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0xb84
+  __TEXT.__objc_methlist: 0xd00
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0xb66
   __TEXT.__gcc_except_tab: 0xb0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8e0
+  __DATA_CONST.__objc_selrefs: 0x978
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__const: 0x6d0
   __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0x22a0
+  __AUTH_CONST.__objc_const: 0x2000
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D3E265A2-3169-39E4-8FED-DBCE2CBC52AC
-  Functions: 282
-  Symbols:   983
+  UUID: C6355A9F-4333-37A0-998C-44FEB0119519
+  Functions: 286
+  Symbols:   987
   CStrings:  719
 
Symbols:
+ +[SHClusterQuery artistsCluster].cold.1
+ +[SHClusterQuery tracksCluster].cold.1
+ +[SHInsightsConfiguration bagContract].cold.1
+ +[SHInsightsConfiguration fetchSharedInstanceWithCompletion:].cold.1
Functions:
~ -[SHClusterLoader loadFromURL:type:storefront:reuseExistingData:completion:] : 648 -> 644
~ ___89+[SHAffinityGroupQuery affinityGroupsForLocation:atDate:configuration:completionHandler:]_block_invoke : 312 -> 352
~ ___89+[SHAffinityGroupQuery affinityGroupsForLocation:atDate:configuration:completionHandler:]_block_invoke_2 : 324 -> 348
~ -[SHJSONLClusterImporter loadDataFromFileInfo:withMetadata:toDestinationURL:error:] : 636 -> 620
~ +[SHClusterQuery artistsCluster] : 84 -> 68
~ +[SHClusterQuery tracksCluster] : 84 -> 68
~ +[SHSQLiteUtils runSQL:onDatabase:replacingTokens:withObjects:rowHandler:error:] : 928 -> 908
~ +[SHClusterMetadataQuery writeMetadata:toDatabaseAtLocation:error:] : 976 -> 972
~ -[SHClusterJSONLReader importClusters:toParentCluster:startIndex:] : 864 -> 856
~ +[SHInsightsConfiguration fetchSharedInstanceWithCompletion:] : 308 -> 292
~ +[SHInsightsConfiguration bagContract] : 84 -> 68
~ -[SHClusterStatementRunner mediaItemsAtCohesionLevel:forQueryMediaIDs:filteredBySeedMediaIDs:error:] : 996 -> 1008
~ -[SHSQLiteClusterImporter loadDataFromFileInfo:withMetadata:toDestinationURL:error:] : 584 -> 592

```
