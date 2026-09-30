## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-1325.12.0.0.0
-  __TEXT.__text: 0x4424c
-  __TEXT.__auth_stubs: 0x1190
-  __TEXT.__const: 0x500
-  __TEXT.__gcc_except_tab: 0x268
-  __TEXT.__oslogstring: 0x7668
-  __TEXT.__cstring: 0x8c9f
-  __TEXT.__unwind_info: 0x628
+1325.17.0.0.0
+  __TEXT.__text: 0x45a7c
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__const: 0x518
+  __TEXT.__gcc_except_tab: 0x2d8
+  __TEXT.__oslogstring: 0x78f8
+  __TEXT.__cstring: 0x8f69
+  __TEXT.__unwind_info: 0x670
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x107
-  __TEXT.__objc_stubs: 0x180
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x380
+  __TEXT.__objc_methname: 0x11b
+  __TEXT.__objc_stubs: 0x1a0
+  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__const: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x8d8
-  __AUTH_CONST.__const: 0x10e8
+  __DATA_CONST.__objc_selrefs: 0x68
+  __AUTH_CONST.__auth_got: 0x908
+  __AUTH_CONST.__const: 0x1108
   __AUTH_CONST.__cfstring: 0xb60
   __DATA.__data: 0x1
   __DATA.__common: 0x3c
-  __DATA.__bss: 0x160
+  __DATA.__bss: 0x178
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B8A9D639-9C92-3208-92AA-BAE8C5E04F2B
-  Functions: 515
-  Symbols:   1109
-  CStrings:  1395
+  UUID: 9C4CB9EB-34EF-3A1D-B4AB-69FC699A6FAF
+  Functions: 522
+  Symbols:   1135
+  CStrings:  1421
 
Symbols:
+ GCC_except_table150
+ GCC_except_table268
+ GCC_except_table328
+ GCC_except_table329
+ GCC_except_table374
+ GCC_except_table385
+ GCC_except_table386
+ GCC_except_table388
+ GCC_except_table390
+ GCC_except_table391
+ GCC_except_table452
+ GCC_except_table517
+ GCC_except_table61
+ GCC_except_table64
+ GCC_except_table69
+ GCC_except_table72
+ _WriteStackshotReport
+ __ZL15gStackshotQueue
+ __ZN11CCConfigure20getLogTapWithContextEP18CCConfigureContext
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__114__split_bufferIP14StackshotEntryNS_9allocatorIS2_EEE12emplace_backIJRS2_EEEvDpOT_
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__15dequeI14StackshotEntryNS_9allocatorIS1_EEED2B9foe210106Ev
+ __ZNSt3__19allocatorIP14StackshotEntryE17allocate_at_leastB9foe210106Em
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ __ZTISt20bad_array_new_length
+ __ZZ16triggerStackshotE9onceToken
+ __ZdlPv
+ ____ZN12CCXPCService21handleIncomingMessageEP17_xpc_connection_sPv_block_invoke.26
+ ___block_descriptor_48_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_tmp.1806
+ ___block_descriptor_tmp.1867
+ ___block_descriptor_tmp.1960
+ ___block_descriptor_tmp.2234
+ ___block_descriptor_tmp.23
+ ___block_descriptor_tmp.2353
+ ___block_descriptor_tmp.27
+ ___block_descriptor_tmp.32
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.44
+ ___block_descriptor_tmp.819
+ ___block_literal_global.1232
+ ___block_literal_global.148
+ ___block_literal_global.153
+ ___block_literal_global.1865
+ ___block_literal_global.2174
+ ___block_literal_global.29
+ ___block_literal_global.63
+ ___block_literal_global.81
+ ___block_literal_global.814
+ ___freeCCCommonResources_block_invoke
+ ___triggerStackshot_block_invoke
+ ___triggerStackshot_block_invoke.85
+ _memmove
+ _objc_alloc
+ _objc_msgSend$initWithUTF8String:
+ _objc_release_x20
+ _triggerStackshot
- GCC_except_table149
- GCC_except_table269
- GCC_except_table367
- GCC_except_table378
- GCC_except_table379
- GCC_except_table381
- GCC_except_table383
- GCC_except_table384
- GCC_except_table445
- GCC_except_table510
- GCC_except_table60
- GCC_except_table62
- GCC_except_table68
- GCC_except_table71
- ____ZN12CCXPCService21handleIncomingMessageEP17_xpc_connection_sPv_block_invoke.20
- ____ZN15CCPipeInterface13freeResourcesEv_block_invoke_2
- ____ZN8CCLogTap11tapLoopImplEv_block_invoke
- ___block_descriptor_tmp.14
- ___block_descriptor_tmp.1797
- ___block_descriptor_tmp.1858
- ___block_descriptor_tmp.1951
- ___block_descriptor_tmp.21
- ___block_descriptor_tmp.2210
- ___block_descriptor_tmp.2329
- ___block_descriptor_tmp.26
- ___block_descriptor_tmp.26.2137
- ___block_descriptor_tmp.30
- ___block_descriptor_tmp.38
- ___block_descriptor_tmp.610
- ___block_descriptor_tmp.824
- ___block_literal_global.1263
- ___block_literal_global.134
- ___block_literal_global.139
- ___block_literal_global.16
- ___block_literal_global.1856
- ___block_literal_global.2166
- ___block_literal_global.23
- ___block_literal_global.818
CStrings:
+ "%s:%06u Daily stackshot limit reached (%zu stackshots). Skipping stackshot for id %s (reason: %s)\n"
+ "%s:%06u Invalid captureId"
+ "%s:%06u Invalid reason"
+ "%s:%06u Stackshot rate limit: a stackshot was triggered within the last %d seconds. Skipping stackshot for id %s (reason: %s)\n"
+ "%s:%06u Triggering stackshot with id %s due to %s\n"
+ "%s:%06u Unable to copy arguments"
+ "%u.%06u"
+ "CCConfigure::watermarkLevel"
+ "CCLogTap::%s:%d cast failed\n"
+ "CCXPCService::handleIncomingMessage Unable to allocate config data\n"
+ "CCXPCService::handleIncomingMessage Unable to allocate scratch buffer\n"
+ "CCXPCService::handleIncomingMessage Unable to get remote connection\n"
+ "CCXPCService::handleIncomingMessage XPC message is not dictionary\n"
+ "CCXPCService::handleIncomingMessage empty configuration\n"
+ "initWithUTF8String:"
+ "triggerStackshot"
+ "triggerStackshot_block_invoke"
- "CCLogTap::tapLoopImpl() entry:%u failed to get pipe interface \n"
- "tapLoopImpl_block_invoke"

```
