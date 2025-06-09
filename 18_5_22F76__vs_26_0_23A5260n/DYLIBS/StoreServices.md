## StoreServices

> `/System/Library/PrivateFrameworks/StoreServices.framework/StoreServices`

```diff

-1451.6.2.1.0
-  __TEXT.__text: 0x2df31c
-  __TEXT.__auth_stubs: 0x1df0
+1451.6.5.0.0
+  __TEXT.__text: 0x2d52a0
+  __TEXT.__auth_stubs: 0x1de0
   __TEXT.__objc_methlist: 0x15598
-  __TEXT.__const: 0x19ef0
+  __TEXT.__const: 0x19b00
   __TEXT.__cstring: 0x14555
   __TEXT.__oslogstring: 0xaa64
   __TEXT.__gcc_except_tab: 0x4648
   __TEXT.__dlopen_cstrs: 0x1be
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x6fb8
-  __TEXT.__eh_frame: 0x3128
+  __TEXT.__unwind_info: 0x6a00
+  __TEXT.__eh_frame: 0x1a8
   __TEXT.__objc_classname: 0x254b
-  __TEXT.__objc_methname: 0x2b0c8
+  __TEXT.__objc_methname: 0x2b11b
   __TEXT.__objc_methtype: 0x343f
-  __TEXT.__objc_stubs: 0x1ace0
-  __DATA_CONST.__got: 0xed8
+  __TEXT.__objc_stubs: 0x1ada0
+  __DATA_CONST.__got: 0xec0
   __DATA_CONST.__const: 0x8488
   __DATA_CONST.__objc_classlist: 0xbb8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa2b8
+  __DATA_CONST.__objc_selrefs: 0xa2e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x940
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0xf10
-  __AUTH_CONST.__const: 0x158f8
+  __AUTH_CONST.__auth_got: 0xf08
+  __AUTH_CONST.__const: 0x16cc8
   __AUTH_CONST.__cfstring: 0x18fc0
   __AUTH_CONST.__objc_const: 0x260b0
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x4920
+  __AUTH.__objc_data: 0x4a10
   __AUTH.__data: 0x40
   __DATA.__objc_ivar: 0x18a4
-  __DATA.__data: 0x1248
+  __DATA.__data: 0x12d8
   __DATA.__bss: 0x548
-  __DATA.__common: 0xaa0
-  __DATA_DIRTY.__objc_data: 0x2c10
+  __DATA.__common: 0xa95
+  __DATA_DIRTY.__objc_data: 0x2b20
   __DATA_DIRTY.__data: 0x398
-  __DATA_DIRTY.__bss: 0x3b0
+  __DATA_DIRTY.__bss: 0x3d0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2BC4C14E-8F3A-3DBD-9D78-266E6182B1E7
-  Functions: 9570
-  Symbols:   29582
-  CStrings:  15921
+  UUID: FF3942A6-9180-3D79-ACDA-99B796A34A40
+  Functions: 9566
+  Symbols:   29581
+  CStrings:  15927
 
Symbols:
+ ___26-[SSAccountStore accounts]_block_invoke.186
+ ___44+[SSAccountStore migrateToAccountsFramework]_block_invoke.225
+ ___44+[SSAccountStore migrateToAccountsFramework]_block_invoke.229
+ ___44+[SSAccountStore migrateToAccountsFramework]_block_invoke.230
+ ___44-[SSAccountStore signOutAccount:completion:]_block_invoke.239
+ ___49-[SSAccountStore _saveAccount:verifyCredentials:]_block_invoke.324
+ ___57-[SSAccountStore updateAccountWithAuthKit:store:options:]_block_invoke.256
+ ___57-[SSAccountStore updateAccountWithAuthKit:store:options:]_block_invoke.267
+ ___65-[SSAccountStore _updateAccountWithAuthKitViaSilentAuth:options:]_block_invoke.369
+ ___71-[SSAccountStore _updateAccountWithAuthKitViaPromptAuth:store:options:]_block_invoke.363
+ ___73-[SSAccountStore _updateAccountWithAuthKitViaSilentPasswordAuth:options:]_block_invoke.373
+ ___block_literal_global.192
+ ___block_literal_global.201
+ ___block_literal_global.205
+ ___block_literal_global.228
+ ___block_literal_global.271
+ ___block_literal_global.310
+ ___block_literal_global.620
+ _objc_msgSend$_setError
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithBundleIDs:states:
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _CFMakeCollectable
- ___26-[SSAccountStore accounts]_block_invoke.183
- ___44+[SSAccountStore migrateToAccountsFramework]_block_invoke.222
- ___44+[SSAccountStore migrateToAccountsFramework]_block_invoke.226
- ___44+[SSAccountStore migrateToAccountsFramework]_block_invoke.227
- ___44-[SSAccountStore signOutAccount:completion:]_block_invoke.236
- ___49-[SSAccountStore _saveAccount:verifyCredentials:]_block_invoke.321
- ___57-[SSAccountStore updateAccountWithAuthKit:store:options:]_block_invoke.253
- ___57-[SSAccountStore updateAccountWithAuthKit:store:options:]_block_invoke.264
- ___65-[SSAccountStore _updateAccountWithAuthKitViaSilentAuth:options:]_block_invoke.366
- ___71-[SSAccountStore _updateAccountWithAuthKitViaPromptAuth:store:options:]_block_invoke.360
- ___73-[SSAccountStore _updateAccountWithAuthKitViaSilentPasswordAuth:options:]_block_invoke.370
- ___block_literal_global.189
- ___block_literal_global.198
- ___block_literal_global.202
- ___block_literal_global.225
- ___block_literal_global.268
- ___block_literal_global.307
- ___block_literal_global.617
CStrings:
+ "_setError"
+ "getBytes:range:"
+ "hasError"
+ "initWithBundleIDs:states:"
+ "position"
+ "setPosition:"

```
