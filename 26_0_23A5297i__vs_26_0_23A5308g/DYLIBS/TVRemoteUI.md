## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

```diff

-548.0.10.0.0
-  __TEXT.__text: 0xcb9d0
-  __TEXT.__auth_stubs: 0x1af0
-  __TEXT.__objc_methlist: 0xb2a8
-  __TEXT.__const: 0x24b4
-  __TEXT.__gcc_except_tab: 0x1e80
-  __TEXT.__cstring: 0x724a
-  __TEXT.__oslogstring: 0x5812
+548.0.15.0.0
+  __TEXT.__text: 0xcd130
+  __TEXT.__auth_stubs: 0x1b00
+  __TEXT.__objc_methlist: 0xb3d0
+  __TEXT.__const: 0x24a4
+  __TEXT.__gcc_except_tab: 0x1ef0
+  __TEXT.__cstring: 0x745a
+  __TEXT.__oslogstring: 0x59c2
   __TEXT.__ustring: 0x4a
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__constg_swiftt: 0x2dcc

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x2a70
+  __TEXT.__unwind_info: 0x2ac0
   __TEXT.__eh_frame: 0x878
-  __TEXT.__objc_classname: 0x1450
-  __TEXT.__objc_methname: 0x1afa7
-  __TEXT.__objc_methtype: 0x44c5
-  __TEXT.__objc_stubs: 0x12da0
-  __DATA_CONST.__got: 0xd20
-  __DATA_CONST.__const: 0x18f8
+  __TEXT.__objc_classname: 0x144f
+  __TEXT.__objc_methname: 0x1b13f
+  __TEXT.__objc_methtype: 0x44c7
+  __TEXT.__objc_stubs: 0x12fa0
+  __DATA_CONST.__got: 0xd28
+  __DATA_CONST.__const: 0x1950
   __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x66f8
+  __DATA_CONST.__objc_selrefs: 0x6790
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x3a8
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0xd88
+  __AUTH_CONST.__auth_got: 0xd90
   __AUTH_CONST.__const: 0x2eb8
-  __AUTH_CONST.__cfstring: 0x3a00
-  __AUTH_CONST.__objc_const: 0x14948
+  __AUTH_CONST.__cfstring: 0x3a20
+  __AUTH_CONST.__objc_const: 0x14a10
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH.__objc_data: 0x6828
   __AUTH.__data: 0x588
-  __DATA.__objc_ivar: 0xb34
+  __DATA.__objc_ivar: 0xb44
   __DATA.__data: 0x2538
   __DATA.__bss: 0x2658
   __DATA.__common: 0x4c8

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8FD5E767-D044-3F17-A837-5C00E2AE67ED
-  Functions: 4667
-  Symbols:   17358
-  CStrings:  7160
+  UUID: ED461089-D510-39BE-A701-323298249ECE
+  Functions: 4698
+  Symbols:   17450
+  CStrings:  7201
 
Symbols:
+ -[TVRAlertController _dictationDidFinish:]
+ -[TVRAlertController _keyboardChanged:completion:]
+ -[TVRAlertController _keyboardHide:]
+ -[TVRAlertController setShouldDismiss:]
+ -[TVRAlertController shouldDismiss]
+ -[TVRKeyboardView contentView]
+ -[TVRKeyboardView dismissButton]
+ -[TVRKeyboardView setContentView:]
+ -[TVRKeyboardView setDismissButton:]
+ -[TVRKeyboardView textFieldDidEndEditing:]
+ -[TVRUIDarkStyleProvider controlGlassVariant]
+ -[TVRUIDevicePickerViewController _cellForDevice:]
+ -[TVRUIDirectionalControlView _isArrowView:]
+ -[TVRUIDirectionalControlView _unhighlightArrowView:]
+ -[TVRUIDirectionalControlView _unhighlightView]
+ -[TVRUIDirectionalControlView centerCornerRadius]
+ -[TVRUIDirectionalControlView centerEdgeLength]
+ -[TVRUIDirectionalControlView highlightAnimator]
+ -[TVRUIDirectionalControlView setHighlightAnimator:]
+ -[TVRUIDirectionalControlView setUnhighlightAnimator:]
+ -[TVRUIDirectionalControlView unhighlightAnimator]
+ -[TVRUIHintsStylePad micVolumeHintContainerWidth]
+ -[TVRUIHintsStylePad micVolumeImage]
+ -[TVRUIHintsStylePhone micVolumeHintContainerWidth]
+ -[TVRUIHintsStylePhone micVolumeImage]
+ -[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:volumeImage:]
+ -[TVRUIHintsViewController _setupVolumeButtonsHintWithPresentation:volumeImage:]
+ -[TVRUIHintsViewController _updateVolumeButtonsHintFrameWithPresentation:volumeImage:]
+ -[TVRUIHintsViewController requestHintsForMicVolume]
+ -[TVRUIHintsViewController requestHintsForSiri:volumeMode:]
+ -[TVRUIHintsVolumeButtonsView initWithPresentation:image:styleProvider:buttonEdge:buttonHeight:]
+ -[_TVRUITabSelectorControlCell setHighlighted:]
+ GCC_except_table12
+ GCC_except_table32
+ GCC_except_table34
+ _$s10TVRemoteUI20FMPFSKBTRangeDotNodeC5pulse8durationySd_tFyycfU_TA
+ _$s10TVRemoteUI23FMPFSKPeripheralDotNodeC28executePartPerimeterRotation33_ED335F153B208A377B3B9CF4357B611CLLyySo8SKActionCFyycfU_
+ _$s10TVRemoteUI23FMPFSKPeripheralDotNodeC28executePartPerimeterRotation33_ED335F153B208A377B3B9CF4357B611CLLyySo8SKActionCFyycfU_TA
+ _$s10TVRemoteUI23FMPFSKPeripheralDotNodeC28executePartPerimeterRotation33_ED335F153B208A377B3B9CF4357B611CLLyySo8SKActionCFyycfU_TA.175
+ _$s10TVRemoteUI23FMPFSKPeripheralDotNodeC5pulse_8animatedySb_SbtFyycfU0_TA
+ _$s10TVRemoteUI23FMPFSKPeripheralDotNodeC5pulse_8animatedySb_SbtFyycfU_TA
+ _$s10TVRemoteUI25FMPFSKPatternFragmentNodeC28executePartPerimeterRotation33_AF19B95688FC6CB0E81FF37542DE202ELLyySo8SKActionCFyycfU_TA
+ _CGRectIntersectsRect
+ _OBJC_CLASS_$_RTIInputSystemDataPayload
+ _OBJC_IVAR_$_TVRAlertController._shouldDismiss
+ _OBJC_IVAR_$_TVRKeyboardView._contentView
+ _OBJC_IVAR_$_TVRKeyboardView._dismissButton
+ _OBJC_IVAR_$_TVRUIDirectionalControlView._highlightAnimator
+ _OBJC_IVAR_$_TVRUIDirectionalControlView._unhighlightAnimator
+ _UIDictationControllerDictationDidFinish
+ ___36-[TVRAlertController _keyboardHide:]_block_invoke
+ ___36-[TVRAlertController _keyboardHide:]_block_invoke_2
+ ___41-[TVRKeyboardView initWithStyleProvider:]_block_invoke
+ ___45-[TVRUIRemoteViewController startConnections]_block_invoke.126
+ ___45-[TVRUIRemoteViewController startConnections]_block_invoke.133
+ ___46-[TVRUIRemoteViewController _showFindingAlert]_block_invoke.205
+ ___50-[TVRAlertController _keyboardChanged:completion:]_block_invoke
+ ___50-[TVRAlertController _keyboardChanged:completion:]_block_invoke_2
+ ___50-[TVRAlertController _keyboardChanged:completion:]_block_invoke_3
+ ___50-[TVRAlertController _keyboardChanged:completion:]_block_invoke_4
+ ___53-[TVRUIDirectionalControlView _unhighlightArrowView:]_block_invoke
+ ___54-[TVRUIRemoteViewController setSupportsVolumeControl:]_block_invoke.207
+ ___58-[TVRUIRemoteViewController _setupNetworkObserverIfNeeded]_block_invoke.178
+ ___59-[TVRUIHintsViewController requestHintsForSiri:volumeMode:]_block_invoke
+ ___59-[TVRUIHintsViewController requestHintsForSiri:volumeMode:]_block_invoke.25
+ ___59-[TVRUIHintsViewController requestHintsForSiri:volumeMode:]_block_invoke_2
+ ___82-[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:volumeImage:]_block_invoke
+ ___82-[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:volumeImage:]_block_invoke_2
+ ___82-[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:volumeImage:]_block_invoke_3
+ ___82-[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:volumeImage:]_block_invoke_4
+ ___82-[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:volumeImage:]_block_invoke_5
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_49_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_73_e8_32s_e5_v8?0ls32l8
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_TVRemoteUI
+ _objc_msgSend$_cellForDevice:
+ _objc_msgSend$_glassButtonConfiguration
+ _objc_msgSend$_isArrowView:
+ _objc_msgSend$_keyboardChanged:completion:
+ _objc_msgSend$_presentVolumeButtonPressWithPresentation:volumeImage:
+ _objc_msgSend$_setupVolumeButtonsHintWithPresentation:volumeImage:
+ _objc_msgSend$_unhighlightArrowView:
+ _objc_msgSend$_unhighlightView
+ _objc_msgSend$_updateVolumeButtonsHintFrameWithPresentation:volumeImage:
+ _objc_msgSend$centerCornerRadius
+ _objc_msgSend$centerEdgeLength
+ _objc_msgSend$clearGlassButtonConfiguration
+ _objc_msgSend$contextBeforeInput
+ _objc_msgSend$controlGlassVariant
+ _objc_msgSend$data
+ _objc_msgSend$documentState
+ _objc_msgSend$endEditing:
+ _objc_msgSend$initWithPresentation:image:styleProvider:buttonEdge:buttonHeight:
+ _objc_msgSend$interfaceOrientation
+ _objc_msgSend$micVolumeImage
+ _objc_msgSend$orientation
+ _objc_msgSend$requestHintsForSiri:volumeMode:
+ _objc_msgSend$setAcceptsDictationSearchResults:
+ _objc_msgSend$setShouldDismiss:
+ _objc_msgSend$shouldDismiss
+ _objc_msgSend$traitOverrides
- -[TVRAlertController _keyboardChanged:]
- -[TVRAlertController hiddenTextField]
- -[TVRAlertController setHiddenTextField:]
- -[TVRUIDirectionalControlView _layoutHighlightViewForView:]
- -[TVRUIHintsViewController _setupVolumeButtonsHintWithPresentation:]
- -[TVRUIHintsViewController _updateVolumeButtonsHintFrameWithPresentation:]
- -[TVRUIHintsVolumeButtonsView initWithPresentation:styleProvider:buttonEdge:buttonHeight:]
- GCC_except_table22
- GCC_except_table29
- GCC_except_table37
- _$s10TVRemoteUI20FMPFSKBTRangeDotNodeC5pulse8durationySd_tFyyYbcfU_TA
- _$s10TVRemoteUI23FMPFSKPeripheralDotNodeC28executePartPerimeterRotation33_ED335F153B208A377B3B9CF4357B611CLLyySo8SKActionCFyyYbcfU_
- _$s10TVRemoteUI23FMPFSKPeripheralDotNodeC28executePartPerimeterRotation33_ED335F153B208A377B3B9CF4357B611CLLyySo8SKActionCFyyYbcfU_TA
- _$s10TVRemoteUI23FMPFSKPeripheralDotNodeC28executePartPerimeterRotation33_ED335F153B208A377B3B9CF4357B611CLLyySo8SKActionCFyyYbcfU_TA.175
- _$s10TVRemoteUI23FMPFSKPeripheralDotNodeC5pulse_8animatedySb_SbtFyyYbcfU0_TA
- _$s10TVRemoteUI23FMPFSKPeripheralDotNodeC5pulse_8animatedySb_SbtFyyYbcfU_TA
- _$s10TVRemoteUI25FMPFSKPatternFragmentNodeC28executePartPerimeterRotation33_AF19B95688FC6CB0E81FF37542DE202ELLyySo8SKActionCFyyYbcfU_TA
- _OBJC_IVAR_$_TVRAlertController._hiddenTextField
- ___39-[TVRAlertController _keyboardChanged:]_block_invoke
- ___39-[TVRAlertController _keyboardChanged:]_block_invoke_2
- ___45-[TVRUIRemoteViewController startConnections]_block_invoke.125
- ___45-[TVRUIRemoteViewController startConnections]_block_invoke.132
- ___46-[TVRUIRemoteViewController _showFindingAlert]_block_invoke.204
- ___54-[TVRUIRemoteViewController setSupportsVolumeControl:]_block_invoke.206
- ___55-[TVRUIHintsViewController requestHintsForSiri:volume:]_block_invoke
- ___55-[TVRUIHintsViewController requestHintsForSiri:volume:]_block_invoke.25
- ___55-[TVRUIHintsViewController requestHintsForSiri:volume:]_block_invoke_2
- ___58-[TVRUIRemoteViewController _setupNetworkObserverIfNeeded]_block_invoke.177
- ___70-[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:]_block_invoke
- ___70-[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:]_block_invoke_2
- ___70-[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:]_block_invoke_3
- ___70-[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:]_block_invoke_4
- ___70-[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:]_block_invoke_5
- ___block_descriptor_42_e8_32s_e5_v8?0ls32l8
- ___block_literal_global.134
- _objc_msgSend$_keyboardChanged:
- _objc_msgSend$_layoutHighlightViewForView:
- _objc_msgSend$_setupVolumeButtonsHintWithPresentation:
- _objc_msgSend$_updateVolumeButtonsHintFrameWithPresentation:
- _objc_msgSend$glassButtonConfiguration
- _objc_msgSend$initWithPresentation:styleProvider:buttonEdge:buttonHeight:
- _objc_msgSend$inputAccessoryTextFieldBackgroundColor
- _objc_msgSend$needsLayout
- _objc_msgSend$setForceDisableDictation:
- _objc_msgSend$setInputAccessoryView:
CStrings:
+ "%@ RemoteViewCtrl received callback to present keyboard. Active Device %@. Sharing client %@ text length: %lu"
+ "%s - scene: %{public}@ current window scene: %{public}@ secureWindow: %{bool}d"
+ "%s note:%{public}@"
+ "%s payload: %{public}@, data length: %lu"
+ "-[TVRAlertController _cancel]"
+ "-[TVRAlertController _keyboardChanged:completion:]"
+ "-[TVRAlertController _keyboardHide:]"
+ "-[TVRAlertController _keyboardWillShow:]"
+ "-[TVRAlertController viewDidLayoutSubviews]"
+ "-[TVRKeyboardView handleTextActionPayload:]"
+ "-[TVRKeyboardView textFieldDidEndEditing:]"
+ "-[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:volumeImage:]"
+ "-[TVRUIHintsViewController _setupVolumeButtonsHintWithPresentation:volumeImage:]"
+ "@\"UIPopoverPresentationController\""
+ "@\"_TtC10TVRemoteUI36FindingSessionPresentationController\""
+ "@52@0:8Q16@24@32I40d44"
+ "A"
+ "Configured RemoteViewController with device-id %{public}@ identifier type %{public}@ device-type %ld launch-context %{public}@"
+ "Deactivating connection - notification scene object: %@ current scene: %@"
+ "RemoteViewCtrl received callback to end text editing for device %{public}@ text length: %lu"
+ "RemoteViewCtrl received callback to update text of local device text field to newText.length: %lu"
+ "TB,N,V_shouldDismiss"
+ "UI requested disconnect with type %ld"
+ "Volume button hint not enabled, volumeMode=%ld, allowVolumeHint=%{bool}d, shouldShowVolumeHint=%{bool}d"
+ "_cellForDevice:"
+ "_dictationDidFinish:"
+ "_glassButtonConfiguration"
+ "_isArrowView:"
+ "_keyboardChanged:completion:"
+ "_keyboardHide:"
+ "_presentVolumeButtonPressWithPresentation:volumeImage:"
+ "_setupVolumeButtonsHintWithPresentation:volumeImage:"
+ "_shouldDismiss"
+ "_unhighlightArrowView:"
+ "_unhighlightView"
+ "_updateVolumeButtonsHintFrameWithPresentation:volumeImage:"
+ "apple.sing.microphone"
+ "beginFrame:%{public}@  endFrame:%@"
+ "centerCornerRadius"
+ "centerEdgeLength"
+ "clearGlassButtonConfiguration"
+ "contextBeforeInput"
+ "controlGlassVariant"
+ "data"
+ "documentState"
+ "endEditing:"
+ "initWithPresentation:image:styleProvider:buttonEdge:buttonHeight:"
+ "interfaceOrientation"
+ "marked range: %{public}@"
+ "micVolumeHintContainerWidth"
+ "micVolumeImage"
+ "oldFrame:%{public}@ - newFrame:%{public}@"
+ "orientation"
+ "payload string length: %lu textField.text length: %lu"
+ "requestHintsForMicVolume"
+ "requestHintsForSiri:volumeMode:"
+ "setAcceptsDictationSearchResults:"
+ "setShouldDismiss:"
+ "shouldDismiss"
+ "traitOverrides"
+ "v28@0:8B16Q20"
- "%@ RemoteViewCtrl received callback to present keyboard. Active Device %@. Sharing client %@"
- "-[TVRUIHintsViewController _presentVolumeButtonPressWithPresentation:]"
- "-[TVRUIHintsViewController _setupVolumeButtonsHintWithPresentation:]"
- "@\"UITextField\""
- "@44@0:8Q16@24I32d36"
- "Configured RemoteViewController with device-id %{public}@  identifier type %{public}@ device-type %ld launch-context %{public}@"
- "RemoteViewCtrl received callback to end text editing for device %@"
- "RemoteViewCtrl received callback to update text of local device text field"
- "T@\"UITextField\",&,N,V_hiddenTextField"
- "UI requesting disconnect with type %ld"
- "Volume button hint not enabled, showVolumeHint=%{bool}d, allowVolumeHint=%{bool}d, shouldShowVolumeHint=%{bool}d"
- "_hiddenTextField"
- "_keyboardChanged:"
- "_layoutHighlightViewForView:"
- "_setupVolumeButtonsHintWithPresentation:"
- "_updateVolumeButtonsHintFrameWithPresentation:"
- "glassButtonConfiguration"
- "hiddenTextField"
- "initWithPresentation:styleProvider:buttonEdge:buttonHeight:"
- "needsLayout"
- "setForceDisableDictation:"
- "setHiddenTextField:"
- "setInputAccessoryView:"

```
