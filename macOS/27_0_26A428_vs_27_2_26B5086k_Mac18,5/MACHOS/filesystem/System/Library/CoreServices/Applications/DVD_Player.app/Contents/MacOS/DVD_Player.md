## DVD Player

> `/System/Library/CoreServices/Applications/DVD Player.app/Contents/MacOS/DVD Player`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-282.5.0.0.0
-  __TEXT.__text: 0xdec8
-  __TEXT.__auth_stubs: 0x8f0
+292.1.0.0.0
+  __TEXT.__text: 0xe00c
+  __TEXT.__auth_stubs: 0x910
   __TEXT.__objc_stubs: 0x3940
   __TEXT.__objc_methlist: 0x164c
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0x1125
-  __TEXT.__objc_methname: 0x4b7b
+  __TEXT.__gcc_except_tab: 0x78
+  __TEXT.__cstring: 0x1156
+  __TEXT.__objc_methname: 0x4b86
   __TEXT.__objc_classname: 0x2c7
   __TEXT.__objc_methtype: 0xf40
-  __TEXT.__unwind_info: 0x548
-  __DATA_CONST.__const: 0x380
-  __DATA_CONST.__cfstring: 0x14a0
+  __TEXT.__unwind_info: 0x550
+  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__cfstring: 0x14c0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__auth_got: 0x488
-  __DATA_CONST.__got: 0x300
+  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__got: 0x310
   __DATA.__objc_const: 0x2ca8
   __DATA.__objc_selrefs: 0x1508
   __DATA.__objc_ivar: 0x260

   - /System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 362
-  Symbols:   260
-  CStrings:  1256
+  Functions: 364
+  Symbols:   264
+  CStrings:  1257
 
Symbols:
+ _DVDSleep
+ _DVDWakeUp
+ _NSWorkspaceDidWakeNotification
+ _NSWorkspaceWillSleepNotification
CStrings:
+ "_deviceMounted: ignoring non-removable volume %@"
+ "_isRemovableVolumeAtPath:"
- "_isValidMedia:"
```
