## Settings

> `/System/Library/PrivateFrameworks/Settings.framework/Settings`

```diff

-207.2.501.0.0
-  __TEXT.__text: 0x7f5cc
-  __TEXT.__auth_stubs: 0x2410
+207.3.3.0.0
+  __TEXT.__text: 0x71158
+  __TEXT.__auth_stubs: 0x23f0
   __TEXT.__delay_helper: 0x158
-  __TEXT.__objc_methlist: 0x610
-  __TEXT.__const: 0x3f08
-  __TEXT.__cstring: 0x3d3e
-  __TEXT.__swift5_typeref: 0x20b3
+  __TEXT.__objc_methlist: 0xb08
+  __TEXT.__const: 0x4168
+  __TEXT.__cstring: 0x399e
+  __TEXT.__swift5_typeref: 0x2191
   __TEXT.__constg_swiftt: 0x2030
   __TEXT.__swift5_reflstr: 0x105b
   __TEXT.__swift5_fieldmd: 0x1244

   __TEXT.__swift5_assocty: 0x5f0
   __TEXT.__swift5_proto: 0x2a0
   __TEXT.__swift5_types: 0x164
+  __TEXT.__swift_as_entry: 0x84
+  __TEXT.__swift_as_ret: 0x8c
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_capture: 0x414
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__oslogstring: 0x7b5
-  __TEXT.__unwind_info: 0x1de0
-  __TEXT.__eh_frame: 0x1bc0
+  __TEXT.__oslogstring: 0x925
+  __TEXT.__unwind_info: 0x1c00
+  __TEXT.__eh_frame: 0x1b80
   __TEXT.__objc_classname: 0xc1
-  __TEXT.__objc_methname: 0x14ca
+  __TEXT.__objc_methname: 0x14db
   __TEXT.__objc_methtype: 0x303
-  __DATA_CONST.__got: 0x770
-  __DATA_CONST.__const: 0x510
+  __DATA_CONST.__got: 0x798
+  __DATA_CONST.__const: 0x468
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e0
+  __DATA_CONST.__objc_selrefs: 0x7d8
   __DATA_CONST.__objc_protorefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x1208
-  __AUTH_CONST.__auth_ptr: 0xc68
-  __AUTH_CONST.__const: 0x22a0
-  __AUTH_CONST.__objc_const: 0x4c40
-  __AUTH.__objc_data: 0x450
-  __DATA.__data: 0x13e8
-  __DATA.__bss: 0x2e50
+  __AUTH_CONST.__auth_got: 0x11f8
+  __AUTH_CONST.__auth_ptr: 0xc70
+  __AUTH_CONST.__const: 0x2480
+  __AUTH_CONST.__objc_const: 0x47c8
+  __DATA.__data: 0x14a0
+  __DATA.__bss: 0x2cd0
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x12e8
-  __DATA_DIRTY.__data: 0x2260
+  __DATA_DIRTY.__data: 0x2278
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0x2100
+  __DATA_DIRTY.__bss: 0x2280
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2636
-  Symbols:   374
-  CStrings:  747
+  Functions: 2558
+  Symbols:   408
+  CStrings:  738
 
Symbols:
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getExistentialTypeMetadata
+ _swift_getFunctionTypeMetadata0
+ _swift_initStructMetadataWithLayoutString
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x10
- _objc_retain_x1
- _swift_allocateGenericValueMetadata
- _swift_initStructMetadata
CStrings:
+ "  item count: %ld"
+ "Collecting open intents..."
+ "Collecting open intents... done!"
+ "Indexing settingsEntities..."
+ "Indexing settingsEntities... Done!"
+ "Indexing settingsEnums..."
+ "Indexing settingsEnums... Done!"
+ "adding done"
+ "com.apple.settingsframework.lnentity"
+ "com.apple.settingsframework.lnenum"
+ "deleteSearchableItems done, adding %ld items to index"
+ "deleteSearchableItems for %s"
+ "domainIdentifier"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
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
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "com.apple.Preferences.firstParty"
- "invalid Collection: less than 'count' elements in collection"

```
