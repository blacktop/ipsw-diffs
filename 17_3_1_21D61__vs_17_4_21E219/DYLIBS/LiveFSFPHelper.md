## LiveFSFPHelper

> `/System/Library/PrivateFrameworks/LiveFSFPHelper.framework/LiveFSFPHelper`

```diff

-208.80.5.0.0
+208.100.36.0.3
   __TEXT.__text: 0x1c78c
   __TEXT.__auth_stubs: 0x730
   __TEXT.__objc_methlist: 0x1044

   __TEXT.__cstring: 0x1789
   __TEXT.__unwind_info: 0x81c
   __TEXT.__objc_classname: 0x2dc
-  __TEXT.__objc_methname: 0x420d
+  __TEXT.__objc_methname: 0x4277
   __TEXT.__objc_methtype: 0x1053
   __TEXT.__objc_stubs: 0x2940
   __DATA_CONST.__got: 0x100

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3728
   __DATA_CONST.__objc_selrefs: 0xd78
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__objc_const: 0x678
   __AUTH_CONST.__cfstring: 0x480

   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x3a8
   __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x178
-  __DATA.__objc_superrefs: 0x60
   __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x540
   __DATA.__bss: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 64B9F80A-3D0F-3A56-A21B-349BD2211F11
+  UUID: 05B1C945-ED66-3584-9D01-3E30A66182E1
   Functions: 616
   Symbols:   2216
-  CStrings:  1281
+  CStrings:  1283
 
Symbols:
+ ___57-[LiveFSFPExtensionHelper itemForIdentifierLocked:error:]_block_invoke.213
+ ___62-[LiveFSFPExtensionHelper itemAtPathLocked:parent:cachedOnly:]_block_invoke.216
+ ___67-[LiveFSFPExtensionHelper disconnectWithOptions:completionHandler:]_block_invoke.250
+ ___67-[LiveFSFPExtensionHelper disconnectWithOptions:completionHandler:]_block_invoke.250.cold.1
+ ___69-[LiveFSFPExtensionHelper trashItemWithIdentifier:completionHandler:]_block_invoke.237
+ ___94-[LiveFSFPExtensionHelper untrashItemWithIdentifier:toParentItemIdentifier:completionHandler:]_block_invoke.238
+ ___94-[LiveFSFPExtensionHelper untrashItemWithIdentifier:toParentItemIdentifier:completionHandler:]_block_invoke.238.cold.1
- ___57-[LiveFSFPExtensionHelper itemForIdentifierLocked:error:]_block_invoke.212
- ___62-[LiveFSFPExtensionHelper itemAtPathLocked:parent:cachedOnly:]_block_invoke.215
- ___67-[LiveFSFPExtensionHelper disconnectWithOptions:completionHandler:]_block_invoke.249
- ___67-[LiveFSFPExtensionHelper disconnectWithOptions:completionHandler:]_block_invoke.249.cold.1
- ___69-[LiveFSFPExtensionHelper trashItemWithIdentifier:completionHandler:]_block_invoke.235
- ___94-[LiveFSFPExtensionHelper untrashItemWithIdentifier:toParentItemIdentifier:completionHandler:]_block_invoke.237
- ___94-[LiveFSFPExtensionHelper untrashItemWithIdentifier:toParentItemIdentifier:completionHandler:]_block_invoke.237.cold.1
CStrings:
+ "T@\"NSArray\",?,R,C"
+ "T@\"NSData\",?,R,C,N"
+ "T@\"NSData\",?,R,N"
+ "T@\"NSDate\",?,R,C,N"
+ "T@\"NSDictionary\",?,R,N"
+ "T@\"NSError\",?,R,C,N"
+ "T@\"NSFileProviderItemVersion\",?,R,N"
+ "T@\"NSNumber\",?,R,C"
+ "T@\"NSNumber\",?,R,C,GisDownloadRequested"
+ "T@\"NSNumber\",?,R,C,N"
+ "T@\"NSPersonNameComponents\",?,R,N"
+ "T@\"NSSet\",?,R,C"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",?,R,N"
+ "T@\"NSURL\",?,R,C"
+ "T@\"UTType\",?,R,C,N"
+ "TB,?,GisSyncRoot"
+ "TB,?,R"
+ "TB,?,R,Gfp_isUbiquitous"
+ "TB,?,R,GisHidden"
+ "TB,?,R,N,Gfp_isAddedByCurrentUser"
+ "TB,?,R,N,Gfp_isLastModifiedByCurrentUser"
+ "TB,?,R,N,GisDownloaded"
+ "TB,?,R,N,GisDownloading"
+ "TB,?,R,N,GisExcludedFromSync"
+ "TB,?,R,N,GisMostRecentVersionDownloaded"
+ "TB,?,R,N,GisRestricted"
+ "TB,?,R,N,GisShared"
+ "TB,?,R,N,GisSharedByCurrentUser"
+ "TB,?,R,N,GisTopLevelSharedItem"
+ "TB,?,R,N,GisTrashed"
+ "TB,?,R,N,GisUploaded"
+ "TB,?,R,N,GisUploading"
+ "TQ,?,R,N"
+ "Tq,?,R,N"
+ "T{NSFileProviderTypeAndCreator=II},?,R,N"
- "T@\"NSArray\",R,C"
- "T@\"NSData\",R,C,N"
- "T@\"NSData\",R,N"
- "T@\"NSDate\",R,C,N"
- "T@\"NSDictionary\",R,N"
- "T@\"NSError\",R,C,N"
- "T@\"NSFileProviderItemVersion\",R,N"
- "T@\"NSNumber\",R,C"
- "T@\"NSNumber\",R,C,GisDownloadRequested"
- "T@\"NSNumber\",R,C,N"
- "T@\"NSPersonNameComponents\",R,N"
- "T@\"NSSet\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSURL\",R,C"
- "T@\"UTType\",R,C,N"
- "TB,GisSyncRoot"
- "TB,R"
- "TB,R,Gfp_isUbiquitous"
- "TB,R,GisHidden"
- "TB,R,N,Gfp_isAddedByCurrentUser"
- "TB,R,N,Gfp_isLastModifiedByCurrentUser"
- "TB,R,N,GisDownloaded"
- "TB,R,N,GisDownloading"
- "TB,R,N,GisExcludedFromSync"
- "TB,R,N,GisMostRecentVersionDownloaded"
- "TB,R,N,GisRestricted"
- "TB,R,N,GisShared"
- "TB,R,N,GisSharedByCurrentUser"
- "TB,R,N,GisTopLevelSharedItem"
- "TB,R,N,GisTrashed"
- "TB,R,N,GisUploaded"
- "TB,R,N,GisUploading"
- "TQ,R,N"
- "Tq,R,N"
- "T{NSFileProviderTypeAndCreator=II},R,N"

```
