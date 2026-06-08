## BrightnessControl

> `/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`

```diff

-2079.120.10.0.0
-  __TEXT.__text: 0xe538
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0xddc
-  __TEXT.__const: 0x3fb0
-  __TEXT.__gcc_except_tab: 0x20c
-  __TEXT.__cstring: 0x12f6
-  __TEXT.__oslogstring: 0xda4
-  __TEXT.__unwind_info: 0x480
-  __TEXT.__objc_classname: 0x1e9
-  __TEXT.__objc_methname: 0x1944
-  __TEXT.__objc_methtype: 0x61b
-  __TEXT.__objc_stubs: 0x1620
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x388
-  __DATA_CONST.__objc_classlist: 0x88
+2285.0.0.502.1
+  __TEXT.__text: 0x17e88
+  __TEXT.__objc_methlist: 0x136c
+  __TEXT.__const: 0x3fda
+  __TEXT.__cstring: 0x1e3e
+  __TEXT.__oslogstring: 0x1aa2
+  __TEXT.__gcc_except_tab: 0x284
+  __TEXT.__swift5_typeref: 0x16
+  __TEXT.__unwind_info: 0x640
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x468
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x778
-  __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0x138
-  __AUTH_CONST.__auth_got: 0x330
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__objc_selrefs: 0x8f0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_arraydata: 0x2e0
+  __DATA_CONST.__got: 0x1d8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x1aa0
-  __AUTH_CONST.__objc_const: 0x20b8
-  __AUTH_CONST.__objc_floatobj: 0x120
+  __AUTH_CONST.__cfstring: 0x2c80
+  __AUTH_CONST.__objc_const: 0x3268
+  __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_floatobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x164
-  __DATA.__data: 0x248
-  __DATA.__bss: 0x28
-  __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x320
+  __AUTH_CONST.__auth_got: 0x4d0
+  __AUTH.__objc_data: 0x2f0
+  __AUTH.__data: 0x30
+  __DATA.__objc_ivar: 0x1e4
+  __DATA.__data: 0x2e0
+  __DATA.__bss: 0x38
+  __DATA_DIRTY.__objc_data: 0x500
+  __DATA_DIRTY.__bss: 0x80
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AFKUser.framework/AFKUser
   - /System/Library/PrivateFrameworks/HID.framework/HID
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B1F5413-A5E3-3E0E-B34B-41439A468D8A
-  Functions: 404
-  Symbols:   1414
-  CStrings:  1045
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  UUID: 72B2FD0E-AF94-394C-A490-06F4DECA85E4
+  Functions: 609
+  Symbols:   2009
+  CStrings:  942
 
Symbols:
+ +[BCAuroraParser parseAuroraCapabilitiesFromProvider:]
+ +[BCAuroraParser parseAuroraCapabilitiesFromProvider:].cold.1
+ +[BCAuroraParser parseAuroraCapabilitiesFromProvider:].cold.2
+ +[BCCPMSParser parseCPMSCapabilitiesFromProvider:andIOMFB:]
+ +[BCCPMSParser parseCPMSCapabilitiesFromProvider:andIOMFB:].cold.1
+ +[BCCPMSParser parseCPMSCapabilitiesFromProvider:andIOMFB:].cold.2
+ +[BCCPMSParser parseCPMSCapabilitiesFromProvider:andIOMFB:].cold.3
+ +[BCCPMSParser parseCPMSCapabilitiesFromProvider:andIOMFB:].cold.4
+ +[BCNativeBrtControl copyAvailableControls]
+ +[BCNativeBrtControl copyAvailableControls].cold.1
+ +[BCNativeBrtControl newMonitorWithHandler:error:]
+ +[BCNativeBrtControl parseAABCapCurve:]
+ +[BCNativeBrtControl parseEDRCapabilities:]
+ +[BCNativeBrtControl parsePanelLimits:toCapabilities:]
+ +[BCRTPLCParser isSupported:]
+ +[BCRTPLCParser parseRTPLCCapabilitiesFromFileForIndex:andProvider:]
+ +[BCRTPLCParser parseRTPLCCapabilitiesFromProvider:]
+ +[CBAPEndpoint endpointForRole:]
+ +[NSArray(PrimitiveArrayConstructible) new2DArrayFromIntegers:xSize:ySize:]
+ +[VMBrtControl copyAvailableControls]
+ +[VMBrtControl copyAvailableControls].cold.1
+ +[VMBrtControl copyAvailableControls].cold.2
+ +[VMBrtControl newMonitorWithHandler:error:]
+ +[VMBrtControl newMonitorWithHandler:error:].cold.1
+ -[BCAppleBacklightBrtControl description]
+ -[BCAppleBacklightBrtControl parseAABCapCurve:]
+ -[BCAppleBacklightBrtControl parseAABCapCurve:].cold.1
+ -[BCAppleBacklightBrtControl parseAABCapCurve:].cold.2
+ -[BCNativeBrtControl ID]
+ -[BCNativeBrtControl copyModuleIdentifier]
+ -[BCNativeBrtControl dealloc]
+ -[BCNativeBrtControl description]
+ -[BCNativeBrtControl initWithService:]
+ -[BCNativeBrtControl initWithService:].cold.1
+ -[BCNativeBrtControl initWithService:].cold.2
+ -[BCNativeBrtControl initWithService:].cold.3
+ -[BCNativeBrtControl maxNits]
+ -[BCNativeBrtControl minNits]
+ -[BCNativeBrtControl parseCapabilities:withDCPEndpoint:andError:]
+ -[BCNativeBrtControl parseCapabilities:withDCPEndpoint:andError:].cold.1
+ -[BCNativeBrtControl parseColorAdaptationCapabilities:]
+ -[BCNativeBrtControl parseDynamicSlider:]
+ -[BCNativeBrtControl parsePAABFromProvider:andIOMFB:]
+ -[BCNativeBrtControl parsePAABFromProvider:andIOMFB:].cold.1
+ -[BCNativeBrtControl parsePAABFromProvider:andIOMFB:].cold.2
+ -[BCNativeBrtControl parsePAABFromProvider:andIOMFB:].cold.3
+ -[BCNativeBrtControl parsePAABFromProvider:andIOMFB:].cold.4
+ -[BCNativeBrtControl parsePAABFromProvider:andIOMFB:].cold.5
+ -[BCNativeBrtControl parsePAABFromProvider:andIOMFB:].cold.6
+ -[BCNativeBrtControl parsePAABFromProvider:andIOMFB:].cold.7
+ -[BCNativeBrtControl parsePAABFromProvider:andIOMFB:].cold.8
+ -[BCNativeBrtControl registryID]
+ -[BCNativeBrtControl setDisplayService:]
+ -[BCNativeBrtControl setDisplayService:].cold.1
+ -[BCNativeBrtControl setNits:error:]
+ -[CBChromaticCorrectionParams aodRampDuration]
+ -[CBChromaticCorrectionParams codingKeys]
+ -[CBChromaticCorrectionParams dealloc]
+ -[CBChromaticCorrectionParams getStrengthForRow:andColumn:]
+ -[CBChromaticCorrectionParams initBezierWithPrefix:fromParser:]
+ -[CBChromaticCorrectionParams initBezierWithPrefix:fromParser:].cold.1
+ -[CBChromaticCorrectionParams initBezierWithPrefix:fromParser:].cold.2
+ -[CBChromaticCorrectionParams initBezierWithPrefix:fromParser:].cold.3
+ -[CBChromaticCorrectionParams initBezierWithPrefix:fromParser:].cold.4
+ -[CBChromaticCorrectionParams initBezierWithPrefix:fromParser:].cold.5
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:]
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.1
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.10
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.11
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.12
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.13
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.14
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.2
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.3
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.4
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.5
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.6
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.7
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.8
+ -[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:].cold.9
+ -[CBChromaticCorrectionParams initFromParserOG:withName:andPrefix:]
+ -[CBChromaticCorrectionParams initFromParserOG:withName:andPrefix:].cold.1
+ -[CBChromaticCorrectionParams initFromParserOG:withName:andPrefix:].cold.2
+ -[CBChromaticCorrectionParams initTablesWithPrefix:fromParser:]
+ -[CBChromaticCorrectionParams initTablesWithPrefix:fromParser:].cold.1
+ -[CBChromaticCorrectionParams initTablesWithPrefix:fromParser:].cold.2
+ -[CBChromaticCorrectionParams initTablesWithPrefix:fromParser:].cold.3
+ -[CBChromaticCorrectionParams initTablesWithPrefix:fromParser:].cold.4
+ -[CBChromaticCorrectionParams initTablesWithPrefix:fromParser:].cold.5
+ -[CBChromaticCorrectionParams initTablesWithPrefix:fromParser:].cold.6
+ -[CBChromaticCorrectionParams initTablesWithPrefix:fromParser:].cold.7
+ -[CBChromaticCorrectionParams initTablesWithPrefix:fromParser:].cold.8
+ -[CBChromaticCorrectionParams initWithProvider:withName:andPrefix:]
+ -[CBChromaticCorrectionParams luxActivationThreshold]
+ -[CBChromaticCorrectionParams luxTable]
+ -[CBChromaticCorrectionParams nitsActivationThreshold]
+ -[CBChromaticCorrectionParams nitsTable]
+ -[CBChromaticCorrectionParams rampBezierAnchors]
+ -[CBChromaticCorrectionParams rampDownDuration]
+ -[CBChromaticCorrectionParams rampDownLuxDeltaThreshold]
+ -[CBChromaticCorrectionParams rampUpDuration]
+ -[CBChromaticCorrectionParams rampUpLuxDeltaThreshold]
+ -[CBChromaticCorrectionParams rampUpdateRate]
+ -[CBChromaticCorrectionParams strengthTable]
+ -[CBChromaticCorrectionParams supported]
+ -[CBCombinedConfigProvider floatArrayFor:]
+ -[CBCombinedConfigProvider floatArrayFor:].cold.1
+ -[CBCombinedConfigProvider iofixedArrayFor:]
+ -[CBCombinedConfigProvider iofixedArrayFor:].cold.1
+ -[CBCombinedConfigProvider loadBool:toDestination:]
+ -[CBCombinedConfigProvider loadString:]
+ -[CBCombinedConfigProvider loadString:].cold.1
+ -[CBCombinedConfigProvider nestedProviderFor:]
+ -[CBCombinedConfigProvider nestedProviderFor:].cold.1
+ -[CBCombinedConfigProvider uintArrayFor:]
+ -[CBCombinedConfigProvider uintArrayFor:].cold.1
+ -[CBDictConfigProvider floatArrayFor:]
+ -[CBDictConfigProvider iofixedArrayFor:]
+ -[CBDictConfigProvider loadBool:toDestination:]
+ -[CBDictConfigProvider loadDictionary:]
+ -[CBDictConfigProvider loadString:]
+ -[CBDictConfigProvider nestedProviderFor:]
+ -[CBDictConfigProvider uintArrayFor:]
+ -[CBGammaContrastPreservationParams luxActivationThreshold]
+ -[CBGammaContrastPreservationParams nitsActivationThreshold]
+ -[CBIORegistryParser floatArrayFor:]
+ -[CBIORegistryParser iofixedArrayFor:]
+ -[CBIORegistryParser loadBool:toDestination:]
+ -[CBIORegistryParser loadString:]
+ -[CBIORegistryParser nestedProviderFor:]
+ -[CBIORegistryParser uintArrayFor:]
+ -[CBNopConfigurationProvider dealloc]
+ -[CBNopConfigurationProvider floatArrayFor:]
+ -[CBNopConfigurationProvider iofixedArrayFor:]
+ -[CBNopConfigurationProvider loadBool:toDestination:]
+ -[CBNopConfigurationProvider loadData:toDestination:]
+ -[CBNopConfigurationProvider loadFixedFloat:toDestination:]
+ -[CBNopConfigurationProvider loadFixedFloat:withScaler:toDestination:]
+ -[CBNopConfigurationProvider loadFloat:toDestination:]
+ -[CBNopConfigurationProvider loadFloatArray:toDestination:]
+ -[CBNopConfigurationProvider loadIOFixedArray:toDestination:]
+ -[CBNopConfigurationProvider loadInt16Array:toDestination:]
+ -[CBNopConfigurationProvider loadInt:toDestination:]
+ -[CBNopConfigurationProvider loadString:]
+ -[CBNopConfigurationProvider loadUint16Array:toDestination:]
+ -[CBNopConfigurationProvider loadUint:toDestination:]
+ -[CBNopConfigurationProvider loadUintArray:toDestination:]
+ -[CBNopConfigurationProvider logHandle]
+ -[CBNopConfigurationProvider nestedProviderFor:]
+ -[CBNopConfigurationProvider setLogHandle:]
+ -[CBNopConfigurationProvider uintArrayFor:]
+ -[NSArray(PrimitiveDataProvider) copyFloatRepresentation]
+ -[VMBrtControl ID]
+ -[VMBrtControl convertArrayValuesUintToFloat:]
+ -[VMBrtControl convertUintToFloat:]
+ -[VMBrtControl copyModuleIdentifier]
+ -[VMBrtControl dealloc]
+ -[VMBrtControl initWithService:]
+ -[VMBrtControl initWithService:].cold.1
+ -[VMBrtControl initWithService:].cold.2
+ -[VMBrtControl initWithService:].cold.3
+ -[VMBrtControl initWithService:].cold.4
+ -[VMBrtControl invalidateForService:]
+ -[VMBrtControl maxNits]
+ -[VMBrtControl minNits]
+ -[VMBrtControl parseAurora:]
+ -[VMBrtControl parseCapabilities:]
+ -[VMBrtControl parseGCP:]
+ -[VMBrtControl registerForTerminationNotifications]
+ -[VMBrtControl registerForTerminationNotifications].cold.1
+ -[VMBrtControl registerForTerminationNotifications].cold.2
+ -[VMBrtControl registryID]
+ -[VMBrtControl setDisplayService:]
+ -[VMBrtControl setNits:error:]
+ GCC_except_table0
+ GCC_except_table15
+ GCC_except_table17
+ GCC_except_table19
+ GCC_except_table23
+ GCC_except_table26
+ GCC_except_table35
+ GCC_except_table62
+ GCC_except_table8
+ _CFBooleanGetTypeID
+ _CFEqual
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _CFPreferencesCopyMultiple
+ _GetCFBooleanValue
+ _IORegistryEntryFromPath
+ _IORegistryEntryGetChildIterator
+ _IORegistryEntryGetName
+ _IOServiceNameMatching
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_BCAABConstraintsParser
+ _OBJC_CLASS_$_BCAuroraParser
+ _OBJC_CLASS_$_BCCPMSParser
+ _OBJC_CLASS_$_BCNativeBrtControl
+ _OBJC_CLASS_$_BCRTPLCParser
+ _OBJC_CLASS_$_CBChromaticCorrectionParams
+ _OBJC_CLASS_$_CBNopConfigurationProvider
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_VMBrtControl
+ _OBJC_IVAR_$_BCAppleBacklightBrtControl.provider
+ _OBJC_IVAR_$_BCNativeBrtControl._backlightService
+ _OBJC_IVAR_$_BCNativeBrtControl._dcpRole
+ _OBJC_IVAR_$_BCNativeBrtControl._iomfbProvider
+ _OBJC_IVAR_$_BCNativeBrtControl._provider
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._aodRampDuration
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._codingKeys
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._log
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._luxActivationThreshold
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._luxTable
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._luxTableOG
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._luxTableSizeOG
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._nitsActivationThreshold
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._nitsTable
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._nitsTableOG
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._nitsTableSizeOG
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._rampBezierAnchors
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._rampBezierAnchorsOG
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._rampDownDuration
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._rampDownLuxDeltaThreshold
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._rampUpDuration
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._rampUpLuxDeltaThreshold
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._rampUpdateRate
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._rampUpdateRateOG
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._strengthTable
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._strengthTableOG
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._strengthTableSizeOG
+ _OBJC_IVAR_$_CBChromaticCorrectionParams._supported
+ _OBJC_IVAR_$_CBCombinedConfigProvider.logHandle
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._luxActivationThreshold
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._nitsActivationThreshold
+ _OBJC_IVAR_$_CBNopConfigurationProvider._logHandle
+ _OBJC_IVAR_$_VMBrtControl._paravirtDisplayService
+ _OBJC_IVAR_$_VMBrtControl._terminationCallback
+ _OBJC_IVAR_$_VMBrtControl._terminationIterator
+ _OBJC_IVAR_$_VMBrtControl._terminationPort
+ _OBJC_METACLASS_$_BCAABConstraintsParser
+ _OBJC_METACLASS_$_BCAuroraParser
+ _OBJC_METACLASS_$_BCCPMSParser
+ _OBJC_METACLASS_$_BCNativeBrtControl
+ _OBJC_METACLASS_$_BCRTPLCParser
+ _OBJC_METACLASS_$_CBChromaticCorrectionParams
+ _OBJC_METACLASS_$_CBNopConfigurationProvider
+ _OBJC_METACLASS_$_VMBrtControl
+ __CLASS_METHODS_BCAABConstraintsParser
+ __DATA_BCAABConstraintsParser
+ __INSTANCE_METHODS_BCAABConstraintsParser
+ __IOFixedToFloat
+ __IVARS_BCAABConstraintsParser
+ __METACLASS_DATA_BCAABConstraintsParser
+ __OBJC_$_CLASS_METHODS_BCAuroraParser
+ __OBJC_$_CLASS_METHODS_BCCPMSParser
+ __OBJC_$_CLASS_METHODS_BCNativeBrtControl
+ __OBJC_$_CLASS_METHODS_BCRTPLCParser
+ __OBJC_$_CLASS_METHODS_CBAPEndpoint
+ __OBJC_$_CLASS_METHODS_VMBrtControl
+ __OBJC_$_INSTANCE_METHODS_BCNativeBrtControl
+ __OBJC_$_INSTANCE_METHODS_CBChromaticCorrectionParams
+ __OBJC_$_INSTANCE_METHODS_CBNopConfigurationProvider
+ __OBJC_$_INSTANCE_METHODS_NSArray(PrimitiveArrayConstructible|PrimitiveDataProvider)
+ __OBJC_$_INSTANCE_METHODS_VMBrtControl
+ __OBJC_$_INSTANCE_VARIABLES_BCNativeBrtControl
+ __OBJC_$_INSTANCE_VARIABLES_CBChromaticCorrectionParams
+ __OBJC_$_INSTANCE_VARIABLES_CBNopConfigurationProvider
+ __OBJC_$_INSTANCE_VARIABLES_VMBrtControl
+ __OBJC_$_PROP_LIST_BCParserPlugin
+ __OBJC_$_PROP_LIST_CBChromaticCorrectionParams
+ __OBJC_$_PROP_LIST_CBNopConfigurationProvider
+ __OBJC_$_PROTOCOL_CLASS_METHODS_BCParserPlugin
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BCParserPlugin
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CBPrimitiveConfigurationProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BCParserPlugin
+ __OBJC_$_PROTOCOL_REFS_BCParserPlugin
+ __OBJC_CLASS_PROTOCOLS_$_CBChromaticCorrectionParams
+ __OBJC_CLASS_PROTOCOLS_$_CBNopConfigurationProvider
+ __OBJC_CLASS_RO_$_BCAuroraParser
+ __OBJC_CLASS_RO_$_BCCPMSParser
+ __OBJC_CLASS_RO_$_BCNativeBrtControl
+ __OBJC_CLASS_RO_$_BCRTPLCParser
+ __OBJC_CLASS_RO_$_CBChromaticCorrectionParams
+ __OBJC_CLASS_RO_$_CBNopConfigurationProvider
+ __OBJC_CLASS_RO_$_VMBrtControl
+ __OBJC_LABEL_PROTOCOL_$_BCParserPlugin
+ __OBJC_METACLASS_RO_$_BCAuroraParser
+ __OBJC_METACLASS_RO_$_BCCPMSParser
+ __OBJC_METACLASS_RO_$_BCNativeBrtControl
+ __OBJC_METACLASS_RO_$_BCRTPLCParser
+ __OBJC_METACLASS_RO_$_CBChromaticCorrectionParams
+ __OBJC_METACLASS_RO_$_CBNopConfigurationProvider
+ __OBJC_METACLASS_RO_$_VMBrtControl
+ __OBJC_PROTOCOL_$_BCParserPlugin
+ __OBJC_PROTOCOL_REFERENCE_$_CBPrimitiveConfigurationProvider
+ __PROPERTIES_BCAABConstraintsParser
+ __PROTOCOLS_BCAABConstraintsParser
+ __PROTOCOLS_BCAABConstraintsParser.2
+ __Z16load_from_readerIbEbP18CBIORegistryReaderP8NSStringPT_
+ __ZN14CoreBrightness21get_value_from_cfdataIbEEbPKvPT_
+ __ZN14CoreBrightness21get_value_from_cfdataIfEEbPKvPT_
+ __ZN14CoreBrightness21get_value_from_cfdataIiEEbPKvPT_
+ __ZN14CoreBrightness21get_value_from_cfdataIjEEbPKvPT_
+ __ZN14CoreBrightness24create_array_from_cfdataIfEEmPKvPPT_
+ __ZN14CoreBrightness24create_array_from_cfdataIiEEmPKvPPT_
+ __ZN14CoreBrightness24create_array_from_cfdataIjEEmPKvPPT_
+ __ZN14CoreBrightness24create_array_from_cfdataIsEEmPKvPPT_
+ __ZN14CoreBrightness24create_array_from_cfdataItEEmPKvPPT_
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIP21_InterestBlockWrapperEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIjEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__16vectorIP21_InterestBlockWrapperNS_9allocatorIS2_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIP21_InterestBlockWrapperNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE24__emplace_back_slow_pathIJRKjEEEPjDpOT_
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ __ZTISt12length_error
+ __ZTISt20bad_array_new_length
+ __ZTVSt12length_error
+ __ZZ24mach_time_to_nanosecondsE8timeBase
+ __ZZL11target_typevE6target
+ __ZdlPv
+ __ZnwmSt19__type_descriptor_t
+ ___37-[VMBrtControl invalidateForService:]_block_invoke
+ ___44+[VMBrtControl newMonitorWithHandler:error:]_block_invoke
+ ___44+[VMBrtControl newMonitorWithHandler:error:]_block_invoke.11
+ ___44+[VMBrtControl newMonitorWithHandler:error:]_block_invoke.16
+ ___44+[VMBrtControl newMonitorWithHandler:error:]_block_invoke.6
+ ___44+[VMBrtControl newMonitorWithHandler:error:]_block_invoke_2
+ ___44+[VMBrtControl newMonitorWithHandler:error:]_block_invoke_2.12
+ ___50+[BCNativeBrtControl newMonitorWithHandler:error:]_block_invoke
+ ___51-[VMBrtControl registerForTerminationNotifications]_block_invoke
+ ___51-[VMBrtControl registerForTerminationNotifications]_block_invoke.42
+ ___58+[BCAppleBacklightBrtControl newMonitorWithHandler:error:]_block_invoke.20
+ ___58+[BCAppleBacklightBrtControl newMonitorWithHandler:error:]_block_invoke.24
+ ___Block_byref_object_copy_.1
+ ___Block_byref_object_copy_.4
+ ___Block_byref_object_dispose_.2
+ ___Block_byref_object_dispose_.5
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_44_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32b40r_e15_v24?0I8I12^v16lr40l8s32l8
+ ___block_descriptor_72_e8_32b40r48r56r_e8_v12?0I8lr40l8s32l8r48l8r56l8
+ ___block_descriptor_92_e8_32o40b48r56r64r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_92_e8_32o40b48r56r64r_e5_v8?0ls40l8r48l8r56l8r64l8s32l8
+ ___cxa_allocate_exception
+ ___cxa_free_exception
+ ___cxa_throw
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_reflection_version
+ __freeInterestBlockWrapper
+ __iokitInterestCallback
+ __newInterestBlockWrapper
+ __newInterestBlockWrapper.cold.1
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_BrightnessControl
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_BrightnessControl
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_BrightnessControl
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_BrightnessControl
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_BrightnessControl
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_BrightnessControl
+ _clock_gettime_nsec_np
+ _dispatch_assert_queue$V2
+ _kBCConfigSliderMapping
+ _kBCDCPExpertService
+ _kBCErrorDomain
+ _kCFBooleanTrue
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _mach_error_string
+ _mach_time_to_microseconds
+ _objc_allocWithZone
+ _objc_autoreleaseReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeak
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$array
+ _objc_msgSend$boolValue
+ _objc_msgSend$capabilitiesKey
+ _objc_msgSend$capitalizedString
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$convertArrayValuesUintToFloat:
+ _objc_msgSend$convertUintToFloat:
+ _objc_msgSend$dataWithContentsOfFile:
+ _objc_msgSend$endpointForRole:
+ _objc_msgSend$floatArrayFor:
+ _objc_msgSend$getStrengthForRow:andColumn:
+ _objc_msgSend$initBezierWithPrefix:fromParser:
+ _objc_msgSend$initCommonWithPrefix:fromParser:
+ _objc_msgSend$initFromParserOG:withName:andPrefix:
+ _objc_msgSend$initTablesWithPrefix:fromParser:
+ _objc_msgSend$initWithProvider:withName:andPrefix:
+ _objc_msgSend$invalidateForService:
+ _objc_msgSend$iofixedArrayFor:
+ _objc_msgSend$isSupported:
+ _objc_msgSend$loadBool:toDestination:
+ _objc_msgSend$loadString:
+ _objc_msgSend$nestedProviderFor:
+ _objc_msgSend$newArrayFromFloats:size:
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$parseAABCapCurve:
+ _objc_msgSend$parseAurora:
+ _objc_msgSend$parseAuroraCapabilitiesFromProvider:
+ _objc_msgSend$parseCPMSCapabilitiesFromProvider:andIOMFB:
+ _objc_msgSend$parseCapabilities:
+ _objc_msgSend$parseCapabilities:withDCPEndpoint:andError:
+ _objc_msgSend$parseColorAdaptationCapabilities:
+ _objc_msgSend$parseDynamicSlider:
+ _objc_msgSend$parseEDRCapabilities:
+ _objc_msgSend$parseFrom:iomfb:
+ _objc_msgSend$parseGCP:
+ _objc_msgSend$parsePAABFromProvider:andIOMFB:
+ _objc_msgSend$parsePanelLimits:toCapabilities:
+ _objc_msgSend$parseRTPLCCapabilitiesFromFileForIndex:andProvider:
+ _objc_msgSend$parseRTPLCCapabilitiesFromProvider:
+ _objc_msgSend$plugin
+ _objc_msgSend$registerForTerminationNotifications
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$supported
+ _objc_msgSend$uintArrayFor:
+ _objc_msgSend$unsignedLongValue
+ _objc_opt_new
+ _objc_opt_self
+ _objc_release_x1
+ _objc_release_x25
+ _objc_release_x26
+ _objc_retain_x23
+ _objc_retain_x26
+ _parseBrightDotMitigationParams
+ _parseChromaticCorrectionParams
+ _sanitize_brightness
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_x20
+ _swift_release_x21
+ _swift_retain_x20
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _symbolic _____ySSSo8NSNumberCG s18_DictionaryStorageC
- -[BCAppleBacklightBrtControl parseAuroraCapabilities]
- -[BCAppleBacklightBrtControl parseAuroraCapabilities].cold.1
- -[BCAppleBacklightBrtControl parseAuroraCapabilities].cold.2
- -[BCAppleBacklightBrtControl parseCPMSParams]
- -[BCAppleBacklightBrtControl parseChromicCorrectionParams]
- -[CBBootArgsConfigProvider loadData:toDestination:]
- -[CBBootArgsConfigProvider loadFloatArray:toDestination:]
- -[CBBootArgsConfigProvider loadIOFixedArray:toDestination:]
- -[CBBootArgsConfigProvider loadInt16Array:toDestination:]
- -[CBBootArgsConfigProvider loadUint16Array:toDestination:]
- -[CBBootArgsConfigProvider loadUintArray:toDestination:]
- -[CBBootArgsConfigProvider logHandle]
- -[CBBootArgsConfigProvider setLogHandle:]
- -[CBDictConfigProvider loadData:toDestination:]
- -[CBDictConfigProvider loadIOFixedArray:toDestination:]
- -[CBDictConfigProvider loadInt16Array:toDestination:]
- -[CBDictConfigProvider loadUint16Array:toDestination:]
- -[CBDictConfigProvider loadUintArray:toDestination:]
- -[CBDictConfigProvider logHandle]
- -[CBDictConfigProvider setLogHandle:]
- -[CBIORegistryParser logHandle]
- -[CBIORegistryParser setLogHandle:]
- GCC_except_table14
- GCC_except_table16
- GCC_except_table18
- GCC_except_table22
- GCC_except_table25
- GCC_except_table40
- GCC_except_table6
- _OBJC_IVAR_$_CBBootArgsConfigProvider._logHandle
- _OBJC_IVAR_$_CBCombinedConfigProvider._logHandle
- _OBJC_IVAR_$_CBDictConfigProvider._logHandle
- _OBJC_IVAR_$_CBIORegistryParser._logHandle
- __OBJC_CLASS_PROTOCOLS_$_CBBootArgsConfigProvider
- __OBJC_CLASS_PROTOCOLS_$_CBDictConfigProvider
- __OBJC_CLASS_PROTOCOLS_$_CBIORegistryParser
- __Z21get_value_from_cfdataIfEbPKvPT_
- __Z21get_value_from_cfdataIiEbPKvPT_
- __Z21get_value_from_cfdataIjEbPKvPT_
- __Z24create_array_from_cfdataIfEmPKvPPT_
- __Z24create_array_from_cfdataIiEmPKvPPT_
- __Z24create_array_from_cfdataIjEmPKvPPT_
- __Z24create_array_from_cfdataIsEmPKvPPT_
- __Z24create_array_from_cfdataItEmPKvPPT_
- __Z25mach_time_to_microsecondsy
- __Z25mach_time_to_microsecondsy.cold.1
- __ZZ24mach_time_to_nanosecondsE18machTimeBaseFactor
- ___58+[BCAppleBacklightBrtControl newMonitorWithHandler:error:]_block_invoke.2
- ___58+[BCAppleBacklightBrtControl newMonitorWithHandler:error:]_block_invoke.6
- ___block_descriptor_32_e22_v16?0"BCBrtControl"8l
- ___block_descriptor_40_e8_32b_e22_v16?0"BCBrtControl"8ls32l8
- ___main_block_invoke
- ___main_block_invoke_2
- ___main_block_invoke_2.cold.1
- _displays
- _mach_absolute_time
- _mach_time_now_in_microseconds.cold.1
- _mach_time_now_in_milliseconds.cold.1
- _mach_time_now_in_nanoseconds.cold.1
- _mach_time_now_in_seconds.cold.1
- _mach_time_to_milliseconds.cold.1
- _mach_time_to_seconds.cold.1
- _main
- _objc_msgSend$dictionaryRepresentation
- _objc_msgSend$parseAuroraCapabilities
- _objc_msgSend$parseCPMSParams
- _objc_msgSend$parseChromicCorrectionParams
- _objc_msgSend$removeObjectForKey:
- _objc_msgSend$stringWithUTF8String:
- _objc_retain_x24
- _setBrightnessOnAllDisplays
CStrings:
+ " "
+ " %f%s"
+ " %f%s "
+ "%@ is not supported"
+ "%@-lux-activation-threshold"
+ "%@-lux-table"
+ "%@-nits-activation-threshold"
+ "%@-nits-table"
+ "%@-ramp-aod-duration"
+ "%@-ramp-bezier-anchors"
+ "%@-ramp-down-duration"
+ "%@-ramp-down-lux-threshold"
+ "%@-ramp-up-duration"
+ "%@-ramp-up-lux-threshold"
+ "%@-ramp-update-rate"
+ "%@-strength-table"
+ "%@-supported"
+ ","
+ "-[BCNativeBrtControl parseCapabilities:withDCPEndpoint:andError:]"
+ "/System/Library/Display/%@/%d-rtplc.bin"
+ "AABConstraints"
+ "AABCurveCap"
+ "AOD ramp duration is negative"
+ "APL Array has wrong size: %lu (expected %d)"
+ "AppleParavirtDisplay"
+ "AuroraMinNits"
+ "BCAppleBacklightBrtControl(BuiltIn: %@)"
+ "BCAppleBacklightBrtControl(DCP: \"%@\", BuiltIn: %@)"
+ "BCAppleBacklightBrtControl(DFR)"
+ "BCNativeBrtControl(DCP: \"%@\")"
+ "BCNativeBrtControl.mm"
+ "BCNativeBrtControl: Could not init for service %u"
+ "BCNativeBrtControl: got back service %u (%@)"
+ "BDM"
+ "B_input"
+ "B_min"
+ "CBAmmolite"
+ "CBTwilight"
+ "CPMSAPLTarget"
+ "Cancelling BCNativeBrtMonitor..."
+ "Cannot determine the associated DCP role"
+ "Cannot get ParavirtBrightnessCaps"
+ "Cannot load color accuracy index. Did the property name changed?"
+ "Cannot obtain luminance-ratio"
+ "Cannot obtain vbatt-current"
+ "CapabilitiesVersion"
+ "Default"
+ "DefaultWPType"
+ "DisplayContainerID"
+ "DisplayID"
+ "DynamicSlider"
+ "E"
+ "Error: failed to create port for display notifications"
+ "Failed to get child iterator err = %#x (%s)"
+ "Failed to get registry ID"
+ "Failed to init DCP endpoint for role %@"
+ "Failed to read brightness capabilities"
+ "Failed to read brightness capabilities: %@"
+ "First ramp Bezier anchor is out of valid [0, 1] range"
+ "IODeviceTree"
+ "IODeviceTree:/core-brightness"
+ "IOMFB gave us NULL service"
+ "I_input"
+ "I_nominal"
+ "I_threshold"
+ "Incorrect number of ramp Bezier anchors"
+ "Invalid Type"
+ "IsVirtualDevice"
+ "L"
+ "LmidProduct"
+ "LminProduct"
+ "Loading RTPLC from file"
+ "Loading RTPLC from file. color-accuracy-index: %d"
+ "Loading RTPLC from ioreg"
+ "Lux activation threshold is negative"
+ "Lux table has less than one element"
+ "Lux table is not monotonically increasing"
+ "LuxActivationThreshold=%f"
+ "LuxTable={%s}"
+ "LuxTableSize=%lu"
+ "MidNits"
+ "Mismatched lengths of AAB cap curve arrays (e.count = %lu, l.count = %lu)"
+ "NitArray has invalid size: %lu (expected %d)"
+ "Nits activation threshold is negative"
+ "Nits table has less than one element"
+ "Nits table is not monotonically increasing"
+ "NitsActivationThreshold=%f"
+ "NitsTable={%s}"
+ "NitsTableSize=%lu"
+ "Not loading CPMS config because use-cpms-lut=%d"
+ "ParavirtBrightnessCaps"
+ "Parsed AAB cap curve: (e: %@, l: %@)"
+ "Parser is null"
+ "PowerAwareAAB"
+ "ProductID"
+ "RTPLC"
+ "RTPLCAPCETable"
+ "RTPLCNitsTable"
+ "Ramp down duration is negative"
+ "Ramp down lux delta threshold is negative"
+ "Ramp up duration is negative"
+ "Ramp up lux delta threshold is negative"
+ "RampAODDuration=%f"
+ "RampBezierAnchors={ %f, %f, %f }"
+ "RampDownDuration=%f"
+ "RampDownLuxDeltaThreshold=%f"
+ "RampUpDuration=%f"
+ "RampUpLuxDeltaThreshold=%f"
+ "RampUpdateRate=%f"
+ "Received IOMFB service %d"
+ "Returned calibration dictionary is of invalid type"
+ "Second ramp Bezier anchor is out of valid [0, 1] range"
+ "Slope"
+ "Strength table element #%lu with value %f is out of the valid [0, 1] range"
+ "Strength table has wrong size %lu for lux table size %lu and nits table size %lu"
+ "StrengthTableSize=%lu"
+ "StrengthTable[%lu]={%s}"
+ "Successfully created DCP endpoint for role %@"
+ "Successfully loaded display-id: %u for role %@"
+ "Third ramp Bezier anchor is out of valid [0, 1] range"
+ "Unable to copy the backlight calibration from the DCP"
+ "Unable to find AppleParavirtDisplay service."
+ "Unable to load AOD ramp duration"
+ "Unable to load lux activation threshold"
+ "Unable to load lux table"
+ "Unable to load nits activation threshold"
+ "Unable to load nits table"
+ "Unable to load ramp Bezier anchors"
+ "Unable to load ramp down duration"
+ "Unable to load ramp down lux delta threshold"
+ "Unable to load ramp up duration"
+ "Unable to load ramp up lux delta threshold"
+ "Unable to load ramp update rate"
+ "Unable to load strength table"
+ "Unable to register for property change notification (error = %d)"
+ "VMBrtControl: Could not init for service %u"
+ "VMBrtControl: changed capabilities for service %u (%@)"
+ "VMBrtControl: cleaning up monitor"
+ "VMBrtControl: failed to find matching AppleParavirtDisplay services"
+ "VMBrtControl: failed to get iterator err = %#x (%s)"
+ "VMBrtControl: got back service %u (%@)"
+ "Virtualization"
+ "WattNitsConversion table has wrong size: %lu (expected %d)"
+ "[GS] Index array size != Bmin array size (%zu != %zu)"
+ "[GS] Index array size != Ithr array size (%zu != %zu)"
+ "[GS] Index array size != nominal current array (%zu != %zu)"
+ "[GS] Index array size != slope array size (%zu != %zu)"
+ "[GS] PAB index array not found"
+ "_newInterestBlockWrapper"
+ "aab-cap-e"
+ "aab-cap-l"
+ "aab-constraint-e0b"
+ "aab-constraint-e2"
+ "aab-constraint-emax"
+ "aab-constraint-emax-threshold"
+ "aab-constraint-l0b"
+ "aab-constraint-l2"
+ "aab-constraint-lmax"
+ "aml"
+ "ammolite"
+ "aurora-supported"
+ "backlight-calibration-parameters"
+ "bdm-lux1"
+ "bdm-lux2"
+ "bdm-nits1"
+ "bdm-nits2"
+ "bdm-supported"
+ "color-accuracy-index"
+ "com.apple.BCBrtControl.Native"
+ "com.apple.BCBrtControl.VirtualMachine"
+ "com.apple.VMBrtControl.global"
+ "cpms-apl-column"
+ "dcpexpert-service"
+ "default-whitepoint-type"
+ "display-id"
+ "ds-max-factor-aab-off"
+ "ds-max-factors"
+ "ds-max-fall-time"
+ "ds-max-pivot"
+ "ds-max-rise-time"
+ "ds-max-rise-time-fast"
+ "ds-max-rise-time-fast-thr"
+ "ds-max-thresholds"
+ "ds-min-factors"
+ "ds-min-fall-time"
+ "ds-min-pivot"
+ "ds-min-rise-time"
+ "ds-min-thresholds"
+ "edm-supported"
+ "edr-aurora-seconds-per-stop"
+ "edr-exit-seconds-per-stop"
+ "edr-potential-headroom"
+ "edr-reference-headroom"
+ "edr-seconds-per-stop"
+ "edr-seconds-per-stop-rapid"
+ "error != nil"
+ "gcp-supported"
+ "gs-b-min"
+ "gs-i-nominal"
+ "gs-i-threshold"
+ "gs-pab-index"
+ "gs-slope"
+ "hw.targettype"
+ "lMaxPanel"
+ "lMaxProduct"
+ "lMaxReachable"
+ "lMidPanel"
+ "lMidProduct"
+ "lMinPanel"
+ "lMinProduct"
+ "lMinReachable"
+ "luminance-ratio"
+ "luxTable"
+ "max_factor_aab_off"
+ "max_factors"
+ "max_fall_time"
+ "max_rise_time"
+ "max_rise_time_fast"
+ "max_rise_time_fast_threshold"
+ "max_thresholds"
+ "milliAmps2NitsScaleFactor"
+ "min_factors"
+ "min_fall_time"
+ "min_rise_time"
+ "min_thresholds"
+ "multi_point"
+ "nitsTable"
+ "pab_scaler_index"
+ "pivoting_L"
+ "pivoting_L_max"
+ "plt-logic-version"
+ "power-lut-data-x not found"
+ "power-lut-data-y not found"
+ "power-lut-use-iofixed"
+ "pre-strobe-nit"
+ "rampBezierAnchors"
+ "ring-light-supported"
+ "rtplc-apce-table"
+ "rtplc-apce-table-ref"
+ "rtplc-nits-table"
+ "rtplc-nits-table-ref"
+ "rtplc-supported"
+ "slider-mapping"
+ "strengthTable"
+ "supports-%@"
+ "supports-edm"
+ "supports-rtplc"
+ "tw"
+ "twilight"
+ "use-cabal"
+ "use-lut"
+ "utilites.mm"
+ "v24@?0I8I12^v16"
+ "vbatt-current"
+ "vector"
- "#16@0:8"
- "@\"<CBIORegInterface>\""
- "@\"AFKEndpointInterface\""
- "@\"CBAPEndpoint\""
- "@\"HIDDevice\""
- "@\"HIDElement\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSObject<OS_os_log>\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@16@0:8"
- "@20@0:8I16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSString\"16"
- "@24@0:8@16"
- "@24@0:8I16I20"
- "@24@0:8Q16"
- "@24@0:8r*16"
- "@28@0:8I16[128c]20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8@?16^@24"
- "@32@0:8I16[128c]20I28"
- "@32@0:8^d16Q24"
- "@32@0:8^f16Q24"
- "@32@0:8^i16Q24"
- "@40@0:8:16@24@32"
- "@40@0:8^f16Q24Q32"
- "@?"
- "@?16@0:8"
- "APToDCPEndpoint"
- "Aurora not supported, skipping Aurora capabilities"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B24@0:8^d16"
- "B24@0:8d16"
- "B32@0:8@\"NSString\"16^I24"
- "B32@0:8@\"NSString\"16^f24"
- "B32@0:8@\"NSString\"16^i24"
- "B32@0:8@\"NSString\"16r^^{__CFData}24"
- "B32@0:8@16@24"
- "B32@0:8@16^I24"
- "B32@0:8@16^f24"
- "B32@0:8@16^i24"
- "B32@0:8@16r^^{__CFData}24"
- "B32@0:8d16^@24"
- "B36@0:8@\"NSString\"16f24^f28"
- "B36@0:8@16f24^f28"
- "B36@0:8i16r^v20Q28"
- "B40@0:8@16@24^@32"
- "B48@0:8i16r^v20Q28^@36I44"
- "BCAppleBacklightBrtControl"
- "BCBrtControl"
- "BCBrtMonitor"
- "BCDisplayList"
- "BCError"
- "BCHIDBrtControl"
- "BCVirtualBrtControl"
- "CBAPEndpoint"
- "CBBootArgsConfigProvider"
- "CBChromaticCorectionParamsProtocol"
- "CBCombinedConfigProvider"
- "CBDictConfigProvider"
- "CBDictSerializer"
- "CBFloatArray"
- "CBFloatArray2D"
- "CBGammaContrastPreservationParams"
- "CBIORegInterface"
- "CBIORegistryParser"
- "CBIORegistryReader"
- "CBPrimitiveConfigurationProvider"
- "CBSerializable"
- "CBUserDefaultsProvider"
- "I"
- "I16@0:8"
- "I32@0:8@16@24"
- "ID"
- "NSObject"
- "PreStrobeDimPeriod"
- "PrimitiveArrayConstructible"
- "Q"
- "Q16@0:8"
- "Q32@0:8@\"NSString\"16^^I24"
- "Q32@0:8@\"NSString\"16^^S24"
- "Q32@0:8@\"NSString\"16^^f24"
- "Q32@0:8@\"NSString\"16^^s24"
- "Q32@0:8@16^^I24"
- "Q32@0:8@16^^S24"
- "Q32@0:8@16^^f24"
- "Q32@0:8@16^^s24"
- "T#,R"
- "T@\"<CBIORegInterface>\",R,V_reader"
- "T@\"NSArray\",R,V_providers"
- "T@\"NSDictionary\",R"
- "T@\"NSDictionary\",R,V_capabilities"
- "T@\"NSDictionary\",R,V_codingKeys"
- "T@\"NSDictionary\",R,V_dict"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_callbackQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R"
- "T@\"NSObject<OS_os_log>\",&"
- "T@\"NSObject<OS_os_log>\",&,V_logHandle"
- "T@\"NSObject<OS_os_log>\",R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,V_bootargs"
- "T@\"NSUUID\",R,V_containerID"
- "T@,R,C"
- "T@?,C,V_displayInvalidHandler"
- "TB,R,V_isValid"
- "TB,V_multipleControlEnabled"
- "TI,R,V_service"
- "TI,R,V_supported"
- "TQ,R"
- "TQ,R,V_registryID"
- "T^{__CFUUID=},R"
- "Td,R,V_maxNits"
- "Td,R,V_minNits"
- "Tf,R"
- "Tf,R,V_ASb"
- "Tf,R,V_Bmax"
- "Tf,R,V_Bmin"
- "Tf,R,V_Kb"
- "Tf,R,V_Kl"
- "Tf,R,V_Lmax"
- "Tf,R,V_Lmin"
- "Tf,R,V_ambientFactor"
- "Tf,R,V_aodRampDuration"
- "Tf,R,V_gammaMax"
- "Tf,R,V_gammaMin"
- "Tf,R,V_gcpFactorHigh"
- "Tf,R,V_gcpFactorLow"
- "Tf,R,V_rampDownDuration"
- "Tf,R,V_rampDownLuxDeltaThreshold"
- "Tf,R,V_rampUpDuration"
- "Tf,R,V_rampUpLuxDeltaThreshold"
- "Tf,R,V_rampUpdateRate"
- "Tf,R,V_referenceLux"
- "Tf,R,V_referenceWhiteBrightness"
- "Ti,R"
- "UTF8String"
- "UUIDString"
- "Vv16@0:8"
- "[128c]"
- "[originalDisp isEqual: disp]"
- "^f"
- "^f16@0:8"
- "^{?=@?}"
- "^{IONotificationPort=}"
- "^{_NSZone=}16@0:8"
- "^{__CFUUID=}"
- "^{__CFUUID=}16@0:8"
- "_ASb"
- "_Bmax"
- "_Bmin"
- "_Kb"
- "_Kl"
- "_Lmax"
- "_Lmin"
- "_ambientFactor"
- "_aodRampDuration"
- "_backlightService"
- "_boostFactorNotification"
- "_boostFactorNotificationPort"
- "_bootargs"
- "_brighntessUpdateCounter"
- "_brightnessElement"
- "_brightnessFadeElement"
- "_brightnessUpdateQueue"
- "_brightnessUpdateTarget"
- "_callbackQueue"
- "_cancel"
- "_capabilities"
- "_cfContainerID"
- "_checkIsValid:"
- "_codingKeys"
- "_cols"
- "_containerID"
- "_count"
- "_data"
- "_desc"
- "_dict"
- "_dispService"
- "_displayInvalidHandler"
- "_displayService"
- "_endpoint"
- "_energySaving"
- "_epQueue"
- "_gammaMax"
- "_gammaMin"
- "_gcpFactorHigh"
- "_gcpFactorLow"
- "_getDeviceNits:"
- "_hidBrightnessDevice"
- "_hidBrightnessService"
- "_id"
- "_isDCP"
- "_isDFR"
- "_isValid"
- "_logHandle"
- "_maxMilliAmps"
- "_maxNits"
- "_maxNitsEDR"
- "_maxUser"
- "_midNits"
- "_minMilliAmps"
- "_minNits"
- "_minUser"
- "_multipleControlEnabled"
- "_nits"
- "_nitsBoostFactor"
- "_nitsScaler"
- "_options"
- "_override"
- "_plane"
- "_providers"
- "_queue"
- "_rampDownDuration"
- "_rampDownLuxDeltaThreshold"
- "_rampUpDuration"
- "_rampUpLuxDeltaThreshold"
- "_rampUpdateRate"
- "_reader"
- "_referenceLux"
- "_referenceWhiteBrightness"
- "_registryID"
- "_rows"
- "_runOnCallbackQueue:"
- "_service"
- "_setDeviceNits:"
- "_size"
- "_supported"
- "_terminationCallback"
- "_terminationIterator"
- "_terminationNotifPort"
- "_thermalMitigation"
- "activate"
- "activate:"
- "addDisplayService:"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "allValues"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "at:"
- "autorelease"
- "boostFactorFromIOFixed:"
- "bootargs"
- "bytes"
- "callbackQueue"
- "cancel"
- "capabilities"
- "cfContainerID"
- "class"
- "close"
- "codingKeys"
- "commitElements:direction:error:"
- "conformsToProtocol:"
- "containerID"
- "copy"
- "copyAllAvailableControls"
- "copyAvailableControls"
- "copyModuleIdentifier"
- "copyNSArray"
- "copyProperty:"
- "copyProperty:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "d24@0:8^@16"
- "data"
- "dataCopy"
- "date"
- "debugDescription"
- "description"
- "dict"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithCapacity:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "displayInvalidHandler"
- "doubleValue"
- "earlierDate:"
- "elementsMatching:"
- "enqueueCommandSync:inputBuffer:inputBufferSize:responseObj:options:"
- "enqueueCommandSync:timestamp:inputBuffer:inputBufferSize:responseTimestamp:outputBuffer:inOutBufferSize:options:"
- "example.m"
- "exceptionWithName:reason:userInfo:"
- "f"
- "f16@0:8"
- "f20@0:8i16"
- "f24@0:8Q16"
- "f32@0:8Q16Q24"
- "failToCreateDisplaysFor:"
- "findDCPServiceWithName:role:"
- "floatValue"
- "get:"
- "getBytes:length:"
- "getCol:andRow:"
- "getNitsWithError:"
- "hash"
- "i16@0:8"
- "init"
- "initWithArray:"
- "initWithBCError:"
- "initWithBootArgs:"
- "initWithCString:encoding:"
- "initWithCapacity:"
- "initWithCount:"
- "initWithDictionary:"
- "initWithDomain:"
- "initWithDomain:code:userInfo:"
- "initWithDouble:"
- "initWithFloat:"
- "initWithFormat:"
- "initWithIOKitError:"
- "initWithInt:"
- "initWithLength:"
- "initWithObjects:"
- "initWithProvider:"
- "initWithProviders:"
- "initWithReader:"
- "initWithService:"
- "initWithService:andOptions:"
- "initWithService:andPlane:"
- "initWithService:andPlane:andOptions:"
- "initWithServiceName:role:"
- "initWithString:"
- "initWithSuiteName:"
- "initWithTimeIntervalSinceNow:"
- "initWithUUIDString:"
- "initWithValues:andCount:"
- "initWithValues:andCountCols:andRows:"
- "intValue"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isValid"
- "laterDate:"
- "length"
- "lengthOfBytesUsingEncoding:"
- "loadData:toDestination:"
- "loadFixedFloat:toDestination:"
- "loadFixedFloat:withScaler:toDestination:"
- "loadFloat:toDestination:"
- "loadFloatArray:toDestination:"
- "loadIOFixedArray:toDestination:"
- "loadInt16Array:toDestination:"
- "loadInt:toDestination:"
- "loadUint16Array:toDestination:"
- "loadUint:toDestination:"
- "loadUintArray:toDestination:"
- "logHandle"
- "main_block_invoke_2"
- "maxNits"
- "minNits"
- "multipleControlEnabled"
- "mutableBytes"
- "mutableData"
- "newArrayFromDoubles:size:"
- "newArrayFromFloats:size:"
- "newArrayFromIntegers:size:"
- "newMonitorForAllControlsWithHandler:error:"
- "newMonitorWithHandler:error:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "open"
- "paramsWithProvider:"
- "parseAuroraCapabilities"
- "parseCPMSParams"
- "parseChromicCorrectionParams"
- "parseColorCapabilities"
- "parserWithReader:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "physicalMax"
- "physicalMin"
- "propertyForKey:"
- "providerFromList:"
- "providerWithDict:"
- "providerWithDomain:"
- "providers"
- "queue"
- "r^f16@0:8"
- "r^f24@0:8Q16"
- "raise:format:"
- "rangeOfString:"
- "reader"
- "readerWithService:"
- "readerWithService:andOptions:"
- "readerWithService:andPlane:"
- "readerWithService:andPlane:andOptions:"
- "refreshBoostFactor"
- "registryID"
- "release"
- "removeDisplayService"
- "removeObjectForKey:"
- "respondsToSelector:"
- "retIOKitError"
- "retain"
- "retainCount"
- "scaleValue:"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "self"
- "sendCommand:inputBuffer:inputBufferSize:"
- "sendOOBCommand:inputBuffer:inputBufferSize:"
- "serialize:"
- "service"
- "setBoostFactor:"
- "setCallbackQueue:"
- "setCancelHandler:"
- "setDispatchQueue:"
- "setDisplayInvalidHandler:"
- "setDisplayService:"
- "setIntegerValue:"
- "setLogHandle:"
- "setMultipleControlEnabled:"
- "setNits:error:"
- "setNitsAsync:completionHandler:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setProperty:property:"
- "setProperty:value:error:"
- "setPropertyAync:value:completionHandler:"
- "setRemovalHandler:"
- "setValue:forKey:"
- "sharedInstance"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "superclass"
- "synchronize"
- "timeIntervalSinceDate:"
- "type"
- "unitExponent"
- "unsignedIntValue"
- "usage"
- "usagePage"
- "userInfo"
- "utilites.m"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8f16"
- "v24@0:8@\"NSObject<OS_os_log>\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v32@0:8d16@?24"
- "v40@0:8@16@24@?32"
- "valueForKey:"
- "zone"

```
