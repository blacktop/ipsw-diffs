## HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-430.0.0.0.0
-  __TEXT.__text: 0x14898
+430.1.0.0.0
+  __TEXT.__text: 0x14c08
   __TEXT.__auth_stubs: 0xad0
   __TEXT.__delay_helper: 0xdc
   __TEXT.__objc_stubs: 0x1d80
   __TEXT.__objc_methlist: 0xd34
-  __TEXT.__const: 0x2b0
-  __TEXT.__cstring: 0x283c
-  __TEXT.__oslogstring: 0x2144
+  __TEXT.__const: 0x280
+  __TEXT.__cstring: 0x284c
+  __TEXT.__oslogstring: 0x2210
   __TEXT.__gcc_except_tab: 0x1cc
   __TEXT.__objc_classname: 0xde
   __TEXT.__objc_methname: 0x46e2
   __TEXT.__objc_methtype: 0xa29
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x5c0
+  __TEXT.__unwind_info: 0x5d0
   __DATA_CONST.__const: 0xe48
   __DATA_CONST.__cfstring: 0x27a0
   __DATA_CONST.__objc_classlist: 0x50

   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 487
-  Symbols:   507
-  CStrings:  1289
+  Functions: 490
+  Symbols:   510
+  CStrings:  1292
 
Symbols:
+ _HTDurationInBackgroundCPURolesFromSortedArray
+ _HTIsBackgroundCPURoleHang
+ _HTIsSiriAIBundleID
CStrings:
+ "Failed to create state info JSON blob for hang (start %llu, end %llu, state info %@). Returning 0ms background duration."
+ "Hang detected: %.2fs (Siri AI in background CPU role with no visible UI, ignoring)"
+ "com.apple.campo"
```
