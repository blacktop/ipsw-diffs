## exclave_pmm_exclave

> `Firmware/image4/exclavecore_bundle.t6050.RELEASE.im4p/exclave_pmm_exclave`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA.__const`
- `__DATA.__data`
- `__DATA.__auth_ptr`
- `__DATA.__mod_init_func`

```diff

-1490.0.21.0.0
-  __TEXT.__text: 0x4cb50
+1490.40.21.0.0
+  __TEXT.__text: 0x4c9d8
   __TEXT.__const: 0x1d140
-  __TEXT.__cstring: 0x121d3
+  __TEXT.__cstring: 0x12235
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__term_offsets: 0x0

   __DATA_CONST.__mod_term_func: 0x0
   __PDATA.__mod_init_func: 0x0
   __PDATA.__shared_cache: 0x0
-  Functions: 1208
+  Functions: 1207
   Symbols:   4
-  CStrings:  1513
+  CStrings:  1517
 
CStrings:
+ "!DO_CHUNKS_OVERLAP(currp, victimp) && !DO_CHUNKS_OVERLAP(currp->next, victimp)"
+ "!os_add_overflow(round_bytes, HEADER_UNIT_SIZE * UNIT_SIZE, &alloc_bytes)"
+ "!os_mul_overflow(units, UNIT_SIZE, &nb)"
+ "!overflow"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.2.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
+ "_insecure_random_buf"
+ "lcm"
+ "round_bytes >= alloc_bytes"
+ "s[0] || s[1]"
- "!(alignment % sizeof(Header)) && !(alignment % UNIT_SIZE)"
- "!os_mul_overflow(nu + PAD_ALLOC(align), UNIT_SIZE, &nb)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveCore.MacOSX.platform/Developer/SDKs/ExclaveCore.MacOSX27.0.Internal.sdk/System/ExclaveCore/System/Library/Frameworks/xrt.framework/Headers/thread.h"
- "alloc_bytes >= sz"
- "p->size * UNIT_SIZE >= sizeof(Header)"
```
