## com.apple.iokit.IOSurface

> `com.apple.iokit.IOSurface`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__got`

```diff

-402.5.0.0.0
-  __TEXT.__cstring: 0x3355
-  __TEXT.__os_log: 0x3501
-  __TEXT.__const: 0x40
-  __TEXT_EXEC.__text: 0x332bc
-  __TEXT_EXEC.__auth_stubs: 0x900
+402.8.0.0.0
+  __TEXT.__cstring: 0x33b7
+  __TEXT.__os_log: 0x3779
+  __TEXT.__const: 0x60
+  __TEXT_EXEC.__text: 0x33968
+  __TEXT_EXEC.__auth_stubs: 0x940
   __DATA.__data: 0x178
   __DATA.__common: 0x460
   __DATA.__bss: 0x38

   __DATA_CONST.__const: 0x46f8
   __DATA_CONST.__kalloc_type: 0xd00
   __DATA_CONST.__kalloc_var: 0xaa0
-  __DATA_CONST.__auth_got: 0x480
+  __DATA_CONST.__auth_got: 0x4a0
   __DATA_CONST.__got: 0xd0
-  Functions: 1324
+  Functions: 1330
   Symbols:   0
-  CStrings:  638
+  CStrings:  649
 
CStrings:
+ "%s"
+ "%s%u"
+ "%s: Couldn't allocate range allocator for graphics memory\n"
+ "112"
+ "1211111212221212121122222212212111212211111112211112221111112111122111121222212222122221222212222122221222212222112111112221112211112112222222222112"
+ "Failed to install %s memory region; checking in anyway\n"
+ "IOSurface: /vram declares %u carveout(s) but %u resolved; positions are ambiguous, installing none\n"
+ "IOSurface: /vram declares %u carveout(s) but none resolved\n"
+ "IOSurface: couldn't count /vram's reg tuples; assuming a single carveout\n"
+ "IOSurface: discovered %u display carveout(s) in /vram\n"
+ "IOSurfaceDeviceMemoryRegion: Couldn't get device memory with index %u for service %s\n"
+ "IOSurfaceDeviceMemoryRegion: Couldn't map device memory\n"
+ "IOSurfaceDeviceMemoryRegion: zero-length device memory with index %u for service %s\n"
+ "reg"
+ "virtual bool IOSurfaceDeviceMemoryRegion::init(IOSurfaceRoot *, OSDictionary *, const char *, uint32_t, uint32_t)"
- "1112"
- "121111121222121212112222221221211121221111111211112221111112111122111121222212222122221222212222122221222212222112111112221112211112112222222222112"
- "PurpleGfxMem"
- "ScalableMemory"
```
