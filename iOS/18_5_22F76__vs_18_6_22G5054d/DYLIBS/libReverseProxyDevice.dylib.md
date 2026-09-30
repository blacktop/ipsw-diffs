## libReverseProxyDevice.dylib

> `/usr/lib/libReverseProxyDevice.dylib`

```diff

-102.0.0.0.0
-  __TEXT.__text: 0x48a4
-  __TEXT.__auth_stubs: 0x6f0
+104.0.0.0.0
+  __TEXT.__text: 0x48ec
+  __TEXT.__auth_stubs: 0x700
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__gcc_except_tab: 0xd4
   __TEXT.__cstring: 0xd84
-  __TEXT.__unwind_info: 0x188
+  __TEXT.__unwind_info: 0x198
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x380
+  __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0x188
   __AUTH_CONST.__cfstring: 0x9e0
   __DATA.__data: 0x4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 52790319-9FC6-318F-B325-B197C4567D4F
+  UUID: 6858EC7D-2BE6-3B0B-AC1A-BC1DA0F65760
   Functions: 77
-  Symbols:   310
+  Symbols:   312
   CStrings:  223
 
Symbols:
+ GCC_except_table25
+ GCC_except_table28
+ __ZN8RPSocket13EventCallback20invoke_and_delete_fnEPS0_
+ _dispatch_async_f
- GCC_except_table29
- __ZN8RPSocket13EventCallback4sendEv
Functions:
~ __ZN8RPSocket11set_invalidEv : 176 -> 224
~ __ZNK8RPSocket13EventCallback11release_allEv -> __ZN8RPSocket13EventCallback20invoke_and_delete_fnEPS0_ : 104 -> 100
~ __ZN8RPSocket13EventCallback4sendEv -> __ZN8RPSocket13EventCallback6invokeEv : 124 -> 376
~ __ZN8RPSocket13EventCallback6invokeEv -> __ZNK8RPSocket13EventCallback11release_allEv : 376 -> 104
~ __ZN8RPSocket13EventCallback9invoke_fnEPS0_ -> __ZN11RPSocket_fd13event_handlerEPv : 4 -> 188
~ __ZN11RPSocket_fd13event_handlerEPv -> __ZN8RPSocket13EventCallback9invoke_fnEPS0_ : 140 -> 4

```
