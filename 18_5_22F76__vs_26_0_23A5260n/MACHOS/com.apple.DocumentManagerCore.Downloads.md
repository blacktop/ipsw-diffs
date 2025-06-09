## com.apple.DocumentManagerCore.Downloads

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Downloads.xpc/com.apple.DocumentManagerCore.Downloads`

```diff

-337.6.3.0.0
-  __TEXT.__text: 0x402c
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_stubs: 0x840
-  __TEXT.__objc_methlist: 0x25c
-  __TEXT.__const: 0x90
+357.2.0.0.0
+  __TEXT.__text: 0x42fc
+  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__objc_stubs: 0x900
+  __TEXT.__objc_methlist: 0x264
+  __TEXT.__const: 0xa8
   __TEXT.__objc_classname: 0x6c
-  __TEXT.__objc_methname: 0xa10
+  __TEXT.__objc_methname: 0xa8b
   __TEXT.__objc_methtype: 0x2c1
   __TEXT.__gcc_except_tab: 0xf0
-  __TEXT.__cstring: 0x1e1
-  __TEXT.__oslogstring: 0x41a
-  __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__auth_got: 0x180
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x360
+  __TEXT.__cstring: 0x23a
+  __TEXT.__oslogstring: 0x47f
+  __TEXT.__unwind_info: 0x120
+  __DATA_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__const: 0x388
   __DATA_CONST.__cfstring: 0x100
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x300
-  __DATA.__objc_selrefs: 0x2f0
+  __DATA.__objc_selrefs: 0x320
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv
   - /System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EF83F124-76B3-387A-ACE0-B904856CACCB
-  Functions: 79
-  Symbols:   83
-  CStrings:  180
+  UUID: 93A7CD73-618C-3996-AD88-7833A82D494F
+  Functions: 81
+  Symbols:   90
+  CStrings:  190
 
Symbols:
+ _DOCSBFolderNotificationIsDownloadsFolderKey
+ _DOCSBFolderNotificationURLKey
+ _DOCSBFolderProgressCompletedDistributedNotification
+ _OBJC_CLASS_$_FINode
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ ___kCFBooleanTrue
+ _objc_opt_isKindOfClass
CStrings:
+ "%s URL: %@ posting notification: %@ userInfo: %@"
+ "%s URL: %@ request to post notification: %@"
+ "-[DLDocumentDownloads _notifyDownloadCompleted:]"
+ "Could not fetch root URL of iCloud Drive domain %{public}@. Error: %@"
+ "_notifyDownloadCompleted:"
+ "defaultCenter"
+ "doc_fetchRootNodeForProviderDomain:completionHandler:"
+ "fetchURL:"
+ "fiNodeFromURL:"
+ "fpfs_fpItem"
+ "postNotificationName:object:userInfo:options:"
+ "v24@?0@\"NSObject<DOCNode>\"8@\"NSError\"16"
- "Could not fetch root URL of iCloud Drive domain %@. Error: %@"
- "doc_fetchRootItemForProviderDomain:completionHandler:"

```
