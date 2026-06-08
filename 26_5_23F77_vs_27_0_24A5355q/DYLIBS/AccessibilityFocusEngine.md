## AccessibilityFocusEngine

> `/System/Library/PrivateFrameworks/AccessibilityFocusEngine.framework/AccessibilityFocusEngine`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x3c34
-  __TEXT.__auth_stubs: 0x350
+3229.1.6.0.0
+  __TEXT.__text: 0x3660
   __TEXT.__objc_methlist: 0x300
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__cstring: 0x104
+  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__cstring: 0x106
   __TEXT.__oslogstring: 0x481
-  __TEXT.__unwind_info: 0x158
-  __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0xc9c
-  __TEXT.__objc_methtype: 0x1e0
-  __TEXT.__objc_stubs: 0xd40
-  __DATA_CONST.__got: 0x70
+  __TEXT.__unwind_info: 0x128
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3b8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x338
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x60

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B28DC2C-98DB-3237-9686-DA2F3E5E327B
-  Functions: 95
-  Symbols:   404
-  CStrings:  207
+  UUID: A2FE1B51-EAB4-3876-A908-C04A926436D1
+  Functions: 71
+  Symbols:   357
+  CStrings:  39
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x4
+ _objc_retain_x8
- -[AXFocusManager _currentFocusContainers].cold.1
- -[AXFocusManager _moveFocusContainerFocusInDirection:].cold.1
- -[AXFocusManager _moveFocusContainerFocusInDirection:].cold.2
- -[AXFocusManager _moveFocusContainerFocusInDirection:].cold.3
- -[AXFocusManager _moveFocusContainerFocusInDirection:].cold.4
- -[AXFocusManager _moveFocusInRemoteElement:withHeading:byGroup:].cold.1
- -[AXFocusManager _moveFocusInRemoteElement:withHeading:byGroup:].cold.2
- -[AXFocusManager _moveFocusWithHeading:byGroup:queryString:shouldWrap:].cold.1
- -[AXFocusManager _moveFocusWithHeading:byGroup:shouldWrap:].cold.1
- -[AXFocusManager _moveFocusWithHeading:byGroup:shouldWrap:].cold.2
- -[AXFocusManager _moveFocusWithHeading:byGroup:shouldWrap:].cold.3
- -[AXFocusManager _moveFocusWithHeading:byGroup:shouldWrap:].cold.4
- -[AXFocusManager _recursiveMoveFocusInFocusContainer:withHeading:byGroup:].cold.1
- -[AXFocusManager _recursiveMoveFocusInFocusContainer:withHeading:byGroup:].cold.2
- -[AXFocusManager _recursiveMoveFocusInFocusContainer:withHeading:byGroup:].cold.3
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- ___59-[AXFocusManager _moveFocusWithHeading:byGroup:shouldWrap:]_block_invoke.cold.1
- ___59-[AXFocusManager _moveFocusWithHeading:byGroup:shouldWrap:]_block_invoke.cold.2
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x27
CStrings:
- ".cxx_destruct"
- "@\"AXElement\""
- "@\"NSHashTable\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8q16"
- "AXElementNamesItem"
- "AXFocusEngine"
- "AXFocusManager"
- "B16@0:8"
- "B24@0:8@16"
- "B28@0:8Q16B24"
- "B32@0:8Q16@24"
- "B32@0:8Q16B24B28"
- "B36@0:8@16Q24B32"
- "B40@0:8@16Q24@32"
- "Q24@0:8@16"
- "T@\"AXElement\",&,N,V_focusContainerForSuccessfulTypeaheadMovement"
- "T@\"AXElement\",R,N"
- "T@\"NSHashTable\",&,N,V_observers"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_movementQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_observersQueue"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_typeaheadString"
- "T@\"NSString\",R,N"
- "TB,R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
- "T{CGSize=dd},R,N"
- "T{os_unfair_lock_s=I},N,V_observersLock"
- "_currentFocusContainers"
- "_enumerateObservers:"
- "_focusContainerForSuccessfulTypeaheadMovement"
- "_focusOnFocusContainer:"
- "_handleFailedFocusMovementWithHeading:byGroup:"
- "_indexOfTypeaheadPIDInFocusContainers:"
- "_moveFocusContainerFocusInDirection:"
- "_moveFocusInFocusContainer:withHeading:queryString:"
- "_moveFocusInRemoteElement:withHeading:byGroup:"
- "_moveFocusWithHeading:byGroup:queryString:shouldWrap:"
- "_moveFocusWithHeading:byGroup:shouldWrap:"
- "_moveToElementWithHeading:queryString:"
- "_movementQueue"
- "_observers"
- "_observersLock"
- "_observersQueue"
- "_recursiveMoveFocusInFocusContainer:withHeading:byGroup:"
- "_recursiveMoveFocusInFocusContainer:withHeading:queryString:"
- "_typeaheadString"
- "_verifyPIDForTypeahead"
- "addObject:"
- "addObserver:"
- "allObjects"
- "application"
- "applicationForHostFocusSystem"
- "applicationIsExtension"
- "arrayByAddingObject:"
- "arrayWithAXAttribute:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "axArrayByIgnoringNilElementsWithCount:"
- "axSafelyAddObjectsFromArray:"
- "boolWithAXAttribute:"
- "bundleId"
- "containsObject:"
- "containsString:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentApplication"
- "currentApplications"
- "currentElement"
- "currentFocusContainer"
- "currentFocusElement"
- "didFocus"
- "disableFocus"
- "elementForAttribute:"
- "elementForAttribute:parameter:"
- "elementForAttribute:shouldFetchAttributes:"
- "elementForRemoteFocusSystem"
- "elementFrame"
- "elementLabelContainerSize"
- "elementName"
- "elementWithAXUIElement:"
- "enableFocus"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsWithOptions:usingBlock:"
- "fbSceneIdentifier"
- "firstObject"
- "focusContainerForSuccessfulTypeaheadMovement"
- "focusContainersForCurrentSceneIdentifier:"
- "focusManager:didHitBoundaryWithHeading:"
- "focusManager:didMoveToElement:"
- "focusOnApplication"
- "focusOnRemoteSceneID"
- "focusOnSceneForTypeahead"
- "frame"
- "hasNativeFocusElements"
- "hasRemoteFocusSystem"
- "indexOfObject:"
- "indexOfObjectPassingTest:"
- "init"
- "intValue"
- "isContinuitySessionActive"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToString:"
- "isPIPWindowVisible"
- "isSpacer"
- "length"
- "lowercaseString"
- "moveFocusInsideForward:"
- "moveFocusInsideForward:shouldWrap:"
- "moveFocusWithHeading:byGroup:"
- "moveFocusWithHeading:queryString:"
- "moveFocusWithHeading:withQueryString:"
- "movementQueue"
- "numberWithAXAttribute:"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithLong:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "objectWithAXAttribute:"
- "observers"
- "observersLock"
- "observersQueue"
- "performAXAction:"
- "performAction:withValue:"
- "remoteSceneID"
- "removeObject:"
- "removeObjectsInArray:"
- "removeObserver:"
- "reverseObjectEnumerator"
- "safeValueForKey:"
- "server"
- "setFocusContainerForSuccessfulTypeaheadMovement:"
- "setMovementQueue:"
- "setObject:forKeyedSubscript:"
- "setObservers:"
- "setObserversLock:"
- "setObserversQueue:"
- "setTypeaheadQueryString:"
- "setTypeaheadString:"
- "systemApplication"
- "systemWideElement"
- "typeaheadQueryString"
- "typeaheadString"
- "uiElement"
- "userInputLabels"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8B16B20"
- "v28@0:8Q16B24"
- "v32@0:8Q16@24"
- "v40@0:8Q16B24@28B36"
- "weakObjectsHashTable"
- "windowSceneIdentifier"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=dd}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
