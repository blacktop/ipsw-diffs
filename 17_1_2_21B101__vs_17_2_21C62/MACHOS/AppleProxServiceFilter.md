## AppleProxServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/AppleProxServiceFilter.plugin/AppleProxServiceFilter`

```diff

-31.1.0.0.0
-  __TEXT.__text: 0x3db0
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_stubs: 0x620
-  __TEXT.__objc_methlist: 0x4b0
-  __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0x404
-  __TEXT.__cstring: 0x552
-  __TEXT.__objc_methname: 0xd6b
-  __TEXT.__oslogstring: 0x4d7
+31.3.0.0.0
+  __TEXT.__text: 0x3e44
+  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__objc_stubs: 0x660
+  __TEXT.__objc_methlist: 0x4d8
+  __TEXT.__gcc_except_tab: 0x3e4
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x555
+  __TEXT.__objc_methname: 0xd77
+  __TEXT.__oslogstring: 0x4eb
   __TEXT.__objc_classname: 0x91
-  __TEXT.__objc_methtype: 0x45e
-  __TEXT.__unwind_info: 0x1c4
-  __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x1c8
-  __DATA_CONST.__got: 0x28
+  __TEXT.__objc_methtype: 0x47e
+  __TEXT.__unwind_info: 0x1b0
+  __DATA_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0xa40
+  __DATA_CONST.__cfstring: 0xa60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xb78
-  __DATA.__objc_selrefs: 0x370
-  __DATA.__objc_classrefs: 0x38
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0xba8
+  __DATA.__objc_selrefs: 0x378
+  __DATA.__objc_classrefs: 0x30
   __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 115
-  Symbols:   79
-  CStrings:  384
+  Functions: 116
+  Symbols:   84
+  CStrings:  388
 
Symbols:
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_walltime
- _OBJC_CLASS_$_NSTimer
- __ZSt9terminatev
- ___cxa_begin_catch
CStrings:
+ "!\x12"
+ "@\"NSObject<OS_dispatch_source>\""
+ "@20@0:8f16"
+ "AggregationTimeout"
+ "Send Call Day event"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_aggTimer"
+ "_floatToNsNumber:"
+ "floatValue"
+ "i"
+ "numberWithDouble:"
- "!\x11"
- "@\"NSTimer\""
- "T@\"NSTimer\",&,N,V_aggTimer"
- "invalidate"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "v16@?0@\"NSTimer\"8"

```
