## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-64.216.0.0.0
-  __TEXT.__text: 0x28e84
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x1e8c
+64.218.0.0.0
+  __TEXT.__text: 0x2985c
+  __TEXT.__auth_stubs: 0x9f0
+  __TEXT.__objc_methlist: 0x1f14
   __TEXT.__const: 0x1b0
   __TEXT.__cstring: 0x2329
-  __TEXT.__oslogstring: 0x3216
+  __TEXT.__oslogstring: 0x32e6
   __TEXT.__gcc_except_tab: 0x2a8
-  __TEXT.__swift5_typeref: 0xa7
+  __TEXT.__swift5_typeref: 0x9f
   __TEXT.__swift5_capture: 0x88
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x800
+  __TEXT.__unwind_info: 0x7f8
   __TEXT.__eh_frame: 0x2e8
-  __TEXT.__objc_classname: 0x43f
-  __TEXT.__objc_methname: 0x4ea0
-  __TEXT.__objc_methtype: 0x6da
-  __TEXT.__objc_stubs: 0x3d00
-  __DATA_CONST.__got: 0x970
-  __DATA_CONST.__const: 0x920
-  __DATA_CONST.__objc_classlist: 0x130
+  __TEXT.__objc_classname: 0x45e
+  __TEXT.__objc_methname: 0x51ab
+  __TEXT.__objc_methtype: 0x6fd
+  __TEXT.__objc_stubs: 0x3fa0
+  __DATA_CONST.__got: 0x9a0
+  __DATA_CONST.__const: 0x918
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10e0
+  __DATA_CONST.__objc_selrefs: 0x1190
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x540
-  __AUTH_CONST.__auth_ptr: 0x90
+  __AUTH_CONST.__auth_got: 0x508
+  __AUTH_CONST.__auth_ptr: 0x88
   __AUTH_CONST.__const: 0x788
-  __AUTH_CONST.__cfstring: 0x2340
-  __AUTH_CONST.__objc_const: 0x3e78
+  __AUTH_CONST.__cfstring: 0x2360
+  __AUTH_CONST.__objc_const: 0x4008
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x4a0
+  __AUTH.__objc_data: 0x4f0
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x2ac
-  __DATA.__data: 0x350
+  __DATA.__objc_ivar: 0x2c0
+  __DATA.__data: 0x348
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/Anvil.framework/Anvil
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 939
-  Symbols:   421
-  CStrings:  1543
+  Functions: 949
+  Symbols:   430
+  CStrings:  1580
 
Symbols:
+ _BiomeLibrary
+ _IAPayloadKeyWritingToolsSlot
+ _IAPayloadKeyWritingToolsSlotID
+ _IAPayloadKeyWritingToolsSlotType
+ _IAPayloadValueWritingToolsSlotTypeLongText
+ _IAPayloadValueWritingToolsSlotTypePhoto
+ _IAPayloadValueWritingToolsSlotTypeShortText
+ _OBJC_CLASS_$_BMGeneratedImageUserInteraction
+ _OBJC_CLASS_$_NSLocale
CStrings:
+ "\x16\x11\x134Q"
+ "@\"IASWritingToolsAttachmentsCount\""
+ "GeneratedImageFeatures"
+ "GenerativeExperiences"
+ "IASWritingToolsAttachmentsCount"
+ "T@\"IASWritingToolsAttachmentsCount\",&,N,V_modelAttachments"
+ "T@\"IASWritingToolsAttachmentsCount\",&,N,V_slotAttachments"
+ "T@\"NSMutableDictionary\",&,N,V_slotAttachmentsBySlotID"
+ "TB,N,V_sendToBiomeStream"
+ "TQ,N,V_missingAttachments"
+ "TQ,N,V_numImagesAttached"
+ "TQ,N,V_slotFillingForm"
+ "UUID"
+ "UserInteraction"
+ "[%!{(MISSING)private}@] handleSlotFormCompletedSignal: payloads are malformed slotsAndResponses nil? : (%!d(MISSING))"
+ "[%!{(MISSING)private}@] handleSlotFormCompletedSignal: questionDict is NOT dict (%!{(MISSING)private}@)"
+ "[%!{(MISSING)private}@] handleSlotFormCompletedSignal: slotType (%!{(MISSING)private}@) is NOT a valid type for slot (%!{(MISSING)private}@)"
+ "_missingAttachments"
+ "_modelAttachments"
+ "_numImagesAttached"
+ "_sendToBiomeStream"
+ "_slotAttachments"
+ "_slotAttachmentsBySlotID"
+ "_slotFillingForm"
+ "currentLocale"
+ "dictionary"
+ "handleAttachmentsModifiedSignal:isForSlotForm:"
+ "handleSlotFormCompletedSignal:"
+ "initWithTimestamp:prompt:tokenLength:identifier:topic:usage:userInterfaceLanguage:userSetRegionFormat:personalization:result:feature:"
+ "languageCode"
+ "missingAttachments"
+ "modelAttachments"
+ "nil"
+ "now"
+ "numImagesAttached"
+ "regionCode"
+ "sendBiomeAnalytics"
+ "sendEvent:"
+ "sendToBiomeStream"
+ "setMissingAttachments:"
+ "setModelAttachments:"
+ "setNumImagesAttached:"
+ "setSendToBiomeStream:"
+ "setSlotAttachments:"
+ "setSlotAttachmentsBySlotID:"
+ "setSlotFillingForm:"
+ "slotAttachments"
+ "slotAttachmentsBySlotID"
- "\x16\x11\x131A\x11"
- "T@\"IASignalAnalyticsObject\",&,N,V_slotFormCompletedSignal"
- "TQ,N,V_numPhotosAttached"
- "[%!{(MISSING)private}@] getSlotFillingForm: questionDict is NOT dict (%!{(MISSING)private}@)"
- "_numPhotosAttached"
- "_slotFormCompletedSignal"
- "chatGPTAccount"
- "getSlotFillingForm"
- "handleAttachmentsModifiedSignal:"
- "numPhotosAttached"
- "setNumPhotosAttached:"
- "setSlotFormCompletedSignal:"
- "slotFormCompletedSignal"

```
