## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/ProtectedCloudStorage`

```diff

-1303.0.6.0.0
-  __TEXT.__text: 0x6cb48
+1303.40.9.0.0
+  __TEXT.__text: 0x6cc8c
   __TEXT.__objc_methlist: 0x2028
   __TEXT.__const: 0x3c8
-  __TEXT.__cstring: 0xe0b4
-  __TEXT.__oslogstring: 0x4089
-  __TEXT.__gcc_except_tab: 0x3630
+  __TEXT.__cstring: 0xe153
+  __TEXT.__oslogstring: 0x40af
+  __TEXT.__gcc_except_tab: 0x363c
   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__unwind_info: 0x1da8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x1658
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x4240
+  __DATA_CONST.__objc_arraydata: 0x4248
   __DATA_CONST.__got: 0x688
   __AUTH_CONST.__const: 0x9a0
-  __AUTH_CONST.__cfstring: 0x18920
+  __AUTH_CONST.__cfstring: 0x189a0
   __AUTH_CONST.__objc_const: 0x38a8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__auth_got: 0xc58
+  __AUTH_CONST.__auth_got: 0xc50
   __AUTH.__objc_data: 0x370
-  __AUTH.__data: 0x13a8
+  __AUTH.__data: 0x13b0
   __DATA.__objc_ivar: 0x2a0
   __DATA.__data: 0x918
   __DATA.__common: 0x40

   - /usr/lib/libsqlite3.dylib
   Functions: 2125
   Symbols:   4209
-  CStrings:  3796
+  CStrings:  3800
 
Functions:
~ _PCSDBRRepairWrappingKeyFromEscrowIdentityOuterBlob : 1700 -> 1740
~ _PCSDBRRepairWrappingKeyFromEscrowIdentity : 696 -> 728
~ ___PCSDBRUnwrapKeys_block_invoke : 724 -> 972
~ __PCSUpdateKeychainForwardTable : 76 -> 68
~ _PCSCacheCurrentIdentitiesForServices : 1044 -> 1056
CStrings:
+ "FlagMissingDBRRecord"
+ "No Primary DBR Record. Account needs DBR repair."
+ "get wrapping key failed with no error"
+ "unable to unwrap wrapping key with escrow identity"
```
