## mbuseragent

> `/System/Library/CoreServices/Setup Assistant.app/Contents/Resources/mbuseragent`

```diff

-7217.1.0.0.0
-  __TEXT.__text: 0x45018
+7407.4.12.204.0
+  __TEXT.__text: 0x46ed0
   __TEXT.__auth_stubs: 0x1050
-  __TEXT.__objc_stubs: 0x8a60
-  __TEXT.__objc_methlist: 0x33c0
+  __TEXT.__objc_stubs: 0x8ec0
+  __TEXT.__objc_methlist: 0x4c60
   __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x64c
-  __TEXT.__cstring: 0xb5e4
-  __TEXT.__objc_methname: 0xc7f9
-  __TEXT.__objc_classname: 0x3d4
-  __TEXT.__objc_methtype: 0x1c1e
+  __TEXT.__gcc_except_tab: 0x67c
+  __TEXT.__cstring: 0xbd2e
+  __TEXT.__objc_methname: 0xd121
+  __TEXT.__objc_classname: 0x3f7
+  __TEXT.__objc_methtype: 0x1cda
   __TEXT.__dlopen_cstrs: 0x138
   __TEXT.__oslogstring: 0xc60
-  __TEXT.__unwind_info: 0xe18
+  __TEXT.__unwind_info: 0xf10
   __DATA_CONST.__auth_got: 0x838
   __DATA_CONST.__got: 0x688
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1b80
-  __DATA_CONST.__cfstring: 0x7ca0
+  __DATA_CONST.__const: 0x1c30
+  __DATA_CONST.__cfstring: 0x8080
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_nlclslist: 0x8
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x90

   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x1e0
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0xbc78
-  __DATA.__objc_selrefs: 0x2cd0
-  __DATA.__objc_ivar: 0x3d4
+  __DATA.__objc_const: 0x9940
+  __DATA.__objc_selrefs: 0x2fa0
+  __DATA.__objc_ivar: 0x3f4
   __DATA.__objc_data: 0x960
-  __DATA.__data: 0x7c8
+  __DATA.__data: 0x828
   __DATA.__bss: 0x358
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 026E16DE-4675-3FD9-82AF-0850B9E947D0
-  Functions: 1658
+  UUID: 78E7032E-E834-31FF-BC3C-445E9EBEA188
+  Functions: 1755
   Symbols:   484
-  CStrings:  4654
+  CStrings:  4810
 
Symbols:
+ _OBJC_CLASS_$_SUPreferenceManager
+ _PCSIdentitySetCreate
+ _kPCSServiceFDE
- _OBJC_CLASS_$_CSFFeatureManager
- _PCSIdentitySetup
- _kPCSSetupPassword
CStrings:
+ "\""
+ "-[MBAnalyticsManager applyAnalyticsDataFromArray:]"
+ "-[MBSAConnection activateProximityServerWithCompletion:]_block_invoke"
+ "-[MBSAConnection connectionWithErrorHandler:]_block_invoke"
+ "-[MBSAConnection invalidateProximitySessionWithCompletion:]_block_invoke"
+ "-[MBSAConnection overrideSASInformation:]"
+ "-[MBSAConnection prepareForAppleAccountSignInWithCompletion:]_block_invoke"
+ "-[MBSAConnection proximityDisplayCode:]"
+ "-[MBSAConnection proximityPINCodeTypeChanged:]"
+ "-[MBSAConnection proximitySessionLost]"
+ "-[MBSAConnection proximitySessionReady:]"
+ "-[MBSAConnection retrieveMessageSessionWithCompletion:]_block_invoke"
+ "-[MBSAConnection setTestingModeEnablement:]_block_invoke"
+ "-[MBUserConfigurator fetchIntelligenceEnablementStatusWithCompletionBlock:]_block_invoke"
+ "."
+ "/var/db/.AppleSetupTermsOfService"
+ "@\"<ProximitySetupConnectionHandler>\""
+ "@\"CWInterface\""
+ "AK bag check completed, intelligence allowed."
+ "Attempting to apply invalid analytics data, bailing!"
+ "Attempting to generate PCS Identity without iCloud username"
+ "AutoUpdate"
+ "AutoUpdateIsSupervised"
+ "B32@0:8@\"NSArray\"16@\"NSArray\"24"
+ "BOOL MBTOSRequiredCookieExists()"
+ "Checking AK configuration bag for offer intelligence upsell"
+ "Checking intelligence availability status..."
+ "Current intelligence opt in state: %lu"
+ "Current intelligence opt in state: %lu allows showing intelligence upsell"
+ "Debug value for key %@ is %@"
+ "Error activating proximity: %@"
+ "Error fetching proximity session: %@"
+ "Error invalidating proximity: %@"
+ "Error launching mbsystemadmininstration: %@"
+ "Error setting testing mode: %@"
+ "Finished call to PCS setup with appleID=%@, id=%@ (err=%@)"
+ "From iOS"
+ "LicenseFallback"
+ "No message dict pointer, not attempting to show error"
+ "None (originally from Mac)"
+ "None (originally from Windows)"
+ "Not eligible for intelligence upsell as user has already opted out"
+ "Removed TOS required cookie with success: %i, error: %@"
+ "ResumePostUserSessionChange"
+ "SASoftwareUpdateManagerProtocol"
+ "Setting TOS cookie"
+ "Somehow attempting to call %s without a proximity manager"
+ "SpoofedCurrentProductMarketingVersion"
+ "SpoofedPreviousProductMarketingVersion"
+ "System requires license: %i"
+ "T@\"<ProximitySetupConnectionHandler>\",W,V_proximityHandler"
+ "T@\"CWInterface\",&,V_overrideDefaultInterface"
+ "T@\"NSMutableDictionary\",&,V_initialSetupAnalytics"
+ "T@\"NSMutableDictionary\",&,V_proximitySetupAnalytics"
+ "TB,V_automaticallyInstallMacOSUpdatesLockedInValue"
+ "TB,V_didJoinNetworkUsingProximityData"
+ "TB,V_downloadUpdatesInBackgroundLockedInValue"
+ "TB,V_recordProximityAnalytics"
+ "_automaticallyInstallMacOSUpdatesLockedInValue"
+ "_didJoinNetworkUsingProximityData"
+ "_downloadUpdatesInBackgroundLockedInValue"
+ "_initialSetupAnalytics"
+ "_overrideDefaultInterface"
+ "_proximityHandler"
+ "_proximitySetupAnalytics"
+ "_recordProximityAnalytics"
+ "activateProximityServerWithCompletion:"
+ "analyticsData"
+ "applyAnalyticsDataFromArray:"
+ "automaticallyInstallMacOSUpdates"
+ "automaticallyInstallMacOSUpdatesLockedInValue"
+ "com.apple.setupassistant.macos.initialsetup"
+ "com.apple.setupassistant.macos.proximitysetup"
+ "configureAutoUpdateValues"
+ "createTeslaUsersWithInfo:prepareFirstAdminForResume:completionBlock:"
+ "defaultInterface"
+ "didJoinNetworkUsingProximityData"
+ "downloadUpdatesInBackground"
+ "downloadUpdatesInBackgroundLockedInValue"
+ "fast_user_switch"
+ "id  _Nullable MBDebugInitializationDictValueForKey(NSString * _Nonnull __strong)"
+ "initWithNetworkManager:networkList:"
+ "initialSetupAnalytics"
+ "interfaceName"
+ "invalidateProximitySessionWithCompletion:"
+ "ios_macos_proximity"
+ "isMacOSAutoUpdateManaged"
+ "joinNetworkUsingProximityNetworks:withPasswords:"
+ "joinedNetworkUsingProximityData"
+ "noteNetworkJoinedUsingProximityData:"
+ "noteProximityAppleAccountSignInSuccess:"
+ "noteProximityConnectionAvailableForAppleAccountSignIn:"
+ "noteUsedProximityDataForSetup:"
+ "noteUserSelectedMacBuddyMigrationMode:"
+ "noteUserUsedVisualProximityPairing:"
+ "overrideDefaultInterface"
+ "overrideSASInformation:"
+ "prepareForAppleAccountSignInWithCompletion:"
+ "prepareInitialSetupAnalytics"
+ "prepareProximitySetupAnalytics"
+ "preserveAnalyticsData:withCompletionBlock:"
+ "proximityAppleAccountSignInResult"
+ "proximityAvailableForAppleAccount"
+ "proximityDisplayCode:"
+ "proximityHandler"
+ "proximityPINCodeTypeChanged:"
+ "proximitySessionLost"
+ "proximitySessionReady:"
+ "proximitySetupAnalytics"
+ "recordProximityAnalytics"
+ "removeTOSRequiredCookie:"
+ "retrieveAnalyticsDataWithCompletionBlock:"
+ "retrieveMessageSessionWithCompletion:"
+ "setAutomaticallyInstallConfigDataAndSecurityUpdates:"
+ "setAutomaticallyInstallMacOSUpdates:"
+ "setAutomaticallyInstallMacOSUpdatesLockedInValue:"
+ "setDidJoinNetworkUsingProximityData:"
+ "setDownloadUpdatesInBackground:"
+ "setDownloadUpdatesInBackgroundLockedInValue:"
+ "setInitialSetupAnalytics:"
+ "setOverrideDefaultInterface:"
+ "setProximityHandler:"
+ "setProximitySetupAnalytics:"
+ "setRecordProximityAnalytics:"
+ "setTOSRequiredCookie:"
+ "setTestingModeEnablement:"
+ "setupiCloudPasswordResetWithCompletion:"
+ "shouldPrepareTeslaUserForResumePostUserSessionSwap"
+ "spoofedCurrentProductMarketingVersion"
+ "spoofedPreviousProductMarketingVersion"
+ "usedProximityDataForSetup"
+ "usedVisualProximityPairing"
+ "v16@?0@\"NSString\"8"
+ "v24@0:8@\"CUMessageSession\"16"
+ "v24@0:8@\"SASProximityInformation\"16"
+ "v24@0:8@?<v@?@\"CUMessageSession\">16"
+ "v36@0:8@\"NSArray\"16B24@?<v@?BB>28"
+ "void MBRemoveTOSRequiredCookie()"
+ "void MBSetTOSRequiredCookie()"
- "-[MBUserConfigurator fetchIntelligenceEnablementStatusWithCompletionBlock:]_block_invoke_2"
- "-[MBUserConfigurator systemIsEligibleForIntelligenceUsingCache:completion:]_block_invoke_3"
- "-[MBUserConfigurator systemIsEligibleForIntelligenceUsingCache:completion:]_block_invoke_4"
- "Attempting to generate PCS Identity without iCloud username or password"
- "Error updating availability: %@"
- "Failed to get Intelligence status: %@"
- "Fetched Intelligence status: %i"
- "Finished call to PCS setup with appleID=%@, p=0x%x, id=%@ (err=%@)"
- "addNetworksFromProximity:"
- "createTeslaUsersWithInfo:completionBlock:"
- "getGMOptInToggleWithCompletion:"
- "iCloudRecoveryUserPassword"
- "updateAvailabilityWithCompletion:"
- "v32@0:8@\"NSArray\"16@?<v@?BB>24"

```
