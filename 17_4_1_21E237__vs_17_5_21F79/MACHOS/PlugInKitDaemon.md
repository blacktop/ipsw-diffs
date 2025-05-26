## PlugInKitDaemon

> `/System/Library/PrivateFrameworks/PlugInKitDaemon.framework/PlugInKitDaemon`

```diff

-473.100.2.0.0
-  __TEXT.__text: 0x17244
+473.120.3.0.0
+  __TEXT.__text: 0x1759c
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_stubs: 0x2fc0
-  __TEXT.__objc_methlist: 0xd44
+  __TEXT.__objc_stubs: 0x2fe0
+  __TEXT.__objc_methlist: 0xd7c
   __TEXT.__const: 0x6a
-  __TEXT.__objc_methname: 0x2e67
-  __TEXT.__oslogstring: 0x2abd
-  __TEXT.__cstring: 0x1091
+  __TEXT.__objc_methname: 0x2ebb
+  __TEXT.__oslogstring: 0x2b07
+  __TEXT.__cstring: 0x10b4
   __TEXT.__objc_classname: 0x190
-  __TEXT.__objc_methtype: 0x6c8
+  __TEXT.__objc_methtype: 0x6f3
   __TEXT.__gcc_except_tab: 0x374
-  __TEXT.__unwind_info: 0x3e4
+  __TEXT.__unwind_info: 0x460
   __DATA_CONST.__auth_got: 0x5c0
   __DATA_CONST.__got: 0x398
   __DATA_CONST.__const: 0x4f0
-  __DATA_CONST.__cfstring: 0x1020
+  __DATA_CONST.__cfstring: 0x1040
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x2a80
-  __DATA.__objc_selrefs: 0xd08
-  __DATA.__objc_ivar: 0x110
+  __DATA.__objc_const: 0x2af0
+  __DATA.__objc_selrefs: 0xd20
+  __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x300
   __DATA.__bss: 0x68

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 412
-  Symbols:   1434
-  CStrings:  1065
+  Functions: 419
+  Symbols:   1443
+  CStrings:  1073
 
Symbols:
+ -[PKDExternalProviders initWithUserManagementProvider:]
+ -[PKDPersonaCache external]
+ -[PKDPersonaCache initWithExternalProviders:]
+ -[PKDPersonaCache lock_isSyncedSuccessfully]
+ -[PKDPersonaCache personasForBundleIdentifier:error:]
+ -[PKDPlugIn _personaIDForClient:requestedPersona:].cold.5
+ -[PKDUserManagementProvider listAllPersonaAttributesWithError:]
+ -[PKDUserManagementProvider personaGenerationIdentifierWithError:]
+ OBJC_IVAR_$_PKDPersonaCache._external
+ OBJC_IVAR_$_PKDPersonaCache._lock_isSyncedSuccessfully
+ _OBJC_$_PROP_LIST_PKDExternalProviders.97
+ _OBJC_$_PROP_LIST_PKDUserManagementProvider.50
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _objc_msgSend$initWithExternalProviders:
+ _objc_msgSend$isSharedIPad
+ _objc_msgSend$personasForBundleIdentifier:error:
- -[PKDPersonaCache init]
- -[PKDPersonaCache personasForBundleIdentifier:]
- -[PKDPersonaCache sharedUserManager]
- OBJC_IVAR_$_PKDPersonaCache._sharedUserManager
- _OBJC_$_PROP_LIST_PKDExternalProviders.96
- _OBJC_$_PROP_LIST_PKDUserManagementProvider.45
- _objc_msgSend$personasForBundleIdentifier:
- _objc_msgSend$sharedUserManager
CStrings:
+ "@\"NSArray\"24@0:8^@16"
+ "@24@0:8^@16"
+ "@32@0:8@16^@24"
+ "Q24@0:8^@16"
+ "TB,R,N,V_lock_isSyncedSuccessfully"
+ "[u %{public}@] [%@(%@)] failed for get personas for bundle identifier: %@"
+ "_lock_isSyncedSuccessfully"
+ "failed to sync with UserManagement"
+ "initWithExternalProviders:"
+ "initWithUserManagementProvider:"
+ "isSharedIPad"
+ "lock_isSyncedSuccessfully"
+ "personasForBundleIdentifier:error:"
- "@\"UMUserManager\""
- "T@\"UMUserManager\",R,N,V_sharedUserManager"
- "_sharedUserManager"
- "personasForBundleIdentifier:"
- "sharedUserManager"

```
