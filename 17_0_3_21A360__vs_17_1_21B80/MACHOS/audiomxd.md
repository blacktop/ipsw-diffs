## audiomxd

> `/usr/libexec/audiomxd`

```diff

-1387.1.10.30.3
-  __TEXT.__text: 0x3a34
-  __TEXT.__auth_stubs: 0x880
+1387.2.13.30.2
+  __TEXT.__text: 0x3a84
+  __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_stubs: 0x160
   __TEXT.__const: 0x8a
   __TEXT.__gcc_except_tab: 0x2c0
-  __TEXT.__cstring: 0x34f
-  __TEXT.__oslogstring: 0x2b7
+  __TEXT.__cstring: 0x347
+  __TEXT.__oslogstring: 0x304
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x102
   __TEXT.__unwind_info: 0x180
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x450
-  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3c0
-  __DATA_CONST.__cfstring: 0x40
+  __DATA_CONST.__const: 0x400
+  __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x58
   __DATA.__objc_classrefs: 0x30

   - /usr/lib/libobjc.A.dylib
   Functions: 64
   Symbols:   176
-  CStrings:  83
+  CStrings:  85
 
Symbols:
+ __dispatch_main_q
+ _notify_register_dispatch
- _CFNotificationCenterAddObserver
- _CFNotificationCenterGetDarwinNotifyCenter
CStrings:
+ "%25s:%-5d Could not register for language change notification, err = %u"
+ "%25s:%-5d com.apple.language.changed notification received, audiomxd exiting"
+ "com.apple.language.changed"
+ "v12@?0i8"
- "%25s:%-5d AppleLanguagePreferencesChangedNotification, audiomxd exiting"
- "AppleLanguagePreferencesChangedNotification"

```
