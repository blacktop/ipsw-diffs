## SystemStatusUI

> `/System/Library/PrivateFrameworks/SystemStatusUI.framework/SystemStatusUI`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA.__objc_ivar`
- `__DATA_DIRTY.__objc_data`

```diff

-284.1.0.0.0
-  __TEXT.__text: 0xa1fa4
-  __TEXT.__objc_methlist: 0xaf24
-  __TEXT.__const: 0x3870
+286.101.0.0.0
+  __TEXT.__text: 0xa2758
+  __TEXT.__objc_methlist: 0xafd4
+  __TEXT.__const: 0x39b0
   __TEXT.__swift5_typeref: 0x2694
   __TEXT.__constg_swiftt: 0x70c
-  __TEXT.__cstring: 0x2bba
+  __TEXT.__cstring: 0x2b5e
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift5_reflstr: 0x238
   __TEXT.__swift5_assocty: 0x1b0

   __TEXT.__swift5_proto: 0x110
   __TEXT.__swift5_types: 0x94
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0xf7c
+  __TEXT.__gcc_except_tab: 0xf90
   __TEXT.__ustring: 0xac
   __TEXT.__oslogstring: 0x581
-  __TEXT.__unwind_info: 0x25d8
+  __TEXT.__unwind_info: 0x25f0
   __TEXT.__eh_frame: 0xec
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1af0
-  __DATA_CONST.__objc_classlist: 0x648
+  __DATA_CONST.__const: 0x1b18
+  __DATA_CONST.__objc_classlist: 0x650
   __DATA_CONST.__objc_catlist: 0x98
-  __DATA_CONST.__objc_protolist: 0x140
+  __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5330
+  __DATA_CONST.__objc_selrefs: 0x5370
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x300
   __DATA_CONST.__got: 0x1098
-  __AUTH_CONST.__const: 0x1408
-  __AUTH_CONST.__cfstring: 0x3ca0
-  __AUTH_CONST.__objc_const: 0x13b28
+  __AUTH_CONST.__const: 0x1428
+  __AUTH_CONST.__cfstring: 0x3c80
+  __AUTH_CONST.__objc_const: 0x13c10
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x1c0
   __AUTH_CONST.__auth_got: 0xbd0
-  __AUTH.__objc_data: 0x1238
+  __AUTH.__objc_data: 0x1288
   __AUTH.__data: 0x280
   __DATA.__objc_ivar: 0x528
-  __DATA.__data: 0x16e0
-  __DATA.__bss: 0x1d98
+  __DATA.__data: 0x1740
+  __DATA.__bss: 0x1da8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_ivar: 0x52c
   __DATA_DIRTY.__objc_data: 0x2d78
-  __DATA_DIRTY.__data: 0x50
+  __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x1f0
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4182
-  Symbols:   9103
-  CStrings:  625
+  Functions: 4194
+  Symbols:   9129
+  CStrings:  624
 
Symbols:
+ +[STUIStatusBarDisplayItemPlacementBatteryGroup groupWithHighPriority:lowPriority:includePercentPlacement:includeNotChargingPlacement:]
+ +[STUIStatusBarDisplayItemPlacementNetworkGroup _groupWithCellularGroup:wifiGroup:includeCellularName:wifiSuppressesCellularType:placeVPNFirst:]
+ +[STUIStatusBarDisplayItemPlacementNetworkGroup groupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:cellularTypeClass:includeCellularName:allowDualNetwork:wifiSuppressesCellularType:placeVPNFirst:]
+ +[STUIStatusBarDisplayItemPlacementNetworkGroup groupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:includeCellularName:wifiSuppressesCellularType:placeVPNFirst:]
+ +[STUIStatusBarDisplayItemPlacementNetworkGroup secondaryGroupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:placeVPNFirst:]
+ +[STUIStatusBarDisplayItemPlacementNetworkGroup wifiSuppressesCellularTypeForCurrentRegion]
+ -[STUIStatusBar menuBarLeadingItemSpacing]
+ -[STUIStatusBarBatteryItem initWithIdentifier:statusBar:]
+ -[STUIStatusBarIndicatorItem useHierarchicalSystemImageForUpdate:]
+ -[STUIStatusBarIndicatorNotChargingItem canEnableDisplayItem:fromData:]
+ -[STUIStatusBarIndicatorNotChargingItem indicatorEntryKey]
+ -[STUIStatusBarIndicatorNotChargingItem systemImageNameForUpdate:]
+ -[STUIStatusBarIndicatorNotChargingItem useHierarchicalSystemImageForUpdate:]
+ -[STUIStatusBarVisualProvider_Pad leadingItemSpacing]
+ GCC_except_table59
+ _OBJC_CLASS_$_STUIStatusBarIndicatorNotChargingItem
+ _OBJC_METACLASS_$_STUIStatusBarIndicatorNotChargingItem
+ __OBJC_$_INSTANCE_METHODS_STUIStatusBarIndicatorNotChargingItem
+ __OBJC_$_PROTOCOL_CLASS_METHODS_STUIStatusBarBatteryView_Internal
+ __OBJC_$_PROTOCOL_METHOD_TYPES_STUIStatusBarBatteryView_Internal
+ __OBJC_$_PROTOCOL_REFS_STUIStatusBarBatteryView_Internal
+ __OBJC_CLASS_RO_$_STUIStatusBarIndicatorNotChargingItem
+ __OBJC_LABEL_PROTOCOL_$_STUIStatusBarBatteryView_Internal
+ __OBJC_METACLASS_RO_$_STUIStatusBarIndicatorNotChargingItem
+ __OBJC_PROTOCOL_$_STUIStatusBarBatteryView_Internal
+ ___91+[STUIStatusBarDisplayItemPlacementNetworkGroup wifiSuppressesCellularTypeForCurrentRegion]_block_invoke
+ ___block_descriptor_40_e8_32w_e8_v16?0q8lw32l8
+ _objc_msgSend$_groupWithCellularGroup:wifiGroup:includeCellularName:wifiSuppressesCellularType:placeVPNFirst:
+ _objc_msgSend$_verticalOffsetFor:
+ _objc_msgSend$_weightFor:
+ _objc_msgSend$groupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:cellularTypeClass:includeCellularName:allowDualNetwork:wifiSuppressesCellularType:placeVPNFirst:
+ _objc_msgSend$groupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:includeCellularName:wifiSuppressesCellularType:placeVPNFirst:
+ _objc_msgSend$groupWithHighPriority:lowPriority:includePercentPlacement:includeNotChargingPlacement:
+ _objc_msgSend$imageByApplyingSymbolConfiguration:
+ _objc_msgSend$secondaryGroupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:placeVPNFirst:
+ _objc_msgSend$setAllowsEdgeAntialiasing:
+ _objc_msgSend$useHierarchicalSystemImageForUpdate:
+ _objc_msgSend$wifiSuppressesCellularTypeForCurrentRegion
- +[STUIStatusBarDisplayItemPlacementBatteryGroup groupWithHighPriority:lowPriority:]
- +[STUIStatusBarDisplayItemPlacementNetworkGroup _groupWithCellularGroup:wifiGroup:includeCellularName:wifiSuppressesCellularType:]
- +[STUIStatusBarDisplayItemPlacementNetworkGroup groupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:cellularTypeClass:includeCellularName:allowDualNetwork:wifiSuppressesCellularType:]
- +[STUIStatusBarDisplayItemPlacementNetworkGroup groupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:includeCellularName:wifiSuppressesCellularType:]
- +[STUIStatusBarDisplayItemPlacementNetworkGroup secondaryGroupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:]
- _objc_msgSend$_groupWithCellularGroup:wifiGroup:includeCellularName:wifiSuppressesCellularType:
- _objc_msgSend$batteryPercentageAlwaysEnabled
- _objc_msgSend$groupWithHighPriority:lowPriority:
- _objc_msgSend$groupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:cellularTypeClass:includeCellularName:allowDualNetwork:wifiSuppressesCellularType:
- _objc_msgSend$groupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:includeCellularName:wifiSuppressesCellularType:
- _objc_msgSend$secondaryGroupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:
- _objc_msgSend$supportsCondensedBatteryPercentage
CStrings:
+ "-[STUIStatusBarVisualProvider_Fallback setupInContainerView:]"
+ "bolt.slash.fill"
- "Class  _Nonnull STUIStatusBarGetVisualProviderClassForScreen(UIScreen *__strong _Nonnull, NSDictionary * _Nullable __strong)"
- "STUIStatusBarVisualProvider_RoundierPad"
- "main"
```
