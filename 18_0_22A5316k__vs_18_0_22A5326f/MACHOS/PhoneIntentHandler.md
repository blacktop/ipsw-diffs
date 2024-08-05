## PhoneIntentHandler

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/PlugIns/PhoneIntentHandler.appex/PhoneIntentHandler`

```diff

-1469.100.11.0.0
-  __TEXT.__text: 0x2e3fc
-  __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_stubs: 0x50c0
-  __TEXT.__objc_methlist: 0x1890
-  __TEXT.__const: 0x1c2
-  __TEXT.__cstring: 0x163f
-  __TEXT.__oslogstring: 0x6ba3
+1471.100.2.2.1
+  __TEXT.__text: 0x2e904
+  __TEXT.__auth_stubs: 0xda0
+  __TEXT.__objc_stubs: 0x5100
+  __TEXT.__objc_methlist: 0x1898
+  __TEXT.__const: 0x1c8
+  __TEXT.__cstring: 0x1663
+  __TEXT.__oslogstring: 0x6d63
   __TEXT.__objc_classname: 0x69d
-  __TEXT.__objc_methname: 0x6804
-  __TEXT.__objc_methtype: 0x12f3
+  __TEXT.__objc_methname: 0x6875
+  __TEXT.__objc_methtype: 0x1307
   __TEXT.__gcc_except_tab: 0x258
-  __TEXT.__swift5_typeref: 0x23a
+  __TEXT.__swift5_typeref: 0x238
   __TEXT.__swift5_fieldmd: 0x8c
   __TEXT.__constg_swiftt: 0x148
   __TEXT.__swift5_reflstr: 0x39
-  __TEXT.__swift5_capture: 0x120
+  __TEXT.__swift5_capture: 0x1e8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x898
-  __TEXT.__eh_frame: 0x778
-  __DATA_CONST.__auth_got: 0x6d8
+  __TEXT.__unwind_info: 0x8c0
+  __TEXT.__eh_frame: 0x7a8
+  __DATA_CONST.__auth_got: 0x6e0
   __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x9e0
-  __DATA_CONST.__cfstring: 0xf60
+  __DATA_CONST.__auth_ptr: 0x68
+  __DATA_CONST.__const: 0xbb8
+  __DATA_CONST.__cfstring: 0xfc0
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe8

   __DATA_CONST.__objc_arraydata: 0x1d0
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x5500
-  __DATA.__objc_selrefs: 0x1668
+  __DATA.__objc_selrefs: 0x1678
   __DATA.__objc_ivar: 0x17c
   __DATA.__objc_data: 0xfa8
-  __DATA.__data: 0xc18
+  __DATA.__data: 0xc58
   __DATA.__bss: 0x68
   __DATA.__common: 0x20
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 752
-  Symbols:   401
-  CStrings:  1851
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 763
+  Symbols:   411
+  CStrings:  1860
 
Symbols:
+ _INCallCapabilityGetBackingType
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "(unknown: %!i(MISSING))"
+ "AUDIO_CALL"
+ "B36@0:8q16q24B32"
+ "Call capability is already set in plugin, no inferring needed"
+ "Inferring audio callCapability because provider is FaceTime, request callCapability was audio and audio is supported"
+ "Inferring video callCapability because provider is FaceTime, requested callCapability was video and video is supported."
+ "VIDEO_CALL"
+ "[WARN] Unable to infer callCapability. Execution Context is assistantDialog. Provider is Facetime, but neither facetime audio nor video calling are supported."
+ "[WARN] Unable to infer callCapability. Execution Context is not assistantDialog. Provider is Facetime, but neither facetime audio nor video calling are supported."
+ "_executionContext"
+ "inferCallCapabilityForPreferredCallProvider:recentCall:initialCallCapability:idiom:isDisplayDisabled:executionContext:"
+ "q60@0:8q16@24q32q40B48q52"
+ "shouldInferAudioCapabilityForRequestedCallCapability:idiom:isDisplayDisabled:"
- "Call capability is already set, no inferring needed"
- "[WARN] Unable to infer callCapability. Provider is Facetime, but neither facetime audio nor video calling are supported."
- "inferCallCapabilityForPreferredCallProvider:recentCall:initialCallCapability:idiom:isDisplayDisabled:"
- "q52@0:8q16@24q32q40B48"

```
