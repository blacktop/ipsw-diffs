## modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

-513.0.0.0.0
-  __TEXT.__text: 0x159470
-  __TEXT.__auth_stubs: 0x37a0
+522.0.0.0.0
+  __TEXT.__text: 0x159e0c
+  __TEXT.__auth_stubs: 0x3840
   __TEXT.__objc_methlist: 0x158
-  __TEXT.__const: 0x5056
-  __TEXT.__cstring: 0x3280
-  __TEXT.__swift5_typeref: 0x2359
-  __TEXT.__swift5_capture: 0xbc8
-  __TEXT.__objc_methname: 0x492
-  __TEXT.__oslogstring: 0x8409
+  __TEXT.__const: 0x5096
+  __TEXT.__cstring: 0x32d0
+  __TEXT.__swift5_typeref: 0x242d
+  __TEXT.__swift5_capture: 0xba8
+  __TEXT.__objc_methname: 0x4ba
+  __TEXT.__oslogstring: 0x85e9
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x2778
+  __TEXT.__constg_swiftt: 0x27ec
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_reflstr: 0x1ec3
-  __TEXT.__swift5_fieldmd: 0x1c60
-  __TEXT.__swift5_types: 0x198
+  __TEXT.__swift5_fieldmd: 0x1c98
+  __TEXT.__swift5_types: 0x19c
   __TEXT.__objc_classname: 0x78
   __TEXT.__objc_methtype: 0x191
   __TEXT.__swift_as_entry: 0x8c4
   __TEXT.__swift_as_ret: 0xa1c
-  __TEXT.__swift5_proto: 0x2d8
+  __TEXT.__swift5_proto: 0x2dc
   __TEXT.__swift5_assocty: 0x1a0
-  __TEXT.__swift5_protos: 0x80
-  __TEXT.__unwind_info: 0x5cd8
-  __TEXT.__eh_frame: 0x145a0
-  __DATA_CONST.__auth_got: 0x1bd0
-  __DATA_CONST.__got: 0xe98
-  __DATA_CONST.__auth_ptr: 0xc70
-  __DATA_CONST.__const: 0x3cf0
-  __DATA_CONST.__objc_classlist: 0x190
+  __TEXT.__swift5_protos: 0x84
+  __TEXT.__unwind_info: 0x6088
+  __TEXT.__eh_frame: 0x14578
+  __DATA_CONST.__auth_got: 0x1c20
+  __DATA_CONST.__got: 0xea0
+  __DATA_CONST.__auth_ptr: 0xc98
+  __DATA_CONST.__const: 0x3cb0
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA.__objc_const: 0x3b88
-  __DATA.__objc_selrefs: 0x220
+  __DATA.__objc_const: 0x3c58
+  __DATA.__objc_selrefs: 0x230
   __DATA.__objc_data: 0x550
-  __DATA.__data: 0x5878
+  __DATA.__data: 0x5980
   __DATA.__common: 0x568
   __DATA.__bss: 0x4d40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/ANEClientSignals.framework/ANEClientSignals
   - /System/Library/PrivateFrameworks/AppleIntelligenceReporting.framework/AppleIntelligenceReporting

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7AE217DD-3F06-308C-991A-8B0FF5071100
-  Functions: 6429
-  Symbols:   1559
-  CStrings:  1004
+  UUID: C2F17344-6B03-3B4F-B224-D7C2E2C7866F
+  Functions: 6426
+  Symbols:   1575
+  CStrings:  1017
 
Symbols:
+ _$s10Foundation25NSFastEnumerationIteratorVMa
+ _$s10Foundation25NSFastEnumerationIteratorVStAAMc
+ _$sScI4next9isolation7ElementQzSgScA_pSgYi_tYa7FailureQzYKFTj
+ _$sScI4next9isolation7ElementQzSgScA_pSgYi_tYa7FailureQzYKFTjTu
+ _$sSo7NSArrayC10FoundationE12makeIteratorAC017NSFastEnumerationD0VyF
+ _$sSt4next7ElementQzSgyFTj
+ _$ss018_bridgeAnyObjectToB0yypyXlSgF
+ _$ss15LazyMapSequenceV8IteratorVMn
+ _$ss15LazyMapSequenceVMn
+ _$ss18LazyFilterSequenceV8IteratorVMn
+ _$ss18LazyFilterSequenceVMn
+ _$ss27_bridgeAnythingToObjectiveCyyXlxlF
+ _$ss38_bridgeAnythingNonVerbatimToObjectiveCyyXlxnlF
+ _IOPSCopyPowerSourcesInfo
+ _IOPSCopyPowerSourcesList
+ _IOPSGetPowerSourceDescription
CStrings:
+ "Could not create internalBatteryPowerDescription."
+ "Device is charging and connected to power"
+ "Device is fully charged and connected to power"
+ "Device is not connected to power"
+ "Failed to create power source snapshot."
+ "Failed to read power source list."
+ "PID %d: Rate limit exceeded. Allowing request because device is connected to power."
+ "_TtC13modelmanagerd13PowerProvider"
+ "__swift_objectForKeyedSubscript:"
+ "_powerStatus"
+ "fetchNextStreamingRequest for request: %s cannot be called concurrencly"
+ "internalStreamSet"

```
