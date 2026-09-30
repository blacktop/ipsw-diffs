## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-4.34.0.0.0
-  __TEXT.__text: 0x2c51c
+4.40.0.0.0
+  __TEXT.__text: 0x2cc90
   __TEXT.__auth_stubs: 0xe80
-  __TEXT.__objc_methlist: 0x2360
+  __TEXT.__objc_methlist: 0x23e8
   __TEXT.__const: 0x150
   __TEXT.__gcc_except_tab: 0x6ec
-  __TEXT.__cstring: 0x3072
-  __TEXT.__oslogstring: 0x437c
+  __TEXT.__cstring: 0x3116
+  __TEXT.__oslogstring: 0x4445
   __TEXT.__dlopen_cstrs: 0x165
-  __TEXT.__unwind_info: 0xb68
+  __TEXT.__unwind_info: 0xb80
   __TEXT.__objc_classname: 0x401
-  __TEXT.__objc_methname: 0x8191
-  __TEXT.__objc_methtype: 0x1192
-  __TEXT.__objc_stubs: 0x51c0
+  __TEXT.__objc_methname: 0x8318
+  __TEXT.__objc_methtype: 0x11a5
+  __TEXT.__objc_stubs: 0x5300
   __DATA_CONST.__got: 0x618
   __DATA_CONST.__const: 0xe78
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e70
+  __DATA_CONST.__objc_selrefs: 0x1ed0
   __DATA_CONST.__objc_superrefs: 0x90
   __AUTH_CONST.__auth_got: 0x750
-  __AUTH_CONST.__const: 0xc80
-  __AUTH_CONST.__cfstring: 0x3820
+  __AUTH_CONST.__const: 0xc40
+  __AUTH_CONST.__cfstring: 0x38a0
   __AUTH_CONST.__objc_const: 0x3cc8
-  __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__objc_intobj: 0x168
   __AUTH.__objc_data: 0xc30
   __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x2b1
-  __DATA.__bss: 0x930
+  __DATA.__bss: 0x910
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0xa8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1095
-  Symbols:   1735
-  CStrings:  2331
+  Functions: 1107
+  Symbols:   1747
+  CStrings:  2351
 
Symbols:
+ _DMCConfigurationProfilesSystemGroupContainerMetadataFilePath
+ _DMCSendUPPVerificationOfflineNotification
+ _DMCUPPVerificationOfflineNotification
+ _MDMSystemReturnToServiceStorageDirectory
+ _MDMUserReturnToServiceStorageDirectory
- _DMCSendUPPValidationOfflineNotification
- _DMCUPPValidationOfflineNotification
- _MDMStashFileDirectory
- _MDMStashedCloudConfigProfilePath
- _MDMStashedConfigurationDictionaryPath
- _MDMStashedMDMProfilePath
- _MDMStashedWiFiProfilePath
CStrings:
+ ".com.apple.mobile_container_manager.metadata.plist"
+ "@40@0:8@16^@24@?32"
+ "Conflicting account with altDSID (%!{(MISSING)public}@) exists. Identifier: %!@(MISSING), type: %!{(MISSING)public}@"
+ "DMCObliterationShelter: Failed to migrate stashed directory. Error: %!{(MISSING)public}@"
+ "DMCObliterationShelter: Migrating sheltered files."
+ "DMCObliterationShelter: Nothing to migrate."
+ "DMC_SDP_RATCHET_STRICT_TEXT_INSTALL_PROFILE"
+ "DMC_SDP_RATCHET_STRICT_TEXT_MDM_ENROLL"
+ "Library/MDM_ReturnToService"
+ "Sending UPP verification offline notification."
+ "_allPathsToClear"
+ "_cloudConfigProfilePath_retrieve"
+ "_cloudConfigProfilePath_stash"
+ "_configurationDictionaryPath_retrieve"
+ "_configurationDictionaryPath_stash"
+ "_containerMetadataPlistPath_stash"
+ "_createDirectoryAtPathIfNeeded:error:"
+ "_dmc_accountWithType:error:criteria:"
+ "_mdmProfilePath_retrieve"
+ "_mdmProfilePath_stash"
+ "_ratchetStrictTextForOperation:"
+ "_retrievalDirectoryPath"
+ "_stashDirectoryPath"
+ "_wifiProfilePath_retrieve"
+ "_wifiProfilePath_stash"
+ "com.apple.devicemanagementclient.uppVerificationOffline"
+ "dmc_conflictingAccountsExistWithAltDSID:error:"
+ "migrateAllFiles"
+ "moveItemAtPath:toPath:error:"
- "Ignoring inactive iTunes Account (%!{(MISSING)public}@). Identifier: %!@(MISSING)"
- "Sending UPP validation offline notification."
- "_allPossiblePaths"
- "_cloudConfigProfilePath"
- "_configurationDictionaryPath"
- "_dmc_accountWithType:criteria:"
- "_mdmProfilePath"
- "_wifiProfilePath"
- "com.apple.devicemanagementclient.uppValidationOffline"

```
