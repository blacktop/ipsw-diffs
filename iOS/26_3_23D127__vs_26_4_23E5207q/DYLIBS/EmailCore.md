## EmailCore

> `/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore`

```diff

-3864.400.21.0.0
-  __TEXT.__text: 0x55044
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0x5048
-  __TEXT.__const: 0xe90
-  __TEXT.__gcc_except_tab: 0x6f28
-  __TEXT.__cstring: 0x7d24
+3864.500.147.2.3
+  __TEXT.__text: 0x57710
+  __TEXT.__auth_stubs: 0x1030
+  __TEXT.__objc_methlist: 0x5088
+  __TEXT.__const: 0xeb0
+  __TEXT.__gcc_except_tab: 0x7054
+  __TEXT.__cstring: 0x8397
   __TEXT.__oslogstring: 0x1010
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x52
   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x2838
-  __TEXT.__objc_classname: 0xd27
-  __TEXT.__objc_methname: 0xb140
-  __TEXT.__objc_methtype: 0x1751
-  __TEXT.__objc_stubs: 0x7800
-  __DATA_CONST.__got: 0x6b0
-  __DATA_CONST.__const: 0x2208
-  __DATA_CONST.__objc_classlist: 0x330
+  __TEXT.__unwind_info: 0x29d0
+  __TEXT.__objc_classname: 0xd77
+  __TEXT.__objc_methname: 0xb20e
+  __TEXT.__objc_methtype: 0x1792
+  __TEXT.__objc_stubs: 0x7860
+  __DATA_CONST.__got: 0x6b8
+  __DATA_CONST.__const: 0x2218
+  __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a10
+  __DATA_CONST.__objc_selrefs: 0x2a20
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x848
+  __AUTH_CONST.__auth_got: 0x828
   __AUTH_CONST.__const: 0x738
-  __AUTH_CONST.__cfstring: 0x52a0
-  __AUTH_CONST.__objc_const: 0x9fa8
+  __AUTH_CONST.__cfstring: 0x5320
+  __AUTH_CONST.__objc_const: 0xa060
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x198
-  __AUTH.__objc_data: 0x3e0
+  __AUTH.__objc_data: 0x430
   __AUTH.__data: 0x88
   __DATA.__objc_ivar: 0x4bc
-  __DATA.__data: 0xda4
-  __DATA.__bss: 0x3d0
+  __DATA.__data: 0xe08
+  __DATA.__bss: 0x3c0
   __DATA.__common: 0x24
   __DATA_DIRTY.__objc_data: 0x1c20
   __DATA_DIRTY.__data: 0xb50
-  __DATA_DIRTY.__bss: 0x228
+  __DATA_DIRTY.__bss: 0x238
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 67C13BF9-A2DB-348C-A326-2B5B24A1CB6A
-  Functions: 1943
-  Symbols:   7683
-  CStrings:  4503
+  UUID: 08A62949-5A5E-3E05-9FC4-524D42E404AF
+  Functions: 1956
+  Symbols:   7729
+  CStrings:  4508
 
Symbols:
+ +[ECBIMIInfo bimiInfoForDNSRecord:error:]
+ +[ECBIMIInfo bimiInfoForHeaders:error:]
+ +[_ECBIMIDNSRecordParser bimiInfoForDNSRecord:error:]
+ +[_ECBIMIHeaderParser bimiInfoForHeaders:error:]
+ -[ECDNSClient getBIMIRecordFromDomain:selector:error:]
+ _ECBIMIInfoErrorDomain
+ _ECMessageHeaderKeyBIMISelector
+ _OBJC_CLASS_$__ECBIMIDNSRecordParser
+ _OBJC_METACLASS_$__ECBIMIDNSRecordParser
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ __OBJC_$_CLASS_METHODS__ECBIMIDNSRecordParser
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ECBIMIRecordSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ECBIMIRecordSource
+ __OBJC_$_PROTOCOL_REFS_ECBIMIRecordSource
+ __OBJC_CLASS_RO_$__ECBIMIDNSRecordParser
+ __OBJC_LABEL_PROTOCOL_$_ECBIMIRecordSource
+ __OBJC_METACLASS_RO_$__ECBIMIDNSRecordParser
+ __OBJC_PROTOCOL_$_ECBIMIRecordSource
+ __PROTOCOLS_ECLocalMessageActionID.3
+ _objc_msgSend$bimiInfoForDNSRecord:error:
+ _objc_msgSend$databaseID
+ _objc_msgSend$initWithDatabaseID:
+ _prop_clear.cold.1
- +[ECBIMIInfo bimiInfoForHeaders:]
- +[_ECBIMIHeaderParser bimiInfoForHeaders:]
- __PROTOCOLS_ECLocalMessageActionID.2
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x6
CStrings:
+ "%@._bimi.%@"
+ "@\"ECBIMIInfo\"40@0:8@\"NSString\"16@\"NSString\"24o^@32"
+ "ECBIMIInfoErrorDomain"
+ "ECBIMIRecordSource"
+ "ECLocalMessageActionID"
+ "Internal Error %d in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/common.c near line %d"
+ "Internal Error %d in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/server.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/common/plugin_common.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/client.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/common.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/anonymous.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/cram.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/digestmd5.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/gssapi.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/login.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/ntlm.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/plain.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/saslplugins/apop.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/saslplugins/atoken.c near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/saslplugins/atoken2.m near line %d"
+ "Out of Memory in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/saslplugins/oauthbearer.c near line %d"
+ "Parameter Error in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/common/plugin_common.c near line %d"
+ "Parameter Error in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/anonymous.c near line %d"
+ "Parameter Error in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/cram.c near line %d"
+ "Parameter Error in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/digestmd5.c near line %d"
+ "Parameter Error in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/gssapi.c near line %d"
+ "Parameter Error in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/login.c near line %d"
+ "Parameter Error in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/plain.c near line %d"
+ "Parameter Error in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/saslplugins/apop.c near line %d"
+ "Parameter error in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/checkpw.c near line %d"
+ "Parameter error in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/client.c near line %d"
+ "Parameter error in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/common.c near line %d"
+ "Parameter error in /Library/Caches/com.apple.xbs/DCA20E81-B4FC-4EFC-A494-9E77D4F17855/TemporaryDirectory.OSsDuA/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/server.c near line %d"
+ "_ECBIMIDNSRecordParser"
+ "bimi-selector"
+ "bimiInfoForDNSRecord:error:"
+ "bimiInfoForHeaders:error:"
+ "default"
+ "getBIMIRecordFromDomain:selector:error:"
- "Internal Error %d in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/common.c near line %d"
- "Internal Error %d in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/server.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/common/plugin_common.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/client.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/common.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/anonymous.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/cram.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/digestmd5.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/gssapi.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/login.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/ntlm.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/plain.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/apop.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/atoken.c near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/atoken2.m near line %d"
- "Out of Memory in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/oauthbearer.c near line %d"
- "Parameter Error in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/common/plugin_common.c near line %d"
- "Parameter Error in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/anonymous.c near line %d"
- "Parameter Error in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/cram.c near line %d"
- "Parameter Error in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/digestmd5.c near line %d"
- "Parameter Error in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/gssapi.c near line %d"
- "Parameter Error in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/login.c near line %d"
- "Parameter Error in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/plugins/plain.c near line %d"
- "Parameter Error in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/saslplugins/apop.c near line %d"
- "Parameter error in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/checkpw.c near line %d"
- "Parameter error in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/client.c near line %d"
- "Parameter error in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/common.c near line %d"
- "Parameter error in /Library/Caches/com.apple.xbs/Sources/Mail_Email/Email/SASL/cyrus_sasl/lib/server.c near line %d"
- "bimiInfoForHeaders:"

```
