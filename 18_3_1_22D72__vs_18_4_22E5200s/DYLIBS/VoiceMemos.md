## VoiceMemos

> `/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos`

```diff

-1252.0.0.0.0
-  __TEXT.__text: 0x45d70
-  __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_methlist: 0x35b0
-  __TEXT.__gcc_except_tab: 0x19bc
-  __TEXT.__const: 0x1e8
-  __TEXT.__cstring: 0x5f16
-  __TEXT.__oslogstring: 0x27fa
+1268.0.0.0.0
+  __TEXT.__text: 0x46140
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__objc_methlist: 0x3ab4
+  __TEXT.__gcc_except_tab: 0x19fc
+  __TEXT.__const: 0x1f0
+  __TEXT.__cstring: 0x5ea7
+  __TEXT.__oslogstring: 0x2830
   __TEXT.__ustring: 0x22
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1840
+  __TEXT.__unwind_info: 0x1908
   __TEXT.__objc_classname: 0x80a
-  __TEXT.__objc_methname: 0xb2ae
-  __TEXT.__objc_methtype: 0x1585
-  __TEXT.__objc_stubs: 0x86c0
+  __TEXT.__objc_methname: 0xb28d
+  __TEXT.__objc_methtype: 0x1562
+  __TEXT.__objc_stubs: 0x86e0
   __DATA_CONST.__got: 0x638
-  __DATA_CONST.__const: 0x1d48
+  __DATA_CONST.__const: 0x1d50
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2af0
+  __DATA_CONST.__objc_selrefs: 0x2bb8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x640
+  __AUTH_CONST.__auth_got: 0x638
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x720
   __AUTH_CONST.__cfstring: 0x30e0
-  __AUTH_CONST.__objc_const: 0x60d8
+  __AUTH_CONST.__objc_const: 0x57d8
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x2c0
   __DATA.__data: 0x7f0
-  __DATA.__bss: 0x178
-  __DATA_DIRTY.__objc_data: 0xf50
-  __DATA_DIRTY.__bss: 0x120
+  __DATA.__bss: 0x120
+  __DATA_DIRTY.__objc_data: 0xfa0
+  __DATA_DIRTY.__bss: 0x178
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1764
-  Symbols:   2335
+  Functions: 1813
+  Symbols:   2394
   CStrings:  2912
 
Symbols:
+ _kVMLogCategoryPointsOfInterest
- _fmod
CStrings:
+ "%s -- Attempted to write metadata before finalization"
+ "+[RCMutableMovie movieWithURL:error:]"
+ "+[RCSavedRecordingsModel _copyFileIntoRecordingsDirectory:error:]"
+ "@64@0:8@16d24@32@40@48^@56"
+ "AVFileTypeForFileExtension:"
+ "Attempted to write metadata before finalization"
+ "BOOL _checkCanAppend(RCWaveformGenerator * _Nonnull __strong, SEL _Nonnull)"
+ "PointsOfInterest"
+ "RCWaveformGenerator.mm"
+ "RCWaveformSegment.mm"
+ "T@\"RCRecordingsFolder\",R,N"
+ "_copyFileIntoRecordingsDirectory:error:"
+ "canContainFragments"
+ "insertRecordingWithAudioFile:duration:date:customTitleBase:uniqueID:error:"
+ "supportedFileTypes"
+ "userFolder"
+ "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float>>=\"__value_\"^f}}"
- "+[RCSavedRecordingsModel _copyFileIntoRecordingsDirectory:]"
- "/Library/Caches/com.apple.xbs/Sources/VoiceMemos_Framework/Framework/Waveform/RCWaveformGenerator.mm"
- "/Library/Caches/com.apple.xbs/Sources/VoiceMemos_Framework/Framework/Waveform/RCWaveformSegment.mm"
- "<Unknown File>"
- "<Unknown Function>"
- "@40@0:8@16d24@32"
- "@48@0:8@16d24@32@40"
- "@56@0:8@16d24@32@40@48"
- "BOOL _checkCanAppend(RCWaveformGenerator *__strong, SEL)"
- "RCCaptureFormat.m"
- "_copyFileIntoRecordingsDirectory:"
- "insertRecordingWithAudioFile:duration:date:"
- "insertRecordingWithAudioFile:duration:date:customLabelBase:"
- "insertRecordingWithAudioFile:duration:date:customTitleBase:uniqueID:"
- "nextRecordingDefaultLabelWithCustomLabelBase:"
- "unsupported file extension: %@"
- "{vector<float, std::allocator<float> >=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float> >=\"__value_\"^f}}"

```
