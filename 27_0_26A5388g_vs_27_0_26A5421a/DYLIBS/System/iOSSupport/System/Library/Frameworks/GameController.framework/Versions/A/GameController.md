## GameController

> `/System/iOSSupport/System/Library/Frameworks/GameController.framework/Versions/A/GameController`

```diff

-14.0.21.0.0
-  __TEXT.__text: 0xff618
+14.0.24.0.0
+  __TEXT.__text: 0x104328
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xff1c
+  __TEXT.__objc_methlist: 0x100ec
   __TEXT.__const: 0x23fc
-  __TEXT.__gcc_except_tab: 0x3658
-  __TEXT.__cstring: 0xa081
+  __TEXT.__gcc_except_tab: 0x371c
+  __TEXT.__cstring: 0xa111
   __TEXT.__oslogstring: 0x85d8
   __TEXT.__swift5_typeref: 0x878
   __TEXT.__swift5_reflstr: 0x34f

   __TEXT.__swift5_types: 0xb0
   __TEXT.__swift5_capture: 0x10c
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x4d40
+  __TEXT.__unwind_info: 0x4df0
   __TEXT.__eh_frame: 0x170
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2c48
-  __DATA_CONST.__objc_classlist: 0xa28
+  __DATA_CONST.__const: 0x2d18
+  __DATA_CONST.__objc_classlist: 0xa48
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x818
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f30
+  __DATA_CONST.__objc_selrefs: 0x4f50
   __DATA_CONST.__objc_protorefs: 0x4d0
-  __DATA_CONST.__objc_superrefs: 0x900
+  __DATA_CONST.__objc_superrefs: 0x918
   __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__got: 0xdc0
+  __DATA_CONST.__got: 0xdd0
   __AUTH_CONST.__const: 0x23c0
-  __AUTH_CONST.__cfstring: 0xb3a0
-  __AUTH_CONST.__objc_const: 0x4cac0
-  __AUTH_CONST.__objc_intobj: 0x1098
+  __AUTH_CONST.__cfstring: 0xb4e0
+  __AUTH_CONST.__objc_const: 0x4d720
+  __AUTH_CONST.__objc_intobj: 0x10c8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xfe0
-  __AUTH.__objc_data: 0x4b58
+  __AUTH.__objc_data: 0x4c98
   __AUTH.__data: 0x5a0
-  __DATA.__objc_ivar: 0x16a0
+  __DATA.__objc_ivar: 0x16c0
   __DATA.__data: 0x5f10
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x2800
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x1e50
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0x220
+  __DATA_DIRTY.__bss: 0x230
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7682
-  Symbols:   16957
-  CStrings:  2420
+  Functions: 7721
+  Symbols:   17056
+  CStrings:  2430
 
Symbols:
+ +[_GCCollectionEventGamepadEventAdapterConfig supportsSecureCoding]
+ +[_GCCollectionEventGamepadEventAdapterDescription supportsSecureCoding]
+ +[_GCSteam2ControllerProfile deviceManager:prepareLogicalDevice:]
+ +[_GCSteam2ControllerProfile deviceManager:willPublishPhysicalDevice:]
+ +[_GCSteam2ControllerProfile deviceManager]
+ +[_GCSteam2ControllerProfile logicalDevice:getSystemButtonName:sfSymbolName:needsMFiCompatibility:]
+ +[_GCSteam2ControllerProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:]
+ +[_GCSteam2ControllerProfile logicalDevice:makeControllerPhysicalInputProfileDescriptionWithIdentifier:bindings:]
+ +[_GCSteam2ControllerProfile logicalDeviceControllerProductCategory:]
+ +[_GCSteam2ControllerProfile physicalDeviceGetHapticCapabilities:]
+ +[_GCSteam2ControllerProfile physicalDeviceGetHapticCapabilityGraph:]
+ -[_GCCollectionEventGamepadEventAdapter .cxx_destruct]
+ -[_GCCollectionEventGamepadEventAdapter dealloc]
+ -[_GCCollectionEventGamepadEventAdapter initWithConfiguration:source:]
+ -[_GCCollectionEventGamepadEventAdapter init]
+ -[_GCCollectionEventGamepadEventAdapter observeGamepadEvents:]
+ -[_GCCollectionEventGamepadEventAdapter observers]
+ -[_GCCollectionEventGamepadEventAdapter setObservers:]
+ -[_GCCollectionEventGamepadEventAdapterConfig .cxx_destruct]
+ -[_GCCollectionEventGamepadEventAdapterConfig applyCollectionEvent:toExtendedEvent:]
+ -[_GCCollectionEventGamepadEventAdapterConfig encodeWithCoder:]
+ -[_GCCollectionEventGamepadEventAdapterConfig initWithCoder:]
+ -[_GCCollectionEventGamepadEventAdapterConfig init]
+ -[_GCCollectionEventGamepadEventAdapterConfig mapAxisKey:toPositiveGamepadElement:negativeGamepadElement:]
+ -[_GCCollectionEventGamepadEventAdapterConfig mapKey:toGamepadElement:]
+ -[_GCCollectionEventGamepadEventAdapterDescription .cxx_destruct]
+ -[_GCCollectionEventGamepadEventAdapterDescription encodeWithCoder:]
+ -[_GCCollectionEventGamepadEventAdapterDescription initWithCoder:]
+ -[_GCCollectionEventGamepadEventAdapterDescription initWithConfiguration:source:]
+ -[_GCCollectionEventGamepadEventAdapterDescription init]
+ -[_GCCollectionEventGamepadEventAdapterDescription materializeWithContext:]
+ -[_GCNintendoFusedJoyConHapticDriver endHaptics]
+ OBJC_IVAR_$__GCCollectionEventGamepadEventAdapter._config
+ OBJC_IVAR_$__GCCollectionEventGamepadEventAdapter._observation
+ OBJC_IVAR_$__GCCollectionEventGamepadEventAdapter._observers
+ OBJC_IVAR_$__GCCollectionEventGamepadEventAdapterConfig._axisMappings
+ OBJC_IVAR_$__GCCollectionEventGamepadEventAdapterConfig._buttonMappings
+ OBJC_IVAR_$__GCCollectionEventGamepadEventAdapterDescription._config
+ OBJC_IVAR_$__GCCollectionEventGamepadEventAdapterDescription._materializedObject
+ OBJC_IVAR_$__GCCollectionEventGamepadEventAdapterDescription._sourceDescription
+ _GCFLOC_BUTTON_L5
+ _GCFLOC_BUTTON_R5
+ _GCProductCategorySteam
+ _OBJC_CLASS_$__GCCollectionEventGamepadEventAdapter
+ _OBJC_CLASS_$__GCCollectionEventGamepadEventAdapterConfig
+ _OBJC_CLASS_$__GCCollectionEventGamepadEventAdapterDescription
+ _OBJC_CLASS_$__GCSteam2ControllerProfile
+ _OBJC_METACLASS_$__GCCollectionEventGamepadEventAdapter
+ _OBJC_METACLASS_$__GCCollectionEventGamepadEventAdapterConfig
+ _OBJC_METACLASS_$__GCCollectionEventGamepadEventAdapterDescription
+ _OBJC_METACLASS_$__GCSteam2ControllerProfile
+ __110+[_GCSpatialDeviceProfile logicalDevice:makeControllerPhysicalInputProfileDescriptionWithIdentifier:bindings:]_block_invoke
+ __OBJC_$_CLASS_METHODS__GCCollectionEventGamepadEventAdapterConfig
+ __OBJC_$_CLASS_METHODS__GCCollectionEventGamepadEventAdapterDescription
+ __OBJC_$_CLASS_METHODS__GCSteam2ControllerProfile
+ __OBJC_$_CLASS_PROP_LIST__GCCollectionEventGamepadEventAdapterConfig
+ __OBJC_$_CLASS_PROP_LIST__GCCollectionEventGamepadEventAdapterDescription
+ __OBJC_$_CLASS_PROP_LIST__GCSteam2ControllerProfile
+ __OBJC_$_INSTANCE_METHODS__GCCollectionEventGamepadEventAdapter
+ __OBJC_$_INSTANCE_METHODS__GCCollectionEventGamepadEventAdapterConfig
+ __OBJC_$_INSTANCE_METHODS__GCCollectionEventGamepadEventAdapterDescription
+ __OBJC_$_INSTANCE_VARIABLES__GCCollectionEventGamepadEventAdapter
+ __OBJC_$_INSTANCE_VARIABLES__GCCollectionEventGamepadEventAdapterConfig
+ __OBJC_$_INSTANCE_VARIABLES__GCCollectionEventGamepadEventAdapterDescription
+ __OBJC_$_PROP_LIST__GCCollectionEventGamepadEventAdapter
+ __OBJC_$_PROP_LIST__GCCollectionEventGamepadEventAdapterDescription
+ __OBJC_$_PROP_LIST__GCSteam2ControllerProfile
+ __OBJC_CLASS_PROTOCOLS_$__GCCollectionEventGamepadEventAdapter
+ __OBJC_CLASS_PROTOCOLS_$__GCCollectionEventGamepadEventAdapterConfig
+ __OBJC_CLASS_PROTOCOLS_$__GCCollectionEventGamepadEventAdapterDescription
+ __OBJC_CLASS_PROTOCOLS_$__GCSteam2ControllerProfile
+ __OBJC_CLASS_RO_$__GCCollectionEventGamepadEventAdapter
+ __OBJC_CLASS_RO_$__GCCollectionEventGamepadEventAdapterConfig
+ __OBJC_CLASS_RO_$__GCCollectionEventGamepadEventAdapterDescription
+ __OBJC_CLASS_RO_$__GCSteam2ControllerProfile
+ __OBJC_METACLASS_RO_$__GCCollectionEventGamepadEventAdapter
+ __OBJC_METACLASS_RO_$__GCCollectionEventGamepadEventAdapterConfig
+ __OBJC_METACLASS_RO_$__GCCollectionEventGamepadEventAdapterDescription
+ __OBJC_METACLASS_RO_$__GCSteam2ControllerProfile
+ ___110+[_GCSpatialDeviceProfile logicalDevice:makeControllerPhysicalInputProfileDescriptionWithIdentifier:bindings:]_block_invoke
+ ___43+[_GCSteam2ControllerProfile deviceManager]_block_invoke
+ ___62-[_GCCollectionEventGamepadEventAdapter observeGamepadEvents:]_block_invoke
+ ___70-[_GCCollectionEventGamepadEventAdapter initWithConfiguration:source:]_block_invoke
+ ___84-[_GCCollectionEventGamepadEventAdapterConfig applyCollectionEvent:toExtendedEvent:]_block_invoke
+ ___84-[_GCCollectionEventGamepadEventAdapterConfig applyCollectionEvent:toExtendedEvent:]_block_invoke_2
+ ___block_descriptor_48_e8_32s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8
+ ___block_descriptor_48_e8_32s_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8
+ ___block_descriptor_56_e8_32s40s48r_e41_"_GCHIDEventParser"16?0"NSDictionary"8lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48w_e20_v24?08"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
+ ___os_log_helper_16_0_0
+ ___os_log_helper_16_2_1_8_66
+ ___os_log_helper_16_2_2_8_34_8_0
+ ___os_log_helper_16_2_2_8_66_8_64
+ ___os_log_helper_16_2_3_8_0_8_0_8_32
+ _objc_msgSend$applyCollectionEvent:toExtendedEvent:
+ _objc_msgSend$endHaptics
+ _objc_msgSend$hasValidValueForKey:
+ _objc_msgSend$mapAxisKey:toPositiveGamepadElement:negativeGamepadElement:
+ _objc_msgSend$mapKey:toGamepadElement:
- LoadGameControllerUIFramework
CStrings:
+ "AC Power"
+ "Steam Controller"
+ "TwoHandleHapticCapabilityGraph"
+ "axisMappings"
+ "button.l4"
+ "button.l5"
+ "button.r4"
+ "button.r5"
+ "buttonMappings"
+ "steamcontroller2"
```
