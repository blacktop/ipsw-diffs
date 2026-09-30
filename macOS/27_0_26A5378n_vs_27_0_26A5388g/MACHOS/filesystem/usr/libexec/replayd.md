## replayd

> `/usr/libexec/replayd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
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
-  __TEXT.__text: 0xc5e44
-  __TEXT.__auth_stubs: 0x1b00
-  __TEXT.__objc_stubs: 0xec40
-  __TEXT.__objc_methlist: 0x754c
+740.57.1.0.0
+  __TEXT.__text: 0xc6700
+  __TEXT.__auth_stubs: 0x1b10
+  __TEXT.__objc_stubs: 0xeca0
+  __TEXT.__objc_methlist: 0x7574
   __TEXT.__const: 0x430
-  __TEXT.__oslogstring: 0x15250
-  __TEXT.__cstring: 0x17255
+  __TEXT.__oslogstring: 0x15411
+  __TEXT.__cstring: 0x17289
   __TEXT.__objc_classname: 0xacb
-  __TEXT.__objc_methname: 0x16079
-  __TEXT.__objc_methtype: 0x4064
-  __TEXT.__gcc_except_tab: 0xf4c
+  __TEXT.__objc_methname: 0x160db
+  __TEXT.__objc_methtype: 0x409d
+  __TEXT.__gcc_except_tab: 0xfcc
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x22d0
-  __DATA_CONST.__const: 0x2860
-  __DATA_CONST.__cfstring: 0x6340
+  __TEXT.__unwind_info: 0x22f8
+  __DATA_CONST.__const: 0x28d0
+  __DATA_CONST.__cfstring: 0x6360
   __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0xd90
-  __DATA_CONST.__got: 0xd00
+  __DATA_CONST.__auth_got: 0xd98
+  __DATA_CONST.__got: 0xd08
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x110b8
-  __DATA.__objc_selrefs: 0x4638
-  __DATA.__objc_ivar: 0xdd4
+  __DATA.__objc_const: 0x110e8
+  __DATA.__objc_selrefs: 0x4650
+  __DATA.__objc_ivar: 0xdd8
   __DATA.__objc_data: 0x1cc0
   __DATA.__data: 0xc98
-  __DATA.__bss: 0x288
+  __DATA.__bss: 0x290
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3736
-  Symbols:   846
-  CStrings:  7380
+  Functions: 3745
+  Symbols:   848
+  CStrings:  7396
 
Symbols:
+ __dispatch_source_type_signal
+ _signal
CStrings:
+ " [ERROR] %{public}s:%d %p endSessionAtSourceTime: raised %@: %@"
+ " [ERROR] %{public}s:%d RPConnectionManager: SIGTERM received, stopping active clients"
+ " [ERROR] %{public}s:%d endSessionAtSourceTime: raised %@: %@"
+ " [ERROR] %{public}s:%d start called after audio recorder queue was freed"
+ " [ERROR] %{public}s:%d stop called but audio recorder queue is freed or not started"
+ " [INFO] %{public}s:%d session=%p  contentStream=%@"
+ " [INFO] %{public}s:%d session=%p  filter=%@"
+ " [INFO] %{public}s:%d session=%p  properties=%@"
+ " [INFO] %{public}s:%d session=%p  queue=%@"
+ " [INFO] %{public}s:%d session=%p Created"
+ "-[RPClient stopStreamForStreamID:stopSource:error:]"
+ "-[SCCaptureSession stopAndInvalidateWithStreamData:userStopped:stopSource:completionHandler:]"
+ "RPDaemonRun_block_invoke"
+ "STSS"
+ "getRecordingAlertTitle:body:forError:"
+ "reason"
+ "stopAndInvalidateWithStreamData:userStopped:stopSource:completionHandler:"
+ "stopSourceForStreamStopReason:"
+ "stopStreamForStreamID:stopSource:error:"
+ "v40@0:8@16q24@32"
+ "v40@0:8^@16^@24@32"
+ "v44@0:8@16B24q28@?36"
- " [ERROR] %{public}s:%d stop called but not never start"
- " [INFO] %{public}s:%d session=%p Created contentStream=%@ filter=%@ properties=%@ queue=%@"
- "-[RPClient stopStreamForStreamID:error:]"
- "-[SCCaptureSession stopAndInvalidateWithStreamData:userStopped:completionHandler:]"
- "stopAndInvalidateWithStreamData:userStopped:completionHandler:"
- "stopStreamForStreamID:error:"
```
