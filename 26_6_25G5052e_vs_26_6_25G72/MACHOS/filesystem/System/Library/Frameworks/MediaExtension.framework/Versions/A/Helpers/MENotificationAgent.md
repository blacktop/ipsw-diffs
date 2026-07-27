## MENotificationAgent

> `/System/Library/Frameworks/MediaExtension.framework/Versions/A/Helpers/MENotificationAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`

```diff

-3330.10.1.0.0
-  __TEXT.__text: 0x12a8
-  __TEXT.__auth_stubs: 0x260
+3330.13.2.0.0
+  __TEXT.__text: 0xeac
+  __TEXT.__auth_stubs: 0x230
   __TEXT.__objc_stubs: 0x580
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x397
-  __TEXT.__oslogstring: 0x21e
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x376
   __TEXT.__objc_methname: 0x3d0
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x138
+  __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__cfstring: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x160
-  __DATA.__bss: 0xc
+  __DATA.__bss: 0x4
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 9
-  Symbols:   67
-  CStrings:  86
+  Symbols:   64
+  CStrings:  75
 
Symbols:
- __os_log_impl
- _os_log_create
- _os_log_type_enabled
Functions:
~ sub_100000ac8 -> sub_100000a78 : 780 -> 520
~ sub_100000dd4 -> sub_100000c80 : 2360 -> 1944
~ sub_100001bf8 -> sub_100001904 : 200 -> 4
~ sub_100001cc0 -> sub_100001908 : 176 -> 28
CStrings:
- "%@: Failed to convert user info XPC dictionary to CF dictionary"
- "%@: Invalid UserInfo entry for notification event"
- "%@: No XPC_EVENT_KEY_NAME in event"
- "%@: Unable to post user notification because of error %@"
- "%@: UserInfo was not a dictionary for notification event"
- "%@: active %.2f seconds and processed %d notifications"
- "%@: invalid notification bundleIDs value"
- "%@: sandbox_init_with_parameters err:%d errorbuf:%s -- Exiting."
- "MediaExtension format readers and video decoders enabled -- thank you for setting \"ffctl CoreMedia/MediaExtensions=on\""
- "com.apple.coremedia"
- "me_agent_log"
```
