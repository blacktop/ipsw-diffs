## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

```diff

-263.5.23.0.0
-  __TEXT.__text: 0x544bc
-  __TEXT.__auth_stubs: 0x1010
+263.6.1.0.0
+  __TEXT.__text: 0x54658
+  __TEXT.__auth_stubs: 0x1030
   __TEXT.__objc_methlist: 0x548
-  __TEXT.__gcc_except_tab: 0x6780
+  __TEXT.__gcc_except_tab: 0x67a4
   __TEXT.__const: 0xb19
-  __TEXT.__cstring: 0x3cea
+  __TEXT.__cstring: 0x3d14
   __TEXT.__oslogstring: 0x2f7d
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x2350
+  __TEXT.__unwind_info: 0x2374
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x12e
   __TEXT.__objc_methname: 0x175b
   __TEXT.__objc_methtype: 0x2666
   __TEXT.__objc_stubs: 0xcc0
-  __DATA_CONST.__got: 0x330
+  __DATA_CONST.__got: 0x348
   __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x0

   __AUTH_CONST.__cfstring: 0x900
   __AUTH_CONST.__const: 0x9b8
   __AUTH_CONST.__objc_const: 0x1f8
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x818
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x828
   __DATA.__got_weak: 0x10
   __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x249
+  __DATA.__data: 0x299
   __DATA.__bss: 0x30
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__data: 0x30
-  __DATA_DIRTY.__bss: 0x230
+  __DATA_DIRTY.__bss: 0x1e0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1566
-  Symbols:   4378
-  CStrings:  1139
+  Functions: 1567
+  Symbols:   4385
+  CStrings:  1141
 
Symbols:
+ _MXSessionCreateWithOptions
+ __ZN2as6server21ConstAudioSessionInfo15CreateMXSessionE19MXSessionClientTypeNSt3__18optionalI13audit_token_tEERKNS0_26SessionCreationDescriptionE.cold.1
+ _abort_with_reason
+ _kMXSessionCreationOption_AuditToken
+ _kMXSessionCreationOption_IsolatedAudioUseCaseID
+ _kMXSessionCreationOption_SessionType
CStrings:
+ "C"
+ "assertion failure: optToken.has_value()"

```
