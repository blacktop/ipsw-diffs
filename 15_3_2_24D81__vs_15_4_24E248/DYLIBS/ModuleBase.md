## ModuleBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/Versions/A/ModuleBase`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x80b8
+1656.100.223.0.0
+  __TEXT.__text: 0x83c0
   __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_methlist: 0x714
-  __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x933
+  __TEXT.__objc_methlist: 0x9f4
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0x935
   __TEXT.__ustring: 0xc
   __TEXT.__gcc_except_tab: 0xa0
   __TEXT.__oslogstring: 0x752
-  __TEXT.__unwind_info: 0x248
-  __TEXT.__objc_classname: 0x154
-  __TEXT.__objc_methname: 0x1f45
-  __TEXT.__objc_methtype: 0xcbe
-  __TEXT.__objc_stubs: 0x1540
-  __DATA_CONST.__got: 0x138
+  __TEXT.__unwind_info: 0x270
+  __TEXT.__objc_classname: 0x152
+  __TEXT.__objc_methname: 0x201a
+  __TEXT.__objc_methtype: 0xcdc
+  __TEXT.__objc_stubs: 0x1620
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x710
+  __DATA_CONST.__objc_selrefs: 0x828
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __AUTH_CONST.__auth_got: 0x1a0
   __AUTH_CONST.__const: 0x370
   __AUTH_CONST.__cfstring: 0xa20
-  __AUTH_CONST.__objc_const: 0x1910
+  __AUTH_CONST.__objc_const: 0x13a8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0xd0

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/Versions/A/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EAB816F7-EC83-3796-A84B-B7C86D370DA5
-  Functions: 194
-  Symbols:   657
-  CStrings:  717
+  UUID: 6B7B1393-55DF-3DB9-B8FA-8D6C1BDC5D6A
+  Functions: 201
+  Symbols:   677
+  CStrings:  725
 
Symbols:
+ +[AgentProxy daemonInstance].cold.1
+ +[AuthenticationManager sharedInstance].cold.1
+ -[AuthenticationManager _cancelationErrorWithDescription:cancelledByHigherPriority:]
+ -[RemoteContext dealloc].cold.1
+ LA_LOG.cold.1
+ LA_LOG_AuthenticationManager.cold.1
+ LA_LOG_MechanismManager.cold.1
+ _LACErrorCancelledByHigherPriorityAuthenticationKey
+ _LACErrorCodeSystemCancel
+ _LACErrorSubcodeInterruptedByAnotherEvaluation
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$_LACCachedExternalizedContext
+ _OBJC_CLASS_$_LACPolicyUtilities
+ _OBJC_CLASS_$_NSDictionary
+ __78-[AuthenticationManager remoteAuthenticationInProgressWithPriority:pid:reply:]_block_invoke.45
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACAgentProxyXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextExternalizing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LACContextExternalizing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACAgentProxyXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextExternalizing
+ __OBJC_$_PROTOCOL_REFS_LACContextExternalizing
+ __OBJC_LABEL_PROTOCOL_$_LACAgentProxyXPC
+ __OBJC_LABEL_PROTOCOL_$_LACContextExternalizing
+ __OBJC_LABEL_PROTOCOL_$_LACRemoteAuthenticationOwnership
+ __OBJC_LABEL_PROTOCOL_$_LACRemoteContextOwnership
+ __OBJC_PROTOCOL_$_LACAgentProxyXPC
+ __OBJC_PROTOCOL_$_LACContextExternalizing
+ __OBJC_PROTOCOL_$_LACRemoteAuthenticationOwnership
+ __OBJC_PROTOCOL_$_LACRemoteContextOwnership
+ ___block_descriptor_32_e40_v24?0"<LACAgentProxyXPC>"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e56_v24?0"<LACRemoteAuthenticationOwnership>"8"NSError"16l
+ __block_literal_global.110
+ _objc_msgSend$_cancelationErrorWithDescription:cancelledByHigherPriority:
+ _objc_msgSend$analyticsData
+ _objc_msgSend$biomeDialogEvent
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$errorWithCode:subcode:debugDescription:
+ _objc_msgSend$errorWithCode:subcode:userInfo:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$setBundleID:
- -[AuthenticationManager _cancelationError]
- _OBJC_CLASS_$_LACachedExternalizedContext
- __78-[AuthenticationManager remoteAuthenticationInProgressWithPriority:pid:reply:]_block_invoke.43
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAAgentProxyXPC
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAAgentProxyXPC
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_REFS_LAContextExternalizationProt
- __OBJC_LABEL_PROTOCOL_$_LAAgentProxyXPC
- __OBJC_LABEL_PROTOCOL_$_LAContextExternalizationProt
- __OBJC_LABEL_PROTOCOL_$_LARemoteAuthenticationOwnership
- __OBJC_LABEL_PROTOCOL_$_LARemoteContextOwnership
- __OBJC_PROTOCOL_$_LAAgentProxyXPC
- __OBJC_PROTOCOL_$_LAContextExternalizationProt
- __OBJC_PROTOCOL_$_LARemoteAuthenticationOwnership
- __OBJC_PROTOCOL_$_LARemoteContextOwnership
- ___block_descriptor_32_e39_v24?0"<LAAgentProxyXPC>"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48bs_e55_v24?0"<LARemoteAuthenticationOwnership>"8"NSError"16l
- __block_literal_global.106
- _objc_msgSend$_cancelationError
CStrings:
+ "@\"<LACRemoteAuthenticationOwnership>\""
+ "@\"<LACRemoteContextOwnership>\""
+ "@\"LACCachedExternalizedContext\""
+ "@28@0:8@16B24"
+ "LACAgentProxyXPC"
+ "LACContextExternalizing"
+ "LACRemoteAuthenticationOwnership"
+ "LACRemoteContextOwnership"
+ "T@\"<LACRemoteContextOwnership>\",R,N,V_ownership"
+ "T@\"LACCachedExternalizedContext\",R,N,V_cachedExternalizedContext"
+ "_cancelationErrorWithDescription:cancelledByHigherPriority:"
+ "analyticsData"
+ "biomeDialogEvent"
+ "dictionaryWithObjects:forKeys:count:"
+ "errorWithCode:subcode:debugDescription:"
+ "errorWithCode:subcode:userInfo:"
+ "numberWithBool:"
+ "setBundleID:"
+ "v24@0:8@?<v@?@\"<LACAgentProxyXPC>\"@\"NSError\">16"
+ "v24@?0@\"<LACAgentProxyXPC>\"8@\"NSError\"16"
+ "v24@?0@\"<LACRemoteAuthenticationOwnership>\"8@\"NSError\"16"
+ "v32@0:8q16@?<v@?@\"<LACRemoteAuthenticationOwnership>\"@\"NSError\">24"
+ "v40@0:8q16@\"<LACOriginatorProt>\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8q16@\"<LACOriginatorProt>\"24@?<v@?@@\"NSError\">32"
+ "v40@0:8q16@\"<LACOriginatorProt>\"24@?<v@?B@\"NSError\">32"
+ "v44@0:8B16q20@\"<LACOriginatorProt>\"28@?<v@?B@\"NSError\">36"
+ "v48@0:8@\"EvaluationRequest\"16@\"<LAUIDelegate>\"24@\"<LACOriginatorProt>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
+ "v48@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
+ "v48@0:8@16q24@\"<LACOriginatorProt>\"32@?<v@?B@\"NSError\">40"
+ "v56@0:8@\"NSData\"16q24@\"NSDictionary\"32@\"<LACOriginatorProt>\"40@?<v@?B@\"NSError\">48"
+ "v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
+ "v64@0:8@\"NSUUID\"16@\"<LACRemoteContextOwnership>\"24@\"NSString\"32@\"NSUUID\"40Q48@?<v@?@\"<LACRemoteContextOwnership>\"@\"NSError\">56"
- "@\"<LARemoteAuthenticationOwnership>\""
- "@\"<LARemoteContextOwnership>\""
- "@\"LACachedExternalizedContext\""
- "LAAgentProxyXPC"
- "LAContextExternalizationProt"
- "LARemoteAuthenticationOwnership"
- "LARemoteContextOwnership"
- "T@\"<LARemoteContextOwnership>\",R,N,V_ownership"
- "T@\"LACachedExternalizedContext\",R,N,V_cachedExternalizedContext"
- "_cancelationError"
- "v24@0:8@?<v@?@\"<LAAgentProxyXPC>\"@\"NSError\">16"
- "v24@?0@\"<LAAgentProxyXPC>\"8@\"NSError\"16"
- "v24@?0@\"<LARemoteAuthenticationOwnership>\"8@\"NSError\"16"
- "v32@0:8q16@?<v@?@\"<LARemoteAuthenticationOwnership>\"@\"NSError\">24"
- "v40@0:8q16@\"<LAOriginatorProt>\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8q16@\"<LAOriginatorProt>\"24@?<v@?@@\"NSError\">32"
- "v40@0:8q16@\"<LAOriginatorProt>\"24@?<v@?B@\"NSError\">32"
- "v44@0:8B16q20@\"<LAOriginatorProt>\"28@?<v@?B@\"NSError\">36"
- "v48@0:8@\"EvaluationRequest\"16@\"<LAUIDelegate>\"24@\"<LAOriginatorProt>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@\"NSData\"16@\"<LAContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
- "v48@0:8@16q24@\"<LAOriginatorProt>\"32@?<v@?B@\"NSError\">40"
- "v56@0:8@\"NSData\"16q24@\"NSDictionary\"32@\"<LAOriginatorProt>\"40@?<v@?B@\"NSError\">48"
- "v64@0:8@\"NSUUID\"16@\"<LAContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
- "v64@0:8@\"NSUUID\"16@\"<LARemoteContextOwnership>\"24@\"NSString\"32@\"NSUUID\"40Q48@?<v@?@\"<LARemoteContextOwnership>\"@\"NSError\">56"

```
