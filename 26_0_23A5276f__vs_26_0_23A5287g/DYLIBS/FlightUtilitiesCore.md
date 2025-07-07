## FlightUtilitiesCore

> `/System/Library/PrivateFrameworks/FlightUtilitiesCore.framework/FlightUtilitiesCore`

```diff

-174.0.0.0.0
-  __TEXT.__text: 0xdb20
-  __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_methlist: 0xb6c
-  __TEXT.__const: 0x27a
-  __TEXT.__cstring: 0x8d0
+177.0.0.0.0
+  __TEXT.__text: 0x10e34
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_methlist: 0xf1c
+  __TEXT.__const: 0x2d2
+  __TEXT.__cstring: 0xc60
   __TEXT.__swift5_typeref: 0x10f
-  __TEXT.__swift5_capture: 0x170
+  __TEXT.__swift5_capture: 0x180
   __TEXT.__constg_swiftt: 0x98
   __TEXT.__swift5_reflstr: 0x36
   __TEXT.__swift5_fieldmd: 0x54

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__unwind_info: 0x3b0
-  __TEXT.__eh_frame: 0x6d0
-  __TEXT.__objc_classname: 0x102
-  __TEXT.__objc_methname: 0x1871
-  __TEXT.__objc_methtype: 0x56e
-  __TEXT.__objc_stubs: 0x16c0
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x1d8
-  __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x38
+  __TEXT.__unwind_info: 0x428
+  __TEXT.__eh_frame: 0x6f8
+  __TEXT.__objc_classname: 0x153
+  __TEXT.__objc_methname: 0x2187
+  __TEXT.__objc_methtype: 0x6b8
+  __TEXT.__objc_stubs: 0x1c80
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x1f8
+  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x730
-  __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x480
-  __AUTH_CONST.__const: 0x338
-  __AUTH_CONST.__cfstring: 0xa00
-  __AUTH_CONST.__objc_const: 0x13a0
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0xb0
+  __DATA_CONST.__objc_selrefs: 0x8e0
+  __DATA_CONST.__objc_superrefs: 0x48
+  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__const: 0x360
+  __AUTH_CONST.__cfstring: 0xca0
+  __AUTH_CONST.__objc_const: 0x1a68
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH.__objc_data: 0x1f0
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0xb8
-  __DATA.__data: 0x2c8
+  __DATA.__objc_ivar: 0xf8
+  __DATA.__data: 0x328
   __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0x2d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 28BAD014-386A-3982-8ED3-AB4F01B149B1
-  Functions: 304
-  Symbols:   932
-  CStrings:  591
+  UUID: 5F8A9A95-3E4E-395E-86BE-D185F65D1A4D
+  Functions: 367
+  Symbols:   1164
+  CStrings:  733
 
Symbols:
+ +[FUArrivalInfo supportsSecureCoding]
+ +[FUBaseStopInfo supportsSecureCoding]
+ +[FUDepartureInfo supportsSecureCoding]
+ +[FUFutureFlightState newWithState:andDate:]
+ +[FUFutureFlightState supportsSecureCoding]
+ -[FUArrivalInfo .cxx_destruct]
+ -[FUArrivalInfo baggageClaim]
+ -[FUArrivalInfo copyWithZone:]
+ -[FUArrivalInfo description]
+ -[FUArrivalInfo divertedAirport]
+ -[FUArrivalInfo encodeWithCoder:]
+ -[FUArrivalInfo initWithAirport:gate:terminal:baggageClaim:divertedAirport:displayTime:scheduledGateTime:currentGateTime:scheduledRunwayTime:currentRunwayTime:gateBufferMinutes:runwayBufferMinutes:]
+ -[FUArrivalInfo initWithCoder:]
+ -[FUArrivalInfo isEqual:]
+ -[FUArrivalInfo setBaggageClaim:]
+ -[FUArrivalInfo setDivertedAirport:]
+ -[FUBaseStopInfo .cxx_destruct]
+ -[FUBaseStopInfo _deltaGateMinutes]
+ -[FUBaseStopInfo airport]
+ -[FUBaseStopInfo copyWithZone:]
+ -[FUBaseStopInfo currentGateTime]
+ -[FUBaseStopInfo currentRunwayTime]
+ -[FUBaseStopInfo delayFromSchedule]
+ -[FUBaseStopInfo description]
+ -[FUBaseStopInfo displayTime]
+ -[FUBaseStopInfo encodeWithCoder:]
+ -[FUBaseStopInfo flightTimeStatus]
+ -[FUBaseStopInfo gateBufferMinutes]
+ -[FUBaseStopInfo gate]
+ -[FUBaseStopInfo initWithAirport:gate:terminal:displayTime:scheduledGateTime:currentGateTime:scheduledRunwayTime:currentRunwayTime:gateBufferMinutes:runwayBufferMinutes:]
+ -[FUBaseStopInfo initWithCoder:]
+ -[FUBaseStopInfo isEqual:]
+ -[FUBaseStopInfo runwayBufferMinutes]
+ -[FUBaseStopInfo scheduledGateTime]
+ -[FUBaseStopInfo scheduledRunwayTime]
+ -[FUBaseStopInfo setDisplayTime:]
+ -[FUBaseStopInfo terminal]
+ -[FUDepartureInfo copyWithZone:]
+ -[FUFlight initWithDisplayAirline:queriedAirlineTitle:displayFlightNumber:airline:flightNumber:flightIdentifier:operatorAirline:operatorFlightNumber:cancellationMessage:allLegs:legs:identifier:departureLegIndex:arrivalLegIndex:expirationDate:rawResponse:]
+ -[FUFlightLeg _calculateCurrentProgress]
+ -[FUFlightLeg _computedFlightStateWithBuffer:]
+ -[FUFlightLeg _nowDate]
+ -[FUFlightLeg arrivalInfo]
+ -[FUFlightLeg computedFlightState]
+ -[FUFlightLeg dateOfNextExpectedUpdate]
+ -[FUFlightLeg departureInfo]
+ -[FUFlightLeg flightState]
+ -[FUFlightLeg initWithStatus:duration:departure:arrival:flightState:departureInfo:arrivalInfo:dateLastUpdated:]
+ -[FUFlightLeg setArrivalInfo:]
+ -[FUFlightLeg setDepartureInfo:]
+ -[FUFlightLeg setFlightState:]
+ -[FUFlightStep initWithAirport:gate:terminal:legStatus:delayFromSchedule:scheduledTime:estimatedTime:actualTime:runwayTime:departure:]
+ -[FUFutureFlightState .cxx_destruct]
+ -[FUFutureFlightState copyWithZone:]
+ -[FUFutureFlightState encodeWithCoder:]
+ -[FUFutureFlightState expectedDate]
+ -[FUFutureFlightState futureState]
+ -[FUFutureFlightState initWithCoder:]
+ -[FUFutureFlightState initWithState:andDate:]
+ -[FUFutureFlightState isEqual:]
+ -[FUFutureFlightState setExpectedDate:]
+ -[FUFutureFlightState setFutureState:]
+ _NSStringFromClass
+ _OBJC_CLASS_$_FUArrivalInfo
+ _OBJC_CLASS_$_FUBaseStopInfo
+ _OBJC_CLASS_$_FUDepartureInfo
+ _OBJC_CLASS_$_FUFutureFlightState
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_IVAR_$_FUArrivalInfo._baggageClaim
+ _OBJC_IVAR_$_FUArrivalInfo._divertedAirport
+ _OBJC_IVAR_$_FUBaseStopInfo._airport
+ _OBJC_IVAR_$_FUBaseStopInfo._currentGateTime
+ _OBJC_IVAR_$_FUBaseStopInfo._currentRunwayTime
+ _OBJC_IVAR_$_FUBaseStopInfo._displayTime
+ _OBJC_IVAR_$_FUBaseStopInfo._gate
+ _OBJC_IVAR_$_FUBaseStopInfo._gateBufferMinutes
+ _OBJC_IVAR_$_FUBaseStopInfo._runwayBufferMinutes
+ _OBJC_IVAR_$_FUBaseStopInfo._scheduledGateTime
+ _OBJC_IVAR_$_FUBaseStopInfo._scheduledRunwayTime
+ _OBJC_IVAR_$_FUBaseStopInfo._terminal
+ _OBJC_IVAR_$_FUFlightLeg._arrivalInfo
+ _OBJC_IVAR_$_FUFlightLeg._departureInfo
+ _OBJC_IVAR_$_FUFlightLeg._flightState
+ _OBJC_IVAR_$_FUFutureFlightState._expectedDate
+ _OBJC_IVAR_$_FUFutureFlightState._futureState
+ _OBJC_METACLASS_$_FUArrivalInfo
+ _OBJC_METACLASS_$_FUBaseStopInfo
+ _OBJC_METACLASS_$_FUDepartureInfo
+ _OBJC_METACLASS_$_FUFutureFlightState
+ __DateAdjustedForwardByMinutes
+ __OBJC_$_CLASS_METHODS_FUArrivalInfo
+ __OBJC_$_CLASS_METHODS_FUBaseStopInfo
+ __OBJC_$_CLASS_METHODS_FUDepartureInfo
+ __OBJC_$_CLASS_METHODS_FUFutureFlightState
+ __OBJC_$_CLASS_PROP_LIST_FUArrivalInfo
+ __OBJC_$_CLASS_PROP_LIST_FUBaseStopInfo
+ __OBJC_$_CLASS_PROP_LIST_FUDepartureInfo
+ __OBJC_$_CLASS_PROP_LIST_FUFutureFlightState
+ __OBJC_$_INSTANCE_METHODS_FUArrivalInfo
+ __OBJC_$_INSTANCE_METHODS_FUBaseStopInfo
+ __OBJC_$_INSTANCE_METHODS_FUDepartureInfo
+ __OBJC_$_INSTANCE_METHODS_FUFutureFlightState
+ __OBJC_$_INSTANCE_VARIABLES_FUArrivalInfo
+ __OBJC_$_INSTANCE_VARIABLES_FUBaseStopInfo
+ __OBJC_$_INSTANCE_VARIABLES_FUFutureFlightState
+ __OBJC_$_PROP_LIST_FUArrivalInfo
+ __OBJC_$_PROP_LIST_FUBaseStopInfo
+ __OBJC_$_PROP_LIST_FUFutureFlightState
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FUStopInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FUStopInfo
+ __OBJC_$_PROTOCOL_REFS_FUStopInfo
+ __OBJC_CLASS_PROTOCOLS_$_FUArrivalInfo
+ __OBJC_CLASS_PROTOCOLS_$_FUBaseStopInfo
+ __OBJC_CLASS_PROTOCOLS_$_FUDepartureInfo
+ __OBJC_CLASS_PROTOCOLS_$_FUFutureFlightState
+ __OBJC_CLASS_RO_$_FUArrivalInfo
+ __OBJC_CLASS_RO_$_FUBaseStopInfo
+ __OBJC_CLASS_RO_$_FUDepartureInfo
+ __OBJC_CLASS_RO_$_FUFutureFlightState
+ __OBJC_LABEL_PROTOCOL_$_FUStopInfo
+ __OBJC_METACLASS_RO_$_FUArrivalInfo
+ __OBJC_METACLASS_RO_$_FUBaseStopInfo
+ __OBJC_METACLASS_RO_$_FUDepartureInfo
+ __OBJC_METACLASS_RO_$_FUFutureFlightState
+ __OBJC_PROTOCOL_$_FUStopInfo
+ ___46-[FUFlightLeg _computedFlightStateWithBuffer:]_block_invoke
+ ___block_descriptor_40_e8_32s_e29_B24?0"NSDate"8"NSNumber"16ls32l8
+ _objc_msgSend$_calculateCurrentProgress
+ _objc_msgSend$_computedFlightStateWithBuffer:
+ _objc_msgSend$_deltaGateMinutes
+ _objc_msgSend$_nowDate
+ _objc_msgSend$arrivalInfo
+ _objc_msgSend$arrivalTime
+ _objc_msgSend$bufferMinutes
+ _objc_msgSend$compare:
+ _objc_msgSend$components:fromDate:toDate:options:
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$current
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$currentGateTime
+ _objc_msgSend$currentProgress
+ _objc_msgSend$currentRunwayTime
+ _objc_msgSend$dateByAddingComponents:toDate:options:
+ _objc_msgSend$dateLastUpdated
+ _objc_msgSend$decodeIntForKey:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$departureInfo
+ _objc_msgSend$departureTime
+ _objc_msgSend$description
+ _objc_msgSend$displayTime
+ _objc_msgSend$doesNotRecognizeSelector:
+ _objc_msgSend$expectedDate
+ _objc_msgSend$flightState
+ _objc_msgSend$futureState
+ _objc_msgSend$gateArrivalTimes
+ _objc_msgSend$gateBufferMinutes
+ _objc_msgSend$gateDepartureTimes
+ _objc_msgSend$initWithAirport:gate:terminal:baggageClaim:divertedAirport:displayTime:scheduledGateTime:currentGateTime:scheduledRunwayTime:currentRunwayTime:gateBufferMinutes:runwayBufferMinutes:
+ _objc_msgSend$initWithAirport:gate:terminal:displayTime:scheduledGateTime:currentGateTime:scheduledRunwayTime:currentRunwayTime:gateBufferMinutes:runwayBufferMinutes:
+ _objc_msgSend$initWithState:andDate:
+ _objc_msgSend$minute
+ _objc_msgSend$now
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$pegasusDefinedState
+ _objc_msgSend$pegasusDisplayFields
+ _objc_msgSend$runwayArrivalTimes
+ _objc_msgSend$runwayBufferMinutes
+ _objc_msgSend$runwayDepartureTimes
+ _objc_msgSend$scheduled
+ _objc_msgSend$scheduledGateTime
+ _objc_msgSend$scheduledRunwayTime
+ _objc_msgSend$setArrivalInfo:
+ _objc_msgSend$setDepartureInfo:
+ _objc_msgSend$setFlightState:
+ _objc_msgSend$setMinute:
+ _objc_retainBlock
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_setProperty_atomic_copy
+ _objectdestroy.34Tm
- -[FUFlightLeg _currentProgress]
- -[FUFlightLeg setBaggageClaim:]
- _OBJC_IVAR_$_FUFlightLeg._baggageClaim
- __OBJC_$_PROTOCOL_CLASS_METHODS_FUFlightFactoryInternalProtocol
- ___26-[FUFlightLeg description]_block_invoke
- ___block_descriptor_40_e8_32s_e15_"NSString"8?0ls32l8
- _objc_msgSend$_currentProgress
- _objc_msgSend$setBaggageClaim:
- _objectdestroy.29Tm
CStrings:
+ "\n"
+ "<%@: %p> {airport: %@, gate: %@, terminal: %@, baggageClaim: %@, divertedAirport: %@, scheduledGateTime: %@, currentGateTime: %@, scheduledRunwayTime: %@, currentRunwayTime: %@, gateBufferMinutes: %@, runwayBufferMinutes: %@}"
+ "<%@: %p> {airport: %@, gate: %@, terminal: %@, displayTime: %@, scheduledGateTime: %@, currentGateTime: %@, scheduledRunwayTime: %@, currentRunwayTime: %@, gateBufferMinutes: %@, runwayBufferMinutes: %@}"
+ "@\"FUAirport\"16@0:8"
+ "@\"FUArrivalInfo\""
+ "@\"FUDepartureInfo\""
+ "@\"NSDate\"16@0:8"
+ "@\"NSNumber\"16@0:8"
+ "@112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
+ "@144@0:8@16@24Q32@40Q48@56@64Q72@80@88@96@104Q112Q120@128@136"
+ "@32@0:8q16@24"
+ "@80@0:8q16d24@32@40q48@56@64@72"
+ "@92@0:8@16@24@32q40@48@56@64@72@80B88"
+ "@96@0:8@16@24@32@40@48@56@64@72@80@88"
+ "B24@?0@\"NSDate\"8@\"NSNumber\"16"
+ "Computed FUFlightState is before the server FUFlightState for flight leg: %@"
+ "FUArrivalInfo"
+ "FUBaseStopInfo"
+ "FUDepartureInfo"
+ "FUFlightStateArrived"
+ "FUFlightStateCancelled"
+ "FUFlightStateDeparted"
+ "FUFlightStateDiverted"
+ "FUFlightStateEnRoute"
+ "FUFlightStateLanded"
+ "FUFlightStateLostVessel"
+ "FUFlightStateRedirected"
+ "FUFlightStateScheduled"
+ "FUFlightStateUnknown"
+ "FUFutureFlightState"
+ "FUStopInfo"
+ "Leg: %@ => %@  \n  Flight State: %@  \n  Computed Flight State: %@  \n  Current Progress: %.1f%%  \n  Departure Info: %@  \n  Arrival Info: %@"
+ "T@\"FUAirport\",&,V_divertedAirport"
+ "T@\"FUAirport\",R,V_airport"
+ "T@\"FUArrivalInfo\",&,V_arrivalInfo"
+ "T@\"FUDepartureInfo\",&,V_departureInfo"
+ "T@\"NSDate\",C,V_expectedDate"
+ "T@\"NSDate\",R"
+ "T@\"NSDate\",R,V_currentGateTime"
+ "T@\"NSDate\",R,V_currentRunwayTime"
+ "T@\"NSDate\",R,V_scheduledGateTime"
+ "T@\"NSDate\",R,V_scheduledRunwayTime"
+ "T@\"NSNumber\",R,V_gateBufferMinutes"
+ "T@\"NSNumber\",R,V_runwayBufferMinutes"
+ "T@\"NSString\",C,V_baggageClaim"
+ "T@\"NSString\",R,V_gate"
+ "T@\"NSString\",R,V_terminal"
+ "Tq,V_flightState"
+ "Tq,V_futureState"
+ "Unknown FUFlightState: %ld"
+ "_arrivalInfo"
+ "_calculateCurrentProgress"
+ "_computedFlightStateWithBuffer:"
+ "_currentGateTime"
+ "_currentRunwayTime"
+ "_deltaGateMinutes"
+ "_departureInfo"
+ "_displayTime"
+ "_divertedAirport"
+ "_expectedDate"
+ "_flightState"
+ "_futureState"
+ "_gateBufferMinutes"
+ "_nowDate"
+ "_runwayBufferMinutes"
+ "_scheduledGateTime"
+ "_scheduledRunwayTime"
+ "arrivalInfo"
+ "arrivalTime"
+ "bufferMinutes"
+ "compare:"
+ "components:fromDate:toDate:options:"
+ "computedFlightState"
+ "current"
+ "currentCalendar"
+ "currentGateTime"
+ "currentRunwayTime"
+ "dateByAddingComponents:toDate:options:"
+ "dateOfNextExpectedUpdate"
+ "decodeIntForKey:"
+ "decodeObjectForKey:"
+ "departureInfo"
+ "departureTime"
+ "displayTime"
+ "doesNotRecognizeSelector:"
+ "expectedDate"
+ "flightState"
+ "flightTimeStatus"
+ "futureState"
+ "gateArrivalTimes"
+ "gateBufferMinutes"
+ "gateDepartureTimes"
+ "initWithAirport:gate:terminal:baggageClaim:divertedAirport:displayTime:scheduledGateTime:currentGateTime:scheduledRunwayTime:currentRunwayTime:gateBufferMinutes:runwayBufferMinutes:"
+ "initWithAirport:gate:terminal:displayTime:scheduledGateTime:currentGateTime:scheduledRunwayTime:currentRunwayTime:gateBufferMinutes:runwayBufferMinutes:"
+ "initWithAirport:gate:terminal:legStatus:delayFromSchedule:scheduledTime:estimatedTime:actualTime:runwayTime:departure:"
+ "initWithDisplayAirline:queriedAirlineTitle:displayFlightNumber:airline:flightNumber:flightIdentifier:operatorAirline:operatorFlightNumber:cancellationMessage:allLegs:legs:identifier:departureLegIndex:arrivalLegIndex:expirationDate:rawResponse:"
+ "initWithState:andDate:"
+ "initWithStatus:duration:departure:arrival:flightState:departureInfo:arrivalInfo:dateLastUpdated:"
+ "minute"
+ "newWithState:andDate:"
+ "now"
+ "numberWithInteger:"
+ "pegasusDefinedState"
+ "pegasusDisplayFields"
+ "q20@0:8B16"
+ "runwayArrivalTimes"
+ "runwayBufferMinutes"
+ "runwayDepartureTimes"
+ "scheduled"
+ "scheduledGateTime"
+ "scheduledRunwayTime"
+ "setArrivalInfo:"
+ "setDepartureInfo:"
+ "setDisplayTime:"
+ "setDivertedAirport:"
+ "setExpectedDate:"
+ "setFlightState:"
+ "setFutureState:"
+ "setMinute:"
- "$"
- "@\"NSString\"8@?0"
- "FUFlightStatusArrived"
- "FUFlightStatusCancelled"
- "FUFlightStatusDiverted"
- "FUFlightStatusEnRoute"
- "FUFlightStatusRedirected"
- "FUFlightStatusScheduled"
- "Leg: %@ => %@ %@ Takeoff %@ Landing %@ baggage %@"
- "Status not defined"
- "T@\"NSString\",&,V_baggageClaim"
- "_currentProgress"

```
