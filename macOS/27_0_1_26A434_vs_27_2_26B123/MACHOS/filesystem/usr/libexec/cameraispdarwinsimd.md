## cameraispdarwinsimd

> `/usr/libexec/cameraispdarwinsimd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-20.70.0.0.0
-  __TEXT.__text: 0x14d48
-  __TEXT.__auth_stubs: 0xd40
+20.107.1.0.0
+  __TEXT.__text: 0x15514
+  __TEXT.__auth_stubs: 0xd60
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x1ae3
-  __TEXT.__const: 0x160
-  __TEXT.__gcc_except_tab: 0x1dc
-  __TEXT.__oslogstring: 0x22ef
-  __TEXT.__unwind_info: 0x548
+  __TEXT.__cstring: 0x1cde
+  __TEXT.__const: 0x170
+  __TEXT.__gcc_except_tab: 0x1d0
+  __TEXT.__oslogstring: 0x23e2
+  __TEXT.__unwind_info: 0x560
   __DATA_CONST.__const: 0x7d88
   __DATA_CONST.__cfstring: 0x5e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x6a8
+  __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__data: 0x3bdbe8
+  __DATA.__data: 0x5acc70
   __DATA.__bss: 0xb8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 295
-  Symbols:   244
-  CStrings:  406
+  Functions: 304
+  Symbols:   246
+  CStrings:  422
 
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
+ "/usr/local/share/firmware/isp/2727_01XX.dat"
+ "/usr/local/share/firmware/isp/3527_02XX.dat"
+ "/usr/local/share/firmware/isp/3527_03XX.dat"
+ "/usr/local/share/firmware/isp/4227_01XX.dat"
+ "/usr/local/share/firmware/isp/4427_01XX.dat"
+ "/usr/local/share/firmware/isp/7127_02XX.dat"
+ "/usr/local/share/firmware/isp/7327_01XX.dat"
+ "/usr/local/share/firmware/isp/7327_02XX.dat"
+ "20.107.1"
+ "CacheChannelConfigs"
+ "Unexpected client Get data length=%zu expected=%zu (pid %{private}d)\n"
+ "Unexpected client Set data length=%zu expected=%zu (pid %{private}d)\n"
- "%s - Error getting camera config - chan: %d, res: 0x%08X\n"
- "20.70"
```
