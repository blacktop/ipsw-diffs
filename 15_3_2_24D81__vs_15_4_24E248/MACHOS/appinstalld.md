## appinstalld

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/Support/appinstalld`

```diff

-1378.60.22.0.0
-  __TEXT.__text: 0x35d70
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_stubs: 0x4d00
-  __TEXT.__objc_methlist: 0x19b4
+1378.100.35.0.0
+  __TEXT.__text: 0x36a68
+  __TEXT.__auth_stubs: 0xf10
+  __TEXT.__objc_stubs: 0x4d80
+  __TEXT.__objc_methlist: 0x1fdc
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x1508
-  __TEXT.__cstring: 0xca40
-  __TEXT.__objc_methname: 0x729c
+  __TEXT.__gcc_except_tab: 0x174c
+  __TEXT.__cstring: 0xcd66
+  __TEXT.__objc_methname: 0x73d8
   __TEXT.__objc_classname: 0x449
-  __TEXT.__objc_methtype: 0x15f5
+  __TEXT.__objc_methtype: 0x1634
   __TEXT.__oslogstring: 0x693
   __TEXT.__ustring: 0x84
-  __TEXT.__unwind_info: 0x988
-  __DATA_CONST.__auth_got: 0x7a0
+  __TEXT.__unwind_info: 0x9c8
+  __DATA_CONST.__auth_got: 0x798
   __DATA_CONST.__got: 0x298
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xac0
-  __DATA_CONST.__cfstring: 0x5a80
+  __DATA_CONST.__const: 0xac8
+  __DATA_CONST.__cfstring: 0x5b20
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90

   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x300
   __DATA_CONST.__objc_dictobj: 0x780
-  __DATA.__objc_const: 0x48e0
-  __DATA.__objc_selrefs: 0x1698
+  __DATA.__objc_const: 0x3ea0
+  __DATA.__objc_selrefs: 0x1770
   __DATA.__objc_ivar: 0x1a0
   __DATA.__objc_data: 0x910
   __DATA.__data: 0x7d8

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90A562B1-65AC-36DA-AC82-28959DF7C189
-  Functions: 780
-  Symbols:   339
-  CStrings:  2993
+  UUID: FD2E0583-4ED4-36CB-8514-93BED4AC55D5
+  Functions: 794
+  Symbols:   338
+  CStrings:  3018
 
Symbols:
- _strncmp
CStrings:
+ "-[MIClientConnection _finalizeStagedUpdateForIdentifier:completion:]"
+ "-[MIClientConnection _placeholderInstallForStagedIdentifier:completion:]"
+ "-[MIClientConnection allStagedUpdatesWithCompletion:]"
+ "-[MIClientConnection cancelUpdateForStagedIdentifiers:completion:]"
+ "-[MIClientConnection finalizeStagedInstallForIdentifier:returningResultInfo:completion:]"
+ "-[MIClientConnection installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:]"
+ "-[MIInstaller _applyStagedUpdateForIdentifier:withError:]"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileInstallation_Daemon/patch.c"
+ "@28@0:8B16^@20"
+ "@32@0:8^@16^@24"
+ "Failed to clear staged container status for %@ : %@"
+ "Failed to find journaled entry for staged identifier: %@"
+ "Failed to get journaled entries: %@"
+ "Failed to install parallel placeholder for staged update for identifier: %@"
+ "Failed to purge some staged updates. Failed to find: %@ and purge %@ staged identifiers"
+ "Installing parallel placeholder for %@"
+ "Installing parallel placeholder for staged update \"%@\" requested by %@"
+ "Making staged update live for \"%@\" requested by %@"
+ "Not freeing temp container because it is staged: %@"
+ "Returning staged update identifier %@"
+ "Staged Update Placeholder"
+ "System app install missing system app entitlement."
+ "_applyStagedUpdateForIdentifier:withError:"
+ "_finalizeStagedUpdateForIdentifier:completion:"
+ "_gatherLaunchServicesRegistrationInfoForStagedPlaceholder:withError:"
+ "_placeholderInstallForStagedIdentifier:completion:"
+ "allStagedUpdatesWithCompletion:"
+ "applyStagedUpdateForIdentifier:withError:"
+ "cancelUpdateForStagedIdentifiers:completion:"
+ "com.apple.appinstalld.placeholder-install-for-staged-update"
+ "com.apple.appinstalld.placeholder-install-for-staged-update-error"
+ "com.apple.appinstalld.placeholder-installation-for-staged-update-complete"
+ "finalizeStagedInstallForIdentifier:returningResultInfo:completion:"
+ "installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:"
+ "installParallelPlaceholderForStagedUpdateWithResultingRecord:error:"
+ "isStagedContainer"
+ "isStagedUpdate"
+ "journalEntryForIdentifier:"
+ "journaledEntriesCleaningFailuresWithError:"
+ "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
+ "v32@0:8@\"NSSet\"16@?<v@?B@\"NSError\">24"
- "-[MIClientConnection _finalizeStagedUpdateForUUID:completion:]"
- "-[MIClientConnection cancelUpdateForStagedUUID:completion:]"
- "-[MIClientConnection finalizeStagedInstallForUUID:returningResultInfo:completion:]"
- "-[MIInstaller _applyStagedUpdateForUUID:withError:]"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/MobileInstallation_Daemon/patch.c"
- "EOF"
- "Failed to query staged container status %@ : %@"
- "Install of known system app missing system app entitlement"
- "Installing parallel placeholder"
- "Returning staged update UUID %@"
- "System app install missing system app entitlement"
- "Unexpectedly failed to get signing info for bundle %@: %@"
- "_applyStagedUpdateForUUID:withError:"
- "_finalizeStagedUpdateForUUID:completion:"
- "_gatherLaunchServicesRegistrationInfoWithError:"
- "applyStagedUpdateForUUID:withError:"
- "cancelUpdateForStagedUUID:completion:"
- "finalizeStagedInstallForUUID:returningResultInfo:completion:"
- "isStagedUpdateContainer:withError:"
- "journalEntryForUniqueIdentifier:"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"

```
