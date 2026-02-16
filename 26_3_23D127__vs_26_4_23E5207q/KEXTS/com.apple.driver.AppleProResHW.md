## com.apple.driver.AppleProResHW

> `com.apple.driver.AppleProResHW`

```diff

-501.4.0.0.0
-  __TEXT.__const: 0x21e8
-  __TEXT.__os_log: 0x9688
-  __TEXT.__cstring: 0xffa
-  __TEXT_EXEC.__text: 0x3e2b4
+550.45.0.0.0
+  __TEXT.__const: 0x21d8
+  __TEXT.__os_log: 0x97d4
+  __TEXT.__cstring: 0x103e
+  __TEXT_EXEC.__text: 0x3dcc0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3b8
   __DATA.__common: 0x70
   __DATA.__bss: 0x6cc0
-  __DATA_CONST.__auth_got: 0x288
+  __DATA_CONST.__auth_got: 0x2d0
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0xa138
+  __DATA_CONST.__const: 0xa140
   __DATA_CONST.__kalloc_type: 0x480
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 4361087B-D9DB-3D11-9F80-3652150B7943
-  Functions: 2043
+  UUID: 73380110-0309-3BC8-A1EA-241568F2AB70
+  Functions: 2050
   Symbols:   0
-  CStrings:  521
+  CStrings:  530
 
CStrings:
+ "\"AppleProResHW (0x%x): %s(): ProResHW is hung, client timed out (duration = %llu msec) attempting to transition to power state %lu\" @%s:%d"
+ "12111112122212121122111121111112111111211111121122221111222221111211111121111112111111211111111111111111111111111111112112112112111111111111111111111111111111111111111111111111111111111111111111111222222222222222222111111122221111111111111111212222211112"
+ "AppleProResHW (0x%x): %s(): AppleProResHW ERROR: Could not set power state to %lu"
+ "AppleProResHW (0x%x): %s(): Attempting to report invalid event to CoreAnalytics\n"
+ "AppleProResHW (0x%x): %s(): CFA=%d plane allocSize=%llu, planeCount=%u planeSize=%u BytesPerRow=%u Data/Stride R=%llx/%u\n"
+ "AppleProResHW (0x%x): %s(): CFA=%d plane allocSize=%llu, planeSize=%u BytesPerRow=%u Data/Stride R=%llx/%u\n"
+ "AppleProResHW (0x%x): %s(): CoreAnalytics: Failed to send CA event (Return code: %d)\n"
+ "AppleProResHW (0x%x): %s(): CoreAnalytics: event %s\n"
+ "AppleProResHW (0x%x): %s(): DevID %d: Invalid CoreIdx(%d) to set AXI2AF parity"
+ "AppleProResHW (0x%x): %s(): Planar Data/Stride R=%p,%u Gr=%p,%u Gb=%p,%u B=%p,%u Plane Count=%d CFA=%d\n"
+ "AppleProResHW (0x%x): %s(): Tiled Meta Base=%llx\n"
+ "AppleProResHW (0x%x): %s(): Tiled MetaData Base=%llx\n"
+ "AppleProResHW (0x%x): %s(): insufficient PowerProvider states %u"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProRes ERROR: Plane count is not 4 or 1 or 0!\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): AppleProRes RAW ERROR: Plane count is not 4 or 1 or 0!\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Compressed not allowed for RAW pixel formats\n"
+ "ERROR AppleProResHW: %d: %s(): insufficient PowerProvider states %u\n"
+ "ERROR: AppleProResHW (0x%x): %d: %s(): HW error decStatus=%d status0=0x%x statusCode=%d status2=0x%x crccrd0d=0x%x crccrd1d=0x%x\n\n"
+ "ERROR: AppleProResHW (0x%x): %d: %s(): HW error encStatus=%d status0=0x%x statusCode=%d status2=0x%x crcdrdd=0x%x\n\n"
+ "axi2af_parity_enable"
+ "com.apple.AppleProResHW.ProResHWInfo"
+ "enableAFLinkParity"
+ "powerRequestTimeouts"
+ "reportHWInfo"
+ "reportHardwareStatus"
- "\"AppleProResHW (0x%x): %s(): ProResHW is hung, client timed out attempting to transition to power state %lu\" @%s:%d"
- "1211111212221212112211112111111211111121111112112222111122222111121111112111111211111121111111111111111111111111111111211211211211111111111111111111111111111111111111111111111111111111111111111111122222222222222222211111112222111111111111212222211112"
- "AppleProResHW (0x%x): %s(): CFA=%d Data/Stride R=%p,%u\n"
- "AppleProResHW (0x%x): %s(): Data/Stride R=%p,%u Gr=%p,%u Gb=%p,%u B=%p,%u Plane Count=%d CFA=%d\n"
- "AppleProResHW (0x%x): %s(): Dec Desc V0\n"
- "AppleProResHW (0x%x): %s(): Dec Desc V2\n"
- "AppleProResHW (0x%x): %s(): Override CFA=%d Meta=%p Data/Stride R=%p,%u\n"
- "AppleProResHW (0x%x): %s(): Single plane bp16 case, Data/Stride R=%p,%u, Plane Count=%d CFA=%d\n"
- "AppleProResHW (0x%x): %s(): plane allocSize=%llu, Size=%u\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): AppleProRes ERROR: Plane count is not 4 or 0 or 1!\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): AppleProRes RAW ERROR: Plane count is not 0 or 4!\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): AppleProResHW ERROR: Could not set power state to %lu\n"
- "ERROR AppleProResHW: %d: %s(): insufficient PowerProvider states\n"
- "ERROR: AppleProResHW (0x%x): %d: %s(): HW error decStatus=%d status0=0x%x statusCode=%d status2=0x%x\n\n"
- "ERROR: AppleProResHW (0x%x): %d: %s(): HW error encStatus=%d status0=0x%x statusCode=%d status2=0x%x \n\n"
- "The offset of the pointer inside its valid memory range can't be represented using int32_t"

```
