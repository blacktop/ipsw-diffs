## Routine

> `/System/Library/Assistant/Plugins/Routine.assistantBundle/Routine`

```diff

-1075.0.2.0.0
-  __TEXT.__text: 0x2464
-  __TEXT.__auth_stubs: 0x2f0
+1109.0.3.0.0
+  __TEXT.__text: 0x20b4
   __TEXT.__objc_methlist: 0x14c
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x202
+  __TEXT.__cstring: 0x206
   __TEXT.__oslogstring: 0x148
-  __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0x7e
-  __TEXT.__objc_methname: 0x5b3
-  __TEXT.__objc_methtype: 0xff
-  __TEXT.__objc_stubs: 0x5c0
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__gcc_except_tab: 0x94
+  __TEXT.__unwind_info: 0xe0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x3c8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x30

   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9280F225-E781-3291-B476-F3F69AEBFA28
+  UUID: 5A5A8619-4961-3D53-B703-53FF1A263C99
   Functions: 39
-  Symbols:   87
-  CStrings:  108
+  Symbols:   91
+  CStrings:  30
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x5
+ _objc_retain_x8
- _objc_retain
- _objc_retainAutoreleasedReturnValue
CStrings:
- ".cxx_destruct"
- "@\"GEOLocationShifter\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"RTRoutineManager\""
- "@16@0:8"
- "@36@0:8@16B24^@28"
- "@68@0:8@16d24d32d40@48B56@60"
- "B32@0:8{CLLocationCoordinate2D=dd}16"
- "RTAssistantVehicleEventCreate"
- "RTAssistantVehicleEventDelete"
- "RTAssistantVehicleEventSearch"
- "RTExtensions"
- "RTLocationShifter"
- "T@\"GEOLocationShifter\",&,N,V_locationShifter"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"RTRoutineManager\",&,N,V_routineManager"
- "_geoLocationShifter"
- "_locationShifter"
- "_queue"
- "_routineManager"
- "accuracy"
- "addObject:"
- "clearAllVehicleEventsWithHandler:"
- "code"
- "count"
- "date"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "fetchLastVehicleEventsWithHandler:"
- "horizontalUncertainty"
- "init"
- "initWithCapacity:"
- "initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:referenceFrame:"
- "initWithErrorCode:"
- "initWithLatitude:longitude:horizontalUncertainty:date:referenceFrame:"
- "initWithReason:"
- "isLocationShiftRequiredForCoordinate:"
- "latitude"
- "localizedDescription"
- "location"
- "locationShifter"
- "longitude"
- "notes"
- "numberWithBool:"
- "numberWithDouble:"
- "performWithCompletion:"
- "queue"
- "referenceFrame"
- "routineManager"
- "setAccuracy:"
- "setDate:"
- "setEvents:"
- "setLatitude:"
- "setLocation:"
- "setLocationShifter:"
- "setLongitude:"
- "setNotes:"
- "setQueue:"
- "setRoutineManager:"
- "setUserSetLocation:"
- "setVehicleIdentifier:"
- "shiftCoordinate:accuracy:handler:"
- "shiftCoordinate:accuracy:shiftedCoordinate:shiftedAccuracy:"
- "shiftCoordinate:accuracy:withCompletionHandler:mustGoToNetworkCallback:errorHandler:callbackQueue:"
- "shiftLocation:handler:"
- "shiftedLocation:allowNetwork:error:"
- "userSetLocation"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@16@?24"
- "v48@0:8{CLLocationCoordinate2D=dd}16d32@?40"
- "vehicleEventAtLocation:notes:handler:"
- "vehicleEventWithDate:latitude:longitude:accuracy:notes:userSetLocation:vehicleIdentifier:"
- "vehicleIdentifier"

```
