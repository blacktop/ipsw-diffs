## ConnectivityModule

> `/System/Library/ControlCenter/Bundles/ConnectivityModule.bundle/ConnectivityModule`

```diff

-655.1.3.100.0
-  __TEXT.__text: 0x8088
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x139c
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__cstring: 0x480
-  __TEXT.__oslogstring: 0x465
-  __TEXT.__unwind_info: 0x310
-  __TEXT.__objc_classname: 0x32c
-  __TEXT.__objc_methname: 0x40f3
-  __TEXT.__objc_methtype: 0xd8e
-  __TEXT.__objc_stubs: 0x25c0
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x250
-  __DATA_CONST.__objc_classlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x68
+655.1.9.0.0
+  __TEXT.__text: 0x5a00
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_methlist: 0x1064
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x4c
+  __TEXT.__cstring: 0x32b
+  __TEXT.__oslogstring: 0x318
+  __TEXT.__unwind_info: 0x240
+  __TEXT.__objc_classname: 0x24a
+  __TEXT.__objc_methname: 0x3788
+  __TEXT.__objc_methtype: 0xcf5
+  __TEXT.__objc_stubs: 0x1b20
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0x1b0
+  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe58
+  __DATA_CONST.__objc_selrefs: 0xb38
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x260
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x3c0
-  __AUTH_CONST.__objc_const: 0x1c50
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xf0
-  __DATA.__data: 0x4e0
-  __DATA_DIRTY.__objc_data: 0x1e0
+  __AUTH_CONST.__cfstring: 0x280
+  __AUTH_CONST.__objc_const: 0x1668
+  __DATA.__objc_ivar: 0xc0
+  __DATA.__data: 0x480
+  __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C2F08768-9B8F-3B6C-BAD9-9C7F1E2271CD
-  Functions: 295
-  Symbols:   155
-  CStrings:  837
+  UUID: 4B6B00FD-1EA3-3E67-809C-3F31AEA68658
+  Functions: 224
+  Symbols:   128
+  CStrings:  683
 
Symbols:
+ _OBJC_CLASS_$_CCUICellularDataModuleViewController
- _CGRectGetMaxX
- _MCFeatureAppCellularDataModificationAllowed
- _OBJC_CLASS_$_CCUIAlwaysExpandedMenuModuleViewController
- _OBJC_CLASS_$_CCUICellularMenuModuleItem
- _OBJC_CLASS_$_CCUICellularMenuModuleItemIndicatorView
- _OBJC_CLASS_$_CCUICellularMenuModuleItemTrailingView
- _OBJC_CLASS_$_CCUIConnectivityCellularDataViewController
- _OBJC_CLASS_$_CCUIConnectivityCellularModuleViewController
- _OBJC_CLASS_$_CCUIMenuModuleItem
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSURL
- _OBJC_CLASS_$_NSUserDefaults
- _OBJC_CLASS_$_UIFont
- _OBJC_CLASS_$_UIFontMetrics
- _OBJC_CLASS_$_UILabel
- _OBJC_METACLASS_$_CCUIAlwaysExpandedMenuModuleViewController
- _OBJC_METACLASS_$_CCUICellularMenuModuleItem
- _OBJC_METACLASS_$_CCUICellularMenuModuleItemIndicatorView
- _OBJC_METACLASS_$_CCUICellularMenuModuleItemTrailingView
- _OBJC_METACLASS_$_CCUIConnectivityCellularDataViewController
- _OBJC_METACLASS_$_CCUIConnectivityCellularModuleViewController
- _OBJC_METACLASS_$_CCUIMenuModuleItem
- _OBJC_METACLASS_$_UIView
- _UIRectCenteredYInRectScale
- __CTServerConnectionGetCellularDataIsEnabled
- __CTServerConnectionSetCellularDataIsEnabled
- __os_log_error_impl
- _objc_retain_x1
CStrings:
+ "@\"CCUICellularDataModuleViewController\""
+ "T@\"CCUICellularDataModuleViewController\",&,N,V_cellularDataModuleViewController"
+ "T@\"CCUICellularDataModuleViewController\",&,N,V_expandedCellularDataButtonViewController"
+ "_cellularDataModuleViewController"
+ "cellularDataModuleViewController"
+ "setCellularDataModuleViewController:"
- "@\"CCUIContentModuleDetailClickPresentationInteractionManager\""
- "@\"CCUIContentModuleDetailTransitioningDelegate\""
- "@\"NSMutableDictionary\""
- "@\"UILabel\""
- "B8@?0"
- "CCUICellularMenuModuleItem"
- "CCUICellularMenuModuleItemIndicatorView"
- "CCUICellularMenuModuleItemTrailingView"
- "CCUIConnectivityCellularDataViewController"
- "CCUIConnectivityCellularModuleViewController"
- "CONTROL_CENTER_STATUS_CELLULAR_DATA_NAME"
- "CONTROL_CENTER_STATUS_CELLULAR_DATA_OFF"
- "CONTROL_CENTER_STATUS_CELLULAR_DATA_ON"
- "CONTROL_CENTER_STATUS_CELLULAR_SETTINGS"
- "Cellular Data state updated to %{public}@ [ capable: %d enabled: %d airplaneMode: %d subtitle: %{private}@ ]"
- "CellularDataGlyph"
- "ControlCenterCellularDataButtonDemoMode"
- "CoreTelephonyClientDelegate"
- "Could not get subscription info. Error: %@"
- "Could not get subscriptions Info. Error: %@"
- "Error setting active data selection to %@. Error: %@"
- "Setting Active user data selection to %@"
- "T@\"CCUIConnectivityButtonViewController\",&,N,V_cellularDataButtonViewController"
- "T@\"CCUIConnectivityButtonViewController\",&,N,V_expandedCellularDataButtonViewController"
- "T@\"NSString\",C,N,V_shortLabel"
- "T@\"UILabel\",&,N,V_indicatorLabel"
- "Td,N,V_baseline"
- "Td,N,V_cornerRadius"
- "Td,N,V_fontSize"
- "Td,N,V_minPadding"
- "Toggle Cellular Data state from %{public}@"
- "URLWithString:"
- "UUIDString"
- "_baseline"
- "_cellularDataButtonViewController"
- "_clickPresentationInteractionManager"
- "_cornerRadius"
- "_detailTransitioningDelegate"
- "_fontSize"
- "_glyphImageForDisplayBars:"
- "_indicatorLabel"
- "_isCellularDataButtonDemoMode"
- "_isCellularDataRestricted"
- "_menuItemForCellularPlan:"
- "_minPadding"
- "_multipleSubscriptionsAvailable"
- "_shortLabel"
- "_shouldReverseLayoutDirection"
- "_simIndicatorCache"
- "_updateCellularMenuItems"
- "_updateGlyphImageWithDisplayBars:"
- "activeSubscriptionsDidChange"
- "array"
- "baseline"
- "blackColor"
- "boolForKey:"
- "boolValue"
- "bottomAnchor"
- "cellular-data"
- "cellularDataButtonViewController"
- "cellularbars"
- "centerYAnchor"
- "com.apple.ControlCenter.CellularData"
- "constraintEqualToAnchor:"
- "constraintGreaterThanOrEqualToAnchor:constant:"
- "constraintGreaterThanOrEqualToAnchor:multiplier:"
- "constraintGreaterThanOrEqualToConstant:"
- "cornerRadius"
- "defaultMetrics"
- "displayBars"
- "doubleValue"
- "dualSimCapabilityDidChange"
- "effectiveBoolValueForSetting:"
- "fontDescriptor"
- "fontDescriptorWithSymbolicTraits:"
- "fontSize"
- "fontWithDescriptor:size:"
- "getCurrentDataServiceDescriptorSync:"
- "getPublicSignalStrength:error:"
- "getShortLabel:error:"
- "getSubscriptionInfoWithError:"
- "getSubscriptionUserFacingName:error:"
- "heightAnchor"
- "indicatorForMenuItem:"
- "indicatorLabel"
- "indicatorView"
- "initWithNibName:bundle:"
- "initWithTitle:identifier:handler:"
- "intrinsicContentSize"
- "isSimHidden"
- "layer"
- "layoutSubviews"
- "leadingAnchor"
- "minPadding"
- "objectForKeyedSubscript:"
- "openURL:completionHandler:"
- "prefs:root=MOBILE_DATA_SETTINGS_ID"
- "scaledFontForFont:"
- "scaledValueForValue:"
- "setActive:"
- "setActiveUserDataSelection:completion:"
- "setAdjustsFontForContentSizeCategory:"
- "setBackgroundColor:"
- "setBaseline:"
- "setCellularDataButtonViewController:"
- "setContentCompressionResistancePriority:forAxis:"
- "setContentHuggingPriority:forAxis:"
- "setContentMode:"
- "setCornerRadius:"
- "setExpanded:"
- "setFont:"
- "setFontSize:"
- "setFooterButtonTitle:handler:"
- "setIndentation:"
- "setIndicatorLabel:"
- "setMasksToBounds:"
- "setMenuItems:"
- "setMinPadding:"
- "setMinimumMenuItems:"
- "setNumberOfLines:"
- "setObject:forKeyedSubscript:"
- "setSelected:"
- "setShortLabel:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTranslatesAutoresizingMaskIntoConstraints:"
- "setUseTrailingInset:"
- "setVisibleMenuItems:"
- "shortLabel"
- "signalStrengthChanged:info:"
- "simLessSubscriptionsDidChange"
- "sizeThatFits:"
- "standardUserDefaults"
- "subscriptionInfoDidChange"
- "subscriptionsInUse"
- "subviews"
- "systemFontOfSize:"
- "systemGrayColor"
- "systemImageNamed:variableValue:withConfiguration:"
- "topAnchor"
- "trailingAnchor"
- "trailingViewForMenuItem:"
- "unregisterObserver:"
- "userDataPreferred"
- "uuid"
- "v16@?0@\"NSError\"8"
- "widthAnchor"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}32@0:8{CGSize=dd}16"

```
