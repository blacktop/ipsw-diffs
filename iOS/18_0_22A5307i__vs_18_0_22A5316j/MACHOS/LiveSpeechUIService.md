## LiveSpeechUIService

> `/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService`

```diff

-3132.8.0.0.0
-  __TEXT.__text: 0xa5b64
-  __TEXT.__auth_stubs: 0x2b80
+3134.3.0.0.0
+  __TEXT.__text: 0xa46e8
+  __TEXT.__auth_stubs: 0x2b70
   __TEXT.__objc_stubs: 0xa0
-  __TEXT.__objc_methlist: 0x3e8
-  __TEXT.__const: 0x4800
+  __TEXT.__objc_methlist: 0x400
+  __TEXT.__const: 0x46f0
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__cstring: 0x24aa
-  __TEXT.__oslogstring: 0xeeb
-  __TEXT.__objc_classname: 0xd3
-  __TEXT.__objc_methname: 0x1d04
-  __TEXT.__objc_methtype: 0x8bd
+  __TEXT.__cstring: 0x24fa
+  __TEXT.__oslogstring: 0xebb
+  __TEXT.__objc_classname: 0xb5
+  __TEXT.__objc_methname: 0x1cd5
+  __TEXT.__objc_methtype: 0x86e
   __TEXT.__dlopen_cstrs: 0x6a
-  __TEXT.__swift5_typeref: 0x102b1
-  __TEXT.__constg_swiftt: 0x1b9c
+  __TEXT.__swift5_typeref: 0x1032f
+  __TEXT.__constg_swiftt: 0x1ad8
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x17a7
-  __TEXT.__swift5_fieldmd: 0x1580
-  __TEXT.__swift5_assocty: 0x5d8
-  __TEXT.__swift5_proto: 0x1dc
-  __TEXT.__swift5_types: 0x140
-  __TEXT.__swift5_capture: 0x9e4
+  __TEXT.__swift5_reflstr: 0x16d7
+  __TEXT.__swift5_fieldmd: 0x1508
+  __TEXT.__swift5_assocty: 0x5c0
+  __TEXT.__swift5_proto: 0x1d8
+  __TEXT.__swift5_types: 0x13c
+  __TEXT.__swift5_capture: 0x9c4
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x1b08
+  __TEXT.__unwind_info: 0x1ad0
   __TEXT.__eh_frame: 0x13a0
-  __DATA_CONST.__auth_got: 0x15d0
-  __DATA_CONST.__got: 0xbb0
-  __DATA_CONST.__auth_ptr: 0xc78
-  __DATA_CONST.__const: 0x33b8
+  __DATA_CONST.__auth_got: 0x15c8
+  __DATA_CONST.__got: 0xb98
+  __DATA_CONST.__auth_ptr: 0xc48
+  __DATA_CONST.__const: 0x32a8
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA.__objc_const: 0x2308
-  __DATA.__objc_selrefs: 0x6b8
+  __DATA.__objc_const: 0x22a8
+  __DATA.__objc_selrefs: 0x6d0
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x1420
-  __DATA.__data: 0x37f0
+  __DATA.__objc_data: 0x13c0
+  __DATA.__data: 0x3770
   __DATA.__objc_stublist: 0x18
-  __DATA.__bss: 0x4030
-  __DATA.__common: 0x188
+  __DATA.__bss: 0x3f80
+  __DATA.__common: 0x190
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2899
-  Symbols:   336
-  CStrings:  763
+  Functions: 2857
+  Symbols:   334
+  CStrings:  759
 
Symbols:
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$__TtC19LiveSpeechUIService29LiveSpeechCaptionsCallManager
+ _OBJC_METACLASS_$__TtC19LiveSpeechUIService29LiveSpeechCaptionsCallManager
- _OBJC_CLASS_$_AXLTPhoneCallListener
- _OBJC_CLASS_$__TtC19LiveSpeechUIService21LiveSpeechCallManager
- _OBJC_METACLASS_$__TtC19LiveSpeechUIService21LiveSpeechCallManager
- __AXSLiveTranscriptionInCallEnabled
- _kAXSLiveTranscriptionInCallEnabledDidChangeNotification
CStrings:
+ "AXLiveSpeechAddPhrasePlaceholder"
+ "Failed to set audio session properties: %!@(MISSING)"
+ "T@\"_TtC19LiveSpeechUIService29LiveSpeechCaptionsCallManager\",N,R"
+ "_TtC19LiveSpeechUIService29LiveSpeechCaptionsCallManager"
+ "_TtP19LiveSpeechUIService37LiveSpeechCaptionsCallManagerDelegate_"
+ "_isActive"
+ "addObject:"
+ "allActiveCallsEnded"
+ "allObjects"
+ "callConnected"
+ "com.apple.ax.livespeechcaptions.call"
+ "containsObject:"
+ "count"
+ "observers"
+ "removeObject:"
+ "weakObjectsHashTable"
- "AXLTPhoneCallListenerDelegate"
- "Failed to configure live speech audio session with error: %!@(MISSING)"
- "_TtC19LiveSpeechUIService21LiveSpeechCallManager"
- "_audioHistogramSize"
- "audioHistogram"
- "audioHistogram"
- "com.appl.ax.livespeech.call"
- "doubleValue"
- "histogramTimer"
- "inCallOn"
- "inCallStateChanged"
- "isCallActive"
- "phoneCallListenerCallConnected:callID:"
- "phoneCallListenerCallDialing:"
- "phoneCallListenerCallEnded:callID:"
- "setUtilityType:"
- "updateInCallState: %!{(MISSING)bool}d"
- "v24@0:8@\"AXLTPhoneCallListener\"16"
- "v32@0:8@\"AXLTPhoneCallListener\"16@\"NSUUID\"24"

```
