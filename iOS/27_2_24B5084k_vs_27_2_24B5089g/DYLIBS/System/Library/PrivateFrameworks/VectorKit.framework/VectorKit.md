## VectorKit

> `/System/Library/PrivateFrameworks/VectorKit.framework/VectorKit`

```diff

-2043.31.6.17.7
-  __TEXT.__text: 0x11f8130
+2044.31.6.17.11
+  __TEXT.__text: 0x11f8254
   __TEXT.__objc_methlist: 0x110d4
-  __TEXT.__const: 0x792e8
-  __TEXT.__gcc_except_tab: 0x76148
-  __TEXT.__oslogstring: 0x1155f
+  __TEXT.__const: 0x79318
+  __TEXT.__gcc_except_tab: 0x7616c
+  __TEXT.__oslogstring: 0x11543
   __TEXT.__cstring: 0x9af18
   __TEXT.__ustring: 0xf8
   __TEXT.__unwind_info: 0x3a328

   __DATA.__data: 0x328b8
   __DATA_DIRTY.__objc_data: 0x1590
   __DATA_DIRTY.__data: 0x1c
-  __DATA_DIRTY.__bss: 0x59078
+  __DATA_DIRTY.__bss: 0x590d8
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
Functions:
~ __ZN2md9GridLogic15runBeforeLayoutERKNS_13LayoutContextERKNS_17LogicDependenciesIJN3gdc8TypeListIJNS_17StyleLogicContextEEEENS6_IJNS_20TileSelectionContextEEEEEE20ResolvedDependenciesERNS_11GridContextE : 1692 -> 1836
~ __ZN2md9MapEngineC2Efffb16VKMapViewPurposeRKNSt3__110shared_ptrINS_11TaskContextEEE12VKMapPurposeONS2_10unique_ptrINS_16AnimationManagerENS2_14default_deleteISA_EEEERKN3geo10linear_mapINS_16MapEngineSettingExNS2_8equal_toISH_EENS2_9allocatorINS2_4pairISH_xEEEENS2_6vectorISM_SN_EEEEyP24GEOApplicationAuditTokenPKc : 180008 -> 179992
~ -[VKMapView _applyMapDisplayStyle:animated:duration:] : 1880 -> 2008
~ __ZN2md10StyleLogic19updateConfigurationE9VKMapType : 11848 -> 11868
~ -[VKTrafficFeature attributes] : 1432 -> 1448
CStrings:
+ "[StyleLogic:%p] requestDisplayStyle: clientTarget already at style:%s but transitionTargetStyle:%s was still stale -- correcting"
+ "[StyleLogic:%p] updateConfiguration same-manager switch: mapType:%@ carrying forward transitionTargetStyle:%s transitionAnimated:%s"
- "[StyleLogic:%p] requestDisplayStyle: clientTarget already matched requested style:%s animated:%s, but transitionTargetStyle:%s transitionAnimated:%s did not"
- "[StyleLogic:%p] updateConfiguration same-manager switch: mapType:%@ transitionTargetStyle:%s transitionAnimated:%s resetting to Day"
```
