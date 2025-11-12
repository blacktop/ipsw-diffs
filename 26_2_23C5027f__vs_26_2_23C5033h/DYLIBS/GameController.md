## GameController

> `/System/Library/Frameworks/GameController.framework/GameController`

```diff

-13.2.7.0.0
-  __TEXT.__text: 0x1071a0
+13.2.8.0.0
+  __TEXT.__text: 0x10716c
   __TEXT.__auth_stubs: 0x1c30
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xff0c

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 42DCEA15-761C-33C2-9F57-A69853A313CC
-  Functions: 7405
-  Symbols:   27505
+  UUID: FC481C26-1431-3C73-B4AF-B759447630D3
+  Functions: 7404
+  Symbols:   27503
   CStrings:  9859
 
Functions:
- _OUTLINED_FUNCTION_5
~ ___66-[_GCCollectionEventHIDAdapter initWithRootParser:source:service:]_block_invoke : 404 -> 648
+ _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_18
~ -[GCGearShifterElement _setSources:] : 184 -> 200
~ -[GCGearShifterElement _sources] : 48 -> 44
~ -[GCGearShifterElement _positionDidChangeHandler] : 52 -> 48
~ -[GCGearShifterElement _setPositionDidChangeHandler:] : 96 -> 92
~ -[GCGearShifterElement _lastPositionTimestamp] : 60 -> 56
~ -[GCGearShifterElement _deltaDidChangeHandler] : 52 -> 48
~ -[GCGearShifterElement _setDeltaDidChangeHandler:] : 96 -> 92
~ -[GCGearShifterElement _delta] : 64 -> 60
~ -[GCGearShifterElement _lastDeltaTimestamp] : 60 -> 56
~ -[GCMouseInput handleScrollEventWithDelta:] : 468 -> 464
~ -[GCDeviceSession _updateEventDelivery] : 168 -> 164
~ -[_GCDevicePhysicalInputInitializationContext _stateMagic:] : 84 -> 92
~ -[_GCDevicePhysicalInputPressInput _setSources:] : 180 -> 196
~ -[_GCDevicePhysicalInputPressInput _sources] : 48 -> 44
~ -[_GCDevicePhysicalInputPressInput _isAnalog] : 52 -> 48
~ -[_GCDevicePhysicalInputPressInput _pressedThreshold] : 56 -> 52
~ -[_GCDevicePhysicalInputPressInput _valueDidChangeHandler] : 48 -> 44
~ -[_GCDevicePhysicalInputPressInput _setValueDidChangeHandler:] : 92 -> 88
~ -[_GCDevicePhysicalInputPressInput _value] : 56 -> 52
~ -[_GCDevicePhysicalInputPressInput _lastValueTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputPressInput _lastPressedTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputPressInput value] : 56 -> 52
~ -[_GCDevicePhysicalInputPressInput isAnalog] : 52 -> 48
~ -[_GCDevicePhysicalInputPressInput lastValueTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputPressInput isPressed] : 112 -> 108
~ -[_GCDevicePhysicalInputPressInput lastPressedStateTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputTouchInput _setSources:] : 180 -> 196
~ -[_GCDevicePhysicalInputTouchInput _sources] : 48 -> 44
~ -[_GCDevicePhysicalInputTouchInput _touchedThreshold] : 56 -> 52
~ -[_GCDevicePhysicalInputTouchInput _value] : 56 -> 52
~ -[_GCDevicePhysicalInputTouchInput _lastTouchedTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputTouchInput isTouched] : 112 -> 108
~ -[_GCDevicePhysicalInputTouchInput lastTouchedStateTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputJoystickElement _press] : 88 -> 84
~ -[_GCDevicePhysicalInputJoystickElement _touch] : 88 -> 84
~ -[_GCDevicePhysicalInputJoystickElement _xy] : 72 -> 68
~ -[_GCDevicePhysicalInputJoystickElement _x] : 72 -> 68
~ -[_GCDevicePhysicalInputJoystickElement _y] : 72 -> 68
~ -[_GCDevicePhysicalInputJoystickElement _up] : 72 -> 68
~ -[_GCDevicePhysicalInputJoystickElement _down] : 72 -> 68
~ -[_GCDevicePhysicalInputJoystickElement _left] : 72 -> 68
~ -[_GCDevicePhysicalInputJoystickElement _right] : 72 -> 68
~ -[_GCDevicePhysicalInputSwitchElement _setSources:] : 180 -> 196
~ -[_GCDevicePhysicalInputSwitchElement _sources] : 48 -> 44
~ -[_GCDevicePhysicalInputSwitchElement _positionDidChangeHandler] : 48 -> 44
~ -[_GCDevicePhysicalInputSwitchElement _setPositionDidChangeHandler:] : 92 -> 88
~ -[_GCDevicePhysicalInputSwitchElement _lastPositionTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputSwitchElement lastPositionTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputClickableDirectionPadElement _pressedInput] : 76 -> 72
~ -[_GCHIDServiceAuditor noteHIDEventReceived:] : 68 -> 64
~ -[_GCHIDEventSubjectAuditor noteHIDEventReceived:] : 192 -> 208
~ -[_GCHIDEventSubjectAuditor noteHIDEventPublished:] : 160 -> 172
~ -[_GCDevicePhysicalInputStateTable updateStateTableWithContentsOf:] : 668 -> 688
~ -[_GCDevicePhysicalInputMutableStateTable allocatePrimitiveSlot] : 64 -> 60
~ -[_GCDevicePhysicalInputAxisInput _setSources:] : 180 -> 196
~ -[_GCDevicePhysicalInputAxisInput _sources] : 48 -> 44
~ -[_GCDevicePhysicalInputAxisInput _valueDidChangeHandler] : 48 -> 44
~ -[_GCDevicePhysicalInputAxisInput _setValueDidChangeHandler:] : 92 -> 88
~ -[_GCDevicePhysicalInputAxisInput _value] : 56 -> 52
~ -[_GCDevicePhysicalInputAxisInput _lastValueTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputAxisInput value] : 56 -> 52
~ -[_GCDevicePhysicalInputAxisInput lastValueTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputAxisInput update:withValue:timestamp:] : 200 -> 196
~ -[_GCDevicePhysicalInputAxis2DInput _setSources:] : 180 -> 196
~ -[_GCDevicePhysicalInputAxis2DInput _sources] : 48 -> 44
~ -[_GCDevicePhysicalInputAxis2DInput _valueDidChangeHandler] : 48 -> 44
~ -[_GCDevicePhysicalInputAxis2DInput _setValueDidChangeHandler:] : 92 -> 88
~ -[_GCDevicePhysicalInputAxis2DInput _value] : 60 -> 56
~ -[_GCDevicePhysicalInputAxis2DInput _lastValueTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputAxis2DInput value] : 60 -> 56
~ -[_GCDevicePhysicalInputAxis2DInput lastValueTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputAxis2DInput update:withValue:timestamp:] : 220 -> 216
~ -[GCSteeringWheelElement _setSources:] : 184 -> 200
~ -[GCSteeringWheelElement _sources] : 48 -> 44
~ -[GCSteeringWheelElement _maximumDegreesOfRotation] : 56 -> 52
~ -[GCSteeringWheelElement _valueDidChangeHandler] : 48 -> 44
~ -[GCSteeringWheelElement _setValueDidChangeHandler:] : 76 -> 72
~ -[GCSteeringWheelElement _deltaDidChangeHandler] : 48 -> 44
~ -[GCSteeringWheelElement _setDeltaDidChangeHandler:] : 76 -> 72
~ -[GCSteeringWheelElement _value] : 56 -> 52
~ -[GCSteeringWheelElement _delta] : 56 -> 52
~ -[GCSteeringWheelElement _lastTimestamp] : 56 -> 52
~ -[GCSteeringWheelElement maximumDegreesOfRotation] : 56 -> 52
~ -[GCSteeringWheelElement value] : 56 -> 52
~ -[GCSteeringWheelElement lastValueTimestamp] : 56 -> 52
~ -[GCSteeringWheelElement delta] : 56 -> 52
~ -[GCSteeringWheelElement lastDeltaTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputSensorInput _minimumValue] : 56 -> 52
~ -[_GCDevicePhysicalInputSensorInput _maximumValue] : 56 -> 52
~ -[_GCDevicePhysicalInputSensorInput _valueDidChangeHandler] : 48 -> 44
~ -[_GCDevicePhysicalInputSensorInput _setValueDidChangeHandler:] : 92 -> 88
~ -[_GCDevicePhysicalInputSensorInput _value] : 56 -> 52
~ -[_GCDevicePhysicalInputSensorInput _lastValueTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputSensorInput isEqualToInput:] : 328 -> 324
~ -[_GCDevicePhysicalInputSensorInput value] : 60 -> 56
~ -[_GCDevicePhysicalInputSensorInput lastValueTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputSensorInput minimumValue] : 56 -> 52
~ -[_GCDevicePhysicalInputSensorInput maximumValue] : 56 -> 52
~ -[_GCDevicePhysicalInputSensorInput update:withValue:timestamp:] : 200 -> 196
~ -[_GCDevicePhysicalInputDirectionPadElement _xy] : 72 -> 68
~ -[_GCDevicePhysicalInputDirectionPadElement _x] : 72 -> 68
~ -[_GCDevicePhysicalInputDirectionPadElement _y] : 72 -> 68
~ -[_GCDevicePhysicalInputDirectionPadElement _up] : 72 -> 68
~ -[_GCDevicePhysicalInputDirectionPadElement _down] : 72 -> 68
~ -[_GCDevicePhysicalInputDirectionPadElement _left] : 72 -> 68
~ -[_GCDevicePhysicalInputDirectionPadElement _right] : 72 -> 68
~ -[_GCDevicePhysicalInputCapacitiveDirectionPadElement _touchedInput] : 76 -> 72
~ -[GCSyntheticDeviceManager _kernel_open:] : 100 -> 96
~ -[GCSyntheticDeviceManager _kernel_terminateAllDevices:] : 84 -> 80
~ -[_GCDevicePhysicalInput setTransactionQueueDepth:] : 112 -> 120
~ -[_GCDevicePhysicalInput handleGamepadEvent:] : 176 -> 172
~ -[_GCDevicePhysicalInput handleMouseEvent:] : 104 -> 100
~ -[_GCDevicePhysicalInput handleCollectionEvent:] : 176 -> 172
~ -[_GCDevicePhysicalInputElement _localizedName] : 48 -> 44
~ -[_GCDevicePhysicalInputElement _symbol] : 48 -> 44
~ -[_GCDevicePhysicalInputButtonElement _setSources:] : 180 -> 196
~ -[_GCDevicePhysicalInputButtonElement _touch] : 92 -> 88
~ -[_GCDevicePhysicalInputButtonElement _force] : 92 -> 88
~ -[_GCDevicePhysicalInputButtonElement _sources] : 48 -> 44
~ -[_GCDevicePhysicalInputButtonElement _isAnalog] : 52 -> 48
~ -[_GCDevicePhysicalInputButtonElement _pressedThreshold] : 56 -> 52
~ -[_GCDevicePhysicalInputButtonElement _valueDidChangeHandler] : 48 -> 44
~ -[_GCDevicePhysicalInputButtonElement _setValueDidChangeHandler:] : 76 -> 72
~ -[_GCDevicePhysicalInputButtonElement _pressedDidChangeHandler] : 48 -> 44
~ -[_GCDevicePhysicalInputButtonElement _setPressedDidChangeHandler:] : 76 -> 72
~ -[_GCDevicePhysicalInputButtonElement _value] : 56 -> 52
~ -[_GCDevicePhysicalInputButtonElement _lastValueTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputButtonElement _lastPressedTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputButtonElement _pressed] : 56 -> 52
~ -[_GCDevicePhysicalInputButtonElement value] : 56 -> 52
~ -[_GCDevicePhysicalInputButtonElement isAnalog] : 52 -> 48
~ -[_GCDevicePhysicalInputButtonElement lastValueTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputButtonElement isPressed] : 112 -> 108
~ -[_GCDevicePhysicalInputButtonElement lastPressedStateTimestamp] : 56 -> 52
~ -[_GCDevicePhysicalInputTransaction detach] : 76 -> 84

```
