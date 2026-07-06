## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/Versions/A/FileProviderDaemon`

```diff

-  __TEXT.__text: 0xab053c
-  __TEXT.__objc_methlist: 0x9b9c
-  __TEXT.__const: 0x2de10
-  __TEXT.__cstring: 0x4a7c5
-  __TEXT.__oslogstring: 0x20652
-  __TEXT.__gcc_except_tab: 0xd488
+  __TEXT.__text: 0xabce68
+  __TEXT.__objc_methlist: 0x9c54
+  __TEXT.__const: 0x2de50
+  __TEXT.__cstring: 0x4ddc5
+  __TEXT.__oslogstring: 0x20762
+  __TEXT.__gcc_except_tab: 0xd68c
   __TEXT.__ustring: 0x171e
   __TEXT.__dlopen_cstrs: 0xc3
-  __TEXT.__constg_swiftt: 0x14794
-  __TEXT.__swift5_typeref: 0x149e0
-  __TEXT.__swift5_builtin: 0x8e8
-  __TEXT.__swift5_reflstr: 0xf85d
-  __TEXT.__swift5_fieldmd: 0xd04c
+  __TEXT.__constg_swiftt: 0x147e8
+  __TEXT.__swift5_typeref: 0x14b6e
+  __TEXT.__swift5_builtin: 0x8fc
+  __TEXT.__swift5_reflstr: 0xf8dd
+  __TEXT.__swift5_fieldmd: 0xd0d8
   __TEXT.__swift5_mpenum: 0x13c
   __TEXT.__swift5_assocty: 0x29c0
-  __TEXT.__swift5_capture: 0x1a7dc
+  __TEXT.__swift5_capture: 0x1a850
   __TEXT.__swift5_proto: 0x1c64
-  __TEXT.__swift5_types: 0xc48
+  __TEXT.__swift5_types: 0xc50
   __TEXT.__swift5_types2: 0x8
   __TEXT.__swift_as_entry: 0x1d4
   __TEXT.__swift_as_ret: 0x190
-  __TEXT.__swift_as_cont: 0x3dc
+  __TEXT.__swift_as_cont: 0x3d8
   __TEXT.__swift5_protos: 0xbc
-  __TEXT.__unwind_info: 0x16418
-  __TEXT.__eh_frame: 0x2d230
+  __TEXT.__unwind_info: 0x16598
+  __TEXT.__eh_frame: 0x2d6f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x978
-  __DATA_CONST.__objc_classlist: 0x5a8
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6200
+  __DATA_CONST.__objc_selrefs: 0x6250
   __DATA_CONST.__objc_protorefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x158
-  __DATA_CONST.__got: 0x1960
-  __AUTH_CONST.__const: 0x4d458
+  __DATA_CONST.__got: 0x19b8
+  __AUTH_CONST.__const: 0x4f540
   __AUTH_CONST.__cfstring: 0x75a0
-  __AUTH_CONST.__objc_const: 0x27f30
+  __AUTH_CONST.__objc_const: 0x28080
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x3068
-  __AUTH.__objc_data: 0x1b50
-  __AUTH.__data: 0x2898
+  __AUTH_CONST.__auth_got: 0x3080
+  __AUTH.__objc_data: 0x1be0
+  __AUTH.__data: 0x2678
   __DATA.__objc_ivar: 0xba0
-  __DATA.__data: 0x8110
-  __DATA.__bss: 0x27140
-  __DATA.__common: 0x21b
-  __DATA_DIRTY.__objc_data: 0x34e0
-  __DATA_DIRTY.__data: 0x10b80
-  __DATA_DIRTY.__bss: 0xf590
-  __DATA_DIRTY.__common: 0x918
+  __DATA.__data: 0x7e40
+  __DATA.__bss: 0x26830
+  __DATA.__common: 0x1fb
+  __DATA_DIRTY.__objc_data: 0x3530
+  __DATA_DIRTY.__data: 0x10fe0
+  __DATA_DIRTY.__bss: 0xfea0
+  __DATA_DIRTY.__common: 0x938
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 31542
-  Symbols:   24391
-  CStrings:  8925
+  Functions: 31623
+  Symbols:   24434
+  CStrings:  9025
 
Sections:
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types2 : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
Symbols:
+ -[FPDAppMonitor dealloc]
+ -[FPDAppMonitor waitForInitialPopulate]
+ -[FPDDomainDeadEndBackend searchableItemIdentifiersForURL:request:completionHandler:]
+ -[FPDDomainExtensionBackend searchableItemIdentifiersForURL:request:completionHandler:]
+ -[FPDXPCServicer _test_exitDaemonWithCompletionHandler:]
+ -[FPDXPCServicer _test_setForceLowDiskState:completionHandler:]
+ -[FPDXPCServicer searchableItemIdentifiersForURL:completionHandler:]
+ GCC_except_table137
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table153
+ GCC_except_table159
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table194
+ GCC_except_table195
+ GCC_except_table207
+ GCC_except_table208
+ GCC_except_table209
+ GCC_except_table213
+ GCC_except_table215
+ GCC_except_table219
+ GCC_except_table221
+ GCC_except_table226
+ GCC_except_table244
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table273
+ GCC_except_table275
+ GCC_except_table280
+ GCC_except_table281
+ GCC_except_table282
+ GCC_except_table286
+ GCC_except_table290
+ GCC_except_table291
+ GCC_except_table295
+ GCC_except_table296
+ GCC_except_table303
+ GCC_except_table307
+ GCC_except_table309
+ GCC_except_table318
+ GCC_except_table328
+ GCC_except_table335
+ GCC_except_table336
+ GCC_except_table337
+ GCC_except_table341
+ GCC_except_table346
+ GCC_except_table360
+ GCC_except_table386
+ GCC_except_table387
+ GCC_except_table388
+ GCC_except_table417
+ GCC_except_table438
+ GCC_except_table441
+ GCC_except_table454
+ GCC_except_table455
+ GCC_except_table456
+ GCC_except_table460
+ GCC_except_table464
+ GCC_except_table465
+ GCC_except_table466
+ _FPFileLockedByFlock
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSAttribute
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSTarget
+ _OBJC_CLASS_$__TtC18FileProviderDaemon27FPDExtensionKeepaliveRecord
+ _OBJC_METACLASS_$__TtC18FileProviderDaemon27FPDExtensionKeepaliveRecord
+ _OUTLINED_FUNCTION_30
+ __68-[FPDXPCServicer searchableItemIdentifiersForURL:completionHandler:]_block_invoke
+ __CLASS_METHODS__TtC18FileProviderDaemon27FPDExtensionKeepaliveRecord
+ __DATA__TtC18FileProviderDaemon27FPDExtensionKeepaliveRecord
+ __INSTANCE_METHODS__TtC18FileProviderDaemon27FPDExtensionKeepaliveRecord
+ __IVARS__TtC18FileProviderDaemon27FPDExtensionKeepaliveRecord
+ __METACLASS_DATA__TtC18FileProviderDaemon27FPDExtensionKeepaliveRecord
+ ___56-[FPDXPCServicer _test_exitDaemonWithCompletionHandler:]_block_invoke
+ ___63-[FPDXPCServicer _test_setForceLowDiskState:completionHandler:]_block_invoke
+ ___68-[FPDXPCServicer searchableItemIdentifiersForURL:completionHandler:]_block_invoke
+ ___87-[FPDDomainExtensionBackend searchableItemIdentifiersForURL:request:completionHandler:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16l
+ __swift_closure_destructor.1012Tm
+ __swift_closure_destructor.1015Tm
+ __swift_closure_destructor.1018Tm
+ __swift_closure_destructor.1021Tm
+ __swift_closure_destructor.108Tm
+ __swift_closure_destructor.1224Tm
+ __swift_closure_destructor.124Tm
+ __swift_closure_destructor.135Tm
+ __swift_closure_destructor.1558Tm
+ __swift_closure_destructor.155Tm
+ __swift_closure_destructor.1627Tm
+ __swift_closure_destructor.164Tm
+ __swift_closure_destructor.1675Tm
+ __swift_closure_destructor.1678Tm
+ __swift_closure_destructor.167Tm
+ __swift_closure_destructor.1722Tm
+ __swift_closure_destructor.1752Tm
+ __swift_closure_destructor.1763Tm
+ __swift_closure_destructor.1768Tm
+ __swift_closure_destructor.176Tm
+ __swift_closure_destructor.1847Tm
+ __swift_closure_destructor.1875Tm
+ __swift_closure_destructor.192Tm
+ __swift_closure_destructor.1950Tm
+ __swift_closure_destructor.195Tm
+ __swift_closure_destructor.196Tm
+ __swift_closure_destructor.198Tm
+ __swift_closure_destructor.2069Tm
+ __swift_closure_destructor.207Tm
+ __swift_closure_destructor.216Tm
+ __swift_closure_destructor.217Tm
+ __swift_closure_destructor.219Tm
+ __swift_closure_destructor.224Tm
+ __swift_closure_destructor.22Tm
+ __swift_closure_destructor.231Tm
+ __swift_closure_destructor.238Tm
+ __swift_closure_destructor.239Tm
+ __swift_closure_destructor.2498Tm
+ __swift_closure_destructor.251Tm
+ __swift_closure_destructor.263Tm
+ __swift_closure_destructor.2806Tm
+ __swift_closure_destructor.283Tm
+ __swift_closure_destructor.288Tm
+ __swift_closure_destructor.2919Tm
+ __swift_closure_destructor.297Tm
+ __swift_closure_destructor.3056Tm
+ __swift_closure_destructor.305Tm
+ __swift_closure_destructor.3063Tm
+ __swift_closure_destructor.306Tm
+ __swift_closure_destructor.3073Tm
+ __swift_closure_destructor.3076Tm
+ __swift_closure_destructor.309Tm
+ __swift_closure_destructor.3150Tm
+ __swift_closure_destructor.3181Tm
+ __swift_closure_destructor.324Tm
+ __swift_closure_destructor.3287Tm
+ __swift_closure_destructor.339Tm
+ __swift_closure_destructor.3425Tm
+ __swift_closure_destructor.3455Tm
+ __swift_closure_destructor.3531Tm
+ __swift_closure_destructor.3541Tm
+ __swift_closure_destructor.3544Tm
+ __swift_closure_destructor.3547Tm
+ __swift_closure_destructor.354Tm
+ __swift_closure_destructor.360Tm
+ __swift_closure_destructor.3623Tm
+ __swift_closure_destructor.3629Tm
+ __swift_closure_destructor.3638Tm
+ __swift_closure_destructor.384Tm
+ __swift_closure_destructor.405Tm
+ __swift_closure_destructor.408Tm
+ __swift_closure_destructor.4124Tm
+ __swift_closure_destructor.4168Tm
+ __swift_closure_destructor.4174Tm
+ __swift_closure_destructor.4304Tm
+ __swift_closure_destructor.444Tm
+ __swift_closure_destructor.447Tm
+ __swift_closure_destructor.450Tm
+ __swift_closure_destructor.4511Tm
+ __swift_closure_destructor.4514Tm
+ __swift_closure_destructor.4518Tm
+ __swift_closure_destructor.4521Tm
+ __swift_closure_destructor.4635Tm
+ __swift_closure_destructor.4661Tm
+ __swift_closure_destructor.4700Tm
+ __swift_closure_destructor.470Tm
+ __swift_closure_destructor.477Tm
+ __swift_closure_destructor.4817Tm
+ __swift_closure_destructor.4823Tm
+ __swift_closure_destructor.486Tm
+ __swift_closure_destructor.5038Tm
+ __swift_closure_destructor.512Tm
+ __swift_closure_destructor.5226Tm
+ __swift_closure_destructor.529Tm
+ __swift_closure_destructor.5499Tm
+ __swift_closure_destructor.5531Tm
+ __swift_closure_destructor.5834Tm
+ __swift_closure_destructor.6045Tm
+ __swift_closure_destructor.622Tm
+ __swift_closure_destructor.628Tm
+ __swift_closure_destructor.6335Tm
+ __swift_closure_destructor.6349Tm
+ __swift_closure_destructor.63Tm
+ __swift_closure_destructor.645Tm
+ __swift_closure_destructor.6555Tm
+ __swift_closure_destructor.6562Tm
+ __swift_closure_destructor.6587Tm
+ __swift_closure_destructor.69Tm
+ __swift_closure_destructor.701Tm
+ __swift_closure_destructor.728Tm
+ __swift_closure_destructor.749Tm
+ __swift_closure_destructor.758Tm
+ __swift_closure_destructor.814Tm
+ __swift_closure_destructor.848Tm
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_msgSend$keepaliveForPid:auditToken:
+ _objc_msgSend$searchableItemIdentifiersForURL:request:completionHandler:
+ _objc_msgSend$targetWithPid:
+ _objc_msgSend$waitForInitialPopulate
+ _symbolic SaySSGSg______pSgIeggg_ s5ErrorP
+ _symbolic SaySSGSg______pSgIegng_ s5ErrorP
+ _symbolic So12RBSAssertionC
+ _symbolic _____ 18FileProviderDaemon27FPDExtensionKeepaliveRecordC
+ _symbolic _____ So13audit_token_ta
+ _symbolic _____SgXw 18FileProviderDaemon27FPDExtensionKeepaliveRecordC
+ _symbolic _____SgXwz_Xx 18FileProviderDaemon27FPDExtensionKeepaliveRecordC
+ _symbolic ______A7At s6UInt32V
+ _symbolic _____y2ID_____QzG 18FileProviderDaemon21ForceIngestionTrackerV AA0A4ItemP
+ _symbolic _____ySDy2ID_____Qz_____yxq__GGG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon0C4ItemP AD18BackgroundUploaderC0G12UploadReasonO
+ _symbolic _____ySDyxSiGG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____yShy2ID_____Qy_GG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon0C4ItemP
+ _symbolic _____yShy2ID_____QzGG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon0C4ItemP
+ _symbolic _____y_____So6FPItemCq0_q1_GSgXwz_AB_AD__________SaySSGSgABRszADRs______yABGRb0______R0_AKyADGRb1______R1_AB13URLBackedItem_____Rt0_r2__lXX 18FileProviderDaemon10SyncEngineC AA7VFSItemV AA11VFSFileTreeC AA06FPFileH0C AA0aH6WriterC AA09URLBackedahJ0P AA012DomainBackedahJ0P AM
+ _symbolic _____y_____y2ID_____QzGSgG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon20InUseTrackerSnapshotV AD0C4ItemP
+ _symbolic _____y_____yq_GG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon0C20TreeChangeAggregatorV
+ _symbolic _____y_____yxG_SDy_____Shy2ID_____QzGGtG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon0C20TreeChangeAggregatorV s6UInt64V AD0C4ItemP
+ _symbolic _____y_____yxq__GG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon16ConcreteDatabaseC25DirectoryManifestInstance33_E89B838F23AA85B19E281E0E7007A7C8LLV
+ _type_layout_string So13audit_token_ta
- GCC_except_table156
- GCC_except_table161
- GCC_except_table162
- GCC_except_table163
- GCC_except_table178
- GCC_except_table187
- GCC_except_table191
- GCC_except_table192
- GCC_except_table197
- GCC_except_table198
- GCC_except_table210
- GCC_except_table211
- GCC_except_table212
- GCC_except_table216
- GCC_except_table218
- GCC_except_table222
- GCC_except_table224
- GCC_except_table232
- GCC_except_table247
- GCC_except_table254
- GCC_except_table256
- GCC_except_table278
- GCC_except_table279
- GCC_except_table283
- GCC_except_table284
- GCC_except_table285
- GCC_except_table289
- GCC_except_table293
- GCC_except_table294
- GCC_except_table298
- GCC_except_table302
- GCC_except_table306
- GCC_except_table315
- GCC_except_table316
- GCC_except_table321
- GCC_except_table331
- GCC_except_table338
- GCC_except_table343
- GCC_except_table345
- GCC_except_table347
- GCC_except_table349
- GCC_except_table363
- GCC_except_table389
- GCC_except_table390
- GCC_except_table391
- GCC_except_table420
- GCC_except_table448
- GCC_except_table452
- __swift_closure_destructor.1001Tm
- __swift_closure_destructor.102Tm
- __swift_closure_destructor.11Tm
- __swift_closure_destructor.1204Tm
- __swift_closure_destructor.147Tm
- __swift_closure_destructor.149Tm
- __swift_closure_destructor.152Tm
- __swift_closure_destructor.1554Tm
- __swift_closure_destructor.1607Tm
- __swift_closure_destructor.163Tm
- __swift_closure_destructor.1655Tm
- __swift_closure_destructor.1658Tm
- __swift_closure_destructor.166Tm
- __swift_closure_destructor.1715Tm
- __swift_closure_destructor.172Tm
- __swift_closure_destructor.1738Tm
- __swift_closure_destructor.1743Tm
- __swift_closure_destructor.1761Tm
- __swift_closure_destructor.178Tm
- __swift_closure_destructor.1827Tm
- __swift_closure_destructor.1855Tm
- __swift_closure_destructor.1958Tm
- __swift_closure_destructor.197Tm
- __swift_closure_destructor.199Tm
- __swift_closure_destructor.203Tm
- __swift_closure_destructor.2077Tm
- __swift_closure_destructor.208Tm
- __swift_closure_destructor.211Tm
- __swift_closure_destructor.218Tm
- __swift_closure_destructor.221Tm
- __swift_closure_destructor.225Tm
- __swift_closure_destructor.232Tm
- __swift_closure_destructor.245Tm
- __swift_closure_destructor.2506Tm
- __swift_closure_destructor.257Tm
- __swift_closure_destructor.2814Tm
- __swift_closure_destructor.282Tm
- __swift_closure_destructor.287Tm
- __swift_closure_destructor.291Tm
- __swift_closure_destructor.2927Tm
- __swift_closure_destructor.294Tm
- __swift_closure_destructor.303Tm
- __swift_closure_destructor.3064Tm
- __swift_closure_destructor.3071Tm
- __swift_closure_destructor.307Tm
- __swift_closure_destructor.3081Tm
- __swift_closure_destructor.3084Tm
- __swift_closure_destructor.3158Tm
- __swift_closure_destructor.3189Tm
- __swift_closure_destructor.318Tm
- __swift_closure_destructor.3295Tm
- __swift_closure_destructor.333Tm
- __swift_closure_destructor.3433Tm
- __swift_closure_destructor.3463Tm
- __swift_closure_destructor.346Tm
- __swift_closure_destructor.348Tm
- __swift_closure_destructor.3539Tm
- __swift_closure_destructor.3549Tm
- __swift_closure_destructor.3552Tm
- __swift_closure_destructor.3555Tm
- __swift_closure_destructor.3631Tm
- __swift_closure_destructor.3637Tm
- __swift_closure_destructor.363Tm
- __swift_closure_destructor.3646Tm
- __swift_closure_destructor.378Tm
- __swift_closure_destructor.393Tm
- __swift_closure_destructor.402Tm
- __swift_closure_destructor.4132Tm
- __swift_closure_destructor.4176Tm
- __swift_closure_destructor.4182Tm
- __swift_closure_destructor.429Tm
- __swift_closure_destructor.4312Tm
- __swift_closure_destructor.432Tm
- __swift_closure_destructor.4519Tm
- __swift_closure_destructor.4522Tm
- __swift_closure_destructor.4526Tm
- __swift_closure_destructor.4529Tm
- __swift_closure_destructor.454Tm
- __swift_closure_destructor.4643Tm
- __swift_closure_destructor.465Tm
- __swift_closure_destructor.4669Tm
- __swift_closure_destructor.4708Tm
- __swift_closure_destructor.474Tm
- __swift_closure_destructor.480Tm
- __swift_closure_destructor.4825Tm
- __swift_closure_destructor.4831Tm
- __swift_closure_destructor.487Tm
- __swift_closure_destructor.49Tm
- __swift_closure_destructor.5046Tm
- __swift_closure_destructor.515Tm
- __swift_closure_destructor.5234Tm
- __swift_closure_destructor.52Tm
- __swift_closure_destructor.532Tm
- __swift_closure_destructor.5507Tm
- __swift_closure_destructor.5539Tm
- __swift_closure_destructor.5842Tm
- __swift_closure_destructor.6053Tm
- __swift_closure_destructor.618Tm
- __swift_closure_destructor.624Tm
- __swift_closure_destructor.6343Tm
- __swift_closure_destructor.6357Tm
- __swift_closure_destructor.647Tm
- __swift_closure_destructor.6512Tm
- __swift_closure_destructor.6519Tm
- __swift_closure_destructor.6544Tm
- __swift_closure_destructor.697Tm
- __swift_closure_destructor.724Tm
- __swift_closure_destructor.751Tm
- __swift_closure_destructor.760Tm
- __swift_closure_destructor.810Tm
- __swift_closure_destructor.81Tm
- __swift_closure_destructor.844Tm
- __swift_closure_destructor.93Tm
- __swift_closure_destructor.946Tm
- __swift_closure_destructor.992Tm
- __swift_closure_destructor.995Tm
- __swift_closure_destructor.998Tm
- _swift_runtimeSupportsNoncopyableTypes
- get_type_metadata 15Synchronization5MutexVy18FileProviderDaemon10FPCKReportVG noncopyable
- get_type_metadata 15Synchronization5MutexVy18FileProviderDaemon12DynamicErrorVSgAFcSgG noncopyable
- get_type_metadata 15Synchronization5MutexVy18FileProviderDaemon12VFSIOContextVG noncopyable
- get_type_metadata 15Synchronization5MutexVySDySO18FileProviderDaemon14WeakEnumeratorVGG noncopyable
- get_type_metadata 15Synchronization5MutexVySDySSSiGG noncopyable
- get_type_metadata 15Synchronization5MutexVySDySo27NSFileProviderContentPolicyV04FileD6Daemon0eF18BehaviorDescriptorVGG noncopyable
- get_type_metadata 15Synchronization5MutexVySays6UInt64V_So10wharf_stepVtGG noncopyable
- get_type_metadata 15Synchronization5MutexVySbG noncopyable
- get_type_metadata 15Synchronization5MutexVySo26OS_dispatch_source_data_or_p17garbageCollection_SoAD_p15capturedContenttSgG noncopyable
- get_type_metadata 15Synchronization6AtomicVySbG noncopyable
- get_type_metadata 15Synchronization6AtomicVys6UInt64VG noncopyable
- get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_AA0A10TreeWriterCyxGRb0_ADyq_GRb1_r2_l15Synchronization5MutexVyAA20InUseTrackerSnapshotVy2IDQzGSgG noncopyable
- get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_AA0A10TreeWriterCyxGRb0_ADyq_GRb1_r2_lAA21ForceIngestionTrackerVy2IDQzG noncopyable
- get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVyAA0A20TreeChangeAggregatorVyq_GG noncopyable
- get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVyAA0A20TreeChangeAggregatorVyxG_SDys6UInt64VShy2IDQzGGtG noncopyable
- get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVyAA16ConcreteDatabaseC25DirectoryManifestInstance33_E89B838F23AA85B19E281E0E7007A7C8LLVyxq__GG noncopyable
- get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVySDy2IDQzAA18BackgroundUploaderC0H12UploadReasonOyxq__GGG noncopyable
- get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVyShy2IDQy_GG noncopyable
- get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVyShy2IDQzGG noncopyable
- get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVySo17OS_os_transaction_pSgG noncopyable
- get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization6AtomicVySbG noncopyable
- get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization6AtomicVySo45FPDExclusiveSharedSystemSchedulerWatcherStateVG noncopyable
- get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization6AtomicVys5Int64VG noncopyable
- get_type_metadata 18FileProviderDaemon0A6ItemIDRzl15Synchronization5MutexVySDyxSiGG noncopyable
- get_type_metadata l18FileProviderDaemon17VFSFileDescriptorV noncopyable
CStrings:
+ "\n   ORDER BY fp.metadata_last_used_date DESC"
+ "\n   ORDER BY fp.metadata_last_used_date DESC\n   LIMIT "
+ "\n ORDER BY bd.scheduling_timestamp\n LIMIT "
+ "\n ORDER BY bd.scheduling_timestamp DESC"
+ "\n ORDER BY bd.scheduling_timestamp DESC\n LIMIT "
+ "  SELECT fp.metadata_size\n    FROM background_downloader AS bd INDEXED BY background_downloader__reason_speculativeSet\n   INNER JOIN reconciliation_table AS rt ON (rt.fs_id = bd.id)\n   INNER JOIN fp_snapshot AS fp ON (fp.id = rt.fp_id)\n   WHERE bd.reason & "
+ "-[FPDXPCServicer _test_exitDaemonWithCompletionHandler:]"
+ "-[FPDXPCServicer _test_exitDaemonWithCompletionHandler:]_block_invoke"
+ "-[FPDXPCServicer _test_setForceLowDiskState:completionHandler:]"
+ "-[FPDXPCServicer _test_setForceLowDiskState:completionHandler:]_block_invoke"
+ "-[FPDXPCServicer searchableItemIdentifiersForURL:completionHandler:]"
+ "-[FPDXPCServicer searchableItemIdentifiersForURL:completionHandler:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/app-library/FPDFetchAppLibraryIconOperation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDAccessRight.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDDomain.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDDomainExtensionBackend.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDDomainIndexer/FPDDomainIndexer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDExtensionManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDExtensionRequestRecord.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDExtensionSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDFilePresenter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDKnownFolderAlertPresenter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDProcessMonitor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDProvider.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDPushConnection.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDSharedSystemScheduler.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDVolume.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDVolumeManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/FPDXPCServicer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/action operation engine/FPActionOperationLocator+Daemon.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDActionOperation.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDActionOperationEngine.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDItemIterator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDIterator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/action operation engine/download/FPDDownloadManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/action operation engine/move/FPDMoveReader.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/action operation engine/move/FPDMoveWriter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fileproviderd/action operation engine/move/FPDMoveWriterToProvider.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/fpfs/FPDDomainFPFSBackend.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/fpfs/FPFSGlobalProgress.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/fpfs/InternalPathsManager.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/fpfs/enumerators/ChangeEnumerator.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/fpck/PeriodicFPCK.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/BackgroundDownloaderPacer.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/FPFSSQLRestoreEngine.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/Prequelite+FSSyncAdditions.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLBackgroundDownloader.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLDatabase+DiagnosticCollection.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLDatabase+EagerlyDownload.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLDatabase+Telemetry.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLDatabase+VFSIDLookupCache.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLDatabase.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLHistoryTable.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLItemJobRegistry.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLJobRegistry.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLReconciliationTable+Search.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLReconciliationTable.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLSnapshot.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLSyncStateTable.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLThrottler.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/tree/VFSFileTree+Lookup.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/tree/VFSFileTree.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/tree/VFSItem.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/tree/VFSLookupScope.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/interfaces/file-tree/item/FileItemID.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/interfaces/job/Job.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/interfaces/job/TestingOperation.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/interfaces/persistence/JobRegistry.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/interfaces/persistence/ReconciliationTable.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/interfaces/persistence/SyncStateStore.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/interfaces/persistence/types/ItemReconciliation.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/sync-logic/ConcreteDatabase.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/sync-logic/Database+JobExecution.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/sync-logic/Maintenance.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/sync-logic/Materialization.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/sync-logic/Propagation.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/sync-logic/Reconciliation.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/utilities/PausableTimer.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/utilities/Utilities.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/libfssync/wharf/DocumentWharf.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Vnh7t4/Sources/FileProvider_executables/fssync/tests/units/FSTester/FSTester.swift"
+ "CO-ROUTINE enumeration_view\nCO-ROUTINE (subquery-3)\nCOMPOUND QUERY\nLEFT-MOST SUBQUERY\nSEARCH reconciliation_table USING COVERING INDEX reconciliation_materialized_set_opt\nUNION ALL\nSEARCH tombstone_table USING COVERING INDEX tombstone_materialized_set_opt\nSEARCH (subquery-3)\nSCAN enumeration_view"
+ "CO-ROUTINE parent_dirs\nSETUP\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nRECURSIVE STEP\nSCAN pd\nSEARCH snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nSCAN pd\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "CO-ROUTINE parent_dirs\nSETUP\nSEARCH snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nRECURSIVE STEP\nSCAN pd\nSEARCH snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nSCAN pd\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "CO-ROUTINE parent_dirs\nSETUP\nSEARCH snap USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)\nRECURSIVE STEP\nSCAN pd\nSEARCH snap USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)\nSCAN pd\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "FileProviderBackground"
+ "FileProviderDaemon.FPDExtensionKeepaliveRecord"
+ "MERGE (UNION)\nLEFT\nSEARCH background_downloader USING COVERING INDEX background_downloader__state__scheduling_timestamp (state=?)\nUSE TEMP B-TREE FOR ORDER BY\nRIGHT\nSEARCH background_downloader USING INDEX background_downloader__state__scheduling_timestamp (state=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "MULTI-INDEX OR\nINDEX 1\nSEARCH reconciliation_table USING INDEX reconciliation_background_upload_simple (fs_scheduling_state=? AND fs_scheduling_state_conditions=?)\nINDEX 2\nSEARCH reconciliation_table USING INDEX reconciliation_fp_scheduling_state (fp_scheduling_state=?)"
+ "MULTI-INDEX OR\nINDEX 1\nSEARCH reconciliation_table USING INDEX reconciliation_background_upload_simple (fs_scheduling_state=?)\nINDEX 2\nSEARCH reconciliation_table USING INDEX reconciliation_fp_scheduling_state (fp_scheduling_state=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "MULTI-INDEX OR\nINDEX 1\nSEARCH reconciliation_table USING INDEX reconciliation_is_pending (is_pending=?)\nINDEX 2\nSEARCH reconciliation_table USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "Precondition throwed error "
+ "SCAN background_downloader"
+ "SCAN bd USING INDEX background_downloader__reason_speculativeSet\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)"
+ "SCAN bd USING INDEX background_downloader__reason_speculativeSet\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SCAN parent_rt\nCORRELATED SCALAR SUBQUERY 1\nSEARCH snap USING INDEX FS_snapshot_parent_id_idx (parent_id=?)\nSEARCH child_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SCAN reconciliation_table"
+ "SCAN reconciliation_table\nUSE TEMP B-TREE FOR ORDER BY"
+ "SCAN reconciliation_table USING COVERING INDEX reconciliation_table__item_is_flocked"
+ "SCAN rt\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)"
+ "SCAN rt USING INDEX recursive_deletion_root"
+ "SCAN tombstone_table"
+ "SEARCH background_downloader USING COVERING INDEX sqlite_autoindex_background_downloader_1 (id=? AND extent_location=? AND extent_length=?)"
+ "SEARCH background_downloader USING COVERING INDEX sqlite_autoindex_background_downloader_1 (id=?)"
+ "SEARCH background_downloader USING INDEX background_downloader__state__scheduling_timestamp (state=?)"
+ "SEARCH background_downloader USING INDEX sqlite_autoindex_background_downloader_1 (id=?)"
+ "SEARCH bd USING INDEX background_downloader__state__scheduling_timestamp (state=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)"
+ "SEARCH child_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH child_rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH snap USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH jobs USING INDEX jobs_state__side__scheduling_ordering (scheduling_state=? AND side=?)\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH jobs USING INDEX jobs_state__side__scheduling_ordering (scheduling_state=? AND side=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)"
+ "SEARCH original_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH original_snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nSEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH sibling_snap USING INDEX FS_snapshot_parent_id__filename_idx (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH original_rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH original_snap USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)\nSEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH sibling_snap USING INDEX FP_snapshot_parent_id__filename_idx (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH snap USING INDEX FP_snapshot_parent_id__filename_idx (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH snap USING INDEX FP_snapshot_parent_id__filename_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH snap USING INDEX FP_snapshot_parent_id_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH snap USING INDEX FS_snapshot_parent_id__filename_idx (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH snap USING INDEX FS_snapshot_parent_id__filename_idx_other (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH snap USING INDEX FS_snapshot_parent_id_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH reconciliation_table USING COVERING INDEX reconciliation_fs_disk_import_status__fs_id (fs_disk_import_status=?)"
+ "SEARCH reconciliation_table USING COVERING INDEX reconciliation_fs_id_old_version_clone (fs_captured_content_file_id=?)"
+ "SEARCH reconciliation_table USING COVERING INDEX reconciliation_pending_set (fp_id>?)"
+ "SEARCH reconciliation_table USING COVERING INDEX reconciliation_table__item_is_flocked (item_is_flocked=?)"
+ "SEARCH reconciliation_table USING INDEX reconciliation__fp_scheduling_state__fp_id (fp_scheduling_state=? AND fp_id>?)"
+ "SEARCH reconciliation_table USING INDEX reconciliation_background_upload_simple (fs_scheduling_state=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH reconciliation_table USING INDEX reconciliation_fp_scheduling_state (fp_scheduling_state=?)"
+ "SEARCH reconciliation_table USING INDEX reconciliation_fs_disk_import_status__fp_id (fs_disk_import_status=? AND fp_id>?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH reconciliation_table USING INDEX reconciliation_fs_disk_import_status__fp_id (fs_disk_import_status=?)"
+ "SEARCH reconciliation_table USING INDEX reconciliation_fs_disk_import_status__fp_id (fs_disk_import_status=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH reconciliation_table USING INDEX reconciliation_fs_disk_import_status__fs_id (fs_disk_import_status=? AND fs_id>?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH reconciliation_table USING INDEX reconciliation_fs_disk_import_status__fs_id (fs_disk_import_status=?)"
+ "SEARCH reconciliation_table USING INDEX reconciliation_global_progress_materialize (fs_materialization_status=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH reconciliation_table USING INDEX reconciliation_is_pending (is_pending=?)"
+ "SEARCH reconciliation_table USING INDEX reconciliation_table__item_is_flocked (item_is_flocked=?)"
+ "SEARCH reconciliation_table USING INTEGER PRIMARY KEY (rowid=?)"
+ "SEARCH reconciliation_table USING INTEGER PRIMARY KEY (rowid>?)"
+ "SEARCH rt USING COVERING INDEX reconciliation_fs_id_old_version_clone (fs_captured_content_file_id>?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH rt USING INDEX reconciliation_global_progress_fp (kind=?)\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)"
+ "SEARCH rt USING INDEX reconciliation_global_progress_fs (kind=?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)"
+ "SEARCH rt USING INDEX reconciliation_global_progress_materialize (fs_materialization_status=? AND kind=?)\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)"
+ "SEARCH rt USING INDEX reconciliation_kind_last_content_change (kind=? AND last_content_change=? AND rowid>?)"
+ "SEARCH rt USING INDEX reconciliation_kind_last_content_change (kind=?)\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)"
+ "SEARCH rt USING INDEX reconciliation_table_last_change (last_change>?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?) LEFT-JOIN\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?) LEFT-JOIN"
+ "SEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?) LEFT-JOIN\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?) LEFT-JOIN"
+ "SEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?) LEFT-JOIN\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?) LEFT-JOIN"
+ "SEARCH rt USING INTEGER PRIMARY KEY (rowid>?)"
+ "SEARCH rt USING INTEGER PRIMARY KEY (rowid>?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)"
+ "SEARCH snap USING INDEX FP_snapshot_parent_id__filename_idx (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH snap USING INDEX FP_snapshot_parent_id__filename_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH snap USING INDEX FP_snapshot_parent_id_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH snap USING INDEX FS_snapshot_parent_id__filename_idx (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH snap USING INDEX FS_snapshot_parent_id_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH snap USING INDEX FS_snapshot_parent_id_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH snap USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH tombstone_table USING COVERING INDEX tombstone_materialized_set_opt (enumeration_anchor<?)"
+ "SEARCH tombstone_table USING COVERING INDEX tombstone_table_asc (last_change<?)"
+ "SEARCH tombstone_table USING COVERING INDEX tombstone_table_asc (last_change>?)"
+ "SELECT fp.metadata_size\n  FROM background_downloader AS bd\n INNER JOIN reconciliation_table AS rt ON (rt.fs_id = bd.id)\n INNER JOIN fp_snapshot AS fp ON (fp.id = rt.fp_id)\n WHERE bd.state = "
+ "[ERROR] can't get CS identifiers for URL %@ for extension %@; %@"
+ "deletion of unknown item racing with deferred ingestion on "
+ "eagerlyDownloadContentPolicyExhausted"
+ "eagerlyDownloadPinnedExhausted"
+ "extension-keepalive"
+ "failed to acquire keepalive assertion for pid %{public}d: %{public}@"
+ "fileproviderd extension keepalive"
+ "keepalive assertion for pid %{public}d invalidated"
+ "keepalive assertion for pid %{public}d invalidated: %{public}@"
+ "searchableItemIdentifiers("
+ "searchableItemIdentifiers(for:request:completionHandler:)"
+ "sharedSchedulerIsDeferred(_:)"
- "\n   ORDER BY fp.metadata_last_used_date DESC\n   "
- "\n ORDER BY bd.scheduling_timestamp\n "
- "\n ORDER BY bd.scheduling_timestamp DESC\n  "
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/app-library/FPDFetchAppLibraryIconOperation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDAccessRight.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDDomain.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDDomainExtensionBackend.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDDomainIndexer/FPDDomainIndexer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDExtensionManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDExtensionRequestRecord.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDExtensionSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDFilePresenter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDKnownFolderAlertPresenter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDProcessMonitor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDProvider.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDPushConnection.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDSharedSystemScheduler.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDVolume.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDVolumeManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/FPDXPCServicer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/action operation engine/FPActionOperationLocator+Daemon.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDActionOperation.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDActionOperationEngine.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDItemIterator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/action operation engine/FPDIterator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/action operation engine/download/FPDDownloadManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/action operation engine/move/FPDMoveReader.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/action operation engine/move/FPDMoveWriter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fileproviderd/action operation engine/move/FPDMoveWriterToProvider.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/fpfs/FPDDomainFPFSBackend.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/fpfs/FPFSGlobalProgress.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/fpfs/InternalPathsManager.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/fpfs/enumerators/ChangeEnumerator.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/fpck/PeriodicFPCK.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/BackgroundDownloaderPacer.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/FPFSSQLRestoreEngine.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/Prequelite+FSSyncAdditions.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLBackgroundDownloader.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLDatabase+DiagnosticCollection.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLDatabase+EagerlyDownload.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLDatabase+Telemetry.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLDatabase+VFSIDLookupCache.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLDatabase.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLHistoryTable.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLItemJobRegistry.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLJobRegistry.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLReconciliationTable+Search.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLReconciliationTable.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLSnapshot.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLSyncStateTable.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/persistence/SQLThrottler.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/tree/VFSFileTree+Lookup.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/tree/VFSFileTree.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/tree/VFSItem.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/implementations/file-system/tree/VFSLookupScope.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/interfaces/file-tree/item/FileItemID.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/interfaces/job/Job.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/interfaces/job/TestingOperation.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/interfaces/persistence/JobRegistry.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/interfaces/persistence/ReconciliationTable.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/interfaces/persistence/SyncStateStore.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/interfaces/persistence/types/ItemReconciliation.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/sync-logic/ConcreteDatabase.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/sync-logic/Database+JobExecution.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/sync-logic/Maintenance.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/sync-logic/Materialization.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/sync-logic/Propagation.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/sync-logic/Reconciliation.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/utilities/PausableTimer.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/utilities/Utilities.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/libfssync/wharf/DocumentWharf.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7aDZaP/Sources/FileProvider_executables/fssync/tests/units/FSTester/FSTester.swift"
- "fp.metadata_size"

```
