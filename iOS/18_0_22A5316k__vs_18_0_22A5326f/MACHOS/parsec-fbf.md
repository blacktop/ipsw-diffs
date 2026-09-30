## parsec-fbf

> `/System/Library/PrivateFrameworks/CoreParsec.framework/parsec-fbf`

```diff

-3400.140.1.0.0
-  __TEXT.__text: 0x1490e0
-  __TEXT.__auth_stubs: 0x3740
+3400.147.2.0.0
+  __TEXT.__text: 0x1499ec
+  __TEXT.__auth_stubs: 0x3730
   __TEXT.__objc_stubs: 0x40
   __TEXT.__objc_methlist: 0x378
-  __TEXT.__const: 0xcd6c
+  __TEXT.__const: 0xcfac
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x9c91
-  __TEXT.__swift5_typeref: 0x4944
-  __TEXT.__constg_swiftt: 0x7b54
-  __TEXT.__swift5_fieldmd: 0x524c
-  __TEXT.__swift5_reflstr: 0x4a25
+  __TEXT.__cstring: 0x9e11
+  __TEXT.__constg_swiftt: 0x7b74
+  __TEXT.__swift5_typeref: 0x49f2
   __TEXT.__swift5_builtin: 0x334
-  __TEXT.__swift5_assocty: 0x808
-  __TEXT.__swift5_proto: 0xb08
+  __TEXT.__swift5_reflstr: 0x49d5
+  __TEXT.__swift5_fieldmd: 0x5274
   __TEXT.__swift5_types: 0x548
-  __TEXT.__objc_methname: 0x2a04
   __TEXT.__swift5_protos: 0x1b0
-  __TEXT.__swift5_capture: 0xfb0
-  __TEXT.__oslogstring: 0x3742
+  __TEXT.__swift5_proto: 0xb2c
   __TEXT.__swift5_mpenum: 0xa0
+  __TEXT.__oslogstring: 0x3812
+  __TEXT.__swift5_assocty: 0x808
+  __TEXT.__objc_methname: 0x2b6e
+  __TEXT.__swift5_capture: 0xfc4
   __TEXT.__objc_classname: 0xfe
   __TEXT.__objc_methtype: 0x24c
+  __TEXT.__swift5_types2: 0x4
   __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__unwind_info: 0x6078
-  __TEXT.__eh_frame: 0xa660
-  __DATA_CONST.__auth_got: 0x1bb0
-  __DATA_CONST.__got: 0xbe0
-  __DATA_CONST.__auth_ptr: 0x1640
-  __DATA_CONST.__const: 0xcae0
-  __DATA_CONST.__cfstring: 0x1a00
+  __TEXT.__unwind_info: 0x6130
+  __TEXT.__eh_frame: 0xa7b8
+  __DATA_CONST.__auth_got: 0x1ba8
+  __DATA_CONST.__got: 0xc00
+  __DATA_CONST.__auth_ptr: 0x1638
+  __DATA_CONST.__const: 0xccb8
+  __DATA_CONST.__cfstring: 0x19e0
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA.__objc_const: 0x7b78
-  __DATA.__objc_selrefs: 0x10e0
+  __DATA.__objc_selrefs: 0x1170
   __DATA.__objc_data: 0x1438
-  __DATA.__data: 0xc698
+  __DATA.__data: 0xc728
+  __DATA.__common: 0x5f8
   __DATA.__bss: 0xdf40
-  __DATA.__common: 0x5f0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9195
-  Symbols:   1460
-  CStrings:  2199
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 9231
+  Symbols:   1472
+  CStrings:  2222
 
Symbols:
+ _$ss31withCheckedThrowingContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5Error_pGXEtYaKlF
+ _$ss31withCheckedThrowingContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5Error_pGXEtYaKlFTu
+ _OBJC_CLASS_$_BatchMetadata
+ _OBJC_CLASS_$_FLDPGBatchFactory
+ _OBJC_CLASS_$_OspreyChannel
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _swift_runtimeSupportsNoncopyableTypes
- _$s20PegasusConfiguration6ClientVyAcA0C4TypeOcfC
- _$sScC12continuation8functionScCyxq_GSccyxq_G_SStcfC
CStrings:
+ "%!s(MISSING) batch housekeeping complete: did nothing."
+ "%!s(MISSING) batch housekeeping failed!"
+ "%!s(MISSING) batch housekeeping purged %!l(MISSING)d."
+ "BatchMetadata_init(row:)"
+ "DPGUploadService dealloced"
+ "Error initializing BatchMetadata from SQLiteRow: %!s(MISSING) [%!@(MISSING)]"
+ "Failed to get batchID from BatchMetadata"
+ "Failed to initialize database: %!s(MISSING) [%!@(MISSING)]"
+ "Failed to process batch telemetry: %!s(MISSING) [%!@(MISSING)]"
+ "SELECT\n    s.batchId,\n    s.timestampRefId,\n    s.status,\n    s.processedAttempts,\n    s.dateCreated,\n    s.dateUploaded,\n    s.dateLastProcessed,\n    COUNT(DISTINCT(r.rowId)) as eventCount,\n    COALESCE(sum(length(r.payload)), 0) as batchSize\nFROM batchStatus s\nLEFT JOIN records r ON s.batchId = r.batchId\nWHERE s.dateUploaded IS NOT NULL\n   OR s.dateCreated < strftime('%!s(MISSING)',datetime('now', '-7 day'))\n   OR s.status IN (4, 5, 6)\nGROUP BY s.batchId;"
+ "action"
+ "assetDeliveryBloomFilter"
+ "assetDeliveryGetPreloadedData"
+ "assetDeliveryPrefilterPrefetch"
+ "assetDeliveryPreloadAsset"
+ "assetDeliveryRedact"
+ "assetDeliveryRetrieveAsset"
+ "batchIdIterator"
+ "batchIdentifier"
+ "buttons"
+ "db"
+ "dpgService"
+ "initWithURL:configuration:"
+ "isDPG"
+ "isDPGBundleID:"
+ "leadingSwipeButtonItems"
+ "setActionCardType:"
+ "setActionTarget:"
+ "setBatchIdentifier:"
+ "setBatchSize:"
+ "setCardSectionType:"
+ "setCommandType:"
+ "setDateCreated:"
+ "setDateLastProcessed:"
+ "setDateUploaded:"
+ "setDestination:"
+ "setEventCount:"
+ "setExperimentId:"
+ "setExperimentInfos:"
+ "setExperimentNamespaceId:"
+ "setFeedbackType:"
+ "setHashedIdentifier:"
+ "setKnownSectionBundleIdentifier:"
+ "setPartialClientIp:"
+ "setProcessedAttempts:"
+ "setResultSectionId:"
+ "setTimestampReferenceIdentifier:"
+ "setTreatmentId:"
+ "sigHandlers"
+ "trailingSwipeButtonItems"
- "Batch housekeeping complete: did nothing"
- "Batch housekeeping completed: Purged %!l(MISSING)d, broken down by status %!s(MISSING)"
- "Batch housekeeping failed!"
- "assetDeliveryAssetAccessBloomFilter"
- "assetDeliveryAssetAccessPathFilter"
- "assetDeliveryAssetRedactPath"
- "assetDeliveryFetchAssetsSafariSummarization"
- "assetDeliveryFetchAssetsUAF"
- "assetDeliveryPreinstalledAssetsSafariSummarization"
- "assetDeliverySanitizeSafariSummarization"
- "batchDescriptors"
- "getPurgableBatchIds"
- "last_"
- "setButtons:"
- "setCard:"
- "setCardSection:"
- "setCompactCard:"
- "setInlineCard:"
- "setJsonFeedback:"
- "setLeadingSwipeButtonItems:"
- "setReason:"
- "setResult:"
- "setTrailingSwipeButtonItems:"
- "sigHup"
- "sigInt"
- "sigTerm"
- "underlyingError"

```
