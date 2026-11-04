## GenerativePartnerService

> `/System/Library/PrivateFrameworks/GenerativePartnerService.framework/GenerativePartnerService`

```diff

-297.12.4.0.0
-  __TEXT.__text: 0x9b804
-  __TEXT.__objc_methlist: 0x36c
-  __TEXT.__swift5_typeref: 0x1a39
-  __TEXT.__swift5_fieldmd: 0x18cc
-  __TEXT.__const: 0x58c8
-  __TEXT.__constg_swiftt: 0x1780
-  __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x16d1
-  __TEXT.__swift5_assocty: 0x3b8
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_proto: 0x328
-  __TEXT.__swift5_types: 0x1f8
-  __TEXT.__cstring: 0x27bb
-  __TEXT.__swift5_capture: 0x1668
-  __TEXT.__oslogstring: 0x47cd
-  __TEXT.__swift_as_entry: 0x1f4
-  __TEXT.__swift_as_ret: 0x20c
-  __TEXT.__swift_as_cont: 0x444
+297.15.7.0.0
+  __TEXT.__text: 0x86fec
+  __TEXT.__objc_methlist: 0x394
+  __TEXT.__cstring: 0x249b
+  __TEXT.__swift5_typeref: 0x17a1
+  __TEXT.__swift5_fieldmd: 0x16d0
+  __TEXT.__const: 0x4f28
+  __TEXT.__constg_swiftt: 0x1640
+  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_reflstr: 0x1551
+  __TEXT.__swift5_assocty: 0x358
+  __TEXT.__swift5_protos: 0x18
+  __TEXT.__swift5_proto: 0x2cc
+  __TEXT.__swift5_types: 0x1d8
+  __TEXT.__swift5_capture: 0x13b0
+  __TEXT.__oslogstring: 0x3b0d
+  __TEXT.__swift_as_entry: 0x1cc
+  __TEXT.__swift_as_ret: 0x1c0
+  __TEXT.__swift_as_cont: 0x3b0
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x3450
-  __TEXT.__eh_frame: 0x5770
+  __TEXT.__unwind_info: 0x2ee8
+  __TEXT.__eh_frame: 0x4c30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x320
-  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__const: 0x330
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x420
+  __DATA_CONST.__objc_selrefs: 0x400
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__got: 0x820
-  __AUTH_CONST.__const: 0x6de8
-  __AUTH_CONST.__objc_const: 0x1370
-  __AUTH_CONST.__auth_got: 0x1670
+  __DATA_CONST.__got: 0x770
+  __AUTH_CONST.__const: 0x6450
+  __AUTH_CONST.__objc_const: 0x1170
+  __AUTH_CONST.__auth_got: 0x1500
   __AUTH.__objc_data: 0x1e0
-  __AUTH.__data: 0x7f0
-  __DATA.__data: 0xa98
-  __DATA.__common: 0x88
-  __DATA_DIRTY.__objc_data: 0x358
-  __DATA_DIRTY.__data: 0x17e0
-  __DATA_DIRTY.__bss: 0x1980
-  __DATA_DIRTY.__common: 0x170
+  __AUTH.__data: 0x698
+  __DATA.__data: 0x938
+  __DATA.__common: 0x70
+  __DATA_DIRTY.__objc_data: 0x308
+  __DATA_DIRTY.__data: 0x15f0
+  __DATA_DIRTY.__bss: 0x1380
+  __DATA_DIRTY.__common: 0x138
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4985
-  Symbols:   240
-  CStrings:  531
+  Functions: 4526
+  Symbols:   232
+  CStrings:  455
 
Symbols:
- _OBJC_CLASS_$_AMSFeatureFlagITFE
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSJSONSerialization
- _OBJC_CLASS_$_OS_dispatch_queue
- _TCCAccessCopyBundleIdentifiersForService
- _TCCAccessResetForBundleId
- _TCCAccessSetForBundleId
- _swift_deletedAsyncMethodErrorTu
CStrings:
+ "%{public}s: no XPC client; %{public}s needs the com.apple.generativeexperiences.ExternalProviderService entitlement. Returning an empty list."
+ "%{public}s: no XPC client; %{public}s needs the com.apple.generativeexperiences.ExternalProviderService entitlement. Returning nil."
+ "Internal change handler set for GenerativePartnerServiceEngine"
+ "Invalid number of keys found, expected one."
+ "Localizable-APPLE_FEATURE_AI_CHINA"
+ "[ERROR] This process does not have the entitlement to read/write to %{public}s. Some features will be missing."
+ "externalProviders(filter:)"
+ "invokedProviderName(in:locale:)"
- "#/^((?i:(?:(?:hey|dis|oye|e a[íi]|ei|oi|hej)\\s+|嘿\\s*)?siri(?:야)?))([,，、])/#"
- "%{public}s entitlements missing; can not cache provider list."
- "%{public}s failed with exception: %{public}@"
- "%{public}s: First unlock: warming provider cache"
- "%{public}s: Registering first-unlock provider-cache warm-up"
- "%{public}s: [Non-XPC-client path] Setting the internal change handler"
- "%{public}s: adding %{public}ld uninstalled supported app(s): %{public}s"
- "%{public}s: caching %{public}ld supported apps: %{public}s"
- "%{public}s: disabled by bag key; treating as no supported apps"
- "%{public}s: expected one platformAttributes entry, got %{public}ld for %{public}s; skipping"
- "%{public}s: fetch failed; keeping existing cache, will retry"
- "%{public}s: fetched and stored %{public}ld external providers"
- "%{public}s: lookup failed: %{public}@"
- "%{public}s: no cache populated this lifetime; fetching fresh"
- "%{public}s: returned %{public}ld supported apps: %{public}s"
- "%{public}s: returning %{public}ld providers"
- "%{public}s: serving provider %{public}s"
- "%{public}s: supported apps unchanged (%{public}ld); skipping rebuild"
- "%{public}s: supported-apps cache stale or unpopulated"
- "%{public}s: using cached external providers"
- "%{public}s: warm-up populate; kicking supported-apps fetch"
- "/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework"
- "Adding AgentIntent provider: %{public}s"
- "Deprecated: externalProviders(for useCase: %{public}s returning all %{public}ld external providers"
- "Enhanced Siri is not opted in; skipping the vip metadata refresh"
- "Enhanced Siri turned on; refreshing the vip metadata skipped while it was off"
- "Error monitoring assets: %@"
- "Error: could not generate SHA256 hash for %{public}s"
- "Failed to decode the metadata of external providers: %@"
- "Failed to encode the metadata of external providers: %@"
- "Failed to find external vip providers with bundle ids: %s"
- "Failed to process vip data from Model Catalog: %@"
- "Failed to read blocked data from Model Catalog: %@"
- "Failed to read vip data from Model Catalog"
- "Fetching initial configuration"
- "GenerativePartnerServiceSupportedAppsLookupEnabled"
- "Internal change handler set for ExternalProviderService"
- "Invalid ToolBox database; do not cache invalid provider list."
- "Loaded %{public}ld invocation patterns (locale=%{public}s version=%{public}s)"
- "Monitor task already running"
- "Provider with bundle id \"%{public}s\" is remotely restricted. Hiding from both EPS platform and Settings UI."
- "Received update for ThirdPartyProviderConfiguration: %s"
- "Refreshed metadata for %{public}ld providers"
- "Skipping %{public}s"
- "Skipping VIP provider \"%s\": not available on %s"
- "Skipping provider without model-delegation entitlement: %{public}s (%{public}s)"
- "Skipping uncompilable pattern: %{public}s"
- "System ChatGPT wrapper has availability = .forciblyHidden, Hiding from both EPS platform and Settings UI."
- "TCCUtils - resetting %{public}s for %{public}s"
- "TCCUtils - toggling on %{public}s for %{public}s"
- "VIP bundle IDs to be added from UserDefaults: %{public}s"
- "[ERROR] TCCUtils - FAILED to reset %{public}s for %{public}s"
- "[ERROR] TCCUtils - FAILED to toggle on %{public}s for %{public}s"
- "[ERROR] This process does not have the entitlement to read/write to %{public}s. Will not use a cache for external provider lists, and other features will be missing."
- "action"
- "converted_patterns"
- "could not parse "
- "externalProviderMetadataItems"
- "externalProviders()"
- "fetchAndStoreExternalProviders()"
- "fetchSupportedApps()"
- "installedExternalProviders(matching:)"
- "installedExternalProviders: %{public}s"
- "isExternalIntelligenceAllowed is false, returning an empty list of external providers"
- "modelcatalogmonitor"
- "no Enigma asset for "
- "no ask_provider patterns in "
- "no enigma_patterns directory in "
- "no locale given and none to resolve from"
- "pattern"
- "priority"
- "received an empty metadata for external providers"
- "received an empty name for %s"
- "received nil from UserDefaults for externalProviderMetadata"
- "refreshSupportedAppsCache()"
- "refreshSupportedAppsIfStale()"
- "refreshSupportedAppsOnWarmUp()"
- "regex"
- "supportedFeatures"
- "supportsExtendedRouting"
- "toolDatabase agentIntent query: %{public}ld ms"
- "version"
- "vipAndBlockedProvider/blocked.json"
- "vipAndBlockedProvider/vip.json"
```
