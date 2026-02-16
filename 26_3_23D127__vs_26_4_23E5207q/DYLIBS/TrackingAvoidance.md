## TrackingAvoidance

> `/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance`

```diff

-107.0.12.0.1
-  __TEXT.__text: 0x49668
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x470c
-  __TEXT.__const: 0x350
+107.0.12.0.3
+  __TEXT.__text: 0x4ea0c
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_methlist: 0x4924
+  __TEXT.__const: 0x328
   __TEXT.__oslogstring: 0x703a
-  __TEXT.__cstring: 0x2e7f
-  __TEXT.__gcc_except_tab: 0x65c
-  __TEXT.__unwind_info: 0xd68
-  __TEXT.__objc_classname: 0x78e
-  __TEXT.__objc_methname: 0xce1b
-  __TEXT.__objc_methtype: 0x1278
-  __TEXT.__objc_stubs: 0x7640
-  __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x790
-  __DATA_CONST.__objc_classlist: 0x228
+  __TEXT.__cstring: 0x2f5d
+  __TEXT.__gcc_except_tab: 0x634
+  __TEXT.__unwind_info: 0xfc8
+  __TEXT.__objc_classname: 0x7c1
+  __TEXT.__objc_methname: 0xd181
+  __TEXT.__objc_methtype: 0x12e2
+  __TEXT.__objc_stubs: 0x7780
+  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__const: 0x798
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2228
+  __DATA_CONST.__objc_selrefs: 0x22a0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__auth_got: 0x2c8
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x47e0
-  __AUTH_CONST.__objc_const: 0x8708
+  __AUTH_CONST.__cfstring: 0x4960
+  __AUTH_CONST.__objc_const: 0x8bc0
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x62c
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x660
   __DATA.__data: 0x600
   __DATA_DIRTY.__objc_data: 0x1310
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BCB070D9-807D-3DC9-AA40-CEB99CAAA4C9
-  Functions: 1537
-  Symbols:   5414
-  CStrings:  3543
+  UUID: 41B8016A-FC82-3DDF-80EC-F5864FFF2FDA
+  Functions: 1594
+  Symbols:   5586
+  CStrings:  3609
 
Symbols:
+ +[TAFamiliarityIndexEvent supportsSecureCoding]
+ +[TAPredictedContext supportsSecureCoding]
+ -[TAFamiliarityIndexEvent .cxx_destruct]
+ -[TAFamiliarityIndexEvent copyWithZone:]
+ -[TAFamiliarityIndexEvent dateInterval]
+ -[TAFamiliarityIndexEvent date]
+ -[TAFamiliarityIndexEvent descriptionDictionary]
+ -[TAFamiliarityIndexEvent description]
+ -[TAFamiliarityIndexEvent description].cold.1
+ -[TAFamiliarityIndexEvent encodeWithCoder:]
+ -[TAFamiliarityIndexEvent encodeWithOSLogCoder:options:maxLength:]
+ -[TAFamiliarityIndexEvent error]
+ -[TAFamiliarityIndexEvent familiarityIndex]
+ -[TAFamiliarityIndexEvent familiarityScore]
+ -[TAFamiliarityIndexEvent getDate]
+ -[TAFamiliarityIndexEvent initWithCoder:]
+ -[TAFamiliarityIndexEvent initWithFamiliarityIndex:dateInterval:lookbackInterval:referenceLocation:date:error:]
+ -[TAFamiliarityIndexEvent isEqual:]
+ -[TAFamiliarityIndexEvent lookbackIntervalInWeeks]
+ -[TAFamiliarityIndexEvent lookbackInterval]
+ -[TAFamiliarityIndexEvent referenceLocation]
+ -[TAFamiliarityIndexEvent setDateInterval:]
+ -[TAFamiliarityIndexEvent setFamiliarityIndex:]
+ -[TALocationOfInterest initWithType:latitude:longitude:horizontalAccuracy:referenceFrame:purpose:date:]
+ -[TALocationOfInterest purpose]
+ -[TAPredictedContext .cxx_destruct]
+ -[TAPredictedContext contextProbability]
+ -[TAPredictedContext coordinate]
+ -[TAPredictedContext copyWithZone:]
+ -[TAPredictedContext dateInterval]
+ -[TAPredictedContext descriptionDictionary]
+ -[TAPredictedContext description]
+ -[TAPredictedContext encodeWithCoder:]
+ -[TAPredictedContext endDate]
+ -[TAPredictedContext getDate]
+ -[TAPredictedContext hash]
+ -[TAPredictedContext initWithCoder:]
+ -[TAPredictedContext initWithLatitude:longitude:creationDate:startDate:endDate:contextProbability:]
+ -[TAPredictedContext isEqual:]
+ -[TAPredictedContext latitude]
+ -[TAPredictedContext longitude]
+ -[TAPredictedContext startDate]
+ _CLLocationCoordinate2DIsValid
+ _OBJC_CLASS_$_TAFamiliarityIndexEvent
+ _OBJC_CLASS_$_TAPredictedContext
+ _OBJC_IVAR_$_TAFamiliarityIndexEvent._date
+ _OBJC_IVAR_$_TAFamiliarityIndexEvent._dateInterval
+ _OBJC_IVAR_$_TAFamiliarityIndexEvent._error
+ _OBJC_IVAR_$_TAFamiliarityIndexEvent._familiarityIndex
+ _OBJC_IVAR_$_TAFamiliarityIndexEvent._lookbackInterval
+ _OBJC_IVAR_$_TAFamiliarityIndexEvent._referenceLocation
+ _OBJC_IVAR_$_TALocationOfInterest._purpose
+ _OBJC_IVAR_$_TAPredictedContext._contextProbability
+ _OBJC_IVAR_$_TAPredictedContext._creationDate
+ _OBJC_IVAR_$_TAPredictedContext._endDate
+ _OBJC_IVAR_$_TAPredictedContext._latitude
+ _OBJC_IVAR_$_TAPredictedContext._longitude
+ _OBJC_IVAR_$_TAPredictedContext._startDate
+ _OBJC_METACLASS_$_TAFamiliarityIndexEvent
+ _OBJC_METACLASS_$_TAPredictedContext
+ __OBJC_$_CLASS_METHODS_TAFamiliarityIndexEvent
+ __OBJC_$_CLASS_METHODS_TAPredictedContext
+ __OBJC_$_CLASS_PROP_LIST_TAFamiliarityIndexEvent
+ __OBJC_$_CLASS_PROP_LIST_TAPredictedContext
+ __OBJC_$_INSTANCE_METHODS_TAFamiliarityIndexEvent
+ __OBJC_$_INSTANCE_METHODS_TAPredictedContext
+ __OBJC_$_INSTANCE_VARIABLES_TAFamiliarityIndexEvent
+ __OBJC_$_INSTANCE_VARIABLES_TAPredictedContext
+ __OBJC_$_PROP_LIST_TAFamiliarityIndexEvent
+ __OBJC_$_PROP_LIST_TAPredictedContext
+ __OBJC_CLASS_PROTOCOLS_$_TAFamiliarityIndexEvent
+ __OBJC_CLASS_PROTOCOLS_$_TAPredictedContext
+ __OBJC_CLASS_RO_$_TAFamiliarityIndexEvent
+ __OBJC_CLASS_RO_$_TAPredictedContext
+ __OBJC_METACLASS_RO_$_TAFamiliarityIndexEvent
+ __OBJC_METACLASS_RO_$_TAPredictedContext
+ _objc_msgSend$contextProbability
+ _objc_msgSend$error
+ _objc_msgSend$familiarityIndex
+ _objc_msgSend$initWithFamiliarityIndex:dateInterval:lookbackInterval:referenceLocation:date:error:
+ _objc_msgSend$initWithLatitude:longitude:
+ _objc_msgSend$initWithLatitude:longitude:creationDate:startDate:endDate:contextProbability:
+ _objc_msgSend$initWithType:latitude:longitude:horizontalAccuracy:referenceFrame:purpose:date:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$lookbackInterval
+ _objc_msgSend$lookbackIntervalInWeeks
+ _objc_msgSend$purpose
+ _objc_msgSend$referenceLocation
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithType:latitude:longitude:horizontalAccuracy:date:
- _objc_msgSend$initWithType:latitude:longitude:horizontalAccuracy:referenceFrame:date:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x5
CStrings:
+ "@\"CLLocation\""
+ "@\"NSError\""
+ "@64@0:8d16@24d32@40@48@56"
+ "@64@0:8d16d24@32@40@48d56"
+ "@72@0:8Q16d24d32d40Q48Q56@64"
+ "ContextProbability"
+ "DateIntervalEnd"
+ "DateIntervalStart"
+ "EndDate"
+ "Error"
+ "FamiliarityIndex"
+ "LookbackInterval"
+ "Purpose"
+ "StartDate"
+ "T@\"CLLocation\",R,C,N,V_referenceLocation"
+ "T@\"NSDate\",R,C,N,V_endDate"
+ "T@\"NSDate\",R,C,N,V_startDate"
+ "T@\"NSDateInterval\",C,N,V_dateInterval"
+ "T@\"NSError\",R,C,N,V_error"
+ "TAFamiliarityIndexEvent"
+ "TAPredictedContext"
+ "TAPredictedContext: lat=%.6f, lon=%.6f, creation=%@, start=%@, end=%@, probability=%.3f"
+ "TQ,R,N,V_purpose"
+ "Td,N,V_familiarityIndex"
+ "Td,R,N,V_contextProbability"
+ "Td,R,N,V_lookbackInterval"
+ "T{CLLocationCoordinate2D=dd},R,N"
+ "_contextProbability"
+ "_dateInterval"
+ "_endDate"
+ "_error"
+ "_familiarityIndex"
+ "_lookbackInterval"
+ "_purpose"
+ "_referenceLocation"
+ "_startDate"
+ "a"
+ "contextProbability"
+ "error"
+ "familiarityIndex"
+ "familiarityScore"
+ "initWithFamiliarityIndex:dateInterval:lookbackInterval:referenceLocation:date:error:"
+ "initWithLatitude:longitude:"
+ "initWithLatitude:longitude:creationDate:startDate:endDate:contextProbability:"
+ "initWithType:latitude:longitude:horizontalAccuracy:referenceFrame:purpose:date:"
+ "localizedDescription"
+ "lookbackInterval"
+ "lookbackIntervalInWeeks"
+ "motorcycle"
+ "nil"
+ "purpose"
+ "referenceLocation"
+ "setDateInterval:"
+ "setFamiliarityIndex:"

```
