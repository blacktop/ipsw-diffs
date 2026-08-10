## libmecabra.dylib

> `/usr/lib/libmecabra.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1154.0.0.0.0
-  __TEXT.__text: 0x26b520
+1159.0.0.0.0
+  __TEXT.__text: 0x26c760
   __TEXT.__lazy_helpers: 0xfc
   __TEXT.__objc_methlist: 0x3e4
-  __TEXT.__const: 0x3001c
+  __TEXT.__const: 0x3004c
   __TEXT.__dlopen_cstrs: 0x152
-  __TEXT.__cstring: 0x16aab
-  __TEXT.__gcc_except_tab: 0x1a790
-  __TEXT.__ustring: 0x32ae
-  __TEXT.__oslogstring: 0x4a0e
-  __TEXT.__unwind_info: 0xce60
+  __TEXT.__cstring: 0x16b15
+  __TEXT.__gcc_except_tab: 0x1a82c
+  __TEXT.__ustring: 0x32cc
+  __TEXT.__oslogstring: 0x4a59
+  __TEXT.__unwind_info: 0xce90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x16860
+  __DATA_CONST.__const: 0x16840
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x348
   __DATA_CONST.__got: 0x440
-  __AUTH_CONST.__const: 0x435f0
+  __AUTH_CONST.__const: 0x43620
   __AUTH_CONST.__cfstring: 0x9240
   __AUTH_CONST.__objc_const: 0x3c0
   __AUTH_CONST.__weak_auth_got: 0x60

   __AUTH.__thread_bss: 0x618
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x1bec
-  __DATA.__bss: 0x1c40
-  __DATA.__common: 0xa28
+  __DATA.__bss: 0x1c90
+  __DATA.__common: 0xa30
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 11145
+  Functions: 11150
   Symbols:   1095
-  CStrings:  4423
+  CStrings:  4429
 
CStrings:
+ "%s: File size: %zu bytes"
+ "Blocklist is empty."
+ "Blocklist is truncated."
+ "Failed to reload blocklist."
+ "Malformed length in Blocklist."
+ "Malformed offset in Blocklist."
+ "[E5Runner] Path %zu: surface='%s', originalCost=%f, e5RunnerProb=%f, geometryCost=%f, syllableMatchPenalty=%f, adaptationBoost=%f, readingMismatchPenalty=%f, dynamicWordReward=%f, finalScore=%f"
- "[E5Runner] Path %zu: surface='%s', originalCost=%f, e5RunnerProb=%f, geometryCost=%f, syllableMatchPenalty=%f, adaptationBoost=%f, readingMismatchPenalty=%f, finalScore=%f"
```
