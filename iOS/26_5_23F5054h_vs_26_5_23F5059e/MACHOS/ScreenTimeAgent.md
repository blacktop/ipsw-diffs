## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

-605.5.9.0.0
-  __TEXT.__text: 0x13412c
-  __TEXT.__auth_stubs: 0x23f0
-  __TEXT.__objc_stubs: 0x12ee0
-  __TEXT.__objc_methlist: 0xa2fc
-  __TEXT.__const: 0x5098
-  __TEXT.__gcc_except_tab: 0x22f0
-  __TEXT.__cstring: 0xac2e
-  __TEXT.__oslogstring: 0x14860
-  __TEXT.__objc_methname: 0x1dc27
+605.5.10.0.0
+  __TEXT.__text: 0x135538
+  __TEXT.__auth_stubs: 0x2440
+  __TEXT.__objc_stubs: 0x12f40
+  __TEXT.__objc_methlist: 0xa30c
+  __TEXT.__const: 0x50a8
+  __TEXT.__gcc_except_tab: 0x22f4
+  __TEXT.__cstring: 0xac9e
+  __TEXT.__oslogstring: 0x149c0
+  __TEXT.__objc_methname: 0x1dca7
   __TEXT.__objc_classname: 0x2d02
   __TEXT.__objc_methtype: 0x5e22
   __TEXT.__constg_swiftt: 0x35f0
   __TEXT.__swift5_typeref: 0x2d52
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0x2109
-  __TEXT.__swift5_fieldmd: 0x1640
+  __TEXT.__swift5_reflstr: 0x2129
+  __TEXT.__swift5_fieldmd: 0x164c
   __TEXT.__swift5_assocty: 0x2e8
   __TEXT.__swift5_proto: 0x288
   __TEXT.__swift5_types: 0x190
   __TEXT.__swift5_capture: 0x2200
   __TEXT.__swift_as_entry: 0x264
-  __TEXT.__swift_as_ret: 0x198
+  __TEXT.__swift_as_ret: 0x19c
   __TEXT.__swift5_protos: 0xc8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x4840
-  __TEXT.__eh_frame: 0x61d0
-  __DATA_CONST.__auth_got: 0x1208
-  __DATA_CONST.__got: 0x13a0
+  __TEXT.__unwind_info: 0x4858
+  __TEXT.__eh_frame: 0x6240
+  __DATA_CONST.__auth_got: 0x1230
+  __DATA_CONST.__got: 0x13a8
   __DATA_CONST.__auth_ptr: 0x6b8
-  __DATA_CONST.__const: 0x9cb0
-  __DATA_CONST.__cfstring: 0x4ca0
+  __DATA_CONST.__const: 0x9cb8
+  __DATA_CONST.__cfstring: 0x4ce0
   __DATA_CONST.__objc_classlist: 0x6a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x510

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x1ecc0
-  __DATA.__objc_selrefs: 0x5830
+  __DATA.__objc_const: 0x1ece0
+  __DATA.__objc_selrefs: 0x5848
   __DATA.__objc_ivar: 0x814
   __DATA.__objc_data: 0x4de8
-  __DATA.__data: 0x7548
+  __DATA.__data: 0x7558
   __DATA.__bss: 0x37c0
   __DATA.__common: 0xe8
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 29605940-A0AF-3A4E-BCEB-2FB45C79A4AA
-  Functions: 6270
-  Symbols:   1354
-  CStrings:  8096
+  UUID: 1F1F0942-401B-398F-A317-B3BCABAA6963
+  Functions: 6277
+  Symbols:   1360
+  CStrings:  8109
 
Symbols:
+ _$s10Foundation12NotificationV4nameSo18NSNotificationNameavg
+ _$s15ScreenTimeSwift21STExpressIntroductionO4UserO6remoteyAESi_tcAEmFWC
+ _$s15ScreenTimeSwift21STExpressIntroductionO8InternalO16DeferredSettingsV16settingsDefaultsAC0hJ0Vvg
+ _$s15ScreenTimeSwift21STExpressIntroductionO8InternalO16DeferredSettingsV4userAC4UserOvg
+ _$s15ScreenTimeSwift21STExpressIntroductionO8InternalO16DeferredSettingsVMa
+ _$s15ScreenTimeSwift21STExpressIntroductionO8InternalO16DeferredSettingsVMn
+ _$s15ScreenTimeSwift21STExpressIntroductionO8InternalO26SettingsDefaultsDataSourceP4loadAE08DeferredG0VSgyYaKFTj
+ _$s15ScreenTimeSwift21STExpressIntroductionO8InternalO26SettingsDefaultsDataSourceP4loadAE08DeferredG0VSgyYaKFTjTu
+ _$s7Combine10PublishersO9MergeManyV5merge4withAEy_xGx_tF
- _$s15ScreenTimeSwift21STExpressIntroductionO16SettingsDefaultsVMn
- _$s15ScreenTimeSwift21STExpressIntroductionO8InternalO26SettingsDefaultsDataSourceP4loadAC0gH0VSgyYaKFTj
- _$s15ScreenTimeSwift21STExpressIntroductionO8InternalO26SettingsDefaultsDataSourceP4loadAC0gH0VSgyYaKFTjTu
CStrings:
+ "(none)"
+ "Done saving settings defaults for user %{private}s"
+ "Failed to create pending passcode activity payload: %{public}@"
+ "Failed to save passcode activity sent date: %{public}@"
+ "Found pending deferred settings for remote user; eligible for merge"
+ "Found saved settings defaults: %{public}s for user: %{private}s"
+ "Received notification: %{public}s"
+ "STFamilyDidUpdateNotification"
+ "Saving settings defaults for user %{private}s"
+ "Sending pending passcode activity after reachability change (lastUse: %{public}@, lastSent: %{public}@)"
+ "_sendPendingPasscodeActivityIfNeeded"
+ "com.apple.ScreenTimeAgent.familyOrganizationController.sendPendingPasscodeActivity"
+ "lastPasscodeActivityNotificationSentDate"
+ "setLastPasscodeActivityNotificationSentDate:"
+ "settingsDefaultsDataSource"
- "Done saving settings defaults for local user"
- "Found saved settings defaults: %{public}s"
- "Received notification"
- "Saving settings defaults for local user"

```
