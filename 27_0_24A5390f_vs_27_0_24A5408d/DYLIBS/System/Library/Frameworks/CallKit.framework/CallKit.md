## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1397.100.1.0.0
-  __TEXT.__text: 0x67700
-  __TEXT.__objc_methlist: 0x927c
+1403.100.1.0.0
+  __TEXT.__text: 0x678a8
+  __TEXT.__objc_methlist: 0x92a4
   __TEXT.__const: 0x130
   __TEXT.__cstring: 0x63ab
-  __TEXT.__oslogstring: 0x3bb1
-  __TEXT.__gcc_except_tab: 0x6e4
+  __TEXT.__oslogstring: 0x3c25
+  __TEXT.__gcc_except_tab: 0x6f8
   __TEXT.__unwind_info: 0x1de8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3240
-  Symbols:   6840
-  CStrings:  1005
+  Functions: 3244
+  Symbols:   6844
+  CStrings:  1006
 
Symbols:
+ -[CXProvider _registerCurrentConfigurationIfAudioSessionIDStaleOnQueue]
+ -[CXProvider _registerCurrentConfigurationOnQueue]
+ -[CXProvider currentOpaqueAudioSessionID]
+ ___28-[CXProvider performAction:]_block_invoke
CStrings:
+ "Cached audioSessionID %u no longer matches current opaqueSessionID %u; re-registering configuration for CXProvider."
```
