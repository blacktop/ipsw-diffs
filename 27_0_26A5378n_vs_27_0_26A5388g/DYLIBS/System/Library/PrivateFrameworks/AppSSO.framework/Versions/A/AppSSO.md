## AppSSO

> `/System/Library/PrivateFrameworks/AppSSO.framework/Versions/A/AppSSO`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-643.0.21.0.0
-  __TEXT.__text: 0x32958
-  __TEXT.__objc_methlist: 0x1cd4
+643.0.33.0.0
+  __TEXT.__text: 0x32bf8
+  __TEXT.__objc_methlist: 0x1cfc
   __TEXT.__const: 0x160
   __TEXT.__gcc_except_tab: 0x1bac
-  __TEXT.__oslogstring: 0x552f
-  __TEXT.__cstring: 0x3a68
+  __TEXT.__oslogstring: 0x560c
+  __TEXT.__cstring: 0x3a95
   __TEXT.__dlopen_cstrs: 0x7b6
-  __TEXT.__unwind_info: 0xf60
+  __TEXT.__unwind_info: 0xf78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13e0
+  __DATA_CONST.__objc_selrefs: 0x1400
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__got: 0x228
-  __AUTH_CONST.__const: 0x1100
+  __AUTH_CONST.__const: 0x10d0
   __AUTH_CONST.__cfstring: 0x1460
   __AUTH_CONST.__objc_const: 0x49b8
   __AUTH_CONST.__objc_intobj: 0x78

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1192
-  Symbols:   2199
-  CStrings:  789
+  Functions: 1190
+  Symbols:   2205
+  CStrings:  791
 
Symbols:
+ -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:]
+ -[SOConfigurationHost _profileMatchesTeamIdentifier:requiredTeamIdentifier:]
+ -[SOConfigurationHost hasAnyMDMProfileForExtension:teamIdentifier:]
+ -[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:]
+ GCC_except_table41
+ GCC_except_table46
+ GCC_except_table57
+ ___108-[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:]_block_invoke
+ ___109-[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:]_block_invoke
+ _objc_msgSend$_isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:
+ _objc_msgSend$_profileMatchesTeamIdentifier:requiredTeamIdentifier:
+ _objc_msgSend$extensionTeamIdentifier
+ _objc_msgSend$hasAnyMDMProfileForExtension:teamIdentifier:
+ _objc_msgSend$isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:
- -[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]
- GCC_except_table48
- GCC_except_table60
- ___93-[SOConfigurationHost isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]_block_invoke
- ___94-[SOConfigurationHost _isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:]_block_invoke
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0l
- _objc_msgSend$_isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:
- _objc_msgSend$hasAnyMDMProfileForExtension:
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
