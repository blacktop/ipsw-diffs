## SiriUIActivation

> `/System/Library/PrivateFrameworks/SiriUIActivation.framework/SiriUIActivation`

```diff

-3404.59.4.1.3
-  __TEXT.__text: 0x218c4
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x1c2c
+3404.68.1.1.2
+  __TEXT.__text: 0x2256c
+  __TEXT.__auth_stubs: 0xd50
+  __TEXT.__objc_methlist: 0x1c34
   __TEXT.__const: 0x2be
   __TEXT.__gcc_except_tab: 0xadc
-  __TEXT.__cstring: 0x3962
-  __TEXT.__oslogstring: 0x40c4
+  __TEXT.__cstring: 0x39c2
+  __TEXT.__oslogstring: 0x4104
   __TEXT.__swift5_typeref: 0x177
   __TEXT.__constg_swiftt: 0x134
   __TEXT.__swift5_reflstr: 0x11b

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0xa98
-  __TEXT.__eh_frame: 0x570
+  __TEXT.__unwind_info: 0xaa0
+  __TEXT.__eh_frame: 0x5c0
   __TEXT.__objc_classname: 0x318
-  __TEXT.__objc_methname: 0x7786
+  __TEXT.__objc_methname: 0x77ac
   __TEXT.__objc_methtype: 0x14aa
-  __TEXT.__objc_stubs: 0x5320
-  __DATA_CONST.__got: 0x470
+  __TEXT.__objc_stubs: 0x5360
+  __DATA_CONST.__got: 0x490
   __DATA_CONST.__const: 0xb80
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a28
+  __DATA_CONST.__objc_selrefs: 0x1a38
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH_CONST.__auth_got: 0x6b8
   __AUTH_CONST.__auth_ptr: 0x90
   __AUTH_CONST.__const: 0x3d0
-  __AUTH_CONST.__cfstring: 0x7a0
+  __AUTH_CONST.__cfstring: 0x7c0
   __AUTH_CONST.__objc_const: 0x1c30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30

   __DATA_DIRTY.__objc_data: 0x328
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x40
+  - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreHaptics.framework/CoreHaptics

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 719
-  Symbols:   966
-  CStrings:  1697
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
- _objc_retain_x27
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initializeBufferWithCopyOfBuffer
CStrings:
+ "%s #activation prewarming camera for bundleID '%{public}@'"
+ "-[SiriPresentationViewController _prewarmCameraForBundleIdentifier:]"
+ "-[SiriPresentationViewController _restartVisualIntelligenceIfNeeded]"
+ "_prewarmCameraForBundleIdentifier:"
+ "_restartVisualIntelligenceIfNeeded"
+ "com.apple.VisualIntelligenceCamera"
+ "isForceTelephonyURL"
+ "numberWithLongLong:"
+ "saeAvailable"
- "-[SiriPresentationViewController _restartVisualIntelligenceIfNeededForRequestOptions:]"
- "_restartVisualIntelligenceIfNeededForRequestOptions:"
- "hasTelephonyScheme"
- "isSAEEnabled"

```
