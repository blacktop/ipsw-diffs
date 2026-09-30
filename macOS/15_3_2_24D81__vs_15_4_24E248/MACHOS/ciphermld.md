## ciphermld

> `/usr/libexec/ciphermld`

```diff

-239.80.5.0.0
-  __TEXT.__text: 0x2604
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x46d
+274.101.1.0.0
+  __TEXT.__text: 0x2748
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x1fd
   __TEXT.__objc_methname: 0x10
-  __TEXT.__oslogstring: 0x47
+  __TEXT.__oslogstring: 0x67
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x59
+  __TEXT.__swift5_typeref: 0x63
   __TEXT.__unwind_info: 0xe8
   __TEXT.__eh_frame: 0xa8
-  __DATA_CONST.__auth_got: 0x250
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__auth_got: 0x288
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
-  __DATA.__data: 0x30
-  __DATA.__common: 0x8
+  __DATA.__data: 0x50
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CipherML.framework/Versions/A/CipherML

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 863105AF-A9B1-3642-BB94-CB98A234DE9E
-  Functions: 33
-  Symbols:   119
-  CStrings:  31
+  UUID: 36D69863-938E-3C85-9ED3-CBA981E53D43
+  Functions: 39
+  Symbols:   132
+  CStrings:  20
 
Symbols:
+ _$s8Dispatch0A13WorkItemFlagsVMa
+ _$s8Dispatch0A13WorkItemFlagsVMn
+ _$s8Dispatch0A13WorkItemFlagsVs10SetAlgebraAAMc
+ _$s8Dispatch0A3QoSV11unspecifiedACvgZ
+ _$s8Dispatch0A3QoSVMa
+ _$sSayxGSTsMc
+ _$sSo18OS_dispatch_sourceC8DispatchE16makeSignalSource6signal5queueSo0a1_b1_c1_H0_ps5Int32V_So0a1_b1_I0CSgtFZ
+ _$sSo18OS_dispatch_sourceP8DispatchE15setEventHandler3qos5flags7handleryAC0D3QoSV_AC0D13WorkItemFlagsVyyXBSgtF
+ _$sSo18OS_dispatch_sourceP8DispatchE6resumeyyF
+ _$ss10SetAlgebraPyxqd__ncSTRd__7ElementQyd__ACRtzlufCTj
+ _OBJC_CLASS_$_OS_dispatch_source
+ __Block_copy
+ __Block_release
+ __NSConcreteStackBlock
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftOSLog
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$sypN
- _swift_arrayDestroy
CStrings:
+ "Received SIGTERM, shutting down"
+ "v8@?0"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
