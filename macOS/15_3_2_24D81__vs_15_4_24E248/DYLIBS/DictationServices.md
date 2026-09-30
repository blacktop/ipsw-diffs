## DictationServices

> `/System/Library/PrivateFrameworks/SpeechObjects.framework/Versions/A/Frameworks/DictationServices.framework/Versions/A/DictationServices`

```diff

-6.1.51.0.0
-  __TEXT.__text: 0x4e488
+6.1.51.3.0
+  __TEXT.__text: 0x4e618
   __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x54f4
+  __TEXT.__objc_methlist: 0x5fc4
   __TEXT.__const: 0x380
   __TEXT.__gcc_except_tab: 0xac0
   __TEXT.__cstring: 0x430d
   __TEXT.__oslogstring: 0x1570
   __TEXT.__ustring: 0x7c
   __TEXT.__dlopen_cstrs: 0xc4
-  __TEXT.__unwind_info: 0x1530
+  __TEXT.__unwind_info: 0x1550
   __TEXT.__objc_classname: 0xedd
   __TEXT.__objc_methname: 0x1129e
   __TEXT.__objc_methtype: 0x3137

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4038
+  __DATA_CONST.__objc_selrefs: 0x4510
   __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0x150
   __AUTH_CONST.__auth_got: 0x7b0
   __AUTH_CONST.__const: 0x1410
   __AUTH_CONST.__cfstring: 0x4b80
-  __AUTH_CONST.__objc_const: 0x110c0
+  __AUTH_CONST.__objc_const: 0xfc40
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FE788FB8-F491-3C1B-A922-D9D450616C0F
-  Functions: 2083
-  Symbols:   6067
+  UUID: C3466290-7098-3E18-944B-BD8C89D062CA
+  Functions: 2117
+  Symbols:   6110
   CStrings:  4852
 
Symbols:
+ +[DSRMessageTracerUtilities sharedDSRMessageTracerUtilities].cold.1
+ +[DSRSiriInstrumentationUtilities sharedDSRSiriInstrumentationUtilities].cold.1
+ +[SOActionsPopoverManager sharedManager].cold.1
+ +[SOAudioDeviceManager isClamshellClosed].cold.1
+ +[SOAudioDeviceManager sharedAudioDeviceManager].cold.1
+ +[SOCommandCreationManager sharedManager].cold.1
+ +[SOCommandEditingViewController defaultViewController].cold.1
+ +[SOCorrectionManager sharedManager].cold.1
+ +[SODictationAdvancedCommandsFileManager sharedInstance].cold.1
+ +[SODictationPreferences offLineDictationSupportedLanguages].cold.1
+ +[SODictationPreferences sharedDictationPreferences].cold.1
+ +[SODictationRecognizerModeOverlayView _imageBundle].cold.1
+ +[SORecognitionFeedbackManager sharedSORecognitionFeedbackManager].cold.1
+ +[SOSelectionOverlayManager sharedManager].cold.1
+ -[SODictationCommandItem _isNashvilleLocale:].cold.1
+ -[SOElementNumbersCyclingView setItems:].cold.1
+ -[SOGridElementView _centeredBadgeFrameForBadgeSize:screenOrigin:].cold.1
+ -[SOLabeledBadgeView _maskImage].cold.1
+ -[SOLabeledElementsOverlayController addLabeledElements:].cold.2
+ -[SOLabeledElementsOverlayController clearLabeledElements].cold.2
+ -[SOLabeledElementsOverlayController hideLabeledElements].cold.2
+ -[SOLabeledElementsOverlayController showLabeledElements].cold.2
+ -[SOSelectionOverlayManager showTextSegmentsForSelectedString:selectionRect:startIndex:].cold.1
+ -[SO_AXElementNamesCyclingView setItems:].cold.1
+ -[SO_AXElementNamesItemView setPositioningMode:].cold.1
+ DSRLogAppCompatibility.cold.1
+ DSRLogAssetDownload.cold.1
+ DSRLogAudioDevice.cold.1
+ DSRLogAudioLogging.cold.1
+ DSRLogContext.cold.1
+ DSRLogGeneral.cold.1
+ DSRLogHUDPositioning.cold.1
+ DSRLogIOKit.cold.1
+ DSRLogInputMethodKit.cold.1
+ DSRLogMigrator.cold.1
+ DSRLogPreferences.cold.1
+ DSRLogRecognitionEvents.cold.1
+ DSRLogSystemEvents.cold.1
+ DSRLogTypewriterEffect.cold.1
+ DSRLogUIElements.cold.1

```
