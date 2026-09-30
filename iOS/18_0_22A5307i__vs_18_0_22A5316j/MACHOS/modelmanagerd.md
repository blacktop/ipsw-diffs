## modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

-117.0.0.0.0
-  __TEXT.__text: 0x10a1b4
-  __TEXT.__auth_stubs: 0x2c90
-  __TEXT.__const: 0x2430
-  __TEXT.__cstring: 0x258c
-  __TEXT.__swift5_typeref: 0x18cc
+121.0.0.0.0
+  __TEXT.__text: 0x110298
+  __TEXT.__auth_stubs: 0x2cd0
+  __TEXT.__const: 0x2450
+  __TEXT.__cstring: 0x26ac
+  __TEXT.__swift5_typeref: 0x18f0
   __TEXT.__swift5_capture: 0xa3c
   __TEXT.__objc_methname: 0x418
-  __TEXT.__oslogstring: 0x5985
+  __TEXT.__oslogstring: 0x5cd5
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1b58
+  __TEXT.__constg_swiftt: 0x1b90
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x13b2
-  __TEXT.__swift5_fieldmd: 0x11ec
+  __TEXT.__swift5_reflstr: 0x13e2
+  __TEXT.__swift5_fieldmd: 0x1210
   __TEXT.__swift5_types: 0xfc
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_proto: 0x1e4
   __TEXT.__swift5_assocty: 0xd0
   __TEXT.__objc_classname: 0x5b
   __TEXT.__objc_methtype: 0x191
-  __TEXT.__unwind_info: 0x49a0
-  __TEXT.__eh_frame: 0xecc4
-  __DATA_CONST.__auth_got: 0x1648
-  __DATA_CONST.__got: 0xb88
-  __DATA_CONST.__auth_ptr: 0x910
+  __TEXT.__unwind_info: 0x4a40
+  __TEXT.__eh_frame: 0xeedc
+  __DATA_CONST.__auth_got: 0x1668
+  __DATA_CONST.__got: 0xba8
+  __DATA_CONST.__auth_ptr: 0x920
   __DATA_CONST.__const: 0x2780
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA.__objc_const: 0x2a50
+  __DATA.__objc_const: 0x2ab0
   __DATA.__objc_selrefs: 0x138
   __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x4b68
-  __DATA.__common: 0x4d0
+  __DATA.__data: 0x4be0
+  __DATA.__common: 0x4d8
   __DATA.__bss: 0x3548
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4994
-  Symbols:   1223
-  CStrings:  726
+  Functions: 5048
+  Symbols:   1230
+  CStrings:  744
 
Symbols:
+ _$s10Foundation4DateV1goiySbAC_ACtFZ
+ _$s19CollectionsInternal10OrderedSetV11descriptionSSvg
+ _$s20ModelManagerServices0A10XPCRequestO20CreateSessionRequestV016parentOfOnBehalfI3PIDSivg
+ _$s20ModelManagerServices11AssetPolicyOSQAAMc
+ _$s20ModelManagerServices14InferenceErrorO13alreadyLoadedyA2C7ContextVcACmFWC
+ _$s20ModelManagerServices14InferenceErrorO9notLoadedyA2C7ContextVcACmFWC
+ _$s20ModelManagerServices37InferenceProviderRequestConfigurationV11requestUUID10Foundation0I0Vvg
+ _$s20ModelManagerServices37InferenceProviderRequestConfigurationV24sessionLoggingIdentifier07requestiJ016assetIdentifiers0K4UUID0hN013onBehalfOfPID06parentq2OnpqR010auditToken0U10SessionUID07useCaseJ00l6BundleJ00K8PriorityACSS_SSShySSG10Foundation0N0VASS2iAA05AuditV0VSgs6UInt32VS2SAA0F8PriorityOtcfC
+ _$s20ModelManagerServices9AssetInfoV10identifier4cost7version20hasForegroundSession20timeLastRequestEndedACSS_AA0D4CostVSSSb10Foundation4DateVtcfC
+ _$s20ModelManagerServices9StateDumpV10assertions13currentPolicy6assets8sessions8requests15runningRequests18inferenceProviders16disabledUseCases6trials6budgetACSayAA9AssertionC9DaemonRepVG_AA0H0VShyAC05AssetD0VGShyAC07SessionD0VGShyAC07RequestD0VGShyAA14UUIDIdentifierVyAA07OneShotZ0CGGShyAC017InferenceProviderD0VGShySSGSDySSATGs6UInt64VtcfC
+ _objc_retain_x24
- _$s10Foundation4DateV20timeIntervalSinceNowSdvg
- _$s20ModelManagerServices37InferenceProviderRequestConfigurationV24sessionLoggingIdentifier07requestiJ016assetIdentifiers0K4UUID0hN013onBehalfOfPID10auditToken0S10SessionUID07useCaseJ00l6BundleJ00K8PriorityACSS_SSShySSG10Foundation0N0VARSiAA05AuditT0VSgs6UInt32VS2SAA0fZ0OtcfC
- _$s20ModelManagerServices9AssetInfoV10identifier4cost7version20hasForegroundSessionACSS_AA0D4CostVSSSbtcfC
- _$s20ModelManagerServices9StateDumpV10assertions13currentPolicy6assets8sessions8requests18inferenceProviders16disabledUseCases6trials6budgetACSayAA9AssertionC9DaemonRepVG_AA0H0VShyAC05AssetD0VGShyAC07SessionD0VGShyAC07RequestD0VGShyAC017InferenceProviderD0VGShySSGSDySSASGs6UInt64VtcfC
CStrings:
+ "Additional assets need transitioning, next task wake in %!f(MISSING) seconds"
+ "Asset %!s(MISSING) already loaded into %!s(MISSING)"
+ "Asset %!s(MISSING) already unloaded from %!s(MISSING)"
+ "Asset %!s(MISSING) received handleConnectionTermination"
+ "Inference Provider extension %!s(MISSING) calling %!l(MISSING)d terminationHandlers"
+ "Inference Provider extension %!s(MISSING) finished calling terminationHandlers"
+ "InferenceProvider Extension Terminated"
+ "InferenceProvider await endOfStream (%!s(MISSING)) finished"
+ "InferenceProvider awaiting endOfStream (%!s(MISSING)) on %!s(MISSING)"
+ "InferenceProvider requestInference (%!s(MISSING)) executing on %!s(MISSING)"
+ "InferenceProvider requestInference (%!s(MISSING)) finished"
+ "ModelCatalog asset update stream ended unexpectedly"
+ "Prewarm not allowed by current policy"
+ "Process State Update"
+ "Purge Inactive Assets"
+ "Remaining purge candidates %!s(MISSING) generated task wake times in the past.  Ending inactive asset purge task"
+ "Remaining transition candidates %!s(MISSING) generated task wake times in the past.  Ending asset transition task"
+ "Transition Assets"
+ "Trial Update"
+ "Unload Assets For Version Change"
+ "We can't acquire assets for foreground group but there are no nonzero cost active groups"
+ "While unloading assets for pending version change: remaining candidates %!s(MISSING) generated task wake times in the past.  Ending task"
+ "addSession(supportedAssetBundleIdentifiers:useCaseIdentifier:onBehalfOfPID:parentOfOnBehalfOfPID:auditToken:createdByPID:containsSensitiveData:loggingIdentifier:id:alreadyLockedInferenceProvider:)"
+ "assetUpdateWatcher"
+ "lastPid"
+ "parentOfOnBehalfOfPID"
+ "requestInference (%!s(MISSING)) called for exited extension"
+ "requestInference (%!s(MISSING)) failed with XPC Error %!@(MISSING), checking exit status"
+ "terminatedExtensionError found process %!d(MISSING) jettisoned"
+ "terminatedExtensionError returning abnormal extension termination with %!@(MISSING) for %!d(MISSING)"
+ "unloadAsset for %!s(MISSING) failed to move all dependents to dynamic or load, giving up after multiple attmpts"
+ "unloadAsset for %!s(MISSING) failed to unload all dependents, giving up after multiple attmpts"
+ "unloadIfNeededToMakeRoom couldn't unload enough assets to get under budget. Lowest was %!l(MISSING)luKB."
- "Additional assets need to be transitioned, next task wake in %!f(MISSING) seconds"
- "Asset update stream ended unexpectedly"
- "Calling back streaming request hit error %!@(MISSING)"
- "InferenceProvider await endOfStream finished"
- "InferenceProvider awaiting endOfStream on %!s(MISSING)"
- "InferenceProvider requestInference executing on %!s(MISSING)"
- "InferenceProvider requestInference finished"
- "InferenceProvider requestInference finished on %!s(MISSING)"
- "We can't acquire assets for foreground group but there are no active groups"
- "acquireAssetsIfAllowedByPolicy got past minCostAfterLoading, but couldn't unload enough assets to get under budget. Lowest was %!l(MISSING)luKB."
- "addSession(supportedAssetBundleIdentifiers:useCaseIdentifier:onBehalfOfPID:auditToken:createdByPID:containsSensitiveData:loggingIdentifier:id:alreadyLockedInferenceProvider:)"
- "requestInference called for exited extension"
- "requestInference failed with XPC Error %!@(MISSING), checking exit status"
- "terminatedExtensionError found process jettisoned"
- "terminatedExtensionError returning abnormal extension termination with %!@(MISSING)"

```
