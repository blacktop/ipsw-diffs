## VoiceControl

> `/System/Library/PrivateFrameworks/VoiceControl.framework/Versions/A/VoiceControl`

```diff

-40.1.0.0.0
-  __TEXT.__text: 0x3f8cc
-  __TEXT.__objc_methlist: 0x934
+41.1.3.0.0
+  __TEXT.__text: 0x3fe58
+  __TEXT.__objc_methlist: 0x93c
   __TEXT.__const: 0x12d8
   __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__cstring: 0x1d1a
+  __TEXT.__cstring: 0x1d3a
   __TEXT.__dlopen_cstrs: 0x7a
-  __TEXT.__oslogstring: 0xa1d
+  __TEXT.__oslogstring: 0xa9d
   __TEXT.__constg_swiftt: 0x594
   __TEXT.__swift5_typeref: 0x58e
   __TEXT.__swift5_fieldmd: 0x80c

   __TEXT.__swift5_capture: 0x64
   __TEXT.__swift5_protos: 0x10
   __TEXT.__unwind_info: 0xbe8
-  __TEXT.__eh_frame: 0x638
+  __TEXT.__eh_frame: 0x62c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x690
+  __DATA_CONST.__objc_selrefs: 0x6a0
   __DATA_CONST.__got: 0x2a8
   __AUTH_CONST.__const: 0x1de0
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0xab8
-  __AUTH_CONST.__auth_got: 0x9d8
-  __AUTH_CONST.__auth_ptr: 0x270
+  __AUTH_CONST.__auth_got: 0x9e8
+  __AUTH_CONST.__auth_ptr: 0x278
   __AUTH.__objc_data: 0x590
   __AUTH.__data: 0x3f0
-  __DATA.__data: 0x598
+  __DATA.__data: 0x5a0
   __DATA.__bss: 0x1c30
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x1d8

   - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/Speech.framework/Versions/A/Speech
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/Versions/A/AXCoreUtilities

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1231
-  Symbols:   594
-  CStrings:  271
+  Functions: 1234
+  Symbols:   597
+  CStrings:  274
 
Symbols:
+ _IOPMAssertionDeclareUserActivity
+ _keypath_get_selector_vciScreenshotStorageEnabled
+ _objc_msgSend$processName
+ _objc_msgSend$setVciScreenshotStorageEnabled:
+ _objc_msgSend$vciScreenshotStorageEnabled
+ _swift_endAccess
- _keypath_get_selector_voiceControlIntelligenceScreenshotDebugging
- _objc_msgSend$setVoiceControlIntelligenceScreenshotDebugging:
- _objc_msgSend$voiceControlIntelligenceScreenshotDebugging
CStrings:
+ "Declared user activity from %{public}s, assertion %{public}u"
+ "Failed to declare user activity from %{public}s: %{public}d"
+ "Voice Control Command Matched"
```
