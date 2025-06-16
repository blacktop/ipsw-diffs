## CoreVideo

> `/System/Library/Frameworks/CoreVideo.framework/CoreVideo`

```diff

-682.6.0.0.0
-  __TEXT.__text: 0x39300
+692.1.0.0.0
+  __TEXT.__text: 0x39290
   __TEXT.__auth_stubs: 0xef0
   __TEXT.__cstring: 0x7d2b
   __TEXT.__objc_databytes: 0x493

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D6E98580-0BF0-3B9F-B095-69D08424380F
+  UUID: B033943C-EFC4-3543-8B11-D918B6BDF17F
   Functions: 1379
   Symbols:   4625
   CStrings:  1226
Symbols:
+ __ZN20CVMetalBufferBacking4initEP15CVBufferBackingPv
- __ZN20CVMetalBufferBacking4initEP13CVImageBufferP15CVBufferBackingPv
Functions:
~ __ZN20CVMetalBufferBacking5allocEPK13__CFAllocator : 144 -> 148
~ __ZN20CVMetalBufferBackingC2EPKv : 60 -> 64
~ __ZN20CVMetalBufferBacking8finalizeEv : 196 -> 148
~ __ZN20CVMetalBufferBacking4initEP13CVImageBufferP15CVBufferBackingPv -> __ZN20CVMetalBufferBacking4initEP15CVBufferBackingPv : 280 -> 232
~ __ZN18CVMetalBufferCache35createBufferBackingFromImageBackingEPK13__CFAllocatorP13CVImageBufferP14CVImageBackingPi : 652 -> 628

```
