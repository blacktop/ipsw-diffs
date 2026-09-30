## com.apple.filesystems.cd9660

> `com.apple.filesystems.cd9660`

```diff

-  __TEXT.__cstring: 0x312
+  __TEXT.__cstring: 0x42a
   __TEXT.__const: 0x1016
-  __TEXT_EXEC.__text: 0x51bc
-  __TEXT_EXEC.__auth_stubs: 0x5b0
+  __TEXT_EXEC.__text: 0x5314
+  __TEXT_EXEC.__auth_stubs: 0x5c0
   __DATA.__data: 0xd10
   __DATA.__common: 0x50
   __DATA.__bss: 0x8
   __DATA_CONST.__kalloc_type: 0x2c0
-  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0x20
-  Functions: 89
-  Symbols:   293
-  CStrings:  30
+  Functions: 90
+  Symbols:   295
+  CStrings:  35
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ _cd9660_ratelimit_log_allowed
+ _nanouptime
CStrings:
+ "2121222222222222222222112222"
+ "cd9660: RRIP SL trailing %td bytes too small for component header\n"
+ "cd9660: RRIP invalid SL component length %d\n"
+ "cd9660: RRIP invalid SL length %d\n"
+ "cd9660: RRIP malformed SUSP entry (type '%c%c', length %zu, remaining %td)\n"
+ "cd9660: aborting RRIP CE chain at %d entries (blk=%u)\n"
- "21212222222222222222221122"

```
