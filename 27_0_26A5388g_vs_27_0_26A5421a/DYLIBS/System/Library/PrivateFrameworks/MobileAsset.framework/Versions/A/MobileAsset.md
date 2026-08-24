## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset`

```diff

-2215.0.16.0.0
-  __TEXT.__text: 0x95c7c
-  __TEXT.__objc_methlist: 0x6d74
+2215.0.20.0.0
+  __TEXT.__text: 0x979ac
+  __TEXT.__objc_methlist: 0x6f64
   __TEXT.__const: 0x2b4
-  __TEXT.__cstring: 0x13a45
-  __TEXT.__oslogstring: 0xb893
-  __TEXT.__gcc_except_tab: 0x1310
-  __TEXT.__unwind_info: 0x1ea8
+  __TEXT.__cstring: 0x13df4
+  __TEXT.__oslogstring: 0xbac1
+  __TEXT.__gcc_except_tab: 0x136c
+  __TEXT.__unwind_info: 0x1f10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1038
-  __DATA_CONST.__objc_classlist: 0x280
+  __DATA_CONST.__const: 0x1058
+  __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3808
+  __DATA_CONST.__objc_selrefs: 0x38a8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x248
+  __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x350
-  __DATA_CONST.__got: 0x470
-  __AUTH_CONST.__const: 0x2160
-  __AUTH_CONST.__cfstring: 0xfcc0
-  __AUTH_CONST.__objc_const: 0xa970
+  __DATA_CONST.__got: 0x480
+  __AUTH_CONST.__const: 0x2190
+  __AUTH_CONST.__cfstring: 0x10020
+  __AUTH_CONST.__objc_const: 0xac90
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xb40
-  __DATA.__objc_ivar: 0x90c
+  __AUTH.__objc_data: 0xbe0
+  __DATA.__objc_ivar: 0x92c
   __DATA.__data: 0x358
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x198

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3125
-  Symbols:   6265
-  CStrings:  2814
+  Functions: 3165
+  Symbols:   6350
+  CStrings:  2846
 
Symbols:
+ +[MAAutoAssetMigrationInfo supportsSecureCoding]
+ +[MAAutoAssetMigrationResults supportsSecureCoding]
+ +[MAAutoAssetSet preinstalledAssetMigrationResults:]
+ -[MAAutoAssetMigrationInfo .cxx_destruct]
+ -[MAAutoAssetMigrationInfo assetSpecifier]
+ -[MAAutoAssetMigrationInfo assetType]
+ -[MAAutoAssetMigrationInfo assetVersion]
+ -[MAAutoAssetMigrationInfo description]
+ -[MAAutoAssetMigrationInfo encodeWithCoder:]
+ -[MAAutoAssetMigrationInfo hash]
+ -[MAAutoAssetMigrationInfo initWithCoder:]
+ -[MAAutoAssetMigrationInfo isEqual:]
+ -[MAAutoAssetMigrationInfo migrationError]
+ -[MAAutoAssetMigrationInfo migrationSucceeded]
+ -[MAAutoAssetMigrationInfo setAssetSpecifier:]
+ -[MAAutoAssetMigrationInfo setAssetType:]
+ -[MAAutoAssetMigrationInfo setAssetVersion:]
+ -[MAAutoAssetMigrationInfo setMigrationError:]
+ -[MAAutoAssetMigrationInfo setMigrationSucceeded:]
+ -[MAAutoAssetMigrationResults .cxx_destruct]
+ -[MAAutoAssetMigrationResults addFailedMigratedInfo:]
+ -[MAAutoAssetMigrationResults addFailedMigratedInfoForDescriptor:withError:]
+ -[MAAutoAssetMigrationResults addSetupError:]
+ -[MAAutoAssetMigrationResults addSuccessfullyMigratedInfo:]
+ -[MAAutoAssetMigrationResults addSuccessfullyMigratedInfoForDescriptor:]
+ -[MAAutoAssetMigrationResults description]
+ -[MAAutoAssetMigrationResults encodeWithCoder:]
+ -[MAAutoAssetMigrationResults failedMigratedAssetInfo]
+ -[MAAutoAssetMigrationResults hash]
+ -[MAAutoAssetMigrationResults infoFromDescriptor:]
+ -[MAAutoAssetMigrationResults infoFromDescriptor:withError:]
+ -[MAAutoAssetMigrationResults initWithCoder:]
+ -[MAAutoAssetMigrationResults init]
+ -[MAAutoAssetMigrationResults isEqual:]
+ -[MAAutoAssetMigrationResults setFailedMigrated:]
+ -[MAAutoAssetMigrationResults setSuccessfullyMigrated:]
+ -[MAAutoAssetMigrationResults setupErrors]
+ -[MAAutoAssetMigrationResults successfullyMigratedAssetInfo]
+ GCC_except_table264
+ OBJC_IVAR_$_MAAutoAssetMigrationInfo._assetSpecifier
+ OBJC_IVAR_$_MAAutoAssetMigrationInfo._assetType
+ OBJC_IVAR_$_MAAutoAssetMigrationInfo._assetVersion
+ OBJC_IVAR_$_MAAutoAssetMigrationInfo._migrationError
+ OBJC_IVAR_$_MAAutoAssetMigrationInfo._migrationSucceeded
+ OBJC_IVAR_$_MAAutoAssetMigrationResults._failedMigratedAssetInfo
+ OBJC_IVAR_$_MAAutoAssetMigrationResults._setupErrors
+ OBJC_IVAR_$_MAAutoAssetMigrationResults._successfullyMigratedAssetInfo
+ _OBJC_CLASS_$_MAAutoAssetMigrationInfo
+ _OBJC_CLASS_$_MAAutoAssetMigrationResults
+ _OBJC_METACLASS_$_MAAutoAssetMigrationInfo
+ _OBJC_METACLASS_$_MAAutoAssetMigrationResults
+ __OBJC_$_CLASS_METHODS_MAAutoAssetMigrationInfo
+ __OBJC_$_CLASS_METHODS_MAAutoAssetMigrationResults
+ __OBJC_$_CLASS_PROP_LIST_MAAutoAssetMigrationInfo
+ __OBJC_$_CLASS_PROP_LIST_MAAutoAssetMigrationResults
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetMigrationInfo
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetMigrationResults
+ __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetMigrationInfo
+ __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetMigrationResults
+ __OBJC_$_PROP_LIST_MAAutoAssetMigrationInfo
+ __OBJC_$_PROP_LIST_MAAutoAssetMigrationResults
+ __OBJC_CLASS_PROTOCOLS_$_MAAutoAssetMigrationInfo
+ __OBJC_CLASS_PROTOCOLS_$_MAAutoAssetMigrationResults
+ __OBJC_CLASS_RO_$_MAAutoAssetMigrationInfo
+ __OBJC_CLASS_RO_$_MAAutoAssetMigrationResults
+ __OBJC_METACLASS_RO_$_MAAutoAssetMigrationInfo
+ __OBJC_METACLASS_RO_$_MAAutoAssetMigrationResults
+ ___52+[MAAutoAssetSet preinstalledAssetMigrationResults:]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e42_v24?0"SUCoreConnectMessage"8"NSError"16l
+ _kMobileAssetPreferencesInternalVariantAsSeed
+ _objc_msgSend$addFailedMigratedInfo:
+ _objc_msgSend$addSuccessfullyMigratedInfo:
+ _objc_msgSend$arrayIsEqual:to:
+ _objc_msgSend$errorIsEqual:to:
+ _objc_msgSend$failedMigratedAssetInfo
+ _objc_msgSend$infoFromDescriptor:
+ _objc_msgSend$infoFromDescriptor:withError:
+ _objc_msgSend$migrationError
+ _objc_msgSend$migrationSucceeded
+ _objc_msgSend$setAssetSpecifier:
+ _objc_msgSend$setAssetType:
+ _objc_msgSend$setMigrationError:
+ _objc_msgSend$setMigrationSucceeded:
+ _objc_msgSend$setupErrors
+ _objc_msgSend$successfullyMigratedAssetInfo
CStrings:
+ "AssetMigrationInfo: { Type: %@ | Specifier: %@ | Version: %@ | MigrationSucceeded: %@ |  MigrationError: %@}\n"
+ "InternalVariantAsSeed"
+ "MA-AUTO-SET(REPLY):MIGRATION_RESULTS"
+ "MA-AUTO-SET:MIGRATION_RESULTS"
+ "MA-auto-set{_failedOperation:_failedOperation:preinstalledAssetMigrationResults} | failure reported by server | %{public}@"
+ "MA-auto-set{_failedOperation:_failedOperation:preinstalledAssetMigrationResults} | no response message from server | %{public}@"
+ "MA-auto-set{_failedOperation:preinstalledAssetMigrationResults} | unable to create shared SUCoreConnectClient for the client process"
+ "MA-auto-set{_successOperation:preinstalledAssetMigrationResults} | SUCCESS"
+ "MA-auto-set{preinstalledAssetMigrationResults} connection client initialized for server connection"
+ "PreinstalledMigrationCookieNotFound"
+ "PreinstalledMigrationCookieParseFailed"
+ "PreinstalledMigrationCreateResultsFailed"
+ "PreinstalledMigrationDecryptAssetFailed"
+ "PreinstalledMigrationFailedCreateDesc"
+ "PreinstalledMigrationInvalidPlist"
+ "PreinstalledMigrationMalformedDir"
+ "PreinstalledMigrationMoveFailed"
+ "PreinstalledMigrationNoAssetsForType"
+ "PreinstalledMigrationNonAutoAsset"
+ "PreinstalledMigrationPersistResultsFailed"
+ "PreinstalledMigrationRepoReadError"
+ "PreinstalledMigrationResultsNotFound"
+ "PreinstalledMigrationSetClassFailed"
+ "TIMEOUT-30"
+ "[MigrationResults>>>\nSuccessully migrated assets:\n%@\nFailed migrated assets:\n%@\nSetupError:\n%@\n<<<]"
+ "failedInfo"
+ "migrationError"
+ "migrationResults"
+ "migrationSuccess"
+ "preinstalledAssetMigrationResults"
+ "setupErrors"
+ "successInfo"
```
