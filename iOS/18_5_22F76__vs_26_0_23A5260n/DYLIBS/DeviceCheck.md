## DeviceCheck

> `/System/Library/Frameworks/DeviceCheck.framework/DeviceCheck`

```diff

-109.6.0.0.0
-  __TEXT.__text: 0x8ea4
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0x664
+119.0.0.0.0
+  __TEXT.__text: 0xa028
+  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__objc_methlist: 0x67c
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x79c
-  __TEXT.__gcc_except_tab: 0x440
-  __TEXT.__oslogstring: 0x9cd
-  __TEXT.__unwind_info: 0x280
+  __TEXT.__cstring: 0x7f0
+  __TEXT.__gcc_except_tab: 0x43c
+  __TEXT.__oslogstring: 0xc8e
+  __TEXT.__unwind_info: 0x2a0
   __TEXT.__objc_classname: 0xf8
-  __TEXT.__objc_methname: 0xfd1
-  __TEXT.__objc_methtype: 0x55f
-  __TEXT.__objc_stubs: 0xbe0
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x4b8
+  __TEXT.__objc_methname: 0x105b
+  __TEXT.__objc_methtype: 0x5b9
+  __TEXT.__objc_stubs: 0xc40
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__const: 0x558
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x458
+  __DATA_CONST.__objc_selrefs: 0x470
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x270
-  __AUTH_CONST.__const: 0x160
+  __AUTH_CONST.__auth_got: 0x278
+  __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x640
-  __AUTH_CONST.__objc_const: 0xa58
+  __AUTH_CONST.__objc_const: 0xa60
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 392CD873-ABC7-3644-ABBA-DB39B29C97AF
-  Functions: 161
-  Symbols:   770
-  CStrings:  400
+  UUID: E4651F14-8339-33C1-A160-6284369F9AE3
+  Functions: 174
+  Symbols:   832
+  CStrings:  416
 
Symbols:
+ -[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]
+ -[DCAppAttestServicePriv getPropertiesForKeyId:teamIdentifier:completionHandler:]
+ GCC_except_table13
+ GCC_except_table21
+ GCC_except_table25
+ GCC_except_table30
+ GCC_except_table36
+ GCC_except_table43
+ _OBJC_CLASS_$_SecKeyProxy
+ ___46-[DCAppAttestController isSupportedWithError:]_block_invoke.86
+ ___66-[DCAppAttestController generateKeyWithTeamIdentifier:completion:]_block_invoke.21
+ ___66-[DCAppAttestController generateKeyWithTeamIdentifier:completion:]_block_invoke.cold.1
+ ___71-[DCAppAttestController sign:withKey:teamIdentifier:completionHandler:]_block_invoke.80
+ ___71-[DCAppAttestController sign:withKey:teamIdentifier:completionHandler:]_block_invoke.81
+ ___71-[DCAppAttestController sign:withKey:teamIdentifier:completionHandler:]_block_invoke.cold.1
+ ___71-[DCAppAttestController sign:withKey:teamIdentifier:completionHandler:]_block_invoke.cold.2
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.82
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.83
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.83.cold.1
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.83.cold.2
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.83.cold.3
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.83.cold.4
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.cold.1
+ ___80-[DCAppAttestController getPropertiesForKeyId:teamIdentifier:completionHandler:]_block_invoke.cold.2
+ ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.41
+ ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.42
+ ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.cold.1
+ ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.cold.2
+ ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.cold.3
+ ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.cold.4
+ ___91-[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.73
+ ___91-[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.cold.1
+ ___91-[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.cold.2
+ ___91-[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.cold.3
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.50
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.56
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.56.cold.1
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.57
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.66.cold.1
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.66.cold.2
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.68
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.68.cold.1
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.69
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.cold.1
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.cold.2
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.cold.3
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.67
+ ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.67.cold.1
+ ___block_descriptor_48_e8_32s40bs_e43_v24?0"NSXPCListenerEndpoint"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.156
+ ___clientProcessingQueue_block_invoke
+ ___clientProcessingQueue_block_invoke.cold.1
+ _clientProcessingQueue
+ _clientProcessingQueue.cold.1
+ _clientProcessingQueue.queue
+ _clientProcessingQueue.queueCreationGuard
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create
+ _objc_msgSend$createKeyFromEndpoint:error:
+ _objc_msgSend$getKeyProxyEndpoint:keyId:teamIdentifier:completion:
+ _objc_msgSend$getPropertiesForKeyId:teamIdentifier:completionHandler:
- -[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:].cold.1
- -[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:].cold.2
- -[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:].cold.1
- -[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:].cold.2
- -[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:].cold.3
- -[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:].cold.1
- -[DCAppAttestController generateAssertion:teamIdentifier:clientDataHash:completionHandler:].cold.2
- -[DCAppAttestController sign:withKey:teamIdentifier:completionHandler:].cold.1
- GCC_except_table11
- GCC_except_table18
- GCC_except_table22
- GCC_except_table26
- GCC_except_table31
- GCC_except_table34
- GCC_except_table4
- ___46-[DCAppAttestController isSupportedWithError:]_block_invoke.77
- ___71-[DCAppAttestController sign:withKey:teamIdentifier:completionHandler:]_block_invoke.76
- ___83-[DCAppAttestController attestKey:teamIdentifier:clientDataHash:completionHandler:]_block_invoke.40
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.53
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.53.cold.1
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.54
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.63
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.63.cold.1
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.63.cold.2
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.65
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke.65.cold.1
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.64
- ___99-[DCAppAttestController attestKey:keyAttributes:clientDataHash:authData:options:completionHandler:]_block_invoke_2.64.cold.1
- _objc_retain_x28
CStrings:
+ "%25s:%-5d Created client processing queue. { queueName=%s }"
+ "%25s:%-5d Dispatching attest key onto client processing queue. { label=%s }"
+ "%25s:%-5d Dispatching generate assertion onto client processing queue. { label=%s }"
+ "%25s:%-5d Dispatching generate key onto client processing queue. { label=%s }"
+ "%25s:%-5d Dispatching get properties for key onto client processing queue. { label=%s }"
+ "%25s:%-5d Dispatching sign onto client processing queue. { label=%s }"
+ "%25s:%-5d Failed to create key from key proxy endpoint. { endpoint=%@ }"
+ "%25s:%-5d Failed to get key proxy endpoint. { error=%@ }"
+ "%25s:%-5d Fetched key properties. { endpoint=%@, properties=%@ }"
+ "%25s:%-5d Received key proxy endpoint. { endpoint=%@ }"
+ "com.apple.devicecheck.client.processing"
+ "createKeyFromEndpoint:error:"
+ "getKeyProxyEndpoint:keyId:teamIdentifier:completion:"
+ "getPropertiesForKeyId:teamIdentifier:completionHandler:"
+ "v24@?0@\"NSXPCListenerEndpoint\"8@\"NSError\"16"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">40"

```
