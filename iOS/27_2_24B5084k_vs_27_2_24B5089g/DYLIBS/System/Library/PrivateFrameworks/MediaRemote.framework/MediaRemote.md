## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4026.200.11.0.0
-  __TEXT.__text: 0x30660c
-  __TEXT.__objc_methlist: 0x2c888
+4026.200.15.0.0
+  __TEXT.__text: 0x306624
+  __TEXT.__objc_methlist: 0x2c890
   __TEXT.__const: 0x650
-  __TEXT.__cstring: 0x2de64
-  __TEXT.__oslogstring: 0xeb44
+  __TEXT.__cstring: 0x2de57
+  __TEXT.__oslogstring: 0xebb9
   __TEXT.__gcc_except_tab: 0x6364
   __TEXT.__dlopen_cstrs: 0x777
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xee18
+  __TEXT.__unwind_info: 0xee28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf9a0
+  __DATA_CONST.__objc_selrefs: 0xf9b0
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x1038
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__got: 0x14d8
-  __AUTH_CONST.__const: 0x3440
+  __AUTH_CONST.__const: 0x3460
   __AUTH_CONST.__cfstring: 0x24a40
   __AUTH_CONST.__objc_const: 0x47fa8
   __AUTH_CONST.__objc_intobj: 0x528

   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xbc0
-  __AUTH.__objc_data: 0x8700
+  __AUTH.__objc_data: 0x5f00
   __DATA.__objc_ivar: 0x33f0
   __DATA.__data: 0x1ca8
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2da0
+  __DATA_DIRTY.__objc_data: 0x55a0
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x5c8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 21036
-  Symbols:   35612
-  CStrings:  6775
+  Functions: 21039
+  Symbols:   35616
+  CStrings:  6776
 
Symbols:
+ -[MRMediaRemoteService requestPushToStartTokenWithCompletion:]
+ -[MRNowPlayingPushTokenManager requestStartToken]
+ -[MRUserSettings remoteSessionStalenessGraceInterval]
+ ___49-[MRNowPlayingPushTokenManager requestStartToken]_block_invoke
+ ___53-[MRUserSettings remoteSessionStalenessGraceInterval]_block_invoke
+ ___62-[MRMediaRemoteService requestPushToStartTokenWithCompletion:]_block_invoke
+ _objc_msgSend$layoutRole
+ _objc_msgSend$requestPushToStartTokenWithCompletion:
+ _remoteSessionStalenessGraceInterval.__interval
+ _remoteSessionStalenessGraceInterval.__once
- -[MRMediaRemoteService remoteSessionAssertionsWithCompletion:]
- -[MRUserSettings remoteSessionDefaultAssertionInterval]
- ___55-[MRUserSettings remoteSessionDefaultAssertionInterval]_block_invoke
- ___62-[MRMediaRemoteService remoteSessionAssertionsWithCompletion:]_block_invoke
- _remoteSessionDefaultAssertionInterval.__interval
- _remoteSessionDefaultAssertionInterval.__once
CStrings:
+ "[MRNowPlayingPushTokenManager] requestStartToken"
+ "[MRNowPlayingPushTokenManager] requestStartToken failed: %{public}@"
+ "remoteSessionStalenessGraceInterval"
- "assertions"
- "remoteSessionDefaultAssertionInterval"
```
