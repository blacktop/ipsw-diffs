## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-622.1.21.10.3
-  __TEXT.__text: 0xe9728
-  __TEXT.__auth_stubs: 0x2310
+622.1.22.10.4
+  __TEXT.__text: 0xe9814
+  __TEXT.__auth_stubs: 0x2360
   __TEXT.__objc_methlist: 0x758c
   __TEXT.__const: 0xec64
   __TEXT.__gcc_except_tab: 0x13ec
-  __TEXT.__cstring: 0xb526
+  __TEXT.__cstring: 0xb2d6
   __TEXT.__oslogstring: 0x2ee7
   __TEXT.__dlopen_cstrs: 0x308
   __TEXT.__ustring: 0x6d4e
   __TEXT.__constg_swiftt: 0x14d8
-  __TEXT.__swift5_typeref: 0x1dfe
+  __TEXT.__swift5_typeref: 0x1e3a
   __TEXT.__swift5_reflstr: 0x1333
   __TEXT.__swift5_fieldmd: 0x218c
   __TEXT.__swift5_builtin: 0x190

   __TEXT.__swift_as_ret: 0xf8
   __TEXT.__swift5_mpenum: 0x90
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x4118
+  __TEXT.__unwind_info: 0x4120
   __TEXT.__eh_frame: 0x31b0
   __TEXT.__objc_classname: 0x1fc7
   __TEXT.__objc_methname: 0x16223

   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x170
-  __AUTH_CONST.__auth_got: 0x11a0
+  __AUTH_CONST.__auth_got: 0x11c8
   __AUTH_CONST.__const: 0x6098
   __AUTH_CONST.__cfstring: 0x4560
   __AUTH_CONST.__objc_const: 0xe668

   __AUTH.__objc_data: 0x3490
   __AUTH.__data: 0xe90
   __DATA.__objc_ivar: 0x6e0
-  __DATA.__data: 0x2ac8
+  __DATA.__data: 0x2ad0
   __DATA.__bss: 0xc490
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C78A8A74-B7C7-302D-8AA7-EF569D27CC74
+  UUID: 61F161E4-E30B-329B-983A-8968FD5AE7F6
   Functions: 5921
-  Symbols:   10550
-  CStrings:  5375
+  Symbols:   10551
+  CStrings:  5363
 
Symbols:
+ _swift_getTupleTypeMetadata
+ _symbolic _____7service_SS12providerName_____8biometry_____22accountCreationOptionst 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO So14LABiometryTypeV 0aB4Core38ASCPublicKeyAccountRegistrationOptionsC
+ _symbolic _____7service______8biometry_____22accountCreationOptionst 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO So14LABiometryTypeV 0aB4Core38ASCPublicKeyAccountRegistrationOptionsC
- _symbolic _____7service_SS12providerName_____8biometryt 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO So14LABiometryTypeV
- _symbolic _____7service______8biometryt 22AuthenticationServices24ASAuthorizationUIContextV7ServiceO So14LABiometryTypeV
CStrings:
+ "service biometry accountCreationOptions "
+ "service providerName biometry accountCreationOptions "
+ "“%@” requires a phone number to create an account. Your account will be protected by a passkey, a secure alternative to a password, that will be saved in “%@”."
+ "“%@” requires a phone number to create an account. Your account will be protected by a passkey, a secure alternative to a password."
+ "“%@” requires an email address or phone number to create an account. Your account will be protected by a passkey, a secure alternative to a password, that will be saved in “%@”."
+ "“%@” requires an email address or phone number to create an account. Your account will be protected by a passkey, a secure alternative to a password."
+ "“%@” requires an email address to create an account. Your account will be protected by a passkey, a secure alternative to a password, that will be saved in “%@”."
+ "“%@” requires an email address to create an account. Your account will be protected by a passkey, a secure alternative to a password."
+ "“%@” requires your name and a phone number to create an account. Your account will be protected by a passkey, a secure alternative to a password, that will be saved in “%@”."
+ "“%@” requires your name and a phone number to create an account. Your account will be protected by a passkey, a secure alternative to a password."
+ "“%@” requires your name and an email address or phone number to create an account. Your account will be protected by a passkey, a secure alternative to a password, that will be saved in “%@”."
+ "“%@” requires your name and an email address or phone number to create an account. Your account will be protected by a passkey, a secure alternative to a password."
+ "“%@” requires your name and an email address to create an account. Your account will be protected by a passkey, a secure alternative to a password, that will be saved in “%@”."
+ "“%@” requires your name and an email address to create an account. Your account will be protected by a passkey, a secure alternative to a password."
- "An account will be created for “%@” with a passkey saved in “%@”."
- "An account will be created for “%@” with a passkey saved in “%@”. (app)"
- "An account will be created for “%@” with a passkey saved in “%@”. (website)"
- "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Face\u00a0ID."
- "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Face\u00a0ID. (app)"
- "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Face\u00a0ID. (website)"
- "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Optic\u00a0ID."
- "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Optic\u00a0ID. (app)"
- "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Optic\u00a0ID. (website)"
- "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Touch\u00a0ID."
- "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Touch\u00a0ID. (app)"
- "An account will be created for “%@” with a passkey saved in “%@”. You can sign in to this account with Touch\u00a0ID. (website)"
- "An account will be created for “%@” with a passkey."
- "An account will be created for “%@” with a passkey. (app)"
- "An account will be created for “%@” with a passkey. (website)"
- "An account will be created for “%@” with a passkey. You can sign in to this account with Face\u00a0ID."
- "An account will be created for “%@” with a passkey. You can sign in to this account with Face\u00a0ID. (app)"
- "An account will be created for “%@” with a passkey. You can sign in to this account with Face\u00a0ID. (website)"
- "An account will be created for “%@” with a passkey. You can sign in to this account with Optic\u00a0ID."
- "An account will be created for “%@” with a passkey. You can sign in to this account with Optic\u00a0ID. (app)"
- "An account will be created for “%@” with a passkey. You can sign in to this account with Optic\u00a0ID. (website)"
- "An account will be created for “%@” with a passkey. You can sign in to this account with Touch\u00a0ID."
- "An account will be created for “%@” with a passkey. You can sign in to this account with Touch\u00a0ID. (app)"
- "An account will be created for “%@” with a passkey. You can sign in to this account with Touch\u00a0ID. (website)"
- "service biometry "
- "service providerName biometry "

```
