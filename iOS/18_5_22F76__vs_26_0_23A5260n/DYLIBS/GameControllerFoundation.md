## GameControllerFoundation

> `/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation`

```diff

-12.5.2.0.0
-  __TEXT.__text: 0x6bf58
+13.0.28.0.0
+  __TEXT.__text: 0x6dfe8
   __TEXT.__auth_stubs: 0x1420
-  __TEXT.__objc_methlist: 0x6604
+  __TEXT.__objc_methlist: 0x68b4
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x3350
-  __TEXT.__cstring: 0x6a87
-  __TEXT.__oslogstring: 0x305b
+  __TEXT.__gcc_except_tab: 0x3384
+  __TEXT.__cstring: 0x6d1d
+  __TEXT.__oslogstring: 0x30a9
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x2040
+  __TEXT.__unwind_info: 0x20d0
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x1753
-  __TEXT.__objc_methname: 0x889a
-  __TEXT.__objc_methtype: 0x2977
-  __TEXT.__objc_stubs: 0x51c0
+  __TEXT.__objc_classname: 0x174f
+  __TEXT.__objc_methname: 0x8e35
+  __TEXT.__objc_methtype: 0x296a
+  __TEXT.__objc_stubs: 0x51e0
   __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x1b18
+  __DATA_CONST.__const: 0x1b88
   __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c68
+  __DATA_CONST.__objc_selrefs: 0x1d80
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0x140
   __AUTH_CONST.__auth_got: 0xa28
   __AUTH_CONST.__const: 0x548
-  __AUTH_CONST.__cfstring: 0x6ac0
-  __AUTH_CONST.__objc_const: 0x13f40
+  __AUTH_CONST.__cfstring: 0x6d40
+  __AUTH_CONST.__objc_const: 0x14498
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x28a0
+  __AUTH.__objc_data: 0x26c0
   __AUTH.__data: 0x10b0
-  __DATA.__objc_ivar: 0x7e0
+  __DATA.__objc_ivar: 0x854
   __DATA.__data: 0x1080
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x130
-  __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__bss: 0x48
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x120
+  __DATA_DIRTY.__objc_data: 0x500
+  __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EF327038-F1B5-30D0-9BB4-F41CF5817616
-  Functions: 2753
-  Symbols:   9618
-  CStrings:  4174
+  UUID: AAC76E1D-8357-30AD-B402-8C2622E12472
+  Functions: 2837
+  Symbols:   9804
+  CStrings:  4288
 
Symbols:
+ +[GCDevicePhysicalInputJoystickElementDescription supportsSecureCoding]
+ -[GCDevicePhysicalInputButtonElementDescription eventAnalogPressValueField]
+ -[GCDevicePhysicalInputButtonElementDescription eventForceValueField]
+ -[GCDevicePhysicalInputButtonElementDescription eventTouchValueField]
+ -[GCDevicePhysicalInputButtonElementDescription setEventAnalogPressValueField:]
+ -[GCDevicePhysicalInputButtonElementDescription setEventForceValueField:]
+ -[GCDevicePhysicalInputButtonElementDescription setEventTouchValueField:]
+ -[GCDevicePhysicalInputButtonElementDescription setSupportsForce:]
+ -[GCDevicePhysicalInputButtonElementDescription setSupportsTouch:]
+ -[GCDevicePhysicalInputButtonElementDescription setTouchSources:]
+ -[GCDevicePhysicalInputButtonElementDescription setTouchedThreshold:]
+ -[GCDevicePhysicalInputButtonElementDescription supportsForce]
+ -[GCDevicePhysicalInputButtonElementDescription supportsTouch]
+ -[GCDevicePhysicalInputButtonElementDescription touchSources]
+ -[GCDevicePhysicalInputButtonElementDescription touchedThreshold]
+ -[GCDevicePhysicalInputJoystickElementDescription .cxx_destruct]
+ -[GCDevicePhysicalInputJoystickElementDescription analogAxes]
+ -[GCDevicePhysicalInputJoystickElementDescription analogPress]
+ -[GCDevicePhysicalInputJoystickElementDescription copyWithZone:]
+ -[GCDevicePhysicalInputJoystickElementDescription description]
+ -[GCDevicePhysicalInputJoystickElementDescription directionPressedThreshold]
+ -[GCDevicePhysicalInputJoystickElementDescription downSources]
+ -[GCDevicePhysicalInputJoystickElementDescription encodeWithCoder:]
+ -[GCDevicePhysicalInputJoystickElementDescription eventPressValueField]
+ -[GCDevicePhysicalInputJoystickElementDescription eventTouchValueField]
+ -[GCDevicePhysicalInputJoystickElementDescription eventXValueField]
+ -[GCDevicePhysicalInputJoystickElementDescription eventYValueField]
+ -[GCDevicePhysicalInputJoystickElementDescription initWithCoder:]
+ -[GCDevicePhysicalInputJoystickElementDescription init]
+ -[GCDevicePhysicalInputJoystickElementDescription isEqual:]
+ -[GCDevicePhysicalInputJoystickElementDescription leftSources]
+ -[GCDevicePhysicalInputJoystickElementDescription pressSources]
+ -[GCDevicePhysicalInputJoystickElementDescription pressedThreshold]
+ -[GCDevicePhysicalInputJoystickElementDescription rightSources]
+ -[GCDevicePhysicalInputJoystickElementDescription setAnalogAxes:]
+ -[GCDevicePhysicalInputJoystickElementDescription setAnalogPress:]
+ -[GCDevicePhysicalInputJoystickElementDescription setDirectionPressedThreshold:]
+ -[GCDevicePhysicalInputJoystickElementDescription setDownSources:]
+ -[GCDevicePhysicalInputJoystickElementDescription setEventPressValueField:]
+ -[GCDevicePhysicalInputJoystickElementDescription setEventTouchValueField:]
+ -[GCDevicePhysicalInputJoystickElementDescription setEventXValueField:]
+ -[GCDevicePhysicalInputJoystickElementDescription setEventYValueField:]
+ -[GCDevicePhysicalInputJoystickElementDescription setLeftSources:]
+ -[GCDevicePhysicalInputJoystickElementDescription setPressSources:]
+ -[GCDevicePhysicalInputJoystickElementDescription setPressedThreshold:]
+ -[GCDevicePhysicalInputJoystickElementDescription setRightSources:]
+ -[GCDevicePhysicalInputJoystickElementDescription setSupportsPress:]
+ -[GCDevicePhysicalInputJoystickElementDescription setSupportsTouch:]
+ -[GCDevicePhysicalInputJoystickElementDescription setTouchSources:]
+ -[GCDevicePhysicalInputJoystickElementDescription setTouchedThreshold:]
+ -[GCDevicePhysicalInputJoystickElementDescription setUpSources:]
+ -[GCDevicePhysicalInputJoystickElementDescription setXSources:]
+ -[GCDevicePhysicalInputJoystickElementDescription setXySources:]
+ -[GCDevicePhysicalInputJoystickElementDescription setYSources:]
+ -[GCDevicePhysicalInputJoystickElementDescription supportsPress]
+ -[GCDevicePhysicalInputJoystickElementDescription supportsTouch]
+ -[GCDevicePhysicalInputJoystickElementDescription touchSources]
+ -[GCDevicePhysicalInputJoystickElementDescription touchedThreshold]
+ -[GCDevicePhysicalInputJoystickElementDescription upSources]
+ -[GCDevicePhysicalInputJoystickElementDescription xSources]
+ -[GCDevicePhysicalInputJoystickElementDescription xySources]
+ -[GCDevicePhysicalInputJoystickElementDescription ySources]
+ -[GCHIDEventSystemClient _onqueue_services:added:removed:]
+ -[GCHIDEventSystemClient _servicesQueue]
+ -[GCHIDEventSystemClient eventQueue]
+ -[GCHIDEventSystemClient servicesQueue]
+ -[GCHIDEventSystemClient servicesUpdatedAsynchronously]
+ -[GCHIDEventSystemClient setEventQueue:]
+ -[GCHIDEventSystemClient setEventQueue:].cold.1
+ -[GCHIDEventSystemClient setServicesQueue:]
+ -[GCHIDEventSystemClient setServicesQueue:].cold.1
+ -[GCHIDEventSystemClient setServicesUpdatedAsynchronously:]
+ -[GCHIDEventSystemClient setServicesUpdatedAsynchronously:].cold.1
+ -[GCHIDEventSystemClient unregisterServicesChangedObserver:notifyExisting:].cold.1
+ -[_GCDeviceDBBundleDevicePersonalitiesEnumerator nextObject].cold.1
+ -[_GCFLocalizedString initWithCoder:].cold.2
+ -[_GCFLocalizedString initWithCoder:].cold.3
+ -[_GCFStaticLocalizedString bundle].cold.1
+ _CFAllocatorAllocateTyped
+ _GCPrepareIOCFPlugInVtbl.cold.2
+ _IOGCDeviceInterfacePrepareObjCVtbl.cold.2
+ _OBJC_CLASS_$_GCDevicePhysicalInputJoystickElementDescription
+ _OBJC_IVAR_$_GCDevicePhysicalInputButtonElementDescription._eventAnalogPressValueField
+ _OBJC_IVAR_$_GCDevicePhysicalInputButtonElementDescription._eventForceValueField
+ _OBJC_IVAR_$_GCDevicePhysicalInputButtonElementDescription._eventTouchValueField
+ _OBJC_IVAR_$_GCDevicePhysicalInputButtonElementDescription._supportsForce
+ _OBJC_IVAR_$_GCDevicePhysicalInputButtonElementDescription._supportsTouch
+ _OBJC_IVAR_$_GCDevicePhysicalInputButtonElementDescription._touchSources
+ _OBJC_IVAR_$_GCDevicePhysicalInputButtonElementDescription._touchedThreshold
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._analogAxes
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._analogPress
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._directionPressedThreshold
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._downSources
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._eventPressValueField
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._eventTouchValueField
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._eventXValueField
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._eventYValueField
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._leftSources
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._pressSources
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._pressedThreshold
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._rightSources
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._supportsPress
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._supportsTouch
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._touchSources
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._touchedThreshold
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._upSources
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._xSources
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._xySources
+ _OBJC_IVAR_$_GCDevicePhysicalInputJoystickElementDescription._ySources
+ _OBJC_IVAR_$_GCHIDEventSystemClient._eventQueue
+ _OBJC_IVAR_$_GCHIDEventSystemClient._isModifyingMatchCriteria
+ _OBJC_IVAR_$_GCHIDEventSystemClient._servicesQueue
+ _OBJC_IVAR_$_GCHIDEventSystemClient._servicesUpdatedAsynchronously
+ _OBJC_METACLASS_$_GCDevicePhysicalInputJoystickElementDescription
+ __OBJC_$_CLASS_METHODS_GCDevicePhysicalInputJoystickElementDescription
+ __OBJC_$_CLASS_PROP_LIST_GCDevicePhysicalInputJoystickElementDescription
+ __OBJC_$_INSTANCE_METHODS_GCDevicePhysicalInputJoystickElementDescription
+ __OBJC_$_INSTANCE_VARIABLES_GCDevicePhysicalInputJoystickElementDescription
+ __OBJC_$_PROP_LIST_GCDevicePhysicalInputJoystickElementDescription
+ __OBJC_CLASS_PROTOCOLS_$_GCDevicePhysicalInputJoystickElementDescription
+ __OBJC_CLASS_RO_$_GCDevicePhysicalInputJoystickElementDescription
+ __OBJC_METACLASS_RO_$_GCDevicePhysicalInputJoystickElementDescription
+ ___IOGCDEVICEMANAGER_IS_CALLING_OUT_TO_CLIENT_MATCH_HANDLER__
+ ___IOGCDEVICE_IS_CALLING_OUT_TO_CLIENT_REMOVAL_HANDLER__
+ _____EventCallback_block_invoke.167
+ _____EventCallback_block_invoke.167.cold.1
+ _____IOGCDeviceManagerHandleDevices_block_invoke.36
+ _____IOGCDeviceManagerHandleDevices_block_invoke.cold.1
+ _____ServiceMatchedCallback_block_invoke
+ _____ServiceMatchedCallback_block_invoke.cold.1
+ _____ServiceMatchedCallback_block_invoke.cold.2
+ _____ServiceRemovedCallback_block_invoke
+ _____ServiceRemovedCallback_block_invoke.cold.1
+ _____ServiceRemovedCallback_block_invoke.cold.2
+ ___block_descriptor_48_e46_v28?0Q8"NSObject<OS_dispatch_mach_msg>"16i24ls32l8
+ ___block_descriptor_48_e8_32o40o_e19_v16?0"GCPromise"8ls32l8s40l8
+ ___block_descriptor_48_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_64_e8_32o_e5_v8?0ls32l8
+ _dispatch_sync
+ _objc_msgSend$futureOnQueue:withBlock:
- +[GCDevicePhysicalInputCapacitiveButtonElementDescription supportsSecureCoding]
- -[GCDevicePhysicalInputCapacitiveButtonElementDescription copyWithZone:]
- -[GCDevicePhysicalInputCapacitiveButtonElementDescription encodeWithCoder:]
- -[GCDevicePhysicalInputCapacitiveButtonElementDescription eventTouchedValueField]
- -[GCDevicePhysicalInputCapacitiveButtonElementDescription initWithCoder:]
- -[GCDevicePhysicalInputCapacitiveButtonElementDescription init]
- -[GCDevicePhysicalInputCapacitiveButtonElementDescription isEqual:]
- -[GCDevicePhysicalInputCapacitiveButtonElementDescription setEventTouchedValueField:]
- -[GCDevicePhysicalInputCapacitiveButtonElementDescription setTouchedThreshold:]
- -[GCDevicePhysicalInputCapacitiveButtonElementDescription touchedThreshold]
- _CFAllocatorAllocate
- _OBJC_CLASS_$_GCDevicePhysicalInputCapacitiveButtonElementDescription
- _OBJC_IVAR_$_GCDevicePhysicalInputCapacitiveButtonElementDescription._eventTouchedValueField
- _OBJC_IVAR_$_GCDevicePhysicalInputCapacitiveButtonElementDescription._touchedThreshold
- _OBJC_METACLASS_$_GCDevicePhysicalInputCapacitiveButtonElementDescription
- _OUTLINED_FUNCTION_18
- __OBJC_$_CLASS_METHODS_GCDevicePhysicalInputCapacitiveButtonElementDescription
- __OBJC_$_CLASS_PROP_LIST_GCDevicePhysicalInputCapacitiveButtonElementDescription
- __OBJC_$_INSTANCE_METHODS_GCDevicePhysicalInputCapacitiveButtonElementDescription
- __OBJC_$_INSTANCE_VARIABLES_GCDevicePhysicalInputCapacitiveButtonElementDescription
- __OBJC_$_PROP_LIST_GCDevicePhysicalInputCapacitiveButtonElementDescription
- __OBJC_CLASS_PROTOCOLS_$_GCDevicePhysicalInputCapacitiveButtonElementDescription
- __OBJC_CLASS_RO_$_GCDevicePhysicalInputCapacitiveButtonElementDescription
- __OBJC_METACLASS_RO_$_GCDevicePhysicalInputCapacitiveButtonElementDescription
- ___ServiceMatchedCallback.cold.1
- ___ServiceRemovedCallback.cold.1
- _____EventCallback_block_invoke.cold.1
- _____IOGCDeviceManagerHandleDevices_block_invoke_4
- ___block_descriptor_40_e8_32o_e46_v28?0Q8"NSObject<OS_dispatch_mach_msg>"16i24ls32l8
- ___chkstk_darwin
- _objc_retain_x28
CStrings:
+ "\""
+ "#NOTE Duplicate HID Service Matched: serviceID='%#010llx'"
+ "#NOTE Un-tracked HID Service Removed: serviceID='%#010llx'"
+ "%@ #ERROR Failed to setup disconnection observation of %@.  Device will be ignored."
+ ")"
+ "@\"GCFuture\"28@0:8@\"<GCHIDSystemServiceMatchObserver>\"16B24"
+ "@28@0:8@16B24"
+ "BUG IN CLIENT OF GCIOCFPlugInInterfaceObjC: vtbl offset out of supported range."
+ "BUG IN CLIENT OF IOGCDeviceInterface: vtbl offset out of supported range."
+ "Button %@ %@ P:%#zx V:%#zx T:%#zx F:%#zx"
+ "Decoded localized string is missing 'bundle'."
+ "Decoded localized string is missing 'key'."
+ "GCDevicePhysicalInputJoystickElementDescription"
+ "Joystick %@ %@ X%#zx Y%#zx P%#zx T%#zx"
+ "T@\"NSArray\",C,N,V_pressSources"
+ "T@\"NSArray\",C,N,V_touchSources"
+ "T@\"NSObject<OS_dispatch_queue>\",&"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N"
+ "TB,N"
+ "TB,N,V_analogAxes"
+ "TB,N,V_analogPress"
+ "TB,N,V_supportsForce"
+ "TB,N,V_supportsPress"
+ "TB,N,V_supportsTouch"
+ "TQ,N,V_eventAnalogPressValueField"
+ "TQ,N,V_eventForceValueField"
+ "TQ,N,V_eventPressValueField"
+ "TQ,N,V_eventTouchValueField"
+ "TQ,N,V_eventXValueField"
+ "TQ,N,V_eventYValueField"
+ "Tf,N,V_directionPressedThreshold"
+ "The source bundle of static localized string '%@' could not be determined.  This is a #BUG."
+ "_analogAxes"
+ "_analogPress"
+ "_directionPressedThreshold"
+ "_eventAnalogPressValueField"
+ "_eventForceValueField"
+ "_eventPressValueField"
+ "_eventQueue"
+ "_eventTouchValueField"
+ "_eventXValueField"
+ "_eventYValueField"
+ "_isModifyingMatchCriteria"
+ "_pressSources"
+ "_servicesQueue"
+ "_servicesUpdatedAsynchronously"
+ "_supportsForce"
+ "_supportsPress"
+ "_supportsTouch"
+ "_touchSources"
+ "analogAxes"
+ "analogPress"
+ "coder"
+ "directionPressedThreshold"
+ "eventAnalogPressValueField"
+ "eventForceValueField"
+ "eventPressValueField"
+ "eventQueue"
+ "eventTouchValueField"
+ "eventXValueField"
+ "eventYValueField"
+ "pressSources"
+ "servicesQueue"
+ "servicesUpdatedAsynchronously"
+ "setAnalogAxes:"
+ "setAnalogPress:"
+ "setDirectionPressedThreshold:"
+ "setEventAnalogPressValueField:"
+ "setEventForceValueField:"
+ "setEventPressValueField:"
+ "setEventQueue:"
+ "setEventTouchValueField:"
+ "setEventXValueField:"
+ "setEventYValueField:"
+ "setPressSources:"
+ "setServicesQueue:"
+ "setServicesUpdatedAsynchronously:"
+ "setSupportsForce:"
+ "setSupportsPress:"
+ "setSupportsTouch:"
+ "setTouchSources:"
+ "supportsForce"
+ "supportsPress"
+ "supportsTouch"
+ "touchSources"
- "#WARNING Duplicate HID Service Matched: serviceID='%#010llx'"
- "#WARNING Un-tracked HID Service Removed: serviceID='%#010llx'"
- "@\"<GCHIDSystemServiceInfo>\"24@0:8Q16"
- "Button %@ %#zx %@"
- "GCDevicePhysicalInputCapacitiveButtonElementDescription"
- "v28@0:8@\"<GCHIDSystemServiceMatchObserver>\"16B24"

```
