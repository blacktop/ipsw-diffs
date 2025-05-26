## ShazamCore

> `/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore`

```diff

-236.4.0.0.0
-  __TEXT.__text: 0x9040
+236.7.0.0.0
+  __TEXT.__text: 0x8e50
   __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0xd14
+  __TEXT.__objc_methlist: 0xcc4
   __TEXT.__const: 0x72
   __TEXT.__cstring: 0x94a
-  __TEXT.__oslogstring: 0x52f
-  __TEXT.__gcc_except_tab: 0x104
+  __TEXT.__oslogstring: 0x50a
+  __TEXT.__gcc_except_tab: 0xe4
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x388
+  __TEXT.__unwind_info: 0x374
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x1e4
-  __TEXT.__objc_methname: 0x281e
-  __TEXT.__objc_methtype: 0x53c
-  __TEXT.__objc_stubs: 0x1e60
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_methname: 0x2692
+  __TEXT.__objc_methtype: 0x4f0
+  __TEXT.__objc_stubs: 0x1d60
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x498
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x17f0
-  __DATA_CONST.__objc_selrefs: 0xa18
+  __DATA_CONST.__objc_const: 0x1780
+  __DATA_CONST.__objc_selrefs: 0x9d0
   __AUTH_CONST.__cfstring: 0xce0
   __AUTH_CONST.__objc_const: 0x8a8
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0x2a0
   __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_classrefs: 0x188
+  __DATA.__objc_classrefs: 0x180
   __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0xd8
+  __DATA.__objc_ivar: 0xd0
   __DATA.__data: 0x120
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
-  Functions: 300
-  Symbols:   1305
-  CStrings:  719
+  Functions: 293
+  Symbols:   1278
+  CStrings:  703
 
Symbols:
+ -[SHRemoteConfiguration fetchMusicSubscriptionStatus:]
+ GCC_except_table16
+ GCC_except_table19
+ ___54-[SHRemoteConfiguration fetchMusicSubscriptionStatus:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e66_v24?0"ICLightweightMusicSubscriptionStatusResponse"8"NSError"16ls32l8
+ ___block_literal_global.44
+ ___block_literal_global.46
+ ___block_literal_global.48
+ ___block_literal_global.50
+ ___block_literal_global.52
+ ___block_literal_global.54
+ ___block_literal_global.56
+ ___block_literal_global.58
+ ___block_literal_global.60
+ ___block_literal_global.62
- -[SHMusicSubscriptionStatus hasActiveAppleMusicSubscription]
- -[SHRemoteConfiguration dealloc]
- -[SHRemoteConfiguration didChangeMusicSubscriptionStatus:]
- -[SHRemoteConfiguration fetchMusicSubscriptionStatus]
- -[SHRemoteConfiguration musicSubscriptionStatus]
- -[SHRemoteConfiguration setMusicSubscriptionStatus:]
- -[SHRemoteConfiguration setSubscriptionRequest:]
- -[SHRemoteConfiguration subscriptionRequest]
- GCC_except_table17
- GCC_except_table20
- GCC_except_table32
- _ICMusicSubscriptionStatusDidChangeNotification
- _OBJC_CLASS_$_NSNotificationCenter
- _OBJC_IVAR_$_SHRemoteConfiguration._musicSubscriptionStatus
- _OBJC_IVAR_$_SHRemoteConfiguration._subscriptionRequest
- ___53-[SHRemoteConfiguration fetchMusicSubscriptionStatus]_block_invoke
- ___block_descriptor_40_e8_32w_e66_v24?0"ICLightweightMusicSubscriptionStatusResponse"8"NSError"16lw32l8
- ___block_literal_global.49
- ___block_literal_global.51
- ___block_literal_global.53
- ___block_literal_global.55
- ___block_literal_global.57
- ___block_literal_global.59
- ___block_literal_global.61
- ___block_literal_global.63
- ___block_literal_global.65
- ___block_literal_global.67
- _objc_msgSend$addObserver:selector:name:object:
- _objc_msgSend$appleMusicSubscriptionStatus
- _objc_msgSend$cancel
- _objc_msgSend$defaultCenter
- _objc_msgSend$fetchMusicSubscriptionStatus
- _objc_msgSend$setMusicSubscriptionStatus:
- _objc_msgSend$setSubscriptionRequest:
- _objc_msgSend$subscriptionRequest
CStrings:
+ "\f"
+ "fetchMusicSubscriptionStatus:"
- "\x0e"
- "@\"ICLightweightMusicSubscriptionStatusRequest\""
- "@\"SHMusicSubscriptionStatus\""
- "Music subscription status did change"
- "T@\"ICLightweightMusicSubscriptionStatusRequest\",&,N,V_subscriptionRequest"
- "T@\"SHMusicSubscriptionStatus\",&,N,V_musicSubscriptionStatus"
- "_musicSubscriptionStatus"
- "_subscriptionRequest"
- "addObserver:selector:name:object:"
- "cancel"
- "defaultCenter"
- "didChangeMusicSubscriptionStatus:"
- "fetchMusicSubscriptionStatus"
- "hasActiveAppleMusicSubscription"
- "musicSubscriptionStatus"
- "setMusicSubscriptionStatus:"
- "setSubscriptionRequest:"
- "subscriptionRequest"

```
