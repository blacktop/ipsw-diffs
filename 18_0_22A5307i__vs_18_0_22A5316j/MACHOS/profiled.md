## profiled

> `/usr/libexec/profiled`

```diff

-2337.0.0.0.0
-  __TEXT.__text: 0x9d6ac
+2343.0.0.0.0
+  __TEXT.__text: 0x9d380
   __TEXT.__auth_stubs: 0x20e0
-  __TEXT.__objc_stubs: 0xfa40
-  __TEXT.__objc_methlist: 0x4cc4
+  __TEXT.__objc_stubs: 0xfa20
+  __TEXT.__objc_methlist: 0x4c94
   __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0x1a80
-  __TEXT.__oslogstring: 0xcbc2
-  __TEXT.__cstring: 0x8a69
-  __TEXT.__objc_methname: 0x133c9
+  __TEXT.__gcc_except_tab: 0x19a0
+  __TEXT.__oslogstring: 0xcac0
+  __TEXT.__cstring: 0x8ad7
+  __TEXT.__objc_methname: 0x13398
   __TEXT.__objc_classname: 0xb36
-  __TEXT.__objc_methtype: 0x1feb
+  __TEXT.__objc_methtype: 0x1ff1
   __TEXT.__info_plist: 0x61b
-  __TEXT.__unwind_info: 0x16a8
+  __TEXT.__unwind_info: 0x1698
   __DATA_CONST.__auth_got: 0x1080
   __DATA_CONST.__got: 0x1b70
-  __DATA_CONST.__const: 0x1af8
-  __DATA_CONST.__cfstring: 0x8280
+  __DATA_CONST.__const: 0x1b28
+  __DATA_CONST.__cfstring: 0x82c0
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x7248
-  __DATA.__objc_selrefs: 0x4350
+  __DATA.__objc_selrefs: 0x4348
   __DATA.__objc_ivar: 0x1c4
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0x4ea

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1925
+  Functions: 1921
   Symbols:   1450
-  CStrings:  4883
+  CStrings:  4881
 
Symbols:
+ _OBJC_CLASS_$_MDMProvisioningProfileTrust
+ _OBJC_CLASS_$_MOEffectiveSettingsStore
- _OBJC_CLASS_$_DMCProvisioningProfileTrust
- _OBJC_CLASS_$_LSApplicationRecord
CStrings:
+ "%!@(MISSING) is attempting to clear the passcode"
+ "-[MCProfileServiceServer clearPasscodeWithEscrowKeybagData:secret:senderBundleID:completion:]_block_invoke"
+ "@\"MDMProvisioningProfileTrust\""
+ "B52@0:8@16@24B32@36^@44"
+ "ScreenTime"
+ "T@\"MDMProvisioningProfileTrust\",&,N,V_profileTrust"
+ "_allowsPasswordPoliciesFromProfile:outError:"
+ "anyUPPExistsForManagedAppSigners"
+ "blockedByFilter"
+ "changePasscodeFrom:to:skipRecovery:senderBundleID:outError:"
+ "changePasscodeWithRecoveryPasscode:to:skipRecovery:senderBundleID:outError:"
+ "clearPasscodeWithEscrowKeybagData:secret:senderBundleID:completion:"
+ "clearPasscodeWithEscrowKeybagData:secret:senderBundleID:outError:"
+ "com.apple.managedconfiguration.profiled.MCInstaller"
+ "didEnrollInMDMWithPasscode:duringMigration:"
+ "mayChangePasscode"
+ "policy"
+ "restrictionsAlreadyInstalledFromPayload:"
+ "sendPasscodeChangedEventWithChangeType:oldPasscodeExists:isClearingPasscode:newPasscodeUnlockScreenType:newPasscodeSimpleType:passcodeRecoverySupported:passcodeRecoveryRestricted:recoverySkipped:senderBundleID:"
+ "senderBundleID"
+ "simplified_agent"
+ "updateTrustedCodeSigningIdentities:validateBundleIDs:validateManagedApps:"
+ "v60@0:8q16B24B28i32i36B40B44B48@52"
+ "webContent"
- "-[MCProfileServiceServer clearPasscodeWithEscrowKeybagData:secret:completion:]_block_invoke"
- "@\"DMCProvisioningProfileTrust\""
- "App signer identities to validate: %!{(MISSING)public}@"
- "B44@0:8@16@24B32^@36"
- "Could not find record of managed app %!{(MISSING)public}@, %!{(MISSING)public}@"
- "Could not find signer identity of managed app %!{(MISSING)public}@"
- "Getting signer identity of app %!{(MISSING)public}@"
- "Getting signer identity of managed app %!{(MISSING)public}@"
- "Managed app signer identities: %!{(MISSING)public}@"
- "T@\"DMCProvisioningProfileTrust\",&,N,V_profileTrust"
- "_appSignersToValidateForBundleIDs:"
- "_appSigningIdentityForBundleIdentifier:"
- "_managedAppSigners"
- "_workQueueUpdateMISUPPTrustWithTrustCodeSigningIdentities:validateApps:validateManagedApps:"
- "anyUPPExistsForManagedAppSigners:"
- "changePasscodeFrom:to:outError:"
- "changePasscodeFrom:to:skipRecovery:outError:"
- "changePasscodeWithRecoveryPasscode:to:skipRecovery:outError:"
- "clearPasscodeWithEscrowKeybagData:secret:outError:"
- "didEnrollInMDMWithPasscode:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "managedAppIDs"
- "sendPasscodeChangedEventWithChangeType:oldPasscodeExists:isClearingPasscode:newPasscodeUnlockScreenType:newPasscodeSimpleType:passcodeRecoverySupported:passcodeRecoveryRestricted:recoverySkipped:"
- "signerIdentity"
- "updateMISUPPTrustWithTrustCodeSigningIdentities:managedAppSigners:appSignersToValidate:validateManagedApps:"
- "v52@0:8q16B24B28i32i36B40B44B48"

```
