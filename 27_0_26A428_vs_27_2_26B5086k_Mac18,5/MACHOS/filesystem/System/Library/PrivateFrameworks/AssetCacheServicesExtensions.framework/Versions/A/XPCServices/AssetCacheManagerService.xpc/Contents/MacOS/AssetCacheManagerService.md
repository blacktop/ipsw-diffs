## AssetCacheManagerService

> `/System/Library/PrivateFrameworks/AssetCacheServicesExtensions.framework/Versions/A/XPCServices/AssetCacheManagerService.xpc/Contents/MacOS/AssetCacheManagerService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-157.0.0.0.0
-  __TEXT.__text: 0xb324
+157.40.2.0.0
+  __TEXT.__text: 0xc658
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x1580
-  __TEXT.__objc_methlist: 0x884
-  __TEXT.__const: 0x108
-  __TEXT.__objc_methname: 0x16c8
+  __TEXT.__objc_stubs: 0x1880
+  __TEXT.__objc_methlist: 0x904
+  __TEXT.__const: 0x130
+  __TEXT.__objc_methname: 0x19b6
   __TEXT.__objc_classname: 0xd4
-  __TEXT.__objc_methtype: 0x587
-  __TEXT.__cstring: 0x75f
-  __TEXT.__oslogstring: 0x799
-  __TEXT.__gcc_except_tab: 0x1e4
-  __TEXT.__unwind_info: 0x3b0
-  __DATA_CONST.__const: 0x6c0
-  __DATA_CONST.__cfstring: 0x920
+  __TEXT.__objc_methtype: 0x609
+  __TEXT.__cstring: 0x7e4
+  __TEXT.__oslogstring: 0x952
+  __TEXT.__gcc_except_tab: 0x1fc
+  __TEXT.__unwind_info: 0x408
+  __DATA_CONST.__const: 0x768
+  __DATA_CONST.__cfstring: 0xa00
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0x288
-  __DATA.__objc_const: 0x1098
-  __DATA.__objc_selrefs: 0x698
-  __DATA.__objc_ivar: 0x44
+  __DATA_CONST.__got: 0x298
+  __DATA.__objc_const: 0x10f0
+  __DATA.__objc_selrefs: 0x760
+  __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x240
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/AssetCacheServicesExtensions.framework/Versions/A/AssetCacheServicesExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 235
-  Symbols:   162
-  CStrings:  479
+  Functions: 261
+  Symbols:   164
+  CStrings:  528
 
Symbols:
+ _OBJC_CLASS_$_ACSDataPathValidator
+ _OBJC_CLASS_$_AssetCacheConfiguration
+ _getgrnam_r
+ _getpwnam_r
+ _kACSMSettingsDDMConfigKey
- _CFPreferencesAppValueIsForced
- _CFPreferencesCopyAppValue
- __kACSMManagedPreferencesDomain
CStrings:
+ "%@ %@ is not a permitted cache location"
+ "%@ %@ rejected: %@"
+ "%@ is not the path of a cache that can be absorbed: %@"
+ "%@ managed by your system administrator"
+ ", "
+ "/"
+ "/Library/Server/Caching/Data"
+ "/Volumes/*/%@"
+ "/tmp/%@"
+ "@\"AssetCacheConfiguration\""
+ "AbsorbCache"
+ "B40@0:8@16@24^@32"
+ "Cannot activate: %@ %@ rejected: %@"
+ "Cannot auto-activate the Content Cache: %@"
+ "Cannot auto-activate the Content Cache: data migration in progress"
+ "Refusing to absorb from %{public}@: %{public}@"
+ "Refusing to change managed setting(s) %{public}@"
+ "S"
+ "T@\"AssetCacheConfiguration\",&,V_configuration"
+ "Unable to forget the saved DDM configuration: %@"
+ "Unable to roll back the saved DDM configuration: %@"
+ "Unable to save the DDM configuration: %@"
+ "Vv36@0:8@\"NSString\"16B24@?<v@?B@\"NSError\">28"
+ "Vv36@0:8@16B24@?28"
+ "_absorbAllowedRoots"
+ "_applyManagementPolicyForKey:toSettings:"
+ "_applyManagementPolicyToSettings:"
+ "_assetcache user/group not found"
+ "_checkDelta:againstEffectiveSettings:error:"
+ "_configuration"
+ "_dataPathAllowedRoots"
+ "_isDDMActive"
+ "_policyFlagForKey:"
+ "_resetSettings:toDefaultForKey:"
+ "absorbCacheFrom:%{public}@ readOnly:%d for client pid %d"
+ "absorbCacheFrom:readOnly:forClientProcessIdentifier:withCallback:"
+ "absorbCacheFrom:readOnly:withCallback:"
+ "componentsJoinedByString:"
+ "configuration"
+ "ddmManagedKeys"
+ "defaultSettings"
+ "exportSettingsToLegacyLocationWithError:"
+ "isManagedKey:"
+ "managedByDDM"
+ "managedValueForKey:"
+ "readOnly"
+ "restrictedKeys"
+ "saveDDMConfiguration:error:"
+ "savedDDMConfiguration"
+ "secureCreateDirectoryAtPath:allowedRoots:owner:group:leafMode:parentMode:error:"
+ "setConfiguration:"
+ "setting managed by your system administrator"
+ "settings"
+ "sharedConfiguration"
+ "sortedArrayUsingSelector:"
+ "stringByAppendingString:"
+ "updateSettingsWithBlock:error:"
+ "v40@0:8@16B24i28@?32"
+ "validateAndResolvePath:allowedRoots:resolvedPath:error:"
- "%@ %@ does not end with /%@"
- "/Library/Application Support/Apple/AssetCache/Data"
- "/Library/Preferences/com.apple.AssetCache.plist"
- "ListenWithPeersAndParents"
- "Port"
- "_overrideSettings:withManagedValueForKey:"
- "_overrideWithManagedPrefSettings:"
- "dictionaryWithContentsOfFile:"
- "failed to update %@"
- "writeToFile:atomically:"
```
