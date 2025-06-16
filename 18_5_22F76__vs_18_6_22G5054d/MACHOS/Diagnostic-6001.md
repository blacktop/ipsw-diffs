## Diagnostic-6001

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6001.appex/Diagnostic-6001`

```diff

-820.122.1.0.0
-  __TEXT.__text: 0x3d8
-  __TEXT.__auth_stubs: 0xb0
+820.140.8.0.0
+  __TEXT.__text: 0x7f0
+  __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_stubs: 0x240
-  __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x18
+  __TEXT.__objc_methlist: 0x50
+  __TEXT.__const: 0x28
   __TEXT.__cstring: 0x39
+  __TEXT.__oslogstring: 0xdb
   __TEXT.__objc_classname: 0x18
-  __TEXT.__objc_methname: 0x182
+  __TEXT.__objc_methname: 0x192
   __TEXT.__objc_methtype: 0x39
-  __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0x60
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0xa0
+  __DATA.__objc_selrefs: 0xa8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
+  - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DF5CB8E6-05B3-3976-81D3-2D736F9C649F
-  Functions: 6
-  Symbols:   28
-  CStrings:  38
+  UUID: 3D2FD469-7A64-378C-BF63-64586E14572B
+  Functions: 9
+  Symbols:   40
+  CStrings:  46
 
Symbols:
+ _DiagnosticLogHandleForCategory
+ __os_log_error_impl
+ __os_log_impl
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _objc_release_x23
+ _objc_release_x8
+ _objc_retain_x1
+ _objc_retain_x21
+ _os_log_type_enabled
CStrings:
+ "About to start monitoring for motion with interval %f"
+ "Motion result is %@"
+ "Motion update failed with error %@"
+ "Motion update recieved"
+ "Processing motion event %@"
+ "Stopping motion updates"
+ "Timed out waiting for motion event!"
+ "debugDescription"
+ "teardown"
- "mainQueue"

```
