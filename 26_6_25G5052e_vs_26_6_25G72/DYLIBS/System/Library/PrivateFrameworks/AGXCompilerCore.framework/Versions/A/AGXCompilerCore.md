## AGXCompilerCore

> `/System/Library/PrivateFrameworks/AGXCompilerCore.framework/Versions/A/AGXCompilerCore`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__data`

```diff

-353.12.0.0.0
-  __TEXT.__text: 0x22b5d8
-  __TEXT.__auth_stubs: 0x2770
+353.14.0.0.0
+  __TEXT.__text: 0x22b264
+  __TEXT.__auth_stubs: 0x2760
   __TEXT.__const: 0x39d28
   __TEXT.__oslogstring: 0x3fe
-  __TEXT.__cstring: 0x1b184
+  __TEXT.__cstring: 0x1b116
   __TEXT.__objc_methname: 0xb
   __TEXT.__objc_stubs: 0x20
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x7968
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x13c0
+  __AUTH_CONST.__auth_got: 0x13b8
   __AUTH_CONST.__const: 0x726e0
   __AUTH_CONST.__cfstring: 0x40
   __AUTH.__data: 0x50

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 7278
-  Symbols:   10240
-  CStrings:  4578
+  Symbols:   10239
+  CStrings:  4573
 
Symbols:
- __ZN4llvm11raw_ostreamlsEm
Functions:
~ __ZN4llvm6detail9PassModelINS_6ModuleE29DeduplicateGlobalBindingsPassNS_17PreservedAnalysesENS_15AnalysisManagerIS2_JEEEJEE3runERS2_RS6_ : 2760 -> 1856
~ __ZL23pluginSupportsOSVersion12AGCOSVersion : 100 -> 120
CStrings:
- "' has type "
- ", duplicate '"
- ": "
- "First occurrence '"
- "Type mismatch for duplicate global bindings at binding index "
```
