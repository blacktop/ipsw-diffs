## VoiceMemos

> `/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos`

```diff

-1378.6.0.0.0
-  __TEXT.__text: 0x49a7c
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0x3e04
-  __TEXT.__gcc_except_tab: 0x1828
+1378.7.0.0.0
+  __TEXT.__text: 0x49d8c
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_methlist: 0x3e34
+  __TEXT.__gcc_except_tab: 0x1824
   __TEXT.__const: 0x290
-  __TEXT.__cstring: 0x6572
-  __TEXT.__oslogstring: 0x2a33
+  __TEXT.__cstring: 0x64a2
+  __TEXT.__oslogstring: 0x2ab9
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x1a68
+  __TEXT.__unwind_info: 0x1a88
   __TEXT.__objc_classname: 0x82d
-  __TEXT.__objc_methname: 0xbf27
-  __TEXT.__objc_methtype: 0x1576
-  __TEXT.__objc_stubs: 0x9060
+  __TEXT.__objc_methname: 0xbfbf
+  __TEXT.__objc_methtype: 0x15bc
+  __TEXT.__objc_stubs: 0x90c0
   __DATA_CONST.__got: 0x690
-  __DATA_CONST.__const: 0x1d50
+  __DATA_CONST.__const: 0x1d98
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ea0
+  __DATA_CONST.__objc_selrefs: 0x2eb8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x5f8
-  __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x3340
-  __AUTH_CONST.__objc_const: 0x5bb8
+  __AUTH_CONST.__auth_got: 0x5f0
+  __AUTH_CONST.__const: 0x8a0
+  __AUTH_CONST.__cfstring: 0x3360
+  __AUTH_CONST.__objc_const: 0x5bf0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x310
+  __DATA.__objc_ivar: 0x314
   __DATA.__data: 0x7a0
   __DATA.__bss: 0x180
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F3CA5FD-8075-3741-9610-AE4DCC3B7B20
-  Functions: 1919
-  Symbols:   6718
-  CStrings:  3486
+  UUID: 16A07872-5C64-3A34-9424-951273F6B7C0
+  Functions: 1930
+  Symbols:   6748
+  CStrings:  3498
 
Symbols:
+ -[RCSSavedRecordingService cleanupExportedFileAtURL:withToken:completionBlock:]
+ -[RCSSavedRecordingService cleanupExportedFileAtURL:withToken:completionBlock:].cold.1
+ -[RCSSavedRecordingService cleanupExportedFileAtURL:withToken:completionBlock:].cold.2
+ -[RCVoiceMemoMetadata exportCleanupToken]
+ -[RCVoiceMemoMetadata setExportCleanupToken:]
+ GCC_except_table116
+ GCC_except_table120
+ GCC_except_table125
+ GCC_except_table132
+ GCC_except_table76
+ GCC_except_table89
+ GCC_except_table95
+ _OBJC_IVAR_$_RCVoiceMemoMetadata._exportCleanupToken
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB9nqe210106ERKf
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
+ ___108+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:includeAsset:completionHandler:]_block_invoke.2
+ ___108+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:includeAsset:completionHandler:]_block_invoke.2.cold.1
+ ___108+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:includeAsset:completionHandler:]_block_invoke.2.cold.2
+ ___79-[RCSSavedRecordingService cleanupExportedFileAtURL:withToken:completionBlock:]_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40bs_e41_v24?0"RCVoiceMemoMetadata"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e63_v24?0"<RCSSavedRecordingServiceProtocol>"8?<v?"NSError">16ls32l8s40l8
+ _objc_msgSend$cleanupExportedFileAtURL:withToken:completionBlock:
+ _objc_msgSend$exportCleanupToken
+ _objc_msgSend$setExportCleanupToken:
- GCC_except_table114
- GCC_except_table118
- GCC_except_table121
- GCC_except_table130
- GCC_except_table137
- GCC_except_table163
- GCC_except_table74
- GCC_except_table83
- GCC_except_table87
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB9foe210106ERKf
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
- ___block_descriptor_49_e8_32s40bs_e41_v24?0"RCVoiceMemoMetadata"8"NSError"16ls40l8s32l8
CStrings:
+ "%s -- Cleanup called with nil parameter"
+ "%s -- Cleanup failed: %@"
+ "%s -- Cleanup succeeded"
+ "%s -- Scheduling cleanup of temp file: %@"
+ "%s -- Sending service request to cleanup exported file: %@"
+ "%s -- Sending service request to fetchMetadataForRecordingWithUUID, includeAsset: %@"
+ "-[RCSSavedRecordingService cleanupExportedFileAtURL:withToken:completionBlock:]"
+ "T@\"NSString\",&,N,V_exportCleanupToken"
+ "Vv40@0:8@\"NSURL\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@16@24@?32"
+ "_exportCleanupToken"
+ "cleanupExportedFileAtURL:withToken:completionBlock:"
+ "exportCleanupToken"
+ "setExportCleanupToken:"
- "\r"
- "%s -- Failed to access secure url for recording with UUID %@"
- "%s -- Sending service request to fetchRecordingUUIDsForExport, includeAsset: %@"
- "/AppleInternal/Library/BuildRoots/4~CJFtugAQw66kZBAGmUtKyRcWg1jARmJC3aTeb54/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"

```
