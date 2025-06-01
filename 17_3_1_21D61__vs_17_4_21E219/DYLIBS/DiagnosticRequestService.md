## DiagnosticRequestService

> `/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService`

```diff

-308.80.4.0.0
-  __TEXT.__text: 0x67b34
+316.100.13.0.0
+  __TEXT.__text: 0x67c24
   __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_methlist: 0x4684
-  __TEXT.__const: 0xcd8
+  __TEXT.__objc_methlist: 0x46b4
+  __TEXT.__const: 0xcf8
   __TEXT.__gcc_except_tab: 0x84c
-  __TEXT.__cstring: 0x4f2f
-  __TEXT.__oslogstring: 0xa69b
+  __TEXT.__cstring: 0x4f5f
+  __TEXT.__oslogstring: 0xa6b3
   __TEXT.__swift5_typeref: 0x278
   __TEXT.__constg_swiftt: 0x24c
   __TEXT.__swift5_fieldmd: 0x240

   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1ad8
+  __TEXT.__unwind_info: 0x1b30
   __TEXT.__eh_frame: 0x440
   __TEXT.__objc_classname: 0x975
-  __TEXT.__objc_methname: 0xa64b
+  __TEXT.__objc_methname: 0xa6fb
   __TEXT.__objc_methtype: 0x10b9
-  __TEXT.__objc_stubs: 0x7960
+  __TEXT.__objc_stubs: 0x7a40
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x1240
+  __DATA_CONST.__const: 0x1278
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x6850
-  __DATA_CONST.__objc_selrefs: 0x2298
-  __AUTH_CONST.__cfstring: 0x4d60
+  __DATA_CONST.__objc_selrefs: 0x22d0
+  __DATA_CONST.__objc_classrefs: 0x3c0
+  __DATA_CONST.__objc_superrefs: 0x1f8
+  __AUTH_CONST.__cfstring: 0x4dc0
   __AUTH_CONST.__objc_const: 0x23f8
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__const: 0x1030
+  __AUTH_CONST.__const: 0x1050
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x798
   __AUTH.__objc_data: 0x5e8
   __AUTH.__data: 0x300
-  __DATA.__objc_classrefs: 0x3b8
-  __DATA.__objc_superrefs: 0x1f8
   __DATA.__objc_ivar: 0x428
   __DATA.__objc_data: 0x48
-  __DATA.__data: 0x6f8
+  __DATA.__data: 0x6b8
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x15d0
+  __DATA.__bss: 0x15e0
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x1580
   __DATA_DIRTY.__data: 0xe0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8C288B03-F3EB-3307-BAF6-84D165A4B33F
-  Functions: 2351
-  Symbols:   6530
-  CStrings:  4340
+  UUID: 15316B87-0FA3-3C4F-8184-61338ED11F26
+  Functions: 2356
+  Symbols:   6554
+  CStrings:  4355
 
Symbols:
+ +[DRSDampeningConfiguration ppsCEArchiveConfiguration]
+ +[DRSDampeningConfiguration ppsXCArchiveConfiguration]
+ +[DRSSubmitLogToCKContainerRequest(CKRecord_Private) xcRecordZoneID]
+ -[DRSSubmitLogToCKContainerRequest(CKRecord_Private) zoneID]
+ GCC_except_table112
+ GCC_except_table142
+ GCC_except_table153
+ GCC_except_table157
+ GCC_except_table160
+ GCC_except_table71
+ GCC_except_table78
+ GCC_except_table81
+ _OBJC_CLASS_$_CKRecordZone
+ ___109-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:completionHandler:]_block_invoke.217
+ ___109-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:completionHandler:]_block_invoke.218
+ ___109-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:completionHandler:]_block_invoke.222
+ ___51-[DRSTeamDampeningConfiguration initWithPlistDict:]_block_invoke.329
+ ___60-[DRSService _registerPermissiveExpeditedUploadXPCActivity:]_block_invoke.184
+ ___63-[DRSDampeningManager _ON_MOC_QUEUE_moRepresentationInContext:]_block_invoke.459
+ ___68+[DRSSubmitLogToCKContainerRequest(CKRecord_Private) xcRecordZoneID]_block_invoke
+ ___87+[DRSDampeningManager dampeningManagerFromPersistentContainer:deleteBadState:errorOut:]_block_invoke.454
+ ___block_descriptor_57_e8_32s40s48s_e21_v20?0B8"NSString"12ls32l8s40l8s48l8
+ ___block_literal_global.205
+ ___block_literal_global.207
+ ___block_literal_global.215
+ ___block_literal_global.361
+ _kDRSDMPPSCEArchiveIssueCategory
+ _kDRSDMPPSXCArchiveIssueCategory
+ _kDRTriggerUpload_isAsync
+ _objc_msgSend$initWithRecordType:zoneID:
+ _objc_msgSend$initWithZoneName:
+ _objc_msgSend$ppsCEArchiveConfiguration
+ _objc_msgSend$ppsXCArchiveConfiguration
+ _objc_msgSend$setAllowsExpensiveNetworkAccess:
+ _objc_msgSend$setXPCActivity:
+ _objc_msgSend$xcRecordZoneID
+ _objc_msgSend$zoneID
+ _xcRecordZoneID.kRecordZone
+ _xcRecordZoneID.onceToken
- GCC_except_table110
- GCC_except_table140
- GCC_except_table149
- GCC_except_table155
- GCC_except_table158
- GCC_except_table69
- GCC_except_table75
- GCC_except_table79
- ___109-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:completionHandler:]_block_invoke.208
- ___109-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:completionHandler:]_block_invoke.209
- ___109-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:completionHandler:]_block_invoke.213
- ___51-[DRSTeamDampeningConfiguration initWithPlistDict:]_block_invoke.321
- ___60-[DRSService _registerPermissiveExpeditedUploadXPCActivity:]_block_invoke.178
- ___63-[DRSDampeningManager _ON_MOC_QUEUE_moRepresentationInContext:]_block_invoke.451
- ___87+[DRSDampeningManager dampeningManagerFromPersistentContainer:deleteBadState:errorOut:]_block_invoke.446
- ___block_descriptor_56_e8_32s40s48s_e21_v20?0B8"NSString"12ls32l8s40l8s48l8
- ___block_literal_global.198
- ___block_literal_global.206
- ___block_literal_global.352
- ___block_literal_global.56
- ___block_literal_global.62
- _objc_msgSend$setXpcActivity:
CStrings:
+ "3pDevEngagement"
+ "T@\"NSString\",?,R,C"
+ "Triggering CK work due to request from [%d]. Expedited:%@, Async:%@"
+ "ce-archive"
+ "initWithRecordType:zoneID:"
+ "initWithZoneName:"
+ "isAsync"
+ "ppsCEArchiveConfiguration"
+ "ppsXCArchiveConfiguration"
+ "setAllowsExpensiveNetworkAccess:"
+ "setXPCActivity:"
+ "xc-archive"
+ "xcRecordZoneID"
+ "zoneID"
- "Triggering CK work due to request from [%d]"
- "setXpcActivity:"

```
