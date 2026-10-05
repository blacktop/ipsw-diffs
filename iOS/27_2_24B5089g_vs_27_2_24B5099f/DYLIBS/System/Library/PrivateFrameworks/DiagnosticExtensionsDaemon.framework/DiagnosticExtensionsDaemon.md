## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-224.0.0.0.0
-  __TEXT.__text: 0x739a0
-  __TEXT.__objc_methlist: 0x7054
+225.0.0.0.0
+  __TEXT.__text: 0x73a08
+  __TEXT.__objc_methlist: 0x7044
   __TEXT.__const: 0x362
-  __TEXT.__cstring: 0x56f0
+  __TEXT.__cstring: 0x56e0
   __TEXT.__gcc_except_tab: 0x1ac0
-  __TEXT.__oslogstring: 0x9908
+  __TEXT.__oslogstring: 0x98c8
   __TEXT.__ustring: 0xc
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x48

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2188
-  __DATA_CONST.__objc_classlist: 0x278
+  __DATA_CONST.__const: 0x2198
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bc8
+  __DATA_CONST.__objc_selrefs: 0x3bc0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__got: 0x6e8
-  __AUTH_CONST.__const: 0xc20
-  __AUTH_CONST.__cfstring: 0x5040
-  __AUTH_CONST.__objc_const: 0x13b30
+  __DATA_CONST.__got: 0x6d8
+  __AUTH_CONST.__const: 0xc40
+  __AUTH_CONST.__cfstring: 0x5020
+  __AUTH_CONST.__objc_const: 0x13ad0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x6a0
   __AUTH.__objc_data: 0x90
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x5f4
+  __DATA.__objc_ivar: 0x5f8
   __DATA.__data: 0xad0
-  __DATA_DIRTY.__objc_data: 0x18e0
+  __DATA_DIRTY.__objc_data: 0x1890
   __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2932
-  Symbols:   4297
-  CStrings:  1791
+  Functions: 2934
+  Symbols:   4299
+  CStrings:  1787
 
Symbols:
+ +[DEDSeedingFinisher(SecurityResearchDevice) isERMCommPageCheckCompiledIn]
+ -[DEDConfiguration protectedDefaults]
+ -[DEDPersistence discardLegacyStoreKeys]
+ -[DEDPersistence protectedDefaults]
+ -[DEDPersistence setProtectedDefaults:]
+ GCC_except_table134
+ _DEDDeferredExtensionUserDefaultsKey
+ _DEDGroupContainerName
+ _OBJC_IVAR_$_DEDPersistence._protectedDefaults
+ __OBJC_$_CLASS_METHODS_DEDSeedingFinisher(SecurityResearchDevice)
+ ___37-[DEDConfiguration protectedDefaults]_block_invoke
+ ___73-[DEDSeedingFinisher(SecurityResearchDevice) isSecurityResearchDeviceERM]_block_invoke
+ _isSecurityResearchDeviceERM.ermEnabled
+ _isSecurityResearchDeviceERM.onceToken
+ _protectedDefaults.onceToken
+ _protectedDefaults.protectedDefaults
- +[DEDDirectoriesCleanup didRun]
- +[DEDDirectoriesCleanup isDryRun]
- +[DEDDirectoriesCleanup run]
- +[DEDDirectoriesCleanup shouldRun]
- -[DEDController upgradeToClassCDataProtectionIfNeeded]
- GCC_except_table138
- _NSURLFileProtectionCompleteUntilFirstUserAuthentication
- _OBJC_CLASS_$_DEDDirectoriesCleanup
- _OBJC_METACLASS_$_DEDDirectoriesCleanup
- __OBJC_$_CLASS_METHODS_DEDDirectoriesCleanup
- __OBJC_$_CLASS_METHODS_DEDSeedingFinisher
- __OBJC_CLASS_RO_$_DEDDirectoriesCleanup
- __OBJC_METACLASS_RO_$_DEDDirectoriesCleanup
- ___54-[DEDController upgradeToClassCDataProtectionIfNeeded]_block_invoke
CStrings:
+ "bugsession:"
+ "discarded [%lu] legacy keys"
+ "failed to archive bug session [%{public}@], not updating the store: [%{public}@]"
+ "group.com.apple.diagnosticextensionsd"
+ "no group container for [%{public}@]; protected defaults will not be protected"
+ "overrideDevice"
- "%@.c-data-class-upgrade"
- "DEDUpgradedToClassC"
- "Error setting file protection key: %@"
- "Upgrading: [%{public}@]"
- "directoriesCleanupDone"
- "directoriesCleanupDryRun"
- "failed to archive bug session with error: [%{public}@]"
- "upgradeToClassCDataProtectionIfNeeded already done"
- "upgradeToClassCDataProtectionIfNeeded end"
- "upgradeToClassCDataProtectionIfNeeded start"
```
