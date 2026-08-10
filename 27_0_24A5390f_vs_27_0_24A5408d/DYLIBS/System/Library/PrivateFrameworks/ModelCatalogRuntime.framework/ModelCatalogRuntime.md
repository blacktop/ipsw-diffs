## ModelCatalogRuntime

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-302.1.0.2.0
-  __TEXT.__text: 0x83d60
+302.6.0.1.100
+  __TEXT.__text: 0x89e64
   __TEXT.__objc_methlist: 0x604
-  __TEXT.__const: 0x30a8
-  __TEXT.__constg_swiftt: 0x1244
-  __TEXT.__swift5_typeref: 0x1a26
+  __TEXT.__const: 0x3458
+  __TEXT.__constg_swiftt: 0x1300
+  __TEXT.__swift5_typeref: 0x1bb6
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0xa23
-  __TEXT.__swift5_fieldmd: 0xbcc
-  __TEXT.__swift5_assocty: 0x1d8
-  __TEXT.__swift5_capture: 0x1414
-  __TEXT.__cstring: 0x14fb
-  __TEXT.__oslogstring: 0x432a
-  __TEXT.__swift5_proto: 0x17c
-  __TEXT.__swift5_types: 0x110
+  __TEXT.__swift5_reflstr: 0xad3
+  __TEXT.__swift5_fieldmd: 0xcc8
+  __TEXT.__swift5_assocty: 0x1f0
+  __TEXT.__swift5_capture: 0x15c4
+  __TEXT.__cstring: 0x191b
+  __TEXT.__oslogstring: 0x458a
+  __TEXT.__swift5_proto: 0x1ac
+  __TEXT.__swift5_types: 0x124
   __TEXT.__swift_as_entry: 0x164
   __TEXT.__swift_as_ret: 0x178
   __TEXT.__swift_as_cont: 0x310
-  __TEXT.__swift5_protos: 0x4c
+  __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1cb8
-  __TEXT.__eh_frame: 0x4464
+  __TEXT.__unwind_info: 0x1e70
+  __TEXT.__eh_frame: 0x4574
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x4a0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x4590
+  __AUTH_CONST.__const: 0x4cf0
   __AUTH_CONST.__objc_const: 0x1698
-  __AUTH_CONST.__auth_got: 0x1490
+  __AUTH_CONST.__auth_got: 0x14e0
   __AUTH.__objc_data: 0x120
   __AUTH.__data: 0x488
-  __DATA.__data: 0x768
-  __DATA.__bss: 0x1a10
-  __DATA.__common: 0x18
+  __DATA.__data: 0x830
+  __DATA.__bss: 0x1f90
+  __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x400
   __DATA_DIRTY.__data: 0x1608
-  __DATA_DIRTY.__common: 0x398
+  __DATA_DIRTY.__common: 0x3d8
   __DATA_DIRTY.__bss: 0xa80
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3176
-  Symbols:   248
-  CStrings:  342
+  Functions: 3315
+  Symbols:   252
+  CStrings:  372
 
Symbols:
+ __CFXPCCreateCFObjectFromXPCObject
+ _notify_post
+ _os_eligibility_get_domain_answer
+ _swift_retain_x9
CStrings:
+ "Failed to post asset set updated notification for %s: %u"
+ "NOT_YET_AVAILABLE"
+ "OSEligibilityProbe: domain %{public}s answer=%{public}s countryPolicy=[%{public}s] isChina=%{bool}d"
+ "OSEligibilityProbe: domain %{public}s returned no context dictionary"
+ "OSEligibilityProbe: query for domain %{public}s failed with status %d"
+ "OSEligibilityProbe: querying domain %{public}s"
+ "OS_ELIGIBILITY_CONTEXT_COUNTRY_POLICY"
+ "bm_deviceInfo('deviceType')"
+ "bm_deviceInfo('isInternalBuild')"
+ "bm_featureFlagValue('"
+ "bm_gmBypass('adm')"
+ "bm_gmBypass('afm')"
+ "bm_isBuddyComplete()"
+ "bm_isSeedBuild()"
+ "bm_mobileGestalt('chipID')"
+ "bm_mobileGestalt('deviceSupportsGenerativeModelSystems')"
+ "bm_mobileGestalt('deviceSupportsHandwritingSynthesisModel')"
+ "bm_mobileGestalt('hardwarePlatform')"
+ "bm_mobileGestalt('isSimulator')"
+ "bm_osEligibility"
+ "bm_osEligibility received unknown domain: %{public}s"
+ "bm_osEligibility('copernicium', false)"
+ "bm_osEligibility(domain: %{public}s, allowChinaCountryPolicy: %{bool}d) -> answer: %{public}s, countryPolicy: [%{public}s], isChina: %{bool}d, result: %{bool}d"
+ "bm_userDefaults('com.apple.MobileSMS', 'IncludeSmartRepliesKey')"
+ "bm_userDefaults('com.apple.ModelCatalog.SpotlightKnowledge', 'AEMPreviousEmbeddingModelVersion')"
+ "bm_userDefaults('com.apple.spatialphotosrelive', 'LocallyDisabled')"
+ "com.apple.modelcatalog.agent.launchevents"
+ "com.apple.modelcatalog.asset-set-updated."
+ "com.apple.os-eligibility-domain.change.copernicium"
+ "copernicium"
+ "evaluationInputs"
- "com.apple.modelcatalog.launchevents.registration"
```
