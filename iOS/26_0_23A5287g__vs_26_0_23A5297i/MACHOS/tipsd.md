## tipsd

> `/usr/libexec/tipsd`

```diff

-816.0.0.0.0
-  __TEXT.__text: 0x125f8
+818.0.0.0.0
+  __TEXT.__text: 0x12d98
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_stubs: 0x2360
-  __TEXT.__objc_methlist: 0xb90
-  __TEXT.__const: 0x242
-  __TEXT.__cstring: 0xce9
-  __TEXT.__objc_methname: 0x2fae
-  __TEXT.__oslogstring: 0x1022
-  __TEXT.__objc_classname: 0x1ac
+  __TEXT.__objc_stubs: 0x2400
+  __TEXT.__objc_methlist: 0xbe8
+  __TEXT.__const: 0x24a
+  __TEXT.__cstring: 0xd79
+  __TEXT.__objc_methname: 0x314e
+  __TEXT.__oslogstring: 0x108a
+  __TEXT.__objc_classname: 0x1ad
   __TEXT.__objc_methtype: 0xdae
-  __TEXT.__gcc_except_tab: 0x208
+  __TEXT.__gcc_except_tab: 0x230
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x1e5
   __TEXT.__swift5_capture: 0x17c

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__unwind_info: 0x4d8
   __TEXT.__eh_frame: 0x5d8
   __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x3a0
+  __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__auth_ptr: 0xd8
   __DATA_CONST.__const: 0x9e8
-  __DATA_CONST.__cfstring: 0x7e0
+  __DATA_CONST.__cfstring: 0x820
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0xb20
-  __DATA.__objc_selrefs: 0xc28
-  __DATA.__objc_ivar: 0x5c
+  __DATA.__objc_const: 0xb80
+  __DATA.__objc_selrefs: 0xc68
+  __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x640
-  __DATA.__common: 0x18
+  __DATA.__common: 0x20
   __DATA.__bss: 0x200
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F96F8481-C24D-3EE9-8981-676524B54F74
-  Functions: 366
-  Symbols:   362
-  CStrings:  821
+  UUID: 161F58DF-6B34-3C5A-AC16-5707DDAACD2D
+  Functions: 377
+  Symbols:   364
+  CStrings:  840
 
Symbols:
+ _TPSAnalyticsDaemonActiveReasonSupportFlowConnection
+ _TPSTipKitProcessedDate
CStrings:
+ "New connection coming in: %@, standardAccess %d, appAccess %d, device expert access %d, support flow access %d"
+ "Support Flow connection established. %@"
+ "Support Flow xpc connection invalidated"
+ "T@\"NSMutableSet\",&,N,V_supportFlowConnections"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_supportFlowConnectionQueue"
+ "_addSupportFlowXPCConnection:"
+ "_removeSupportFlowXPCConnection:"
+ "_supportFlowConnectionQueue"
+ "_supportFlowConnections"
+ "_supportFlowXPCConnectionContainsConnection:"
+ "com.apple.private.tipsd.supportFlowApp"
+ "com.apple.tipsd.supportFlow.analytics"
+ "com.apple.tipsd.supportFlowConnectionQueue"
+ "setSupportFlowConnectionQueue:"
+ "setSupportFlowConnections:"
+ "supportFlowConnectionQueue"
+ "supportFlowConnections"
+ "supportFlowSessionAnalyticsInterface"
- "New connection coming in: %@, standardAccess %d, appAccess %d, device expert access %d"

```
