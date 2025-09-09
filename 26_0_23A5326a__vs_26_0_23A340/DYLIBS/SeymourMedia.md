## SeymourMedia

> `/System/Library/PrivateFrameworks/SeymourMedia.framework/SeymourMedia`

```diff

 2026.0.6.1.2
-  __TEXT.__text: 0x118c78
-  __TEXT.__auth_stubs: 0x4900
+  __TEXT.__text: 0x11abac
+  __TEXT.__auth_stubs: 0x49d0
   __TEXT.__objc_methlist: 0x9a4
-  __TEXT.__const: 0x7bb4
+  __TEXT.__const: 0x7ba4
   __TEXT.__cstring: 0x3c2c
-  __TEXT.__constg_swiftt: 0x3468
-  __TEXT.__swift5_typeref: 0x417e
+  __TEXT.__constg_swiftt: 0x3470
+  __TEXT.__swift5_typeref: 0x4192
   __TEXT.__swift5_builtin: 0x258
   __TEXT.__swift5_reflstr: 0x2380
   __TEXT.__swift5_fieldmd: 0x28fc
   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_proto: 0x4dc
   __TEXT.__swift5_types: 0x31c
-  __TEXT.__swift5_capture: 0x39c4
-  __TEXT.__oslogstring: 0x4f93
+  __TEXT.__swift5_capture: 0x3a18
+  __TEXT.__oslogstring: 0x50c3
   __TEXT.__swift5_protos: 0xc0
   __TEXT.__swift_as_entry: 0x128
   __TEXT.__swift_as_ret: 0x118
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0x3800
-  __TEXT.__eh_frame: 0x5158
+  __TEXT.__unwind_info: 0x3850
+  __TEXT.__eh_frame: 0x5188
   __TEXT.__objc_classname: 0x1df
-  __TEXT.__objc_methname: 0x2881
+  __TEXT.__objc_methname: 0x2980
   __TEXT.__objc_methtype: 0xac8
   __TEXT.__objc_stubs: 0x4e0
-  __DATA_CONST.__got: 0x1490
+  __DATA_CONST.__got: 0x14b0
   __DATA_CONST.__const: 0x340
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd50
+  __DATA_CONST.__objc_selrefs: 0xd90
   __DATA_CONST.__objc_protorefs: 0x78
-  __AUTH_CONST.__auth_got: 0x2488
-  __AUTH_CONST.__const: 0xbd38
+  __AUTH_CONST.__auth_got: 0x24f0
+  __AUTH_CONST.__const: 0xbdc0
   __AUTH_CONST.__objc_const: 0x4048
   __AUTH.__objc_data: 0xcc8
   __AUTH.__data: 0x19b0
-  __DATA.__data: 0x1f28
+  __DATA.__data: 0x1f38
   __DATA.__bss: 0x77b0
   __DATA.__common: 0xe0
   __DATA_DIRTY.__objc_data: 0x230

   - /System/Library/PrivateFrameworks/ActivityRingsUI.framework/ActivityRingsUI
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FitnessUtilities.framework/FitnessUtilities
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/JetEngine.framework/JetEngine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ADC7331A-349C-32F4-8117-075DC9C66734
-  Functions: 5602
-  Symbols:   2602
-  CStrings:  1267
+  UUID: 8B4AAF63-8393-3AD6-A1E0-02AED0B023F4
+  Functions: 5614
+  Symbols:   2610
+  CStrings:  1280
 
Symbols:
+ _OBJC_CLASS_$_AVMediaPresentationSelector
+ _OBJC_CLASS_$_AVMediaPresentationSetting
+ _OBJC_CLASS_$_AVMediaSelectionOption
+ ___swift_memcpy4_4
+ _block_copy_helper.111
+ _block_copy_helper.122
+ _block_copy_helper.148
+ _block_copy_helper.155
+ _block_copy_helper.174
+ _block_copy_helper.181
+ _block_copy_helper.193
+ _block_descriptor.113
+ _block_descriptor.124
+ _block_descriptor.150
+ _block_descriptor.157
+ _block_descriptor.176
+ _block_descriptor.183
+ _block_descriptor.195
+ _block_destroy_helper.112
+ _block_destroy_helper.123
+ _block_destroy_helper.149
+ _block_destroy_helper.156
+ _block_destroy_helper.175
+ _block_destroy_helper.182
+ _block_destroy_helper.194
+ _objectdestroy.129Tm
+ _objectdestroy.146Tm
+ _objectdestroy.57Tm
+ _objectdestroy.61Tm
+ _symbolic _____ 11SeymourCore19AudioFocusSelectionO
+ _symbolic _____ 11SeymourCore23AudioLanguagePreferenceV
+ _symbolic _____Sg 11SeymourCore23AudioLanguagePreferenceV
- _block_copy_helper.108
- _block_copy_helper.119
- _block_copy_helper.145
- _block_copy_helper.152
- _block_copy_helper.171
- _block_copy_helper.178
- _block_copy_helper.190
- _block_descriptor.110
- _block_descriptor.121
- _block_descriptor.147
- _block_descriptor.154
- _block_descriptor.173
- _block_descriptor.180
- _block_descriptor.192
- _block_destroy_helper.109
- _block_destroy_helper.120
- _block_destroy_helper.146
- _block_destroy_helper.153
- _block_destroy_helper.172
- _block_destroy_helper.179
- _block_destroy_helper.191
- _objectdestroy.126Tm
- _objectdestroy.143Tm
- _objectdestroy.58Tm
CStrings:
+ "AVAssetCache has mediaSelectionOptions: %s"
+ "No option customMediaSelectionScheme for group: %@"
+ "No option mediaPresentationSetting for audioFocusSelection: %s"
+ "Preferred language %s is not available in AVAssetCache, selecting %s instead."
+ "assetCache"
+ "mediaCharacteristic"
+ "mediaPresentationLanguagesForMediaSelectionGroup:"
+ "mediaSelectionOptionsInMediaSelectionGroup:"
+ "selectMediaPresentationLanguage with: %s"
+ "selectMediaPresentationLanguage:forMediaSelectionGroup:"
+ "selectMediaPresentationSetting:forMediaSelectionGroup:"
+ "selectors"
+ "settings"

```
