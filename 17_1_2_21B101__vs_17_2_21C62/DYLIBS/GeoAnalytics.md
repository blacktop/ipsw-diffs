## GeoAnalytics

> `/System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics`

```diff

-1940.31.8.9.13
-  __TEXT.__text: 0x9873c
-  __TEXT.__auth_stubs: 0x830
+1940.32.9.28.10
+  __TEXT.__text: 0x98550
+  __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_methlist: 0x182c
   __TEXT.__const: 0x518
   __TEXT.__gcc_except_tab: 0x3a8
   __TEXT.__cstring: 0xf593
   __TEXT.__oslogstring: 0x9c4
   __TEXT.__dlopen_cstrs: 0x126
-  __TEXT.__unwind_info: 0xdb4
+  __TEXT.__unwind_info: 0xdbc
   __TEXT.__objc_classname: 0x322
-  __TEXT.__objc_methname: 0x10d26
-  __TEXT.__objc_methtype: 0x16ac
-  __TEXT.__objc_stubs: 0xcf20
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__objc_methname: 0x10d6e
+  __TEXT.__objc_methtype: 0x16ce
+  __TEXT.__objc_stubs: 0xcf40
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x50d0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8

   __AUTH_CONST.__cfstring: 0x12340
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_intobj: 0xea0
+  __AUTH_CONST.__objc_intobj: 0xf00
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH_CONST.__auth_got: 0x430
+  __AUTH_CONST.__auth_got: 0x440
   __DATA.__got_weak: 0x10
   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x5a8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1364
-  Symbols:   5952
-  CStrings:  4676
+  Functions: 1365
+  Symbols:   5958
+  CStrings:  4677
 
Symbols:
+ +[GEOAPPortal captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:crowdsourcingDetails:arFailureTypes:]
+ +[GEOAPPortal captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:crowdsourcingDetails:arFailureTypes:additionalStates:providedDropRate:completionQueue:completionBlock:]
+ _GeoServicesConfig_VLFCrowdsourcingDataCollectionEnabled
+ ___281+[GEOAPPortal(UserAction) capturePlaceCardUserAction:target:value:mapItem:timestamp:resultIndex:targetID:providerID:animationID:actionURL:photoID:placeCardType:localizedMapItemCategory:availableActions:unactionableUIElements:modules:commingledRichProviderIds:actionRichProviderId:]_block_invoke_2
+ ___341+[GEOAPPortal captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:crowdsourcingDetails:arFailureTypes:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke
+ ___341+[GEOAPPortal captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:crowdsourcingDetails:arFailureTypes:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke_2
+ ___341+[GEOAPPortal captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:crowdsourcingDetails:arFailureTypes:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke_3
+ _geo_assert_reentrant_isolated
+ _geo_reentrant_isolate_sync
+ _geo_reentrant_isolater_create_with_format
+ _objc_msgSend$captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:crowdsourcingDetails:arFailureTypes:additionalStates:providedDropRate:completionQueue:completionBlock:
+ _objc_msgSend$setCrowdsourcingDetails:
+ _objc_msgSend$setIsOptedInToVlCrowdsourcing:
+ _objc_msgSend$stateImpressionObject
- +[GEOAPPortal captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:arFailureTypes:]
- +[GEOAPPortal captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:arFailureTypes:additionalStates:providedDropRate:completionQueue:completionBlock:]
- ___320+[GEOAPPortal captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:arFailureTypes:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke
- ___320+[GEOAPPortal captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:arFailureTypes:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke_2
- ___320+[GEOAPPortal captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:arFailureTypes:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke_3
- _geo_assert_isolated
- _objc_msgSend$captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:arFailureTypes:additionalStates:providedDropRate:completionQueue:completionBlock:
- _objc_msgSend$completedStep
- _objc_msgSend$stepFeedbacks
CStrings:
+ "@\"geo_reentrant_isolater\""
+ "captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:crowdsourcingDetails:arFailureTypes:"
+ "captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:crowdsourcingDetails:arFailureTypes:additionalStates:providedDropRate:completionQueue:completionBlock:"
+ "setCrowdsourcingDetails:"
+ "setIsOptedInToVlCrowdsourcing:"
+ "v132@0:8@16@24@32@40i48@52{GEOVLFPositionContextClassification=ddi{?=b1b1b1}}60@84@92@100@108@116@124"
+ "v164@0:8@16@24@32@40i48@52{GEOVLFPositionContextClassification=ddi{?=b1b1b1}}60@84@92@100@108@116@124@132@140@148@?156"
- "captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:arFailureTypes:"
- "captureVlfUsageWithEntryPoint:sessionTimeMs:timeRoundedToHour:localizationDetails:finalState:postFusionCorrection:initialPositionContextClassification:initialLocation:initializationFailureDetails:arStates:deviceOrientations:arFailureTypes:additionalStates:providedDropRate:completionQueue:completionBlock:"
- "completedStep"
- "stepFeedbacks"
- "v124@0:8@16@24@32@40i48@52{GEOVLFPositionContextClassification=ddi{?=b1b1b1}}60@84@92@100@108@116"
- "v156@0:8@16@24@32@40i48@52{GEOVLFPositionContextClassification=ddi{?=b1b1b1}}60@84@92@100@108@116@124@132@140@?148"

```
