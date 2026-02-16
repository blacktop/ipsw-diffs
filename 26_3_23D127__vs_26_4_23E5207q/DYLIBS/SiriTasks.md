## SiriTasks

> `/System/Library/PrivateFrameworks/SiriTasks.framework/SiriTasks`

```diff

-3515.3.1.0.0
-  __TEXT.__text: 0xb768
-  __TEXT.__auth_stubs: 0x390
+3520.84.5.1.6
+  __TEXT.__text: 0xcaa8
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_methlist: 0x1ac8
   __TEXT.__const: 0x28
   __TEXT.__cstring: 0xec5
   __TEXT.__oslogstring: 0x8c
-  __TEXT.__unwind_info: 0x4b8
+  __TEXT.__unwind_info: 0x508
   __TEXT.__objc_classname: 0x50e
   __TEXT.__objc_methname: 0x23d6
   __TEXT.__objc_methtype: 0x445

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x9f8
   __DATA_CONST.__objc_superrefs: 0x180
-  __AUTH_CONST.__auth_got: 0x1d0
+  __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x16e0
   __AUTH_CONST.__objc_const: 0x37a8

   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8FE2416D-08A8-3E33-B2CE-EC1ECC095EFB
+  UUID: 1DC7B279-CAD2-3DDC-967F-BA4FB50EB6FA
   Functions: 495
-  Symbols:   1843
+  Symbols:   1840
   CStrings:  1001
 
Symbols:
+ _objc_autorelease
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutorelease
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x25
- _objc_retain_x3
Functions:
~ -[STMapItem initWithCoder:] : 408 -> 428
~ -[STMapItem _aceContextObjectValue] : 500 -> 508
~ -[STMapItem initWithMKMapItem:] : 436 -> 464
~ ___31-[STMapItem initWithMKMapItem:]_block_invoke : 84 -> 88
~ -[STUpdateAlarmAction initWithCoder:] : 152 -> 156
~ -[STUpdateAlarmAction modifications] : 16 -> 64
~ -[STMapViewport initWithCoder:] : 452 -> 464
~ -[STMapViewport _aceContextObjectValue] : 516 -> 520
~ -[STDeleteAlarmAction initWithCoder:] : 152 -> 156
~ -[STDeleteAlarmAction alarmIds] : 16 -> 64
~ -[STDeleteAlarmAction _initWithAlarmIds:] : 212 -> 208
~ -[STShowDraftMessageUsageResult description] : 164 -> 172
~ -[STWeatherAttributes initWithCoder:] : 348 -> 364
~ -[STWeatherAttributes chanceOfPrecipitation] : 16 -> 64
~ -[STWeatherAttributes lowTemperature] : 16 -> 64
~ -[STWeatherAttributes highTemperature] : 16 -> 64
~ -[STWeatherAttributes temperature] : 16 -> 64
~ -[STWeatherAttributes _initWithCondition:temperature:highTemperature:lowTemperature:chanceOfPrecipitation:] : 272 -> 256
~ -[STShowMessageRequest initWithCoder:] : 180 -> 184
~ -[STShowMessageRequest message] : 16 -> 64
~ -[STEmailMessage setReceivingAddresses:] : 20 -> 80
~ -[STEmailMessage setBccRecipients:] : 20 -> 80
~ -[STEmailMessage setCcRecipients:] : 20 -> 80
~ -[STEmailMessage setToRecipients:] : 20 -> 80
~ -[STEmailMessage setSender:] : 20 -> 80
~ -[STEmailMessage setMessageIdentifier:] : 20 -> 80
~ -[STEmailMessage initWithCoder:] : 916 -> 980
~ -[STEmailMessage _personAttributesForRecipients:] : 840 -> 888
~ -[STEmailMessage _aceContextObjectValue] : 516 -> 536
~ -[STAlarmShowAlarmAndPerformActionRequest initWithCoder:] : 152 -> 156
~ -[STAlarmShowAlarmAndPerformActionRequest action] : 16 -> 64
~ -[STAlarmShowAlarmAndPerformActionRequest _initWithAction:] : 212 -> 208
~ -[STGenericIntentDateRange initWithCoder:] : 248 -> 260
~ -[STGenericIntentDateRange encodeWithCoder:] : 128 -> 136
~ -[STGenericIntentLocation initWithCoder:] : 208 -> 212
~ -[STGenericIntentLocation encodeWithCoder:] : 148 -> 156
~ -[STGenericIntentLocation initWithName:latitude:longitude:] : 136 -> 128
~ -[STGenericIntentGroup initWithCoder:] : 148 -> 152
~ -[STGenericIntentTopic initWithCoder:] : 148 -> 152
~ -[STGenericIntentPerson initWithCoder:] : 148 -> 152
~ -[STGenericIntent setIntentRequest:] : 12 -> 64
~ -[STGenericIntent setSiriTask:] : 12 -> 64
~ -[STGenericIntent setParameters:] : 12 -> 64
~ -[STGenericIntent initWithCoder:] : 520 -> 544
~ -[STGenericIntent encodeWithCoder:] : 148 -> 156
~ -[STGenericIntent getPlacesParameter:] : 108 -> 116
~ -[STGenericIntent getGroupParameter:] : 108 -> 116
~ -[STGenericIntent getPersonParameter:] : 108 -> 116
~ -[STGenericIntent getTopicParameter:] : 108 -> 116
~ -[STGenericIntent getDateRangeParameter:] : 108 -> 116
~ -[STGenericIntent handleWithProgress:] : 172 -> 180
~ ___38-[STGenericIntent handleWithProgress:]_block_invoke : 200 -> 216
~ -[STGenericIntentHelper setWaitForIntentCompleteSemaphore:] : 12 -> 64
~ -[STGenericIntentHelper setSiriResponseQueue:] : 12 -> 64
~ -[STGenericIntentHelper setHandlers:] : 12 -> 64
~ -[STGenericIntentHelper _invokeHandlerForIntent:] : 392 -> 404
~ -[STGenericIntentHelper forIntent:registerHandler:] : 200 -> 188
~ _initINVocabularyUpdater : 84 -> 100
~ _INVocabularyUpdaterFunction : 12 -> 60
~ -[STGenericIntentHelper _handleIntent:withTask:andApplication:] : 2516 -> 2708
~ -[STGenericIntentHelper handleSiriTask:withApplication:] : 252 -> 240
~ ___56-[STGenericIntentHelper handleSiriTask:withApplication:]_block_invoke : 240 -> 244
~ ___43-[STGenericIntentHelper finishedLaunching:]_block_invoke_2 : 68 -> 72
~ -[STGenericIntentHelper init] : 244 -> 256
~ +[STGenericIntentHelper sharedHelper] : 84 -> 100
~ ___27-[STGenericIntent finished]_block_invoke : 96 -> 104
~ -[STGenericIntent initWithName:] : 148 -> 144
~ -[STCreateAlarmAction initWithCoder:] : 152 -> 156
~ -[STCreateAlarmAction alarm] : 16 -> 64
~ -[STCreateAlarmAction _initWithAlarm:] : 212 -> 208
~ -[STShowChannelRequest initWithCoder:] : 152 -> 156
~ -[STTimerShowTimerAndPerformAction initWithCoder:] : 448 -> 472
~ -[STTimerShowTimerAndPerformAction _initWithTimers:templateActions:timerAction:] : 188 -> 184
~ -[STTimerShowTimerAndPerformAction _initWithTimer:action:] : 160 -> 164
~ -[STShowAlarmAction initWithCoder:] : 152 -> 156
~ -[STShowAlarmAction alarmIds] : 16 -> 64
~ -[STShowAlarmAction _initWithAlarmIds:] : 212 -> 208
~ -[STSurfPaymentAction initWithCoder:] : 152 -> 156
~ -[STSurfPaymentAction action] : 188 -> 204
~ -[STSurfPaymentAction interaction] : 16 -> 64
~ -[STGenericIntentResponse description] : 156 -> 164
~ -[STShowDailyWeatherForecastRequest initWithCoder:] : 420 -> 440
~ -[STShowDailyWeatherForecastRequest city] : 16 -> 64
~ -[STShowDailyWeatherForecastRequest dailyAttributes] : 16 -> 64
~ -[STShowDailyWeatherForecastRequest currentAttributes] : 16 -> 64
~ -[STShowDailyWeatherForecastRequest _initWithCurrentAttributes:dailyAttributes:city:startWeekday:] : 236 -> 224
~ -[STShowWeatherConditionsRequest initWithCoder:] : 208 -> 216
~ -[STShowWeatherConditionsRequest city] : 16 -> 64
~ -[STShowWeatherConditionsRequest attributes] : 16 -> 64
~ -[STShowWeatherConditionsRequest _initWithAttributes:city:] : 168 -> 160
~ -[STShowMapsSearchResultsRequest initWithCoder:] : 264 -> 276
~ -[STShowMapsSearchResultsRequest extSessionGuidCreatedTimestamp] : 16 -> 64
~ -[STShowMapsSearchResultsRequest extSessionGuid] : 16 -> 64
~ -[STShowMapsSearchResultsRequest searchResults] : 16 -> 64
~ -[STShowMapsSearchResultsRequest _initWithLocation:extSessionGuid:extSessionGuidCreatedTimestamp:] : 212 -> 204
~ -[STShowStockOverviewRequest initWithCoder:] : 580 -> 616
~ -[STShowStockOverviewRequest chartData] : 16 -> 64
~ -[STShowStockOverviewRequest changePercent] : 16 -> 64
~ -[STShowStockOverviewRequest change] : 16 -> 64
~ -[STShowStockOverviewRequest low] : 16 -> 64
~ -[STShowStockOverviewRequest high] : 16 -> 64
~ -[STShowStockOverviewRequest price] : 16 -> 64
~ -[STShowStockOverviewRequest exchange] : 16 -> 64
~ -[STShowStockOverviewRequest symbol] : 16 -> 64
~ -[STShowStockOverviewRequest name] : 16 -> 64
~ -[STShowStockOverviewRequest _initWithName:symbol:exchange:price:high:low:change:changePercent:chartData:] : 464 -> 472
~ -[STStartNavigationRequest initWithCoder:] : 456 -> 480
~ -[STStartNavigationRequest extSessionGuidCreatedTimestamp] : 16 -> 64
~ -[STStartNavigationRequest extSessionGuid] : 16 -> 64
~ -[STStartNavigationRequest departureDate] : 16 -> 64
~ -[STStartNavigationRequest arrivalDate] : 16 -> 64
~ -[STStartNavigationRequest destinationLocation] : 16 -> 64
~ -[STStartNavigationRequest startLocation] : 16 -> 64
~ -[STStartNavigationRequest _initWithStartLocation:destinationLocation:directionsType:arrivalDate:departureDate:extSessionGuid:extSessionGuidCreatedTimestamp:] : 360 -> 344
~ -[STSendEmailRequest initWithCoder:] : 152 -> 156
~ -[STSendEmailRequest message] : 16 -> 64
~ -[STWatchFace _aceContextObjectValue] : 228 -> 240
~ -[STAlarmModification initWithCoder:] : 432 -> 452
~ -[STAlarmModification minute] : 16 -> 64
~ -[STAlarmModification label] : 16 -> 64
~ -[STAlarmModification hour] : 16 -> 64
~ -[STAlarmModification enabled] : 16 -> 64
~ -[STAlarmModification alarmId] : 16 -> 64
~ -[STAlarmModification _initWithAddedFrequency:alarmId:enabled:hour:label:minute:removedFrequency:] : 436 -> 408
~ -[STShowWeatherForecastRequest initWithCoder:] : 480 -> 504
~ -[STShowWeatherForecastRequest units] : 16 -> 64
~ -[STShowWeatherForecastRequest city] : 16 -> 64
~ -[STShowWeatherForecastRequest hourlyForecasts] : 16 -> 64
~ -[STShowWeatherForecastRequest currentConditions] : 16 -> 64
~ -[STShowWeatherForecastRequest _initWithCurrentConditions:hourlyForecasts:city:units:forecastType:] : 272 -> 264
~ -[STReminderListObject initWithCoder:] : 152 -> 156
~ -[STReminderListObject setName:] : 20 -> 72
~ -[STReminderListObject name] : 16 -> 64
~ -[STReminderListObject _aceValue] : 172 -> 184
~ -[STShowMapPointRequest initWithCoder:] : 292 -> 304
~ -[STShowMapPointRequest extSessionGuidCreatedTimestamp] : 16 -> 64
~ -[STShowMapPointRequest extSessionGuid] : 16 -> 64
~ -[STShowMapPointRequest mapPointData] : 16 -> 64
~ -[STShowMapPointRequest _initWithPlaceData:extSessionGuid:extSessionGuidCreatedTimestamp:] : 212 -> 204
~ -[STMapViewportVertex encodeWithCoder:] : 116 -> 124
~ -[STSendDraftMessageRequest initWithCoder:] : 152 -> 156
~ -[STSendDraftMessageRequest message] : 16 -> 64
~ -[STWeatherCurrentConditions initWithCoder:] : 292 -> 304
~ -[STWeatherCurrentConditions lowTemperature] : 16 -> 64
~ -[STWeatherCurrentConditions highTemperature] : 16 -> 64
~ -[STWeatherCurrentConditions temperature] : 16 -> 64
~ -[STWeatherCurrentConditions _initWithConditionCode:temperature:highTemperature:lowTemperature:] : 228 -> 220
~ -[STUpdateWatchListRequest initWithCoder:] : 424 -> 448
~ -[STWeatherHourlyForecast initWithCoder:] : 268 -> 276
~ -[STWeatherHourlyForecast chanceOfPrecipitation] : 16 -> 64
~ -[STWeatherHourlyForecast temperature] : 16 -> 64
~ -[STWeatherHourlyForecast _initWithConditionCodeIndex:timeIndex:temperature:chanceOfPrecipitation:] : 208 -> 200
~ -[STStartWorkoutRequest initWithCoder:] : 324 -> 328
~ _initHKQuantity : 84 -> 100
~ _HKQuantityFunction : 12 -> 60
~ -[STStartWorkoutRequest workoutGoal] : 16 -> 64
~ -[STStartWorkoutRequest _initWithType:location:goal:goalType:userMode:isOpenGoal:skipActivitySetup:] : 248 -> 240
~ -[STShowWeatherCurrentConditionsRequest initWithCoder:] : 264 -> 276
~ -[STShowWeatherCurrentConditionsRequest units] : 16 -> 64
~ -[STShowWeatherCurrentConditionsRequest city] : 16 -> 64
~ -[STShowWeatherCurrentConditionsRequest currentConditions] : 16 -> 64
~ -[STShowWeatherCurrentConditionsRequest _initWithCurrentConditions:city:units:] : 212 -> 204
~ -[STGenericIntentRequest initWithCoder:] : 280 -> 292
~ -[STGenericIntentRequest info] : 16 -> 64
~ -[STGenericIntentRequest utterance] : 16 -> 64
~ -[STGenericIntentRequest intentString] : 16 -> 64
~ -[STGenericIntentRequest appIdentifier] : 16 -> 64
~ -[STGenericIntentRequest initWithAppIdentifier:intentString:utterance:info:] : 280 -> 268
~ -[STGenericIntentRequest(AFAnalytics) _af_analyticsContextDescription] : 320 -> 340
~ _STStringFromGenericIntentResponseCode : 144 -> 152
~ -[STMediaChannel setStreamUrl:] : 20 -> 80
~ -[STMediaChannel initWithCoder:] : 320 -> 336
~ -[STShowHourlyWeatherForecastRequest initWithCoder:] : 448 -> 468
~ -[STShowHourlyWeatherForecastRequest city] : 16 -> 64
~ -[STShowHourlyWeatherForecastRequest hourlyAttributes] : 16 -> 64
~ -[STShowHourlyWeatherForecastRequest currentAttributes] : 16 -> 64
~ -[STShowHourlyWeatherForecastRequest _initWithCurrentAttributes:hourlyAttributes:city:startHour:forecastType:] : 252 -> 248
~ -[STShowDraftMessageRequest initWithCoder:] : 152 -> 156
~ -[STShowDraftMessageRequest createUsageResult] : 104 -> 108
~ -[STShowDraftMessageRequest draftMessageIdentifier] : 16 -> 64

```
