## IPConfiguration

> `/System/Library/PrivateFrameworks/IPConfiguration.framework/IPConfiguration`

```diff

-521.0.0.0.0
-  __TEXT.__text: 0x77a4
-  __TEXT.__auth_stubs: 0x6a0
+525.0.0.0.0
+  __TEXT.__text: 0x8134
+  __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0xd0
-  __TEXT.__oslogstring: 0x721
-  __TEXT.__cstring: 0x5a7
-  __TEXT.__unwind_info: 0x188
+  __TEXT.__const: 0xd8
+  __TEXT.__oslogstring: 0x829
+  __TEXT.__cstring: 0x600
+  __TEXT.__unwind_info: 0x198
   __TEXT.__objc_classname: 0x1b
   __TEXT.__objc_methname: 0x10f
   __TEXT.__objc_methtype: 0x63
   __TEXT.__objc_stubs: 0x140
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0x430
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x50
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x188
-  __AUTH_CONST.__cfstring: 0x480
+  __AUTH_CONST.__cfstring: 0x4c0
   __AUTH_CONST.__objc_const: 0x10
   __DATA.__data: 0x70
   __DATA.__bss: 0x20

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED968634-28A0-3A43-8D76-E5E3FC4FCC48
-  Functions: 90
-  Symbols:   178
-  CStrings:  188
+  UUID: D1CB4755-F6DA-32F9-98DF-A0BEBB9D50C0
+  Functions: 94
+  Symbols:   183
+  CStrings:  199
 
Symbols:
+ _CFDataCreateWithBytesNoCopy
+ _CFPropertyListCreateWithData
+ _IPConfigurationCopyIPv4RouterInformation
+ _kCFAllocatorNull
+ _vm_deallocate
CStrings:
+ "%s: interface must not be NULL"
+ "ARPResolvedHardwareAddress"
+ "ARPResolvedIPAddress"
+ "IPConfigurationCopyIPv4RouterInformation"
+ "ipconfig_get_ipv4_router() missing properties"
+ "ipconfig_get_ipv4_router() returned invalid data"
+ "ipconfig_get_ipv4_router() returned no information"
+ "ipconfig_get_ipv4_router_info(%s) failed, %s"
+ "ipconfig_get_ipv4_router_info(%s) success"

```
