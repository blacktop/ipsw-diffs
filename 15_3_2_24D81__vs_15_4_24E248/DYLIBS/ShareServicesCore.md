## ShareServicesCore

> `/System/Library/PrivateFrameworks/ShareServicesCore.framework/Versions/A/ShareServicesCore`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x11d00
+751.0.104.0.0
+  __TEXT.__text: 0x11be0
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0xd6c
+  __TEXT.__objc_methlist: 0x11cc
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x4d4
   __TEXT.__cstring: 0x1a9d
   __TEXT.__oslogstring: 0x613
   __TEXT.__unwind_info: 0x4d8
   __TEXT.__objc_classname: 0x2b1
-  __TEXT.__objc_methname: 0x3fca
+  __TEXT.__objc_methname: 0x3fe8
   __TEXT.__objc_methtype: 0xaf0
   __TEXT.__objc_stubs: 0x3380
   __DATA_CONST.__got: 0x348

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe18
+  __DATA_CONST.__objc_selrefs: 0x1008
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x2d0
   __AUTH_CONST.__const: 0x9f0
   __AUTH_CONST.__cfstring: 0xd80
-  __AUTH_CONST.__objc_const: 0x26f8
+  __AUTH_CONST.__objc_const: 0x1f28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x550

   - /System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9D45D4FB-8757-341C-8B92-144BC8E70679
-  Functions: 402
+  UUID: 9265F0D8-388D-3D1B-96DD-7C6CCE044382
+  Functions: 401
   Symbols:   1366
-  CStrings:  1130
+  CStrings:  1132
 
Symbols:
+ __80-[SBLAssetsShareKitManager sharingService:shouldPrepareItems:completionHandler:]_block_invoke.646
+ __Block_byref_object_copy_.43
+ __Block_byref_object_dispose_.44
+ __block_literal_global.35
+ __block_literal_global.693
- __80-[SBLAssetsShareKitManager sharingService:shouldPrepareItems:completionHandler:]_block_invoke.642
- __Block_byref_object_copy_.50
- __Block_byref_object_dispose_.51
- __block_literal_global.41
- __block_literal_global.689
Functions:
~ -[SBLShareKitShareableStoryItem exportWithConfiguration:completionHandler:] : 964 -> 960
~ ___75-[SBLShareKitShareableStoryItem exportWithConfiguration:completionHandler:]_block_invoke : 268 -> 264
~ -[SBLShareKitShareableStoryItem exportWithCompletionHandler:] : 324 -> 320
~ ___61-[SBLShareKitShareableStoryItem exportWithCompletionHandler:]_block_invoke : 288 -> 284
~ -[SBLShareKitShareableItem setProgress:] : 196 -> 184
~ -[SBLShareKitShareableAssetItem _exportAlternateAssetWithCompletionHandler:] : 536 -> 532
~ ___76-[SBLShareKitShareableAssetItem _exportAlternateAssetWithCompletionHandler:]_block_invoke : 136 -> 132
~ -[SBLShareKitShareableAssetItem _exportLivePhotoWithCompletionHandler:] : 600 -> 596
~ ___71-[SBLShareKitShareableAssetItem _exportLivePhotoWithCompletionHandler:]_block_invoke : 136 -> 132
~ -[SBLShareKitShareableAssetItem _exportAssetWithCompletionHandler:] : 932 -> 928
~ ___67-[SBLShareKitShareableAssetItem _exportAssetWithCompletionHandler:]_block_invoke : 136 -> 132
- sub_248597948
~ -[SBLShareKitShareableAssetItem initWithSessionGroup:workerQueue:replyQueue:] : 148 -> 144
~ -[SBLDownloadProvidersOperation px_start] : 1088 -> 1080
~ ___41-[SBLDownloadProvidersOperation px_start]_block_invoke : 176 -> 172
~ ___41-[SBLDownloadProvidersOperation px_start]_block_invoke_2 : 256 -> 252
~ -[SBLFullfillProvidersOperation px_start] : 1004 -> 984
~ ___41-[SBLFullfillProvidersOperation px_start]_block_invoke : 176 -> 172
~ ___41-[SBLFullfillProvidersOperation px_start]_block_invoke_2 : 256 -> 252
~ -[NSItemProvider(SBL) sbl_registerLoadHandlers] : 1948 -> 1796
~ +[NSItemProvider(SBL) _sbl_itemProviderWithSharableItem:] : 424 -> 420
~ -[SBLShareKitSession sessionBegin:] : 2644 -> 2632
~ -[SBLShareKitSession sessionPrepare] : 404 -> 400
~ -[SBLShareKitManager resetForMenu:] : 208 -> 216
~ -[SBLShareKitManager populateMenu:forSharableObjects:sharingParams:allowedLatency:completion:] : 1536 -> 1540
~ -[SBLAssetsShareKitManager sharingItemsForObjects:sharingParams:] : 872 -> 868
CStrings:
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/shareservices/Source/ShareServicesCore/ShareKit/NSItemProvider+SBL.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/shareservices/Source/ShareServicesCore/ShareKit/SBLSetDesktopSharingService.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/shareservices/Source/ShareServicesCore/ShareKit/SBLShareKitManager.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/shareservices/Source/ShareServicesCore/ShareKit/SBLShareKitOperations.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/shareservices/Source/ShareServicesCore/ShareKit/SBLShareKitSession.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/shareservices/Source/ShareServicesCore/ShareKit/SBLShareKitShareableItem.m"
+ "focalLength"
+ "focalLengthIn35mm"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/shareservices/Source/ShareServicesCore/ShareKit/NSItemProvider+SBL.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/shareservices/Source/ShareServicesCore/ShareKit/SBLSetDesktopSharingService.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/shareservices/Source/ShareServicesCore/ShareKit/SBLShareKitManager.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/shareservices/Source/ShareServicesCore/ShareKit/SBLShareKitOperations.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/shareservices/Source/ShareServicesCore/ShareKit/SBLShareKitSession.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/shareservices/Source/ShareServicesCore/ShareKit/SBLShareKitShareableItem.m"

```
