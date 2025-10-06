## CoreDuetContext

> `/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext`

```diff

-1852.4.2.0.3
-  __TEXT.__text: 0x33e20
-  __TEXT.__auth_stubs: 0x8e0
+1852.4.7.0.3
+  __TEXT.__text: 0x33bc0
+  __TEXT.__auth_stubs: 0x8c0
   __TEXT.__objc_methlist: 0x2dfc
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x2692
+  __TEXT.__cstring: 0x249d
   __TEXT.__oslogstring: 0x3144
-  __TEXT.__gcc_except_tab: 0xbdc
+  __TEXT.__gcc_except_tab: 0xbe0
   __TEXT.__dlopen_cstrs: 0xbb
   __TEXT.__unwind_info: 0xe08
   __TEXT.__objc_classname: 0x59f

   __TEXT.__objc_methtype: 0x15a7
   __TEXT.__objc_stubs: 0x5060
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0xde8
+  __DATA_CONST.__const: 0xd48
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0

   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x480
+  __AUTH_CONST.__auth_got: 0x470
   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x240
   __DATA.__objc_superrefs: 0xa0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2670781F-5ED0-3401-B7BE-5E9E4551A44D
-  Functions: 1431
-  Symbols:   4797
-  CStrings:  2631
+  UUID: 910B975A-CA6D-37D6-8DF6-64C0CF25FD01
+  Functions: 1427
+  Symbols:   4783
+  CStrings:  2627
 
Symbols:
+ GCC_except_table101
+ GCC_except_table109
+ GCC_except_table117
+ GCC_except_table123
+ GCC_except_table129
+ GCC_except_table134
+ GCC_except_table31
+ GCC_except_table38
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table80
+ GCC_except_table85
+ GCC_except_table93
+ ___108-[_CDClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.152
+ ___111-[_CDClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.148
+ ___45-[_CDInMemoryContext addCallback:forKeyPath:]_block_invoke.27
+ ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.127
+ ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.127.cold.1
+ ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.130
+ ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.130.cold.1
+ ___47-[_CDUserContextServerClient registerCallback:]_block_invoke_2.cold.1
+ ___54-[_CDUserContextServerClient _valuesForPaths:handler:]_block_invoke.143
+ ___66-[_CDClientContext valuesForKeyPaths:inContextsMatchingPredicate:]_block_invoke.155
+ ___68-[_CDClientContext setObject:lastModifiedDate:forContextualKeyPath:]_block_invoke.158
+ ___69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke.122
+ ___69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke_2.123
+ ___69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke_2.cold.1
+ ___79-[_CDClientContext valuesForKeyPaths:synchronous:responseQueue:withCompletion:]_block_invoke.156
+ ___79-[_CDUserContextServerClient performRegistrationCallbackWithRegistration:info:]_block_invoke.135
+ ___89-[_CDClientContext addObjects:toArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.143
+ ___92-[_CDClientContext setObject:forContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.141
+ ___94-[_CDClientContext removeObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.145
+ ___block_literal_global.121
+ ___block_literal_global.129
+ ___block_literal_global.132
+ ___block_literal_global.134
+ ___block_literal_global.141
+ ___cd_dispatch_async_capture_tx_block_invoke
- GCC_except_table10
- GCC_except_table102
- GCC_except_table110
- GCC_except_table118
- GCC_except_table124
- GCC_except_table130
- GCC_except_table135
- GCC_except_table47
- GCC_except_table50
- GCC_except_table66
- GCC_except_table81
- GCC_except_table83
- GCC_except_table86
- GCC_except_table94
- ___108-[_CDClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.155
- ___111-[_CDClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.151
- ___45-[_CDInMemoryContext addCallback:forKeyPath:]_block_invoke.28
- ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.131
- ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.131.cold.1
- ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.134
- ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.134.cold.1
- ___47-[_CDUserContextServerClient registerCallback:]_block_invoke_4
- ___47-[_CDUserContextServerClient registerCallback:]_block_invoke_4.cold.1
- ___52-[_CDUserContextServerClient _valueForPath:handler:]_block_invoke_2
- ___54-[_CDUserContextServerClient _valuesForPaths:handler:]_block_invoke.147
- ___56-[_CDClientContext handleContextualChange:info:handler:]_block_invoke_2
- ___58-[_CDUserContextServerClient _hasKnowledgeOfPath:handler:]_block_invoke_3
- ___66-[_CDClientContext valuesForKeyPaths:inContextsMatchingPredicate:]_block_invoke.156
- ___66-[_CDInMemoryContext locationCoordinatorCircularRegionsDidChange:]_block_invoke_2
- ___68-[_CDClientContext setObject:lastModifiedDate:forContextualKeyPath:]_block_invoke.159
- ___69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke.124
- ___69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke_2.125
- ___69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke_3
- ___69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke_3.126
- ___69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke_3.cold.1
- ___79-[_CDClientContext valuesForKeyPaths:synchronous:responseQueue:withCompletion:]_block_invoke.157
- ___79-[_CDUserContextServerClient performRegistrationCallbackWithRegistration:info:]_block_invoke.139
- ___89-[_CDClientContext addObjects:toArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.145
- ___92-[_CDClientContext setObject:forContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.143
- ___94-[_CDClientContext removeObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.148
- ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs80bs_e5_v8?0ls32l8s40l8s48l8s72l8s80l8s56l8s64l8
- ___block_literal_global.123
- ___block_literal_global.133
- ___block_literal_global.136
- ___block_literal_global.138
- ___block_literal_global.145
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
CStrings:
+ "cd_dispatch_async_tx"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDClientContext.m:952"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDInMemoryContext.m:137"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:233"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:268"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:423"

```
