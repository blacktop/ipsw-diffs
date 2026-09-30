## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-  __TEXT.__text: 0x1016bc
+  __TEXT.__text: 0x101844
   __TEXT.__auth_stubs: 0x1700
   __TEXT.__objc_methlist: 0xb24c
   __TEXT.__const: 0x14ac
   __TEXT.__cstring: 0x18416
-  __TEXT.__oslogstring: 0x9137
+  __TEXT.__oslogstring: 0x91ba
   __TEXT.__gcc_except_tab: 0xfb4
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x50

   - /usr/lib/libobjc.A.dylib
   Functions: 5755
   Symbols:   11366
-  CStrings:  8940
+  CStrings:  8943
 
Symbols:
+ _MCFixPermissionOfManagedConfigurationFile
+ _MCFixPermissionOfManagedConfigurationFileFM
+ _MCFixPermissionsOfManagedConfigurationDirectoryAndContents
+ _MCFixPermissionsOfManagedConfigurationDirectoryAndContentsFM
- _MCFixPermissionOfSystemGroupContainerFile
- _MCFixPermissionOfSystemGroupContainerFileFM
- _MCFixPermissionsOfSystemGroupContainerDirectoryAndContents
- _MCFixPermissionsOfSystemGroupContainerDirectoryAndContentsFM
Functions:
~ ___MCHasMigrated_block_invoke : 576 -> 836
~ ___MCHasMDMMigrated_block_invoke : 380 -> 512
CStrings:
+ "Failed to decode System Metadata: %{public}@"
+ "Failed to decode User Metadata: %{public}@"
+ "Failed to load System Metadata: %{public}@"
```
