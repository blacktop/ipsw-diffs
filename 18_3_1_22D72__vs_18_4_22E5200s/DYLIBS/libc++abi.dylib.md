## libc++abi.dylib

> `/usr/lib/libc++abi.dylib`

```diff

-1800.105.0.0.0
-  __TEXT.__text: 0x15aa4
+1900.178.0.0.0
+  __TEXT.__text: 0x15838
   __TEXT.__lcxx_override: 0x174
-  __TEXT.__auth_stubs: 0x380
+  __TEXT.__auth_stubs: 0x340
   __TEXT.__init_offsets: 0x4
-  __TEXT.__gcc_except_tab: 0x588
-  __TEXT.__cstring: 0x1127
+  __TEXT.__gcc_except_tab: 0x56c
+  __TEXT.__cstring: 0x10a8
   __TEXT.__const: 0x1650
-  __TEXT.__unwind_info: 0x8d8
+  __TEXT.__unwind_info: 0x8b8
   __TEXT.__eh_frame: 0xd8
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x410
   __AUTH_CONST.__const: 0x3600
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_got: 0x1a8
   __AUTH.__data: 0x8
   __DATA.__data: 0x48
+  __DATA.__thread_vars: 0x18
   __DATA.__crash_info: 0x40
+  __DATA.__thread_bss: 0x10
   __DATA.__common: 0x8
   __DATA.__bss: 0x220
-  __DATA_DIRTY.__data: 0xa8
-  __DATA_DIRTY.__bss: 0x18
+  __DATA_DIRTY.__data: 0x98
+  __DATA_DIRTY.__bss: 0x10
   - /usr/lib/libSystem.B.dylib
-  Functions: 707
-  Symbols:   976
-  CStrings:  275
+  Functions: 703
+  Symbols:   975
+  CStrings:  272
 
Symbols:
+ ___cxa_call_terminate
+ __tlv_bootstrap
- _pthread_getspecific
- _pthread_key_create
- _pthread_once
- _pthread_setspecific
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/libcxx_os/libcxxabi/src/private_typeinfo.cpp"
+ "catching a class without an object?"
- "cannot allocate __cxa_eh_globals"
- "cannot create thread specific key for __cxa_get_globals()"
- "cannot zero out thread value for __cxa_get_globals()"
- "execute once failure in __cxa_get_globals_fast()"
- "std::__libcpp_tls_set failure in __cxa_get_globals()"

```
