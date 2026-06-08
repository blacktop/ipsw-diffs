## com.apple.DocumentManagerCore.Downloads

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Downloads.xpc/com.apple.DocumentManagerCore.Downloads`

```diff

-367.5.1.0.0
-  __TEXT.__text: 0x4134
-  __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_stubs: 0x900
-  __TEXT.__objc_methlist: 0x264
-  __TEXT.__const: 0xa8
-  __TEXT.__objc_classname: 0x6c
-  __TEXT.__objc_methname: 0xa8b
-  __TEXT.__objc_methtype: 0x2c1
-  __TEXT.__gcc_except_tab: 0xe4
-  __TEXT.__cstring: 0x23a
-  __TEXT.__oslogstring: 0x47f
-  __TEXT.__unwind_info: 0x130
-  __DATA_CONST.__auth_got: 0x170
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x388
-  __DATA_CONST.__cfstring: 0x100
-  __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x18
+389.2.0.0.0
+  __TEXT.__text: 0x4388
+  __TEXT.__auth_stubs: 0x330
+  __TEXT.__objc_stubs: 0xc60
+  __TEXT.__objc_methlist: 0x384
+  __TEXT.__const: 0xb0
+  __TEXT.__objc_classname: 0x95
+  __TEXT.__objc_methname: 0xdcb
+  __TEXT.__objc_methtype: 0x37a
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__cstring: 0x337
+  __TEXT.__oslogstring: 0x5a6
+  __TEXT.__unwind_info: 0x128
+  __DATA_CONST.__const: 0x370
+  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x300
-  __DATA.__objc_selrefs: 0x320
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x120
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0x108
+  __DATA.__objc_const: 0x6c0
+  __DATA.__objc_selrefs: 0x410
+  __DATA.__objc_ivar: 0x1c
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F3114FBC-3A0A-3C06-AB62-ECD10BC804D0
-  Functions: 82
-  Symbols:   87
-  CStrings:  190
+  UUID: F010F5A0-B69F-37F2-B639-F49BCBAA7884
+  Functions: 91
+  Symbols:   101
+  CStrings:  262
 
Symbols:
+ _NSOSStatusErrorDomain
+ _OBJC_CLASS_$_DLFIMoveOperationWrapper
+ _OBJC_CLASS_$_DOCFeature
+ _OBJC_CLASS_$_DOCNodeStartupManager
+ _OBJC_CLASS_$_FIMoveOperation
+ _OBJC_CLASS_$_FIOperationReply
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_METACLASS_$_DLFIMoveOperationWrapper
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_setProperty_nonatomic_copy
+ _objc_storeStrong
- _OBJC_CLASS_$_FPDeleteOperation
- __NSConcreteGlobalBlock
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
CStrings:
+ ".cxx_destruct"
+ "@\"FIMoveOperation\""
+ "@\"FINode\""
+ "@\"FIOperationReply\"24@?0@\"FIOperation\"8@\"FIOperationError\"16"
+ "@\"NSArray\""
+ "@\"NSDictionary\""
+ "@\"NSDictionary\"16@0:8"
+ "@32@0:8@16@24"
+ "@?"
+ "@?16@0:8"
+ "@?<v@?@\"NSError\">16@0:8"
+ "B"
+ "Could not fetch URL for folder: %@. Error: %@"
+ "Couldn't find a downloads location: %{public}@"
+ "DLFIMoveOperationWrapper"
+ "DLMoveOperation"
+ "Failed to fetch URL for root node: %@"
+ "I28@?0@\"FIOperation\"8I16@\"FIOperationRecord\"20"
+ "Q"
+ "Replacing placeholder URL: %@ failed with error: %{public}@"
+ "T@\"FIMoveOperation\",&,N,V_wrappedOperation"
+ "T@\"FINode\",&,N,V_firstResultNode"
+ "T@\"NSDictionary\",C,N"
+ "T@?,C,N"
+ "T@?,C,N,V_actionCompletionBlock"
+ "TB,N"
+ "TB,N,V_shouldBounceOnCollision"
+ "TQ,N"
+ "TQ,N,V_lastUsageUpdatePolicy"
+ "URLByDeletingLastPathComponent"
+ "Unable to locate moved file"
+ "Unable to move file to Downloads"
+ "_actionCompletionBlock"
+ "_firstResultNode"
+ "_lastUsageUpdatePolicy"
+ "_shouldBounceOnCollision"
+ "_sourceNodes"
+ "_targetFilenamesByURL"
+ "_wrappedOperation"
+ "actionCompletionBlock"
+ "addObject:"
+ "allValues"
+ "arrayWithCapacity:"
+ "cancelled"
+ "checkResourceIsReachableAndReturnError:"
+ "copy"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "dictionaryWithCapacity:"
+ "error"
+ "errorWithDomain:code:userInfo:"
+ "fetchDefaultDownloadsLocationSettingsItem:"
+ "filePathURL"
+ "fileURL"
+ "firstResultNode"
+ "initWithResolution:error:"
+ "initWithSourceNodes:destinationFolder:"
+ "isEqualToString:"
+ "isFileReferenceURL"
+ "itemForURL:error:"
+ "lastUsageUpdatePolicy"
+ "length"
+ "objectForKeyedSubscript:"
+ "performMoveOperationToURL: Could not find result for sourceURL=%{public}@"
+ "performMoveOperationToURL: Move operation failed with error: %{public}@"
+ "performMoveOperationToURL: Source file not reachable: %{public}@, error: %{public}@"
+ "performMoveOperationToURL:urlWrapper:newFileName:notifyOnCompletion:completionHandler:"
+ "schedule"
+ "setCompletionHandler:"
+ "setConflictHandler:"
+ "setErrorHandler:"
+ "setFirstResultNode:"
+ "setObject:forKeyedSubscript:"
+ "setTargetFilenamesByNode:"
+ "setTargetFilenamesByURL:"
+ "setTargetFilenamesByURL: No matching source node found for URL: %{public}@"
+ "setTargetFilenamesByURL: No source nodes available to set target filenames"
+ "setWrappedOperation:"
+ "setupCallbacks"
+ "shared"
+ "shouldBounceOnCollision"
+ "startIfNeeded"
+ "stringByStandardizingPath"
+ "targetFilenamesByURL"
+ "useFIOperations"
+ "v16@0:8"
+ "v20@0:8B16"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8Q16"
+ "v24@?0@\"DOCDownloadSettingsItem\"8@\"NSError\"16"
+ "v24@?0@\"FIOperation\"8@\"NSArray\"16"
+ "v52@0:8@16@24@32B40@?44"
+ "wrappedOperation"
- "@24@0:8@16"
- "@32@0:8@16^@24"
- "@40@0:8@16@24@?32"
- "@48@0:8@16@24@32@?40"
- "Couldn't fetch parent item: %@"
- "Couldn't find a downloads location: %@"
- "Failed to create temp directory: %@"
- "Moving URL: %@ to parent: %@"
- "Replacing placeholder URL: %@ failed with error: %@"
- "Unable to delete placeholder: %@"
- "Unable to fetch placeholder item from URL: %@ error: %@"
- "createDeleteOperation:"
- "createMoveOperation:destinationItem:completionHandler:"
- "createMoveOperation:parentItem:newFileName:completionHandler:"
- "createTemporaryFolderURLAppropriateForURL:error:"
- "deleteItemIgnoringResult:"
- "fetchDefaultDownloadsLocationItem:"
- "fetchParentsForItemID:recursively:completionHandler:"
- "fpfs_fpItem"
- "importItemAtURLToDownloads:completionHandler:"
- "initWithItems:"
- "initWithItems:destinationFolder:"
- "itemID"
- "objectForKey:"
- "setTargetFilenamesByItem:"

```
