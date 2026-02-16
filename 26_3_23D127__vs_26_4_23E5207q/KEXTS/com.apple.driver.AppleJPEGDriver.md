## com.apple.driver.AppleJPEGDriver

> `com.apple.driver.AppleJPEGDriver`

```diff

-7.7.2.0.0
-  __TEXT.__cstring: 0x2829
-  __TEXT.__os_log: 0x8c84
-  __TEXT.__const: 0x3684
-  __TEXT_EXEC.__text: 0x2aa54
+7.7.8.0.0
+  __TEXT.__cstring: 0x296c
+  __TEXT.__os_log: 0x9171
+  __TEXT.__const: 0x35ec
+  __TEXT_EXEC.__text: 0x29f58
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2208
   __DATA.__common: 0x380

   __DATA_CONST.__got: 0x98
   __DATA_CONST.__mod_init_func: 0xb0
   __DATA_CONST.__mod_term_func: 0xb0
-  __DATA_CONST.__const: 0x4700
-  __DATA_CONST.__kalloc_type: 0xb80
-  UUID: 56BF938B-1EB0-3107-9532-E5FFFA9E8647
-  Functions: 1629
+  __DATA_CONST.__const: 0x4830
+  __DATA_CONST.__kalloc_type: 0xd00
+  UUID: 43CC61E1-8F46-301F-92A4-AA8118D37EAF
+  Functions: 1682
   Symbols:   0
-  CStrings:  502
+  CStrings:  510
 
CStrings:
+ "1122211111111122121122222222212222222222222222222222222222222222222222222222222222222221111222221122222222222222212222222121112222222222222"
+ "AppleJPEGDriver: %s: Timeout occurred, cleaning up mPendingSetup for codec %d\n"
+ "AppleJPEGDriver: %s: codec, tlimit vir [%p], tlimit_outstanding vir [%p]\n"
+ "AppleJPEGDriver: %s:[%d] Error: Still has pending transaction. May have issue when reset.\n"
+ "AppleJPEGDriver: %s:[%d] std_done %x, dma done %x error=0x%x, pendingRequst=%p\n"
+ "AppleJPEGDriver: ** %s[%p] : 'axi2af_parity_enable' boot-arg detected: %u\n"
+ "axi2af_parity_enable"
+ "virtual uint32_t AppleJPEGWrapperControl::read_jw_axi_tcount()"
+ "virtual uint32_t AppleJPEGWrapperControl::read_jw_axi_tlimit()"
+ "virtual void AppleJPEGWrapperControl::set_jw_axi_tcount(uint32_t)"
+ "virtual void AppleJPEGWrapperControl::set_jw_axi_tlimit(uint32_t)"
+ "void AppleJPEGHal::pollingForAXI()"
+ "void AppleJPEGPM::setPUPowerState(uint32_t, bool, bool)"
- "1122211111111122121122222222212222222222222222222222222222222222222222222222222222222221111222221122222222222222212222222122222222222222"
- "AppleJPEGDriver: %s: codec, tlimit [0x%016llx], tlimit_outstanding [0x%016llx]\n"
- "AppleJPEGDriver: %s: codec, tlimit vir [0x%016llx], tlimit_outstanding vir [0x%016llx]\n"
- "AppleJPEGDriver: %s: codec, vir=0x%016llx, phy=0x%016llx, length=%u\n"
- "void AppleJPEGPM::setPUPowerState(uint32_t, bool)"

```
