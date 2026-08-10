## fairplaydeviceidentityd

> `/usr/libexec/fairplaydeviceidentityd`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

 1.33.0.0.0
-  __TEXT.__text: 0x5522a8
+  __TEXT.__text: 0x5a7edc
   __TEXT.__auth_stubs: 0x450
   __TEXT.__objc_stubs: 0x140
-  __TEXT.__const: 0x4de10
+  __TEXT.__const: 0x4e280
   __TEXT.__gcc_except_tab: 0xb0
   __TEXT.__cstring: 0x28f
   __TEXT.__oslogstring: 0x188
   __TEXT.__objc_methname: 0xa9
-  __TEXT.__unwind_info: 0x4d8
-  __TEXT.__eh_frame: 0xd0
-  __DATA_CONST.__const: 0x322a0
+  __TEXT.__unwind_info: 0x530
+  __TEXT.__eh_frame: 0x100
+  __DATA_CONST.__const: 0x35dc0
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48

   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_selrefs: 0x50
-  __DATA.__data: 0x1e70
-  __DATA.__common: 0xb40
+  __DATA.__data: 0x1fc0
+  __DATA.__common: 0xce8
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 318
-  Symbols:   176
+  Functions: 340
+  Symbols:   199
   CStrings:  45
 
Symbols:
+ _clock_gettime
+ _clock_gettime_nsec_np
+ _fclose
+ _fopen
+ _fprintf
+ _fwrite
+ _nanosleep
+ _pthread_cond_broadcast
+ _pthread_cond_destroy
+ _pthread_cond_init
+ _pthread_cond_signal
+ _pthread_cond_timedwait
+ _pthread_cond_wait
+ _pthread_create
+ _pthread_detach
+ _pthread_join
+ _pthread_mutex_destroy
+ _pthread_mutex_init
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
+ _qsort
+ _snprintf
+ _strlen
```
