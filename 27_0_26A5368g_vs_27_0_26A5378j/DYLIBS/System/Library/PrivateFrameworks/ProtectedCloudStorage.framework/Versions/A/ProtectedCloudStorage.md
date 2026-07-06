## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Versions/A/ProtectedCloudStorage`

```diff

-  __TEXT.__text: 0x6fc80
-  __TEXT.__objc_methlist: 0x1f00
+  __TEXT.__text: 0x705a8
+  __TEXT.__objc_methlist: 0x1f10
   __TEXT.__const: 0x3d0
   __TEXT.__cstring: 0xdf6b
-  __TEXT.__oslogstring: 0x3f72
-  __TEXT.__gcc_except_tab: 0x3638
+  __TEXT.__oslogstring: 0x3fc4
+  __TEXT.__gcc_except_tab: 0x3580
   __TEXT.__dlopen_cstrs: 0x214
-  __TEXT.__unwind_info: 0x1848
+  __TEXT.__unwind_info: 0x1868
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1530
+  __DATA_CONST.__objc_selrefs: 0x1538
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x4240
-  __DATA_CONST.__got: 0x5e8
-  __AUTH_CONST.__const: 0x24a0
+  __DATA_CONST.__got: 0x5f8
+  __AUTH_CONST.__const: 0x2550
   __AUTH_CONST.__cfstring: 0x18760
   __AUTH_CONST.__objc_const: 0x37b8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__auth_got: 0xb48
-  __AUTH.__objc_data: 0x280
-  __AUTH.__data: 0x2a0
+  __AUTH.__objc_data: 0x370
+  __AUTH.__data: 0x11e8
   __DATA.__objc_ivar: 0x29c
   __DATA.__data: 0x898
   __DATA.__bss: 0x2c0
   __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x870
-  __DATA_DIRTY.__data: 0xf98
+  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__bss: 0x118
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2142
-  Symbols:   4636
-  CStrings:  6918
+  Functions: 2152
+  Symbols:   4651
+  CStrings:  6922
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
Symbols:
+ +[PCSAccountsModel inducedFailureEnabled:]
+ PCSDBRGetWrappingKey
+ _PCSDBRRepairWrappingKeyFromEscrowIdentity
+ _PCSDBRRepairWrappingKeyFromEscrowIdentityOuterBlob
+ __DeleteWrappingKeyAndFail
+ __PCSDBRRepairWrappingKeyFromEscrowIdentityOuterBlob_block_invoke
+ __PCSDBRUnwrapKeys_block_invoke
+ __ValidateInnerBlob
+ ___PCSDBRGetWrappingKey_block_invoke
+ ___PCSDBRRepairWrappingKeyFromEscrowIdentityOuterBlob_block_invoke
+ ___PCSDBRUnwrapKeys_block_invoke_2
+ ___ValidateInnerBlob_block_invoke
+ ____DeleteWrappingKeyAndFail_block_invoke
+ ____ValidateInnerBlob_block_invoke
+ ____ValidateInnerBlob_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e61_v48?0"NSData"8"NSData"16"NSData"24"NSData"32"NSError"40l
+ ___block_descriptor_56_e8_32s40r48r_e23_v32?0q8q16"NSError"24l
+ ___block_descriptor_56_e8_32s40s48bs_e34_v40?0"NSData"8q16q24"NSError"32l
+ ___block_descriptor_56_e8_32s40s48bs_e61_v48?0"NSData"8"NSData"16"NSData"24"NSData"32"NSError"40l
+ ___block_descriptor_72_e8_32s40s48r56r64r_e34_v40?0"NSData"8q16q24"NSError"32l
+ _objc_msgSend$inducedFailureEnabled:
- __PCSDBRGetWrappingKey
- ___PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke
- ____PCSDBRGetWrappingKey_block_invoke
- ____PCSDBRRepairWrappingKeyFromEscrowIdentity_block_invoke
- ___block_descriptor_56_e8_32r40r48r_e34_v40?0"NSData"8q16q24"NSError"32l
- ___block_descriptor_64_e8_32s40r48r56r_e34_v40?0"NSData"8q16q24"NSError"32l
CStrings:
+ "Failure %@ induced (defaults %@/%@)"
+ "PCSIdentityGenerateBlobForPasswordChange"
+ "error while attempting to get wrapping key: %@"
+ "failed to unwrap inner blob: %@"
+ "failed to unwrap inner blob: %@, retrying"
+ "unwrapped inner blob"
- "Disallowing repair with escrow identity operation (due to %@/%@)"
- "error while attempting to repair wrapping key using escrow identity: %@"

```
