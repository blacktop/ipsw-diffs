## profiled

> `/usr/libexec/profiled`

```diff

-2381.2.7.5.2
-  __TEXT.__text: 0x9da1c
-  __TEXT.__auth_stubs: 0x2130
-  __TEXT.__objc_stubs: 0xfaa0
-  __TEXT.__objc_methlist: 0x4ca4
-  __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0x194c
-  __TEXT.__oslogstring: 0xcba3
-  __TEXT.__cstring: 0x8b95
-  __TEXT.__objc_methname: 0x133fe
+2400.4.9.0.0
+  __TEXT.__text: 0x9f04c
+  __TEXT.__auth_stubs: 0x2230
+  __TEXT.__objc_stubs: 0xfbe0
+  __TEXT.__objc_methlist: 0x56e4
+  __TEXT.__const: 0x1fc
+  __TEXT.__gcc_except_tab: 0x1940
+  __TEXT.__oslogstring: 0xcd6a
+  __TEXT.__cstring: 0x8c48
+  __TEXT.__objc_methname: 0x13639
   __TEXT.__objc_classname: 0xb36
-  __TEXT.__objc_methtype: 0x203d
-  __TEXT.__unwind_info: 0x16a0
-  __DATA_CONST.__auth_got: 0x10a8
-  __DATA_CONST.__got: 0x1b98
-  __DATA_CONST.__const: 0x1b38
-  __DATA_CONST.__cfstring: 0x8360
+  __TEXT.__objc_methtype: 0x205a
+  __TEXT.__unwind_info: 0x1700
+  __DATA_CONST.__auth_got: 0x1128
+  __DATA_CONST.__got: 0x1ba0
+  __DATA_CONST.__const: 0x1b50
+  __DATA_CONST.__cfstring: 0x8480
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x7278
-  __DATA.__objc_selrefs: 0x4358
+  __DATA.__objc_const: 0x6088
+  __DATA.__objc_selrefs: 0x45d0
   __DATA.__objc_ivar: 0x1c0
   __DATA.__objc_data: 0x1bd0
-  __DATA.__data: 0x4ea
+  __DATA.__data: 0x540
   __DATA.__common: 0x20
   __DATA.__bss: 0x268
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1923
-  Symbols:   1460
-  CStrings:  4894
+  Functions: 2025
+  Symbols:   1477
+  CStrings:  4926
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _CFDataGetTypeID
+ _CFDictionaryGetValueIfPresent
+ _MCFeatureAllowedCameraRestrictionBundleIDs
+ _MDMCloudConfigurationPendingMigrationDetailsFilePath
+ _MDMSendPendingMigrationCloudConfigurationDetailsChangedNotification
+ _ccder_blob_decode_len
+ _ccder_blob_decode_sequence_tl
+ _ccder_blob_decode_tag
+ _ccder_blob_encode_body
+ _ccder_blob_encode_tl
+ _ccder_sizeof
+ _kMDMEnrollmentSSOAppStoreIDKey
+ _memcmp
+ _qsort
- _MCSettingsErrorDomain
CStrings:
+ "@\"NSArray\"24@0:8@\"NSArray\"16"
+ "Attempting to set kAKSConfigInactivityRebootEnabled config with value: %x\n..."
+ "BackOffDelay"
+ "BindKEKToKB"
+ "Could not mark pending cloud configuration to be excluded from backup."
+ "Could not store pending cloud configuration."
+ "Error calling aks_set_configuration with kAKSConfigInactivityRebootEnabled config! Error code: %x\n"
+ "EscrowPasscodePeriod"
+ "EscrowTokenPeriod"
+ "GracePeriod"
+ "InactivityRebootEnabled"
+ "MaxUnlockAttempts"
+ "OnenessAutomaticMode"
+ "Removing pending cloud configuration."
+ "Storing pending cloud configuration for migration"
+ "Successfully set kAKSConfigInactivityRebootEnabled config with value: %x\n"
+ "UserUUID"
+ "_saveCloudConfigDetails:outError:"
+ "_savePendingCloudConfigDetails:outError:"
+ "_saveSetAsideDetails:"
+ "_unpairFromDevicesIfNeededWithDetails:outError:"
+ "_updateCloudConfigDetails:"
+ "_validateCloudConfigDetails:outError:"
+ "_verifyActivationState:"
+ "_verifyCloudConfigSourceWithDetails:outError:"
+ "aks_set_configuration"
+ "cloudConfigurationStoreDetailsForPendingMigration:completion:"
+ "extensionIDsFromESSOProfileIdentifiers:"
+ "initiateDEPPushTokenSyncWithCompletionHandler:"
+ "profiled-CloudConfigStoreDetailsForMigration"
+ "saveCloudConfigurationDetailsForPendingMigration:outError:"
+ "setIdleRebootValue:"
+ "unassignFromDEPWithCompletionHandler:"
+ "updateCloudConfigurationWithRMAccountIdentifier:"
- "SETTINGS_DEVICE_IS_LOCKED_P_SETTING"
- "setRequiredAppIDForMDM:"

```
