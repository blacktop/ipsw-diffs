## GameController

> `/System/Library/Frameworks/GameController.framework/Versions/A/GameController`

```diff

-14.0.21.0.0
-  __TEXT.__text: 0x10ca48
+14.0.24.0.0
+  __TEXT.__text: 0x111cd0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xfdcc
+  __TEXT.__objc_methlist: 0xff9c
   __TEXT.__const: 0x240c
-  __TEXT.__gcc_except_tab: 0x368c
-  __TEXT.__cstring: 0xa111
+  __TEXT.__gcc_except_tab: 0x3750
+  __TEXT.__cstring: 0xa1a1
   __TEXT.__oslogstring: 0x8978
   __TEXT.__swift5_typeref: 0x878
   __TEXT.__swift5_reflstr: 0x34f

   __TEXT.__swift5_types: 0xb0
   __TEXT.__swift5_capture: 0x10c
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x4d58
+  __TEXT.__unwind_info: 0x4e00
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd60
-  __DATA_CONST.__objc_classlist: 0x9f8
+  __DATA_CONST.__const: 0xd68
+  __DATA_CONST.__objc_classlist: 0xa18
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x818
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4eb8
+  __DATA_CONST.__objc_selrefs: 0x4ed8
   __DATA_CONST.__objc_protorefs: 0x4d0
-  __DATA_CONST.__objc_superrefs: 0x8f0
+  __DATA_CONST.__objc_superrefs: 0x908
   __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__got: 0xda0
-  __AUTH_CONST.__const: 0x4808
-  __AUTH_CONST.__cfstring: 0xb480
-  __AUTH_CONST.__objc_const: 0x4c5f8
-  __AUTH_CONST.__objc_intobj: 0x1050
+  __DATA_CONST.__got: 0xdb0
+  __AUTH_CONST.__const: 0x48f8
+  __AUTH_CONST.__cfstring: 0xb5c0
+  __AUTH_CONST.__objc_const: 0x4d258
+  __AUTH_CONST.__objc_intobj: 0x1080
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xea8
-  __AUTH.__objc_data: 0x4a18
+  __AUTH.__objc_data: 0x4b58
   __AUTH.__data: 0x5a0
-  __DATA.__objc_ivar: 0x1690
+  __DATA.__objc_ivar: 0x16b0
   __DATA.__data: 0x5f10
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x27e0
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x1db0
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0x228
+  __DATA_DIRTY.__bss: 0x238
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7717
-  Symbols:   16848
-  CStrings:  2453
+  Functions: 7758
+  Symbols:   16949
+  CStrings:  2463
 
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
+ __84-[_GCCollectionEventGamepadEventAdapterConfig applyCollectionEvent:toExtendedEvent:]_block_invoke
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
+ ___block_descriptor_48_e8_32s_e34_v32?0"NSNumber"8"NSArray"16^B24l
+ ___block_descriptor_48_e8_32s_e35_v32?0"NSNumber"8"NSNumber"16^B24l
+ ___block_descriptor_56_e8_32s40s48r_e41_"_GCHIDEventParser"16?0"NSDictionary"8l
+ ___block_descriptor_64_e8_32s40s48w_e20_v24?08"NSError"16l
+ ___block_descriptor_64_e8_32s40s48w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48r
+ ___destroy_helper_block_e8_32s40s48r
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
