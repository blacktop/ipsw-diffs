## AppleServiceToolkit

> `/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/Versions/A/AppleServiceToolkit`

```diff

-183.0.0.0.0
-  __TEXT.__text: 0x3012c
+190.0.0.0.0
+  __TEXT.__text: 0x30554
   __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0x2f3c
+  __TEXT.__objc_methlist: 0x3704
   __TEXT.__const: 0x170
-  __TEXT.__gcc_except_tab: 0x12b0
+  __TEXT.__gcc_except_tab: 0x12ac
   __TEXT.__oslogstring: 0x1f7f
-  __TEXT.__cstring: 0x2718
-  __TEXT.__unwind_info: 0xc10
+  __TEXT.__cstring: 0x2780
+  __TEXT.__unwind_info: 0xc50
   __TEXT.__objc_classname: 0x71e
-  __TEXT.__objc_methname: 0x7415
-  __TEXT.__objc_methtype: 0x1a77
-  __TEXT.__objc_stubs: 0x5700
+  __TEXT.__objc_methname: 0x7540
+  __TEXT.__objc_methtype: 0x1a7a
+  __TEXT.__objc_stubs: 0x57e0
   __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0x350
+  __DATA_CONST.__const: 0x390
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a90
+  __DATA_CONST.__objc_selrefs: 0x1bb0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x2b0
-  __AUTH_CONST.__const: 0xad0
-  __AUTH_CONST.__cfstring: 0x2740
-  __AUTH_CONST.__objc_const: 0x6e38
+  __AUTH_CONST.__const: 0xaf0
+  __AUTH_CONST.__cfstring: 0x2840
+  __AUTH_CONST.__objc_const: 0x6128
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x1360
-  __DATA.__objc_ivar: 0x384
+  __DATA.__objc_ivar: 0x390
   __DATA.__data: 0x7f8
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x170
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0A0DD05C-6344-30E3-9DD0-551DEEDAFED1
-  Functions: 1213
-  Symbols:   3141
-  CStrings:  2509
+  UUID: 5B09AD7D-9965-3CF1-ABEB-C1EE2800843C
+  Functions: 1234
+  Symbols:   3178
+  CStrings:  2539
 
Symbols:
+ +[ASTConnectionUtilities allowCellularSizeThreshold].cold.1
+ +[ASTConnectionUtilities getServerLoggingSelection].cold.1
+ +[ASTConnectionUtilities isGzipEnabled].cold.1
+ +[ASTConnectionUtilities useChunkedTransferEncoding].cold.1
+ +[ASTEnvironment currentEnvironment].cold.1
+ +[ASTEnvironment isInternalBuild].cold.1
+ +[ASTEnvironment isServicePart]
+ +[ASTEnvironment protocolVersion]
+ +[ASTEnvironment protocolVersion].cold.1
+ +[ASTLinking isAXRuntimeFrameworkAvailable].cold.1
+ +[ASTLinking isCheckerBoardServicesFrameworkAvailable].cold.1
+ +[ASTLinking isCoreAnalyticsFrameworkAvailable].cold.1
+ +[ASTRequest isEstimatedTimeRemainingFeatureEnabled].cold.1
+ +[ASTTestAutomation sharedInstance].cold.1
+ -[ASTAction acceptableDecoderClasses].cold.1
+ -[ASTEnvironment _defaultServerSelection].cold.1
+ -[ASTEnvironment _defaultServerURL].cold.1
+ -[ASTEnvironment isDiagnosticsMode]
+ -[ASTInstructionalPrompt navigationBarActions]
+ -[ASTInstructionalPrompt setNavigationBarActions:]
+ -[ASTNetworking _requestTimeInterval].cold.1
+ -[ASTNetworking networkDisconnectRetryCount].cold.1
+ -[ASTSessionInfo _descriptionForSessionType:]
+ -[ASTSessionInfo deviceIndex]
+ -[ASTSessionInfo initWithQueuedSuiteType:isGuided:deviceIndex:sessionType:]
+ -[ASTSessionInfo sessionType]
+ ASTLogHandleForCategory.cold.1
+ GCC_except_table103
+ GCC_except_table106
+ GCC_except_table118
+ GCC_except_table90
+ GCC_except_table95
+ OBJC_IVAR_$_ASTInstructionalPrompt._navigationBarActions
+ OBJC_IVAR_$_ASTSessionInfo._deviceIndex
+ OBJC_IVAR_$_ASTSessionInfo._sessionType
+ _ASTInstructionIconIdentifierKey
+ _ASTInstructionNavBarActionsKey
+ _ASTInstructionSubtitleKey
+ _ASTInstructionTitleKey
+ __141-[ASTMaterializedConnectionManager requestSelfServiceSuitesAvailableWithConfigCode:withPayloadSigner:allowsCellularAccess:completionHandler:]_block_invoke.98
+ __165-[ASTMaterializedConnectionManager requestInstructionalPromptDetailsWithInstructionID:type:withPayloadSigner:language:locale:allowsCellularAccess:completionHandler:]_block_invoke.cold.3
+ ___33+[ASTEnvironment protocolVersion]_block_invoke
+ ___block_descriptor_40_e8_32bs_e68_v68?0B8B12i16q20"NSString"28"NSString"36q44"NSURL"52"NSError"60l
+ ___block_descriptor_64_e8_32s40s48s56r_e44_v24?0"ASTInstructionalPrompt"8"NSError"16l
+ __block_literal_global.71
+ __block_literal_global.96
+ __block_literal_global.98
+ _objc_msgSend$_descriptionForSessionType:
+ _objc_msgSend$deviceIndex
+ _objc_msgSend$initWithID:type:iconLocator:localizedTitle:localizedSubtitle:imageLocators:instructions:options:
+ _objc_msgSend$initWithQueuedSuiteType:isGuided:deviceIndex:sessionType:
+ _objc_msgSend$isDiagnosticsMode
+ _objc_msgSend$navigationBarActions
+ _objc_msgSend$protocolVersion
+ _objc_msgSend$sessionType
+ _objc_msgSend$setNavigationBarActions:
+ protocolVersion.onceToken
- -[ASTRemoteServerSession _showInstructionalPromptWithData:].cold.2
- -[ASTSessionInfo initWithQueuedSuiteType:isGuided:]
- GCC_except_table105
- GCC_except_table116
- GCC_except_table120
- GCC_except_table97
- GCC_except_table98
- _OUTLINED_FUNCTION_8
- __141-[ASTMaterializedConnectionManager requestSelfServiceSuitesAvailableWithConfigCode:withPayloadSigner:allowsCellularAccess:completionHandler:]_block_invoke.80
- ___block_descriptor_40_e8_32bs_e62_v56?0B8B12q16"NSString"24"NSString"32"NSURL"40"NSError"48l
- ___block_descriptor_80_e8_32s40s48s56s64r_e53_v40?0"NSArray"8"NSArray"16"NSArray"24"NSError"32l
- ___copy_helper_block_e8_32s40s48s56s64r
- ___destroy_helper_block_e8_32s40s48s56s64r
- __block_literal_global.68
- __block_literal_global.78
- _objc_msgSend$initWithID:type:imageLocators:instructions:options:
- _objc_msgSend$initWithQueuedSuiteType:isGuided:
CStrings:
+ "%@%@"
+ "@40@0:8q16B24i28q32"
+ "ProtocolVersion"
+ "T@\"NSArray\",&,N,V_navigationBarActions"
+ "Ti,R,N,V_deviceIndex"
+ "Tq,R,N,V_sessionType"
+ "[ASTSessionInfo queuedSuiteType: %@, isGuided: %d, deviceIndex: %d sessionType: %@]"
+ "_descriptionForSessionType:"
+ "_deviceIndex"
+ "_navigationBarActions"
+ "_sessionType"
+ "deviceIndex"
+ "diagnostics"
+ "https://idiagnostics-acstage.corp.apple.com/%@/v%@/"
+ "https://idiagnostics-it.apple.com/%@/v%@/"
+ "https://idiagnostics-it1.apple.com/%@/v%@/"
+ "https://idiagnostics-it2.apple.com/%@/v%@/"
+ "https://idiagnostics-it4-ause1.apple.com/%@/v%@/"
+ "https://idiagnostics-mdn1.apple.com/%@/v%@/"
+ "https://idiagnostics-nwk1.apple.com/%@/v%@/"
+ "https://idiagnostics-prod2-mdn.apple.com/%@/v%@/"
+ "https://idiagnostics-prod2-rno.apple.com/%@/v%@/"
+ "https://idiagnostics-prod2.apple.com/%@/v%@/"
+ "https://idiagnostics-qa.apple.com/%@/v%@/"
+ "https://idiagnostics-reno.apple.com/%@/v%@/"
+ "https://idiagnostics-stage1.apple.com/%@/v%@/"
+ "https://idiagnostics-staging.apple.com/%@/v%@/"
+ "https://idiagnostics-uat.apple.com/%@/v%@/"
+ "https://idiagnostics-uat1.apple.com/%@/v%@/"
+ "https://idiagnostics.apple.com/%@/v%@/"
+ "iconIdentifier"
+ "initWithQueuedSuiteType:isGuided:deviceIndex:sessionType:"
+ "isDiagnosticsMode"
+ "mas"
+ "navigationBarActions"
+ "nonguided"
+ "protocolVersion"
+ "sessionType"
+ "setNavigationBarActions:"
+ "subtitle"
+ "v24@?0@\"ASTInstructionalPrompt\"8@\"NSError\"16"
+ "v56@0:8@\"NSArray\"16@\"NSString\"24d32B40B44@?<v@?BBiq@\"NSString\"@\"NSString\"q@\"NSURL\"@\"NSError\">48"
+ "v68@0:8@\"NSNumber\"16@\"NSString\"24@?<@\"NSData\"@?@\"NSData\"^@>32@\"NSString\"40@\"NSString\"48B56@?<v@?@\"ASTInstructionalPrompt\"@\"NSError\">60"
+ "v68@?0B8B12i16q20@\"NSString\"28@\"NSString\"36q44@\"NSURL\"52@\"NSError\"60"
- " https://idiagnostics-acstage.corp.apple.com/%@/v1.6/"
- "@28@0:8q16B24"
- "[ASTSessionInfo queuedSuiteType: %@, isGuided: %d]"
- "https://idiagnostics-it.apple.com/%@/v1.6/"
- "https://idiagnostics-it1.apple.com/%@/v1.6/"
- "https://idiagnostics-it2.apple.com/%@/v1.6/"
- "https://idiagnostics-it4-ause1.apple.com/%@/v1.6/"
- "https://idiagnostics-mdn1.apple.com/%@/v1.6/"
- "https://idiagnostics-nwk1.apple.com/%@/v1.6/"
- "https://idiagnostics-prod2-mdn.apple.com/%@/v1.6/"
- "https://idiagnostics-prod2-rno.apple.com/%@/v1.6/"
- "https://idiagnostics-prod2.apple.com/%@/v1.6/"
- "https://idiagnostics-qa.apple.com/%@/v1.6/"
- "https://idiagnostics-reno.apple.com/%@/v1.6/"
- "https://idiagnostics-stage1.apple.com/%@/v1.6/"
- "https://idiagnostics-staging.apple.com/%@/v1.6/"
- "https://idiagnostics-uat.apple.com/%@/v1.6/"
- "https://idiagnostics-uat1.apple.com/%@/v1.6/"
- "https://idiagnostics.apple.com/%@/v1.6/"
- "initWithQueuedSuiteType:isGuided:"
- "v40@?0@\"NSArray\"8@\"NSArray\"16@\"NSArray\"24@\"NSError\"32"
- "v56@0:8@\"NSArray\"16@\"NSString\"24d32B40B44@?<v@?BBq@\"NSString\"@\"NSString\"@\"NSURL\"@\"NSError\">48"
- "v56@?0B8B12q16@\"NSString\"24@\"NSString\"32@\"NSURL\"40@\"NSError\"48"
- "v68@0:8@\"NSNumber\"16@\"NSString\"24@?<@\"NSData\"@?@\"NSData\"^@>32@\"NSString\"40@\"NSString\"48B56@?<v@?@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSError\">60"

```
