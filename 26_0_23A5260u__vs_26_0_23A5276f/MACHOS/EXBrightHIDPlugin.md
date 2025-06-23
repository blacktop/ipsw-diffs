## EXBrightHIDPlugin

> `/System/Library/HIDPlugins/ServiceFilters/EXBrightHIDPlugin.plugin/EXBrightHIDPlugin`

```diff

-2079.0.9.502.1
-  __TEXT.__text: 0x24f0
-  __TEXT.__auth_stubs: 0x510
+2079.0.21.0.0
+  __TEXT.__text: 0x26e4
+  __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_stubs: 0x100
   __TEXT.__objc_methlist: 0x28c
-  __TEXT.__const: 0x88
+  __TEXT.__const: 0x98
   __TEXT.__objc_methname: 0x369
-  __TEXT.__cstring: 0x19c
-  __TEXT.__oslogstring: 0x3be
+  __TEXT.__cstring: 0x1bc
+  __TEXT.__oslogstring: 0x4ae
   __TEXT.__objc_classname: 0x30
   __TEXT.__objc_methtype: 0x359
   __TEXT.__swift5_typeref: 0x2e

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x100
   __TEXT.__eh_frame: 0x70
-  __DATA_CONST.__auth_got: 0x290
+  __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__const: 0x98
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0A6B776F-A6CC-3546-8ED5-8679D2C150F2
+  UUID: 5E68C5EA-11B5-3087-88E0-0CA7F6A40993
   Functions: 58
-  Symbols:   535
-  CStrings:  147
+  Symbols:   525
+  CStrings:  152
 
Symbols:
+ _AMFDRSealingManifestCopyLocalMultiCombinedDataAddDataClassWithMultiData
+ _os_parse_boot_arg_int
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_EXBrightHIDPlugin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_EXBrightHIDPlugin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_EXBrightHIDPlugin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_EXBrightHIDPlugin
Functions:
~ -[EXBrightHIDPlugin fetchFDRBundlesFromDisk] : 668 -> 1076
~ _OUTLINED_FUNCTION_1 : 28 -> 12
~ -[EXBrightHIDPlugin initWithService:].cold.1 : 128 -> 124
~ -[EXBrightHIDPlugin initWithService:].cold.2 : 128 -> 124
~ -[EXBrightHIDPlugin initWithService:].cold.3 : 52 -> 60
~ -[EXBrightHIDPlugin initWithService:].cold.4 : 52 -> 60
~ -[EXBrightHIDPlugin forwardFDRBundles].cold.1 : 52 -> 60
~ -[EXBrightHIDPlugin forwardFDRBundles].cold.2 : 52 -> 60
~ -[EXBrightHIDPlugin fetchFDRBundlesFromDisk].cold.1 : 52 -> 120
~ -[EXBrightHIDPlugin fetchFDRBundlesFromDisk].cold.2 : 52 -> 60
~ -[EXBrightHIDPlugin fetchFDRBundlesFromDisk].cold.3 : 52 -> 60
CStrings:
+ "[EXBright] %s=%lld"
+ "[EXBright] Data begin failed. Error: '%@'."
+ "[EXBright] [SealingManifest] Added data class %@."
+ "[EXBright] [SealingManifest] Failed to add data class %@. Error: '%@'."
+ "[EXBright] [SealingMap] Added data class %@."
+ "[EXBright] [SealingMap] Failed to add data class %@. Error: '%@'."
+ "exbright_r2r_path_enforce"
- "[EXBright] Data begin failed"
- "[EXBright] Failed to add data class %@"

```
