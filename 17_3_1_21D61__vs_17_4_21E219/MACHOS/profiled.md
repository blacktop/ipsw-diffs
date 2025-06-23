## profiled

> `/usr/libexec/profiled`

```diff

-2261.0.0.0.0
-  __TEXT.__text: 0x99290
-  __TEXT.__auth_stubs: 0x2090
-  __TEXT.__objc_stubs: 0xf440
-  __TEXT.__objc_methlist: 0x4bb8
-  __TEXT.__gcc_except_tab: 0x126c
-  __TEXT.__oslogstring: 0xc0bb
-  __TEXT.__cstring: 0x89e0
+2288.0.1.0.0
+  __TEXT.__text: 0x99b40
+  __TEXT.__auth_stubs: 0x20f0
+  __TEXT.__objc_stubs: 0xf520
+  __TEXT.__objc_methlist: 0x4bb0
+  __TEXT.__gcc_except_tab: 0x128c
+  __TEXT.__oslogstring: 0xc19b
+  __TEXT.__cstring: 0x8aab
   __TEXT.__const: 0x68
-  __TEXT.__objc_methname: 0x12eae
+  __TEXT.__objc_methname: 0x12ea6
   __TEXT.__objc_classname: 0xb36
-  __TEXT.__objc_methtype: 0x1ffc
-  __TEXT.__unwind_info: 0x15cc
-  __DATA_CONST.__auth_got: 0x1058
-  __DATA_CONST.__got: 0x1588
-  __DATA_CONST.__const: 0x1af0
-  __DATA_CONST.__cfstring: 0x8360
+  __TEXT.__objc_methtype: 0x1fb6
+  __TEXT.__unwind_info: 0x15d4
+  __DATA_CONST.__auth_got: 0x1088
+  __DATA_CONST.__got: 0x15a0
+  __DATA_CONST.__const: 0x1b00
+  __DATA_CONST.__cfstring: 0x8420
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x180
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x808
+  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__objc_intobj: 0x198
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x70f0
-  __DATA.__objc_selrefs: 0x4198
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x800
-  __DATA.__objc_superrefs: 0x140
+  __DATA.__objc_const: 0x71b0
+  __DATA.__objc_selrefs: 0x41c8
   __DATA.__objc_ivar: 0x1c0
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0x4ea

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
-  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration

   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement
   - /System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore
+  - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 600AE817-46BA-3118-A63B-056822D80280
-  Functions: 1902
-  Symbols:   1426
-  CStrings:  5831
+  UUID: 3ED1DDF9-45C5-3ECB-8E8E-941B5A478B1F
+  Functions: 1901
+  Symbols:   1436
+  CStrings:  5858
 
Symbols:
+ _MCClientRestrictionsErrorDomain
+ _MCGestaltIsPhone
+ _MCGestaltIsVisionDevice
+ _MCGestaltIsWatch
+ _MCGestaltIsiPad
+ _MCSettingParameterRangeMaximumKey
+ _OBJC_CLASS_$_DMCRatchet
+ _OBJC_CLASS_$_SUUtility
+ _calloc
+ _kMCClientRestrictionsOverrideRestrictions
+ _objc_release_x2
- _OBJC_CLASS_$_LARatchetManager
CStrings:
+ "@48@0:8@16q24@32@40"
+ "B116@0:8@16B24@28B36@40@48@56@64@72B80^B84^B92^B100^@108"
+ "CLIENT_RESTRICTION_ERROR_ALREADY_OVERRIDDEN"
+ "CLIENT_RESTRICTION_ERROR_CANNOT_OVERRIDE_P_CLIENT_TYPE"
+ "ERROR_PROFILE_DRIVEN_ENROLLMENT_BLOCKED"
+ "Profile %{public}@ cancelled queueing for installation"
+ "Profile %{public}@ failed queueing for %{public}@ because UI profile installation is restricted"
+ "Profile %{public}@ failed queueing for %{public}@ because profile-driven MDM enrollment is blocked"
+ "Profile %{public}@ failed queueing for %{public}@ with purgatory error: %{public}@"
+ "Profile %{public}@ succesfully queued in holding tank for %{public}@"
+ "Profile %{public}@ successfully queued for Settings jump for %{public}@"
+ "Profile '%{public}@' does not define a target device. Assuming %{public}lu..."
+ "Profile purgatory followUp failed to clear pending followUp items with error: %{public}@"
+ "Profile purgatory followUp failed to create MCProfile with error: %{public}@"
+ "Profile purgatory followUp failed to post with error: %{public}@"
+ "Purging purgatory profile data for identifier: %@"
+ "Purging purgatory profiles"
+ "SOFTWARE_UPDATE_DEVICE_ID"
+ "T@\"NSArray\",?,R,&,N"
+ "T@\"NSString\",?,R,C"
+ "TargetDeviceResolver skipping prompt because only this device is available"
+ "_applyHeuristicsToRestrictions:forProfile:ignoresUnrestrictableApps:"
+ "_postPurgatoryFollowUpForProfileData:targetDevice:"
+ "_profileDrivenEnrollmentBlocked"
+ "_queueProfileData:profile:forDevice:completion:"
+ "_reallyRemoveInstalledProfileWithIdentifier:installationType:options:source:"
+ "_replacePurgatoryProfilesForTargetDevice:"
+ "_showPromptForThisDeviceAndOtherDevicesWithCompletionBlock:"
+ "addPurgatoryProfileData:identifier:targetDevice:outError:"
+ "applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:completion:"
+ "applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:sender:localizedClientDescription:localizedWarningMessage:completion:"
+ "awaitDeviceConfiguredWithCompletionHandler:"
+ "canOverrideRestrictions"
+ "com.apple.aac"
+ "currentProductType"
+ "fetchCloudConfigWithCompletionHandler:"
+ "isAuthorizedForOperation:"
+ "isDeviceConfigured"
+ "isVisionDevice"
+ "isVisionProfileEnrollEnabled"
+ "markCloudConfigurationAsUICompleted"
+ "memberQueueOverridingRestrictionClientUUID"
+ "payloadsRequiringRatchetWithStolenDeviceProtection"
+ "peekPurgatoryProfileDataForTargetDevice:"
+ "purgatorySupportedForDevice:"
+ "purgePurgatoryProfileWithIdentifier:targetDevice:"
+ "purgePurgatoryProfilesForTargetDevice:"
+ "restoreSetAsideCloudConfigAndProfilesWithCompletionHandler:"
+ "sendPurgatoryProfileData:identifier:targetDevice:outError:"
+ "setClientRestrictions:overrideRestrictions:appsAndOptions:system:clientType:clientUUID:sender:localizedClientDescription:localizedWarning:shouldRecomputeNag:outRestrictionsChanged:outEffectiveSettingsChanged:outRecomputedNag:outError:"
+ "setMemberQueueOverridingRestrictionClientUUID:"
+ "setUserControllableViewsSyncStatus:error:"
+ "softwareUpdateDeviceIDWithDefaultValue:"
+ "storeCloudConfig:completionHandler:"
+ "thisDeviceType"
+ "v24@0:8@?<v@?>16"
+ "v48@0:8@16@24Q32@?40"
+ "v76@0:8@\"NSDictionary\"16B24@\"NSArray\"28@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSString\"60@?<v@?BB@\"NSError\">68"
+ "v76@0:8@16B24@28@36@44@52@60@?68"
+ "v84@0:8@16B24@28@36@44@52@60@68@?76"
- "@40@0:8@16@24Q32"
- "B100@0:8@16@24@32@40@48@56B64^B68^B76^B84^@92"
- "B100@0:8@16B24@28@36@44@52@60^B68^B76^B84^@92"
- "B104@0:8@16@24@32@40@48@56@64^B72^B80^B88^@96"
- "B104@0:8@16B24@28@36@44@52@60B68^B72^B80^B88^@96"
- "B112@0:8@16@24B32@36@44@52@60@68B76^B80^B88^B96^@104"
- "Creating profile with profile data failed with error: %{public}@"
- "Failed to clear pending followUp Items with error: %{public}@"
- "Posting Follow Up Failed with error: %{public}@"
- "Profile '%{public}@' cancelled queueing for installation"
- "Profile '%{public}@' cannot be queued for '%{public}@' while UI profile installation is restricted"
- "Profile '%{public}@' failed queueing for %{public}@ with error: %{public}@"
- "Profile '%{public}@' succesfully queued in holding tank for %{public}@"
- "Profile '%{public}@' successfully queued for Settings jump for %{public}@"
- "Purging profiles from purgatory for the device"
- "Remove profile data with identifier: %@"
- "T@\"NSArray\",R,&,N"
- "TargetDeviceResolver skipping prompt because only valid target is iPhone"
- "_applyHeuristicsToRestrictions:forProfile:outError:"
- "_purgatorySupportedForDevice:"
- "_queueProfileData:profile:forDevice:"
- "_showPromptForPhoneAndOtherDevicesWithCompletionBlock:"
- "addProfileData:withIdentifier:toHoldingTankForDevice:outError:"
- "applyRestrictionDictionary:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:completion:"
- "applyRestrictionDictionary:appsAndOptions:clientType:clientUUID:sender:localizedClientDescription:localizedWarningMessage:completion:"
- "isFeatureEnabled"
- "leaveClique:"
- "peekProfileDataFromPurgatoryForDeviceType:"
- "purgeProfileWithIdentifier:fromPurgatoryForTargetDeviceType:"
- "purgeProfilesFromPurgatoryForTargetDeviceType:"
- "sendProfileData:withIdentifier:toPurgatoryForTargetDeviceType:outError:"
- "setClientRestrictions:appsAndOptions:clientType:clientUUID:sender:localizedClientDescription:localizedWarning:outRestrictionsChanged:outEffectiveSettingsChanged:outRecomputedNag:outError:"
- "setClientRestrictions:appsAndOptions:system:clientType:clientUUID:sender:localizedClientDescription:localizedWarning:shouldRecomputeNag:outRestrictionsChanged:outEffectiveSettingsChanged:outRecomputedNag:outError:"
- "setClientRestrictions:clientType:clientUUID:sender:localizedClientDescription:localizedWarning:shouldRecomputeNag:outRestrictionsChanged:outEffectiveSettingsChanged:outRecomputedNag:outError:"
- "setClientRestrictions:system:clientType:clientUUID:sender:localizedClientDescription:localizedWarning:outRestrictionsChanged:outEffectiveSettingsChanged:outRecomputedNag:outError:"
- "setClientRestrictions:system:clientType:clientUUID:sender:localizedClientDescription:localizedWarning:shouldRecomputeNag:outRestrictionsChanged:outEffectiveSettingsChanged:outRecomputedNag:outError:"
- "targetDeviceTypeForCurrentDevice"
- "unavailablePayloadsWithStolenDeviceProtection"
- "v72@0:8@\"NSDictionary\"16@\"NSArray\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@?<v@?BB@\"NSError\">64"

```
