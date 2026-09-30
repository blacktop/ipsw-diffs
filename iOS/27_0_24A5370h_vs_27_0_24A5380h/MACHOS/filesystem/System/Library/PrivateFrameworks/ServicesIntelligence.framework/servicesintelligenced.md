## servicesintelligenced

> `/System/Library/PrivateFrameworks/ServicesIntelligence.framework/servicesintelligenced`

```diff

-  __TEXT.__text: 0xea00
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_stubs: 0x200
+  __TEXT.__text: 0x1275c
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_stubs: 0x380
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x29a
-  __TEXT.__cstring: 0x5b8
+  __TEXT.__const: 0x2ca
+  __TEXT.__cstring: 0x688
   __TEXT.__swift5_typeref: 0x177
   __TEXT.__objc_methtype: 0x12c
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_types: 0x8
   __TEXT.__objc_classname: 0x3e
-  __TEXT.__objc_methname: 0x367
-  __TEXT.__swift5_capture: 0x170
-  __TEXT.__oslogstring: 0x8ac
-  __TEXT.__swift_as_entry: 0x44
-  __TEXT.__swift_as_ret: 0x74
-  __TEXT.__swift_as_cont: 0xb8
-  __TEXT.__unwind_info: 0x400
-  __TEXT.__eh_frame: 0xb80
-  __DATA_CONST.__const: 0x628
+  __TEXT.__objc_methname: 0x487
+  __TEXT.__swift5_capture: 0x1c8
+  __TEXT.__oslogstring: 0xd6c
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x98
+  __TEXT.__swift_as_cont: 0xe0
+  __TEXT.__unwind_info: 0x498
+  __TEXT.__eh_frame: 0xe38
+  __DATA_CONST.__const: 0x740
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x580
-  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__auth_got: 0x5c8
+  __DATA_CONST.__got: 0x190
   __DATA_CONST.__auth_ptr: 0xa0
   __DATA.__objc_const: 0x1d8
-  __DATA.__objc_selrefs: 0x120
+  __DATA.__objc_selrefs: 0x180
   __DATA.__data: 0x290
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 230
-  Symbols:   258
-  CStrings:  135
+  Functions: 269
+  Symbols:   274
+  CStrings:  166
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__constg_swiftt : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__data : content changed
Symbols:
+ _$s10Foundation22_convertNSErrorToErrorys0E0_pSo0C0CSgF
+ _$s20ServicesIntelligence0aB8ProviderC17refreshDomainData6domain14requestContextyAA0E0O_AA07RequestI0VSgtYaKF
+ _$s20ServicesIntelligence0aB8ProviderC17refreshDomainData6domain14requestContextyAA0E0O_AA07RequestI0VSgtYaKFTu
+ _$s20ServicesIntelligence0aB8ProviderC26refreshTopicMappingsViaPIR14requestContextyAA07RequestJ0VSg_tYaF
+ _$s20ServicesIntelligence0aB8ProviderC26refreshTopicMappingsViaPIR14requestContextyAA07RequestJ0VSg_tYaFTu
+ _$s20ServicesIntelligence0aB8ProviderC27deferredClassBDatabaseCount14requestContextSiAA07RequestI0VSg_tYaF
+ _$s20ServicesIntelligence0aB8ProviderC27deferredClassBDatabaseCount14requestContextSiAA07RequestI0VSg_tYaFTu
+ _$s20ServicesIntelligence0aB8ProviderC30recoverDeferredClassBDatabases14requestContextSiAA07RequestI0VSg_tYaF
+ _$s20ServicesIntelligence0aB8ProviderC30recoverDeferredClassBDatabases14requestContextSiAA07RequestI0VSg_tYaFTu
+ _$s20ServicesIntelligence0aB8ProviderC32isSemanticProfileWorkloadAllowedSbyYaF
+ _$s20ServicesIntelligence0aB8ProviderC32isSemanticProfileWorkloadAllowedSbyYaFTu
+ _$s20ServicesIntelligence6DomainO4appsyA2CmFWC
+ _$s20ServicesIntelligence6DomainOMa
+ _OBJC_CLASS_$_BGRepeatingSystemTaskRequest
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _objc_release_x28
+ _objc_retain_x20
+ _swift_release_x21
+ _swift_release_x28
+ _swift_retain_x19
+ _swift_retain_x25
- _$s20ServicesIntelligence0aB8ProviderC20refreshTopicMappings14requestContextyAA07RequestH0VSg_tYaKF
- _$s20ServicesIntelligence0aB8ProviderC20refreshTopicMappings14requestContextyAA07RequestH0VSg_tYaKFTu
- _$s20ServicesIntelligence10FitnessXPCC6ServerC3runyyFTj
- _$s20ServicesIntelligence10FitnessXPCC6ServerC6sharedAEvgZ
- _$s20ServicesIntelligence10FitnessXPCC6ServerCMa
- _swift_retain_x23
CStrings:
+ ".refreshDomainData"
+ ".refreshTopicMappingsViaPIR"
+ "[%s] Account not eligible (storefront / personalization / u18); skipping semantic profile workload"
+ "[Daemon][cancelClassBRecoveryTask] Cancelled Class B recovery task — nothing left to recover"
+ "[Daemon][cancelClassBRecoveryTask] Failed to cancel Class B recovery task: %@"
+ "[Daemon][class-b-db-recovery] All recovered — parked task"
+ "[Daemon][class-b-db-recovery] Background task fired"
+ "[Daemon][class-b-db-recovery] Failed to park task, completing instead: %@"
+ "[Daemon][class-b-db-recovery] Recovery attempt complete, %ld still deferred"
+ "[Daemon][class-b-db-recovery] Shadow task completed"
+ "[Daemon][class-b-db-recovery] Shadow task started"
+ "[Daemon][listenForLaunchEvents] Registering handler for Class B DB recovery task"
+ "[Daemon][reconcileClassBRecoveryTask] Class B recovery task already submitted; ensured scheduling (%ld deferred)"
+ "[Daemon][reconcileClassBRecoveryTask] Failed to submit Class B recovery task: %@"
+ "[Daemon][reconcileClassBRecoveryTask] Submitted Class B recovery task (%ld deferred)"
+ "[Daemon][refreshDomainData] complete"
+ "[Daemon][refreshDomainData] failed: %@"
+ "[Daemon][refreshDomainData] start"
+ "[Daemon][refreshTopicMappingsViaPIR] complete"
+ "[Daemon][refreshTopicMappingsViaPIR] start"
+ "cancelTaskRequestWithIdentifier:error:"
+ "com.apple.servicesintelligenced.class-b-db-recovery"
+ "com.apple.servicesintelligenced.launchevents.classBRecovery"
+ "executeSemanticProfileWorkload(label:)"
+ "initWithIdentifier:"
+ "resumeScheduling:error:"
+ "setInterval:"
+ "setMinDurationBetweenInstances:"
+ "setPriority:"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setRequiresProtectionClass:"
+ "setTaskExpiredWithRetryAfter:error:"
+ "submitTaskRequest:error:"
+ "taskRequestForIdentifier:"
- ".refreshTopicMappings"
- "[Daemon][refreshTopicMappings] complete"
- "[Daemon][refreshTopicMappings] failed: %@"
- "[Daemon][refreshTopicMappings] start"

```
