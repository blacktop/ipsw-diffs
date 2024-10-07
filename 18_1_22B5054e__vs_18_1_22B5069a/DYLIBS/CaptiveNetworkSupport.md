## CaptiveNetworkSupport

> `/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport`

```diff

-480.40.3.0.0
-  __TEXT.__text: 0x2b758
-  __TEXT.__auth_stubs: 0x1450
+480.40.4.0.0
+  __TEXT.__text: 0x2bc48
+  __TEXT.__auth_stubs: 0x14b0
   __TEXT.__objc_methlist: 0xbc
   __TEXT.__const: 0x1e0
   __TEXT.__gcc_except_tab: 0x17c
-  __TEXT.__oslogstring: 0x4873
-  __TEXT.__cstring: 0x1c68
-  __TEXT.__unwind_info: 0x878
+  __TEXT.__oslogstring: 0x4941
+  __TEXT.__cstring: 0x1cc9
+  __TEXT.__unwind_info: 0x880
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methname: 0x97f
   __TEXT.__objc_methtype: 0x56e

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xa38
+  __AUTH_CONST.__auth_got: 0xa68
   __AUTH_CONST.__const: 0x6e0
-  __AUTH_CONST.__cfstring: 0x1e80
+  __AUTH_CONST.__cfstring: 0x1ea0
   __AUTH_CONST.__objc_const: 0x868
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0x2b9

   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x70
-  __DATA_DIRTY.__bss: 0x258
+  __DATA_DIRTY.__bss: 0x260
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 683
-  Symbols:   1124
-  CStrings:  1148
+  Functions: 686
+  Symbols:   1133
+  CStrings:  1157
 
Symbols:
+ _SCDynamicStoreCreate
+ _SCDynamicStoreCreateRunLoopSource
+ _SCDynamicStoreSetNotificationKeys
+ _SCNetworkInterfaceAdvisoryIsSpecificSet
+ _SCNetworkInterfaceCopyAdvisoryNotificationKey
+ __SCNetworkInterfaceCreateWithBSDName
CStrings:
+ "%!s(MISSING): %!@(MISSING) already registered, ignoring %!@(MISSING)"
+ "%!s(MISSING): SCDynamicStoreCreate() failed, %!s(MISSING)"
+ "%!s(MISSING): SCDynamicStoreSetNotificationKeys failed"
+ "%!s(MISSING): Wi-Fi %!@(MISSING) is %!s(MISSING)suppressed"
+ "%!s(MISSING): _SCNetworkInterfaceCreateWithBSDName(%!@(MISSING)) failed %!s(MISSING)"
+ "CaptiveNetworkSupport-480.40.4"
+ "UIAllowed"
+ "UIAllowedNewInterface"
+ "UIAllowedRegisterForAdvisoryChanges"
+ "UIAllowedWiFiSuppressedCheck"
- "CaptiveNetworkSupport-480.40.3"

```
