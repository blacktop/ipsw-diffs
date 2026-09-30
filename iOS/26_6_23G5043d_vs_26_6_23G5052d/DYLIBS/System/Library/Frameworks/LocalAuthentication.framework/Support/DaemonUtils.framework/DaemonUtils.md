## DaemonUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils`

```diff

-  __TEXT.__text: 0xb70c
+  __TEXT.__text: 0xb848
   __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0x1518
-  __TEXT.__const: 0x168
+  __TEXT.__objc_methlist: 0x1528
+  __TEXT.__const: 0x170
   __TEXT.__cstring: 0x6fd
-  __TEXT.__oslogstring: 0xab6
-  __TEXT.__gcc_except_tab: 0x150
+  __TEXT.__oslogstring: 0xaee
+  __TEXT.__gcc_except_tab: 0x158
   __TEXT.__unwind_info: 0x4d8
   __TEXT.__objc_classname: 0x2e4
-  __TEXT.__objc_methname: 0x2c67
-  __TEXT.__objc_methtype: 0x864
-  __TEXT.__objc_stubs: 0x23e0
+  __TEXT.__objc_methname: 0x2ca2
+  __TEXT.__objc_methtype: 0x893
+  __TEXT.__objc_stubs: 0x2420
   __DATA_CONST.__got: 0x280
   __DATA_CONST.__const: 0x240
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc10
+  __DATA_CONST.__objc_selrefs: 0xc20
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x298
   __AUTH_CONST.__const: 0x2e0
   __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__objc_const: 0x34b8
+  __AUTH_CONST.__objc_const: 0x34d8
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x188
+  __DATA.__objc_ivar: 0x18c
   __DATA.__data: 0x420
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x5f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 423
-  Symbols:   1714
-  CStrings:  912
+  Functions: 424
+  Symbols:   1719
+  CStrings:  918
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __TEXT.__objc_classname : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[LAAnalyticsDTO _skipRetryInterval]
+ -[LAAnalyticsDTO initForStatusMonitoringWithEnvironment:device:workQueue:]
+ _OBJC_IVAR_$_LAAnalyticsDTO._device
+ ___74-[LAAnalyticsDTO initForStatusMonitoringWithEnvironment:device:workQueue:]_block_invoke
+ _objc_msgSend$_skipRetryInterval
+ _objc_msgSend$hasBeenUnlockedSinceBoot
- -[LAAnalyticsDTO initForStatusMonitoringWithEnvironment:workQueue:]
- ___67-[LAAnalyticsDTO initForStatusMonitoringWithEnvironment:workQueue:]_block_invoke
CStrings:
+ "@\"<LACDTODeviceInfoProvider>\""
+ "@40@0:8@16@24@32"
+ "Skipping status check (%{public}@): setup=%d, unlock=%d"
+ "_device"
+ "_skipRetryInterval"
+ "hasBeenUnlockedSinceBoot"
+ "initForStatusMonitoringWithEnvironment:device:workQueue:"
- "a"
- "initForStatusMonitoringWithEnvironment:workQueue:"

```
