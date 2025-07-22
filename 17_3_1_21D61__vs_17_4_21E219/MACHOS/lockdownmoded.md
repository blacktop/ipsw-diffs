## lockdownmoded

> `/System/Library/PrivateFrameworks/LockdownMode.framework/lockdownmoded`

```diff

-65.0.0.0.0
-  __TEXT.__text: 0x2c950
-  __TEXT.__auth_stubs: 0x10a0
+65.100.3.0.0
+  __TEXT.__text: 0x2dae4
+  __TEXT.__auth_stubs: 0x10d0
   __TEXT.__objc_methlist: 0xfc
-  __TEXT.__const: 0xc4e
-  __TEXT.__objc_methname: 0x1251
-  __TEXT.__cstring: 0x3609
+  __TEXT.__const: 0xc2e
+  __TEXT.__cstring: 0x3829
+  __TEXT.__objc_methname: 0x1240
   __TEXT.__swift5_typeref: 0x68f
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0xa08

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__gcc_except_tab: 0x10
   __TEXT.__oslogstring: 0xa7
-  __TEXT.__unwind_info: 0x670
+  __TEXT.__unwind_info: 0x654
   __TEXT.__eh_frame: 0x578
-  __DATA_CONST.__auth_got: 0x858
+  __DATA_CONST.__auth_got: 0x870
   __DATA_CONST.__got: 0x220
   __DATA_CONST.__auth_ptr: 0x70
   __DATA_CONST.__const: 0xe68

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_classrefs: 0x110
   __DATA.__objc_const: 0x1430
-  __DATA.__objc_selrefs: 0x390
-  __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0x110
+  __DATA.__objc_selrefs: 0x388
   __DATA.__objc_data: 0x598
-  __DATA.__data: 0x147a
+  __DATA.__data: 0x12da
   __DATA.__bss: 0x111d
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2760551E-C464-341C-88E4-0FB330016A48
-  Functions: 599
-  Symbols:   474
-  CStrings:  541
+  UUID: 07DF4455-6A3E-3913-927C-68E81C57AA69
+  Functions: 595
+  Symbols:   477
+  CStrings:  551
 
Symbols:
+ _$sSw10copyMemory4fromySW_tF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
+ _objc_retain_x2
- _objc_retain_x9
CStrings:
+ "Insufficient space allocated to copy string contents"
+ "Swift/ContiguousArrayBuffer.swift"
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
+ "invalid Collection: less than 'count' elements in collection"
- "Could not turn off Lockdown Mode due to an error: %@"
- "TURN_OFF_AND_RESTART"
- "Turning off Lockdown Mode…"
- "actionWithIdentifier:title:options:"
- "turnOff notifications delegate"

```
