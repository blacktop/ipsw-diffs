## AXRuntime

> `/System/Library/PrivateFrameworks/AXRuntime.framework/Versions/A/AXRuntime`

```diff

-3148.7.15.0.0
-  __TEXT.__text: 0x42e38
+3148.15.11.1.0
+  __TEXT.__text: 0x42e50
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0x2cbc
+  __TEXT.__objc_methlist: 0x30ec
   __TEXT.__const: 0x410
   __TEXT.__cstring: 0x553b
-  __TEXT.__oslogstring: 0xe38
-  __TEXT.__gcc_except_tab: 0x670
+  __TEXT.__oslogstring: 0xe43
+  __TEXT.__gcc_except_tab: 0x67c
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0xbb
-  __TEXT.__unwind_info: 0x1070
+  __TEXT.__unwind_info: 0x1118
   __TEXT.__objc_classname: 0x2d3
   __TEXT.__objc_methname: 0x6d3b
   __TEXT.__objc_methtype: 0x119e
   __TEXT.__objc_stubs: 0x4da0
-  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__got: 0x298
   __DATA_CONST.__const: 0x820
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1df8
+  __DATA_CONST.__objc_selrefs: 0x1e78
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xb8
   __AUTH_CONST.__auth_got: 0x8d0
   __AUTH_CONST.__const: 0x1310
   __AUTH_CONST.__cfstring: 0x4ca0
-  __AUTH_CONST.__objc_const: 0x39b8
+  __AUTH_CONST.__objc_const: 0x31c8
   __AUTH_CONST.__objc_intobj: 0x1560
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D1AF4288-1390-3559-A473-CD9CB5B8D460
-  Functions: 1556
-  Symbols:   3594
+  UUID: 2F6A7D83-977F-3627-A208-7D7B7BFC238B
+  Functions: 1561
+  Symbols:   3650
   CStrings:  2903
 
Symbols:
+ +[AXElement systemWideElement].cold.1
+ +[AXElementTransactionLogging sharedLogger].cold.1
+ +[AXPidSuspensionInfo shared].cold.1
+ +[AXProfileDatabase sharedDatabase].cold.1
+ +[AXRemoteElement initialize].cold.1
+ +[AXSimpleRuntimeManager sharedManager].cold.1
+ -[AXElement setAssistiveTechFocused:].cold.1
+ -[AXNotificationObserver _didObserveNotification:notificationData:].cold.1
+ -[AXRemoteElement _getRemoteValuesOffMainThread:].cold.1
+ -[AXUIElement _elementsWithParameter:parameters:prefetchAttributes:].cold.1
+ -[NSObject(AXPropertyListCoersion) _axRecursivelyPropertyListCoercedRepresentationWithError:].cold.1
+ AXAttributeForXCAttribute.cold.1
+ AXBroadcastNotificationToAllClients.cold.1
+ AXGetCurrentSerializationStyle.cold.1
+ AXObserverAddNotification.cold.1
+ AXObserverAddNotification.cold.2
+ AXObserverRemoveNotification.cold.1
+ AXObserverRemoveNotification.cold.2
+ AXProcessCanContactSystemWideServer.cold.1
+ AXSerializeCFType3.cold.2
+ AXSerializeWrapper.cold.2
+ AXSetCurrentSerializationStyle.cold.1
+ AXUIElementCopyAttributeValueRecursive.cold.1
+ AXUIElementCopyAttributeValueRecursive.cold.2
+ AXUIElementCopyMultipleAttributeValues.cold.1
+ AXUIElementCopyMultipleAttributeValues.cold.2
+ AXUIElementCopyParameterizedAttributeValueRecursive.cold.1
+ AXUIElementCopyParameterizedAttributeValueRecursive.cold.2
+ AXUIElementPerformAction.cold.1
+ AXUIElementPerformAction.cold.2
+ AXUIElementPerformFencedActionWithValue.cold.1
+ AXUIElementPerformFencedActionWithValue.cold.2
+ AXUIElementRegisterForApplicationDeath.cold.1
+ AXUIElementSetAttributeValue.cold.1
+ AXUIElementSetAttributeValue.cold.2
+ AXUIElementSharedSystemApp.cold.1
+ AXUIElementSharedSystemWide.cold.1
+ AXUnserializeCFType3.cold.2
+ AXUnserializeWrapper.cold.1
+ AXUnserializeWrapper.cold.2
+ AXXCAttributeForAttribute.cold.1
+ _AXAddNotificationObserver.cold.1
+ _AXAddToElementCache.cold.1
+ _AXBroadcastEventProcessNotification.cold.1
+ _AXDetermineRequestingClient.cold.2
+ _AXInitializeElementCache.cold.1
+ _AXInitializeObserverAccess.cold.1
+ _AXNotificationObserverClientDied.cold.1
+ _AXRemoveNotificationObserver.cold.1
+ _AXUIElementCopyElementAtPositionWithParams.cold.1
+ _AXUIElementCopyElementAtPositionWithParams.cold.2
+ _AXUIElementPostNotification.cold.1
+ _AXUIScreenConvertToCAScreen.cold.1
+ _OUTLINED_FUNCTION_2
+ __MergedGlobals
+ ___AXAddToElementCache_block_invoke.cold.2
+ getSerializeMethodForType.cold.1
- _AXCacheHelper
- __ElementCache
CStrings:
+ "Sending notification to client: %d, %{sensitive}@"
- "Sending notification to client: %d, %@"

```
