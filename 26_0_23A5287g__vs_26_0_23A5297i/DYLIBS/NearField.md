## NearField

> `/System/Library/PrivateFrameworks/NearField.framework/NearField`

```diff

-360.37.0.0.0
-  __TEXT.__text: 0xb703c
+360.38.0.0.0
+  __TEXT.__text: 0xb7e78
   __TEXT.__auth_stubs: 0x840
   __TEXT.__delay_helper: 0x354
-  __TEXT.__objc_methlist: 0x725c
+  __TEXT.__objc_methlist: 0x7294
   __TEXT.__const: 0x2a7
-  __TEXT.__cstring: 0x6f3d
-  __TEXT.__oslogstring: 0x5a80
-  __TEXT.__unwind_info: 0x1ce8
+  __TEXT.__cstring: 0x719e
+  __TEXT.__oslogstring: 0x5c71
+  __TEXT.__unwind_info: 0x1cf8
   __TEXT.__objc_classname: 0x11a3
-  __TEXT.__objc_methname: 0xe13d
-  __TEXT.__objc_methtype: 0x3d70
-  __TEXT.__objc_stubs: 0x82e0
+  __TEXT.__objc_methname: 0xe21c
+  __TEXT.__objc_methtype: 0x3db9
+  __TEXT.__objc_stubs: 0x8360
   __DATA_CONST.__got: 0x548
-  __DATA_CONST.__const: 0x29f0
+  __DATA_CONST.__const: 0x2a60
   __DATA_CONST.__objc_classlist: 0x3b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3400
+  __DATA_CONST.__objc_selrefs: 0x3428
   __DATA_CONST.__objc_protorefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x210
   __AUTH_CONST.__auth_got: 0x428
-  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__cfstring: 0x4100
-  __AUTH_CONST.__objc_const: 0xc2d0
+  __AUTH_CONST.__objc_const: 0xc318
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH.__objc_data: 0xff0
-  __DATA.__objc_ivar: 0x560
+  __DATA.__objc_ivar: 0x568
   __DATA.__data: 0x1e14
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_ivar: 0x1a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8FCE6C7D-530A-3C74-BC32-EB620E30120A
-  Functions: 2750
+  UUID: E344B354-EB71-312F-9EA7-71B6B455085D
+  Functions: 2759
   Symbols:   471
-  CStrings:  4902
+  CStrings:  4925
 
CStrings:
+ "%c[%{public}s %{public}s]:%i Calling %lu waiting clients"
+ "%c[%{public}s %{public}s]:%i Clearing XPC Connection"
+ "%c[%{public}s %{public}s]:%i Connection ID doesn't match (%lu vs %lu), may have already refreshed. Ignoring"
+ "%c[%{public}s %{public}s]:%i Stale update received from %d -> %d. Ignoring"
+ "%c[%{public}s %{public}s]:%i Unexpected connectionID (%lu vs %lu); dropping request"
+ "%s:%i ConnectionID does not match active (%lu), may have already been cleared"
+ "%{public}s:%i ConnectionID does not match active (%lu), may have already been cleared"
+ "+[NFHardwareManager _getSharedInstanceForType:]"
+ "-[NFHardwareManager connectToXPCManager:completionShouldExecuteOnCBQueue:withCompletion:]"
+ "@32@0:8B16B20@?24"
+ "Client queued, hwSupport=%u"
+ "NFHardwareManager.m"
+ "Vv36@0:8@\"NSArray\"16I24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "_connectionWasReset"
+ "_getSharedInstanceForType:"
+ "_hwSupportUpdateTime"
+ "_setActiveApplets:withCardType:"
+ "_setActiveApplets:withCardType:error:"
+ "_sync_processHwStateUpdate:atMachTime:"
+ "connectToXPCManager:completionShouldExecuteOnCBQueue:withCompletion:"
+ "hwSupport=Supported, executeOnCBQueue=%d"
+ "managerType < NFHardwareManagerTypeCount"
+ "nil != _xpc"
+ "resetConnection"
+ "resetConnectionWithId:"
+ "setActiveApplets:withTechnology:error:"
+ "setActiveAppletsForTest:withCardType:completion:"
+ "v28@0:8I16Q20"
- "-[NFXPCServiceClient getConnectionAndID:]_block_invoke_2"
- "B24@0:8@?16"
- "Not ready"
- "_isHWReadyAndIfNotQueueClient:"
- "_sharedHardwareManagerWaitOnHWInit:"
- "_sharedHardwareManagerWithNoUIWaitOnHWInit:"
- "client queued"
- "hw supported"
- "ready completion"
- "ready completion CB"

```
