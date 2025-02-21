## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

```diff

-1378.60.22.0.0
-  __TEXT.__text: 0xa12e4
+1378.100.33.0.0
+  __TEXT.__text: 0xa1d20
   __TEXT.__auth_stubs: 0x1370
-  __TEXT.__objc_methlist: 0x4468
+  __TEXT.__objc_methlist: 0x47b4
   __TEXT.__const: 0xf6c0
-  __TEXT.__gcc_except_tab: 0xa90
-  __TEXT.__cstring: 0x15f54
+  __TEXT.__gcc_except_tab: 0xa8c
+  __TEXT.__cstring: 0x16159
   __TEXT.__dlopen_cstrs: 0x111
   __TEXT.__oslogstring: 0x8b6
-  __TEXT.__unwind_info: 0x13c0
-  __TEXT.__eh_frame: 0xd78
+  __TEXT.__unwind_info: 0x13c8
+  __TEXT.__eh_frame: 0xd70
   __TEXT.__objc_classname: 0x567
-  __TEXT.__objc_methname: 0xd0dc
-  __TEXT.__objc_methtype: 0x17d9
-  __TEXT.__objc_stubs: 0x8280
-  __DATA_CONST.__got: 0x3f8
+  __TEXT.__objc_methname: 0xd1e7
+  __TEXT.__objc_methtype: 0x17f9
+  __TEXT.__objc_stubs: 0x8300
+  __DATA_CONST.__got: 0x400
   __DATA_CONST.__const: 0xc48
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26b8
+  __DATA_CONST.__objc_selrefs: 0x2838
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__objc_arraydata: 0x978
+  __DATA_CONST.__objc_arraydata: 0x9c0
   __AUTH_CONST.__auth_got: 0x9c8
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x54a8
-  __AUTH_CONST.__cfstring: 0xc240
-  __AUTH_CONST.__objc_const: 0x7fd0
-  __AUTH_CONST.__objc_dictobj: 0x11a8
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__const: 0x5468
+  __AUTH_CONST.__cfstring: 0xc300
+  __AUTH_CONST.__objc_const: 0x7a48
+  __AUTH_CONST.__objc_dictobj: 0x11f8
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_ivar: 0x508
-  __DATA.__data: 0x1160
+  __DATA.__objc_ivar: 0x50c
+  __DATA.__data: 0x1158
   __DATA.__bss: 0xf0
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x1180

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1852
-  Symbols:   2252
-  CStrings:  4272
+  Functions: 1870
+  Symbols:   2291
+  CStrings:  4288
 
Symbols:
+ _OBJC_CLASS_$_MIMCMContainer
+ _OBJC_METACLASS_$_MIMCMContainer
CStrings:
+ "-[MIContainer _doInitWithContainer:error:]"
+ "-[MIContainer _isStagedUpdateContainer:withError:]"
+ "CF_MIEmergencyOffloadVersion"
+ "Did not find any placeholder entitlements in %@"
+ "Failed to clear staged update container %@ after failing to make it live %@ : %@"
+ "Failed to read placeholder entitlements file from %@"
+ "Found emergency offloaded app %@ from OS build %@"
+ "Found empty entitlements for %@ at %@"
+ "Found empty placeholder entitlements in %@"
+ "Found no entitlements for %@ at %@"
+ "Skipping purging of transient container because it is staged: %@"
+ "TB,N,V_isStagedContainer"
+ "This app has the same bundle ID (\"%@\") as a known deletable system app but is missing the required entitlement \"%@\" = true (boolean)."
+ "This app has the same bundle ID (\"%@\") as a known deletable system app, but was signed with no entitlements at all and thus is missing the required entitlement \"%@\" = true (boolean)."
+ "_isStagedContainer"
+ "_isStagedUpdateContainer:withError:"
+ "allStagedUpdatesWithCompletion:"
+ "cancelUpdateForStagedIdentifiers:completion:"
+ "dictionaryWithContentsOfURL:error:"
+ "emergencyOffloadVersion"
+ "finalizeStagedInstallForIdentifier:returningResultInfo:completion:"
+ "installParallelPlaceholderForStagedIdentifier:returningResultInfo:completion:"
+ "isStagedContainer"
+ "setIsStagedContainer:"
+ "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
+ "v32@0:8@\"NSSet\"16@?<v@?B@\"NSError\">24"
- "-[MIContainer isStagedUpdateContainer:withError:]"
- "Clearing staged container requested for non transient container"
- "Could not get entitlements from %@"
- "Failed to clear staged update container after failing to make it live %@ : %@"
- "Failed to query staged container status %@ : %@. Treating it as staged."
- "Unknown watchkit version value: %hhu"
- "cancelUpdateForStagedUUID:completion:"
- "finalizeStagedInstallForUUID:returningResultInfo:completion:"
- "isStagedUpdateContainer:withError:"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"

```
