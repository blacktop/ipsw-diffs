## rtcreportingd

> `/usr/libexec/rtcreportingd`

```diff

-48.26.0.0.0
-  __TEXT.__text: 0x891d0
-  __TEXT.__auth_stubs: 0x20e0
-  __TEXT.__const: 0x3a56
-  __TEXT.__cstring: 0x3f47
+74.6.0.0.0
+  __TEXT.__text: 0x89f2c
+  __TEXT.__auth_stubs: 0x2120
+  __TEXT.__const: 0x3b56
+  __TEXT.__cstring: 0x44e7
   __TEXT.__constg_swiftt: 0x164c
   __TEXT.__swift5_typeref: 0x11f2
-  __TEXT.__swift5_reflstr: 0xe15
-  __TEXT.__swift5_fieldmd: 0x19cc
+  __TEXT.__swift5_reflstr: 0xe25
+  __TEXT.__swift5_fieldmd: 0x19e4
+  __TEXT.__objc_methname: 0x5cf
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x1a0
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_proto: 0x398
   __TEXT.__swift5_types: 0x1c4
   __TEXT.__objc_classname: 0x55
-  __TEXT.__objc_methname: 0x5a5
   __TEXT.__objc_methtype: 0xad
   __TEXT.__swift5_capture: 0x298
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2fd0
-  __TEXT.__eh_frame: 0x6748
-  __DATA_CONST.__auth_got: 0x1070
-  __DATA_CONST.__got: 0x470
+  __TEXT.__unwind_info: 0x2fac
+  __TEXT.__eh_frame: 0x66f0
+  __DATA_CONST.__auth_got: 0x1090
+  __DATA_CONST.__got: 0x480
   __DATA_CONST.__auth_ptr: 0xd8
   __DATA_CONST.__const: 0x4588
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x88
   __DATA.__objc_const: 0x1d38
-  __DATA.__objc_selrefs: 0x170
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x80
+  __DATA.__objc_selrefs: 0x178
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x36f8
+  __DATA.__data: 0x3668
   __DATA.__bss: 0x6d00
   __DATA.__common: 0x200
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4023
-  Symbols:   791
-  CStrings:  468
+  Functions: 4016
+  Symbols:   798
+  CStrings:  503
 
Symbols:
+ _$s10Foundation13__DataStorageC5bytes6lengthACSVSg_Sitcfc
+ _$s10Foundation4DataV06InlineB0VyAESWcfC
+ _$s10Foundation4DataV14RangeReferenceCMa
+ _$s10Foundation4DataV5bytes5countACSV_SitcfC
+ _$sSw10copyMemory4fromySW_tF
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFyXl_Ts5
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _MCFeatureAppAnalyticsAllowed
+ _MCFeatureAppAndAccessoryAnalyticsAllowed
+ _OBJC_CLASS_$_MCRestrictionManager
+ _os_eligibility_get_domain_answer
- _$s10Foundation4DataV15_RepresentationOyAESWcfC
- _$sSW5countSivg
- _$sSv10copyMemory4from9byteCountySV_SitF
- _$sSw5countSivg
- _objc_retain_x28
CStrings:
+ "Can't construct Array with count < 0"
+ "Device is eligible for Elisabeth"
+ "Division by zero"
+ "Division results in an overflow"
+ "Insufficient space allocated to copy string contents"
+ "Must take zero or more splits"
+ "Negative value is not representable"
+ "Not enough bits to represent the passed value"
+ "Range requires lowerBound <= upperBound"
+ "Swift/Array.swift"
+ "Swift/Collection.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
+ "Swift/Range.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unable to determine eligibility due to error %d"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "_canShareWithDevelopers"
+ "_isDeviceEligibleForPE"
+ "boolSettingForFeature:"
+ "disable_pe"
+ "invalid Collection: less than 'count' elements in collection"
+ "skipping %{public}s:%{public}s: PE disabled"

```
