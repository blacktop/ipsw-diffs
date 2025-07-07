## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-488.0.0.0.0
-  __TEXT.__text: 0xa3960
+490.2.0.0.0
+  __TEXT.__text: 0xa49dc
   __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x7b94
+  __TEXT.__objc_methlist: 0x7bcc
   __TEXT.__const: 0x3da
-  __TEXT.__gcc_except_tab: 0x2f60
-  __TEXT.__cstring: 0xdfdb
-  __TEXT.__oslogstring: 0x351d
+  __TEXT.__gcc_except_tab: 0x3084
+  __TEXT.__cstring: 0xe25b
+  __TEXT.__oslogstring: 0x3544
   __TEXT.__dlopen_cstrs: 0x7a7
   __TEXT.__swift5_typeref: 0x46
   __TEXT.__swift5_capture: 0x30

   __TEXT.__swift5_reflstr: 0xb
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x24e8
+  __TEXT.__unwind_info: 0x2540
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x83f
-  __TEXT.__objc_methname: 0x13be3
+  __TEXT.__objc_methname: 0x13c86
   __TEXT.__objc_methtype: 0x2183
-  __TEXT.__objc_stubs: 0xea80
+  __TEXT.__objc_stubs: 0xeb00
   __DATA_CONST.__got: 0x648
-  __DATA_CONST.__const: 0x3370
+  __DATA_CONST.__const: 0x33c0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4850
+  __DATA_CONST.__objc_selrefs: 0x4880
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x430
   __AUTH_CONST.__auth_got: 0x890
-  __AUTH_CONST.__const: 0xd38
-  __AUTH_CONST.__cfstring: 0x8ba0
+  __AUTH_CONST.__const: 0xd58
+  __AUTH_CONST.__cfstring: 0x8d00
   __AUTH_CONST.__objc_const: 0xa3b8
   __AUTH_CONST.__objc_intobj: 0xa98
   __AUTH_CONST.__objc_arrayobj: 0x1f8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C1AE54B8-C0A9-3675-8BBE-7429AB8CABFE
-  Functions: 3470
-  Symbols:   11210
-  CStrings:  6731
+  UUID: A2C01250-AC3A-3F5F-8228-5DB80811C6E1
+  Functions: 3480
+  Symbols:   11244
+  CStrings:  6765
 
Symbols:
+ -[AXHAServer unregisterAvailableDevicesListener:]
+ -[AXHAServer unregisterPropertyUpdateListener:]
+ -[HUHearingSettings _convertHACCModule:]
+ -[HUHearingSettings _convertHACCPreference:]
+ -[HUHearingSettings _convertLuckHACCModuleRawValue:]
+ _HACCModuleCSSoundsPreference
+ _HACCModuleLiveListenPreference
+ _HACCModulePMETogglePreference
+ _HACCModuleSSLPreference
+ _HACCModuleStatusPreference
+ _HUIModuleHeadphoneLevelPreference
+ ___43-[AXHAServer comfortSoundsAssetsDidUpdate:]_block_invoke.172
+ ___46-[HUHearingSettings hearingControlCenterOrder]_block_invoke
+ ___46-[HUHearingSettings hearingControlCenterOrder]_block_invoke_2
+ ___50-[HUHearingSettings setHearingControlCenterOrder:]_block_invoke
+ ___63-[HUAccessoryManager getCurrentRouteInformationWithCompletion:]_block_invoke.cold.1
+ ___93-[HUComfortSoundsAssetManager assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.26
+ ___block_descriptor_32_e24_B32?0"AXAsset"8Q16^B24l
+ ___block_literal_global.29
+ _objc_msgSend$_convertHACCModule:
+ _objc_msgSend$_convertHACCPreference:
+ _objc_msgSend$_convertLuckHACCModuleRawValue:
+ _objc_msgSend$arrayWithCapacity:
- ___43-[AXHAServer comfortSoundsAssetsDidUpdate:]_block_invoke.166
CStrings:
+ "-[AXHAServer unregisterAvailableDevicesListener:]"
+ "-[AXHAServer unregisterPropertyUpdateListener:]"
+ "-[HUComfortSoundsAssetManager assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke"
+ "-[HUHearingSettings hearingControlCenterOrder]"
+ "-[HUHearingSettings setHearingControlCenterOrder:]"
+ "AssetType"
+ "Couldn't get current route information"
+ "Error during unarchiving: %@"
+ "HACCModuleCSSoundsPreference"
+ "HACCModuleLiveListenPreference"
+ "HACCModulePMETogglePreference"
+ "HACCModuleSSLPreference"
+ "HACCModuleStatusPreference"
+ "HUIModuleHeadphoneLevelPreference"
+ "T@\"NSArray\",&,N"
+ "The asset %@ property is %@"
+ "Unregister from available devices listener: %@"
+ "Unregister from property update listener: %@"
+ "Updated for audio route change: LL stream selected %@, HA stream available %@"
+ "_convertHACCModule:"
+ "_convertHACCPreference:"
+ "_convertLuckHACCModuleRawValue:"
+ "arrayWithCapacity:"
+ "unregisterAvailableDevicesListener:"
+ "unregisterPropertyUpdateListener:"
- "T@\"NSArray\",&,D,N"
- "Updated for audio route change: LL stream selected %@, HA stream avaialble %@"

```
