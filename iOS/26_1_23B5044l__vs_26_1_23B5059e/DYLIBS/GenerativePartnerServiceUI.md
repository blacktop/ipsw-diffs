## GenerativePartnerServiceUI

> `/System/Library/PrivateFrameworks/GenerativePartnerServiceUI.framework/GenerativePartnerServiceUI`

```diff

-209.12.0.0.0
-  __TEXT.__text: 0x882c4
-  __TEXT.__auth_stubs: 0x2a40
+209.18.2.0.0
+  __TEXT.__text: 0x8cfc0
+  __TEXT.__auth_stubs: 0x2ac0
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0x3dc
-  __TEXT.__const: 0x3c94
-  __TEXT.__cstring: 0x39a2
-  __TEXT.__swift5_typeref: 0x8a2c
-  __TEXT.__oslogstring: 0x1f2d
-  __TEXT.__swift5_capture: 0x914
-  __TEXT.__constg_swiftt: 0x196c
-  __TEXT.__swift5_reflstr: 0x1376
+  __TEXT.__const: 0x3d94
+  __TEXT.__cstring: 0x3b72
+  __TEXT.__swift5_typeref: 0x8e64
+  __TEXT.__oslogstring: 0x203d
+  __TEXT.__swift5_capture: 0x940
+  __TEXT.__constg_swiftt: 0x19d8
+  __TEXT.__swift5_reflstr: 0x13c6
   __TEXT.__swift5_assocty: 0x2c8
-  __TEXT.__swift5_fieldmd: 0x11c4
+  __TEXT.__swift5_fieldmd: 0x1214
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_proto: 0x1f8
-  __TEXT.__swift5_types: 0x144
+  __TEXT.__swift5_proto: 0x1fc
+  __TEXT.__swift5_types: 0x14c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift_as_entry: 0xf8
+  __TEXT.__swift_as_entry: 0xfc
   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__unwind_info: 0x2180
-  __TEXT.__eh_frame: 0x31b0
+  __TEXT.__unwind_info: 0x2210
+  __TEXT.__eh_frame: 0x3348
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methname: 0xe1f
   __TEXT.__objc_methtype: 0x1af
-  __DATA_CONST.__got: 0xa18
+  __DATA_CONST.__got: 0xa38
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x570
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1520
-  __AUTH_CONST.__const: 0x3448
-  __AUTH_CONST.__objc_const: 0x11c8
-  __AUTH.__objc_data: 0x818
+  __AUTH_CONST.__auth_got: 0x1560
+  __AUTH_CONST.__const: 0x35c8
+  __AUTH_CONST.__objc_const: 0x1208
+  __AUTH.__objc_data: 0x848
   __AUTH.__data: 0x1108
-  __DATA.__data: 0x19ec
+  __DATA.__data: 0x1a3c
   __DATA.__bss: 0x3638
-  __DATA.__common: 0x128
+  __DATA.__common: 0x130
   __DATA_DIRTY.__objc_data: 0xe0
-  __DATA_DIRTY.__data: 0x840
+  __DATA_DIRTY.__data: 0x848
   __DATA_DIRTY.__bss: 0x780
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation
+  - /System/Library/PrivateFrameworks/GenerativePartnerService.framework/GenerativePartnerService
   - /System/Library/PrivateFrameworks/JetEngine.framework/JetEngine
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog

   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 16834A2D-1054-39AA-A812-4A1EF503820A
-  Functions: 3404
-  Symbols:   255
-  CStrings:  666
+  UUID: 0989A098-A873-3037-B682-985DFFF15AE6
+  Functions: 3472
+  Symbols:   256
+  CStrings:  679
 
Symbols:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_runtimeSupportsNoncopyableTypes
- _objc_retain_x9
- _swift_unknownObjectRetain_n
CStrings:
+ " isn’t available in this region."
+ "%{public}s - will perform reloadSpecifiers(), invocationSource: %s"
+ "%{public}s: Presenting regional unavailability alert, reason = useCaseDoesNotAllowCurrentIPCountryCode"
+ "%{public}s: previousPartnerID: %{public}s, currentPartnerID: %{public}s"
+ "Emitted analytics event for %{public}s with %s"
+ "LLM with id \"%{public}s\" unavailability status changed to: unavailable = %{bool,public}d"
+ "availabilityDidChange(for:availability:)"
+ "handleManageSubscriptionAction(from:)"
+ "init(parentController:settings:)"
+ "intendedDefaultLLM is nil"
+ "parentController is nil when attempting to present onboarding sheet"
+ "previousAvailability"
+ "previousPartnerID"
+ "reasons: %{public}s"
+ "receivedActiveProviderUpdate()"
+ "receivedUseConfirmationPromptsUpdate()"
+ "sharedOnChangeListeners()"
+ "showOnboardingSelectionSheet(preselectedPartnerID:)"
+ "updateVisibility(needsReload:debugInvocationSourceString:)"
- "%{public}s.%{public}s GM restricted with info: %{public}s"
- "%{public}s.%{public}s GM unavailable with info: %{public}s"
- "Emitted analytics event for %s with %s"
- "LLM with id: \"%{public}s\" unavailable; status changed to: %{bool,public}d"
- "SettingsRestrictionsManager"
- "defaultLLM is nil"

```
