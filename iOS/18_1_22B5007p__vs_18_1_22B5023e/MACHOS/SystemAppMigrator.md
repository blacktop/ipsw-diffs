## SystemAppMigrator

> `/System/Library/DataClassMigrators/SystemAppMigrator.migrator/SystemAppMigrator`

```diff

-1378.0.23.0.0
-  __TEXT.__text: 0xa678
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_stubs: 0x18a0
+1378.40.3.0.0
+  __TEXT.__text: 0xa620
+  __TEXT.__auth_stubs: 0x8a0
+  __TEXT.__objc_stubs: 0x1880
   __TEXT.__objc_methlist: 0x5c4
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x340
-  __TEXT.__cstring: 0x34d2
-  __TEXT.__objc_methname: 0x249a
+  __TEXT.__gcc_except_tab: 0x34c
+  __TEXT.__cstring: 0x347b
+  __TEXT.__objc_methname: 0x2460
   __TEXT.__objc_classname: 0xbf
   __TEXT.__objc_methtype: 0x568
   __TEXT.__oslogstring: 0x142
   __TEXT.__unwind_info: 0x268
-  __DATA_CONST.__auth_got: 0x468
+  __DATA_CONST.__auth_got: 0x460
   __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x3a0
-  __DATA_CONST.__cfstring: 0x18c0
+  __DATA_CONST.__const: 0x378
+  __DATA_CONST.__cfstring: 0x18a0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0xe18
-  __DATA.__objc_selrefs: 0x748
+  __DATA.__objc_selrefs: 0x740
   __DATA.__objc_ivar: 0x68
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 167
-  Symbols:   237
-  CStrings:  655
+  Functions: 166
+  Symbols:   236
+  CStrings:  653
 
Symbols:
- _objc_retain_x9
CStrings:
+ "MISystemAppMigrator: Got unexpected disposition %!@(MISSING) when uninstalling %!@(MISSING)"
+ "setIgnoreRemovability:"
+ "setIgnoreRestrictions:"
- "MISystemAppMigrator: Failed to uninstall app %!@(MISSING), resultant disposition: %!@(MISSING)"
- "MISystemAppMigrator: Failed to update removability for %!@(MISSING) to PossibleAndAllowed: %!@(MISSING)"
- "setRemovability:forAppWithIdentity:byClient:completion:"
- "setRequestUserConfirmation:"
- "setWaitForDeletion:"

```
