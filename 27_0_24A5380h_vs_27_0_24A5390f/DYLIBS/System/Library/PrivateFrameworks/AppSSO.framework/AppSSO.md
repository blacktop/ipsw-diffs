## AppSSO

> `/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-643.0.21.0.0
-  __TEXT.__text: 0x2baac
-  __TEXT.__objc_methlist: 0x1c2c
+643.0.33.0.0
+  __TEXT.__text: 0x2bca8
+  __TEXT.__objc_methlist: 0x1c54
   __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x1958
-  __TEXT.__oslogstring: 0x4bb8
-  __TEXT.__cstring: 0x37d9
+  __TEXT.__gcc_except_tab: 0x195c
+  __TEXT.__oslogstring: 0x4c95
+  __TEXT.__cstring: 0x3806
   __TEXT.__dlopen_cstrs: 0x6dc
-  __TEXT.__unwind_info: 0xe28
+  __TEXT.__unwind_info: 0xe40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12f8
+  __DATA_CONST.__objc_selrefs: 0x1318
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x28

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1067
-  Symbols:   1982
-  CStrings:  731
+  Functions: 1065
+  Symbols:   1988
+  CStrings:  733
 
Symbols:
+ -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:]
+ -[SOConfigurationHost _profileMatchesTeamIdentifier:requiredTeamIdentifier:]
+ -[SOConfigurationHost hasAnyMDMProfileForExtension:teamIdentifier:]
+ -[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:]
+ GCC_except_table25
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table43
+ GCC_except_table51
+ GCC_except_table56
+ ___108-[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:]_block_invoke
+ ___109-[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:]_block_invoke
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ _objc_msgSend$_isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:
+ _objc_msgSend$_profileMatchesTeamIdentifier:requiredTeamIdentifier:
+ _objc_msgSend$extensionTeamIdentifier
+ _objc_msgSend$hasAnyMDMProfileForExtension:teamIdentifier:
+ _objc_msgSend$isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:
- -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]
- GCC_except_table23
- GCC_except_table24
- GCC_except_table33
- GCC_except_table34
- GCC_except_table46
- _OUTLINED_FUNCTION_13
- ___93-[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]_block_invoke
- ___94-[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]_block_invoke
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- _objc_msgSend$_isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:
- _objc_msgSend$hasAnyMDMProfileForExtension:
- _objc_retain_x25
CStrings:
+ "%s extensionIdentifier: %{public}@, teamIdentifier: %{public}@ on %@"
+ "-[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:]"
+ "-[SOConfigurationHost hasAnyMDMProfileForExtension:teamIdentifier:]"
+ "-[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:]"
+ "ignoring profile team identifier mismatch because extension signature validation is disabled"
+ "profile team identifier mismatch for extension: %{public}@, profile=%{public}@, required=%{public}@"
- "%s extensionIdentifier: %{public}@ on %@"
- "-[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]"
- "-[SOConfigurationHost hasAnyMDMProfileForExtension:]"
- "-[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]"
```
