## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-820.4.17.0.0
-  __TEXT.__text: 0x17f364
+820.4.21.2.3
+  __TEXT.__text: 0x17fad4
   __TEXT.__auth_stubs: 0x2890
-  __TEXT.__objc_methlist: 0x1242c
+  __TEXT.__objc_methlist: 0x1244c
   __TEXT.__cstring: 0x18960
   __TEXT.__const: 0x65c8
   __TEXT.__gcc_except_tab: 0x1410
-  __TEXT.__oslogstring: 0xdb1b
+  __TEXT.__oslogstring: 0xdc5b
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0xba
   __TEXT.__swift5_typeref: 0x1f88

   __TEXT.__swift_as_entry: 0x190
   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x7398
+  __TEXT.__unwind_info: 0x73a8
   __TEXT.__eh_frame: 0x5a40
   __TEXT.__objc_classname: 0x25ad
-  __TEXT.__objc_methname: 0x287e5
-  __TEXT.__objc_methtype: 0x6b72
-  __TEXT.__objc_stubs: 0x15840
-  __DATA_CONST.__got: 0x1138
-  __DATA_CONST.__const: 0x60c0
+  __TEXT.__objc_methname: 0x28885
+  __TEXT.__objc_methtype: 0x6b82
+  __TEXT.__objc_stubs: 0x158c0
+  __DATA_CONST.__got: 0x1140
+  __DATA_CONST.__const: 0x60e8
   __DATA_CONST.__objc_classlist: 0x828
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x85f0
+  __DATA_CONST.__objc_selrefs: 0x8620
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x280
   __AUTH_CONST.__auth_got: 0x1458
   __AUTH_CONST.__const: 0x5a28
   __AUTH_CONST.__cfstring: 0x115c0
-  __AUTH_CONST.__objc_const: 0x24f28
+  __AUTH_CONST.__objc_const: 0x24f58
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH.__objc_data: 0x2cd0
   __AUTH.__data: 0x1128
-  __DATA.__objc_ivar: 0x1064
+  __DATA.__objc_ivar: 0x1068
   __DATA.__data: 0x3a98
   __DATA.__bss: 0x8510
   __DATA.__common: 0x20

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CF6EFD65-7D65-3CA7-AD95-916277EAB64A
-  Functions: 11014
-  Symbols:   25430
-  CStrings:  13669
+  UUID: 301E034E-1672-3DE1-9B41-3AE64E6C85A5
+  Functions: 11023
+  Symbols:   25455
+  CStrings:  13685
 
Symbols:
+ -[GKPlayerCredentialController accountManager]
+ -[GKPlayerCredentialController recoverDSIDForCredential:completionHandler:]
+ -[GKPlayerCredentialController recoverDSIDForCredential:completionHandler:].cold.1
+ -[GKPlayerCredentialController setAccountManager:]
+ _OBJC_CLASS_$_AKAccountManager
+ _OBJC_IVAR_$_GKPlayerCredentialController._accountManager
+ ___71-[GKPlayerCredentialController setPrimaryCredential:completionHandler:]_block_invoke.44
+ ___71-[GKPlayerCredentialController setPrimaryCredential:completionHandler:]_block_invoke.46
+ ___71-[GKPlayerCredentialController setPrimaryCredential:completionHandler:]_block_invoke_2.45
+ ___75-[GKPlayerCredentialController recoverDSIDForCredential:completionHandler:]_block_invoke
+ ___75-[GKPlayerCredentialController recoverDSIDForCredential:completionHandler:]_block_invoke.53
+ ___75-[GKPlayerCredentialController recoverDSIDForCredential:completionHandler:]_block_invoke.cold.1
+ ___75-[GKPlayerCredentialController recoverDSIDForCredential:completionHandler:]_block_invoke.cold.2
+ ___75-[GKPlayerCredentialController recoverDSIDForCredential:completionHandler:]_block_invoke.cold.3
+ ___83-[GKPlayerCredentialController replaceCredential:withCredential:completionHandler:]_block_invoke.49
+ ___block_descriptor_64_e8_32s40s48s56s_e43_v24?0"ACAccountStore"8?<v?"NSError">16ls32l8s40l8s48l8s56l8
+ ___block_literal_global.191
+ _objc_msgSend$DSIDForAccount:
+ _objc_msgSend$accountManager
+ _objc_msgSend$authKitAccountWithAltDSID:error:
+ _objc_msgSend$sharedInstance
- ___71-[GKPlayerCredentialController setPrimaryCredential:completionHandler:]_block_invoke.43
- ___71-[GKPlayerCredentialController setPrimaryCredential:completionHandler:]_block_invoke.45
- ___71-[GKPlayerCredentialController setPrimaryCredential:completionHandler:]_block_invoke_2.44
- ___83-[GKPlayerCredentialController replaceCredential:withCredential:completionHandler:]_block_invoke.48
- ___block_literal_global.182
- ___block_literal_global.25
CStrings:
+ "@\"AKAccountManager\""
+ "CRED: DSID recovery finished for credential (%@), (error:%@)"
+ "CRED: recovering DSID for credential (%@):"
+ "DSID recovery: DSID already present, skipping recovery"
+ "DSID recovery: no AuthKit account for altDSID, error: %@"
+ "DSID recovery: no DSID on AuthKit account"
+ "DSID recovery: no altDSID on credential"
+ "DSID recovery: username mismatch"
+ "DSIDForAccount:"
+ "T@\"AKAccountManager\",&,N,V_accountManager"
+ "_accountManager"
+ "accountManager"
+ "authKitAccountWithAltDSID:error:"
+ "recoverDSIDForCredential:completionHandler:"
+ "setAccountManager:"
+ "sharedInstance"

```
