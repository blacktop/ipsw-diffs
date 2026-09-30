## libsystem_dnssd.dylib

> `/usr/lib/system/libsystem_dnssd.dylib`

```diff

-2559.80.8.0.0
-  __TEXT.__text: 0x62d0
+2600.100.146.0.0
+  __TEXT.__text: 0x6250
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__const: 0x122
+  __TEXT.__const: 0x12a
   __TEXT.__cstring: 0x1a8e
-  __TEXT.__unwind_info: 0x1c8
-  __DATA_CONST.__got: 0x20
+  __TEXT.__unwind_info: 0x1c0
+  __DATA_CONST.__got: 0x18
   __DATA_CONST.__const: 0x60
   __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x20
   __DATA.__bss: 0x28
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 97
+  Functions: 96
   Symbols:   159
   CStrings:  133
 
CStrings:
+ "DNSServiceSendQueuedRequestsInternal ERROR: writev(fd:%d, written:%zd, total:%zd bytes) failed, errno[%d]:%s"
+ "DNSServiceSendQueuedRequestsInternal: writev(fd:%d, numMsg:%u, %zd bytes) succeed"
+ "dnssd_clientstub CallbackWithError called with bad op %u"
+ "dnssd_clientstub DNSServiceAddRecord called with non-DNSServiceRegister DNSServiceRef %p %u"
+ "dnssd_clientstub DNSServiceProcessResult daemon version %u does not match client version %d"
+ "dnssd_clientstub DNSServiceRegisterRecord called with non-DNSServiceCreateConnection DNSServiceRef %p %u"
+ "dnssd_clientstub kDNSServiceFlagsShareConnection used with invalid DNSServiceRef %p %08X %08X op %u"
- "DNSServiceSendQueuedRequestsInternal ERROR: writev(fd:%d, written:%zu, total:%zu bytes) failed, errno[%d]:%s"
- "DNSServiceSendQueuedRequestsInternal: writev(fd:%d, numMsg:%d, %zu bytes) succeed"
- "dnssd_clientstub CallbackWithError called with bad op %d"
- "dnssd_clientstub DNSServiceAddRecord called with non-DNSServiceRegister DNSServiceRef %p %d"
- "dnssd_clientstub DNSServiceProcessResult daemon version %d does not match client version %d"
- "dnssd_clientstub DNSServiceRegisterRecord called with non-DNSServiceCreateConnection DNSServiceRef %p %d"
- "dnssd_clientstub kDNSServiceFlagsShareConnection used with invalid DNSServiceRef %p %08X %08X op %d"

```
