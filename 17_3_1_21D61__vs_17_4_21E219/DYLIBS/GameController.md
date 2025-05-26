## GameController

> `/System/Library/Frameworks/GameController.framework/GameController`

```diff

-11.3.1.0.0
-  __TEXT.__text: 0xe06f0
-  __TEXT.__auth_stubs: 0x1760
+11.4.11.0.0
+  __TEXT.__text: 0xe6bfc
+  __TEXT.__auth_stubs: 0x1770
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xbd50
-  __TEXT.__const: 0x30b4
-  __TEXT.__cstring: 0x8fcf
-  __TEXT.__gcc_except_tab: 0x3f90
-  __TEXT.__oslogstring: 0x9a89
+  __TEXT.__objc_methlist: 0xc1a8
+  __TEXT.__const: 0x30f4
+  __TEXT.__cstring: 0x8cc3
+  __TEXT.__gcc_except_tab: 0x4160
+  __TEXT.__oslogstring: 0x9b00
   __TEXT.__dlopen_cstrs: 0xf8
   __TEXT.__swift5_typeref: 0x2ca
   __TEXT.__swift5_reflstr: 0x12f

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x4020
+  __TEXT.__unwind_info: 0x41d4
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x38d4
-  __TEXT.__objc_methname: 0x179e8
-  __TEXT.__objc_methtype: 0x733a
-  __TEXT.__objc_stubs: 0xeac0
-  __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0x2bf8
-  __DATA_CONST.__objc_classlist: 0x790
-  __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x6f0
+  __TEXT.__objc_classname: 0x3c06
+  __TEXT.__objc_methname: 0x17ed2
+  __TEXT.__objc_methtype: 0x75a4
+  __TEXT.__objc_stubs: 0xebe0
+  __DATA_CONST.__got: 0x540
+  __DATA_CONST.__const: 0x2cd8
+  __DATA_CONST.__objc_classlist: 0x800
+  __DATA_CONST.__objc_catlist: 0xa0
+  __DATA_CONST.__objc_protolist: 0x760
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3b670
-  __DATA_CONST.__objc_selrefs: 0x4cd0
+  __DATA_CONST.__objc_const: 0x3e2c0
+  __DATA_CONST.__objc_selrefs: 0x4da8
+  __DATA_CONST.__objc_protorefs: 0x488
+  __DATA_CONST.__objc_classrefs: 0x970
+  __DATA_CONST.__objc_superrefs: 0x788
   __DATA_CONST.__objc_arraydata: 0x740
-  __AUTH_CONST.__objc_const: 0x6088
-  __AUTH_CONST.__cfstring: 0x9e60
-  __AUTH_CONST.__const: 0x1780
+  __AUTH_CONST.__objc_const: 0x66a0
+  __AUTH_CONST.__cfstring: 0xa280
+  __AUTH_CONST.__const: 0x17a0
   __AUTH_CONST.__objc_intobj: 0x13b0
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0xbc8
-  __AUTH.__objc_data: 0x3fc0
+  __AUTH_CONST.__auth_got: 0xbd0
+  __AUTH.__objc_data: 0x4420
   __AUTH.__data: 0xb0
   __DATA.__got_weak: 0x8
-  __DATA.__objc_protorefs: 0x488
-  __DATA.__objc_classrefs: 0x910
-  __DATA.__objc_superrefs: 0x6e8
-  __DATA.__objc_ivar: 0x14e0
-  __DATA.__data: 0x5320
+  __DATA.__objc_ivar: 0x1598
+  __DATA.__data: 0x5890
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1380
+  __DATA.__bss: 0x13e0
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__bss: 0x180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5750
-  Symbols:   21542
-  CStrings:  7761
+  Functions: 5916
+  Symbols:   22192
+  CStrings:  7910
 
Symbols:
+ +[GCDevicePhysicalInputCapacitiveButtonElementDescription(Client) parametersClass]
+ +[GCDevicePhysicalInputCapacitiveDirectionPadElementDescription(Client) parametersClass]
+ +[GCKeyboardAndMouseManager managerWithQueue:]
+ +[NSValue(GCTypes) valueWithGCPoint2:]
+ +[_GCDevicePhysicalInputAxis2DInput updateContextSize]
+ +[_GCDevicePhysicalInputCapacitiveButtonElement updateContextSize]
+ +[_GCDevicePhysicalInputCapacitiveDirectionPadElement updateContextSize]
+ +[_GCDevicePhysicalInputTouchedStateInput updateContextSize]
+ -[GCDevicePhysicalInputCapacitiveButtonElementDescription(Client) makeParameters]
+ -[GCDevicePhysicalInputCapacitiveDirectionPadElementDescription(Client) makeParameters]
+ -[GCKeyboardAndMouseManagerImpl .cxx_destruct]
+ -[GCKeyboardAndMouseManagerImpl _onqueue_addMouse:]
+ -[GCKeyboardAndMouseManagerImpl _onqueue_addMouse:].cold.1
+ -[GCKeyboardAndMouseManagerImpl _onqueue_addMouse:].cold.2
+ -[GCKeyboardAndMouseManagerImpl _onqueue_addMouse:].cold.3
+ -[GCKeyboardAndMouseManagerImpl _onqueue_addMouse:].cold.4
+ -[GCKeyboardAndMouseManagerImpl _onqueue_ensureEmulatedControllerWithDevice:added:]
+ -[GCKeyboardAndMouseManagerImpl _onqueue_publishKeyboard:]
+ -[GCKeyboardAndMouseManagerImpl _onqueue_publishMouse:]
+ -[GCKeyboardAndMouseManagerImpl _onqueue_refreshKeyboards]
+ -[GCKeyboardAndMouseManagerImpl _onqueue_removeMouse:]
+ -[GCKeyboardAndMouseManagerImpl _onqueue_unpublishKeyboard:]
+ -[GCKeyboardAndMouseManagerImpl _onqueue_unpublishMouse:]
+ -[GCKeyboardAndMouseManagerImpl addDeviceWithServiceRef:]
+ -[GCKeyboardAndMouseManagerImpl addDeviceWithServiceRef:].cold.1
+ -[GCKeyboardAndMouseManagerImpl addDeviceWithServiceRef:].cold.2
+ -[GCKeyboardAndMouseManagerImpl coalescedKeyboard]
+ -[GCKeyboardAndMouseManagerImpl currentMouse]
+ -[GCKeyboardAndMouseManagerImpl emulatedControllerMapping]
+ -[GCKeyboardAndMouseManagerImpl handleHIDEvent:]
+ -[GCKeyboardAndMouseManagerImpl handleHIDEvent:atTimestamp:forSubject:]
+ -[GCKeyboardAndMouseManagerImpl initWithQueue:]
+ -[GCKeyboardAndMouseManagerImpl keyboardHIDServices]
+ -[GCKeyboardAndMouseManagerImpl mice]
+ -[GCKeyboardAndMouseManagerImpl observeValueForKeyPath:ofObject:change:context:]
+ -[GCKeyboardAndMouseManagerImpl removeDeviceWithServiceRef:]
+ -[GCKeyboardAndMouseManagerImpl setCurrentMouse:]
+ -[GCKeyboardAndMouseManagerImpl setCurrentMouse:].cold.1
+ -[GCKeyboardAndMouseManagerImpl setCurrentMouse:].cold.2
+ -[GCKeyboardAndMouseManagerImpl setEmulatedControllerEnabled:]
+ -[GCKeyboardAndMouseManagerImpl setEmulatedControllerMapping:]
+ -[GCKeyboardAndMouseManagerImpl setKeyboardHIDServices:]
+ -[GCKeyboardAndMouseManagerImpl updateCurrentMouseAfterDisconnecting:]
+ -[GCMouse initWithName:additionalButtons:]
+ -[GCMouse init]
+ -[GCMouseInput initWithIdentifier:]
+ -[GCMouseInput initWithIdentifier:additionalButtons:]
+ -[GCMouseInput(PubSub) _handleButtonEventType:buttonMask:]
+ -[GCMouseInput(PubSub) handleDigitizerEvent:]
+ -[GCMouseInput(PubSub) handleMouseButtonEventAddingButtonMask:]
+ -[GCMouseInput(PubSub) handleMouseButtonEventRemovingButtonMask:]
+ -[GCMouseInput(PubSub) handleMouseButtonEventSettingButtonMask:]
+ -[GCMouseInput(PubSub) handleMouseMovementEventWithDelta:]
+ -[GCMouseInput(PubSub) handleScrollEventWithDelta:]
+ -[GCMouseInput(PubSub) setButtonEventSource:]
+ -[GCMouseInput(PubSub) setDigitizerEventSource:]
+ -[GCMouseInput(PubSub) setPointerEventSource:]
+ -[GCMouseInput(PubSub) setScrollEventSource:]
+ -[NSValue(GCTypes) GCPoint2Value]
+ -[_GCButtonEventImpl copyWithZone:]
+ -[_GCButtonEventImpl initWithButtonEvent:]
+ -[_GCButtonEventImpl mask]
+ -[_GCButtonEventImpl setMask:]
+ -[_GCButtonEventImpl setTimestamp:]
+ -[_GCButtonEventImpl timestamp]
+ -[_GCControllerManager appInBackground]
+ -[_GCControllerManager(Legacy) enableKeyboardAndMouseSupport]
+ -[_GCDevicePhysicalInputAxis2DInput __setLastValueTimestamp:]
+ -[_GCDevicePhysicalInputAxis2DInput __setValue:]
+ -[_GCDevicePhysicalInputAxis2DInput _canWrap]
+ -[_GCDevicePhysicalInputAxis2DInput _isAnalog]
+ -[_GCDevicePhysicalInputAxis2DInput _lastValueTimestamp]
+ -[_GCDevicePhysicalInputAxis2DInput _setAnalog:]
+ -[_GCDevicePhysicalInputAxis2DInput _setCanWrap:]
+ -[_GCDevicePhysicalInputAxis2DInput _setLastValueTimestamp:]
+ -[_GCDevicePhysicalInputAxis2DInput _setSources:]
+ -[_GCDevicePhysicalInputAxis2DInput _setValue:]
+ -[_GCDevicePhysicalInputAxis2DInput _setValueDidChangeHandler:]
+ -[_GCDevicePhysicalInputAxis2DInput _sources]
+ -[_GCDevicePhysicalInputAxis2DInput _valueDidChangeHandler]
+ -[_GCDevicePhysicalInputAxis2DInput _value]
+ -[_GCDevicePhysicalInputAxis2DInput canWrap]
+ -[_GCDevicePhysicalInputAxis2DInput initWithParameters:]
+ -[_GCDevicePhysicalInputAxis2DInput initWithTemplate:context:]
+ -[_GCDevicePhysicalInputAxis2DInput init]
+ -[_GCDevicePhysicalInputAxis2DInput isAnalog]
+ -[_GCDevicePhysicalInputAxis2DInput isEqualToInput:]
+ -[_GCDevicePhysicalInputAxis2DInput lastValueLatency]
+ -[_GCDevicePhysicalInputAxis2DInput lastValueTimestamp]
+ -[_GCDevicePhysicalInputAxis2DInput postCommit:sender:]
+ -[_GCDevicePhysicalInputAxis2DInput preCommit:sender:]
+ -[_GCDevicePhysicalInputAxis2DInput setValueDidChangeHandler:]
+ -[_GCDevicePhysicalInputAxis2DInput sources]
+ -[_GCDevicePhysicalInputAxis2DInput update:forUsages:with:]
+ -[_GCDevicePhysicalInputAxis2DInput update:withValue:timestamp:]
+ -[_GCDevicePhysicalInputAxis2DInput valueDidChangeHandler]
+ -[_GCDevicePhysicalInputAxis2DInput value]
+ -[_GCDevicePhysicalInputAxis2DInputParameters .cxx_destruct]
+ -[_GCDevicePhysicalInputAxis2DInputParameters canWrap]
+ -[_GCDevicePhysicalInputAxis2DInputParameters copyWithZone:]
+ -[_GCDevicePhysicalInputAxis2DInputParameters init]
+ -[_GCDevicePhysicalInputAxis2DInputParameters isAnalog]
+ -[_GCDevicePhysicalInputAxis2DInputParameters isEqual:]
+ -[_GCDevicePhysicalInputAxis2DInputParameters setAnalog:]
+ -[_GCDevicePhysicalInputAxis2DInputParameters setCanWrap:]
+ -[_GCDevicePhysicalInputAxis2DInputParameters setSources:]
+ -[_GCDevicePhysicalInputAxis2DInputParameters sources]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement _lastTouchedTimestamp]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement _setLastTouchedTimestamp:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement _setTouchedDidChangeHandler:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement _setTouchedValue:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement _setTouchedValueField:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement _touchedDidChangeHandler]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement _touchedValueField]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement _touchedValue]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement initWithParameters:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement initWithTemplate:context:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement isEqualToElement:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement isTouched]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement lastTouchedStateLatency]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement lastTouchedStateTimestamp]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement postCommit:sender:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement preCommit:sender:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement setTouchedDidChangeHandler:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement touchedDidChangeHandler]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement touchedInput]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement update:forGamepadEvent:withTimestamp:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElement update:forUsages:with:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElementParameters copyWithZone:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElementParameters eventTouchedValueField]
+ -[_GCDevicePhysicalInputCapacitiveButtonElementParameters init]
+ -[_GCDevicePhysicalInputCapacitiveButtonElementParameters isEqual:]
+ -[_GCDevicePhysicalInputCapacitiveButtonElementParameters setEventTouchedValueField:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement _setTouchedValueField:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement _touchedInput]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement _touchedValueField]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement description]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement initWithParameters:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement initWithTemplate:context:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement isEqualToElement:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement postCommit:sender:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement preCommit:sender:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement touchedInput]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement update:forGamepadEvent:withTimestamp:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement update:forUsages:with:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElementParameters .cxx_destruct]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElementParameters copyWithZone:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElementParameters eventTouchedValueField]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElementParameters init]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElementParameters isEqual:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElementParameters setEventTouchedValueField:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElementParameters setTouchedSources:]
+ -[_GCDevicePhysicalInputCapacitiveDirectionPadElementParameters touchedSources]
+ -[_GCDevicePhysicalInputDirectionPadElement _xy]
+ -[_GCDevicePhysicalInputDirectionPadElement xyAxes]
+ -[_GCDevicePhysicalInputDirectionPadElementParameters setXySources:]
+ -[_GCDevicePhysicalInputDirectionPadElementParameters xySources]
+ -[_GCDevicePhysicalInputTouchedStateInput __setLastTouchedTimestamp:]
+ -[_GCDevicePhysicalInputTouchedStateInput __setTouched:]
+ -[_GCDevicePhysicalInputTouchedStateInput _lastTouchedTimestamp]
+ -[_GCDevicePhysicalInputTouchedStateInput _setLastTouchedTimestamp:]
+ -[_GCDevicePhysicalInputTouchedStateInput _setSources:]
+ -[_GCDevicePhysicalInputTouchedStateInput _setTouched:]
+ -[_GCDevicePhysicalInputTouchedStateInput _setTouchedDidChangeHandler:]
+ -[_GCDevicePhysicalInputTouchedStateInput _sources]
+ -[_GCDevicePhysicalInputTouchedStateInput _touchedDidChangeHandler]
+ -[_GCDevicePhysicalInputTouchedStateInput _touched]
+ -[_GCDevicePhysicalInputTouchedStateInput description]
+ -[_GCDevicePhysicalInputTouchedStateInput initWithParameters:]
+ -[_GCDevicePhysicalInputTouchedStateInput initWithTemplate:context:]
+ -[_GCDevicePhysicalInputTouchedStateInput init]
+ -[_GCDevicePhysicalInputTouchedStateInput isEqualToInput:]
+ -[_GCDevicePhysicalInputTouchedStateInput isTouched]
+ -[_GCDevicePhysicalInputTouchedStateInput lastTouchedStateLatency]
+ -[_GCDevicePhysicalInputTouchedStateInput lastTouchedStateTimestamp]
+ -[_GCDevicePhysicalInputTouchedStateInput postCommit:sender:]
+ -[_GCDevicePhysicalInputTouchedStateInput preCommit:sender:]
+ -[_GCDevicePhysicalInputTouchedStateInput setTouchedDidChangeHandler:]
+ -[_GCDevicePhysicalInputTouchedStateInput sources]
+ -[_GCDevicePhysicalInputTouchedStateInput touchedDidChangeHandler]
+ -[_GCDevicePhysicalInputTouchedStateInput update:forUsages:with:]
+ -[_GCDevicePhysicalInputTouchedStateInput update:withValue:timestamp:]
+ -[_GCDevicePhysicalInputTouchedStateInputParameters .cxx_destruct]
+ -[_GCDevicePhysicalInputTouchedStateInputParameters copyWithZone:]
+ -[_GCDevicePhysicalInputTouchedStateInputParameters init]
+ -[_GCDevicePhysicalInputTouchedStateInputParameters isEqual:]
+ -[_GCDevicePhysicalInputTouchedStateInputParameters setSources:]
+ -[_GCDevicePhysicalInputTouchedStateInputParameters sources]
+ -[_GCDigitizerEventImpl copyWithZone:]
+ -[_GCDigitizerEventImpl initWithDigitizerEvent:]
+ -[_GCDigitizerEventImpl setTimestamp:]
+ -[_GCDigitizerEventImpl setX:]
+ -[_GCDigitizerEventImpl setY:]
+ -[_GCDigitizerEventImpl timestamp]
+ -[_GCDigitizerEventImpl x]
+ -[_GCDigitizerEventImpl y]
+ -[_GCGamepadEventImpl buttonBackLeftPrimary]
+ -[_GCGamepadEventImpl buttonBackLeftSecondary]
+ -[_GCGamepadEventImpl buttonBackRightPrimary]
+ -[_GCGamepadEventImpl buttonBackRightSecondary]
+ -[_GCGamepadEventImpl buttonLeftBumper]
+ -[_GCGamepadEventImpl buttonRightBumper]
+ -[_GCGamepadEventImpl setButtonBackLeftPrimary:]
+ -[_GCGamepadEventImpl setButtonBackLeftSecondary:]
+ -[_GCGamepadEventImpl setButtonBackRightPrimary:]
+ -[_GCGamepadEventImpl setButtonBackRightSecondary:]
+ -[_GCGamepadEventImpl setButtonLeftBumper:]
+ -[_GCGamepadEventImpl setButtonRightBumper:]
+ -[_GCKeyboardAndMouseEventSubject .cxx_destruct]
+ -[_GCKeyboardAndMouseEventSubject addMaskAndPublishButtonEvent:atTimestamp:]
+ -[_GCKeyboardAndMouseEventSubject buttonEventObservers]
+ -[_GCKeyboardAndMouseEventSubject digitizerEventObservers]
+ -[_GCKeyboardAndMouseEventSubject init]
+ -[_GCKeyboardAndMouseEventSubject keyboardEventObservers]
+ -[_GCKeyboardAndMouseEventSubject pointerEventObservers]
+ -[_GCKeyboardAndMouseEventSubject publishButtonEvent:]
+ -[_GCKeyboardAndMouseEventSubject publishDigitizerEvent:]
+ -[_GCKeyboardAndMouseEventSubject publishKeyboardEvent:]
+ -[_GCKeyboardAndMouseEventSubject publishPointerEvent:]
+ -[_GCKeyboardAndMouseEventSubject publishScrollEvent:]
+ -[_GCKeyboardAndMouseEventSubject removeMaskAndPublishButtonEvent:atTimestamp:]
+ -[_GCKeyboardAndMouseEventSubject scrollEventObservers]
+ -[_GCKeyboardAndMouseEventSubject setButtonEventObservers:]
+ -[_GCKeyboardAndMouseEventSubject setDigitizerEventObservers:]
+ -[_GCKeyboardAndMouseEventSubject setKeyboardEventObservers:]
+ -[_GCKeyboardAndMouseEventSubject setPointerEventObservers:]
+ -[_GCKeyboardAndMouseEventSubject setScrollEventObservers:]
+ -[_GCKeyboardAndMouseEventSubject(Button) observeButtonEvents:]
+ -[_GCKeyboardAndMouseEventSubject(Digitizer) observeDigitizerEvents:]
+ -[_GCKeyboardAndMouseEventSubject(Keyboard) observeKeyboardEvents:]
+ -[_GCKeyboardAndMouseEventSubject(Pointer) observePointerEvents:]
+ -[_GCKeyboardAndMouseEventSubject(Scroll) observeScrollEvents:]
+ -[_GCPointerEventImpl copyWithZone:]
+ -[_GCPointerEventImpl initWithPointerEvent:]
+ -[_GCPointerEventImpl setTimestamp:]
+ -[_GCPointerEventImpl setX:]
+ -[_GCPointerEventImpl setY:]
+ -[_GCPointerEventImpl timestamp]
+ -[_GCPointerEventImpl x]
+ -[_GCPointerEventImpl y]
+ -[_GCScrollEventImpl copyWithZone:]
+ -[_GCScrollEventImpl initWithScrollEvent:]
+ -[_GCScrollEventImpl setTimestamp:]
+ -[_GCScrollEventImpl setX:]
+ -[_GCScrollEventImpl setY:]
+ -[_GCScrollEventImpl timestamp]
+ -[_GCScrollEventImpl x]
+ -[_GCScrollEventImpl y]
+ GCC_except_table46
+ _$s14GameController19GCButtonElementNameV10leftBumperACvau
+ _$s14GameController19GCButtonElementNameV10leftBumperACvgZ
+ _$s14GameController19GCButtonElementNameV10leftBumperACvpZ
+ _$s14GameController19GCButtonElementNameV10leftBumper_WZ
+ _$s14GameController19GCButtonElementNameV10leftBumper_Wz
+ _$s14GameController19GCButtonElementNameV11rightBumperACvau
+ _$s14GameController19GCButtonElementNameV11rightBumperACvgZ
+ _$s14GameController19GCButtonElementNameV11rightBumperACvpZ
+ _$s14GameController19GCButtonElementNameV11rightBumper_WZ
+ _$s14GameController19GCButtonElementNameV11rightBumper_Wz
+ _$s14GameController19GCButtonElementNameV14backLeftButton8positionACSi_tFZ
+ _$s14GameController19GCButtonElementNameV14backLeftButton8positionACSi_tFZTm
+ _$s14GameController19GCButtonElementNameV15backRightButton8positionACSi_tFZ
+ _CFStringCreateWithFormat
+ _GCFLOC_BUTTON_L4
+ _GCFLOC_BUTTON_M1
+ _GCFLOC_BUTTON_M2
+ _GCFLOC_BUTTON_M3
+ _GCFLOC_BUTTON_M4
+ _GCFLOC_BUTTON_R4
+ _GCInputBackLeftButton
+ _GCInputBackLeftPrimaryButton
+ _GCInputBackLeftSecondaryButton
+ _GCInputBackRightButton
+ _GCInputBackRightPrimaryButton
+ _GCInputBackRightSecondaryButton
+ _GCInputLeftBumper
+ _GCInputRightBumper
+ _GCPoint2Zero
+ _NSStringFromGCPoint2
+ _OBJC_CLASS_$_GCDevicePhysicalInputCapacitiveButtonElementDescription
+ _OBJC_CLASS_$_GCDevicePhysicalInputCapacitiveDirectionPadElementDescription
+ _OBJC_CLASS_$_GCKeyboardAndMouseManagerImpl
+ _OBJC_CLASS_$__GCButtonEventImpl
+ _OBJC_CLASS_$__GCDevicePhysicalInputAxis2DInput
+ _OBJC_CLASS_$__GCDevicePhysicalInputAxis2DInputParameters
+ _OBJC_CLASS_$__GCDevicePhysicalInputCapacitiveButtonElement
+ _OBJC_CLASS_$__GCDevicePhysicalInputCapacitiveButtonElementParameters
+ _OBJC_CLASS_$__GCDevicePhysicalInputCapacitiveDirectionPadElement
+ _OBJC_CLASS_$__GCDevicePhysicalInputCapacitiveDirectionPadElementParameters
+ _OBJC_CLASS_$__GCDevicePhysicalInputTouchedStateInput
+ _OBJC_CLASS_$__GCDevicePhysicalInputTouchedStateInputParameters
+ _OBJC_CLASS_$__GCDigitizerEventImpl
+ _OBJC_CLASS_$__GCKeyboardAndMouseEventSubject
+ _OBJC_CLASS_$__GCPointerEventImpl
+ _OBJC_CLASS_$__GCScrollEventImpl
+ _OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._coalescedKeyboard
+ _OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._currentMouse
+ _OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._devicesQueue
+ _OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._emulatedController
+ _OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._emulatedControllerMapping
+ _OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._hidServiceSubjects
+ _OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._keyboardHIDServices
+ _OBJC_IVAR_$_GCKeyboardAndMouseManagerImpl._mice
+ _OBJC_IVAR_$_GCMouse._handlerQueue
+ _OBJC_IVAR_$_GCMouse._mouseInput
+ _OBJC_IVAR_$_GCMouse._vendorName
+ _OBJC_IVAR_$_GCMouseInput._buttonEventObservation
+ _OBJC_IVAR_$_GCMouseInput._digitizerEventObservation
+ _OBJC_IVAR_$_GCMouseInput._pointerEventObservation
+ _OBJC_IVAR_$_GCMouseInput._scrollEventObservation
+ _OBJC_IVAR_$__GCButtonEventImpl.mask
+ _OBJC_IVAR_$__GCButtonEventImpl.timestamp
+ _OBJC_IVAR_$__GCDevicePhysicalInputAxis2DInput._canWrapSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputAxis2DInput._isAnalogSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputAxis2DInput._sourcesSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputAxis2DInput._valueChangedHandlerSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputAxis2DInput._valueSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputAxis2DInput._valueTimestampSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputAxis2DInputParameters._analog
+ _OBJC_IVAR_$__GCDevicePhysicalInputAxis2DInputParameters._canWrap
+ _OBJC_IVAR_$__GCDevicePhysicalInputAxis2DInputParameters._sources
+ _OBJC_IVAR_$__GCDevicePhysicalInputCapacitiveButtonElement._touchedChangedHandlerSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputCapacitiveButtonElement._touchedTimestampSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputCapacitiveButtonElement._touchedValueFieldSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputCapacitiveButtonElement._touchedValueSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputCapacitiveButtonElementParameters._eventTouchedValueField
+ _OBJC_IVAR_$__GCDevicePhysicalInputCapacitiveDirectionPadElement._touchedInputSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputCapacitiveDirectionPadElement._touchedValueFieldSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputCapacitiveDirectionPadElementParameters._eventTouchedValueField
+ _OBJC_IVAR_$__GCDevicePhysicalInputCapacitiveDirectionPadElementParameters._touchedSources
+ _OBJC_IVAR_$__GCDevicePhysicalInputDirectionPadElement._xyAxesSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputDirectionPadElementParameters._xySources
+ _OBJC_IVAR_$__GCDevicePhysicalInputTouchedStateInput._sourcesSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputTouchedStateInput._touchedChangedHandlerSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputTouchedStateInput._touchedSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputTouchedStateInput._touchedTimestampSlot
+ _OBJC_IVAR_$__GCDevicePhysicalInputTouchedStateInputParameters._sources
+ _OBJC_IVAR_$__GCDigitizerEventImpl.timestamp
+ _OBJC_IVAR_$__GCDigitizerEventImpl.x
+ _OBJC_IVAR_$__GCDigitizerEventImpl.y
+ _OBJC_IVAR_$__GCKeyboardAndMouseEventSubject._buttonEventObservers
+ _OBJC_IVAR_$__GCKeyboardAndMouseEventSubject._digitizerEventObservers
+ _OBJC_IVAR_$__GCKeyboardAndMouseEventSubject._keyboardEventObservers
+ _OBJC_IVAR_$__GCKeyboardAndMouseEventSubject._lastButtonMask
+ _OBJC_IVAR_$__GCKeyboardAndMouseEventSubject._pointerEventObservers
+ _OBJC_IVAR_$__GCKeyboardAndMouseEventSubject._scrollEventObservers
+ _OBJC_IVAR_$__GCPointerEventImpl.timestamp
+ _OBJC_IVAR_$__GCPointerEventImpl.x
+ _OBJC_IVAR_$__GCPointerEventImpl.y
+ _OBJC_IVAR_$__GCScrollEventImpl.timestamp
+ _OBJC_IVAR_$__GCScrollEventImpl.x
+ _OBJC_IVAR_$__GCScrollEventImpl.y
+ _OBJC_METACLASS_$_GCKeyboardAndMouseManagerImpl
+ _OBJC_METACLASS_$__GCButtonEventImpl
+ _OBJC_METACLASS_$__GCDevicePhysicalInputAxis2DInput
+ _OBJC_METACLASS_$__GCDevicePhysicalInputAxis2DInputParameters
+ _OBJC_METACLASS_$__GCDevicePhysicalInputCapacitiveButtonElement
+ _OBJC_METACLASS_$__GCDevicePhysicalInputCapacitiveButtonElementParameters
+ _OBJC_METACLASS_$__GCDevicePhysicalInputCapacitiveDirectionPadElement
+ _OBJC_METACLASS_$__GCDevicePhysicalInputCapacitiveDirectionPadElementParameters
+ _OBJC_METACLASS_$__GCDevicePhysicalInputTouchedStateInput
+ _OBJC_METACLASS_$__GCDevicePhysicalInputTouchedStateInputParameters
+ _OBJC_METACLASS_$__GCDigitizerEventImpl
+ _OBJC_METACLASS_$__GCKeyboardAndMouseEventSubject
+ _OBJC_METACLASS_$__GCPointerEventImpl
+ _OBJC_METACLASS_$__GCScrollEventImpl
+ __OBJC_$_CATEGORY_GCDevicePhysicalInputCapacitiveButtonElementDescription_$_Client
+ __OBJC_$_CATEGORY_GCDevicePhysicalInputCapacitiveDirectionPadElementDescription_$_Client
+ __OBJC_$_CATEGORY_NSValue_$_GCTypes
+ __OBJC_$_CLASS_METHODS_GCDevicePhysicalInputCapacitiveButtonElementDescription(Client)
+ __OBJC_$_CLASS_METHODS_GCDevicePhysicalInputCapacitiveDirectionPadElementDescription(Client)
+ __OBJC_$_CLASS_METHODS_GCKeyboardAndMouseManager
+ __OBJC_$_CLASS_METHODS_GCMouse
+ __OBJC_$_CLASS_METHODS_NSValue(GCTypes)
+ __OBJC_$_CLASS_METHODS__GCDevicePhysicalInputAxis2DInput
+ __OBJC_$_CLASS_METHODS__GCDevicePhysicalInputCapacitiveButtonElement
+ __OBJC_$_CLASS_METHODS__GCDevicePhysicalInputCapacitiveDirectionPadElement
+ __OBJC_$_CLASS_METHODS__GCDevicePhysicalInputTouchedStateInput
+ __OBJC_$_CLASS_PROP_LIST_GCMouse
+ __OBJC_$_INSTANCE_METHODS_GCDevicePhysicalInputCapacitiveButtonElementDescription(Client)
+ __OBJC_$_INSTANCE_METHODS_GCDevicePhysicalInputCapacitiveDirectionPadElementDescription(Client)
+ __OBJC_$_INSTANCE_METHODS_GCKeyboardAndMouseManagerImpl
+ __OBJC_$_INSTANCE_METHODS_GCMouse
+ __OBJC_$_INSTANCE_METHODS_GCMouseInput(PubSub)
+ __OBJC_$_INSTANCE_METHODS_NSValue(GCTypes)
+ __OBJC_$_INSTANCE_METHODS__GCButtonEventImpl
+ __OBJC_$_INSTANCE_METHODS__GCControllerManagerServer(Connections)
+ __OBJC_$_INSTANCE_METHODS__GCDevicePhysicalInputAxis2DInput
+ __OBJC_$_INSTANCE_METHODS__GCDevicePhysicalInputAxis2DInputParameters
+ __OBJC_$_INSTANCE_METHODS__GCDevicePhysicalInputCapacitiveButtonElement
+ __OBJC_$_INSTANCE_METHODS__GCDevicePhysicalInputCapacitiveButtonElementParameters
+ __OBJC_$_INSTANCE_METHODS__GCDevicePhysicalInputCapacitiveDirectionPadElement
+ __OBJC_$_INSTANCE_METHODS__GCDevicePhysicalInputCapacitiveDirectionPadElementParameters
+ __OBJC_$_INSTANCE_METHODS__GCDevicePhysicalInputTouchedStateInput
+ __OBJC_$_INSTANCE_METHODS__GCDevicePhysicalInputTouchedStateInputParameters
+ __OBJC_$_INSTANCE_METHODS__GCDigitizerEventImpl
+ __OBJC_$_INSTANCE_METHODS__GCKeyboardAndMouseEventSubject(Button|Keyboard|Scroll|Digitizer|Pointer)
+ __OBJC_$_INSTANCE_METHODS__GCPointerEventImpl
+ __OBJC_$_INSTANCE_METHODS__GCScrollEventImpl
+ __OBJC_$_INSTANCE_VARIABLES_GCKeyboardAndMouseManagerImpl
+ __OBJC_$_INSTANCE_VARIABLES__GCButtonEventImpl
+ __OBJC_$_INSTANCE_VARIABLES__GCDevicePhysicalInputAxis2DInput
+ __OBJC_$_INSTANCE_VARIABLES__GCDevicePhysicalInputAxis2DInputParameters
+ __OBJC_$_INSTANCE_VARIABLES__GCDevicePhysicalInputCapacitiveButtonElement
+ __OBJC_$_INSTANCE_VARIABLES__GCDevicePhysicalInputCapacitiveButtonElementParameters
+ __OBJC_$_INSTANCE_VARIABLES__GCDevicePhysicalInputCapacitiveDirectionPadElement
+ __OBJC_$_INSTANCE_VARIABLES__GCDevicePhysicalInputCapacitiveDirectionPadElementParameters
+ __OBJC_$_INSTANCE_VARIABLES__GCDevicePhysicalInputTouchedStateInput
+ __OBJC_$_INSTANCE_VARIABLES__GCDevicePhysicalInputTouchedStateInputParameters
+ __OBJC_$_INSTANCE_VARIABLES__GCDigitizerEventImpl
+ __OBJC_$_INSTANCE_VARIABLES__GCKeyboardAndMouseEventSubject
+ __OBJC_$_INSTANCE_VARIABLES__GCPointerEventImpl
+ __OBJC_$_INSTANCE_VARIABLES__GCScrollEventImpl
+ __OBJC_$_PROP_LIST_GCAxis2DInput
+ __OBJC_$_PROP_LIST_GCKeyboardAndMouseManagerImpl
+ __OBJC_$_PROP_LIST_GCMouse
+ __OBJC_$_PROP_LIST_GCTouchedStateInput
+ __OBJC_$_PROP_LIST__GCButtonEvent
+ __OBJC_$_PROP_LIST__GCButtonEventImpl
+ __OBJC_$_PROP_LIST__GCControllerManagerServer
+ __OBJC_$_PROP_LIST__GCDevicePhysicalInputAxis2DInput
+ __OBJC_$_PROP_LIST__GCDevicePhysicalInputCapacitiveButtonElement
+ __OBJC_$_PROP_LIST__GCDevicePhysicalInputTouchedStateInput
+ __OBJC_$_PROP_LIST__GCDigitizerEvent
+ __OBJC_$_PROP_LIST__GCDigitizerEventImpl
+ __OBJC_$_PROP_LIST__GCPointerEvent
+ __OBJC_$_PROP_LIST__GCPointerEventImpl
+ __OBJC_$_PROP_LIST__GCScrollEvent
+ __OBJC_$_PROP_LIST__GCScrollEventImpl
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCAxis2DInput
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GCTouchedStateInput
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCButtonEvent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCButtonEventSink
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCButtonEventSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCDigitizerEvent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCDigitizerEventSink
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCDigitizerEventSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCPointerEvent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCPointerEventSink
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCPointerEventSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCScrollEvent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCScrollEventSink
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCScrollEventSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCAxis2DInput
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GCTouchedStateInput
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCButtonEvent
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCButtonEventSink
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCButtonEventSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCDigitizerEvent
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCDigitizerEventSink
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCDigitizerEventSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCPointerEvent
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCPointerEventSink
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCPointerEventSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCScrollEvent
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCScrollEventSink
+ __OBJC_$_PROTOCOL_METHOD_TYPES__GCScrollEventSource
+ __OBJC_$_PROTOCOL_REFS_GCAxis2DInput
+ __OBJC_$_PROTOCOL_REFS_GCTouchedStateInput
+ __OBJC_$_PROTOCOL_REFS__GCButtonEvent
+ __OBJC_$_PROTOCOL_REFS__GCButtonEventSink
+ __OBJC_$_PROTOCOL_REFS__GCButtonEventSource
+ __OBJC_$_PROTOCOL_REFS__GCDigitizerEvent
+ __OBJC_$_PROTOCOL_REFS__GCDigitizerEventSink
+ __OBJC_$_PROTOCOL_REFS__GCDigitizerEventSource
+ __OBJC_$_PROTOCOL_REFS__GCPointerEvent
+ __OBJC_$_PROTOCOL_REFS__GCPointerEventSink
+ __OBJC_$_PROTOCOL_REFS__GCPointerEventSource
+ __OBJC_$_PROTOCOL_REFS__GCScrollEvent
+ __OBJC_$_PROTOCOL_REFS__GCScrollEventSink
+ __OBJC_$_PROTOCOL_REFS__GCScrollEventSource
+ __OBJC_CLASS_PROTOCOLS_$_GCMouse
+ __OBJC_CLASS_PROTOCOLS_$_GCMouseInput(PubSub)
+ __OBJC_CLASS_PROTOCOLS_$__GCButtonEventImpl
+ __OBJC_CLASS_PROTOCOLS_$__GCDevicePhysicalInputAxis2DInput
+ __OBJC_CLASS_PROTOCOLS_$__GCDevicePhysicalInputCapacitiveButtonElement
+ __OBJC_CLASS_PROTOCOLS_$__GCDevicePhysicalInputTouchedStateInput
+ __OBJC_CLASS_PROTOCOLS_$__GCDigitizerEventImpl
+ __OBJC_CLASS_PROTOCOLS_$__GCKeyboardAndMouseEventSubject(Button|Keyboard|Scroll|Digitizer|Pointer)
+ __OBJC_CLASS_PROTOCOLS_$__GCPointerEventImpl
+ __OBJC_CLASS_PROTOCOLS_$__GCScrollEventImpl
+ __OBJC_CLASS_RO_$_GCKeyboardAndMouseManagerImpl
+ __OBJC_CLASS_RO_$__GCButtonEventImpl
+ __OBJC_CLASS_RO_$__GCDevicePhysicalInputAxis2DInput
+ __OBJC_CLASS_RO_$__GCDevicePhysicalInputAxis2DInputParameters
+ __OBJC_CLASS_RO_$__GCDevicePhysicalInputCapacitiveButtonElement
+ __OBJC_CLASS_RO_$__GCDevicePhysicalInputCapacitiveButtonElementParameters
+ __OBJC_CLASS_RO_$__GCDevicePhysicalInputCapacitiveDirectionPadElement
+ __OBJC_CLASS_RO_$__GCDevicePhysicalInputCapacitiveDirectionPadElementParameters
+ __OBJC_CLASS_RO_$__GCDevicePhysicalInputTouchedStateInput
+ __OBJC_CLASS_RO_$__GCDevicePhysicalInputTouchedStateInputParameters
+ __OBJC_CLASS_RO_$__GCDigitizerEventImpl
+ __OBJC_CLASS_RO_$__GCKeyboardAndMouseEventSubject
+ __OBJC_CLASS_RO_$__GCPointerEventImpl
+ __OBJC_CLASS_RO_$__GCScrollEventImpl
+ __OBJC_LABEL_PROTOCOL_$_GCAxis2DInput
+ __OBJC_LABEL_PROTOCOL_$_GCTouchedStateInput
+ __OBJC_LABEL_PROTOCOL_$__GCButtonEvent
+ __OBJC_LABEL_PROTOCOL_$__GCButtonEventSink
+ __OBJC_LABEL_PROTOCOL_$__GCButtonEventSource
+ __OBJC_LABEL_PROTOCOL_$__GCDigitizerEvent
+ __OBJC_LABEL_PROTOCOL_$__GCDigitizerEventSink
+ __OBJC_LABEL_PROTOCOL_$__GCDigitizerEventSource
+ __OBJC_LABEL_PROTOCOL_$__GCPointerEvent
+ __OBJC_LABEL_PROTOCOL_$__GCPointerEventSink
+ __OBJC_LABEL_PROTOCOL_$__GCPointerEventSource
+ __OBJC_LABEL_PROTOCOL_$__GCScrollEvent
+ __OBJC_LABEL_PROTOCOL_$__GCScrollEventSink
+ __OBJC_LABEL_PROTOCOL_$__GCScrollEventSource
+ __OBJC_METACLASS_RO_$_GCKeyboardAndMouseManagerImpl
+ __OBJC_METACLASS_RO_$__GCButtonEventImpl
+ __OBJC_METACLASS_RO_$__GCDevicePhysicalInputAxis2DInput
+ __OBJC_METACLASS_RO_$__GCDevicePhysicalInputAxis2DInputParameters
+ __OBJC_METACLASS_RO_$__GCDevicePhysicalInputCapacitiveButtonElement
+ __OBJC_METACLASS_RO_$__GCDevicePhysicalInputCapacitiveButtonElementParameters
+ __OBJC_METACLASS_RO_$__GCDevicePhysicalInputCapacitiveDirectionPadElement
+ __OBJC_METACLASS_RO_$__GCDevicePhysicalInputCapacitiveDirectionPadElementParameters
+ __OBJC_METACLASS_RO_$__GCDevicePhysicalInputTouchedStateInput
+ __OBJC_METACLASS_RO_$__GCDevicePhysicalInputTouchedStateInputParameters
+ __OBJC_METACLASS_RO_$__GCDigitizerEventImpl
+ __OBJC_METACLASS_RO_$__GCKeyboardAndMouseEventSubject
+ __OBJC_METACLASS_RO_$__GCPointerEventImpl
+ __OBJC_METACLASS_RO_$__GCScrollEventImpl
+ __OBJC_PROTOCOL_$_GCAxis2DInput
+ __OBJC_PROTOCOL_$_GCTouchedStateInput
+ __OBJC_PROTOCOL_$__GCButtonEvent
+ __OBJC_PROTOCOL_$__GCButtonEventSink
+ __OBJC_PROTOCOL_$__GCButtonEventSource
+ __OBJC_PROTOCOL_$__GCDigitizerEvent
+ __OBJC_PROTOCOL_$__GCDigitizerEventSink
+ __OBJC_PROTOCOL_$__GCDigitizerEventSource
+ __OBJC_PROTOCOL_$__GCPointerEvent
+ __OBJC_PROTOCOL_$__GCPointerEventSink
+ __OBJC_PROTOCOL_$__GCPointerEventSource
+ __OBJC_PROTOCOL_$__GCScrollEvent
+ __OBJC_PROTOCOL_$__GCScrollEventSink
+ __OBJC_PROTOCOL_$__GCScrollEventSource
+ ___29-[_GCRacingWheelManager init]_block_invoke.88
+ ___34-[GCControllerMBDelegate stopScan]_block_invoke.89
+ ___34-[GCControllerMBDelegate stopScan]_block_invoke.90
+ ___40-[GCRemoteUserDefaultsProxy boolForKey:]_block_invoke.148
+ ___40-[GCRemoteUserDefaultsProxy dataForKey:]_block_invoke.136
+ ___40-[_GCControllerManager setupHIDMonitor:]_block_invoke.130
+ ___40-[_GCControllerManager setupHIDMonitor:]_block_invoke.131
+ ___41-[GCGamepad(Legacy) _legacy_handleEvent:]_block_invoke.99
+ ___41-[GCRemoteUserDefaultsProxy arrayForKey:]_block_invoke.144
+ ___41-[GCRemoteUserDefaultsProxy floatForKey:]_block_invoke.156
+ ___42-[GCRemoteUserDefaultsProxy doubleForKey:]_block_invoke.152
+ ___42-[GCRemoteUserDefaultsProxy objectForKey:]_block_invoke.128
+ ___42-[GCRemoteUserDefaultsProxy stringForKey:]_block_invoke.132
+ ___43-[GCRemoteUserDefaultsProxy integerForKey:]_block_invoke.160
+ ___43-[GCSyntheticDeviceManager initWithServer:]_block_invoke.112
+ ___43-[GCSyntheticDeviceManager initWithServer:]_block_invoke.114
+ ___45-[GCLightXPCProxyClientEndpoint refreshLight]_block_invoke.94
+ ___45-[GCMouseInput(PubSub) setButtonEventSource:]_block_invoke
+ ___45-[GCMouseInput(PubSub) setScrollEventSource:]_block_invoke
+ ___46-[GCGameIntentManager tryPresentAppLibraryPod]_block_invoke.113
+ ___46-[GCGameIntentManager tryPresentAppLibraryPod]_block_invoke.113.cold.1
+ ___46-[GCMicroGamepad(Legacy) _legacy_handleEvent:]_block_invoke.167
+ ___46-[GCMouseInput(PubSub) setPointerEventSource:]_block_invoke
+ ___46-[GCRemoteUserDefaultsProxy dictionaryForKey:]_block_invoke.140
+ ___47-[_GCNintendoJoyConDevice setDriverConnection:]_block_invoke.104
+ ___47-[_GCNintendoJoyConDevice setDriverConnection:]_block_invoke_2.106
+ ___48-[GCMouseInput(PubSub) setDigitizerEventSource:]_block_invoke
+ ___48-[_GCDefaultPhysicalDevice setDriverConnection:]_block_invoke.259
+ ___48-[_GCDefaultPhysicalDevice setDriverConnection:]_block_invoke.262
+ ___48-[_GCDefaultPhysicalDevice setDriverConnection:]_block_invoke_2.256
+ ___48-[_GCDefaultPhysicalDevice setDriverConnection:]_block_invoke_2.261
+ ___48-[_GCDefaultPhysicalDevice setDriverConnection:]_block_invoke_3.258
+ ___49-[GCBatteryXPCProxyClientEndpoint refreshBattery]_block_invoke.89
+ ___49-[GCExtendedGamepad(PubSub) _handleGamepadEvent:]_block_invoke.476
+ ___49-[GCExtendedGamepad(PubSub) _handleGamepadEvent:]_block_invoke.477
+ ___49-[_GCControllerManagerAppClient _connectToDaemon]_block_invoke.166
+ ___49-[_GCControllerManagerAppClient _connectToDaemon]_block_invoke.166.cold.1
+ ___49-[_GCControllerManagerAppClient _connectToDaemon]_block_invoke.167
+ ___50-[GCSettingsXPCProxyClientEndpoint refreshProfile]_block_invoke.89
+ ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke.114
+ ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke.136
+ ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke.96
+ ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_2.104
+ ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_2.116
+ ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_2.138
+ ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_3.118
+ ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_3.139
+ ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_4.120
+ ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_4.140
+ ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_5.122
+ ___50-[_GCNintendoJoyConDeviceManager claimHIDService:]_block_invoke.156
+ ___50-[_GCNintendoJoyConDeviceManager claimHIDService:]_block_invoke.157
+ ___51-[GCApplicationStateMonitor initializeStateMonitor]_block_invoke.92
+ ___51-[GCKeyboardAndMouseManagerImpl _onqueue_addMouse:]_block_invoke
+ ___52-[_GCControllerManagerAppClient startVideoRecording]_block_invoke.221
+ ___52-[_GCControllerManagerAppClient startVideoRecording]_block_invoke.221.cold.1
+ ___53-[GCMouseInput initWithIdentifier:additionalButtons:]_block_invoke
+ ___55-[GCControllerCBDelegate centralManagerDidUpdateState:]_block_invoke.105
+ ___55-[GCKeyboardAndMouseManagerImpl _onqueue_publishMouse:]_block_invoke
+ ___56-[GCPhysicalInputProfile(PubSub) setGamepadEventSource:]_block_invoke.429
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.169
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.172
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.175
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.178
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.181
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.184
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.187
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.190
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.193
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.170
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.170.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.173
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.173.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.176
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.176.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.179
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.179.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.182
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.182.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.185
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.185.cold.1
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.188
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.191
+ ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.194
+ ___57-[GCKeyboardAndMouseManagerImpl _onqueue_unpublishMouse:]_block_invoke
+ ___57-[GCKeyboardAndMouseManagerImpl addDeviceWithServiceRef:]_block_invoke
+ ___57-[GCKeyboardAndMouseManagerImpl addDeviceWithServiceRef:]_block_invoke_2
+ ___58-[GCKeyboardAndMouseManagerImpl _onqueue_publishKeyboard:]_block_invoke
+ ___58-[GCMouseInput(PubSub) _handleButtonEventType:buttonMask:]_block_invoke
+ ___58-[GCMouseInput(PubSub) handleMouseMovementEventWithDelta:]_block_invoke
+ ___58-[GCMouseInput(PubSub) handleMouseMovementEventWithDelta:]_block_invoke_2
+ ___59-[GCAdaptiveTriggersXPCProxyClientEndpoint refreshStatuses]_block_invoke.86
+ ___60-[GCKeyboardAndMouseManagerImpl _onqueue_unpublishKeyboard:]_block_invoke
+ ___60-[GCKeyboardAndMouseManagerImpl removeDeviceWithServiceRef:]_block_invoke
+ ___60-[GCKeyboardAndMouseManagerImpl removeDeviceWithServiceRef:]_block_invoke_2
+ ___62-[GCApplicationStateMonitor addObserver:forProcessIdentifier:]_block_invoke.94
+ ___62-[GCKeyboardAndMouseManagerImpl setEmulatedControllerEnabled:]_block_invoke
+ ___63-[_GCDriverClientConnection connectToDeviceService:withClient:]_block_invoke.89
+ ___63-[_GCKeyboardAndMouseEventSubject(Button) observeButtonEvents:]_block_invoke
+ ___63-[_GCKeyboardAndMouseEventSubject(Scroll) observeScrollEvents:]_block_invoke
+ ___65-[_GCKeyboardAndMouseEventSubject(Pointer) observePointerEvents:]_block_invoke
+ ___67-[GCSystemGestureXPCProxyClientEndpoint refreshSystemGesturesState]_block_invoke.89
+ ___67-[_GCKeyboardAndMouseEventSubject(Keyboard) observeKeyboardEvents:]_block_invoke
+ ___68-[GCPhysicalInputProfile applyGestureSettingsToButton:withSettings:]_block_invoke.133
+ ___68-[GCPhysicalInputProfile applyGestureSettingsToButton:withSettings:]_block_invoke.135
+ ___68-[GCPhysicalInputProfile applyGestureSettingsToButton:withSettings:]_block_invoke.139
+ ___69-[_GCKeyboardAndMouseEventSubject(Digitizer) observeDigitizerEvents:]_block_invoke
+ ___71-[GCKeyboardAndMouseManagerImpl handleHIDEvent:atTimestamp:forSubject:]_block_invoke
+ ___71-[_GCControllerManager(Legacy) controllerWithUDID:setValue:forElement:]_block_invoke.196
+ ___71-[_GCControllerManagerAppClient(ControllerService) publishControllers:]_block_invoke.379
+ ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.181
+ ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.184
+ ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.212
+ ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.214
+ ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.223
+ ___74-[_GCControllerManagerServer(Connections) acceptIncomingDriverConnection:]_block_invoke.371
+ ___74-[_GCControllerManagerServer(Connections) acceptIncomingDriverConnection:]_block_invoke.371.cold.1
+ ___74-[_GCControllerManagerServer(Connections) acceptIncomingDriverConnection:]_block_invoke.371.cold.2
+ ___75-[GCSyntheticDeviceManager observeValueForKeyPath:ofObject:change:context:]_block_invoke.131
+ ___80-[GCKeyboardAndMouseManagerImpl observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___80-[GCKeyboardAndMouseManagerImpl observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
+ ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.229
+ ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.229.cold.1
+ ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.230
+ ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.230.cold.1
+ ___81+[_GCExtendedMFiControllerProfile determineCapabilitiesWithServiceInfo:initInfo:]_block_invoke_2
+ ___91-[_GCControllerGestureAwareButtonInput __onqueue_executeLongPressRecognizerForEvent:queue:]_block_invoke.121
+ ___91-[_GCControllerGestureAwareButtonInput __onqueue_executeLongPressRecognizerForEvent:queue:]_block_invoke.122
+ ___91-[_GCControllerGestureAwareButtonInput __onqueue_executeLongPressRecognizerForEvent:queue:]_block_invoke.123
+ ___93-[_GCControllerGestureAwareButtonInput __onqueue_executeDoublePressRecognizerForEvent:queue:]_block_invoke.118
+ ___93-[_GCControllerGestureAwareButtonInput __onqueue_executeDoublePressRecognizerForEvent:queue:]_block_invoke.119
+ ___93-[_GCControllerGestureAwareButtonInput __onqueue_executeSinglePressRecognizerForEvent:queue:]_block_invoke.124
+ ___GCControllerManagerInitXPC_block_invoke.320
+ ___GCControllerManagerInitXPC_block_invoke.339
+ ____gc_log_keyboard_and_mouse_block_invoke
+ ___block_descriptor_40_e26_v16?0"<_GCButtonEvent>"8lu32l8
+ ___block_descriptor_40_e26_v16?0"<_GCScrollEvent>"8lu32l8
+ ___block_descriptor_40_e27_v16?0"<_GCPointerEvent>"8lu32l8
+ ___block_descriptor_40_e29_v16?0"<_GCDigitizerEvent>"8lu32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_64_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.100
+ ___block_literal_global.105
+ ___block_literal_global.107
+ ___block_literal_global.111
+ ___block_literal_global.113
+ ___block_literal_global.115
+ ___block_literal_global.117
+ ___block_literal_global.119
+ ___block_literal_global.127
+ ___block_literal_global.134
+ ___block_literal_global.135
+ ___block_literal_global.142
+ ___block_literal_global.143
+ ___block_literal_global.147
+ ___block_literal_global.151
+ ___block_literal_global.155
+ ___block_literal_global.159
+ ___block_literal_global.177
+ ___block_literal_global.192
+ ___block_literal_global.210
+ ___block_literal_global.224
+ ___block_literal_global.234
+ ___block_literal_global.253
+ ___block_literal_global.262
+ ___block_literal_global.267
+ ___block_literal_global.269
+ ___block_literal_global.270
+ ___block_literal_global.272
+ ___block_literal_global.281
+ ___block_literal_global.283
+ ___block_literal_global.290
+ ___block_literal_global.292
+ ___block_literal_global.322
+ ___block_literal_global.34
+ ___block_literal_global.342
+ ___block_literal_global.347
+ ___block_literal_global.357
+ ___block_literal_global.362
+ ___block_literal_global.453
+ ___block_literal_global.460
+ ___block_literal_global.47
+ ___block_literal_global.51
+ ___block_literal_global.59
+ ___copy_constructor_8_8_s0_t8w39_s48_s56_s64
+ ___destructor_8_s0_s48_s56_s64
+ ___handleAncillaryButtonEvent_block_invoke.104
+ __gc_log_keyboard_and_mouse
+ __gc_log_keyboard_and_mouse.Log
+ __gc_log_keyboard_and_mouse.onceToken
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_GameController
+ __unnamed_array_storage.106
+ __unnamed_array_storage.173
+ __unnamed_array_storage.352
+ __unnamed_array_storage.411
+ __unnamed_array_storage.412
+ __unnamed_array_storage.421
+ __unnamed_array_storage.422
+ __unnamed_array_storage.429
+ __unnamed_array_storage.439
+ __unnamed_array_storage.444
+ __unnamed_array_storage.454
+ __unnamed_array_storage.459
+ __unnamed_array_storage.469
+ _dispatch_get_current_queue
+ _lastTouchedStateLatency.sTimebaseInfo
+ _objc_msgSend$_onqueue_ensureEmulatedControllerWithDevice:added:
+ _objc_msgSend$_setTouchedDidChangeHandler:
+ _objc_msgSend$_touchedDidChangeHandler
+ _objc_msgSend$additionalAliases
+ _objc_msgSend$buttonEventObservers
+ _objc_msgSend$digitizerEventObservers
+ _objc_msgSend$eventTouchedValueField
+ _objc_msgSend$handleDigitizerEvent:
+ _objc_msgSend$initWithIdentifier:additionalButtons:
+ _objc_msgSend$initWithName:additionalButtons:
+ _objc_msgSend$keyWindow
+ _objc_msgSend$keyboardEventObservers
+ _objc_msgSend$managerWithQueue:
+ _objc_msgSend$mask
+ _objc_msgSend$observeButtonEvents:
+ _objc_msgSend$observeDigitizerEvents:
+ _objc_msgSend$observePointerEvents:
+ _objc_msgSend$observeScrollEvents:
+ _objc_msgSend$pointerEventObservers
+ _objc_msgSend$queue
+ _objc_msgSend$scrollEventObservers
+ _objc_msgSend$setButtonEventObservers:
+ _objc_msgSend$setButtonEventSource:
+ _objc_msgSend$setDigitizerEventObservers:
+ _objc_msgSend$setDigitizerEventSource:
+ _objc_msgSend$setKeyboardEventObservers:
+ _objc_msgSend$setMask:
+ _objc_msgSend$setPointerEventObservers:
+ _objc_msgSend$setPointerEventSource:
+ _objc_msgSend$setScrollEventObservers:
+ _objc_msgSend$setScrollEventSource:
+ _objc_msgSend$setSet:
+ _objc_msgSend$setX:
+ _objc_msgSend$setY:
+ _objc_msgSend$touchedDidChangeHandler
+ _objc_msgSend$touchedInput
+ _objc_msgSend$touchedSources
+ _objc_msgSend$x
+ _objc_msgSend$xyAxes
+ _objc_msgSend$xySources
+ _objc_msgSend$y
+ _touchedInputUpdateContext.Offset
+ _xAxisUpdateContext
+ _xyAxesUpdateContext.Offset
- +[GCMouse(Private) supportsSecureCoding]
- -[GCKeyboardAndMouseManager .cxx_destruct]
- -[GCKeyboardAndMouseManager _onqueue_publishKeyboard:]
- -[GCKeyboardAndMouseManager _onqueue_refreshKeyboards]
- -[GCKeyboardAndMouseManager _onqueue_unpublishKeyboard:]
- -[GCKeyboardAndMouseManager _queue_removeDevice:registryID:]
- -[GCKeyboardAndMouseManager addMouse:]
- -[GCKeyboardAndMouseManager ensureEmulatedControllerWithDevice:added:]
- -[GCKeyboardAndMouseManager handleKeyboardEventAsFrontmostApp:]
- -[GCKeyboardAndMouseManager handleMouseEventAsFrontmostApp:]
- -[GCKeyboardAndMouseManager keyboardHIDServices]
- -[GCKeyboardAndMouseManager observeValueForKeyPath:ofObject:change:context:]
- -[GCKeyboardAndMouseManager publishDevice:withNotificationName:]
- -[GCKeyboardAndMouseManager removeDevice:registryID:]
- -[GCKeyboardAndMouseManager setCurrentMouse:]
- -[GCKeyboardAndMouseManager setEmulatedControllerEnabled:]
- -[GCKeyboardAndMouseManager setKeyboardHIDServices:]
- -[GCKeyboardAndMouseManager storeDevice:]
- -[GCKeyboardAndMouseManager unpublishDevice:withNotificationName:]
- -[GCKeyboardAndMouseManager updateCurrentDevice:]
- -[GCKeyboardAndMouseManager updateCurrentDeviceAfterDisconnecting:]
- -[GCKeyboardAndMouseManager updateCurrentMouseAfterDisconnecting:]
- -[GCMouse proxyController]
- -[GCMouse setProxyController:]
- -[GCMouse(Private) _legacy_description]
- -[GCMouse(Private) _legacy_handleEvent:]
- -[GCMouse(Private) _legacy_isAttachedToDevice]
- -[GCMouse(Private) _legacy_isEqualToController:]
- -[GCMouse(Private) _legacy_physicalInputProfileName]
- -[GCMouse(Private) _legacy_physicalInputProfile]
- -[GCMouse(Private) _legacy_playerIndex]
- -[GCMouse(Private) _legacy_productCategory]
- -[GCMouse(Private) _legacy_setPlayerIndex:]
- -[GCMouse(Private) _legacy_vendorName]
- -[GCMouse(Private) addServiceRef:]
- -[GCMouse(Private) addServiceRefsWithDevice:]
- -[GCMouse(Private) areAllHIDDevicesConnected]
- -[GCMouse(Private) clearServiceRef]
- -[GCMouse(Private) createInputBufferForDevice:withSize:]
- -[GCMouse(Private) debugName]
- -[GCMouse(Private) deviceHash]
- -[GCMouse(Private) encodeWithCoder:]
- -[GCMouse(Private) hasServiceRef:]
- -[GCMouse(Private) hidServices]
- -[GCMouse(Private) initWithCoder:]
- -[GCMouse(Private) initWithServiceRef:]
- -[GCMouse(Private) isATVRemote]
- -[GCMouse(Private) isForwarded]
- -[GCMouse(Private) isPublished]
- -[GCMouse(Private) physicalDeviceUniqueID]
- -[GCMouse(Private) profile]
- -[GCMouse(Private) removeServiceRef:]
- -[GCMouse(Private) sampleRate]
- -[GCMouse(Private) service]
- -[GCMouse(Private) setAllHIDDevicesConnected:]
- -[GCMouse(Private) setDebugName:]
- -[GCMouse(Private) setForwarded:]
- -[GCMouse(Private) setPhysicalDeviceUniqueID:]
- -[GCMouse(Private) setProfile:]
- -[GCMouse(Private) setPublished:]
- -[GCMouse(Private) setUniqueIdentifier:]
- -[GCMouse(Private) setVendorName:]
- -[GCMouse(Private) uniqueIdentifier]
- -[GCMouseInput _handleButtonEventType:buttonMask:]
- -[GCMouseInput _handleDigitizerEvent:]
- -[GCMouseInput _handleEventImpl:]
- -[GCMouseInput _handleEventImpl:].cold.1
- -[GCMouseInput _handleEventRec:]
- -[GCMouseInput _legacy_handleButtonEvent:]
- -[GCMouseInput _legacy_handleEvent:]
- -[GCMouseInput _legacy_handlePointerEvent:]
- -[GCMouseInput _legacy_handleScrollEvent:]
- -[GCMouseInput _mouseButtons]
- -[GCMouseInput appDidBecomeActive]
- -[GCMouseInput appWillResignActive]
- -[GCMouseInput controller]
- -[GCMouseInput handleMouseButtonEventAddingButtonMask:]
- -[GCMouseInput handleMouseButtonEventRemovingButtonMask:]
- -[GCMouseInput handleMouseButtonEventSettingButtonMask:]
- -[GCMouseInput handleMouseMovementEventWithDelta:]
- -[GCMouseInput handleScrollEventWithDelta:]
- -[GCMouseInput handlerQueue]
- -[GCMouseInput initWithController:]
- -[GCMouseInput initWithController:].cold.1
- -[GCMouseInput initWithController:].cold.2
- -[GCMouseInput productCategory]
- -[GCMouseInput setController:]
- -[GCMouseInput shouldAcceptMouseEvents]
- -[_GCAppClientProxy enableFeature:]
- -[_GCControllerManager enableKeyboardAndMouseSupport]
- -[_GCControllerManager(Legacy) _legacy_coalescedKeyboard]
- -[_GCControllerManager(Legacy) _legacy_mice]
- -[_GCControllerManager(Legacy) setCurrentMouse:]
- -[_GCControllerManagerAppClient enableKeyboardAndMouseSupport]
- -[_GCControllerManagerAppClient handleKeyboardEventAsFrontmostApp:]
- -[_GCControllerManagerAppClient handleMouseEventAsFrontmostApp:]
- -[_GCControllerManagerAppClient mice]
- -[_GCControllerManagerServer(KeyboardAndMouseMonitoring) disableKeyboardAndMouseSupportForPID:]
- -[_GCControllerManagerServer(KeyboardAndMouseMonitoring) enableKeyboardAndMouseSupportForPID:]
- -[_GCControllerManagerServer(KeyboardAndMouseMonitoring) pidsWithKeyboardAndMouseSupport]
- -[_GCGamepadEventImpl buttonL4]
- -[_GCGamepadEventImpl buttonL5]
- -[_GCGamepadEventImpl buttonR4]
- -[_GCGamepadEventImpl buttonR5]
- -[_GCGamepadEventImpl setButtonL4:]
- -[_GCGamepadEventImpl setButtonL5:]
- -[_GCGamepadEventImpl setButtonR4:]
- -[_GCGamepadEventImpl setButtonR5:]
- -[_GCHapticSyntheticCommand initWithHapticCommand:].cold.1
- GCC_except_table43
- GCC_except_table47
- _OBJC_IVAR_$_GCKeyboardAndMouseManager._coalescedKeyboard
- _OBJC_IVAR_$_GCKeyboardAndMouseManager._currentMouse
- _OBJC_IVAR_$_GCKeyboardAndMouseManager._devicesByRegistryID
- _OBJC_IVAR_$_GCKeyboardAndMouseManager._devicesQueue
- _OBJC_IVAR_$_GCKeyboardAndMouseManager._emulatedController
- _OBJC_IVAR_$_GCKeyboardAndMouseManager._keyboardHIDServices
- _OBJC_IVAR_$_GCMouse._proxyController
- _OBJC_IVAR_$_GCMouseInput._controller
- _OBJC_IVAR_$_GCMouseInput._isActive
- _OBJC_IVAR_$_GCMouseInput._wasInitialized
- _OBJC_IVAR_$__GCControllerManagerAppClient._hasEnabledKeyboardMouseSupport
- __OBJC_$_CLASS_METHODS_GCMouse(Private)
- __OBJC_$_INSTANCE_METHODS_GCMouse(Private)
- __OBJC_$_INSTANCE_METHODS_GCMouseInput
- __OBJC_$_INSTANCE_METHODS__GCControllerManagerServer(Connections|KeyboardAndMouseMonitoring)
- __OBJC_$_PROP_LIST_GCMouseInput
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__GCAppClientInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES__GCAppClientInterface
- __OBJC_CLASS_PROTOCOLS_$_GCMouse(Private)
- __OBJC_CLASS_PROTOCOLS_$_GCMouseInput
- ___29-[_GCRacingWheelManager init]_block_invoke.85
- ___33-[GCKeyboardAndMouseManager mice]_block_invoke
- ___33-[GCMouseInput _handleEventImpl:]_block_invoke
- ___34-[GCControllerMBDelegate stopScan]_block_invoke.86
- ___34-[GCControllerMBDelegate stopScan]_block_invoke.87
- ___35-[GCMouseInput initWithController:]_block_invoke
- ___38-[GCKeyboardAndMouseManager addMouse:]_block_invoke
- ___40-[GCRemoteUserDefaultsProxy boolForKey:]_block_invoke.145
- ___40-[GCRemoteUserDefaultsProxy dataForKey:]_block_invoke.133
- ___40-[_GCControllerManager setupHIDMonitor:]_block_invoke.127
- ___40-[_GCControllerManager setupHIDMonitor:]_block_invoke.128
- ___41-[GCGamepad(Legacy) _legacy_handleEvent:]_block_invoke.96
- ___41-[GCRemoteUserDefaultsProxy arrayForKey:]_block_invoke.141
- ___41-[GCRemoteUserDefaultsProxy floatForKey:]_block_invoke.153
- ___42-[GCMouseInput _legacy_handleButtonEvent:]_block_invoke
- ___42-[GCRemoteUserDefaultsProxy doubleForKey:]_block_invoke.149
- ___42-[GCRemoteUserDefaultsProxy objectForKey:]_block_invoke.125
- ___42-[GCRemoteUserDefaultsProxy stringForKey:]_block_invoke.129
- ___43-[GCMouseInput _legacy_handlePointerEvent:]_block_invoke
- ___43-[GCMouseInput _legacy_handlePointerEvent:]_block_invoke_2
- ___43-[GCRemoteUserDefaultsProxy integerForKey:]_block_invoke.157
- ___43-[GCSyntheticDeviceManager initWithServer:]_block_invoke.109
- ___43-[GCSyntheticDeviceManager initWithServer:]_block_invoke.111
- ___45-[GCLightXPCProxyClientEndpoint refreshLight]_block_invoke.91
- ___46-[GCGameIntentManager tryPresentAppLibraryPod]_block_invoke.110
- ___46-[GCGameIntentManager tryPresentAppLibraryPod]_block_invoke.110.cold.1
- ___46-[GCMicroGamepad(Legacy) _legacy_handleEvent:]_block_invoke.163
- ___46-[GCRemoteUserDefaultsProxy dictionaryForKey:]_block_invoke.137
- ___47-[_GCNintendoJoyConDevice setDriverConnection:]_block_invoke.101
- ___47-[_GCNintendoJoyConDevice setDriverConnection:]_block_invoke_2.103
- ___48-[GCKeyboardInput(PubSub) _handleKeyboardEvent:]_block_invoke.cold.1
- ___48-[_GCDefaultPhysicalDevice setDriverConnection:]_block_invoke.247
- ___48-[_GCDefaultPhysicalDevice setDriverConnection:]_block_invoke.258
- ___48-[_GCDefaultPhysicalDevice setDriverConnection:]_block_invoke_2.248
- ___48-[_GCDefaultPhysicalDevice setDriverConnection:]_block_invoke_2.257
- ___48-[_GCDefaultPhysicalDevice setDriverConnection:]_block_invoke_3.250
- ___49-[GCBatteryXPCProxyClientEndpoint refreshBattery]_block_invoke.86
- ___49-[GCExtendedGamepad(PubSub) _handleGamepadEvent:]_block_invoke.436
- ___49-[GCExtendedGamepad(PubSub) _handleGamepadEvent:]_block_invoke.437
- ___49-[_GCControllerManagerAppClient _connectToDaemon]_block_invoke.162
- ___49-[_GCControllerManagerAppClient _connectToDaemon]_block_invoke.162.cold.1
- ___49-[_GCControllerManagerAppClient _connectToDaemon]_block_invoke.163
- ___50-[GCSettingsXPCProxyClientEndpoint refreshProfile]_block_invoke.86
- ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke.108
- ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke.133
- ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke.93
- ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_2.101
- ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_2.113
- ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_2.135
- ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_3.115
- ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_3.136
- ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_4.117
- ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_4.137
- ___50-[_GCControllerInputComponent setSettingsProfile:]_block_invoke_5.119
- ___50-[_GCNintendoJoyConDeviceManager claimHIDService:]_block_invoke.153
- ___50-[_GCNintendoJoyConDeviceManager claimHIDService:]_block_invoke.154
- ___51-[GCApplicationStateMonitor initializeStateMonitor]_block_invoke.89
- ___52-[_GCControllerManagerAppClient startVideoRecording]_block_invoke.217
- ___52-[_GCControllerManagerAppClient startVideoRecording]_block_invoke.217.cold.1
- ___53-[GCKeyboardAndMouseManager addDeviceWithServiceRef:]_block_invoke
- ___53-[GCKeyboardAndMouseManager removeDevice:registryID:]_block_invoke
- ___54-[GCKeyboardAndMouseManager _onqueue_publishKeyboard:]_block_invoke
- ___55-[GCControllerCBDelegate centralManagerDidUpdateState:]_block_invoke.102
- ___56-[GCKeyboardAndMouseManager _onqueue_unpublishKeyboard:]_block_invoke
- ___56-[GCKeyboardAndMouseManager removeDeviceWithServiceRef:]_block_invoke
- ___56-[GCPhysicalInputProfile(PubSub) setGamepadEventSource:]_block_invoke.425
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.165
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.168
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.171
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.174
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.177
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.180
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.183
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.186
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke.189
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.166
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.166.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.169
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.169.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.172
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.172.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.175
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.175.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.178
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.178.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.181
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.181.cold.1
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.184
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.187
- ___56-[_GCControllerManagerAppClient _resumeDaemonConnection]_block_invoke_2.190
- ___58-[GCKeyboardAndMouseManager setEmulatedControllerEnabled:]_block_invoke
- ___59-[GCAdaptiveTriggersXPCProxyClientEndpoint refreshStatuses]_block_invoke.83
- ___62-[GCApplicationStateMonitor addObserver:forProcessIdentifier:]_block_invoke.91
- ___63-[_GCDriverClientConnection connectToDeviceService:withClient:]_block_invoke.86
- ___64-[GCKeyboardAndMouseManager publishDevice:withNotificationName:]_block_invoke
- ___66-[GCKeyboardAndMouseManager unpublishDevice:withNotificationName:]_block_invoke
- ___67-[GCSystemGestureXPCProxyClientEndpoint refreshSystemGesturesState]_block_invoke.86
- ___68-[GCPhysicalInputProfile applyGestureSettingsToButton:withSettings:]_block_invoke.130
- ___68-[GCPhysicalInputProfile applyGestureSettingsToButton:withSettings:]_block_invoke.132
- ___68-[GCPhysicalInputProfile applyGestureSettingsToButton:withSettings:]_block_invoke.136
- ___71-[_GCControllerManager(Legacy) controllerWithUDID:setValue:forElement:]_block_invoke.192
- ___71-[_GCControllerManagerAppClient(ControllerService) publishControllers:]_block_invoke.382
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.177
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.180
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.208
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.210
- ___72-[_GCDefaultLogicalDevice initWithPhysicalDevice:configuration:manager:]_block_invoke.219
- ___74-[_GCControllerManagerServer(Connections) acceptIncomingDriverConnection:]_block_invoke.367
- ___74-[_GCControllerManagerServer(Connections) acceptIncomingDriverConnection:]_block_invoke.367.cold.1
- ___74-[_GCControllerManagerServer(Connections) acceptIncomingDriverConnection:]_block_invoke.367.cold.2
- ___75-[GCSyntheticDeviceManager observeValueForKeyPath:ofObject:change:context:]_block_invoke.128
- ___76-[GCKeyboardAndMouseManager observeValueForKeyPath:ofObject:change:context:]_block_invoke
- ___76-[GCKeyboardAndMouseManager observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
- ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.225
- ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.225.cold.1
- ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.226
- ___80-[_GCControllerManagerAppClient stopVideoRecordingWithClipBuffering:controller:]_block_invoke.226.cold.1
- ___91-[_GCControllerGestureAwareButtonInput __onqueue_executeLongPressRecognizerForEvent:queue:]_block_invoke.117
- ___91-[_GCControllerGestureAwareButtonInput __onqueue_executeLongPressRecognizerForEvent:queue:]_block_invoke.118
- ___91-[_GCControllerGestureAwareButtonInput __onqueue_executeLongPressRecognizerForEvent:queue:]_block_invoke.119
- ___93-[_GCControllerGestureAwareButtonInput __onqueue_executeDoublePressRecognizerForEvent:queue:]_block_invoke.115
- ___93-[_GCControllerGestureAwareButtonInput __onqueue_executeDoublePressRecognizerForEvent:queue:]_block_invoke.116
- ___93-[_GCControllerGestureAwareButtonInput __onqueue_executeSinglePressRecognizerForEvent:queue:]_block_invoke.121
- ___GCControllerManagerInitXPC_block_invoke.318
- ___GCControllerManagerInitXPC_block_invoke.337
- ___block_descriptor_64_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_literal_global.106
- ___block_literal_global.108
- ___block_literal_global.110
- ___block_literal_global.114
- ___block_literal_global.116
- ___block_literal_global.121
- ___block_literal_global.126
- ___block_literal_global.128
- ___block_literal_global.130
- ___block_literal_global.140
- ___block_literal_global.144
- ___block_literal_global.148
- ___block_literal_global.152
- ___block_literal_global.156
- ___block_literal_global.174
- ___block_literal_global.188
- ___block_literal_global.206
- ___block_literal_global.220
- ___block_literal_global.230
- ___block_literal_global.249
- ___block_literal_global.258
- ___block_literal_global.263
- ___block_literal_global.265
- ___block_literal_global.266
- ___block_literal_global.268
- ___block_literal_global.277
- ___block_literal_global.279
- ___block_literal_global.286
- ___block_literal_global.288
- ___block_literal_global.31
- ___block_literal_global.320
- ___block_literal_global.340
- ___block_literal_global.345
- ___block_literal_global.35
- ___block_literal_global.353
- ___block_literal_global.358
- ___block_literal_global.449
- ___block_literal_global.456
- ___block_literal_global.48
- ___block_literal_global.50
- ___block_literal_global.96
- ___block_literal_global.97
- ___block_literal_global.98
- ___copy_constructor_8_8_s0_t8w39_s48_s56
- ___destructor_8_s0_s48_s56
- ___handleAncillaryButtonEvent_block_invoke.101
- __unnamed_array_storage.103
- __unnamed_array_storage.170
- __unnamed_array_storage.350
- __unnamed_array_storage.405
- __unnamed_array_storage.406
- __unnamed_array_storage.418
- __unnamed_array_storage.419
- __unnamed_array_storage.426
- __unnamed_array_storage.433
- __unnamed_array_storage.441
- __unnamed_array_storage.442
- __unnamed_array_storage.456
- __unnamed_array_storage.457
- _objc_msgSend$_handleDigitizerEvent:
- _objc_msgSend$_handleEventImpl:
- _objc_msgSend$_handleEventRec:
- _objc_msgSend$_legacy_coalescedKeyboard
- _objc_msgSend$_legacy_mice
- _objc_msgSend$_legacy_mouse
- _objc_msgSend$_queue_removeDevice:registryID:
- _objc_msgSend$addMouse:
- _objc_msgSend$addServiceRef:
- _objc_msgSend$addServiceRefsWithDevice:
- _objc_msgSend$createInputBufferForDevice:withSize:
- _objc_msgSend$disableKeyboardAndMouseSupportForPID:
- _objc_msgSend$enableFeature:
- _objc_msgSend$enableKeyboardAndMouseSupportForPID:
- _objc_msgSend$ensureEmulatedControllerWithDevice:added:
- _objc_msgSend$initWithSet:
- _objc_msgSend$mouseButtonPressedPrivate
- _objc_msgSend$mouseMovedHandlerPrivate
- _objc_msgSend$publishDevice:withNotificationName:
- _objc_msgSend$removeDevice:registryID:
- _objc_msgSend$setDebugName:
- _objc_msgSend$setHandlerQueue:
- _objc_msgSend$setIsProxyController:
- _objc_msgSend$setProfile:
- _objc_msgSend$setProxyController:
- _objc_msgSend$shouldAcceptMouseEvents
- _objc_msgSend$storeDevice:
- _objc_msgSend$uniqueIdentifier
- _objc_msgSend$unpublishDevice:withNotificationName:
- _objc_msgSend$updateCurrentDevice:
- _objc_msgSend$updateCurrentDeviceAfterDisconnecting:
- _objc_msgSend$updateCurrentMouseAfterDisconnecting:
- _os_transaction_create
CStrings:
+ "\x01\x11\x14\x1a"
+ "\x01A\x16"
+ "\x01\xf0\xb2"
+ "\x04\x13"
+ "\x11?\x0f\x0f\x0f\n\x11\""
+ "\x17"
+ " (touched)"
+ "#NOTE Added HID service %@ is already tracked as a mouse."
+ "#NOTE Already tracking HID service: %@"
+ "#NOTE Not currently tracking added mouse HID service %@.  It may have already disconnected."
+ "#WARNING Ignoring added HID Service because it returned an invalid registryID:\n%@"
+ "#WARNING Ignoring removed HID Service because it returned an invalid registryID:\n%@"
+ "%@ is Magic mouse or Magic trackpad!"
+ "%@ is normal mouse device!"
+ "*** Back button names begin at position '0'.  Position '%zd' is not valid."
+ "<%@ %p> {\n\t.DpadUp: %@\n\t.DpadDown: %@\n\t.DpadLeft: %@\n\t.DpadRight: %@\n\t.ButtonA: %@\n\t.ButtonB: %@\n\t.ButtonX: %@\n\t.ButtonY: %@\n\t.LeftShoulder: %@\n\t.RightShoulder: %@\n\t.LeftThumbstickUp: %@\n\t.LeftThumbstickDown: %@\n\t.LeftThumbstickLeft: %@\n\t.LeftThumbstickRight: %@\n\t.RightThumbstickUp: %@\n\t.RightThumbstickDown: %@\n\t.RightThumbstickLeft: %@\n\t.RightThumbstickRight: %@\n\t.LeftTrigger: %@\n\t.RightTrigger: %@\n\t.LeftThumbstickButton: %@\n\t.RightThumbstickButton: %@\n\t.ButtonHome: %@\n\t.ButtonMenu: %@\n\t.ButtonOptions: %@\n\t.ButtonSpecial0: %@\n\t.ButtonSpecial1: %@\n\t.ButtonSpecial2: %@\n\t.ButtonSpecial3: %@\n\t.ButtonSpecial4: %@\n\t.ButtonSpecial5: %@\n\t.ButtonSpecial6: %@\n\t.ButtonSpecial7: %@\n\t.ButtonSpecial8: %@\n\t.ButtonSpecial9: %@\n\t.ButtonSpecial10: %@\n\t.ButtonSpecial11: %@\n\t.ButtonSpecial12: %@\n\t.ButtonSpecial13: %@\n\t.ButtonSpecial14: %@\n\t.ButtonShare: %@\n}"
+ "<%@ %p> {\n\t.DpadUp: %f\n\t.DpadDown: %f\n\t.DpadLeft: %f\n\t.DpadRight: %f\n\t.ButtonA: %f\n\t.ButtonB: %f\n\t.ButtonX: %f\n\t.ButtonY: %f\n\t.LeftShoulder: %f\n\t.RightShoulder: %f\n\t.LeftThumbstickUp: %f\n\t.LeftThumbstickDown: %f\n\t.LeftThumbstickLeft: %f\n\t.LeftThumbstickRight: %f\n\t.RightThumbstickUp: %f\n\t.RightThumbstickDown: %f\n\t.RightThumbstickLeft: %f\n\t.RightThumbstickRight: %f\n\t.LeftTrigger: %f\n\t.RightTrigger: %f\n\t.LeftThumbstickButton: %f\n\t.RightThumbstickButton: %f\n\t.ButtonHome: %f\n\t.ButtonMenu: %f\n\t.ButtonOptions: %f\n\t.ButtonSpecial0: %f\n\t.ButtonSpecial1: %f\n\t.ButtonSpecial2: %f\n\t.ButtonSpecial3: %f\n\t.ButtonSpecial4: %f\n\t.ButtonSpecial5: %f\n\t.ButtonSpecial6: %f\n\t.ButtonSpecial7: %f\n\t.ButtonSpecial8: %f\n\t.ButtonSpecial9: %f\n\t.ButtonSpecial10: %f\n\t.ButtonSpecial11: %f\n\t.ButtonSpecial12: %f\n\t.ButtonSpecial13: %f\n\t.ButtonSpecial14: %f\n\t.ButtonShare: %f\n}"
+ "<Direction Pad '%@'; up = %f, down = %f, left = %f, right = %f, pressed = %f, touched = %i>"
+ "<TouchedStateInput; %@>"
+ "@\"<GCAxis2DInput>\"16@0:8"
+ "@\"GCMouseInput\""
+ "@24@0:8@?<v@?@\"<_GCButtonEvent>\">16"
+ "@24@0:8@?<v@?@\"<_GCDigitizerEvent>\">16"
+ "@24@0:8@?<v@?@\"<_GCPointerEvent>\">16"
+ "@24@0:8@?<v@?@\"<_GCScrollEvent>\">16"
+ "@24@0:8r^{?=[22{?=@BB(?={?=iBfq}{?=iiii})iBBB@@@}]BB}16"
+ "@24@0:8{GCPoint2=ff}16"
+ "@28@0:8@16I24"
+ "@32@0:8@16r^{?=[22{?=@BB(?={?=iBfq}{?=iiii})iBBB@@@}]BB}24"
+ "@40@0:8Q16[47f]24Q32"
+ "@88@0:8{?=@BB(?={?=iBfq}{?=iiii})iBBB@@@}16"
+ "@?<v@?@\"<GCPhysicalInputElement>\"@\"<GCAxis2DInput>\"{GCPoint2=ff}>16@0:8"
+ "@?<v@?@\"<GCPhysicalInputElement>\"@\"<GCTouchedStateInput>\"B>16@0:8"
+ "BUTTON_L4"
+ "BUTTON_M1"
+ "BUTTON_M2"
+ "BUTTON_M3"
+ "BUTTON_M4"
+ "BUTTON_R4"
+ "Back Left Button %ld"
+ "Back Left Button 0"
+ "Back Left Button 1"
+ "Back Right Button %ld"
+ "Back Right Button 0"
+ "Back Right Button 1"
+ "Digitizer"
+ "GCAxis2DInput"
+ "GCKeyboardAndMouseManagerImpl"
+ "GCPoint2Value"
+ "GCTouchedStateInput"
+ "GCTypes"
+ "Generic Mouse"
+ "HID Service has both keyboard and mouse profiles at the same time:\n%@"
+ "Keyboard+Mouse"
+ "Left Bumper"
+ "No longer tracking %@"
+ "Now tracking %@. Is Keyboard(%{BOOL}d), Mouse(%{BOOL}d)"
+ "Pointer"
+ "Posting GCMouseDidBecomeCurrent for %@"
+ "Posting GCMouseDidConnectNotification for %@."
+ "Posting GCMouseDidDisconnectNotification for %@."
+ "Posting GCMouseDidStopBeingCurrent for %@"
+ "Right Bumper"
+ "T@\"<GCAxis2DInput>\",R"
+ "T@\"GCMouseInput\",R,N,V_mouseInput"
+ "T@\"NSArray\",C,V_buttonEventObservers"
+ "T@\"NSArray\",C,V_digitizerEventObservers"
+ "T@\"NSArray\",C,V_keyboardEventObservers"
+ "T@\"NSArray\",C,V_pointerEventObservers"
+ "T@\"NSArray\",C,V_scrollEventObservers"
+ "T@\"NSSet\",R,C,D"
+ "T@\"NSSet\",R,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@?,C,N,V_mouseButtonPressedPrivate"
+ "T@?,C,N,V_mouseMovedHandlerPrivate"
+ "TB,R,GisTouched"
+ "TQ,N,Vtimestamp"
+ "Tf,N,Vx"
+ "Tf,N,Vy"
+ "Tq,N,Vmask"
+ "T{GCPoint2=ff},R"
+ "T{GCPoint2=ff},R,N"
+ "[47@\"GCControllerElement\"]"
+ "[47{UsagePage_Usage_Pair=\"usagePage\"q\"usage\"q}]"
+ "[otherElement isKindOfClass:_GCDevicePhysicalInputAxis2DInput.class]"
+ "[otherElement isKindOfClass:_GCDevicePhysicalInputTouchedStateInput.class]"
+ "^[47C]"
+ "_GCButtonEvent"
+ "_GCButtonEventImpl"
+ "_GCButtonEventSink"
+ "_GCButtonEventSource"
+ "_GCDevicePhysicalInputAxis2DInput"
+ "_GCDevicePhysicalInputAxis2DInput.m"
+ "_GCDevicePhysicalInputAxis2DInputParameters"
+ "_GCDevicePhysicalInputCapacitiveButtonElement"
+ "_GCDevicePhysicalInputCapacitiveButtonElementParameters"
+ "_GCDevicePhysicalInputCapacitiveDirectionPadElement"
+ "_GCDevicePhysicalInputCapacitiveDirectionPadElementParameters"
+ "_GCDevicePhysicalInputTouchedStateInput"
+ "_GCDevicePhysicalInputTouchedStateInput.m"
+ "_GCDevicePhysicalInputTouchedStateInputParameters"
+ "_GCDigitizerEvent"
+ "_GCDigitizerEventImpl"
+ "_GCDigitizerEventSink"
+ "_GCDigitizerEventSource"
+ "_GCKeyboardAndMouseEventSubject"
+ "_GCPointerEvent"
+ "_GCPointerEventImpl"
+ "_GCPointerEventSink"
+ "_GCPointerEventSource"
+ "_GCScrollEvent"
+ "_GCScrollEventImpl"
+ "_GCScrollEventSink"
+ "_GCScrollEventSource"
+ "_buttonEventObservation"
+ "_buttonEventObservers"
+ "_digitizerEventObservation"
+ "_digitizerEventObservers"
+ "_eventTouchedValueField"
+ "_hidServiceSubjects"
+ "_keyboardEventObservers"
+ "_lastButtonMask"
+ "_mice"
+ "_mouseInput"
+ "_onqueue_ensureEmulatedControllerWithDevice:added:"
+ "_pointerEventObservation"
+ "_pointerEventObservers"
+ "_scrollEventObservation"
+ "_scrollEventObservers"
+ "_setTouchedDidChangeHandler:"
+ "_touchedChangedHandlerSlot"
+ "_touchedDidChangeHandler"
+ "_touchedInputSlot"
+ "_touchedSlot"
+ "_touchedSources"
+ "_touchedTimestampSlot"
+ "_touchedValueFieldSlot"
+ "_touchedValueSlot"
+ "_xyAxesSlot"
+ "_xySources"
+ "appInBackground"
+ "button.left.bottom.primary"
+ "button.left.bottom.secondary"
+ "button.right.bottom.primary"
+ "button.right.bottom.secondary"
+ "buttonBackLeftPrimary"
+ "buttonBackLeftSecondary"
+ "buttonBackRightPrimary"
+ "buttonBackRightSecondary"
+ "buttonEventObservers"
+ "buttonLeftBumper"
+ "buttonRightBumper"
+ "digitizerEventObservers"
+ "eventTouchedValueField"
+ "handleDigitizerEvent:"
+ "initWithButtonEvent:"
+ "initWithDigitizerEvent:"
+ "initWithIdentifier:additionalButtons:"
+ "initWithName:additionalButtons:"
+ "initWithPointerEvent:"
+ "initWithScrollEvent:"
+ "keyWindow"
+ "keyboardEventObservers"
+ "l4.button.horizontal"
+ "lastTouchedStateLatency"
+ "lastTouchedStateTimestamp"
+ "m1.button.horizontal"
+ "m2.button.horizontal"
+ "m3.button.horizontal"
+ "m4.button.horizontal"
+ "managerWithQueue:"
+ "mask"
+ "observeButtonEvents:"
+ "observeDigitizerEvents:"
+ "observePointerEvents:"
+ "observeScrollEvents:"
+ "pointerEventObservers"
+ "r4.button.horizontal"
+ "scrollEventObservers"
+ "setButtonBackLeftPrimary:"
+ "setButtonBackLeftSecondary:"
+ "setButtonBackRightPrimary:"
+ "setButtonBackRightSecondary:"
+ "setButtonEventObservers:"
+ "setButtonEventSource:"
+ "setButtonLeftBumper:"
+ "setButtonRightBumper:"
+ "setDigitizerEventObservers:"
+ "setDigitizerEventSource:"
+ "setKeyboardEventObservers:"
+ "setMask:"
+ "setPointerEventObservers:"
+ "setPointerEventSource:"
+ "setScrollEventObservers:"
+ "setScrollEventSource:"
+ "setSet:"
+ "setTouchedDidChangeHandler:"
+ "setX:"
+ "setY:"
+ "touchedDidChangeHandler"
+ "touchedSources"
+ "v16@?0@\"<_GCButtonEvent>\"8"
+ "v16@?0@\"<_GCDigitizerEvent>\"8"
+ "v16@?0@\"<_GCPointerEvent>\"8"
+ "v16@?0@\"<_GCScrollEvent>\"8"
+ "v24@0:8@\"<_GCButtonEventSource>\"16"
+ "v24@0:8@\"<_GCDigitizerEventSource>\"16"
+ "v24@0:8@\"<_GCPointerEventSource>\"16"
+ "v24@0:8@\"<_GCScrollEventSource>\"16"
+ "v24@0:8@?<v@?@\"<GCPhysicalInputElement>\"@\"<GCAxis2DInput>\"{GCPoint2=ff}>16"
+ "v24@0:8@?<v@?@\"<GCPhysicalInputElement>\"@\"<GCTouchedStateInput>\"B>16"
+ "v24@0:8^{?=[22{?=@BB(?={?=iBfq}{?=iiii})iBBB@@@}]BB}16"
+ "v24@0:8r^{?=[22{?=@BB(?={?=iBfq}{?=iiii})iBBB@@@}]BB}16"
+ "v32@0:8@16^{?=[22{?=@BB(?={?=iBfq}{?=iiii})iBBB@@@}]BB}24"
+ "v32@0:8^{?=[22{?=@BB(?={?=iBfq}{?=iiii})iBBB@@@}]BB}16@24"
+ "valueWithGCPoint2:"
+ "x"
+ "xyAxes"
+ "xySources"
+ "y"
+ "{%.*g, %.*g}"
+ "{?=\"mask\"Q\"buttons\"[47f]}"
+ "{GCPoint2=ff}"
+ "{GCPoint2=ff}16@0:8"
- "\x01\xf0\xa2"
- "\x04\x12"
- "\x11?\x0f\x0f\x0f\b\x11\""
- "4\x11\x17"
- "<%@ %p> {\n\tGCExtendedEventInputDpadUp: %@\n\tGCExtendedEventInputDpadDown: %@\n\tGCExtendedEventInputDpadLeft: %@\n\tGCExtendedEventInputDpadRight: %@\n\tGCExtendedEventInputButtonA: %@\n\tGCExtendedEventInputButtonB: %@\n\tGCExtendedEventInputButtonX: %@\n\tGCExtendedEventInputButtonY: %@\n\tGCExtendedEventInputLeftShoulder: %@\n\tGCExtendedEventInputRightShoulder: %@\n\tGCExtendedEventInputLeftThumbstickUp: %@\n\tGCExtendedEventInputLeftThumbstickDown: %@\n\tGCExtendedEventInputLeftThumbstickLeft: %@\n\tGCExtendedEventInputLeftThumbstickRight: %@\n\tGCExtendedEventInputRightThumbstickUp: %@\n\tGCExtendedEventInputRightThumbstickDown: %@\n\tGCExtendedEventInputRightThumbstickLeft: %@\n\tGCExtendedEventInputRightThumbstickRight: %@\n\tGCExtendedEventInputLeftTrigger: %@\n\tGCExtendedEventInputRightTrigger: %@\n\tGCExtendedEventInputLeftThumbstickButton: %@\n\tGCExtendedEventInputRightThumbstickButton: %@\n\tGCExtendedEventInputButtonHome: %@\n\tGCExtendedEventInputButtonMenu: %@\n\tGCExtendedEventInputButtonOptions: %@\n\tGCExtendedEventInputButtonSpecial0: %@\n\tGCExtendedEventInputButtonSpecial1: %@\n\tGCExtendedEventInputButtonSpecial2: %@\n\tGCExtendedEventInputButtonSpecial3: %@\n\tGCExtendedEventInputButtonSpecial4: %@\n\tGCExtendedEventInputButtonSpecial5: %@\n\tGCExtendedEventInputButtonSpecial6: %@\n\tGCExtendedEventInputButtonSpecial7: %@\n\tGCExtendedEventInputButtonSpecial8: %@\n\tGCExtendedEventInputButtonSpecial9: %@\n\tGCExtendedEventInputButtonSpecial10: %@\n\tGCExtendedEventInputButtonSpecial11: %@\n\tGCExtendedEventInputButtonSpecial12: %@\n\tGCExtendedEventInputButtonSpecial13: %@\n\tGCExtendedEventInputButtonSpecial14: %@\n\tGCExtendedEventInputButtonShare: %@\n\tGCExtendedEventInputButtonL4: %@\n\tGCExtendedEventInputButtonL5: %@\n\tGCExtendedEventInputButtonR4: %@\n\tGCExtendedEventInputButtonR5: %@\n}"
- "<%@ %p> {\n\tGCExtendedEventInputDpadUp: %f\n\tGCExtendedEventInputDpadDown: %f\n\tGCExtendedEventInputDpadLeft: %f\n\tGCExtendedEventInputDpadRight: %f\n\tGCExtendedEventInputButtonA: %f\n\tGCExtendedEventInputButtonB: %f\n\tGCExtendedEventInputButtonX: %f\n\tGCExtendedEventInputButtonY: %f\n\tGCExtendedEventInputLeftShoulder: %f\n\tGCExtendedEventInputRightShoulder: %f\n\tGCExtendedEventInputLeftThumbstickUp: %f\n\tGCExtendedEventInputLeftThumbstickDown: %f\n\tGCExtendedEventInputLeftThumbstickLeft: %f\n\tGCExtendedEventInputLeftThumbstickRight: %f\n\tGCExtendedEventInputRightThumbstickUp: %f\n\tGCExtendedEventInputRightThumbstickDown: %f\n\tGCExtendedEventInputRightThumbstickLeft: %f\n\tGCExtendedEventInputRightThumbstickRight: %f\n\tGCExtendedEventInputLeftTrigger: %f\n\tGCExtendedEventInputRightTrigger: %f\n\tGCExtendedEventInputLeftThumbstickButton: %f\n\tGCExtendedEventInputRightThumbstickButton: %f\n\tGCExtendedEventInputButtonHome: %f\n\tGCExtendedEventInputButtonMenu: %f\n\tGCExtendedEventInputButtonOptions: %f\n\tGCExtendedEventInputButtonSpecial0: %f\n\tGCExtendedEventInputButtonSpecial1: %f\n\tGCExtendedEventInputButtonSpecial2: %f\n\tGCExtendedEventInputButtonSpecial3: %f\n\tGCExtendedEventInputButtonSpecial4: %f\n\tGCExtendedEventInputButtonSpecial5: %f\n\tGCExtendedEventInputButtonSpecial6: %f\n\tGCExtendedEventInputButtonSpecial7: %f\n\tGCExtendedEventInputButtonSpecial8: %f\n\tGCExtendedEventInputButtonSpecial9: %f\n\tGCExtendedEventInputButtonSpecial10: %f\n\tGCExtendedEventInputButtonSpecial11: %f\n\tGCExtendedEventInputButtonSpecial12: %f\n\tGCExtendedEventInputButtonSpecial13: %f\n\tGCExtendedEventInputButtonSpecial14: %f\n\tGCExtendedEventInputButtonShare: %f\n\tGCExtendedEventInputButtonL4: %f\n\tGCExtendedEventInputButtonL5: %f\n\tGCExtendedEventInputButtonR4: %f\n\tGCExtendedEventInputButtonR5: %f\n}"
- "@24@0:8r^{?=[16{?=@BB(?={?=iBfq}{?=iiii})iBBB@@}]BB}16"
- "@32@0:8@16r^{?=[16{?=@BB(?={?=iBfq}{?=iiii})iBBB@@}]BB}24"
- "@40@0:8Q16[45f]24Q32"
- "@80@0:8{?=@BB(?={?=iBfq}{?=iiii})iBBB@@}16"
- "A\x17"
- "Device has both keyboard and mouse profiles at the same time: %@"
- "Disabling keyboard and mouse support for %d"
- "Enabling keyboard and mouse support for %d"
- "Found Magic mouse or Magic trackpad!"
- "Keyboard/Mouse Client PID %i"
- "KeyboardAndMouseMonitoring"
- "Normal mouse device found!"
- "Posting GCMouseDidBecomeCurrentNotification: %@"
- "Posting GCMouseDidStopBeingCurrentNotification: %@"
- "Removing mouse: %@"
- "T@\"GCController\",&,N,V_proxyController"
- "T@\"GCMouse\",&"
- "T@\"GCMouseInput\",R,N"
- "T@\"NSMutableSet\",&,N,V_aliases"
- "Unknown event with type: %d"
- "[45@\"GCControllerElement\"]"
- "[45{UsagePage_Usage_Pair=\"usagePage\"q\"usage\"q}]"
- "^[45C]"
- "_devicesByRegistryID"
- "_handleDigitizerEvent:"
- "_handleEventImpl:"
- "_handleEventRec:"
- "_hasEnabledKeyboardMouseSupport"
- "_isActive"
- "_legacy_coalescedKeyboard"
- "_legacy_mice"
- "_mouseButtons"
- "_proxyController"
- "_queue_removeDevice:registryID:"
- "_wasInitialized"
- "addMouse:"
- "added to devices by registry id lookup"
- "buttonL4"
- "buttonL5"
- "buttonR4"
- "buttonR5"
- "client - enableKeyboardAndMouseSupport"
- "disableKeyboardAndMouseSupportForPID:"
- "enableFeature:"
- "enableKeyboardAndMouseSupportForPID:"
- "ensureEmulatedControllerWithDevice:added:"
- "handleKeyboardEventAsFrontmostApp:"
- "handleMouseEventAsFrontmostApp:"
- "initWithHapticCommand: %hu"
- "initWithSet:"
- "nameLocalizationKey ="
- "pidsWithKeyboardAndMouseSupport is now %@"
- "posting GCDevice connect notification for %@ device: %@"
- "posting GCDevice disconnect notification for %@ device: %@"
- "proxyController"
- "publishDevice:withNotificationName:"
- "removeDevice:registryID:"
- "setButtonL4:"
- "setButtonL5:"
- "setButtonR4:"
- "setButtonR5:"
- "setProxyController:"
- "shouldAcceptMouseEvents"
- "storeDevice:"
- "unpublishDevice:withNotificationName:"
- "updateCurrentDevice:"
- "updateCurrentDeviceAfterDisconnecting:"
- "updateCurrentMouseAfterDisconnecting:"
- "v24@0:8@\"GCKeyboardEventData\"16"
- "v24@0:8@\"GCMouseEventData\"16"
- "v24@0:8^{?=[16{?=@BB(?={?=iBfq}{?=iiii})iBBB@@}]BB}16"
- "v24@0:8r^{?=[16{?=@BB(?={?=iBfq}{?=iiii})iBBB@@}]BB}16"
- "v32@0:8@16^{?=[16{?=@BB(?={?=iBfq}{?=iiii})iBBB@@}]BB}24"
- "v32@0:8^{?=[16{?=@BB(?={?=iBfq}{?=iiii})iBBB@@}]BB}16@24"
- "{?=\"mask\"Q\"buttons\"[45f]}"

```
