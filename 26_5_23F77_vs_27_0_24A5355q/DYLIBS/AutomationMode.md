## AutomationMode

> `/System/Library/PrivateFrameworks/AutomationMode.framework/AutomationMode`

```diff

-31.0.0.0.0
-  __TEXT.__text: 0x4278
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x3c0
+34.0.0.0.0
+  __TEXT.__text: 0x4054
+  __TEXT.__objc_methlist: 0x3f0
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x138
-  __TEXT.__cstring: 0x37b
+  __TEXT.__gcc_except_tab: 0x12c
+  __TEXT.__cstring: 0x380
   __TEXT.__oslogstring: 0x566
-  __TEXT.__unwind_info: 0x1f8
-  __TEXT.__objc_classname: 0xb8
-  __TEXT.__objc_methname: 0xb0a
-  __TEXT.__objc_methtype: 0x265
-  __TEXT.__objc_stubs: 0x7e0
-  __DATA_CONST.__got: 0x58
+  __TEXT.__unwind_info: 0x200
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c8
+  __DATA_CONST.__objc_selrefs: 0x2e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1a8
-  __AUTH_CONST.__const: 0x100
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0x700
+  __AUTH_CONST.__objc_const: 0x708
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x1e0

   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F513382-D9E2-33AF-AA03-C8B69D052002
-  Functions: 115
-  Symbols:   468
-  CStrings:  236
+  UUID: D642AEB8-FB9E-3CFF-8D7A-CB69F38CD52E
+  Functions: 120
+  Symbols:   485
+  CStrings:  75
 
Symbols:
+ -[XAMWriter _usingAsyncProxyResetResentAuthenticationWithCompletion:]
+ -[XAMWriter resetRecentAuthenticationWithCompletion:]
+ -[XAMWriter resetRecentAuthenticationWithError:]
+ GCC_except_table12
+ GCC_except_table37
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table49
+ GCC_except_table52
+ GCC_except_table55
+ _XAMResetRecentAuthentication
+ _XAMResetRecentAuthenticationWithCompletion
+ ___43-[XAMWriter enableAutomationModeWithError:]_block_invoke.23
+ ___48-[XAMWriter resetRecentAuthenticationWithError:]_block_invoke
+ ___48-[XAMWriter resetRecentAuthenticationWithError:]_block_invoke_2
+ ___54-[XAMWriter _setAutomationModeEnabled:withCompletion:]_block_invoke.15.cold.1
+ ___54-[XAMWriter _setAutomationModeEnabled:withCompletion:]_block_invoke.16
+ ___69-[XAMWriter _usingAsyncProxyResetResentAuthenticationWithCompletion:]_block_invoke
+ ___69-[XAMWriter _usingAsyncProxyResetResentAuthenticationWithCompletion:]_block_invoke.19
+ ___69-[XAMWriter _usingAsyncProxyResetResentAuthenticationWithCompletion:]_block_invoke.19.cold.1
+ ___73-[XAMWriter _usingAsyncProxyEnablePasswordlessAutomation:withCompletion:]_block_invoke.18
+ ___73-[XAMWriter _usingAsyncProxyEnablePasswordlessAutomation:withCompletion:]_block_invoke.18.cold.1
+ ___block_literal_global.22
+ ___block_literal_global.27
+ ___block_literal_global.29
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_usingAsyncProxyResetResentAuthenticationWithCompletion:
+ _objc_msgSend$resetRecentAuthenticationWithCompletion:
+ _objc_msgSend$resetRecentAuthenticationWithError:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- GCC_except_table31
- GCC_except_table36
- GCC_except_table39
- GCC_except_table43
- GCC_except_table46
- _OUTLINED_FUNCTION_3
- ___43-[XAMWriter enableAutomationModeWithError:]_block_invoke.21
- ___54-[XAMWriter _setAutomationModeEnabled:withCompletion:]_block_invoke.14
- ___54-[XAMWriter _setAutomationModeEnabled:withCompletion:]_block_invoke.14.cold.1
- ___73-[XAMWriter _usingAsyncProxyEnablePasswordlessAutomation:withCompletion:]_block_invoke.17
- ___73-[XAMWriter _usingAsyncProxyEnablePasswordlessAutomation:withCompletion:]_block_invoke.17.cold.1
- ___block_literal_global.20
- ___block_literal_global.23
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<XAMAuthorization>\"24@0:8^@16"
- "@\"<XAMAuthorizationProvider>\""
- "@\"NSData\"16@0:8"
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16@?24"
- "@32@0:8@?16@24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "AutomationModeReaderProtocol"
- "AutomationModeWriterProtocol"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@?16^@24"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"<XAMAuthorizationProvider>\",R,V_authorizationProvider"
- "T@\"NSData\",R"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,V_changeNotificationName"
- "T@\"XAMObserver\",R"
- "T@\"XAMWriter\",R"
- "T@?,R,V_readerConnectionFactory"
- "T@?,R,V_writerConnectionFactory"
- "TB,R"
- "TB,R,V_isAutomationModeEnabled"
- "TQ,R"
- "URLByAppendingPathComponent:"
- "UTF8String"
- "UUID"
- "Vv16@0:8"
- "XAMAuthorization"
- "XAMAuthorizationProvider"
- "XAMHandlerRecord"
- "XAMLocalAuthenticationProvider"
- "XAMObserver"
- "XAMWriter"
- "^{_NSZone=}16@0:8"
- "_authenticateAndEnableAutomationModeWithProxy:completion:"
- "_authorizationProvider"
- "_block"
- "_changeNotificationName"
- "_enableAutomationModeWithProxy:authorization:completion:"
- "_enableAutomationModeWithProxy:completion:"
- "_handlers"
- "_hasReceivedAutomationModeEnabledState"
- "_isAutomationModeEnabled"
- "_listenForAutomationModeChangeNotifications"
- "_makeAuthorizationContext"
- "_notifyHandlers"
- "_observationToken"
- "_queue"
- "_readerConnectionFactory"
- "_setAutomationModeEnabled:withCompletion:"
- "_usingAsyncProxyEnablePasswordlessAutomation:withCompletion:"
- "_usingSyncProxy:withError:"
- "_writerConnectionFactory"
- "allValues"
- "authorizationProvider"
- "authorizationWithError:"
- "automationModeRequiresAuthentication"
- "autorelease"
- "bundleForClass:"
- "changeNotificationName"
- "class"
- "code"
- "conformsToProtocol:"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "createNoAuthenticationRequiredCookieWithCompletion:"
- "createNoAuthenticationRequiredCookieWithError:"
- "currentAutomationModeEnabledStateFromDaemon"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "disableAutomationModeWithCompletion:"
- "disableAutomationModeWithError:"
- "domain"
- "enableAutomationModeWithAuthorization:completion:"
- "enableAutomationModeWithCompletion:"
- "enableAutomationModeWithError:"
- "environment"
- "evaluatePolicy:localizedReason:reply:"
- "evaluatePolicy:options:error:"
- "externalizedContext"
- "fileURLWithPath:"
- "hash"
- "i"
- "init"
- "initWithChangeNotificationName:readerConnectionFactory:"
- "initWithMachServiceName:options:"
- "initWithWriterConnectionFactory:authorizationProvider:"
- "interfaceWithProtocol:"
- "invalidate"
- "isAutomationModeEnabled"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "localizedAuthorizationReason"
- "localizedStringForKey:value:table:"
- "objectForKeyedSubscript:"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processInfo"
- "queue"
- "readerConnectionFactory"
- "registerAutomationModeChangeHandlerOnQueue:withBlock:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeNoAuthenticationRequiredCookieWithCompletion:"
- "removeNoAuthenticationRequiredCookieWithError:"
- "requestAuthorizationWithReply:"
- "requestAutomationModeEnabledStateWithReply:"
- "requestAutomationModeRequiresAuthenticationWithReply:"
- "resetSharedWriter"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setObject:forKeyedSubscript:"
- "setOptionCallerName:"
- "setRemoteObjectInterface:"
- "sharedInstance"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "unregisterAutomationModeChangeHandler:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"<XAMAuthorization>\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?B>16"
- "v28@0:8B16@?20"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@16@24@?32"
- "writerConnectionFactory"
- "zone"

```
