## libAccessibility.dylib

> `/usr/lib/libAccessibility.dylib`

```diff

-3237.1.0.0.0
-  __TEXT.__text: 0x37464
+3240.3.0.0.0
+  __TEXT.__text: 0x37a20
   __TEXT.__objc_methlist: 0x364
-  __TEXT.__const: 0x208
+  __TEXT.__const: 0x210
   __TEXT.__dlopen_cstrs: 0x119
   __TEXT.__gcc_except_tab: 0x164
-  __TEXT.__cstring: 0x97c0
-  __TEXT.__oslogstring: 0x1611
+  __TEXT.__cstring: 0x9836
+  __TEXT.__oslogstring: 0x182f
   __TEXT.__unwind_info: 0xd68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x598
+  __DATA_CONST.__objc_selrefs: 0x5b8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__got: 0x150
   __AUTH_CONST.__const: 0x3700
-  __AUTH_CONST.__cfstring: 0x6f20
+  __AUTH_CONST.__cfstring: 0x7000
   __AUTH_CONST.__objc_const: 0x740
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_floatobj: 0x50

   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x48
   __DATA.__data: 0x12f8
-  __DATA.__bss: 0x1600
+  __DATA.__bss: 0x1608
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x368
+  __DATA_DIRTY.__bss: 0x360
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MediaAccessibility.framework/MediaAccessibility

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1492
-  Symbols:   3398
-  CStrings:  1262
+  Functions: 1490
+  Symbols:   3401
+  CStrings:  1277
 
Symbols:
+ GCC_except_table1371
+ GCC_except_table1403
+ GCC_except_table1408
+ GCC_except_table1409
+ GCC_except_table1474
+ GCC_except_table1484
+ GCC_except_table1485
+ _OBJC_CLASS_$_NSDate
+ _objc_msgSend$date
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$subarrayWithRange:
- GCC_except_table1373
- GCC_except_table1405
- GCC_except_table1410
- GCC_except_table1411
- GCC_except_table1478
- GCC_except_table1486
- GCC_except_table1487
- __AXSSetAppleTVRemoteForceLiveTVButtons
- __AXSSetAppleTVRemoteUsesSimpleGestures
Functions:
~ __AXSTripleClickCopyOptions : 1568 -> 2312
~ __AXSAssistiveTouchSetEnabled : 440 -> 1348
~ __AXSSetTripleClickOptions : 892 -> 796
~ __AXSLiveTranscriptionSetFontFamily : 24 -> 84
~ __AXSLiveTranscriptionSetTextColorData : 24 -> 28
~ __AXSLiveTranscriptionSetBackgroundColorData : 24 -> 28
- __AXSSetAppleTVRemoteUsesSimpleGestures
- __AXSSetAppleTVRemoteForceLiveTVButtons
~ _AXRuntimeCheck_SoundRecognitionMedinaKShotEnrollmentEnabled : 72 -> 116
CStrings:
+ "AssistiveTouchSettingsEvents"
+ "Removing AccessibilityReader triple click option, feature disabled: %@"
+ "Removing HoverText triple click option, feature disabled: %@"
+ "Removing LiveTranscription triple click option, feature disabled: %@"
+ "Removing NearbyDeviceControl triple click option, feature disabled: %@"
+ "Removing OnDeviceEyeTracking triple click option, feature disabled: %@"
+ "Removing TwiceRemoteScreen triple click option, feature disabled: %@"
+ "Setting AssistiveTouchEnabled to %{bool}d, requested by %{public}@ [%d], caller frames: %{public}@"
+ "Setting triple click options: previous: %@, new: %@, caller: %@"
+ "SoundDetection_Medina_KShotEnrollment"
+ "callerFrames"
+ "enabled"
+ "pid"
+ "process"
+ "timestamp"
+ "unknown"
- "Setting triple click options: %@"
```
