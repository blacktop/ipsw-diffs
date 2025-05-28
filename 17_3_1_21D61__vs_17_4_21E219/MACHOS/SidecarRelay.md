## SidecarRelay

> `/usr/libexec/SidecarRelay`

```diff

-315.4.0.0.0
-  __TEXT.__text: 0x7699c
-  __TEXT.__auth_stubs: 0x1af0
+315.105.0.0.0
+  __TEXT.__text: 0x7d234
+  __TEXT.__auth_stubs: 0x1b20
   __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0x6a4
-  __TEXT.__cstring: 0x4bdd
+  __TEXT.__cstring: 0x537d
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x30d3
-  __TEXT.__constg_swiftt: 0x1d1c
-  __TEXT.__swift5_typeref: 0x1972
+  __TEXT.__const: 0x3eaa
+  __TEXT.__constg_swiftt: 0x1f18
+  __TEXT.__swift5_typeref: 0x1ab8
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0xbaa
-  __TEXT.__swift5_fieldmd: 0x11d0
-  __TEXT.__swift5_assocty: 0x230
-  __TEXT.__swift5_proto: 0x26c
-  __TEXT.__swift5_types: 0x158
+  __TEXT.__swift5_reflstr: 0xe1a
+  __TEXT.__swift5_fieldmd: 0x1324
+  __TEXT.__swift5_assocty: 0x410
+  __TEXT.__swift5_proto: 0x2fc
+  __TEXT.__swift5_types: 0x174
   __TEXT.__objc_classname: 0x146
-  __TEXT.__objc_methname: 0x1894
+  __TEXT.__objc_methname: 0x18bc
   __TEXT.__objc_methtype: 0x9f1
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__swift5_capture: 0x8fc
-  __TEXT.__unwind_info: 0x22c8
-  __TEXT.__eh_frame: 0x1288
-  __DATA_CONST.__auth_got: 0xd80
-  __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__auth_ptr: 0xc0
-  __DATA_CONST.__const: 0x48b0
+  __TEXT.__swift5_capture: 0x91c
+  __TEXT.__unwind_info: 0x2444
+  __TEXT.__eh_frame: 0x1258
+  __DATA_CONST.__auth_got: 0xd98
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__auth_ptr: 0xd0
+  __DATA_CONST.__const: 0x50a0
   __DATA_CONST.__cfstring: 0x60
-  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x49c0
+  __DATA_CONST.__objc_protorefs: 0x78
+  __DATA_CONST.__objc_classrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0x4cb8
   __DATA.__objc_selrefs: 0x738
-  __DATA.__objc_protorefs: 0x78
-  __DATA.__objc_classrefs: 0x178
-  __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x1638
-  __DATA.__data: 0x3500
-  __DATA.__bss: 0x4298
+  __DATA.__data: 0x3890
+  __DATA.__bss: 0x5498
   __DATA.__common: 0x110
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3739
-  Symbols:   733
-  CStrings:  858
+  Functions: 4221
+  Symbols:   736
+  CStrings:  902
 
Symbols:
+ _$sSw10copyMemory4fromySW_tF
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFyXl_Ts5
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss26DefaultStringInterpolationV15literalCapacity18interpolationCountABSi_SitcfC
- _$sSw5countSivg
- _objc_release_x1
CStrings:
+ " - remote device IDS identifier: ["
+ "315.105"
+ "Calling completion block that was left unexecuted during deinitialization."
+ "Can't construct Array with count < 0"
+ "Cancelling timer that is still alive during deinitialization."
+ "Division by zero"
+ "Division results in an overflow"
+ "Error encountered: [%@]."
+ "Handling remote initiation request. Request: [%s. Options: [%s]"
+ "Insufficient space allocated to copy string contents"
+ "Must take zero or more splits"
+ "Negative value is not representable"
+ "Not enough bits to represent the passed value"
+ "Operation deinitialized without prior execution of completion block"
+ "Range requires lowerBound <= upperBound"
+ "SidecarRelay/RemoteDisplayInitiationOperation.swift"
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
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "_TtC12SidecarRelay27EnhancedDiscoveryController"
+ "_TtC12SidecarRelay32RemoteDisplayInitiationOperation"
+ "cancelled"
+ "completion"
+ "deviceGenerationChangedPassthroughSubject"
+ "enhancedDiscoveryController"
+ "initWithDevice:sessionState:visualDetectability:"
+ "invalid Collection: less than 'count' elements in collection"
+ "lastTriggerAttemptTime"
+ "outstandingOperation"
+ "queue"
- "315.4"
- "initWithDevice:sessionState:"

```
