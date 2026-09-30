## GenerativeExperiencesRuntime

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime`

```diff

-154.744.10.3.0
-  __TEXT.__text: 0x7a214
-  __TEXT.__auth_stubs: 0x3130
-  __TEXT.__objc_methlist: 0x908
+154.749.4.0.0
+  __TEXT.__text: 0x8753c
+  __TEXT.__auth_stubs: 0x3160
+  __TEXT.__objc_methlist: 0x918
   __TEXT.__const: 0x27d2
-  __TEXT.__cstring: 0x371d
-  __TEXT.__constg_swiftt: 0x1058
-  __TEXT.__swift5_typeref: 0x1f21
+  __TEXT.__cstring: 0x396d
+  __TEXT.__constg_swiftt: 0x1060
+  __TEXT.__swift5_typeref: 0x1f05
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x962
-  __TEXT.__swift5_fieldmd: 0xa08
+  __TEXT.__swift5_reflstr: 0x982
+  __TEXT.__swift5_fieldmd: 0xa38
   __TEXT.__swift5_assocty: 0x3b0
-  __TEXT.__oslogstring: 0x3d3d
+  __TEXT.__oslogstring: 0x44cd
   __TEXT.__swift5_proto: 0x1b8
   __TEXT.__swift5_types: 0x10c
-  __TEXT.__swift_as_entry: 0x21c
-  __TEXT.__swift_as_ret: 0x23c
-  __TEXT.__swift5_capture: 0xc7c
+  __TEXT.__swift_as_entry: 0x244
+  __TEXT.__swift_as_ret: 0x264
+  __TEXT.__swift5_capture: 0xcb0
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__unwind_info: 0x2108
-  __TEXT.__eh_frame: 0x6090
+  __TEXT.__unwind_info: 0x2268
+  __TEXT.__eh_frame: 0x66a8
   __TEXT.__objc_classname: 0x46
-  __TEXT.__objc_methname: 0x1aea
+  __TEXT.__objc_methname: 0x1afc
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0xc90
+  __DATA_CONST.__got: 0xd98
   __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f8
+  __DATA_CONST.__objc_selrefs: 0x600
   __DATA_CONST.__objc_protorefs: 0x80
-  __AUTH_CONST.__auth_got: 0x1898
-  __AUTH_CONST.__auth_ptr: 0xb20
-  __AUTH_CONST.__const: 0x2880
-  __AUTH_CONST.__objc_const: 0x21a8
+  __AUTH_CONST.__auth_got: 0x18b0
+  __AUTH_CONST.__auth_ptr: 0xaa8
+  __AUTH_CONST.__const: 0x2998
+  __AUTH_CONST.__objc_const: 0x21b0
   __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x6d8
-  __DATA.__data: 0xf88
+  __DATA.__data: 0x1018
   __DATA.__bss: 0x1b30
-  __DATA.__common: 0x50
+  __DATA.__common: 0xf8
   __DATA_DIRTY.__objc_data: 0x5a0
   __DATA_DIRTY.__data: 0x1630
   __DATA_DIRTY.__bss: 0x1580

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
+  - /System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences
   - /System/Library/PrivateFrameworks/GenerativeFunctions.framework/GenerativeFunctions

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2813
-  Symbols:   225
-  CStrings:  693
+  Functions: 2942
+  Symbols:   229
+  CStrings:  730
 
Symbols:
+ __os_activity_create
+ _geteuid
+ _os_activity_scope_enter
+ _os_activity_scope_leave
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "AvailabilityManagedConfiguration.updateManagedConfiguration()"
+ "AvailabilityManager.updateAccessNotGrantedUseCases(shouldUpdateSecureCache:)"
+ "AvailabilityManager.updateAll()"
+ "AvailabilityManager.updateAvailabilityCache()"
+ "AvailabilityManager.updateDisabledUseCases()"
+ "AvailabilityManager.updateUseCaseReadiness()"
+ "AvailabilityManager.updateUseCasesWhoseAssetsOutOfStorage()"
+ "AvailabilityReporter.reportCurrentAvailabilityState()"
+ "AvailabilityStreamWriter performed coalesced write of event: %{public}s"
+ "Failed to create os_activity"
+ "GenerativeFunctionsFoundation/OSAvailability.swift"
+ "No availability cache or ticket status change. Not invoking reportCurrentAvailabilityState"
+ "UserDefaults.set(accessNotGrantedUseCases): %s"
+ "UserDefaults.set(availability): %{public}s"
+ "UserDefaults.set(disabledUseCases): %s"
+ "UserDefaults.set(disallowedUseCases): %s"
+ "UserDefaults.set(essentialAssetReadiness): %{bool,public}d"
+ "UserDefaults.set(reasons): %s"
+ "UserDefaults.set(useCaseReadiness): %{public}s"
+ "UserDefaults.set(useCasesWhoseAssetsAreOutOfStorage): %{public}s"
+ "VisualIntelligenceControlWidgetMigration"
+ "VisualIntelligenceControlWidgetMigration: Attempting to add the VisualIntelligence ControlWidget to control center"
+ "VisualIntelligenceControlWidgetMigration: running"
+ "[End] AvailabilityReporter.reportCurrentAvailabilityState()"
+ "[Start] AvailabilityReporter.reportCurrentAvailabilityState()"
+ "didAccessNotGrantedUseCasesChanged: %{bool,public}d UUID: %{public}s"
+ "didChangeUseCaseReadiness: %{bool,public}d UUID: %{public}s"
+ "didDisabledUseCasesChanged: %{bool,public}d UUID: %{public}s"
+ "didDisallowedUseCasesChanged: %{bool,public}d UUID: %{public}s"
+ "didUseCasesWhoseAssetsOutOfStorageChanged: %{bool,public}d UUID: %{public}s"
+ "getAvailabilityReasonsPairIncludingSiriAsset: AFSettingsConnection().areSiriSAEAssetsAvailable(): %{bool,public}d"
+ "getAvailabilityReasonsPairIncludingSiriAsset: CatalogClient().siriResourceAvailability(): %{public}@"
+ "getAvailabilityReasonsPairIncludingSiriAsset: calling AFSettingsConnection().areSiriSAEAssetsAvailable()"
+ "getAvailabilityReasonsPairIncludingSiriAsset: calling CatalogClient().siriResourceAvailability()"
+ "getTelemetry returning:\n %s"
+ "getTelemetry statusStep: status=%lld useCaseIdentifier=%s categoryMask=%lld"
+ "getTelemetryWith:"
+ "updateAvailabilityCache: CloudSubscriptionFeatures.Availability.current(): %{public}s"
+ "updateAvailabilityCache: calling CloudSubscriptionFeatures.Availability.current()"
+ "updateAvailabilityCache: calling CloudeSubscriptionAvailability.getAccessStatus(requireSecureAccessStatus:)"
+ "updateAvailabilityCache: calling CloudeSubscriptionAvailability.getAccessStatus(requireSecureAccessStatus:) %{public}s"
- "AvailabilityStreamWriter performed coalesced write of event: %s"
- "getAvailabilityReasonsPairIncludingSiriAsset: CatalogClient().siriResourceAvailability: %{public}@"
- "getAvailabilityReasonsPairIncludingSiriAsset: areSiriAssetsAvailable: %{bool,public}d"
- "updateAvailabilityCache: cloudAvailabilityState: %{public}s"

```
