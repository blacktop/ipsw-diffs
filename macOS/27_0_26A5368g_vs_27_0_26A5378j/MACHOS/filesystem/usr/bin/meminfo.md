## meminfo

> `/usr/bin/meminfo`

```diff

-  __TEXT.__text: 0xc318
-  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__text: 0xfe78
+  __TEXT.__auth_stubs: 0x970
   __TEXT.__objc_stubs: 0x100
-  __TEXT.__const: 0x6b4
+  __TEXT.__const: 0x784
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x1b0
-  __TEXT.__constg_swiftt: 0x16c
-  __TEXT.__swift5_reflstr: 0x1e7
-  __TEXT.__swift5_fieldmd: 0x39c
-  __TEXT.__cstring: 0x7d9
+  __TEXT.__swift5_typeref: 0x222
+  __TEXT.__constg_swiftt: 0x1c0
+  __TEXT.__swift5_reflstr: 0x23a
+  __TEXT.__swift5_fieldmd: 0x444
+  __TEXT.__cstring: 0x899
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x38
-  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_protos: 0x4
   __TEXT.__objc_methname: 0x98
-  __TEXT.__unwind_info: 0x2a0
-  __TEXT.__eh_frame: 0x268
-  __DATA_CONST.__const: 0x588
+  __TEXT.__unwind_info: 0x320
+  __TEXT.__eh_frame: 0x390
+  __DATA_CONST.__const: 0x710
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x460
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__auth_ptr: 0x180
+  __DATA_CONST.__auth_got: 0x4c0
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__auth_ptr: 0x198
   __DATA.__objc_selrefs: 0x40
-  __DATA.__data: 0x1e8
+  __DATA.__data: 0x218
   __DATA.__bss: 0x640
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/ArgumentParserInternal.framework/Versions/A/ArgumentParserInternal
   - /System/Library/PrivateFrameworks/perfdata.framework/Versions/A/perfdata
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  Functions: 216
-  Symbols:   238
-  CStrings:  56
+  Functions: 269
+  Symbols:   257
+  CStrings:  60
 
Sections:
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA.__objc_selrefs : content changed
Symbols:
+ _$s10Foundation4DataVN
+ _$sSD10FoundationE34_conditionallyBridgeFromObjectiveC_6resultSbSo12NSDictionaryC_SDyxq_GSgztFZ
+ _$sSS10FoundationE4data8encodingSSSgAA4DataVh_SSAAE8EncodingVtcfC
+ _$sSS10FoundationE8EncodingV4utf8ACvgZ
+ _$sSS10FoundationE8EncodingVMa
+ _$sSS4hash4intoys6HasherVz_tF
+ _$sSSSHsWP
+ _$sSis23CustomStringConvertiblesWP
+ _$ss18_DictionaryStorageC4copy8originalAByxq_Gs05__RawaB0C_tFZ
+ _$ss18_DictionaryStorageC6resize8original8capacity4moveAByxq_Gs05__RawaB0C_SiSbtFZ
+ _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
+ _$ss18_DictionaryStorageCMn
+ _$ss53KEY_TYPE_OF_DICTIONARY_VIOLATES_HASHABLE_REQUIREMENTSys5NeverOypXpF
+ _$sypN
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperties
+ _IORegistryEntryFromPath
+ _OBJC_CLASS_$_NSDictionary
+ __swiftEmptyDictionarySingleton
+ _kCFAllocatorDefault
+ _kIOMainPortDefault
+ _swift_bridgeObjectRetain_n
+ _swift_dynamicCastObjCClass
- _$ss042_stdlib_isOSVersionAtLeastOrVariantVersiondE0yBi1_Bw_BwBwBwBwBwtF
- _$ss5NeverON
- _$ss5NeverOs5ErrorsWP
- _swift_willThrowTypedImpl
CStrings:
+ "Expand wired-zone memory into individual zones."
+ "IODeviceTree:/chosen"
+ "IODeviceTree:/chosen/carveout-memory-map"
+ "Show static carveout breakdown from device tree."
+ "VM_KERN_COUNT_WIRED_STATIC_"
- "VM_KERN_COUNT_STATIC_"

```
