## Accessibility

> `/System/Library/Frameworks/Accessibility.framework/Accessibility`

```diff

-502.7.8.0.0
-  __TEXT.__text: 0x13b68
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x111c
-  __TEXT.__const: 0x1264
+534.1.0.0.0
+  __TEXT.__text: 0x15330
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x130c
+  __TEXT.__const: 0x126c
   __TEXT.__gcc_except_tab: 0x308
-  __TEXT.__cstring: 0xf52
+  __TEXT.__cstring: 0x1002
   __TEXT.__dlopen_cstrs: 0x274
   __TEXT.__oslogstring: 0x108
   __TEXT.__swift5_typeref: 0x381

   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x8c0
+  __TEXT.__unwind_info: 0x900
   __TEXT.__eh_frame: 0x590
-  __TEXT.__objc_classname: 0x33e
-  __TEXT.__objc_methname: 0x2410
-  __TEXT.__objc_methtype: 0x50e
-  __TEXT.__objc_stubs: 0x1540
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x410
-  __DATA_CONST.__objc_classlist: 0x100
+  __TEXT.__objc_classname: 0x37c
+  __TEXT.__objc_methname: 0x2800
+  __TEXT.__objc_methtype: 0x534
+  __TEXT.__objc_stubs: 0x1900
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x3f0
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x930
+  __DATA_CONST.__objc_selrefs: 0xa68
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__const: 0x930
-  __AUTH_CONST.__cfstring: 0xac0
-  __AUTH_CONST.__objc_const: 0x27d0
+  __AUTH_CONST.__auth_got: 0x5a0
+  __AUTH_CONST.__const: 0x970
+  __AUTH_CONST.__cfstring: 0xb40
+  __AUTH_CONST.__objc_const: 0x2b50
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x148
-  __DATA.__data: 0x368
-  __DATA.__bss: 0x1530
+  __AUTH.__objc_data: 0x690
+  __AUTH.__data: 0x90
+  __DATA.__objc_ivar: 0x15c
+  __DATA.__data: 0x360
+  __DATA.__bss: 0x1560
   __DATA.__common: 0x19
   __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__data: 0x168
+  __DATA_DIRTY.__data: 0x108
   __DATA_DIRTY.__bss: 0xac0
   __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 52E541D4-B1D6-3CD0-84E5-0F065D8D1F24
-  Functions: 830
-  Symbols:   1909
-  CStrings:  815
+  UUID: A0F02A6F-004F-3E99-AE79-AD6B797764BB
+  Functions: 881
+  Symbols:   2074
+  CStrings:  884
 
Symbols:
+ +[AXBrailleTable defaultTableForLocale:]
+ +[AXBrailleTable languageAgnosticTables]
+ +[AXBrailleTable supportedLocales]
+ +[AXBrailleTable supportsSecureCoding]
+ +[AXBrailleTable tablesForLocale:]
+ +[AXBrailleTranslationResult supportsSecureCoding]
+ +[AXBrailleTranslator sharedLock]
+ +[AXBrailleTranslator sharedLock].cold.1
+ -[AXBrailleTable .cxx_destruct]
+ -[AXBrailleTable brltTable]
+ -[AXBrailleTable copyWithZone:]
+ -[AXBrailleTable encodeWithCoder:]
+ -[AXBrailleTable identifier]
+ -[AXBrailleTable initWithBRLTTable:]
+ -[AXBrailleTable initWithCoder:]
+ -[AXBrailleTable initWithIdentifier:]
+ -[AXBrailleTable isEightDot]
+ -[AXBrailleTable language]
+ -[AXBrailleTable locales]
+ -[AXBrailleTable localizedName]
+ -[AXBrailleTable localizedProviderName]
+ -[AXBrailleTable providerIdentifier]
+ -[AXBrailleTable setBrltTable:]
+ -[AXBrailleTranslationResult .cxx_destruct]
+ -[AXBrailleTranslationResult copyWithZone:]
+ -[AXBrailleTranslationResult encodeWithCoder:]
+ -[AXBrailleTranslationResult initWithCoder:]
+ -[AXBrailleTranslationResult initWithInputString:ResultString:locationMap:]
+ -[AXBrailleTranslationResult inputString]
+ -[AXBrailleTranslationResult locationMap]
+ -[AXBrailleTranslationResult resultString]
+ -[AXBrailleTranslator .cxx_destruct]
+ -[AXBrailleTranslator backTranslateBraille:]
+ -[AXBrailleTranslator initWithBrailleTable:]
+ -[AXBrailleTranslator setTranslator:]
+ -[AXBrailleTranslator translatePrintText:]
+ -[AXBrailleTranslator translator]
+ _BRLTServiceTranslatorFunction
+ _BRLTTableEnumeratorFunction
+ _BRLTTableFunction
+ _BrailleTranslationLibrary.sLib
+ _BrailleTranslationLibrary.sOnce
+ _CFStringCreateCopy
+ _OBJC_CLASS_$_AXBrailleTable
+ _OBJC_CLASS_$_AXBrailleTranslationResult
+ _OBJC_CLASS_$_AXBrailleTranslator
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_IVAR_$_AXBrailleTable._brltTable
+ _OBJC_IVAR_$_AXBrailleTranslationResult._inputString
+ _OBJC_IVAR_$_AXBrailleTranslationResult._locationMap
+ _OBJC_IVAR_$_AXBrailleTranslationResult._resultString
+ _OBJC_IVAR_$_AXBrailleTranslator._translator
+ _OBJC_METACLASS_$_AXBrailleTable
+ _OBJC_METACLASS_$_AXBrailleTranslationResult
+ _OBJC_METACLASS_$_AXBrailleTranslator
+ __OBJC_$_CLASS_METHODS_AXBrailleTable
+ __OBJC_$_CLASS_METHODS_AXBrailleTranslationResult
+ __OBJC_$_CLASS_METHODS_AXBrailleTranslator
+ __OBJC_$_INSTANCE_METHODS_AXBrailleTable
+ __OBJC_$_INSTANCE_METHODS_AXBrailleTranslationResult
+ __OBJC_$_INSTANCE_METHODS_AXBrailleTranslator
+ __OBJC_$_INSTANCE_VARIABLES_AXBrailleTable
+ __OBJC_$_INSTANCE_VARIABLES_AXBrailleTranslationResult
+ __OBJC_$_INSTANCE_VARIABLES_AXBrailleTranslator
+ __OBJC_$_PROP_LIST_AXBrailleTable
+ __OBJC_$_PROP_LIST_AXBrailleTranslationResult
+ __OBJC_$_PROP_LIST_AXBrailleTranslator
+ __OBJC_CLASS_PROTOCOLS_$_AXBrailleTable
+ __OBJC_CLASS_PROTOCOLS_$_AXBrailleTranslationResult
+ __OBJC_CLASS_RO_$_AXBrailleTable
+ __OBJC_CLASS_RO_$_AXBrailleTranslationResult
+ __OBJC_CLASS_RO_$_AXBrailleTranslator
+ __OBJC_METACLASS_RO_$_AXBrailleTable
+ __OBJC_METACLASS_RO_$_AXBrailleTranslationResult
+ __OBJC_METACLASS_RO_$_AXBrailleTranslator
+ ___33+[AXBrailleTranslator sharedLock]_block_invoke
+ ___BrailleTranslationLibrary_block_invoke
+ ___block_literal_global.103
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_Accessibility
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_Accessibility
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_Accessibility
+ _classBRLTServiceTranslator
+ _classBRLTTable
+ _classBRLTTableEnumerator
+ _dlopen
+ _getBRLTServiceTranslatorClass
+ _getBRLTTableClass
+ _getBRLTTableEnumeratorClass
+ _initBRLTServiceTranslator
+ _initBRLTServiceTranslator.cold.1
+ _initBRLTTable
+ _initBRLTTable.cold.1
+ _initBRLTTableEnumerator
+ _initBRLTTableEnumerator.cold.1
+ _kCTFontContentSizeCategoryL
+ _objc_msgSend$brailleForText:locations:
+ _objc_msgSend$brltTable
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$defaultTablesArrayForLocale:
+ _objc_msgSend$externalServiceIdentifier
+ _objc_msgSend$identifier
+ _objc_msgSend$initWithBRLTTable:
+ _objc_msgSend$initWithExternalIdentifier:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithInputString:ResultString:locationMap:
+ _objc_msgSend$initWithTable:
+ _objc_msgSend$language
+ _objc_msgSend$languageAgnosticTables
+ _objc_msgSend$locales
+ _objc_msgSend$localizedName
+ _objc_msgSend$localizedService
+ _objc_msgSend$locationMap
+ _objc_msgSend$lock
+ _objc_msgSend$providerIdentifier
+ _objc_msgSend$resultString
+ _objc_msgSend$sharedLock
+ _objc_msgSend$supportedLocales
+ _objc_msgSend$supportsTranslationMode8Dot
+ _objc_msgSend$tableEnumeratorWithSystemBundlePath
+ _objc_msgSend$tableIdentifier
+ _objc_msgSend$tablesForLocale:inBundle:
+ _objc_msgSend$textForBraille:locations:
+ _objc_msgSend$translator
+ _objc_msgSend$translatorBundles
+ _objc_msgSend$unlock
+ _sharedLock._sharedLock
+ _sharedLock.onceToken
+ _swift_dynamicCast
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_Accessibility
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_Accessibility
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_Accessibility
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_Accessibility
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_Accessibility
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_Accessibility
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_Accessibility
CStrings:
+ "%@.%@"
+ "/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation"
+ "@\"BRLTServiceTranslator\""
+ "@\"BRLTTable\""
+ "AXBrailleTable"
+ "AXBrailleTranslationResult"
+ "AXBrailleTranslator"
+ "BRLTServiceTranslator"
+ "BRLTTable"
+ "BRLTTableEnumerator"
+ "T@\"BRLTServiceTranslator\",&,N,V_translator"
+ "T@\"BRLTTable\",&,N,V_brltTable"
+ "T@\"NSArray\",R,N,V_locationMap"
+ "T@\"NSSet\",R,N"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_inputString"
+ "T@\"NSString\",R,N,V_resultString"
+ "TB,R,N"
+ "_brltTable"
+ "_inputString"
+ "_locationMap"
+ "_resultString"
+ "_translator"
+ "backTranslateBraille:"
+ "brailleForText:locations:"
+ "brltTable"
+ "decodeObjectOfClass:forKey:"
+ "defaultTableForLocale:"
+ "defaultTablesArrayForLocale:"
+ "externalServiceIdentifier"
+ "initWithBRLTTable:"
+ "initWithBrailleTable:"
+ "initWithExternalIdentifier:"
+ "initWithIdentifier:"
+ "initWithInputString:ResultString:locationMap:"
+ "initWithTable:"
+ "inputString"
+ "isEightDot"
+ "language"
+ "languageAgnosticTables"
+ "locales"
+ "localizedName"
+ "localizedProviderName"
+ "localizedService"
+ "locationMap"
+ "lock"
+ "providerIdentifier"
+ "resultString"
+ "setBrltTable:"
+ "setTranslator:"
+ "sharedLock"
+ "supportedLocales"
+ "supportsTranslationMode8Dot"
+ "tableEnumeratorWithSystemBundlePath"
+ "tableIdentifier"
+ "tablesForLocale:"
+ "tablesForLocale:inBundle:"
+ "textForBraille:locations:"
+ "translatePrintText:"
+ "translator"
+ "translatorBundles"
+ "unlock"

```
