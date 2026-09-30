## ProtectedCloudStorage

> `/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Versions/A/ProtectedCloudStorage`

```diff

-1303.0.6.0.0
-  __TEXT.__text: 0x6f130
+1303.40.9.0.0
+  __TEXT.__text: 0x6f284
   __TEXT.__objc_methlist: 0x1f10
   __TEXT.__const: 0x3d0
-  __TEXT.__cstring: 0xdf6b
-  __TEXT.__oslogstring: 0x4029
-  __TEXT.__gcc_except_tab: 0x3580
+  __TEXT.__cstring: 0xe00a
+  __TEXT.__oslogstring: 0x404f
+  __TEXT.__gcc_except_tab: 0x358c
   __TEXT.__dlopen_cstrs: 0x214
   __TEXT.__unwind_info: 0x1dd8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x1538
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x4240
+  __DATA_CONST.__objc_arraydata: 0x4248
   __DATA_CONST.__got: 0x5f8
   __AUTH_CONST.__const: 0x2550
-  __AUTH_CONST.__cfstring: 0x18760
+  __AUTH_CONST.__cfstring: 0x187e0
   __AUTH_CONST.__objc_const: 0x37b8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__auth_got: 0xb48
+  __AUTH_CONST.__auth_got: 0xb40
   __AUTH.__objc_data: 0x370
-  __AUTH.__data: 0x11e8
+  __AUTH.__data: 0x11f0
   __DATA.__objc_ivar: 0x29c
   __DATA.__data: 0x898
   __DATA.__common: 0x40

   - /usr/lib/libsqlite3.dylib
   Functions: 2152
   Symbols:   4290
-  CStrings:  3777
+  CStrings:  3781
 
Functions:
~ _PCSDBRRepairWrappingKeyFromEscrowIdentityOuterBlob : 1744 -> 1792
~ _PCSDBRRepairWrappingKeyFromEscrowIdentity : 748 -> 780
~ ___PCSDBRUnwrapKeys_block_invoke : 760 -> 1016
~ __PCSUpdateKeychainForwardTable : 76 -> 68
~ _PCSCacheCurrentIdentitiesForServices : 1064 -> 1076
CStrings:
+ "FlagMissingDBRRecord"
+ "No Primary DBR Record. Account needs DBR repair."
+ "get wrapping key failed with no error"
+ "unable to unwrap wrapping key with escrow identity"
```
