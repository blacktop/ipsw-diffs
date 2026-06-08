## com.apple.CloudDocs.iCloudDriveFileProviderManaged

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProviderManaged.appex/com.apple.CloudDocs.iCloudDriveFileProviderManaged`

```diff

-4479.122.1.0.0
-  __TEXT.__text: 0x28600
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x2c20
-  __TEXT.__objc_methlist: 0x1e0c
+5044.0.0.0.0
+  __TEXT.__text: 0x23d38
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_stubs: 0x2c40
+  __TEXT.__objc_methlist: 0x1e2c
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x2cd4
-  __TEXT.__objc_methname: 0x5315
-  __TEXT.__cstring: 0x46d2
-  __TEXT.__oslogstring: 0x249d
-  __TEXT.__objc_classname: 0x6e9
+  __TEXT.__gcc_except_tab: 0x23b4
+  __TEXT.__objc_methname: 0x5360
+  __TEXT.__cstring: 0x44f8
+  __TEXT.__oslogstring: 0x247e
+  __TEXT.__objc_classname: 0x6d5
   __TEXT.__objc_methtype: 0x3620
-  __TEXT.__unwind_info: 0xb10
-  __DATA_CONST.__auth_got: 0x2f8
-  __DATA_CONST.__got: 0x270
+  __TEXT.__unwind_info: 0xa50
   __DATA_CONST.__const: 0x10a8
   __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0xe0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA.__objc_const: 0x7d50
-  __DATA.__objc_selrefs: 0x1268
-  __DATA.__objc_ivar: 0x134
+  __DATA_CONST.__auth_got: 0x320
+  __DATA_CONST.__got: 0x270
+  __DATA.__objc_const: 0x7db8
+  __DATA.__objc_selrefs: 0x1278
+  __DATA.__objc_ivar: 0x138
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0xae0
   __DATA.__bss: 0x90

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
-  - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 9A997AA8-A92D-3927-8BA5-8513F07DB15F
-  Functions: 625
-  Symbols:   182
-  CStrings:  1469
+  UUID: 43EA59E2-6CB4-33FB-95C5-ED1C02C6EEF8
+  Functions: 609
+  Symbols:   187
+  CStrings:  1464
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "-[ICDFileProviderExtension importDidFinishWithCompletionHandler:]_block_invoke_2"
+ "@\"NSProgress\"32@0:8@\"BRFileObjectID\"16@?<v@?@\"NSURL\"@\"NSData\"@\"NSError\">24"
+ "@\"NSProgress\"32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSDictionary\"@\"NSError\">24"
+ "@\"NSProgress\"72@0:8@\"<NSFileProviderItem>\"16Q24@\"FPSandboxingURLWrapper\"32Q40@\"NSFileProviderRequest\"48@\"NSDictionary\"56@?<v@?@\"BRQueryItem\"QB@\"NSError\">64"
+ "@\"NSProgress\"80@0:8@\"<NSFileProviderItem>\"16@\"NSFileProviderItemVersion\"24Q32@\"FPSandboxingURLWrapper\"40Q48@\"NSFileProviderRequest\"56@\"NSDictionary\"64@?<v@?@\"BRQueryItem\"QB@\"NSError\">72"
+ "@72@0:8@16Q24@32Q40@48@56@?64"
+ "@80@0:8@16@24Q32@40Q48@56@64@?72"
+ "[DEBUG] Cancelling operations - %@%@"
+ "[WARNING] generating thumbnail for small file was canceled%@"
+ "_getAsyncProxy"
+ "_isManagedAccount"
+ "br_isManagedAppleID"
+ "brc_errorDownloadCancelled"
+ "discreteProgressWithTotalUnitCount:"
+ "isCancelled"
+ "newAsyncFPFSProxy"
+ "objectAtIndex:"
+ "rampNumberForAccountWithReply:"
+ "v32@?0@\"NSProgress\"8@\"NSArray\"16@?<v@?@\"BRFileObjectID\"@\"NSURL\"@\"NSData\"@\"NSError\">24"
+ "v40@0:8@\"NSData\"16Q24@?<v@?@\"NSArray<NSFileProviderItem>\"@\"NSArray\"@\"NSData\"@\"NSError\">32"
+ "v40@0:8@\"NSObject<BROperationClient>\"16@\"NSString\"24@?<v@?@\"NSNumber\"@\"NSError\">32"
- "-[ICDFileProviderExtension _isSharableItem:withCompletionHandler:]_block_invoke_2"
- "-[ICDFileProviderExtension createItemBasedOnTemplate:fields:contents:options:request:completionHandler:]_block_invoke"
- "-[ICDFileProviderExtension deleteItemWithIdentifier:baseVersion:options:request:completionHandler:]_block_invoke"
- "-[ICDFileProviderExtension importDidFinishWithCompletionHandler:]_block_invoke_3"
- "-[ICDFileProviderExtension(Thumbnails) _fetchThumbnailsForItemIdentifiersWithVersionMap:requestedSize:perThumbnailCompletionHandler:completionHandler:]_block_invoke_2"
- "[DEBUG] Failed creating proxy with %@%@"
- "[DEBUG] finished fetching all thumbnail batches%@"
- "[ERROR] no zone ID found, returning.%@"
- "_getAsyncProxyWithErrorHandler:"
- "com.apple.br.fetch-thumbnail"
- "dataWithContentsOfURL:"
- "error"
- "firstObject"
- "newSyncProxy"
- "removeObjectAtIndex:"
- "setError:"
- "v24@?0@\"NSArray\"8@?<v@?@\"BRFileObjectID\"@\"NSURL\"@\"NSData\"@\"NSError\">16"
- "v32@0:8@\"BRFileObjectID\"16@?<v@?@\"NSURL\"@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSDictionary\"@\"NSError\">24"
- "v40@0:8@\"NSData\"16Q24@?<v@?@\"NSArray<NSFileProviderItem_Private>\"@\"NSArray\"@\"NSData\"@\"NSError\">32"
- "v56@0:8@\"NSString\"16@\"NSFileProviderItemVersion\"24Q32@\"NSFileProviderRequest\"40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24Q32@40@?48"
- "v72@0:8@\"<NSFileProviderItem>\"16Q24@\"FPSandboxingURLWrapper\"32Q40@\"NSFileProviderRequest\"48@\"NSDictionary\"56@?<v@?@\"BRQueryItem\"QB@\"NSError\">64"
- "v72@0:8@16Q24@32Q40@48@56@?64"
- "v80@0:8@\"<NSFileProviderItem>\"16@\"NSFileProviderItemVersion\"24Q32@\"FPSandboxingURLWrapper\"40Q48@\"NSFileProviderRequest\"56@\"NSDictionary\"64@?<v@?@\"BRQueryItem\"QB@\"NSError\">72"
- "v80@0:8@16@24Q32@40Q48@56@64@?72"

```
