## InAppMessagesCore

> `/System/Library/PrivateFrameworks/InAppMessagesCore.framework/InAppMessagesCore`

```diff

 4024.100.3.0.0
-  __TEXT.__text: 0x37ec
-  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__text: 0x3a44
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x72c
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x45f
-  __TEXT.__gcc_except_tab: 0x6c
+  __TEXT.__gcc_except_tab: 0x60
   __TEXT.__oslogstring: 0x33
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__unwind_info: 0x1a8
   __TEXT.__objc_classname: 0x11e
   __TEXT.__objc_methname: 0x14f4
   __TEXT.__objc_methtype: 0x29c

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x668
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x188
+  __AUTH_CONST.__auth_got: 0x160
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__objc_const: 0x13d0

   - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A7158D62-57C0-3946-AF8A-E6B2621949E5
+  UUID: 45F3763C-47F3-3909-886F-95B53CBBE7B0
   Functions: 120
-  Symbols:   665
+  Symbols:   660
   CStrings:  475
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ _IAMLogCategoryDefault : 68 -> 84
~ -[ICIAMMetricEvent(Metrics) reportableDictionary] : 268 -> 288
~ -[ICIAMMetricEvent(Metrics) reportableDictionaryForClickEventWithMessageIdentifier:andTargetIdentifier:] : 240 -> 248
~ -[NSArray(Utilities) iam_map:] : 228 -> 240
~ ___30-[NSArray(Utilities) iam_map:]_block_invoke : 132 -> 144
~ -[NSArray(Utilities) iam_compactMap:] : 228 -> 240
~ ___37-[NSArray(Utilities) iam_compactMap:]_block_invoke : 104 -> 108
~ -[NSArray(Utilities) iam_dictionaryFromArrayOfICIIAMParameters] : 404 -> 420
~ -[ICInAppMessageMetadataEntry(Utilities) numberOfDisplays] : 64 -> 68
~ -[ICInAppMessageMetadataEntry(Utilities) setNumberOfDisplays:] : 100 -> 104
~ -[ICInAppMessageMetadataEntry(Utilities) didCancelUserNotification] : 64 -> 68
~ -[ICInAppMessageMetadataEntry(Utilities) setDidCancelUserNotification:] : 100 -> 104
~ -[IAMImpression initWithMessageEntry:targetIdentifier:] : 152 -> 148
~ -[IAMImpression messageIdentifier] : 80 -> 88
~ -[IAMImpression messageType] : 60 -> 64
~ _IAMLogCategoryDefault_Oversize : 68 -> 84
~ -[IAMImpression(Metrics) reportableMetricsEventDictionary] : 1020 -> 1112
~ ___48-[NSDictionary(IAMSubset) isSubsetOfDictionary:]_block_invoke : 348 -> 360
~ -[IAMDecomposedKey constructCompoundPredicateIfNeeded] : 140 -> 144
~ ___54-[IAMDecomposedKey constructCompoundPredicateIfNeeded]_block_invoke : 300 -> 304
~ -[IAMDecomposedKey setRuleDestructuredIdentifiers:] : 12 -> 64
~ -[IAMEvent matchesWithKey:] : 88 -> 92
~ -[IAMValueEvent initWithName:value:] : 168 -> 164
~ -[IAMValueEvent value] : 16 -> 8
~ -[IAMValueEvent setValue:] : 12 -> 8
~ -[IAMValueEvent .cxx_destruct] : 20 -> 12
~ -[IAMFigaroEvent name] : 92 -> 100
~ -[IAMFigaroEvent matchesWithKey:] : 372 -> 412
~ -[IAMFigaroEvent decomposeKey:] : 772 -> 820
~ -[IAMFigaroEvent serializeFigaroEventProperties:withPrefix:] : 384 -> 376
~ ___60-[IAMFigaroEvent serializeFigaroEventProperties:withPrefix:]_block_invoke : 384 -> 404
~ -[IAMApplicationDidBecomeActiveEvent initWithName:] : 120 -> 124
~ -[IAMApplicationDidBecomeActiveEvent initWithName:type:] : 120 -> 124
~ -[IAMContent initWithTitle:subtitle:body:images:actions:contentParameters:identifier:] : 308 -> 292
~ -[IAMContent initWithICMessageContent:] : 380 -> 420
~ -[IAMMessage initWithIdentifier:messageGroupIdentifier:contentPages:requiresCloseButton:] : 208 -> 200
~ -[IAMMessage initWithICInAppMessageEntry:] : 236 -> 256
~ -[ICIAMMessageContent(Metrics) dictionaryRepresentationWithReportableMetricsEvents] : 656 -> 692
~ -[IAMAction initWithIdentifier:displayText:url:requiresDelegate:actionParameters:] : 244 -> 228
~ -[IAMAction initWithICAction:] : 280 -> 304
~ -[IAMTempTestMessages initWithDisplayType:] : 1780 -> 1832
~ -[IAMTempTestMessages setMessageEntry:] : 12 -> 64
~ -[IAMImage initWithIdentifier:url:] : 156 -> 152
~ -[IAMImage initWithIdentifier:url:width:height:] : 176 -> 172
~ -[IAMImage initWithICImage:] : 216 -> 228
~ -[ICIAMMessageAction(Metrics) dictionaryRepresentationWithReportableMetricsEvents] : 168 -> 180

```
