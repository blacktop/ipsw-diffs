## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

```diff

-  __TEXT.__text: 0xa7a174
+  __TEXT.__text: 0xa7a20c
   __TEXT.__auth_stubs: 0x14d0
   __TEXT.__objc_methlist: 0x14e4
   __TEXT.__const: 0xa68f8
-  __TEXT.__cstring: 0x550f8
+  __TEXT.__cstring: 0x5515f
   __TEXT.__gcc_except_tab: 0x18a0
   __TEXT.__unwind_info: 0x2840
   __TEXT.__eh_frame: 0xf08

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 18262
-  Symbols:   44540
-  CStrings:  9650
+  Functions: 18263
+  Symbols:   44544
+  CStrings:  9652
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ __ZZN6webrtc5Event4WaitENS_9TimeDeltaES1_ENK3$_0clENSt3__18optionalI8timespecEE
Functions:
~ __ZN6webrtc5Event4WaitENS_9TimeDeltaES1_ : 644 -> 460
+ __ZZN6webrtc5Event4WaitENS_9TimeDeltaES1_ENK3$_0clENSt3__18optionalI8timespecEE
CStrings:
+ "Event::Wait pthread_cond_timedwait failed with error "
+ "Event::Wait pthread_cond_wait failed with error "

```
