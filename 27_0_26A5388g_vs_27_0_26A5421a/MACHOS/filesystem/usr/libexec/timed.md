## timed

> `/usr/libexec/timed`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-340.0.12.0.0
-  __TEXT.__text: 0x18094
+340.0.14.0.0
+  __TEXT.__text: 0x18154
   __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_stubs: 0x2760
-  __TEXT.__objc_methlist: 0xd6c
+  __TEXT.__objc_stubs: 0x2780
+  __TEXT.__objc_methlist: 0xd7c
   __TEXT.__const: 0x290
-  __TEXT.__objc_methname: 0x25ef
+  __TEXT.__objc_methname: 0x2626
   __TEXT.__cstring: 0x20dc
   __TEXT.__objc_classname: 0x111
   __TEXT.__objc_methtype: 0x554

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__auth_got: 0x5a8
   __DATA_CONST.__got: 0x1c8
-  __DATA.__objc_const: 0x1da0
-  __DATA.__objc_selrefs: 0xb68
+  __DATA.__objc_const: 0x1db0
+  __DATA.__objc_selrefs: 0xb70
   __DATA.__objc_ivar: 0x174
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x310

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 648
+  Functions: 649
   Symbols:   247
-  CStrings:  1294
+  CStrings:  1297
 
CStrings:
+ "340.0.14"
+ "TB,R,GisAudioAccessory"
+ "audioAccessory"
+ "isAudioAccessory"
- "340.0.12"
```
