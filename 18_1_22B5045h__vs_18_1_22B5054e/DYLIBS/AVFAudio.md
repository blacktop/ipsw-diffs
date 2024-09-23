## AVFAudio

> `/System/Library/Frameworks/AVFAudio.framework/AVFAudio`

```diff

-684.203.0.0.0
-  __TEXT.__text: 0x113fd0
-  __TEXT.__auth_stubs: 0x1fd0
+684.206.0.0.0
+  __TEXT.__text: 0x113df8
+  __TEXT.__auth_stubs: 0x1fe0
   __TEXT.__objc_methlist: 0x5180
   __TEXT.__const: 0x626
-  __TEXT.__gcc_except_tab: 0x14f38
-  __TEXT.__cstring: 0xe413
-  __TEXT.__oslogstring: 0x17521
+  __TEXT.__gcc_except_tab: 0x14f30
+  __TEXT.__cstring: 0xe464
+  __TEXT.__oslogstring: 0x175ba
   __TEXT.__dlopen_cstrs: 0xa9
-  __TEXT.__unwind_info: 0x5d10
+  __TEXT.__unwind_info: 0x5cd8
   __TEXT.__objc_classname: 0xa12
-  __TEXT.__objc_methname: 0xbb1b
+  __TEXT.__objc_methname: 0xbb3e
   __TEXT.__objc_methtype: 0x2761
-  __TEXT.__objc_stubs: 0x7800
+  __TEXT.__objc_stubs: 0x7820
   __DATA_CONST.__got: 0x570
   __DATA_CONST.__const: 0x1960
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3158
+  __DATA_CONST.__objc_selrefs: 0x3160
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2b0
-  __AUTH_CONST.__auth_got: 0x1000
+  __AUTH_CONST.__auth_got: 0x1008
   __AUTH_CONST.__const: 0x6780
-  __AUTH_CONST.__cfstring: 0x3460
+  __AUTH_CONST.__cfstring: 0x3500
   __AUTH_CONST.__objc_const: 0x8f58
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x414
   __DATA.__data: 0x7e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3854
-  Symbols:   4883
-  CStrings:  5809
+  Functions: 3848
+  Symbols:   4879
+  CStrings:  5816
 
Symbols:
+ _AVAudioSessionCategoryHearingTest
+ _objc_exception_throw
CStrings:
+ "Failed to create tap due to format mismatch, %!@(MISSING)"
+ "%!s(MISSING):%!d(MISSING) Error: input hw format invalid"
+ "Input HW format and tap format not matching"
+ "exceptionWithName:reason:userInfo:"
+ "%!s(MISSING):%!d(MISSING) Failed to create tap, config change pending!"
+ "Input HW format is invalid"
+ "OSStatus"
+ "%!s(MISSING):%!d(MISSING) Format mismatch: input hw %!@(MISSING), client format %!@(MISSING)"
+ "Failed to set output format on node to tap"
- "format.sampleRate == hwFormat.sampleRate"
- "IsFormatSampleRateAndChannelCountValid(hwFormat)"

```
