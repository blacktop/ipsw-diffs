## ManagedSettingsExtension

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/PlugIns/ManagedSettingsExtension.appex/ManagedSettingsExtension`

```diff

-2381.2.7.5.2
-  __TEXT.__text: 0x1b0a4
+2400.4.12.0.0
+  __TEXT.__text: 0x1e618
   __TEXT.__auth_stubs: 0x900
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__objc_methlist: 0x3ac
+  __TEXT.__objc_methlist: 0x59c
   __TEXT.__objc_classname: 0x8d
-  __TEXT.__objc_methname: 0x17c3
+  __TEXT.__objc_methname: 0x1a61
   __TEXT.__objc_methtype: 0x241
-  __TEXT.__const: 0xbd8
-  __TEXT.__constg_swiftt: 0xb7c
+  __TEXT.__const: 0xcf8
+  __TEXT.__constg_swiftt: 0xbbc
   __TEXT.__swift5_typeref: 0x7ca
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0x1a6
   __TEXT.__swift5_fieldmd: 0x53c
   __TEXT.__swift5_types: 0x80
-  __TEXT.__cstring: 0x18a2
+  __TEXT.__cstring: 0x1762
   __TEXT.__swift5_proto: 0x78
   __TEXT.__swift5_protos: 0x6c
-  __TEXT.__oslogstring: 0x1cdd
+  __TEXT.__oslogstring: 0x1f2d
   __TEXT.__swift5_capture: 0x28
-  __TEXT.__unwind_info: 0x300
+  __TEXT.__unwind_info: 0x2d0
   __TEXT.__eh_frame: 0x110
   __DATA_CONST.__auth_got: 0x488
-  __DATA_CONST.__got: 0x480
-  __DATA_CONST.__auth_ptr: 0x1b8
-  __DATA_CONST.__const: 0xba8
+  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__auth_ptr: 0x1c8
+  __DATA_CONST.__const: 0xbe8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0xbb0
-  __DATA.__objc_selrefs: 0x7d8
+  __DATA.__objc_const: 0x950
+  __DATA.__objc_selrefs: 0x940
   __DATA.__objc_data: 0x170
   __DATA.__data: 0x390
   __DATA.__common: 0x40

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 408
-  Symbols:   235
-  CStrings:  561
+  Functions: 419
+  Symbols:   252
+  CStrings:  586
 
Symbols:
+ _MCFeatureCalculatorInputModeRPNAllowed
+ _MCFeatureCalculatorInputModeUnitConversionAllowed
+ _MCFeatureCalculatorModeMathPaperAllowed
+ _MCFeatureCalculatorModeProgrammerAllowed
+ _MCFeatureCalculatorModeScientificAllowed
+ _MCFeatureSafariHistoryClearingAllowed
+ _MCFeatureSafariPrivateBrowsingAllowed
+ _MCFeatureSquareRootOnBasicCalculatorForced
+ _objc_release_x26
+ _objc_retain_x23
+ _objc_retain_x24
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
- _swift_allocateGenericValueMetadata
CStrings:
+ "Applying denyHistoryClearing settings: %{bool,public}d"
+ "Applying denyInputModeRPN settings: %{bool}d, privacy: .public)"
+ "Applying denyInputModeUnitConversion settings: %{bool}d, privacy: .public)"
+ "Applying denyModeMathPaper settings: %{bool}d, privacy: .public)"
+ "Applying denyModeProgrammer settings: %{bool}d, privacy: .public)"
+ "Applying denyModeScientific settings: %{bool}d, privacy: .public)"
+ "Applying denyPrivateBrowsing settings: %{bool,public}d"
+ "Applying forceSquareRootOnBasicCalculator settings: %{bool}d, privacy: .public)"
+ "calculatorInputModeRPNAllowed"
+ "calculatorInputModeUnitConversionAllowed"
+ "calculatorModeMathPaperAllowed"
+ "calculatorModeProgrammerAllowed"
+ "calculatorModeScientificAllowed"
+ "denyHistoryClearing"
+ "denyHistoryClearingMetadata"
+ "denyInputModeRPN"
+ "denyInputModeRPNMetadata"
+ "denyInputModeUnitConversion"
+ "denyInputModeUnitConversionMetadata"
+ "denyModeMathPaper"
+ "denyModeMathPaperMetadata"
+ "denyModeProgrammer"
+ "denyModeProgrammerMetadata"
+ "denyModeScientific"
+ "denyModeScientificMetadata"
+ "denyPrivateBrowsing"
+ "denyPrivateBrowsingMetadata"
+ "effectiveDenyHistoryClearing should never be nil"
+ "effectiveDenyInputModeRPN should never be nil"
+ "effectiveDenyInputModeUnitConversion should never be nil"
+ "effectiveDenyModeMathPaper should never be nil"
+ "effectiveDenyModeProgrammer should never be nil"
+ "effectiveDenyModeScientific should never be nil"
+ "effectiveDenyPrivateBrowsing should never be nil"
+ "effectiveForceSquareRootOnBasicCalculator should never be nil"
+ "forceSquareRootOnBasicCalculator"
+ "forceSquareRootOnBasicCalculatorMetadata"
+ "safariHistoryClearingAllowed"
+ "safariPrivateBrowsingAllowed"
+ "squareRootOnBasicCalculatorForced"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
