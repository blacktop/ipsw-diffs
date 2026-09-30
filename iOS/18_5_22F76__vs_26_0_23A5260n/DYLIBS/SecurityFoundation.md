## SecurityFoundation

> `/System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation`

```diff

-55290.0.0.0.0
-  __TEXT.__text: 0x10954
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x2ee0
+55293.0.0.0.0
+  __TEXT.__text: 0x1377c
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_methlist: 0x3310
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x922
+  __TEXT.__cstring: 0x9fb
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__unwind_info: 0x8e0
-  __TEXT.__objc_classname: 0xc6f
-  __TEXT.__objc_methname: 0x306f
-  __TEXT.__objc_methtype: 0xe25
-  __TEXT.__objc_stubs: 0x17e0
-  __DATA_CONST.__got: 0x418
+  __TEXT.__unwind_info: 0x980
+  __TEXT.__objc_classname: 0xcb6
+  __TEXT.__objc_methname: 0x3448
+  __TEXT.__objc_methtype: 0xf43
+  __TEXT.__objc_stubs: 0x1ac0
+  __DATA_CONST.__got: 0x438
   __DATA_CONST.__const: 0x258
-  __DATA_CONST.__objc_classlist: 0x3f0
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_classlist: 0x400
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf8
-  __DATA_CONST.__objc_superrefs: 0x210
-  __AUTH_CONST.__auth_got: 0x478
+  __DATA_CONST.__objc_selrefs: 0xc20
+  __DATA_CONST.__objc_superrefs: 0x220
+  __AUTH_CONST.__auth_got: 0x4a8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x840
-  __AUTH_CONST.__objc_const: 0x81c8
-  __DATA.__objc_ivar: 0x314
-  __DATA.__data: 0x5a0
+  __AUTH_CONST.__cfstring: 0x980
+  __AUTH_CONST.__objc_const: 0x8448
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x320
+  __DATA.__data: 0x6a8
   __DATA_DIRTY.__objc_data: 0x2760
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D26BEFC-5DBF-3FA5-85B6-C40FDFD43012
-  Functions: 844
-  Symbols:   3364
-  CStrings:  971
+  UUID: 7E3229AD-4CBE-30F4-8096-4FCBF28D952C
+  Functions: 915
+  Symbols:   3567
+  CStrings:  1041
 
Symbols:
+ +[SPAKE2WebVerifier generateCodeWithError:]
+ -[SPAKE2Common _decodeBase64:withKey:info:error:]
+ -[SPAKE2Common _decodeBinary:withKey:info:error:]
+ -[SPAKE2Common _decryptMessageInBase64:info:error:]
+ -[SPAKE2Common _decryptMessageInBinary:info:error:]
+ -[SPAKE2Common _encodeBase64:withKey:info:error:]
+ -[SPAKE2Common _encodeBinary:withKey:info:error:]
+ -[SPAKE2Common _encryptMessageAsBase64:info:error:]
+ -[SPAKE2Common _encryptMessageAsBinary:info:error:]
+ -[SPAKE2Common getRawSessionKey]
+ -[SPAKE2Common getSessionKey]
+ -[SPAKE2Common initWithSalt:code:rng:cp:]
+ -[SPAKE2Common processMsg2Orig:error:]
+ -[SPAKE2Common processMsg2Web:error:]
+ -[SPAKE2Common raw_session_key]
+ -[SPAKE2Common setRaw_session_key:]
+ -[SPAKE2Common setupRFCProver:]
+ -[SPAKE2Common setupRFCVerifier:]
+ -[SPAKE2Prover hasKey]
+ -[SPAKE2Prover initWithSalt:code:rng:error:]
+ -[SPAKE2Prover keyMatchesWith:]
+ -[SPAKE2Prover testGetW0]
+ -[SPAKE2Prover testGetW1]
+ -[SPAKE2Verifier hasKey]
+ -[SPAKE2Verifier keyMatchesWith:]
+ -[SPAKE2Verifier testGetW0]
+ -[SPAKE2Verifier testGetW1]
+ -[SPAKE2WebProver .cxx_destruct]
+ -[SPAKE2WebProver _decodeBase64:withKey:error:]
+ -[SPAKE2WebProver _decodeBinary:withKey:error:]
+ -[SPAKE2WebProver _encodeBase64:withKey:error:]
+ -[SPAKE2WebProver _encodeBinary:withKey:error:]
+ -[SPAKE2WebProver common]
+ -[SPAKE2WebProver decryptMessageInBase64:error:]
+ -[SPAKE2WebProver decryptMessageInBinary:error:]
+ -[SPAKE2WebProver encryptMessageAsBase64:error:]
+ -[SPAKE2WebProver encryptMessageAsBinary:error:]
+ -[SPAKE2WebProver getKey]
+ -[SPAKE2WebProver getMsg1WithError:]
+ -[SPAKE2WebProver getMsg2WithError:]
+ -[SPAKE2WebProver hasKey]
+ -[SPAKE2WebProver initWithSalt:code:error:]
+ -[SPAKE2WebProver initWithSalt:code:rng:error:]
+ -[SPAKE2WebProver isVerified]
+ -[SPAKE2WebProver keyMatchesWith:]
+ -[SPAKE2WebProver processMsg1:error:]
+ -[SPAKE2WebProver processMsg2:error:]
+ -[SPAKE2WebProver setCommon:]
+ -[SPAKE2WebProver testGetW0]
+ -[SPAKE2WebProver testGetW1]
+ -[SPAKE2WebVerifier .cxx_destruct]
+ -[SPAKE2WebVerifier _decodeBase64:withKey:error:]
+ -[SPAKE2WebVerifier _decodeBinary:withKey:error:]
+ -[SPAKE2WebVerifier _encodeBase64:withKey:error:]
+ -[SPAKE2WebVerifier _encodeBinary:withKey:error:]
+ -[SPAKE2WebVerifier common]
+ -[SPAKE2WebVerifier decryptMessageInBase64:error:]
+ -[SPAKE2WebVerifier decryptMessageInBinary:error:]
+ -[SPAKE2WebVerifier encryptMessageAsBase64:error:]
+ -[SPAKE2WebVerifier encryptMessageAsBinary:error:]
+ -[SPAKE2WebVerifier getCode]
+ -[SPAKE2WebVerifier getKey]
+ -[SPAKE2WebVerifier getMsg1WithError:]
+ -[SPAKE2WebVerifier getMsg2WithError:]
+ -[SPAKE2WebVerifier hasKey]
+ -[SPAKE2WebVerifier initWithSalt:code:error:]
+ -[SPAKE2WebVerifier initWithSalt:code:rng:error:]
+ -[SPAKE2WebVerifier isVerified]
+ -[SPAKE2WebVerifier keyMatchesWith:]
+ -[SPAKE2WebVerifier processMsg1:error:]
+ -[SPAKE2WebVerifier processMsg2:error:]
+ -[SPAKE2WebVerifier setCommon:]
+ -[SPAKE2WebVerifier testGetW0]
+ -[SPAKE2WebVerifier testGetW1]
+ _OBJC_CLASS_$_SPAKE2WebProver
+ _OBJC_CLASS_$_SPAKE2WebVerifier
+ _OBJC_IVAR_$_SPAKE2Common._raw_session_key
+ _OBJC_IVAR_$_SPAKE2WebProver._common
+ _OBJC_IVAR_$_SPAKE2WebVerifier._common
+ _OBJC_METACLASS_$_SPAKE2WebProver
+ _OBJC_METACLASS_$_SPAKE2WebVerifier
+ __OBJC_$_CLASS_METHODS_SPAKE2WebVerifier
+ __OBJC_$_INSTANCE_METHODS_SPAKE2WebProver
+ __OBJC_$_INSTANCE_METHODS_SPAKE2WebVerifier
+ __OBJC_$_INSTANCE_VARIABLES_SPAKE2WebProver
+ __OBJC_$_INSTANCE_VARIABLES_SPAKE2WebVerifier
+ __OBJC_$_PROP_LIST_SPAKE2WebProver
+ __OBJC_$_PROP_LIST_SPAKE2WebVerifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPAKE2ProtocolBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPAKE2ProtocolWeb
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SPAKE2ProtocolBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SPAKE2ProtocolWeb
+ __OBJC_$_PROTOCOL_REFS_SPAKE2Protocol
+ __OBJC_$_PROTOCOL_REFS_SPAKE2ProtocolWeb
+ __OBJC_CLASS_PROTOCOLS_$_SPAKE2WebProver
+ __OBJC_CLASS_PROTOCOLS_$_SPAKE2WebVerifier
+ __OBJC_CLASS_RO_$_SPAKE2WebProver
+ __OBJC_CLASS_RO_$_SPAKE2WebVerifier
+ __OBJC_LABEL_PROTOCOL_$_SPAKE2ProtocolBase
+ __OBJC_LABEL_PROTOCOL_$_SPAKE2ProtocolWeb
+ __OBJC_METACLASS_RO_$_SPAKE2WebProver
+ __OBJC_METACLASS_RO_$_SPAKE2WebVerifier
+ __OBJC_PROTOCOL_$_SPAKE2ProtocolBase
+ __OBJC_PROTOCOL_$_SPAKE2ProtocolWeb
+ _cc_clear
+ _ccgcm_one_shot
+ _cchkdf
+ _ccspake_cp_256_rfc
+ _ccspake_prover_initialize
+ _ccspake_verifier_initialize
+ _context
+ _idProver
+ _idVerifier
+ _objc_msgSend$_decodeBase64:withKey:info:error:
+ _objc_msgSend$_decodeBinary:withKey:info:error:
+ _objc_msgSend$_decryptMessageInBase64:info:error:
+ _objc_msgSend$_decryptMessageInBinary:info:error:
+ _objc_msgSend$_encodeBase64:withKey:info:error:
+ _objc_msgSend$_encodeBinary:withKey:info:error:
+ _objc_msgSend$_encryptMessageAsBase64:info:error:
+ _objc_msgSend$_encryptMessageAsBinary:info:error:
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$appendData:
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$dataWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$dataWithData:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$getRawSessionKey
+ _objc_msgSend$getSessionKey
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$initWithSalt:code:rng:cp:
+ _objc_msgSend$initWithSalt:code:rng:error:
+ _objc_msgSend$isEqualToData:
+ _objc_msgSend$processMsg2Orig:error:
+ _objc_msgSend$processMsg2Web:error:
+ _objc_msgSend$raw_session_key
+ _objc_msgSend$setRaw_session_key:
+ _objc_msgSend$setupRFCProver:
+ _objc_msgSend$setupRFCVerifier:
- -[SPAKE2Common getKey]
- -[SPAKE2Common initWithSalt:code:]
- -[SPAKE2Common processMsg2:error:]
- __OBJC_CLASS_PROTOCOLS_$_SPAKE2Common
- _objc_msgSend$getKey
- _objc_msgSend$initWithSalt:code:
- _objc_msgSend$processMsg2:error:
CStrings:
+ "2\"\""
+ "@\"NSData\"32@0:8@\"NSString\"16^@24"
+ "@\"NSData\"40@0:8@\"NSData\"16@\"NSData\"24^@32"
+ "@\"NSData\"40@0:8@\"NSString\"16@\"NSData\"24^@32"
+ "@\"NSString\"32@0:8@\"NSData\"16^@24"
+ "@\"NSString\"40@0:8@\"NSData\"16@\"NSData\"24^@32"
+ "@48@0:8@16@24^{ccrng_state=^?}32^@40"
+ "@48@0:8@16@24^{ccrng_state=^?}32^{ccspake_cp=}40"
+ "SPAKE2ProtocolBase"
+ "SPAKE2ProtocolWeb"
+ "SPAKE2WebProver"
+ "SPAKE2WebVerifier"
+ "T@\"NSMutableData\",&,V_raw_session_key"
+ "Tr^{ccdigest_info=QQQQ*^v^?^?i^?},?,R,N,G_ccDigestInfo"
+ "_decodeBase64:withKey:error:"
+ "_decodeBase64:withKey:info:error:"
+ "_decodeBinary:withKey:error:"
+ "_decodeBinary:withKey:info:error:"
+ "_decryptMessageInBase64:info:error:"
+ "_decryptMessageInBinary:info:error:"
+ "_encodeBase64:withKey:error:"
+ "_encodeBase64:withKey:info:error:"
+ "_encodeBinary:withKey:error:"
+ "_encodeBinary:withKey:info:error:"
+ "_encryptMessageAsBase64:info:error:"
+ "_encryptMessageAsBinary:info:error:"
+ "_raw_session_key"
+ "appendBytes:length:"
+ "appendData:"
+ "base64EncodedStringWithOptions:"
+ "ccgm_one_shot failed: %d"
+ "cchkdf failed: %d"
+ "ccspake_prover_initialize failed: %d"
+ "ccspake_verifier_initialize failed: %d"
+ "dataWithBytesNoCopy:length:freeWhenDone:"
+ "dataWithData:"
+ "dataWithLength:"
+ "decryptMessageInBase64:error:"
+ "decryptMessageInBinary:error:"
+ "encryptMessageAsBase64:error:"
+ "encryptMessageAsBinary:error:"
+ "failed to decode base64"
+ "getRawSessionKey"
+ "getSessionKey"
+ "hasKey"
+ "initWithBase64EncodedString:options:"
+ "initWithSalt:code:rng:cp:"
+ "initWithSalt:code:rng:error:"
+ "isEqualToData:"
+ "keyMatchesWith:"
+ "malloc failed"
+ "message too short"
+ "processMsg2Orig:error:"
+ "processMsg2Web:error:"
+ "r^{ccdigest_info=QQQQ*^v^?^?i^?}16@0:8"
+ "r^{ccdigest_info=QQQQ*^v^?^?i^?}24@0:8^@16"
+ "raw_session_key"
+ "setRaw_session_key:"
+ "setupRFCProver:"
+ "setupRFCVerifier:"
+ "testGetW0"
+ "testGetW1"
+ "unknown version: %d"
+ "webProver"
+ "webVerifier"
- "2\"!"
- "Tr^{ccdigest_info=QQQQ*^v^?^?i},?,R,N,G_ccDigestInfo"
- "initWithSalt:code:"
- "r^{ccdigest_info=QQQQ*^v^?^?i}16@0:8"
- "r^{ccdigest_info=QQQQ*^v^?^?i}24@0:8^@16"

```
