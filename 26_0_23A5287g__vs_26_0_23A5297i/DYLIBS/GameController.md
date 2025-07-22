## GameController

> `/System/Library/Frameworks/GameController.framework/GameController`

```diff

-13.0.32.0.0
-  __TEXT.__text: 0xf93e8
+13.0.36.0.0
+  __TEXT.__text: 0xfad18
   __TEXT.__auth_stubs: 0x1780
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xfa3c
-  __TEXT.__const: 0x3364
-  __TEXT.__cstring: 0x9da4
-  __TEXT.__gcc_except_tab: 0x578c
-  __TEXT.__oslogstring: 0x9729
+  __TEXT.__objc_methlist: 0xfb8c
+  __TEXT.__const: 0x3374
+  __TEXT.__cstring: 0x9de6
+  __TEXT.__gcc_except_tab: 0x58b4
+  __TEXT.__oslogstring: 0x97fd
   __TEXT.__dlopen_cstrs: 0xfd
   __TEXT.__swift5_typeref: 0x2ac
   __TEXT.__swift5_reflstr: 0x13f

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x20
-  __TEXT.__unwind_info: 0x5088
-  __TEXT.__objc_classname: 0x410f
-  __TEXT.__objc_methname: 0x189ea
-  __TEXT.__objc_methtype: 0x7a51
-  __TEXT.__objc_stubs: 0xf0c0
+  __TEXT.__unwind_info: 0x50e8
+  __TEXT.__objc_classname: 0x4163
+  __TEXT.__objc_methname: 0x18b84
+  __TEXT.__objc_methtype: 0x7a92
+  __TEXT.__objc_stubs: 0xf240
   __DATA_CONST.__got: 0xb28
-  __DATA_CONST.__const: 0x2d58
-  __DATA_CONST.__objc_classlist: 0x958
+  __DATA_CONST.__const: 0x2d30
+  __DATA_CONST.__objc_classlist: 0x970
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x7a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5148
+  __DATA_CONST.__objc_selrefs: 0x5198
   __DATA_CONST.__objc_protorefs: 0x4b8
-  __DATA_CONST.__objc_superrefs: 0x8a0
+  __DATA_CONST.__objc_superrefs: 0x8b8
   __DATA_CONST.__objc_arraydata: 0x570
   __AUTH_CONST.__auth_got: 0xbd8
   __AUTH_CONST.__const: 0x1438
-  __AUTH_CONST.__cfstring: 0xb240
-  __AUTH_CONST.__objc_const: 0x480c0
+  __AUTH_CONST.__cfstring: 0xb2e0
+  __AUTH_CONST.__objc_const: 0x483d8
   __AUTH_CONST.__objc_intobj: 0x14a0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x5280
+  __AUTH.__objc_data: 0x5370
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0x1764
+  __DATA.__objc_ivar: 0x1780
   __DATA.__data: 0x5bf0
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1550

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: 6572BB63-E951-3163-9715-B684C58E32D6
-  Functions: 6942
-  Symbols:   25915
-  CStrings:  9619
+  UUID: 897881B1-20AC-3E34-BEC9-45CB5177A76E
+  Functions: 6990
+  Symbols:   26054
+  CStrings:  9658
 
Symbols:
+ +[_GCThumbstickHIDEventParser supportsSecureCoding]
+ -[GCSystemButtonServer activeProcessRespondingToSystemButton:]
+ -[GCSystemButtonServer activeProcessRespondingToSystemButton:].cold.1
+ -[GCSystemButtonServer activeProcessRespondingToSystemButton:].cold.2
+ -[GCSystemButtonServer dealloc]
+ -[GCSystemButtonServer responders]
+ -[GCSystemButtonService dealloc]
+ -[GCSystemButtonService debugDescription]
+ -[GCSystemButtonService description]
+ -[GCSystemButtonService respondingProcessBundleIdentifiers]
+ -[_GCDevicePhysicalInputJoystickElement update:forCollectionEvent:withTimestamp:]
+ -[_GCSystemButtonClientProxy _systemButtonRespondersChanged:]
+ -[_GCSystemButtonClientProxy connection]
+ -[_GCSystemButtonClientProxy handleButtonPress].cold.1
+ -[_GCSystemButtonClientProxy observeValueForKeyPath:ofObject:change:context:].cold.2
+ -[_GCSystemButtonResponder .cxx_destruct]
+ -[_GCSystemButtonResponder _initWithBundleIdentifier:]
+ -[_GCSystemButtonResponder bundleIdentifier]
+ -[_GCSystemButtonResponder description]
+ -[_GCSystemButtonResponder init]
+ -[_GCSystemButtonResponder invalidate]
+ -[_GCSystemButtonResponder isInvalid]
+ -[_GCSystemButtonServiceInternal .cxx_destruct]
+ -[_GCSystemButtonServiceInternal _applyLatestConsumerStatus]
+ -[_GCSystemButtonServiceInternal _applyLatestConsumerStatus].cold.1
+ -[_GCSystemButtonServiceInternal _buttonConsumerInvalidated:]
+ -[_GCSystemButtonServiceInternal _invalidate]
+ -[_GCSystemButtonServiceInternal _resumeServerConnection]
+ -[_GCSystemButtonServiceInternal beginConsumingPressesWithReason:consumer:priority:]
+ -[_GCSystemButtonServiceInternal consumeSystemButtonPressEventAtPriority:]
+ -[_GCSystemButtonServiceInternal consumeSystemButtonPressEventAtPriority:].cold.1
+ -[_GCSystemButtonServiceInternal init]
+ -[_GCSystemButtonServiceInternal isAvailable]
+ -[_GCSystemButtonServiceInternal localizedName]
+ -[_GCSystemButtonServiceInternal observeValueForKeyPath:ofObject:change:context:]
+ -[_GCSystemButtonServiceInternal respondingProcessBundleIdentifiers]
+ -[_GCSystemButtonServiceInternal setActiveClientsRespondingToSystemButton:]
+ -[_GCSystemButtonServiceInternal setSystemButtonAvailable:localizedName:sfSymbolName:]
+ -[_GCSystemButtonServiceInternal sfSymbolName]
+ -[_GCThumbstickHIDEventParser description]
+ -[_GCThumbstickHIDEventParser encodeWithCoder:]
+ -[_GCThumbstickHIDEventParser initWithCoder:]
+ -[_GCThumbstickHIDEventParser parse:into:]
+ -[_GCThumbstickHIDEventParser parseXAxisForKey:]
+ -[_GCThumbstickHIDEventParser parseYAxisForKey:]
+ -[_GCThumbstickHIDEventParser requiredOrdinal]
+ -[_GCThumbstickHIDEventParser setRequiredOrdinal:]
+ _OBJC_CLASS_$__GCSystemButtonResponder
+ _OBJC_CLASS_$__GCSystemButtonServiceInternal
+ _OBJC_CLASS_$__GCThumbstickHIDEventParser
+ _OBJC_IVAR_$_GCSystemButtonServer._responders
+ _OBJC_IVAR_$_GCSystemButtonService._impl
+ _OBJC_IVAR_$__GCDefaultLogicalDevice._clientToSystemButtonResponderAssertion
+ _OBJC_IVAR_$__GCSystemButtonResponder._bundleIdentifier
+ _OBJC_IVAR_$__GCSystemButtonResponder._invalid
+ _OBJC_IVAR_$__GCSystemButtonServiceInternal._available
+ _OBJC_IVAR_$__GCSystemButtonServiceInternal._consumers
+ _OBJC_IVAR_$__GCSystemButtonServiceInternal._localizedName
+ _OBJC_IVAR_$__GCSystemButtonServiceInternal._respondingProcessBundleIdentifiers
+ _OBJC_IVAR_$__GCSystemButtonServiceInternal._serverConnection
+ _OBJC_IVAR_$__GCSystemButtonServiceInternal._serverConnectionInterruption
+ _OBJC_IVAR_$__GCSystemButtonServiceInternal._serverConnectionInvalidation
+ _OBJC_IVAR_$__GCSystemButtonServiceInternal._sfSymbolName
+ _OBJC_IVAR_$__GCThumbstickHIDEventParser._requiredOrdinal
+ _OBJC_IVAR_$__GCThumbstickHIDEventParser._xAxisKey
+ _OBJC_IVAR_$__GCThumbstickHIDEventParser._yAxisKey
+ _OBJC_METACLASS_$__GCSystemButtonResponder
+ _OBJC_METACLASS_$__GCSystemButtonServiceInternal
+ _OBJC_METACLASS_$__GCThumbstickHIDEventParser
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ __OBJC_$_CLASS_METHODS__GCThumbstickHIDEventParser
+ __OBJC_$_CLASS_PROP_LIST__GCThumbstickHIDEventParser
+ __OBJC_$_INSTANCE_METHODS_GCSystemGesturesState
+ __OBJC_$_INSTANCE_METHODS__GCSystemButtonResponder
+ __OBJC_$_INSTANCE_METHODS__GCSystemButtonServiceInternal
+ __OBJC_$_INSTANCE_METHODS__GCThumbstickHIDEventParser
+ __OBJC_$_INSTANCE_VARIABLES__GCSystemButtonResponder
+ __OBJC_$_INSTANCE_VARIABLES__GCSystemButtonServiceInternal
+ __OBJC_$_INSTANCE_VARIABLES__GCThumbstickHIDEventParser
+ __OBJC_$_PROP_LIST__GCSystemButtonResponder
+ __OBJC_$_PROP_LIST__GCSystemButtonServiceInternal
+ __OBJC_$_PROP_LIST__GCThumbstickHIDEventParser
+ __OBJC_CLASS_PROTOCOLS_$__GCSystemButtonResponder
+ __OBJC_CLASS_PROTOCOLS_$__GCSystemButtonServiceInternal
+ __OBJC_CLASS_PROTOCOLS_$__GCThumbstickHIDEventParser
+ __OBJC_CLASS_RO_$__GCSystemButtonResponder
+ __OBJC_CLASS_RO_$__GCSystemButtonServiceInternal
+ __OBJC_CLASS_RO_$__GCThumbstickHIDEventParser
+ __OBJC_METACLASS_RO_$__GCSystemButtonResponder
+ __OBJC_METACLASS_RO_$__GCSystemButtonServiceInternal
+ __OBJC_METACLASS_RO_$__GCThumbstickHIDEventParser
+ ___38-[_GCSystemButtonServiceInternal init]_block_invoke
+ ___38-[_GCSystemButtonServiceInternal init]_block_invoke.157
+ ___38-[_GCSystemButtonServiceInternal init]_block_invoke.157.cold.1
+ ___38-[_GCSystemButtonServiceInternal init]_block_invoke.158
+ ___38-[_GCSystemButtonServiceInternal init]_block_invoke.cold.1
+ ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157
+ ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157.cold.1
+ ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157.cold.2
+ ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157.cold.3
+ ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157.cold.4
+ ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157.cold.5
+ ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.157.cold.6
+ ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.cold.5
+ ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.cold.6
+ ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.cold.7
+ ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.cold.8
+ _objc_msgSend$activeProcessRespondingToSystemButton:
+ _objc_msgSend$beginConsumingPressesWithReason:consumer:priority:
+ _objc_msgSend$isAvailable
+ _objc_msgSend$parseXAxisForKey:
+ _objc_msgSend$parseYAxisForKey:
+ _objc_msgSend$peerValueForEntitlement:
+ _objc_msgSend$responders
+ _objc_msgSend$respondingProcessBundleIdentifiers
+ _objc_msgSend$setActiveClientsRespondingToSystemButton:
+ _objc_msgSend$setAnalogAxes:
+ _objc_msgSend$setDirectionPressedThreshold:
+ _objc_msgSend$setEventPressValueField:
+ _objc_msgSend$setSupportsPress:
+ _objc_msgSend$sfSymbolName
- +[GCStylus(Discovery) styluses]
- +[GCSystemGesturesState(NSSecureCoding) supportsSecureCoding]
- -[GCSystemButtonService _applyLatestConsumerStatus]
- -[GCSystemButtonService _applyLatestConsumerStatus].cold.1
- -[GCSystemButtonService _buttonConsumerInvalidated:]
- -[GCSystemButtonService _init]
- -[GCSystemButtonService _resumeServerConnection]
- -[GCSystemButtonService consumeSystemButtonPressEventAtPriority:]
- -[GCSystemButtonService consumeSystemButtonPressEventAtPriority:].cold.1
- -[GCSystemButtonService setSystemButtonAvailable:localizedName:sfSymbolName:]
- -[GCSystemGesturesState(NSSecureCoding) encodeWithCoder:]
- -[GCSystemGesturesState(NSSecureCoding) initWithCoder:]
- -[_GCDefaultPhysicalDevice _workaround_MFiCombinedHomeVendorButton:].cold.1
- -[_GCHIDEventParser parseBooleanEventField:forKey:]
- -[_GCHIDEventParser parseDoubleEventField:forKey:]
- _OBJC_IVAR_$_GCSystemButtonService._available
- _OBJC_IVAR_$_GCSystemButtonService._consumers
- _OBJC_IVAR_$_GCSystemButtonService._localizedName
- _OBJC_IVAR_$_GCSystemButtonService._serverConnection
- _OBJC_IVAR_$_GCSystemButtonService._serverConnectionInterruption
- _OBJC_IVAR_$_GCSystemButtonService._serverConnectionInvalidation
- _OBJC_IVAR_$_GCSystemButtonService._sfSymbolName
- _OBJC_IVAR_$__GCHIDEventParser._booleanMappings
- _OBJC_IVAR_$__GCHIDEventParser._doubleMappings
- __OBJC_$_CLASS_METHODS_GCSystemGesturesState(NSSecureCoding)
- __OBJC_$_INSTANCE_METHODS_GCSystemGesturesState(NSSecureCoding)
- __OBJC_CLASS_PROTOCOLS_$_GCSystemButtonService
- __OBJC_CLASS_PROTOCOLS_$_GCSystemGesturesState(NSSecureCoding)
- ___30-[GCSystemButtonService _init]_block_invoke
- ___30-[GCSystemButtonService _init]_block_invoke.158
- ___30-[GCSystemButtonService _init]_block_invoke.158.cold.1
- ___30-[GCSystemButtonService _init]_block_invoke.159
- ___30-[GCSystemButtonService _init]_block_invoke.cold.1
- ___32-[_GCHIDEventParser parse:into:]_block_invoke
- ___32-[_GCHIDEventParser parse:into:]_block_invoke_2
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.151
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.151.cold.1
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.151.cold.2
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.151.cold.3
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.151.cold.4
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.151.cold.5
- ___95+[_GCSpatialDeviceProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]_block_invoke.151.cold.6
- ___block_descriptor_48_e8_32s_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8
- _objc_msgSend$parseDoubleEventField:forKey:
- _objc_msgSend$styli
CStrings:
+ "%@ %p; %@"
+ "@\"_GCSystemButtonServiceInternal\""
+ "Child element is not a button."
+ "Clients handling system button changed"
+ "ELO detected, deploying HOME button workaround..."
+ "Error processing child element: %@"
+ "Parse 'Thumbstick %zd' Event X->%#llx Y->%#llx"
+ "Reported availability changed: %{BOOL}d -> %{BOOL}d"
+ "Server connection invalidated."
+ "System button responder: %@"
+ "T@\"NSSet\",R,C,V_respondingProcessBundleIdentifiers"
+ "TB,R,GisAvailable"
+ "TQ,N,V_requiredOrdinal"
+ "Unavailable"
+ "Vv24@0:8@\"NSSet\"16"
+ "Vv24@0:8@16"
+ "[GCSystemButtonService] Invalidate"
+ "_GCSystemButtonResponder"
+ "_GCSystemButtonServiceInternal"
+ "_GCThumbstickHIDEventParser"
+ "_clientToSystemButtonResponderAssertion"
+ "_requiredOrdinal"
+ "_responders"
+ "_respondingProcessBundleIdentifiers"
+ "_xAxisKey"
+ "_yAxisKey"
+ "activeProcessRespondingToSystemButton:"
+ "parseXAxisForKey:"
+ "parseYAxisForKey:"
+ "requiredOrdinal"
+ "responders"
+ "respondingProcessBundleIdentifiers"
+ "setActiveClientsRespondingToSystemButton:"
+ "setAnalogAxes:"
+ "setDirectionPressedThreshold:"
+ "setEventPressValueField:"
+ "setRequiredOrdinal:"
+ "setSupportsPress:"
+ "xAxisKey"
+ "yAxisKey"
- "#ERROR Server connection invalidated."
- "Reported availability change: %{BOOL}d -> %{BOOL}d"
- "_booleanMappings"
- "_doubleMappings"
- "booleanMappings"
- "doubleMappings"
- "parseBooleanEventField:forKey:"
- "parseDoubleEventField:forKey:"

```
