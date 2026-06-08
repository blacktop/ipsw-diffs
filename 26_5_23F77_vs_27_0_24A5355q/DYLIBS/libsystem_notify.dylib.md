## libsystem_notify.dylib

> `/usr/lib/system/libsystem_notify.dylib`

```diff

-348.120.4.0.0
-  __TEXT.__text: 0xa24c
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__const: 0x118
-  __TEXT.__cstring: 0xc79
+367.0.0.0.0
+  __TEXT.__text: 0xa2c8
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0xcd6
   __TEXT.__dof_notify: 0x5a6
-  __DATA_CONST.__got: 0x60
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x248
-  __AUTH_CONST.__auth_got: 0x320
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__auth_got: 0x320
   __DATA.__data: 0x20
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 082935E9-82C8-338E-A403-38474DE5468A
+  UUID: E51999F5-289A-3083-83EE-02DEF4B3CCB0
   Functions: 90
   Symbols:   135
-  CStrings:  83
+  CStrings:  84
 
CStrings:
+ "[bug in libnotify] refcount underrun"
+ "[bug in libnotify] resurrecting name_node"
+ "[bug in libnotify] resurrecting registration_node"
- "atomic_refcount_release"
- "result >= 0"

```
