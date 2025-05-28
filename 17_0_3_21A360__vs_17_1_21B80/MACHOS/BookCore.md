## BookCore

> `/private/var/staged_system_apps/Books.app/Frameworks/BookCore.framework/BookCore`

```diff

-5919.0.0.0.0
-  __TEXT.__text: 0x1fb2f0
-  __TEXT.__auth_stubs: 0x3f60
-  __TEXT.__objc_stubs: 0x306a0
-  __TEXT.__objc_methlist: 0x1c704
-  __TEXT.__cstring: 0x13db7
+5983.0.0.0.0
+  __TEXT.__text: 0x1fd494
+  __TEXT.__auth_stubs: 0x3fe0
+  __TEXT.__objc_stubs: 0x306e0
+  __TEXT.__objc_methlist: 0x1c70c
+  __TEXT.__cstring: 0x13ef7
   __TEXT.__objc_classname: 0x42c0
-  __TEXT.__objc_methname: 0x4887a
+  __TEXT.__objc_methname: 0x48926
   __TEXT.__objc_methtype: 0xb4ad
-  __TEXT.__const: 0x2614
-  __TEXT.__gcc_except_tab: 0x324c
-  __TEXT.__oslogstring: 0x8cb8
+  __TEXT.__const: 0x2744
+  __TEXT.__gcc_except_tab: 0x3294
+  __TEXT.__oslogstring: 0x8d56
   __TEXT.__ustring: 0x48
-  __TEXT.__swift5_typeref: 0x1274
-  __TEXT.__constg_swiftt: 0x130c
+  __TEXT.__swift5_typeref: 0x12c2
+  __TEXT.__constg_swiftt: 0x1330
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0xaaa
-  __TEXT.__swift5_fieldmd: 0xc38
-  __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__swift5_proto: 0xd8
-  __TEXT.__swift5_types: 0xf8
-  __TEXT.__swift5_capture: 0xb60
+  __TEXT.__swift5_reflstr: 0xada
+  __TEXT.__swift5_fieldmd: 0xc90
+  __TEXT.__swift5_assocty: 0x120
+  __TEXT.__swift5_proto: 0xec
+  __TEXT.__swift5_types: 0xfc
+  __TEXT.__swift5_capture: 0xb74
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x86f0
-  __TEXT.__eh_frame: 0xc08
-  __DATA_CONST.__auth_got: 0x1fc8
-  __DATA_CONST.__got: 0xbe8
+  __TEXT.__unwind_info: 0x8940
+  __TEXT.__eh_frame: 0xd90
+  __DATA_CONST.__auth_got: 0x2008
+  __DATA_CONST.__got: 0xbf8
   __DATA_CONST.__auth_ptr: 0x90
-  __DATA_CONST.__const: 0xabc8
-  __DATA_CONST.__cfstring: 0x11960
+  __DATA_CONST.__const: 0xaca0
+  __DATA_CONST.__cfstring: 0x119a0
   __DATA_CONST.__objc_classlist: 0xf18
   __DATA_CONST.__objc_catlist: 0x150
   __DATA_CONST.__objc_protolist: 0x6e0

   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x3688
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA_CONST.__objc_doubleobj: 0xb0
-  __DATA.__objc_const: 0x3c258
-  __DATA.__objc_selrefs: 0x10508
+  __DATA_CONST.__objc_doubleobj: 0xc0
+  __DATA.__objc_const: 0x3c298
+  __DATA.__objc_selrefs: 0x10520
   __DATA.__objc_protorefs: 0x230
-  __DATA.__objc_classrefs: 0x1220
+  __DATA.__objc_classrefs: 0x1228
   __DATA.__objc_superrefs: 0x938
   __DATA.__objc_ivar: 0x1e6c
   __DATA.__objc_data: 0xa3c0
-  __DATA.__data: 0x6b38
-  __DATA.__bss: 0x5b30
+  __DATA.__data: 0x6d28
+  __DATA.__bss: 0x5db0
   __DATA.__common: 0x28
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration
+  - /System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib

   - @rpath/BookAnalytics.framework/BookAnalytics
   - @rpath/JSApp.framework/JSApp
   - @rpath/TemplateUI.framework/TemplateUI
-  Functions: 14144
-  Symbols:   3457
-  CStrings:  17525
+  Functions: 14194
+  Symbols:   3461
+  CStrings:  17542
 
Symbols:
+ _BCInvalidationWindowForSamplesOverride
+ _BCJSInvalidationWindowForSamplesKey
+ _OBJC_CLASS_$_TFCapabilities
+ _kBCBookReadingTimesThresholdForPurgingSamplesFromRecents
CStrings:
+ "B44@0:8@16q24@32i40"
+ "BCDragRepresentationFactory.m"
+ "BCInvalidationWindowForSamplesOverride"
+ "BCJSInvalidationWindowForSamplesKey"
+ "BKSeriesManager.m"
+ "BKSeriesManagerUpdater.m"
+ "Purge Tracking: %lu expired books: %@"
+ "Purge Tracking: One or both oldest date missing oldestDateToAvoidPurgeOfSamples=%@ oldestDateToAvoidPurgeOfNonSamples=%@"
+ "Purge Tracking: update launch tracking for %lu assets"
+ "all"
+ "analytics.jitterTimestampEnabled2"
+ "checkAvailabilityForStoreID:type:fileID:line:"
+ "fetchMixedAssetsWithBookIds:audiobookIds:relationships:views:additionalParameters:batchSize:fileID:line:completionHandler:"
+ "fetchMixedSeriesWithBookSeriesIds:audiobookSeriesIds:relationships:views:additionalParameters:batchSize:fileID:line:completionHandler:"
+ "fetchResourcesWithAdamIDs:relationships:views:additionalParameters:batchSize:fileID:line:completionHandler:"
+ "fetchStoreURLForAdamID:type:fileID:line:completionHandler:"
+ "fetchStoreURLOfUnknownTypeForAdamID:fileID:line:completionHandler:"
+ "genreName"
+ "internal"
+ "isInternalBuild"
+ "oldestDateToAvoidPurgeOfBooks"
+ "oldestDateToAvoidPurgeOfSamples"
+ "ppt"
+ "public"
+ "readingNow.featureReadNowEnabled"
+ "readingNow.readNowEnablementLevel"
+ "recentsNotEngagedSinceDateForSamples:dateForNonSamples:completion:"
+ "seed"
+ "v44@0:8@\"NSString\"16@\"NSString\"24i32@?<v@?@\"NSURL\"@\"NSError\">36"
+ "v52@0:8@\"NSString\"16q24@\"NSString\"32i40@?<v@?@\"NSURL\"@\"NSError\">44"
- "B32@0:8@16q24"
- "Purge Tracking: No oldestDateToAvoidPurge... skipping."
- "analytics.jitterTimestampEnabled"
- "checkAvailabilityForStoreID:type:"
- "fetchMixedAssetsWithBookIds:audiobookIds:relationships:views:additionalParameters:batchSize:completionHandler:"
- "fetchMixedSeriesWithBookSeriesIds:audiobookSeriesIds:relationships:views:additionalParameters:batchSize:completionHandler:"
- "fetchResourcesWithAdamIDs:relationships:views:additionalParameters:batchSize:completionHandler:"
- "fetchStoreURLForAdamID:type:completionHandler:"
- "fetchStoreURLOfUnknownTypeForAdamID:completionHandler:"
- "oldestDateToAvoidPurge"
- "recentsNotEngagedSince:completion:"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSURL\"@\"NSError\">24"
- "v40@0:8@\"NSString\"16q24@?<v@?@\"NSURL\"@\"NSError\">32"

```
