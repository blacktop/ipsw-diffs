## dhcp6d

> `/usr/libexec/dhcp6d`

```diff

-494.120.6.0.0
-  __TEXT.__text: 0x7660
-  __TEXT.__auth_stubs: 0x690
+521.0.0.0.0
+  __TEXT.__text: 0x7c08
+  __TEXT.__auth_stubs: 0x6c0
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x95e
+  __TEXT.__cstring: 0x984
   __TEXT.__oslogstring: 0x55b
-  __TEXT.__unwind_info: 0x1b8
-  __DATA_CONST.__auth_got: 0x348
-  __DATA_CONST.__got: 0x80
+  __TEXT.__unwind_info: 0x1c8
+  __DATA_CONST.__auth_got: 0x360
+  __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1d0
-  __DATA_CONST.__cfstring: 0x640
+  __DATA_CONST.__const: 0x1e0
+  __DATA_CONST.__cfstring: 0x680
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
-  UUID: 2D775428-673C-341B-9BB2-EA4A8741E359
-  Functions: 100
-  Symbols:   128
-  CStrings:  240
+  UUID: 28815C00-4EFF-3E84-9E1A-8F790BE15106
+  Functions: 104
+  Symbols:   135
+  CStrings:  245
 
Symbols:
+ _CFArrayAppendValue
+ _CFArrayCreateMutable
+ _CFStringCreateWithFormat
+ _kSCPropNetDNSEncryptedServerAddresses
+ _kSCPropNetDNSEncryptedServerAuthenticationDomainName
+ _kSCPropNetDNSEncryptedServerServiceParameters
+ _kSCPropNetDNSEncryptedServerServicePriority
CStrings:
+ "%@\n"
+ "%d.%d.%d.%d"
+ "DNS_ENCRYPTED_SERVERS"

```
