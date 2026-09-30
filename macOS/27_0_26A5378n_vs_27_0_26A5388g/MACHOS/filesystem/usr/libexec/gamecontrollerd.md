## gamecontrollerd

> `/usr/libexec/gamecontrollerd`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`

```diff

-14.0.19.0.0
-  __TEXT.__text: 0x32a8
+14.0.21.0.0
+  __TEXT.__text: 0x3370
   __TEXT.__auth_stubs: 0x3d0
   __TEXT.__objc_stubs: 0x960
-  __TEXT.__objc_methlist: 0x4dc
-  __TEXT.__objc_classname: 0xc0
-  __TEXT.__objc_methname: 0xe7c
-  __TEXT.__objc_methtype: 0x6a1
+  __TEXT.__objc_methlist: 0x534
+  __TEXT.__objc_classname: 0xfb
+  __TEXT.__objc_methname: 0xf36
+  __TEXT.__objc_methtype: 0x79b
   __TEXT.__cstring: 0x3a9
   __TEXT.__const: 0x30
   __TEXT.__oslogstring: 0x555

   __DATA_CONST.__const: 0x200
   __DATA_CONST.__cfstring: 0x240
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0x120
-  __DATA.__objc_const: 0xbf8
-  __DATA.__objc_selrefs: 0x450
-  __DATA.__objc_ivar: 0x54
+  __DATA_CONST.__got: 0x130
+  __DATA.__objc_const: 0xca8
+  __DATA.__objc_selrefs: 0x478
+  __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x248
+  __DATA.__data: 0x308
   __DATA.__bss: 0x98
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 90
-  Symbols:   108
-  CStrings:  325
+  Symbols:   110
+  CStrings:  339
 
Symbols:
+ _OBJC_CLASS_$_GCSystemButtonArbitrationServer
+ _OBJC_CLASS_$_GCUserNotificationXPCProxyClient
Functions:
~ sub_100001c80 : 1068 -> 1156
~ sub_100002248 -> sub_1000022a0 : 312 -> 368
~ sub_100002c0c -> sub_100002c9c : 604 -> 620
~ sub_100003a24 -> sub_100003ac4 : 384 -> 424
CStrings:
+ "@\"GCFuture\"24@0:8@\"<GCUserNotificationRequest>\"16"
+ "@\"GCSystemButtonArbitrationServer\""
+ "@\"GCUserNotificationXPCProxyClient\""
+ "B32@0:8@\"GCXApplicationServicesApplicationTarget\"16@\"GCXApplicationServicesApplicationTarget\"24"
+ "B32@0:8@\"NSString\"16@\"NSString\"24"
+ "GCSystemButtonArbitrationService"
+ "GCUserNotificationService"
+ "_systemButtonArbitrationServer"
+ "_userNotificationManager"
+ "checkExceptionForApp:parent:"
+ "checkSystemGestureEnabled"
+ "clientProxyWithConnection:server:userDefaultsProxy:gameIntentProxy:userNotificationProxy:"
+ "performActions:"
+ "presentUserNotificationForRequest:"
+ "promptIfNeededForApp:parent:"
+ "settingsGeneration"
+ "systemGestureAction"
+ "v24@0:8@\"NSArray\"16"
- "clientProxyWithConnection:server:userDefaultsProxy:gameIntentProxy:"
- "launchApplicationWithBundleIdentifier:"
- "togglePlatformGamesLibrary"
- "v24@0:8@\"NSString\"16"
```
