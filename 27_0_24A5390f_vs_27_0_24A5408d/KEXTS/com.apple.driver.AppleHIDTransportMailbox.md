## com.apple.driver.AppleHIDTransportMailbox

> `com.apple.driver.AppleHIDTransportMailbox`

```diff

-10100.39.0.0.0
+10100.41.0.0.0
   __TEXT.__const: 0x125
-  __TEXT.__cstring: 0x3357
-  __TEXT_EXEC.__text: 0x17c98
-  __TEXT_EXEC.__auth_stubs: 0x420
+  __TEXT.__cstring: 0x3130
+  __TEXT_EXEC.__text: 0x17698
+  __TEXT_EXEC.__auth_stubs: 0x410
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x12e0
   __DATA_CONST.__kalloc_type: 0x80
-  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0xc0
   Functions: 357
   Symbols:   0
-  CStrings:  307
+  CStrings:  296
 
Functions:
~ __ZN35AppleHIDTransportProtocolSCMMailbox24enableInputReportLoggingEhb -> sub_fffffe0008ee5c5c : 956 -> 16
~ __ZN35AppleHIDTransportProtocolSCMMailbox29drainInputReportLoggingBufferEP18IOMemoryDescriptorPy -> sub_fffffe0008ee5d9c : 612 -> 16
CStrings:
- "[0x%llx][%llx][%s::%s]: ERROR!! drain failed with ret=0x%08X (%s)"
- "[0x%llx][%llx][%s::%s]: ERROR!! failed to allocate input report logging buffer (%u bytes)"
- "[0x%llx][%llx][%s::%s]: ERROR!! invalid interfaceID %u"
- "[0x%llx][%llx][%s::%s]: allocated input report logging buffer (%u bytes, watermark %u bytes)"
- "[0x%llx][%llx][%s::%s]: interface %u %s, mask=0x%08X"
- "[0x%llx][%llx][%s::%s]: released input report logging buffer"
- "[0x%llx][%llx][%s::%s]: wrote %llu bytes, %u bytes remaining"
- "disabled"
- "drainInputReportLoggingBuffer"
- "enableInputReportLogging"
- "enabled"
```
