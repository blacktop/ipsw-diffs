## bootpd

> `/usr/libexec/bootpd`

```diff

-494.120.6.0.0
-  __TEXT.__text: 0x10078
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x1e44
+521.0.0.0.0
+  __TEXT.__text: 0x10e28
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__const: 0xe8
+  __TEXT.__cstring: 0x1ed1
   __TEXT.__oslogstring: 0x114f
-  __TEXT.__unwind_info: 0x2d8
-  __DATA_CONST.__auth_got: 0x468
-  __DATA_CONST.__got: 0x98
+  __TEXT.__unwind_info: 0x2e8
+  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1300
-  __DATA_CONST.__cfstring: 0xb60
+  __DATA_CONST.__const: 0x1318
+  __DATA_CONST.__cfstring: 0xc40
   __DATA.__data: 0xa8
   __DATA.__common: 0x311
   __DATA.__bss: 0x1350

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libresolv.9.dylib
-  UUID: FFE5EEAB-3889-3214-AA04-65C3CA2C6881
-  Functions: 195
-  Symbols:   182
-  CStrings:  731
+  UUID: 221A1BBA-4DCE-3B2D-ABA3-93E4C2646AAD
+  Functions: 201
+  Symbols:   197
+  CStrings:  745
 
Symbols:
+ _CFArrayAppendArray
+ _CFArraySortValues
+ _CFDataFind
+ _CFNumberCompare
+ _CFSetAddValue
+ _CFSetContainsValue
+ _CFSetCreateMutable
+ _CFStringAppend
+ _CFStringCompare
+ _CFStringCreateWithFormat
+ _kCFTypeSetCallBacks
+ _kSCPropNetDNSEncryptedServerAddresses
+ _kSCPropNetDNSEncryptedServerAuthenticationDomainName
+ _kSCPropNetDNSEncryptedServerServiceParameters
+ _kSCPropNetDNSEncryptedServerServicePriority
CStrings:
+ "\n}"
+ "EncryptedServerAddresses"
+ "EncryptedServerName"
+ "EncryptedServerParameters"
+ "EncryptedServerPriority"
+ "dns_dnr_data"
+ "encrypted_dns_server"
+ "{ %@ (%@)\n%@\n'%@'\n}"
- "option_162"

```
