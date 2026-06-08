## CoreIDCredBuilder

> `/System/Library/PrivateFrameworks/CoreIDCredBuilder.framework/CoreIDCredBuilder`

```diff

-8.504.0.0.0
-  __TEXT.__text: 0xa310
-  __TEXT.__auth_stubs: 0xa10
+9.31.0.0.0
+  __TEXT.__text: 0x92bc
   __TEXT.__objc_methlist: 0x514
   __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x3a3
+  __TEXT.__cstring: 0x3b3
   __TEXT.__swift5_typeref: 0x1e8
   __TEXT.__constg_swiftt: 0xec
   __TEXT.__swift5_reflstr: 0x18

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x300
+  __TEXT.__swift_as_cont: 0x18
+  __TEXT.__unwind_info: 0x290
   __TEXT.__eh_frame: 0x498
-  __TEXT.__objc_classname: 0x165
-  __TEXT.__objc_methname: 0xcbe
-  __TEXT.__objc_methtype: 0x3a1
-  __TEXT.__objc_stubs: 0x680
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0xc0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x510
+  __DATA_CONST.__got: 0x1b0
   __AUTH_CONST.__const: 0xf0
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x988
+  __AUTH_CONST.__auth_got: 0x570
   __AUTH.__objc_data: 0x298
   __AUTH.__data: 0x138
   __DATA.__objc_ivar: 0x54

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5F3519B8-A3D2-32F9-8771-CE6C03BD16F0
-  Functions: 190
-  Symbols:   420
-  CStrings:  226
+  UUID: 5EA655D2-A767-3923-A613-349FCA1C41CF
+  Functions: 184
+  Symbols:   447
+  CStrings:  28
 
Symbols:
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.21
+ ___swift_closure_destructor.21Tm
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.29
+ ___swift_closure_destructor.33
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_CoreIDCredBuilder
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x7
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain_x20
+ _swift_retain_x21
- _objectdestroy.21Tm
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"_TtC17CoreIDCredBuilder26CIDCInternalPayloadBuilder\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8Q16Q24Q32"
- "@40@0:8q16@24@32"
- "@48@0:8q16@24@32@40"
- "@56@0:8Q16Q24Q32@40^@48"
- "@64@0:8Q16@24@32@40@48@56"
- "@72@0:8Q16@24@32@40@48@56q64"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "@80@0:8Q16@24@32@40@48@56q64q72"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16^@24"
- "B40@0:8@16@24^@32"
- "CIDCBuilderSignatureDetails"
- "CIDCElement"
- "CIDCPayloadBuilder"
- "CIDCPayloadBuilderDelegate"
- "CIDCPayloadBuilderDetails"
- "CIDCSessionCryptarch"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSArray\",&,N,V_arrayValue"
- "T@\"NSArray\",&,N,V_issuerCertificate"
- "T@\"NSData\",&,N,V_dataValue"
- "T@\"NSData\",&,N,V_deviceKey"
- "T@\"NSData\",&,N,V_issuerKey"
- "T@\"NSData\",&,N,V_signature"
- "T@\"NSData\",N,R"
- "T@\"NSDate\",&,N,V_dateValue"
- "T@\"NSDate\",&,N,V_validFrom"
- "T@\"NSDate\",&,N,V_validUntil"
- "T@\"NSDictionary\",&,N,V_dictionaryValue"
- "T@\"NSDictionary\",&,N,V_elements"
- "T@\"NSDictionary\",&,N,V_integerKeyedDictionaryValue"
- "T@\"NSNumber\",&,N,V_numberValue"
- "T@\"NSString\",&,N,V_docType"
- "T@\"NSString\",&,N,V_elementIdentifier"
- "T@\"NSString\",&,N,V_stringValue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"_TtC17CoreIDCredBuilder26CIDCInternalPayloadBuilder\",&,N,V_payloadBuilder"
- "TQ,N,R"
- "TQ,N,V_format"
- "TQ,R"
- "Tq,N,V_signingAlgorithm"
- "Tq,N,V_timePolicy"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC17CoreIDCredBuilder26CIDCInternalPayloadBuilder"
- "_TtCC17CoreIDCredBuilder26CIDCInternalPayloadBuilderP33_83E0D80B61EDDC1630A996E1B5194FE834CIDCInternalPayloadBuilderDelegate"
- "_arrayValue"
- "_dataValue"
- "_dateValue"
- "_deviceKey"
- "_dictionaryValue"
- "_docType"
- "_elementIdentifier"
- "_elements"
- "_format"
- "_integerKeyedDictionaryValue"
- "_issuerCertificate"
- "_issuerKey"
- "_numberValue"
- "_payloadBuilder"
- "_signature"
- "_signingAlgorithm"
- "_stringValue"
- "_timePolicy"
- "_validFrom"
- "_validUntil"
- "arrayValue"
- "autorelease"
- "buildPayloadWithDetails:completion:"
- "buildPayloadWithDetails:completionHandler:"
- "class"
- "conformsToProtocol:"
- "curve"
- "dataValue"
- "dateValue"
- "dealloc"
- "debugDescription"
- "decryptData:error:"
- "delegate"
- "deriveSessionKeysFromSessionTranscript:error:"
- "deriveSessionKeysFromSessionTranscript:intermediateKeyMaterial:error:"
- "description"
- "deviceKey"
- "dictionaryValue"
- "docType"
- "elementIdentifier"
- "elements"
- "encryptData:error:"
- "format"
- "hash"
- "init"
- "initWithDelegate:"
- "initWithDelegate:payloadBuilder:"
- "initWithElementIdentifier:arrayValue:"
- "initWithElementIdentifier:dataValue:"
- "initWithElementIdentifier:dateValue:"
- "initWithElementIdentifier:dictionaryValue:"
- "initWithElementIdentifier:integerKeyedDictionaryValue:"
- "initWithElementIdentifier:numberValue:"
- "initWithElementIdentifier:stringValue:"
- "initWithElementIdentifier:stringValue:dataValue:dateValue:numberValue:arrayValue:dictionaryValue:integerKeyedDictionaryValue:"
- "initWithFormat:docType:elements:validFrom:validUntil:deviceKey:"
- "initWithFormat:docType:elements:validFrom:validUntil:deviceKey:signingAlgorithm:"
- "initWithFormat:docType:elements:validFrom:validUntil:deviceKey:signingAlgorithm:timePolicy:"
- "initWithRole:curve:variant:"
- "initWithRole:curve:variant:localKey:error:"
- "initWithSigningAlgorithm:issuerCertificate:issuerKey:signature:"
- "initWithSigningAlgorithm:issuerCertificate:signature:"
- "initWithSigningAlgorithm:issuerKey:signature:"
- "integerKeyedDictionaryValue"
- "integerValue"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "issuerCertificate"
- "issuerKey"
- "numberValue"
- "payloadBuilder"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "privateKey"
- "publicKey"
- "q"
- "q16@0:8"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "role"
- "self"
- "sessionCryptarch"
- "setArrayValue:"
- "setDataValue:"
- "setDateValue:"
- "setDeviceKey:"
- "setDictionaryValue:"
- "setDocType:"
- "setElementIdentifier:"
- "setElements:"
- "setFormat:"
- "setIntegerKeyedDictionaryValue:"
- "setIssuerCertificate:"
- "setIssuerKey:"
- "setNumberValue:"
- "setPayloadBuilder:"
- "setRemoteKey:error:"
- "setSignature:"
- "setSigningAlgorithm:"
- "setStringValue:"
- "setTimePolicy:"
- "setValidFrom:"
- "setValidUntil:"
- "signPayloadWithBuilder:data:completion:"
- "signature"
- "signingAlgorithm"
- "stringValue"
- "superclass"
- "timePolicy"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v24@?0@\"CIDCBuilderSignatureDetails\"8@\"NSError\"16"
- "v32@0:8@\"CIDCPayloadBuilderDetails\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@\"CIDCPayloadBuilder\"16@\"NSData\"24@?<v@?@\"CIDCBuilderSignatureDetails\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "validFrom"
- "validUntil"
- "variant"
- "zone"

```
