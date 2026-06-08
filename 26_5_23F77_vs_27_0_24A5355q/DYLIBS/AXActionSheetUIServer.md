## AXActionSheetUIServer

> `/System/Library/AccessibilityBundles/AXActionSheetUIServer.axuiservice/AXActionSheetUIServer`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x11c0
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__objc_methlist: 0x31c
+3229.1.6.0.0
+  __TEXT.__text: 0x102c
+  __TEXT.__objc_methlist: 0x344
   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x158
   __TEXT.__oslogstring: 0xda
-  __TEXT.__cstring: 0xed
-  __TEXT.__unwind_info: 0xa8
-  __TEXT.__objc_classname: 0x61
-  __TEXT.__objc_methname: 0xb17
-  __TEXT.__objc_methtype: 0x41e
-  __TEXT.__objc_stubs: 0x4a0
-  __DATA_CONST.__got: 0x78
+  __TEXT.__cstring: 0xef
+  __TEXT.__unwind_info: 0xa0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c8
+  __DATA_CONST.__objc_selrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0x3c0
+  __AUTH_CONST.__objc_const: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0DC67FB5-CB93-3605-8B61-5A5FB14DFB5C
-  Functions: 19
-  Symbols:   173
-  CStrings:  189
+  UUID: 7A055972-1E5B-31CF-B892-6A9CEB4796D4
+  Functions: 18
+  Symbols:   171
+  CStrings:  38
 
Symbols:
+ GCC_except_table8
+ ___86-[AXActionSheetUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke.383
+ ___block_literal_global.386
+ ___block_literal_global.419
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x8
- GCC_except_table2
- ___47-[AXActionSheetUIServer _informClientOfChoice:]_block_invoke.cold.1
- ___86-[AXActionSheetUIServer processMessage:withIdentifier:fromClientWithIdentifier:error:]_block_invoke.362
- ___block_literal_global.365
- ___block_literal_global.398
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x25
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AXUIAlertStyleProvider>\"24@0:8@\"NSString\"16"
- "@\"AXAccessQueue\"24@0:8Q16"
- "@\"NSDictionary\"48@0:8@\"NSDictionary\"16Q24@\"NSString\"32^@40"
- "@\"NSDictionary\"52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40^@44"
- "@\"NSMutableSet\""
- "@\"NSSet\"24@0:8Q16"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8Q16"
- "@\"UIAlertController\""
- "@\"UIViewController\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@48@0:8@16Q24@32^@40"
- "@52@0:8@16Q24@32i40^@44"
- "AXActionSheetUIServer"
- "AXUIAlertDelegate"
- "AXUIContentViewControllerDelegate"
- "AXUIService"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",&,N,V_alertIdentifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_actionSheetClients"
- "_alertController"
- "_alertIdentifier"
- "_emptyViewController"
- "_informClientOfChoice:"
- "accessQueueForProcessingMessageWithIdentifier:"
- "actionWithTitle:style:handler:"
- "addAction:"
- "addContentViewController:withUserInteractionEnabled:forService:context:completion:"
- "addObject:"
- "alertControllerWithTitle:message:preferredStyle:"
- "alertIdentifier"
- "alertWithIdentifierDidAppear:"
- "alertWithIdentifierDidDisappear:"
- "alertWithIdentifierWasActivated:"
- "alertWithIdentifierWasActivated:userInfo:"
- "alertWithIdentifierWasEnqueued:"
- "autorelease"
- "backgroundAccessQueue"
- "boolValue"
- "class"
- "clientMessengerWithIdentifier:"
- "conformsToProtocol:"
- "connectionWillBeInterruptedForClientWithIdentifier:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d24@0:8@\"NSString\"16"
- "d24@0:8@16"
- "d28@0:8@\"UIViewController\"16B24"
- "d28@0:8@16B24"
- "debugDescription"
- "delayForDequeuingAlertWithIdentifier:"
- "description"
- "desiredWindowLevelForAlertWithIdentifier:"
- "desiredWindowLevelForContentViewController:userInteractionEnabled:"
- "dictionaryWithObject:forKey:"
- "dismissViewControllerAnimated:completion:"
- "doubleValue"
- "externalDisplaySceneConnected:"
- "externalDisplaySceneConnected:forSceneClientIdentifier:"
- "externalDisplaySceneDisconnected:"
- "externalDisplaySceneDisconnected:forSceneClientIdentifier:"
- "hash"
- "hideAlertWithIdentifier:forService:"
- "i24@0:8@\"NSString\"16"
- "i24@0:8@16"
- "imageWithData:"
- "indexOfObject:"
- "integerValue"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSafeToProcessMessageFromUnentitledProcessWithIdentifier:"
- "isScreenLockedWithPasscode:"
- "length"
- "localizedUppercaseString"
- "mainDisplaySceneConnected:"
- "messageWithIdentifierRequiresWritingBlock:"
- "messageWithIdentifierShouldBeProcessedAsynchronously:"
- "numberWithInteger:"
- "objectAtIndex:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "possibleRequiredEntitlementsForProcessingMessageWithIdentifier:"
- "presentViewController:animated:completion:"
- "processInitializationMessage:"
- "processMessage:withIdentifier:fromClientWithIdentifier:error:"
- "processMessage:withIdentifier:fromClientWithIdentifier:pid:error:"
- "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:completion:"
- "processMessageAsynchronously:withIdentifier:fromClientWithIdentifier:pid:completion:"
- "release"
- "remoteSceneDidHandleHomeGesture:"
- "removeAllObjects"
- "removeContentViewController:withUserInteractionEnabled:forService:"
- "requiredEntitlementForProcessingMessageWithIdentifier:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "server"
- "serviceTypeForClientWithIdentifier:"
- "serviceWasFullyInitialized"
- "set"
- "setAlertIdentifier:"
- "sharedDisplayManager"
- "sharedInstance"
- "shouldPreventAutorotatingAllContentViewControllers"
- "showAlertWithText:subtitleText:iconImage:type:priority:duration:forService:"
- "stringWithFormat:"
- "styleProviderForAlertWithIdentifier:"
- "superclass"
- "unsignedIntegerValue"
- "v16@0:8"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"UIWindowScene\"16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
- "v32@0:8@\"UIWindowScene\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v48@0:8@\"NSDictionary\"16Q24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16Q24@32@?40"
- "v52@0:8@\"NSDictionary\"16Q24@\"NSString\"32i40@?<v@?@\"NSDictionary\"@\"NSError\">44"
- "v52@0:8@16Q24@32i40@?44"
- "zone"

```
