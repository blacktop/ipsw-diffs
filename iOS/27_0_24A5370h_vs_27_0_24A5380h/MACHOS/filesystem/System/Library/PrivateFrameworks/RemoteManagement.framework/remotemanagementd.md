## remotemanagementd

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd`

```diff

-  __TEXT.__text: 0x8a298
+  __TEXT.__text: 0x8b2b8
   __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_stubs: 0xc320
-  __TEXT.__objc_methlist: 0x49e8
+  __TEXT.__objc_stubs: 0xc360
+  __TEXT.__objc_methlist: 0x4a28
   __TEXT.__const: 0xf0
   __TEXT.__gcc_except_tab: 0x3fe8
-  __TEXT.__cstring: 0x2fac
-  __TEXT.__objc_classname: 0xff8
-  __TEXT.__objc_methname: 0xf0ac
+  __TEXT.__cstring: 0x3019
+  __TEXT.__objc_classname: 0x1032
+  __TEXT.__objc_methname: 0xf0f9
   __TEXT.__objc_methtype: 0x265b
-  __TEXT.__oslogstring: 0xc217
-  __TEXT.__ustring: 0x246
-  __TEXT.__unwind_info: 0x2098
-  __DATA_CONST.__const: 0x2740
-  __DATA_CONST.__cfstring: 0x33e0
-  __DATA_CONST.__objc_classlist: 0x2f0
+  __TEXT.__oslogstring: 0xc31b
+  __TEXT.__ustring: 0x2ec
+  __TEXT.__unwind_info: 0x20a0
+  __DATA_CONST.__const: 0x2760
+  __DATA_CONST.__cfstring: 0x3460
+  __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x150
   __DATA_CONST.__auth_got: 0x440
-  __DATA_CONST.__got: 0x930
-  __DATA.__objc_const: 0x8598
-  __DATA.__objc_selrefs: 0x3508
+  __DATA_CONST.__got: 0x9f8
+  __DATA.__objc_const: 0x86a8
+  __DATA.__objc_selrefs: 0x3518
   __DATA.__objc_ivar: 0x2ac
-  __DATA.__objc_data: 0x1d60
+  __DATA.__objc_data: 0x1db0
   __DATA.__data: 0xc68
-  __DATA.__bss: 0x590
+  __DATA.__bss: 0x5a0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2553
+  Functions: 2566
   Symbols:   434
-  CStrings:  4488
+  CStrings:  4505
 
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
+ "Ignoring migration: not system scoped"
+ "Ignoring migration: old database does not exist"
+ "New database exists, removing old directory"
+ "RMMigrationProtectedContainer"
+ "Starting migration from %{public}@ to %{public}@"
+ "createMissingStatusValueErrorWithKeyPath:"
+ "isEqualToArray:"
+ "migrationProtectedContainer"
+ "predicateStatusItemsError:forActivation:"
- "Not OK to migrate: new database exists"
- "Not OK to migrate: old database does not exist"
- "_directoryExistsAtURL:"
- "_okToMigrateFromURL:toURL:"

```
