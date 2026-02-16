## AppleHIDFeedback

> `/System/Library/PrivateFrameworks/AppleHIDFeedback.framework/AppleHIDFeedback`

```diff

 13.0.0.0.0
-  __TEXT.__text: 0x4d98
-  __TEXT.__auth_stubs: 0x450
+  __TEXT.__text: 0x525c
+  __TEXT.__auth_stubs: 0x430
   __TEXT.__objc_methlist: 0x324
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x818
   __TEXT.__oslogstring: 0x685
-  __TEXT.__gcc_except_tab: 0x30c
-  __TEXT.__unwind_info: 0x1a0
+  __TEXT.__gcc_except_tab: 0x2ec
+  __TEXT.__unwind_info: 0x200
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methname: 0xc28
   __TEXT.__objc_methtype: 0x1b3

   __DATA_CONST.__objc_selrefs: 0x350
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x238
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x580
   __AUTH_CONST.__objc_const: 0x580

   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D714B4C7-31F9-304B-8EBD-F675EB32AA9A
+  UUID: A156FA69-DAD3-3F17-90FD-C17812EA8B07
   Functions: 91
-  Symbols:   436
+  Symbols:   434
   CStrings:  319
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ -[AHFPencilPatternLibrary init] : 984 -> 1048
~ ___31-[AHFPencilPatternLibrary init]_block_invoke : 60 -> 64
~ -[AHFPencilPatternLibrary waveformIndexWithType:] : 136 -> 140
~ -[AHFPencilPatternLibrary createPatternsLibraryFrom:] : 2952 -> 3120
~ -[AHFPencilPatternLibrary getReportForPattern:timestampUs:prevTimestampUs:error:] : 572 -> 600
~ -[AHFPencilPatternLibrary isReport:equalTo:] : 176 -> 180
~ -[AHFPencilPatternLibrary maybeGetExploratoryPayload:] : 600 -> 620
~ -[AHFPencilPatternLibrary setLibrary:] : 12 -> 64
~ _failure : 288 -> 300
~ _LoggingFramework : 68 -> 84
~ +[AHFManager sharedInstance] : 160 -> 176
~ -[AHFManager playFeedback:powerSourceID:timestamp:error:] : 648 -> 664
~ -[AHFManager setTrackpadController:] : 12 -> 64
~ -[AHFManager setPencilController:] : 12 -> 64
~ -[AHFPencilController initializeDigitizerStylusSystem] : 572 -> 576
~ ___54-[AHFPencilController initializeDigitizerStylusSystem]_block_invoke : 424 -> 432
~ ___54-[AHFPencilController initializeDigitizerStylusSystem]_block_invoke.13 : 264 -> 272
~ -[AHFPencilController initializeOpaqueTouchSystem] : 572 -> 576
~ ___50-[AHFPencilController initializeOpaqueTouchSystem]_block_invoke : 424 -> 432
~ ___50-[AHFPencilController initializeOpaqueTouchSystem]_block_invoke.24 : 264 -> 272
~ -[AHFPencilController initializePencilHapticsSystem] : 544 -> 548
~ ___52-[AHFPencilController initializePencilHapticsSystem]_block_invoke : 448 -> 452
~ ___52-[AHFPencilController initializePencilHapticsSystem]_block_invoke.35 : 260 -> 264
~ -[AHFPencilController playFeedbackGated:haptics:timestamp:error:] : 540 -> 552
~ ___61-[AHFPencilController playFeedback:senderID:timestamp:error:]_block_invoke : 452 -> 472
~ -[AHFPencilController playFeedback:accessoryID:timestamp:error:] : 648 -> 640
~ ___64-[AHFPencilController playFeedback:accessoryID:timestamp:error:]_block_invoke : 440 -> 452
~ -[AHFPencilController setPatternsLibrary:] : 12 -> 64
~ -[AHFPencilController setQueue:] : 12 -> 64
~ -[AHFPencilController setDigitizerStylusClient:] : 12 -> 64
~ -[AHFPencilController setAvailableDigitizerStylus:] : 12 -> 64
~ -[AHFPencilController setOpaqueTouchClient:] : 12 -> 64
~ -[AHFPencilController setAvailableOpaqueTouch:] : 12 -> 64
~ -[AHFPencilController setPencilHapticsClient:] : 12 -> 64
~ -[AHFTrackpadController dealloc] : 112 -> 120
~ -[AHFTrackpadController initializeTrackpadSystem] : 692 -> 724
~ ___49-[AHFTrackpadController initializeTrackpadSystem]_block_invoke : 460 -> 472
~ ___49-[AHFTrackpadController initializeTrackpadSystem]_block_invoke.16 : 296 -> 308
~ -[AHFTrackpadController getActuationIdForPattern:] : 368 -> 372
~ -[AHFTrackpadController playFeedbackGated:client:timestamp:error:] : 488 -> 492
~ ___63-[AHFTrackpadController playFeedback:senderID:timestamp:error:]_block_invoke : 308 -> 328
~ -[AHFTrackpadController playFeedback:accessoryID:timestamp:error:] : 776 -> 768
~ ___66-[AHFTrackpadController playFeedback:accessoryID:timestamp:error:]_block_invoke : 436 -> 456
~ -[AHFTrackpadController setQueue:] : 12 -> 64
~ -[AHFTrackpadController setTrackpadClient:] : 12 -> 64
~ -[AHFTrackpadController setAvailableTrackpads:] : 12 -> 64

```
