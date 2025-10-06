## DiagnosticRequestService

> `/System/Library/PrivateFrameworks/DiagnosticRequestService.framework/DiagnosticRequestService`

```diff

-316.100.13.0.0
-  __TEXT.__text: 0x67c24
+316.120.2.0.0
+  __TEXT.__text: 0x682ac
   __TEXT.__auth_stubs: 0xf10
   __TEXT.__objc_methlist: 0x46b4
   __TEXT.__const: 0xcf8
   __TEXT.__gcc_except_tab: 0x84c
-  __TEXT.__cstring: 0x4f5f
-  __TEXT.__oslogstring: 0xa6b3
+  __TEXT.__cstring: 0x507f
+  __TEXT.__oslogstring: 0xa751
   __TEXT.__swift5_typeref: 0x278
   __TEXT.__constg_swiftt: 0x24c
   __TEXT.__swift5_fieldmd: 0x240

   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1b30
+  __TEXT.__unwind_info: 0x1b38
   __TEXT.__eh_frame: 0x440
   __TEXT.__objc_classname: 0x975
   __TEXT.__objc_methname: 0xa6fb

   __DATA_CONST.__objc_selrefs: 0x22d0
   __DATA_CONST.__objc_classrefs: 0x3c0
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__cfstring: 0x4dc0
+  __AUTH_CONST.__cfstring: 0x4e80
   __AUTH_CONST.__objc_const: 0x23f8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__const: 0x1050

   __DATA.__objc_data: 0x48
   __DATA.__data: 0x6b8
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x15e0
+  __DATA.__bss: 0x15b0
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x1580
   __DATA_DIRTY.__data: 0xe0
-  __DATA_DIRTY.__bss: 0x330
+  __DATA_DIRTY.__bss: 0x360
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 26B67319-504B-3EB4-916E-F62A43EC7C83
-  Functions: 2356
-  Symbols:   6554
-  CStrings:  4355
+  UUID: 221B8571-3A8C-3203-A334-37EC49074BF0
+  Functions: 2358
+  Symbols:   6558
+  CStrings:  4371
 
Symbols:
+ _DRValidateCKRecordDictionary
+ ___109-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:completionHandler:]_block_invoke.223
+ ___109-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:completionHandler:]_block_invoke.224
+ ___109-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:completionHandler:]_block_invoke.228
+ ___block_literal_global.208
+ ___block_literal_global.210
+ ___block_literal_global.218
+ ___block_literal_global.367
+ __isSupportedRecordDictionaryValueType
- ___109-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:completionHandler:]_block_invoke.217
- ___109-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:completionHandler:]_block_invoke.218
- ___109-[DRSCloudKitHelper uploadRequests:contactDecisionServer:xpcActivity:remainingUploadQuota:completionHandler:]_block_invoke.222
- ___block_literal_global.205
- ___block_literal_global.207
- ___block_literal_global.215
- ___block_literal_global.361
CStrings:
+ "'recordDictionary' has a non-NSString key"
+ "'recordDictionary' is nil or empty"
+ "'recordDictionary' value of type '%@' for array with key '%@' is not allowed"
+ "'recordDictionary' value of type '%@' for key '%@' is not allowed"
+ "Could not create CKRecord for request"
+ "CouldNotCreateCKRecord"
+ "Failed to generate CKRecord for request %{public}@"
+ "MalformedCKRecordDictionaryError"
+ "MalformedRecordDictionary"
+ "Record dictionary for %{public}@ is malformed: %{public}@"

```
