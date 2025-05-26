## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-550.8.1.0.0
-  __TEXT.__text: 0x7668c
-  __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x7880
-  __TEXT.__const: 0x1cbf
-  __TEXT.__cstring: 0x12cc8
+580.4.2.0.0
+  __TEXT.__text: 0x76cc8
+  __TEXT.__auth_stubs: 0x1150
+  __TEXT.__objc_methlist: 0x78e8
+  __TEXT.__const: 0x1da7
+  __TEXT.__cstring: 0x12dfa
   __TEXT.__gcc_except_tab: 0xfd8
   __TEXT.__oslogstring: 0x588
-  __TEXT.__unwind_info: 0x1954
+  __TEXT.__unwind_info: 0x1960
   __TEXT.__objc_classname: 0x9ad
-  __TEXT.__objc_methname: 0xf5b2
-  __TEXT.__objc_methtype: 0x27cf
-  __TEXT.__objc_stubs: 0x83e0
+  __TEXT.__objc_methname: 0xf892
+  __TEXT.__objc_methtype: 0x27e6
+  __TEXT.__objc_stubs: 0x8440
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x2280
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xed98
-  __DATA_CONST.__objc_selrefs: 0x3418
+  __DATA_CONST.__objc_const: 0xee88
+  __DATA_CONST.__objc_selrefs: 0x3468
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_classrefs: 0x268
+  __DATA_CONST.__objc_classrefs: 0x270
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__objc_const: 0x3a8
-  __AUTH_CONST.__cfstring: 0x4740
+  __AUTH_CONST.__cfstring: 0x4800
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x8b0
+  __AUTH_CONST.__auth_got: 0x8b8
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x107c
+  __DATA.__objc_ivar: 0x1090
   __DATA.__data: 0x1928
-  __DATA.__bss: 0x118
+  __DATA.__bss: 0x128
   __DATA.__common: 0x0
-  __DATA_DIRTY.__const: 0x400
+  __DATA_DIRTY.__const: 0x420
   __DATA_DIRTY.__objc_const: 0x19d8
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x1a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3146
-  Symbols:   9856
-  CStrings:  5848
+  Functions: 3158
+  Symbols:   9893
+  CStrings:  5887
 
Symbols:
+ -[RPEndpoint updateTrustStatusFlagsWithIdentity:]
+ -[RPNFCTransaction localAuthenticationMessage]
+ -[RPNFCTransaction localValidationMessage]
+ -[RPNFCTransaction setLocalAuthenticationMessage:]
+ -[RPNFCTransaction setLocalValidationMessage:]
+ -[RPNearFieldContext initWithApplicationLabel:supportedApplicationLabels:pkData:bonjourListenerUUID:]
+ -[RPNearFieldContext supportedApplicationLabels]
+ -[RPNearFieldTapEvent applicationDomain]
+ -[RPNearFieldTapEvent initWithIdentifier:applicationLabel:pkData:bonjourListenerUUID:isSameAccount:contactID:forceSingleBandAWDLMode:knownIdentity:isUnsupportedApplicationLabel:]
+ -[RPNearFieldTapEvent isUnsupportedApplicationLabel]
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_IVAR_$_RPNFCTransaction._localAuthenticationMessage
+ _OBJC_IVAR_$_RPNFCTransaction._localValidationMessage
+ _OBJC_IVAR_$_RPNearFieldContext._supportedApplicationLabels
+ _OBJC_IVAR_$_RPNearFieldTapEvent._applicationDomain
+ _OBJC_IVAR_$_RPNearFieldTapEvent._isUnsupportedApplicationLabel
+ ___block_literal_global.1287
+ ___shouldPrintSensitiveData_block_invoke
+ _formatSensitiveData
+ _objc_msgSend$appendString:
+ _objc_msgSend$initWithApplicationLabel:supportedApplicationLabels:pkData:bonjourListenerUUID:
+ _objc_msgSend$supportedApplicationLabels
+ _os_variant_has_internal_content
+ _shouldPrintSensitiveData
+ _shouldPrintSensitiveData.onceToken
+ _shouldPrintSensitiveData.sensitive
- -[RPNearFieldTapEvent initWithIdentifier:applicationLabel:pkData:bonjourListenerUUID:isSameAccount:contactID:forceSingleBandAWDLMode:knownIdentity:]
- ___block_literal_global.1284
CStrings:
+ "\x1a"
+ "\"\x13\x14"
+ "%sID "
+ "%sIDS "
+ "%sPI "
+ "'%@'"
+ "'%~@'"
+ ", ADSID "
+ ", AID "
+ ", ATag <%.*@>"
+ ", AccountAltDSID "
+ ", AltDSID "
+ ", CID "
+ ", CNID "
+ ", Cl "
+ ", HKI "
+ ", HKUID "
+ ", ID "
+ ", IDP "
+ ", IDS "
+ ", MRI "
+ ", MRtI "
+ ", Md "
+ ", Nm "
+ ", OSV "
+ ", PI "
+ ", Rm "
+ ", SKA "
+ ", SV "
+ ", UDID "
+ ", Used SKAs "
+ ", isUnsupportedApplicationLabel '%d'"
+ "-[RPConnection _configureForSessionPairing:]"
+ "580.4.2"
+ "@48@0:8@16@24@32@40"
+ "@72@0:8@16@24@32@40B48@52B60B64B68"
+ "Backwards compatibility authType (%s) -> (%s)"
+ "Backwards compatibility change authType (%s) -> (%s)"
+ "Configuring for session pairing\n"
+ "ConnectionDate %@\n"
+ "Error %@\n"
+ "ID %@\n"
+ "RPNFCTransaction\n"
+ "RPNearFieldTap ID %{mask}, appLabel %@, appDomain %@, date %@ sameAccount %d CNID %@"
+ "RemoteAuthenticationMessage %@\n"
+ "RemoteIdentity %@\n"
+ "RemoteValidationMessage %@\n"
+ "Role %@\n"
+ "State %@\n"
+ "T@\"NSArray\",R,C,N,V_supportedApplicationLabels"
+ "T@\"NSString\",R,N,V_applicationDomain"
+ "T@\"RPTransportServiceHandoverMessage\",&,N,V_localAuthenticationMessage"
+ "T@\"RPTransportServiceHandoverMessage\",&,N,V_localValidationMessage"
+ "TB,R,N,V_isUnsupportedApplicationLabel"
+ "TapEvent %@\n"
+ "_applicationDomain"
+ "_isUnsupportedApplicationLabel"
+ "_localAuthenticationMessage"
+ "_localValidationMessage"
+ "_supportedApplicationLabels"
+ "appendString:"
+ "applicationDomain"
+ "initWithApplicationLabel:supportedApplicationLabels:pkData:bonjourListenerUUID:"
+ "initWithIdentifier:applicationLabel:pkData:bonjourListenerUUID:isSameAccount:contactID:forceSingleBandAWDLMode:knownIdentity:isUnsupportedApplicationLabel:"
+ "isUnsupportedApplicationLabel"
+ "localAuthenticationMessage"
+ "localValidationMessage"
+ "missingFlag.RPStatusFlagsAWDLPairingMode"
+ "privateLoggingEnabled"
+ "setLocalAuthenticationMessage:"
+ "setLocalValidationMessage:"
+ "supportedApplicationLabels"
+ "updateTrustStatusFlagsWithIdentity:"
- "\x19"
- "\"\x13\x12"
- "%sID %@"
- "%sIDS %.*@"
- "%sPI %@"
- ", ADSID '%.*@'"
- ", AID '%{mask}'"
- ", ATag <%@>"
- ", AccountAltDSID '%@'"
- ", AccountAltDSID '%{mask}'"
- ", AltDSID %.*@'"
- ", CID '%@`"
- ", HKI '%.*@'"
- ", ID '%@'"
- ", ID '%{mask}'"
- ", IDP '%.*@'"
- ", IDS '%{mask}'"
- ", Nm '%{mask}'"
- ", PI '%@'"
- ", SKA '%.*@'"
- ", UDID '%@'"
- ", Used SKAs %@"
- "550.8.1"
- "@68@0:8@16@24@32@40B48@52B60B64"
- "ConnectionDate %@"
- "Error %@"
- "ID %@"
- "RPNearFieldTap ID %{mask}, appLabel %@, date %@ sameAccount %d CNID %@"
- "RemoteAuthenticationMessage %@"
- "RemoteIdentity %@"
- "RemoteValidationMessage %@"
- "Role %@"
- "State %@"
- "TapEvent %@"
- "initWithIdentifier:applicationLabel:pkData:bonjourListenerUUID:isSameAccount:contactID:forceSingleBandAWDLMode:knownIdentity:"

```
