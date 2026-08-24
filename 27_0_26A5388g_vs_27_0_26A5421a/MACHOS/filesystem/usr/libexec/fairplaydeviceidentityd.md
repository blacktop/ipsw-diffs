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
-  __TEXT.__text: 0x5091f4
+  __TEXT.__text: 0x54ac34
   __TEXT.__auth_stubs: 0x3e0
   __TEXT.__objc_stubs: 0x140
-  __TEXT.__const: 0x72aa0
+  __TEXT.__const: 0x72a40
   __TEXT.__cstring: 0x2ac
   __TEXT.__gcc_except_tab: 0xb0
   __TEXT.__oslogstring: 0x318
   __TEXT.__objc_methname: 0xa9
-  __TEXT.__unwind_info: 0x3e8
-  __TEXT.__eh_frame: 0x240
-  __DATA_CONST.__const: 0x26ad0
+  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__eh_frame: 0x2e8
+  __DATA_CONST.__const: 0x29bc0
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48

   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_selrefs: 0x50
-  __DATA.__data: 0x18c0
-  __DATA.__common: 0xe8
+  __DATA.__data: 0x1ad8
+  __DATA.__common: 0x294
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 256
-  Symbols:   160
+  Functions: 322
+  Symbols:   183
   CStrings:  56
 
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
