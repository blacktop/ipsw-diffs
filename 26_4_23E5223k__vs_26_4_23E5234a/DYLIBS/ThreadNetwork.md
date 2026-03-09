## ThreadNetwork

> `/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`

```diff

-335.0.17.0.0
-  __TEXT.__text: 0xcd98
+335.0.19.0.0
+  __TEXT.__text: 0xd440
   __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0xbb8
+  __TEXT.__objc_methlist: 0xbe8
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0xfac
-  __TEXT.__oslogstring: 0x4f6
+  __TEXT.__cstring: 0x113d
+  __TEXT.__oslogstring: 0x5fc
   __TEXT.__gcc_except_tab: 0x164
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x338
   __TEXT.__objc_classname: 0x180
-  __TEXT.__objc_methname: 0x2379
-  __TEXT.__objc_methtype: 0x864
-  __TEXT.__objc_stubs: 0x1040
+  __TEXT.__objc_methname: 0x242b
+  __TEXT.__objc_methtype: 0x880
+  __TEXT.__objc_stubs: 0x1080
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x288
+  __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f0
+  __DATA_CONST.__objc_selrefs: 0x610
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __AUTH_CONST.__auth_got: 0x1e8
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x4e0
-  __AUTH_CONST.__objc_const: 0x1a90
+  __AUTH_CONST.__objc_const: 0x1aa0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0x130

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 95E8ED77-24F1-3ED2-8EE0-C8B3E98B7EA5
-  Functions: 310
-  Symbols:   1128
-  CStrings:  524
+  UUID: B185EAC5-4A57-307C-801A-AC697111CD3A
+  Functions: 316
+  Symbols:   1143
+  CStrings:  541
 
Symbols:
+ -[THClient countNonAppleRecordsWithCompletion:]
+ -[THClient countPreferredFrozenRecordsWithCompletion:]
+ ___47-[THClient countNonAppleRecordsWithCompletion:]_block_invoke
+ ___47-[THClient countNonAppleRecordsWithCompletion:]_block_invoke_2
+ ___54-[THClient countPreferredFrozenRecordsWithCompletion:]_block_invoke
+ ___54-[THClient countPreferredFrozenRecordsWithCompletion:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e20_v24?0Q8"NSError"16ls32l8
+ _objc_msgSend$ctcsServerCountNonAppleRecordsWithCompletion:
+ _objc_msgSend$ctcsServerCountPreferredFrozenRecordsWithCompletion:
CStrings:
+ "%s:%d: - Response: count = %lu, error = %@"
+ "-[THClient countNonAppleRecordsWithCompletion:]"
+ "-[THClient countNonAppleRecordsWithCompletion:]_block_invoke_2"
+ "-[THClient countPreferredFrozenRecordsWithCompletion:]"
+ "-[THClient countPreferredFrozenRecordsWithCompletion:]_block_invoke_2"
+ "-[THClient retrieveCredentialsForBorderAgent:completion:]_block_invoke"
+ "-[THClient retrieveCredentialsForExtendedPANID:completion:]_block_invoke"
+ "Client: %s Failed to retrun record, error: %@ \n"
+ "Client: %s Returning record successfully, error: %@ \n"
+ "Client: %s:%d - Counting 3P saved Border Agent credentials"
+ "Client: %s:%d - Counting frozen preferred network records"
+ "countNonAppleRecordsWithCompletion:"
+ "countPreferredFrozenRecordsWithCompletion:"
+ "ctcsServerCountNonAppleRecordsWithCompletion:"
+ "ctcsServerCountPreferredFrozenRecordsWithCompletion:"
+ "v24@0:8@?<v@?Q@\"NSError\">16"
+ "v24@?0Q8@\"NSError\"16"

```
