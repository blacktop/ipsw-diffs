## AVFAudio

> `/System/Library/Frameworks/AVFAudio.framework/AVFAudio`

```diff

-743.206.0.0.0
+743.302.0.0.0
   __TEXT.__text: 0x119b8c
   __TEXT.__auth_stubs: 0x21c0
   __TEXT.__objc_methlist: 0x58f4

   __TEXT.__unwind_info: 0x6048
   __TEXT.__objc_classname: 0xa45
   __TEXT.__objc_methname: 0xbf2d
-  __TEXT.__objc_methtype: 0x2882
+  __TEXT.__objc_methtype: 0x288e
   __TEXT.__objc_stubs: 0x7aa0
   __DATA_CONST.__got: 0x5f8
   __DATA_CONST.__const: 0x1988

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 72E9F8CF-DC49-3902-BA9D-34AF7D540F0C
+  UUID: 89E93B0F-94EA-3FA7-9DD6-00B551B7901B
   Functions: 3881
-  Symbols:   12988
+  Symbols:   12989
   CStrings:  6384
 
Symbols:
+ _AVAudioSessionModeDualRoute
CStrings:
+ "{unique_ptr<AVAudioFileImpl, std::default_delete<AVAudioFileImpl>>=\"\"{?=\"__ptr_\"^{AVAudioFileImpl}}}"
+ "{unique_ptr<PulseTone, std::default_delete<PulseTone>>=\"\"{?=\"__ptr_\"^{PulseTone}}}"
- "{unique_ptr<AVAudioFileImpl, std::default_delete<AVAudioFileImpl>>=\"__ptr_\"^{AVAudioFileImpl}}"
- "{unique_ptr<PulseTone, std::default_delete<PulseTone>>=\"__ptr_\"^{PulseTone}}"

```
