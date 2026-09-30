## EmailCore

> `/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore`

```diff

-3860.100.5.2.1
-  __TEXT.__text: 0x540fc
+3863.100.1.2.5
+  __TEXT.__text: 0x54674
   __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_methlist: 0x4ed8
+  __TEXT.__objc_methlist: 0x4f28
   __TEXT.__const: 0xe70
-  __TEXT.__gcc_except_tab: 0x6dd8
-  __TEXT.__cstring: 0x7cc4
+  __TEXT.__gcc_except_tab: 0x6e94
+  __TEXT.__cstring: 0x7d04
   __TEXT.__oslogstring: 0xcd8
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x52
   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x27c0
-  __TEXT.__objc_classname: 0xce4
-  __TEXT.__objc_methname: 0xad83
-  __TEXT.__objc_methtype: 0x1706
-  __TEXT.__objc_stubs: 0x7600
-  __DATA_CONST.__got: 0x6a0
-  __DATA_CONST.__const: 0x21e0
-  __DATA_CONST.__objc_classlist: 0x320
+  __TEXT.__unwind_info: 0x2800
+  __TEXT.__objc_classname: 0xcfc
+  __TEXT.__objc_methname: 0xae68
+  __TEXT.__objc_methtype: 0x171b
+  __TEXT.__objc_stubs: 0x7620
+  __DATA_CONST.__got: 0x6a8
+  __DATA_CONST.__const: 0x2208
+  __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2958
+  __DATA_CONST.__objc_selrefs: 0x2978
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__auth_got: 0x830
-  __AUTH_CONST.__const: 0x6f8
-  __AUTH_CONST.__cfstring: 0x5280
-  __AUTH_CONST.__objc_const: 0x9c58
+  __AUTH_CONST.__const: 0x718
+  __AUTH_CONST.__cfstring: 0x52a0
+  __AUTH_CONST.__objc_const: 0x9cf8
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH.__objc_data: 0x1b0
+  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH.__objc_data: 0x390
   __AUTH.__data: 0x88
   __DATA.__objc_ivar: 0x4a4
   __DATA.__data: 0xd44
-  __DATA.__bss: 0x3a0
+  __DATA.__bss: 0x3b0
   __DATA.__common: 0x24
-  __DATA_DIRTY.__objc_data: 0x1db0
+  __DATA_DIRTY.__objc_data: 0x1c20
   __DATA_DIRTY.__data: 0xb50
   __DATA_DIRTY.__bss: 0x208
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F8EC0ADA-4D63-3EDF-BEFB-92F164279366
-  Functions: 1911
-  Symbols:   7547
-  CStrings:  4451
+  UUID: 29D31393-7998-33ED-8C9E-CC8F3BF6284B
+  Functions: 1921
+  Symbols:   7584
+  CStrings:  4461
 
Symbols:
+ +[ECDMARCVerifier _alignmentForDKIMSigningDomain:andSenderDomain:senderOrganizationDomain:onlyCheckStrictAlignment:]
+ +[ECDMARCVerifier alignmentForDKIMSigningDomain:andSenderDomain:]
+ -[ECDKIMServerStatement .cxx_destruct]
+ -[ECDKIMServerStatement dkimServerResultSelector]
+ -[ECDKIMServerStatement dkimServerResult]
+ -[ECDKIMServerStatement dkimServerSigningDomain]
+ -[ECDKIMServerStatement setDkimServerResult:]
+ -[ECDKIMServerStatement setDkimServerResultSelector:]
+ -[ECDKIMServerStatement setDkimServerSigningDomain:]
+ -[ECMessageAuthenticationResult dkimServerStatements]
+ -[ECMessageAuthenticationResult setDkimServerStatements:]
+ -[ECMessageAuthenticator _resultForDKIMStatement:]
+ -[ECMessageAuthenticator _resultForDKIMStatement:].cold.1
+ -[ECMessageAuthenticator _resultForDMARCStatement:]
+ -[ECMessageAuthenticator _resultForDMARCStatement:].cold.1
+ -[ECMessageAuthenticator _signingDomainForDKIMStatement:]
+ _OBJC_CLASS_$_ECDKIMServerStatement
+ _OBJC_IVAR_$_ECDKIMServerStatement._dkimServerResult
+ _OBJC_IVAR_$_ECDKIMServerStatement._dkimServerResultSelector
+ _OBJC_IVAR_$_ECDKIMServerStatement._dkimServerSigningDomain
+ _OBJC_IVAR_$_ECMessageAuthenticationResult._dkimServerStatements
+ _OBJC_METACLASS_$_ECDKIMServerStatement
+ __OBJC_$_INSTANCE_METHODS_ECDKIMServerStatement
+ __OBJC_$_INSTANCE_VARIABLES_ECDKIMServerStatement
+ __OBJC_$_PROP_LIST_ECDKIMServerStatement
+ __OBJC_$_PROP_LIST_ECMessageBodyElement.248
+ __OBJC_CLASS_RO_$_ECDKIMServerStatement
+ __OBJC_METACLASS_RO_$_ECDKIMServerStatement
+ ___50-[ECMessageAuthenticator _resultForDKIMStatement:]_block_invoke
+ ___51-[ECMessageAuthenticator _resultForDMARCStatement:]_block_invoke
+ ___block_descriptor_56_ea8_32s40s48r_e54_v32?0"ECHeaderAuthenticationResultStatement"8Q16^B24ls32l8r48l8s40l8
+ ___block_literal_global.251
+ ___block_literal_global.257
+ __resultForDKIMStatement:.kDKIMResultByResultString
+ __resultForDKIMStatement:.onceToken
+ __resultForDMARCStatement:.kDMARCStatusByResultString
+ __resultForDMARCStatement:.onceToken
+ _objc_msgSend$_alignmentForDKIMSigningDomain:andSenderDomain:senderOrganizationDomain:onlyCheckStrictAlignment:
+ _objc_msgSend$_resultForDKIMStatement:
+ _objc_msgSend$_resultForDMARCStatement:
+ _objc_msgSend$_signingDomainForDKIMStatement:
+ _objc_msgSend$setDkimServerResult:
+ _objc_msgSend$setDkimServerStatements:
- -[ECMessageAuthenticationResult dkimHasServerResult]
- -[ECMessageAuthenticationResult dkimServerResultSelector]
- -[ECMessageAuthenticationResult dkimServerSigningDomain]
- -[ECMessageAuthenticationResult dkimServerVerified]
- -[ECMessageAuthenticationResult setDkimHasServerResult:]
- -[ECMessageAuthenticationResult setDkimServerResultSelector:]
- -[ECMessageAuthenticationResult setDkimServerSigningDomain:]
- -[ECMessageAuthenticationResult setDkimServerVerified:]
- -[ECMessageAuthenticator _addServerResultsFromMessage:toResult:].cold.1
- -[ECMessageBodyElement reset]
- _OBJC_IVAR_$_ECMessageAuthenticationResult._dkimHasServerResult
- _OBJC_IVAR_$_ECMessageAuthenticationResult._dkimServerResultSelector
- _OBJC_IVAR_$_ECMessageAuthenticationResult._dkimServerSigningDomain
- _OBJC_IVAR_$_ECMessageAuthenticationResult._dkimServerVerified
- __OBJC_$_PROP_LIST_ECMessageBodyElement.249
- ___block_literal_global.252
- ___block_literal_global.279
- __addServerResultsFromMessage:toResult:.kDMARCStatusByResultString
- __addServerResultsFromMessage:toResult:.onceToken
- _objc_msgSend$dkimHasServerResult
- _objc_msgSend$firstStatementForMethod:
- _objc_msgSend$reset
- _objc_msgSend$setDkimHasServerResult:
- _objc_msgSend$setDkimServerVerified:
CStrings:
+ "?"
+ "ECDKIMServerStatement"
+ "T@\"NSArray\",C,N,V_dkimServerStatements"
+ "Tq,N,V_dkimServerResult"
+ "_alignmentForDKIMSigningDomain:andSenderDomain:senderOrganizationDomain:onlyCheckStrictAlignment:"
+ "_dkimServerResult"
+ "_dkimServerStatements"
+ "_resultForDKIMStatement:"
+ "_resultForDMARCStatement:"
+ "_signingDomainForDKIMStatement:"
+ "alignmentForDKIMSigningDomain:andSenderDomain:"
+ "dkimServerResult"
+ "dkimServerStatements"
+ "neutral"
+ "q44@0:8@16@24^@32B40"
+ "setDkimServerResult:"
+ "setDkimServerStatements:"
+ "v32@?0@\"ECHeaderAuthenticationResultStatement\"8Q16^B24"
- "TB,N,V_dkimHasServerResult"
- "TB,N,V_dkimServerVerified"
- "_dkimHasServerResult"
- "_dkimServerVerified"
- "dkimHasServerResult"
- "dkimServerVerified"
- "reset"
- "setDkimHasServerResult:"
- "setDkimServerVerified:"

```
