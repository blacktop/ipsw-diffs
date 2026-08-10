## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2483.0.5.0.0
-  __TEXT.__text: 0xf61fc
-  __TEXT.__objc_methlist: 0xb2b4
+2483.2.6.0.0
+  __TEXT.__text: 0xf7134
+  __TEXT.__objc_methlist: 0xb33c
   __TEXT.__const: 0x152c
-  __TEXT.__cstring: 0x186d0
-  __TEXT.__oslogstring: 0x94c9
-  __TEXT.__gcc_except_tab: 0x1020
+  __TEXT.__cstring: 0x186ab
+  __TEXT.__oslogstring: 0x9798
+  __TEXT.__gcc_except_tab: 0x1040
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x3250
+  __TEXT.__unwind_info: 0x3288
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4e18
-  __DATA_CONST.__objc_classlist: 0x3d0
+  __DATA_CONST.__const: 0x4e40
+  __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5db0
+  __DATA_CONST.__objc_selrefs: 0x5e18
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0xe8
-  __DATA_CONST.__got: 0xab0
-  __AUTH_CONST.__const: 0x20b0
+  __DATA_CONST.__got: 0xac0
+  __AUTH_CONST.__const: 0x2130
   __AUTH_CONST.__cfstring: 0x19640
-  __AUTH_CONST.__objc_const: 0xd770
+  __AUTH_CONST.__objc_const: 0xd808
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0xbf8
-  __AUTH.__objc_data: 0x23a0
+  __AUTH.__objc_data: 0x23f0
   __DATA.__objc_ivar: 0x994
   __DATA.__data: 0xca0
-  __DATA.__bss: 0xc59
+  __DATA.__bss: 0xc89
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x228

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5797
-  Symbols:   11459
-  CStrings:  4611
+  Functions: 5817
+  Symbols:   11499
+  CStrings:  4621
 
Symbols:
+ +[MCAppManagedFeaturesBackupExclusions appIDsAtPath:]
+ +[MCAppManagedFeaturesBackupExclusions appIDs]
+ +[MCAppManagedFeaturesBackupExclusions removeAtPath:error:]
+ +[MCAppManagedFeaturesBackupExclusions removeWithError:]
+ +[MCAppManagedFeaturesBackupExclusions setAppIDs:atPath:error:]
+ +[MCAppManagedFeaturesBackupExclusions setAppIDs:error:]
+ +[MCRestrictionUtilities boolFeatureForPayloadRestrictionKey:]
+ +[MCRestrictionUtilities boolFeaturesWithPayloadRestictionKeyAlias]
+ +[MCRestrictionUtilities boolPayloadRestrictionKeysForFeature:]
+ -[MCProfileConnection(Misc) areAppRatingExceptionsAllowedForScreenTime]
+ GCC_except_table373
+ _MCAppManagedFeaturesDoNotBackupAppIDsFilePath
+ _MCAppManagedFeaturesDoNotBackupAppIDsFilePath.once
+ _MCAppManagedFeaturesDoNotBackupAppIDsFilePath.str
+ _MCFeatureSpringBoardShouldConsiderAppAllowlistAsTransient
+ _OBJC_CLASS_$_MCAppManagedFeaturesBackupExclusions
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_METACLASS_$_MCAppManagedFeaturesBackupExclusions
+ __OBJC_$_CLASS_METHODS_MCAppManagedFeaturesBackupExclusions
+ __OBJC_CLASS_RO_$_MCAppManagedFeaturesBackupExclusions
+ __OBJC_METACLASS_RO_$_MCAppManagedFeaturesBackupExclusions
+ ___71-[MCProfileConnection(Misc) areAppRatingExceptionsAllowedForScreenTime]_block_invoke
+ ___MCAppManagedFeaturesDoNotBackupAppIDsFilePath_block_invoke
+ ____boolAliasToFeatures_block_invoke
+ ____boolFeaturesToAlias_block_invoke
+ ___block_descriptor_40_e8_32r_e30_v24?0"NSNumber"8"NSError"16lr32l8
+ __boolAliasToFeatures.dict
+ __boolAliasToFeatures.onceToken
+ __boolFeaturesToAlias
+ __boolFeaturesToAlias.dict
+ __boolFeaturesToAlias.onceToken
+ _kMCAllowSiriAIKey
+ _objc_msgSend$appIDs
+ _objc_msgSend$appIDsAtPath:
+ _objc_msgSend$areAppRatingsLockedDownOnlyByScreenTimeWithCompletion:
+ _objc_msgSend$boolFeatureForPayloadRestrictionKey:
+ _objc_msgSend$boolFeaturesWithPayloadRestictionKeyAlias
+ _objc_msgSend$boolPayloadRestrictionKeysForFeature:
+ _objc_msgSend$orderedSetWithArray:
+ _objc_msgSend$removeAtPath:error:
+ _objc_msgSend$setAppIDs:atPath:error:
+ _objc_msgSend$stringByDeletingLastPathComponent
- _kSoftwareUpdatePath
- _kSoftwareUpdatePathKey
CStrings:
+ "AppManagedFeatures backup-exclusions file has a non-string entry, ignoring file"
+ "AppManagedFeatures backup-exclusions file has unexpected %{public}@ type: %{public}@"
+ "AppManagedFeatures/DoNotBackupAppIDs.plist"
+ "Cannot read AppManagedFeatures backup-exclusions: no file path"
+ "Cannot remove AppManagedFeatures backup-exclusions: no file path"
+ "Cannot write AppManagedFeatures backup-exclusions: no file path"
+ "FEATURE_SIRI_AI"
+ "Failed to check if apps rating are locked down only by Screen Time. Error: %{public}@"
+ "Failed to create AppManagedFeatures backup-exclusions directory: %{public}@"
+ "Failed to remove AppManagedFeatures backup-exclusions: %{public}@"
+ "Failed to serialize AppManagedFeatures backup-exclusions: %{public}@"
+ "Failed to write AppManagedFeatures backup-exclusions: %{public}@"
+ "PreventBackupAppIDs"
+ "SpringBoardShouldConsiderAppAllowlistAsTransient"
+ "allowSiriAI"
+ "com.apple.NanoRemote"
+ "com.apple.Remote"
- "FEATURE_DELAYED_SOFTWARE_UPDATES"
- "FEATURE_RAPID_SECURITY_RESPONSE_INSTALLATION"
- "FEATURE_RAPID_SECURITY_RESPONSE_REMOVAL"
- "FEATURE_SOFTWARE_UPDATE_DELAY"
- "RecommendationCadence"
- "SoftwareUpdateSettings"
- "com.apple.TVRemoteApp"
```
