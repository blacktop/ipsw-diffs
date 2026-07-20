## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-740.53.1.0.0
-  __TEXT.__text: 0xb790c
-  __TEXT.__auth_stubs: 0x1900
-  __TEXT.__objc_stubs: 0xefa0
-  __TEXT.__objc_methlist: 0x7350
+740.57.1.0.0
+  __TEXT.__text: 0xb7fa0
+  __TEXT.__auth_stubs: 0x1910
+  __TEXT.__objc_stubs: 0xf000
+  __TEXT.__objc_methlist: 0x7378
   __TEXT.__const: 0x3e4
-  __TEXT.__gcc_except_tab: 0xf24
-  __TEXT.__objc_methname: 0x15be0
-  __TEXT.__oslogstring: 0x15e09
-  __TEXT.__cstring: 0x17846
+  __TEXT.__gcc_except_tab: 0xfa4
+  __TEXT.__objc_methname: 0x15c42
+  __TEXT.__oslogstring: 0x15f42
+  __TEXT.__cstring: 0x1787a
   __TEXT.__objc_classname: 0xa44
-  __TEXT.__objc_methtype: 0x439b
-  __TEXT.__unwind_info: 0x2298
-  __DATA_CONST.__const: 0x29e0
-  __DATA_CONST.__cfstring: 0x5c80
+  __TEXT.__objc_methtype: 0x43c3
+  __TEXT.__unwind_info: 0x22c0
+  __DATA_CONST.__const: 0x2a70
+  __DATA_CONST.__cfstring: 0x5ca0
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x130

   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0xc90
-  __DATA_CONST.__got: 0xc80
+  __DATA_CONST.__auth_got: 0xc98
+  __DATA_CONST.__got: 0xc88
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x11248
-  __DATA.__objc_selrefs: 0x4658
-  __DATA.__objc_ivar: 0xd68
+  __DATA.__objc_const: 0x11278
+  __DATA.__objc_selrefs: 0x4670
+  __DATA.__objc_ivar: 0xd6c
   __DATA.__objc_data: 0x18b0
   __DATA.__data: 0xe54
   __DATA.__bss: 0x258

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3613
-  Symbols:   799
-  CStrings:  7299
+  Functions: 3622
+  Symbols:   801
+  CStrings:  7310
 
Symbols:
+ __dispatch_source_type_signal
+ _signal
CStrings:
+ " [ERROR] %{public}s:%d %p endSessionAtSourceTime: raised %@: %@"
+ " [ERROR] %{public}s:%d RPConnectionManager: SIGTERM received, stopping active clients"
+ " [ERROR] %{public}s:%d endSessionAtSourceTime: raised %@: %@"
+ " [ERROR] %{public}s:%d start called after audio recorder queue was freed"
+ " [ERROR] %{public}s:%d stop called but audio recorder queue is freed or not started"
+ "-[RPClient stopStreamForStreamID:stopSource:error:]"
+ "-[SCCaptureSession stopAndInvalidateWithStreamData:userStopped:stopSource:completionHandler:]"
+ "RPDaemonRun_block_invoke"
+ "STSS"
+ "getRecordingAlertTitle:body:forError:"
+ "reason"
+ "stopAndInvalidateWithStreamData:userStopped:stopSource:completionHandler:"
+ "stopSourceForStreamStopReason:"
+ "stopStreamForStreamID:stopSource:error:"
+ "v40@0:8^@16^@24@32"
+ "v44@0:8@16B24q28@?36"
- " [ERROR] %{public}s:%d stop called but not never start"
- "-[RPClient stopStreamForStreamID:error:]"
- "-[SCCaptureSession stopAndInvalidateWithStreamData:userStopped:completionHandler:]"
- "stopAndInvalidateWithStreamData:userStopped:completionHandler:"
- "stopStreamForStreamID:error:"
```
