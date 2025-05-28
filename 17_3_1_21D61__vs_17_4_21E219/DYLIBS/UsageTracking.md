## UsageTracking

> `/System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking`

```diff

-324.0.0.0.0
-  __TEXT.__text: 0x1f984
+336.0.0.0.0
+  __TEXT.__text: 0x1fa08
   __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0xdd0
+  __TEXT.__objc_methlist: 0xdd8
   __TEXT.__const: 0x95
-  __TEXT.__cstring: 0x101d
+  __TEXT.__cstring: 0x1032
   __TEXT.__oslogstring: 0x848
   __TEXT.__gcc_except_tab: 0x45c
   __TEXT.__unwind_info: 0x55c
   __TEXT.__objc_classname: 0x24a
-  __TEXT.__objc_methname: 0x4fc1
-  __TEXT.__objc_methtype: 0xd04
-  __TEXT.__objc_stubs: 0x2ee0
+  __TEXT.__objc_methname: 0x5055
+  __TEXT.__objc_methtype: 0xd14
+  __TEXT.__objc_stubs: 0x2f00
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0xbd0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1850
-  __DATA_CONST.__objc_selrefs: 0xd90
+  __DATA_CONST.__objc_const: 0x1880
+  __DATA_CONST.__objc_selrefs: 0xd98
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x210
+  __DATA_CONST.__objc_superrefs: 0x78
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__cfstring: 0xc60
+  __AUTH_CONST.__cfstring: 0xc80
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x278
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x210
-  __DATA.__objc_superrefs: 0x78
-  __DATA.__objc_ivar: 0x10c
+  __DATA.__objc_ivar: 0x110
   __DATA.__data: 0x240
   __DATA.__bss: 0x10
   __DATA_DIRTY.__const: 0x80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 412
-  Symbols:   1741
-  CStrings:  882
+  Functions: 413
+  Symbols:   1745
+  CStrings:  886
 
Symbols:
+ -[USDeviceActivityEvent includesPastActivity]
+ -[USDeviceActivityEvent initWithApplicationTokens:categoryTokens:webDomainTokens:threshold:includesPastActivity:]
+ -[USDeviceActivityEvent initWithBundleIdentifiers:categoryIdentifiers:webDomains:threshold:includesPastActivity:]
+ _OBJC_IVAR_$_USDeviceActivityEvent._includesPastActivity
+ _objc_msgSend$includesPastActivity
- -[USDeviceActivityEvent initWithApplicationTokens:categoryTokens:webDomainTokens:threshold:]
- -[USDeviceActivityEvent initWithBundleIdentifiers:categoryIdentifiers:webDomains:threshold:]
CStrings:
+ "IncludesPastActivity"
+ "TB,R,V_includesPastActivity"
+ "_includesPastActivity"
+ "includesPastActivity"
+ "initWithApplicationTokens:categoryTokens:webDomainTokens:threshold:includesPastActivity:"
+ "initWithBundleIdentifiers:categoryIdentifiers:webDomains:threshold:includesPastActivity:"
+ "startVideoUsageForBundleIdentifier:profileIdentifier:uniqueIdentifier:URL:mediaURL:usageTrusted:replyHandler:"
+ "stopVideoUsageForBundleIdentifier:profileIdentifier:uniqueIdentifier:URL:mediaURL:usageTrusted:replyHandler:"
+ "v68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSURL\"40@\"NSURL\"48B56@?<v@?>60"
+ "v68@0:8@16@24@32@40@48B56@?60"
- "initWithApplicationTokens:categoryTokens:webDomainTokens:threshold:"
- "initWithBundleIdentifiers:categoryIdentifiers:webDomains:threshold:"
- "startVideoUsageForBundleIdentifier:profileIdentifier:URL:mediaURL:usageTrusted:replyHandler:"
- "stopVideoUsageForBundleIdentifier:profileIdentifier:URL:mediaURL:usageTrusted:replyHandler:"
- "v60@0:8@\"NSString\"16@\"NSString\"24@\"NSURL\"32@\"NSURL\"40B48@?<v@?>52"
- "v60@0:8@16@24@32@40B48@?52"

```
