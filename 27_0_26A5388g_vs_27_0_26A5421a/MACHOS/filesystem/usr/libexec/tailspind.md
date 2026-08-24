## tailspind

> `/usr/libexec/tailspind`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-267.0.0.0.0
-  __TEXT.__text: 0xcf38
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_stubs: 0x8e0
+268.0.0.0.0
+  __TEXT.__text: 0xd674
+  __TEXT.__auth_stubs: 0xa60
+  __TEXT.__objc_stubs: 0x960
   __TEXT.__objc_methlist: 0x254
-  __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x11f1
-  __TEXT.__objc_methname: 0xcf1
-  __TEXT.__oslogstring: 0x236c
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x1289
+  __TEXT.__gcc_except_tab: 0x314
+  __TEXT.__oslogstring: 0x2492
+  __TEXT.__dlopen_cstrs: 0x5c
+  __TEXT.__objc_methname: 0xd2f
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x119
-  __TEXT.__gcc_except_tab: 0x288
-  __TEXT.__unwind_info: 0x3e8
-  __DATA_CONST.__const: 0x3b8
-  __DATA_CONST.__cfstring: 0x740
+  __TEXT.__unwind_info: 0x400
+  __DATA_CONST.__const: 0x430
+  __DATA_CONST.__cfstring: 0x780
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x520
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__auth_got: 0x540
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x3c0
-  __DATA.__objc_selrefs: 0x2d8
+  __DATA.__objc_selrefs: 0x2f8
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x2164
+  __DATA.__data: 0x2168
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x5b4
+  __DATA.__bss: 0x5c8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 265
-  Symbols:   207
-  CStrings:  441
+  Functions: 273
+  Symbols:   213
+  CStrings:  457
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _TSPCPUTraceOptions_PidFilters
+ _objc_getClass
+ _tailspin_config_apply_sync
+ _tailspin_config_create_with_current_state
+ _tailspin_cputrace_enabled_set_with_options
CStrings:
+ "/System/Library/PrivateFrameworks/CoreDiagnostics.framework/Contents/MacOS/CoreDiagnostics"
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
