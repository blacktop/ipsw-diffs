## gamecontrollerd

> `/usr/libexec/gamecontrollerd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`

```diff

-14.0.19.0.0
-  __TEXT.__text: 0x1fcc
+14.0.21.0.0
+  __TEXT.__text: 0x207c
   __TEXT.__auth_stubs: 0x380
   __TEXT.__objc_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x494
-  __TEXT.__objc_classname: 0xc0
-  __TEXT.__objc_methname: 0xc4e
-  __TEXT.__objc_methtype: 0x655
-  __TEXT.__cstring: 0x315
+  __TEXT.__objc_methlist: 0x4dc
+  __TEXT.__objc_classname: 0xfb
+  __TEXT.__objc_methname: 0xcd5
+  __TEXT.__objc_methtype: 0x6e8
+  __TEXT.__cstring: 0x316
   __TEXT.__oslogstring: 0x19e
   __TEXT.__gcc_except_tab: 0xb0
   __TEXT.__const: 0x18

   __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__auth_got: 0x1d0
-  __DATA_CONST.__got: 0xc8
-  __DATA.__objc_const: 0xbb8
-  __DATA.__objc_selrefs: 0x3c8
-  __DATA.__objc_ivar: 0x4c
+  __DATA_CONST.__got: 0xd8
+  __DATA.__objc_const: 0xc60
+  __DATA.__objc_selrefs: 0x3e8
+  __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x248
+  __DATA.__data: 0x308
   __DATA.__bss: 0x98
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 72
-  Symbols:   92
-  CStrings:  282
+  Symbols:   94
+  CStrings:  294
 
Symbols:
+ _OBJC_CLASS_$_GCSystemButtonArbitrationServer
+ _OBJC_CLASS_$_GCUserNotificationManager
Functions:
~ sub_10000187c : 856 -> 936
~ sub_100001d40 -> sub_100001d90 : 296 -> 352
~ sub_1000028c4 -> sub_10000294c : 344 -> 384
CStrings:
+ "@\"GCFuture\"24@0:8@\"<GCUserNotificationRequest>\"16"
+ "@\"GCSystemButtonArbitrationServer\""
+ "@\"GCUserNotificationManager\""
+ "B32@0:8@\"NSString\"16@\"NSString\"24"
+ "GCSystemButtonArbitrationService"
+ "GCUserNotificationService"
+ "_systemButtonArbitrationServer"
+ "_userNotificationManager"
+ "checkExceptionForApp:parent:"
+ "checkSystemGestureEnabled"
+ "performActions:"
+ "presentUserNotificationForRequest:"
+ "settingsGeneration"
+ "systemGestureAction"
+ "v24@0:8@\"NSArray\"16"
- "launchApplicationWithBundleIdentifier:"
- "togglePlatformGamesLibrary"
- "v24@0:8@\"NSString\"16"
```
