## GenerativePartnerService

> `/System/Library/PrivateFrameworks/GenerativePartnerService.framework/Versions/A/GenerativePartnerService`

```diff

-291.6.0.3.203
-  __TEXT.__text: 0x9383c
-  __TEXT.__objc_methlist: 0x364
-  __TEXT.__swift5_typeref: 0x180b
-  __TEXT.__swift5_fieldmd: 0x171c
-  __TEXT.__const: 0x5168
-  __TEXT.__constg_swiftt: 0x1638
+297.6.0.5.0
+  __TEXT.__text: 0x9af28
+  __TEXT.__objc_methlist: 0x36c
+  __TEXT.__swift5_typeref: 0x19ed
+  __TEXT.__swift5_fieldmd: 0x187c
+  __TEXT.__const: 0x56a8
+  __TEXT.__constg_swiftt: 0x1714
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x15b1
-  __TEXT.__swift5_assocty: 0x358
+  __TEXT.__swift5_reflstr: 0x1691
+  __TEXT.__swift5_assocty: 0x388
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_proto: 0x2d0
-  __TEXT.__swift5_types: 0x1d4
-  __TEXT.__cstring: 0x288b
-  __TEXT.__swift5_capture: 0x15bc
-  __TEXT.__oslogstring: 0x42bd
-  __TEXT.__swift_as_entry: 0x1d4
-  __TEXT.__swift_as_ret: 0x1e8
-  __TEXT.__swift_as_cont: 0x400
+  __TEXT.__swift5_proto: 0x310
+  __TEXT.__swift5_types: 0x1f0
+  __TEXT.__cstring: 0x2a2b
+  __TEXT.__swift5_capture: 0x1614
+  __TEXT.__oslogstring: 0x442d
+  __TEXT.__swift_as_entry: 0x1e4
+  __TEXT.__swift_as_ret: 0x1f4
+  __TEXT.__swift_as_cont: 0x414
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x2f80
-  __TEXT.__eh_frame: 0x4f58
+  __TEXT.__unwind_info: 0x31a8
+  __TEXT.__eh_frame: 0x5298
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x440
+  __DATA_CONST.__objc_selrefs: 0x458
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__got: 0x848
-  __AUTH_CONST.__const: 0x6830
-  __AUTH_CONST.__objc_const: 0x12e8
-  __AUTH_CONST.__auth_got: 0x1480
+  __AUTH_CONST.__const: 0x6ca0
+  __AUTH_CONST.__objc_const: 0x1370
+  __AUTH_CONST.__auth_got: 0x1508
   __AUTH.__objc_data: 0x250
-  __AUTH.__data: 0x7e8
-  __DATA.__data: 0xa50
+  __AUTH.__data: 0x8b8
+  __DATA.__data: 0xbb8
   __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_data: 0x2e8
-  __DATA_DIRTY.__data: 0x15d0
+  __DATA_DIRTY.__data: 0x1508
   __DATA_DIRTY.__bss: 0x1480
   __DATA_DIRTY.__common: 0x150
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4756
+  Functions: 4915
   Symbols:   197
-  CStrings:  515
+  CStrings:  534
 
CStrings:
+ "%{public}s failed with exception: %{public}@"
+ "%{public}s: EPS init start"
+ "%{public}s: First unlock: warming provider cache"
+ "%{public}s: Registering first-unlock provider-cache warm-up"
+ "%{public}s: [Non-XPC-client path] Setting the internal change handler"
+ "%{public}s: [XPC-client path] Setting the internal change handler through XPC"
+ "%{public}s: fetched and stored %{public}ld external providers"
+ "%{public}s: fetching providers via XPC"
+ "%{public}s: no cache populated this lifetime; fetching fresh"
+ "%{public}s: returning %{public}ld external providers from XPC"
+ "%{public}s: returning %{public}ld providers"
+ "%{public}s: serving provider %{public}s"
+ "%{public}s: using cached external providers"
+ "/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework"
+ "Enhanced Siri is not opted in; skipping the vip metadata refresh"
+ "Enhanced Siri turned on; refreshing the vip metadata skipped while it was off"
+ "Loaded %{public}ld invocation patterns (locale=%{public}s version=%{public}s)"
+ "No invocation patterns for %{public}s: %{public}s"
+ "No invocation patterns: %{public}s"
+ "Refreshed metadata for %{public}ld providers"
+ "Skipping VIP provider \"%s\": not available on %s"
+ "Skipping uncompilable pattern: %{public}s"
+ "action"
+ "converted_patterns"
+ "could not parse "
+ "externalProviders()"
+ "fetchAndStoreExternalProviders()"
+ "installedExternalProviders()"
+ "no Enigma asset for "
+ "no ask_provider patterns in "
+ "no enigma_patterns directory in "
+ "no locale given and none to resolve from"
+ "pattern"
+ "priority"
+ "regex"
+ "requestCompletion_v3(...) failed with ExternalProviderError: %s"
+ "requestCompletion_v3: streaming event error: %{public}@"
+ "version"
- "EPS init start"
- "Error during XPC call to fetch externalProviders: %{public}@. Trying local fallback."
- "External providers changed; notify observers."
- "ExternalProviderService: configuration changed, refreshing cache"
- "Fetching externalProviders() locally"
- "Fetching externalProviders() via XPC"
- "No cache; retrieve fresh external providers"
- "No changes found in external providers list."
- "No providers returned (this is suspicious)"
- "Refreshing cache at medium priority"
- "Returning %{public}ld external providers from XPC"
- "Serving cached provider: %{public}s"
- "Storing retrieved external providers"
- "Updating external providers list now."
- "Using cache for externalProviders"
- "[Non-XPC-client path] Setting the internal change handler"
- "[XPC-client path] Setting the internal change handler through XPC"
- "externalProviders() failed with exception: %{public}@"
- "externalProviders() returning %{public}ld providers"
```
