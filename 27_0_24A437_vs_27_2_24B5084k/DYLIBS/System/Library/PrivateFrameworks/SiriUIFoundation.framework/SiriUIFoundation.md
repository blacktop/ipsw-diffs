## SiriUIFoundation

> `/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation`

```diff

-3600.55.37.11.4
-  __TEXT.__text: 0x8ca68
-  __TEXT.__objc_methlist: 0x4748
-  __TEXT.__const: 0x387c
-  __TEXT.__cstring: 0x6676
+3605.22.2.0.0
+  __TEXT.__text: 0x8d0e0
+  __TEXT.__objc_methlist: 0x4768
+  __TEXT.__const: 0x38bc
+  __TEXT.__cstring: 0x66e6
   __TEXT.__oslogstring: 0x6fab
-  __TEXT.__gcc_except_tab: 0x984
+  __TEXT.__gcc_except_tab: 0xa28
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__swift5_typeref: 0x1594
-  __TEXT.__swift5_capture: 0x734
+  __TEXT.__swift5_typeref: 0x15aa
+  __TEXT.__swift5_capture: 0x77c
   __TEXT.__constg_swiftt: 0x14d4
-  __TEXT.__swift5_reflstr: 0x10fa
-  __TEXT.__swift5_fieldmd: 0xf7c
+  __TEXT.__swift5_reflstr: 0x111a
+  __TEXT.__swift5_fieldmd: 0xf94
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_proto: 0x254
   __TEXT.__swift5_types: 0x130
-  __TEXT.__swift_as_entry: 0xe8
+  __TEXT.__swift_as_entry: 0xec
   __TEXT.__swift_as_ret: 0xfc
-  __TEXT.__swift_as_cont: 0x180
+  __TEXT.__swift_as_cont: 0x188
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x2f10
-  __TEXT.__eh_frame: 0x23c8
+  __TEXT.__unwind_info: 0x2f50
+  __TEXT.__eh_frame: 0x2458
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19b0
+  __DATA_CONST.__const: 0x19d8
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2fa8
+  __DATA_CONST.__objc_selrefs: 0x2fc0
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0xa98
-  __AUTH_CONST.__const: 0x3aa1
+  __AUTH_CONST.__const: 0x3b41
   __AUTH_CONST.__cfstring: 0x23c0
-  __AUTH_CONST.__objc_const: 0x9080
+  __AUTH_CONST.__objc_const: 0x90a0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xf40
+  __AUTH_CONST.__auth_got: 0xf28
   __AUTH.__objc_data: 0x1170
   __AUTH.__data: 0xc28
-  __DATA.__objc_ivar: 0x438
+  __DATA.__objc_ivar: 0x43c
   __DATA.__data: 0x1750
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0xf48
-  __DATA_DIRTY.__data: 0x9d0
+  __DATA_DIRTY.__data: 0x9e0
   __DATA_DIRTY.__bss: 0x208
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3376
-  Symbols:   4837
-  CStrings:  1129
+  Functions: 3392
+  Symbols:   4848
+  CStrings:  1132
 
Symbols:
+ +[SRUIFIntelligenceFlowFeatureFlag(SWEFeatureFlags) isDashboardCampoEnabled]
+ +[SRUIFSiriFeatureFlag(SWEFeatureFlags) isContinuousConversationHomepodEnabled]
+ _AFIsHorseman
+ _OBJC_IVAR_$_SRUIFAceCommandRecords._recordsQueue
+ ___47-[SRUIFAceCommandRecords _recordForAceCommand:]_block_invoke
+ ___51-[SRUIFAceCommandRecords aceCommandWithIdentifier:]_block_invoke
+ ___56-[SRUIFAceCommandRecords registerAceCommand:completion:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8
+ ___swift_closure_destructor.64Tm
+ __dispatch_queue_attr_concurrent
+ _dispatch_barrier_sync
+ _objc_msgSend$allValues
+ _objc_msgSend$isContinuousConversationHomepodEnabled
+ _objc_msgSend$sendEmphasisUpdateWithIdentifier:appBundleId:personaId:completionHandler:
+ _objc_msgSend$setInteractionLinkId:
+ _objc_msgSend$setLogLinkId:
+ _symbolic So8NSStringC
+ _symbolic So8NSStringCSg
- ___block_descriptor_48_e8_32s40s_e48_v32?0"NSString"8"SRUIFAceCommandRecord"16^B24ls32l8s40l8
- ___swift_closure_destructor.57Tm
- _objc_msgSend$_recordsByCommandIdentifier
- _objc_msgSend$aceCommandWithIdentifier:
- _objc_msgSend$setSiriAceViewId:
- _objc_msgSend$setSiriInputStreamId:
- _objc_msgSend$setSiriRequestId:
- _symbolic _____Sg 18AppIntentsServices0bC0O14InterfaceIdiomO
CStrings:
+ "-[SRUIFAceCommandRecords registerAceCommand:completion:]_block_invoke"
+ "DashboardCampo"
+ "com.apple.siriui.SRUIFAceCommandRecords"
+ "continuous_conversation_homepod"
- "v32@?0@\"NSString\"8@\"SRUIFAceCommandRecord\"16^B24"
```
