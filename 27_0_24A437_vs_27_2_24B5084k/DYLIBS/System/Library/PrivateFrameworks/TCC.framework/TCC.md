## TCC

> `/System/Library/PrivateFrameworks/TCC.framework/TCC`

```diff

-913.0.1.0.0
-  __TEXT.__text: 0x1596c
+918.0.0.0.0
+  __TEXT.__text: 0x1638c
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__cstring: 0x3389
-  __TEXT.__oslogstring: 0x1665
+  __TEXT.__cstring: 0x3547
+  __TEXT.__oslogstring: 0x1796
   __TEXT.__const: 0x398
-  __TEXT.__unwind_info: 0x870
+  __TEXT.__unwind_info: 0x8b8
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1870
+  __DATA_CONST.__const: 0x1920
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x2d8
-  __AUTH_CONST.__cfstring: 0x1720
+  __AUTH_CONST.__cfstring: 0x17a0
   __AUTH_CONST.__objc_const: 0xf58
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x208
-  __DATA.__data: 0x958
+  __DATA.__data: 0x970
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 597
-  Symbols:   962
-  CStrings:  611
+  Functions: 613
+  Symbols:   974
+  CStrings:  631
 
Symbols:
+ _OUTLINED_FUNCTION_12
+ _TCCAccessCopyAuthorizationsFromBundleId
+ _TCCCopyIconIdentifierForService
+ ___TCCAccessCopyAuthorizationsFromBundleId_block_invoke
+ ___TCCAccessCopyAuthorizationsFromBundleId_block_invoke_2
+ ___TCCCopyIconIdentifierForService_block_invoke
+ ___TCCCopyIconIdentifierForService_block_invoke_2
+ _kTCCServiceAccessoryWorker
+ _kTCCServiceAccessoryWorkerGPU
+ _kTCCServiceMotionSensors
+ _tcc_authorization_record_get_eligible_for_reprompt
+ _tcc_authorization_record_set_eligible_for_reprompt
CStrings:
+ "%{public}s Requesting icon identifier for %s"
+ "%{public}s: both source and destination bundle identifiers are required"
+ "%{public}s: failed to convert bundle identifiers"
+ "%{public}s: identifier for %{public}s return NULL"
+ "Eligible For Reprompt, "
+ "TCCAccessCopyAuthorizations"
+ "TCCAccessCopyAuthorizationsFromBundleId"
+ "TCCAccessCopyAuthorizationsFromBundleId() IPC"
+ "TCCAccessCopyAuthorizationsFromBundleId_block_invoke_2"
+ "TCCCopyIconIdentifierForService"
+ "TCCCopyIconIdentifierForService() Sync IPC"
+ "TCCCopyIconIdentifierForService_block_invoke"
+ "TCCCopyIconIdentifierForService_block_invoke_2"
+ "TCCD_MSG_MESSAGE_ELIGIBLE_FOR_REPROMPT"
+ "destination_bundle_id"
+ "iconIdentifier"
+ "kTCCServiceAccessoryWorker"
+ "kTCCServiceAccessoryWorkerGPU"
+ "kTCCServiceMotionSensors"
+ "source_bundle_id"
```
