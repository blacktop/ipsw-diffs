## WebProcess

> `/System/Library/AccessibilityBundles/WebProcess.axbundle/WebProcess`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x1ee8
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_methlist: 0x238
+3036.2.0.0.0
+  __TEXT.__text: 0x1a18
+  __TEXT.__objc_methlist: 0x220
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x4b6
-  __TEXT.__oslogstring: 0x48
-  __TEXT.__unwind_info: 0x130
-  __TEXT.__objc_classname: 0xd1
-  __TEXT.__objc_methname: 0xb47
-  __TEXT.__objc_methtype: 0xca
-  __TEXT.__objc_stubs: 0xa20
-  __DATA_CONST.__got: 0x80
+  __TEXT.__cstring: 0x49f
+  __TEXT.__oslogstring: 0x16
+  __TEXT.__unwind_info: 0x120
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x348
+  __DATA_CONST.__objc_selrefs: 0x320
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0x68
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x3e0
+  __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0x360
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__common: 0x8
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x1e0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FAD4609E-5E48-30DC-8095-285AEDACE9D1
-  Functions: 61
-  Symbols:   327
-  CStrings:  209
+  UUID: C2AFB6D4-0E19-321E-B1CF-DD682C589B67
+  Functions: 56
+  Symbols:   313
+  CStrings:  77
 
Symbols:
+ ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke.404
+ ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_2.409
+ ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_3.419
+ ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_4.423
+ ___block_literal_global.10
+ ___block_literal_global.363
+ ___block_literal_global.372
+ ___block_literal_global.381
+ ___block_literal_global.394
+ ___block_literal_global.397
+ ___block_literal_global.400
+ ___block_literal_global.403
+ ___block_literal_global.407
+ ___block_literal_global.412
+ ___block_literal_global.422
+ ___block_literal_global.426
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
- +[AXWebProcessGlue accessibilityInitializeBundle].cold.1
- -[WKAccessibilityWebPageObjectAccessibility _axUnarchivedTokenForData:]
- -[WKAccessibilityWebPageObjectAccessibility _axUnarchivedTokenForData:].cold.1
- -[WKAccessibilityWebPageObjectAccessibility setRemoteTokenData:]
- _AXLogAppAccessibility
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSKeyedUnarchiver
- _OBJC_CLASS_$_NSSet
- ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke.383
- ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_2.388
- ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_3.398
- ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_4.402
- ___40+[AXWebProcessGlue _initializeAXRuntime]_block_invoke_5.cold.1
- ___block_literal_global.342
- ___block_literal_global.351
- ___block_literal_global.360
- ___block_literal_global.370
- ___block_literal_global.373
- ___block_literal_global.376
- ___block_literal_global.379
- ___block_literal_global.382
- ___block_literal_global.386
- ___block_literal_global.401
- ___block_literal_global.405
- __os_log_error_impl
- _objc_msgSend$_axUnarchivedTokenForData:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
- _objc_retain_x21
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8q16"
- "@32@0:8q16@24"
- "@32@0:8{CGPoint=dd}16"
- "AXWebProcessGlue"
- "B16@0:8"
- "B28@0:8Q16B24"
- "B32@0:8Q16@24"
- "B32@0:8i16@20I28"
- "NSData"
- "Problem with unarchiving remote token data: %@ %@"
- "SafeCategory"
- "UIAccessibilityLoaderForWebKit"
- "^v16@0:8"
- "__WKAccessibilityWebPageObjectAccessibility_super"
- "__WKNSObjectAccessibility_super"
- "_accessibilityApplication"
- "_accessibilityClippingFrame"
- "_accessibilityFindDescendant:"
- "_accessibilityFirstDescendant"
- "_accessibilityFirstElementForFocusForRemoteElement"
- "_accessibilityHostPid"
- "_accessibilityInitializeRuntimeOverrides"
- "_accessibilityInitializeSubclassRuntimeOverrides"
- "_accessibilityIsVisibleByCompleteHitTest"
- "_accessibilityIsVisibleByCompleteHitTest:"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityMoveFocusWithHeading:byGroup:"
- "_accessibilityMoveFocusWithHeading:toElementMatchingQuery:"
- "_accessibilityPerformValidations:"
- "_accessibilityResponderElement"
- "_accessibilityResponderElementForFocus"
- "_accessibilitySetRetainedValue:forKey:"
- "_accessibilityTextViewTextOperationResponder"
- "_accessibilityUnignoredDescendant"
- "_accessibilityUnregister"
- "_accessibilityValueForKey:"
- "_axCachedRootObject"
- "_axListenForRemoteElement"
- "_axRemoteElementRegistered:"
- "_axSetCachedRootObject:"
- "_axUnarchivedTokenForData:"
- "_disableCaching"
- "_enableCaching"
- "_initializeAXRuntime"
- "_initializeRemoteElement:"
- "_initializeRootIfNecessary"
- "_iosAccessibilityAttributeValue:"
- "_iosAccessibilityAttributeValue:forParameter:"
- "_iosAccessibilityPerformAction:withValue:fencePort:"
- "_iosAccessibilitySetValue:forAttribute:"
- "_isSerializableAccessibilityElement"
- "_performInitialAccessibilityBundleLoad:monitorForFutureLoadEvents:trackingMode:"
- "accessibilityContainer"
- "accessibilityElementAtIndex:"
- "accessibilityElements"
- "accessibilityFrame"
- "accessibilityInitializeBundle"
- "accessibilityRemoteSubstituteChildren:"
- "addObserver:selector:name:object:"
- "arrayWithObjects:count:"
- "bundleWithIdentifier:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "defaultCenter"
- "firstObject"
- "i16@0:8"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isEqual:"
- "lastObject"
- "localizedStringForKey:value:table:"
- "objectAtIndex:"
- "objectForKey:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "pointerValue"
- "postNotificationName:object:"
- "registerRemoteElement:remotePort:"
- "remoteChildrenDelegate"
- "remoteElementForBlock:"
- "remotePid"
- "remoteTokenData"
- "safeCGRectForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeDictionaryForKey:"
- "safeValueForKey:"
- "setAccessibilityContainer:"
- "setApplicationElementCallback:"
- "setAttributeCallback:"
- "setClientObserverCallback:"
- "setDebugBuild:"
- "setHitTestCallback:"
- "setOnClientSide:"
- "setOutgoingValuePreprocessor:"
- "setOverrideProcessName:"
- "setParameterizedAttributeCallback:"
- "setPerformActionCallback:"
- "setRemoteChildrenDelegate:"
- "setRemoteTokenData:"
- "setSetAttributeCallback:"
- "setValidationTargetName:"
- "setWithObjects:"
- "sharedInstance"
- "sharedManager"
- "start"
- "unarchivedObjectOfClasses:fromData:error:"
- "unregister"
- "unsignedIntegerValue"
- "userInfo"
- "uuid"
- "v16@0:8"
- "v24@0:8@16"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:isKindOfClass:"
- "valueWithPointer:"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
