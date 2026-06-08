## libcryptex_core.dylib

> `/usr/lib/libcryptex_core.dylib`

```diff

-662.120.27.0.0
-  __TEXT.__text: 0x16cdc
-  __TEXT.__auth_stubs: 0xde0
+746.0.0.0.0
+  __TEXT.__text: 0x160d4
   __TEXT.__objc_methlist: 0x444
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x1b92
-  __TEXT.__oslogstring: 0x2c29
-  __TEXT.__gcc_except_tab: 0x2cc
-  __TEXT.__unwind_info: 0x518
-  __TEXT.__objc_classname: 0xcd
-  __TEXT.__objc_methname: 0xab9
-  __TEXT.__objc_methtype: 0x19e
-  __TEXT.__objc_stubs: 0xa20
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0xfa0
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x1b9a
+  __TEXT.__oslogstring: 0x2c25
+  __TEXT.__gcc_except_tab: 0x1ec
+  __TEXT.__unwind_info: 0x498
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xfb8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_nlclslist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x328
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x700
+  __DATA_CONST.__got: 0x270
   __AUTH_CONST.__const: 0x258
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0xab0
+  __AUTH_CONST.__auth_got: 0x720
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x5c
-  __DATA.__data: 0x298
+  __DATA.__data: 0x2a0
   __DATA.__bss: 0x288
   __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E1EB5791-B206-3D22-9D4E-03465D89235C
-  Functions: 429
-  Symbols:   1357
-  CStrings:  776
+  UUID: AA82889E-7E87-351A-8353-BA631F9D83B8
+  Functions: 425
+  Symbols:   1350
+  CStrings:  591
 
Symbols:
+ __cryptex_content_type_dyld_closures
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
- GCC_except_table54
- GCC_except_table55
- GCC_except_table56
- GCC_except_table57
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%{public}s: (%p) Updating %s homedir: %s -> %s"
+ "(null)"
+ "746"
+ "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Thu May 21 08:14:44 PDT 2026; root:libcryptex-746~413/libcryptex_core/RELEASE_ARM64E"
+ "Darwin Cryptex Core Interface Version 2.0.0: Thu May 21 08:14:44 PDT 2026; root:libcryptex-746~413/libcryptex_core/RELEASE_ARM64E"
+ "Dyld Closures"
- "%{public}s: (%p) Updating %s homedir: (null) -> %s"
- ".cxx_destruct"
- "662.120.27"
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_cryptex_signature>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSString\""
- "@(#)VERSION:Darwin Cryptex Core Interface Version 2.0.0: Sat Apr 18 17:49:10 PDT 2026; root:libcryptex-662.120.27~92/libcryptex_core/RELEASE_ARM64E"
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8q16"
- "@28@0:8I16@20"
- "@32@0:8@16@24"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24q32"
- "@72@0:8@16@24@32q40@48@56@64"
- "B16@0:8"
- "B24@0:8@16"
- "CollationElement"
- "CryptexTSS"
- "Darwin Cryptex Core Interface Version 2.0.0: Sat Apr 18 17:49:10 PDT 2026; root:libcryptex-662.120.27~92/libcryptex_core/RELEASE_ARM64E"
- "I"
- "I16@0:8"
- "OS_cryptex_base"
- "OS_cryptex_core"
- "OS_cryptex_core_cx1_properties"
- "OS_cryptex_host"
- "OS_cryptex_magister"
- "OS_cryptex_scrivener"
- "OS_cryptex_signature"
- "OS_session_core"
- "Q"
- "Q16@0:8"
- "T@\"NSArray\",R,&,V_cle_command_args"
- "T@\"NSData\",&,N,V_info_content"
- "T@\"NSDictionary\",&,N,V_response"
- "T@\"NSDictionary\",R,&,V_cle_env"
- "T@\"NSError\",&,N,V_nserr"
- "T@\"NSMutableSet\",&,N,V_coll_elems"
- "T@\"NSObject<OS_cryptex_signature>\",&,N,V_tssp_sign"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dq"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_dq"
- "T@\"NSObject<OS_os_log>\",&,N,V_log"
- "T@\"NSObject<OS_os_log>\",R,N,V_log"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_im4m_array"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_listener"
- "T@\"NSObject<OS_xpc_object>\",R,N,V_tss_request"
- "T@\"NSString\",&,N,V_tssURL"
- "T@\"NSString\",R,&,N,V_cle_bundle_id"
- "T@\"NSString\",R,&,N,V_cle_bundle_version"
- "T@\"NSString\",R,&,V_cle_mnt_path"
- "T@\"NSString\",R,C,V_cle_command"
- "T@\"NSString\",R,N,V_tssUsage"
- "TI,N,V_coll_uid"
- "TQ,R,N,V_flags"
- "Tq,R,N,V_cle_scope"
- "URLQueryAllowedCharacterSet"
- "UTF8String"
- "_cle_bundle_id"
- "_cle_bundle_version"
- "_cle_command"
- "_cle_command_args"
- "_cle_env"
- "_cle_mnt_path"
- "_cle_scope"
- "_coll_elems"
- "_coll_uid"
- "_dq"
- "_flags"
- "_im4m_array"
- "_info_content"
- "_listener"
- "_log"
- "_nserr"
- "_response"
- "_tssURL"
- "_tssUsage"
- "_tss_request"
- "_tssp_sign"
- "activate"
- "addObject:"
- "appendCollationElement:"
- "appendFormat:"
- "array"
- "base64EncodedStringWithOptions:"
- "bytes"
- "cle_bundle_id"
- "cle_bundle_version"
- "cle_command"
- "cle_command_args"
- "cle_env"
- "cle_mnt_path"
- "cle_scope"
- "coll_elems"
- "coll_uid"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "copy"
- "copyAbsolutePath:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createEndpoint"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithJSONObject:options:error:"
- "dataWithPropertyList:format:options:error:"
- "dealloc"
- "defaultManager"
- "description"
- "dq"
- "enumerateCollationElements:"
- "enumerateElements:"
- "enumerateObjectsUsingBlock:"
- "fileExistsAtPath:"
- "flags"
- "generateDiavloRequest:"
- "generatePackedSignatures"
- "getID"
- "getValidPaths:forBundleID:"
- "im4m_array"
- "info_content"
- "init"
- "initWithBase64EncodedString:options:"
- "initWithBundle:version:atPath:withScope:withCommand:withCommandArgs:withEnv:"
- "initWithData:encoding:"
- "initWithFlags:"
- "initWithID:queue:"
- "initWithXPC:"
- "initWithXPC:queue:"
- "isEmpty"
- "isEqualToString:"
- "isSSOAvailable"
- "length"
- "listener"
- "localizedDescription"
- "log"
- "mountPointOfBundleID:"
- "nserr"
- "objectForKeyedSubscript:"
- "packToXPC"
- "parseMessage:"
- "propertyListWithData:options:format:error:"
- "q"
- "q16@0:8"
- "removeCollationElementWithPath:"
- "removeObject:"
- "response"
- "scopeToString:"
- "set"
- "setColl_elems:"
- "setColl_uid:"
- "setDq:"
- "setIm4m_array:"
- "setInfoData:"
- "setInfo_content:"
- "setListener:"
- "setLog:"
- "setManifestArray:"
- "setNserr:"
- "setObject:forKeyedSubscript:"
- "setResponse:"
- "setTssURL:"
- "setTssp_sign:"
- "setURL:"
- "setupHandler"
- "stringByAddingPercentEncodingWithAllowedCharacters:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "tssFormatRequest:withHeaders:withURL:"
- "tssFormatResponse:withHeaderData:withCode:"
- "tssSendRequest"
- "tssSerializeRequest"
- "tssStampRequest"
- "tssSubmit"
- "tssURL"
- "tssUsage"
- "tss_request"
- "tssp_sign"
- "v16@0:8"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8@?16"

```
