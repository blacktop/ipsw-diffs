## fairplaydeviceidentityd

> `/usr/libexec/fairplaydeviceidentityd`

```diff

-1.31.0.0.0
-  __TEXT.__text: 0x3f0b90
-  __TEXT.__auth_stubs: 0x3f0
+1.32.0.0.0
+  __TEXT.__text: 0x51f060
+  __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_stubs: 0x140
-  __TEXT.__const: 0x33998
+  __TEXT.__const: 0x55e30
   __TEXT.__gcc_except_tab: 0xb0
   __TEXT.__cstring: 0x28f
   __TEXT.__oslogstring: 0x188
   __TEXT.__objc_methname: 0xa9
-  __TEXT.__unwind_info: 0x1e0
-  __TEXT.__eh_frame: 0x88
-  __DATA_CONST.__auth_got: 0x208
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x26ef0
+  __TEXT.__unwind_info: 0x3c8
+  __TEXT.__eh_frame: 0xd8
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x34680
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_selrefs: 0x50
-  __DATA.__data: 0xe38
-  __DATA.__common: 0x100
+  __DATA.__data: 0x1a08
+  __DATA.__common: 0xb60
+  __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 03420F81-B96B-32F0-B6AD-9042A0472F14
-  Functions: 132
-  Symbols:   155
+  UUID: 71CF39B3-DCCA-304C-A275-843083B5F039
+  Functions: 266
+  Symbols:   175
   CStrings:  52
 
Symbols:
+ _CFStringGetBytes
+ _CFStringGetLength
+ _NDR_record
+ _arc4random
+ _bootstrap_look_up
+ _bootstrap_port
+ _gettimeofday
+ _mach_msg
+ _mach_msg_destroy
+ _mach_port_deallocate
+ _mig_dealloc_reply_port
+ _mig_get_reply_port
+ _mig_put_reply_port
+ _objc_release_x24
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x24
+ _pthread_rwlock_destroy
+ _pthread_rwlock_init
+ _pthread_rwlock_rdlock
+ _pthread_rwlock_unlock
+ _pthread_rwlock_wrlock
+ _vm_allocate
+ _vm_deallocate
+ _voucher_mach_msg_set
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x22

```
