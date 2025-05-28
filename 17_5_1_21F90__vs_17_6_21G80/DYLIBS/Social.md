## Social

> `/System/Library/Frameworks/Social.framework/Social`

```diff

-759.0.0.0.0
-  __TEXT.__text: 0x3cdb8
+759.1.0.0.0
+  __TEXT.__text: 0x3d3a0
   __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_methlist: 0x42cc
+  __TEXT.__objc_methlist: 0x4390
   __TEXT.__const: 0x9f0
-  __TEXT.__cstring: 0x9a70
+  __TEXT.__cstring: 0x9afa
   __TEXT.__gcc_except_tab: 0x470
   __TEXT.__ustring: 0x604
   __TEXT.__oslogstring: 0x73
   __TEXT.__dlopen_cstrs: 0x43
-  __TEXT.__unwind_info: 0x1048
-  __TEXT.__objc_classname: 0xdfc
-  __TEXT.__objc_methname: 0xd7fb
-  __TEXT.__objc_methtype: 0x368c
-  __TEXT.__objc_stubs: 0x9180
-  __DATA_CONST.__got: 0x2d0
+  __TEXT.__unwind_info: 0x106c
+  __TEXT.__objc_classname: 0xe1b
+  __TEXT.__objc_methname: 0xd9e3
+  __TEXT.__objc_methtype: 0x36a9
+  __TEXT.__objc_stubs: 0x9280
+  __DATA_CONST.__got: 0x2f0
   __DATA_CONST.__const: 0x10d8
-  __DATA_CONST.__objc_classlist: 0x308
+  __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf540
-  __DATA_CONST.__objc_selrefs: 0x2df0
+  __DATA_CONST.__objc_const: 0xf7d8
+  __DATA_CONST.__objc_selrefs: 0x2e40
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_classrefs: 0x4f0
-  __DATA_CONST.__objc_superrefs: 0x208
-  __DATA_CONST.__objc_arraydata: 0x128
+  __DATA_CONST.__objc_classrefs: 0x508
+  __DATA_CONST.__objc_superrefs: 0x210
+  __DATA_CONST.__objc_arraydata: 0x140
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__objc_const: 0x2490
-  __AUTH_CONST.__cfstring: 0x7000
+  __AUTH_CONST.__objc_const: 0x24d8
+  __AUTH_CONST.__cfstring: 0x70a0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__auth_got: 0x708
-  __AUTH.__objc_data: 0x1db0
+  __AUTH.__objc_data: 0x1e00
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x604
+  __DATA.__objc_ivar: 0x62c
   __DATA.__data: 0xe80
   __DATA.__bss: 0x438
   __DATA.__common: 0x8

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1547
-  Symbols:   6410
-  CStrings:  3724
+  Functions: 1565
+  Symbols:   6477
+  CStrings:  3752
 
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
+ _ACAccountDataclassCalendars
+ _ACAccountDataclassContacts
+ _ACAccountDataclassMail
+ _ACAccountDataclassNotes
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_SLWebTokenHandlerResponse
+ _OBJC_IVAR_$_SLGoogleOAuth2TokenResponse._grantedDataclasses
+ _OBJC_IVAR_$_SLWebAuthIdentity._grantedDataclasses
+ _OBJC_IVAR_$_SLWebTokenHandlerResponse._displayName
+ _OBJC_IVAR_$_SLWebTokenHandlerResponse._expiryDate
+ _OBJC_IVAR_$_SLWebTokenHandlerResponse._grantedDataclasses
+ _OBJC_IVAR_$_SLWebTokenHandlerResponse._idToken
+ _OBJC_IVAR_$_SLWebTokenHandlerResponse._refreshToken
+ _OBJC_IVAR_$_SLWebTokenHandlerResponse._token
+ _OBJC_IVAR_$_SLWebTokenHandlerResponse._usernames
+ _OBJC_IVAR_$_SLYahooWebOAuth2TokenResponse._grantedDataclasses
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
+ __unnamed_array_storage.32
+ __unnamed_array_storage.44
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
- __unnamed_array_storage.38
- _objc_msgSend$_fetchNamesForToken:idToken:completion:
CStrings:
+ "\x06\x13"
+ "\a"
+ "@72@0:8@16@24@32@40@48@56@64"
+ "SLWebTokenHandlerResponse"
+ "T@\"NSArray\",R"
+ "T@\"NSArray\",R,N,V_grantedDataclasses"
+ "T@\"NSArray\",R,N,V_usernames"
+ "T@\"NSArray\",R,V_grantedDataclasses"
+ "T@\"NSDate\",R,N,V_expiryDate"
+ "T@\"NSString\",&,N,V_token"
+ "_fetchNamesForAuthResponse:completion:"
+ "_grantedDataclasses"
+ "_usernames"
+ "allObjects"
+ "dataclassesForScopes:"
+ "enable_granular_consent"
+ "enable_granular_consent=true"
+ "exchangeAuthCode:usingRedirect:codeVerifier:forAccountResponse:"
+ "grantedDataclasses"
+ "include_granted_scopes"
+ "include_granted_scopes=true"
+ "initWithTokenResponse:usernames:displayname:"
+ "initWithUsername:token:displayName:refreshToken:youTubeUsername:idToken:grantedDataclasses:"
+ "loginScopes"
+ "set"
+ "setToken:"
+ "true"
+ "v24@?0@\"<SLWebOAuth2TokenResponse>\"8@\"NSError\"16"
+ "v24@?0@\"SLWebTokenHandlerResponse\"8@\"NSError\"16"
- "_fetchNamesForToken:idToken:completion:"
- "v48@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24@\"NSDate\"32@\"NSError\"40"

```
