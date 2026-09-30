## AssistantUI

> `/System/Library/PrivateFrameworks/AssistantUI.framework/AssistantUI`

```diff

-3403.11.2.11.3
-  __TEXT.__text: 0x54e80
-  __TEXT.__auth_stubs: 0xe70
-  __TEXT.__objc_methlist: 0x4b60
-  __TEXT.__const: 0x5b4
-  __TEXT.__gcc_except_tab: 0x15c8
-  __TEXT.__cstring: 0x7bdb
-  __TEXT.__oslogstring: 0x4efa
+3404.68.1.1.2
+  __TEXT.__text: 0x55e04
+  __TEXT.__auth_stubs: 0xe80
+  __TEXT.__objc_methlist: 0x6afc
+  __TEXT.__const: 0x5c4
+  __TEXT.__gcc_except_tab: 0x15ac
+  __TEXT.__cstring: 0x7d7b
+  __TEXT.__oslogstring: 0x50be
   __TEXT.__dlopen_cstrs: 0x46f
   __TEXT.__ustring: 0x1c
   __TEXT.__constg_swiftt: 0x1f0

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x1b40
+  __TEXT.__unwind_info: 0x1bb8
   __TEXT.__objc_classname: 0xb4e
-  __TEXT.__objc_methname: 0x15bb1
-  __TEXT.__objc_methtype: 0x447a
-  __TEXT.__objc_stubs: 0xf8e0
-  __DATA_CONST.__got: 0xbc0
-  __DATA_CONST.__const: 0x19d8
+  __TEXT.__objc_methname: 0x15d9a
+  __TEXT.__objc_methtype: 0x44ac
+  __TEXT.__objc_stubs: 0xfa60
+  __DATA_CONST.__got: 0xbd8
+  __DATA_CONST.__const: 0x1a20
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4bb8
+  __DATA_CONST.__objc_selrefs: 0x4ee0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x110
-  __AUTH_CONST.__auth_got: 0x748
+  __AUTH_CONST.__auth_got: 0x750
   __AUTH_CONST.__auth_ptr: 0x40
-  __AUTH_CONST.__const: 0xca0
-  __AUTH_CONST.__cfstring: 0x2980
-  __AUTH_CONST.__objc_const: 0xb608
+  __AUTH_CONST.__const: 0xcc0
+  __AUTH_CONST.__cfstring: 0x29a0
+  __AUTH_CONST.__objc_const: 0x7c00
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x818
   __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x560
+  __DATA.__objc_ivar: 0x564
   __DATA.__data: 0x14f8
-  __DATA.__bss: 0x300
+  __DATA.__bss: 0x2c0
   __DATA_DIRTY.__objc_data: 0x960
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2230
-  Symbols:   2917
-  CStrings:  4716
+  Functions: 2302
+  Symbols:   2993
+  CStrings:  4751
 
Symbols:
+ _SAUIPhotoPickerRequestClassIdentifier
+ _SRUIFTypeToSiriLatencyDuration
+ __os_log_debug_impl
+ _kCACornerCurveID1
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _SAUIStartImmersiveExperienceClassIdentifier
- __swift_FORCE_LOAD_$_swiftFileProvider
CStrings:
+ "\x01\x13\x15\x11!\x18"
+ "%s #latency type to siri latency timer cancelled"
+ "%s #latency type to siri latency timer fired"
+ "%s #latency type to siri latency timer started"
+ "%s Calling completion to render bug button image"
+ "%s Error in starting direct request: %@"
+ "%s Found and loaded debug bundle to render bug button"
+ "%s Loading debug bundle to render bug button"
+ "%s Photo assetIdentifiers are sent via direct invocation: %@"
+ "%s SAStartLocalRequest with PhotoPicker result: %@"
+ "%s State machine should not be used initially on the main thread because it can block on an XPC call"
+ "-[AFUISiriCompactView _loadReportBugButtonTemplateImageInBackgroundWithCompletion:]"
+ "-[AFUISiriCompactView _loadReportBugButtonTemplateImageInBackgroundWithCompletion:]_block_invoke"
+ "-[AFUISiriSession _cancelTypeToSiriLatencyTimerIfNeeded]"
+ "-[AFUISiriSession _handlePhotoPickerRequest:completion:]_block_invoke"
+ "-[AFUISiriSession _startTypeToSiriLatencyTimer]"
+ "-[AFUISiriSession _typeToSiriLatencyTimerFired]"
+ "_cancelTypeToSiriLatencyTimerIfNeeded"
+ "_handlePhotoPickerRequest:completion:"
+ "_photoPickerDirectActionRequestWith:assetIdentifiers:"
+ "_setContinuousCornerRadius:"
+ "_startDirectRequestWith:turnIdentifier:completion:"
+ "_startTypeToSiriLatencyTimer"
+ "_typeToSiriLatencyTimer"
+ "_typeToSiriLatencyTimerFired"
+ "assetIdentifiers"
+ "assistantConnection:replayAll:with:"
+ "assistantConnection:replayAt:with:"
+ "assistantConnection:setReplayEnabled:"
+ "assistantConnection:setReplayOverridePath:"
+ "directInvocationBundleIdentifier"
+ "saeAvailable"
+ "setUserData:"
+ "siriSessionReplayAll:with:"
+ "siriSessionReplayAt:with:"
+ "siriSessionRequestedPhotoSelectionWithPhotoPickerRequest:completion:"
+ "siriSessionSetReplayEnabled:"
+ "siriSessionSetReplayOverridePath:"
+ "startAttendingWithDeviceID:"
+ "v24@0:8@\"NSURL\"16"
+ "v32@0:8@\"AFConnection\"16@\"NSURL\"24"
+ "v32@0:8@\"SAUIPhotoPickerRequest\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8Q16@\"NSURL\"24"
+ "v40@0:8@\"AFConnection\"16Q24@\"NSURL\"32"
+ "\xd2\x11"
- "\x01\x13\x14\x11!\x18"
- "%s %@ should not be used initially on the main thread because it can block on an XPC call"
- "cancelPhotoSelectionWithAnimation:"
- "isSAEEnabled"
- "requestPhotoSelectionWithSearchString:completion:"
- "siriSessionDidReceiveStartImmersiveExperienceCommand:completion:"
- "siriSessionRequestedPhotoSelectionWithSearchString:completion:"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
- "v32@0:8@\"SAUIStartImmersiveExperience\"16@?<v@?@\"AceObject<SAAceCommand>\">24"
- "\xc2\x11"

```
