## SiriUIActivation

> `/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation`

```diff

-3403.11.2.11.3
-  __TEXT.__text: 0x22250
-  __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x1454
-  __TEXT.__const: 0x28e
+3404.68.1.1.2
+  __TEXT.__text: 0x2256c
+  __TEXT.__auth_stubs: 0xd50
+  __TEXT.__objc_methlist: 0x1c34
+  __TEXT.__const: 0x2be
   __TEXT.__gcc_except_tab: 0xadc
-  __TEXT.__cstring: 0x3bc0
-  __TEXT.__oslogstring: 0x40c4
+  __TEXT.__cstring: 0x39c2
+  __TEXT.__oslogstring: 0x4104
   __TEXT.__swift5_typeref: 0x177
   __TEXT.__constg_swiftt: 0x134
   __TEXT.__swift5_reflstr: 0x11b

   __TEXT.__swift5_capture: 0xec
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0xac8
-  __TEXT.__eh_frame: 0x588
+  __TEXT.__swift_as_entry: 0x30
+  __TEXT.__swift_as_ret: 0x34
+  __TEXT.__unwind_info: 0xaa0
+  __TEXT.__eh_frame: 0x5c0
   __TEXT.__objc_classname: 0x318
-  __TEXT.__objc_methname: 0x7777
+  __TEXT.__objc_methname: 0x77ac
   __TEXT.__objc_methtype: 0x14aa
-  __TEXT.__objc_stubs: 0x5300
-  __DATA_CONST.__got: 0x470
-  __DATA_CONST.__const: 0xb88
+  __TEXT.__objc_stubs: 0x5360
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0xb80
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1950
+  __DATA_CONST.__objc_selrefs: 0x1a38
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x6c0
+  __AUTH_CONST.__auth_got: 0x6b8
   __AUTH_CONST.__auth_ptr: 0x90
   __AUTH_CONST.__const: 0x3d0
-  __AUTH_CONST.__cfstring: 0x7a0
-  __AUTH_CONST.__objc_const: 0x2ac0
+  __AUTH_CONST.__cfstring: 0x7c0
+  __AUTH_CONST.__objc_const: 0x1c30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xa0

   __DATA_DIRTY.__objc_data: 0x328
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x40
+  - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreHaptics.framework/CoreHaptics

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 726
-  Symbols:   962
-  CStrings:  1709
+  Functions: 720
+  Symbols:   973
+  CStrings:  1702
 
Symbols:
+ _AVCapturePrewarmReasonCameraLaunchSiri
+ _AVCapturePrewarmReasonKey
+ _AVCapturePrewarmUserInteractionAbsoluteTimeKey
+ _AVCapturePrewarmUserInteractionContinuousTimeKey
+ _AVCapturePrewarmWithOptions
+ _mach_continuous_time
+ _objc_retain_x28
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- __swift_FORCE_LOAD_$_swiftFileProvider
CStrings:
+ "#activation #quickTypeGate %s: exiting beginPollingWithContinuation"
+ "%s #activation prewarming camera for bundleID '%{public}@'"
+ "%s #visualIntelligence Successfully killed Visual Intelligence"
+ "-[SiriPresentationViewController _prewarmCameraForBundleIdentifier:]"
+ "-[SiriPresentationViewController _restartVisualIntelligenceIfNeeded]"
+ "_prewarmCameraForBundleIdentifier:"
+ "_restartVisualIntelligenceIfNeeded"
+ "com.apple.VisualIntelligenceCamera"
+ "isForceTelephonyURL"
+ "numberWithLongLong:"
+ "preheatRequest"
+ "saeAvailable"
- "#kcs #activation #quickTypeGate %s: exiting beginPollingWithContinuation"
- "%s #visualIntelligence Succesfully killed Visual Intelligence"
- "-[SiriPresentationViewController _restartVisualIntelligenceIfNeededForRequestOptions:]"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_restartVisualIntelligenceIfNeededForRequestOptions:"
- "hasTelephonyScheme"
- "invalid Collection: less than 'count' elements in collection"
- "isSAEEnabled"

```
