## CaptiveNetwork

> `/System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork`

```diff

-491.120.4.0.0
-  __TEXT.__text: 0xa348
+504.0.0.0.2
+  __TEXT.__text: 0xa378
   __TEXT.__auth_stubs: 0x800
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x667
+  __TEXT.__cstring: 0x67f
   __TEXT.__oslogstring: 0x70b
-  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__unwind_info: 0x2c0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x15
   __TEXT.__objc_methname: 0x2c

   __DATA_CONST.__objc_selrefs: 0x10
   __AUTH_CONST.__auth_got: 0x408
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x820
+  __AUTH_CONST.__cfstring: 0x840
   __AUTH_CONST.__objc_const: 0x40
-  __DATA.__data: 0x148
+  __DATA.__data: 0x150
   __DATA.__bss: 0x78
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x30

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0ADE70E7-027B-37A8-9D30-068ACD1F05C5
-  Functions: 211
-  Symbols:   626
-  CStrings:  233
+  UUID: 6284D940-04E1-3358-91AE-7D8245DF4FB9
+  Functions: 210
+  Symbols:   627
+  CStrings:  235
 
Symbols:
+ _CFAllocatorAllocateTyped
+ _CNNetworkCreate.cold.1
+ _CNNetworkCreateWithSSIDAndBSSID.cold.1
+ _kCNSCaptivePortalClientAuthenticationURLProperty
- _CFAllocatorAllocate
- ___CNNetworkAllocate
- ___CNNetworkAllocate.cold.1
Functions:
~ _CFStringMallocCString : 152 -> 160
~ _MachServerCallback : 240 -> 248
~ _CNNetworkCreate : 84 -> 140
- ___CNNetworkAllocate
~ _CNNetworkCreateWithSSIDAndBSSID : 236 -> 288
CStrings:
+ "ClientAuthenticationURL"

```
