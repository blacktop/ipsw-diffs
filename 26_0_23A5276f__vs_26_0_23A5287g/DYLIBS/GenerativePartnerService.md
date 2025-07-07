## GenerativePartnerService

> `/System/Library/PrivateFrameworks/GenerativePartnerService.framework/GenerativePartnerService`

```diff

-202.0.2.0.0
-  __TEXT.__text: 0x149a0
-  __TEXT.__auth_stubs: 0xd00
+205.1.0.0.0
+  __TEXT.__text: 0x1578c
+  __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_methlist: 0x70
-  __TEXT.__cstring: 0x846
-  __TEXT.__swift5_typeref: 0x47c
-  __TEXT.__swift5_reflstr: 0x30c
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__const: 0xf16
+  __TEXT.__cstring: 0x851
+  __TEXT.__const: 0xf18
   __TEXT.__constg_swiftt: 0x4f0
+  __TEXT.__swift5_typeref: 0x47c
   __TEXT.__swift5_fieldmd: 0x384
   __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_reflstr: 0x31c
+  __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0xe0
   __TEXT.__swift5_types: 0x48
-  __TEXT.__oslogstring: 0x715
+  __TEXT.__oslogstring: 0xaed
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift5_capture: 0x6c
+  __TEXT.__swift5_capture: 0x7c
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x748
+  __TEXT.__unwind_info: 0x718
   __TEXT.__eh_frame: 0x4f8
-  __TEXT.__objc_methname: 0x159
+  __TEXT.__objc_methname: 0x17e
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x680
-  __AUTH_CONST.__const: 0xa90
+  __DATA_CONST.__objc_selrefs: 0x98
+  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__const: 0xab8
   __AUTH_CONST.__objc_const: 0x2a8
   __AUTH.__objc_data: 0x1e0
   __AUTH.__data: 0x190
   __DATA.__data: 0x348
-  __DATA.__bss: 0x1880
   __DATA.__common: 0x68
+  __DATA.__bss: 0x1880
   __DATA_DIRTY.__data: 0x1f0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 05137918-61DA-39E1-A222-E4551BA449B3
-  Functions: 814
+  UUID: 7DDB2CB0-49F3-372A-8ECF-E3206BB4DB6D
+  Functions: 821
   Symbols:   122
-  CStrings:  95
+  CStrings:  105
 
CStrings:
+ "%{public}ld llms available"
+ "%{public}s.%{public}s: first run - migrating legacy GenerativeAssistantSettings: %{public}s"
+ "%{public}s.%{public}s: first run - no legacy GenerativeAssistantSettings found"
+ "%{public}s.%{public}s: observer %s already registered. Ignoring."
+ "Availability change detected for LLM id: %{public}s: %{public}s; reloading"
+ "Could not find isEnbled key in legacy domain (%{public}s; Cannot verify read/write access."
+ "Could not find migration key in GPS domain. Cannot verify read/write access."
+ "Could not retrieve key/value written to GPS domain. Cannot verify read/write access."
+ "Could not retrieve key/value written to legacy domain (%{public}s. Cannot verify read/write access."
+ "Did not find any provider declarations in bundle: %{public}@"
+ "Entitlement key %{public}@ is present, but isn't an array of strings!"
+ "Error decoding providers: %{public}@"
+ "Full read/write access is not confirmed; please file a radar for this process"
+ "LLM with id: \"%{public}s\" is unavailable and removed from the available LLM list"
+ "LLM with id: \"%{public}s\" unavailable; status changed to: %{bool,public}d"
+ "Loaded %{public}ld providers"
+ "Loading llms%{public}s"
+ "Missing entitlement key %{public}@"
+ "Missing legacy shared prefs entitlement for \"%{public}s\". Performing manual read/write check..."
+ "Missing target shared prefs read-write entitlement for \"%{public}s\". Performing manual read/write check..."
+ "Returning available providers filtered by .isChina=%{bool,public}d: %{public}s"
+ "Selected LLM id: %{public}s was disabled due to availability change"
+ "Subscribing to availability changes for LLM id: %{public}s"
+ "Unable to construct resourceBundleQuery for ModelBundle(%{public}s: locale: %{public}s. Error: %{public}@"
+ "Unable to select new llm with id: \"%{public}s\""
+ "Verified read/write access to GPS domain"
+ "Verified read/write access to legacy domain (%{public}s"
+ "[iconImageData] icon data successfully read from %{public}s"
+ "[iconImageData] unable to find icon resource URL for %{public}s.svg under bundle resources"
+ "[iconImageData] unable to read data from file at %{public}s"
+ "read/write shared prefs access for \"%{public}s\" confirmed: %{bool,public}d"
+ "removeObjectForKey:"
+ "setValue:forKey:"
+ "updateLLMAvailability for: %{public}ld LLMs"
+ "updateLLMAvailability: LLM %{public}s use case %{public}s is available"
+ "updateLLMAvailability: LLM %{public}s use case %{public}s is unavailable: %{public}s"
- "%ld llms available"
- "%s.%s: first run - migrating legacy GenerativeAssistantSettings: %s"
- "%s.%s: first run - no legacy GenerativeAssistantSettings found"
- "%s.%s: observer %s already registered. Ignoring."
- "Availability change detected for LLM id: %s: %s; reloading"
- "Did not find any provider declarations in bundle: %@"
- "Entitlement key %@ is present, but isn't an array of strings!"
- "Error decoding providers: %@"
- "LLM with id: \"%s\" is unavailable and removed from the available LLM list"
- "LLM with id: \"%s\" unavailable; status changed to: %{bool}d"
- "Loaded %ld providers"
- "Loading llms%s"
- "Missing entitlement key %@"
- "Missing legacy shared prefs entitlement for \"%s\""
- "Missing target shared prefs read-write entitlement for \"%s\""
- "Returning available providers filtered by .isChina=%{bool}d: %s"
- "Selected LLM id: %s was disabled due to availability change"
- "Subscribing to availability changes for LLM id: %s"
- "Unable to construct resourceBundleQuery for ModelBundle(%s: locale: %{public}s. Error: %{public}@"
- "Unable to select new llm with id: \"%s\""
- "[iconImageData] icon data successfully read from %s"
- "[iconImageData] unable to find icon resource URL for %s.svg under bundle resources"
- "[iconImageData] unable to read data from file at %s"
- "updateLLMAvailability for: %ld LLMs"
- "updateLLMAvailability: LLM %s use case %s is available"
- "updateLLMAvailability: LLM %s use case %s is unavailable: %s"

```
