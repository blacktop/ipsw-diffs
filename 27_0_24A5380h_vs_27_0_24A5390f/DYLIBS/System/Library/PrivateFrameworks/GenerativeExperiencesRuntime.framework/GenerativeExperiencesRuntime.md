## GenerativeExperiencesRuntime

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-287.0.6.0.0
-  __TEXT.__text: 0xe7014
-  __TEXT.__objc_methlist: 0x95c
-  __TEXT.__const: 0x5a7c
-  __TEXT.__cstring: 0x1e65
-  __TEXT.__constg_swiftt: 0x1ea8
-  __TEXT.__swift5_typeref: 0x286c
+291.1.0.5.0
+  __TEXT.__text: 0xeab80
+  __TEXT.__objc_methlist: 0x94c
+  __TEXT.__const: 0x5b4c
+  __TEXT.__cstring: 0x1ed5
+  __TEXT.__constg_swiftt: 0x1f14
+  __TEXT.__swift5_typeref: 0x2898
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0xffd
-  __TEXT.__swift5_fieldmd: 0x1428
+  __TEXT.__swift5_reflstr: 0x104d
+  __TEXT.__swift5_fieldmd: 0x145c
   __TEXT.__swift5_assocty: 0x400
-  __TEXT.__oslogstring: 0x8760
-  __TEXT.__swift5_proto: 0x300
-  __TEXT.__swift5_types: 0x21c
-  __TEXT.__swift_as_entry: 0x334
-  __TEXT.__swift_as_ret: 0x354
-  __TEXT.__swift_as_cont: 0x6fc
-  __TEXT.__swift5_capture: 0x276c
+  __TEXT.__oslogstring: 0x89a0
+  __TEXT.__swift5_proto: 0x304
+  __TEXT.__swift5_types: 0x220
+  __TEXT.__swift_as_entry: 0x350
+  __TEXT.__swift_as_ret: 0x368
+  __TEXT.__swift_as_cont: 0x73c
+  __TEXT.__swift5_capture: 0x2794
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x33a0
-  __TEXT.__eh_frame: 0x90ec
+  __TEXT.__unwind_info: 0x3468
+  __TEXT.__eh_frame: 0x941c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x128
-  __DATA_CONST.__objc_classlist: 0x1d0
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6e0
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x8428
-  __AUTH_CONST.__objc_const: 0x3150
-  __AUTH_CONST.__auth_got: 0x2780
+  __AUTH_CONST.__const: 0x8488
+  __AUTH_CONST.__objc_const: 0x3248
+  __AUTH_CONST.__auth_got: 0x27b0
   __AUTH.__objc_data: 0x3b8
-  __AUTH.__data: 0x430
-  __DATA.__data: 0xad8
-  __DATA.__bss: 0x2770
-  __DATA.__common: 0x78
+  __AUTH.__data: 0x508
+  __DATA.__data: 0xb08
+  __DATA.__bss: 0x27f0
+  __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x6c8
-  __DATA_DIRTY.__data: 0x32d0
+  __DATA_DIRTY.__data: 0x3298
   __DATA_DIRTY.__bss: 0x2900
   __DATA_DIRTY.__common: 0x2b0
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
   - /System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
+  - /System/Library/PrivateFrameworks/DeviceConfiguration.framework/DeviceConfiguration
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/GenerativeAgentsTransportRuntime.framework/GenerativeAgentsTransportRuntime

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5122
-  Symbols:   282
-  CStrings:  647
+  Functions: 5187
+  Symbols:   283
+  CStrings:  656
 
Symbols:
+ _swift_task_isCancelledWithFlags
CStrings:
+ "AvailabilityDeviceConfiguration.restrictedUseCases()"
+ "Device Configuration fetch failed: %{public}@"
+ "Device Configuration unavailable; preserving previous MDM restrictions"
+ "EnhancedSiriVisibility: migration cleared stale hasAppEverBeenInstalled (non-EU, bit set but app not installed) to allow reinstall."
+ "Failed to subscribe to Device Configuration changes: %@"
+ "ForceVisualIntelligenceDisallowed"
+ "GenerativeAppsVisibility: Request to install %{public}s accepted."
+ "Received DeviceConfiguration change for %{public}s"
+ "Skipping availability report: base availability not yet cached this boot."
+ "WARNING: forcing allowVisualIntelligence=false"
+ "[End] checking Device Configuration"
+ "[Start] checking Device Configuration"
+ "allowVisualIntelligence"
+ "com.apple.externalproviderservice-xpc"
+ "com.apple.generativeexperiences.deviceConfiguration.modelCatalogChanged"
+ "updatePQAIndexingReadiness: PQA CSF push failed: %{public}@"
+ "updatePQAIndexingReadiness: PQA CSF push succeeded"
+ "updatePQAIndexingReadiness: single-flight task already running, skipping"
- "GenerativeAppsVisibility: Request to install %{public}s succeeded."
- "XPC: %{public}s called with TCC service: %{public}s"
- "XPC: %{public}s called with TCC service: %{public}s, app bundle ID: %{public}s"
- "com.apple.externalproviderservice"
- "tccAuthorizedBundleIdentifiers(service:reply:)"
- "tccForceAuthorize(service:for:)"
- "tccForceReset(service:for:)"
- "updatePQAIndexingReadiness: CSF push failed: %{public}@"
- "updatePQAIndexingReadiness: CSF push succeeded"
```
