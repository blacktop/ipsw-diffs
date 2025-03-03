## ManagedSettingsAgent

> `/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent`

```diff

-242.2.2.0.0
-  __TEXT.__text: 0x5fd98
-  __TEXT.__auth_stubs: 0x1ad0
+242.4.8.0.0
+  __TEXT.__text: 0x5d304
+  __TEXT.__auth_stubs: 0x1af0
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__objc_methlist: 0x220
-  __TEXT.__const: 0x12fc
+  __TEXT.__objc_methlist: 0x598
+  __TEXT.__const: 0x144c
   __TEXT.__objc_classname: 0x121
-  __TEXT.__objc_methname: 0xf00
+  __TEXT.__objc_methname: 0xee5
   __TEXT.__objc_methtype: 0x194
-  __TEXT.__cstring: 0x1c35
+  __TEXT.__cstring: 0x18c5
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xcc0
-  __TEXT.__swift5_typeref: 0xf9b
+  __TEXT.__constg_swiftt: 0xcc8
+  __TEXT.__swift5_typeref: 0xf8d
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x77d
   __TEXT.__swift5_fieldmd: 0x738
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_proto: 0x108
   __TEXT.__swift5_types: 0x80
-  __TEXT.__oslogstring: 0x2352
+  __TEXT.__oslogstring: 0x23e2
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_capture: 0x34c
-  __TEXT.__unwind_info: 0xbd8
-  __TEXT.__eh_frame: 0x1798
-  __DATA_CONST.__auth_got: 0xd70
-  __DATA_CONST.__got: 0x428
-  __DATA_CONST.__auth_ptr: 0x3d0
-  __DATA_CONST.__const: 0x1910
+  __TEXT.__unwind_info: 0xb18
+  __TEXT.__eh_frame: 0x1838
+  __DATA_CONST.__auth_got: 0xd80
+  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__auth_ptr: 0x3a8
+  __DATA_CONST.__const: 0x1908
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA.__objc_const: 0x19c0
-  __DATA.__objc_selrefs: 0x300
-  __DATA.__objc_data: 0x610
-  __DATA.__data: 0x18e0
+  __DATA.__objc_const: 0x16f0
+  __DATA.__objc_selrefs: 0x3a8
+  __DATA.__objc_data: 0x2c8
+  __DATA.__data: 0x18e8
   __DATA.__bss: 0x1990
   __DATA.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1007
-  Symbols:   664
-  CStrings:  473
+  Functions: 951
+  Symbols:   671
+  CStrings:  455
 
Symbols:
+ _$s15ManagedSettings010WebContentB0V12FilterPolicyOSQAAMc
+ _$s15ManagedSettings010WebContentB0V15blockedByFilterAA15SettingMetadataVyAC0G6PolicyOGvgZ
+ _$s15ManagedSettings06SafariB0V19denyHistoryClearingAA15SettingMetadataVySbGvgZ
+ _$s15ManagedSettings06SafariB0V19denyPrivateBrowsingAA15SettingMetadataVySbGvgZ
+ _$s15ManagedSettings11PersistenceC013readEffectiveB04fromSDySSSo8NSObjectCG10Foundation3URLV_tKFZ
+ _$s15ManagedSettings11PersistenceC07readRawB04fromSDySSSo8NSObjectCG10Foundation3URLV_tKFZ
+ _$s15ManagedSettings11PersistenceC08writeRawB0_2toySDySSSo8NSObjectCG_10Foundation3URLVtKFZ
+ _$s15ManagedSettings11PersistenceC09readLocalB04fromSDySSSo8NSObjectCG10Foundation3URLV_tKFZ
+ _$s15ManagedSettings11PersistenceC7rawData4from10Foundation0E0VSgAF3URLV_tKFZ
+ _objc_release_x9
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _$s15ManagedSettings11PersistenceC4data4from10Foundation4DataVSgAF3URLV_tKFZ
- _$s15ManagedSettings11PersistenceC4read4fromSDySSSo8NSObjectCG10Foundation3URLV_tKFZ
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- __swift_FORCE_LOAD_$_swiftFileProvider
CStrings:
+ "Failed to read effective settings from %{public}s: %{public}s"
+ "Failed to read local settings from %{public}s: %{public}s"
+ "Skipping effective settings from %{public}s because the file does not exist"
+ "Skipping local settings from %{public}s because the file does not exist"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Failed to read settings from %{public}s: %{public}s"
- "Insufficient space allocated to copy string contents"
- "Skipping settings from %{public}s because the file does not exist"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
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
- "copyItemAtURL:toURL:error:"
- "invalid Collection: less than 'count' elements in collection"

```
