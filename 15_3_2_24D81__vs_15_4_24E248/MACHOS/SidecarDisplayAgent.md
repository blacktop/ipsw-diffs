## SidecarDisplayAgent

> `/usr/libexec/SidecarDisplayAgent`

```diff

-342.3.1.0.0
-  __TEXT.__text: 0x82444
-  __TEXT.__auth_stubs: 0x2ea0
+342.4.4.0.0
+  __TEXT.__text: 0x7f530
+  __TEXT.__auth_stubs: 0x2e50
   __TEXT.__objc_stubs: 0x500
-  __TEXT.__objc_methlist: 0x388
-  __TEXT.__const: 0x4774
-  __TEXT.__cstring: 0x322b
+  __TEXT.__objc_methlist: 0x794
+  __TEXT.__const: 0x44c4
+  __TEXT.__cstring: 0x2d9b
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x31d8
-  __TEXT.__swift5_typeref: 0x17f4
-  __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x13ea
-  __TEXT.__swift5_fieldmd: 0x1ca4
-  __TEXT.__swift5_assocty: 0x520
-  __TEXT.__swift5_proto: 0x2fc
-  __TEXT.__swift5_types: 0x26c
+  __TEXT.__constg_swiftt: 0x314c
+  __TEXT.__swift5_typeref: 0x1706
+  __TEXT.__swift5_builtin: 0x118
+  __TEXT.__swift5_reflstr: 0x133a
+  __TEXT.__swift5_fieldmd: 0x1bac
+  __TEXT.__swift5_assocty: 0x4c0
+  __TEXT.__swift5_proto: 0x2d4
+  __TEXT.__swift5_types: 0x258
   __TEXT.__objc_classname: 0x181
-  __TEXT.__objc_methname: 0x1a31
+  __TEXT.__objc_methname: 0x1a4c
   __TEXT.__objc_methtype: 0x5af
   __TEXT.__swift5_capture: 0x624
-  __TEXT.__oslogstring: 0x1e8a
+  __TEXT.__oslogstring: 0x1f4a
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__swift5_mpenum: 0x8
   __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__unwind_info: 0x2888
-  __TEXT.__eh_frame: 0x1218
-  __DATA_CONST.__auth_got: 0x1760
-  __DATA_CONST.__got: 0x6e0
-  __DATA_CONST.__auth_ptr: 0xa10
-  __DATA_CONST.__const: 0x4728
+  __TEXT.__unwind_info: 0x2780
+  __TEXT.__eh_frame: 0x1198
+  __DATA_CONST.__auth_got: 0x1738
+  __DATA_CONST.__got: 0x6e8
+  __DATA_CONST.__auth_ptr: 0xa40
+  __DATA_CONST.__const: 0x45a0
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x4370
-  __DATA.__objc_selrefs: 0x990
+  __DATA.__objc_const: 0x3c70
+  __DATA.__objc_selrefs: 0xa60
   __DATA.__objc_ivar: 0x14
-  __DATA.__objc_data: 0xd40
-  __DATA.__data: 0x4800
+  __DATA.__objc_data: 0xcf0
+  __DATA.__data: 0x46f0
+  __DATA.__bss: 0x49f8
   __DATA.__common: 0x2c8
-  __DATA.__bss: 0x4e78
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: CDC6A7D9-23F0-3508-8304-683ED60D7358
-  Functions: 4307
-  Symbols:   1218
-  CStrings:  1047
+  UUID: F451F190-2377-354E-B008-10B54209CCE9
+  Functions: 4275
+  Symbols:   1213
+  CStrings:  1026
 
Symbols:
+ _$s10Foundation4DataV15_RepresentationOys5UInt8VSicig
+ _OBJC_CLASS_$_NSUUID
+ _copysign
- _$s10Foundation13__DataStorageC5bytes6lengthACSVSg_Sitcfc
- _$s10Foundation4DataV14RangeReferenceCMa
- _$s10Foundation4DataVys5UInt8VSicig
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
CStrings:
+ "342.4.4"
+ "Remote device version is: %ld, configuring the audio stream to use the LLW0 path."
+ "Remote device version is: %s, configuring the audio stream to use the AWDL path."
+ "initWithUUIDBytes:"
+ "supportsAudioUsingUDPNW"
+ "version"
- "342.3.1"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Must take zero or more splits"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "invalid Collection: less than 'count' elements in collection"

```
