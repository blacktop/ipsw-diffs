## FlightUtilitiesCore

> `/System/Library/PrivateFrameworks/FlightUtilitiesCore.framework/FlightUtilitiesCore`

```diff

 182.0.0.0.0
-  __TEXT.__text: 0x11188
-  __TEXT.__auth_stubs: 0x950
+  __TEXT.__text: 0x11a48
+  __TEXT.__auth_stubs: 0x8f0
   __TEXT.__objc_methlist: 0xf3c
   __TEXT.__const: 0x2ea
-  __TEXT.__cstring: 0xc60
+  __TEXT.__cstring: 0xa80
   __TEXT.__swift5_typeref: 0x10f
   __TEXT.__swift5_capture: 0x180
   __TEXT.__constg_swiftt: 0x98

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__unwind_info: 0x438
+  __TEXT.__unwind_info: 0x448
   __TEXT.__eh_frame: 0x6f8
-  __TEXT.__objc_classname: 0x153
-  __TEXT.__objc_methname: 0x21be
-  __TEXT.__objc_methtype: 0x6b8
-  __TEXT.__objc_stubs: 0x1cc0
+  __TEXT.__objc_classname: 0x1db
+  __TEXT.__objc_methname: 0x21cc
+  __TEXT.__objc_methtype: 0x7cd
+  __TEXT.__objc_stubs: 0x1d00
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_classlist: 0x78

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8f8
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__auth_got: 0x480
   __AUTH_CONST.__const: 0x360
   __AUTH_CONST.__cfstring: 0xca0
   __AUTH_CONST.__objc_const: 0x1a98

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 405FBA89-9AC8-329B-A253-1F0C9EE5FC01
+  UUID: 30E6D370-DBF3-3901-BF55-C5EE953A5D2F
   Functions: 370
-  Symbols:   1173
-  CStrings:  738
+  Symbols:   1170
+  CStrings:  735
 
Symbols:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithProtobuf:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
Functions:
~ +[FUUtils testDate] : 12 -> 60
~ +[FUUtils setTestDate:] : 16 -> 64
~ +[FUUtils enumerateFlightCodesInString:usingBlock:] : 400 -> 408
~ +[FUUtils airportFromSFAirport:] : 296 -> 320
~ +[FUUtils extractTimeForFlightStep:fromLeg:] : 540 -> 572
~ +[FUUtils convertFlightModel:withError:] : 3108 -> 3400
~ -[FUArrivalInfo initWithAirport:gate:terminal:baggageClaim:divertedAirport:displayTime:scheduledGateTime:currentGateTime:scheduledRunwayTime:currentRunwayTime:gateBufferMinutes:runwayBufferMinutes:] : 264 -> 256
~ -[FUArrivalInfo isEqual:] : 416 -> 448
~ -[FUArrivalInfo copyWithZone:] : 644 -> 692
~ -[FUArrivalInfo encodeWithCoder:] : 176 -> 184
~ -[FUArrivalInfo initWithCoder:] : 208 -> 216
~ -[FUArrivalInfo description] : 428 -> 480
~ -[FUDepartureInfo copyWithZone:] : 548 -> 588
~ -[FUFutureFlightState isEqual:] : 240 -> 256
~ -[FUFutureFlightState copyWithZone:] : 132 -> 136
~ -[FUFutureFlightState encodeWithCoder:] : 136 -> 140
~ -[FUFutureFlightState initWithCoder:] : 144 -> 148
~ -[FUBaseStopInfo initWithAirport:gate:terminal:displayTime:scheduledGateTime:currentGateTime:scheduledRunwayTime:currentRunwayTime:gateBufferMinutes:runwayBufferMinutes:] : 480 -> 448
~ -[FUBaseStopInfo isEqual:] : 1616 -> 1776
~ -[FUBaseStopInfo setDisplayTime:] : 12 -> 64
~ -[FUBaseStopInfo displayTime] : 32 -> 72
~ -[FUBaseStopInfo _deltaGateMinutes] : 156 -> 172
~ -[FUBaseStopInfo flightTimeStatus] : 108 -> 112
~ -[FUBaseStopInfo delayFromSchedule] : 140 -> 148
~ -[FUBaseStopInfo encodeWithCoder:] : 476 -> 516
~ -[FUBaseStopInfo initWithCoder:] : 556 -> 596
~ -[FUBaseStopInfo description] : 396 -> 444
~ -[FUFlight initWithDisplayAirline:queriedAirlineTitle:displayFlightNumber:airline:flightNumber:flightIdentifier:operatorAirline:operatorFlightNumber:cancellationMessage:allLegs:legs:identifier:departureLegIndex:arrivalLegIndex:expirationDate:rawResponse:] : 548 -> 544
~ -[FUFlight isEqual:] : 1452 -> 1580
~ -[FUFlight description] : 320 -> 364
~ -[FUFlight copyWithZone:] : 524 -> 540
~ -[FUFlight legsAsFlights] : 480 -> 500
~ -[FUFlight flightCode] : 144 -> 156
~ -[FUFlight displayFlightCode] : 128 -> 136
~ -[FUFlight operatorFlightCode] : 144 -> 156
~ -[FUFlight setAllLegs:] : 128 -> 140
~ -[FUFlight setDepartureLegIndex:arrivalLegIndex:] : 148 -> 156
~ -[FUFlight status] : 372 -> 376
~ -[FUFlight relevantLeg] : 384 -> 376
~ -[FUFlight firstLeg] : 128 -> 140
~ -[FUFlight lastLeg] : 128 -> 140
~ -[FUFlight departure] : 76 -> 84
~ -[FUFlight arrival] : 76 -> 84
~ -[FUFlight duration] : 80 -> 88
~ -[FUFlight identifier] : 456 -> 508
~ +[FUFlight timeFormatterForIdentifier] : 168 -> 176
~ +[FUFlight loadFlightsWithNumber:airlineCode:date:dateType:completionHandler:] : 184 -> 172
~ -[FUFlight encodeWithCoder:] : 880 -> 960
~ -[FUFlight initWithCoder:] : 792 -> 840
~ -[FUFlight setIdentifier:] : 12 -> 64
~ -[FUFlightLeg initWithStatus:duration:departure:arrival:flightState:departureInfo:arrivalInfo:dateLastUpdated:] : 300 -> 280
~ -[FUFlightLeg isEqual:] : 944 -> 1008
~ -[FUFlightLeg _currentProgress] : 456 -> 512
~ -[FUFlightLeg computedFlightState] : 144 -> 148
~ -[FUFlightLeg baggageClaim] : 76 -> 84
~ -[FUFlightLeg dateOfNextExpectedUpdate] : 444 -> 512
~ __DateAdjustedForwardByMinutes : 152 -> 160
~ -[FUFlightLeg description] : 468 -> 512
~ -[FUFlightLeg _calculateCurrentProgress] : 320 -> 356
~ -[FUFlightLeg _computedFlightStateWithBuffer:] : 816 -> 892
~ ___46-[FUFlightLeg _computedFlightStateWithBuffer:]_block_invoke : 124 -> 128
~ -[FUFlightLeg encodeWithCoder:] : 472 -> 516
~ -[FUFlightLeg initWithCoder:] : 408 -> 428
~ -[FUAirline isEqual:] : 832 -> 912
~ -[FUAirline copyWithZone:] : 288 -> 308
~ -[FUAirline description] : 140 -> 152
~ -[FUAirline encodeWithCoder:] : 392 -> 432
~ -[FUAirline initWithCoder:] : 336 -> 356
~ -[FUStepTime description] : 168 -> 176
~ -[FUStepTime isEqual:] : 240 -> 256
~ -[FUStepTime copyWithZone:] : 132 -> 136
~ -[FUStepTime timeIntervalSinceNow] : 112 -> 120
~ -[FUStepTime encodeWithCoder:] : 172 -> 180
~ -[FUStepTime initWithCoder:] : 192 -> 196
~ -[FUFlightStep initWithAirport:gate:terminal:legStatus:delayFromSchedule:scheduledTime:estimatedTime:actualTime:runwayTime:departure:] : 396 -> 368
~ -[FUFlightStep isEqual:] : 1420 -> 1560
~ -[FUFlightStep copyWithZone:] : 460 -> 492
~ -[FUFlightStep time] : 220 -> 224
~ -[FUFlightStep setDelayFromSchedule:] : 140 -> 148
~ -[FUFlightStep delayFromSchedule] : 208 -> 232
~ -[FUFlightStep status] : 88 -> 92
~ -[FUFlightStep description] : 140 -> 152
~ -[FUFlightStep encodeWithCoder:] : 700 -> 772
~ -[FUFlightStep initWithCoder:] : 560 -> 596
~ +[FUFlightFactory flightFactoryClassWithProvider:] : 124 -> 132
~ +[FUFlightFactory loadFlightWithIdentifier:completionHandler:] : 468 -> 488
~ ___62+[FUFlightFactory loadFlightWithIdentifier:completionHandler:]_block_invoke : 868 -> 896
~ +[FUFlightFactory subscribeToUpdatesForFlightsWithNumber:airlineCode:date:updatesHandler:completionHandler:] : 148 -> 156
~ +[FUFlightFactory subscribeToUpdatesForFlightsWithNumber:airlineCode:date:completionHandler:] : 148 -> 156
~ +[FUFlightFactory fetchUpdateForChannelId:completionHandler:] : 148 -> 156
~ -[FUAirport isEqual:] : 916 -> 996
~ -[FUAirport copyWithZone:] : 304 -> 324
~ -[FUAirport description] : 172 -> 184
~ ___49-[FUAirport fetchPlacemarkWithCompletionHandler:]_block_invoke : 92 -> 96
~ ___49-[FUAirport fetchPlacemarkWithCompletionHandler:]_block_invoke_2 : 160 -> 168
~ -[FUAirport encodeWithCoder:] : 508 -> 556
~ -[FUAirport initWithCoder:] : 440 -> 468
~ -[FUAirport setTimeZone:] : 12 -> 64
~ +[FUFlightFactory_Parsec loadFlightsWithNumber:airlineCode:date:dateType:userAgent:sessionID:completionHandler:] : 260 -> 248
~ ___112+[FUFlightFactory_Parsec loadFlightsWithNumber:airlineCode:date:dateType:userAgent:sessionID:completionHandler:]_block_invoke : 512 -> 524
~ +[FUFlightFactory_Parsec validatedFlightNumber:airlineCode:error:] : 240 -> 256
~ +[FUFlightFactory_Parsec httpQuery:date:bundleIdentifier:userAgent:sessionID:completionHandler:] : 512 -> 524
~ ___96+[FUFlightFactory_Parsec httpQuery:date:bundleIdentifier:userAgent:sessionID:completionHandler:]_block_invoke : 240 -> 248
~ +[FUFlightFactory_Parsec loadFlightStructuresWithFlightNumber:airlineCode:date:dateType:userAgent:sessionID:completionHandler:] : 500 -> 492
~ ___127+[FUFlightFactory_Parsec loadFlightStructuresWithFlightNumber:airlineCode:date:dateType:userAgent:sessionID:completionHandler:]_block_invoke : 176 -> 184
~ +[FUFlightFactory_Parsec subscribeToUpdatesForFlightsWithNumber:airlineCode:date:completionHandler:] : 264 -> 268
~ +[FUFlightFactory_Parsec unsubscribeFromFlightUpdateChannel:] : 76 -> 80
~ sub_24faa53e8 -> sub_254a41f24 : 876 -> 880
~ sub_24faa5754 -> sub_254a42294 : 276 -> 252
~ sub_24faa5868 -> sub_254a42390 : 1340 -> 1328
~ sub_24faa5f14 -> sub_254a42a30 : 812 -> 792
~ sub_24faa6358 -> sub_254a42e60 : 324 -> 300
~ sub_24faa6500 -> sub_254a42ff0 : 416 -> 408
~ sub_24faa6778 -> sub_254a43260 : 368 -> 344
~ sub_24faa68e8 -> sub_254a433b8 : 388 -> 300
~ sub_24faa6a6c -> sub_254a434e4 : 280 -> 296
~ sub_24faa6ca4 -> sub_254a4372c : 304 -> 280
~ sub_24faa6dd4 -> sub_254a43844 : 432 -> 424
~ sub_24faa6f84 -> sub_254a439ec : 376 -> 356
~ sub_24faa7200 -> sub_254a43c54 : 564 -> 528
~ sub_24faa7564 -> sub_254a43f94 : 276 -> 252
~ sub_24faa7678 -> sub_254a44090 : 416 -> 408
~ sub_24faa7818 -> sub_254a44228 : 408 -> 388
~ sub_24faa79b0 -> sub_254a443ac : 500 -> 464
~ sub_24faa7c40 -> sub_254a44618 : 256 -> 264
~ sub_24faa7d40 -> sub_254a44720 : 388 -> 380
~ sub_24faa7ec4 -> sub_254a4489c : 184 -> 168
~ sub_24faa7f7c -> sub_254a44944 : 412 -> 376
~ sub_24faa8188 -> sub_254a44b2c : 52 -> 44
~ sub_24faa8434 -> sub_254a44dd0 : 244 -> 220
~ sub_24faa891c -> sub_254a452a0 : 248 -> 224
~ sub_24faa8ce0 -> sub_254a4564c : 800 -> 796
~ sub_24faa9000 -> sub_254a45968 : 276 -> 252
~ sub_24faa9114 -> sub_254a45a64 : 1444 -> 1408
~ sub_24faa9b6c -> sub_254a46498 : 800 -> 796
~ sub_24faa9e8c -> sub_254a467b4 : 276 -> 252
~ sub_24faa9fa0 -> sub_254a468b0 : 1300 -> 1296
~ sub_24faaa81c -> sub_254a47128 : 276 -> 252
~ sub_24faaa930 -> sub_254a47224 : 704 -> 672
~ sub_24faab2e8 -> sub_254a47bbc : 96 -> 88
~ sub_24faab70c -> sub_254a47fd8 : 104 -> 96
~ sub_24faab8b8 -> sub_254a4817c : 12 -> 8

```
