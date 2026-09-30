## libwebrtc.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libwebrtc.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

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
-  Symbols:   23542
-  CStrings:  9600
+  Functions: 18263
+  Symbols:   23543
+  CStrings:  9602
 
Symbols:
+ __ZZN6webrtc5Event4WaitENS_9TimeDeltaES1_ENK3$_0clENSt3__18optionalI8timespecEE
Functions:
~ __ZN6webrtc5Event4WaitENS_9TimeDeltaES1_ : 644 -> 460
+ __ZZN6webrtc5Event4WaitENS_9TimeDeltaES1_ENK3$_0clENSt3__18optionalI8timespecEE
CStrings:
+ "Event::Wait pthread_cond_timedwait failed with error "
+ "Event::Wait pthread_cond_wait failed with error "
```
