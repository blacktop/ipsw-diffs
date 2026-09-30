## DataMigration

> `/System/Library/PrivateFrameworks/DataMigration.framework/DataMigration`

```diff

-2858.0.0.0.0
-  __TEXT.__text: 0x71b4
-  __TEXT.__objc_methlist: 0x960
-  __TEXT.__cstring: 0x1769
+2858.1.3.0.0
+  __TEXT.__text: 0x73d4
+  __TEXT.__objc_methlist: 0x970
+  __TEXT.__cstring: 0x17f9
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x74
-  __TEXT.__unwind_info: 0x3a0
+  __TEXT.__unwind_info: 0x3a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1a8
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x690
+  __DATA_CONST.__objc_selrefs: 0x698
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__got: 0x168
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x1060
+  __DATA_CONST.__got: 0x170
+  __AUTH_CONST.__const: 0x160
+  __AUTH_CONST.__cfstring: 0x10a0
   __AUTH_CONST.__objc_const: 0xdc8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 244
-  Symbols:   715
-  CStrings:  171
+  Functions: 247
+  Symbols:   720
+  CStrings:  173
 
Symbols:
+ +[DMConnection _migrationPluginResultsAllowedClasses]
+ +[DMConnection _migrationPluginResultsFromArchivedData:error:]
+ GCC_except_table14
+ GCC_except_table21
+ _NSDebugDescriptionErrorKey
+ ___53+[DMConnection _migrationPluginResultsAllowedClasses]_block_invoke
+ __migrationPluginResultsAllowedClasses.allowedClasses
+ __migrationPluginResultsAllowedClasses.onceToken
+ _objc_autorelease
+ _objc_msgSend$_migrationPluginResultsAllowedClasses
+ _objc_msgSend$_migrationPluginResultsFromArchivedData:error:
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
- -[DMMigrationDeferredExitManager _exitClean]
- GCC_except_table15
- GCC_except_table18
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- _objc_msgSend$_exitClean
- _objc_msgSend$unarchivedObjectOfClass:fromData:error:
- _xpc_transaction_exit_clean
CStrings:
+ "Data migrator -migrationPluginResults: did unarchive a %@ instead of a dictionary; discarding it"
+ "cancelDeferredExitWithConnection: will end transaction"
+ "deferred exit did timeout. will end transaction"
+ "migration plugin results archive root was a %@, not a dictionary"
- "cancelDeferredExitWithConnection: will end transaction and exit"
- "deferred exit did timeout. will end transaction and exit"
```
