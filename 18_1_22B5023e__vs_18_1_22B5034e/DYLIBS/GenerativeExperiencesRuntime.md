## GenerativeExperiencesRuntime

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime`

```diff

-145.505.100.0.0
-  __TEXT.__text: 0x54968
-  __TEXT.__auth_stubs: 0x2780
+145.513.100.0.0
+  __TEXT.__text: 0x57aa8
+  __TEXT.__auth_stubs: 0x2840
   __TEXT.__objc_methlist: 0x36c
-  __TEXT.__const: 0x1ad0
-  __TEXT.__cstring: 0x2a1d
-  __TEXT.__swift5_typeref: 0x136a
-  __TEXT.__oslogstring: 0x1f50
-  __TEXT.__constg_swiftt: 0xae8
-  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__const: 0x1ce0
+  __TEXT.__cstring: 0x2b3d
+  __TEXT.__swift5_typeref: 0x1394
+  __TEXT.__oslogstring: 0x2210
+  __TEXT.__constg_swiftt: 0xb34
+  __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_reflstr: 0x581
-  __TEXT.__swift5_fieldmd: 0x6c4
-  __TEXT.__swift5_assocty: 0x1f0
-  __TEXT.__swift5_proto: 0x140
-  __TEXT.__swift5_types: 0xc8
-  __TEXT.__swift5_capture: 0x8cc
+  __TEXT.__swift5_fieldmd: 0x6fc
+  __TEXT.__swift5_assocty: 0x238
+  __TEXT.__swift5_proto: 0x160
+  __TEXT.__swift5_types: 0xd0
+  __TEXT.__swift5_capture: 0x8e0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x1700
-  __TEXT.__eh_frame: 0x4038
+  __TEXT.__unwind_info: 0x1788
+  __TEXT.__eh_frame: 0x41b0
   __TEXT.__objc_classname: 0x46
-  __TEXT.__objc_methname: 0x1445
+  __TEXT.__objc_methname: 0x1474
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x988
-  __DATA_CONST.__const: 0x260
+  __DATA_CONST.__got: 0xa28
+  __DATA_CONST.__const: 0x280
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a8
+  __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_protorefs: 0x70
-  __AUTH_CONST.__auth_got: 0x13c0
-  __AUTH_CONST.__auth_ptr: 0x860
-  __AUTH_CONST.__const: 0x1b58
+  __AUTH_CONST.__auth_got: 0x1420
+  __AUTH_CONST.__auth_ptr: 0x868
+  __AUTH_CONST.__const: 0x1bf8
   __AUTH_CONST.__objc_const: 0x1a30
   __AUTH.__objc_data: 0xbc0
   __AUTH.__data: 0x6a8
-  __DATA.__data: 0xcf0
-  __DATA.__bss: 0x1600
-  __DATA.__common: 0x80
+  __DATA.__data: 0xd50
+  __DATA.__bss: 0x1a00
+  __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x9f8
+  __DATA_DIRTY.__data: 0x960
   __DATA_DIRTY.__bss: 0xf00
   __DATA_DIRTY.__common: 0xe0
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/IntelligenceFlowShared.framework/IntelligenceFlowShared
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
   - /System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport
   - /System/Library/PrivateFrameworks/PromptKit.framework/PromptKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1993
-  Symbols:   183
-  CStrings:  474
+  Functions: 2053
+  Symbols:   190
+  CStrings:  491
 
Symbols:
+ _MCFeatureGenmojiAllowed
+ _MCEffectiveSettingsChangedNotification
+ _MCFeatureImagePlaygroundAllowed
+ _MCFeatureImageWandAllowed
+ _MCFeatureWritingToolsAllowed
+ _getuid
+ _OBJC_CLASS_$_MCProfileConnection
CStrings:
+ "sharedConnection"
+ "com.apple.profilePreferencesForMDMChangedNotification"
+ "Received %!{(MISSING)public}s for Availability update"
+ "getAvailabilityReasonsPairIncludingSiriAsset: final: %!{(MISSING)public}s - %!{(MISSING)public}s"
+ "ManagedConfiguration: %!{(MISSING)public}s is not allowed"
+ "Can't encode Disallowed Use Cases with error: %!@(MISSING)"
+ "VisualGeneration.KeyboardEmojiGenerator"
+ "managedConfigurationUseCaseIdentifierIsAllowed: MCProfileConnection.shared().effectiveBoolValue for %!{(MISSING)public}s is %!{(MISSING)public}s"
+ "[End] update Managed Configuration"
+ "effectiveBoolValueForSetting:"
+ "[Start] update Managed Configuration"
+ "No managed use case cache change. Bail out sending notification"
+ "Did set secure availability: %!{(MISSING)public}s; reasons: %!{(MISSING)public}s"
+ "Failed to set secure availability: %!{(MISSING)public}s; reasons: %!{(MISSING)public}s"
+ "com.apple.managedconfiguration.effectivesettingschanged"
+ "managedConfigurationUseCaseIdentifierIsAllowed: useCaseIdentifierToMCFeature is nil for %!{(MISSING)public}s"
+ "com.apple.GenerativePlayground"
+ "getAvailabilityReasonsPairIncludingSiriAsset: areSiriAssetsAvailable: %!{(MISSING)bool,public}d"
+ "com.apple.WritingTools"
+ "getCloudAvailabilityStateAvailabilityReasonsPair: cloudAvailabilityState.toAvailabilityReasonsPair: %!{(MISSING)public}s - %!{(MISSING)public}s"
+ "com.apple.PaperKit.ImageGeneration"
- "Received %!s(MISSING) for Availability update"
- "updateAvailabilityCache: final: %!{(MISSING)public}s - %!{(MISSING)public}s"
- "updateAvailabilityCache: cloudAvailabilityState.toAvailabilityReasonsPair: %!{(MISSING)public}s - %!{(MISSING)public}s"
- "updateAvailabilityCache: areSiriAssetsAvailable: %!{(MISSING)bool,public}d"

```
