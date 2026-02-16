## captiveagent

> `/usr/libexec/captiveagent`

```diff

-514.80.3.0.1
-  __TEXT.__text: 0x10a34
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_stubs: 0x1600
+514.100.16.0.0
+  __TEXT.__text: 0x11e34
+  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__objc_stubs: 0x16a0
   __TEXT.__objc_methlist: 0xcb8
   __TEXT.__const: 0x146
-  __TEXT.__gcc_except_tab: 0x388
-  __TEXT.__objc_methname: 0x1d3b
-  __TEXT.__oslogstring: 0x16fc
-  __TEXT.__cstring: 0x7c3
+  __TEXT.__oslogstring: 0x193e
+  __TEXT.__gcc_except_tab: 0x37c
+  __TEXT.__objc_methname: 0x1d9a
+  __TEXT.__cstring: 0x7c5
   __TEXT.__objc_classname: 0xd1
   __TEXT.__objc_methtype: 0xa05
-  __TEXT.__unwind_info: 0x448
-  __DATA_CONST.__auth_got: 0x588
-  __DATA_CONST.__got: 0x1b0
+  __TEXT.__unwind_info: 0x548
+  __DATA_CONST.__auth_got: 0x590
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x500
-  __DATA_CONST.__cfstring: 0x8a0
+  __DATA_CONST.__cfstring: 0x8c0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA.__objc_const: 0x1948
-  __DATA.__objc_selrefs: 0x858
+  __DATA.__objc_selrefs: 0x880
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x2f8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 12FC448A-4EFB-318D-8885-9242F207D511
-  Functions: 311
-  Symbols:   239
-  CStrings:  781
+  UUID: 3CF723CB-C466-3765-BDCB-5DE67C91A4B8
+  Functions: 316
+  Symbols:   248
+  CStrings:  800
 
Symbols:
+ _CFStringCreateMutableCopy
+ _CFStringGetLength
+ _CFStringReplace
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ ___NSDictionary0__struct
+ _kSCPropNetProxiesBypassAllowed
+ _kSCPropNetProxiesHTTPEnable
+ _kSCPropNetProxiesHTTPSEnable
+ _kSCPropNetProxiesProxyAutoConfigEnable
+ _kSCPropNetProxiesProxyAutoDiscoveryEnable
+ _kSCPropNetProxiesSOCKSEnable
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x8
CStrings:
+ "*"
+ "CAAPIHandler: setting empty proxy configuration"
+ "CAAPIHandler: setting proxy configuration: %@"
+ "CNCaptiveProber: setting empty proxy configuration"
+ "CNCaptiveProber: setting proxy configuration: %@"
+ "CNTokenAuthenticator: setting empty proxy configuration"
+ "CNTokenAuthenticator: setting proxy configuration: %@"
+ "CNWISPrLoginHandler: setting empty proxy configuration"
+ "CNWISPrLoginHandler: setting proxy configuration: %@"
+ "array"
+ "connectionProxyDictionary"
+ "found valid interface (%@) proxy configuration: %@"
+ "global proxy configuration has captive bypass disabled"
+ "initWithDictionary:"
+ "intersectOrderedSet:"
+ "orderedSetWithArray:"
+ "proxies: %@"
+ "sessionConfiguration:"
+ "starting data task with proxy configuration: %@"
- "sessionConfiguration"

```
