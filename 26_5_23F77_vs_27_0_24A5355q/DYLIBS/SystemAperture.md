## SystemAperture

> `/System/Library/PrivateFrameworks/SystemAperture.framework/SystemAperture`

```diff

-85.0.0.0.0
-  __TEXT.__text: 0x1938
-  __TEXT.__auth_stubs: 0x2b0
+96.0.0.0.0
+  __TEXT.__text: 0x1818
   __TEXT.__objc_methlist: 0x2b4
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x188
-  __TEXT.__gcc_except_tab: 0x10c
+  __TEXT.__cstring: 0x18d
+  __TEXT.__gcc_except_tab: 0xcc
   __TEXT.__oslogstring: 0x117
-  __TEXT.__unwind_info: 0x140
-  __TEXT.__objc_classname: 0x8d
-  __TEXT.__objc_methname: 0x7db
-  __TEXT.__objc_methtype: 0x1ba
-  __TEXT.__objc_stubs: 0x540
-  __DATA_CONST.__got: 0x50
+  __TEXT.__unwind_info: 0x138
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x260
+  __DATA_CONST.__objc_selrefs: 0x268
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x240
   __AUTH_CONST.__objc_const: 0x910
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x128
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A9B8475D-E116-344D-9FB2-B4520F5011AB
-  Functions: 40
-  Symbols:   240
-  CStrings:  187
+  UUID: 062D15E6-E6A3-3A27-9B40-3CA270467D58
+  Functions: 41
+  Symbols:   245
+  CStrings:  47
 
Symbols:
+ _SAHasBlankingRegionBehavior
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$hasBlankingRegionBehavior
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSMutableOrderedSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSTimer\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8d16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B36@0:8B16@\"NSString\"20@\"NSString\"28"
- "B36@0:8B16@20@28"
- "NSObject"
- "Q16@0:8"
- "SAAssertion"
- "SAAutomaticallyInvalidatable"
- "SAAutomaticallyInvalidatingAssertion"
- "SAInvalidatable"
- "Subclass"
- "SystemApertureAdditions"
- "T#,R"
- "T@\"NSArray\",R,C,N,G_descriptionConstituents"
- "T@\"NSDate\",?,R,C,N"
- "T@\"NSDate\",?,R,C,N,V_creationDate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,G_invalidationReason"
- "TB,N,GisAutomaticallyInvalidatable"
- "TB,N,GisAutomaticallyInvalidatable,V_automaticallyInvalidatable"
- "TB,R,N,GisValid"
- "TB,R,N,GisValid,V_valid"
- "TQ,R"
- "Td,R,N,V_invalidationInterval"
- "Vv16@0:8"
- "^v16@0:8"
- "^{_NSZone=}16@0:8"
- "_automaticallyInvalidatable"
- "_creationDate"
- "_descriptionConstituents"
- "_invalidateInvalidationTimerIfNecessary"
- "_invalidationBlocks"
- "_invalidationInterval"
- "_invalidationReason"
- "_invalidationTimer"
- "_key"
- "_lockReason"
- "_scheduleInvalidationTimerIfNecessary"
- "_setAutomaticallyInvalidatable:lockingWithKey:reason:"
- "_valid"
- "addInvalidationBlock:"
- "addObject:"
- "appendFormat:"
- "appendString:"
- "arrayByAddingObject:"
- "arrayWithObjects:count:"
- "automaticallyInvalidatable"
- "autorelease"
- "behaviorOverridingTarget"
- "class"
- "clientIdentifier"
- "conformsToProtocol:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "creationDate"
- "currentHandler"
- "d"
- "d16@0:8"
- "dealloc"
- "debugDescription"
- "description"
- "descriptionConstituents"
- "element"
- "elementDescription"
- "elementIdentifier"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasActivityBehavior"
- "hasAlertBehavior"
- "hasIndicatorBehavior"
- "hash"
- "init"
- "initWithFormat:"
- "initWithInvalidationInterval:"
- "initWithObjectsAndKeys:"
- "invalidate"
- "invalidateWithReason:"
- "invalidationInterval"
- "invalidationReason"
- "isAutomaticallyInvalidatable"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "now"
- "numberWithDouble:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pointerAtIndex:"
- "release"
- "removePointerAtIndex:"
- "resetAutomaticInvalidationTimer"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "sa_compact"
- "sa_lastPointer"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "self"
- "setAutomaticallyInvalidatable:"
- "setAutomaticallyInvalidatable:lockingWithKey:reason:"
- "setObject:forKey:"
- "setValue:forKey:"
- "stringWithFormat:"
- "superclass"
- "uniqueElementIdentifier"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"<SAInvalidatable>\"@\"NSString\">16"
- "valid"
- "viewProvider"
- "zone"

```
