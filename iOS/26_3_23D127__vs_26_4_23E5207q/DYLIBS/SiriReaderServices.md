## SiriReaderServices

> `/System/Library/PrivateFrameworks/SiriReaderServices.framework/SiriReaderServices`

```diff

-3515.12.1.0.0
-  __TEXT.__text: 0x80c
-  __TEXT.__auth_stubs: 0x1c0
+3520.88.6.1.4
+  __TEXT.__text: 0x814
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_methlist: 0x1f0
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0xac

   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xf0
+  __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x278

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A2874928-6EEF-3507-8CCA-84DE2E4717AF
+  UUID: CBBB0A56-C6D1-3032-8C68-45DDDE8E9368
   Functions: 15
-  Symbols:   123
+  Symbols:   119
   CStrings:  96
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_release_x25
- _objc_release_x26
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x6
Functions:
~ +[SiriReaderUtilities readerStartingToneAudioAssetURL] : 144 -> 156
~ -[SiriReaderConnection init] : 192 -> 196
~ -[SiriReaderConnection readText:textBody:textIdentifier:textLocale:textLeadingImage:] : 224 -> 212
~ -[SiriReaderConnection readText:textBody:textIdentifier:textLocale:textLeadingImage:activationSource:] : 228 -> 216
~ -[SiriReaderConnection getPlaybackStatusForIdentifier:] : 252 -> 256
~ -[SiriReaderConnection pausePlaybackForIdentifier:] : 124 -> 128
~ -[SiriReaderConnection resumePlaybackForIdentifier:] : 124 -> 128
~ -[SiriReaderConnection endMediaSessionForIdentifier:] : 124 -> 128

```
