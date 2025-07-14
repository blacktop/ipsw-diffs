## com.apple.PrintKit.PrinterTool

> `/System/Library/PrivateFrameworks/PrintKit.framework/XPCServices/com.apple.PrintKit.PrinterTool.xpc/com.apple.PrintKit.PrinterTool`

```diff

-288.7.0.0.0
-  __TEXT.__text: 0x524f8
-  __TEXT.__auth_stubs: 0x1660
-  __TEXT.__objc_stubs: 0x4320
-  __TEXT.__objc_methlist: 0x18f8
-  __TEXT.__const: 0xc00
-  __TEXT.__gcc_except_tab: 0x88d0
-  __TEXT.__oslogstring: 0x40fb
-  __TEXT.__cstring: 0x7565
-  __TEXT.__objc_methname: 0x4590
-  __TEXT.__objc_classname: 0x391
-  __TEXT.__objc_methtype: 0x13d9
+288.9.0.0.0
+  __TEXT.__text: 0x52680
+  __TEXT.__auth_stubs: 0x1680
+  __TEXT.__objc_stubs: 0x43a0
+  __TEXT.__objc_methlist: 0x1930
+  __TEXT.__const: 0x8d0
+  __TEXT.__gcc_except_tab: 0x89b0
+  __TEXT.__oslogstring: 0x4156
+  __TEXT.__cstring: 0x7573
+  __TEXT.__objc_methname: 0x467a
+  __TEXT.__objc_classname: 0x38f
+  __TEXT.__objc_methtype: 0x1409
   __TEXT.__ustring: 0x66
-  __TEXT.__unwind_info: 0x27d8
+  __TEXT.__unwind_info: 0x2794
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xb48
-  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__auth_got: 0xb58
+  __DATA_CONST.__got: 0x380
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xd560
-  __DATA_CONST.__cfstring: 0xc520
+  __DATA_CONST.__const: 0xd140
+  __DATA_CONST.__cfstring: 0xc540
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_intobj: 0xca8
-  __DATA.__objc_const: 0x4040
-  __DATA.__objc_selrefs: 0x12f0
-  __DATA.__objc_ivar: 0x2bc
+  __DATA.__objc_const: 0x4110
+  __DATA.__objc_selrefs: 0x1308
+  __DATA.__objc_ivar: 0x2d0
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x2db0
   __DATA.__bss: 0x150

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9B1F5326-6F98-3E89-B4DD-2F0FB3DE479C
-  Functions: 1326
-  Symbols:   1016
-  CStrings:  4940
+  UUID: 3E0452D7-7C3C-3A4E-91B5-C68D10F8DEDB
+  Functions: 1295
+  Symbols:   1013
+  CStrings:  4956
 
Symbols:
+ __ZN17Printd_Parameters23_del_RequestingUserNameEv
+ __ZTVN10__cxxabiv121__vmi_class_type_infoE
+ _nw_parameters_set_account_id
+ _nw_parameters_set_attributed_bundle_identifier
- __ZN17Printd_ParametersC2EP5ipp_t
- __ZN17Printd_ParametersD0Ev
- __ZN17Printd_ParametersD1Ev
- __ZN17Printd_ParametersD2Ev
- __ZTI17Printd_Parameters
- __ZTS17Printd_Parameters
- __ZTV17Printd_Parameters
CStrings:
+ "\x01\x12\x13#"
+ "\x02#\x13\x16"
+ "\a\x14"
+ "%s credential"
+ "@\"ipp_request_t\""
+ "Basic"
+ "CLEARING"
+ "Not storing credential"
+ "STORING"
+ "T@\"IPPSession\",&,V_session"
+ "T@\"NSString\",R,V_clientBundleIdentifier"
+ "^{JobRequestAttributes=@}"
+ "_canResendInitialRequest"
+ "_clientBundleIdentifier"
+ "_credentialFromPrompt"
+ "_initialRequest"
+ "_rememberCredentialSent:"
+ "_send0_initialPayload:"
+ "_updateInitialMessageIfDefaultCredential:"
+ "_userCanceledAuth"
+ "auth cred completion - canceled? %d"
+ "auth trust completion - canceled? %d"
+ "clientBundleIdentifier"
+ "hasPassword"
+ "initWithProxy:session:"
+ "setSession:"
+ "set_sourceApplicationSecondaryIdentifier:"
+ "storeCredentialBasedOnTransactionResult:"
+ "transport error: %{public}@ => %{public}@"
+ "updateInitialPayloadUserName:"
+ "v16@?0^{GET_JOBS_Response=@}8"
+ "v16@?0^{GET_PRINTER_ATTRIBUTES_Response=@}8"
+ "v16@?0^{_Response=@}8"
+ "v24@0:8^{Real_IPP_Message=^^?@}16"
- "\x01\x14"
- "\x01\x15#"
- "\x02\x13\x13\x16"
- "\x06\x14"
- "!"
- "%@: _isWaitingForConnectionWithError: %@"
- "URLSession:task:_isWaitingForConnectionWithError:"
- "^{JobRequestAttributes=^^?@}"
- "_credential"
- "_initialPayload"
- "_send0_initialPayload"
- "_updatedCredential:"
- "initWithProxy:"
- "setWaitsForConnectivity:"
- "storeCredential:"
- "transport error: %@"
- "uploadTaskWithRequest:fromData:"
- "v16@?0^{GET_JOBS_Response=^^?@}8"
- "v16@?0^{GET_PRINTER_ATTRIBUTES_Response=^^?@}8"
- "v16@?0^{_Response=^^?@}8"

```
