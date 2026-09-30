## GameController

> `/System/Library/Frameworks/GameController.framework/GameController`

```diff

-13.1.8.0.0
-  __TEXT.__text: 0x105848
+13.2.7.0.0
+  __TEXT.__text: 0x1071a0
   __TEXT.__auth_stubs: 0x1c30
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xfd8c
-  __TEXT.__const: 0x3d24
-  __TEXT.__cstring: 0xa179
-  __TEXT.__gcc_except_tab: 0x5964
+  __TEXT.__objc_methlist: 0xff0c
+  __TEXT.__const: 0x3d44
+  __TEXT.__cstring: 0xa279
+  __TEXT.__gcc_except_tab: 0x59ec
   __TEXT.__oslogstring: 0x97d8
   __TEXT.__dlopen_cstrs: 0xfd
   __TEXT.__swift5_typeref: 0x574

   __TEXT.__swift5_types: 0x60
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0xc4
-  __TEXT.__unwind_info: 0x5370
+  __TEXT.__unwind_info: 0x53e8
   __TEXT.__eh_frame: 0xf8
-  __TEXT.__objc_classname: 0x41ad
-  __TEXT.__objc_methname: 0x18f87
-  __TEXT.__objc_methtype: 0x7bcc
-  __TEXT.__objc_stubs: 0xf3a0
+  __TEXT.__objc_classname: 0x41b3
+  __TEXT.__objc_methname: 0x1920b
+  __TEXT.__objc_methtype: 0x7bdd
+  __TEXT.__objc_stubs: 0xf600
   __DATA_CONST.__got: 0xba8
-  __DATA_CONST.__const: 0x2d68
+  __DATA_CONST.__const: 0x2db0
   __DATA_CONST.__objc_classlist: 0x990
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x7e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52c0
+  __DATA_CONST.__objc_selrefs: 0x5358
   __DATA_CONST.__objc_protorefs: 0x4f0
   __DATA_CONST.__objc_superrefs: 0x8c8
   __DATA_CONST.__objc_arraydata: 0x570
   __AUTH_CONST.__auth_got: 0xe30
-  __AUTH_CONST.__const: 0x1f78
-  __AUTH_CONST.__cfstring: 0xb4c0
-  __AUTH_CONST.__objc_const: 0x48ed8
+  __AUTH_CONST.__const: 0x1f98
+  __AUTH_CONST.__cfstring: 0xb800
+  __AUTH_CONST.__objc_const: 0x49440
   __AUTH_CONST.__objc_intobj: 0x14a0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x5010
   __AUTH.__data: 0xe0
-  __DATA.__objc_ivar: 0x17a4
+  __DATA.__objc_ivar: 0x17bc
   __DATA.__data: 0x5e10
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1f10

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 460C387F-A994-39E2-9BC7-A8A12483A3EB
-  Functions: 7372
-  Symbols:   27389
-  CStrings:  9775
+  UUID: 42DCEA15-761C-33C2-9F57-A69853A313CC
+  Functions: 7405
+  Symbols:   27505
+  CStrings:  9859
 
Symbols:
+ +[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]
+ -[GCDeviceSessionConfiguration enableInputEventBufferingPreview]
+ -[GCDeviceSessionConfiguration setEnableInputEventBufferingPreview:]
+ -[GCPhysicalInputElementCollection debugDescription]
+ -[GCPhysicalInputElementCollection description]
+ -[_GCControllerInputComponentDescription enableEventBufferingPreviewForNIS]
+ -[_GCControllerInputComponentDescription setEnableEventBufferingPreviewForNIS:]
+ -[_GCDevicePhysicalInput peekTransaction]
+ -[_GCDevicePhysicalInputAxis2DInput debugDescription]
+ -[_GCDevicePhysicalInputAxis2DInput description]
+ -[_GCDevicePhysicalInputAxisInput debugDescription]
+ -[_GCDevicePhysicalInputAxisInput description]
+ -[_GCDevicePhysicalInputButtonElement physicalExtents]
+ -[_GCDevicePhysicalInputComponent debugDescription]
+ -[_GCDevicePhysicalInputComponent description]
+ -[_GCDevicePhysicalInputComponent enableEventBufferingPreviewForNIS]
+ -[_GCDevicePhysicalInputElement debugDescription]
+ -[_GCDevicePhysicalInputElement description]
+ -[_GCDevicePhysicalInputFacade debugDescription]
+ -[_GCDevicePhysicalInputFacade description]
+ -[_GCDevicePhysicalInputFacade peekNextInputState]
+ -[_GCDevicePhysicalInputPressInput debugDescription]
+ -[_GCDevicePhysicalInputPressInput physicalExtents]
+ -[_GCDevicePhysicalInputSensorInput debugDescription]
+ -[_GCDevicePhysicalInputSensorInput physicalExtents]
+ -[_GCDevicePhysicalInputSensorInput scaledValue]
+ -[_GCDevicePhysicalInputTouchInput debugDescription]
+ -[_GCForceHIDEventParser parseForceForKey:normlaizedWithMinimumValue:maxiumumValue:]
+ -[_GCLegacyDeviceSession orderedControllers]
+ -[_GCLegacyDeviceSession orderedMice]
+ -[_GCLegacyDeviceSession orderedSpatialAccessories]
+ -[_GCLegacyDeviceSession orderedStyli]
+ _OBJC_IVAR_$_GCDeviceSessionConfiguration._enableInputEventBufferingPreview
+ _OBJC_IVAR_$__GCControllerInputComponentDescription._enableEventBufferingPreviewForNIS
+ _OBJC_IVAR_$__GCDevicePhysicalInputComponent._collectionEventBuffer
+ _OBJC_IVAR_$__GCDevicePhysicalInputComponent._eventBufferLock
+ _OBJC_IVAR_$__GCForceHIDEventParser._physicalMax
+ _OBJC_IVAR_$__GCForceHIDEventParser._physicalMin
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.157
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.157.cold.1
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.157.cold.2
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.157.cold.3
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.157.cold.4
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.157.cold.5
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.157.cold.6
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.175
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.175.cold.1
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.175.cold.2
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.175.cold.3
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.175.cold.4
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.175.cold.5
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.175.cold.6
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.cold.1
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.cold.2
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.cold.3
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.cold.4
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.cold.5
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.cold.6
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.cold.7
+ ___105+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:]_block_invoke.cold.8
+ ___44-[_GCLegacyDeviceSession orderedControllers]_block_invoke
+ ___48-[_GCDevicePhysicalInputFacade debugDescription]_block_invoke
+ ___48-[_GCDevicePhysicalInputFacade debugDescription]_block_invoke_2
+ ___65-[_GCDevicePhysicalInputComponent(PubSub) handleCollectionEvent:]_block_invoke_2
+ ___block_descriptor_32_e39_q24?0"GCController"8"GCController"16l
+ ___block_descriptor_32_e63_q24?0"<GCPhysicalInputElement>"8"<GCPhysicalInputElement>"16l
+ ___block_descriptor_40_e8_32o_e25_v32?0"NSString"8Q16^B24ls32l8
+ ___block_literal_global.157
+ ___block_literal_global.227
+ _objc_msgSend$axes
+ _objc_msgSend$compare:options:
+ _objc_msgSend$elementEnumerator
+ _objc_msgSend$enableEventBufferingPreviewForNIS
+ _objc_msgSend$enableInputEventBufferingPreview
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$forceMaxExtent
+ _objc_msgSend$forceMinExtent
+ _objc_msgSend$orderedControllers
+ _objc_msgSend$orderedMice
+ _objc_msgSend$orderedSpatialAccessories
+ _objc_msgSend$orderedStyli
+ _objc_msgSend$parseForceForKey:normlaizedWithMinimumValue:maxiumumValue:
+ _objc_msgSend$peekTransaction
+ _objc_msgSend$physicalExtents
+ _objc_msgSend$setEnableEventBufferingPreviewForNIS:
+ _objc_msgSend$setEnableInputEventBufferingPreview:
+ _objc_msgSend$setForceMaxExtent:
+ _objc_msgSend$setForceMinExtent:
+ _objc_msgSend$switches
- +[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]
- -[GCDeviceCollection orderedCollection]
- -[_GCDevicePhysicalInputButtonElement debugDescription]
- ___39-[GCDeviceCollection orderedCollection]_block_invoke
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157.cold.1
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157.cold.2
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157.cold.3
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157.cold.4
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157.cold.5
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157.cold.6
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.169
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.169.cold.1
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.169.cold.2
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.169.cold.3
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.169.cold.4
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.169.cold.5
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.169.cold.6
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.cold.1
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.cold.2
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.cold.3
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.cold.4
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.cold.5
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.cold.6
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.cold.7
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.cold.8
- ___block_descriptor_32_e11_q24?0816l
- _objc_msgSend$parseForceForKey:
CStrings:
+ "\n)"
+ " = %@,"
+ "\"%@\""
+ "%@ name: '%@', sfsymbol: '%@'"
+ "%@, analog: %s, press = %f%@"
+ "%@, position: %zd"
+ "%@, press = %f%@"
+ "%@, timestamp: %f"
+ "%@, timestamp: %f> ("
+ "%@, value: {up: %f, down: %f, left: %f, right: %f}"
+ "%@, value: {up: %f, down: %f, left: %f, right: %f}, press = %f%@"
+ "%@> {"
+ "%f"
+ "%f%@"
+ "("
+ ")"
+ ","
+ ", \"%@\""
+ ", %zi buttons, %zi axes, %zi switches, %zi dpads"
+ "<%@ %p; "
+ "<%@ %p; '%@'> %@"
+ "<%@ %p> ("
+ "Axis"
+ "DeviceInput "
+ "Dpad"
+ "Element"
+ "EnableInputEventBufferingPreview"
+ "LIVE"
+ "PhysicalMax"
+ "PhysicalMin"
+ "SNAPSHOT"
+ "Switch"
+ "T@\"<GCPhysicalInputExtents>\",R"
+ "TB,N,V_enableEventBufferingPreviewForNIS"
+ "TB,N,V_enableInputEventBufferingPreview"
+ "_collectionEventBuffer"
+ "_enableEventBufferingPreviewForNIS"
+ "_enableInputEventBufferingPreview"
+ "_physicalMax"
+ "_physicalMin"
+ "compare:options:"
+ "enableEventBufferingPreviewForNIS"
+ "enableInputEventBufferingPreview"
+ "enumerateObjectsUsingBlock:"
+ "forceMaxExtent"
+ "forceMinExtent"
+ "orderedControllers"
+ "orderedMice"
+ "orderedSpatialAccessories"
+ "orderedStyli"
+ "parseForceForKey:normlaizedWithMinimumValue:maxiumumValue:"
+ "peekNextInputState"
+ "peekTransaction"
+ "physicalExtents"
+ "q24@?0@\"<GCPhysicalInputElement>\"8@\"<GCPhysicalInputElement>\"16"
+ "q24@?0@\"GCController\"8@\"GCController\"16"
+ "scaledValue"
+ "setEnableEventBufferingPreviewForNIS:"
+ "setEnableInputEventBufferingPreview:"
+ "setForceMaxExtent:"
+ "setForceMinExtent:"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v40@0:8Q16d24d32"
+ "{%f, %f}"
+ "|"
- "<Button %p '%@'; name = '%@', symbol = '%@', analog = %s, source = %zi, value = %f%@>"
- "<Button '%@'; value = %f%@>"
- "<Direction Pad '%@'; up = %f, down = %f, left = %f, right = %f, pressed = %f>"
- "<Direction Pad '%@'; up = %f, down = %f, left = %f, right = %f>"
- "<Joystick '%@'; up = %f, down = %f, left = %f, right = %f>"
- "<PressInput; value = %f%@>"
- "<SensorInput; value = %f>"
- "<Switch '%@'; position = %zd>"
- "<TouchedStateInput; %@>"
- "T@\"<GCPhysicalInputExtents>\",R,C"
- "q24@?0@8@16"

```
