## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

```diff

-1321.0.0.0.0
-  __TEXT.__text: 0x28838
+1322.3.0.0.0
+  __TEXT.__text: 0x28d64
   __TEXT.__auth_stubs: 0x650
   __TEXT.__const: 0x600
-  __TEXT.__cstring: 0x47c1
+  __TEXT.__cstring: 0x4839
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x1588
   __DATA_CONST.__helper: 0x8
   __AUTH_CONST.__auth_got: 0x328
-  __AUTH_CONST.__const: 0x1828
+  __AUTH_CONST.__const: 0x1730
   __AUTH.__data: 0x8
   __DATA.__crash_info: 0x148
   __DATA.__data: 0x120

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: E63888B9-F2AF-32F4-8D27-7D3C6CC7ED73
-  Functions: 1047
-  Symbols:   2762
-  CStrings:  534
+  UUID: 274FC511-EED1-3500-BFB4-69E0EB6945A2
+  Functions: 1057
+  Symbols:   2779
+  CStrings:  541
 
Symbols:
+ __ZN11Diagnostics11appendErrorEPKcz.cold.1
+ __ZN11Diagnostics11appendErrorEPKcz.cold.2
+ __ZN11Diagnostics11appendErrorEPKcz.cold.3
+ __ZN11Diagnostics11appendErrorEPKcz.cold.4
+ __ZN11Diagnostics5errorEPKc12va_list_wrap.cold.1
+ __ZN11Diagnostics5errorEPKc12va_list_wrap.cold.2
+ __ZN11Diagnostics5errorEPKc12va_list_wrap.cold.3
+ __ZN11Diagnostics5errorEPKc12va_list_wrap.cold.4
+ __ZN11DiagnosticsC1Ev
+ __ZN16SafeRemoteBuffer4dataEv
+ __ZN16SafeRemoteBufferC1EjyyPi
+ __ZN16SafeRemoteBufferD1Ev
+ __dyld_call_with_writable_tpro_memory
+ _mach_vm_read
+ _vm_read_safe
+ _vsnprintf
- __ZN11DiagnosticsC1Eb
- __ZNK6mach_o12PlatformInfo14versionForYearEtb
- __ZNK6mach_o18PlatformInfo_macOS14versionForYearEtb
- __ZNK6mach_o18PlatformInfo_sepOS14versionForYearEtb
- __ZNK6mach_o21PlatformInfo_firmware14versionForYearEtb
- __simple_sresize
- __simple_string
CStrings:
+ "(actualSize + 1) == expectedSize"
+ "Diagnostics.cpp"
+ "actualSize >= 0"
+ "appendError"
+ "error"
+ "expectedSize >= 0"
+ "kr == KERN_SUCCESS"

```
