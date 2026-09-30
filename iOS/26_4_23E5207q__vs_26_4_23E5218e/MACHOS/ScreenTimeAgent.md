## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

-605.4.13.0.0
-  __TEXT.__text: 0x12e4e8
+605.4.16.0.0
+  __TEXT.__text: 0x12ff10
   __TEXT.__auth_stubs: 0x23e0
-  __TEXT.__objc_stubs: 0x12a60
-  __TEXT.__objc_methlist: 0xa21c
-  __TEXT.__const: 0x4d58
+  __TEXT.__objc_stubs: 0x12bc0
+  __TEXT.__objc_methlist: 0xa2c4
+  __TEXT.__const: 0x4dd8
   __TEXT.__gcc_except_tab: 0x22d8
-  __TEXT.__cstring: 0xab4e
-  __TEXT.__oslogstring: 0x13c90
-  __TEXT.__objc_methname: 0x1d7c7
+  __TEXT.__cstring: 0xabee
+  __TEXT.__oslogstring: 0x14320
+  __TEXT.__objc_methname: 0x1d997
   __TEXT.__objc_classname: 0x2cc2
   __TEXT.__objc_methtype: 0x5e02
-  __TEXT.__constg_swiftt: 0x3230
-  __TEXT.__swift5_typeref: 0x28b8
+  __TEXT.__constg_swiftt: 0x3290
+  __TEXT.__swift5_typeref: 0x2920
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_reflstr: 0x2059
-  __TEXT.__swift5_fieldmd: 0x1540
-  __TEXT.__swift5_assocty: 0x248
-  __TEXT.__swift5_proto: 0x260
+  __TEXT.__swift5_fieldmd: 0x1550
+  __TEXT.__swift5_assocty: 0x250
+  __TEXT.__swift5_proto: 0x264
   __TEXT.__swift5_types: 0x18c
   __TEXT.__swift5_capture: 0x21f0
   __TEXT.__swift_as_entry: 0x264
   __TEXT.__swift_as_ret: 0x198
-  __TEXT.__swift5_protos: 0xa4
+  __TEXT.__swift5_protos: 0xa8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x4780
-  __TEXT.__eh_frame: 0x6168
+  __TEXT.__unwind_info: 0x47c8
+  __TEXT.__eh_frame: 0x6198
   __DATA_CONST.__auth_got: 0x1200
-  __DATA_CONST.__got: 0x1360
+  __DATA_CONST.__got: 0x1390
   __DATA_CONST.__auth_ptr: 0x6b0
-  __DATA_CONST.__const: 0x9af8
-  __DATA_CONST.__cfstring: 0x4c20
+  __DATA_CONST.__const: 0x9b60
+  __DATA_CONST.__cfstring: 0x4ca0
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x510

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x1ea90
-  __DATA.__objc_selrefs: 0x5710
+  __DATA.__objc_const: 0x1eb70
+  __DATA.__objc_selrefs: 0x5768
   __DATA.__objc_ivar: 0x814
   __DATA.__objc_data: 0x4cf8
-  __DATA.__data: 0x7318
-  __DATA.__bss: 0x37b0
-  __DATA.__common: 0xb8
+  __DATA.__data: 0x7340
+  __DATA.__bss: 0x37c0
+  __DATA.__common: 0xd0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BA7E00DE-35C5-3E3F-BB67-378AE35EEADF
-  Functions: 6177
-  Symbols:   1348
-  CStrings:  8004
+  UUID: 95135138-C4E2-3E18-87EE-66B89322F11D
+  Functions: 6207
+  Symbols:   1351
+  CStrings:  8046
 
Symbols:
+ _$s15ScreenTimeSwift21RegulatoryAccountTypeOs23CustomStringConvertibleAAMc
+ _OBJC_CLASS_$_CEMActivationSimpleDeclaration
+ _OBJC_CLASS_$_CEMPredicateiCloudAccount
+ _STBlueprintConfigurationBaseIdentifier
- _STRegionRatingsDontAllowValue
CStrings:
+ "%@.appExceptionsActivation.%@"
+ "%{public}@: Updated is third party replacing app & website activity to false"
+ "%{public}@: Updated is third party replacing app & website activity to true"
+ "(null)"
+ "Account state change: canCloudKitMirror=%{public}d, oldCanMirror=%{public}d, familyMembers=%d, appleID=%@, initializing=%{public}d"
+ "CloudKit mirroring capability: %{public}d (supportsDeviceToDeviceEncryption)"
+ "Creating app exceptions cache"
+ "Disabling app & website activity due to third party application being authorized for app & website usage."
+ "Failed to create declarations for app exceptions:%@ activation:%@"
+ "Failed to fetch local user with error: %{public}@"
+ "Failed to request internal authorization after enabling management: %{public}@"
+ "Failed to reset data access authorizations with error: %{public}@"
+ "Failed to revoke internal authorization: %{public}@"
+ "Family has %lu members"
+ "Fetching app & website activity enabled"
+ "Identifier"
+ "No app exceptions declaration created. Skipping serialized payload creation."
+ "Processing regulatory app store rating override. %{public}s"
+ "RegulatoryPolicyProviderUtility determined regulatory account type for local user from userAgeRangeFetcher: ageRange=%{public}lu, altDSID present=true"
+ "RegulatoryPolicyProviderUtility mapped age range to regulatory account type: ageRange=%{public}lu, accountType=%{public}s"
+ "RegulatoryPolicyProviderUtility no altDSID for local user, using unknown age range"
+ "Restriction values for %{public}@: ratingApps=%{public}@, ratingMovies=%{public}@, ratingTVShows=%{public}@"
+ "Restriction values: Found ratings declaration %{public}@ but no Payload"
+ "Restriction values: No system.ratings declarations found in updated declarations"
+ "Serialization error. Exceptions:%@ activation:%@"
+ "Setting rating to `Don't Allow`"
+ "Successfully reset data access authorizations"
+ "Third party replacing app & website activity is already true and app & website activity is disabled, nothing to do."
+ "User not signed inor invalid identifier. Not processing app exceptions"
+ "_logRestrictionValuesFromDeclarations:"
+ "appExceptionsDeclarationForUser:usingCache:"
+ "appStore"
+ "applyAppsRatingOverrideWithRegulatoryPolicy:"
+ "buildWithDSID:"
+ "buildWithIdentifier:withStandardConfigurations:withPredicate:"
+ "disableAppAndWebsiteActivityDueToThirdPartyAppWithCompletionHandler:"
+ "failed set third party replacing app & website activity: %{public}@"
+ "isAppAndWebsiteActivityEnabledWithCompletionHandler:"
+ "isThirdPartyReplacingAppAndWebsiteActivity"
+ "rangeOfString:"
+ "resetDataAccessAuthorizationsWithCompletionHandler:"
+ "serializedAppExceptionsDeclarationsForUser:"
+ "setIsThirdPartyReplacingAppAndWebsiteActivity:"
+ "setMaximumRating:"
- "Failed to request internal authorization after enabling management: %@{public}"
- "Failed to revoke internal authorization: %@{public}"
- "RevokeAccess policy but apps rating is set to %@. Applying `Don't Allow` restriction"
- "RevokeAccess policy is active. Updating CEM configurations"
- "Unexpected number of app rating declarations found: %@"
- "_updateDeclarations:withRegulatoryPolicy:"
- "payloadRatingApps"
- "setPayloadRatingApps:"

```
