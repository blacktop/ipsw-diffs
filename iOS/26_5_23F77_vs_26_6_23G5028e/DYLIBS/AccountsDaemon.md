## AccountsDaemon

> `/System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon`

```diff

-1036.0.0.0.0
-  __TEXT.__text: 0x7fc48
-  __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_methlist: 0x3c34
+1037.0.0.0.0
+  __TEXT.__text: 0x80018
+  __TEXT.__auth_stubs: 0x1770
+  __TEXT.__objc_methlist: 0x3c4c
   __TEXT.__const: 0xc2a
   __TEXT.__oslogstring: 0x89ea
-  __TEXT.__cstring: 0x3b23
+  __TEXT.__cstring: 0x3b43
   __TEXT.__gcc_except_tab: 0x25b4
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__swift5_typeref: 0x5de
+  __TEXT.__swift5_typeref: 0x5e2
   __TEXT.__constg_swiftt: 0x384
   __TEXT.__swift5_reflstr: 0x24b
   __TEXT.__swift5_fieldmd: 0x230
-  __TEXT.__swift5_capture: 0x268
+  __TEXT.__swift5_capture: 0x26c
   __TEXT.__swift5_proto: 0x58
   __TEXT.__swift5_types: 0x38
   __TEXT.__swift_as_entry: 0x4c

   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1db0
-  __TEXT.__eh_frame: 0x9b0
+  __TEXT.__unwind_info: 0x1db8
+  __TEXT.__eh_frame: 0x9b8
   __TEXT.__objc_classname: 0x739
   __TEXT.__objc_methname: 0xb6e9
   __TEXT.__objc_methtype: 0x2649
   __TEXT.__objc_stubs: 0x9380
   __DATA_CONST.__got: 0xd68
-  __DATA_CONST.__const: 0x1690
+  __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0xbd0
-  __AUTH_CONST.__const: 0xc70
-  __AUTH_CONST.__cfstring: 0x32a0
-  __AUTH_CONST.__objc_const: 0x4ae8
+  __AUTH_CONST.__auth_got: 0xbc8
+  __AUTH_CONST.__const: 0xc50
+  __AUTH_CONST.__cfstring: 0x32c0
+  __AUTH_CONST.__objc_const: 0x4af8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x368

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: AF6A5571-3FF2-31AA-9223-ACC3C90CB022
-  Functions: 2316
-  Symbols:   7322
-  CStrings:  3513
+  UUID: 2D2BC7F9-24D6-33C1-88D3-9FA3B8A24E83
+  Functions: 2320
+  Symbols:   7326
+  CStrings:  3516
 
Symbols:
+ -[ACDDatabaseConnection lastAnalyticsSendInterval]
+ -[ACDDatabaseConnection setLastAnalyticsSendInterval:]
+ GCC_except_table26
+ GCC_except_table54
+ ___62-[ACDAccountStore credentialForAccountWithIdentifier:handler:]_block_invoke.149
+ ___65-[ACDAccountStore renewCredentialsForAccount:options:completion:]_block_invoke.207
+ ___65-[ACDAccountStore renewCredentialsForAccount:options:completion:]_block_invoke_2.209
+ ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.192
+ ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.194
+ ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.194.cold.1
+ ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.194.cold.2
+ ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.198
+ ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.198.cold.1
+ ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.198.cold.2
+ ___block_descriptor_48_e8_32s_e8_v16?0q8ls32l8
+ ___block_literal_global.200
+ ___block_literal_global.230
+ _objc_msgSend$lastAnalyticsSendInterval
+ _objc_msgSend$postMonthlyAnalytics:completionHandler:
+ _objc_msgSend$setLastAnalyticsSendInterval:
+ _symbolic SiIeyBy_
- GCC_except_table52
- ___62-[ACDAccountStore credentialForAccountWithIdentifier:handler:]_block_invoke.150
- ___65-[ACDAccountStore renewCredentialsForAccount:options:completion:]_block_invoke.208
- ___65-[ACDAccountStore renewCredentialsForAccount:options:completion:]_block_invoke_2.210
- ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.193
- ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.195
- ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.195.cold.1
- ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.195.cold.2
- ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.199
- ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.199.cold.1
- ___66-[ACDAccountStore saveAccount:verify:dataclassActions:completion:]_block_invoke.199.cold.2
- ___block_literal_global.201
- ___block_literal_global.231
- ___block_literal_global.68
- _objc_msgSend$doubleValue
- _objc_msgSend$initWithDouble:
- _objc_msgSend$postMonthlyAnalyticsWithCompletionHandler:
- _symbolic IeyB_
CStrings:
+ "ACAnalyticsLastSentInterval"
+ "lastAnalyticsSendInterval"
+ "postMonthlyAnalytics:completionHandler:"
+ "setLastAnalyticsSendInterval:"
+ "v16@?0q8"
+ "v32@0:8q16@?<v@?q>24"
- "doubleValue"
- "initWithDouble:"
- "postMonthlyAnalyticsWithCompletionHandler:"
- "v24@0:8@?<v@?>16"

```
