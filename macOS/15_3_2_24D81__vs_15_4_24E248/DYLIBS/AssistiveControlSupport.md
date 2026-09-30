## AssistiveControlSupport

> `/System/Library/PrivateFrameworks/AssistiveControlSupport.framework/Versions/A/AssistiveControlSupport`

```diff

 388.0.0.0.0
-  __TEXT.__text: 0x63284
+  __TEXT.__text: 0x631e4
   __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x5eec
+  __TEXT.__objc_methlist: 0x607c
   __TEXT.__const: 0x470
   __TEXT.__cstring: 0x42ad
   __TEXT.__oslogstring: 0x1f2
-  __TEXT.__gcc_except_tab: 0x96c
-  __TEXT.__unwind_info: 0x1780
+  __TEXT.__gcc_except_tab: 0x970
+  __TEXT.__unwind_info: 0x1768
   __TEXT.__objc_classname: 0x7d3
   __TEXT.__objc_methname: 0x106f4
   __TEXT.__objc_methtype: 0x15d2

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3da8
+  __DATA_CONST.__objc_selrefs: 0x3e08
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0x7e0
   __AUTH_CONST.__const: 0x1510
   __AUTH_CONST.__cfstring: 0x6100
-  __AUTH_CONST.__objc_const: 0x8b70
+  __AUTH_CONST.__objc_const: 0x88a0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x1158
   __AUTH_CONST.__objc_arrayobj: 0xd8

   - /System/Library/PrivateFrameworks/UniversalAccess.framework/Versions/A/Libraries/libUAPreferences.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D8337049-079A-3F64-8793-36487FD13E58
-  Functions: 2309
-  Symbols:   6062
+  UUID: 115BE8C7-8338-3FC4-850D-590928DDDEDC
+  Functions: 2321
+  Symbols:   6087
   CStrings:  4688
 
Symbols:
+ +[ACSHFunctionKeyMapper _fallbackFKeyModifiedMacKeyCodeMap].cold.1
+ +[ACSHFunctionKeyMapper _regularKeyCodesAndModifiersBySystemActionMap].cold.1
+ +[ACSHFunctionKeyMapper appleEventsBySystemActionMap].cold.1
+ +[ACSHFunctionKeyMapper orderedFunctionKeyMacKeyCodes].cold.1
+ +[ACSHFunctionKeyMapper sharedFunctionKeyMapper].cold.1
+ +[ACSHFunctionKeyMapper specialKeyCodesbySystemActionMap].cold.1
+ +[ACSHKeyboardData _keyboardMetadataByKeyboardType].cold.1
+ +[ACSHKeyboardData allKeyboardData].cold.1
+ +[ACSHKeyboardLayout relevantModifiers].cold.1
+ +[ACSHPanelButton displayImageIdentifierForSystemActionType:].cold.1
+ +[ACSHPanelButtonView _descriptionForPanelButtonViewState:].cold.1
+ +[ACSHPanelButtonView _resizingFontSizesInDescendingOrder].cold.1
+ +[ACSHPanelGenerator dwellActionsPanelForMergingIntoPanel:].cold.1
+ +[ACSHSymbolDrawingManager _systemFontOfSize:weight:].cold.1
+ +[NSDictionary(ACSHPreferenceDictionaryExtras) acsh_cachedColorForString:].cold.1
+ -[ACSHAssistiveControlPreferences _colorFromBundleNamed:].cold.1
+ ACSHAppKitFontWeightForString.cold.1
+ ACSHCarbonModifierBitsByEventModifierFlags.cold.1
+ ACSHColorToString.cold.1
+ ACSHDescriptionForSystemActionType.cold.1
+ ACSHGetAssistiveControlPIDs.cold.1
+ ACSHStringForAppKitFontWeight.cold.1
+ ACSHThemeInfo.cold.1
+ __ACSHOpenPreferencesForAssistiveControlType_block_invoke.cold.2
+ _enumTranslator.cold.1

```
