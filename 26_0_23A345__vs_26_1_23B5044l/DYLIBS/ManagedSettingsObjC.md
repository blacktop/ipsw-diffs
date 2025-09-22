## ManagedSettingsObjC

> `/System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC`

```diff

-263.0.0.0.0
-  __TEXT.__text: 0x29ec8
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x3db4
+265.0.0.0.0
+  __TEXT.__text: 0x2ac14
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_methlist: 0x3e24
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x4ec
-  __TEXT.__cstring: 0x1184
+  __TEXT.__gcc_except_tab: 0x570
+  __TEXT.__cstring: 0x1152
   __TEXT.__oslogstring: 0x1610
-  __TEXT.__unwind_info: 0xf30
+  __TEXT.__unwind_info: 0xf88
   __TEXT.__objc_classname: 0xd02
-  __TEXT.__objc_methname: 0x6854
-  __TEXT.__objc_methtype: 0x1057
-  __TEXT.__objc_stubs: 0x2420
+  __TEXT.__objc_methname: 0x6ab2
+  __TEXT.__objc_methtype: 0x10ca
+  __TEXT.__objc_stubs: 0x2480
   __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0x990
+  __DATA_CONST.__const: 0xa30
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1778
+  __DATA_CONST.__objc_selrefs: 0x17c0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x218
-  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__auth_got: 0x290
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x1ce0
-  __AUTH_CONST.__objc_const: 0x8638
+  __AUTH_CONST.__cfstring: 0x1c80
+  __AUTH_CONST.__objc_const: 0x8650
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0x2f4

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9701FBB9-ADDE-34B2-92EA-879FC970FE5C
-  Functions: 1353
-  Symbols:   4752
-  CStrings:  1946
+  UUID: A93198E0-5D58-3ABC-BD55-1E4A0F0CA2F0
+  Functions: 1368
+  Symbols:   4793
+  CStrings:  1952
 
Symbols:
+ +[MOEffectiveShieldSettings appResponsibleForShieldingBundleIdentifier:categoryIdentifier:completionHandler:]
+ +[MOEffectiveShieldSettings appResponsibleForShieldingBundleIdentifier:categoryIdentifier:error:]
+ +[MOEffectiveShieldSettings appResponsibleForShieldingCategoryIdentifier:completionHandler:]
+ +[MOEffectiveShieldSettings appResponsibleForShieldingCategoryIdentifier:error:]
+ +[MOEffectiveShieldSettings appResponsibleForShieldingWebDomain:categoryIdentifier:completionHandler:]
+ +[MOEffectiveShieldSettings appResponsibleForShieldingWebDomain:categoryIdentifier:error:]
+ GCC_except_table24
+ ___102+[MOEffectiveShieldSettings appResponsibleForShieldingWebDomain:categoryIdentifier:completionHandler:]_block_invoke
+ ___109+[MOEffectiveShieldSettings appResponsibleForShieldingBundleIdentifier:categoryIdentifier:completionHandler:]_block_invoke
+ ___80+[MOEffectiveShieldSettings appResponsibleForShieldingCategoryIdentifier:error:]_block_invoke
+ ___80+[MOEffectiveShieldSettings appResponsibleForShieldingCategoryIdentifier:error:]_block_invoke_2
+ ___90+[MOEffectiveShieldSettings appResponsibleForShieldingWebDomain:categoryIdentifier:error:]_block_invoke
+ ___90+[MOEffectiveShieldSettings appResponsibleForShieldingWebDomain:categoryIdentifier:error:]_block_invoke_2
+ ___92+[MOEffectiveShieldSettings appResponsibleForShieldingCategoryIdentifier:completionHandler:]_block_invoke
+ ___97+[MOEffectiveShieldSettings appResponsibleForShieldingBundleIdentifier:categoryIdentifier:error:]_block_invoke
+ ___97+[MOEffectiveShieldSettings appResponsibleForShieldingBundleIdentifier:categoryIdentifier:error:]_block_invoke_2
+ ___block_descriptor_48_e8_32r40r_e30_v24?0"NSString"8"NSError"16lr32l8r40l8
+ ___block_descriptor_56_e8_32s40r48r_e54_v24?0"<MOEffectiveShieldSettingsProxy>"8"NSError"16ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48bs_e54_v24?0"<MOEffectiveShieldSettingsProxy>"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e54_v24?0"<MOEffectiveShieldSettingsProxy>"8"NSError"16ls32l8s40l8s56l8s48l8
+ _objc_msgSend$appResponsibleForShieldingBundleIdentifier:categoryIdentifier:replyHandler:
+ _objc_msgSend$appResponsibleForShieldingCategoryIdentifier:replyHandler:
+ _objc_msgSend$appResponsibleForShieldingWebDomain:categoryIdentifier:replyHandler:
+ _objc_retain_x9
CStrings:
+ "appResponsibleForShieldingBundleIdentifier:categoryIdentifier:completionHandler:"
+ "appResponsibleForShieldingBundleIdentifier:categoryIdentifier:error:"
+ "appResponsibleForShieldingBundleIdentifier:categoryIdentifier:replyHandler:"
+ "appResponsibleForShieldingCategoryIdentifier:completionHandler:"
+ "appResponsibleForShieldingCategoryIdentifier:error:"
+ "appResponsibleForShieldingCategoryIdentifier:replyHandler:"
+ "appResponsibleForShieldingWebDomain:categoryIdentifier:completionHandler:"
+ "appResponsibleForShieldingWebDomain:categoryIdentifier:error:"
+ "appResponsibleForShieldingWebDomain:categoryIdentifier:replyHandler:"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "safari.denyHistoryClearing"
- "safari.denyPrivateBrowsing"
- "webContent.blockedByFilter"

```
