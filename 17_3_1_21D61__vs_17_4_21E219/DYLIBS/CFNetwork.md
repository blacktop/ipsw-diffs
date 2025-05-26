## CFNetwork

> `/System/Library/Frameworks/CFNetwork.framework/CFNetwork`

```diff

-1492.0.1.0.0
-  __TEXT.__text: 0x286518
-  __TEXT.__auth_stubs: 0x5610
-  __TEXT.__objc_methlist: 0x8e90
+1494.0.7.0.0
+  __TEXT.__text: 0x287490
+  __TEXT.__auth_stubs: 0x5620
+  __TEXT.__objc_methlist: 0x8ea8
   __TEXT.__const: 0xc9a4c
-  __TEXT.__gcc_except_tab: 0x13f3c
-  __TEXT.__cstring: 0x1ab09
-  __TEXT.__oslogstring: 0x1036c
+  __TEXT.__gcc_except_tab: 0x13f94
+  __TEXT.__cstring: 0x1aaf6
+  __TEXT.__oslogstring: 0x1042f
   __TEXT.__dlopen_cstrs: 0x104b
   __TEXT.__dof_CFNetwork: 0xf3b
-  __TEXT.__unwind_info: 0xc84c
+  __TEXT.__unwind_info: 0xc88c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x15ca
-  __TEXT.__objc_methname: 0x17f94
-  __TEXT.__objc_methtype: 0x6e05
-  __TEXT.__objc_stubs: 0xe9e0
+  __TEXT.__objc_methname: 0x17fe4
+  __TEXT.__objc_methtype: 0x6e14
+  __TEXT.__objc_stubs: 0xe9c0
   __DATA_CONST.__got: 0x758
-  __DATA_CONST.__const: 0x9f48
+  __DATA_CONST.__const: 0x9ff0
   __DATA_CONST.__objc_classlist: 0x508
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x123b8
-  __DATA_CONST.__objc_selrefs: 0x4c80
+  __DATA_CONST.__objc_selrefs: 0x4c88
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x5e8
+  __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__const: 0x13f58
-  __AUTH_CONST.__cfstring: 0xfc00
+  __AUTH_CONST.__const: 0x13f28
+  __AUTH_CONST.__cfstring: 0xfbe0
   __AUTH_CONST.__objc_const: 0x39e0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x2b20
+  __AUTH_CONST.__auth_got: 0x2b28
   __AUTH.__objc_data: 0x17c0
   __AUTH.__cfstring_CFN: 0x7b60
   __AUTH.__data: 0x358
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x5e8
-  __DATA.__objc_superrefs: 0x410
   __DATA.__objc_ivar: 0x13d4
-  __DATA.__data: 0x1950
+  __DATA.__data: 0x1958
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xdb8
+  __DATA.__bss: 0xda0
   __DATA_DIRTY.__objc_data: 0x1a90
   __DATA_DIRTY.__data: 0x270
-  __DATA_DIRTY.__bss: 0x9e0
+  __DATA_DIRTY.__bss: 0x9f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13522
-  Symbols:   2551
-  CStrings:  9824
+  Functions: 13530
+  Symbols:   2555
+  CStrings:  9829
 
Symbols:
+ __CFHTTPAuthenticationCheckOriginAllowedAsThirdParty
+ __CFHTTPAuthenticationGetPATAuthHeaders
+ __CFHTTPAuthenticationGetPATSchemes
+ _nw_connection_force_cancel
+ _objc_retain_x6
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
CStrings:
+ "%{public}@ PAT parsing token key failed %@"
+ "%{public}@ authenticator finished cont %d headers %{sensitive}@"
+ "%{public}@ authenticator finished cont %d req %{sensitive}@ headers %{sensitive}@"
+ "%{public}@ extractor finished successfully, discarding previous error [%ld]"
+ "B32@0:8@16^B24"
+ "T@\"NSString\",?,R,C"
+ "_extractorFinishedSuccessfully"
+ "_onqueue_handleConnectionsAtAPSleep"
+ "_setSchemeWasUpgradedDueToDynamicHSTS:"
+ "nw_connection_force_cancel connection=%llu"
+ "shouldPromoteHostToHTTPS:isPreload:"
- "%{public}@ authenticator finished cont %d headers %@"
- "%{public}@ authenticator finished cont %d req %@ headers %@"
- "TB,V_inPrivateBrowsing"
- "_onqueue_logConnectionsAtAPSleep"
- "set_inPrivateBrowsing:"

```
