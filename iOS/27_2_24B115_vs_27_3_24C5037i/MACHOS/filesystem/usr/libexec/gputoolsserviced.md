## gputoolsserviced

> `/usr/libexec/gputoolsserviced`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2027.1.3.0.0
-  __TEXT.__text: 0x32900
-  __TEXT.__auth_stubs: 0xf20
+2027.2.4.0.0
+  __TEXT.__text: 0x32944
+  __TEXT.__auth_stubs: 0xf40
   __TEXT.__objc_stubs: 0x5680
   __TEXT.__objc_methlist: 0x363c
   __TEXT.__const: 0x4d0

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x798
+  __DATA_CONST.__auth_got: 0x7a8
   __DATA_CONST.__got: 0x288
   __DATA.__objc_const: 0x6f00
   __DATA.__objc_selrefs: 0x1de8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 1180
-  Symbols:   328
+  Symbols:   330
   CStrings:  2100
 
Symbols:
+ _IOObjectRelease
+ _IOServiceClose
Functions:
~ sub_1000091f4 : 10620 -> 10648
~ sub_10000c6d4 -> sub_10000c6f0 : 6484 -> 6500
~ sub_10000e290 -> sub_10000e2bc : 48 -> 72
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/capabilities/runtime/GTCapabilitiesRuntime.m:315"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/capabilities/runtime/GTCapabilitiesRuntime.m:313"
```
