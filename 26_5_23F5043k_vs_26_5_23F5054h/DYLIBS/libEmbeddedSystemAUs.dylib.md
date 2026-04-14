## libEmbeddedSystemAUs.dylib

> `/System/Library/Frameworks/AudioToolbox.framework/libEmbeddedSystemAUs.dylib`

```diff

-1556.603.0.0.0
-  __TEXT.__text: 0xefa90
+1556.604.0.0.0
+  __TEXT.__text: 0xefb84
   __TEXT.__auth_stubs: 0x27c0
   __TEXT.__const: 0xa950
   __TEXT.__dlopen_cstrs: 0x2c1

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9B2E97A-4B2D-3952-ACA8-291C711AEDC3
+  UUID: 7510715A-10AE-3C70-A9AC-3FCBDACC49B1
   Functions: 3666
   Symbols:   9641
   CStrings:  2163
Symbols:
+ __ZNK5ausdk7AUScope12RestoreStateENSt3__14spanIKhLm18446744073709551615EEE
- __ZNK5ausdk7AUScope12RestoreStateEPKh
Functions:
~ __ZNK5ausdk12AUBufferList27CopyBufferContentsToOrErrorER15AudioBufferList : 208 -> 224
~ __ZN5ausdk12AUEffectBase18ProcessBufferListsERjRK15AudioBufferListRS2_j : 500 -> 560
~ __ZNK5ausdk7AUScope12RestoreStateEPKh -> __ZNK5ausdk7AUScope12RestoreStateENSt3__14spanIKhLm18446744073709551615EEE : 148 -> 292
~ __ZN5ausdk6AUBase12RestoreStateEPKv : 988 -> 1012

```
