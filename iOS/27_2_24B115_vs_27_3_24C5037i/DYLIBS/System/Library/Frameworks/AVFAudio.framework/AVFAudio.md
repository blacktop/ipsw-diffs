## AVFAudio

> `/System/Library/Frameworks/AVFAudio.framework/AVFAudio`

```diff

-794.210.0.0.0
-  __TEXT.__text: 0x111970
+794.303.0.0.0
+  __TEXT.__text: 0x1119ac
   __TEXT.__realtime: 0x1d04
   __TEXT.__objc_methlist: 0x5b2c
   __TEXT.__dlopen_cstrs: 0xa9

   __DATA_CONST.__got: 0x6b8
   __AUTH_CONST.__const: 0x7018
   __AUTH_CONST.__cfstring: 0x3920
-  __AUTH_CONST.__objc_const: 0x8b98
+  __AUTH_CONST.__objc_const: 0x8bb8
   __AUTH_CONST.__weak_auth_got: 0x38
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0x1248
-  __DATA.__objc_ivar: 0x444
+  __DATA.__objc_ivar: 0x448
   __DATA.__data: 0x930
   __DATA_DIRTY.__objc_data: 0x2030
   __DATA_DIRTY.__bss: 0x38

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 4137
-  Symbols:   8067
+  Symbols:   8068
   CStrings:  3377
 
Symbols:
+ _OBJC_IVAR_$_AudioPlayerImpl._weakSelf
+ __ZL25LocalPlayerHandleCallbackP15AudioPlayerImpljmPKv
- __ZL25LocalPlayerHandleCallbackP13AVAudioPlayerjmPKv
Functions:
~ -[AudioPlayerImpl dealloc] : 352 -> 364
~ -[AVAudioPlayer(AVAudioPlayerPriv) initBase] : 652 -> 664
~ -[AVAudioPlayer(AVAudioPlayerPriv) handleInterruption:] : 512 -> 508
~ __ZL25LocalPlayerHandleCallbackP13AVAudioPlayerjmPKv -> __ZL25LocalPlayerHandleCallbackP15AudioPlayerImpljmPKv : 576 -> 600
~ sub_1bff8d024 -> sub_1c0d63050 : 56 -> 64
~ sub_1bff8d05c -> sub_1c0d63090 : 92 -> 100
```
