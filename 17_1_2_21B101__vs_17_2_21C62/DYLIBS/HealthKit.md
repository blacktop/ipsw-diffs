## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-4146.1.11.3.0
-  __TEXT.__text: 0x26a5b8
+4146.2.12.1.3
+  __TEXT.__text: 0x26b2e0
   __TEXT.__auth_stubs: 0x2500
-  __TEXT.__objc_methlist: 0x278b4
-  __TEXT.__cstring: 0x2b779
+  __TEXT.__objc_methlist: 0x27a64
+  __TEXT.__cstring: 0x2b859
   __TEXT.__const: 0x4070
   __TEXT.__oslogstring: 0xb079
   __TEXT.__gcc_except_tab: 0x3684

   __TEXT.__swift5_types: 0x124
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xc6d0
+  __TEXT.__unwind_info: 0xc710
   __TEXT.__eh_frame: 0x1278
-  __TEXT.__objc_classname: 0x774d
-  __TEXT.__objc_methname: 0x54920
-  __TEXT.__objc_methtype: 0xb19d
-  __TEXT.__objc_stubs: 0x271e0
+  __TEXT.__objc_classname: 0x7780
+  __TEXT.__objc_methname: 0x54b6a
+  __TEXT.__objc_methtype: 0xb1d6
+  __TEXT.__objc_stubs: 0x272c0
   __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0xd970
-  __DATA_CONST.__objc_classlist: 0x1798
+  __DATA_CONST.__const: 0xd9d0
+  __DATA_CONST.__objc_classlist: 0x17a8
   __DATA_CONST.__objc_catlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x720
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x35728
-  __DATA_CONST.__objc_selrefs: 0xf8f8
+  __DATA_CONST.__objc_const: 0x358f8
+  __DATA_CONST.__objc_selrefs: 0xf958
   __DATA_CONST.__objc_arraydata: 0x6688
-  __AUTH_CONST.__cfstring: 0x2d580
-  __AUTH_CONST.__objc_const: 0x17640
+  __AUTH_CONST.__cfstring: 0x2d640
+  __AUTH_CONST.__objc_const: 0x17760
   __AUTH_CONST.__const: 0x5e80
   __AUTH_CONST.__objc_intobj: 0x42f0
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x100
   __AUTH_CONST.__objc_arrayobj: 0x600
   __AUTH_CONST.__auth_got: 0x1298
-  __AUTH.__objc_data: 0xcbd8
+  __AUTH.__objc_data: 0xcc78
   __AUTH.__data: 0xd20
   __DATA.__got_weak: 0x8
   __DATA.__objc_protorefs: 0x570
-  __DATA.__objc_classrefs: 0x1648
-  __DATA.__objc_superrefs: 0x1558
-  __DATA.__objc_ivar: 0x29d0
+  __DATA.__objc_classrefs: 0x1658
+  __DATA.__objc_superrefs: 0x1560
+  __DATA.__objc_ivar: 0x29ec
   __DATA.__data: 0x9b20
   __DATA.__bss: 0x53e0
   __DATA.__common: 0x940

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: CFA92F68-0B26-3CF6-B1AF-2A16E04242A8
-  Functions: 18391
-  Symbols:   52671
-  CStrings:  26858
+  UUID: 63950E10-6E0A-34B2-A2B7-B538ACD1B45D
+  Functions: 18429
+  Symbols:   52783
+  CStrings:  26894
 
Symbols:
+ +[HKMedicalIDSyncRequest supportsSecureCoding]
+ +[HKSummarySharingSyncRequest supportsSecureCoding]
+ -[HKCloudSyncRequest allowCellular]
+ -[HKCloudSyncRequest medicalIDSyncRequest]
+ -[HKCloudSyncRequest qualityOfService]
+ -[HKCloudSyncRequest requestWithMedicalIDSyncRequest:]
+ -[HKCloudSyncRequest requestWithSummarySharingSyncRequest:]
+ -[HKCloudSyncRequest setAllowCellular:]
+ -[HKCloudSyncRequest setMedicalIDSyncRequest:]
+ -[HKCloudSyncRequest setQualityOfService:]
+ -[HKCloudSyncRequest setSummarySharingSyncRequest:]
+ -[HKCloudSyncRequest summarySharingSyncRequest]
+ -[HKConceptStore fetchConceptIndexerStateWithCompletion:]
+ -[HKHealthRecordsStore fetchCurrentIngestionStateWithCompletion:]
+ -[HKMedicalIDSyncRequest copyWithZone:]
+ -[HKMedicalIDSyncRequest description]
+ -[HKMedicalIDSyncRequest encodeWithCoder:]
+ -[HKMedicalIDSyncRequest initWithCoder:]
+ -[HKMedicalIDSyncRequest isEqual:]
+ -[HKMedicalIDSyncRequest mergeWithRequest:]
+ -[HKStateSyncRequest isEqual:]
+ -[HKSummarySharingSyncRequest copyWithZone:]
+ -[HKSummarySharingSyncRequest description]
+ -[HKSummarySharingSyncRequest encodeWithCoder:]
+ -[HKSummarySharingSyncRequest initWithCoder:]
+ -[HKSummarySharingSyncRequest initWithPush:pull:]
+ -[HKSummarySharingSyncRequest isEqual:]
+ -[HKSummarySharingSyncRequest mergeWithRequest:]
+ -[HKSummarySharingSyncRequest pull]
+ -[HKSummarySharingSyncRequest push]
+ -[_HKBehavior setShouldOverrideSiriUOD:]
+ -[_HKBehavior shouldOverrideSiriUOD]
+ GCC_except_table244
+ GCC_except_table245
+ _HKProductTypePrefixVisionPro
+ _OBJC_CLASS_$_HKMedicalIDSyncRequest
+ _OBJC_CLASS_$_HKSummarySharingSyncRequest
+ _OBJC_IVAR_$_HKCloudSyncRequest._allowCellular
+ _OBJC_IVAR_$_HKCloudSyncRequest._medicalIDSyncRequest
+ _OBJC_IVAR_$_HKCloudSyncRequest._qualityOfService
+ _OBJC_IVAR_$_HKCloudSyncRequest._summarySharingSyncRequest
+ _OBJC_IVAR_$_HKSummarySharingSyncRequest._pull
+ _OBJC_IVAR_$_HKSummarySharingSyncRequest._push
+ _OBJC_IVAR_$__HKBehavior._shouldOverrideSiriUOD
+ _OBJC_METACLASS_$_HKMedicalIDSyncRequest
+ _OBJC_METACLASS_$_HKSummarySharingSyncRequest
+ __OBJC_$_CLASS_METHODS_HKMedicalIDSyncRequest
+ __OBJC_$_CLASS_METHODS_HKSummarySharingSyncRequest
+ __OBJC_$_CLASS_PROP_LIST_HKMedicalIDSyncRequest
+ __OBJC_$_CLASS_PROP_LIST_HKSummarySharingSyncRequest
+ __OBJC_$_INSTANCE_METHODS_HKMedicalIDSyncRequest
+ __OBJC_$_INSTANCE_METHODS_HKSummarySharingSyncRequest
+ __OBJC_$_INSTANCE_VARIABLES_HKSummarySharingSyncRequest
+ __OBJC_$_PROP_LIST_HKSummarySharingSyncRequest
+ __OBJC_CLASS_PROTOCOLS_$_HKMedicalIDSyncRequest
+ __OBJC_CLASS_PROTOCOLS_$_HKSummarySharingSyncRequest
+ __OBJC_CLASS_RO_$_HKMedicalIDSyncRequest
+ __OBJC_CLASS_RO_$_HKSummarySharingSyncRequest
+ __OBJC_METACLASS_RO_$_HKMedicalIDSyncRequest
+ __OBJC_METACLASS_RO_$_HKSummarySharingSyncRequest
+ ___57-[HKConceptStore fetchConceptIndexerStateWithCompletion:]_block_invoke
+ ___57-[HKConceptStore fetchConceptIndexerStateWithCompletion:]_block_invoke_2
+ ___57-[HKConceptStore fetchConceptIndexerStateWithCompletion:]_block_invoke_3
+ ___65-[HKHealthRecordsStore fetchCurrentIngestionStateWithCompletion:]_block_invoke
+ ___65-[HKHealthRecordsStore fetchCurrentIngestionStateWithCompletion:]_block_invoke_2
+ ___65-[HKHealthRecordsStore fetchCurrentIngestionStateWithCompletion:]_block_invoke_3
+ ___block_descriptor_40_e8_32bs_e8_v16?0Q8ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v16?0q8ls32l8
+ __unnamed_array_storage.1007
+ __unnamed_array_storage.772
+ __unnamed_array_storage.985
+ __unnamed_array_storage.986
+ _kHKComAppleMomentsdBundleId
+ _objc_msgSend$allowCellular
+ _objc_msgSend$medicalIDSyncRequest
+ _objc_msgSend$qualityOfService
+ _objc_msgSend$setAllowCellular:
+ _objc_msgSend$setMedicalIDSyncRequest:
+ _objc_msgSend$setSummarySharingSyncRequest:
+ _objc_msgSend$summarySharingSyncRequest
- GCC_except_table242
- GCC_except_table243
- __unnamed_array_storage.1003
- __unnamed_array_storage.1004
- __unnamed_array_storage.769
- __unnamed_array_storage.982
- __unnamed_array_storage.983
CStrings:
+ "<%@:%p %@\n| Changes Sync Request: %@\n| Context Sync Request: %@\n| State Sync Request: %@\n| Medical ID Sync Request: %@\n| Summary Sharing Sync Request: %@\n| Allow Cellular: %d\n| Quality of Service: %ld\n"
+ "@\"HKMedicalIDSyncRequest\""
+ "@\"HKSummarySharingSyncRequest\""
+ "HKMedicalIDSyncRequest"
+ "HKSummarySharingSyncRequest"
+ "RealityDevice"
+ "T@\"HKMedicalIDSyncRequest\",C,N,V_medicalIDSyncRequest"
+ "T@\"HKSummarySharingSyncRequest\",C,N,V_summarySharingSyncRequest"
+ "TB,N,V_allowCellular"
+ "TB,N,V_shouldOverrideSiriUOD"
+ "_allowCellular"
+ "_medicalIDSyncRequest"
+ "_shouldOverrideSiriUOD"
+ "_summarySharingSyncRequest"
+ "allowCellular"
+ "com.apple.momentsd"
+ "fetchConceptIndexerStateWithCompletion:"
+ "fetchCurrentIngestionStateWithCompletion:"
+ "medicalIDSyncRequest"
+ "requestWithMedicalIDSyncRequest:"
+ "requestWithSummarySharingSyncRequest:"
+ "setAllowCellular:"
+ "setMedicalIDSyncRequest:"
+ "setShouldOverrideSiriUOD:"
+ "setSummarySharingSyncRequest:"
+ "shouldOverrideSiriUOD"
+ "summarySharingSyncRequest"
- "<%@:%p %@\n| Changes Sync Request: %@\n| Context Sync Request: %@\n| State Sync Request: %@\n"

```
