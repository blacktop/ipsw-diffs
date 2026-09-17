## CallKit

> `/System/Library/Frameworks/CallKit.framework/Versions/A/CallKit`

```diff

-1403.100.1.0.0
-  __TEXT.__text: 0x6937c
-  __TEXT.__objc_methlist: 0x917c
+1406.200.51.1.1
+  __TEXT.__text: 0x69ee0
+  __TEXT.__objc_methlist: 0x91fc
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x62ed
-  __TEXT.__oslogstring: 0x39c9
+  __TEXT.__cstring: 0x635c
+  __TEXT.__oslogstring: 0x3a9a
   __TEXT.__gcc_except_tab: 0x690
-  __TEXT.__unwind_info: 0x2860
+  __TEXT.__unwind_info: 0x2890
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3468
+  __DATA_CONST.__objc_selrefs: 0x34b0
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x388
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x4b8
   __AUTH_CONST.__const: 0x1200
-  __AUTH_CONST.__cfstring: 0x41e0
-  __AUTH_CONST.__objc_const: 0xee88
+  __AUTH_CONST.__cfstring: 0x4220
+  __AUTH_CONST.__objc_const: 0xeed8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x14f0
-  __DATA.__objc_ivar: 0x92c
+  __DATA.__objc_ivar: 0x930
   __DATA.__data: 0x1740
   __DATA_DIRTY.__objc_data: 0x1360
   __DATA_DIRTY.__bss: 0xd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3238
-  Symbols:   6851
-  CStrings:  982
+  Functions: 3253
+  Symbols:   6873
+  CStrings:  989
 
Symbols:
+ -[CXCallDirectoryHost migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withReply:]
+ -[CXCallDirectoryHost synchronizeExtensionsIfPlistValidationChangesWithReply:]
+ -[CXCallDirectoryManager migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withCompletionHandler:]
+ -[CXCallDirectoryManager synchronizeExtensionsIfPlistValidationChangesWithCompletionHandler:]
+ -[CXCallDirectoryStore featureFlags]
+ -[CXCallDirectoryStore initReadOnly:temporary:featureFlags:error:]
+ -[CXCallDirectoryStore initWithTemplateURL:readOnly:temporary:featureFlags:error:]
+ -[CXCallDirectoryStore migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:error:]
+ -[CXFeatures isCallDirectoryApplicationMigrationEnabled]
+ GCC_except_table18
+ GCC_except_table20
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table85
+ GCC_except_table87
+ GCC_except_table93
+ OBJC_IVAR_$_CXCallDirectoryStore._featureFlags
+ __112-[CXCallDirectoryManager migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withCompletionHandler:]_block_invoke_2
+ __93-[CXCallDirectoryManager synchronizeExtensionsIfPlistValidationChangesWithCompletionHandler:]_block_invoke_2
+ ___112-[CXCallDirectoryManager migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withCompletionHandler:]_block_invoke
+ ___112-[CXCallDirectoryManager migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withCompletionHandler:]_block_invoke_2
+ ___78-[CXCallDirectoryHost synchronizeExtensionsIfPlistValidationChangesWithReply:]_block_invoke
+ ___93-[CXCallDirectoryManager synchronizeExtensionsIfPlistValidationChangesWithCompletionHandler:]_block_invoke
+ ___93-[CXCallDirectoryManager synchronizeExtensionsIfPlistValidationChangesWithCompletionHandler:]_block_invoke_2
+ ___97-[CXCallDirectoryHost migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withReply:]_block_invoke
+ _objc_msgSend$callDirectoryHost:requestedMigrationOfAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withCompletionHandler:
+ _objc_msgSend$callDirectoryHost:requestedToSynchronizeExtensionsIfPlistValidationChangedWithCompletionHandler:
+ _objc_msgSend$featureFlags
+ _objc_msgSend$initReadOnly:temporary:featureFlags:error:
+ _objc_msgSend$initWithTemplateURL:readOnly:temporary:featureFlags:error:
+ _objc_msgSend$isCallDirectoryApplicationMigrationEnabled
+ _objc_msgSend$migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withReply:
+ _objc_msgSend$synchronizeExtensionsIfPlistValidationChangesWithReply:
- -[CXCallDirectoryStore initWithTemplateURL:readOnly:temporary:error:]
- GCC_except_table12
- GCC_except_table17
- GCC_except_table19
- GCC_except_table58
- GCC_except_table60
- GCC_except_table62
- GCC_except_table64
- GCC_except_table84
- GCC_except_table86
- GCC_except_table92
- _objc_msgSend$initWithTemplateURL:readOnly:temporary:error:
CStrings:
+ "CallDirectoryApplicationMigration"
+ "UPDATE Extension SET bundle_id = ? WHERE bundle_id = ?"
+ "[WARN] Application migration is disabled by feature flag"
+ "application-migration"
+ "compactStoreWithReply"
+ "migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withReply:"
+ "synchronizeExtensionsIfPlistValidationChangesWithReply"
```
