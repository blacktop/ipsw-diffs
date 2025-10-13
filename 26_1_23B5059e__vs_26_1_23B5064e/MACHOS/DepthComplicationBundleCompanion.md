## DepthComplicationBundleCompanion

> `/System/Library/NanoTimeKit/ComplicationBundles/DepthComplicationBundleCompanion.bundle/DepthComplicationBundleCompanion`

```diff

-2026.1.8.0.0
-  __TEXT.__text: 0x2ff94
-  __TEXT.__auth_stubs: 0x13d0
-  __TEXT.__objc_methlist: 0x774
-  __TEXT.__const: 0x934
-  __TEXT.__cstring: 0x1dd0
-  __TEXT.__objc_methname: 0x11a0
-  __TEXT.__constg_swiftt: 0x145c
-  __TEXT.__swift5_typeref: 0x7a4
-  __TEXT.__swift5_reflstr: 0x995
-  __TEXT.__swift5_fieldmd: 0x918
+2026.1.11.0.0
+  __TEXT.__text: 0x32b18
+  __TEXT.__auth_stubs: 0x1410
+  __TEXT.__objc_methlist: 0x73c
+  __TEXT.__const: 0xa14
+  __TEXT.__cstring: 0x1ea0
+  __TEXT.__objc_methname: 0x11df
+  __TEXT.__constg_swiftt: 0x142c
+  __TEXT.__swift5_typeref: 0x824
+  __TEXT.__swift5_reflstr: 0x9b5
+  __TEXT.__swift5_fieldmd: 0x940
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_proto: 0x14
-  __TEXT.__swift5_types: 0x84
+  __TEXT.__swift5_proto: 0x20
+  __TEXT.__swift5_types: 0x88
   __TEXT.__objc_classname: 0x71
   __TEXT.__objc_methtype: 0x31c
-  __TEXT.__oslogstring: 0x96e
-  __TEXT.__swift5_capture: 0xc0
+  __TEXT.__oslogstring: 0xa2e
+  __TEXT.__swift5_capture: 0xd0
+  __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x6f0
+  __TEXT.__unwind_info: 0x720
   __TEXT.__eh_frame: 0xa8
-  __DATA_CONST.__auth_got: 0x9e8
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__auth_ptr: 0x240
-  __DATA_CONST.__const: 0x860
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__auth_got: 0xa08
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__auth_ptr: 0x268
+  __DATA_CONST.__const: 0xa10
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA.__objc_const: 0x1b48
-  __DATA.__objc_selrefs: 0x6a0
-  __DATA.__objc_data: 0x1628
-  __DATA.__data: 0x1830
+  __DATA.__objc_const: 0x1a58
+  __DATA.__objc_selrefs: 0x6a8
+  __DATA.__objc_data: 0x1530
+  __DATA.__data: 0x1850
   __DATA.__common: 0x128
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x280
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F2F30C3A-F714-380B-95A0-4FC1812AB1BC
-  Functions: 575
-  Symbols:   221
-  CStrings:  518
+  UUID: B1B8C302-E4A8-3EF2-A5C5-2646B06E7D8D
+  Functions: 605
+  Symbols:   223
+  CStrings:  530
 
Symbols:
+ _OBJC_CLASS_$_NSTimer
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
- _CGRectGetMinY
- _OBJC_CLASS_$_UIFont
CStrings:
+ "$__lazy_storage_$_underwaterTimeTypeLabel"
+ "ComplicationMetadataKeyCurrentDepth"
+ "ComplicationMetadataKeyCurrentDepthCategory"
+ "ComplicationMetadataKeyDisplayTimeCategory"
+ "ComplicationMetadataKeyDiveUnderwaterTimePreviousDuration"
+ "ComplicationMetadataKeyUnderwaterTimeCategory"
+ "ComplicationMetadataUnderwaterTimeEndDate"
+ "ComplicationMetadataUnderwaterTimeStartDate"
+ "DepthRectangularLiveView: Unexpected metrics type: %s"
+ "DepthRectangularLiveView: updateTimeDisplay: Invalid state to update time display (metrics: %s, alwaysOn: %{bool}d)"
+ "DisplayTime: Failed to decode DiveUnderwaterTime from metadata"
+ "DisplayTime: Failed to decode UnderwaterTime from metadata"
+ "DisplayTime: Failed to decode category from metadata"
+ "TimelineDataProvider: Not updating depth model with sensor due to mismatching isHistorical=%{bool}d and isActiveDive=%{bool}d"
+ "UnderwaterTime: Unable to create time from category=%s startDate=%s endDate=%s"
+ "Unhandled UnderwaterTime case"
+ "active"
+ "completed"
+ "configurationByApplyingConfiguration:"
+ "configurationWithPaletteColors:"
+ "displayedTimeTypeLabel"
+ "historicalUnderwaterDuration"
+ "imageWithConfiguration:"
+ "invalidate"
+ "isActiveDive"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "sessionTime"
+ "systemImageNamed:"
+ "tentative"
+ "updateTimer"
+ "v16@?0@\"NSTimer\"8"
+ "zero"
- "DEPTH_DIVE_PAUSED"
- "DEPTH_DIVE_TO_CONTINUE"
- "DepthComplicationBundleCompanion.TentativeEndTimerView"
- "TimelineDataProvider: Not updating depth model with sensor due to mismatching isHistorical=%{bool}d and isSubmerged=%{bool}d"
- "TimelineDataProvider: Not updating water temperature model with sensor value since we are not currently submerged."
- "TimelineDataProvider: Received depth update: %{private}s (%s)"
- "TimelineDataProvider: Updating water temperature model with %{private}s (%s)"
- "_TtC32DepthComplicationBundleCompanion21TentativeEndTimerView"
- "_systemImageNamed:withConfiguration:"
- "bringSubviewToFront:"
- "divePausedLabel"
- "diveToContinueLabel"
- "isSubmerged"
- "pauseSymbolAttachment"
- "pointSize"
- "setBackgroundColor:"
- "showTentativeView"
- "systemFontOfSize:"
- "temperatureSubject"
- "tentativeTimeView"

```
