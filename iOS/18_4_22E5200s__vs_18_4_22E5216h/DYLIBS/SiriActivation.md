## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3404.59.4.1.3
-  __TEXT.__text: 0x494e0
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x5c84
-  __TEXT.__const: 0x782
-  __TEXT.__cstring: 0x981d
-  __TEXT.__oslogstring: 0x678b
+3404.68.1.1.2
+  __TEXT.__text: 0x4962c
+  __TEXT.__auth_stubs: 0xb70
+  __TEXT.__objc_methlist: 0x5c6c
+  __TEXT.__const: 0x792
+  __TEXT.__cstring: 0x985d
+  __TEXT.__oslogstring: 0x683e
   __TEXT.__gcc_except_tab: 0xa3c
   __TEXT.__dlopen_cstrs: 0x168
   __TEXT.__swift5_typeref: 0x102

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x1498
+  __TEXT.__unwind_info: 0x14a0
   __TEXT.__eh_frame: 0x110
   __TEXT.__objc_classname: 0xf6d
-  __TEXT.__objc_methname: 0xd2da
+  __TEXT.__objc_methname: 0xd2d8
   __TEXT.__objc_methtype: 0x2084
-  __TEXT.__objc_stubs: 0x8ea0
+  __TEXT.__objc_stubs: 0x8ec0
   __DATA_CONST.__got: 0x688
-  __DATA_CONST.__const: 0x15e0
+  __DATA_CONST.__const: 0x15e8
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2be0
+  __DATA_CONST.__objc_selrefs: 0x2be8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x510
-  __AUTH_CONST.__auth_got: 0x5c0
+  __AUTH_CONST.__auth_got: 0x5c8
   __AUTH_CONST.__auth_ptr: 0x68
-  __AUTH_CONST.__const: 0x5c0
-  __AUTH_CONST.__cfstring: 0x46e0
-  __AUTH_CONST.__objc_const: 0x9758
+  __AUTH_CONST.__const: 0x5e0
+  __AUTH_CONST.__cfstring: 0x4700
+  __AUTH_CONST.__objc_const: 0x9730
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0xe18
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x628
+  __DATA.__objc_ivar: 0x624
   __DATA.__data: 0xf38
-  __DATA.__bss: 0x490
+  __DATA.__bss: 0x4a0
   __DATA_DIRTY.__objc_data: 0x1220
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2065
-  Symbols:   2555
-  CStrings:  3790
+  Functions: 2066
+  Symbols:   2557
+  CStrings:  3792
 
Symbols:
+ _AFDeviceSupportsVisualIntelligence
+ _AFIsAppleIntelligenceEnabled
+ _SiriIsCurrentProcessSpringBoard
- _AFVisualIntelligenceCameraRestricted
CStrings:
+ "%s #activation isVisualIntelligenceCameraControlLaunchEnabled: %d, isVisualIntelligenceSupported: %d, isCameraControlEnabled: %d, isAppleIntelligenceEnabled: %d"
+ "%s #activation isVisualIntelligenceWidgetControlEnabled: %d"
+ "-[SASActivationSourceEligibility shouldSystemOfferActivationForSource:systemAssistantExperienceEnabled:]"
+ "SASRequestSourceControlCenterTalkToSiri"
+ "SpringBoard"
+ "_saeAvailable"
+ "processName"
+ "saeAvailable"
+ "visualIntelligenceCameraControlEnabled"
- "%s #activation prewarmBundleIdentifier=%@"
- "-[SiriTostadaSource loadPrewarmBundleIdentifier]"
- "_isSAEEnabled"
- "_prewarmBundleIdentifier"
- "com.apple.VisualIntelligenceCamera"
- "isSAEEnabled"
- "loadPrewarmBundleIdentifier"

```
