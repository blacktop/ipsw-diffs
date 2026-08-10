## tailspind

> `/usr/libexec/tailspind`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-267.0.0.0.0
-  __TEXT.__text: 0xe888
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_stubs: 0xba0
+268.0.0.0.0
+  __TEXT.__text: 0xef98
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_stubs: 0xc20
   __TEXT.__objc_methlist: 0x254
-  __TEXT.__const: 0x134
-  __TEXT.__cstring: 0x135f
-  __TEXT.__objc_methname: 0xee2
-  __TEXT.__oslogstring: 0x2ab7
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x139c
+  __TEXT.__gcc_except_tab: 0x318
+  __TEXT.__oslogstring: 0x2bdd
+  __TEXT.__dlopen_cstrs: 0x5c
+  __TEXT.__objc_methname: 0xf20
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x119
-  __TEXT.__gcc_except_tab: 0x288
-  __TEXT.__unwind_info: 0x440
-  __DATA_CONST.__const: 0x448
-  __DATA_CONST.__cfstring: 0x840
+  __TEXT.__unwind_info: 0x460
+  __DATA_CONST.__const: 0x4c0
+  __DATA_CONST.__cfstring: 0x880
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x640
-  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__auth_got: 0x668
+  __DATA_CONST.__got: 0x188
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x3c0
-  __DATA.__objc_selrefs: 0x388
+  __DATA.__objc_selrefs: 0x3a8
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x2164
+  __DATA.__data: 0x2168
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x5c8
+  __DATA.__bss: 0x5d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 286
-  Symbols:   255
-  CStrings:  513
+  Functions: 294
+  Symbols:   262
+  CStrings:  528
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _TSPCPUTraceOptions_PidFilters
+ _objc_getClass
+ _objc_retain_x9
+ _tailspin_config_apply_sync
+ _tailspin_config_create_with_current_state
+ _tailspin_cputrace_enabled_set_with_options
CStrings:
+ "B12@?0i8"
+ "CPUTrace pid selection enablement: %d"
+ "CPUTrace pid selection: Failed to apply tailspin config"
+ "CPUTrace pid selection: Failed to get tailspin config"
+ "CPUTrace pid selection: Got pid %d"
+ "CPUTrace pid selection: libhwtrace not present"
+ "CPUTracePIDSelectorObjC"
+ "CPUTracePIDSelectorObjC not present"
+ "CPUTracePidSelectionEnabled"
+ "CoreDiagnostics not present"
+ "boolValue"
+ "initWithSuiteName:"
+ "objectForKey:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics"
+ "startWithCallback:"
```
