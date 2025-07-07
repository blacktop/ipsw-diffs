## continuitycaptured

> `/usr/libexec/continuitycaptured`

```diff

-655.0.0.122.4
-  __TEXT.__text: 0x10104
+659.0.0.0.4
+  __TEXT.__text: 0x108ec
   __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0x1bc0
-  __TEXT.__objc_methlist: 0x81c
+  __TEXT.__objc_stubs: 0x1c60
+  __TEXT.__objc_methlist: 0x82c
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x5d8
-  __TEXT.__objc_methname: 0x1ffa
-  __TEXT.__oslogstring: 0x2213
-  __TEXT.__cstring: 0x13d6
+  __TEXT.__gcc_except_tab: 0x60c
+  __TEXT.__objc_methname: 0x2073
+  __TEXT.__oslogstring: 0x237f
+  __TEXT.__cstring: 0x13df
   __TEXT.__objc_classname: 0x19f
   __TEXT.__objc_methtype: 0x85a
-  __TEXT.__unwind_info: 0x418
+  __TEXT.__unwind_info: 0x428
   __DATA_CONST.__auth_got: 0x360
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0x838
+  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__const: 0x8b0
   __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x90
   __DATA.__objc_const: 0xc48
-  __DATA.__objc_selrefs: 0x880
+  __DATA.__objc_selrefs: 0x8a8
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x3c0

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
+  - /System/Library/PrivateFrameworks/MediaServices.framework/MediaServices
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 44A31420-E602-38BE-BC4B-C5DA4FCF5887
-  Functions: 221
-  Symbols:   222
-  CStrings:  714
+  UUID: 9D59F559-20A9-3D7C-B434-A8177941A05E
+  Functions: 230
+  Symbols:   224
+  CStrings:  725
 
Symbols:
+ _OBJC_CLASS_$_ICPrivacyInfo
+ _OBJC_CLASS_$_MSVBlockGuard
CStrings:
+ "%{public}@ Error checking music account user state: %@"
+ "%{public}@ could not load regulatory info"
+ "%{public}@ display name not accepted for ICMediaUser activeUserState, bailing to Music"
+ "%{public}@ got ICMediaUser activeUserState, retrying checking music account"
+ "%{public}@ retrieved music account state hasAcceptedPrivacyAck:%d hasAcceptedDisplayName:%d"
+ "%{public}@ timed out re-loading ICMediaUser activeUserState"
+ "%{public}@ unable to refresh ICMediaUser activeUserState when checking music account"
+ "_checkMusicAccount:"
+ "disarm"
+ "initWithTimeout:interruptionHandler:"
+ "privacyAcknowledgementRequiredForMusic"
+ "sharedPrivacyInfo"
+ "v16@?0q8"
- "%{public}@ got ICMediaUser activeUserState, retrying join"
- "%{public}@ unable to refresh ICMediaUser activeUserState, bailing to Music"

```
