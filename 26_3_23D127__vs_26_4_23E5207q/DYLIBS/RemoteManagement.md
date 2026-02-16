## RemoteManagement

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement`

```diff

-585.80.2.0.0
-  __TEXT.__text: 0x49278
-  __TEXT.__auth_stubs: 0x1500
+585.100.8.0.0
+  __TEXT.__text: 0x507ec
+  __TEXT.__auth_stubs: 0x1480
   __TEXT.__objc_methlist: 0x1b88
-  __TEXT.__const: 0x16fc
-  __TEXT.__cstring: 0x2967
-  __TEXT.__oslogstring: 0x491b
-  __TEXT.__gcc_except_tab: 0x4b8
-  __TEXT.__swift5_typeref: 0x629
-  __TEXT.__swift5_capture: 0x7c
+  __TEXT.__const: 0x182c
+  __TEXT.__cstring: 0x2317
+  __TEXT.__oslogstring: 0x49ab
+  __TEXT.__gcc_except_tab: 0x4f4
+  __TEXT.__swift5_typeref: 0x63f
   __TEXT.__constg_swiftt: 0x9a0
   __TEXT.__swift5_reflstr: 0x303
   __TEXT.__swift5_fieldmd: 0x488
-  __TEXT.__swift5_proto: 0xfc
+  __TEXT.__swift5_proto: 0x114
   __TEXT.__swift5_types: 0x78
+  __TEXT.__swift5_capture: 0x5c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xf70
-  __TEXT.__eh_frame: 0x1808
-  __TEXT.__objc_classname: 0x370
-  __TEXT.__objc_methname: 0x5a03
-  __TEXT.__objc_methtype: 0x890
-  __TEXT.__objc_stubs: 0x2ec0
+  __TEXT.__unwind_info: 0xf60
+  __TEXT.__eh_frame: 0x1650
+  __TEXT.__objc_classname: 0x5cd
+  __TEXT.__objc_methname: 0x5d10
+  __TEXT.__objc_methtype: 0xabb
+  __TEXT.__objc_stubs: 0x3160
   __DATA_CONST.__got: 0x588
-  __DATA_CONST.__const: 0x638
+  __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x1388
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0xa90
-  __AUTH_CONST.__const: 0xb50
-  __AUTH_CONST.__cfstring: 0x1ae0
+  __AUTH_CONST.__auth_got: 0xa50
+  __AUTH_CONST.__const: 0xb28
+  __AUTH_CONST.__cfstring: 0x1ac0
   __AUTH_CONST.__objc_const: 0x2e48
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x778
   __AUTH.__data: 0xab0
   __DATA.__objc_ivar: 0xc8
-  __DATA.__data: 0x6b0
-  __DATA.__bss: 0x20b0
+  __DATA.__data: 0x6d0
+  __DATA.__bss: 0x23b0
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E88621EB-22E4-3FA6-911F-B7E03A9316EA
-  Functions: 1370
-  Symbols:   2970
-  CStrings:  1856
+  UUID: 51C74FCF-CB80-352F-9667-171FB8DE8723
+  Functions: 1374
+  Symbols:   3028
+  CStrings:  1859
 
Symbols:
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _associated conformance So10CFErrorRefa14CoreFoundation9_CFObjectSCSH
+ _associated conformance So10CFErrorRefaSHSCSQ
+ _associated conformance So9SecKeyRefa14CoreFoundation9_CFObjectSCSH
+ _associated conformance So9SecKeyRefaSHSCSQ
+ _objc_msgSend$_atsContext
+ _objc_msgSend$allHeaderFields
+ _objc_msgSend$chipID
+ _objc_msgSend$copyCurrentPersonaContextWithError:
+ _objc_msgSend$createPersonaContextForBackgroundProcessingWithPersonaUniqueString:
+ _objc_msgSend$currentDevice
+ _objc_msgSend$currentPersona
+ _objc_msgSend$dataTaskWithRequest:completionHandler:
+ _objc_msgSend$ephemeralSessionConfiguration
+ _objc_msgSend$error
+ _objc_msgSend$hasSEP
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$oidsAnonymous:nonce:coresidency:
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$response
+ _objc_msgSend$restorePersonaWithSavedPersonaContext:
+ _objc_msgSend$sessionWithConfiguration:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$set_atsContext:
+ _objc_msgSend$userPersonaUniqueString
+ _objc_msgSend$valueForKey:
- +[RMMDMHelper _enrollDDMChannelIfNeededWithController:profileIdentifier:enrollmentType:scope:username:personaID:error:].cold.6
- +[RMMDMHelper _enrollDDMChannelIfNeededWithController:profileIdentifier:enrollmentType:scope:username:personaID:error:].cold.7
- +[RMMDMHelper _unenrollDDMChannelWithController:enrollmentURL:enrollmentType:error:].cold.3
- +[RMMDMHelper unenrollWithProfileIdentifier:enrollmentType:scope:error:].cold.1
- +[RMMDMHelper unenrollWithProfileIdentifier:enrollmentType:scope:error:].cold.2
- GCC_except_table19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _swift_retain_n
- _symbolic ______pSg s5ErrorP
CStrings:
+ "Cannot use DDM channel because it is a different enrollment type."
+ "Executing DeclarativeManagement command for %{public}@, type: %{public}@."
+ "Ignore unenroll request for %{public}@: DDM is not active."
+ "Management channel found is not the right enrollment type: expected %{public}@, got %{public}@. Error: %{public}@"
+ "Processing DeclarativeManagement command for %{public}@, type: %{public}@."
+ "Unenrolling DDM channel."
- "Cannot enroll DDM channel because a different enrollment type already exists."
- "Ignore unenroll request for %{public}@: rMDM is not active."
- "Management channel found does not match expected channel."
- "Management channel found is not the right enrollment type. Error: %{public}@"
- "Processing RemoteManagement command for %{public}@, type: %{public}@."

```
