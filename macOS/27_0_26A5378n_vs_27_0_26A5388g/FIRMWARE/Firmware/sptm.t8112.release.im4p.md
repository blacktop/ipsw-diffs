## sptm.t8112.release.im4p

> `Firmware/sptm.t8112.release.im4p`

### Sections with Same Size but Changed Content

- `__LATE_CONST.__late_const`

```diff

-820.0.8.0.0
-  __TEXT.__cstring: 0x13ccd
+820.0.16.0.0
+  __TEXT.__cstring: 0x13daf
   __TEXT.__const: 0xa74
   __TEXT.__binname: 0x40
   __TEXT.__chain_starts: 0x14
-  __DATA_CONST.__const: 0x7410
+  __DATA_CONST.__const: 0x7430
   __LATE_CONST.__late_const: 0x7c838
-  __TEXT_EXEC.__text: 0x588c0
+  __TEXT_EXEC.__text: 0x588a8
   __TEXT_EXEC.__exc: 0x2000
   __LAST.__pinst: 0xc
   __DATA.__data: 0xf

   __DATA.__bss: 0x5fa8
   __DATA.__common: 0xb488
   __BOOTDATA.__data: 0x18000
-  Functions: 371
+  Functions: 369
   Symbols:   1
-  CStrings:  2339
+  CStrings:  2345
 
CStrings:
+ "%s: AMCC cache enabled unexpectedly: lock_group=%u aperture=%u plane=%u addr=%#llx read=%#x masked=%#x expected=%#x"
+ "%s: Invalid exception vector type: %s (%u) (current_hop=%llu, dispatch_state=%s)"
+ "%s: Provided CTXID %d does not fit in the ASID field"
+ "%s: Unexpected current_hop %llu (vector_type=%s (%u), dispatch_state=%s)"
+ "%s: lock group %u %s region has been locked unexpectedly (write_disabled=%d locked=%d)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VjN6yO/Sources/SPTM/sptm/boot/hib/hibernate_restore.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VjN6yO/Sources/SPTM/sptm/core/sptm_hibentry.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VjN6yO/Sources/SPTM/sptm/iommu/dart/t8110dart.c"
+ "INVALID_DISPATCH_STATE"
+ "INVALID_EVENT_TYPE"
+ "INVALID_VECTOR_TYPE"
+ "SPTM-820.0.16|2026-07-10:21:42:00.266834|"
+ "SPTM_VECTOR_FIQ"
+ "SPTM_VECTOR_IRQ"
+ "SPTM_VECTOR_SERROR"
+ "SPTM_VECTOR_SYNC"
+ "internal-isa-vm-allowed"
+ "tlbi_info_for_tlbi_asid"
- "%s: %u is not a valid dispatch event type (valid dispatch event types are 0 - %u)"
- "%s: %u is not a valid dispatch state (valid dispatch states are 0 - %u)"
- "%s: AMCC cache has been enabled unexpectedly"
- "%s: Invalid exception vector type: %u"
- "%s: Unexpected current_hop %llu"
- "%s: lock group %u %s region has been locked unexpectedly"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yLLxGH/Sources/SPTM/sptm/boot/hib/hibernate_restore.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yLLxGH/Sources/SPTM/sptm/core/sptm_hibentry.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yLLxGH/Sources/SPTM/sptm/iommu/dart/t8110dart.c"
- "SPTM-820.0.8|2026-06-26:20:02:19.635312|"
- "event_type_to_string"
- "state_to_string"
```
