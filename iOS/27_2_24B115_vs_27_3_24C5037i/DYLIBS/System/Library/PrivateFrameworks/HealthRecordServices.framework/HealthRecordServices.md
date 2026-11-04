## HealthRecordServices

> `/System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices`

```diff

-7027.1.56.2.9
-  __TEXT.__text: 0x131930
-  __TEXT.__objc_methlist: 0x604c
-  __TEXT.__const: 0x168ae
-  __TEXT.__cstring: 0x619a
+7027.2.13.0.0
+  __TEXT.__text: 0x133078
+  __TEXT.__objc_methlist: 0x61a4
+  __TEXT.__const: 0x16b1e
+  __TEXT.__cstring: 0x635a
   __TEXT.__oslogstring: 0xd03
-  __TEXT.__gcc_except_tab: 0x164
+  __TEXT.__gcc_except_tab: 0x184
   __TEXT.__ustring: 0x10c
-  __TEXT.__swift5_typeref: 0x29ad
-  __TEXT.__constg_swiftt: 0x3fec
-  __TEXT.__swift5_reflstr: 0x20a9
-  __TEXT.__swift5_fieldmd: 0x544c
+  __TEXT.__swift5_typeref: 0x29dd
+  __TEXT.__constg_swiftt: 0x402c
+  __TEXT.__swift5_reflstr: 0x2109
+  __TEXT.__swift5_fieldmd: 0x549c
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_assocty: 0x548
-  __TEXT.__swift5_proto: 0x1688
-  __TEXT.__swift5_types: 0x66c
+  __TEXT.__swift5_assocty: 0x560
+  __TEXT.__swift5_proto: 0x16ac
+  __TEXT.__swift5_types: 0x674
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift_as_entry: 0x140
   __TEXT.__swift_as_cont: 0x36c

   __TEXT.__swift5_capture: 0x848
   __TEXT.__swift_as_ret: 0x138
   __TEXT.__swift5_acfuncs: 0x28
-  __TEXT.__unwind_info: 0x8410
+  __TEXT.__unwind_info: 0x84d0
   __TEXT.__eh_frame: 0x8e60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1678
-  __DATA_CONST.__objc_classlist: 0x460
+  __DATA_CONST.__const: 0x16c8
+  __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23a8
+  __DATA_CONST.__objc_selrefs: 0x23f0
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0x2b8
+  __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x3c8
-  __DATA_CONST.__got: 0x9e0
-  __AUTH_CONST.__const: 0xd2f8
-  __AUTH_CONST.__cfstring: 0x5940
-  __AUTH_CONST.__objc_const: 0xbea8
+  __DATA_CONST.__got: 0x9f0
+  __AUTH_CONST.__const: 0xd3d8
+  __AUTH_CONST.__cfstring: 0x59e0
+  __AUTH_CONST.__objc_const: 0xc0c8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__auth_got: 0x1110
-  __AUTH.__objc_data: 0x2918
+  __AUTH_CONST.__auth_got: 0x1120
+  __AUTH.__objc_data: 0x29b8
   __AUTH.__data: 0x24e0
-  __DATA.__objc_ivar: 0x5a0
-  __DATA.__data: 0x4ac0
+  __DATA.__objc_ivar: 0x5a8
+  __DATA.__data: 0x4af0
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x570

   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /System/Library/PrivateFrameworks/XPCDistributed.framework/XPCDistributed
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9510
-  Symbols:   5538
-  CStrings:  1161
+  Functions: 9567
+  Symbols:   5598
+  CStrings:  1173
 
Symbols:
+ +[HKMedicalHistoryFHIRSynthesisRequest supportsSecureCoding]
+ +[HKMedicalHistoryFHIRSynthesisResult supportsSecureCoding]
+ -[HDHealthRecordsIngestionServiceClient resolveClinicalHealthLink:error:]
+ -[HDHealthRecordsXPCServiceClient synthesizeMedicalHistoryFHIRWithRequest:completion:]
+ -[HKMedicalHistoryFHIRSynthesisRequest .cxx_destruct]
+ -[HKMedicalHistoryFHIRSynthesisRequest copyWithZone:]
+ -[HKMedicalHistoryFHIRSynthesisRequest encodeWithCoder:]
+ -[HKMedicalHistoryFHIRSynthesisRequest hash]
+ -[HKMedicalHistoryFHIRSynthesisRequest initWithCoder:]
+ -[HKMedicalHistoryFHIRSynthesisRequest initWithRecord:]
+ -[HKMedicalHistoryFHIRSynthesisRequest init]
+ -[HKMedicalHistoryFHIRSynthesisRequest isEqual:]
+ -[HKMedicalHistoryFHIRSynthesisRequest record]
+ -[HKMedicalHistoryFHIRSynthesisResult .cxx_destruct]
+ -[HKMedicalHistoryFHIRSynthesisResult FHIRResource]
+ -[HKMedicalHistoryFHIRSynthesisResult copyWithZone:]
+ -[HKMedicalHistoryFHIRSynthesisResult encodeWithCoder:]
+ -[HKMedicalHistoryFHIRSynthesisResult hash]
+ -[HKMedicalHistoryFHIRSynthesisResult initWithCoder:]
+ -[HKMedicalHistoryFHIRSynthesisResult initWithFHIRResource:]
+ -[HKMedicalHistoryFHIRSynthesisResult init]
+ -[HKMedicalHistoryFHIRSynthesisResult isEqual:]
+ _OBJC_CLASS_$_HKFHIRResource
+ _OBJC_CLASS_$_HKMedicalHistoryFHIRSynthesisRequest
+ _OBJC_CLASS_$_HKMedicalHistoryFHIRSynthesisResult
+ _OBJC_CLASS_$_HKMedicalHistoryRecord
+ _OBJC_IVAR_$_HKMedicalHistoryFHIRSynthesisRequest._record
+ _OBJC_IVAR_$_HKMedicalHistoryFHIRSynthesisResult._FHIRResource
+ _OBJC_METACLASS_$_HKMedicalHistoryFHIRSynthesisRequest
+ _OBJC_METACLASS_$_HKMedicalHistoryFHIRSynthesisResult
+ __OBJC_$_CLASS_METHODS_HKMedicalHistoryFHIRSynthesisRequest
+ __OBJC_$_CLASS_METHODS_HKMedicalHistoryFHIRSynthesisResult
+ __OBJC_$_CLASS_PROP_LIST_HKMedicalHistoryFHIRSynthesisRequest
+ __OBJC_$_CLASS_PROP_LIST_HKMedicalHistoryFHIRSynthesisResult
+ __OBJC_$_INSTANCE_METHODS_HKMedicalHistoryFHIRSynthesisRequest
+ __OBJC_$_INSTANCE_METHODS_HKMedicalHistoryFHIRSynthesisResult
+ __OBJC_$_INSTANCE_VARIABLES_HKMedicalHistoryFHIRSynthesisRequest
+ __OBJC_$_INSTANCE_VARIABLES_HKMedicalHistoryFHIRSynthesisResult
+ __OBJC_$_PROP_LIST_HKMedicalHistoryFHIRSynthesisRequest
+ __OBJC_$_PROP_LIST_HKMedicalHistoryFHIRSynthesisResult
+ __OBJC_CLASS_PROTOCOLS_$_HKMedicalHistoryFHIRSynthesisRequest
+ __OBJC_CLASS_PROTOCOLS_$_HKMedicalHistoryFHIRSynthesisResult
+ __OBJC_CLASS_RO_$_HKMedicalHistoryFHIRSynthesisRequest
+ __OBJC_CLASS_RO_$_HKMedicalHistoryFHIRSynthesisResult
+ __OBJC_METACLASS_RO_$_HKMedicalHistoryFHIRSynthesisRequest
+ __OBJC_METACLASS_RO_$_HKMedicalHistoryFHIRSynthesisResult
+ ___73-[HDHealthRecordsIngestionServiceClient resolveClinicalHealthLink:error:]_block_invoke
+ ___73-[HDHealthRecordsIngestionServiceClient resolveClinicalHealthLink:error:]_block_invoke_2
+ ___73-[HDHealthRecordsIngestionServiceClient resolveClinicalHealthLink:error:]_block_invoke_3
+ ___86-[HDHealthRecordsXPCServiceClient synthesizeMedicalHistoryFHIRWithRequest:completion:]_block_invoke
+ ___86-[HDHealthRecordsXPCServiceClient synthesizeMedicalHistoryFHIRWithRequest:completion:]_block_invoke_2
+ ___block_descriptor_48_e8_32r40r_e52_v24?0"HKSMARTHealthLinkParsingResult"8"NSError"16lr32l8r40l8
+ ___block_descriptor_56_e8_32s40r48r_e52_v16?0"<HDHealthRecordsIngestionServiceInterface>"8ls32l8r40l8r48l8
+ _associated conformance 20HealthRecordServices08ClinicalA19LinkResolutionErrorO10Foundation09LocalizedG0AAs0G0
+ _associated conformance 20HealthRecordServices08ClinicalA19LinkResolutionErrorO10Foundation13CustomNSErrorAAs0G0
+ _associated conformance 20HealthRecordServices08ClinicalA19LinkResolutionErrorOSHAASQ
+ _associated conformance 20HealthRecordServices19TextExtractionErrorO29RecognitionTimedOutCodingKeys33_8D7B5D0208F771943343F43AA2D3B8BELLOs0J3KeyAAs23CustomStringConvertible
+ _associated conformance 20HealthRecordServices19TextExtractionErrorO29RecognitionTimedOutCodingKeys33_8D7B5D0208F771943343F43AA2D3B8BELLOs0J3KeyAAs28CustomDebugStringConvertible
+ _symbolic _____ 20HealthRecordServices08ClinicalA19LinkResolutionErrorO
+ _symbolic _____ 20HealthRecordServices19TextExtractionErrorO29RecognitionTimedOutCodingKeys33_8D7B5D0208F771943343F43AA2D3B8BELLO
CStrings:
+ "FHIRResource"
+ "Record"
+ "The HTML document content is not valid UTF-8"
+ "The HTML document has no content"
+ "The SMART Health Link is no longer valid"
+ "The SMART Health Link passcode was rejected"
+ "The docx file has no text"
+ "com.apple.health.records.ClinicalHealthLinkResolution"
+ "labkit-shl-1.multidev.apple.com"
+ "recognitionTimedOut"
+ "text recognition did not finish in time"
+ "v24@?0@\"HKSMARTHealthLinkParsingResult\"8@\"NSError\"16"
```
