## DiagnosticRequestService

> `/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService`

```diff

-411.80.3.0.0
-  __TEXT.__text: 0x6be34
-  __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_methlist: 0x4d5c
-  __TEXT.__const: 0xdf0
-  __TEXT.__gcc_except_tab: 0xc00
-  __TEXT.__cstring: 0x568f
-  __TEXT.__oslogstring: 0xbd2a
+411.100.13.0.0
+  __TEXT.__text: 0x70a30
+  __TEXT.__auth_stubs: 0xed0
+  __TEXT.__objc_methlist: 0x4d6c
+  __TEXT.__const: 0xe08
+  __TEXT.__gcc_except_tab: 0xba8
+  __TEXT.__cstring: 0x551f
+  __TEXT.__oslogstring: 0xbe60
   __TEXT.__swift5_typeref: 0x278
   __TEXT.__constg_swiftt: 0x24c
   __TEXT.__swift5_fieldmd: 0x240

   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1728
-  __TEXT.__eh_frame: 0x4b0
-  __TEXT.__objc_classname: 0x978
-  __TEXT.__objc_methname: 0xb550
-  __TEXT.__objc_methtype: 0x111d
-  __TEXT.__objc_stubs: 0x8580
-  __DATA_CONST.__got: 0x430
-  __DATA_CONST.__const: 0x1358
+  __TEXT.__unwind_info: 0x1b00
+  __TEXT.__eh_frame: 0x450
+  __TEXT.__objc_classname: 0xa62
+  __TEXT.__objc_methname: 0xb5d4
+  __TEXT.__objc_methtype: 0x116b
+  __TEXT.__objc_stubs: 0x8620
+  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__const: 0x1340
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2688
+  __DATA_CONST.__objc_selrefs: 0x26a0
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__auth_got: 0x7c0
-  __AUTH_CONST.__const: 0xf30
-  __AUTH_CONST.__cfstring: 0x55e0
+  __AUTH_CONST.__auth_got: 0x778
+  __AUTH_CONST.__const: 0xf50
+  __AUTH_CONST.__cfstring: 0x5620
   __AUTH_CONST.__objc_const: 0x8a58
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x20

   __DATA.__objc_ivar: 0x454
   __DATA.__data: 0x750
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x1050
+  __DATA.__bss: 0x1060
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x1618
-  __DATA_DIRTY.__data: 0x448
+  __DATA_DIRTY.__data: 0x450
   __DATA_DIRTY.__bss: 0x950
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6D8486AB-8D6B-30EF-A7DE-01F457DD2ED0
-  Functions: 2464
-  Symbols:   7166
-  CStrings:  4727
+  UUID: 40806E08-8252-3C84-B627-3D1BDF562A4A
+  Functions: 2477
+  Symbols:   7198
+  CStrings:  4735
 
Symbols:
+ +[DRSDampeningConfiguration ppsAppleCareConfiguration]
+ +[DRSSubmitLogToCKContainerRequest(CKRecord_Private) appleCareArchiveZoneID]
+ +[DRSSubmitLogToCKContainerRequest(CKRecord_Private) appleCareArchiveZoneID].cold.1
+ GCC_except_table170
+ GCC_except_table179
+ GCC_except_table181
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table59
+ GCC_except_table82
+ GCC_except_table85
+ GCC_except_table89
+ GCC_except_table99
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ ___116-[DRSService _ckQueueDownstreamOnly_uploadInFlightWithTransaction:xpcActivity:ckHelper:isExpedited:completionBlock:]_block_invoke.104
+ ___116-[DRSService _ckQueueDownstreamOnly_uploadInFlightWithTransaction:xpcActivity:ckHelper:isExpedited:completionBlock:]_block_invoke.121
+ ___125-[DRSService _ckQueueOnly_submitOutstandingEnableDataGatheringQueriesWithTransaction:xpcActivity:ckHelper:followupWorkBlock:]_block_invoke.147
+ ___136-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:backingPersistentContainer:completionHandler:]_block_invoke.244
+ ___136-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:backingPersistentContainer:completionHandler:]_block_invoke.245
+ ___136-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:backingPersistentContainer:completionHandler:]_block_invoke.249
+ ___51-[DRSTeamDampeningConfiguration initWithPlistDict:]_block_invoke.434
+ ___63-[DRSDampeningManager _ON_MOC_QUEUE_moRepresentationInContext:]_block_invoke.564
+ ___76+[DRSSubmitLogToCKContainerRequest(CKRecord_Private) appleCareArchiveZoneID]_block_invoke
+ ___87+[DRSDampeningManager dampeningManagerFromPersistentContainer:deleteBadState:errorOut:]_block_invoke.559
+ ___block_literal_global.106
+ ___block_literal_global.142
+ ___block_literal_global.228
+ ___block_literal_global.230
+ ___block_literal_global.238
+ ___block_literal_global.392
+ ___block_literal_global.73
+ _appleCareArchiveZoneID.appleCareArchiveZone
+ _appleCareArchiveZoneID.onceToken
+ _kDRSDMPPSAppleCareIssueCategory
+ _objc_msgSend$appleCareArchiveZoneID
+ _objc_msgSend$codeServiceWithName:databaseScope:
+ _objc_msgSend$codeServiceWithName:serviceInstanceURL:
+ _objc_msgSend$ppsAppleCareConfiguration
+ _objc_msgSend$unsignedIntValue
- GCC_except_table129
- GCC_except_table169
- GCC_except_table178
- GCC_except_table180
- GCC_except_table184
- GCC_except_table187
- GCC_except_table83
- GCC_except_table88
- GCC_except_table98
- ___116-[DRSService _ckQueueDownstreamOnly_uploadInFlightWithTransaction:xpcActivity:ckHelper:isExpedited:completionBlock:]_block_invoke.103
- ___116-[DRSService _ckQueueDownstreamOnly_uploadInFlightWithTransaction:xpcActivity:ckHelper:isExpedited:completionBlock:]_block_invoke.120
- ___125-[DRSService _ckQueueOnly_submitOutstandingEnableDataGatheringQueriesWithTransaction:xpcActivity:ckHelper:followupWorkBlock:]_block_invoke.146
- ___136-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:backingPersistentContainer:completionHandler:]_block_invoke.233
- ___136-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:backingPersistentContainer:completionHandler:]_block_invoke.238
- ___136-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:backingPersistentContainer:completionHandler:]_block_invoke.243
- ___51-[DRSTeamDampeningConfiguration initWithPlistDict:]_block_invoke.430
- ___63-[DRSDampeningManager _ON_MOC_QUEUE_moRepresentationInContext:]_block_invoke.560
- ___87+[DRSDampeningManager dampeningManagerFromPersistentContainer:deleteBadState:errorOut:]_block_invoke.555
- ___block_descriptor_44_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
- ___block_literal_global.222
- ___block_literal_global.224
- ___block_literal_global.232
- ___block_literal_global.386
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "Default checkin encountered already scheduled activity with %{public, name=delaySeconds}lld s as a delay cap"
+ "DefaultCheckInFoundRegisteredActivity"
+ "DefaultCheckInPath"
+ "DefaultCheckInPermissiveExpeditedUploadXPCActivity"
+ "NoScheduledActivityEncountered"
+ "Nothing scheduled at default check-in"
+ "ProactiveSchedulingPath"
+ "acSupportLogZone"
+ "acdiagnostics-archive"
+ "appleCareArchiveZoneID"
+ "ppsAppleCareConfiguration"
+ "unsignedIntValue"

```
