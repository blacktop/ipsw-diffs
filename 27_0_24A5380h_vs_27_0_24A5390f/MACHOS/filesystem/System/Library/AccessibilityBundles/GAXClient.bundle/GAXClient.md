## GAXClient

> `/System/Library/AccessibilityBundles/GAXClient.bundle/GAXClient`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-1059.0.0.0.0
-  __TEXT.__text: 0x9dfc
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_stubs: 0x1960
-  __TEXT.__objc_methlist: 0xa44
-  __TEXT.__const: 0x78
+1061.0.0.0.0
+  __TEXT.__text: 0xa1ec
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_stubs: 0x19e0
+  __TEXT.__objc_methlist: 0xa4c
+  __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__oslogstring: 0x961
-  __TEXT.__cstring: 0x29cb
-  __TEXT.__objc_methname: 0x1c45
+  __TEXT.__oslogstring: 0xb20
+  __TEXT.__cstring: 0x29ff
+  __TEXT.__objc_methname: 0x1c7f
   __TEXT.__objc_classname: 0x897
   __TEXT.__objc_methtype: 0x3b6
-  __TEXT.__unwind_info: 0x390
-  __DATA_CONST.__const: 0xc98
+  __TEXT.__unwind_info: 0x398
+  __DATA_CONST.__const: 0xcb8
   __DATA_CONST.__cfstring: 0x2960
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x308
-  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__auth_got: 0x330
+  __DATA_CONST.__got: 0x210
   __DATA.__objc_const: 0x2248
-  __DATA.__objc_selrefs: 0x848
+  __DATA.__objc_selrefs: 0x868
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x11d0
   __DATA.__data: 0x8
-  __DATA.__bss: 0x61
+  __DATA.__bss: 0x71
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 251
-  Symbols:   458
-  CStrings:  746
+  Functions: 253
+  Symbols:   465
+  CStrings:  756
 
Symbols:
+ _AXIsInternalInstall
+ _bootstrap_look_up2
+ _bootstrap_port
+ _mach_port_deallocate
+ _mach_task_self_
+ _notify_get_state
+ _notify_register_check
CStrings:
+ "GAX client became active but per-PID IPC registration is GONE (backboard cannot reach us). Service:%{public}@"
+ "GAX client became active. Per-PID IPC registration is alive. Service:%{public}@"
+ "GAX client became active; unexpected bootstrap_look_up2 result (kr=%{public}d). Service:%{public}@"
+ "Skipping ASAM re-adoption on client load: backboard reports no active session."
+ "Suppressing stale currentlyActiveSession: backboard reports no active session."
+ "UTF8String"
+ "_logIPCRegistrationState"
+ "com.apple.accessibility.guidedaccess.session.active"
+ "isRunning"
+ "serviceName"
```
