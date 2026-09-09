## Diagnostic-9006

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9006.appex/Diagnostic-9006`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1307.2.4.0.0
-  __TEXT.__text: 0x3eec
-  __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_stubs: 0x11c0
+  __TEXT.__text: 0x4514
+  __TEXT.__auth_stubs: 0x330
+  __TEXT.__objc_stubs: 0x1300
   __TEXT.__objc_methlist: 0x8d0
-  __TEXT.__const: 0x78
+  __TEXT.__const: 0x80
   __TEXT.__objc_classname: 0xc8
-  __TEXT.__objc_methname: 0x1fbb
+  __TEXT.__objc_methname: 0x2007
   __TEXT.__objc_methtype: 0xb01
   __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__cstring: 0x3eb
-  __TEXT.__oslogstring: 0x10f
+  __TEXT.__cstring: 0x46a
+  __TEXT.__oslogstring: 0x14f
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__const: 0xb0
-  __DATA_CONST.__cfstring: 0x500
+  __TEXT.__unwind_info: 0xe8
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__cfstring: 0x5a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x170
-  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0xf8
   __DATA.__objc_const: 0xba0
-  __DATA.__objc_selrefs: 0x828
+  __DATA.__objc_selrefs: 0x840
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x240

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 88
-  Symbols:   89
-  CStrings:  486
+  Functions: 91
+  Symbols:   102
+  CStrings:  498
 
Symbols:
+ _CRErrorDomain
+ _MGGetBoolAnswer
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_CRPreflightController
+ _OBJC_CLASS_$_CRRepairStatus
+ _OBJC_CLASS_$_NSError
+ __dispatch_main_q
+ _dispatch_async
+ _dispatch_get_global_queue
+ _dispatch_semaphore_signal
+ _dispatch_time
+ _objc_retain_x19
+ _objc_retain_x21
CStrings:
+ "1"
+ "InDiagnosticsMode"
+ "InternalBuild"
+ "Preflight error: %@"
+ "Preflight results: %@"
+ "Preflight success: %d"
+ "Preflight time out"
+ "Service part mTub/MLB not supported"
+ "errorWithDomain:code:userInfo:"
+ "isServicePartWithError:"
+ "preflight:withReply:"
+ "v28@?0B8@\"NSDictionary\"12@\"NSError\"20"
```
