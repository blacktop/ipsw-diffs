## AccessibilityFoundation

> `/System/Library/PrivateFrameworks/AccessibilitySupport.framework/Versions/A/Frameworks/AccessibilityFoundation.framework/Versions/A/AccessibilityFoundation`

```diff

-387.5.2.0.0
-  __TEXT.__text: 0x48a44
+387.7.3.0.0
+  __TEXT.__text: 0x48a24
   __TEXT.__auth_stubs: 0x1760
-  __TEXT.__objc_methlist: 0x64a8
+  __TEXT.__objc_methlist: 0x6934
   __TEXT.__const: 0x290
   __TEXT.__cstring: 0x4b69
   __TEXT.__oslogstring: 0xd3e
-  __TEXT.__gcc_except_tab: 0x308
+  __TEXT.__gcc_except_tab: 0x30c
   __TEXT.__dlopen_cstrs: 0x117
   __TEXT.__dof_Accessibi: 0x609
-  __TEXT.__unwind_info: 0x1530
+  __TEXT.__unwind_info: 0x1568
   __TEXT.__objc_classname: 0x784
   __TEXT.__objc_methname: 0x103f4
   __TEXT.__objc_methtype: 0x2832
-  __TEXT.__objc_stubs: 0x9360
+  __TEXT.__objc_stubs: 0x9380
   __DATA_CONST.__got: 0x5f0
   __DATA_CONST.__const: 0x780
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d38
+  __DATA_CONST.__objc_selrefs: 0x3de8
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0xbc0
   __AUTH_CONST.__const: 0x1070
   __AUTH_CONST.__cfstring: 0x6760
-  __AUTH_CONST.__objc_const: 0xb560
+  __AUTH_CONST.__objc_const: 0xace8
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x168

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F555AED8-1D6F-3BF1-97C5-AD061DB327AD
-  Functions: 2512
-  Symbols:   5659
+  UUID: 3F91C3CE-4901-34E4-B8A9-C7DC1A3C1D08
+  Functions: 2554
+  Symbols:   5719
   CStrings:  4785
 
Symbols:
+ +[AXFApplicationInfoProvider shared].cold.1
+ +[AXFDispatchQueue globalQueueWithQualityOfService:].cold.1
+ +[AXFDispatchQueue globalQueueWithQualityOfService:].cold.2
+ +[AXFDispatchQueue globalQueueWithQualityOfService:].cold.3
+ +[AXFDispatchQueue globalQueueWithQualityOfService:].cold.4
+ +[AXFDispatchQueue globalQueueWithQualityOfService:].cold.5
+ +[AXFDispatchQueue mainQueue].cold.1
+ +[AXFObserverManagerIPC observerThread].cold.1
+ +[AXFScreenManager keyPathsForValuesAffectingMainScreen].cold.1
+ +[AXFTextPosition invalidPosition].cold.1
+ +[AXFTextRange invalidRange].cold.1
+ +[AXFUIElement _shouldCreateInstanceForApplicationRef:applicationProcessIdentifier:applicationProcessSerialNumber:applicationIdentifier:].cold.1
+ +[AXFUIElement _uiElementAtCoordinate:applicationElementRef:includeIgnored:].cold.2
+ +[AXFUIElement _uiElementAtCoordinate:applicationElementRef:includeIgnored:].cold.3
+ +[AXFUIElement _uiElementAtCoordinate:applicationElementRef:includeIgnored:].cold.4
+ +[AXFUIElement systemWideElement].cold.1
+ +[NSCharacterSet(AXFAdditions) axf_greekCharacterSet].cold.1
+ +[NSCharacterSet(AXFAdditions) axf_tabCharacterSet].cold.1
+ +[NSCharacterSet(AXFAdditions) axf_whitespaceExcludingTabCharacterSet].cold.1
+ +[_SCRUIElementCache _attributesForAllPopulationLevels].cold.1
+ -[AXFComposedCharacter copyUnicodeDescriptionString].cold.1
+ -[AXFFaultingElementArray nilSentinel].cold.1
+ -[AXFObserver initWithTarget:selector:queue:].cold.1
+ -[AXFUIElement _copyAttributeNames].cold.1
+ -[AXFUIElement _copyParameterizedAttributeNames].cold.1
+ -[AXFUIElement _hashLabelWithElementsUsed:].cold.1
+ -[AXFUIElement _nonPromotableAttributesCatalyst].cold.1
+ -[AXFUIElement _nonPromotableAttributesMac].cold.1
+ -[AXFUIElement descriptionForAction:].cold.1
+ -[AXFUIElement isPromotable].cold.1
+ -[AXFUIElement pointForAXAttribute:].cold.1
+ -[AXFWindowManagerController _enumerateWindowObserverNotifications:].cold.1
+ AXEGetLog.cold.1
+ AXFDateTimeComponentDescription.cold.1
+ AXFDateTimeDescription.cold.1
+ AXFDateTimeDescription.cold.2
+ AXFGetLog.cold.1
+ AXKGetLog.cold.1
+ AXVGetLog.cold.1
+ KAGetLog.cold.1
+ SCGetLog.cold.1
+ VOGetLog.cold.1
+ ZMGetLog.cold.1
+ _AXFAccessibilityOrientationForString.cold.1
+ _AXFAccessibilityRulerMarkerTypeForString.cold.1
+ _AXFAccessibilitySortDirectionForString.cold.1
+ _AXFAccessibilityUnitsForString.cold.1
+ _AXFEnsureOutgoingRect.cold.1
+ _AXFStringForAccessibilityOrientation.cold.1
+ _AXFStringForAccessibilityRulerMarkerType.cold.1
+ _AXFStringForAccessibilitySortDirection.cold.1
+ _AXFStringForAccessibilityUnits.cold.1
+ _AXFUIElementConvertScreenSpaceAutomatically.cold.1
+ _AXFUIElementCopyActionNames.cold.1
+ _AXFUIElementCopyAttributeValue.cold.1
+ _AXFUIElementCopyAttributeValues.cold.1
+ _AXFUIElementCopyMultipleAttributeValues.cold.1
+ _AXFUIElementCopyParameterizedAttributeValue.cold.1
+ _objc_msgSend$screenLocked
+ applicationIdentifierToObserverIDMap.cold.1

```
