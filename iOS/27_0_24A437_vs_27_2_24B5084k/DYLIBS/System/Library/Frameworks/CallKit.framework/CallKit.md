## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

```diff

-1403.100.1.0.0
-  __TEXT.__text: 0x64f08
-  __TEXT.__objc_methlist: 0x92a4
+1406.200.51.2.1
+  __TEXT.__text: 0x659a0
+  __TEXT.__objc_methlist: 0x9324
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x63ab
-  __TEXT.__oslogstring: 0x3c25
+  __TEXT.__cstring: 0x641a
+  __TEXT.__oslogstring: 0x3cf6
   __TEXT.__gcc_except_tab: 0x6f8
-  __TEXT.__unwind_info: 0x2908
+  __TEXT.__unwind_info: 0x2938
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xdb8
+  __DATA_CONST.__const: 0xde0
   __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34e8
+  __DATA_CONST.__objc_selrefs: 0x3530
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x4f0
   __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0x4360
-  __AUTH_CONST.__objc_const: 0xf0e8
+  __AUTH_CONST.__cfstring: 0x43a0
+  __AUTH_CONST.__objc_const: 0xf138
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x2300
-  __DATA.__objc_ivar: 0x94c
+  __DATA.__objc_ivar: 0x950
   __DATA.__data: 0x1740
   __DATA_DIRTY.__objc_data: 0x5a0
   __DATA_DIRTY.__bss: 0x80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3244
-  Symbols:   6844
-  CStrings:  1006
+  Functions: 3259
+  Symbols:   6866
+  CStrings:  1013
 
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
+ GCC_except_table13
+ GCC_except_table18
+ GCC_except_table46
+ GCC_except_table51
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table85
+ _OBJC_IVAR_$_CXCallDirectoryStore._featureFlags
+ ___112-[CXCallDirectoryManager migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withCompletionHandler:]_block_invoke
+ ___112-[CXCallDirectoryManager migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withCompletionHandler:]_block_invoke_2
+ ___78-[CXCallDirectoryHost synchronizeExtensionsIfPlistValidationChangesWithReply:]_block_invoke
+ ___93-[CXCallDirectoryManager synchronizeExtensionsIfPlistValidationChangesWithCompletionHandler:]_block_invoke
+ ___93-[CXCallDirectoryManager synchronizeExtensionsIfPlistValidationChangesWithCompletionHandler:]_block_invoke_2
+ ___97-[CXCallDirectoryHost migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withReply:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ _objc_msgSend$callDirectoryHost:requestedMigrationOfAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withCompletionHandler:
+ _objc_msgSend$callDirectoryHost:requestedToSynchronizeExtensionsIfPlistValidationChangedWithCompletionHandler:
+ _objc_msgSend$initReadOnly:temporary:featureFlags:error:
+ _objc_msgSend$initWithTemplateURL:readOnly:temporary:featureFlags:error:
+ _objc_msgSend$isCallDirectoryApplicationMigrationEnabled
+ _objc_msgSend$migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:withReply:
+ _objc_msgSend$synchronizeExtensionsIfPlistValidationChangesWithReply:
- -[CXCallDirectoryStore initWithTemplateURL:readOnly:temporary:error:]
- GCC_except_table12
- GCC_except_table15
- GCC_except_table17
- GCC_except_table43
- GCC_except_table47
- GCC_except_table52
- GCC_except_table56
- GCC_except_table76
- GCC_except_table78
- GCC_except_table84
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
