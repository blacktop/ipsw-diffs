## DeviceIdentity

> `/System/Library/PrivateFrameworks/DeviceIdentity.framework/Versions/A/DeviceIdentity`

```diff

-1015.81.2.0.0
-  __TEXT.__text: 0x1f218
+1017.100.16.0.0
+  __TEXT.__text: 0x1f458
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0x1f4
+  __TEXT.__objc_methlist: 0x3d4
   __TEXT.__const: 0x88ca
-  __TEXT.__cstring: 0x3e24
+  __TEXT.__cstring: 0x3ecc
   __TEXT.__gcc_except_tab: 0x8b0
   __TEXT.__dlopen_cstrs: 0x11f
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x5df
-  __TEXT.__unwind_info: 0x3b8
+  __TEXT.__unwind_info: 0x3f8
   __TEXT.__objc_classname: 0x77
-  __TEXT.__objc_methname: 0x131d
+  __TEXT.__objc_methname: 0x1389
   __TEXT.__objc_methtype: 0x26e
-  __TEXT.__objc_stubs: 0xf40
+  __TEXT.__objc_stubs: 0xfc0
   __DATA_CONST.__got: 0x250
   __DATA_CONST.__const: 0x1378
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x498
+  __DATA_CONST.__objc_selrefs: 0x5b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x450
+  __DATA_CONST.__objc_arraydata: 0x460
   __AUTH_CONST.__auth_got: 0x410
   __AUTH_CONST.__const: 0x330
-  __AUTH_CONST.__cfstring: 0x3f20
-  __AUTH_CONST.__objc_const: 0xa18
+  __AUTH_CONST.__cfstring: 0x4000
+  __AUTH_CONST.__objc_const: 0x688
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DFC413EF-7CE8-34B6-B115-947BA33FEA89
-  Functions: 281
-  Symbols:   1010
-  CStrings:  1390
+  UUID: 38D33442-2F50-366B-86D2-CB5893392136
+  Functions: 322
+  Symbols:   1056
+  CStrings:  1409
 
Symbols:
+ +[DeviceTypeDeviceIdentity sharedInstance].cold.1
+ +[GestaltHlprDeviceIdentity getSharedInstance].cold.1
+ _OBJC_CLASS_$_NSRegularExpression
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.154
+ __DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.155
+ __DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.155.cold.1
+ __DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.260
+ __DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.307
+ __block_literal_global.323
+ _clientNameSuffixIsValid
+ _createBAAClientName
+ _createUserAgentValue
+ _kMAOptionsBAAClientNameSuffix
+ _merge_dict_cb.cold.1
+ _objc_msgSend$copy
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$stringByAppendingFormat:
+ copyCertificateOIDsThatDiffer.cold.1
+ copyDeviceIdentitySerialQueue.cold.1
+ copy_ucrt_path.cold.1
+ der_key_validate.cold.1
+ der_key_validate.cold.2
+ get_aks_client_connection.cold.1
+ isRunningInDiagnosticsMode.cold.1
+ isRunningInRecovery.cold.1
+ isRunningInRootLaunchdContext.cold.1
+ isSupportedDeviceIdentityClient.cold.2
+ lockcrypto_query_certificate_properties.cold.1
- _ACTIVATION_TOOL_USER_AGENT
- __DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.152
- __DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.153
- __DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.153.cold.1
- __DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.257
- __DeviceIdentityIssueClientCertificateWithCompletion_block_invoke.301
- __block_literal_global.320
CStrings:
+ "#%@"
+ "BAAClientNameSuffix"
+ "Failed to create regex."
+ "Invalid type for option '%@'."
+ "Invalid value for option '%@': %@"
+ "^[A-Za-z0-9_-]{0,64}$"
+ "clientNameSuffixIsValid"
+ "copy"
+ "firstMatchInString:options:range:"
+ "imagent"
+ "macOS Device Activator (MobileActivation-1017.100.16)"
+ "regularExpressionWithPattern:options:error:"
+ "stringByAppendingFormat:"
- "macOS Device Activator (MobileActivation-1015.81.2)"

```
