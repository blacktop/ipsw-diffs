## RemotePaymentPassActionsMessagesExtension

> `/Applications/RemotePaymentPassActionsService.app/PlugIns/RemotePaymentPassActionsMessagesExtension.appex/RemotePaymentPassActionsMessagesExtension`

```diff

-1265.0.0.0.0
-  __TEXT.__text: 0x867c
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_stubs: 0x2060
-  __TEXT.__objc_methlist: 0x888
+1269.0.0.0.0
+  __TEXT.__text: 0x904c
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_stubs: 0x2220
+  __TEXT.__objc_methlist: 0x8c8
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__objc_methname: 0x27d3
-  __TEXT.__cstring: 0x707
-  __TEXT.__oslogstring: 0xe76
+  __TEXT.__objc_methname: 0x296b
+  __TEXT.__cstring: 0x73f
+  __TEXT.__oslogstring: 0x10a9
   __TEXT.__objc_classname: 0x21a
-  __TEXT.__objc_methtype: 0xdaa
-  __TEXT.__unwind_info: 0x218
-  __DATA_CONST.__auth_got: 0x258
-  __DATA_CONST.__got: 0x1e8
-  __DATA_CONST.__const: 0x318
-  __DATA_CONST.__cfstring: 0x3a0
+  __TEXT.__objc_methtype: 0xd8e
+  __TEXT.__unwind_info: 0x230
+  __DATA_CONST.__auth_got: 0x270
+  __DATA_CONST.__got: 0x1f8
+  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__cfstring: 0x3e0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x1108
-  __DATA.__objc_selrefs: 0xa58
-  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_const: 0x10e8
+  __DATA.__objc_selrefs: 0xad0
+  __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E094D449-4A2F-32DA-AECC-CBD4AC5D3239
-  Functions: 141
-  Symbols:   160
-  CStrings:  600
+  UUID: C971C58F-CF16-3310-95AF-D81CD877D557
+  Functions: 147
+  Symbols:   165
+  CStrings:  626
 
Symbols:
+ _NPKSecureArchiveObject
+ _NPKSecureUnarchiveObject
+ _OBJC_CLASS_$_NPKRemotePassActionRequest
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSFileManager
+ _PKSharedCacheDirectoryPath
- _OBJC_CLASS_$_NSCache
CStrings:
+ "Debug: Removed archive for identifier: %@"
+ "Debug: Removed empty directory at url: %@"
+ "Debug: Returning object %@ for identifier %@"
+ "Debug: Set object %@ for identifier %@"
+ "Error: Failed to create NPKRemotePassActionCompanionConversationManager directory with error: %@"
+ "Error: Failed to get directory contents at path: %@ with error: %@"
+ "Error: Failed to read archive with url: %@"
+ "Error: Failed to remove archive at url: %@ with error: %@"
+ "Error: Failed to remove empty directory at url: %@ with error: %@"
+ "Error: Failed to write archive to url: %@"
+ "Notice: Did cancel sending message: %@, conversation: %@"
+ "Warning: No archive found to remove for identifier: %@"
+ "_removeRequestForIdentifier:withQueue:"
+ "_requestForIdentifier:withQueue:"
+ "_setRequest:forIdentifier:withQueue:"
+ "_sharedDirectoryPath"
+ "_urlForMessageIdentifier:"
+ "archive"
+ "contentsOfDirectoryAtPath:error:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "dataWithContentsOfURL:"
+ "defaultManager"
+ "didCancelSendingMessage:conversation:"
+ "fileExistsAtPath:"
+ "fileURLWithPath:"
+ "fileURLWithPath:isDirectory:"
+ "path"
+ "removeItemAtURL:error:"
+ "removeRequestForIdentifier:"
+ "stringByAppendingPathComponent:"
+ "stringByAppendingPathExtension:"
+ "writeToURL:atomically:"
- "@\"NSCache\""
- "@40@0:8@16@24@32"
- "Notice: Returning object %@ for identifier %@"
- "Notice: Setting object %@ for identifier %@"
- "_objectForIdentifier:inCache:withQueue:"
- "_requestCache"
- "_setObject:forIdentifier:inCache:withQueue:"
- "objectForKey:"
- "removeObjectForKey:"

```
