## mmaintenanced

> `/usr/libexec/mmaintenanced`

```diff

-136.120.6.0.0
-  __TEXT.__text: 0x13bf0
-  __TEXT.__auth_stubs: 0xad0
+136.140.3.0.0
+  __TEXT.__text: 0x13e88
+  __TEXT.__auth_stubs: 0xb10
   __TEXT.__init_offsets: 0x4
-  __TEXT.__oslogstring: 0x193b
-  __TEXT.__cstring: 0x10b0
+  __TEXT.__oslogstring: 0x199f
+  __TEXT.__cstring: 0x10dd
   __TEXT.__const: 0x4d8
   __TEXT.__gcc_except_tab: 0x6f0
-  __TEXT.__unwind_info: 0x6dc
+  __TEXT.__unwind_info: 0x6e8
   __TEXT.__eh_frame: 0x88
-  __DATA_CONST.__auth_got: 0x570
+  __DATA_CONST.__auth_got: 0x590
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0xa90
   __DATA_CONST.__cfstring: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 29F70A00-4547-3898-A237-641096409489
-  Functions: 447
-  Symbols:   224
-  CStrings:  329
+  UUID: 50C92474-DFFF-37EC-90E1-92CBFDBB74C4
+  Functions: 455
+  Symbols:   228
+  CStrings:  335
 
Symbols:
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _CFStringCreateWithCString
+ _IOObjectRelease
CStrings:
+ "CFStringCreateWithCString failed"
+ "IODeviceTree:/chosen"
+ "Incorrect valueRef's length"
+ "Unable to open iodevicetree to read %s"
+ "dram-ecc"
+ "dram-vendor-id"

```
