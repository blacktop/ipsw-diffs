## diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

-490.120.2.0.0
-  __TEXT.__text: 0x19018
+490.120.6.0.0
+  __TEXT.__text: 0x1922c
   __TEXT.__auth_stubs: 0x1690
   __TEXT.__objc_stubs: 0x520
   __TEXT.__objc_methlist: 0xc8
-  __TEXT.__cstring: 0x2cbf
+  __TEXT.__cstring: 0x2cfc
   __TEXT.__const: 0x78
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0xd4

   __TEXT.__objc_methname: 0x475
   __TEXT.__objc_methtype: 0x102
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x5b8
+  __TEXT.__unwind_info: 0x5c8
   __DATA_CONST.__auth_got: 0xb58
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x8

   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x130
-  __DATA.__bss: 0xda8
+  __DATA.__bss: 0xdb0
   __DATA.__common: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 490
+  Functions: 494
   Symbols:   408
-  CStrings:  631
+  CStrings:  633
 
Symbols:
+ _fstatfs_ext
+ _statfs_ext
- _MKBDeviceUnlockedSinceBoot
- _fstatfs
CStrings:
+ " Device is not unlocked, delaying probe of %@"
+ "Lock notification received - device is %slocked"
+ "com.apple.mobile.keybagd.lock_status"
+ "un"
- "First unlock notification received"
- "com.apple.mobile.keybagd.first_unlock"

```
