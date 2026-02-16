## KeychainSyncAccountNotification

> `/System/Library/Accounts/Notification/KeychainSyncAccountNotification.bundle/KeychainSyncAccountNotification`

```diff

-61901.80.25.0.0
-  __TEXT.__text: 0x1114
-  __TEXT.__auth_stubs: 0x200
+61901.100.267.0.2
+  __TEXT.__text: 0x246c
+  __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_methlist: 0x18c
-  __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xb9
-  __TEXT.__oslogstring: 0x377
-  __TEXT.__unwind_info: 0x68
+  __TEXT.__const: 0xa0
+  __TEXT.__cstring: 0x259
+  __TEXT.__oslogstring: 0x642
+  __TEXT.__unwind_info: 0xe0
   __TEXT.__objc_classname: 0x46
-  __TEXT.__objc_methname: 0x47a
+  __TEXT.__objc_methname: 0x4b3
   __TEXT.__objc_methtype: 0x1f3
-  __TEXT.__objc_stubs: 0x340
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x80
+  __TEXT.__objc_stubs: 0x380
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a8
-  __AUTH_CONST.__auth_got: 0x108
+  __DATA_CONST.__objc_selrefs: 0x1b8
+  __AUTH_CONST.__auth_got: 0x138
+  __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x230
   __DATA.__data: 0xc0
+  __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12C78441-1027-3A70-8F05-29FA2A0EF6C4
-  Functions: 5
-  Symbols:   60
-  CStrings:  123
+  UUID: DC962078-FFC2-3D94-BA12-5B0D540203BE
+  Functions: 41
+  Symbols:   90
+  CStrings:  165
 
Symbols:
+ _OBJC_CLASS_$_OTOperationConfiguration
+ _SecDeleteInternalItemsOnSignOut
+ _SecIsInternalRelease
+ __NSConcreteGlobalBlock
+ __SecDebVerboseDatabaseLoggingClearOverride
+ __SecDebVerboseDatabaseLoggingIsEnabled
+ __SecDebVerboseDatabaseLoggingSetOverride
+ __SecDeleteInternalKeychainItemsOnSignoutClearOverride
+ __SecDeleteInternalKeychainItemsOnSignoutIsEnabled
+ __SecDeleteInternalKeychainItemsOnSignoutSetOverride
+ __SecInfoPlistConsistencyEnforcementIsEnabled
+ __SecProtectLoginKeychainWithDP
+ __SecSystemKeychainAlwaysClearOverride
+ __SecSystemKeychainAlwaysIsEnabled
+ __SecSystemKeychainAlwaysOverride
+ __SecTrustEarlyAnchorExpirationEnabled
+ __SecTrustQWACValidationEnabled
+ __SecTrustRemoveOldAppleAnchorSource
+ __SecTrustRemoveOldSystemAnchorSource
+ __SecTrustUseCRLite
+ __SecTrustUseCRLiteClearOverride
+ __SecTrustUseCRLiteEnforcement
+ __SecTrustUseCRLiteEnforcementClearOverride
+ __SecTrustUseCRLiteEnforcementSetOverride
+ __SecTrustUseCRLiteSetOverride
+ __SecTrustUsePolicyGraphVerifier
+ __os_feature_enabled_impl
+ _dispatch_once
+ _objc_alloc_init
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x22
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
CStrings:
+ "%s is %s (via feature flags)"
+ "CRLite usage overridden to %s"
+ "CRLite usage override removed"
+ "CRLiteEnforcement usage overridden to %s"
+ "CRLiteEnforcement usage override removed"
+ "Deleted items on sign out"
+ "Deleting Internal Keychain Items on Signout overridden to %s"
+ "Deleting Internal Keychain Items on Signout override removed"
+ "EarlyAnchorExpiration"
+ "EnableInfoPlistConsistencyEnforcement"
+ "Info.plist Consistency Enforcement is %s"
+ "ItemDelete"
+ "ItemDelete: Failed to delete items on sign out: %@"
+ "ProtectLoginKeychainWithDP"
+ "QWACValidation"
+ "RemoveOldAppleAnchorSource"
+ "RemoveOldSystemAnchorSource"
+ "SecDbVerboseDatabaseLogging"
+ "SecDeleteInternalKeychainItemsOnSignout"
+ "SecSystemKeychainAlwaysSupported"
+ "Security"
+ "System Keychain Always Supported overridden to %s"
+ "System Keychain Always Supported override removed"
+ "System Keychain Always Supported set via feature flag to %s"
+ "UseCRLite"
+ "UseCRLiteEnforcement"
+ "UsePolicyGraphVerifier"
+ "Verbose Databse Logging overridden to %s"
+ "Verbose Databse Logging override removed"
+ "codesign"
+ "device is still trusted, not deleting keychain items"
+ "disabled"
+ "dp_login"
+ "enabled"
+ "fetchCliqueStatus:configuration:reply:"
+ "ff is %s"
+ "keychain"
+ "personaIdentifier"
+ "trust"
+ "trustd"
+ "v24@?0q8@\"NSError\"16"
+ "v8@?0"

```
