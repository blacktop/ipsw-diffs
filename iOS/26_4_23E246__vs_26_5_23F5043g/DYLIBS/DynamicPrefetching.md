## DynamicPrefetching

> `/System/Library/PrivateFrameworks/DynamicPrefetching.framework/DynamicPrefetching`

```diff

-3.4.0.0.0
-  __TEXT.__text: 0x12ec0
-  __TEXT.__auth_stubs: 0x710
+3.4.0.2.0
+  __TEXT.__text: 0x12f28
+  __TEXT.__auth_stubs: 0x700
   __TEXT.__const: 0x390
   __TEXT.__gcc_except_tab: 0xb48
   __TEXT.__cstring: 0x3e6

   __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0xe8
   __AUTH_CONST.__cfstring: 0x1a0
   __DATA.__data: 0x28
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x170
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 28D1AD9F-A39F-30E3-B132-A04F44722FE3
+  UUID: 97063F91-3F1D-35F7-A233-CE8EAFB3A647
   Functions: 346
   Symbols:   1024
   CStrings:  180
Symbols:
+ __ZN12_GLOBAL__N_114timeout_activeE
+ _dispatch_activate
+ _objc_retain_x24
- _dispatch_resume
- _dispatch_suspend
- _objc_retain_x25
Functions:
~ ___start_scenario_block_invoke : 1728 -> 1740
~ __ZN12_GLOBAL__N_121end_scenario_internalEP8NSStringN11Prefetching2V18ScenarioEb : 664 -> 696
~ ____ZN12_GLOBAL__N_14initEv_block_invoke : 532 -> 560
~ ____ZN12_GLOBAL__N_132activate_scenario_timeout_sourceEP8NSStringN11Prefetching2V18ScenarioE_block_invoke : 196 -> 228

```
