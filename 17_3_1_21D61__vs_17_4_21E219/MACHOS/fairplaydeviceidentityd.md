## fairplaydeviceidentityd

> `/usr/libexec/fairplaydeviceidentityd`

```diff

-1.15.0.0.0
-  __TEXT.__text: 0x32dbf4
-  __TEXT.__auth_stubs: 0x410
+1.16.0.0.0
+  __TEXT.__text: 0x392c20
+  __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_stubs: 0xe0
-  __TEXT.__const: 0x2f560
+  __TEXT.__const: 0x31f80
   __TEXT.__gcc_except_tab: 0x30
   __TEXT.__cstring: 0x266
   __TEXT.__oslogstring: 0x11e
   __TEXT.__objc_methname: 0x88
-  __TEXT.__unwind_info: 0x1cc
-  __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__auth_got: 0x218
-  __DATA_CONST.__got: 0xb8
+  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__eh_frame: 0x88
+  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x152a8
+  __DATA_CONST.__const: 0x1e9b8
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_selrefs: 0x38
-  __DATA.__objc_classrefs: 0x18
-  __DATA.__data: 0x3a0
-  __DATA.__bss: 0x8
-  __DATA.__common: 0xaac
+  __DATA.__data: 0xe40
+  __DATA.__common: 0xcc
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EBA757D7-F524-3353-A0A3-F383C5CBF708
-  Functions: 124
-  Symbols:   146
+  UUID: 58038FC3-B523-3AD8-B266-15848CA4ADC6
+  Functions: 122
+  Symbols:   141
   CStrings:  45
 
Symbols:
+ _CFDataGetBytePtr
+ _CFStringCreateExternalRepresentation
+ _CFStringCreateWithCString
+ _MGCopyAnswer
+ _dispatch_once
+ _getpid
+ _proc_pidpath
+ _strnlen
+ _sysctlbyname
- _CFStringCreateWithCStringNoCopy
- _CFStringGetLength
- _CFStringGetMaximumSizeForEncoding
- _CFStringGetSystemEncoding
- _arc4random
- _gettimeofday
- _kCFAllocatorNull
- _memcpy
- _pthread_rwlock_destroy
- _pthread_rwlock_init
- _pthread_rwlock_unlock
- _pthread_rwlock_wrlock
- _vm_allocate
- _vm_deallocate

```
