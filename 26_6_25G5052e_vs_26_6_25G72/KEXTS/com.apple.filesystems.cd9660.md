## com.apple.filesystems.cd9660

> `com.apple.filesystems.cd9660`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__kalloc_type`

```diff

-39.160.3.0.0
-  __TEXT.__cstring: 0x312
+39.160.4.0.0
+  __TEXT.__cstring: 0x3f3
   __TEXT.__const: 0x1016
-  __TEXT_EXEC.__text: 0x513c
+  __TEXT_EXEC.__text: 0x5298
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd10
   __DATA.__common: 0x50
   __DATA.__bss: 0x8
-  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__kalloc_type: 0x2c0
-  Functions: 89
-  Symbols:   293
-  CStrings:  30
+  Functions: 90
+  Symbols:   295
+  CStrings:  34
 
Symbols:
+ _cd9660_ratelimit_log_allowed
+ _nanouptime
Functions:
~ _cd9660_rrip_loop : 508 -> 564
~ _cd9660_rrip_slink : 724 -> 868
+ _cd9660_ratelimit_log_allowed
CStrings:
+ "2121222222222222222222112222"
+ "cd9660: RRIP SL trailing %td bytes too small for component header\n"
+ "cd9660: RRIP invalid SL component length %d\n"
+ "cd9660: RRIP invalid SL length %d\n"
+ "cd9660: RRIP malformed SUSP entry (type '%c%c', length %zu, remaining %td)\n"
- "21212222222222222222221122"
```
