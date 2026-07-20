## System

> `/System/Library/CoreAccessories/PlugIns/Platform/System.platform/System`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1203.0.0.0.0
-  __TEXT.__text: 0x4ea8
-  __TEXT.__objc_methlist: 0x600
-  __TEXT.__cstring: 0x68b
+1210.0.0.502.1
+  __TEXT.__text: 0x4d9c
+  __TEXT.__objc_methlist: 0x5e8
+  __TEXT.__cstring: 0x676
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0xc8
   __TEXT.__oslogstring: 0x6e5
-  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__unwind_info: 0x1b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a0
+  __DATA_CONST.__objc_selrefs: 0x480
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x540
-  __AUTH_CONST.__objc_const: 0xad8
+  __AUTH_CONST.__cfstring: 0x520
+  __AUTH_CONST.__objc_const: 0xaa8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x200
+  __DATA.__objc_ivar: 0x30
+  __DATA.__data: 0x1fc
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x78

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 134
-  Symbols:   445
-  CStrings:  99
+  Functions: 132
+  Symbols:   436
+  CStrings:  98
 
Symbols:
- -[MediaLibraryHelper _updateITunesRadioEnabled]
- -[MediaLibraryHelper iTunesRadioEnabled]
- _CFPreferencesGetAppIntegerValue
- _OBJC_CLASS_$_MPRadioLibrary
- _OBJC_IVAR_$_MediaLibraryHelper._iTunesRadioEnabled
- ___iTunesRadioEnabledOverride.__overrideRadioAvailable
- _objc_msgSend$_updateITunesRadioEnabled
- _objc_msgSend$defaultRadioLibrary
- _objc_msgSend$isEnabled
CStrings:
- "overrideRadioEnabled"
```
