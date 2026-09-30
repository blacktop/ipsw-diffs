## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-738.1.0.0.0
-  __TEXT.__text: 0x53f4c
+740.1.0.0.0
+  __TEXT.__text: 0x544ac
   __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x59ec
-  __TEXT.__const: 0x40a
-  __TEXT.__cstring: 0x5251
-  __TEXT.__oslogstring: 0x5cbd
+  __TEXT.__objc_methlist: 0x5a3c
+  __TEXT.__const: 0x42a
+  __TEXT.__cstring: 0x52a1
+  __TEXT.__oslogstring: 0x5e9f
   __TEXT.__gcc_except_tab: 0xa44
   __TEXT.__ustring: 0x24
   __TEXT.__dlopen_cstrs: 0x15e

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1760
-  __TEXT.__objc_classname: 0xa96
-  __TEXT.__objc_methname: 0xfb78
-  __TEXT.__objc_methtype: 0x2306
-  __TEXT.__objc_stubs: 0x8fc0
+  __TEXT.__unwind_info: 0x17e0
+  __TEXT.__objc_classname: 0xab6
+  __TEXT.__objc_methname: 0xfc53
+  __TEXT.__objc_methtype: 0x22f1
+  __TEXT.__objc_stubs: 0x8fe0
   __DATA_CONST.__got: 0x760
   __DATA_CONST.__const: 0x1e70
-  __DATA_CONST.__objc_classlist: 0x228
+  __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32a8
+  __DATA_CONST.__objc_selrefs: 0x32c8
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x1c8
+  __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x698
   __AUTH_CONST.__const: 0x1740
-  __AUTH_CONST.__cfstring: 0x55a0
-  __AUTH_CONST.__objc_const: 0xe868
+  __AUTH_CONST.__cfstring: 0x55e0
+  __AUTH_CONST.__objc_const: 0xe938
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0xf20
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH.__objc_data: 0xf70
   __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0x6c0
+  __DATA.__objc_ivar: 0x6c4
   __DATA.__data: 0x1060
   __DATA.__bss: 0x520
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B975C691-5A5B-37C7-82E7-467FB1FDC7D0
-  Functions: 2603
-  Symbols:   8754
-  CStrings:  4805
+  UUID: 769A30D6-0144-3919-BDF2-30EFECBF20D5
+  Functions: 2612
+  Symbols:   8783
+  CStrings:  4818
 
Symbols:
+ -[CRCarPlayLiveActivitiesDenylist .cxx_destruct]
+ -[CRCarPlayLiveActivitiesDenylist _updateDenyListFromPreferences]
+ -[CRCarPlayLiveActivitiesDenylist containsBundleIdentifier:]
+ -[CRCarPlayLiveActivitiesDenylist denyListBundleIdentifiersSet]
+ -[CRCarPlayLiveActivitiesDenylist handleLiveActivitiesDenylistChangedNotification:]
+ -[CRCarPlayLiveActivitiesDenylist init]
+ -[CRCarPlayLiveActivitiesDenylist setDenyListBundleIdentifiers:]
+ -[CRCarPlayLiveActivitiesDenylist setDenyListBundleIdentifiersSet:]
+ _CRCarPlayLiveActivitiesDenylistPreferenceKey
+ _CRMinViewAreaPixelSize
+ _CRPointScaleWithSize
+ _OBJC_CLASS_$_CRCarPlayLiveActivitiesDenylist
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_IVAR_$_CRCarPlayLiveActivitiesDenylist._denyListBundleIdentifiersSet
+ _OBJC_METACLASS_$_CRCarPlayLiveActivitiesDenylist
+ __OBJC_$_INSTANCE_METHODS_CRCarPlayLiveActivitiesDenylist
+ __OBJC_$_INSTANCE_VARIABLES_CRCarPlayLiveActivitiesDenylist
+ __OBJC_$_PROP_LIST_CRCarPlayLiveActivitiesDenylist
+ __OBJC_CLASS_RO_$_CRCarPlayLiveActivitiesDenylist
+ __OBJC_METACLASS_RO_$_CRCarPlayLiveActivitiesDenylist
+ ___83-[CRCarPlayLiveActivitiesDenylist handleLiveActivitiesDenylistChangedNotification:]_block_invoke
+ ___block_literal_global.221
+ ___block_literal_global.227
+ ___block_literal_global.232
+ ___block_literal_global.237
+ _objc_msgSend$_updateDenyListFromPreferences
+ _objc_msgSend$denyListBundleIdentifiersSet
+ _objc_msgSend$isEqualToSet:
- -[CRDisplayScaleInfo _minViewAreaPixelSize]
- -[CRDisplayScaleInfo _pointScaleForSize:]
- ___block_literal_global.218
- ___block_literal_global.229
- ___block_literal_global.234
- _objc_msgSend$_minViewAreaPixelSize
- _objc_msgSend$_pointScaleForSize:
CStrings:
+ "%{public}@ display sizes match special case. Scale zoomFactor set to %{public}@"
+ "CRCanvasSizeOverridesWithAirplayDisplays: CRDisplayScaleInfo: %{public}@"
+ "CRCarPlayLiveActivitiesDenylist"
+ "CRScaledDisplaysWithAirplayDisplays: CRDisplayScaleInfo: %{public}@"
+ "CRScaledDisplaysWithAirplayDisplays: error creating CRDisplayScaleInfo: %{public}@"
+ "Default primary display scale canvas size calculated: Result(%{public}@)=SquaredPixelSize(%{public}@) x PreferredToOriginalRatio(%{public}@) at PointScale(%{public}@); minHSize(%{public}@);minWSize(%{public}@)\nDisplayInfo: %{public}@"
+ "LiveActivitiesDenylist"
+ "Optimal[no ZoomFactor] primary display scale canvas size calculated: Result(%{public}@) = PixelSize(%{public}@) x OptimalScaleFactor(%{public}@) at PointScale(%{public}@)\nDisplayInfo: %{public}@"
+ "Optimal[with ZoomFactor] primary display scale canvas size calculated: Result(%{public}@) = SquaredPixelSize(%{public}@) x AdjustedScale(%{public}@); AdjustedScale=PreferredToOriginalScaleRatio(%{public}@)/zoomFactor(%{public}@)\nDisplayInfo: %{public}@"
+ "Physical size is zero, applying default size Result(%{public}@) = PointSize(%{public}@)/CROptimalPointsPerMM(%{public}@)"
+ "Primary display height is less than minimum: Size(%{public}@) < Min(%{public}@); Returning minimal size"
+ "Primary display width is less than minimum: Size(%{public}@) < Min(%{public}@); Returning minimal size"
+ "Secondary display size after scaling: Size(%{public}@) = SquaredPixelSize(%{public}@) x Scale(%{public}@); Scale = PreferredToOriginalScaleRatio(%{public}@)/ZoomFactor(%{public}@) at PointScale(%{public}@)"
+ "T@\"NSSet\",&,N,V_denyListBundleIdentifiersSet"
+ "Unable to parse display physical size: %{public}@"
+ "Unable to parse display pixel size: %{public}@"
+ "_denyListBundleIdentifiersSet"
+ "_updateDenyListFromPreferences"
+ "com.apple.carkit.liveactivities.denylist-changed"
+ "denyListBundleIdentifiersSet"
+ "handleLiveActivitiesDenylistChangedNotification:"
+ "isEqualToSet:"
+ "setDenyListBundleIdentifiers:"
+ "setDenyListBundleIdentifiersSet:"
+ "videoPlayback"
+ "videoPlaybackInfo"
- "%@ display sizes match special case. Scale zoomFactor set to %@"
- "CRCanvasSizeOverridesWithAirplayDisplays: CRDisplayScaleInfo: %@"
- "CRScaledDisplaysWithAirplayDisplays: CRDisplayScaleInfo: %@"
- "CRScaledDisplaysWithAirplayDisplays: error creating CRDisplayScaleInfo: %@"
- "Default primary display scale canvas size calculated: Result(%@)=SquaredPixelSize(%@) x PreferredToOriginalRatio(%@) at PointScale(%@); minHSize(%@);minWSize(%@)\nDisplayInfo: %@"
- "Optimal[no ZoomFactor] primary display scale canvas size calculated: Result(%@) = PixelSize(%@) x OptimalScaleFactor(%@) at PointScale(%@)\nDisplayInfo: %@"
- "Optimal[with ZoomFactor] primary display scale canvas size calculated: Result(%@) = SquaredPixelSize(%@) x AdjustedScale(%@); AdjustedScale=PreferredToOriginalScaleRatio(%@)/zoomFactor(%@)\nDisplayInfo: %@"
- "Primary display height is less than minimum: Size(%@) < Min(%@); Returning minimal size"
- "Primary display width is less than minimum: Size(%@) < Min(%@); Returning minimal size"
- "Q32@0:8{CGSize=dd}16"
- "Secondary display size after scaling: Size(%@) = SquaredPixelSize(%@) x Scale(%@); Scale = PreferredToOriginalScaleRatio(%@)/ZoomFactor(%@) at PointScale(%@)"
- "_minViewAreaPixelSize"
- "_pointScaleForSize:"
- "video2"
- "video2Info"

```
