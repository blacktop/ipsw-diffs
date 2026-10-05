## CTMessagingSettings

> `/System/Library/PrivateFrameworks/CTMessagingSettings.framework/CTMessagingSettings`

```diff

-13496.3.0.0.0
-  __TEXT.__text: 0x24838
+13498.0.0.0.0
+  __TEXT.__text: 0x29fdc
   __TEXT.__objc_methlist: 0x3f4
-  __TEXT.__const: 0xe94
-  __TEXT.__cstring: 0x1071
-  __TEXT.__swift5_typeref: 0x1666
-  __TEXT.__swift5_capture: 0x318
-  __TEXT.__oslogstring: 0x44b
+  __TEXT.__const: 0xee4
+  __TEXT.__cstring: 0x11b1
+  __TEXT.__swift5_typeref: 0x170e
+  __TEXT.__swift5_capture: 0x328
+  __TEXT.__oslogstring: 0x114b
   __TEXT.__constg_swiftt: 0x464
   __TEXT.__swift5_reflstr: 0x316
   __TEXT.__swift5_fieldmd: 0x2ec

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x24
-  __TEXT.__unwind_info: 0x878
-  __TEXT.__eh_frame: 0x4c0
+  __TEXT.__unwind_info: 0x8c8
+  __TEXT.__eh_frame: 0x530
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x468
+  __DATA_CONST.__objc_selrefs: 0x480
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__got: 0x300
-  __AUTH_CONST.__const: 0x9b0
+  __AUTH_CONST.__const: 0x9d8
   __AUTH_CONST.__objc_const: 0x608
-  __AUTH_CONST.__auth_got: 0x8f0
+  __AUTH_CONST.__auth_got: 0x8e0
   __AUTH.__objc_data: 0x3f8
-  __AUTH.__data: 0x318
-  __DATA.__data: 0x7b0
+  __AUTH.__data: 0x320
+  __DATA.__data: 0x7d0
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 575
-  Symbols:   467
-  CStrings:  106
+  Functions: 595
+  Symbols:   469
+  CStrings:  152
 
Symbols:
+ ___swift_closure_destructor.76Tm
+ ___swift_destroy_boxed_opaque_existential_0
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA5GroupVyAA7SectionVyAA9EmptyViewVACyAA6ToggleVyAA4TextVGAA32_EnvironmentKeyTransformModifierVySbGGAMGSgGAA017_AppearanceActionN0VGAA0H0HPAuaYHPAtaYHpAsaYHPAiaYHPyHC_AraYHPAnaYHPyHC_AqA0hN0HPyHCHCAmaYHPyHCHC_HC_HC_AwaZHPyHCHC
+ _symbolic _____y_____4slot_Sb12isRCSEnabledSb0B11DisplayabletG s23_ContiguousArrayStorageC So18CTSubscriptionSlotV
+ _symbolic _____y_____y__________y_____y_____G_____ySbGGAFGSgG 7SwiftUI5GroupV AA7SectionV AA9EmptyViewV AA15ModifiedContentV AA6ToggleV AA4TextV AA32_EnvironmentKeyTransformModifierV
+ _symbolic _____y_____y_____y_____AAy_____y_____G_____ySbGGAFGSgG_____G 7SwiftUI15ModifiedContentV AA5GroupV AA7SectionV AA9EmptyViewV AA6ToggleV AA4TextV AA32_EnvironmentKeyTransformModifierV AA017_AppearanceActionN0V
- ___swift_closure_destructor.73Tm
- _get_witness_table 7SwiftUI7SectionVyAA9EmptyViewVAA15ModifiedContentVyAA6ToggleVyAA4TextVGAA32_EnvironmentKeyTransformModifierVySbGGAKGSgAA0E0HpAqaSHPAeaSHPyHC_ApaSHPAlaSHPyHC_AoA0eM0HPyHCHCAkaSHPyHCHC_HC
- _swift_retain_x22
- _swift_retain_x26
CStrings:
+ "%{public}s failed for slot %{public}ld: %{public}@"
+ ", cellularDataRequirement="
+ ", disablementReason="
+ ", enabledByDefault="
+ ", quickSwitchRole="
+ ", supportsComposingIndicator="
+ ", userPreferenceForSwitch="
+ "Active subscription changing for slot %{public}ld: slotDropped=%{bool,public}d, labelChanged=%{bool,public}d, phoneNumberChanged=%{bool,public}d"
+ "Active subscription count changing: %{public}ld -> %{public}ld, slots [%{public}s] -> [%{public}s]"
+ "Cannot reload RCS specifiers: userInfo is not a CTMessagingSettingsProvider"
+ "Could not notify observers of MMS enabled change: no Darwin notify center"
+ "Creating MMS specifier as a link pane for %{public}ld subscriptions, slots: %{public}s"
+ "Creating MMS specifier as a single switch for slot %{public}ld"
+ "Creating RCS specifier as a link pane for %{public}ld subscription(s)"
+ "Dismissing RCS pane: no displayable content. partiallyActiveSimSupported=%{bool,public}d, subscription slots=[%{public}s]"
+ "Dropping MMS enabled write for key %{public}s: could not open %{public}s defaults suite"
+ "Dropping MMS enabled=%{bool,public}d write: specifier userInfo is not a CTXPCContextInfo"
+ "First RCS system configuration observed for slot %{public}ld: operationStatus=[%{public}s], encryption=[%{public}s], business=[%{public}s]"
+ "MMS default disabled for slot %{public}ld: carrier bundle MMS value is not a dictionary"
+ "MMS default disabled for slot %{public}ld: no MMS key in carrier bundle"
+ "MMS default enabled for slot %{public}ld: carrier bundle has no MMSDefaultEnabled key"
+ "MMS default for slot %{public}ld from carrier bundle: %{bool,public}d"
+ "MMS pane loaded"
+ "MMS pane title not set: specifier userInfo is not a CTMessagingSettingsProvider"
+ "MMS pane will be blank: hosting controller has no view"
+ "MMS pane will be blank: specifier userInfo is not a CTMessagingSettingsProvider"
+ "Not creating MMS specifier: no MMS-capable subscriptions"
+ "Not creating RCS specifier: RCSOnPartiallyActiveSim is enabled and no subscription is displayable"
+ "Not creating RCS specifier: no RCS-capable subscriptions"
+ "RCS business messages switch: displayed=%{bool,public}d, enabled=%{bool,public}d, interactive=%{bool,public}d"
+ "RCS business messaging capabilities changing for slot %{public}ld: [%{public}s] -> [%{public}s]"
+ "RCS enabled changing for slot %{public}ld: %{bool,public}d -> %{bool,public}d"
+ "RCS encryption capabilities changing for slot %{public}ld: [%{public}s] -> [%{public}s]"
+ "RCS encryption switch: displayed=%{bool,public}d, enabled=%{bool,public}d, interactive=%{bool,public}d"
+ "RCS messaging capabilities changing for slot %{public}ld: [%{public}s] -> [%{public}s]"
+ "RCS operation status changing for slot %{public}ld: [%{public}s] -> [%{public}s]"
+ "RCS pane loaded"
+ "RCS pane rendered %{public}ld toggle(s) (multi-subscription layout) for slots [%{public}s], from %{public}ld RCS subscription(s)"
+ "RCS pane rendered 1 toggle (single-subscription layout) for slot %{public}ld"
+ "RCS pane title not set: specifier userInfo is not a CTMessagingSettingsProvider"
+ "RCS pane will be blank: hosting controller has no view"
+ "RCS pane will be blank: specifier userInfo is not a CTMessagingSettingsProvider"
+ "RCS specifier displayability for slot %{public}ld: rcsEnabled=%{bool,public}d, displayable=%{bool,public}d"
+ "Reloading MMS specifiers"
+ "Reloading RCS specifiers"
+ "Reporting MMS as disabled: specifier userInfo is not a CTXPCContextInfo"
+ "Setting MMS enabled: %{bool,public}d for key: %{public}s, slot: %{public}ld"
+ "Setting RCS business messages enabled: %{bool,public}d"
+ "Setting RCS enabled: %{bool,public}d for slot: %{public}ld"
+ "Setting RCS encryption enabled: %{bool,public}d"
+ "disableBusinessMessaging"
+ "enableBusinessMessaging"
+ "notificationDisplay="
+ "registrationState="
+ "setLazuliEncryption(%{bool,public}d) failed for slot %{public}ld: %{public}@"
- "Active contexts have changed to: %@"
- "RCS business messaging capabilities have changed"
- "RCS enabled changing %{bool}d -> %{bool}d"
- "RCS encryption capabilities have changed"
- "RCS messaging capabilities have changed"
- "RCS operation status has changed"
- "RCS system configuration has changed to: %s"
- "Setting MMS enabled: %{bool}d for key: %s"
- "Setting RCS enabled: %{bool}d for: %@"
```
