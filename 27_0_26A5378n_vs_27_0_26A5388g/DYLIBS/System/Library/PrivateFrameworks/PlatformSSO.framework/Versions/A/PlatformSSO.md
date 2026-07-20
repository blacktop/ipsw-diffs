## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/Versions/A/PlatformSSO`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-643.0.21.0.0
-  __TEXT.__text: 0x10eb5c
-  __TEXT.__objc_methlist: 0x474c
-  __TEXT.__const: 0x1f10
-  __TEXT.__gcc_except_tab: 0x1f98
-  __TEXT.__cstring: 0xe46f
-  __TEXT.__oslogstring: 0x8ea8
-  __TEXT.__dlopen_cstrs: 0x3db
-  __TEXT.__swift5_typeref: 0x634
-  __TEXT.__swift5_fieldmd: 0x830
-  __TEXT.__constg_swiftt: 0xb10
-  __TEXT.__swift5_reflstr: 0x83a
-  __TEXT.__swift5_builtin: 0x28
+643.0.33.0.0
+  __TEXT.__text: 0x11570c
+  __TEXT.__objc_methlist: 0x47cc
+  __TEXT.__const: 0x2140
+  __TEXT.__gcc_except_tab: 0x1fe8
+  __TEXT.__cstring: 0xe59f
+  __TEXT.__oslogstring: 0x9878
+  __TEXT.__dlopen_cstrs: 0x42d
+  __TEXT.__swift5_typeref: 0x6bc
+  __TEXT.__swift5_fieldmd: 0x8bc
+  __TEXT.__constg_swiftt: 0xbc8
+  __TEXT.__swift5_reflstr: 0x8da
+  __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_proto: 0x7c
-  __TEXT.__swift5_types: 0x64
-  __TEXT.__swift_as_entry: 0x29c
-  __TEXT.__swift_as_ret: 0x290
-  __TEXT.__swift_as_cont: 0x28c
+  __TEXT.__swift5_types: 0x6c
+  __TEXT.__swift_as_entry: 0x2c0
+  __TEXT.__swift_as_ret: 0x2b8
+  __TEXT.__swift_as_cont: 0x2a0
+  __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x270
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x30a0
-  __TEXT.__eh_frame: 0x3df8
+  __TEXT.__unwind_info: 0x31a8
+  __TEXT.__eh_frame: 0x4088
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5a0
+  __DATA_CONST.__const: 0x5b8
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32f0
+  __DATA_CONST.__objc_selrefs: 0x3368
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0xa0
-  __DATA_CONST.__got: 0x980
-  __AUTH_CONST.__const: 0x2c20
-  __AUTH_CONST.__cfstring: 0x6240
-  __AUTH_CONST.__objc_const: 0xa930
+  __DATA_CONST.__got: 0x998
+  __AUTH_CONST.__const: 0x2d10
+  __AUTH_CONST.__cfstring: 0x62a0
+  __AUTH_CONST.__objc_const: 0xa9e8
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0xc88
+  __AUTH_CONST.__auth_got: 0xca0
   __AUTH.__objc_data: 0x960
-  __AUTH.__data: 0xe28
-  __DATA.__objc_ivar: 0x410
+  __AUTH.__data: 0xeb8
+  __DATA.__objc_ivar: 0x414
   __DATA.__data: 0x7b0
-  __DATA.__bss: 0xe98
+  __DATA.__bss: 0xea8
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x550
-  __DATA_DIRTY.__bss: 0x120
+  __DATA_DIRTY.__bss: 0x130
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4146
-  Symbols:   5566
-  CStrings:  2102
+  Functions: 4219
+  Symbols:   5601
+  CStrings:  2134
 
Symbols:
+ -[PODaemonProcess _backfillExtensionTeamIdentifierIfNeeded]
+ -[PODirectoryServices findPlatformSSOUserByRecordName:]
+ -[PODirectoryServices fullNameForUserName:]
+ -[POExtension _validateExtensionTeamIdentifier:]
+ -[POExtension initWithExtensionBundleIdentifier:teamIdentifier:delegate:]
+ -[POExtension initWithExtensionBundleIdentifier:teamIdentifier:extensionManager:delegate:]
+ -[POExtensionAgentProcess teamIdentifierForXPCConnection:]
+ -[POLoginProcess shouldDenyUnmappedPlatformSSONodeUser]
+ -[POProfile extensionTeamIdentifier]
+ -[PORegistrationManager loadSSOExtensionWithExtensionBundleIdentifier:teamIdentifier:]
+ -[POUnlockProcess shouldDenyUnmappedPlatformSSONodeUser]
+ GCC_except_table104
+ GCC_except_table113
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table143
+ GCC_except_table147
+ GCC_except_table151
+ GCC_except_table157
+ GCC_except_table161
+ GCC_except_table164
+ GCC_except_table171
+ GCC_except_table177
+ GCC_except_table183
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table197
+ GCC_except_table200
+ GCC_except_table208
+ GCC_except_table221
+ GCC_except_table231
+ GCC_except_table264
+ GCC_except_table273
+ GCC_except_table58
+ GCC_except_table70
+ GCC_except_table82
+ OBJC_IVAR_$_POProfile._extensionTeamIdentifier
+ _SecTaskCopyTeamIdentifier
+ __59-[PODaemonProcess _backfillExtensionTeamIdentifierIfNeeded]_block_invoke
+ ___59-[PODaemonProcess _backfillExtensionTeamIdentifierIfNeeded]_block_invoke
+ ___swift_memcpy25_8
+ _get_enum_tag_for_layout_string 11PlatformSSO21POOpenIDAuthenticatorC19PendingNotification33_A050C60567236DE6C462A1CA717C4A03LLO
+ _get_enum_tag_for_layout_string 11PlatformSSO23POPasswordAuthenticatorC19PendingNotification33_CA05275239268D3B9F3FFE68D341B68ALLO
+ _objc_msgSend$_backfillExtensionTeamIdentifierIfNeeded
+ _objc_msgSend$_extensionBundle
+ _objc_msgSend$_validateExtensionTeamIdentifier:
+ _objc_msgSend$bundleURL
+ _objc_msgSend$checkSignatureOfFile:teamIdentifier:trusted:signedBySet:certificates:error:
+ _objc_msgSend$extensionTeamIdentifier
+ _objc_msgSend$findPlatformSSOUserByRecordName:
+ _objc_msgSend$fullNameForUserName:
+ _objc_msgSend$hasAnyMDMProfileForExtension:teamIdentifier:
+ _objc_msgSend$initWithExtensionBundleIdentifier:teamIdentifier:extensionManager:delegate:
+ _objc_msgSend$isConfigurationActiveForExtensionIdentifier:teamIdentifier:runningAsAgent:completion:
+ _objc_msgSend$isExtensionSignatureValidated
+ _objc_msgSend$loadSSOExtensionWithExtensionBundleIdentifier:teamIdentifier:
+ _objc_msgSend$setExtensionTeamIdentifier:
+ _objc_msgSend$shouldDenyUnmappedPlatformSSONodeUser
+ _objc_msgSend$teamIdentifierForXPCConnection:
+ _swift_cvw_enumFn_getEnumTag
+ _symbolic SS8userName_t
+ _symbolic So9LAContextC17credentialContext_SS8userNamet
+ _symbolic So9LAContextCSg17credentialContext_SS8userNamet
+ _symbolic _____ 11PlatformSSO21POOpenIDAuthenticatorC19PendingNotification33_A050C60567236DE6C462A1CA717C4A03LLO
+ _symbolic _____ 11PlatformSSO23POPasswordAuthenticatorC19PendingNotification33_CA05275239268D3B9F3FFE68D341B68ALLO
+ _symbolic _____Sg 11PlatformSSO21POOpenIDAuthenticatorC19PendingNotification33_A050C60567236DE6C462A1CA717C4A03LLO
+ _symbolic _____Sg 11PlatformSSO23POPasswordAuthenticatorC19PendingNotification33_CA05275239268D3B9F3FFE68D341B68ALLO
+ _type_layout_string 11PlatformSSO21POOpenIDAuthenticatorC19PendingNotification33_A050C60567236DE6C462A1CA717C4A03LLO
+ _type_layout_string 11PlatformSSO23POPasswordAuthenticatorC19PendingNotification33_CA05275239268D3B9F3FFE68D341B68ALLO
- GCC_except_table107
- GCC_except_table134
- GCC_except_table138
- GCC_except_table140
- GCC_except_table141
- GCC_except_table146
- GCC_except_table150
- GCC_except_table154
- GCC_except_table155
- GCC_except_table159
- GCC_except_table163
- GCC_except_table169
- GCC_except_table175
- GCC_except_table182
- GCC_except_table189
- GCC_except_table195
- GCC_except_table199
- GCC_except_table205
- GCC_except_table220
- GCC_except_table230
- GCC_except_table263
- GCC_except_table271
- GCC_except_table38
- GCC_except_table66
- GCC_except_table80
- GCC_except_table88
- __54-[POExtensionAgentProcess isCallerCurrentSSOExtension]_block_invoke_2
- ___54-[POExtensionAgentProcess isCallerCurrentSSOExtension]_block_invoke_2
- ___block_descriptor_57_e8_32s40s48s_e20_v24?0Q8"NSError"16l
- _objc_msgSend$hasAnyMDMProfileForExtension:
- _objc_msgSend$initWithExtensionBundleIdentifier:extensionManager:delegate:
- _objc_msgSend$isConfigurationActiveForExtensionIdentifier:runningAsAgent:completion:
- isCallerCurrentSSOExtension.extensionIdentifier
- isCallerCurrentSSOExtension.onceToken
CStrings:
+ ")#Y"
+ "-[PODirectoryServices findPlatformSSOUserByRecordName:]"
+ "Apple"
+ "Authentication flow cancelled"
+ "Authentication flow: Queuing agent notification for password auth unlock"
+ "Authentication flow: Queuing agent notification for token auth unlock"
+ "Back-filling extension team identifier on device configuration"
+ "Caller team identifier is not current extension"
+ "Failed to save device configuration when back-filling team identifier."
+ "Generic identity provider name shown when no account display name is configured"
+ "No team identifier in profile to back-fill device configuration"
+ "PlatformSSO extension bundle identifier mismatch: requested=%{public}@, loaded=%{public}@"
+ "PlatformSSO extension has no bundle path; cannot validate team identifier %{public}@"
+ "PlatformSSO extension signature check failed for %{public}@: %{public}@"
+ "PlatformSSO extension team identifier mismatch: requested=%{public}@, signed=%{public}@"
+ "Profile extension team is different than registered extension team"
+ "Refusing auth for Platform SSO node user %{public}@ with no local account mapping (create-users and AGM disabled)"
+ "Refusing auth for Platform SSO node user %{public}@ with no local account mapping (create-users and AGM disabled). (rdar://177602229)"
+ "Skipping local account password sync; AllowWebLoginPasswordSync is disabled for web login"
+ "The user is not a platform SSO user, skipping notification."
+ "User state is needs registration, key is invalid, or new user pending registration"
+ "configureAuthenticators(%{public}s, hasUsername=%{bool,public}d): primary=%{public}s, secondary=%{public}s, fallback=%{public}s"
+ "handleSuccessfulResponse: Queuing agent notification for token auth unlock"
+ "handleUserSEPKeyUserAuthentication: Queuing agent notification for unlock"
+ "ignoring PlatformSSO extension team identifier mismatch because extension signature validation is disabled"
+ "invalid team identifier of the extension, teamIdentifier=%{public}@, requiredTeamIdentifier=%{public}@"
+ "migrated stashed login state for temporary session account, no user configuration to update"
+ "migrating stashed AGM login state for temporary session account %{public}@"
+ "policyForSessionType(%{public}s): nil - hasDeviceConfig=%{bool,public}d, registrationCompleted=%{bool,public}d, hasLoginConfig=%{bool,public}d"
+ "policyForSessionType(%{public}s): nil - policy has no biometric requirement: %{public}s"
+ "policyForSessionType(%{public}s): nil - session type does not support required touchID"
+ "policyForSessionType(%{public}s): nil - unknown session type"
+ "preserving stashed decryption context for temporary session account %{public}@"
+ "resolveResult(%{public}s): no secondary auth method - returning primary result"
+ "resolveResult(%{public}s): primary succeeded, requiring secondary %{public}s"
+ "shouldRun(%{public}s, %{public}s): false"
+ "shouldRun(%{public}s, %{public}s): false - OpenID not configured"
+ "shouldRun(%{public}s, %{public}s): false - no biometric policy"
+ "shouldRun(%{public}s, %{public}s): false - registration not completed"
+ "shouldRun(%{public}s, %{public}s): true"
+ "shouldRun(%{public}s, %{public}s): true - biometric 2FA fallback"
+ "shouldRun(%{public}s, %{public}s): true - device loginType"
+ "shouldRun(%{public}s, %{public}s): true - openID fallback"
+ "shouldRun(%{public}s, %{public}s): true - supportsCreateNewUsers"
+ "shouldRun(%{public}s, %{public}s): true - user loginType"
+ "teamIdentifier: CPCopyBundleIdentifierAndTeamFromAuditToken(): %{public}@"
+ "teamIdentifier: SecTaskCopyTeamIdentifier() failed %{public}@"
+ "teamIdentifier: SecTaskCreateWithAuditToken() failed"
+ "teamIdentifier: The entitlements are not validated."
- "(#Y"
- "Authentication flow: Notifying agent for password auth unlock"
- "Authentication flow: Notifying agent for token auth unlock"
- "Authentication flow:Notifying agent for password auth unlock"
- "User state is needs registration or key is invalid"
- "configureAuthenticators(%s): primary=%s, secondary=%s, fallback=%s"
- "handleSuccessfulResponse: Notifying agent for token auth unlock"
- "handleSuccessfulResponse: Notifying agent for unlock"
- "shouldRun(%s, %s): false"
- "shouldRun(%s, %s): false - OpenID not configured"
- "shouldRun(%s, %s): false - no biometric policy"
- "shouldRun(%s, %s): false - registration not completed"
- "shouldRun(%s, %s): true"
- "shouldRun(%s, %s): true - device loginType"
- "shouldRun(%s, %s): true - openID fallback"
- "shouldRun(%s, %s): true - supportsCreateNewUsers"
- "shouldRun(%s, %s): true - user loginType"
```
