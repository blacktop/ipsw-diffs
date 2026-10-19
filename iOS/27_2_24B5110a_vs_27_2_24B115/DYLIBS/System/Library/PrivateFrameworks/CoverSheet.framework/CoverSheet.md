## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

```diff

 159.2.4.0.0
-  __TEXT.__text: 0x186f00
-  __TEXT.__objc_methlist: 0x1658c
-  __TEXT.__const: 0x4154
-  __TEXT.__cstring: 0xcaef
-  __TEXT.__oslogstring: 0x8f34
-  __TEXT.__gcc_except_tab: 0x1270
+  __TEXT.__text: 0x192080
+  __TEXT.__objc_methlist: 0x169c4
+  __TEXT.__const: 0x415c
+  __TEXT.__cstring: 0xd0cc
+  __TEXT.__oslogstring: 0x9269
+  __TEXT.__gcc_except_tab: 0x139c
   __TEXT.__ustring: 0xa4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x5990
+  __TEXT.__unwind_info: 0x5a28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x40b0
-  __DATA_CONST.__objc_classlist: 0x7b0
+  __DATA_CONST.__const: 0x40f8
+  __DATA_CONST.__objc_classlist: 0x7c8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x670
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc6f8
+  __DATA_CONST.__objc_selrefs: 0xc950
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x5f0
-  __DATA_CONST.__objc_arraydata: 0x1078
-  __DATA_CONST.__got: 0x1590
+  __DATA_CONST.__objc_superrefs: 0x600
+  __DATA_CONST.__objc_arraydata: 0x1108
+  __DATA_CONST.__got: 0x15b8
   __AUTH_CONST.__const: 0xcf0
-  __AUTH_CONST.__cfstring: 0xc880
-  __AUTH_CONST.__objc_const: 0x3c920
-  __AUTH_CONST.__objc_arrayobj: 0x1248
-  __AUTH_CONST.__objc_intobj: 0x438
+  __AUTH_CONST.__cfstring: 0xd180
+  __AUTH_CONST.__objc_const: 0x3d760
+  __AUTH_CONST.__objc_arrayobj: 0x12a8
+  __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_doubleobj: 0x660
   __AUTH_CONST.__auth_got: 0xd28
-  __AUTH.__objc_data: 0xf00
-  __DATA.__objc_ivar: 0x1bc4
+  __AUTH.__objc_data: 0xf50
+  __DATA.__objc_ivar: 0x1ca8
   __DATA.__data: 0x56f8
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x3de0
+  __DATA_DIRTY.__objc_data: 0x3e80
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7957
-  Symbols:   14111
-  CStrings:  2664
+  Functions: 8048
+  Symbols:   14287
+  CStrings:  2743
 
Symbols:
+ +[CSInadvertentTouchIDRecognizerSettings settingsControllerModule]
+ -[CSCoverSheetViewController _inadvertentTouchIDRecognizerDidUpdate:]
+ -[CSCoverSheetViewController _setupInadvertentTouchIDRecognizer]
+ -[CSInadvertentTouchIDRecognizer .cxx_destruct]
+ -[CSInadvertentTouchIDRecognizer _debugLayerWithRect:cornerCutouts:color:]
+ -[CSInadvertentTouchIDRecognizer _evaluateProtectionState]
+ -[CSInadvertentTouchIDRecognizer _isActiveProtectionMode:]
+ -[CSInadvertentTouchIDRecognizer _loadFromSettings:]
+ -[CSInadvertentTouchIDRecognizer _protectionModeDescription:]
+ -[CSInadvertentTouchIDRecognizer _removeDebugLayers]
+ -[CSInadvertentTouchIDRecognizer _updateBiometricBlockState:]
+ -[CSInadvertentTouchIDRecognizer _updateDebugViews]
+ -[CSInadvertentTouchIDRecognizer _updateStrictCoverageState:]
+ -[CSInadvertentTouchIDRecognizer _updateToChangedForReason:]
+ -[CSInadvertentTouchIDRecognizer biometricAuthShouldBeBlocked]
+ -[CSInadvertentTouchIDRecognizer canBePreventedByGestureRecognizer:]
+ -[CSInadvertentTouchIDRecognizer canPreventGestureRecognizer:]
+ -[CSInadvertentTouchIDRecognizer dealloc]
+ -[CSInadvertentTouchIDRecognizer initWithTarget:action:]
+ -[CSInadvertentTouchIDRecognizer lockScreenActive]
+ -[CSInadvertentTouchIDRecognizer reset]
+ -[CSInadvertentTouchIDRecognizer setLockScreenActive:]
+ -[CSInadvertentTouchIDRecognizer setShowsViewDebugArea:]
+ -[CSInadvertentTouchIDRecognizer settings:changedValueForKey:]
+ -[CSInadvertentTouchIDRecognizer showsViewDebugArea]
+ -[CSInadvertentTouchIDRecognizer strictCoverageRequired]
+ -[CSInadvertentTouchIDRecognizer touchesBegan:withEvent:]
+ -[CSInadvertentTouchIDRecognizer touchesCancelled:withEvent:]
+ -[CSInadvertentTouchIDRecognizer touchesEnded:withEvent:]
+ -[CSInadvertentTouchIDRecognizer touchesMoved:withEvent:]
+ -[CSInadvertentTouchIDRecognizerSettings cornerAllowBottomLeftX]
+ -[CSInadvertentTouchIDRecognizerSettings cornerAllowBottomLeftY]
+ -[CSInadvertentTouchIDRecognizerSettings cornerAllowBottomRightX]
+ -[CSInadvertentTouchIDRecognizerSettings cornerAllowBottomRightY]
+ -[CSInadvertentTouchIDRecognizerSettings cornerAllowTopLeftX]
+ -[CSInadvertentTouchIDRecognizerSettings cornerAllowTopLeftY]
+ -[CSInadvertentTouchIDRecognizerSettings cornerAllowTopRightX]
+ -[CSInadvertentTouchIDRecognizerSettings cornerAllowTopRightY]
+ -[CSInadvertentTouchIDRecognizerSettings edgeProtectionBottomInset]
+ -[CSInadvertentTouchIDRecognizerSettings edgeProtectionBottomMode]
+ -[CSInadvertentTouchIDRecognizerSettings edgeProtectionLeftInset]
+ -[CSInadvertentTouchIDRecognizerSettings edgeProtectionLeftMode]
+ -[CSInadvertentTouchIDRecognizerSettings edgeProtectionRightInset]
+ -[CSInadvertentTouchIDRecognizerSettings edgeProtectionRightMode]
+ -[CSInadvertentTouchIDRecognizerSettings edgeProtectionTopInset]
+ -[CSInadvertentTouchIDRecognizerSettings edgeProtectionTopMode]
+ -[CSInadvertentTouchIDRecognizerSettings impermissibleTouchCountMode]
+ -[CSInadvertentTouchIDRecognizerSettings impermissibleTouchCount]
+ -[CSInadvertentTouchIDRecognizerSettings isEnabled]
+ -[CSInadvertentTouchIDRecognizerSettings lockScreenActiveMode]
+ -[CSInadvertentTouchIDRecognizerSettings setCornerAllowBottomLeftX:]
+ -[CSInadvertentTouchIDRecognizerSettings setCornerAllowBottomLeftY:]
+ -[CSInadvertentTouchIDRecognizerSettings setCornerAllowBottomRightX:]
+ -[CSInadvertentTouchIDRecognizerSettings setCornerAllowBottomRightY:]
+ -[CSInadvertentTouchIDRecognizerSettings setCornerAllowTopLeftX:]
+ -[CSInadvertentTouchIDRecognizerSettings setCornerAllowTopLeftY:]
+ -[CSInadvertentTouchIDRecognizerSettings setCornerAllowTopRightX:]
+ -[CSInadvertentTouchIDRecognizerSettings setCornerAllowTopRightY:]
+ -[CSInadvertentTouchIDRecognizerSettings setDefaultValues]
+ -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionBottomInset:]
+ -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionBottomMode:]
+ -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionLeftInset:]
+ -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionLeftMode:]
+ -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionRightInset:]
+ -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionRightMode:]
+ -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionTopInset:]
+ -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionTopMode:]
+ -[CSInadvertentTouchIDRecognizerSettings setEnabled:]
+ -[CSInadvertentTouchIDRecognizerSettings setImpermissibleTouchCount:]
+ -[CSInadvertentTouchIDRecognizerSettings setImpermissibleTouchCountMode:]
+ -[CSInadvertentTouchIDRecognizerSettings setLockScreenActiveMode:]
+ -[CSInadvertentTouchIDRecognizerSettings setShowsViewDebugArea:]
+ -[CSInadvertentTouchIDRecognizerSettings setTreatsRestrictiveAsBlocking:]
+ -[CSInadvertentTouchIDRecognizerSettings showsViewDebugArea]
+ -[CSInadvertentTouchIDRecognizerSettings treatsRestrictiveAsBlocking]
+ -[CSLockScreenSettings inadvertentTouchIDRecognizerSettings]
+ -[CSLockScreenSettings setInadvertentTouchIDRecognizerSettings:]
+ -[CSMagSafeAccessory _getEmblemResourceURLForNFCType:]
+ -[CSMagSafeAccessory emblemResourceURL]
+ -[CSMagSafeAccessoryWalletEmblemView .cxx_destruct]
+ -[CSMagSafeAccessoryWalletEmblemView _dismissAnimation]
+ -[CSMagSafeAccessoryWalletEmblemView _presentAnimation]
+ -[CSMagSafeAccessoryWalletEmblemView emblemView]
+ -[CSMagSafeAccessoryWalletEmblemView initWithFrame:emblemResourceURL:]
+ -[CSMagSafeAccessoryWalletEmblemView layoutSubviews]
+ -[CSMagSafeAccessoryWalletEmblemView setEmblemView:]
+ GCC_except_table15
+ GCC_except_table755
+ GCC_except_table767
+ GCC_except_table776
+ GCC_except_table791
+ GCC_except_table802
+ GCC_except_table839
+ _OBJC_CLASS_$_BSUICAPackageView
+ _OBJC_CLASS_$_CSInadvertentTouchIDRecognizer
+ _OBJC_CLASS_$_CSInadvertentTouchIDRecognizerSettings
+ _OBJC_CLASS_$_CSMagSafeAccessoryWalletEmblemView
+ _OBJC_IVAR_$_CSCoverSheetViewController._inadvertentTouchIDRecognizer
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._biometricAuthShouldBeBlocked
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowBottomLeftX
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowBottomLeftY
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowBottomRightX
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowBottomRightY
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowTopLeftX
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowTopLeftY
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowTopRightX
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowTopRightY
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionBottomInset
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionBottomLayer
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionBottomMode
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionLeftInset
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionLeftLayer
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionLeftMode
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionRightInset
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionRightLayer
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionRightMode
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionTopInset
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionTopLayer
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionTopMode
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._enabled
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._impermissibleTouchCount
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._impermissibleTouchCountMode
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._lockScreenActive
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._lockScreenActiveMode
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._needsDebugViewUpdate
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._showsViewDebugArea
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._strictCoverageRequired
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._trackedTouches
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._treatsRestrictiveAsBlocking
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowBottomLeftX
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowBottomLeftY
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowBottomRightX
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowBottomRightY
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowTopLeftX
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowTopLeftY
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowTopRightX
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowTopRightY
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionBottomInset
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionBottomMode
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionLeftInset
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionLeftMode
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionRightInset
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionRightMode
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionTopInset
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionTopMode
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._enabled
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._impermissibleTouchCount
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._impermissibleTouchCountMode
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._lockScreenActiveMode
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._showsViewDebugArea
+ _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._treatsRestrictiveAsBlocking
+ _OBJC_IVAR_$_CSLockScreenSettings._inadvertentTouchIDRecognizerSettings
+ _OBJC_IVAR_$_CSMagSafeAccessory._emblemResourceURL
+ _OBJC_IVAR_$_CSMagSafeAccessoryWalletEmblemView._emblemView
+ _OBJC_METACLASS_$_CSInadvertentTouchIDRecognizer
+ _OBJC_METACLASS_$_CSInadvertentTouchIDRecognizerSettings
+ _OBJC_METACLASS_$_CSMagSafeAccessoryWalletEmblemView
+ __OBJC_$_CLASS_METHODS_CSInadvertentTouchIDRecognizerSettings
+ __OBJC_$_INSTANCE_METHODS_CSInadvertentTouchIDRecognizer
+ __OBJC_$_INSTANCE_METHODS_CSInadvertentTouchIDRecognizerSettings
+ __OBJC_$_INSTANCE_METHODS_CSMagSafeAccessoryWalletEmblemView
+ __OBJC_$_INSTANCE_VARIABLES_CSInadvertentTouchIDRecognizer
+ __OBJC_$_INSTANCE_VARIABLES_CSInadvertentTouchIDRecognizerSettings
+ __OBJC_$_INSTANCE_VARIABLES_CSMagSafeAccessoryWalletEmblemView
+ __OBJC_$_PROP_LIST_CSInadvertentTouchIDRecognizer
+ __OBJC_$_PROP_LIST_CSInadvertentTouchIDRecognizerSettings
+ __OBJC_$_PROP_LIST_CSMagSafeAccessoryWalletEmblemView
+ __OBJC_CLASS_PROTOCOLS_$_CSInadvertentTouchIDRecognizer
+ __OBJC_CLASS_RO_$_CSInadvertentTouchIDRecognizer
+ __OBJC_CLASS_RO_$_CSInadvertentTouchIDRecognizerSettings
+ __OBJC_CLASS_RO_$_CSMagSafeAccessoryWalletEmblemView
+ __OBJC_METACLASS_RO_$_CSInadvertentTouchIDRecognizer
+ __OBJC_METACLASS_RO_$_CSInadvertentTouchIDRecognizerSettings
+ __OBJC_METACLASS_RO_$_CSMagSafeAccessoryWalletEmblemView
+ ___51-[CSInadvertentTouchIDRecognizer _updateDebugViews]_block_invoke
+ ___51-[CSInadvertentTouchIDRecognizer _updateDebugViews]_block_invoke_2
+ ___58-[CSInadvertentTouchIDRecognizer _evaluateProtectionState]_block_invoke
+ ___58-[CSInadvertentTouchIDRecognizer _evaluateProtectionState]_block_invoke_2
+ ___58-[CSInadvertentTouchIDRecognizer _evaluateProtectionState]_block_invoke_3
+ ___block_descriptor_40_e8_32r_e8_Q16?0Q8lr32l8
+ ___block_descriptor_40_e8_d16?0d8l
+ _kCAFillRuleEvenOdd
- GCC_except_table753
- GCC_except_table763
- GCC_except_table774
- GCC_except_table789
- GCC_except_table800
- GCC_except_table837
CStrings:
+ "4"
+ "5+"
+ "?\f"
+ "BLOCKING"
+ "Block"
+ "BlockBioAuth"
+ "Bottom Inset %"
+ "Bottom-Left X %"
+ "Bottom-Left Y %"
+ "Bottom-Right X %"
+ "Bottom-Right Y %"
+ "CSInadvertentTouchIDRecognizer"
+ "Charge Ring Build"
+ "Corner Allow Zones"
+ "DoNothing"
+ "Edge Bottom"
+ "Edge Inset Protection"
+ "Edge Left"
+ "Edge Right"
+ "Edge Top"
+ "Enabled"
+ "Impermissible Touch Count"
+ "Inadvertent Settings"
+ "Inadvertent TouchID Settings"
+ "InadvertentTouchIDRecognizer - after load (treatsRestrictiveAsBlocking: %{BOOL}d)"
+ "InadvertentTouchIDRecognizer - biometric block state changed: %{public}@"
+ "InadvertentTouchIDRecognizer - escalating Restrictive to BlockBioAuth (treatsRestrictiveAsBlocking enabled)"
+ "InadvertentTouchIDRecognizer - failed to update to changed for reason: %@"
+ "InadvertentTouchIDRecognizer - protection state: %{public}@\n  contributors: [%{public}@]"
+ "InadvertentTouchIDRecognizer - protection state: NONE (no active checks)"
+ "InadvertentTouchIDRecognizer - settings changed key: %{public}@ (treatsRestrictiveAsBlocking: %{BOOL}d, trackedTouches: %lu, blocked: %{BOOL}d, strict: %{BOOL}d)"
+ "InadvertentTouchIDRecognizer - strict coverage state changed: %{public}@"
+ "Left Inset %"
+ "Lock Screen Active"
+ "No Impact"
+ "Out"
+ "Protection Modes"
+ "Q16@?0Q8"
+ "RESTRICTIVE"
+ "Restrictive"
+ "Right Inset %"
+ "Top Inset %"
+ "Top-Left X %"
+ "Top-Left Y %"
+ "Top-Right X %"
+ "Top-Right Y %"
+ "Touch Count"
+ "Treat Restrictive as Blocking"
+ "cornerAllowBottomLeftX"
+ "cornerAllowBottomLeftY"
+ "cornerAllowBottomRightX"
+ "cornerAllowBottomRightY"
+ "cornerAllowTopLeftX"
+ "cornerAllowTopLeftY"
+ "cornerAllowTopRightX"
+ "cornerAllowTopRightY"
+ "edgeProtectionBottom(%@): touch at (%.1f, %.1f) inside bottom inset"
+ "edgeProtectionBottomInset"
+ "edgeProtectionBottomMode"
+ "edgeProtectionLeft(%@): touch at (%.1f, %.1f) inside left inset"
+ "edgeProtectionLeftInset"
+ "edgeProtectionLeftMode"
+ "edgeProtectionRight(%@): touch at (%.1f, %.1f) inside right inset"
+ "edgeProtectionRightInset"
+ "edgeProtectionRightMode"
+ "edgeProtectionTop(%@): touch at (%.1f, %.1f) inside top inset"
+ "edgeProtectionTopInset"
+ "edgeProtectionTopMode"
+ "impermissibleTouchCount"
+ "impermissibleTouchCount(%@): %lu touches >= threshold %lu"
+ "impermissibleTouchCountMode"
+ "inadvertentTouchIDRecognizer didUpdate biometricBlock: %{BOOL}d (delegate: %{public}@)"
+ "inadvertentTouchIDRecognizerSettings"
+ "lockScreenActive(%@)"
+ "lockScreenActiveMode"
+ "showsViewDebugArea"
+ "treatsRestrictiveAsBlocking"
+ "updateBiometricBlockState"
+ "updateStrictCoverageState"
+ "wallet-inset-zeus"
- "?\v"
```
