## Keychain Circle Notification

> `/System/Library/CoreServices/Keychain Circle Notification.app/Contents/MacOS/Keychain Circle Notification`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.0.55.0.1
-  __TEXT.__text: 0x65a8
-  __TEXT.__auth_stubs: 0x3d0
+62460.1.2.0.0
+  __TEXT.__text: 0x66b4
+  __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_stubs: 0x10c0
   __TEXT.__objc_methlist: 0x898
-  __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x74d
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x754
   __TEXT.__objc_methname: 0x1987
   __TEXT.__objc_classname: 0xc2
   __TEXT.__objc_methtype: 0x726
-  __TEXT.__oslogstring: 0x931
+  __TEXT.__oslogstring: 0x94d
   __TEXT.__ustring: 0x1c
   __TEXT.__unwind_info: 0x160
-  __DATA_CONST.__const: 0x240
+  __DATA_CONST.__const: 0x260
   __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x1f0
-  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__auth_got: 0x218
+  __DATA_CONST.__got: 0x168
   __DATA.__objc_const: 0xb60
   __DATA.__objc_selrefs: 0x738
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x180
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Cocoa.framework/Versions/A/Cocoa

   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Versions/A/ProtectedCloudStorage
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 110
-  Symbols:   115
-  CStrings:  512
+  Functions: 111
+  Symbols:   121
+  CStrings:  514
 
Symbols:
+ __dispatch_source_type_signal
+ _dispatch_activate
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _signal
+ _xpc_transaction_exit_clean
Functions:
~ sub_100002e44 : 4 -> 152
+ sub_100002edc
CStrings:
+ "SIGTERM, exiting when clean"
+ "signal"
```
