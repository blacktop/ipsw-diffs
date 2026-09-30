## AccessibilitySharedSupport

> `/System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Versions/A/AccessibilitySharedSupport`

```diff

-502.5.4.0.0
-  __TEXT.__text: 0x4f7d0
+502.7.5.0.0
+  __TEXT.__text: 0x4f5d4
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x4260
+  __TEXT.__objc_methlist: 0x483c
   __TEXT.__const: 0x2e8
-  __TEXT.__cstring: 0x3c6d
-  __TEXT.__oslogstring: 0x2f53
-  __TEXT.__gcc_except_tab: 0x1038
+  __TEXT.__cstring: 0x3c8b
+  __TEXT.__oslogstring: 0x2fc9
+  __TEXT.__gcc_except_tab: 0x1040
   __TEXT.__ustring: 0x17e
   __TEXT.__dlopen_cstrs: 0x29f
-  __TEXT.__unwind_info: 0x1090
+  __TEXT.__unwind_info: 0x10c8
   __TEXT.__objc_classname: 0x906
-  __TEXT.__objc_methname: 0xc706
-  __TEXT.__objc_methtype: 0x1fb2
-  __TEXT.__objc_stubs: 0x9260
+  __TEXT.__objc_methname: 0xc834
+  __TEXT.__objc_methtype: 0x1fe2
+  __TEXT.__objc_stubs: 0x92e0
   __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0xa18
+  __DATA_CONST.__const: 0xb70
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2db0
+  __DATA_CONST.__objc_selrefs: 0x2fb0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x390
   __AUTH_CONST.__auth_got: 0x470
   __AUTH_CONST.__const: 0x13a0
-  __AUTH_CONST.__cfstring: 0x4aa0
-  __AUTH_CONST.__objc_const: 0x79d0
+  __AUTH_CONST.__cfstring: 0x4ac0
+  __AUTH_CONST.__objc_const: 0x6ff0
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_floatobj: 0x1c0
   __AUTH.__objc_data: 0x1450
-  __DATA.__objc_ivar: 0x478
+  __DATA.__objc_ivar: 0x47c
   __DATA.__data: 0x718
   __DATA.__bss: 0x350
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 911CB6A4-DB0B-38A3-87EE-14D317260439
-  Functions: 1989
-  Symbols:   4819
-  CStrings:  4089
+  UUID: 04AEA12F-A1F4-34A1-8F7A-35833501B71E
+  Functions: 2013
+  Symbols:   4854
+  CStrings:  4104
 
Symbols:
+ +[AXSSAudioDeviceManager sharedAudioDeviceManager].cold.1
+ +[AXSSLanguageManager commonPunctuationCharacters].cold.1
+ +[AXSSLanguageManager shared].cold.1
+ +[AXSSMotionTrackingCameraManager _sortedAndFilteredCaptureDevicesFromDevices:].cold.1
+ +[AXSSMotionTrackingExpressionConfiguration _defaultSensitivitiesForAllFacialExpressions].cold.1
+ +[AXSSMotionTrackingExpressionConfiguration _facialExpressionToSensitivityToValueMapping].cold.1
+ +[AXSSMotionTrackingExpressionConfiguration _populateExpressionArraysForProcessedExpressions:previousExpressions:startExpressionsOutSet:endExpressionsOutSet:].cold.1
+ +[AXSSMotionTrackingExpressionConfiguration_Exclave _facialExpressionToActivationToValueMapping].cold.1
+ +[AXSSMotionTrackingUtilities axss_frequencyElementMatchingDict].cold.1
+ +[AXSSMotionTrackingUtilities axss_statusElementMatchingDict].cold.1
+ +[AXSSMotionTrackingUtilities axss_xPositionElementMatchingDict].cold.1
+ +[AXSSMotionTrackingUtilities axss_yPositionElementMatchingDict].cold.1
+ +[AXSSMotionTrackingVirtualEyeTracker _eyeTrackerHIDReportDescriptorData].cold.1
+ +[AXSSPunctuationManager sharedDatabase].cold.1
+ +[AXSSSpeechSynthesisController sharedInstance].cold.1
+ +[AXSSWordDescriptionManager sharedInstance].cold.1
+ -[AXSSCloudKitHelper initWithContainerIdentifier:zoneName:].cold.1
+ -[AXSSInterDeviceCommunicator _sendICloudMessage:toDevice:]
+ -[AXSSInterDeviceCommunicator _sendICloudMessage:toDevice:].cold.1
+ -[AXSSInterDeviceCommunicator hasPeers]
+ -[AXSSInterDeviceCommunicator hearingAidsMessagesObserver]
+ -[AXSSInterDeviceCommunicator sendHearingAidsMessage:toDevice:]
+ -[AXSSInterDeviceCommunicator setHearingAidsMessagesObserver:]
+ -[AXSSKeyChord isTextInputChord].cold.1
+ -[AXSSKeyChord isTextInputTabChord].cold.1
+ -[AXSSMotionTrackingVideoFileInputManager _update].cold.1
+ -[AXSSMotionTrackingVirtualEyeTracker _moveOnReportingQueueToPoint:].cold.2
+ AXSSLanguageConvertToCanonicalForm.cold.1
+ AXSSLogForCategory.cold.1
+ GCC_except_table21
+ GCC_except_table37
+ GCC_except_table52
+ GCC_except_table76
+ OBJC_IVAR_$_AXSSInterDeviceCommunicator._hearingAidsMessagesObserver
+ __52-[AXSSWordDescriptionManager_ja descriptionForWord:]_block_invoke.cold.1
+ __52-[AXSSWordDescriptionManager_ja descriptionForWord:]_block_invoke.cold.2
+ __52-[AXSSWordDescriptionManager_ja descriptionForWord:]_block_invoke.cold.3
+ __52-[AXSSWordDescriptionManager_ja descriptionForWord:]_block_invoke.cold.4
+ __52-[AXSSWordDescriptionManager_ja descriptionForWord:]_block_invoke.cold.5
+ __52-[AXSSWordDescriptionManager_ja descriptionForWord:]_block_invoke.cold.6
+ _objc_msgSend$_sendICloudMessage:toDevice:
+ _objc_msgSend$didReceiveHearingAidsMessage:fromDevice:
+ _objc_msgSend$didUpdateDevices:
+ _objc_msgSend$hearingAidsMessagesObserver
- GCC_except_table26
- GCC_except_table36
- GCC_except_table50
- GCC_except_table75
- _OUTLINED_FUNCTION_9
CStrings:
+ "@\"<AXSSInterDeviceHearingAidsMessagesObserver>\""
+ "Did receive Hearing Aids message: %@ from device: %@"
+ "Message sent with identifier %@"
+ "Sending message %@ to device: %@"
+ "T@\"<AXSSInterDeviceHearingAidsMessagesObserver>\",W,N,V_hearingAidsMessagesObserver"
+ "_hearingAidsMessagesObserver"
+ "_sendICloudMessage:toDevice:"
+ "com.apple.hearing.hearingaids"
+ "didReceiveHearingAidsMessage:fromDevice:"
+ "didUpdateDevices:"
+ "hasPeers"
+ "hearingAidsMessagesObserver"
+ "sendHearingAidsMessage:toDevice:"
+ "setHearingAidsMessagesObserver:"

```
