## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3401.17.1.0.0
-  __TEXT.__text: 0x157d24
+3401.22.1.0.0
+  __TEXT.__text: 0x157e0c
   __TEXT.__auth_stubs: 0x1c20
-  __TEXT.__objc_methlist: 0x131e8
+  __TEXT.__objc_methlist: 0x13210
   __TEXT.__const: 0x5c0
   __TEXT.__gcc_except_tab: 0x378c
-  __TEXT.__cstring: 0x27177
-  __TEXT.__oslogstring: 0x1f741
+  __TEXT.__cstring: 0x2719d
+  __TEXT.__oslogstring: 0x1f72b
   __TEXT.__dlopen_cstrs: 0x197
-  __TEXT.__unwind_info: 0x4ee0
+  __TEXT.__unwind_info: 0x4ed8
   __TEXT.__objc_classname: 0x2f3f
-  __TEXT.__objc_methname: 0x380aa
-  __TEXT.__objc_methtype: 0x7c85
-  __TEXT.__objc_stubs: 0x1bfa0
+  __TEXT.__objc_methname: 0x38184
+  __TEXT.__objc_methtype: 0x7cc1
+  __TEXT.__objc_stubs: 0x1bfc0
   __DATA_CONST.__got: 0x1a88
   __DATA_CONST.__const: 0x4128
   __DATA_CONST.__objc_classlist: 0x858
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x4a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa6b8
+  __DATA_CONST.__objc_selrefs: 0xa6d0
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x438
   __AUTH_CONST.__auth_got: 0xe28
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1e20
-  __AUTH_CONST.__cfstring: 0x8fa0
-  __AUTH_CONST.__objc_const: 0x257d0
+  __AUTH_CONST.__cfstring: 0x8fc0
+  __AUTH_CONST.__objc_const: 0x25800
   __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_floatobj: 0x4c0
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __DATA.__objc_ivar: 0x1a84
+  __DATA.__objc_ivar: 0x1a88
   __DATA.__data: 0x3710
   __DATA.__bss: 0x678
   __DATA.__common: 0x18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8296
-  Symbols:   10084
-  CStrings:  14502
+  Functions: 8299
+  Symbols:   10087
+  CStrings:  14509
 
CStrings:
+ "forceCancelSecondPassTrigger"
+ "+[CSSiriAudioActivationInfo _shouldAllowRecordWhileBeepWithRecordRoute:playbackRoute:supportsEchoCancellation:speechRecordingMode:recordingInfo:]"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "secondpassTriggerCancellationLock"
+ "_shouldAllowRecordWhileBeepWithRecordRoute:playbackRoute:supportsEchoCancellation:speechRecordingMode:recordingInfo:"
+ "BuiltInMicrophoneDevice"
+ "cancelSecondPassTrigger"
+ "_cancelSecondPassTrigger"
+ "setSecondpassTriggerCancellationLock:"
+ "B52@0:8@16@24B32q36@44"
+ "%!s(MISSING) supportsEchoCancellation:%!u(MISSING) speechRecordingMode:%!l(MISSING)d recordRoute:%!{(MISSING)public}@ playbackRoute:%!{(MISSING)public}@, route in recordingInfo: %!{(MISSING)public}@"
+ "TB,N,V_cancelSecondPassTrigger"
+ "setCancelSecondPassTrigger:"
+ "T{os_unfair_lock_s=I},N,V_secondpassTriggerCancellationLock"
+ "{os_unfair_lock_s=I}16@0:8"
+ "_secondpassTriggerCancellationLock"
+ "%!s(MISSING) Requested cancelling 2nd pass trigger"
- "isSecondPassCancelled"
- "+[CSSiriAudioActivationInfo _shouldAllowRecordWhileBeepWithRecordRoute:playbackRoute:supportsEchoCancellation:speechRecordingMode:]"
- "%!s(MISSING) Second Pass request is marked for cancellation before second pass completion"
- "_shouldAllowRecordWhileBeepWithRecordRoute:playbackRoute:supportsEchoCancellation:speechRecordingMode:"
- "_isSecondPassCancelled"
- "setIsSecondPassCancelled:"
- "B44@0:8@16@24B32q36"
- "%!s(MISSING) Requested cancelling 2nd pass"
- "%!s(MISSING) supportsEchoCancellation:%!u(MISSING) speechRecordingMode:%!l(MISSING)d recordRoute:%!l(MISSING)d playbackRoute:%!l(MISSING)d"
- "TB,N,V_isSecondPassCancelled"

```
