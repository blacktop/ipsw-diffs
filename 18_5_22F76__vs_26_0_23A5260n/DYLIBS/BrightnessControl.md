## BrightnessControl

> `/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`

```diff

-1902.120.21.0.1
-  __TEXT.__text: 0x9af8
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x4a8
-  __TEXT.__const: 0x3fa8
-  __TEXT.__gcc_except_tab: 0x1f4
-  __TEXT.__cstring: 0xb96
-  __TEXT.__oslogstring: 0xb76
-  __TEXT.__unwind_info: 0x318
-  __TEXT.__objc_classname: 0x8d
-  __TEXT.__objc_methname: 0xd78
-  __TEXT.__objc_methtype: 0x297
-  __TEXT.__objc_stubs: 0xf60
-  __DATA_CONST.__got: 0x100
+2079.0.9.502.1
+  __TEXT.__text: 0xdec8
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0xd84
+  __TEXT.__const: 0x3fb0
+  __TEXT.__gcc_except_tab: 0x208
+  __TEXT.__cstring: 0x11ee
+  __TEXT.__oslogstring: 0xd25
+  __TEXT.__unwind_info: 0x468
+  __TEXT.__objc_classname: 0x1e9
+  __TEXT.__objc_methname: 0x1927
+  __TEXT.__objc_methtype: 0x62a
+  __TEXT.__objc_stubs: 0x15a0
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x388
-  __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x410
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_selrefs: 0x770
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2d0
+  __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0xdc0
-  __AUTH_CONST.__objc_const: 0xb88
-  __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__cfstring: 0x18a0
+  __AUTH_CONST.__objc_const: 0x2098
+  __AUTH_CONST.__objc_floatobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xc0
-  __DATA.__data: 0x4
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x160
+  __DATA.__data: 0x248
   __DATA.__bss: 0x28
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 919DAAA7-B978-3E65-B3AB-9A351A2BE1B7
-  Functions: 234
-  Symbols:   816
-  CStrings:  574
+  UUID: F1B9E589-0301-35D5-A030-E0DEA26C9204
+  Functions: 385
+  Symbols:   1360
+  CStrings:  1009
 
Symbols:
+ +[CBCombinedConfigProvider providerFromList:]
+ +[CBDictConfigProvider providerWithDict:]
+ +[CBDictSerializer serialize:]
+ +[CBGammaContrastPreservationParams paramsWithProvider:]
+ +[CBIORegistryParser parserWithReader:]
+ +[CBIORegistryReader readerWithService:]
+ +[CBIORegistryReader readerWithService:andOptions:]
+ +[CBIORegistryReader readerWithService:andPlane:]
+ +[CBIORegistryReader readerWithService:andPlane:andOptions:]
+ +[CBUserDefaultsProvider providerWithDomain:]
+ +[NSArray(PrimitiveArrayConstructible) newArrayFromDoubles:size:]
+ +[NSArray(PrimitiveArrayConstructible) newArrayFromFloats:size:]
+ +[NSArray(PrimitiveArrayConstructible) newArrayFromIntegers:size:]
+ -[BCAppleBacklightBrtControl parseChromicCorrectionParams]
+ -[BCAppleBacklightBrtControl parseColorCapabilities]
+ -[CBBootArgsConfigProvider bootargs]
+ -[CBBootArgsConfigProvider dealloc]
+ -[CBBootArgsConfigProvider initWithBootArgs:]
+ -[CBBootArgsConfigProvider init]
+ -[CBBootArgsConfigProvider loadFixedFloat:toDestination:]
+ -[CBBootArgsConfigProvider loadFixedFloat:withScaler:toDestination:]
+ -[CBBootArgsConfigProvider loadFloat:toDestination:]
+ -[CBBootArgsConfigProvider loadFloatArray:toDestination:]
+ -[CBBootArgsConfigProvider loadIOFixedArray:toDestination:]
+ -[CBBootArgsConfigProvider loadInt16Array:toDestination:]
+ -[CBBootArgsConfigProvider loadInt:toDestination:]
+ -[CBBootArgsConfigProvider loadUint:toDestination:]
+ -[CBBootArgsConfigProvider loadUintArray:toDestination:]
+ -[CBBootArgsConfigProvider logHandle]
+ -[CBBootArgsConfigProvider setLogHandle:]
+ -[CBCombinedConfigProvider dealloc]
+ -[CBCombinedConfigProvider initWithProviders:]
+ -[CBCombinedConfigProvider loadFixedFloat:toDestination:]
+ -[CBCombinedConfigProvider loadFixedFloat:withScaler:toDestination:]
+ -[CBCombinedConfigProvider loadFloat:toDestination:]
+ -[CBCombinedConfigProvider loadFloatArray:toDestination:]
+ -[CBCombinedConfigProvider loadFloatArray:toDestination:].cold.1
+ -[CBCombinedConfigProvider loadIOFixedArray:toDestination:]
+ -[CBCombinedConfigProvider loadIOFixedArray:toDestination:].cold.1
+ -[CBCombinedConfigProvider loadInt16Array:toDestination:]
+ -[CBCombinedConfigProvider loadInt16Array:toDestination:].cold.1
+ -[CBCombinedConfigProvider loadInt:toDestination:]
+ -[CBCombinedConfigProvider loadUint:toDestination:]
+ -[CBCombinedConfigProvider loadUintArray:toDestination:]
+ -[CBCombinedConfigProvider loadUintArray:toDestination:].cold.1
+ -[CBCombinedConfigProvider logHandle]
+ -[CBCombinedConfigProvider providers]
+ -[CBCombinedConfigProvider setLogHandle:]
+ -[CBDictConfigProvider dealloc]
+ -[CBDictConfigProvider description]
+ -[CBDictConfigProvider dict]
+ -[CBDictConfigProvider initWithDictionary:]
+ -[CBDictConfigProvider loadFixedFloat:toDestination:]
+ -[CBDictConfigProvider loadFixedFloat:withScaler:toDestination:]
+ -[CBDictConfigProvider loadFloat:toDestination:]
+ -[CBDictConfigProvider loadFloatArray:toDestination:]
+ -[CBDictConfigProvider loadIOFixedArray:toDestination:]
+ -[CBDictConfigProvider loadInt16Array:toDestination:]
+ -[CBDictConfigProvider loadInt:toDestination:]
+ -[CBDictConfigProvider loadUint:toDestination:]
+ -[CBDictConfigProvider loadUintArray:toDestination:]
+ -[CBDictConfigProvider logHandle]
+ -[CBDictConfigProvider setLogHandle:]
+ -[CBFloatArray at:]
+ -[CBFloatArray copyNSArray]
+ -[CBFloatArray count]
+ -[CBFloatArray dataCopy]
+ -[CBFloatArray data]
+ -[CBFloatArray dealloc]
+ -[CBFloatArray description]
+ -[CBFloatArray get:]
+ -[CBFloatArray initWithCount:]
+ -[CBFloatArray initWithValues:andCount:]
+ -[CBFloatArray mutableData]
+ -[CBFloatArray objectAtIndexedSubscript:]
+ -[CBFloatArray2D getCol:andRow:]
+ -[CBFloatArray2D initWithValues:andCountCols:andRows:]
+ -[CBGammaContrastPreservationParams ASb]
+ -[CBGammaContrastPreservationParams Bmax]
+ -[CBGammaContrastPreservationParams Bmin]
+ -[CBGammaContrastPreservationParams Kb]
+ -[CBGammaContrastPreservationParams Kl]
+ -[CBGammaContrastPreservationParams Lmax]
+ -[CBGammaContrastPreservationParams Lmin]
+ -[CBGammaContrastPreservationParams ambientFactor]
+ -[CBGammaContrastPreservationParams aodRampDuration]
+ -[CBGammaContrastPreservationParams codingKeys]
+ -[CBGammaContrastPreservationParams dealloc]
+ -[CBGammaContrastPreservationParams gammaMax]
+ -[CBGammaContrastPreservationParams gammaMin]
+ -[CBGammaContrastPreservationParams gcpFactorHigh]
+ -[CBGammaContrastPreservationParams gcpFactorLow]
+ -[CBGammaContrastPreservationParams initWithProvider:]
+ -[CBGammaContrastPreservationParams initWithProvider:].cold.1
+ -[CBGammaContrastPreservationParams initWithProvider:].cold.2
+ -[CBGammaContrastPreservationParams initWithProvider:].cold.3
+ -[CBGammaContrastPreservationParams initWithProvider:].cold.4
+ -[CBGammaContrastPreservationParams initWithProvider:].cold.5
+ -[CBGammaContrastPreservationParams initWithProvider:].cold.6
+ -[CBGammaContrastPreservationParams initWithProvider:].cold.7
+ -[CBGammaContrastPreservationParams isEqual:]
+ -[CBGammaContrastPreservationParams rampDownDuration]
+ -[CBGammaContrastPreservationParams rampDownLuxDeltaThreshold]
+ -[CBGammaContrastPreservationParams rampUpDuration]
+ -[CBGammaContrastPreservationParams rampUpLuxDeltaThreshold]
+ -[CBGammaContrastPreservationParams rampUpdateRate]
+ -[CBGammaContrastPreservationParams referenceLux]
+ -[CBGammaContrastPreservationParams referenceWhiteBrightness]
+ -[CBGammaContrastPreservationParams supported]
+ -[CBIORegistryParser dealloc]
+ -[CBIORegistryParser description]
+ -[CBIORegistryParser initWithReader:]
+ -[CBIORegistryParser loadData:toDestination:]
+ -[CBIORegistryParser loadFixedFloat:toDestination:]
+ -[CBIORegistryParser loadFixedFloat:withScaler:toDestination:]
+ -[CBIORegistryParser loadFloat:toDestination:]
+ -[CBIORegistryParser loadFloatArray:toDestination:]
+ -[CBIORegistryParser loadIOFixedArray:toDestination:]
+ -[CBIORegistryParser loadInt16Array:toDestination:]
+ -[CBIORegistryParser loadInt:toDestination:]
+ -[CBIORegistryParser loadUint16Array:toDestination:]
+ -[CBIORegistryParser loadUint:toDestination:]
+ -[CBIORegistryParser loadUintArray:toDestination:]
+ -[CBIORegistryParser logHandle]
+ -[CBIORegistryParser reader]
+ -[CBIORegistryParser setLogHandle:]
+ -[CBIORegistryReader copyProperty:]
+ -[CBIORegistryReader dealloc]
+ -[CBIORegistryReader initWithService:]
+ -[CBIORegistryReader initWithService:andOptions:]
+ -[CBIORegistryReader initWithService:andPlane:]
+ -[CBIORegistryReader initWithService:andPlane:andOptions:]
+ -[CBIORegistryReader initWithService:andPlane:andOptions:].cold.1
+ -[CBIORegistryReader service]
+ -[CBUserDefaultsProvider dealloc]
+ -[CBUserDefaultsProvider description]
+ -[CBUserDefaultsProvider initWithDomain:]
+ GCC_except_table40
+ _CFRetain
+ _CFStringCreateWithCString
+ _CFStringCreateWithFormat
+ _CFStringGetSystemEncoding
+ _NSMallocException
+ _NSRangeException
+ _OBJC_CLASS_$_CBBootArgsConfigProvider
+ _OBJC_CLASS_$_CBCombinedConfigProvider
+ _OBJC_CLASS_$_CBDictConfigProvider
+ _OBJC_CLASS_$_CBDictSerializer
+ _OBJC_CLASS_$_CBFloatArray
+ _OBJC_CLASS_$_CBFloatArray2D
+ _OBJC_CLASS_$_CBGammaContrastPreservationParams
+ _OBJC_CLASS_$_CBIORegistryParser
+ _OBJC_CLASS_$_CBIORegistryReader
+ _OBJC_CLASS_$_CBUserDefaultsProvider
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_IVAR_$_CBBootArgsConfigProvider._bootargs
+ _OBJC_IVAR_$_CBBootArgsConfigProvider._logHandle
+ _OBJC_IVAR_$_CBCombinedConfigProvider._logHandle
+ _OBJC_IVAR_$_CBCombinedConfigProvider._providers
+ _OBJC_IVAR_$_CBDictConfigProvider._dict
+ _OBJC_IVAR_$_CBDictConfigProvider._logHandle
+ _OBJC_IVAR_$_CBFloatArray._count
+ _OBJC_IVAR_$_CBFloatArray._data
+ _OBJC_IVAR_$_CBFloatArray._size
+ _OBJC_IVAR_$_CBFloatArray2D._cols
+ _OBJC_IVAR_$_CBFloatArray2D._rows
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._ASb
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._Bmax
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._Bmin
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._Kb
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._Kl
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._Lmax
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._Lmin
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._ambientFactor
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._aodRampDuration
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._codingKeys
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._gammaMax
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._gammaMin
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._gcpFactorHigh
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._gcpFactorLow
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._logHandle
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._rampDownDuration
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._rampDownLuxDeltaThreshold
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._rampUpDuration
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._rampUpLuxDeltaThreshold
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._rampUpdateRate
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._referenceLux
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._referenceWhiteBrightness
+ _OBJC_IVAR_$_CBGammaContrastPreservationParams._supported
+ _OBJC_IVAR_$_CBIORegistryParser._logHandle
+ _OBJC_IVAR_$_CBIORegistryParser._reader
+ _OBJC_IVAR_$_CBIORegistryReader._options
+ _OBJC_IVAR_$_CBIORegistryReader._plane
+ _OBJC_IVAR_$_CBIORegistryReader._service
+ _OBJC_IVAR_$_CBUserDefaultsProvider._desc
+ _OBJC_METACLASS_$_CBBootArgsConfigProvider
+ _OBJC_METACLASS_$_CBCombinedConfigProvider
+ _OBJC_METACLASS_$_CBDictConfigProvider
+ _OBJC_METACLASS_$_CBDictSerializer
+ _OBJC_METACLASS_$_CBFloatArray
+ _OBJC_METACLASS_$_CBFloatArray2D
+ _OBJC_METACLASS_$_CBGammaContrastPreservationParams
+ _OBJC_METACLASS_$_CBIORegistryParser
+ _OBJC_METACLASS_$_CBIORegistryReader
+ _OBJC_METACLASS_$_CBUserDefaultsProvider
+ _OUTLINED_FUNCTION_2
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSArray_$_PrimitiveArrayConstructible
+ __OBJC_$_CATEGORY_NSArray_$_PrimitiveArrayConstructible
+ __OBJC_$_CLASS_METHODS_CBCombinedConfigProvider
+ __OBJC_$_CLASS_METHODS_CBDictConfigProvider
+ __OBJC_$_CLASS_METHODS_CBDictSerializer
+ __OBJC_$_CLASS_METHODS_CBGammaContrastPreservationParams
+ __OBJC_$_CLASS_METHODS_CBIORegistryParser
+ __OBJC_$_CLASS_METHODS_CBIORegistryReader
+ __OBJC_$_CLASS_METHODS_CBUserDefaultsProvider
+ __OBJC_$_INSTANCE_METHODS_CBBootArgsConfigProvider
+ __OBJC_$_INSTANCE_METHODS_CBCombinedConfigProvider
+ __OBJC_$_INSTANCE_METHODS_CBDictConfigProvider
+ __OBJC_$_INSTANCE_METHODS_CBFloatArray
+ __OBJC_$_INSTANCE_METHODS_CBFloatArray2D
+ __OBJC_$_INSTANCE_METHODS_CBGammaContrastPreservationParams
+ __OBJC_$_INSTANCE_METHODS_CBIORegistryParser
+ __OBJC_$_INSTANCE_METHODS_CBIORegistryReader
+ __OBJC_$_INSTANCE_METHODS_CBUserDefaultsProvider
+ __OBJC_$_INSTANCE_VARIABLES_CBBootArgsConfigProvider
+ __OBJC_$_INSTANCE_VARIABLES_CBCombinedConfigProvider
+ __OBJC_$_INSTANCE_VARIABLES_CBDictConfigProvider
+ __OBJC_$_INSTANCE_VARIABLES_CBFloatArray
+ __OBJC_$_INSTANCE_VARIABLES_CBFloatArray2D
+ __OBJC_$_INSTANCE_VARIABLES_CBGammaContrastPreservationParams
+ __OBJC_$_INSTANCE_VARIABLES_CBIORegistryParser
+ __OBJC_$_INSTANCE_VARIABLES_CBIORegistryReader
+ __OBJC_$_INSTANCE_VARIABLES_CBUserDefaultsProvider
+ __OBJC_$_PROP_LIST_CBBootArgsConfigProvider
+ __OBJC_$_PROP_LIST_CBChromaticCorectionParamsProtocol
+ __OBJC_$_PROP_LIST_CBCombinedConfigProvider
+ __OBJC_$_PROP_LIST_CBDictConfigProvider
+ __OBJC_$_PROP_LIST_CBGammaContrastPreservationParams
+ __OBJC_$_PROP_LIST_CBIORegistryParser
+ __OBJC_$_PROP_LIST_CBIORegistryReader
+ __OBJC_$_PROP_LIST_CBPrimitiveConfigurationProvider
+ __OBJC_$_PROP_LIST_CBSerializable
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBChromaticCorectionParamsProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBIORegInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBPrimitiveConfigurationProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBSerializable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBChromaticCorectionParamsProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBIORegInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBPrimitiveConfigurationProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBSerializable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_CBChromaticCorectionParamsProtocol
+ __OBJC_$_PROTOCOL_REFS_CBIORegInterface
+ __OBJC_$_PROTOCOL_REFS_CBPrimitiveConfigurationProvider
+ __OBJC_$_PROTOCOL_REFS_CBSerializable
+ __OBJC_CLASS_PROTOCOLS_$_CBBootArgsConfigProvider
+ __OBJC_CLASS_PROTOCOLS_$_CBCombinedConfigProvider
+ __OBJC_CLASS_PROTOCOLS_$_CBDictConfigProvider
+ __OBJC_CLASS_PROTOCOLS_$_CBGammaContrastPreservationParams
+ __OBJC_CLASS_PROTOCOLS_$_CBIORegistryParser
+ __OBJC_CLASS_PROTOCOLS_$_CBIORegistryReader
+ __OBJC_CLASS_RO_$_CBBootArgsConfigProvider
+ __OBJC_CLASS_RO_$_CBCombinedConfigProvider
+ __OBJC_CLASS_RO_$_CBDictConfigProvider
+ __OBJC_CLASS_RO_$_CBDictSerializer
+ __OBJC_CLASS_RO_$_CBFloatArray
+ __OBJC_CLASS_RO_$_CBFloatArray2D
+ __OBJC_CLASS_RO_$_CBGammaContrastPreservationParams
+ __OBJC_CLASS_RO_$_CBIORegistryParser
+ __OBJC_CLASS_RO_$_CBIORegistryReader
+ __OBJC_CLASS_RO_$_CBUserDefaultsProvider
+ __OBJC_LABEL_PROTOCOL_$_CBChromaticCorectionParamsProtocol
+ __OBJC_LABEL_PROTOCOL_$_CBIORegInterface
+ __OBJC_LABEL_PROTOCOL_$_CBPrimitiveConfigurationProvider
+ __OBJC_LABEL_PROTOCOL_$_CBSerializable
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_CBBootArgsConfigProvider
+ __OBJC_METACLASS_RO_$_CBCombinedConfigProvider
+ __OBJC_METACLASS_RO_$_CBDictConfigProvider
+ __OBJC_METACLASS_RO_$_CBDictSerializer
+ __OBJC_METACLASS_RO_$_CBFloatArray
+ __OBJC_METACLASS_RO_$_CBFloatArray2D
+ __OBJC_METACLASS_RO_$_CBGammaContrastPreservationParams
+ __OBJC_METACLASS_RO_$_CBIORegistryParser
+ __OBJC_METACLASS_RO_$_CBIORegistryReader
+ __OBJC_METACLASS_RO_$_CBUserDefaultsProvider
+ __OBJC_PROTOCOL_$_CBChromaticCorectionParamsProtocol
+ __OBJC_PROTOCOL_$_CBIORegInterface
+ __OBJC_PROTOCOL_$_CBPrimitiveConfigurationProvider
+ __OBJC_PROTOCOL_$_CBSerializable
+ __OBJC_PROTOCOL_$_NSObject
+ __Z16load_from_readerIfEbP18CBIORegistryReaderP8NSStringPT_
+ __Z16load_from_readerIiEbP18CBIORegistryReaderP8NSStringPT_
+ __Z16load_from_readerIjEbP18CBIORegistryReaderP8NSStringPT_
+ __Z21get_value_from_cfdataIfEbPKvPT_
+ __Z21get_value_from_cfdataIiEbPKvPT_
+ __Z21get_value_from_cfdataIjEbPKvPT_
+ __Z22load_array_from_readerIfEmP18CBIORegistryReaderP8NSStringPPT_
+ __Z22load_array_from_readerIjEmP18CBIORegistryReaderP8NSStringPPT_
+ __Z22load_array_from_readerIsEmP18CBIORegistryReaderP8NSStringPPT_
+ __Z22load_array_from_readerItEmP18CBIORegistryReaderP8NSStringPPT_
+ __Z24create_array_from_cfdataIfEmPKvPPT_
+ __Z24create_array_from_cfdataIiEmPKvPPT_
+ __Z24create_array_from_cfdataIjEmPKvPPT_
+ __Z24create_array_from_cfdataIsEmPKvPPT_
+ __Z24create_array_from_cfdataItEmPKvPPT_
+ ___chkstk_darwin
+ ___gxx_personality_v0
+ _createAmmoliteKey
+ _create_uint32_array_from_cfdata
+ _find_bound
+ _get_float_from_bootarg
+ _get_uint32_from_cfdata
+ _kCBGCPASb
+ _kCBGCPAmbientFactor
+ _kCBGCPAmbientMax
+ _kCBGCPAmbientMin
+ _kCBGCPGammaFactorHigh
+ _kCBGCPGammaFactorLow
+ _kCBGCPGammaMax
+ _kCBGCPGammaMin
+ _kCBGCPKb
+ _kCBGCPKl
+ _kCBGCPNitsMax
+ _kCBGCPNitsMin
+ _load_bool_from_edt
+ _objc_exception_throw
+ _objc_msgSend$allValues
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$at:
+ _objc_msgSend$codingKeys
+ _objc_msgSend$copyNSArray
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$exceptionWithName:reason:userInfo:
+ _objc_msgSend$get:
+ _objc_msgSend$init
+ _objc_msgSend$initWithBootArgs:
+ _objc_msgSend$initWithCString:encoding:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithCount:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithDomain:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithFloat:
+ _objc_msgSend$initWithInt:
+ _objc_msgSend$initWithProvider:
+ _objc_msgSend$initWithProviders:
+ _objc_msgSend$initWithReader:
+ _objc_msgSend$initWithService:andOptions:
+ _objc_msgSend$initWithService:andPlane:
+ _objc_msgSend$initWithService:andPlane:andOptions:
+ _objc_msgSend$loadFixedFloat:toDestination:
+ _objc_msgSend$loadFixedFloat:withScaler:toDestination:
+ _objc_msgSend$loadFloat:toDestination:
+ _objc_msgSend$loadFloatArray:toDestination:
+ _objc_msgSend$loadIOFixedArray:toDestination:
+ _objc_msgSend$loadInt16Array:toDestination:
+ _objc_msgSend$loadInt:toDestination:
+ _objc_msgSend$loadUint:toDestination:
+ _objc_msgSend$loadUintArray:toDestination:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$paramsWithProvider:
+ _objc_msgSend$parseChromicCorrectionParams
+ _objc_msgSend$parseColorCapabilities
+ _objc_msgSend$parserWithReader:
+ _objc_msgSend$providerFromList:
+ _objc_msgSend$providerWithDict:
+ _objc_msgSend$providers
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$readerWithService:
+ _objc_msgSend$serialize:
+ _objc_msgSend$setLogHandle:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$valueForKey:
+ _objc_retain_x19
+ _objc_retain_x20
+ _strtof
- __Z10find_boundPKfmfPmS1_
- __Z22get_uint32_from_cfdataPKvPj
- _kIOMasterPortDefault
CStrings:
+ "#16@0:8"
+ "%s-%d"
+ "-[CBGammaContrastPreservationParams initWithProvider:]"
+ "@\"<CBIORegInterface>\""
+ "@\"NSArray\""
+ "@\"NSDictionary\""
+ "@\"NSDictionary\"16@0:8"
+ "@\"NSObject<OS_os_log>\"16@0:8"
+ "@\"NSString\"16@0:8"
+ "@24@0:8:16"
+ "@24@0:8@\"NSString\"16"
+ "@24@0:8I16I20"
+ "@24@0:8r*16"
+ "@28@0:8I16[128c]20"
+ "@28@0:8^d16I24"
+ "@28@0:8^f16I24"
+ "@28@0:8^i16I24"
+ "@32@0:8:16@24"
+ "@32@0:8I16[128c]20I28"
+ "@32@0:8^f16Q24"
+ "@40@0:8:16@24@32"
+ "@40@0:8^f16Q24Q32"
+ "ASb"
+ "AmmlAbsLux"
+ "AmmlPeriod"
+ "AmmlRelLux"
+ "AmmlTable"
+ "AmmlTableFactor"
+ "AuroraCLTMEnterMultiplier"
+ "AuroraCLTMThreshold"
+ "AuroraUPOEnterMultiplier"
+ "AuroraUPOThreshold"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B32@0:8@\"NSString\"16^I24"
+ "B32@0:8@\"NSString\"16^f24"
+ "B32@0:8@\"NSString\"16^i24"
+ "B32@0:8@\"NSString\"16r^^{__CFData}24"
+ "B32@0:8@16^I24"
+ "B32@0:8@16^f24"
+ "B32@0:8@16^i24"
+ "B32@0:8@16r^^{__CFData}24"
+ "B36@0:8@\"NSString\"16f24^f28"
+ "B36@0:8@16f24^f28"
+ "BLRCCTWarning"
+ "Bmax"
+ "Bmin"
+ "CBBootArgsConfigProvider"
+ "CBChromaticCorectionParamsProtocol"
+ "CBCombinedConfigProvider"
+ "CBDictConfigProvider"
+ "CBDictSerializer"
+ "CBFloatArray"
+ "CBFloatArray2D"
+ "CBGammaContrastPreservation"
+ "CBGammaContrastPreservationParams"
+ "CBGammaContrastPreservationParams.mm"
+ "CBIORegInterface"
+ "CBIORegistryParser"
+ "CBIORegistryReader"
+ "CBPrimitiveConfigurationProvider"
+ "CBSerializable"
+ "CBUserDefaultsProvider"
+ "CBUserDefaultsProvider(%@)"
+ "Disabling due to invalid config: %@(%f) <= 0"
+ "Disabling due to invalid config: %@(%f) >= %@(%f)"
+ "Disabling due to invalid config: %@(%f) out of sensible range [0.5,1.5]"
+ "Disabling due to invalid config: %@(%f) out of sensible range [0.5,2]"
+ "Disabling due to invalid config: %@(%f) out of sensible range [1,2]"
+ "DisplayVendorIndex"
+ "ForcedAmmoliteSupport"
+ "HarmonyShiftA"
+ "HarmonyShiftB"
+ "HarmonyStrength"
+ "I16@0:8"
+ "Kb"
+ "Kl"
+ "Lmax"
+ "Lmin"
+ "Loaded %@ = %d from %@"
+ "Loaded %@ = %f from %@"
+ "Loaded %@ = %u from %@"
+ "Loaded %@ from %@"
+ "NSObject"
+ "PAAEnergyConsumptionTarget"
+ "PAAMaxGain"
+ "PAARampDownMaxAPCEPoints"
+ "PAARampDownMinAPCEPoints"
+ "PAARampUpMaxAPCEPoints"
+ "PAARampUpMinAPCEPoints"
+ "PowerAwareAuroraSDRLUT"
+ "PreStrobeDimPeriod"
+ "PrimitiveArrayConstructible"
+ "Q32@0:8@\"NSString\"16^^I24"
+ "Q32@0:8@\"NSString\"16^^S24"
+ "Q32@0:8@\"NSString\"16^^f24"
+ "Q32@0:8@\"NSString\"16^^s24"
+ "Q32@0:8@16^^I24"
+ "Q32@0:8@16^^S24"
+ "Q32@0:8@16^^f24"
+ "Q32@0:8@16^^s24"
+ "SupportCLTMAwareAurora"
+ "T#,R"
+ "T@\"<CBIORegInterface>\",R,V_reader"
+ "T@\"NSArray\",R,V_providers"
+ "T@\"NSDictionary\",R"
+ "T@\"NSDictionary\",R,V_codingKeys"
+ "T@\"NSDictionary\",R,V_dict"
+ "T@\"NSObject<OS_os_log>\",&"
+ "T@\"NSObject<OS_os_log>\",&,V_logHandle"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"NSString\",R,V_bootargs"
+ "TI,R,V_service"
+ "TI,R,V_supported"
+ "Tf,R"
+ "Tf,R,V_ASb"
+ "Tf,R,V_Bmax"
+ "Tf,R,V_Bmin"
+ "Tf,R,V_Kb"
+ "Tf,R,V_Kl"
+ "Tf,R,V_Lmax"
+ "Tf,R,V_Lmin"
+ "Tf,R,V_ambientFactor"
+ "Tf,R,V_aodRampDuration"
+ "Tf,R,V_gammaMax"
+ "Tf,R,V_gammaMin"
+ "Tf,R,V_gcpFactorHigh"
+ "Tf,R,V_gcpFactorLow"
+ "Tf,R,V_rampDownDuration"
+ "Tf,R,V_rampDownLuxDeltaThreshold"
+ "Tf,R,V_rampUpDuration"
+ "Tf,R,V_rampUpLuxDeltaThreshold"
+ "Tf,R,V_rampUpdateRate"
+ "Tf,R,V_referenceLux"
+ "Tf,R,V_referenceWhiteBrightness"
+ "The length of the plane name is >= %zu"
+ "Vv16@0:8"
+ "[128c]"
+ "^f"
+ "^f16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_ASb"
+ "_Bmax"
+ "_Bmin"
+ "_Kb"
+ "_Kl"
+ "_Lmax"
+ "_Lmin"
+ "_ambientFactor"
+ "_aodRampDuration"
+ "_bootargs"
+ "_codingKeys"
+ "_cols"
+ "_count"
+ "_data"
+ "_desc"
+ "_dict"
+ "_gammaMax"
+ "_gammaMin"
+ "_gcpFactorHigh"
+ "_gcpFactorLow"
+ "_options"
+ "_plane"
+ "_providers"
+ "_rampDownDuration"
+ "_rampDownLuxDeltaThreshold"
+ "_rampUpDuration"
+ "_rampUpLuxDeltaThreshold"
+ "_rampUpdateRate"
+ "_reader"
+ "_referenceLux"
+ "_referenceWhiteBrightness"
+ "_rows"
+ "_size"
+ "_supported"
+ "allValues"
+ "ambientFactor"
+ "aml-abs-lux-thresh"
+ "aml-only-support"
+ "aml-period"
+ "aml-rel-lux-thresh"
+ "aml-table"
+ "aml-table-factor"
+ "aodRampDuration"
+ "arrayWithObjects:count:"
+ "at:"
+ "aurora-cltm-enter-multiplier"
+ "aurora-cltm-threshold"
+ "aurora-upo-enter-multiplier"
+ "aurora-upo-threshold"
+ "autorelease"
+ "blr-cct-warning"
+ "bootargs"
+ "class"
+ "codingKeys"
+ "com.apple.CoreBrightness.ChromaticCorrection"
+ "conformsToProtocol:"
+ "copyNSArray"
+ "data"
+ "dataCopy"
+ "debugDescription"
+ "dict"
+ "dictionaryRepresentation"
+ "dictionaryWithCapacity:"
+ "energy-consumption-target"
+ "exceptionWithName:reason:userInfo:"
+ "f16@0:8"
+ "f24@0:8Q16"
+ "f32@0:8Q16Q24"
+ "gammaMax"
+ "gammaMin"
+ "gcp"
+ "gcp-ambient-factor"
+ "gcp-ambient-max"
+ "gcp-ambient-min"
+ "gcp-as-b"
+ "gcp-gamma-factor-high"
+ "gcp-gamma-factor-low"
+ "gcp-gamma-max"
+ "gcp-gamma-min"
+ "gcp-k-b"
+ "gcp-k-l"
+ "gcp-nits-max"
+ "gcp-nits-min"
+ "gcp-ramp-down-duration"
+ "gcp-ramp-down-lux-threshold"
+ "gcp-ramp-up-duration"
+ "gcp-ramp-up-lux-threshold"
+ "gcp-ramp-update-rate"
+ "gcp-reference-ambient-lux"
+ "gcp-reference-white-nits"
+ "gcpFactorHigh"
+ "gcpFactorLow"
+ "get:"
+ "getCol:andRow:"
+ "i"
+ "initWithBootArgs:"
+ "initWithCString:encoding:"
+ "initWithCapacity:"
+ "initWithCount:"
+ "initWithDictionary:"
+ "initWithDomain:"
+ "initWithDouble:"
+ "initWithFloat:"
+ "initWithInt:"
+ "initWithProvider:"
+ "initWithProviders:"
+ "initWithReader:"
+ "initWithService:andOptions:"
+ "initWithService:andPlane:"
+ "initWithService:andPlane:andOptions:"
+ "initWithValues:andCount:"
+ "initWithValues:andCountCols:andRows:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "loadData:toDestination:"
+ "loadFixedFloat:toDestination:"
+ "loadFixedFloat:withScaler:toDestination:"
+ "loadFloat:toDestination:"
+ "loadFloatArray:toDestination:"
+ "loadIOFixedArray:toDestination:"
+ "loadInt16Array:toDestination:"
+ "loadInt:toDestination:"
+ "loadUint16Array:toDestination:"
+ "loadUint:toDestination:"
+ "loadUintArray:toDestination:"
+ "loaded"
+ "luxActivationThreshold"
+ "max-aurora-gain"
+ "mutableData"
+ "newArrayFromDoubles:size:"
+ "newArrayFromFloats:size:"
+ "newArrayFromIntegers:size:"
+ "nitsActivationThreshold"
+ "numberWithUnsignedInt:"
+ "objectAtIndexedSubscript:"
+ "paa-sdr-lut"
+ "pab-scaler-index"
+ "paramsWithProvider:"
+ "parseChromicCorrectionParams"
+ "parseColorCapabilities"
+ "parserWithReader:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "pre-strobe-dim-period"
+ "providerFromList:"
+ "providerWithDict:"
+ "providerWithDomain:"
+ "providers"
+ "r^f16@0:8"
+ "r^f24@0:8Q16"
+ "ramp-down-max-tap-point"
+ "ramp-down-min-tap-point"
+ "ramp-up-max-tap-point"
+ "ramp-up-min-tap-point"
+ "rampDownDuration"
+ "rampDownLuxDeltaThreshold"
+ "rampUpDuration"
+ "rampUpLuxDeltaThreshold"
+ "rampUpdateRate"
+ "rangeOfString:"
+ "reader"
+ "readerWithService:"
+ "readerWithService:andOptions:"
+ "readerWithService:andPlane:"
+ "readerWithService:andPlane:andOptions:"
+ "referenceLux"
+ "referenceWhiteBrightness"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "serialize:"
+ "service"
+ "setLogHandle:"
+ "substringFromIndex:"
+ "superclass"
+ "supported"
+ "supports-cltm-aware-aurora"
+ "supports-gcp"
+ "truetone-shift-a"
+ "truetone-shift-b"
+ "truetone-strength"
+ "unsignedIntValue"
+ "v24@0:8@\"NSObject<OS_os_log>\"16"
+ "valueForKey:"
+ "zone"
- "AuroraCPMSEnterMultiplier"
- "AuroraCPMSThreshold"
- "aurora-cpms-enter-multiplier"
- "aurora-cpms-threshold"

```
