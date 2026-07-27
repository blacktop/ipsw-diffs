## WebInspector

> `/System/Library/PrivateFrameworks/WebInspector.framework/Versions/A/WebInspector`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-7624.4.2.11.2
-  __TEXT.__text: 0x8edc8
-  __TEXT.__auth_stubs: 0xb70
+7624.4.5.11.5
+  __TEXT.__text: 0x8f020
+  __TEXT.__auth_stubs: 0xb80
   __TEXT.__objc_methlist: 0x6850
   __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x5de7
-  __TEXT.__oslogstring: 0x493d
-  __TEXT.__gcc_except_tab: 0xc880
+  __TEXT.__cstring: 0x5e21
+  __TEXT.__oslogstring: 0x497e
+  __TEXT.__gcc_except_tab: 0xc8ec
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x3f58
+  __TEXT.__unwind_info: 0x3f68
   __TEXT.__objc_classname: 0x10b7
-  __TEXT.__objc_methname: 0xc5eb
+  __TEXT.__objc_methname: 0xc603
   __TEXT.__objc_methtype: 0x2169
-  __TEXT.__objc_stubs: 0x72c0
+  __TEXT.__objc_stubs: 0x7300
   __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__const: 0x1e90
   __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3530
+  __DATA_CONST.__objc_selrefs: 0x3538
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__auth_got: 0x5d8
   __AUTH_CONST.__const: 0x10f0
-  __AUTH_CONST.__cfstring: 0x5500
+  __AUTH_CONST.__cfstring: 0x5540
   __AUTH_CONST.__objc_const: 0xa6e8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0xd8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxcselect.dylib
-  Functions: 2892
-  Symbols:   6223
-  CStrings:  3646
+  Functions: 2893
+  Symbols:   6227
+  CStrings:  3650
 
Symbols:
+ _CFPreferencesCopyAppValue
+ _objc_msgSend$initWithContentsOfFile:
+ _objc_msgSend$setSize:
+ iconForDevice
Functions:
~ __Z24RWIOSNameFromDeviceClass14RWIDeviceClass : 40 -> 292
~ _iconForDevice : 912 -> 1256
+ _OUTLINED_FUNCTION_0
~ isInternalInstall.cold.1 : 20 -> 4
CStrings:
+ "Checking for override for device icon in defaults with key '%@'."
+ "FilmingIconForDevice-%@-%@"
+ "FilmingOSNameForDeviceClass-%@"
+ "initWithContentsOfFile:"
```
