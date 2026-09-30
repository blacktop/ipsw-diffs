## IntelligenceFlowContextRuntime

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime`

```diff

-193.0.5.0.0
-  __TEXT.__text: 0x62a1c
-  __TEXT.__auth_stubs: 0x2800
-  __TEXT.__objc_methlist: 0x4a0
-  __TEXT.__const: 0x19f0
-  __TEXT.__cstring: 0x15b1
-  __TEXT.__swift5_typeref: 0x1697
-  __TEXT.__swift5_fieldmd: 0x848
-  __TEXT.__constg_swiftt: 0xd7c
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x6a7
-  __TEXT.__swift5_assocty: 0x128
+197.0.6.0.0
+  __TEXT.__text: 0x6aaac
+  __TEXT.__auth_stubs: 0x2a40
+  __TEXT.__objc_methlist: 0x4b0
+  __TEXT.__const: 0x1b50
+  __TEXT.__cstring: 0x17e1
+  __TEXT.__swift5_typeref: 0x1805
+  __TEXT.__swift5_fieldmd: 0x964
+  __TEXT.__constg_swiftt: 0xea4
+  __TEXT.__swift5_builtin: 0xb4
+  __TEXT.__swift5_reflstr: 0x777
+  __TEXT.__swift5_assocty: 0x140
   __TEXT.__swift5_protos: 0x34
-  __TEXT.__swift5_proto: 0x134
-  __TEXT.__swift5_types: 0xb8
-  __TEXT.__oslogstring: 0xd48
-  __TEXT.__swift_as_entry: 0xf4
-  __TEXT.__swift_as_ret: 0xf0
-  __TEXT.__swift5_capture: 0x3cc
+  __TEXT.__swift5_proto: 0x144
+  __TEXT.__swift5_types: 0xd8
+  __TEXT.__oslogstring: 0xdf8
+  __TEXT.__swift_as_entry: 0x120
+  __TEXT.__swift_as_ret: 0x114
+  __TEXT.__swift5_capture: 0x41c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x1380
-  __TEXT.__eh_frame: 0x3168
+  __TEXT.__unwind_info: 0x1538
+  __TEXT.__eh_frame: 0x3638
   __TEXT.__objc_classname: 0x75
-  __TEXT.__objc_methname: 0x1085
+  __TEXT.__objc_methname: 0x10d7
   __TEXT.__objc_methtype: 0x470
   __TEXT.__objc_stubs: 0x1e0
-  __DATA_CONST.__got: 0x830
-  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__got: 0x878
+  __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x630
+  __DATA_CONST.__objc_selrefs: 0x648
   __DATA_CONST.__objc_protorefs: 0x40
-  __AUTH_CONST.__auth_got: 0x1408
-  __AUTH_CONST.__auth_ptr: 0x8b8
-  __AUTH_CONST.__const: 0x14b0
+  __AUTH_CONST.__auth_got: 0x1528
+  __AUTH_CONST.__auth_ptr: 0x910
+  __AUTH_CONST.__const: 0x1718
   __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__objc_const: 0x15c0
+  __AUTH_CONST.__objc_const: 0x15c8
   __AUTH.__objc_data: 0x1c8
-  __AUTH.__data: 0x5a8
-  __DATA.__data: 0xaf0
+  __AUTH.__data: 0x628
+  __DATA.__data: 0xbe8
   __DATA.__bss: 0xe20
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__data: 0x12c0
+  __DATA_DIRTY.__data: 0x1530
   __DATA_DIRTY.__bss: 0x680
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1804
-  Symbols:   257
-  CStrings:  464
+  Functions: 1950
+  Symbols:   259
+  CStrings:  476
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_getErrorValue
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
CStrings:
+ "Collection failed or was incomplete for the following ContextTypes: %s"
+ "Detects and identifies the point of interest that the user is currently in."
+ "IFCR.ContextRetriever.retrieveContextValuesWithFailures(contextTypes:failedTypes:)"
+ "Identifies personalized locations based on the user's routine. It differentiates between frequently visited places like home, work, gym, school, or other undefined locations."
+ "Recognizes and captures app entities that appear on the user's screen."
+ "Unable to retrieve context for %s due to %s"
+ "category"
+ "could not get POI category for %s"
+ "could not get preferred name for %s"
+ "retrieveContextValuesWithFailures(contextTypes:timeout:)"
+ "retrieveContextValuesWithFailures(contextTypes:timeout:with:)"
+ "retrieveContextValuesWithFailuresWithContextTypes:timeout:with:"
+ "userType"
- "timed out while retrieving context for %s"

```
