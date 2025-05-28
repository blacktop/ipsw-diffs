## SafariServices

> `/System/Library/Frameworks/SafariServices.framework/SafariServices`

```diff

-617.1.17.10.9
-  __TEXT.__text: 0x178514
+617.2.4.10.7
+  __TEXT.__text: 0x1785f8
   __TEXT.__auth_stubs: 0x17e0
   __TEXT.__objc_methlist: 0x149d8
   __TEXT.__const: 0x3ed8
   __TEXT.__cstring: 0xe368
   __TEXT.__gcc_except_tab: 0xaf68
-  __TEXT.__oslogstring: 0x7865
+  __TEXT.__oslogstring: 0x7905
   __TEXT.__ustring: 0x33ce
   __TEXT.__dlopen_cstrs: 0x795
-  __TEXT.__unwind_info: 0x81d8
+  __TEXT.__unwind_info: 0x81e0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x4dcb
-  __TEXT.__objc_methname: 0x57e45
+  __TEXT.__objc_methname: 0x57ecf
   __TEXT.__objc_methtype: 0x11e6b
   __TEXT.__objc_stubs: 0x35920
   __DATA_CONST.__got: 0xc58

   __DATA_CONST.__objc_protolist: 0x840
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x30bb8
-  __DATA_CONST.__objc_selrefs: 0xfe50
+  __DATA_CONST.__objc_selrefs: 0xfe58
   __DATA_CONST.__objc_arraydata: 0x768
   __AUTH_CONST.__cfstring: 0xd500
   __AUTH_CONST.__const: 0x18e8

   - /usr/lib/libsqlite3.dylib
   Functions: 8958
   Symbols:   34673
-  CStrings:  16491
+  CStrings:  16493
 
Symbols:
+ -[SFAddSavedAccountViewController setShouldPopulatePasswordFieldWithNewGeneratedStrongPassword:]
+ -[SFAddSavedAccountViewController shouldPopulatePasswordFieldWithNewGeneratedStrongPassword]
+ _OBJC_IVAR_$_SFAddSavedAccountViewController._shouldPopulatePasswordFieldWithNewGeneratedStrongPassword
+ ___73-[_SFAuthenticationContext _evaluatePolicyForClient:userInitiated:reply:]_block_invoke.66
+ ___73-[_SFAuthenticationContext _evaluatePolicyForClient:userInitiated:reply:]_block_invoke_2.67
+ _objc_msgSend$isDTOMitigationEnabled
+ _objc_msgSend$setShouldPopulatePasswordFieldWithNewGeneratedStrongPassword:
+ _objc_msgSend$shouldPopulatePasswordFieldWithNewGeneratedStrongPassword
- -[SFAddSavedAccountViewController setShouldPreFillStrongPassword:]
- -[SFAddSavedAccountViewController shouldPreFillStrongPassword]
- _OBJC_IVAR_$_SFAddSavedAccountViewController._shouldPreFillStrongPassword
- ___73-[_SFAuthenticationContext _evaluatePolicyForClient:userInitiated:reply:]_block_invoke.65
- ___73-[_SFAuthenticationContext _evaluatePolicyForClient:userInitiated:reply:]_block_invoke_2.66
- _objc_msgSend$initWithSuggestedDomain:
- _objc_msgSend$setShouldPreFillStrongPassword:
- _objc_msgSend$shouldPreFillStrongPassword
CStrings:
+ "Newly created saved account has a password that doesn't match the generated password record it was created from. The generated password record was not deleted."
+ "TB,N,V_shouldPopulatePasswordFieldWithNewGeneratedStrongPassword"
+ "_shouldPopulatePasswordFieldWithNewGeneratedStrongPassword"
+ "isDTOMitigationEnabled"
+ "setShouldPopulatePasswordFieldWithNewGeneratedStrongPassword:"
+ "shouldPopulatePasswordFieldWithNewGeneratedStrongPassword"
- "TB,N,V_shouldPreFillStrongPassword"
- "_shouldPreFillStrongPassword"
- "setShouldPreFillStrongPassword:"
- "shouldPreFillStrongPassword"

```
