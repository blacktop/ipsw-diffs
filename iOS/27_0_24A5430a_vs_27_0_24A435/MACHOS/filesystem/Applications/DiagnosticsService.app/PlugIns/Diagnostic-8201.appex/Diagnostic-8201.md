## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 60.0.0.0.0
-  __TEXT.__text: 0x24494
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_stubs: 0xae0
+  __TEXT.__text: 0x25a54
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__objc_stubs: 0xb60
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x324
-  __TEXT.__gcc_except_tab: 0x2bcc
-  __TEXT.__const: 0x248
-  __TEXT.__cstring: 0x65a3
+  __TEXT.__gcc_except_tab: 0x2c0c
+  __TEXT.__const: 0x258
+  __TEXT.__cstring: 0x676b
   __TEXT.__objc_classname: 0x50
-  __TEXT.__objc_methname: 0xc12
+  __TEXT.__objc_methname: 0xc46
   __TEXT.__objc_methtype: 0x6c9
   __TEXT.__ustring: 0x14a
-  __TEXT.__oslogstring: 0x9c4
-  __TEXT.__unwind_info: 0x7c0
-  __DATA_CONST.__const: 0x578
-  __DATA_CONST.__cfstring: 0x4aa0
+  __TEXT.__oslogstring: 0xa8e
+  __TEXT.__unwind_info: 0x7e0
+  __DATA_CONST.__const: 0x5a8
+  __DATA_CONST.__cfstring: 0x4ac0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x428
-  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__got: 0x360
   __DATA.__objc_const: 0x678
-  __DATA.__objc_selrefs: 0x3c8
+  __DATA.__objc_selrefs: 0x3e8
   __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 490
-  Symbols:   423
-  CStrings:  1070
+  Functions: 495
+  Symbols:   438
+  CStrings:  1089
 
Symbols:
+ _IOServiceNameMatching
+ _OBJC_CLASS_$_NSMutableData
+ __Block_object_assign
+ __Block_object_dispose
+ ___objc_personality_v0
+ _dispatch_get_global_queue
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _notify_cancel
+ _notify_get_state
+ _notify_post
+ _notify_register_check
+ _notify_register_dispatch
CStrings:
+ "ApplePearlExclaveSEPDriver"
+ "Generating reference frames info record...\n"
+ "Reference frames info record written to %s\n"
+ "ReferenceFramesSetInfo, index: %zu, type: %d, count: %d, size: %d\n"
+ "Verifying new reference frames info record...\n"
+ "appendData:"
+ "com.apple.pearld.check_secure_streaming"
+ "com.apple.pearld.ready"
+ "dataWithLength:"
+ "mutableBytes"
+ "notifyResult == 0"
+ "outDataSize <= signedRefFramesInfoRecordData.length"
+ "pearldReady"
+ "reference-info-record.DAT"
+ "requestData"
+ "sema"
+ "setLength:"
+ "signedRefFramesInfoRecordData"
+ "v12@?0i8"
```
