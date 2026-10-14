## audiomxd

> `/usr/libexec/audiomxd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-1638.211.0.0.0
-  __TEXT.__text: 0x43a8
-  __TEXT.__auth_stubs: 0x890
+1638.215.0.0.0
+  __TEXT.__text: 0x4468
+  __TEXT.__auth_stubs: 0x8b0
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__const: 0xa0
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__gcc_except_tab: 0x378
-  __TEXT.__cstring: 0x4ca
-  __TEXT.__oslogstring: 0x326
+  __TEXT.__cstring: 0x4dc
+  __TEXT.__oslogstring: 0x377
   __TEXT.__objc_methname: 0x7f
   __TEXT.__unwind_info: 0x228
   __DATA_CONST.__const: 0x3e8
-  __DATA_CONST.__cfstring: 0x40
+  __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x458
-  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__auth_got: 0x468
+  __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_selrefs: 0x30
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 77
-  Symbols:   171
-  CStrings:  93
+  Symbols:   176
+  CStrings:  95
 
Symbols:
+ _CFPreferencesSynchronize
+ _MGGetSInt32Answer
+ _kCFPreferencesAnyApplication
+ _kCFPreferencesAnyHost
+ _kCFPreferencesAnyUser
Functions:
~ sub_1000029bc : 228 -> 412
~ sub_100004268 -> sub_100004320 : 1708 -> 1716
CStrings:
+ "%25s:%-5d resynchronizing all preferences to pick up new preferred language list"
+ "DeviceClassNumber"
```
