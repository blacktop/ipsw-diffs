## com.apple.CloudDocs.iCloudDriveFileProvider

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider`

```diff

-3437.120.20.0.0
-  __TEXT.__text: 0x279a0
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_stubs: 0x2bc0
-  __TEXT.__objc_methlist: 0x1dc4
+4140.0.0.502.2
+  __TEXT.__text: 0x270ec
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_stubs: 0x2be0
+  __TEXT.__objc_methlist: 0x1d8c
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x2db0
-  __TEXT.__objc_methname: 0x5129
-  __TEXT.__cstring: 0x46b3
-  __TEXT.__oslogstring: 0x2488
-  __TEXT.__objc_classname: 0x73d
-  __TEXT.__objc_methtype: 0x34ac
-  __TEXT.__unwind_info: 0xab0
-  __DATA_CONST.__auth_got: 0x320
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x1028
+  __TEXT.__gcc_except_tab: 0x2cf4
+  __TEXT.__objc_methname: 0x51e1
+  __TEXT.__cstring: 0x4629
+  __TEXT.__oslogstring: 0x24d8
+  __TEXT.__objc_classname: 0x6e9
+  __TEXT.__objc_methtype: 0x35a2
+  __TEXT.__unwind_info: 0xa70
+  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0x1098
   __DATA_CONST.__cfstring: 0x280
-  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xd0
-  __DATA.__objc_const: 0x8180
-  __DATA.__objc_selrefs: 0x1210
-  __DATA.__objc_ivar: 0x140
-  __DATA.__objc_data: 0x960
+  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA.__objc_const: 0x7bc8
+  __DATA.__objc_selrefs: 0x1228
+  __DATA.__objc_ivar: 0x134
+  __DATA.__objc_data: 0x8c0
   __DATA.__data: 0xae0
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
-  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 087E71CE-E1F5-34C4-B12E-83F6917586B4
-  Functions: 625
-  Symbols:   186
-  CStrings:  1457
+  UUID: CD8D344C-D462-327D-BA21-AD4C3F07F0C2
+  Functions: 613
+  Symbols:   189
+  CStrings:  1460
 
Symbols:
+ _OBJC_CLASS_$_BRFeatureFlags
+ _OBJC_CLASS_$_FPItem
+ _OBJC_CLASS_$_NSSecurityScopedURLWrapper
+ _objc_opt_respondsToSelector
+ _objc_release_x1
- _OBJC_CLASS_$_BRFileProvidingOperation
- _exit
CStrings:
+ "-[BRBaseFileEnumerator receiveUpdates:reply:]"
+ "-[ICDFileProviderClientSideCollaborationServiceProxy uploadContents:baseVersion:options:reply:]"
+ "-[ICDFileProviderClientSideCollaborationServiceProxy uploadContents:baseVersion:options:reply:]_block_invoke"
+ "-[ICDFileProviderClientSideCollaborationServiceProxy uploadContents:baseVersion:options:reply:]_block_invoke_2"
+ "-[ICDFileProviderExtension _fetchContentsForItemWithIdentifier:existingContents:version:request:completionHandler:]"
+ "-[ICDFileProviderExtension _fetchContentsForItemWithIdentifier:existingContents:version:request:completionHandler:]_block_invoke"
+ "-[ICDFileProviderExtension _fetchContentsForItemWithIdentifier:existingContents:version:request:completionHandler:]_block_invoke_2"
+ "@\"NSProgress\"48@0:8@\"NSSecurityScopedURLWrapper\"16@\"NSFileProviderItemVersion\"24Q32@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">40"
+ "@\"NSProgress\"56@0:8@\"BRFileObjectID\"16@\"FPSandboxingURLWrapper\"24Q32@\"NSString\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
+ "@\"NSProgress\"60@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24@\"NSFileProviderItemVersion\"32B40Q44@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">52"
+ "@48@0:8@16@24Q32@?40"
+ "@56@0:8@16@24@32@40@?48"
+ "@60@0:8@16@24@32B40Q44@?52"
+ "[DEBUG] Item %@ sync is paused: %d%@"
+ "[DEBUG] ┣%llx Item sync is paused or modify item options are set to fail on conflict. Using our collaboration upload flow%@"
+ "[INFO] ┏%llx %s createItemBasedOnTemplate %@ at '%@' fields:%@ options:%@%@"
+ "[INFO] ┏%llx %s modifyItem %@ fields:%@ options:%@%@"
+ "[INFO] ┳%llx %s: reply(%@, %d, %d, %@)%@"
+ "_fetchContentsForItemWithIdentifier:existingContents:version:request:completionHandler:"
+ "accountDidChangeWithCellularEnabled:isUnlimitedUpdatesEnabled:reply:"
+ "deletionConflicted"
+ "failOnConflict"
+ "getBGSystemTaskActivitiesDefaultConfig:"
+ "getCKRecordIDsForFPItems:reply:"
+ "handleAcceptingCKShareMetadata:reply:"
+ "initWithURL:readonly:"
+ "isSyncPaused"
+ "mayAlreadyExist"
+ "printShareRequests:personaID:isPending:asJSON:reply:"
+ "receiveUpdates:reply:"
+ "requestForAccessEnabled"
+ "setSupportAllowingAccessRequests:"
+ "startDownloadFileObject:existingContents:options:etagIfLoser:reply:"
+ "startOperation:toAutoAcceptShareLink:reply:"
+ "updateContentVersion:"
+ "uploadContents:baseVersion:options:reply:"
+ "uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:options:reply:"
+ "v40@0:8@\"NSObject<BROperationClient>\"16@\"NSURL\"24@?<v@?@\"FPSandboxingURLWrapper\"@\"NSError\">32"
+ "v48@0:8@\"NSFileHandle\"16@\"NSString\"24B32B36@?<v@?@\"NSError\">40"
+ "v48@0:8@16@24B32B36@?40"
- "-[BRBaseFileEnumerator receiveUpdates:logicalExtensions:physicalExtensions:reply:]"
- "-[BRFileProvideriWorkCollaborationProxy fetchLatestRevisionWithCompletionHandler:]"
- "-[BRFileProvideriWorkCollaborationServiceSource listener:shouldAcceptNewConnection:]_block_invoke"
- "-[ICDFileProviderClientSideCollaborationServiceProxy uploadContents:baseVersion:reply:]"
- "-[ICDFileProviderClientSideCollaborationServiceProxy uploadContents:baseVersion:reply:]_block_invoke"
- "-[ICDFileProviderClientSideCollaborationServiceProxy uploadContents:baseVersion:reply:]_block_invoke_2"
- "-[ICDFileProviderExtension fetchContentsForItemWithIdentifier:version:request:completionHandler:]"
- "-[ICDFileProviderExtension fetchContentsForItemWithIdentifier:version:request:completionHandler:]_block_invoke"
- "-[ICDFileProviderExtension fetchContentsForItemWithIdentifier:version:request:completionHandler:]_block_invoke_2"
- "-[ICDFileProviderExtension invalidateExtension]"
- "@\"BRFileProviderExtension\""
- "@\"NSProgress\"48@0:8@\"BRFileObjectID\"16Q24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "@\"NSProgress\"52@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24@\"NSFileProviderItemVersion\"32B40@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">44"
- "@48@0:8@16Q24@32@?40"
- "@52@0:8@16@24@32B40@?44"
- "BRFileProvideriWorkCollaborationProxy"
- "BRFileProvideriWorkCollaborationServiceSource"
- "URLForItemWithPersistentIdentifier:"
- "Vv20@0:8B16"
- "[DEBUG] fetchLatestRevisionWithCompletionHandler: %@, %@%@"
- "[ERROR] Got a request to invalidate the extension from bird.%@"
- "[INFO] ┏%llx %s createItemBasedOnTemplate %@ at '%@' fields:%@ options:%llu%@"
- "[INFO] ┏%llx %s modifyItem %@ fields:%@ options:%llu%@"
- "accountDidChangeWithCellularEnabled:reply:"
- "checkinAskClientIfUsingUbiquity:"
- "initWithURL:"
- "initWithURL:readingOptions:"
- "invalidateExtension"
- "presentAcceptDialogsForShareMetadata:reply:"
- "receiveUpdates:logicalExtensions:physicalExtensions:reply:"
- "setFileProvidingCompletion:"
- "setWantsCurrentVersion:"
- "startDownloadFileObject:options:etagIfLoser:reply:"
- "unlimitedUpdatesOverCellularWithEnablementStatus:reply:"
- "uploadItemIdentifier:withContents:baseVersion:basedOnOriginalVersion:reply:"
- "v48@0:8@\"NSArray\"16@\"NSDictionary\"24@\"NSDictionary\"32@?<v@?>40"
- "v48@0:8@16@24@32@?40"

```
