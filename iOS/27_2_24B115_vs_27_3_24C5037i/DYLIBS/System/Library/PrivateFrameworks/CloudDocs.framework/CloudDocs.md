## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-5168.40.162.0.0
-  __TEXT.__text: 0x7c1dc
-  __TEXT.__objc_methlist: 0x6724
+5168.60.14.0.0
+  __TEXT.__text: 0x7c6b8
+  __TEXT.__objc_methlist: 0x675c
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x3c28
-  __TEXT.__cstring: 0xb8d0
-  __TEXT.__oslogstring: 0x8d68
+  __TEXT.__gcc_except_tab: 0x3c38
+  __TEXT.__cstring: 0xb90f
+  __TEXT.__oslogstring: 0x8eec
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x3058
+  __TEXT.__unwind_info: 0x3080
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4270
+  __DATA_CONST.__objc_selrefs: 0x4298
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x88

   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0xa68
+  __AUTH_CONST.__auth_got: 0xa78
   __AUTH.__objc_data: 0x1270
   __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0x5ec

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3046
-  Symbols:   5130
-  CStrings:  2204
+  Functions: 3054
+  Symbols:   5134
+  CStrings:  2209
 
Symbols:
+ +[BRContainer ubiquitousContainers:declarePublicDocumentScopeForContainerID:]
+ +[BRContainer(BRInternalAdditions) ubiquitousContainerPropertiesForContainerID:inUbiquitousContainers:]
+ +[NSURL(BRAdditions) br_withIOPolicyFlags:type:forBlock:]
+ -[BRContainer(BRInternalAdditions) isMetadataExtracted]
+ -[NSURL(BRCPathAdditions) brc_issueSandboxExtensionOfClass:flags:error:]
+ GCC_except_table111
+ GCC_except_table115
+ GCC_except_table128
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table182
+ GCC_except_table183
+ GCC_except_table185
+ GCC_except_table193
+ GCC_except_table198
+ GCC_except_table208
+ GCC_except_table210
+ GCC_except_table234
+ GCC_except_table51
+ GCC_except_table53
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table67
+ GCC_except_table92
+ ___55-[BRContainer(BRInternalAdditions) isMetadataExtracted]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e16_v16?0"NSData"8ls32l8s40l8
+ _disableiopolicy_np
+ _enableiopolicy_np
- GCC_except_table110
- GCC_except_table127
- GCC_except_table131
- GCC_except_table135
- GCC_except_table140
- GCC_except_table147
- GCC_except_table153
- GCC_except_table155
- GCC_except_table161
- GCC_except_table163
- GCC_except_table172
- GCC_except_table179
- GCC_except_table189
- GCC_except_table190
- GCC_except_table204
- GCC_except_table206
- GCC_except_table230
- GCC_except_table42
- GCC_except_table58
- GCC_except_table60
- GCC_except_table66
- GCC_except_table68
- GCC_except_table74
- GCC_except_table91
- GCC_except_table97
- ___block_descriptor_40_e8_32bs_e16_v16?0"NSData"8ls32l8
CStrings:
+ "+[NSURL(BRAdditions) br_withIOPolicyFlags:type:forBlock:]"
+ "-[NSURL(BRCPathAdditions) brc_issueSandboxExtensionOfClass:flags:error:]"
+ "5168.60.14"
+ "[ERROR] enableiopolicy_np failed for flags: %#x, type: %d, scope: %d, errno: %d%@"
+ "[ERROR] getiopolicy_np failed when enabling flags: %#x, type: %d, scope: %d%@"
+ "[ERROR] sandbox_check: current process does not allow iopolicy syscalls, not running block%@"
+ "[WARNING] no data representation for container %@, returning nil properties - every property read off it is a default, not an answer%@"
- "-[NSURL(BRCPathAdditions) brc_issueSandboxExtensionOfClass:error:]"
- "5168.40.162"
```
