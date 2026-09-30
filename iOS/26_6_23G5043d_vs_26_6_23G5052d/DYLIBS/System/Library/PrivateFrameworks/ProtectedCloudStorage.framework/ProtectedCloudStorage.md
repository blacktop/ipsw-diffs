## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

```diff

-  __TEXT.__text: 0x6f5e4
+  __TEXT.__text: 0x6fddc
   __TEXT.__auth_stubs: 0x1940
   __TEXT.__objc_methlist: 0x2020
   __TEXT.__const: 0x3c8
   __TEXT.__cstring: 0xe097
-  __TEXT.__oslogstring: 0x3e2f
-  __TEXT.__gcc_except_tab: 0x38d8
+  __TEXT.__oslogstring: 0x3e75
+  __TEXT.__gcc_except_tab: 0x3834
   __TEXT.__dlopen_cstrs: 0x2c5
-  __TEXT.__unwind_info: 0x1908
+  __TEXT.__unwind_info: 0x1928
   __TEXT.__objc_classname: 0x326
   __TEXT.__objc_methname: 0x556e
   __TEXT.__objc_methtype: 0x15ef
   __TEXT.__objc_stubs: 0x4440
   __DATA_CONST.__got: 0x678
-  __DATA_CONST.__const: 0x2e50
+  __DATA_CONST.__const: 0x2ef0
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x4240
   __AUTH_CONST.__auth_got: 0xcb0
-  __AUTH_CONST.__const: 0x960
+  __AUTH_CONST.__const: 0x980
   __AUTH_CONST.__cfstring: 0x18940
   __AUTH_CONST.__objc_const: 0x3890
   __AUTH_CONST.__objc_dictobj: 0xc8

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2114
-  Symbols:   6434
-  CStrings:  8179
+  Functions: 2123
+  Symbols:   6455
+  CStrings:  8182
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _PCSDBRGetWrappingKey
+ _PCSDBRRepairWrappingKeyFromEscrowIdentity
+ _PCSDBRRepairWrappingKeyFromEscrowIdentityOuterBlob
+ __DeleteWrappingKeyAndFail
+ __ValidateInnerBlob
+ ___PCSDBRGetWrappingKey_block_invoke
+ ___PCSDBRRepairWrappingKeyFromEscrowIdentityOuterBlob_block_invoke
+ ___PCSDBRUnwrapKeys_block_invoke_2
+ ____DeleteWrappingKeyAndFail_block_invoke
+ ____ValidateInnerBlob_block_invoke
+ ____ValidateInnerBlob_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e61_v48?0"NSData"8"NSData"16"NSData"24"NSData"32"NSError"40ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e23_v32?0q8q16"NSError"24lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e34_v40?0"NSData"8q16q24"NSError"32ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e61_v48?0"NSData"8"NSData"16"NSData"24"NSData"32"NSError"40ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e34_v40?0"NSData"8q16q24"NSError"32lr48l8r56l8r64l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e34_v40?0"NSData"8q16q24"NSError"32lr48l8s32l8r56l8s40l8r64l8
- __PCSDBRGetWrappingKey
- ____PCSDBRGetWrappingKey_block_invoke
- ____PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke
- ___block_descriptor_56_e8_32r40r48r_e34_v40?0"NSData"8q16q24"NSError"32lr32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40r48r56r_e34_v40?0"NSData"8q16q24"NSError"32lr40l8r48l8r56l8s32l8
CStrings:
+ "error while attempting to get wrapping key: %@"
+ "failed to unwrap inner blob: %@"
+ "failed to unwrap inner blob: %@, retrying"
+ "unwrapped inner blob"
- "error while attempting to repair wrapping key using escrow identity: %@"

```
