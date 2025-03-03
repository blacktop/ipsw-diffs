## tipsd

> `/usr/libexec/tipsd`

```diff

-772.1.0.0.0
-  __TEXT.__text: 0x11024
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_stubs: 0x28a0
-  __TEXT.__objc_methlist: 0x764
-  __TEXT.__const: 0x1ba
-  __TEXT.__cstring: 0xc06
-  __TEXT.__objc_methname: 0x34f7
-  __TEXT.__oslogstring: 0x1293
-  __TEXT.__objc_classname: 0x1d5
-  __TEXT.__objc_methtype: 0xebe
-  __TEXT.__gcc_except_tab: 0x270
+778.4.2.0.0
+  __TEXT.__text: 0xf594
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__objc_stubs: 0x2320
+  __TEXT.__objc_methlist: 0xb5c
+  __TEXT.__const: 0x1b2
+  __TEXT.__cstring: 0xba6
+  __TEXT.__objc_methname: 0x2ed8
+  __TEXT.__oslogstring: 0x1020
+  __TEXT.__objc_classname: 0x1ac
+  __TEXT.__objc_methtype: 0xd68
+  __TEXT.__gcc_except_tab: 0x208
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x11b
+  __TEXT.__swift5_typeref: 0x14f
   __TEXT.__swift5_capture: 0xa8
   __TEXT.__constg_swiftt: 0x34
   __TEXT.__swift5_reflstr: 0x51
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x440
-  __TEXT.__eh_frame: 0x2e8
-  __DATA_CONST.__auth_got: 0x5b8
-  __DATA_CONST.__got: 0x378
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0x10
+  __TEXT.__unwind_info: 0x400
+  __TEXT.__eh_frame: 0x2d8
+  __DATA_CONST.__auth_got: 0x5b0
+  __DATA_CONST.__got: 0x330
   __DATA_CONST.__auth_ptr: 0xc0
-  __DATA_CONST.__const: 0x840
-  __DATA_CONST.__cfstring: 0x840
+  __DATA_CONST.__const: 0x808
+  __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x13d8
-  __DATA.__objc_selrefs: 0xc38
+  __DATA.__objc_const: 0xb10
+  __DATA.__objc_selrefs: 0xbf0
   __DATA.__objc_ivar: 0x5c
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0x6b0
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x660
   __DATA.__common: 0x18
   __DATA.__bss: 0x200
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 315
-  Symbols:   357
-  CStrings:  820
+  Functions: 306
+  Symbols:   341
+  CStrings:  745
 
Symbols:
+ _$ss5ErrorP8TipsCoreE015secureEncodableA0sAA_pyF
- _NSLocalizedDescriptionKey
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSMutableArray
- _OBJC_CLASS_$_TPSAnalyticsEventContentRetrieved
- _OBJC_CLASS_$_TPSMiniTipMetadata
- _TPSAnalyticsDaemonActiveReasonTipKitConnection
- _TPSAnalyticsDismissTypeByClient
- _TPSAnalyticsDismissTypeByUser
- _TPSAnalyticsDismissTypeDesiredOutcome
- _TPSAnalyticsDismissTypeDismissalEventOccurred
- _TPSAnalyticsDismissTypeHintMaxDisplayedCountExceeded
- _TPSAnalyticsDismissTypeRestartTrackingDisplayEventOccurred
- _TPSAnalyticsDismissTypeUnknown
- _TPSMiniTipContentManagerServiceInterfaceServerInterface
- __swift_FORCE_LOAD_$_swiftFileProvider
- _kTPSMiniTipContentManagerServiceInterfaceErrorDomain
- _objc_retain_x25
CStrings:
+ "New connection coming in: %@, standardAccess %d, appAccess %d, device expert access %d"
+ "RegisteredDeliveryEventIdentifiers"
- "%@: %ld"
- "@32@0:8q16@24"
- "Checking experiment camp for %@"
- "Checking language changes for %@"
- "Checking preconditions for %@"
- "Content (%@) ineligible due to reason: %@"
- "Content does not contain body text"
- "Content language code (%@) does not match user preferred language (%@)"
- "Discoverability connection established. %@"
- "Discoverability xpc connection invalidated"
- "Fetching for content %@"
- "Hint %@ marked ineligible with dismissType %@"
- "Hint already marked as ineligible for %@"
- "Invalid Content ID"
- "Mini tip is not valid due to %@"
- "Mini tip metadata %@"
- "New connection coming in: %@, standardAccess %d, appAccess %d, discoverability access %d, device expert access %d"
- "Overriding ineligibility due to content %@ already seen on other devices"
- "TPSMiniTipContentManagerServiceInterface"
- "Vv40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
- "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32q40"
- "Vv48@0:8@16@24@32q40"
- "_errorForHintIneligibleReason:contentID:"
- "arrayWithCapacity:"
- "bodyContent"
- "bodyText"
- "bundleIDForIdentifier:"
- "com.apple.bluetooth.pairing"
- "com.apple.private.tipsd.discoverability"
- "contentWithContentIdentifiers:bundleID:context:completionHandler:"
- "contextualTipsInactive"
- "customizationIDForContentID:"
- "dictionaryWithObjects:forKeys:count:"
- "discoverability"
- "displayBundleID"
- "displayStatusCheckForHintIneligibleReasonWithContent:context:bypassExperiment:"
- "donateContentRetrieved:bundleID:context:error:"
- "eventWithTipID:correlationID:bundleID:context:serviceError:"
- "hintDismissedForIdentifier:bundleID:context:reason:"
- "hintInelgibileReasonForIdentifier:"
- "ignoreCloud"
- "ineligibleReasonStringForReason:"
- "initWithContent:"
- "isContentHintDisplayMaxDisplayedCountExceededForIdentifier:"
- "isContentIdentifierHoldoutCamp:"
- "isContextualInfoExistForIdentifier:"
- "isHintInelgibileForIdentifier:"
- "isLocalContent"
- "isPreconditionMatchedForIdentifier:"
- "isPreconditionValidForIdentifier:preconditionDictionary:"
- "miniContent"
- "miniTipMetadataForContent:bundleID:context:"
- "monitoringEventsForContentID:"
- "personalizationFailedForContentID:bundleID:context:"
- "preconditions"
- "q24@0:8@16"
- "q36@0:8@16@24B32"
- "restartTrackingForContentIdentifiers %@"
- "restartTrackingForContentIdentifiers:"
- "restartTriggerTrackingIfNotDisplayedForIdentifier:"
- "restartTriggerTrackingIfNotDisplayedForIdentifiers:"
- "setCustomizationID:"
- "setError:"
- "setMonitoringEvents:"
- "setUserInfo:"
- "statusCheckForHintIneligibleReasonWithContentID:"
- "updateHintDismissedForIdentifier:dismissType:context:"
- "updateHintWouldHaveBeenDisplayedForIdentifier:context:"
- "userInfoForIdentifier:"
- "userLanguageCode"
- "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v48@0:8@16@24@32@40"
- "v52@0:8@16@\"NSString\"24@\"NSString\"32B40@?<v@?B@@\"NSError\">44"
- "v52@0:8@16@24@32B40@?44"
- "validateAndPrepareContentForDisplay"
- "validateAndPrepareContentForDisplay:bundleID:context:skipUsageCheck:completionHandler:"
- "variantIdentifierForIdentifier:"

```
