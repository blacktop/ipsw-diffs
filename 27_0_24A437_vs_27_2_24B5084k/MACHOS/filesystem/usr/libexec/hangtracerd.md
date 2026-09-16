## hangtracerd

> `/usr/libexec/hangtracerd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-426.0.0.0.0
-  __TEXT.__text: 0x35fb0
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_stubs: 0x5ca0
-  __TEXT.__objc_methlist: 0x289c
-  __TEXT.__const: 0x430
-  __TEXT.__cstring: 0x4da0
-  __TEXT.__objc_methname: 0x9c5b
+430.0.0.0.0
+  __TEXT.__text: 0x36860
+  __TEXT.__auth_stubs: 0xfb0
+  __TEXT.__objc_stubs: 0x5d00
+  __TEXT.__objc_methlist: 0x28a4
+  __TEXT.__const: 0x400
+  __TEXT.__cstring: 0x4dde
+  __TEXT.__objc_methname: 0x9c9a
   __TEXT.__objc_classname: 0x37d
   __TEXT.__objc_methtype: 0x1355
-  __TEXT.__gcc_except_tab: 0x430
-  __TEXT.__oslogstring: 0x6779
-  __TEXT.__unwind_info: 0x1018
-  __DATA_CONST.__const: 0x2238
-  __DATA_CONST.__cfstring: 0x6500
+  __TEXT.__gcc_except_tab: 0x450
+  __TEXT.__oslogstring: 0x69bc
+  __TEXT.__unwind_info: 0x1040
+  __DATA_CONST.__const: 0x2260
+  __DATA_CONST.__cfstring: 0x6560
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x7e0
+  __DATA_CONST.__auth_got: 0x7e8
   __DATA_CONST.__got: 0x490
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x5af0
-  __DATA.__objc_selrefs: 0x1ef8
+  __DATA.__objc_selrefs: 0x1f18
   __DATA.__objc_ivar: 0x52c
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x548

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 1386
-  Symbols:   402
-  CStrings:  3160
+  Functions: 1396
+  Symbols:   403
+  CStrings:  3175
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "%s: unable to resolve process path for pid %d, App launch request type"
+ ".."
+ "/"
+ "Display:%@ has no available modes (%lu modes total), dropping from display array: %@"
+ "Enumerating display:%@ of type:%ld"
+ "HANGTRACER_XPC_NAME_KEY for pid %d is missing or exceeds %d bytes; using fallback identifier"
+ "HANGTRACER_XPC_STATE_INFO_KEY data for pid %d is %zu bytes, expected exactly %zu; ignoring"
+ "HANGTRACER_XPC_USER_ACTION_DATA_KEY for pid %d is %zu bytes, exceeding limit of %d; ignoring"
+ "Ignoring non-approved display:%@ due to type:%ld"
+ "Refusing to create a HUDContext with no display to render to."
+ "allTaskingPrefNames"
+ "arrayWithCapacity:"
+ "availableModes"
+ "com.apple.chrono.WidgetRenderer-"
+ "displayType"
+ "displays"
+ "processPath is nil for App launch request type"
- "WidgetRenderer-Default"
- "mainDisplay"
```
