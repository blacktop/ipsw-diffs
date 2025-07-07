## GenerativePartnerServiceUI

> `/System/Library/PrivateFrameworks/GenerativePartnerServiceUI.framework/GenerativePartnerServiceUI`

```diff

-202.0.2.0.0
-  __TEXT.__text: 0x7c11c
-  __TEXT.__auth_stubs: 0x2990
+205.1.0.0.0
+  __TEXT.__text: 0x7daf4
+  __TEXT.__auth_stubs: 0x2a00
+  __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0x3d4
-  __TEXT.__cstring: 0x337a
-  __TEXT.__const: 0x39b4
+  __TEXT.__const: 0x39e4
+  __TEXT.__cstring: 0x348d
+  __TEXT.__swift5_typeref: 0x733c
+  __TEXT.__oslogstring: 0x1b1d
+  __TEXT.__swift5_capture: 0x854
+  __TEXT.__swift5_reflstr: 0x120c
+  __TEXT.__swift5_assocty: 0x2b0
   __TEXT.__constg_swiftt: 0x1834
-  __TEXT.__swift5_typeref: 0x7488
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x1203
   __TEXT.__swift5_fieldmd: 0x1064
-  __TEXT.__swift5_assocty: 0x2b0
+  __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_proto: 0x1ec
   __TEXT.__swift5_types: 0x134
-  __TEXT.__oslogstring: 0x15c4
-  __TEXT.__swift5_capture: 0x834
+  __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift_as_entry: 0xf8
   __TEXT.__swift_as_ret: 0xe4
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x20d8
-  __TEXT.__eh_frame: 0x2f9c
+  __TEXT.__unwind_info: 0x2088
+  __TEXT.__eh_frame: 0x308c
   __TEXT.__objc_classname: 0x1f
-  __TEXT.__objc_methname: 0xddf
+  __TEXT.__objc_methname: 0xde6
   __TEXT.__objc_methtype: 0x1af
-  __DATA_CONST.__got: 0xa20
+  __DATA_CONST.__got: 0xa60
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x548
+  __DATA_CONST.__objc_selrefs: 0x550
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x14c8
-  __AUTH_CONST.__const: 0x3138
+  __AUTH_CONST.__auth_got: 0x1500
+  __AUTH_CONST.__const: 0x3188
   __AUTH_CONST.__objc_const: 0x1178
   __AUTH.__objc_data: 0x8a8
-  __AUTH.__data: 0x1440
-  __DATA.__data: 0x1a58
+  __AUTH.__data: 0x1458
+  __DATA.__data: 0x1a3c
   __DATA.__bss: 0x3970
   __DATA.__common: 0x188
   __DATA_DIRTY.__data: 0x1e8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A2EA1A71-4647-39C4-92EB-FB624DC99C5F
-  Functions: 3219
-  Symbols:   237
-  CStrings:  603
+  UUID: 87D41E0F-8E3D-32B3-87E0-EBF4831E22AC
+  Functions: 3231
+  Symbols:   238
+  CStrings:  616
 
Symbols:
+ _dlopen
CStrings:
+ " to help you write text, create an image, answer questions, and more."
+ "!! You have a rate limit override set to: forceRateLimitState = %{public}s"
+ "%{public}ld llms available"
+ "%{public}s"
+ "%{public}s Completed updating billing plan"
+ "%{public}s Duplicate request to poll; re-enabling post-poll timer"
+ "%{public}s Fetching updated billing plan"
+ "%{public}s Reset polling state"
+ "%{public}s Resetting poll timer"
+ "%{public}s User is not on a paid plan; not updating cached credentials"
+ "%{public}s User is unexpectedly logged out while waiting for billing refresh; not updating cached credentials"
+ "%{public}s Waiting for %{public}llums"
+ "%{public}s lastPollStarted: %{public}s"
+ "%{public}s pollingEndTime: %{public}s"
+ "%{public}s.%{public}s: Calling ExternalAIAuthenticatorHelper().authenticateWithExternalAI()"
+ "%{public}s.%{public}s: ExternalAIAuthenticatorHelper().authenticateWithExternalAI() exception: %{public}@"
+ "%{public}s.%{public}s: ExternalAIAuthenticatorHelper().authenticateWithExternalAI() unknown exception type: %{public}@"
+ "%{public}s.%{public}s: ExternalAIAuthenticatorHelper().signOutOpenAI()"
+ "%{public}s.%{public}s: first run - migrating legacy GenerativeAssistantSettings: %{public}s"
+ "%{public}s.%{public}s: first run - no legacy GenerativeAssistantSettings found"
+ "%{public}s.%{public}s: observer %{public}s already registered. Ignoring."
+ "%{public}s: %{public}s is not allowed"
+ "%{public}s: Bundle.main.bundleIdentifier = %s, callbackURL scheme: %{public}s"
+ "%{public}s: Bundle.main.bundleIdentifier = nil. callbackURL scheme: %{public}s"
+ "%{public}s: Can't retrieve user info as authenticator is nil."
+ "%{public}s: Can't start sign in session as authenticator is nil."
+ "%{public}s: ExternalAIAuthenticator.signOut() exception: %{public}@"
+ "%{public}s: a workspace is required, but the credentials have none"
+ "%{public}s: an empty value for allowedExternalIntelligenceWorkspaceIDs was provided, unable to validate any credentials."
+ "%{public}s: no workspace restriction"
+ "%{public}s: workspace id %{public}s matched. User signed in with an accepted workspace."
+ "(Anvil) Entitlement values for keys %{public}s are present, but the values aren't convertible to [String: Bool]!"
+ "(Anvil) Missing required keychain access groups: %{public}s"
+ "(Anvil) Required entitlement key %{public}s has value <false>"
+ "(Anvil) Unable to find necessary entitlement keys in process: %{public}s"
+ "/System/Library/Frameworks/SafariServices.framework/SafariServices"
+ "An account is needed to use "
+ "Anvil sign in failed: %{public}@"
+ "Availability change detected for LLM id: %{public}s: %{public}s; reloading"
+ "Could not find isEnbled key in legacy domain (%{public}s; Cannot verify read/write access."
+ "Could not find migration key in GPS domain. Cannot verify read/write access."
+ "Could not retrieve key/value written to GPS domain. Cannot verify read/write access."
+ "Could not retrieve key/value written to legacy domain (%{public}s. Cannot verify read/write access."
+ "Did not find any provider declarations in bundle: %{public}@"
+ "Entitlement key %{public}s is present, but its value isn't %{public}s!"
+ "Entitlements for keys %{public}s are present, but the values aren't convertible to [String: Any]!"
+ "Error decoding providers: %{public}@"
+ "Extending Apple Intelligence is not available to children 13 or younger."
+ "Extending Apple Intelligence is protected by a Screen Time passcode."
+ "Full read/write access is not confirmed; please file a radar for this process"
+ "LLM with id: \"%{public}s\" is unavailable and removed from the available LLM list"
+ "LLM with id: \"%{public}s\" unavailable; status changed to: %{bool,public}d"
+ "Loaded %{public}ld providers"
+ "Loading llms%{public}s"
+ "Missing entitlement key %{public}s"
+ "Missing entitlements for keys %{public}s"
+ "Missing legacy shared prefs entitlement for \"%{public}s\". Performing manual read/write check..."
+ "Missing target shared prefs read-write entitlement for \"%{public}s\". Performing manual read/write check..."
+ "Phase change from %{public}s to %{public}s"
+ "Returning available providers filtered by .isChina=%{bool,public}d: %{public}s"
+ "Selected LLM id: %{public}s was disabled due to availability change"
+ "Subscribing to availability changes for LLM id: %{public}s"
+ "Unable to construct resourceBundleQuery for ModelBundle(%{public}s: locale: %{public}s. Error: %{public}@"
+ "Unable to select new llm with id: \"%{public}s\""
+ "Updated rate limit for category %{public}ld to %{bool,public}d"
+ "Verified read/write access to GPS domain"
+ "Verified read/write access to legacy domain (%{public}s"
+ "[Deep Links] Unsupported path component: \"%{public}s\" (expected: \"ExternalAIModel\")"
+ "[Deep Links] handleDeepLinkParams: %{public}s"
+ "[Deep Links] resourceDictionary dump:\n%{public}s"
+ "[Onboarding.init] defaultLLM.id = %{public}s"
+ "[Onboarding.onAppear] preselectedProvider.id = %{public}s"
+ "[Onboarding.onAppear] previouslyActiveProvider.id = %{public}s"
+ "[Onboarding.preselectedProvider] Failed to find LLM provider with ID '%{public}s'"
+ "allowedExternalIntelligenceWorkspaceIDs %{public}s"
+ "com.apple.Settings.AppleIntelligence"
+ "modelBundle retrieval returned nil for LLM provider: %{public}s"
+ "read/write shared prefs access for \"%{public}s\" confirmed: %{bool,public}d"
+ "removeObjectForKey:"
+ "retrieveLatestRateLimitBudget for category %{public}ld failed with error: %{public}@"
+ "retrieveUserInfo() failed: %{public}@"
+ "setValue:forKey:"
+ "updateLLMAvailability for: %{public}ld LLMs"
+ "updateLLMAvailability: LLM %{public}s use case %{public}s is available"
+ "updateLLMAvailability: LLM %{public}s use case %{public}s is unavailable: %s"
- " to help your write text, create an image, answer questions, and more."
- "!! You have a rate limit override set to: forceRateLimitState = %s"
- "%ld llms available"
- "%s Completed updating billing plan"
- "%s Duplicate request to poll; re-enabling post-poll timer"
- "%s Fetching updated billing plan"
- "%s Reset polling state"
- "%s Resetting poll timer"
- "%s User is not on a paid plan; not updating cached credentials"
- "%s User is unexpectedly logged out while waiting for billing refresh; not updating cached credentials"
- "%s Waiting for %llums"
- "%s lastPollStarted: %s"
- "%s pollingEndTime: %s"
- "%s.%s: Calling ExternalAIAuthenticatorHelper().authenticateWithExternalAI()"
- "%s.%s: ExternalAIAuthenticatorHelper().authenticateWithExternalAI() exception: %@"
- "%s.%s: ExternalAIAuthenticatorHelper().authenticateWithExternalAI() unknown exception type: %@"
- "%s.%s: ExternalAIAuthenticatorHelper().signOutOpenAI()"
- "%s.%s: first run - migrating legacy GenerativeAssistantSettings: %s"
- "%s.%s: first run - no legacy GenerativeAssistantSettings found"
- "%s.%s: observer %s already registered. Ignoring."
- "%s: %s is not allowed"
- "%s: Bundle.main.bundleIdentifier = %s, callbackURL scheme: %s"
- "%s: Bundle.main.bundleIdentifier = nil. callbackURL scheme: %s"
- "%s: Can't retrieve user info as authenticator is nil."
- "%s: Can't start sign in session as authenticator is nil."
- "%s: ExternalAIAuthenticator.signOut() exception: %@"
- "%s: a workspace is required, but the credentials have none"
- "%s: an empty value for allowedExternalIntelligenceWorkspaceIDs was provided, unable to validate any credentials."
- "%s: no workspace restriction"
- "%s: workspace id %s matched. User signed in with an accepted workspace."
- "(Anvil) Entitlement values for keys %s are present, but the values aren't convertible to [String: Bool]!"
- "(Anvil) Missing required keychain access groups: %s"
- "(Anvil) Required entitlement key %s has value <false>"
- "(Anvil) Unable to find necessary entitlement keys in process: %s"
- "Anvil sign in failed: %@"
- "Availability change detected for LLM id: %s: %s; reloading"
- "Did not find any provider declarations in bundle: %@"
- "Entitlement key %s is present, but its value isn't %s!"
- "Entitlements for keys %s are present, but the values aren't convertible to [String: Any]!"
- "Error decoding providers: %@"
- "LLM with id: \"%s\" is unavailable and removed from the available LLM list"
- "LLM with id: \"%s\" unavailable; status changed to: %{bool}d"
- "Loaded %ld providers"
- "Loading llms%s"
- "Missing entitlement key %s"
- "Missing entitlements for keys %s"
- "Missing legacy shared prefs entitlement for \"%s\""
- "Missing target shared prefs read-write entitlement for \"%s\""
- "Phase change from %s to %s"
- "Returning available providers filtered by .isChina=%{bool}d: %s"
- "Selected LLM id: %s was disabled due to availability change"
- "Subscribing to availability changes for LLM id: %s"
- "Unable to construct resourceBundleQuery for ModelBundle(%s: locale: %{public}s. Error: %{public}@"
- "Unable to select new llm with id: \"%s\""
- "Updated rate limit for category %ld to %{bool}d"
- "Your parent or guardian has turned off Apple Intelligence Extension features on this "
- "[Deep Links] Unsupported path component: \"%s\" (expected: \"ExternalAIModel\")"
- "[Deep Links] handleDeepLinkParams: %s"
- "[Deep Links] resourceDictionary dump:\n%s"
- "[Onboarding.init] defaultLLM.id = %s"
- "[Onboarding.onAppear] preselectedProvider.id = %s"
- "[Onboarding.onAppear] previouslyActiveProvider.id = %s"
- "[Onboarding.preselectedProvider] Failed to find LLM provider with ID '%s'"
- "allowedExternalIntelligenceWorkspaceIDs %s"
- "isExternalIntelligenceAllowed"
- "modelBundle retrieval returned nil for LLM provider: %s"
- "retrieveLatestRateLimitBudget for category %ld failed with error: %@"
- "retrieveUserInfo() failed: %@"
- "updateLLMAvailability for: %ld LLMs"
- "updateLLMAvailability: LLM %s use case %s is available"
- "updateLLMAvailability: LLM %s use case %s is unavailable: %s"

```
