## mount_afp

> `/sbin/mount_afp`

```diff

-521.0.0.0.0
-  __TEXT.__text: 0x9c8
+523.0.0.0.0
+  __TEXT.__text: 0xa18
   __TEXT.__auth_stubs: 0x150
-  __TEXT.__cstring: 0x29b
+  __TEXT.__cstring: 0x3ce
   __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0xa8
   __DATA_CONST.__got: 0x18

   - /usr/lib/libutil.dylib
   Functions: 3
   Symbols:   26
-  CStrings:  37
+  CStrings:  40
 
CStrings:
+ "*** AFP Network Disk Obsoletion Warning ***\n"
+ "*** AFP client is deprecated in the current version and will be removed in a future version of macOS. ***\n"
+ "*** We encourage users to explore alternatives and migrate their workflows before upgrading to the version which removes support for the AFP client. ***\n\n"

```
