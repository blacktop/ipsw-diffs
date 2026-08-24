## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/Versions/A/FeedbackCore`

```diff

-232.0.0.0.0
-  __TEXT.__text: 0x1013c0
-  __TEXT.__objc_methlist: 0x6ff4
+235.0.0.0.0
+  __TEXT.__text: 0x10141c
+  __TEXT.__lazy_helpers: 0x2a0
+  __TEXT.__objc_methlist: 0x703c
   __TEXT.__const: 0x1c84
-  __TEXT.__cstring: 0x841e
+  __TEXT.__cstring: 0x84de
   __TEXT.__oslogstring: 0x9332
   __TEXT.__gcc_except_tab: 0x121c
   __TEXT.__ustring: 0xdc
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__constg_swiftt: 0x84c
-  __TEXT.__swift5_typeref: 0x1526
+  __TEXT.__swift5_typeref: 0x150a
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_reflstr: 0x4c8
   __TEXT.__swift5_assocty: 0xf0

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x24
-  __TEXT.__unwind_info: 0x3588
-  __TEXT.__eh_frame: 0x12f0
+  __TEXT.__unwind_info: 0x3590
+  __TEXT.__eh_frame: 0x12c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e38
+  __DATA_CONST.__objc_selrefs: 0x4e58
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x4c8
-  __DATA_CONST.__got: 0xc50
+  __DATA_CONST.__got: 0xc38
   __AUTH_CONST.__const: 0x5fc8
   __AUTH_CONST.__cfstring: 0x86a0
-  __AUTH_CONST.__objc_const: 0xe348
+  __AUTH_CONST.__objc_const: 0xe3d8
+  __AUTH_CONST.__lazy_load_got: 0x40
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x468
   __AUTH_CONST.__auth_got: 0xed8
   __AUTH.__objc_data: 0x350
   __AUTH.__data: 0x210
-  __DATA.__objc_ivar: 0x434
-  __DATA.__data: 0x1640
+  __DATA.__objc_ivar: 0x440
+  __DATA.__data: 0x1624
   __DATA.__bss: 0x1e08
   __DATA.__common: 0x108
   __DATA_DIRTY.__objc_data: 0x2360

   - /System/Library/PrivateFrameworks/InternationalSupport.framework/Versions/A/InternationalSupport
   - /System/Library/PrivateFrameworks/PersonaUI.framework/Versions/A/PersonaUI
   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/Versions/A/RegulatoryDomain
-  - /System/Library/PrivateFrameworks/SiriAppIntents.framework/Versions/A/SiriAppIntents
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5112
-  Symbols:   7221
-  CStrings:  2234
+  Functions: 5119
+  Symbols:   7234
+  CStrings:  2236
 
Symbols:
+ -[FBKAttachmentManager initWithMatcherPredicates:pendingFileUrls:pendingExtensions:form:targetDevice:shouldGetSessionStatus:shouldCheckDeferredLogs:attachmentDescriptors:autoGathersDiagnosticExtensions:removesDeletedDEAttachments:]
+ -[FBKAttachmentManager isRemovingAllAttachments]
+ -[FBKAttachmentManager setIsRemovingAllAttachments:]
+ -[FBKDECollector removesDeletedDEAttachments]
+ -[FBKDECollector setRemovesDeletedDEAttachments:]
+ -[FBKDeviceDiagnosticsController initWithDeviceManager:delegate:filerForm:pendingFileUrls:pendingURLExtensions:draftDeviceIds:attachmentDescriptors:autoGathersDiagnosticExtensions:removesDeletedDEAttachments:]
+ -[FBKDeviceDiagnosticsController removesDeletedDEAttachments]
+ -[FBKDeviceDiagnosticsController setRemovesDeletedDEAttachments:]
+ OBJC_IVAR_$_FBKAttachmentManager._isRemovingAllAttachments
+ OBJC_IVAR_$_FBKDECollector._removesDeletedDEAttachments
+ OBJC_IVAR_$_FBKDeviceDiagnosticsController._removesDeletedDEAttachments
+ __209-[FBKDeviceDiagnosticsController initWithDeviceManager:delegate:filerForm:pendingFileUrls:pendingURLExtensions:draftDeviceIds:attachmentDescriptors:autoGathersDiagnosticExtensions:removesDeletedDEAttachments:]_block_invoke
+ ___209-[FBKDeviceDiagnosticsController initWithDeviceManager:delegate:filerForm:pendingFileUrls:pendingURLExtensions:draftDeviceIds:attachmentDescriptors:autoGathersDiagnosticExtensions:removesDeletedDEAttachments:]_block_invoke
+ ___231-[FBKAttachmentManager initWithMatcherPredicates:pendingFileUrls:pendingExtensions:form:targetDevice:shouldGetSessionStatus:shouldCheckDeferredLogs:attachmentDescriptors:autoGathersDiagnosticExtensions:removesDeletedDEAttachments:]_block_invoke
+ ___block_descriptor_99_e8_32s40s48s56s64s72s80s88s_e32_v24?0"NSDictionary"8"NSSet"16l
+ __dyld_lazy_load
+ _lazyLoadFlag$SiriAppIntents
+ _objc_msgSend$initWithDeviceManager:delegate:filerForm:pendingFileUrls:pendingURLExtensions:draftDeviceIds:attachmentDescriptors:autoGathersDiagnosticExtensions:removesDeletedDEAttachments:
+ _objc_msgSend$initWithMatcherPredicates:pendingFileUrls:pendingExtensions:form:targetDevice:shouldGetSessionStatus:shouldCheckDeferredLogs:attachmentDescriptors:autoGathersDiagnosticExtensions:removesDeletedDEAttachments:
+ _objc_msgSend$isRemovingAllAttachments
+ _objc_msgSend$removesDeletedDEAttachments
+ _objc_msgSend$setIsRemovingAllAttachments:
+ _objc_msgSend$setRemovesDeletedDEAttachments:
+ _symbolic ______p s7CVarArgP
- -[FBKAttachmentManager initWithMatcherPredicates:pendingFileUrls:pendingExtensions:form:targetDevice:shouldGetSessionStatus:shouldCheckDeferredLogs:attachmentDescriptors:autoGathersDiagnosticExtensions:]
- -[FBKDeviceDiagnosticsController initWithDeviceManager:delegate:filerForm:pendingFileUrls:pendingURLExtensions:draftDeviceIds:attachmentDescriptors:autoGathersDiagnosticExtensions:]
- __181-[FBKDeviceDiagnosticsController initWithDeviceManager:delegate:filerForm:pendingFileUrls:pendingURLExtensions:draftDeviceIds:attachmentDescriptors:autoGathersDiagnosticExtensions:]_block_invoke
- ___181-[FBKDeviceDiagnosticsController initWithDeviceManager:delegate:filerForm:pendingFileUrls:pendingURLExtensions:draftDeviceIds:attachmentDescriptors:autoGathersDiagnosticExtensions:]_block_invoke
- ___203-[FBKAttachmentManager initWithMatcherPredicates:pendingFileUrls:pendingExtensions:form:targetDevice:shouldGetSessionStatus:shouldCheckDeferredLogs:attachmentDescriptors:autoGathersDiagnosticExtensions:]_block_invoke
- ___block_descriptor_98_e8_32s40s48s56s64s72s80s88s_e32_v24?0"NSDictionary"8"NSSet"16l
- _objc_msgSend$initWithDeviceManager:delegate:filerForm:pendingFileUrls:pendingURLExtensions:draftDeviceIds:attachmentDescriptors:autoGathersDiagnosticExtensions:
- _objc_msgSend$initWithMatcherPredicates:pendingFileUrls:pendingExtensions:form:targetDevice:shouldGetSessionStatus:shouldCheckDeferredLogs:attachmentDescriptors:autoGathersDiagnosticExtensions:
- _symbolic _____Sg 14SiriAppIntents0A10TrajectoryO17RedactionCategoryO
- _symbolic _____y_____G s11_SetStorageC 14SiriAppIntents0C10TrajectoryO17RedactionCategoryO
- _symbolic _____y_____G s23_ContiguousArrayStorageC 14SiriAppIntents0D10TrajectoryO17RedactionCategoryO
CStrings:
+ "SiriRedaction: deleted attachment [%{public}@] has no contentRole; cannot resolve redaction category"
+ "SiriRedaction: gave up after [%d] retries due to persistent race on [%{public}@]"
+ "SiriRedaction: race on [%{public}@]; retrying in 1.0s [attempt %d/%d]"
+ "SiriRedaction: redacted file; dropped category [%{public}@]; url [%{private}@]"
+ "SiriRedaction: redaction failed [%{public}@]; url [%{private}@]"
+ "SiriRedaction: unrecognized redaction category identifier [%{public}@]"
+ "Skipping related-file redaction on removal — removing all attachments for [%{public}@]"
- "SiriRedaction: could not resolve SiriTrajectory.RedactionCategory for deleted attachment [%{public}@]"
- "SiriRedaction: gave up after %d retries due to persistent race on [%{public}@]"
- "SiriRedaction: race on [%{public}@]; retrying in 1.0s (attempt %d/%d)"
- "SiriRedaction: redacted file (dropped category [%{public}@]); url=[%{private}@]"
- "SiriRedaction: redaction failed (%{public}@); url=[%{private}@]"
```
