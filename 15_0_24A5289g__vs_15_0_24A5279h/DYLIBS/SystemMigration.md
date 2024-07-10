## SystemMigration

> `/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/A/SystemMigration`

```diff

-5713.0.1.0.0
-  __TEXT.__text: 0x116fec
-  __TEXT.__auth_stubs: 0x1290
-  __TEXT.__objc_methlist: 0xf488
+5712.0.0.0.1
+  __TEXT.__text: 0x116730
+  __TEXT.__auth_stubs: 0x1270
+  __TEXT.__objc_methlist: 0xf468
   __TEXT.__const: 0x168
   __TEXT.__gcc_except_tab: 0x3a74
-  __TEXT.__cstring: 0x26cc7
+  __TEXT.__cstring: 0x26b42
   __TEXT.__oslogstring: 0x392
   __TEXT.__ustring: 0x36c
-  __TEXT.__unwind_info: 0x3258
+  __TEXT.__unwind_info: 0x3248
   __TEXT.__objc_classname: 0x1744
-  __TEXT.__objc_methname: 0x24bfa
+  __TEXT.__objc_methname: 0x24b75
   __TEXT.__objc_methtype: 0x2e9f
-  __TEXT.__objc_stubs: 0x1c8c0
+  __TEXT.__objc_stubs: 0x1c820
   __DATA_CONST.__got: 0xeb0
   __DATA_CONST.__const: 0x948
   __DATA_CONST.__objc_classlist: 0x5c8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x81a0
+  __DATA_CONST.__objc_selrefs: 0x8178
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0xd28
-  __AUTH_CONST.__auth_got: 0x960
+  __AUTH_CONST.__auth_got: 0x950
   __AUTH_CONST.__const: 0x1ae0
-  __AUTH_CONST.__cfstring: 0x1b760
+  __AUTH_CONST.__cfstring: 0x1b6a0
   __AUTH_CONST.__objc_const: 0x19320
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_arrayobj: 0x420

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libodfde.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 5707
-  Symbols:   13284
-  CStrings:  4258
+  Functions: 5704
+  Symbols:   13274
+  CStrings:  4252
 
Symbols:
+ __27-[SMPaths loadAllFakelinks]_block_invoke.308
+ __30-[SMPaths enumerateFilesystem]_block_invoke.391
- -[SMSystemRuleHandler clearFirmlinkPathContents:]
- -[SMSystemRuleHandler copyFirmlinkContents:newPath:]
- -[SMSystemRuleHandler isPathFirmlink:]
- __27-[SMPaths loadAllFakelinks]_block_invoke.305
- __30-[SMPaths enumerateFilesystem]_block_invoke.388
- _fsctl
- _objc_msgSend$clearFirmlinkPathContents:
- _objc_msgSend$contentsOfDirectoryAtPath:error:
- _objc_msgSend$copyFirmlinkContents:newPath:
- _objc_msgSend$fileURLWithPathComponents:
- _objc_msgSend$isPathFirmlink:
- _removefile
CStrings:
+ "/System/Library/AssetsV2/"
- "%!@(MISSING) is a firmlink, attempting to clear its contents."
- "-[SMSystemRuleHandler clearFirmlinkPathContents:]"
- "-[SMSystemRuleHandler copyFirmlinkContents:newPath:]"
- "Copying children because (oldPathIsFirmlink=%!@(MISSING), newPathIsFirmlink=%!@(MISSING)"
- "Failed to copy %!@(MISSING) to %!@(MISSING): Could not enumerate old path items. %!@(MISSING)"
- "Failed to copy child path %!@(MISSING) to %!@(MISSING): %!@(MISSING)"
- "Unable to remove contents of firmlink %!@(MISSING) (revert to moving aside existing as ~orig): %!s(MISSING)"

```
