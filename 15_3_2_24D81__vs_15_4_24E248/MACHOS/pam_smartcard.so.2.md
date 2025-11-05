## pam_smartcard.so.2

> `/usr/lib/pam/pam_smartcard.so.2`

```diff

 213.0.0.0.0
-  __TEXT.__text: 0xae18
+  __TEXT.__text: 0xa914
   __TEXT.__auth_stubs: 0xc10
   __TEXT.__objc_stubs: 0x100
   __TEXT.__cstring: 0x119f

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpam.2.dylib
-  UUID: D545F840-1141-3472-86A9-3B6496533005
-  Functions: 197
-  Symbols:   529
+  UUID: 40015082-B9E2-39A6-AE94-D1D0B0E02430
+  Functions: 200
+  Symbols:   628
   CStrings:  365
 
Symbols:
+ TKAddSecureToken.cold.10
+ TKAddSecureToken.cold.11
+ TKAddSecureToken.cold.12
+ TKAddSecureToken.cold.13
+ TKAddSecureToken.cold.14
+ TKAddSecureToken.cold.15
+ TKAddSecureToken.cold.8
+ TKAddSecureToken.cold.9
+ TKBindUser.cold.2
+ TKBindUserAm.cold.2
+ TKCopyAvailableTokensInfo.cold.3
+ TKCopyAvailableTokensInfo.cold.4
+ TKCopyAvailableTokensInfo.cold.5
+ TKCopyAvailableTokensInfo.cold.6
+ TKCopyLegacyBindings.cold.10
+ TKCopyLegacyBindings.cold.11
+ TKCopyLegacyBindings.cold.12
+ TKCopyLegacyBindings.cold.7
+ TKCopyLegacyBindings.cold.8
+ TKCopyLegacyBindings.cold.9
+ TKCopySmartCardConfiguration.cold.6
+ TKCopySmartCardConfiguration.cold.7
+ TKCopySmartCardConfiguration.cold.8
+ TKCopySmartCardConfiguration.cold.9
+ TKGetSmartcardSetting.cold.1
+ TKGetSmartcardSetting.cold.2
+ TKGetSmartcardSettingForUser.cold.1
+ TKGetSmartcardSettingForUser.cold.2
+ TKGetSmartcardSettingForUser.cold.3
+ TKGetSmartcardSettingForUser.cold.4
+ TKGetSmartcardSettingForUser.cold.5
+ TKGetSmartcardSettingForUser.cold.6
+ TKGetSmartcardSettingForUser.cold.7
+ TKGetSmartcardSettingForUser.cold.8
+ TKGetSmartcardSettingForUser.cold.9
+ TKGetSmartcardSettingWorker.cold.1
+ TKGetSmartcardSettingWorker.cold.2
+ TKGetSmartcardSettingWorker.cold.3
+ TKGetSmartcardSettingWorker.cold.4
+ TKIsUserBound.cold.4
+ TKIsUserBound.cold.5
+ TKIsUserBound.cold.6
+ TKPerformLogin.cold.10
+ TKPerformLogin.cold.11
+ TKPerformLogin.cold.6
+ TKPerformLogin.cold.7
+ TKPerformLogin.cold.8
+ TKPerformLogin.cold.9
+ TKReadSecureTokenData.cold.10
+ TKReadSecureTokenData.cold.11
+ TKReadSecureTokenData.cold.6
+ TKReadSecureTokenData.cold.7
+ TKReadSecureTokenData.cold.8
+ TKReadSecureTokenData.cold.9
+ TKSmartCardSecureTokenRemove.cold.5
+ TKSmartCardSecureTokenRemove.cold.6
+ TKSmartCardSecureTokenRemove.cold.7
+ TKSmartCardSecureTokenRemove.cold.8
+ TKSmartCardSecureTokenRemove.cold.9
+ TKSmartCardSecureTokenStatus.cold.5
+ TKSmartCardSecureTokenStatus.cold.6
+ TKSmartCardSecureTokenStatus.cold.7
+ TKSmartCardSecureTokenStatus.cold.8
+ TKSmartCardSecureTokenStatus.cold.9
+ TKUnbindUser.cold.2
+ TKUnlockKeybag.cold.4
+ TKUnlockKeybag.cold.5
+ TKUnlockKeybag.cold.6
+ TKValidateAttributeMatchingConfig.cold.5
+ TKValidateAttributeMatchingConfig.cold.6
+ TKValidateAttributeMatchingConfig.cold.7
+ TKValidateAttributeMatchingConfig.cold.8
+ TKValidateAttributeMatchingConfig.cold.9
+ __MergedGlobals
+ __getSystemVolumeUuid_block_invoke.cold.5
+ __getSystemVolumeUuid_block_invoke.cold.6
+ __getSystemVolumeUuid_block_invoke.cold.7
+ __getSystemVolumeUuid_block_invoke.cold.8
+ __getUidForAgent_block_invoke.cold.4
+ __getUidForAgent_block_invoke.cold.5
+ binderWorker.cold.5
+ binderWorker.cold.6
+ binderWorker.cold.7
+ binderWorker.cold.8
+ fvunlockPrefs.cold.2
+ fvunlockPrefs.cold.3
+ getOdCustomEnforcementAttribute.cold.13
+ getOdCustomEnforcementAttribute.cold.14
+ getOdCustomEnforcementAttribute.cold.15
+ getOdCustomEnforcementAttribute.cold.16
+ getOdCustomEnforcementAttribute.cold.17
+ getOdCustomEnforcementAttribute.cold.18
+ getOdCustomEnforcementAttribute.cold.19
+ getOdCustomEnforcementAttribute.cold.20
+ getSystemVolumeUuid.cold.1
+ getUidForAgent.cold.1
+ isEnforcementOverriden.cold.1
+ isEnforcementOverriden.cold.2
+ isMemberOfGroup.cold.5
+ isMemberOfGroup.cold.6
+ isMemberOfGroup.cold.7
+ isMemberOfGroup.cold.8
+ setupConnection.cold.2
+ setupConnection.cold.3
- TKCopyTokenEndpoints.cold.1
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _tk_log.log
- _tk_log.onceToken

```
