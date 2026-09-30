## AppleTracingSupportSymbolication

> `/System/Library/PrivateFrameworks/AppleTracingSupportSymbolication.framework/Versions/A/AppleTracingSupportSymbolication`

```diff

-  __TEXT.__text: 0x20524
-  __TEXT.__const: 0x680
-  __TEXT.__gcc_except_tab: 0x1594
-  __TEXT.__cstring: 0x745
-  __TEXT.__oslogstring: 0x37f
-  __TEXT.__unwind_info: 0xf00
+  __TEXT.__text: 0x225a8
+  __TEXT.__lazy_helpers: 0xa8
+  __TEXT.__const: 0x778
+  __TEXT.__gcc_except_tab: 0x1864
+  __TEXT.__cstring: 0xa47
+  __TEXT.__oslogstring: 0x500
+  __TEXT.__dlopen_cstrs: 0x62
+  __TEXT.__unwind_info: 0xfa0
+  __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x340
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x370
+  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
+  __DATA_CONST.__objc_selrefs: 0xe8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x650
+  __AUTH_CONST.__const: 0x7a0
+  __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__weak_auth_got: 0x18
+  __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__bss: 0xa8
+  __DATA.__data: 0x4
+  __DATA.__bss: 0xc0
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication
   - /System/Library/PrivateFrameworks/DebugSymbols.framework/Versions/A/DebugSymbols
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/Versions/A/LoggingSupport
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/ktrace.framework/Versions/A/ktrace
   - /usr/lib/libRosetta.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 800
-  Symbols:   1433
-  CStrings:  73
+  - /usr/lib/libobjc.A.dylib
+  Functions: 841
+  Symbols:   1560
+  CStrings:  100
 
Sections:
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
Symbols:
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table133
+ GCC_except_table142
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table153
+ GCC_except_table157
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table187
+ GCC_except_table190
+ GCC_except_table194
+ GCC_except_table195
+ GCC_except_table200
+ GCC_except_table205
+ GCC_except_table206
+ GCC_except_table211
+ GCC_except_table215
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table225
+ GCC_except_table233
+ GCC_except_table234
+ GCC_except_table239
+ GCC_except_table240
+ GCC_except_table244
+ GCC_except_table245
+ GCC_except_table249
+ GCC_except_table254
+ GCC_except_table262
+ GCC_except_table263
+ GCC_except_table268
+ GCC_except_table271
+ GCC_except_table274
+ GCC_except_table279
+ GCC_except_table280
+ GCC_except_table300
+ GCC_except_table301
+ GCC_except_table302
+ GCC_except_table303
+ GCC_except_table304
+ GCC_except_table308
+ GCC_except_table311
+ GCC_except_table38
+ GCC_except_table51
+ GCC_except_table62
+ GCC_except_table65
+ GCC_except_table70
+ GCC_except_table80
+ GCC_except_table81
+ GCC_except_table85
+ GCC_except_table89
+ GCC_except_table94
+ GCC_except_table98
+ _CFRetain
+ _CSSSymbolicatorCreateWithFlatbufferConformantJsonString
+ _CSSymbolOwnerGetSegmentWithAddress
+ _OBJC_CLASS_$_BKSACOAuthCredentials
+ _OBJC_CLASS_$_BKSACOAuthCredentials$lazyGOT
+ _OBJC_CLASS_$_BKSACOAuthCredentials$lazyGOT$loadHelper_x8
+ _OBJC_CLASS_$_BKSJob
+ _OBJC_CLASS_$_BKSJob$lazyGOT
+ _OBJC_CLASS_$_BKSJob$lazyGOT$loadHelper_x19
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSUUID
+ _ZZL29AppleConnectClientLibraryCorePPcE16frameworkLibrary
+ _ZZL31getACAuthenticationRequestClassvE9softClass
+ _ZZL38getACDesktopAuthenticationContextClassvE9softClass
+ __ZL25AppleConnectClientLibraryv
+ __ZL29AppleConnectClientLibraryCorePPc
+ __ZL30audit_stringAppleConnectClient
+ __ZL38getACDesktopAuthenticationContextClassv
+ __ZN13SharedLibrary33prepareForResymbolicationWithJSONEPKc
+ __ZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEv
+ __ZNK13SharedLibrary23forEachOffsetAndSegmentERKNSt3__18functionIFvyPKcEEE
+ __ZNKSt3__110__function6__funcIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0FvyPKcEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0FvyPKcEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0FvyPKcEE7__cloneEPNS0_6__baseIS6_EE
+ __ZNKSt3__110__function6__funcIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0FvyPKcEE7__cloneEv
+ __ZNKSt3__18functionIFvyPKcEEclEyS2_
+ __ZNSt3__110__function12__value_funcIFvyPKcEED2B9nqe220106Ev
+ __ZNSt3__110__function6__funcIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0FvyPKcEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0FvyPKcEE7destroyEv
+ __ZNSt3__110__function6__funcIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0FvyPKcEED0Ev
+ __ZNSt3__110__function6__funcIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0FvyPKcEED1Ev
+ __ZNSt3__110__function6__funcIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0FvyPKcEEclEOyOS5_
+ __ZNSt3__119__allocate_at_leastB9nqe220106INS_9allocatorI16ats_bulk_requestEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__16vectorI16ats_bulk_requestNS_9allocatorIS1_EEE20__throw_length_errorB9nqe220106Ev
+ __ZNSt3__16vectorI16ats_bulk_requestNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZTINSt3__110__function6__baseIFvyPKcEEE
+ __ZTINSt3__110__function6__funcIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0FvyPKcEEE
+ __ZTIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0
+ __ZTSNSt3__110__function6__baseIFvyPKcEEE
+ __ZTSNSt3__110__function6__funcIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0FvyPKcEEE
+ __ZTSZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0
+ __ZTVNSt3__110__function6__funcIZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEvE3$_0FvyPKcEEE
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeI4UUIDNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEENS_22__unordered_map_hasherIS2_NS_4pairIKS2_S8_EENS_4hashIS2_EENS_8equal_toIS2_EEEENS_21__unordered_map_equalIS2_SD_SH_SF_EENS6_ISD_EEE16__emplace_uniqueB9nqe220106IJRS2_S8_EEENSB_INS_15__hash_iteratorIPNS_11__hash_nodeIS9_PvEEEEbEEDpOT_ENKUlRSC_SO_OS8_E_clESZ_SO_S10_
+ ___CFConstantStringClassReference
+ ___ZL31getACAuthenticationRequestClassv_block_invoke
+ ___ZL38getACDesktopAuthenticationContextClassv_block_invoke
+ ____ZL29AppleConnectClientLibraryCorePPc_block_invoke
+ ____ZL31getACAuthenticationRequestClassv_block_invoke
+ ____ZL38getACDesktopAuthenticationContextClassv_block_invoke
+ ____ZN20SymbolicationSession34collectSymbolsViaBulkSymbolicationEv_block_invoke
+ ___ats_perform_bulk_symbolication_block_invoke
+ ___block_descriptor_40_ea8_32r_e41_"BKSACOAuthCredentials"16?0"NSString"8l
+ ___block_descriptor_40_ea8_32r_e5_v8?0l
+ ___block_descriptor_48_ea8_32r_e5_v8?0l
+ ___block_descriptor_56_ea8_32s40r48r_e41_v24?0"BKSResultCollection"8"NSError"16l
+ ___copy_helper_block_ea8_32r
+ ___copy_helper_block_ea8_32s40r48r
+ ___destroy_helper_block_ea8_32r
+ ___destroy_helper_block_ea8_32s40r48r
+ __ats_perform_bulk_symbolication_block_invoke
+ __dyld_lazy_load
+ __sl_dlopen
+ _abort_report_np
+ _ats_perform_bulk_symbolication
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _free
+ _lazyLoadFlag$BulkSymbolication
+ _objc_alloc
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_getClass
+ _objc_msgSend
+ _objc_msgSend$UTF8String
+ _objc_msgSend$UUIDString
+ _objc_msgSend$addObject:
+ _objc_msgSend$addRequestForSymbolOwnerUUID:segmentName:offsetIntoSegment:
+ _objc_msgSend$authenticateWithRequest:
+ _objc_msgSend$cancel
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$error
+ _objc_msgSend$fetchCurrentUserNameAndReturnError:
+ _objc_msgSend$generateFlatbufferConformantJSONStringForUUID:error:
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$init
+ _objc_msgSend$initWithGroupName:timeoutInSec:shouldReadFromKeychain:resultCollectionCompletionBlock:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$initWithUserName:serviceClientID:oauthIDToken:oauthAccessToken:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$oauthAccessToken
+ _objc_msgSend$oauthIDToken
+ _objc_msgSend$resume
+ _objc_msgSend$set
+ _objc_msgSend$setAcOAuthCredentialBlock:
+ _objc_msgSend$setAuthType:
+ _objc_msgSend$setEnvironment:
+ _objc_msgSend$setInteractivityType:
+ _objc_msgSend$setOauthClientID:
+ _objc_msgSend$setOauthGrantType:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$userName
+ _objc_opt_class
+ _objc_opt_respondsToSelector
+ _objc_release
+ _objc_retain
+ _objc_retainAutorelease
+ ats_perform_bulk_symbolication
- GCC_except_table122
- GCC_except_table130
- GCC_except_table131
- GCC_except_table138
- GCC_except_table146
- GCC_except_table147
- GCC_except_table151
- GCC_except_table155
- GCC_except_table181
- GCC_except_table182
- GCC_except_table185
- GCC_except_table188
- GCC_except_table192
- GCC_except_table193
- GCC_except_table198
- GCC_except_table203
- GCC_except_table204
- GCC_except_table209
- GCC_except_table213
- GCC_except_table214
- GCC_except_table219
- GCC_except_table223
- GCC_except_table229
- GCC_except_table232
- GCC_except_table235
- GCC_except_table236
- GCC_except_table242
- GCC_except_table243
- GCC_except_table247
- GCC_except_table250
- GCC_except_table259
- GCC_except_table260
- GCC_except_table264
- GCC_except_table265
- GCC_except_table272
- GCC_except_table277
- GCC_except_table278
- GCC_except_table282
- GCC_except_table283
- GCC_except_table287
- GCC_except_table288
- GCC_except_table292
- GCC_except_table295
- GCC_except_table45
- GCC_except_table49
- GCC_except_table66
- GCC_except_table72
- GCC_except_table79
- GCC_except_table90
- GCC_except_table96
CStrings:
+ "@\"BKSACOAuthCredentials\"16@?0@\"NSString\"8"
+ "ACAuthenticationRequest"
+ "ACDesktopAuthenticationContext"
+ "AppleConnect authentication failed: %s"
+ "AppleConnect response missing username or OAuth tokens."
+ "AppleConnectClient framework not available."
+ "Failed to create BKSJob."
+ "No symbols returned for uuid %s: %s"
+ "Unable to allocate AppleConnect request/context."
+ "Unable to find class %s"
+ "[Symbolication] AppleConnect has no signed-in user: %s"
+ "[Symbolication] AppleConnectClient framework not available."
+ "[Symbolication] BulkSymbolication failed to produce results."
+ "[Symbolication] BulkSymbolication failed: %s"
+ "[Symbolication] BulkSymbolication framework not available."
+ "[Symbolication] BulkSymbolication returned results for %u of %lu libraries."
+ "[Symbolication] Failed to ingest BulkSymbolication JSON for uuid %s"
+ "[Symbolication] No SharedLibrary for uuid %s; skipping bulk request"
+ "[Symbolication] Submitting %zu BulkSymbolication requests for %lu libraries (skipped %zu without segment)."
+ "[Symbolication] Unable to allocate AppleConnect context for pre-flight check."
+ "no result collection returned"
+ "softlink:o:path:/AppleInternal/Library/Frameworks/AppleConnectClient.framework/AppleConnectClient"
+ "unknown"
+ "unknown error"
+ "v24@?0@\"BKSResultCollection\"8@\"NSError\"16"
+ "v24@?0r*8r*16"

```
