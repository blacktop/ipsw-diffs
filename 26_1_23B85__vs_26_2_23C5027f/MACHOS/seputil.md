## seputil

> `/usr/libexec/seputil`

```diff

-880.40.6.0.0
-  __TEXT.__text: 0x15b58
+880.60.4.0.0
+  __TEXT.__text: 0x159a8
   __TEXT.__auth_stubs: 0xa30
-  __TEXT.__cstring: 0x5e16
+  __TEXT.__cstring: 0x5e52
   __TEXT.__const: 0xbf4
   __TEXT.__oslogstring: 0x5e
   __TEXT.__gcc_except_tab: 0x274

   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x140
   __DATA_CONST.__cfstring: 0x80
-  __DATA.__data: 0xc20
+  __DATA.__data: 0xc40
   __DATA.__common: 0xc
   __DATA.__bss: 0x8f5
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libz.1.dylib
-  UUID: DA84AE7D-FCFF-3EAB-8362-1A9C2D370DC0
-  Functions: 465
+  UUID: D1760D2D-4101-378E-9591-5AE05F6D1BD0
+  Functions: 466
   Symbols:   195
-  CStrings:  726
+  CStrings:  728
 
Functions:
~ sub_100001c68 : 9884 -> 9400
+ sub_100013cc4
CStrings:
+ "%s: Executed xnu PRNG reseeding dummy API\n"
+ "a:b:c:d:f:g:hkmno:pq:r:s:t:uv:wx:CDFQI:L:NO:PR:ST:W:"
+ "reseed-xnu-prng"
- "a:b:c:d:f:g:hkmno:pq:r:s:t:uv:wx:CDFI:L:NO:PR:ST:W:"

```
