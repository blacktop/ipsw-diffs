## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2393.100.0.0.0
-  __TEXT.__text: 0xcf658
-  __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_methlist: 0xc9a0
+2400.8.1.0.0
+  __TEXT.__text: 0xcf9ac
+  __TEXT.__auth_stubs: 0x1c00
+  __TEXT.__objc_methlist: 0xc9d8
   __TEXT.__const: 0xc5a
-  __TEXT.__gcc_except_tab: 0x2f0c
+  __TEXT.__gcc_except_tab: 0x2eec
   __TEXT.__cstring: 0x12b02
-  __TEXT.__oslogstring: 0x7e01
+  __TEXT.__oslogstring: 0x7de9
   __TEXT.__ustring: 0x3c
   __TEXT.__dlopen_cstrs: 0x3f1
   __TEXT.__swift5_typeref: 0x2a0

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3398
+  __TEXT.__unwind_info: 0x33b0
   __TEXT.__eh_frame: 0x1e8
   __TEXT.__objc_classname: 0xfba
-  __TEXT.__objc_methname: 0x1d8c4
-  __TEXT.__objc_methtype: 0x21c2
-  __TEXT.__objc_stubs: 0xfc20
+  __TEXT.__objc_methname: 0x1d930
+  __TEXT.__objc_methtype: 0x21d0
+  __TEXT.__objc_stubs: 0xfc60
   __DATA_CONST.__got: 0x790
   __DATA_CONST.__const: 0x4ff0
   __DATA_CONST.__objc_classlist: 0x448
-  __DATA_CONST.__objc_catlist: 0x40
+  __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x77b0
+  __DATA_CONST.__objc_selrefs: 0x77c8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x330
   __DATA_CONST.__objc_arraydata: 0xd48
-  __AUTH_CONST.__auth_got: 0xe08
+  __AUTH_CONST.__auth_got: 0xe10
   __AUTH_CONST.__const: 0x18b0
   __AUTH_CONST.__cfstring: 0x12660
-  __AUTH_CONST.__objc_const: 0x125e0
+  __AUTH_CONST.__objc_const: 0x12620
   __AUTH_CONST.__objc_arrayobj: 0xa50
   __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_dictobj: 0xc8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C45C1F17-C1E8-3028-AC79-5D9C9F4622F0
-  Functions: 5463
-  Symbols:   17357
-  CStrings:  12076
+  UUID: 7B86E51C-8E15-3EA5-A491-6F281D12C11A
+  Functions: 5469
+  Symbols:   17374
+  CStrings:  12080
 
Symbols:
+ +[CSIndexJob jobOptionsFromProvideOptions:]
+ +[CSIndexJob provideOptionsFromJobOptions:]
+ -[CSSearchableIndex _issueDiagnose:bundleID:logQuery:completionHandler:]
+ -[CSUnhousedSearchableIndex initWithPath:protectionClass:bundleID:]
+ -[NSUUID(CSCoderAdditions) encodeWithCSCoder:]
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table154
+ GCC_except_table155
+ GCC_except_table159
+ GCC_except_table162
+ GCC_except_table163
+ GCC_except_table166
+ GCC_except_table167
+ GCC_except_table171
+ GCC_except_table172
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table202
+ GCC_except_table203
+ GCC_except_table208
+ GCC_except_table217
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table226
+ GCC_except_table227
+ GCC_except_table231
+ GCC_except_table232
+ GCC_except_table236
+ GCC_except_table237
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table246
+ GCC_except_table247
+ GCC_except_table251
+ GCC_except_table252
+ GCC_except_table255
+ GCC_except_table256
+ GCC_except_table259
+ GCC_except_table260
+ GCC_except_table264
+ GCC_except_table267
+ GCC_except_table284
+ GCC_except_table285
+ GCC_except_table288
+ GCC_except_table313
+ GCC_except_table322
+ _CFUUIDCreateFromString
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUUID_$_CSCoderAdditions
+ __OBJC_$_CATEGORY_NSUUID_$_CSCoderAdditions
+ ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.117
+ ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.134
+ ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.134.cold.1
+ ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.155
+ ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.164
+ ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.164.cold.1
+ ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke_2.158
+ ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke_2.158.cold.1
+ ___72-[CSSearchableIndex _issueDiagnose:bundleID:logQuery:completionHandler:]_block_invoke
+ ___72-[CSSearchableIndex _issueDiagnose:bundleID:logQuery:completionHandler:]_block_invoke_2
+ ___72-[CSSearchableIndex _issueDiagnose:bundleID:logQuery:completionHandler:]_block_invoke_3
+ ___76-[CSSearchableIndex provideDataForBundle:identifier:type:completionHandler:]_block_invoke
+ ___79-[CSSearchableIndex provideFileURLForBundle:identifier:type:completionHandler:]_block_invoke
+ ___block_descriptor_61_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
+ ___block_literal_global.101
+ _connectionWithToken:.connectionLock
+ _defaultSearchableIndex.onceToken.770
+ _defaultSearchableIndex.onceToken.777
+ _defaultSearchableIndex.sDefaultInstance.769
+ _defaultSearchableIndex.sDefaultInstance.776
+ _objc_msgSend$initWithPath:protectionClass:bundleID:
+ _objc_msgSend$provideOptionsFromJobOptions:
- -[CSSearchableIndex _issueDiagnose:logQuery:completionHandler:]
- GCC_except_table148
- GCC_except_table149
- GCC_except_table152
- GCC_except_table153
- GCC_except_table156
- GCC_except_table157
- GCC_except_table160
- GCC_except_table161
- GCC_except_table164
- GCC_except_table165
- GCC_except_table169
- GCC_except_table170
- GCC_except_table179
- GCC_except_table180
- GCC_except_table196
- GCC_except_table197
- GCC_except_table200
- GCC_except_table201
- GCC_except_table206
- GCC_except_table207
- GCC_except_table215
- GCC_except_table216
- GCC_except_table219
- GCC_except_table224
- GCC_except_table225
- GCC_except_table229
- GCC_except_table230
- GCC_except_table234
- GCC_except_table235
- GCC_except_table239
- GCC_except_table240
- GCC_except_table244
- GCC_except_table245
- GCC_except_table249
- GCC_except_table250
- GCC_except_table253
- GCC_except_table254
- GCC_except_table257
- GCC_except_table258
- GCC_except_table262
- GCC_except_table263
- GCC_except_table282
- GCC_except_table283
- GCC_except_table286
- GCC_except_table311
- GCC_except_table312
- GCC_except_table318
- GCC_except_table440
- ___63-[CSSearchableIndex _issueDiagnose:logQuery:completionHandler:]_block_invoke
- ___63-[CSSearchableIndex _issueDiagnose:logQuery:completionHandler:]_block_invoke_2
- ___63-[CSSearchableIndex _issueDiagnose:logQuery:completionHandler:]_block_invoke_3
- ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.115
- ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.133
- ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.133.cold.1
- ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.154
- ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.163
- ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke.163.cold.1
- ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke_2.157
- ___63-[_MDRemoteExtensionContext performJob:acknowledgementHandler:]_block_invoke_2.157.cold.1
- ___block_descriptor_53_e8_32s40w_e5_v8?0ls32l8w40l8
- ___block_literal_global.100
- _defaultSearchableIndex.onceToken.769
- _defaultSearchableIndex.onceToken.776
- _defaultSearchableIndex.sDefaultInstance.768
- _defaultSearchableIndex.sDefaultInstance.775
CStrings:
+ "[qid=%ld] disabling blocking results on indexing"
+ "[qid=%ld][CSUserQuery] disabling blocking results on indexing for client %s"
+ "_issueDiagnose:bundleID:logQuery:completionHandler:"
+ "initWithPath:protectionClass:bundleID:"
+ "jobOptionsFromProvideOptions:"
+ "provideOptionsFromJobOptions:"
+ "q24@0:8q16"
+ "v40@0:8i16@20B28@?32"
- "[qid=%ld] is a live query; also disabling blocking on index."
- "[qid=%ld][CSUserQuery] %s query is a live query; also disabling blocking on index here."
- "_issueDiagnose:logQuery:completionHandler:"
- "v32@0:8i16B20@?24"

```
