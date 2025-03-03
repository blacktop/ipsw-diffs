## AVFAudio

> `/System/Library/Frameworks/AVFAudio.framework/AVFAudio`

```diff

-684.327.0.0.0
-  __TEXT.__text: 0x1147fc
-  __TEXT.__auth_stubs: 0x1fe0
-  __TEXT.__objc_methlist: 0x51a0
-  __TEXT.__const: 0x626
-  __TEXT.__gcc_except_tab: 0x1508c
-  __TEXT.__cstring: 0xe543
-  __TEXT.__oslogstring: 0x1767d
+684.518.1.0.0
+  __TEXT.__text: 0x114ac8
+  __TEXT.__auth_stubs: 0x1fd0
+  __TEXT.__objc_methlist: 0x5754
   __TEXT.__dlopen_cstrs: 0xa9
-  __TEXT.__unwind_info: 0x5d10
-  __TEXT.__objc_classname: 0xa12
-  __TEXT.__objc_methname: 0xbb69
-  __TEXT.__objc_methtype: 0x2761
-  __TEXT.__objc_stubs: 0x7860
-  __DATA_CONST.__got: 0x570
+  __TEXT.__const: 0x656
+  __TEXT.__gcc_except_tab: 0x14dc8
+  __TEXT.__cstring: 0xe59c
+  __TEXT.__oslogstring: 0x1779e
+  __TEXT.__unwind_info: 0x5ca8
+  __TEXT.__objc_classname: 0xa13
+  __TEXT.__objc_methname: 0xbc09
+  __TEXT.__objc_methtype: 0x2780
+  __TEXT.__objc_stubs: 0x78e0
+  __DATA_CONST.__got: 0x578
   __DATA_CONST.__const: 0x1938
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3170
+  __DATA_CONST.__objc_selrefs: 0x3220
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2b0
-  __AUTH_CONST.__auth_got: 0x1008
-  __AUTH_CONST.__const: 0x67e8
-  __AUTH_CONST.__cfstring: 0x3560
-  __AUTH_CONST.__objc_const: 0x8f58
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x1000
+  __AUTH_CONST.__auth_ptr: 0x8
+  __AUTH_CONST.__const: 0x6768
+  __AUTH_CONST.__cfstring: 0x3580
+  __AUTH_CONST.__objc_const: 0x85c8
+  __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x414
+  __DATA.__objc_ivar: 0x41c
   __DATA.__data: 0x820
-  __DATA.__bss: 0x180
+  __DATA.__bss: 0x188
   __DATA_DIRTY.__objc_data: 0x1db0
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x268
+  __DATA_DIRTY.__bss: 0x260
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3855
-  Symbols:   4886
-  CStrings:  5828
+  Functions: 3817
+  Symbols:   4891
+  CStrings:  5849
 
Symbols:
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTVNSt3__117bad_function_callE
- __ZNKSt9exception4whatEv
- _objc_release_x10
CStrings:
+ "\x02!2"
+ "%25s:%-5d AVVoiceTriggerClient init %@, clientType: %d"
+ "%25s:%-5d Acquiring an OS Transaction for ADAMSiriSession"
+ "%25s:%-5d Created AVVoiceTriggerClient (%p) with clientType: %d"
+ "%25s:%-5d Logging Out-of-Session ABC Metric %@"
+ "%25s:%-5d Releasing OS Transaction for ADAMSiriSession"
+ "%25s:%-5d destroyRecordEngine:  synthesizing doneRecording"
+ "%25s:%-5d exclaveSupport: %d corespeechdConclaveEnabled: %d isHACProduct: %d"
+ "%25s:%-5d isMicrophoneBuiltin: %d mVoiceControllerClientType: %ld "
+ "'Category Change'"
+ "'New Device Available'"
+ "'Old Device Unavailable'"
+ "@24@0:8q16"
+ "ADAMSiriSession"
+ "Tq,N,V_clientType"
+ "_clientType"
+ "_disposeADAM"
+ "avvcDualAVVC"
+ "avvcGenerateAutoBugCapture"
+ "clientType"
+ "init:"
+ "isSiriClient"
+ "logABCMetric:category:type:reporterID:"
+ "mADAMTransaction"
+ "setClientType:"
+ "sharedInstance:"
+ "v40@0:8@16I24S28q32"
- "\x02R"
- "%25s:%-5d AVVoiceTriggerClient init %@"
- "%25s:%-5d Created AVVoiceTriggerClient (%p)"
- "%25s:%-5d Non-BT route OutputSupportsVolume: %d"
- "%25s:%-5d destroyRecordEngine:  calling doneRecording by hand"
- "BTDetails_SupportsSoftwareVolume"

```
