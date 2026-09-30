## audiomxd

> `/usr/libexec/audiomxd`

```diff

-1541.1.1.0.0
-  __TEXT.__text: 0x3dd4
+1547.0.0.0.0
+  __TEXT.__text: 0x3f18
   __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_stubs: 0xc0
+  __TEXT.__objc_stubs: 0x100
   __TEXT.__const: 0xa4
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__gcc_except_tab: 0x358
-  __TEXT.__cstring: 0x452
-  __TEXT.__oslogstring: 0x31c
+  __TEXT.__cstring: 0x46b
+  __TEXT.__oslogstring: 0x35d
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x7f
+  __TEXT.__objc_methname: 0xb9
   __TEXT.__unwind_info: 0x170
   __DATA_CONST.__auth_got: 0x458
-  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x360
+  __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x30
+  __DATA.__objc_selrefs: 0x40
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D90B2C2-6F47-3412-9397-3861AEF6596D
-  Functions: 57
-  Symbols:   175
-  CStrings:  91
+  UUID: 38D36BE9-8E67-3AE3-A0C0-EEFEDDC7E766
+  Functions: 59
+  Symbols:   177
+  CStrings:  96
 
Symbols:
+ _NSCurrentLocaleDidChangeNotification
+ _OBJC_CLASS_$_NSNotificationCenter
Functions:
~ sub_100000e78 : 6172 -> 6216
+ sub_100002e48
+ sub_100002f64
CStrings:
+ "%25s:%-5d NSCurrentLocaleDidChangeNotification received"
+ "%25s:%-5d audiomxd exiting"
+ "%25s:%-5d com.apple.language.changed notification received"
+ "addObserverForName:object:queue:usingBlock:"
+ "defaultCenter"
+ "v16@?0@\"NSNotification\"8"
- "%25s:%-5d com.apple.language.changed notification received, audiomxd exiting"

```
