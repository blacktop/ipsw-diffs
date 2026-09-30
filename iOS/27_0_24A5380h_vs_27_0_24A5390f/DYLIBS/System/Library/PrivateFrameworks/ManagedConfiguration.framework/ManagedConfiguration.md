## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-2483.0.1.0.0
-  __TEXT.__text: 0xf5c40
-  __TEXT.__objc_methlist: 0xb28c
-  __TEXT.__const: 0x14c4
-  __TEXT.__cstring: 0x1865d
-  __TEXT.__oslogstring: 0x925b
+2483.0.5.0.0
+  __TEXT.__text: 0xf61fc
+  __TEXT.__objc_methlist: 0xb2b4
+  __TEXT.__const: 0x152c
+  __TEXT.__cstring: 0x186d0
+  __TEXT.__oslogstring: 0x94c9
   __TEXT.__gcc_except_tab: 0x1020
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x3258
+  __TEXT.__unwind_info: 0x3250
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4e10
+  __DATA_CONST.__const: 0x4e18
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d90
+  __DATA_CONST.__objc_selrefs: 0x5db0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__got: 0xab0
   __AUTH_CONST.__const: 0x20b0
-  __AUTH_CONST.__cfstring: 0x19580
-  __AUTH_CONST.__objc_const: 0xd740
+  __AUTH_CONST.__cfstring: 0x19640
+  __AUTH_CONST.__objc_const: 0xd770
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0xbf8
   __AUTH.__objc_data: 0x23a0
-  __DATA.__objc_ivar: 0x990
-  __DATA.__data: 0xc78
+  __DATA.__objc_ivar: 0x994
+  __DATA.__data: 0xca0
   __DATA.__bss: 0xc59
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x280

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5790
-  Symbols:   11441
-  CStrings:  4597
+  Functions: 5797
+  Symbols:   11459
+  CStrings:  4611
 
Symbols:
+ -[MCPasscodeManager _simplePasscodeTypeDescription:]
+ -[MCPasscodeManager _unlockScreenTypeDescription:]
+ -[MCPasscodeManager currentUnlockScreenTypeWithOutSimpleType:]
+ -[MCPasscodeManager recoveryPasscodeUnlockScreenTypeWithOutSimpleType:]
+ -[MCPasscodeManager unlockScreenTypeForSharedDataVolume:withOutSimpleType:]
+ -[MCPasscodeManager unlockScreenTypeForUser:withOutSimpleType:]
+ -[MCPasscodeManager unlockScreenTypeWithPublicPasscodeDict:isRecovery:deviceHandle:outSimplePasscodeType:]
+ -[MCProfileConnection(Misc) isAutoCapitalizationAllowed]
+ -[MCSingleAppModeConfiguration allowAutoCapitalization]
+ -[MCSingleAppModeConfiguration setAllowAutoCapitalization:]
+ GCC_except_table290
+ _MCFeatureAutoCapitalizationAllowed
+ _MCFixPermissionOfManagedConfigurationFile
+ _MCFixPermissionOfManagedConfigurationFileFM
+ _MCFixPermissionsOfManagedConfigurationDirectoryAndContents
+ _MCFixPermissionsOfManagedConfigurationDirectoryAndContentsFM
+ _OBJC_IVAR_$_MCSingleAppModeConfiguration._allowAutoCapitalization
+ ___der_key_last_mesa_auth
+ ___der_key_last_mesa_unlock
+ ___der_key_last_passcode_auth
+ ___der_key_last_passcode_unlock
+ ___der_key_sks_heap_stats
+ _aks_get_convenience_bio_state
+ _aks_get_sks_heap_stats
+ _der_key_last_mesa_auth
+ _der_key_last_mesa_unlock
+ _der_key_last_passcode_auth
+ _der_key_last_passcode_unlock
+ _der_key_sks_heap_stats
+ _objc_msgSend$_simplePasscodeTypeDescription:
+ _objc_msgSend$_unlockScreenTypeDescription:
+ _objc_msgSend$allowAutoCapitalization
+ _objc_msgSend$currentUnlockScreenTypeWithOutSimpleType:
+ _objc_msgSend$recoveryPasscodeUnlockScreenTypeWithOutSimpleType:
+ _objc_msgSend$unlockScreenTypeForSharedDataVolume:withOutSimpleType:
+ _objc_msgSend$unlockScreenTypeForUser:withOutSimpleType:
+ _objc_msgSend$unlockScreenTypeWithPublicPasscodeDict:isRecovery:deviceHandle:outSimplePasscodeType:
- -[MCPasscodeManager currentUnlockSimplePasscodeType]
- -[MCPasscodeManager recoveryPasscodeUnlockSimplePasscodeType]
- -[MCPasscodeManager unlockScreenTypeWithPublicPasscodeDict:isRecovery:deviceHandle:]
- -[MCPasscodeManager unlockSimplePasscodeTypeForSharedDataVolume:]
- -[MCPasscodeManager unlockSimplePasscodeTypeForUser:]
- -[MCPasscodeManager unlockSimplePasscodeTypeWithPublicPasscodeDict:isRecovery:deviceHandle:]
- GCC_except_table289
- _MCFixPermissionOfSystemGroupContainerFile
- _MCFixPermissionOfSystemGroupContainerFileFM
- _MCFixPermissionsOfSystemGroupContainerDirectoryAndContents
- _MCFixPermissionsOfSystemGroupContainerDirectoryAndContentsFM
- _objc_msgSend$currentUnlockSimplePasscodeType
- _objc_msgSend$recoveryPasscodeUnlockSimplePasscodeType
- _objc_msgSend$unlockScreenTypeForSharedDataVolume:
- _objc_msgSend$unlockScreenTypeForUser:
- _objc_msgSend$unlockScreenTypeWithPublicPasscodeDict:isRecovery:deviceHandle:
- _objc_msgSend$unlockSimplePasscodeTypeForSharedDataVolume:
- _objc_msgSend$unlockSimplePasscodeTypeForUser:
- _objc_msgSend$unlockSimplePasscodeTypeWithPublicPasscodeDict:isRecovery:deviceHandle:
CStrings:
+ "Failed to decode System Metadata: %{public}@"
+ "Failed to decode User Metadata: %{public}@"
+ "Failed to load System Metadata: %{public}@"
+ "Invalide simple passcode type value %{public}d. Defaulting to %{public}@"
+ "Invalide unlock screen and simple type state. Defaulting to %{public}@ and %{public}@"
+ "Invalide unlock screen value %{public}d. Defaulting to %{public}@"
+ "Not Simple"
+ "Numeric Long"
+ "Retrieved unlock screen type %{public}@ and simple type %{public}@ for generation %{public}@. Public Dictionary Exists: %{public}@. Is Empty: %{public}@. Generation Exists: %{public}@. Is Recovery: %{public}@"
+ "Retrieving unlock screen type and simple type for generation %{public}@. Public Dictionary Exists: %{public}@. Is Empty: %{public}@. Generation Exists: %{public}@. Is Recovery: %{public}@"
+ "Simple"
+ "Simple 4 Digit"
+ "Simple 6 Digit"
+ "aks_get_convenience_bio_state"
+ "allowAutoCapitalization"
- "Unable to retrieve unlock simple type for generation %{public}@, but retrieved simple unlock screen. Defaulting to Simple 4 Digits"
```
