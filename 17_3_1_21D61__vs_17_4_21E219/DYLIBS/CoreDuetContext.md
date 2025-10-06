## CoreDuetContext

> `/System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext`

```diff

-1852.6.1.0.0
-  __TEXT.__text: 0x33bc0
+1852.19.0.2.0
+  __TEXT.__text: 0x33b4c
   __TEXT.__auth_stubs: 0x8c0
   __TEXT.__objc_methlist: 0x2dfc
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x249d
+  __TEXT.__cstring: 0x24a1
   __TEXT.__oslogstring: 0x3144
   __TEXT.__gcc_except_tab: 0xbe0
   __TEXT.__dlopen_cstrs: 0xbb
   __TEXT.__unwind_info: 0xe08
   __TEXT.__objc_classname: 0x59f
-  __TEXT.__objc_methname: 0x8ac4
+  __TEXT.__objc_methname: 0x8ad6
   __TEXT.__objc_methtype: 0x15a7
   __TEXT.__objc_stubs: 0x5060
   __DATA_CONST.__got: 0x108

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4130
   __DATA_CONST.__objc_selrefs: 0x2020
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x240
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0x3100
+  __AUTH_CONST.__cfstring: 0x3120
   __AUTH_CONST.__const: 0xe20
   __AUTH_CONST.__objc_const: 0xd68
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x470
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x240
-  __DATA.__objc_superrefs: 0xa0
   __DATA.__objc_ivar: 0x1a8
-  __DATA.__data: 0xa50
-  __DATA.__bss: 0x231
+  __DATA.__data: 0xa60
+  __DATA.__bss: 0x221
   __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x368

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1701F89-C79D-31B4-B87E-3E6A1CB72185
+  UUID: 305F8350-672C-3F8B-AB73-A914D4D7A0B7
   Functions: 1427
   Symbols:   4783
-  CStrings:  2627
+  CStrings:  2630
 
Symbols:
+ ___108-[_CDClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.155
+ ___111-[_CDClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.151
+ ___37-[_CDClientContext registerCallback:]_block_invoke.139
+ ___37-[_CDClientContext registerCallback:]_block_invoke_2.140
+ ___37-[_CDClientContext registerCallback:]_block_invoke_2.140.cold.1
+ ___38-[_CDClientContext evaluatePredicate:]_block_invoke.141
+ ___43-[_CDClientContext subscribeToEventStreams]_block_invoke.117
+ ___43-[_CDClientContext subscribeToEventStreams]_block_invoke.119
+ ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.128
+ ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.128.cold.1
+ ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.131
+ ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.131.cold.1
+ ___52-[_CDClientContext hasKnowledgeOfContextualKeyPath:]_block_invoke.129
+ ___54-[_CDUserContextServerClient _valuesForPaths:handler:]_block_invoke.144
+ ___66-[_CDClientContext valuesForKeyPaths:inContextsMatchingPredicate:]_block_invoke.156
+ ___68-[_CDClientContext setObject:lastModifiedDate:forContextualKeyPath:]_block_invoke.159
+ ___69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke.123
+ ___69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke_2.124
+ ___79-[_CDClientContext valuesForKeyPaths:synchronous:responseQueue:withCompletion:]_block_invoke.157
+ ___79-[_CDUserContextServerClient performRegistrationCallbackWithRegistration:info:]_block_invoke.136
+ ___88-[_CDClientContext objectForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.130
+ ___88-[_CDClientContext objectForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.132
+ ___88-[_CDClientContext objectForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke_2.133
+ ___89-[_CDClientContext addObjects:toArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.145
+ ___92-[_CDClientContext setObject:forContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.143
+ ___94-[_CDClientContext removeObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.148
+ ___98-[_CDClientContext lastModifiedDateForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.135
+ ___block_literal_global.100
+ ___block_literal_global.115
+ ___block_literal_global.122
+ ___block_literal_global.125
+ ___block_literal_global.130
+ ___block_literal_global.133
+ ___block_literal_global.89
+ ___block_literal_global.96
- ___108-[_CDClientContext addObjects:andRemoveObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.152
- ___111-[_CDClientContext removeObjectsMatchingPredicate:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.148
- ___37-[_CDClientContext registerCallback:]_block_invoke.138
- ___37-[_CDClientContext registerCallback:]_block_invoke_2.139
- ___37-[_CDClientContext registerCallback:]_block_invoke_2.139.cold.1
- ___38-[_CDClientContext evaluatePredicate:]_block_invoke.140
- ___43-[_CDClientContext subscribeToEventStreams]_block_invoke.116
- ___43-[_CDClientContext subscribeToEventStreams]_block_invoke.118
- ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.127
- ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.127.cold.1
- ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.130
- ___47-[_CDUserContextServerClient registerCallback:]_block_invoke.130.cold.1
- ___52-[_CDClientContext hasKnowledgeOfContextualKeyPath:]_block_invoke.128
- ___54-[_CDUserContextServerClient _valuesForPaths:handler:]_block_invoke.143
- ___66-[_CDClientContext valuesForKeyPaths:inContextsMatchingPredicate:]_block_invoke.155
- ___68-[_CDClientContext setObject:lastModifiedDate:forContextualKeyPath:]_block_invoke.158
- ___69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke.122
- ___69-[_CDUserContextServerClient handlePreviouslyFiredRegistration:info:]_block_invoke_2.123
- ___79-[_CDClientContext valuesForKeyPaths:synchronous:responseQueue:withCompletion:]_block_invoke.156
- ___79-[_CDUserContextServerClient performRegistrationCallbackWithRegistration:info:]_block_invoke.135
- ___88-[_CDClientContext objectForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.129
- ___88-[_CDClientContext objectForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.131
- ___88-[_CDClientContext objectForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke_2.132
- ___89-[_CDClientContext addObjects:toArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.143
- ___92-[_CDClientContext setObject:forContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.141
- ___94-[_CDClientContext removeObjects:fromArrayAtKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.145
- ___98-[_CDClientContext lastModifiedDateForContextualKeyPath:synchronous:responseQueue:withCompletion:]_block_invoke.134
- ___block_literal_global.114
- ___block_literal_global.121
- ___block_literal_global.124
- ___block_literal_global.129
- ___block_literal_global.132
- ___block_literal_global.134
- ___block_literal_global.141
- ___block_literal_global.88
- ___block_literal_global.95
- ___block_literal_global.99
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:1089"
+ "T@\"NSString\",?,R,C"
+ "nil"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CDUserContext/CDUserContext/_CDUserContextServerClient.m:1103"

```
