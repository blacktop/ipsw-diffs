## libsystem_info.dylib

> `/usr/lib/system/libsystem_info.dylib`

```diff

 597.0.0.0.0
-  __TEXT.__text: 0x24ad4
+  __TEXT.__text: 0x24b10
   __TEXT.__auth_stubs: 0xcb0
   __TEXT.__const: 0x2f0
   __TEXT.__cstring: 0x1fd0

   __AUTH_CONST.__auth_got: 0x658
   __AUTH_CONST.__const: 0x798
   __AUTH.__data: 0x1d0
-  __DATA.__data: 0x20c
+  __DATA.__data: 0x21c
   __DATA.__common: 0x3f8
-  __DATA.__bss: 0x569
-  __DATA_DIRTY.__data: 0x4a0
+  __DATA.__bss: 0x571
+  __DATA_DIRTY.__data: 0x490
   __DATA_DIRTY.__bss: 0xe8
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 68E48B92-552A-38A8-A930-9337588E64F5
-  Functions: 904
-  Symbols:   1856
+  UUID: FE9615F2-1FE2-3465-91CE-802AC94F8382
+  Functions: 905
+  Symbols:   1858
   CStrings:  431
 
Symbols:
+ __mdns_now
Functions:
~ _LI_ils_create : 2784 -> 2780
~ __fsi_tokenize : 520 -> 528
~ _getifaddrs : 1520 -> 1528
+ sub_194982d8c
~ __fsi_get_fs : 1684 -> 1660
~ __mdns_deadline : 152 -> 144
+ __mdns_now
- sub_1936574e0
~ _xdr_pmaplist : 220 -> 216
~ _clnt_broadcast : 1696 -> 1688
~ _svc_getreqset : 704 -> 720

```
