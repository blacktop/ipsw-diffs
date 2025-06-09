## Search

> `/System/Library/PrivateFrameworks/Search.framework/Search`

```diff

-2333.50.1.0.0
-  __TEXT.__text: 0x25440
+2374.0.1.0.0
+  __TEXT.__text: 0x25744
   __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_methlist: 0x2488
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x2cfd
-  __TEXT.__gcc_except_tab: 0x504
-  __TEXT.__oslogstring: 0x15d8
+  __TEXT.__objc_methlist: 0x24a8
+  __TEXT.__const: 0x128
+  __TEXT.__cstring: 0x2d39
+  __TEXT.__gcc_except_tab: 0x52c
+  __TEXT.__oslogstring: 0x15fb
   __TEXT.__unwind_info: 0x9a8
-  __TEXT.__objc_classname: 0x3ad
-  __TEXT.__objc_methname: 0x6f30
-  __TEXT.__objc_methtype: 0xba7
-  __TEXT.__objc_stubs: 0x5160
-  __DATA_CONST.__got: 0x568
-  __DATA_CONST.__const: 0xa48
+  __TEXT.__objc_classname: 0x3c8
+  __TEXT.__objc_methname: 0x6f51
+  __TEXT.__objc_methtype: 0xbd3
+  __TEXT.__objc_stubs: 0x5180
+  __DATA_CONST.__got: 0x590
+  __DATA_CONST.__const: 0xa70
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cd0
+  __DATA_CONST.__objc_selrefs: 0x1cd8
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x730
   __AUTH_CONST.__const: 0x6c0
-  __AUTH_CONST.__cfstring: 0x3600
-  __AUTH_CONST.__objc_const: 0x5910
+  __AUTH_CONST.__cfstring: 0x3620
+  __AUTH_CONST.__objc_const: 0x5938
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x324
-  __DATA.__data: 0x4d8
+  __DATA.__data: 0x538
+  __DATA.__bss: 0xa0
   __DATA.__common: 0xe
-  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x668
+  __DATA_DIRTY.__bss: 0x688
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight

   - /System/Library/PrivateFrameworks/People.framework/People
   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
+  - /System/Library/PrivateFrameworks/SearchIntrospectionKit.framework/SearchIntrospectionKit
   - /System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon
   - /System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6CE9AC7F-874F-303F-BDA4-35CF77AF1F8D
-  Functions: 1054
-  Symbols:   3982
-  CStrings:  2601
+  UUID: BB651AB3-92BE-3F46-A1B7-E065486DC37C
+  Functions: 1057
+  Symbols:   4003
+  CStrings:  2608
 
Symbols:
+ -[SPFeedbackManager sendResultSectionsDidLoadFeedback:]
+ GCC_except_table53
+ GCC_except_table87
+ GCC_except_table88
+ _OBJC_CLASS_$_SFResultSectionsDidLoadFeedback
+ _OBJC_CLASS_$_SIFeedbackListener
+ _SPCopyVisibleApps.onceToken
+ _SPCopyVisibleApps.sVisibleAppSet
+ _SSSectionIdentifierSearchThrough
+ _SSSectionIdentifierSyndicatedFilesMessages
+ _SSSectionIdentifierZKWSiriActions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SIFeedbackListenerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SIFeedbackListenerProtocol
+ __OBJC_$_PROTOCOL_REFS_SIFeedbackListenerProtocol
+ __OBJC_LABEL_PROTOCOL_$_SIFeedbackListenerProtocol
+ __OBJC_PROTOCOL_$_SIFeedbackListenerProtocol
+ ___36-[SPDaemonQueryToken handleMessage:]_block_invoke.32
+ ___36-[SPDaemonQueryToken handleMessage:]_block_invoke_2.40
+ ___36-[SPDaemonQueryToken handleMessage:]_block_invoke_3.42
+ ___68-[SPSearchFeedbackProxy sendFeedbackType:feedback:queryId:clientID:]_block_invoke.266
+ ___68-[SPSearchFeedbackProxy sendFeedbackType:feedback:queryId:clientID:]_block_invoke.266.cold.1
+ ___68-[SPSearchFeedbackProxy sendFeedbackType:feedback:queryId:clientID:]_block_invoke.266.cold.2
+ ___68-[SPSearchFeedbackProxy sendFeedbackType:feedback:queryId:clientID:]_block_invoke.267
+ ___SPCopyVisibleApps_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_literal_global.146
+ ___block_literal_global.149
+ ___block_literal_global.152
+ ___block_literal_global.214
+ ___block_literal_global.245
+ ___block_literal_global.257
+ ___block_literal_global.263
+ _objc_msgSend$sendResultSectionsDidLoadFeedback:
+ _updatedVisibleApps
- GCC_except_table51
- GCC_except_table85
- GCC_except_table86
- ___36-[SPDaemonQueryToken handleMessage:]_block_invoke.20
- ___36-[SPDaemonQueryToken handleMessage:]_block_invoke_2.28
- ___36-[SPDaemonQueryToken handleMessage:]_block_invoke_3.30
- ___68-[SPSearchFeedbackProxy sendFeedbackType:feedback:queryId:clientID:]_block_invoke.261
- ___68-[SPSearchFeedbackProxy sendFeedbackType:feedback:queryId:clientID:]_block_invoke.261.cold.1
- ___68-[SPSearchFeedbackProxy sendFeedbackType:feedback:queryId:clientID:]_block_invoke.261.cold.2
- ___68-[SPSearchFeedbackProxy sendFeedbackType:feedback:queryId:clientID:]_block_invoke.262
- ___block_literal_global.159
- ___block_literal_global.161
- ___block_literal_global.164
- ___block_literal_global.210
- ___block_literal_global.240
- ___block_literal_global.252
- ___block_literal_global.258
CStrings:
+ "DOMAIN_SYNDICATED_FILES_FROM_MESSAGES"
+ "ResultSectionsDidLoad"
+ "SIFeedbackListenerProtocol"
+ "T@\"SPSearchQueryContext\",R,V_queryContext"
+ "Updated visible apps:%lu, first:%d"
+ "sendResultSectionsDidLoadFeedback:"
+ "v24@0:8@\"SFResultSectionsDidLoadFeedback\"16"
- "T@\"SPSearchQueryContext\",R,N,V_queryContext"

```
