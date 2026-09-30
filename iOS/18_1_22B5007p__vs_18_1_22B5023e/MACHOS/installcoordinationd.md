## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-627.0.0.0.0
-  __TEXT.__text: 0x8c1bc
+628.40.1.0.0
+  __TEXT.__text: 0x8d2ac
   __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_stubs: 0x95c0
-  __TEXT.__objc_methlist: 0x45b0
+  __TEXT.__objc_stubs: 0x96e0
+  __TEXT.__objc_methlist: 0x4638
   __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x14add
-  __TEXT.__objc_classname: 0x895
-  __TEXT.__oslogstring: 0xc11c
+  __TEXT.__cstring: 0x14e6c
+  __TEXT.__objc_classname: 0x8a7
+  __TEXT.__oslogstring: 0xc251
   __TEXT.__objc_methtype: 0x201b
-  __TEXT.__objc_methname: 0xe80d
-  __TEXT.__gcc_except_tab: 0x27d8
+  __TEXT.__objc_methname: 0xe973
+  __TEXT.__gcc_except_tab: 0x27e0
   __TEXT.__ustring: 0x26c
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x2070
+  __TEXT.__unwind_info: 0x20b0
   __DATA_CONST.__auth_got: 0x7b8
-  __DATA_CONST.__got: 0x3a0
+  __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x25a8
-  __DATA_CONST.__cfstring: 0x7bc0
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __DATA_CONST.__const: 0x2610
+  __DATA_CONST.__cfstring: 0x7d60
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xbed0
-  __DATA.__objc_selrefs: 0x2bd8
-  __DATA.__objc_ivar: 0x408
-  __DATA.__objc_data: 0x1360
+  __DATA.__objc_const: 0xbf90
+  __DATA.__objc_selrefs: 0x2c20
+  __DATA.__objc_ivar: 0x40c
+  __DATA.__objc_data: 0x13b0
   __DATA.__data: 0x5f0
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x1e0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/FontServices.framework/FontServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2823
-  Symbols:   375
-  CStrings:  4774
+  Functions: 2845
+  Symbols:   377
+  CStrings:  4808
 
Symbols:
+ _OBJC_CLASS_$_APApplication
+ _OBJC_CLASS_$_APGuard
CStrings:
+ "%!s(MISSING): App with identity %!@(MISSING) needs to be unlocked before it can be uninstalled : %!@(MISSING)"
+ "%!s(MISSING): Auth was unsuccessful. Error: %!@(MISSING)"
+ "%!s(MISSING): Client %!@(MISSING) is missing ignore app protection operation entitlement. : %!@(MISSING)"
+ "%!s(MISSING): Failed to create app unlock alert for app with bundle ID %!@(MISSING) : %!@(MISSING)"
+ "%!s(MISSING): No record specified with unlock prompt : %!@(MISSING)"
+ "-[IXSAppUninstaller _displayAuthenticationError]_block_invoke"
+ "-[IXSAppUninstaller _promptForUnlockOfAppRecord:identity:clientName:flags:completion:isRemovable:]"
+ "-[IXSAppUninstaller _promptForUnlockOfAppRecord:identity:clientName:flags:completion:isRemovable:]_block_invoke"
+ "-[IXSAppUninstaller _promptForUnlockOfAppRecord:identity:clientName:flags:completion:isRemovable:]_block_invoke_2"
+ "11:12:11"
+ "<confirmation:%!c(MISSING) wait:%!c(MISSING) archive:%!c(MISSING) demote:%!c(MISSING) notAllowed:%!c(MISSING) ignoreRemovability:%!c(MISSING) ignoreRestrictions:%!c(MISSING) ignoreAppProtection:%!c(MISSING)>"
+ "AUTHENTICATE"
+ "AUTHENTICATE_TO_DELETE_APP_MESSAGE"
+ "AUTHENTICATE_TO_DELETE_APP_TITLE"
+ "App with identity %!@(MISSING) needs to be unlocked before it can be uninstalled"
+ "Aug  3 2024"
+ "Authenticate"
+ "Authenticate To Delete \"%!@(MISSING)\""
+ "Authentication is required to delete this app."
+ "COULD_NOT_AUTHENTICATE"
+ "Client %!@(MISSING) is missing ignore app protection operation entitlement."
+ "Failed to create app unlock alert for app with bundle ID %!@(MISSING)"
+ "IXFrameworkBundle_block_invoke"
+ "IXSAppUnlockAlert"
+ "No record specified with unlock prompt"
+ "TB,N,V_ignoreAppProtection"
+ "_displayAuthenticationError"
+ "_ignoreAppProtection"
+ "_promptForUnlockOfAppRecord:identity:clientName:flags:completion:isRemovable:"
+ "applicationWithBundleIdentifier:"
+ "authenticateUnconditionallyWithReason:completion:"
+ "com.apple.private.InstallCoordination.ignoreAppProtection"
+ "displayAlertWithCompletion:uninstallAlertConfiguration:"
+ "ignoreAppProtection"
+ "ignoreAppProtection"
+ "isLocked"
+ "setIgnoreAppProtection:"
+ "sharedGuard"
- "04:30:57"
- "<confirmation:%!c(MISSING) wait:%!c(MISSING) archive:%!c(MISSING) demote:%!c(MISSING) notAllowed:%!c(MISSING) ignoreRemovability:%!c(MISSING) ignoreRestrictions:%!c(MISSING)>"
- "Jul 12 2024"
- "_SharedFrameworkBundle_block_invoke"

```
