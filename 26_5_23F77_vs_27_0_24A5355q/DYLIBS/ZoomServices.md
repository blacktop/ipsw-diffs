## ZoomServices

> `/System/Library/PrivateFrameworks/ZoomServices.framework/ZoomServices`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x57e0
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_methlist: 0x70c
+3229.1.6.0.0
+  __TEXT.__text: 0x54f4
+  __TEXT.__objc_methlist: 0x6f4
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__cstring: 0x806
+  __TEXT.__cstring: 0x783
   __TEXT.__oslogstring: 0x4c
-  __TEXT.__unwind_info: 0x1e8
-  __TEXT.__objc_classname: 0x91
-  __TEXT.__objc_methname: 0x1819
-  __TEXT.__objc_methtype: 0x4ae
-  __TEXT.__objc_stubs: 0xee0
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x218
+  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x210
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a0
+  __DATA_CONST.__objc_selrefs: 0x668
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x268
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x720
+  __DATA_CONST.__got: 0xe8
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0x680
   __AUTH_CONST.__objc_const: 0x640
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x120
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x18
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6DE4538F-9048-3F91-B4B9-C72E3AB5401C
-  Functions: 139
-  Symbols:   616
-  CStrings:  438
+  UUID: 2AB0B7BB-41A3-3EAE-9365-AF7486F64E76
+  Functions: 134
+  Symbols:   596
+  CStrings:  123
 
Symbols:
+ GCC_except_table50
+ _OBJC_CLASS_$_PDRRegistry
+ ___block_literal_global.732
+ ___block_literal_global.745
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$getActivePairedDeviceIncludingAltAccount
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x8
+ _sharedInstance.onceToken.17
- +[ZoomServices sharedInstance].cold.1
- -[ZoomServices notifyZoomIdleSlugOpacityChangedTo:]
- -[ZoomServices shouldSuppressKeyCommandHUD]
- GCC_except_table56
- _AXPerformSafeBlock
- _AXSafeClassFromString
- _NRDevicePropertyIsArchived
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _ZOTMainScreenSize.cold.1
- _ZWAttributeKeyShouldSuppressKeyCommandHUD
- ___41-[ZoomServices _handleChangedAttributes:]_block_invoke
- ___block_literal_global.474
- ___block_literal_global.729
- ___block_literal_global.742
- __shouldSuppressKeyCommandHUD
- __shouldSuppressKeyCommandHUDByDisplayID
- _objc_msgSend$activePairedDeviceSelectorBlock
- _objc_msgSend$dismissOrCancelHUDPresentationIfNeeded
- _objc_msgSend$getAllDevicesWithArchivedAltAccountDevicesMatching:
- _objc_msgSend$initWithUUIDString:
- _objc_msgSend$safeValueForKey:
- _objc_msgSend$valueForProperty:
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x23
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "1fd8e157-2b7c-45b6-b939-ffb8be14e27f"
- "@\"AXAccessQueue\"32@0:8@\"AXUIClient\"16Q24"
- "@\"AXUIClient\""
- "@\"NSDictionary\"48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32^@40"
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8I16"
- "@24@0:8:16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@28@0:8@?16I24"
- "@32@0:8:16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16Q24"
- "@36@0:8@16I24@?28"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24Q32^@40"
- "@?"
- "@?16@0:8"
- "AXUIClientDelegate"
- "AXZoomListenerContainer"
- "B"
- "B16@0:8"
- "B20@0:8I16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8d16"
- "B28@0:8@16I24"
- "B32@0:8@\"AXUIClient\"16Q24"
- "B32@0:8@16Q24"
- "B56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "B60@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48I56"
- "B64@0:8q16{CGRect={CGPoint=dd}{CGSize=dd}}24I56I60"
- "B96@0:8q16{CGRect={CGPoint=dd}{CGSize=dd}}24I56{CGRect={CGPoint=dd}{CGSize=dd}}60I92"
- "NSObject"
- "PrimaryClientOnly"
- "Q16@0:8"
- "T#,R"
- "T@\"AXUIClient\",&,N,V_zoomWindowClient"
- "T@\"NSString\",&,N,Videntifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@?,C,N,Vhandler"
- "TB,N,GisShowingZoomLens,V_showingZoomLens"
- "TB,N,V_inUnitTestMode"
- "TB,N,V_registeredForZoomAttributeListeners"
- "TB,N,V_registeredForZoomListener"
- "TB,N,V_shouldRegisterForZoomListeners"
- "TB,N,V_systemAppReady"
- "TB,N,V_triedToShowLensBeofreSBReady"
- "TB,R,N,GisShowingZoomLens"
- "TQ,R"
- "Td,N"
- "UIKeyShortcutHUDService"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "ZWAttributeKeyShouldSuppressKeyCommandHUD"
- "ZoomServices"
- "ZoomServicesGreyCommandInfo"
- "ZoomServicesKeyboardManager"
- "^{_NSZone=}16@0:8"
- "_applicationDidResume:"
- "_applicationWillSuspend:"
- "_checkSpringBoardStarted"
- "_handleChangedAttributes:"
- "_inUnitTestMode"
- "_isAllowedMagnifierClient"
- "_isPrimaryZoomWindowClient"
- "_pairedDevice"
- "_panWithDirection:onDisplay:"
- "_registeredForZoomAttributeListeners"
- "_registeredForZoomListener"
- "_shouldRegisterForZoomListeners"
- "_showingZoomLens"
- "_systemAppReady"
- "_triedToShowLensBeofreSBReady"
- "_zoomAttributeListeners"
- "_zoomChanged:"
- "_zoomListeners"
- "_zoomWindowClient"
- "activePairedDeviceSelectorBlock"
- "activeZoomMode"
- "activeZoomModeOnDisplay:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "allKeys"
- "allValues"
- "appActivationAnimationStartDelay"
- "appDeactivationAnimationStartDelay"
- "appSwitcherRevealAnimationStartDelay"
- "array"
- "autoPanZoomUsingLocation:withPanningStyle:"
- "autoPanZoomUsingLocation:withPanningStyle:onDisplay:"
- "autorelease"
- "ax_removeObjectsFromArrayUsingBlock:"
- "boolValue"
- "bundleIdentifier"
- "callStackSymbols"
- "class"
- "conformsToProtocol:"
- "connectionWithServiceWasInterruptedForUserInterfaceClient:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d16@0:8"
- "d20@0:8I16"
- "dealloc"
- "debugDescription"
- "defaultActions"
- "defaultCenter"
- "defaultCustomizeGestures"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "dismissOrCancelHUDPresentationIfNeeded"
- "displays"
- "doubleValue"
- "firstObject"
- "floatValue"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "getCurrentZoomFrameOnDisplay:"
- "getCurrentZoomLevelOnDisplay:"
- "getLastSpeakUnderFingerPhrase"
- "handler"
- "hash"
- "hideZoomLens"
- "identifier"
- "idleSlugOpacity"
- "inStandbyMode"
- "inStandbyModeOnDisplay:"
- "inUnitTestMode"
- "indexOfObjectPassingTest:"
- "init"
- "initWithIdentifier:serviceBundleName:"
- "initWithUUIDString:"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMagnifierVisibleWithCompletion:"
- "isMemberOfClass:"
- "isProxy"
- "isShowingZoomLens"
- "isZoomGreyFeatureOn"
- "keyCode"
- "keyDown"
- "keyInfo"
- "keyboardCommandForEvent:"
- "launchMagnifierApp"
- "magnifierUsageCount"
- "mainAccessQueue"
- "mainBundle"
- "modifierState"
- "nameForAction:"
- "notifyZoomAppActivationAnimationDidFinish"
- "notifyZoomAppActivationAnimationWillBegin"
- "notifyZoomAppDeactivationAnimationWillBegin"
- "notifyZoomAppDidBecomeActive:keyboardFrameIfVisible:"
- "notifyZoomAppDidEnterBackground:"
- "notifyZoomAppSwitcherRevealAnimationWillBegin"
- "notifyZoomCarouselLockBegan"
- "notifyZoomCarouselLockEnded"
- "notifyZoomDeviceWasUnlocked"
- "notifyZoomDeviceWillWake"
- "notifyZoomDockPositionWasChangedInSettingsTo:"
- "notifyZoomDragWillEnd"
- "notifyZoomDragWillStart"
- "notifyZoomFluidSwitcherGestureDidFinish"
- "notifyZoomFluidSwitcherGestureDidFinishWithDock"
- "notifyZoomFluidSwitcherGestureWillBegin"
- "notifyZoomFocusDidChangeWithType:rect:contextId:displayId:"
- "notifyZoomFocusDidChangeWithType:rect:contextId:keyboardFrame:displayId:"
- "notifyZoomHomeButtonWasPressed"
- "notifyZoomIdleSlugOpacityChangedTo:"
- "notifyZoomKeyboardDidHideInAppWithBundleID:displayID:"
- "notifyZoomKeyboardWillBecomeVisibleWithFrame:inAppWithBundleID:displayID:"
- "notifyZoomKeyboardWillHideInAppWithBundleID:displayID:"
- "notifyZoomLensModeWasChangedInSettingsTo:"
- "notifyZoomLockButtonWasPressed"
- "notifyZoomReturnedToClockFaceAtIdle"
- "notifyZoomSOSMedicalIDShown"
- "notifyZoomWillHideBrailleInputUI"
- "notifyZoomWillShowBrailleInputUI"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "panDown"
- "panDownOnDisplay:"
- "panLeft"
- "panLeftOnDisplay:"
- "panRight"
- "panRightOnDisplay:"
- "panUp"
- "panUpOnDisplay:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processIdentifier"
- "processInfo"
- "q24@0:8@16"
- "reachabilityScaleFactor"
- "registerForCoalescedZoomAttributesWithChangedHandler:"
- "registerForCoalescedZoomAttributesWithChangedHandler:onDisplay:"
- "registerForZoomAttributes:onDisplay:updatesImmediatelyWithChangedHandler:"
- "registerForZoomAttributes:updatesImmediatelyWithChangedHandler:"
- "registerInterestInZoomAttributes"
- "registeredForZoomAttributeListeners"
- "registeredForZoomListener"
- "release"
- "removeCoalescedZoomAttributesChangedHandler:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObserver:"
- "removeZoomAttributesChangedHandler:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "safeValueForKey:"
- "self"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "sendSynchronousMessage:withIdentifier:error:"
- "server"
- "set"
- "setDelegate:"
- "setHandler:"
- "setIdentifier:"
- "setInUnitTestMode:"
- "setMagnifierEnabled:changeTripleClickMenu:"
- "setMagnifierUsageCount:"
- "setObject:forKeyedSubscript:"
- "setRegisteredForZoomAttributeListeners:"
- "setRegisteredForZoomListener:"
- "setShouldRegisterForZoomListeners:"
- "setShowingZoomLens:"
- "setSystemAppReady:"
- "setTriedToShowLensBeofreSBReady:"
- "setZoomLevel:"
- "setZoomLevel:onDisplay:"
- "setZoomWindowClient:"
- "sharedHUDService"
- "sharedInstance"
- "shouldRegisterForZoomListeners"
- "shouldSuppressKeyCommandHUD"
- "showMagnifier"
- "showZoomLens"
- "showingZoomLens"
- "startMagnifier"
- "startMagnifierChangeTripleClickMenu:"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "superclass"
- "supportsCapability:"
- "symbolNameForAction:"
- "systemAppReady"
- "toggleZoomMenu"
- "translateKeycode"
- "triedToShowLensBeofreSBReady"
- "unsignedIntValue"
- "userInterfaceClient:accessQueueForProcessingMessageWithIdentifier:"
- "userInterfaceClient:messageFromServerForWithIdentifierShouldBeProcessedAsynchronously:"
- "userInterfaceClient:messageWithIdentifierRequiresWritingBlock:"
- "userInterfaceClient:processMessageFromServer:withIdentifier:error:"
- "userInterfaceClient:processMessageFromServerAsynchronously:withIdentifier:completion:"
- "userInterfaceClient:willActivateUserInterfaceServiceWithInitializationMessage:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@\"AXUIClient\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v28@0:8@16I24"
- "v28@0:8d16I24"
- "v32@0:8@\"AXUIClient\"16@\"NSMutableDictionary\"24"
- "v32@0:8@16@24"
- "v40@0:8{CGPoint=dd}16Q32"
- "v44@0:8{CGPoint=dd}16Q32I40"
- "v48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "valueForProperty:"
- "zone"
- "zoomAdjustZoomLevelKbShortcutEnabled"
- "zoomFrame"
- "zoomFrameOnDisplay:"
- "zoomKeyboardShortcutsEnabled"
- "zoomLevelOnDisplay:"
- "zoomPanZoomKbShortcutEnabled"
- "zoomPreferredCurrentLensMode"
- "zoomResizeZoomWindowKbShortcutEnabled"
- "zoomScrollWheelKbShortcutEnabled"
- "zoomSwitchZoomModeKbShortcutEnabled"
- "zoomTempToggleZoomKbShortcutEnabled"
- "zoomToggleZoomKbShortcutEnabled"
- "zoomWindowClient"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}20@0:8I16"

```
