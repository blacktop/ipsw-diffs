## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/Versions/A/InstalledContentLibrary`

```diff

-1378.60.22.0.0
-  __TEXT.__text: 0xab378
-  __TEXT.__auth_stubs: 0x1020
-  __TEXT.__objc_methlist: 0x3bec
-  __TEXT.__cstring: 0x125a1
-  __TEXT.__const: 0x79c0
+1378.100.35.0.0
+  __TEXT.__text: 0xaf5d4
+  __TEXT.__auth_stubs: 0x1010
+  __TEXT.__objc_methlist: 0x3e5c
+  __TEXT.__cstring: 0x127ba
+  __TEXT.__const: 0x7980
   __TEXT.__oslogstring: 0x588
   __TEXT.__gcc_except_tab: 0x7dc
   __TEXT.__dlopen_cstrs: 0x5d
-  __TEXT.__unwind_info: 0xfa8
+  __TEXT.__unwind_info: 0xfb8
   __TEXT.__objc_classname: 0x4ac
-  __TEXT.__objc_methname: 0xb206
-  __TEXT.__objc_methtype: 0x12ae
-  __TEXT.__objc_stubs: 0x6b60
-  __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x698
+  __TEXT.__objc_methname: 0xb311
+  __TEXT.__objc_methtype: 0x12ce
+  __TEXT.__objc_stubs: 0x6be0
+  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__const: 0x660
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2150
+  __DATA_CONST.__objc_selrefs: 0x2248
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x130
-  __DATA_CONST.__objc_arraydata: 0x688
-  __AUTH_CONST.__auth_got: 0x820
-  __AUTH_CONST.__const: 0x9340
-  __AUTH_CONST.__cfstring: 0xa200
-  __AUTH_CONST.__objc_const: 0x7200
-  __AUTH_CONST.__objc_dictobj: 0xf00
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__objc_arraydata: 0x6d0
+  __AUTH_CONST.__auth_got: 0x818
+  __AUTH_CONST.__const: 0x90e0
+  __AUTH_CONST.__cfstring: 0xa2e0
+  __AUTH_CONST.__objc_const: 0x6e40
+  __AUTH_CONST.__objc_dictobj: 0xf50
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_ivar: 0x4b0
-  __DATA.__data: 0x790
-  __DATA.__bss: 0x1c8
-  __DATA.__common: 0x9f8
+  __DATA.__objc_ivar: 0x4b4
+  __DATA.__data: 0x780
+  __DATA.__bss: 0x1b0
+  __DATA.__common: 0x9f0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 33C949F0-4F22-3E1A-A628-AB938FDBF953
-  Functions: 1642
-  Symbols:   3827
-  CStrings:  4924
+  UUID: 0F786A83-12C3-3DB8-A0BD-2C4C67123E9B
+  Functions: 1675
+  Symbols:   3858
+  CStrings:  4948
 
Symbols:
+ +[MIBundle bundleIsInDenyList:].cold.1
+ +[MIExecutableBundle isGrandfatheredNonContainerizedForSigningInfo:].cold.1
+ -[MIBundle _infoPlistKeysToLoad].cold.1
+ -[MIBundle emergencyOffloadVersion]
+ -[MIContainer _isStagedUpdateContainer:withError:]
+ -[MIContainer isStagedContainer]
+ -[MIContainer setIsStagedContainer:]
+ -[MIGlobalConfiguration _isInternalReleaseType].cold.1
+ -[MIGlobalConfiguration installationBlacklist].cold.1
+ -[MIGlobalConfiguration primaryPersonaString].cold.1
+ -[MIInstalledInfoGatherer _populateBundleRecord:error:].cold.1
+ -[MIInstalledInfoGatherer _populateBundleRecord:error:].cold.2
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:].cold.1
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:].cold.2
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:].cold.3
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:].cold.4
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:].cold.5
+ -[MILaunchServicesDatabaseGatherer _scanBundle:inContainer:addingToBundleSet:enumeratingEntry:withError:].cold.6
+ -[MILaunchServicesDatabaseGatherer scanAppExtensionsInFrameworkBundle:withError:].cold.1
+ -[MILaunchServicesDatabaseGatherer scanAppExtensionsInFrameworkBundle:withError:].cold.2
+ -[MILaunchServicesDatabaseGatherer scanAppExtensionsInFrameworkBundle:withError:].cold.3
+ -[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:forPersona:withError:].cold.1
+ -[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:forPersona:withError:].cold.2
+ -[MILaunchServicesDatabaseGatherer scanExecutableBundle:inContainer:forPersona:withError:].cold.3
+ GCC_except_table106
+ MICopyCurrentBuildVersion.cold.1
+ MICopyExtensionCacheEntryWithPlatform.cold.1
+ MIGetCurrentMobileUserInfo.cold.1
+ OBJC_IVAR_$_MIContainer._isStagedContainer
+ __DTypeForVFSType
+ __block_literal_global.190
+ __block_literal_global.323
+ __block_literal_global.329
+ __block_literal_global.375
+ __block_literal_global.380
+ _objc_msgSend$_isStagedUpdateContainer:withError:
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$emergencyOffloadVersion
+ _objc_msgSend$isStagedContainer
+ _objc_msgSend$setIsStagedContainer:
- -[MIContainer isStagedUpdateContainer:withError:]
- GCC_except_table105
- __block_literal_global.187
- __block_literal_global.320
- __block_literal_global.326
- __block_literal_global.372
- __block_literal_global.377
- _dlclose
- _objc_msgSend$isStagedUpdateContainer:withError:
CStrings:
+ "-[MIContainer _doInitWithContainer:error:]"
+ "-[MIContainer _isStagedUpdateContainer:withError:]"
+ "CF_MIEmergencyOffloadVersion"
+ "Did not find any placeholder entitlements in %@"
+ "Failed to clear staged update container %@ after failing to make it live %@ : %@"
+ "Failed to query staged container status %@ : %@"
+ "Failed to read placeholder entitlements file from %@"
+ "Found emergency offloaded app %@ from OS build %@"
+ "Found empty entitlements for %@ at %@"
+ "Found empty placeholder entitlements in %@"
+ "Found no entitlements for %@ at %@"
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
- "cancelUpdateForStagedUUID:completion:"
- "finalizeStagedInstallForUUID:returningResultInfo:completion:"
- "isStagedUpdateContainer:withError:"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"

```
