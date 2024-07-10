## NewsAnalyticsUpload

> `/System/Library/PrivateFrameworks/NewsAnalyticsUpload.framework/Versions/A/NewsAnalyticsUpload`

```diff

-5553.0.0.0.0
-  __TEXT.__text: 0x1ef50
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x740
+5559.0.0.0.0
+  __TEXT.__text: 0x1ef30
+  __TEXT.__auth_stubs: 0xb70
+  __TEXT.__objc_methlist: 0x748
   __TEXT.__const: 0x1639
-  __TEXT.__cstring: 0x319e
-  __TEXT.__gcc_except_tab: 0x1d8
+  __TEXT.__cstring: 0x314e
+  __TEXT.__gcc_except_tab: 0x1c0
   __TEXT.__oslogstring: 0x1c9
   __TEXT.__constg_swiftt: 0x3c8
   __TEXT.__swift5_typeref: 0x46b

   __TEXT.__swift5_reflstr: 0x5fa
   __TEXT.__swift5_assocty: 0xd8
   __TEXT.__swift5_capture: 0x58
-  __TEXT.__unwind_info: 0x9a0
+  __TEXT.__unwind_info: 0x988
   __TEXT.__eh_frame: 0x700
   __TEXT.__objc_classname: 0x230
-  __TEXT.__objc_methname: 0x2da1
-  __TEXT.__objc_methtype: 0xb7b
-  __TEXT.__objc_stubs: 0x1e00
+  __TEXT.__objc_methname: 0x2dea
+  __TEXT.__objc_methtype: 0xb68
+  __TEXT.__objc_stubs: 0x1e40
   __DATA_CONST.__got: 0x358
   __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa18
+  __DATA_CONST.__objc_selrefs: 0xa30
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x5c0
+  __AUTH_CONST.__auth_got: 0x5c8
   __AUTH_CONST.__auth_ptr: 0x200
-  __AUTH_CONST.__const: 0x1d60
+  __AUTH_CONST.__const: 0x1d90
   __AUTH_CONST.__cfstring: 0x5a0
-  __AUTH_CONST.__objc_const: 0x1ba8
+  __AUTH_CONST.__objc_const: 0x1bd8
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x468
   __AUTH.__data: 0x2c0
-  __DATA.__objc_ivar: 0x7c
+  __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x9e8
   __DATA.__bss: 0x3020
   __DATA.__common: 0x30

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 872
-  Symbols:   1238
-  CStrings:  282
+  Symbols:   1241
+  CStrings:  281
 
Symbols:
+ -[NDAnalyticsEnvelopeManager setSubmissionQueue:]
+ -[NDAnalyticsEnvelopeManager submissionQueue]
+ GCC_except_table21
+ GCC_except_table7
+ OBJC_IVAR_$_NDAnalyticsEnvelopeManager._submissionQueue
+ __107-[NDAnalyticsEnvelopeManager _handleOutcomeOfUploadAttemptWithPayload:success:error:willRetry:hitEndpoint:]_block_invoke.86
+ __107-[NDAnalyticsEnvelopeManager _handleOutcomeOfUploadAttemptWithPayload:success:error:willRetry:hitEndpoint:]_block_invoke.86.cold.1
+ __107-[NDAnalyticsEnvelopeManager _handleOutcomeOfUploadAttemptWithPayload:success:error:willRetry:hitEndpoint:]_block_invoke.86.cold.2
+ __59-[NDAnalyticsEnvelopeManager _lastUploadDatesByContentType]_block_invoke.64
+ __61-[NDAnalyticsEnvelopeManager submitEnvelopes:withCompletion:]_block_invoke.34
+ __68-[NDAnalyticsEnvelopeManager _scheduleUploadIfNeededWithCompletion:]_block_invoke.58
+ __74-[NDAnalyticsEnvelopeManager uploadScheduler:performUploadWithCompletion:]_block_invoke.48
+ __74-[NDAnalyticsEnvelopeManager uploadScheduler:performUploadWithCompletion:]_block_invoke.51
+ __74-[NDAnalyticsEnvelopeManager uploadScheduler:performUploadWithCompletion:]_block_invoke_2.49
+ __74-[NDAnalyticsEnvelopeManager uploadScheduler:performUploadWithCompletion:]_block_invoke_2.52
+ ___block_descriptor_56_e8_32s40s48bs_e14_v16?0?<v?>8l
+ __block_literal_global.71
+ _objc_msgSend$initWithQualityOfService:
+ _objc_msgSend$submissionQueue
- -[NDAnalyticsEnvelopeManager submitEnvelopes:withSubmissionCompletion:foregroundUploadCompletion:]
- -[NDAnalyticsEnvelopeManager submitEnvelopes:withSubmissionCompletion:foregroundUploadCompletion:].cold.1
- GCC_except_table23
- GCC_except_table6
- GCC_except_table74
- __107-[NDAnalyticsEnvelopeManager _handleOutcomeOfUploadAttemptWithPayload:success:error:willRetry:hitEndpoint:]_block_invoke.78
- __107-[NDAnalyticsEnvelopeManager _handleOutcomeOfUploadAttemptWithPayload:success:error:willRetry:hitEndpoint:]_block_invoke.82.cold.1
- __107-[NDAnalyticsEnvelopeManager _handleOutcomeOfUploadAttemptWithPayload:success:error:willRetry:hitEndpoint:]_block_invoke.82.cold.2
- __59-[NDAnalyticsEnvelopeManager _lastUploadDatesByContentType]_block_invoke.60
- __68-[NDAnalyticsEnvelopeManager _scheduleUploadIfNeededWithCompletion:]_block_invoke.54
- __74-[NDAnalyticsEnvelopeManager uploadScheduler:performUploadWithCompletion:]_block_invoke.44
- __74-[NDAnalyticsEnvelopeManager uploadScheduler:performUploadWithCompletion:]_block_invoke.47
- __74-[NDAnalyticsEnvelopeManager uploadScheduler:performUploadWithCompletion:]_block_invoke_2.45
- __74-[NDAnalyticsEnvelopeManager uploadScheduler:performUploadWithCompletion:]_block_invoke_2.48
- ___98-[NDAnalyticsEnvelopeManager submitEnvelopes:withSubmissionCompletion:foregroundUploadCompletion:]_block_invoke
- __block_literal_global.35
- __block_literal_global.63
CStrings:
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsAnalyticsUpload/TelemetryUploader.swift"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NAUAnalyticsEnvelopeTracker.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsEnvelopeManager.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsEnvelopeStore.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsEnvelopeStoreEntry.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsPayloadAssembler.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsPayloadAssemblerUtilities.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsPayloadUploader.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsUploadScheduler.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAppConfigAnalyticsPayloadAssemblerConfigProvider.m"
- "-[NDAnalyticsEnvelopeManager submitEnvelopes:withSubmissionCompletion:foregroundUploadCompletion:]"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldspar/Frameworks/NewsAnalyticsUpload/TelemetryUploader.swift"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NAUAnalyticsEnvelopeTracker.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsEnvelopeManager.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsEnvelopeStore.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsEnvelopeStoreEntry.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsPayloadAssembler.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsPayloadAssemblerUtilities.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsPayloadUploader.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAnalyticsUploadScheduler.m"
- "/AppleInternal/Library/BuildRoots/f9304f01-2b4a-11ef-a973-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldspar/Frameworks/NewsDaemon/newsd/Analytics/NDAppConfigAnalyticsPayloadAssemblerConfigProvider.m"

```
