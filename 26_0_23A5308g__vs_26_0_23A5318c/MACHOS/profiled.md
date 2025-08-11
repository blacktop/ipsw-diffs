## profiled

> `/usr/libexec/profiled`

```diff

-2426.1.0.0.0
-  __TEXT.__text: 0xa0550
-  __TEXT.__auth_stubs: 0x20e0
+2428.0.0.0.0
+  __TEXT.__text: 0xa07b4
+  __TEXT.__auth_stubs: 0x20f0
   __TEXT.__objc_stubs: 0x10560
-  __TEXT.__objc_methlist: 0x5acc
+  __TEXT.__objc_methlist: 0x5aec
   __TEXT.__const: 0x20e
   __TEXT.__gcc_except_tab: 0x1c24
-  __TEXT.__oslogstring: 0xd761
+  __TEXT.__oslogstring: 0xd962
   __TEXT.__cstring: 0x89ff
-  __TEXT.__objc_methname: 0x14566
+  __TEXT.__objc_methname: 0x145a4
   __TEXT.__objc_classname: 0xb5b
   __TEXT.__objc_methtype: 0x2239
-  __TEXT.__unwind_info: 0x1748
-  __DATA_CONST.__auth_got: 0x1080
+  __TEXT.__unwind_info: 0x1758
+  __DATA_CONST.__auth_got: 0x1088
   __DATA_CONST.__got: 0x1bb8
   __DATA_CONST.__const: 0x1b90
   __DATA_CONST.__cfstring: 0x85e0

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x6588
-  __DATA.__objc_selrefs: 0x48e0
+  __DATA.__objc_const: 0x6590
+  __DATA.__objc_selrefs: 0x48f0
   __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x540

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 185FD153-3A9A-30CE-BC07-911DC0917985
-  Functions: 2045
-  Symbols:   1459
-  CStrings:  6136
+  UUID: FF68BBC3-4B8D-3A5C-8D52-AEA8D6956B14
+  Functions: 2046
+  Symbols:   1460
+  CStrings:  6145
 
Symbols:
+ _MCRemoveFileIfExists
CStrings:
+ "Locale changed: Reapplying app enforced restrictions"
+ "MCCleanupMigrator: Cloud config file still exists after MCProfileMigrator!"
+ "MCCleanupMigrator: Failed to remove cloud config with error: %{public}@."
+ "MCCleanupMigrator: Failed to remove legacy cloud config with error: %{public}@."
+ "MCCleanupMigrator: Failed to remove legacy post Setup auto install profile with error: %{public}@."
+ "MCCleanupMigrator: Failed to remove post Setup auto install profile with error: %{public}@."
+ "Removing orphaned client restrictions..."
+ "_removeCloudConfigAndAutoInstallProfile"
+ "isLockdownModeEnabled"

```
