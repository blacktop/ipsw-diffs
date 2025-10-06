## bootpd

> `/usr/libexec/bootpd`

```diff

-455.60.2.0.0
-  __TEXT.__text: 0x10030
+455.100.4.0.0
+  __TEXT.__text: 0x10060
   __TEXT.__auth_stubs: 0x8c0
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x1e46

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libresolv.9.dylib
-  UUID: 8CF089FD-3AB6-386B-8DC4-B4EACAB3BAB6
+  UUID: F654F616-D673-3A3A-9622-537C53D44EC0
   Functions: 200
   Symbols:   183
   CStrings:  733
Symbols:
+ __SCNetworkInterfaceIsTetheredHotspot
- __SCNetworkInterfaceIsTethered

```
