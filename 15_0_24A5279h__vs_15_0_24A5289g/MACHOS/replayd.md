## replayd

> `/usr/libexec/replayd`

```diff

-558.41.0.0.0
-  __TEXT.__text: 0xa5664
-  __TEXT.__auth_stubs: 0x1730
-  __TEXT.__objc_stubs: 0xbe60
-  __TEXT.__objc_methlist: 0x52c0
-  __TEXT.__const: 0x430
-  __TEXT.__cstring: 0x1136f
-  __TEXT.__oslogstring: 0xf07d
-  __TEXT.__objc_classname: 0x9ca
-  __TEXT.__objc_methname: 0x11695
-  __TEXT.__objc_methtype: 0x337b
-  __TEXT.__gcc_except_tab: 0xf9c
+558.45.0.0.0
+  __TEXT.__text: 0xa6320
+  __TEXT.__auth_stubs: 0x1750
+  __TEXT.__objc_stubs: 0xbf80
+  __TEXT.__objc_methlist: 0x5348
+  __TEXT.__const: 0x440
+  __TEXT.__oslogstring: 0xf140
+  __TEXT.__cstring: 0x11474
+  __TEXT.__objc_classname: 0x9e2
+  __TEXT.__objc_methname: 0x11855
+  __TEXT.__objc_methtype: 0x33b0
+  __TEXT.__gcc_except_tab: 0xfc0
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__info_plist: 0x4a6
-  __TEXT.__unwind_info: 0x1a20
-  __DATA_CONST.__auth_got: 0xba8
-  __DATA_CONST.__got: 0x9d8
-  __DATA_CONST.__const: 0x2040
-  __DATA_CONST.__cfstring: 0x4fe0
-  __DATA_CONST.__objc_classlist: 0x278
+  __TEXT.__unwind_info: 0x1a50
+  __DATA_CONST.__auth_got: 0xbb8
+  __DATA_CONST.__got: 0x9f8
+  __DATA_CONST.__const: 0x2050
+  __DATA_CONST.__cfstring: 0x4f60
+  __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_intobj: 0x468
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xf360
-  __DATA.__objc_selrefs: 0x3790
-  __DATA.__objc_ivar: 0xb50
-  __DATA.__objc_data: 0x18b0
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA.__objc_const: 0xf4a8
+  __DATA.__objc_selrefs: 0x37d8
+  __DATA.__objc_ivar: 0xb64
+  __DATA.__objc_data: 0x1900
   __DATA.__data: 0xa38
-  __DATA.__bss: 0x260
+  __DATA.__bss: 0x258
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/Versions/A/CallKit
+  - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
+  - /System/Library/PrivateFrameworks/SystemStatus.framework/Versions/A/SystemStatus
   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libCTGreenTeaLogger.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2852
-  Symbols:   699
-  CStrings:  1570
+  Functions: 2869
+  Symbols:   705
+  CStrings:  1573
 
Symbols:
+ _AudioObjectSetPropertyData
+ _OBJC_CLASS_$_STActivityAttribution
+ _OBJC_CLASS_$_STAttributedEntity
+ _OBJC_CLASS_$_STMediaStatusDomainMicrophoneRecordingAttribution
+ _OBJC_CLASS_$_STMediaStatusDomainPublisher
+ _task_info
CStrings:
+ "%!s(MISSING)%!@(MISSING)"
+ ","
+ "-[SCMicAttributionManager dealloc]"
+ "-[SCMicAttributionManager init]"
+ "-[SCMicAttributionManager suppressCoreAudioRecordingIndicator:]"
+ "-[SCMicAttributionManager updateMicrophoneCaptureStarted:withAuditToken:]"
+ "-[SCMicAttributionManager updateMicrophoneCaptureStarted:withAuditToken:]_block_invoke"
+ ".pid."
+ "/usr/libexec/replayd"
+ "RPKTestUtilAuditTokenForCurrentProcess"
+ "TPL"
+ "v16@?0@\"STMutableMediaStatusDomainData\"8"
- "+[SCAppNameUtil isAllowedInternalBundleID:]"
- "NO"
- "ReplayKitTestRunnerMacOS"
- "YES"
- "com.apple."
- "com.apple.WebKit.GPU"
- "com.apple.screencapture"
- "dt.Xcode"
- "replayd"

```
