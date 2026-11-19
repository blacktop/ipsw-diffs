## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/Versions/A/DiagnosticExtensionsDaemon`

```diff

-222.0.0.0.0
-  __TEXT.__text: 0x7df1c
-  __TEXT.__objc_methlist: 0x6fbc
-  __TEXT.__const: 0x372
-  __TEXT.__cstring: 0x5540
+225.0.0.0.0
+  __TEXT.__text: 0x7dbf8
+  __TEXT.__objc_methlist: 0x6ff4
+  __TEXT.__const: 0x392
+  __TEXT.__cstring: 0x54d0
   __TEXT.__gcc_except_tab: 0x1ad0
-  __TEXT.__oslogstring: 0x9658
+  __TEXT.__oslogstring: 0x95f8
   __TEXT.__ustring: 0xc
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x48

   __TEXT.__swift5_reflstr: 0x80
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1da8
+  __TEXT.__unwind_info: 0x1d98
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xad0
-  __DATA_CONST.__objc_classlist: 0x278
+  __DATA_CONST.__const: 0xb00
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b80
+  __DATA_CONST.__objc_selrefs: 0x3ba0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__got: 0x6c8
-  __AUTH_CONST.__const: 0x2270
-  __AUTH_CONST.__cfstring: 0x4e00
-  __AUTH_CONST.__objc_const: 0x13a38
+  __DATA_CONST.__got: 0x6b8
+  __AUTH_CONST.__const: 0x2220
+  __AUTH_CONST.__cfstring: 0x4dc0
+  __AUTH_CONST.__objc_const: 0x13a68
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x50

   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x90
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x5e0
+  __DATA.__objc_ivar: 0x5f0
   __DATA.__data: 0xad0
-  __DATA.__bss: 0x1c0
-  __DATA_DIRTY.__objc_data: 0x18e0
+  __DATA.__bss: 0x1d0
+  __DATA_DIRTY.__objc_data: 0x1890
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x2b8
+  __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 2976
-  Symbols:   5939
-  CStrings:  1762
+  Symbols:   5944
+  CStrings:  1752
 
Symbols:
+ +[DEDSeedingFinisher(SecurityResearchDevice) isERMCommPageCheckCompiledIn]
+ -[DEDBugSessionConfiguration seedingCookieName]
+ -[DEDBugSessionConfiguration seedingFilerURL]
+ -[DEDBugSessionConfiguration seedingUsesPinning]
+ -[DEDBugSessionConfiguration setSeedingCookieName:]
+ -[DEDBugSessionConfiguration setSeedingFilerURL:]
+ -[DEDBugSessionConfiguration setSeedingUsesPinning:]
+ -[DEDConfiguration protectedDefaults]
+ -[DEDPersistence discardLegacyStoreKeys]
+ -[DEDPersistence protectedDefaults]
+ -[DEDPersistence setProtectedDefaults:]
+ GCC_except_table158
+ OBJC_IVAR_$_DEDBugSessionConfiguration._seedingCookieName
+ OBJC_IVAR_$_DEDBugSessionConfiguration._seedingFilerURL
+ OBJC_IVAR_$_DEDBugSessionConfiguration._seedingUsesPinning
+ OBJC_IVAR_$_DEDPersistence._protectedDefaults
+ _DEDDeferredExtensionUserDefaultsKey
+ _DEDDevicePlatformHomeAccessory
+ _DEDGroupContainerName
+ _DEDKeySeedingCookieName
+ _DEDKeySeedingFilerURL
+ _DEDKeySeedingUsesPinning
+ __37-[DEDConfiguration protectedDefaults]_block_invoke
+ __OBJC_$_CLASS_METHODS_DEDSeedingFinisher(SecurityResearchDevice)
+ ___37-[DEDConfiguration protectedDefaults]_block_invoke
+ _objc_msgSend$discardLegacyStoreKeys
+ _objc_msgSend$persistentDomainForName:
+ _objc_msgSend$protectedDefaults
+ _objc_msgSend$seedingCookieName
+ _objc_msgSend$seedingFilerURL
+ _objc_msgSend$seedingUsesPinning
+ protectedDefaults.onceToken
+ protectedDefaults.protectedDefaults
- +[DEDDirectoriesCleanup didRun]
- +[DEDDirectoriesCleanup isDryRun]
- +[DEDDirectoriesCleanup run]
- +[DEDDirectoriesCleanup shouldRun]
- -[DEDController upgradeToClassCDataProtectionIfNeeded]
- GCC_except_table162
- _DEDKeySeedingEnvironment
- _DEDSeedingClientFilerURL
- _NSURLFileProtectionCompleteUntilFirstUserAuthentication
- _OBJC_CLASS_$_DEDDirectoriesCleanup
- _OBJC_METACLASS_$_DEDDirectoriesCleanup
- __28+[DEDDirectoriesCleanup run]_block_invoke
- __54-[DEDController upgradeToClassCDataProtectionIfNeeded]_block_invoke
- __OBJC_$_CLASS_METHODS_DEDDirectoriesCleanup
- __OBJC_$_CLASS_METHODS_DEDSeedingFinisher
- __OBJC_CLASS_RO_$_DEDDirectoriesCleanup
- __OBJC_METACLASS_RO_$_DEDDirectoriesCleanup
- ___28+[DEDDirectoriesCleanup run]_block_invoke
- ___54-[DEDController upgradeToClassCDataProtectionIfNeeded]_block_invoke
- ___block_descriptor_48_e8_32s_e5_v8?0l
- _objc_msgSend$didRun
- _objc_msgSend$findAllItems:includeDirs:
- _objc_msgSend$isDryRun
- _objc_msgSend$lsDir:sorted:
- _objc_msgSend$seedingEnvironment
- _objc_msgSend$setBool:forKey:
- _objc_msgSend$shouldRun
- _objc_msgSend$upgradeToClassCDataProtectionIfNeeded
CStrings:
+ "Discovery returned [%lu] extensions"
+ "HomeAccessory"
+ "No cached extensions; re-running discovery"
+ "Pinning disabled by config; skipping pinning check."
+ "bugsession:"
+ "could not match de directory [%{public}@] to known extensions. This is only an issue if file was triggered by DE flow."
+ "could not match de directory url [%{public}@] to known extensions. This is only an issue if file was triggered by DE flow"
+ "discarded [%lu] legacy keys"
+ "failed to archive bug session [%{public}@], not updating the store: [%{public}@]"
+ "group.com.apple.diagnosticextensionsd"
+ "homeaccessory"
+ "no group container for [%{public}@]; protected defaults will not be protected"
+ "overrideDevice"
+ "seedingCookieName"
+ "seedingFilerURL"
+ "seedingUsesPinning"
- "%@.c-data-class-upgrade"
- "Cleaning up group containers"
- "Could not find feedback group container."
- "DEDUpgradedToClassC"
- "Error setting file protection key: %@"
- "FBAFilerURL"
- "Failed to cleanup directory with error [%{public}@]"
- "Finished: Cleaning up group containers"
- "Group directories cleanup is already done."
- "Removed [%{public}@]"
- "Removing [%{public}@]"
- "Running in development mode; skipping pinning check."
- "Upgrading: [%{public}@]"
- "Using user default value for filer URL"
- "_seedportal_session_uat"
- "com.apple.diagnosticextensions"
- "com.apple.diagnosticextensionsd-group-containers-cleanup"
- "could not match de directory [%{public}@] to known extensions"
- "dir-cleanup"
- "directoriesCleanupDone"
- "directoriesCleanupDryRun"
- "failed to archive bug session with error: [%{public}@]"
- "seedingEnvironment"
- "upgradeToClassCDataProtectionIfNeeded already done"
- "upgradeToClassCDataProtectionIfNeeded end"
- "upgradeToClassCDataProtectionIfNeeded start"
```
