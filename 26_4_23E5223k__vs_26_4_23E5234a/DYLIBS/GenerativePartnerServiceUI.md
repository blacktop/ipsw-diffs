## GenerativePartnerServiceUI

> `/System/Library/PrivateFrameworks/GenerativePartnerServiceUI.framework/GenerativePartnerServiceUI`

```diff

-222.35.2.0.0
-  __TEXT.__text: 0x936e4
-  __TEXT.__auth_stubs: 0x2c00
+222.35.4.0.1
+  __TEXT.__text: 0x89f1c
+  __TEXT.__auth_stubs: 0x2ba0
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_methlist: 0x3dc
-  __TEXT.__const: 0x4c84
-  __TEXT.__swift5_typeref: 0x898e
-  __TEXT.__oslogstring: 0x208d
-  __TEXT.__swift5_capture: 0x940
-  __TEXT.__constg_swiftt: 0x19d8
-  __TEXT.__swift5_reflstr: 0x1436
+  __TEXT.__const: 0x4c74
+  __TEXT.__swift5_typeref: 0x894c
+  __TEXT.__oslogstring: 0x186d
+  __TEXT.__swift5_capture: 0x8d0
+  __TEXT.__constg_swiftt: 0x1960
+  __TEXT.__swift5_reflstr: 0x13b6
   __TEXT.__swift5_assocty: 0x2c8
-  __TEXT.__swift5_fieldmd: 0x1244
-  __TEXT.__cstring: 0x2e03
+  __TEXT.__swift5_fieldmd: 0x1220
+  __TEXT.__cstring: 0x2c93
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_proto: 0x1fc
+  __TEXT.__swift5_proto: 0x200
   __TEXT.__swift5_types: 0x14c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift_as_entry: 0xf8
-  __TEXT.__swift_as_ret: 0xe0
+  __TEXT.__swift_as_entry: 0xf0
+  __TEXT.__swift_as_ret: 0xdc
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__unwind_info: 0x2178
-  __TEXT.__eh_frame: 0x33bc
+  __TEXT.__unwind_info: 0x20c8
+  __TEXT.__eh_frame: 0x3218
   __TEXT.__objc_classname: 0x54a
-  __TEXT.__objc_methname: 0x16b5
+  __TEXT.__objc_methname: 0x15d5
   __TEXT.__objc_methtype: 0x345
-  __TEXT.__objc_stubs: 0x1040
-  __DATA_CONST.__got: 0xae8
-  __DATA_CONST.__const: 0x170
+  __TEXT.__objc_stubs: 0xfa0
+  __DATA_CONST.__got: 0xa80
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x570
+  __DATA_CONST.__objc_selrefs: 0x548
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1608
-  __AUTH_CONST.__const: 0x3558
-  __AUTH_CONST.__objc_const: 0x1208
+  __AUTH_CONST.__auth_got: 0x15d8
+  __AUTH_CONST.__const: 0x3480
+  __AUTH_CONST.__objc_const: 0x11a0
   __AUTH.__objc_data: 0x7d0
   __AUTH.__data: 0x1108
-  __DATA.__data: 0x1ab4
-  __DATA.__bss: 0x3638
+  __DATA.__data: 0x1ad4
+  __DATA.__bss: 0x3738
   __DATA.__common: 0x130
   __DATA_DIRTY.__objc_data: 0x158
-  __DATA_DIRTY.__data: 0x818
+  __DATA_DIRTY.__data: 0x780
   __DATA_DIRTY.__bss: 0x780
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5C42AE17-E7BA-38D6-A76B-08915896221F
-  Functions: 3646
+  UUID: 22598795-AC50-3A1C-AAC6-BE9012C1A23C
+  Functions: 3494
   Symbols:   263
-  CStrings:  678
+  CStrings:  633
 
Symbols:
+ _swift_initStaticObject
- _notify_post
CStrings:
- " for China region."
- "$__lazy_storage_$_generativePartnerServiceUserDefaults"
- "%{public}ld llms available"
- "%{public}s.%{public}s: first run - migrating legacy GenerativeAssistantSettings: %{public}s"
- "%{public}s.%{public}s: first run - no legacy GenerativeAssistantSettings found"
- "%{public}s.%{public}s: no observers registered."
- "%{public}s.%{public}s: observer %{public}s already registered. Ignoring."
- ",\nAllLLMUISettings = "
- ",\nsetupPrompt = "
- ",\nuseConfirmationPrompts = "
- "Availability change detected for LLM id: %{public}s: %{public}s; reloading"
- "Could not find isEnabled key in legacy domain (%{public}s; Cannot verify read/write access."
- "Could not find migration key in GPS domain. Cannot verify read/write access."
- "Could not retrieve key/value written to GPS domain. Cannot verify read/write access."
- "Could not retrieve key/value written to legacy domain (%{public}s. Cannot verify read/write access."
- "Full read/write access is not confirmed; please file a radar for this process"
- "LLM with id \"%{public}s\" unavailability status changed to: unavailable = %{bool,public}d"
- "LLM with id %{public}s is currently selected, but unavailable"
- "LLM with id: \"%{public}s\" is unavailable and removed from the available LLM list"
- "Loading llms%{public}s"
- "Missing legacy shared prefs entitlement for \"%{public}s\". Performing manual read/write check..."
- "Missing target shared prefs read-write entitlement for \"%{public}s\". Performing manual read/write check..."
- "Selected LLM id: %{public}s was disabled due to availability change"
- "Subscribing to availability changes for LLM id: %{public}s"
- "Unable to select new llm with id: \"%{public}s\""
- "Verified read/write access to GPS domain"
- "Verified read/write access to legacy domain (%{public}s"
- "addObserver:forKeyPath:options:context:"
- "availableLLMs"
- "com.apple.security.exception.shared-preference.read-write"
- "gatMigrationComplete2"
- "migrateLegacyUserDefaults(from:)"
- "notifyObservers(_:)"
- "persistentDomainForName:"
- "read/write shared prefs access for \"%{public}s\" confirmed: %{bool,public}d"
- "registerObserver(_:)"
- "removeObjectForKey:"
- "selectedLLMId = "
- "setValue:forKey:"
- "standardUserDefaults"
- "subscribedAvailabilityIdentifiers"
- "updateLLMAvailability for: %{public}ld LLMs"
- "updateLLMAvailability: LLM %{public}s use case %{public}s is available"
- "updateLLMAvailability: LLM %{public}s use case %{public}s is restricted: %{public}s"
- "updateLLMAvailability: LLM %{public}s use case %{public}s is unavailable: %{public}s"

```
