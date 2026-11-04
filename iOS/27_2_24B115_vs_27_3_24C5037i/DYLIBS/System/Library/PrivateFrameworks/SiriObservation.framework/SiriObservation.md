## SiriObservation

> `/System/Library/PrivateFrameworks/SiriObservation.framework/SiriObservation`

```diff

-3605.31.1.11.2
-  __TEXT.__text: 0x144a8
-  __TEXT.__objc_methlist: 0x1330
+3610.11.2.0.0
+  __TEXT.__text: 0x14a48
+  __TEXT.__objc_methlist: 0x1340
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__cstring: 0x2106
-  __TEXT.__oslogstring: 0x6c1
-  __TEXT.__unwind_info: 0x908
+  __TEXT.__gcc_except_tab: 0x194
+  __TEXT.__cstring: 0x21a3
+  __TEXT.__oslogstring: 0x718
+  __TEXT.__unwind_info: 0x930
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9a0
+  __DATA_CONST.__const: 0x9f0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x988
+  __DATA_CONST.__objc_selrefs: 0x998
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__got: 0x188
   __AUTH_CONST.__const: 0x620
   __AUTH_CONST.__cfstring: 0xa20
-  __AUTH_CONST.__objc_const: 0x2050
+  __AUTH_CONST.__objc_const: 0x20b0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__data: 0x40
-  __DATA.__objc_ivar: 0x1bc
+  __AUTH.__data: 0x48
+  __DATA.__objc_ivar: 0x1c8
   __DATA.__data: 0x420
   __DATA_DIRTY.__objc_data: 0x500
-  __DATA_DIRTY.__data: 0xf8
-  __DATA_DIRTY.__bss: 0x240
+  __DATA_DIRTY.__data: 0xf0
+  __DATA_DIRTY.__bss: 0x1b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 598
-  Symbols:   1121
-  CStrings:  284
+  Functions: 603
+  Symbols:   1132
+  CStrings:  289
 
Symbols:
+ -[SOMediaNowPlayingObserver _fetchIsProxyGroupPlayerWithCompletion:]
+ -[SOMediaNowPlayingObserver _setProxyGroupPlayer:]
+ -[SOMediaNowPlayingObserver _updateProxyGroupPlayerStateWithCompletion:]
+ GCC_except_table209
+ GCC_except_table213
+ GCC_except_table300
+ GCC_except_table308
+ _MRMediaRemoteGetDeviceInfo
+ _OBJC_IVAR_$_SOClockTimerManager._isTimerAlarmCoordinationEnabled
+ _OBJC_IVAR_$_SOMediaNowPlayingObserver._proxyGroupPlayerStateGeneration
+ _OBJC_IVAR_$_SOMediaNowPlayingObserver._proxyGroupPlayerStateGroup
+ ___66-[SOMediaNowPlayingObserver mediaRemoteActiveDeviceInfoDidChange:]_block_invoke_2
+ ___68-[SOMediaNowPlayingObserver _fetchIsProxyGroupPlayerWithCompletion:]_block_invoke
+ ___68-[SOMediaNowPlayingObserver getProxyGroupPlayerStateWithCompletion:]_block_invoke_2
+ ___72-[SOMediaNowPlayingObserver _updateProxyGroupPlayerStateWithCompletion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e24_v24?0^v8^{__CFError=}16ls32l8
+ ___block_descriptor_56_e8_32bs40w_e8_v12?0B8lw40l8s32l8
- -[SOMediaNowPlayingObserver _isProxyGroupPlayer]
- -[SOMediaNowPlayingObserver _updateProxyGroupPlayerState]
- GCC_except_table295
- GCC_except_table303
- _CFRelease
- _MRMediaRemoteCopyDeviceInfo
CStrings:
+ "%s %p Ignored a stale isProxyGroupPlayer = %d"
+ "%s Unable to fetch local device info: %@"
+ "-[SOMediaNowPlayingObserver _fetchIsProxyGroupPlayerWithCompletion:]_block_invoke"
+ "-[SOMediaNowPlayingObserver _updateProxyGroupPlayerStateWithCompletion:]_block_invoke"
+ "v12@?0B8"
+ "v24@?0^v8^{__CFError=}16"
- "-[SOMediaNowPlayingObserver _isProxyGroupPlayer]"
```
