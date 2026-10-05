## restorecameraispd

> `/usr/libexec/restorecameraispd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-20.105.6.0.0
-  __TEXT.__text: 0x1d40c
-  __TEXT.__auth_stubs: 0xf90
+20.106.4.0.0
+  __TEXT.__text: 0x1d768
+  __TEXT.__auth_stubs: 0xfb0
   __TEXT.__objc_stubs: 0x4a0
   __TEXT.__const: 0x16e0
-  __TEXT.__cstring: 0x345f
-  __TEXT.__gcc_except_tab: 0x4b8
-  __TEXT.__oslogstring: 0x2350
+  __TEXT.__cstring: 0x350c
+  __TEXT.__gcc_except_tab: 0x4b4
+  __TEXT.__oslogstring: 0x237c
   __TEXT.__objc_methname: 0x32c
-  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__unwind_info: 0x808
   __DATA_CONST.__const: 0x80b8
-  __DATA_CONST.__cfstring: 0x15e0
+  __DATA_CONST.__cfstring: 0x1620
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x7d8
+  __DATA_CONST.__auth_got: 0x7e8
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_selrefs: 0x128
-  __DATA.__data: 0x571c88
+  __DATA.__data: 0x5acc88
   __DATA.__common: 0x7
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 425
-  Symbols:   301
-  CStrings:  644
+  Functions: 430
+  Symbols:   303
+  CStrings:  653
 
Symbols:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "%s - Error reading kernel config cache - chan: %d, res: 0x%08X\n"
+ "%s - channel configs not valid - exiting\n"
+ "%s - kernel config count %d != firmware %d - chan: %d\n"
+ "/usr/local/share/firmware/isp/2027_01XX.dat"
+ "/usr/local/share/firmware/isp/2327_01XX.dat"
+ "/usr/local/share/firmware/isp/2327_02XX.dat"
+ "20.106.4"
+ "CacheChannelConfigs"
+ "Could not find %s as %s (errno: %d)"
+ "Found %s at %s."
+ "Will use ISP references"
+ "Will use SEP references"
+ "sparse reference plist"
+ "sparseLP reference plist"
- "%s - Error getting LSC polynomial - chan: %d, res: 0x%08X\n"
- "%s - Error getting camera config - chan: %d, res: 0x%08X\n"
- "20.105.6"
- "Could not find reference plist at %s (errno: %d). Will use ISP references"
- "Found reference plist at %s. Will use SEP references"
```
