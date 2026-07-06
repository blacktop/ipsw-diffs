## remotemanagementd

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd`

```diff

-  __TEXT.__text: 0x94ec0
+  __TEXT.__text: 0x960d8
   __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_stubs: 0xc260
-  __TEXT.__objc_methlist: 0x49f0
+  __TEXT.__objc_stubs: 0xc320
+  __TEXT.__objc_methlist: 0x4a30
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x4104
-  __TEXT.__cstring: 0x3057
-  __TEXT.__objc_classname: 0xff8
-  __TEXT.__objc_methname: 0xeef1
+  __TEXT.__cstring: 0x30c4
+  __TEXT.__objc_classname: 0x1032
+  __TEXT.__objc_methname: 0xef8c
   __TEXT.__objc_methtype: 0x265b
-  __TEXT.__oslogstring: 0xc316
-  __TEXT.__ustring: 0x246
-  __TEXT.__unwind_info: 0x20d8
-  __DATA_CONST.__const: 0x2898
-  __DATA_CONST.__cfstring: 0x3460
-  __DATA_CONST.__objc_classlist: 0x2f0
+  __TEXT.__oslogstring: 0xc418
+  __TEXT.__ustring: 0x2ec
+  __TEXT.__unwind_info: 0x20e8
+  __DATA_CONST.__const: 0x28b8
+  __DATA_CONST.__cfstring: 0x34e0
+  __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__auth_got: 0x398
-  __DATA_CONST.__got: 0x8d0
-  __DATA.__objc_const: 0x8598
-  __DATA.__objc_selrefs: 0x34c0
+  __DATA_CONST.__got: 0x998
+  __DATA.__objc_const: 0x86a8
+  __DATA.__objc_selrefs: 0x34e0
   __DATA.__objc_ivar: 0x2ac
-  __DATA.__objc_data: 0x1d60
+  __DATA.__objc_data: 0x1db0
   __DATA.__data: 0xc60
-  __DATA.__bss: 0x588
+  __DATA.__bss: 0x598
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2633
+  Functions: 2646
   Symbols:   401
-  CStrings:  4493
+  CStrings:  4512
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__objc_methtype : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
CStrings:
+ "%@ has unpublished predicate status items, leaving state unchanged"
+ "%@ predicate references errored status items: %{public}@"
+ "Activation’s (%@:%@) predicate (%@) references status items in an error state: %@."
+ "Error.PredicateStatusItemsError"
+ "ErroredStatusItems"
+ "Failed to remove old directory: %{public}@"
+ "Ignoring migration: not user scoped"
+ "Ignoring migration: old database does not exist"
+ "New database exists, removing old directory"
+ "RMMigrationProtectedContainer"
+ "Starting migration from %{public}@ to %{public}@"
+ "createMissingStatusValueErrorWithKeyPath:"
+ "dataVaultDirectoryURLInDomain:createIfNeeded:"
+ "isEqualToArray:"
+ "migrationProtectedContainer"
+ "oldBaseDirectoryURLInUserDomain"
+ "predicateStatusItemsError:forActivation:"
- "Not OK to migrate: new database exists"
- "Not OK to migrate: old database does not exist"
- "_directoryExistsAtURL:"
- "_okToMigrateFromURL:toURL:"

```
