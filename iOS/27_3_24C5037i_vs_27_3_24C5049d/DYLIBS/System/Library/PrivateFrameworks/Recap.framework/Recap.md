## Recap

> `/System/Library/PrivateFrameworks/Recap.framework/Recap`

```diff

-202.2.4.0.0
-  __TEXT.__text: 0x21bb8
-  __TEXT.__objc_methlist: 0x3658
-  __TEXT.__const: 0x380
-  __TEXT.__cstring: 0x1ce7
-  __TEXT.__oslogstring: 0x605
-  __TEXT.__gcc_except_tab: 0xc24
-  __TEXT.__dlopen_cstrs: 0x120
+202.2.9.0.0
+  __TEXT.__text: 0x23304
+  __TEXT.__objc_methlist: 0x36d0
+  __TEXT.__const: 0x390
+  __TEXT.__cstring: 0x219e
+  __TEXT.__oslogstring: 0x63b
+  __TEXT.__gcc_except_tab: 0xc9c
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xc28
+  __TEXT.__dlopen_cstrs: 0x5c
+  __TEXT.__unwind_info: 0xc58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6b8
+  __DATA_CONST.__const: 0x768
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ef0
+  __DATA_CONST.__objc_selrefs: 0x1f70
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x4a0
-  __DATA_CONST.__got: 0x408
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x20a0
-  __AUTH_CONST.__objc_const: 0x5500
+  __DATA_CONST.__got: 0x418
+  __AUTH_CONST.__const: 0x440
+  __AUTH_CONST.__cfstring: 0x2460
+  __AUTH_CONST.__objc_const: 0x5538
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x258
-  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_got: 0x768
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x3c0
+  __DATA.__objc_ivar: 0x3c4
   __DATA.__data: 0x9c8
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x4b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1048
-  Symbols:   2164
-  CStrings:  400
+  Functions: 1063
+  Symbols:   2192
+  CStrings:  431
 
Symbols:
+ +[RCPSyntheticEventStream _eventStreamWithCLIArguments:displayUUID:overridesDisplayUUID:]
+ +[RCPSyntheticEventStream eventStreamWithCLIArguments:overridingDisplayUUID:]
+ -[RCPEventScreen isBuiltIn]
+ -[RCPEventScreen setBuiltIn:]
+ -[RCPEventStream cliArgumentsApproximatingGesture:]
+ -[RCPEventStream cliCommandApproximatingGesture:]
+ -[RCPEventStream streamsBySplittingWithType:marks:filenameAdditions:]
+ -[RCPPlayerPlaybackOptions description]
+ -[RCPSyntheticEventStream pinchAtCenter:startSpan:endSpan:angle:duration:]
+ GCC_except_table24
+ GCC_except_table39
+ GCC_except_table56
+ GCC_except_table9
+ _IOHIDEventGetEvent
+ _OBJC_CLASS_$_FBSOrientationObserver
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_IVAR_$_RCPEventScreen._builtIn
+ __RCPCLICoordinateString
+ __RCPCLINumberString
+ __RCPResolveDisplayUUIDArgument
+ ___69-[RCPEventStream streamsBySplittingWithType:marks:filenameAdditions:]_block_invoke
+ ___69-[RCPEventStream streamsBySplittingWithType:marks:filenameAdditions:]_block_invoke_2
+ ___69-[RCPEventStream streamsBySplittingWithType:marks:filenameAdditions:]_block_invoke_3
+ ___69-[RCPEventStream streamsBySplittingWithType:marks:filenameAdditions:]_block_invoke_4
+ ___69-[RCPEventStream streamsBySplittingWithType:marks:filenameAdditions:]_block_invoke_5
+ ___89+[RCPSyntheticEventStream _eventStreamWithCLIArguments:displayUUID:overridesDisplayUUID:]_block_invoke
+ ____RCPCLIDigitizerPath_block_invoke
+ ____RCPResolveDisplayUUIDArgument_block_invoke
+ ___block_descriptor_32_e41_B24?0"RCPEventScreen"8"NSDictionary"16l
+ ___block_descriptor_32_e68_Q40?0"RCPEvent"8Q16"NSNumber"24"_RCPEventDigitizerStreamState"32l
+ ___block_descriptor_40_e8_32s_e68_Q40?0"RCPEvent"8Q16"NSNumber"24"_RCPEventDigitizerStreamState"32ls32l8
+ ___block_descriptor_48_e8_32r40r_e30_v32?0^{__IOHIDEvent=}8Q16^B24lr32l8r40l8
+ ___block_descriptor_57_e8_32s40s48r_e34_v16?0"<RCPEventStreamComposer>"8ls32l8s40l8r48l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e21_v24?0"RCPEvent"8Q16ls32l8s64l8r72l8r80l8s40l8s48l8s56l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72r80r_e21_v24?0"RCPEvent"8Q16ls32l8r72l8r80l8s40l8s48l8s56l8s64l8
+ _kRCPFingerLiftDelay
+ _kRCPMultiTapInterval
+ _objc_retain_x27
- GCC_except_table16
- GCC_except_table35
- GCC_except_table54
- _FrontBoardServicesLibraryCore.frameworkLibrary
- ___71+[RCPSyntheticEventStream eventStreamWithCLIArguments:withDisplayUUID:]_block_invoke
- ___FrontBoardServicesLibraryCore_block_invoke
- ___block_descriptor_56_e8_32s40s48r_e34_v16?0"<RCPEventStreamComposer>"8ls32l8s40l8r48l8
- ___getFBSOrientationObserverClass_block_invoke
- _audit_stringFrontBoardServices
- _getFBSOrientationObserverClass.softClass
CStrings:
+ " { playbackSpeedFactor: %g, minDelayBetweenSends: %g, useHIDEventTimestampsForDelivery: %@, linkEventDeliveryToDisplayRefreshRate: %@, transform: [%g, %g, %g, %g, %g, %g], displayUUIDOverrideSpecified: %@, displayUUIDOverride: %@, customizeHIDEvent: %@"
+ " }"
+ "%.*f"
+ "%0.6f"
+ "'%@'"
+ "--displayUUID %@ needs a device with exactly two built-in displays, found %lu"
+ "."
+ "0"
+ "B24@?0@\"RCPEventScreen\"8@\"NSDictionary\"16"
+ "Please specify an x and y spacing between fingers for multi-finger tap\n"
+ "Q40@?0@\"RCPEvent\"8Q16@\"NSNumber\"24@\"_RCPEventDigitizerStreamState\"32"
+ "The inner built-in display has no display UUID on this device"
+ "a touch position is negative or not finite, which recap cannot express"
+ "event %lu comes from a different sender than the events before it"
+ "event %lu has %lu contacts"
+ "event %lu has no sender properties"
+ "event %lu is not a digitizer event (IOHIDEventType %u)"
+ "inner"
+ "more than one touch sequence (the second starts at event %lu)"
+ "nil"
+ "no contact touches the digitizer"
+ "outer"
+ "pinchAtCenter: called with %lu touches down; ignoring"
+ "recap -c"
+ "set"
+ "spacing"
+ "the recording has no events"
+ "the recording has no screen size"
+ "the recording has no usable timing"
+ "the sender has no primary usage page and usage"
+ "the touch ends with a cancel at event %lu"
+ "the touch never lifts"
+ "the touch returns to where it started"
- "FBSOrientationObserver"
- "softlink:r:path:/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices"
```
