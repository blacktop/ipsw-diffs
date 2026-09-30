## Diagnostic-4009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009.appex/Diagnostic-4009`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-1374.0.5.0.0
-  __TEXT.__text: 0x75ec
+1374.0.27.0.0
+  __TEXT.__text: 0x77c8
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x1840
-  __TEXT.__objc_methlist: 0xd64
-  __TEXT.__cstring: 0xb18
+  __TEXT.__objc_stubs: 0x1820
+  __TEXT.__objc_methlist: 0xd5c
+  __TEXT.__cstring: 0xac1
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x168
   __TEXT.__objc_classname: 0x153
-  __TEXT.__objc_methname: 0x1adf
+  __TEXT.__objc_methname: 0x1abf
   __TEXT.__objc_methtype: 0x777
-  __TEXT.__oslogstring: 0x331
+  __TEXT.__oslogstring: 0x46c
   __TEXT.__unwind_info: 0x2b0
   __DATA_CONST.__const: 0x238
   __DATA_CONST.__cfstring: 0x9e0

   __DATA_CONST.__auth_got: 0x368
   __DATA_CONST.__got: 0x1d8
   __DATA.__objc_const: 0x13d0
-  __DATA.__objc_selrefs: 0x760
+  __DATA.__objc_selrefs: 0x750
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x410
-  __DATA.__data: 0x308
+  __DATA.__data: 0x2e0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 246
+  Functions: 245
   Symbols:   207
-  CStrings:  567
+  CStrings:  569
 
CStrings:
+ "Device does not have Exclaves. Skipping stat capture."
+ "Display pipe stats captured"
+ "Exclaves is not supported, skipping status."
+ "Exclaves is supported."
+ "Platform has display pipe stats, preparing to capture"
+ "Retrieving display pipe stats..."
+ "Returning %lu stats for display pipe client"
+ "Starting display pipe stat capture"
- "/usr/local/bin/h10isp"
- "/usr/local/bin/h13isp"
- "/usr/local/bin/h16isp"
- "/usr/local/bin/h9isp"
- "ispBinary"
- "stringWithUTF8String:"
```
