## ManagedConfigurationUI

> `/System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI`

```diff

-43.0.0.0.0
-  __TEXT.__text: 0x24ad8
+46.0.0.0.0
+  __TEXT.__text: 0x24a44
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0x3938
+  __TEXT.__objc_methlist: 0x3948
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x61c
-  __TEXT.__cstring: 0x2fa4
+  __TEXT.__cstring: 0x2f67
   __TEXT.__ustring: 0x46
-  __TEXT.__unwind_info: 0xca0
+  __TEXT.__unwind_info: 0xc98
   __TEXT.__objc_classname: 0x9c6
-  __TEXT.__objc_methname: 0xab87
-  __TEXT.__objc_methtype: 0x1f40
+  __TEXT.__objc_methname: 0xabe9
+  __TEXT.__objc_methtype: 0x1f63
   __TEXT.__objc_stubs: 0x7800
-  __DATA_CONST.__got: 0x740
+  __DATA_CONST.__got: 0x738
   __DATA_CONST.__const: 0xa38
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2848
+  __DATA_CONST.__objc_selrefs: 0x2850
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x410
-  __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x2620
-  __AUTH_CONST.__objc_const: 0x5630
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0x25e0
+  __AUTH_CONST.__objc_const: 0x5660
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0xf00
-  __DATA.__objc_ivar: 0x2d8
+  __DATA.__objc_ivar: 0x2dc
   __DATA.__data: 0xb40
   __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x230

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0992C3CB-06EF-34FE-97A2-5D891AA58961
+  UUID: 74EC8F90-17AF-3913-B449-C142FE9B5C82
   Functions: 1111
-  Symbols:   4412
+  Symbols:   4411
   CStrings:  2615
 
Symbols:
+ -[MCUIListController _setIsGuestUserModeActive:]
+ -[MCUIListController isGuestUserModeActive]
+ -[MCUIListController setIsGuestUserModeActive:]
+ -[MCURLListenerListController _presentMDMMigrationAlert]
+ _OBJC_IVAR_$_MCUIListController._isGuestUserModeActive
+ ___48-[MCUIListController _setIsGuestUserModeActive:]_block_invoke
+ ___56-[MCURLListenerListController _presentMDMMigrationAlert]_block_invoke
+ _objc_msgSend$_presentMDMMigrationAlert
+ _objc_msgSend$isGuestUserModeActive
+ _objc_msgSend$mdmMigrationAlert
+ _objc_msgSend$setIsGuestUserModeActive:
- -[MCUIListController _mainQueue_setBeginMigrationButtonEnabled:]
- -[MCUIListController migrationIsAvailable]
- -[MCURLListenerListController _startMigration]
- _OBJC_CLASS_$_DMCMigrationHelper
- ___46-[MCURLListenerListController _startMigration]_block_invoke
- ___46-[MCURLListenerListController _startMigration]_block_invoke_2
- ___64-[MCUIListController _mainQueue_setBeginMigrationButtonEnabled:]_block_invoke
- _objc_msgSend$_mainQueue_setBeginMigrationButtonEnabled:
- _objc_msgSend$_startMigration
- _objc_msgSend$launchMigrationApplicationWithError:
- _objc_msgSend$setBeginMigrationButtonEnabled:
CStrings:
+ "TB,N,V_isGuestUserModeActive"
+ "_isGuestUserModeActive"
+ "_presentMDMMigrationAlert"
+ "_setIsGuestUserModeActive:"
+ "isGuestUserModeActive"
+ "mdmMigrationAlert"
+ "profileConnectionDidRequestCurrentPasscodeContext:needsExtractablePasscode:"
+ "setIsGuestUserModeActive:"
+ "v28@0:8@\"MCProfileConnection\"16B24"
- "MIGRATION_REBOOT_WARNING_TEXT"
- "MIGRATION_REBOOT_WARNING_TITLE"
- "_mainQueue_setBeginMigrationButtonEnabled:"
- "_startMigration"
- "launchMigrationApplicationWithError:"
- "migrationIsAvailable"
- "setBeginMigrationButtonEnabled:"

```
