## Social

> `/System/iOSSupport/System/Library/Frameworks/Social.framework/Versions/A/Social`

```diff

-762.0.0.0.0
-  __TEXT.__text: 0x39224
+763.0.0.0.0
+  __TEXT.__text: 0x3980c
   __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x4260
+  __TEXT.__objc_methlist: 0x4320
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x956e
+  __TEXT.__cstring: 0x95f8
   __TEXT.__gcc_except_tab: 0x4f0
   __TEXT.__ustring: 0x59c
   __TEXT.__oslogstring: 0x73
   __TEXT.__dlopen_cstrs: 0x43
-  __TEXT.__unwind_info: 0x1008
-  __TEXT.__objc_classname: 0xdfc
-  __TEXT.__objc_methname: 0xd4c3
-  __TEXT.__objc_methtype: 0x36fe
-  __TEXT.__objc_stubs: 0x8e40
-  __DATA_CONST.__got: 0x700
+  __TEXT.__unwind_info: 0x1028
+  __TEXT.__objc_classname: 0xe1b
+  __TEXT.__objc_methname: 0xd763
+  __TEXT.__objc_methtype: 0x3755
+  __TEXT.__objc_stubs: 0x8f40
+  __DATA_CONST.__got: 0x738
   __DATA_CONST.__const: 0x1038
-  __DATA_CONST.__objc_classlist: 0x308
+  __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2cf8
+  __DATA_CONST.__objc_selrefs: 0x2d48
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x208
-  __DATA_CONST.__objc_arraydata: 0x128
+  __DATA_CONST.__objc_superrefs: 0x210
+  __DATA_CONST.__objc_arraydata: 0x140
   __AUTH_CONST.__auth_got: 0x680
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x6bc0
-  __AUTH_CONST.__objc_const: 0x116a0
+  __AUTH_CONST.__cfstring: 0x6c60
+  __AUTH_CONST.__objc_const: 0x11a80
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0xd20
+  __AUTH.__objc_data: 0xd70
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x5fc
+  __DATA.__objc_ivar: 0x624
   __DATA.__data: 0xe40
   __DATA.__bss: 0x448
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1520
-  Symbols:   4772
-  CStrings:  921
+  Functions: 1538
+  Symbols:   4820
+  CStrings:  927
 
Symbols:
+ +[SLGoogleWebClient dataclassesForScopes:]
+ -[SLGoogleOAuth2TokenResponse grantedDataclasses]
+ -[SLGoogleWebClient loginScopes]
+ -[SLWebAuthIdentity grantedDataclasses]
+ -[SLWebAuthIdentity initWithUsername:token:displayName:refreshToken:youTubeUsername:idToken:grantedDataclasses:]
+ -[SLWebTokenHandlerController _fetchNamesForAuthResponse:completion:]
+ -[SLWebTokenHandlerController exchangeAuthCode:usingRedirect:codeVerifier:forAccountResponse:]
+ -[SLWebTokenHandlerResponse .cxx_destruct]
+ -[SLWebTokenHandlerResponse displayName]
+ -[SLWebTokenHandlerResponse expiryDate]
+ -[SLWebTokenHandlerResponse grantedDataclasses]
+ -[SLWebTokenHandlerResponse idToken]
+ -[SLWebTokenHandlerResponse initWithTokenResponse:usernames:displayname:]
+ -[SLWebTokenHandlerResponse refreshToken]
+ -[SLWebTokenHandlerResponse setToken:]
+ -[SLWebTokenHandlerResponse token]
+ -[SLWebTokenHandlerResponse usernames]
+ -[SLYahooWebOAuth2TokenResponse grantedDataclasses]
+ OBJC_IVAR_$_SLGoogleOAuth2TokenResponse._grantedDataclasses
+ OBJC_IVAR_$_SLWebAuthIdentity._grantedDataclasses
+ OBJC_IVAR_$_SLWebTokenHandlerResponse._displayName
+ OBJC_IVAR_$_SLWebTokenHandlerResponse._expiryDate
+ OBJC_IVAR_$_SLWebTokenHandlerResponse._grantedDataclasses
+ OBJC_IVAR_$_SLWebTokenHandlerResponse._idToken
+ OBJC_IVAR_$_SLWebTokenHandlerResponse._refreshToken
+ OBJC_IVAR_$_SLWebTokenHandlerResponse._token
+ OBJC_IVAR_$_SLWebTokenHandlerResponse._usernames
+ OBJC_IVAR_$_SLYahooWebOAuth2TokenResponse._grantedDataclasses
+ _ACAccountDataclassCalendars
+ _ACAccountDataclassContacts
+ _ACAccountDataclassMail
+ _ACAccountDataclassNotes
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_SLWebTokenHandlerResponse
+ _OBJC_METACLASS_$_SLWebTokenHandlerResponse
+ __OBJC_$_INSTANCE_METHODS_SLWebTokenHandlerResponse
+ __OBJC_$_INSTANCE_VARIABLES_SLWebTokenHandlerResponse
+ __OBJC_$_PROP_LIST_SLWebTokenHandlerResponse
+ __OBJC_CLASS_RO_$_SLWebTokenHandlerResponse
+ __OBJC_METACLASS_RO_$_SLWebTokenHandlerResponse
+ ___69-[SLWebTokenHandlerController _fetchNamesForAuthResponse:completion:]_block_invoke
+ ___69-[SLWebTokenHandlerController _fetchNamesForAuthResponse:completion:]_block_invoke_2
+ ___94-[SLWebTokenHandlerController exchangeAuthCode:usingRedirect:codeVerifier:forAccountResponse:]_block_invoke
+ ___94-[SLWebTokenHandlerController exchangeAuthCode:usingRedirect:codeVerifier:forAccountResponse:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e47_v24?0"SLWebTokenHandlerResponse"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e42_v32?0"NSArray"8"NSString"16"NSError"24ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e48_v24?0"<SLWebOAuth2TokenResponse>"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8s48l8s40l8
+ _objc_msgSend$_fetchNamesForAuthResponse:completion:
+ _objc_msgSend$allObjects
+ _objc_msgSend$dataclassesForScopes:
+ _objc_msgSend$exchangeAuthCode:usingRedirect:codeVerifier:forAccountResponse:
+ _objc_msgSend$grantedDataclasses
+ _objc_msgSend$initWithTokenResponse:usernames:displayname:
+ _objc_msgSend$initWithUsername:token:displayName:refreshToken:youTubeUsername:idToken:grantedDataclasses:
+ _objc_msgSend$set
+ _objc_msgSend$usernames
- -[SLWebTokenHandlerController _fetchNamesForToken:idToken:completion:]
- ___110-[SLWebTokenHandlerController exchangeAuthCode:usingRedirect:codeVerifier:forTokensAndUsernameWithCompletion:]_block_invoke_2
- ___70-[SLWebTokenHandlerController _fetchNamesForToken:idToken:completion:]_block_invoke
- ___70-[SLWebTokenHandlerController _fetchNamesForToken:idToken:completion:]_block_invoke_2
- ___block_descriptor_48_e8_32s40bs_e67_v48?0"NSString"8"NSString"16"NSString"24"NSDate"32"NSError"40ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8s56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e42_v32?0"NSArray"8"NSString"16"NSError"24ls64l8s32l8s40l8s48l8s56l8
- _objc_msgSend$_fetchNamesForToken:idToken:completion:
CStrings:
+ "enable_granular_consent"
+ "enable_granular_consent=true"
+ "include_granted_scopes"
+ "include_granted_scopes=true"
+ "true"
+ "v24@?0@\"<SLWebOAuth2TokenResponse>\"8@\"NSError\"16"
+ "v24@?0@\"SLWebTokenHandlerResponse\"8@\"NSError\"16"
- "v48@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24@\"NSDate\"32@\"NSError\"40"

```
