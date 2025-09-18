## AccessibilityUIService

> `/System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService`

```diff

-3093.2.4.4.11
-  __TEXT.__text: 0x1345c
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x1414
+3093.23.0.0.0
+  __TEXT.__text: 0x13fc4
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_methlist: 0x1454
   __TEXT.__const: 0x1b8
-  __TEXT.__cstring: 0x1174
-  __TEXT.__oslogstring: 0xb9b
-  __TEXT.__gcc_except_tab: 0x3b0
-  __TEXT.__unwind_info: 0x610
-  __TEXT.__objc_classname: 0x358
-  __TEXT.__objc_methname: 0x61af
-  __TEXT.__objc_methtype: 0xf97
-  __TEXT.__objc_stubs: 0x48a0
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x880
+  __TEXT.__cstring: 0x1075
+  __TEXT.__oslogstring: 0xe5d
+  __TEXT.__gcc_except_tab: 0x3dc
+  __TEXT.__unwind_info: 0x638
+  __TEXT.__objc_classname: 0x35a
+  __TEXT.__objc_methname: 0x63c1
+  __TEXT.__objc_methtype: 0x105b
+  __TEXT.__objc_stubs: 0x49e0
+  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__const: 0x8d0
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x22f8
-  __DATA_CONST.__objc_selrefs: 0x14d0
+  __DATA_CONST.__objc_const: 0x23b0
+  __DATA_CONST.__objc_selrefs: 0x1518
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x2a0
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__objc_const: 0x948
-  __AUTH_CONST.__cfstring: 0x980
+  __AUTH_CONST.__cfstring: 0x9a0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__auth_got: 0x430
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x2a0
-  __DATA.__objc_superrefs: 0x78
-  __DATA.__objc_ivar: 0x15c
+  __DATA.__objc_ivar: 0x164
   __DATA.__data: 0x4e8
   __DATA.__common: 0x8
   __DATA.__bss: 0x10

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 32B74D81-0F01-338C-BBF5-E0B17AAC88DF
-  Functions: 506
-  Symbols:   2259
-  CStrings:  1311
+  UUID: 78874282-27E1-32B8-A89D-1CE7E45A70A6
+  Functions: 521
+  Symbols:   2305
+  CStrings:  1338
 
Symbols:
+ -[AXUIAssertionManager setTimerBackground:]
+ -[AXUIAssertionManager setTimerUI:]
+ -[AXUIAssertionManager timerBackground]
+ -[AXUIAssertionManager timerUI]
+ -[AXUIServiceContext pidForClientWithIdentifier:]
+ -[AXUIServiceEntitlementChecker _isSafeToProcessMessageFromUnentitledProcessWithIdentifier:]
+ -[AXUIServiceEntitlementChecker _possibleRequiredEntitlementForMessageWithIdentifier:].cold.1
+ -[AXUIServiceEntitlementChecker serviceCanProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:needsToRequireEntitlements:]
+ -[AXUIServiceEntitlementChecker serviceCanProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:needsToRequireEntitlements:].cold.1
+ -[AXUIServiceManager _processXPCObject:context:].cold.5
+ -[AXUIServiceManager _serviceWithClass:canProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:needsToRequireEntitlements:]
+ GCC_except_table45
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table65
+ GCC_except_table69
+ _AXUIErrorDomainServiceNeedsToRequireEntitlements
+ _OBJC_IVAR_$_AXUIAssertionManager._timerBackground
+ _OBJC_IVAR_$_AXUIAssertionManager._timerUI
+ ___153-[AXUIServiceManager _serviceWithClass:canProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:needsToRequireEntitlements:]_block_invoke
+ ___44-[AXUIDisplayManager _showAlertWithContext:]_block_invoke.431
+ ___44-[AXUIDisplayManager _showAlertWithContext:]_block_invoke.439
+ ___48-[AXUIServiceManager _processXPCObject:context:]_block_invoke.330
+ ___48-[AXUIServiceManager _processXPCObject:context:]_block_invoke_2.331
+ ___48-[AXUIServiceManager _processXPCObject:context:]_block_invoke_3.332
+ ___48-[AXUIServiceManager _processXPCObject:context:]_block_invoke_4
+ ___48-[AXUIServiceManager _processXPCObject:context:]_block_invoke_5
+ ___48-[AXUIServiceManager _processXPCObject:context:]_block_invoke_6
+ ___49-[AXUIServiceContext pidForClientWithIdentifier:]_block_invoke
+ ___51-[AXUIAssertionManager invalidateAssertionIfNeeded]_block_invoke
+ ___53-[AXUIAssertionManager invalidateAssertionUIIfNeeded]_block_invoke
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56r_e5_v8?0ls32l8s40l8u64l8r56l8s48l8
+ ___block_literal_global.349
+ __os_log_fault_impl
+ _objc_msgSend$_isSafeToProcessMessageFromUnentitledProcessWithIdentifier:
+ _objc_msgSend$_serviceWithClass:canProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:needsToRequireEntitlements:
+ _objc_msgSend$assertionBackground
+ _objc_msgSend$assertionUI
+ _objc_msgSend$clientsWithUIAssertion
+ _objc_msgSend$isSafeToProcessMessageFromUnentitledProcessWithIdentifier:
+ _objc_msgSend$pidForClientWithIdentifier:
+ _objc_msgSend$processMessage:withIdentifier:fromClientWithIdentifier:pid:error:
+ _objc_msgSend$processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:pid:completion:
+ _objc_msgSend$serviceCanProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:needsToRequireEntitlements:
+ _objc_msgSend$timerBackground
+ _objc_msgSend$timerUI
- -[AXUIServiceEntitlementChecker serviceCanProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:]
- -[AXUIServiceManager _serviceWithClass:canProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:]
- GCC_except_table42
- GCC_except_table55
- GCC_except_table56
- GCC_except_table62
- GCC_except_table66
- GCC_except_table68
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXUIService
- ___126-[AXUIServiceManager _serviceWithClass:canProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:]_block_invoke
- ___44-[AXUIDisplayManager _showAlertWithContext:]_block_invoke.399
- ___44-[AXUIDisplayManager _showAlertWithContext:]_block_invoke.407
- ___48-[AXUIServiceManager _processXPCObject:context:]_block_invoke.301
- ___48-[AXUIServiceManager _processXPCObject:context:]_block_invoke_2.302
- ___48-[AXUIServiceManager _processXPCObject:context:]_block_invoke_3.303
- ___block_descriptor_88_e8_32s40s48s56r_e5_v8?0ls32l8s40l8u64l8r56l8s48l8
- ___block_literal_global.316
- _objc_msgSend$_serviceWithClass:canProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:
- _objc_msgSend$serviceCanProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:
CStrings:
+ "\x05"
+ "@\"NSDictionary\"52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40^@44"
+ "@52@0:8@16Q24@32i40^@44"
+ "B48@0:8Q16@24^@32^B40"
+ "B56@0:8#16Q24@32^@40^B48"
+ "Can't invalidate Background Assertion, still services are registered"
+ "Can't invalidate UI Assertion, still UI is presented"
+ "Can't invalidate UI Assertion, still clients with UI assertion %@"
+ "Implementors of AXUIService must implement either processMessage:withIdentifier:fromClientWithIdentifier:error: or processMessage:withIdentifier:fromClientWithIdentifier:pid:error:."
+ "Service: '%@' unable to process message:'%@'. The service needs to require entitlements."
+ "T@\"AXDispatchTimer\",&,N,V_timerBackground"
+ "T@\"AXDispatchTimer\",&,N,V_timerUI"
+ "T@\"NSString\",?,R,C"
+ "The service must require entitlements for this operation: %d"
+ "Unexpectedly received an empty array from possibleRequiredEntitlementsForProcessingMessageWithIdentifier:. The array must have at least one object."
+ "_isSafeToProcessMessageFromUnentitledProcessWithIdentifier:"
+ "_serviceWithClass:canProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:needsToRequireEntitlements:"
+ "_timerBackground"
+ "_timerUI"
+ "invalidateAssertionIfNeeded timer"
+ "invalidateAssertionUIIfNeeded timer"
+ "isSafeToProcessMessageFromUnentitledProcessWithIdentifier:"
+ "pidForClientWithIdentifier:"
+ "processMessage:withIdentifier:fromClientWithIdentifier:pid:error:"
+ "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:pid:completion:"
+ "serviceCanProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:needsToRequireEntitlements:"
+ "setTimerBackground:"
+ "setTimerUI:"
+ "timerBackground"
+ "timerUI"
+ "v52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
+ "v52@0:8@16Q24@32i40@?44"
- "-[AXUIServiceEntitlementChecker serviceCanProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:]"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/AccessibilityUmbrellaFramework/Frameworks/AccessibilityUI/Service/AXUIServiceEntitlementChecker.m"
- "B40@0:8Q16@24^@32"
- "B48@0:8#16Q24@32^@40"
- "_serviceWithClass:canProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:"
- "serviceCanProcessMessageWithIdentifier:fromClientWithConnection:possibleRequiredEntitlements:"

```
