## caraccessoryd

> `/usr/libexec/caraccessoryd`

```diff

-335.1.0.0.0
-  __TEXT.__text: 0x1fd78
-  __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0xb20
-  __TEXT.__const: 0x2e8
-  __TEXT.__cstring: 0xcd3
-  __TEXT.__gcc_except_tab: 0xd8
-  __TEXT.__objc_methname: 0x2e6f
-  __TEXT.__oslogstring: 0x2f1b
-  __TEXT.__objc_classname: 0x2cd
-  __TEXT.__objc_methtype: 0xf7a
+336.1.0.0.0
+  __TEXT.__text: 0x21db4
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__objc_stubs: 0x1f00
+  __TEXT.__objc_methlist: 0xc48
+  __TEXT.__const: 0x2f8
+  __TEXT.__cstring: 0xdb3
+  __TEXT.__gcc_except_tab: 0x120
+  __TEXT.__objc_methname: 0x326d
+  __TEXT.__oslogstring: 0x2f5b
+  __TEXT.__objc_classname: 0x309
+  __TEXT.__objc_methtype: 0x1043
   __TEXT.__swift5_typeref: 0x3aa
   __TEXT.__swift5_capture: 0x128
   __TEXT.__constg_swiftt: 0x378
   __TEXT.__swift5_reflstr: 0x183
   __TEXT.__swift5_fieldmd: 0x1c8
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x628
+  __TEXT.__unwind_info: 0x698
   __TEXT.__eh_frame: 0x138
-  __DATA_CONST.__auth_got: 0x738
-  __DATA_CONST.__got: 0x3a0
+  __DATA_CONST.__auth_got: 0x740
+  __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0xa30
-  __DATA_CONST.__cfstring: 0x240
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__cfstring: 0x380
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x178
+  __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x37f0
-  __DATA.__objc_selrefs: 0xbf0
-  __DATA.__objc_ivar: 0x9c
-  __DATA.__objc_data: 0x818
-  __DATA.__data: 0xdc8
+  __DATA.__objc_const: 0x3ab0
+  __DATA.__objc_selrefs: 0xca0
+  __DATA.__objc_ivar: 0xb8
+  __DATA.__objc_data: 0x868
+  __DATA.__data: 0xe28
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 640
-  Symbols:   1839
-  CStrings:  997
+  Functions: 678
+  Symbols:   1928
+  CStrings:  1061
 
Symbols:
+ -[CAFDCarDataServiceAgent pluginCount]
+ -[CAFDCarDataServiceAgent registrationsForPluginID:]
+ -[CAFDCarDataServiceAgent setStateCaptureManager:]
+ -[CAFDCarDataServiceAgent stateCaptureManager]
+ -[CAFDCarDataServiceAgent valuesForPluginID:iids:]
+ -[CAFDStateCaptureManager .cxx_destruct]
+ -[CAFDStateCaptureManager cachedValuesStateCaptures]
+ -[CAFDStateCaptureManager carConfigDidUpdate]
+ -[CAFDStateCaptureManager carConfigSummary]
+ -[CAFDStateCaptureManager carStateCapture]
+ -[CAFDStateCaptureManager currentCarConfiguration]
+ -[CAFDStateCaptureManager delegate]
+ -[CAFDStateCaptureManager init]
+ -[CAFDStateCaptureManager pluginStateCaptures]
+ -[CAFDStateCaptureManager registrationsStateCapture]
+ -[CAFDStateCaptureManager setCachedValuesStateCaptures:]
+ -[CAFDStateCaptureManager setCarStateCapture:]
+ -[CAFDStateCaptureManager setCurrentCarConfiguration:]
+ -[CAFDStateCaptureManager setDelegate:]
+ -[CAFDStateCaptureManager setPluginStateCaptures:]
+ -[CAFDStateCaptureManager setRegistrationsStateCapture:]
+ -[CAFDStateCaptureManager stateCaptureForPluginID:]
+ -[CAFDStateCaptureManager valueCaptureIIDsFromAccessoryConfig:]
+ -[CarDataClient cachedValueForInstanceID:]
+ GCC_except_table42
+ OBJC_IVAR_$_CAFDCarDataServiceAgent._stateCaptureManager
+ OBJC_IVAR_$_CAFDStateCaptureManager._cachedValuesStateCaptures
+ OBJC_IVAR_$_CAFDStateCaptureManager._carStateCapture
+ OBJC_IVAR_$_CAFDStateCaptureManager._currentCarConfiguration
+ OBJC_IVAR_$_CAFDStateCaptureManager._delegate
+ OBJC_IVAR_$_CAFDStateCaptureManager._pluginStateCaptures
+ OBJC_IVAR_$_CAFDStateCaptureManager._registrationsStateCapture
+ _CAFStateCaptureLogging
+ _OBJC_CLASS_$_CAFAccessoryTypes
+ _OBJC_CLASS_$_CAFCharacteristicTypes
+ _OBJC_CLASS_$_CAFDStateCaptureManager
+ _OBJC_CLASS_$_CAFServiceTypes
+ _OBJC_CLASS_$_CAFStateCapture
+ _OBJC_METACLASS_$_CAFDStateCaptureManager
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.241
+ __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.241.cold.1
+ __81-[CAFDCarDataServiceAgent _removeRegistration:instanceIDs:priority:withResponse:]_block_invoke.251
+ __OBJC_$_INSTANCE_METHODS_CAFDStateCaptureManager
+ __OBJC_$_INSTANCE_VARIABLES_CAFDStateCaptureManager
+ __OBJC_$_PROP_LIST_CAFDStateCaptureManager
+ __OBJC_$_PROP_LIST_CAFDStateCaptureManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFDStateCaptureManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFDStateCaptureManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_CAFDStateCaptureManagerDelegate
+ __OBJC_CLASS_RO_$_CAFDStateCaptureManager
+ __OBJC_LABEL_PROTOCOL_$_CAFDStateCaptureManagerDelegate
+ __OBJC_METACLASS_RO_$_CAFDStateCaptureManager
+ __OBJC_PROTOCOL_$_CAFDStateCaptureManagerDelegate
+ ___31-[CAFDStateCaptureManager init]_block_invoke
+ ___31-[CAFDStateCaptureManager init]_block_invoke_2
+ ___42-[CarDataClient cachedValueForInstanceID:]_block_invoke
+ ___43-[CAFDStateCaptureManager carConfigSummary]_block_invoke
+ ___43-[CAFDStateCaptureManager carConfigSummary]_block_invoke_2
+ ___43-[CAFDStateCaptureManager carConfigSummary]_block_invoke_3
+ ___43-[CAFDStateCaptureManager carConfigSummary]_block_invoke_4
+ ___51-[CAFDStateCaptureManager stateCaptureForPluginID:]_block_invoke
+ ___51-[CAFDStateCaptureManager stateCaptureForPluginID:]_block_invoke_2
+ ___51-[CAFDStateCaptureManager stateCaptureForPluginID:]_block_invoke_3
+ ___63-[CAFDStateCaptureManager valueCaptureIIDsFromAccessoryConfig:]_block_invoke
+ ___63-[CAFDStateCaptureManager valueCaptureIIDsFromAccessoryConfig:]_block_invoke_2
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_40_e8_32s_e15_v32?08Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e39_v32?0"NSNumber"8"NSDictionary"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e5_8?0ls32l8
+ ___block_descriptor_40_e8_32w_e5_8?0lw32l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_8?0ls32l8s40l8s48l8
+ _kCarDataConfigurationTypeKey
+ _objc_msgSend$cachedValueForInstanceID:
+ _objc_msgSend$carConfigDidUpdate
+ _objc_msgSend$carConfigSummary
+ _objc_msgSend$currentCarConfiguration
+ _objc_msgSend$delegate
+ _objc_msgSend$initWithIdentifier:capture:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$pluginStateCaptures
+ _objc_msgSend$setCarStateCapture:
+ _objc_msgSend$setCurrentCarConfiguration:
+ _objc_msgSend$setRegistrationsStateCapture:
+ _objc_msgSend$setStateCaptureManager:
+ _objc_msgSend$stateCaptureForPluginID:
+ _objc_msgSend$stateCaptureManager
+ _objc_msgSend$stateCaptureValues
+ _objc_msgSend$valueCaptureIIDsFromAccessoryConfig:
+ _objc_msgSend$valuesForPluginID:iids:
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.239
- __49-[CAFDCarDataServiceAgent carDataChannelDidOpen:]_block_invoke.239.cold.1
- __81-[CAFDCarDataServiceAgent _removeRegistration:instanceIDs:priority:withResponse:]_block_invoke.250
CStrings:
+ "\x02"
+ "$"
+ "%!s(MISSING) fired, capturing [%!@(MISSING)]"
+ "%!s(MISSING) setting up captures for pluginID %!l(MISSING)u"
+ "-[CAFDStateCaptureManager carConfigDidUpdate]"
+ "8\x13"
+ "@\"<CAFDStateCaptureManagerDelegate>\""
+ "@\"CAFDStateCaptureManager\""
+ "@\"CAFStateCapture\""
+ "@\"NSArray\""
+ "@\"NSDictionary\"24@0:8@\"NSNumber\"16"
+ "@\"NSDictionary\"32@0:8Q16@\"NSArray\"24"
+ "@24@0:8@\"NSNumber\"16"
+ "@32@0:8Q16@24"
+ "@8@?0"
+ "CAFDStateCaptureManager"
+ "CAFDStateCaptureManagerDelegate"
+ "Car"
+ "No Car"
+ "Notification Registrations"
+ "PluginConfig %!@(MISSING).%!@(MISSING)"
+ "PluginValues %!@(MISSING).%!@(MISSING)"
+ "T@\"<CAFDStateCaptureManagerDelegate>\",W,N,V_delegate"
+ "T@\"CAFCarConfiguration\",W,N,V_currentCarConfiguration"
+ "T@\"CAFDStateCaptureManager\",&,N,V_stateCaptureManager"
+ "T@\"CAFStateCapture\",&,N,V_carStateCapture"
+ "T@\"CAFStateCapture\",&,N,V_registrationsStateCapture"
+ "T@\"NSArray\",&,N,V_cachedValuesStateCaptures"
+ "T@\"NSMutableDictionary\",&,N,V_pluginStateCaptures"
+ "TQ,R,N"
+ "Unknown Name"
+ "_cachedValuesStateCaptures"
+ "_carStateCapture"
+ "_currentCarConfiguration"
+ "_delegate"
+ "_pluginStateCaptures"
+ "_registrationsStateCapture"
+ "_stateCaptureManager"
+ "cachedValueForInstanceID:"
+ "cachedValuesStateCaptures"
+ "carConfigDidUpdate"
+ "carConfigSummary"
+ "carStateCapture"
+ "configs"
+ "currentCarConfiguration"
+ "delegate"
+ "initWithIdentifier:capture:"
+ "objectAtIndexedSubscript:"
+ "pluginStateCaptures"
+ "registrationsStateCapture"
+ "setCachedValuesStateCaptures:"
+ "setCarStateCapture:"
+ "setCurrentCarConfiguration:"
+ "setPluginStateCaptures:"
+ "setRegistrationsStateCapture:"
+ "setStateCaptureManager:"
+ "stateCaptureForPluginID:"
+ "stateCaptureManager"
+ "stateCaptureValues"
+ "v32@?0@\"NSNumber\"8@\"NSDictionary\"16^B24"
+ "valueCaptureIIDsFromAccessoryConfig:"
+ "valuesForPluginID:iids:"
- "8\x12"

```
