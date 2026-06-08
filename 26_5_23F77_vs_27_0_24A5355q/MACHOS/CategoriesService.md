## CategoriesService

> `/System/Library/PrivateFrameworks/Categories.framework/XPCServices/CategoriesService.xpc/CategoriesService`

```diff

-49.4.1.0.0
-  __TEXT.__text: 0x49dc
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x334
-  __TEXT.__const: 0xb8
-  __TEXT.__objc_methname: 0xb9a
-  __TEXT.__oslogstring: 0x4c6
-  __TEXT.__cstring: 0x5a7
-  __TEXT.__objc_classname: 0xb7
-  __TEXT.__objc_methtype: 0x26b
-  __TEXT.__gcc_except_tab: 0x184
+53.1.0.0.0
+  __TEXT.__text: 0x4f8c
+  __TEXT.__auth_stubs: 0x420
+  __TEXT.__objc_stubs: 0xe80
+  __TEXT.__objc_methlist: 0x37c
+  __TEXT.__const: 0xc0
+  __TEXT.__objc_methname: 0xe85
+  __TEXT.__oslogstring: 0x746
+  __TEXT.__cstring: 0x5f5
+  __TEXT.__objc_classname: 0xb1
+  __TEXT.__objc_methtype: 0x2e8
+  __TEXT.__gcc_except_tab: 0x180
   __TEXT.__unwind_info: 0x160
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x2c8
-  __DATA_CONST.__cfstring: 0x900
+  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__cfstring: 0x9a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x6c8
-  __DATA.__objc_selrefs: 0x3d8
-  __DATA.__objc_ivar: 0x20
+  __DATA_CONST.__auth_got: 0x220
+  __DATA_CONST.__got: 0x1c0
+  __DATA.__objc_const: 0x738
+  __DATA.__objc_selrefs: 0x488
+  __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x120
   __DATA.__bss: 0x38

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 44060492-7E43-336F-B860-559772DD68F4
-  Functions: 76
-  Symbols:   140
-  CStrings:  378
+  UUID: 95628999-F06B-36D1-8BB6-C757943598BA
+  Functions: 86
+  Symbols:   146
+  CStrings:  429
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_CTAppStoreCategories
+ _OBJC_CLASS_$_CTBundleCategoriesLookupResult
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ __os_log_fault_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _dispatch_async
- _dispatch_queue_attr_make_with_autorelease_frequency
- _dispatch_queue_create
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x27
CStrings:
+ "-[Categories_Service appStoreCategoriesForBundleIDs:platform:replyHandler:]"
+ "-[Categories_Service appStoreCategoriesForBundleIDs:platform:replyHandler:]_block_invoke"
+ "-[Categories_Service installedAppCategoriesForBundleIDs:replyHandler:]"
+ "-[Categories_Service installedAppCategoriesForBundleIDs:replyHandler:]_block_invoke"
+ "<%@>::setCategorizationVersion: rejected (missing entitlement %{public}@)"
+ "<%@>::setCategorizationVersion: version=%ld"
+ "@24@0:8q16"
+ "@28@0:8B16^@20"
+ "Caller is not entitled to set the Categories version"
+ "Categories"
+ "Failed to create container directory %{public}@: %{public}@"
+ "Failed to persist version: %{public}@"
+ "Failed to read persisted version plist (defaulting to Classic): %{public}@"
+ "Failed to resolve NSApplicationSupportDirectory: %{public}@"
+ "Loaded persisted version: %ld"
+ "No persisted version found; defaulting to Classic"
+ "Persisted version plist is malformed; defaulting to Classic"
+ "Persisted version value %ld is out of range; defaulting to Classic"
+ "URLByAppendingPathComponent:isDirectory:"
+ "URLForDirectory:inDomain:appropriateForURL:create:error:"
+ "_currentVersion"
+ "_loadPersistedVersion"
+ "_persistVersion:"
+ "_versionLock"
+ "_versionPlistURLCreatingDirectory:error:"
+ "appStoreCategoriesForBundleIDs:platform:replyHandler:"
+ "categorizationVersionWithReplyHandler:"
+ "categorizationVersionWithReplyHandler: returning %ld"
+ "com.apple.private.ctcategoriesservice.setversion"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "dataWithPropertyList:format:options:error:"
+ "defaultManager"
+ "dictionaryWithContentsOfURL:error:"
+ "exportedInterface"
+ "fileExistsAtPath:"
+ "initWithApplicationBundleIdentifier:appStoreCategories:parentAppBundleIdentifier:counterpartBundleIdentifiers:"
+ "initWithPrimary:secondary:"
+ "installedAppCategoriesForBundleIDs:replyHandler:"
+ "integerValue"
+ "numberWithInteger:"
+ "objectAtIndexedSubscript:"
+ "path"
+ "q"
+ "q16@0:8"
+ "setCategorizationVersion: no-op (already %ld)"
+ "setCategorizationVersion:replyHandler:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setWithObjects:"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?q>16"
+ "v32@0:8q16@?24"
+ "v32@0:8q16@?<v@?@\"NSError\">24"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "version"
+ "version.plist"
+ "writeToURL:options:error:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "-[Categories_Service genreIDsAndCounterpartIdentifiersForInstalledBundleIDs:replyHandler:]"
- "-[Categories_Service genreIDsAndCounterpartIdentifiersForInstalledBundleIDs:replyHandler:]_block_invoke"
- "-[Categories_Service lookupAppStoreForBundleIDs:platform:replyHandler:]"
- "-[Categories_Service lookupAppStoreForBundleIDs:platform:replyHandler:]_block_invoke"
- "@\"NSObject<OS_dispatch_queue>\""
- "_queue"
- "com.apple.categoriesservice.lookupdevice"
- "genreIDsAndCounterpartIdentifiersForInstalledBundleIDs:replyHandler:"
- "lookupAppStoreForBundleIDs:platform:replyHandler:"
- "transaction = %d"
- "v32@?0@8Q16^B24"

```
