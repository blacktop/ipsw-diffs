## ManagedSettingsAgent

> `/System/Library/Frameworks/ManagedSettings.framework/Versions/A/ManagedSettingsAgent`

```diff

-242.2.2.0.0
-  __TEXT.__text: 0x57fdc
+242.4.10.0.0
+  __TEXT.__text: 0x566fc
   __TEXT.__auth_stubs: 0x18a0
-  __TEXT.__objc_methlist: 0x170
+  __TEXT.__objc_methlist: 0x434
   __TEXT.__const: 0x133c
-  __TEXT.__cstring: 0x1ad5
-  __TEXT.__objc_methname: 0xbb0
+  __TEXT.__cstring: 0x17b5
+  __TEXT.__objc_methname: 0xb95
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xc2c
-  __TEXT.__swift5_typeref: 0xe09
+  __TEXT.__constg_swiftt: 0xc34
+  __TEXT.__swift5_typeref: 0xe0f
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x741
   __TEXT.__swift5_fieldmd: 0x6f4

   __TEXT.__swift5_types: 0x7c
   __TEXT.__objc_classname: 0x63
   __TEXT.__objc_methtype: 0xfe
-  __TEXT.__oslogstring: 0x20d2
+  __TEXT.__oslogstring: 0x21b2
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_capture: 0x28c
-  __TEXT.__unwind_info: 0xaa0
-  __TEXT.__eh_frame: 0x1660
+  __TEXT.__unwind_info: 0xa40
+  __TEXT.__eh_frame: 0x16d8
   __DATA_CONST.__auth_got: 0xc50
-  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__got: 0x458
   __DATA_CONST.__auth_ptr: 0x380
   __DATA_CONST.__const: 0x14a0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA.__objc_const: 0x1488
-  __DATA.__objc_selrefs: 0x278
-  __DATA.__objc_data: 0x3e8
-  __DATA.__data: 0x1750
+  __DATA.__objc_const: 0x1258
+  __DATA.__objc_selrefs: 0x318
+  __DATA.__objc_data: 0x138
+  __DATA.__data: 0x1760
   __DATA.__common: 0x68
   __DATA.__bss: 0x1b00
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: CEDDC81B-E5E0-3C75-BFCB-AAB02F66A067
-  Functions: 900
-  Symbols:   622
-  CStrings:  418
+  UUID: 319B451C-C64C-31A4-9726-C7B84831AE5C
+  Functions: 871
+  Symbols:   625
+  CStrings:  404
 
Symbols:
+ _$s15ManagedSettings010WebContentB0V12FilterPolicyOSQAAMc
+ _$s15ManagedSettings010WebContentB0V15blockedByFilterAA15SettingMetadataVyAC0G6PolicyOGvgZ
+ _$s15ManagedSettings06SafariB0V19denyHistoryClearingAA15SettingMetadataVySbGvgZ
+ _$s15ManagedSettings06SafariB0V19denyPrivateBrowsingAA15SettingMetadataVySbGvgZ
+ _$s15ManagedSettings11PersistenceC013readEffectiveB04fromSDySSSo8NSObjectCG10Foundation3URLV_tKFZ
+ _$s15ManagedSettings11PersistenceC014readUnmigratedB04fromSDySSSo8NSObjectCG10Foundation3URLV_tFZ
+ _$s15ManagedSettings11PersistenceC07readRawB04fromSDySSSo8NSObjectCG10Foundation3URLV_tKFZ
+ _$s15ManagedSettings11PersistenceC08writeRawB0_2toySDySSSo8NSObjectCG_10Foundation3URLVtKFZ
+ _$s15ManagedSettings11PersistenceC09readLocalB04fromSDySSSo8NSObjectCG10Foundation3URLV_tKFZ
- _$s15ManagedSettings11PersistenceC4read4fromSDySSSo8NSObjectCG10Foundation3URLV_tKFZ
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
CStrings:
+ "Failed to read effective settings from %{public}s: %{public}s"
+ "Failed to read local settings from %{public}s: %{public}s"
+ "Failed to update effective settings for record %{public}s: %{public}s"
+ "Skipping effective settings from %{public}s because the file does not exist"
+ "Skipping local settings from %{public}s because the file does not exist"
- "Can't construct Array with count < 0"
- "Failed to read settings from %{public}s: %{public}s"
- "Insufficient space allocated to copy string contents"
- "Skipping settings from %{public}s because the file does not exist"
- "Swift/Array.swift"
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
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "copyItemAtURL:toURL:error:"
- "invalid Collection: less than 'count' elements in collection"

```
