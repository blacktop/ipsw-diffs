## CoreAudio

> `/System/Library/Components/CoreAudio.component/Contents/MacOS/CoreAudio`

### Sections with Same Size but Changed Content

- `__TEXT.__dof_AudioTool`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-1638.104.3.0.0
-  __TEXT.__text: 0xd5dec
-  __TEXT.__realtime: 0x3ec6c
-  __TEXT.__auth_stubs: 0x2630
-  __TEXT.__objc_stubs: 0x540
-  __TEXT.__const: 0xa760
-  __TEXT.__gcc_except_tab: 0x88ec
-  __TEXT.__cstring: 0x84a6
-  __TEXT.__oslogstring: 0x9c37
+1638.213.0.0.0
+  __TEXT.__text: 0xd5548
+  __TEXT.__realtime: 0x3ec70
+  __TEXT.__auth_stubs: 0x2680
+  __TEXT.__objc_stubs: 0x4e0
+  __TEXT.__const: 0xa750
+  __TEXT.__gcc_except_tab: 0x88c4
+  __TEXT.__cstring: 0x839c
+  __TEXT.__oslogstring: 0x9c08
   __TEXT.__dlopen_cstrs: 0x8e
-  __TEXT.__objc_methname: 0x2e3
+  __TEXT.__objc_methname: 0x2c3
   __TEXT.__dof_AudioTool: 0x2c7
-  __TEXT.__unwind_info: 0x5080
+  __TEXT.__unwind_info: 0x5020
   __TEXT.__eh_frame: 0x108
-  __DATA_CONST.__const: 0x123c0
-  __DATA_CONST.__cfstring: 0x4640
+  __DATA_CONST.__const: 0x12238
+  __DATA_CONST.__cfstring: 0x4540
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x1328
-  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__auth_got: 0x1350
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_selrefs: 0x150
+  __DATA.__objc_selrefs: 0x138
   __DATA.__data: 0xe68
-  __DATA.__bss: 0xd50
+  __DATA.__bss: 0xd18
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4250
-  Symbols:   834
-  CStrings:  2050
+  Functions: 4225
+  Symbols:   836
+  CStrings:  2034
 
Symbols:
+ __ZN20AudioCapturerManager10InitializeEv
+ __ZN20AudioCapturerManager9IsEnabledE8TapPoint
+ __ZN20AudioCapturerManager9SetFormatERK27AudioStreamBasicDescription8TapPoint
+ __ZN20AudioCapturerManagerC1EONSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN20AudioCapturerManagerD1Ev
+ __ZNK20AudioCapturerManager11GetFilePathEv
+ __ZNK20AudioCapturerManager15WriteBufferListEPK15AudioBufferListjxPK17AudioCaptureTrace
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSNumber
- __ZN5caulk14cf_preferences15interpret_int64EPKv
- _objc_opt_class
- _objc_opt_isKindOfClass
CStrings:
+ "%25s:%-5d Capturing audio to file { auio=%p, mCapturer->GetFilePath()=\"%s\" }"
+ "auhal-in-{}"
+ "auhal-out-{}"
- "%25s:%-5d AUIO init { gAUIOCapturesEnabled=0x%x }"
- "%25s:%-5d Capturing audio to file { auio=%p, mCapturer->FilePath()=\"%s\" }"
- "/usr/local/lib/libAudioDiagnostics.dylib"
- "AudioCapture/AudioToolbox"
- "NewAudioCapturerImpl"
- "ObserveAudioDiagnosticPreferenceImpl"
- "auhal-in-%s"
- "auhal-out-%s"
- "auhal_captureinput_callback"
- "auhal_captureinput_ioproc"
- "auhal_captureoutput"
- "auio_capture"
- "boolValue"
- "captureInput"
- "captureOutput"
- "intValue"
- "ring_buffer_mode"
- "v16@?0^v8"
- "valueForKey:"
```
