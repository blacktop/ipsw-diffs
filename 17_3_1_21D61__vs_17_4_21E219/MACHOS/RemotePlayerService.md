## RemotePlayerService

> `/System/Library/Frameworks/MediaPlayer.framework/XPCServices/RemotePlayerService.xpc/RemotePlayerService`

```diff

-4023.410.2.0.0
-  __TEXT.__text: 0x2260
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x184
-  __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__objc_methname: 0xa08
-  __TEXT.__cstring: 0x3cd
-  __TEXT.__oslogstring: 0x37c
+4023.510.7.0.0
+  __TEXT.__text: 0x2268
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x5e0
+  __TEXT.__objc_methlist: 0x190
+  __TEXT.__const: 0x18
+  __TEXT.__gcc_except_tab: 0x60
+  __TEXT.__objc_methname: 0xa1a
+  __TEXT.__cstring: 0x3cf
+  __TEXT.__oslogstring: 0x2f7
   __TEXT.__objc_classname: 0x9b
   __TEXT.__objc_methtype: 0x239
   __TEXT.__dlopen_cstrs: 0xad
-  __TEXT.__unwind_info: 0x114
-  __DATA_CONST.__auth_got: 0x1d8
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x230
-  __DATA_CONST.__cfstring: 0x200
+  __TEXT.__unwind_info: 0x110
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0x1f0
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x7c8
-  __DATA.__objc_selrefs: 0x240
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x60
-  __DATA.__objc_superrefs: 0x8
+  __DATA.__objc_selrefs: 0x248
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x180
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x50
+  - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
+  - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
+  - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/MediaServices.framework/MediaServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA99F679-0697-3643-9A5A-DC5DA940A1DB
-  Functions: 55
-  Symbols:   82
-  CStrings:  227
+  UUID: C7FB3C5E-2AC3-302C-86BA-8E23EA7B7BE9
+  Functions: 56
+  Symbols:   80
+  CStrings:  224
 
Symbols:
+ _AVAudioSessionMediaServicesWereResetNotification
+ _OBJC_CLASS_$_NSNotificationCenter
+ _dlerror
+ _dlsym
- _OBJC_CLASS_$_RBSAssertion
- _OBJC_CLASS_$_RBSDomainAttribute
- _OBJC_CLASS_$_RBSTarget
- _objc_release_x23
- _objc_retain
- _objc_retain_x1
CStrings:
+ "MPSharedBackgroundTaskProvider"
+ "T@\"NSString\",?,R,C"
+ "_mediaServicesReset:"
+ "addObserver:selector:name:object:"
+ "beginTaskWithName:expirationHandler:"
+ "defaultCenter"
+ "endTask:"
+ "id<MSVBackgroundTaskProviding> _sharedBackgroundTaskProvider(void)"
- "MPRemotePlayerService: %{public}@ invalidated with error: %{public}@"
- "MPRemotePlayerService: Took RBSAssertion: %{public}@ %{public}@"
- "PlaybackEnginePrep"
- "acquireWithInvalidationHandler:"
- "attributeWithDomain:name:"
- "com.apple.MediaPlayer.RemotePlayerService"
- "currentProcess"
- "initWithExplanation:target:attributes:"
- "v24@?0@\"RBSAssertion\"8@\"NSError\"16"

```
