## TypistFramework

> `/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework`

```diff

-463.0.0.0.0
-  __TEXT.__text: 0x34eac
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x32e4
-  __TEXT.__const: 0x302
-  __TEXT.__cstring: 0x4ba2
-  __TEXT.__ustring: 0x1156
-  __TEXT.__gcc_except_tab: 0x300
+465.0.0.0.0
+  __TEXT.__text: 0x3ff68
+  __TEXT.__auth_stubs: 0xd90
+  __TEXT.__objc_methlist: 0x357c
+  __TEXT.__const: 0x382
+  __TEXT.__cstring: 0x5872
+  __TEXT.__ustring: 0x12c0
+  __TEXT.__gcc_except_tab: 0xbd8
   __TEXT.__dlopen_cstrs: 0x6d
   __TEXT.__oslogstring: 0xc
   __TEXT.__swift5_typeref: 0xaa

   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xb80
+  __TEXT.__unwind_info: 0xdd8
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x4e6
-  __TEXT.__objc_methname: 0x79d1
-  __TEXT.__objc_methtype: 0x1108
-  __TEXT.__objc_stubs: 0x6dc0
-  __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0x6b0
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__objc_classname: 0x515
+  __TEXT.__objc_methname: 0x8236
+  __TEXT.__objc_methtype: 0x113e
+  __TEXT.__objc_stubs: 0x7a20
+  __DATA_CONST.__got: 0x518
+  __DATA_CONST.__const: 0x900
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2070
-  __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__objc_arraydata: 0x3500
-  __AUTH_CONST.__auth_got: 0x698
-  __AUTH_CONST.__const: 0x5a8
-  __AUTH_CONST.__cfstring: 0xfce0
-  __AUTH_CONST.__objc_const: 0x3d78
+  __DATA_CONST.__objc_selrefs: 0x2348
+  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_arraydata: 0x3ba0
+  __AUTH_CONST.__auth_got: 0x6d8
+  __AUTH_CONST.__const: 0x628
+  __AUTH_CONST.__cfstring: 0x114c0
+  __AUTH_CONST.__objc_const: 0x4668
   __AUTH_CONST.__objc_doubleobj: 0x80
-  __AUTH_CONST.__objc_intobj: 0xaf8
+  __AUTH_CONST.__objc_intobj: 0xbb8
   __AUTH_CONST.__objc_arrayobj: 0x318
-  __AUTH_CONST.__objc_dictobj: 0x2f8
+  __AUTH_CONST.__objc_dictobj: 0x398
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0xc78
+  __AUTH.__objc_data: 0xd18
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x288
+  __DATA.__objc_ivar: 0x28c
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x2d0
+  __DATA.__bss: 0x2f0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x168
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 1B0AD2BE-5796-33DD-BBDF-C12E8AC463F7
-  Functions: 1158
-  Symbols:   4112
-  CStrings:  4867
+  UUID: 6E35C122-343C-38EE-9FCD-58C9C1584170
+  Functions: 1262
+  Symbols:   4514
+  CStrings:  5260
 
Symbols:
+ +[TypistKeyboardDataInProcess _activeInputModesContainsInputMode:]
+ +[TypistKeyboardDataInProcess _variantsByAppendingDualStringKey:toVariants:]
+ +[TypistKeyboardDataInProcess addKeyboardGestureKeys:keys:inPlane:addTo:]
+ +[TypistKeyboardDataInProcess addKeyboardPopupKeys:keys:inPlane:addTo:keyplaneKeycaps:]
+ +[TypistKeyboardDataInProcess addKeyboards:]
+ +[TypistKeyboardDataInProcess appendingSecondaryStringToVariantsTop:secondaryString:withDirection:]
+ +[TypistKeyboardDataInProcess centerOfKey:withOffset:]
+ +[TypistKeyboardDataInProcess cleanUpSwitchTableBasedOnDefaultPlane:defaultPlaneName:]
+ +[TypistKeyboardDataInProcess determineDefaultPlane10Key:basePlaneName:]
+ +[TypistKeyboardDataInProcess determineDefaultPlane:basePlaneName:]
+ +[TypistKeyboardDataInProcess dismissKeyboard]
+ +[TypistKeyboardDataInProcess dismissOneTimeTIActions:]
+ +[TypistKeyboardDataInProcess downActionFlagsForKey:plane:keyplaneKeycaps:]
+ +[TypistKeyboardDataInProcess findKeyBoundsInKeyboard:]
+ +[TypistKeyboardDataInProcess floatingKeyboardDraggablePoint]
+ +[TypistKeyboardDataInProcess generateKeyplaneSwitchTable:]
+ +[TypistKeyboardDataInProcess generateKeyplaneSwitchTableFor10Key:]
+ +[TypistKeyboardDataInProcess generatePopupKeySubtrees:key:plane:layout:keyplaneKeycaps:]
+ +[TypistKeyboardDataInProcess getAllCandidates]
+ +[TypistKeyboardDataInProcess getCandidateBarRect]
+ +[TypistKeyboardDataInProcess getCandidateCenter:]
+ +[TypistKeyboardDataInProcess getCandidateCenterAtIndex:]
+ +[TypistKeyboardDataInProcess getExtendedCandidateViewToggleButtonCenter]
+ +[TypistKeyboardDataInProcess getKeyboardLayout:]
+ +[TypistKeyboardDataInProcess getKeyboardPPM]
+ +[TypistKeyboardDataInProcess getKeyboardPlaneKeys:keys:inPlane:]
+ +[TypistKeyboardDataInProcess getKeyboardScaleTransform]
+ +[TypistKeyboardDataInProcess getKeyboardUISettings]
+ +[TypistKeyboardDataInProcess getKeyplaneDescription:]
+ +[TypistKeyboardDataInProcess getRepresentedStringFromKey:]
+ +[TypistKeyboardDataInProcess getSentenceBoundaryStrings]
+ +[TypistKeyboardDataInProcess getShuangpinEnumeration:]
+ +[TypistKeyboardDataInProcess getShuangpinEnumeration:].cold.1
+ +[TypistKeyboardDataInProcess getTIPreferences]
+ +[TypistKeyboardDataInProcess getVisibleCandidateList:]
+ +[TypistKeyboardDataInProcess getVisibleKeyplaneName]
+ +[TypistKeyboardDataInProcess getWubiEnumeration:]
+ +[TypistKeyboardDataInProcess getWubiEnumeration:].cold.1
+ +[TypistKeyboardDataInProcess hasMarkedText]
+ +[TypistKeyboardDataInProcess isCandidateCellVisible:]
+ +[TypistKeyboardDataInProcess isExtendedCandidateViewMode]
+ +[TypistKeyboardDataInProcess keyHasAccentedVariants:plane:keyplaneKeycaps:]
+ +[TypistKeyboardDataInProcess markedText]
+ +[TypistKeyboardDataInProcess removeKeyboards:]
+ +[TypistKeyboardDataInProcess setKeyboardUISettings:]
+ +[TypistKeyboardDataInProcess setKeyboards:]
+ +[TypistKeyboardDataInProcess setOneHandedKeyboardHandBias:]
+ +[TypistKeyboardDataInProcess setTIPreferences:]
+ +[TypistKeyboardDataInProcess shouldShowDictationKey]
+ +[TypistKeyboardDataInProcess shouldShowGlobeKey]
+ +[TypistKeyboardDataInProcess showCandidateAtIndex:]
+ +[TypistKeyboardDataInProcess showPopupVariantsForKey:key:plane:keyplaneKeycaps:]
+ +[TypistKeyboardDataInProcess switchToKeyboard:]
+ +[TypistKeyboardDataInProcess switchToPlane:]
+ +[TypistKeyboardDataInProcess updateCachedKeyplaneKeycaps:]
+ +[TypistKeyboardDataInputUIClient connectToRemoteKeyboard:]
+ +[TypistKeyboardDataInputUIClient connectToRemoteKeyboard:].cold.1
+ -[TypistKeyboardThai .cxx_destruct]
+ -[TypistKeyboardThai baseCharacters]
+ -[TypistKeyboardThai getPostfixKey:]
+ -[TypistKeyboardThai init:options:]
+ -[TypistKeyboardThai is24KeyThaiKeyboard]
+ -[TypistKeyboardThai setBaseCharacters:]
+ -[TypistKeyboardThai setIs24KeyThai:]
+ -[TypistKeyboardThai setupKeyboardInfo:options:]
+ -[TypistKeyboardThai usesMecabraCandidateBar]
+ GCC_except_table17
+ GCC_except_table24
+ GCC_except_table26
+ GCC_except_table28
+ GCC_except_table3
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table46
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table69
+ GCC_except_table73
+ GCC_except_table80
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table92
+ _CFPreferencesSetAppValue
+ _OBJC_CLASS_$_AFPreferences
+ _OBJC_CLASS_$_TypistKeyboardDataInProcess
+ _OBJC_CLASS_$_TypistKeyboardThai
+ _OBJC_CLASS_$_UIKeyboardInputMode
+ _OBJC_CLASS_$_UIKeyboardLayout
+ _OBJC_CLASS_$_UIKeyboardPreferencesController
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_TypistKeyboardThai._baseCharacters
+ _OBJC_IVAR_$_TypistKeyboardThai._is24KeyThai
+ _OBJC_METACLASS_$_TypistKeyboardDataInProcess
+ _OBJC_METACLASS_$_TypistKeyboardThai
+ _UIKBAttributeValueFixedLeftStr
+ _UIKBAttributeValueLeftStr
+ _UIKBAttributeValueStrictlyLeftStr
+ _UIKeyboardCurrencyVariants
+ _UIKeyboardGetCurrentInputMode
+ _UIKeyboardGetCurrentUILanguage
+ _UIKeyboardRomanAccentVariants
+ _UIKeyboardVariantDirection
+ _UIKeyboardVariantKeycaps
+ _UIKeyboardVariantStrings
+ __OBJC_$_CLASS_METHODS_TypistKeyboardDataInProcess
+ __OBJC_$_INSTANCE_METHODS_TypistKeyboardThai
+ __OBJC_$_INSTANCE_VARIABLES_TypistKeyboardThai
+ __OBJC_$_PROP_LIST_TypistKeyboardDataInProcess
+ __OBJC_$_PROP_LIST_TypistKeyboardThai
+ __OBJC_CLASS_PROTOCOLS_$_TypistKeyboardDataInProcess
+ __OBJC_CLASS_RO_$_TypistKeyboardDataInProcess
+ __OBJC_CLASS_RO_$_TypistKeyboardThai
+ __OBJC_METACLASS_RO_$_TypistKeyboardDataInProcess
+ __OBJC_METACLASS_RO_$_TypistKeyboardThai
+ ___38-[TypistKeyboard generateSwipeStream:]_block_invoke
+ ___38-[TypistKeyboard generateSwipeStream:]_block_invoke.486
+ ___41+[TypistKeyboardDataInProcess markedText]_block_invoke
+ ___44+[TypistKeyboardDataInProcess hasMarkedText]_block_invoke
+ ___44+[TypistKeyboardEmoji resetSelectedCategory]_block_invoke
+ ___45+[TypistKeyboardDataInProcess switchToPlane:]_block_invoke
+ ___46+[TypistKeyboardDataInProcess dismissKeyboard]_block_invoke
+ ___47+[TypistKeyboardDataInProcess getAllCandidates]_block_invoke
+ ___48+[TypistKeyboardDataInProcess switchToKeyboard:]_block_invoke
+ ___48+[TypistKeyboardDataInProcess switchToKeyboard:]_block_invoke_2
+ ___49+[TypistKeyboardDataInProcess getKeyboardLayout:]_block_invoke
+ ___49+[TypistKeyboardDataInProcess getKeyboardLayout:]_block_invoke_2
+ ___49+[TypistKeyboardDataInProcess getKeyboardLayout:]_block_invoke_3
+ ___49+[TypistKeyboardDataInProcess shouldShowGlobeKey]_block_invoke
+ ___50+[TypistKeyboardDataInProcess getCandidateBarRect]_block_invoke
+ ___50+[TypistKeyboardDataInProcess getCandidateCenter:]_block_invoke
+ ___50+[TypistKeyboardDataInProcess getWubiEnumeration:]_block_invoke
+ ___52+[TypistKeyboardDataInProcess getKeyboardUISettings]_block_invoke
+ ___52+[TypistKeyboardDataInProcess showCandidateAtIndex:]_block_invoke
+ ___53+[TypistKeyboardDataInProcess getVisibleKeyplaneName]_block_invoke
+ ___53+[TypistKeyboardDataInProcess setKeyboardUISettings:]_block_invoke
+ ___53+[TypistKeyboardDataInProcess shouldShowDictationKey]_block_invoke
+ ___54+[TypistKeyboardDataInProcess centerOfKey:withOffset:]_block_invoke
+ ___54+[TypistKeyboardDataInProcess getKeyplaneDescription:]_block_invoke
+ ___55+[TypistKeyboardDataInProcess findKeyBoundsInKeyboard:]_block_invoke
+ ___55+[TypistKeyboardDataInProcess getShuangpinEnumeration:]_block_invoke
+ ___55+[TypistKeyboardDataInProcess getVisibleCandidateList:]_block_invoke
+ ___55-[TypistKeyboard _getScaleInFrame:isPencil:dimensions:]_block_invoke
+ ___57+[TypistKeyboardDataInProcess getCandidateCenterAtIndex:]_block_invoke
+ ___58+[TypistKeyboardDataInProcess isExtendedCandidateViewMode]_block_invoke
+ ___59+[TypistKeyboardDataInProcess generateKeyplaneSwitchTable:]_block_invoke
+ ___59+[TypistKeyboardDataInProcess getRepresentedStringFromKey:]_block_invoke
+ ___61+[TypistKeyboardDataInProcess floatingKeyboardDraggablePoint]_block_invoke
+ ___65+[TypistKeyboardDataInProcess getKeyboardPlaneKeys:keys:inPlane:]_block_invoke
+ ___66+[TypistKeyboardDataInProcess _activeInputModesContainsInputMode:]_block_invoke
+ ___73+[TypistKeyboardDataInProcess addKeyboardGestureKeys:keys:inPlane:addTo:]_block_invoke
+ ___73+[TypistKeyboardDataInProcess getExtendedCandidateViewToggleButtonCenter]_block_invoke
+ ___75+[TypistKeyboardDataInProcess downActionFlagsForKey:plane:keyplaneKeycaps:]_block_invoke
+ ___76+[TypistKeyboardDataInProcess keyHasAccentedVariants:plane:keyplaneKeycaps:]_block_invoke
+ ___81+[TypistKeyboardDataInProcess showPopupVariantsForKey:key:plane:keyplaneKeycaps:]_block_invoke
+ ___81+[TypistKeyboardDataInProcess showPopupVariantsForKey:key:plane:keyplaneKeycaps:]_block_invoke_2
+ ___81+[TypistKeyboardDataInProcess showPopupVariantsForKey:key:plane:keyplaneKeycaps:]_block_invoke_3
+ ___87+[TypistKeyboardDataInProcess addKeyboardPopupKeys:keys:inPlane:addTo:keyplaneKeycaps:]_block_invoke
+ ___89+[TypistKeyboardDataInProcess generatePopupKeySubtrees:key:plane:layout:keyplaneKeycaps:]_block_invoke
+ ___block_descriptor_34_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e25_B32?0"NSString"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40r48r56r_e5_v8?0lr40l8r48l8s32l8r56l8
+ ___block_descriptor_64_e8_32s40r48r56r_e5_v8?0lr40l8s32l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_80_e8_32s40s48r56r64r_e5_v8?0lr48l8r56l8s32l8r64l8s40l8
+ ___block_descriptor_96_e8_32r40r48r56r_e5_v8?0lr32l8r40l8r48l8r56l8
+ ___block_descriptor_96_e8_32s40s48r56r64r72r80r_e5_v8?0lr48l8r56l8s32l8r64l8r72l8r80l8s40l8
+ ___block_literal_global.454
+ ___block_literal_global.541
+ ___block_literal_global.560
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ _getShuangpinEnumeration:.shuangpinOnceToken
+ _getShuangpinEnumeration:.shuangpinSchemaDictionary
+ _getWubiEnumeration:.wubiDictionary
+ _getWubiEnumeration:.wubiOnceToken
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$_changeToKeyplane:
+ _objc_msgSend$_floatingKeyboardDraggableRect
+ _objc_msgSend$_getAutocorrectionList
+ _objc_msgSend$_getCurrentKeyplaneName
+ _objc_msgSend$_getLocalizedInputMode
+ _objc_msgSend$_showSmallDisplayKeyplane
+ _objc_msgSend$_variantsByAppendingDualStringKey:toVariants:
+ _objc_msgSend$activeInputModes
+ _objc_msgSend$addKeyboardGestureKeys:keys:inPlane:addTo:
+ _objc_msgSend$addKeyboardPopupKeys:inPlane:addTo:keyplaneKeycaps:
+ _objc_msgSend$appendingSecondaryStringToVariantsTop:secondaryString:withDirection:
+ _objc_msgSend$autocorrectPrompt
+ _objc_msgSend$baseKeyForString:
+ _objc_msgSend$boolForPreferenceKey:
+ _objc_msgSend$calculateCoordinatesForFlickGesture:direction:offset:
+ _objc_msgSend$candidateList
+ _objc_msgSend$changeKeyNameToGenericCharacter:
+ _objc_msgSend$cleanUpSwitchTableBasedOnDefaultPlane:defaultPlaneName:
+ _objc_msgSend$componentName
+ _objc_msgSend$convertPoint:toLayer:
+ _objc_msgSend$convertRepresentedStringsIfNecessary:
+ _objc_msgSend$currentLocale
+ _objc_msgSend$determineDefaultPlane10Key:basePlaneName:
+ _objc_msgSend$determineDefaultPlane:basePlaneName:
+ _objc_msgSend$dictationIsEnabled
+ _objc_msgSend$displayType
+ _objc_msgSend$displayTypeHint
+ _objc_msgSend$downActionFlagsForKey:plane:keyplaneKeycaps:
+ _objc_msgSend$dynamicInsets
+ _objc_msgSend$dynamicLayout
+ _objc_msgSend$factory
+ _objc_msgSend$firstCachedKeyWithName:
+ _objc_msgSend$generatePopupKeySubtrees:key:plane:layout:keyplaneKeycaps:
+ _objc_msgSend$gestureKey
+ _objc_msgSend$getKeyboardPlaneKeys:keys:inPlane:
+ _objc_msgSend$getRootViewControllerViaScene
+ _objc_msgSend$getShuangpinEnumeration:
+ _objc_msgSend$getWubiEnumeration:
+ _objc_msgSend$globeKeyDisplaysAsEmojiKey
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$highlightedVariantsList
+ _objc_msgSend$identifier
+ _objc_msgSend$indexesOfObjectsPassingTest:
+ _objc_msgSend$interactionType
+ _objc_msgSend$is24KeyThaiKeyboard
+ _objc_msgSend$isAutoShifted
+ _objc_msgSend$isCandidateCellVisible:
+ _objc_msgSend$isExtendedList
+ _objc_msgSend$isShiftKeyPlaneChooser
+ _objc_msgSend$isShifted
+ _objc_msgSend$keyHasAccentedVariants:plane:keyplaneKeycaps:
+ _objc_msgSend$keyboardInputModeWithIdentifier:
+ _objc_msgSend$keyplaneNamed:
+ _objc_msgSend$keyplaneView
+ _objc_msgSend$keys
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$lowercaseStringWithLocale:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$objectsAtIndexes:
+ _objc_msgSend$performSelector:withObject:
+ _objc_msgSend$preferencesActions
+ _objc_msgSend$preparePopupVariantsForKey:onKeyplane:
+ _objc_msgSend$removeAutocorrectPromptAndCandidateList
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$rivenTranslationPreference
+ _objc_msgSend$searchForViewInKeyboardWindow:
+ _objc_msgSend$secondaryDisplayStrings
+ _objc_msgSend$secondaryRepresentedStrings
+ _objc_msgSend$selectedVariantIndex
+ _objc_msgSend$set
+ _objc_msgSend$setDictationIsEnabled:
+ _objc_msgSend$setDisplayString:
+ _objc_msgSend$setDisplayType:
+ _objc_msgSend$setHighlightedVariantsList:
+ _objc_msgSend$setKeyboardInputMode:userInitiated:
+ _objc_msgSend$setOneHandedKeyboardHandBias:
+ _objc_msgSend$setOverrideDisplayString:
+ _objc_msgSend$setRepresentedString:
+ _objc_msgSend$setSelectedVariantIndex:
+ _objc_msgSend$setState:
+ _objc_msgSend$setSubtrees:
+ _objc_msgSend$setSuppressDictationOptIn:
+ _objc_msgSend$setValue:forPreferenceKey:
+ _objc_msgSend$setVariantPopupBias:
+ _objc_msgSend$setup50OnFlick:forKey:keyName:planeName:
+ _objc_msgSend$setupTenKey:forKey:keyName:planeName:
+ _objc_msgSend$sharedPreferences
+ _objc_msgSend$shouldShowInternationalKey
+ _objc_msgSend$showPopupVariantsForKey:key:plane:keyplaneKeycaps:
+ _objc_msgSend$showsDedicatedEmojiKeyAlongsideGlobeButton
+ _objc_msgSend$state
+ _objc_msgSend$stringForProperty:
+ _objc_msgSend$subtrees
+ _objc_msgSend$supportsFloating
+ _objc_msgSend$synchronize
+ _objc_msgSend$synchronizePreferences
+ _objc_msgSend$traitsForKey:onKeyplane:
+ _objc_msgSend$updateCachedKeyplaneKeycaps:
+ _objc_msgSend$updateKeyboardHandBias:
+ _objc_msgSend$updateVariantTypeForActions:
+ _objc_msgSend$uppercaseStringWithLocale:
+ _objc_msgSend$valueForPreferenceKey:
+ _objc_msgSend$valueWithCGRect:
+ _objc_msgSend$valueWithUIEdgeInsets:
+ _objc_msgSend$variantType
+ _objc_msgSend$visible
+ _objc_msgSend$visibleCandidates
+ _objc_retainAutoreleasedReturnValue
- +[TypistKeyboardData setConnectionTimeout:]
- +[TypistKeyboardData setTargetApplication:]
- +[TypistKeyboardDataInputUIClient _attemptRemoteKeyboardConnection:targetApplication:]
- +[TypistKeyboardDataInputUIClient connectToRemoteKeyboard:targetApplication:]
- +[TypistKeyboardDataInputUIClient connectToRemoteKeyboard:targetApplication:].cold.1
- +[TypistKeyboardDataInputUIClient targetApplication]
- +[TypistKeyboardDataInputUIClient timeout]
- -[TypistKeyboardDataInputUIClient .cxx_destruct]
- -[TypistKeyboardDataInputUIClient setTargetApplication:]
- -[TypistKeyboardDataInputUIClient targetApplication]
- GCC_except_table4
- GCC_except_table82
- _OBJC_CLASS_$_NSUserDefaults
- _OBJC_IVAR_$_TypistKeyboardDataInputUIClient._targetApplication
- __OBJC_$_INSTANCE_METHODS_TypistKeyboardDataInputUIClient
- __OBJC_$_INSTANCE_VARIABLES_TypistKeyboardDataInputUIClient
- ___block_literal_global.453
- _objc_msgSend$_attemptRemoteKeyboardConnection:targetApplication:
- _objc_msgSend$connectToRemoteKeyboard:targetApplication:
- _objc_msgSend$integerForKey:
- _objc_msgSend$setInteger:forKey:
- _objc_msgSend$standardUserDefaults
- _objc_msgSend$stringForKey:
- _objc_msgSend$targetApplication
- _objc_msgSend$timeout
CStrings:
+ "\x01\x0e"
+ "\x02\x0e"
+ "\x03\x0e"
+ "\x04\x0e"
+ "\x05\x0e"
+ "\x06\x0e"
+ "\a\x0e"
+ "\b\x0e"
+ "\t\x0e"
+ "\n\x0e"
+ "\n------------------------------------ PREPROCESSING Plane:%@"
+ "\nplaneSwitchTable = %@"
+ "\v\x0e"
+ "\f\x0e"
+ "\r\x0e"
+ "\x0e\x0e"
+ "\x0f\x0e"
+ "\x10\x0e"
+ "\x11\x0e"
+ "\x12\x0e"
+ "\x13\x0e"
+ "\x14\x0e"
+ "\x15\x0e"
+ "\x16\x0e"
+ "\x17\x0e"
+ "\x18\x0e"
+ "\x19\x0e"
+ "\x1a\x0e"
+ "\x1b\x0e"
+ "\x1c\x0e"
+ "\x1d\x0e"
+ "\x1d "
+ "\x1e\x0e"
+ "\x1f\x0e"
+ " \x0e"
+ "                      ===> IGNORED"
+ "          { isAlphabet:%d, isShift:%d, isShiftChooser:%d, isLetters:%d }"
+ "      --> More  --> %@"
+ "      --> Shift --> %@"
+ "      --> Switch --> %@"
+ "!\x0e"
+ "\"\x0e"
+ "#\x0e"
+ "#####  DEFAULT PLANE: %@"
+ "########  PLANE NAME: %@"
+ "$\x0e"
+ "%\x0e"
+ "&\x0e"
+ "'\x0e"
+ "("
+ "(\x0e"
+ ")"
+ ")\x0e"
+ "*\x0e"
+ "+"
+ "+\x0e"
+ ",\x0e"
+ "-\x0e"
+ "-%@"
+ "-0-Plus"
+ "-split"
+ ".\x0e"
+ ".?!"
+ "/\x0e"
+ "0\x0e"
+ "1\x0e"
+ "2\x0e"
+ "24key"
+ "3\x0e"
+ "4\x0e"
+ "5\x0e"
+ "6\x0e"
+ "7\x0e"
+ "8\x0e"
+ "9\x0e"
+ ":\x0e"
+ "?\x0e"
+ "@\x0e"
+ "A\x0e"
+ "Active input mode list now contains %@"
+ "Added [%@] to list of keyboard IDs."
+ "Appending keyboards: %@\n to current list: %@"
+ "Assist"
+ "B\x0e"
+ "B24@0:8d16"
+ "B32@?0@\"NSString\"8Q16^B24"
+ "B40@0:8@16@24@32"
+ "B56@0:8@16@24@32@40@48"
+ "C\x0e"
+ "Changing AutoCapitalization Settings: Current=%d ChangeTo=%d"
+ "Changing AutoCorrection Settings: Current=%d ChangeTo=%d"
+ "Changing CapsLock Settings: Current=%d ChangeTo=%d"
+ "Changing CheckSpelling Settings: Current=%d ChangeTo=%d"
+ "Changing Dictation Settings: Current=%@ ChangeTo=%@"
+ "Changing Dictation Settings: Current=%d ChangeTo=%d"
+ "Changing Floating Settings: Current=%@ ChangeTo=%@"
+ "Changing Fuzzy Settings: Current=%d ChangeTo=%d"
+ "Changing GestureKey Settings: Current=%d ChangeTo=%d"
+ "Changing HandBias for One-Handed Keyboard: Current=%@ ChangeTo=%@"
+ "Changing KeyPaddle Settings: Current=%d ChangeTo=%d"
+ "Changing PeriodShortcut Settings: Current=%d ChangeTo=%d"
+ "Changing Predictive Settings: Current=%d ChangeTo=%d"
+ "Changing Shaungpin Settings: Current=%i, ChangeTo=%i"
+ "Changing SmallDisplay Settings: Current=%d ChangeTo=%d"
+ "Changing Smart Dashes Settings: Current=%d ChangeTo=%d"
+ "Changing Smart Full-width Settings: Current=%d ChangeTo=%d"
+ "Changing Smart Quotes Settings: Current=%d ChangeTo=%d"
+ "Changing Typology Settings: Current=%d ChangeTo=%d"
+ "Changing Use CapsLock as Roman Switch Settings: Current=%d ChangeTo=%d"
+ "Changing Wubi Standard Settings: Current=%i, ChangeTo=%i"
+ "Current Keyboards are\n%@"
+ "D\x0e"
+ "Dictation"
+ "Dock and Merge"
+ "E\x0e"
+ "Emoji"
+ "F\x0e"
+ "Floating"
+ "G\x0e"
+ "H\x0e"
+ "HandBias for One-Handed Keyboard is already set to %@"
+ "HandBias for One-Handed Keyboard is changed to %@  %@"
+ "I\x0e"
+ "J\x0e"
+ "K\x0e"
+ "Keyboard [%@] already exists. Skipping..."
+ "L\x0e"
+ "Localizable"
+ "M\x0e"
+ "MecabraWubixingStandard86"
+ "MecabraWubixingStandard98"
+ "MecabraWubixingStandardNewCentury"
+ "New Keyboard is\n%@"
+ "New Keyboards are\n%@"
+ "New Keyboards are:\n%@"
+ "None"
+ "Not floating"
+ "NumberPad"
+ "NumberPad-"
+ "P\x0e"
+ "Plane: %@, Gesture keys -> %@"
+ "Plane: %@, Keys -> %@"
+ "Plane: %@, Popup keys -> %@"
+ "Q\x0e"
+ "Q40@0:8@16@24@32"
+ "R\x0e"
+ "Removed [%@] from the list of keyboards."
+ "Removing keyboard: %@"
+ "Replacing keyboards with: %@"
+ "S\x0e"
+ "ShuangpinTypeMicrosoft"
+ "ShuangpinTypeNone"
+ "ShuangpinTypePinyinJiajia"
+ "ShuangpinTypeSogou"
+ "ShuangpinTypeXiaohe"
+ "ShuangpinTypeZhinengABC"
+ "ShuangpinTypeZiguang"
+ "ShuangpinTypeZiranma"
+ "Switched keyboard to %@"
+ "T\x0e"
+ "TB,N,Gis24KeyThaiKeyboard,V_is24KeyThai"
+ "TUICandidateArrowButton"
+ "Timed out while waiting for activeInputMode to contain %@"
+ "Too many secondaryRepresentedStrings on key '%@'. Unable to determine gesture direction."
+ "TypistKeyboardDataInProcess"
+ "TypistKeyboardThai"
+ "U\x0e"
+ "UIKeyboardCandidateBarCell"
+ "UIKeyboardCandidateGridCell"
+ "UIKeyboardCandidateUnsplitKeyboardToggleButton"
+ "UIKeyboardSplitControlMenu"
+ "Unable to remove [%@] since the ID does not match any keyboard in the current set"
+ "Unable to switch to keyboard [%@] after %ld"
+ "V\x0e"
+ "W\x0e"
+ "X\x0e"
+ "Y\x0e"
+ "[%@] cannot be removed, becuase it's the only keyboard enabled. Aborting..."
+ "[%@]: An error was encountered when trying to tap candidate at index %li: \"%@\""
+ "[%@{%@}]"
+ "[Timeout...]"
+ "[addKeyboardGestureKeys] - FAILURE - keys or planeName is missing!"
+ "_activeInputModesContainsInputMode:"
+ "_changeToKeyplane:"
+ "_floatingKeyboardDraggableRect"
+ "_getAutocorrectionList"
+ "_getCurrentKeyplaneName"
+ "_getLocalizedInputMode"
+ "_is24KeyThai"
+ "_showSmallDisplayKeyplane"
+ "_variantsByAppendingDualStringKey:toVariants:"
+ "actionForItem:"
+ "activeInputModes"
+ "addKeyboardGestureKeys:keys:inPlane:addTo:"
+ "appendingSecondaryStringToVariantsTop:secondaryString:withDirection:"
+ "autocorrectPrompt"
+ "baseKeyForString:"
+ "boolForPreferenceKey:"
+ "candidateList"
+ "cleanUpSwitchTableBasedOnDefaultPlane:defaultPlaneName:"
+ "com.apple.Accessibility"
+ "componentName"
+ "convertPoint:toLayer:"
+ "copy-"
+ "currentLocale"
+ "cut-"
+ "determineDefaultPlane10Key:basePlaneName:"
+ "determineDefaultPlane:basePlaneName:"
+ "dictationIsEnabled"
+ "displayType"
+ "displayTypeHint"
+ "downActionFlagsForKey:plane:keyplaneKeycaps:"
+ "dynamicInsets"
+ "dynamicLayout"
+ "factory"
+ "firstCachedKeyWithName:"
+ "generatePopupKeySubtrees:key:plane:layout:keyplaneKeycaps:"
+ "gestureKey"
+ "getKeyboardPlaneKeys:keys:inPlane:"
+ "getShuangpinEnumeration:"
+ "getWubiEnumeration:"
+ "globeKeyDisplaysAsEmojiKey"
+ "hasSuffix:"
+ "highlightedVariantsList"
+ "identifier"
+ "indexesOfObjectsPassingTest:"
+ "interactionType"
+ "is24KeyThai"
+ "is24KeyThaiKeyboard"
+ "isAutoShifted"
+ "isCandidateCellVisible:"
+ "isExtendedList"
+ "isShiftKeyPlaneChooser"
+ "isShifted"
+ "keyHasAccentedVariants:plane:keyplaneKeycaps:"
+ "keyboard"
+ "keyboardInputModeWithIdentifier:"
+ "keyname"
+ "keyplaneNamed:"
+ "keyplaneView"
+ "keys"
+ "ko_KR@sw=Korean;hw=Automatic"
+ "left"
+ "localizedStringForKey:value:table:"
+ "lowercaseStringWithLocale:"
+ "maybeDefaultPlane"
+ "more-alternate"
+ "more-alternate-small-display"
+ "numberWithInt:"
+ "objectsAtIndexes:"
+ "paste-"
+ "preferencesActions"
+ "preparePopupVariantsForKey:onKeyplane:"
+ "removeAutocorrectPromptAndCandidateList"
+ "replaceObjectAtIndex:withObject:"
+ "right"
+ "rivenTranslationPreference"
+ "second-alternate"
+ "secondaryDisplayString"
+ "secondaryDisplayStrings"
+ "secondaryRepresentedStrings"
+ "selectedVariantIndex"
+ "set"
+ "setDictationIsEnabled:"
+ "setDisplayString:"
+ "setDisplayType:"
+ "setHighlightedVariantsList:"
+ "setIs24KeyThai:"
+ "setKeyboardInputMode:userInitiated:"
+ "setOverrideDisplayString:"
+ "setRepresentedString:"
+ "setSelectedVariantIndex:"
+ "setState:"
+ "setSubtrees:"
+ "setSuppressDictationOptIn:"
+ "setValue:forPreferenceKey:"
+ "setVariantPopupBias:"
+ "sharedPreferences"
+ "shift-alternate"
+ "shift-alternate-small-display"
+ "shouldShowInternationalKey"
+ "showPopupVariantsForKey:key:plane:keyplaneKeycaps:"
+ "showsDedicatedEmojiKeyAlongsideGlobeButton"
+ "state"
+ "stringForProperty:"
+ "subtrees"
+ "supportsFloating"
+ "synchronize"
+ "synchronizePreferences"
+ "th_TH"
+ "traitsForKey:onKeyplane:"
+ "updateCachedKeyplaneKeycaps:"
+ "updateKeyboardHandBias:"
+ "updateVariantTypeForActions:"
+ "uppercaseStringWithLocale:"
+ "valueForPreferenceKey:"
+ "valueWithCGRect:"
+ "valueWithUIEdgeInsets:"
+ "variantType"
+ "visible"
+ "visibleCandidates"
- "B32@0:8d16@24"
- "No target application bundle id is provided for IP keyboard."
- "T@\"NSString\",C,N,V_targetApplication"
- "_attemptRemoteKeyboardConnection:targetApplication:"
- "_targetApplication"
- "connectToRemoteKeyboard:targetApplication:"
- "integerForKey:"
- "setConnectionTimeout:"
- "setInteger:forKey:"
- "setTargetApplication:"
- "standardUserDefaults"
- "stringForKey:"
- "targetApplication"
- "timeout"

```
