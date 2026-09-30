## securityd

> `/usr/libexec/securityd`

```diff

-61439.0.101.0.0
-  __TEXT.__text: 0x22ee90
+61439.0.117.0.1
+  __TEXT.__text: 0x22eae8
   __TEXT.__auth_stubs: 0x38c0
-  __TEXT.__objc_stubs: 0x1a4a0
-  __TEXT.__objc_methlist: 0x1291c
-  __TEXT.__const: 0x8cd
-  __TEXT.__cstring: 0x203aa
-  __TEXT.__oslogstring: 0x28d24
+  __TEXT.__objc_stubs: 0x1a4c0
+  __TEXT.__objc_methlist: 0x12924
+  __TEXT.__const: 0x8d5
+  __TEXT.__cstring: 0x2035e
+  __TEXT.__oslogstring: 0x28cbf
   __TEXT.__gcc_except_tab: 0xab44
   __TEXT.__objc_classname: 0x22ba
-  __TEXT.__objc_methname: 0x2920f
-  __TEXT.__objc_methtype: 0x9862
+  __TEXT.__objc_methname: 0x29233
+  __TEXT.__objc_methtype: 0x9865
   __TEXT.__dlopen_cstrs: 0x2c4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6260
+  __TEXT.__unwind_info: 0x6240
   __DATA_CONST.__auth_got: 0x1c70
   __DATA_CONST.__got: 0xdd8
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x13278
-  __DATA_CONST.__cfstring: 0x1af80
+  __DATA_CONST.__const: 0x131b8
+  __DATA_CONST.__cfstring: 0x1afa0
   __DATA_CONST.__objc_classlist: 0x880
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x210

   __DATA_CONST.__objc_arraydata: 0x3d8
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x23618
+  __DATA.__objc_const: 0x23628
   __DATA.__objc_selrefs: 0x8768
   __DATA.__objc_ivar: 0x1868
   __DATA.__objc_data: 0x5500
   __DATA.__data: 0x20b8
   __DATA.__thread_vars: 0xd8
   __DATA.__thread_bss: 0x1e
-  __DATA.__bss: 0xa78
+  __DATA.__bss: 0xa50
   __DATA.__common: 0x10
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9088
+  Functions: 9084
   Symbols:   1374
-  CStrings:  15238
+  CStrings:  15232
 
CStrings:
+ "Out of band fetch disabled due to CKKS readiness"
+ "Out of band fetch disabled due to CKKS readiness"
+ "allowOutOfBandFetch"
+ "fetchPCSIdentityOutOfBand:forceFetch:complete:"
+ "getCurrentItemOutOfBand:forceFetch:complete:"
+ "secItemFetchCurrentItemOutOfBand:forceFetch:complete:"
+ "secItemFetchPCSIdentityByKeyOutOfBand:forceFetch:complete:"
+ "v36@0:8@\"NSArray\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
- "CKKSHighPriorityOperations"
- "KCSharingAutomaticSyncing"
- "Key Diversification is %!s(MISSING) (via feature flags)"
- "KeychainKeyDiversification"
- "OctagonEscrowMove"
- "SecError Nested Error Capping is %!@(MISSING) (via feature flags)"
- "SecErrorNestedErrorCapping"
- "Skipping escrow move request (feature disabled)"
- "fetchPCSIdentityOutOfBand:complete:"
- "getCurrentItemOutOfBand:complete:"
- "secItemFetchCurrentItemOutOfBand:complete:"
- "secItemFetchPCSIdentityByKeyOutOfBand:complete:"
- "setAutomaticSyncingEnabled:"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"

```
