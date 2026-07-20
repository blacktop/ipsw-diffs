## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
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
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-643.0.21.0.0
-  __TEXT.__text: 0x5adf0
-  __TEXT.__objc_methlist: 0x3534
+643.0.33.0.0
+  __TEXT.__text: 0x5be94
+  __TEXT.__objc_methlist: 0x358c
   __TEXT.__const: 0x322
-  __TEXT.__cstring: 0x8256
-  __TEXT.__oslogstring: 0x2531
-  __TEXT.__gcc_except_tab: 0x13a8
-  __TEXT.__dlopen_cstrs: 0x110
+  __TEXT.__cstring: 0x8296
+  __TEXT.__oslogstring: 0x28f1
+  __TEXT.__gcc_except_tab: 0x13f8
+  __TEXT.__dlopen_cstrs: 0x162
   __TEXT.__swift5_typeref: 0xd9
   __TEXT.__swift5_capture: 0x14c
   __TEXT.__constg_swiftt: 0x4c

   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift_as_cont: 0x58
-  __TEXT.__unwind_info: 0x1578
+  __TEXT.__unwind_info: 0x15a8
   __TEXT.__eh_frame: 0x628
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf60
+  __DATA_CONST.__const: 0xf50
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2398
+  __DATA_CONST.__objc_selrefs: 0x2400
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x438
   __AUTH_CONST.__const: 0xc80
-  __AUTH_CONST.__cfstring: 0x3a00
-  __AUTH_CONST.__objc_const: 0x8608
+  __AUTH_CONST.__cfstring: 0x3a40
+  __AUTH_CONST.__objc_const: 0x8640
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x740
+  __AUTH_CONST.__auth_got: 0x750
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x38c
+  __DATA.__objc_ivar: 0x390
   __DATA.__data: 0x600
   __DATA.__bss: 0x340
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2126
-  Symbols:   3601
-  CStrings:  1034
+  Functions: 2144
+  Symbols:   3618
+  CStrings:  1050
 
Symbols:
+ -[PODirectoryServices fullNameForUserName:]
+ -[POExtension _validateExtensionTeamIdentifier:]
+ -[POExtension initWithExtensionBundleIdentifier:teamIdentifier:delegate:]
+ -[POExtension initWithExtensionBundleIdentifier:teamIdentifier:extensionManager:delegate:]
+ -[POExtensionAgentProcess teamIdentifierForXPCConnection:]
+ -[POProfile extensionTeamIdentifier]
+ -[PORegistrationManager loadSSOExtensionWithExtensionBundleIdentifier:teamIdentifier:]
+ GCC_except_table100
+ GCC_except_table108
+ GCC_except_table114
+ GCC_except_table122
+ GCC_except_table129
+ GCC_except_table177
+ GCC_except_table30
+ GCC_except_table45
+ GCC_except_table5
+ GCC_except_table73
+ _AppSSOCoreLibraryCore.frameworkLibrary
+ _OBJC_IVAR_$_POProfile._extensionTeamIdentifier
+ _OUTLINED_FUNCTION_12
+ _SecTaskCopyTeamIdentifier
+ ___AppSSOCoreLibraryCore_block_invoke
+ ___getSOUtilsClass_block_invoke
+ _audit_stringAppSSOCore
+ _getSOUtilsClass.softClass
+ _objc_msgSend$_extensionBundle
+ _objc_msgSend$_validateExtensionTeamIdentifier:
+ _objc_msgSend$bundleURL
+ _objc_msgSend$checkSignatureOfFile:teamIdentifier:trusted:signedBySet:certificates:error:
+ _objc_msgSend$extension
+ _objc_msgSend$extensionTeamIdentifier
+ _objc_msgSend$hasAnyMDMProfileForExtension:teamIdentifier:
+ _objc_msgSend$initWithExtensionBundleIdentifier:teamIdentifier:extensionManager:delegate:
+ _objc_msgSend$isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:
+ _objc_msgSend$isExtensionSignatureValidated
+ _objc_msgSend$loadSSOExtensionWithExtensionBundleIdentifier:teamIdentifier:
+ _objc_msgSend$setExtensionTeamIdentifier:
+ _objc_msgSend$teamIdentifierForXPCConnection:
+ _objc_retainBlock
- GCC_except_table107
- GCC_except_table113
- GCC_except_table116
- GCC_except_table120
- GCC_except_table127
- GCC_except_table176
- GCC_except_table29
- GCC_except_table32
- GCC_except_table37
- GCC_except_table38
- GCC_except_table51
- GCC_except_table72
- GCC_except_table87
- GCC_except_table99
- ___54-[POExtensionAgentProcess isCallerCurrentSSOExtension]_block_invoke_2
- ___block_descriptor_57_e8_32s40s48s_e20_v24?0Q8"NSError"16ls32l8s40l8s48l8
- _isCallerCurrentSSOExtension.extensionIdentifier
- _isCallerCurrentSSOExtension.onceToken
- _objc_msgSend$hasAnyMDMProfileForExtension:
- _objc_msgSend$initWithExtensionBundleIdentifier:extensionManager:delegate:
- _objc_msgSend$isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:
- _objc_msgSend$loadSSOExtensionWithExtensionBundleIdentifier:
CStrings:
+ ")#Y"
+ "Apple"
+ "Caller team identifier is not current extension"
+ "PlatformSSO extension bundle identifier mismatch: requested=%{public}@, loaded=%{public}@"
+ "PlatformSSO extension has no bundle path; cannot validate team identifier %{public}@"
+ "PlatformSSO extension signature check failed for %{public}@: %{public}@"
+ "PlatformSSO extension team identifier mismatch: requested=%{public}@, signed=%{public}@"
+ "SOUtils"
+ "Skipping local account password sync; AllowWebLoginPasswordSync is disabled for web login"
+ "The user is not a platform SSO user, skipping notification."
+ "User state is needs registration, key is invalid, or new user pending registration"
+ "ignoring PlatformSSO extension team identifier mismatch because extension signature validation is disabled"
+ "invalid team identifier of the extension, teamIdentifier=%{public}@, requiredTeamIdentifier=%{public}@"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore"
+ "teamIdentifier: CPCopyBundleIdentifierAndTeamFromAuditToken(): %{public}@"
+ "teamIdentifier: SecTaskCopyTeamIdentifier() failed %{public}@"
+ "teamIdentifier: SecTaskCreateWithAuditToken() failed"
+ "teamIdentifier: The entitlements are not validated."
- "(#Y"
- "User state is needs registration or key is invalid"
```
