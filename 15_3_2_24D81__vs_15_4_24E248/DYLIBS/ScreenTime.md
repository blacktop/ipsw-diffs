## ScreenTime

> `/System/iOSSupport/System/Library/Frameworks/ScreenTime.framework/Versions/A/ScreenTime`

```diff

-537.3.3.0.0
-  __TEXT.__text: 0x4510
-  __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_methlist: 0x460
+537.4.20.1.0
+  __TEXT.__text: 0x4da4
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__objc_methlist: 0x6cc
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x26b
+  __TEXT.__cstring: 0x287
   __TEXT.__gcc_except_tab: 0x180
-  __TEXT.__oslogstring: 0x53c
-  __TEXT.__unwind_info: 0x208
+  __TEXT.__oslogstring: 0x568
+  __TEXT.__unwind_info: 0x230
   __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methname: 0x1202
-  __TEXT.__objc_methtype: 0x45f
-  __TEXT.__objc_stubs: 0xdc0
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x238
+  __TEXT.__objc_methname: 0x13f4
+  __TEXT.__objc_methtype: 0x57a
+  __TEXT.__objc_stubs: 0xe40
+  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x470
+  __DATA_CONST.__objc_selrefs: 0x538
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1a0
-  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x11e8
+  __AUTH_CONST.__objc_const: 0xee0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x44
+  __DATA.__objc_ivar: 0x4c
   __DATA.__data: 0x2a0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4304E373-74A6-392D-B066-3BED8351AA98
-  Functions: 145
-  Symbols:   516
-  CStrings:  327
+  UUID: 0E942685-2A99-348E-A389-242C1F6BEC4B
+  Functions: 157
+  Symbols:   546
+  CStrings:  345
 
Symbols:
+ -[STWebHistory fetchAllHistoryWithCompletionHandler:]
+ -[STWebHistory fetchHistoryDuringInterval:completionHandler:]
+ -[STWebHistory initWithBundleIdentifier:profileIdentifier:]
+ -[STWebHistory initWithBundleIdentifier:profileIdentifier:error:]
+ -[STWebHistory initWithProfileIdentifier:]
+ -[STWebHistory profileIdentifier]
+ -[STWebpageController _setURL:bundleIdentifier:profileIdentifier:usageState:errorHandler:]
+ -[STWebpageController profileIdentifier]
+ -[STWebpageController setProfileIdentifier:]
+ GCC_except_table11
+ GCC_except_table18
+ GCC_except_table23
+ OBJC_IVAR_$_STWebHistory._profileIdentifier
+ OBJC_IVAR_$_STWebpageController._profileIdentifier
+ _OBJC_CLASS_$_NSDateInterval
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSURL
+ __31-[STWebpageController loadView]_block_invoke.cold.1
+ __32-[STWebHistory deleteAllHistory]_block_invoke.19
+ __32-[STWebHistory deleteAllHistory]_block_invoke.19.cold.1
+ __32-[STWebHistory deleteAllHistory]_block_invoke.19.cold.2
+ __32-[STWebHistory deleteAllHistory]_block_invoke_2.20
+ __32-[STWebHistory deleteAllHistory]_block_invoke_2.20.cold.1
+ __36-[STWebHistory deleteHistoryForURL:]_block_invoke.15
+ __36-[STWebHistory deleteHistoryForURL:]_block_invoke.15.cold.1
+ __36-[STWebHistory deleteHistoryForURL:]_block_invoke.15.cold.2
+ __36-[STWebHistory deleteHistoryForURL:]_block_invoke_2.16
+ __36-[STWebHistory deleteHistoryForURL:]_block_invoke_2.16.cold.1
+ __44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke.17
+ __44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke.17.cold.1
+ __44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke.17.cold.2
+ __44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke_2.18
+ __44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke_2.18.cold.1
+ __44-[STWebpageController setProfileIdentifier:]_block_invoke.cold.1
+ __53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke.cold.1
+ __61-[STWebHistory fetchHistoryDuringInterval:completionHandler:]_block_invoke.cold.1
+ ___44-[STWebpageController setProfileIdentifier:]_block_invoke
+ ___53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke
+ ___53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke_2
+ ___61-[STWebHistory fetchHistoryDuringInterval:completionHandler:]_block_invoke
+ ___61-[STWebHistory fetchHistoryDuringInterval:completionHandler:]_block_invoke_2
+ ___90-[STWebpageController _setURL:bundleIdentifier:profileIdentifier:usageState:errorHandler:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e27_v24?0"NSSet"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e41_v24?0"<STScreenTimeAgent>"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e41_v24?0"<STScreenTimeAgent>"8"NSError"16ls32l8s40l8s48l8
+ __block_literal_global.47
+ __block_literal_global.53
+ __block_literal_global.56
+ _objc_msgSend$_setURL:bundleIdentifier:profileIdentifier:usageState:errorHandler:
+ _objc_msgSend$deleteAllWebApplicationHistory:profileIdentifier:clientBundleURLWrapper:replyHandler:
+ _objc_msgSend$deleteWebHistoryDuringInterval:webApplication:profileIdentifier:clientBundleURLWrapper:replyHandler:
+ _objc_msgSend$deleteWebHistoryForURL:webApplication:profileIdentifier:clientBundleURLWrapper:replyHandler:
+ _objc_msgSend$fetchAllWebApplicationHistory:profileIdentifier:replyHandler:
+ _objc_msgSend$fetchHistoryDuringInterval:webApplication:profileIdentifier:replyHandler:
+ _objc_msgSend$initWithBundleIdentifier:profileIdentifier:
+ _objc_msgSend$initWithBundleIdentifier:profileIdentifier:error:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$profileIdentifier
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setClientBundleURLWrapper:webpageURL:bundleIdentifier:profileIdentifier:usageState:replyHandler:
+ _objc_msgSend$setURL:bundleIdentifier:profileIdentifier:usageState:replyHandler:
+ _objc_opt_class
+ _objc_release_x26
+ _objc_retain
+ _objc_retain_x24
+ _objc_retain_x6
- -[STWebHistory initWithBundleIdentifier:]
- -[STWebpageController _delayedSetURLIsBlocked:]
- -[STWebpageController _setURL:bundleIdentifier:usageState:errorHandler:]
- GCC_except_table15
- GCC_except_table3
- __32-[STWebHistory deleteAllHistory]_block_invoke.18
- __32-[STWebHistory deleteAllHistory]_block_invoke.18.cold.1
- __32-[STWebHistory deleteAllHistory]_block_invoke.18.cold.2
- __32-[STWebHistory deleteAllHistory]_block_invoke_2.19
- __32-[STWebHistory deleteAllHistory]_block_invoke_2.19.cold.1
- __36-[STWebHistory deleteHistoryForURL:]_block_invoke.13
- __36-[STWebHistory deleteHistoryForURL:]_block_invoke.13.cold.1
- __36-[STWebHistory deleteHistoryForURL:]_block_invoke.13.cold.2
- __36-[STWebHistory deleteHistoryForURL:]_block_invoke_2.14
- __36-[STWebHistory deleteHistoryForURL:]_block_invoke_2.14.cold.1
- __44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke.16
- __44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke.16.cold.1
- __44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke.16.cold.2
- __44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke_2.17
- __44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke_2.17.cold.1
- ___72-[STWebpageController _setURL:bundleIdentifier:usageState:errorHandler:]_block_invoke
- __block_literal_global.54
- __block_literal_global.57
- _arc4random_uniform
- _objc_msgSend$_setURL:bundleIdentifier:usageState:errorHandler:
- _objc_msgSend$cancelPreviousPerformRequestsWithTarget:selector:object:
- _objc_msgSend$deleteAllWebApplicationHistory:clientBundleURLWrapper:replyHandler:
- _objc_msgSend$deleteWebHistoryDuringInterval:webApplication:clientBundleURLWrapper:replyHandler:
- _objc_msgSend$deleteWebHistoryForURL:webApplication:clientBundleURLWrapper:replyHandler:
- _objc_msgSend$initWithBundleIdentifier:
- _objc_msgSend$performSelector:withObject:afterDelay:
- _objc_msgSend$setClientBundleURLWrapper:webpageURL:bundleIdentifier:usageState:replyHandler:
- _objc_msgSend$setURL:bundleIdentifier:usageState:replyHandler:
- _objc_retain_x5
CStrings:
+ "%"
+ "@32@0:8@16@24"
+ "@40@0:8@16@24^@32"
+ "Failed to set profileIdentifier: %{public}@"
+ "T@\"NSString\",C,N,V_profileIdentifier"
+ "T@\"NSString\",R,C,V_profileIdentifier"
+ "_profileIdentifier"
+ "_setURL:bundleIdentifier:profileIdentifier:usageState:errorHandler:"
+ "deleteAllWebApplicationHistory:profileIdentifier:clientBundleURLWrapper:replyHandler:"
+ "deleteWebHistoryDuringInterval:webApplication:profileIdentifier:clientBundleURLWrapper:replyHandler:"
+ "deleteWebHistoryForURL:webApplication:profileIdentifier:clientBundleURLWrapper:replyHandler:"
+ "fetchAllHistoryWithCompletionHandler:"
+ "fetchAllWebApplicationHistory:profileIdentifier:replyHandler:"
+ "fetchHistoryDuringInterval:completionHandler:"
+ "fetchHistoryDuringInterval:webApplication:profileIdentifier:replyHandler:"
+ "initWithBundleIdentifier:profileIdentifier:"
+ "initWithBundleIdentifier:profileIdentifier:error:"
+ "initWithObjects:"
+ "initWithProfileIdentifier:"
+ "profileIdentifier"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setClientBundleURLWrapper:webpageURL:bundleIdentifier:profileIdentifier:usageState:replyHandler:"
+ "setProfileIdentifier:"
+ "setURL:bundleIdentifier:profileIdentifier:usageState:replyHandler:"
+ "v24@?0@\"NSSet\"8@\"NSError\"16"
+ "v32@0:8@16@?24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSSet\"@\"NSError\">32"
+ "v48@0:8@\"NSDateInterval\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSSet\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSSecurityScopedURLWrapper\"32@?<v@?@\"NSError\">40"
+ "v56@0:8@\"NSDateInterval\"16@\"NSString\"24@\"NSString\"32@\"NSSecurityScopedURLWrapper\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32@\"NSSecurityScopedURLWrapper\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32q40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
+ "v64@0:8@\"NSSecurityScopedURLWrapper\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40q48@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24@32@40q48@?56"
- "$"
- "_delayedSetURLIsBlocked:"
- "_setURL:bundleIdentifier:usageState:errorHandler:"
- "cancelPreviousPerformRequestsWithTarget:selector:object:"
- "deleteAllWebApplicationHistory:clientBundleURLWrapper:replyHandler:"
- "deleteWebHistoryDuringInterval:webApplication:clientBundleURLWrapper:replyHandler:"
- "deleteWebHistoryForURL:webApplication:clientBundleURLWrapper:replyHandler:"
- "initWithBundleIdentifier:"
- "performSelector:withObject:afterDelay:"
- "setClientBundleURLWrapper:webpageURL:bundleIdentifier:usageState:replyHandler:"
- "setURL:bundleIdentifier:usageState:replyHandler:"
- "v40@0:8@\"NSString\"16@\"NSSecurityScopedURLWrapper\"24@?<v@?@\"NSError\">32"
- "v48@0:8@\"NSDateInterval\"16@\"NSString\"24@\"NSSecurityScopedURLWrapper\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSURL\"16@\"NSString\"24@\"NSSecurityScopedURLWrapper\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSURL\"16@\"NSString\"24q32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24q32@?40"
- "v56@0:8@\"NSSecurityScopedURLWrapper\"16@\"NSURL\"24@\"NSString\"32q40@?<v@?@\"NSError\">48"

```
