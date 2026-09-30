## mlhostd

> `/usr/libexec/mlhostd`

```diff

-3.2.8.0.0
-  __TEXT.__text: 0x475d8
-  __TEXT.__auth_stubs: 0x1980
+3.2.14.0.0
+  __TEXT.__text: 0x3ddd0
+  __TEXT.__auth_stubs: 0x19b0
   __TEXT.__objc_methlist: 0x38
   __TEXT.__const: 0xbd4
-  __TEXT.__cstring: 0x985b
+  __TEXT.__cstring: 0x977b
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x2cc
-  __TEXT.__swift5_typeref: 0x665
+  __TEXT.__swift5_typeref: 0x657
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_reflstr: 0x2b5
   __TEXT.__swift5_fieldmd: 0x2e0
   __TEXT.__swift5_assocty: 0xd8
   __TEXT.__swift5_proto: 0x90
   __TEXT.__swift5_types: 0x40
-  __TEXT.__objc_methname: 0xabb
-  __TEXT.__oslogstring: 0x1e0a
+  __TEXT.__objc_methname: 0xb03
+  __TEXT.__oslogstring: 0x1f5a
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0x342
-  __TEXT.__swift5_capture: 0x1c4
+  __TEXT.__swift5_capture: 0x110
   __TEXT.__info_plist: 0x576
-  __TEXT.__unwind_info: 0x7c0
-  __TEXT.__eh_frame: 0x1030
-  __DATA_CONST.__auth_got: 0xcc0
-  __DATA_CONST.__got: 0x458
-  __DATA_CONST.__auth_ptr: 0x418
-  __DATA_CONST.__const: 0x4f60
+  __TEXT.__unwind_info: 0x700
+  __TEXT.__eh_frame: 0xc98
+  __DATA_CONST.__auth_got: 0xcd8
+  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__auth_ptr: 0x428
+  __DATA_CONST.__const: 0x4d80
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA.__objc_const: 0xac8
-  __DATA.__objc_selrefs: 0x2d0
+  __DATA.__objc_selrefs: 0x2e8
   __DATA.__objc_data: 0x170
-  __DATA.__data: 0xa78
+  __DATA.__data: 0xa58
   __DATA.__bss: 0x1200
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 592
-  Symbols:   661
-  CStrings:  1526
+  Functions: 546
+  Symbols:   674
+  CStrings:  1531
 
Symbols:
+ _$s20LighthouseBackground10MLHostTaskVs23CustomStringConvertibleAAMc
+ _$s20LighthouseBackground11TaskRequestV09getSystemcD010identifierSo08BGSystemcD0CSgSS_tF
+ _$s20LighthouseBackground11TaskRequestV19relatedApplicationsSaySSGSgvg
+ _$s20LighthouseBackground11TaskRequestV19relatedApplicationsSaySSGSgvs
+ _$s20LighthouseBackground11TaskRequestVMa
+ _$s20LighthouseBackground11TaskRequestVMn
+ _$s20LighthouseBackground13OnDemandErrorO010schedulingE0yA2CmFWC
+ _$s20LighthouseBackground13OnDemandErrorO11taskInvalidyA2CmFWC
+ _$s20LighthouseBackground13OnDemandErrorO11taskPendingyA2CmFWC
+ _$s20LighthouseBackground13OnDemandErrorO11taskRunningyA2CmFWC
+ _$s20LighthouseBackground13OnDemandErrorO18clientUnauthorizedyA2CmFWC
+ _$s20LighthouseBackground13OnDemandErrorOMa
+ _$s20LighthouseBackground14OnDemandResultO13taskScheduledyA2CmFWC
+ _$s20LighthouseBackground14OnDemandResultOMa
+ _$s20LighthouseBackground14TaskDefinitionV11taskRequestAA0cF0VSgvM
+ _$s20LighthouseBackground14TaskDefinitionV11taskRequestAA0cF0VSgvg
+ _$s20LighthouseBackground14TaskDefinitionV8criteriaAA19XPCActivityCriteriaVSgvM
+ _$s20LighthouseBackground14TaskDefinitionV8criteriaAA19XPCActivityCriteriaVSgvg
+ _$s20LighthouseBackground19XPCActivityCriteriaVMn
+ _$s20LighthouseBackground30GetOnDemandTaskRequestResponseV5errorAcA0dE5ErrorO_tcfC
+ _$s20LighthouseBackground30GetOnDemandTaskRequestResponseV6resultAcA0dE6ResultO_tcfC
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _swift_setDeallocating
- _$s10Foundation4DateV1poiyA2C_SdtFZ
- _$s20LighthouseBackground10MLHostTaskV17lastExecutionDate10Foundation0G0VSgvg
- _$s20LighthouseBackground10MLHostTaskV21expectedExecutionDate10Foundation0G0VSgvs
- _$s20LighthouseBackground14TaskDefinitionV8criteriaAA19XPCActivityCriteriaVvM
- _$s20LighthouseBackground14TaskDefinitionV8criteriaAA19XPCActivityCriteriaVvg
- _$s20LighthouseBackground19XPCActivityCriteriaV8intervals5Int64Vvg
- _$s20LighthouseBackground30GetOnDemandTaskRequestResponseV6result7messageACSb_SStcfC
- _$sSa28_allocateBufferUninitialized15minimumCapacitys06_ArrayB0VyxGSi_tFZ
- _$ss22_minimumMergeRunLengthyS2iF
- _objc_retain_x27
CStrings:
+ "Client not authorized for onDemand requests."
+ "Deregistering task: %!s(MISSING)"
+ "Failed at generating BGSystemTaskRequest from taskDefinition: %!s(MISSING)"
+ "Failed at scheduling ondemand task: %!s(MISSING)"
+ "Found existing running task: %!s(MISSING)"
+ "Found existing taskRequest: %!@(MISSING)"
+ "Invalid taskName for onDemand request: %!s(MISSING)"
+ "Task cancellation failed: %!@(MISSING)"
+ "Task deregistered successfully: %!s(MISSING)"
+ "deregisterActivities"
+ "deregisterTaskWithIdentifier:"
+ "setScheduleAfter:"
+ "setTrySchedulingBefore:"
- "Can't construct Array with count < 0"
- "Process not allowed to request on-demand task!"
- "Swift/Array.swift"
- "Task already running."
- "Task unregistration failed: %!@(MISSING)"
- "Unregistering task: %!s(MISSING)"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "unregisterActivities"

```
