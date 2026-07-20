## CoreRoutineDiagnostics

> `/System/Library/PrivateFrameworks/CoreRoutineDiagnostics.framework/Versions/A/CoreRoutineDiagnostics`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1117.0.0.0.0
-  __TEXT.__text: 0xf900
+1119.0.0.0.0
+  __TEXT.__text: 0xfa20
   __TEXT.__objc_methlist: 0xabc
   __TEXT.__dlopen_cstrs: 0x6d
-  __TEXT.__const: 0x170
+  __TEXT.__const: 0x178
   __TEXT.__gcc_except_tab: 0x3b4
-  __TEXT.__oslogstring: 0x1b2c
+  __TEXT.__oslogstring: 0x1b79
   __TEXT.__cstring: 0x17d6
   __TEXT.__ustring: 0x7c
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__unwind_info: 0x3d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libobjc.A.dylib
   Functions: 285
   Symbols:   872
-  CStrings:  361
+  CStrings:  362
 
Functions:
~ -[RTTransactionManager endProfilingForTransaction:] : 628 -> 916
CStrings:
+ "Profiling completed for %{public}@, durationMs, %.3f, identifier, %{public}@"
```
